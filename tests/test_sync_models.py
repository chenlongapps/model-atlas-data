from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import tomllib
import unittest
from unittest.mock import patch

from scripts.sync_models import (ROOT, benchmark_bytes, check_staged, main,
                                sync_models, update_content, validate_model)


MODEL = b'''# Keep upstream comments and formatting.
schema = 2
name = "Example"
description = "Example model"
open_weights = false
release_date = "2026-10-01"

[modalities]
input = ["text"]
output = ["text"]

[capabilities]
tools = { supported = false }
reasoning = { supported = true }
temperature = true
top_p = true
top_k = false

[limit]
context = 128_000
output = 8_192
'''
RESULT = {"name": "Example Bench", "score": 42.10, "metric": "accuracy",
          "version": "1.0", "source": "https://example.com/results"}
DEFINITION = {"id": "example-bench-v1", "name": "Example Bench", "version": "1.0", "metric": "accuracy"}
LOCAL_RESULTS = b'''
# Locally verified evaluation conditions; retain this comment.
[[benchmarks]] # Keep result formatting too.
name = "Local Bench"
score = 42.10
effort = "Adaptive/Max"
variant = "without tools"
cost = 3.6589264906126227
cost_unit = "USD/weighted task"
cost_source = "https://example.com/costs"
# No definition or score source: existing records must not be revalidated by sync.
'''


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "local"
        self.upstream = self.base / "upstream"
        self.root.mkdir()
        (self.upstream / "models").mkdir(parents=True)
        license_text = (ROOT / "LICENSE.models-dev").read_bytes()
        self.write(self.root, "LICENSE.models-dev", license_text)
        self.write(self.upstream, "LICENSE", license_text)

    def write(self, root, path, content=MODEL):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        return target

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.root), *args], stderr=subprocess.STDOUT)

    def init_git(self):
        self.git("init", "--initial-branch=main")
        self.git("config", "user.name", "Test")
        self.git("config", "user.email", "test@example.com")
        self.git("add", ".")
        self.git("commit", "-m", "Initial files")

    def upstream_git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.upstream), *args], stderr=subprocess.STDOUT)

    def test_adds_only_models_and_preserves_bytes(self):
        self.write(self.upstream, "models/lab/New-Model.toml")
        self.write(self.upstream, "providers/provider/models/offering.toml")
        self.write(self.upstream, "i18n/zh-CN.toml", b"invalid = [")

        report = sync_models(self.upstream, self.root)

        self.assertEqual(list(report["added"]), ["models/lab/New-Model.toml"])
        self.assertEqual((self.root / "models/lab/New-Model.toml").read_bytes(), MODEL)
        self.assertFalse((self.root / "providers").exists())
        self.assertFalse((self.root / "i18n").exists())
        self.assertEqual(report["skipped"], {})

    def test_invalid_existing_candidates_are_reported_without_modification(self):
        local = b"# Locally verified benchmarks and comments\nlocal = true\n"
        target = self.write(self.root, "models/lab/existing.toml", local)
        self.write(self.upstream, "models/lab/existing.toml", b"invalid = [")
        before = target.stat().st_mtime_ns

        report = sync_models(self.upstream, self.root)

        self.assertEqual(report["existing"], 1)
        self.assertEqual(report["added"], {})
        self.assertEqual(report["updated"], {})
        self.assertIn("models/lab/existing.toml", report["skipped"])
        self.assertEqual(target.read_bytes(), local)
        self.assertEqual(target.stat().st_mtime_ns, before)

    def test_updates_existing_information_but_preserves_local_results_verbatim(self):
        local = MODEL + LOCAL_RESULTS
        target = self.write(self.root, "models/lab/existing.toml", local)
        incoming = MODEL.replace(b'context = 128_000', b'context = 256_000')
        incoming = incoming.replace(b'name = "Example"', b'name = "Example Updated"')
        self.write(self.upstream, "models/lab/existing.toml", incoming + b'\n[[benchmarks]]\nscore = true\n')

        report = sync_models(self.upstream, self.root)

        self.assertEqual(report["added"], {})
        self.assertEqual(report["skipped"], {})
        self.assertEqual(report["conflicts"], {})
        self.assertEqual(tomllib.loads(target.read_text()), tomllib.loads((incoming + LOCAL_RESULTS).decode()))
        self.assertIn(LOCAL_RESULTS, target.read_bytes())
        update = report["updated"]["models/lab/existing.toml"]
        self.assertEqual(set(update["fields"]), {"name", "limit.context"})
        self.assertEqual(update["before"], hashlib.sha256(local).hexdigest())
        self.assertEqual(update["after"], hashlib.sha256(target.read_bytes()).hexdigest())

    def test_existing_model_without_benchmarks_never_imports_upstream_results(self):
        target = self.write(self.root, "models/lab/existing.toml")
        incoming = MODEL.replace(b'output = 8_192', b'output = 16_384')
        self.write(self.upstream, "models/lab/existing.toml", incoming + LOCAL_RESULTS)

        report = sync_models(self.upstream, self.root)

        self.assertEqual(tomllib.loads(target.read_text()), tomllib.loads(incoming.decode()))
        self.assertNotIn("benchmarks", tomllib.loads(target.read_text()))
        self.assertEqual(len(report["updated"]), 1)

    def test_benchmark_only_changes_are_a_no_op_and_keep_mtime(self):
        target = self.write(self.root, "models/lab/existing.toml", MODEL + LOCAL_RESULTS)
        before = target.stat().st_mtime_ns
        self.write(self.upstream, "models/lab/existing.toml", b'benchmarks = "Ignored"\n' + MODEL)

        report = sync_models(self.upstream, self.root)
        self.assertEqual(report["updated"], {})
        self.assertEqual(report["skipped"], {})
        self.assertEqual(target.read_bytes(), MODEL + LOCAL_RESULTS)
        self.assertEqual(target.stat().st_mtime_ns, before)

    def test_upstream_values_replace_stale_local_values_but_keep_missing_fields(self):
        local = MODEL.replace(b'context = 128_000', b'context = 512_000')
        local = local.replace(b'[limit]', b'[limit]\ninput = 100_000')
        target = self.write(self.root, "models/lab/existing.toml", local + LOCAL_RESULTS)
        incoming = MODEL.replace(b'context = 128_000', b'context = 256_000')
        incoming = incoming.replace(b'output = 8_192', b'output = 16_384')
        self.write(self.upstream, "models/lab/existing.toml", incoming)

        report = sync_models(self.upstream, self.root)

        expected = local.replace(b'context = 512_000', b'context = 256_000')
        expected = expected.replace(b'output = 8_192', b'output = 16_384') + LOCAL_RESULTS
        self.assertEqual(tomllib.loads(target.read_text()), tomllib.loads(expected.decode()))
        self.assertEqual(tomllib.loads(target.read_text())["limit"]["input"], 100_000)
        self.assertIn(LOCAL_RESULTS, target.read_bytes())
        self.assertEqual(report["conflicts"], {})
        self.assertEqual(set(report["updated"]["models/lab/existing.toml"]["fields"]),
                         {"limit.context", "limit.output"})

    def test_adds_missing_fields_and_updates_existing_values_without_history(self):
        local = MODEL + LOCAL_RESULTS
        target = self.write(self.root, "models/lab/existing.toml", local)
        incoming = MODEL.replace(b'[limit]', b'[limit]\ninput = 100_000')
        incoming = incoming.replace(b'context = 128_000', b'context = 256_000')
        self.write(self.upstream, "models/lab/existing.toml", incoming)

        report = sync_models(self.upstream, self.root)

        data = tomllib.loads(target.read_text())
        self.assertEqual(data["limit"]["input"], 100_000)
        self.assertEqual(data["limit"]["context"], 256_000)
        self.assertIn(LOCAL_RESULTS, target.read_bytes())
        self.assertEqual(report["conflicts"], {})
        self.assertFalse((self.upstream / ".git").exists())

    def test_translated_description_is_protected_while_other_fields_update(self):
        target = self.write(self.root, "models/lab/existing.toml", MODEL + LOCAL_RESULTS)
        translations = b'[model.descriptions]\n"lab/existing" = "Translated description"\n'
        locale = self.write(self.root, "i18n/zh-CN.toml", translations)
        incoming = MODEL.replace(b'"Example model"', b'"Updated description"')
        incoming = incoming.replace(b'output = 8_192', b'output = 16_384')
        self.write(self.upstream, "models/lab/existing.toml", incoming)

        report = sync_models(self.upstream, self.root)

        expected = (MODEL + LOCAL_RESULTS).replace(b'output = 8_192', b'output = 16_384')
        self.assertEqual(tomllib.loads(target.read_text()), tomllib.loads(expected.decode()))
        self.assertIn(LOCAL_RESULTS, target.read_bytes())
        self.assertIn("translations", report["conflicts"]["models/lab/existing.toml"]["description"])
        self.assertEqual(locale.read_bytes(), translations)

    def test_dry_run_updates_have_same_hashes_without_writing(self):
        target = self.write(self.root, "models/lab/existing.toml", MODEL + LOCAL_RESULTS)
        before = target.stat().st_mtime_ns
        self.write(self.upstream, "models/lab/existing.toml", MODEL.replace(b'output = 8_192', b'output = 16_384'))

        preview = sync_models(self.upstream, self.root, dry_run=True)

        self.assertEqual(target.read_bytes(), MODEL + LOCAL_RESULTS)
        self.assertEqual(target.stat().st_mtime_ns, before)
        report = sync_models(self.upstream, self.root)
        self.assertEqual(preview["updated"], report["updated"])
        repeated = sync_models(self.upstream, self.root)
        self.assertEqual(repeated["updated"], {})

    def test_minimax_open_weights_catches_up_when_both_upstream_versions_are_true(self):
        path = "models/minimax/MiniMax-M3.1-Flash.toml"
        local = MODEL.replace(b'name = "Example"', b'name = "MiniMax-M3.1-Flash"') + LOCAL_RESULTS
        incoming = local.replace(b'open_weights = false', b'open_weights = true')
        target = self.write(self.root, path, local)
        self.init_git()
        self.write(self.upstream, path, incoming)
        self.upstream_git("init", "--initial-branch=dev")
        self.upstream_git("config", "user.name", "Test")
        self.upstream_git("config", "user.email", "test@example.com")
        self.upstream_git("add", ".")
        self.upstream_git("commit", "-m", "Previous upstream already published weights")
        old_sha = self.upstream_git("rev-parse", "HEAD").decode().strip()
        self.git("commit", "--allow-empty", "-m", "chore: sync new Models.dev models", "-m",
                 f"Source: https://github.com/anomalyco/models.dev/tree/{old_sha}/models")
        self.upstream_git("commit", "--allow-empty", "-m", "Current upstream still has open weights")

        report = sync_models(self.upstream, self.root)

        self.assertTrue(tomllib.loads(target.read_text())["open_weights"])
        self.assertTrue(tomllib.loads(self.upstream_git("show", f"{old_sha}:{path}").decode())["open_weights"])
        self.assertEqual(report["updated"][path]["fields"], ["open_weights"])
        self.assertEqual(report["conflicts"], {})
        self.assertEqual(benchmark_bytes(target.read_bytes()), benchmark_bytes(local))
        self.assertIn(LOCAL_RESULTS, target.read_bytes())
        self.git("add", "models/")
        check_staged(self.root, report)

    def test_existing_update_does_not_overwrite_a_racing_local_change(self):
        target = self.write(self.root, "models/lab/existing.toml", MODEL + LOCAL_RESULTS)
        self.write(self.upstream, "models/lab/existing.toml", MODEL.replace(b'output = 8_192', b'output = 16_384'))
        original_open = Path.open

        def race(path, mode="r", *args, **kwargs):
            if path == target and mode == "r+b":
                with original_open(path, "wb") as stream:
                    stream.write(b"racing local changes")
            return original_open(path, mode, *args, **kwargs)

        with patch.object(Path, "open", race), self.assertRaisesRegex(ValueError, "changed during sync"):
            sync_models(self.upstream, self.root)
        self.assertEqual(target.read_bytes(), b"racing local changes")

    def test_upstream_deletion_and_rename_keep_local_files(self):
        self.write(self.root, "models/lab/deleted.toml", b"# local deleted upstream\n")
        self.write(self.root, "models/lab/old-name.toml", b"# old canonical ID\n")
        self.write(self.upstream, "models/lab/new-name.toml")

        sync_models(self.upstream, self.root)

        self.assertEqual((self.root / "models/lab/deleted.toml").read_bytes(), b"# local deleted upstream\n")
        self.assertEqual((self.root / "models/lab/old-name.toml").read_bytes(), b"# old canonical ID\n")
        self.assertTrue((self.root / "models/lab/new-name.toml").exists())

    def test_repeated_run_is_a_no_op(self):
        self.write(self.upstream, "models/lab/new.toml")
        sync_models(self.upstream, self.root)
        report = sync_models(self.upstream, self.root)
        self.assertEqual(report["added"], {})
        self.assertEqual(report["existing"], 1)

    def test_dry_run_does_not_create_models(self):
        self.write(self.upstream, "models/lab/new.toml")
        report = sync_models(self.upstream, self.root, dry_run=True)
        self.assertEqual(len(report["added"]), 1)
        self.assertFalse((self.root / "models").exists())

    def test_invalid_candidates_are_reported_without_blocking_valid_ones(self):
        for name, content in {"syntax": b"invalid = [", "utf8": b'bad = "\xff"',
                              "schema": MODEL.replace(b"schema = 2", b"schema = 1"),
                              "provider": MODEL + b'\n[cost]\ninput = 1\n'}.items():
            self.write(self.upstream, f"models/lab/{name}.toml", content)
        self.write(self.upstream, "models/lab/nested/wrong.toml")
        self.write(self.upstream, "models/lab/valid.toml")

        report = sync_models(self.upstream, self.root)

        self.assertEqual(len(report["skipped"]), 5)
        self.assertEqual(list(report["added"]), ["models/lab/valid.toml"])

    def test_changed_license_stops_before_copy(self):
        self.write(self.upstream, "models/lab/new.toml")
        self.write(self.upstream, "LICENSE", b"Different license")
        with self.assertRaisesRegex(ValueError, "LICENSE changed"):
            sync_models(self.upstream, self.root)
        self.assertFalse((self.root / "models").exists())

    def test_symlinked_source_and_destination_are_rejected(self):
        outside = self.write(self.base, "outside/new.toml")
        (self.upstream / "models/lab").mkdir()
        (self.upstream / "models/lab/source.toml").symlink_to(outside)
        self.write(self.upstream, "models/linked/new.toml")
        (self.root / "models").mkdir()
        (self.root / "models/linked").symlink_to(outside.parent, target_is_directory=True)

        report = sync_models(self.upstream, self.root)

        self.assertEqual(len(report["skipped"]), 2)
        self.assertEqual(report["added"], {})
        self.assertEqual(outside.read_bytes(), MODEL)

    def test_exclusive_creation_does_not_overwrite_a_racing_file(self):
        self.write(self.upstream, "models/lab/new.toml")
        original_open = Path.open

        def race(path, mode="r", *args, **kwargs):
            if mode == "xb":
                with original_open(path, "wb") as stream:
                    stream.write(b"racing writer")
            return original_open(path, mode, *args, **kwargs)

        with patch.object(Path, "open", race), self.assertRaises(FileExistsError):
            sync_models(self.upstream, self.root)
        self.assertEqual((self.root / "models/lab/new.toml").read_bytes(), b"racing writer")

    def test_sync_skips_model_with_unmapped_benchmark(self):
        content = MODEL + b'\n[[benchmarks]]\nname = "Unknown"\nscore = 42\nsource = "https://example.com"\n'
        self.write(self.upstream, "models/lab/new.toml", content)
        report = sync_models(self.upstream, self.root)
        self.assertIn("mapping is missing", report["skipped"]["models/lab/new.toml"])
        self.assertEqual(report["added"], {})

    def test_sync_preserves_optional_effort_without_changing_source_bytes(self):
        definition = b'''id = "example-bench-v1"
name = "Example Bench"
version = "1.0"
metric = "accuracy"
'''
        self.write(self.root, "benchmarks/example.toml", definition)
        result = b'''
[[benchmarks]]
name = "Example Bench"
score = 42.10
version = "1.0"
metric = "accuracy"
variant = "without tools"
source = "https://example.com/results"
'''
        content = MODEL + result + result + b'effort = "Adaptive/Max"\n'
        content += b'cost = 3.6589264906126227\ncost_unit = "USD/weighted task"\n'
        content += b'cost_source = "https://example.com/costs"\n'
        self.write(self.upstream, "models/lab/new.toml", content)
        report = sync_models(self.upstream, self.root)
        self.assertEqual(report["skipped"], {})
        self.assertEqual(list(report["added"]), ["models/lab/new.toml"])
        self.assertEqual((self.root / "models/lab/new.toml").read_bytes(), content)

    def stage_new_model(self):
        self.init_git()
        self.write(self.upstream, "models/lab/new.toml")
        report = sync_models(self.upstream, self.root)
        self.git("add", "models/")
        return report

    def test_staged_guard_accepts_exact_additions(self):
        report = self.stage_new_model()
        check_staged(self.root, report)

    def test_staged_guard_rejects_modified_or_deleted_existing_files(self):
        self.write(self.root, "models/lab/existing.toml")
        report = self.stage_new_model()
        self.write(self.root, "models/lab/existing.toml", b"# changed\n")
        self.git("add", "models/")
        with self.assertRaisesRegex(ValueError, "unexpected staged"):
            check_staged(self.root, report)
        (self.root / "models/lab/existing.toml").unlink()
        self.git("add", "models/")
        with self.assertRaisesRegex(ValueError, "unsupported staged"):
            check_staged(self.root, report)

    def test_staged_guard_rejects_extra_files(self):
        report = self.stage_new_model()
        self.write(self.root, "extra.txt", b"extra")
        self.git("add", "extra.txt")
        with self.assertRaisesRegex(ValueError, "unsupported staged"):
            check_staged(self.root, report)

    def test_staged_guard_rejects_changed_content_or_missing_additions(self):
        report = self.stage_new_model()
        with self.assertRaisesRegex(ValueError, "do not match"):
            check_staged(self.root, {**report, "added": {**report["added"], "models/lab/missing.toml": "missing"}})
        self.write(self.root, "models/lab/new.toml", MODEL + b"# changed\n")
        self.git("add", "models/")
        with self.assertRaisesRegex(ValueError, "content changed"):
            check_staged(self.root, report)

    def test_staged_guard_rejects_unstaged_changes_and_dry_runs(self):
        report = self.stage_new_model()
        self.write(self.root, "LICENSE.models-dev", b"changed")
        with self.assertRaisesRegex(ValueError, "unstaged"):
            check_staged(self.root, report)
        with self.assertRaisesRegex(ValueError, "dry run"):
            check_staged(self.root, {**report, "dry_run": True})

    def test_staged_guard_rejects_symlink_even_with_correct_content_hash(self):
        report = self.stage_new_model()
        self.git("update-index", "--cacheinfo", "120000", self.git("rev-parse", ":models/lab/new.toml").decode().strip(),
                 "models/lab/new.toml")
        with self.assertRaisesRegex(ValueError, "file mode"):
            check_staged(self.root, report)

    def stage_information_update(self):
        self.write(self.root, "models/lab/existing.toml", MODEL + LOCAL_RESULTS)
        self.init_git()
        self.write(self.upstream, "models/lab/existing.toml", MODEL.replace(b'output = 8_192', b'output = 16_384'))
        report = sync_models(self.upstream, self.root)
        self.git("add", "models/")
        return report

    def test_staged_guard_accepts_information_updates_and_checks_before_hash(self):
        report = self.stage_information_update()
        check_staged(self.root, report)
        report["updated"]["models/lab/existing.toml"]["before"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "changed since comparison"):
            check_staged(self.root, report)

    def test_staged_guard_rejects_benchmark_edits_even_with_matching_after_hash(self):
        report = self.stage_information_update()
        target = self.root / "models/lab/existing.toml"
        for content in (target.read_bytes().replace(b"42.10", b"43.10"),
                        target.read_bytes().replace(b"42.10", b"42.1"),
                        target.read_bytes().replace(b"# Keep result formatting too.", b"# Changed comment.")):
            with self.subTest(content=content):
                target.write_bytes(content)
                self.git("add", "models/")
                report["updated"]["models/lab/existing.toml"]["after"] = hashlib.sha256(content).hexdigest()
                with self.assertRaisesRegex(ValueError, "benchmarks changed"):
                    check_staged(self.root, report)

    def test_staged_guard_rejects_missing_reported_update(self):
        report = self.stage_information_update()
        self.git("restore", "--staged", "models/lab/existing.toml")
        with self.assertRaisesRegex(ValueError, "do not match"):
            check_staged(self.root, report)

    def test_cli_writes_report_and_summary_and_checks_staged_changes(self):
        self.init_git()
        self.write(self.upstream, "models/lab/new.toml")
        subprocess.run(["git", "-C", str(self.upstream), "init"], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(self.upstream), "add", "."], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(self.upstream), "-c", "user.name=Test", "-c", "user.email=test@example.com",
                        "commit", "-m", "Upstream"], check=True, capture_output=True)
        report_path, summary_path = self.base / "report.json", self.base / "summary.md"
        with redirect_stdout(StringIO()):
            code = main(["--root", str(self.root), "sync", "--upstream", str(self.upstream),
                         "--report", str(report_path), "--summary", str(summary_path)])
        self.assertEqual(code, 0)
        report = json.loads(report_path.read_text())
        self.assertRegex(report["upstream_sha"], r"^[0-9a-f]{40}$")
        self.assertIn(report["upstream_sha"], summary_path.read_text())
        self.assertIn("follows explicit upstream values", summary_path.read_text())
        self.assertNotIn("Baseline:", summary_path.read_text())
        self.git("add", "models/")
        self.assertEqual(main(["--root", str(self.root), "check-staged", "--report", str(report_path)]), 0)

    def test_cli_failure_returns_nonzero(self):
        with redirect_stderr(StringIO()) as stderr:
            code = main(["--root", str(self.root), "check-staged", "--report", str(self.base / "missing.json")])
        self.assertEqual(code, 1)
        self.assertIn("Sync failed", stderr.getvalue())


class InformationUpdateTests(unittest.TestCase):
    def update(self, local, upstream):
        return update_content(local, tomllib.loads(upstream.decode()))

    def test_local_parameters_survive_upstream_metadata_and_information_updates(self):
        local = MODEL + LOCAL_RESULTS + b'''
[metadata.modelatlas.parameters]
total_billion = 0.35 # Keep reported precision and provenance.
sources = ["https://example.com/card"]
'''
        for extra in (b'', b'\n[metadata]\nupstream_note = "New"\n',
                      b'\n[metadata.modelatlas]\nfuture = true\n'):
            with self.subTest(extra=extra):
                upstream = MODEL.replace(b'output = 8_192', b'output = 16_384') + extra
                updated, fields, conflicts = self.update(local, upstream)
                before, after = (tomllib.loads(v.decode()) for v in (local, updated))
                self.assertEqual(after["metadata"]["modelatlas"]["parameters"],
                                 before["metadata"]["modelatlas"]["parameters"])
                self.assertIn(b'# Keep reported precision and provenance.', updated)
                self.assertEqual(benchmark_bytes(updated), benchmark_bytes(local))
                self.assertIn("limit.output", fields)
                self.assertEqual(conflicts, {})

    def test_invalid_parameter_metadata_is_rejected_during_sync(self):
        invalid = MODEL + b'\n[metadata.modelatlas.parameters]\ntotal_billion = true\n'
        with self.assertRaisesRegex(ValueError, "parameters.total_billion"):
            self.update(MODEL, invalid)

    def test_component_only_parameters_survive_sync_with_all_provenance(self):
        local = MODEL + LOCAL_RESULTS + b'''
[metadata.modelatlas.parameters]
notes = "Complete total is unknown."
[[metadata.modelatlas.parameters.components]]
name = "Transformer"
total_billion = 7
sources = ["https://example.com/transformer"] # Keep source.
'''
        upstream = MODEL.replace(b'output = 8_192', b'output = 16_384') + b'\n[metadata]\nupstream = true\n'
        updated, fields, conflicts = self.update(local, upstream)
        before, after = (tomllib.loads(v.decode()) for v in (local, updated))
        self.assertEqual(before["metadata"]["modelatlas"], after["metadata"]["modelatlas"])
        self.assertNotIn("total_billion", after["metadata"]["modelatlas"]["parameters"])
        self.assertIn(b'# Keep source.', updated)
        self.assertEqual(benchmark_bytes(local), benchmark_bytes(updated))
        self.assertEqual(conflicts, {})

    def test_boolean_values_follow_upstream_in_both_directions(self):
        for previous, incoming in ((b"false", b"true"), (b"true", b"false")):
            with self.subTest(previous=previous, incoming=incoming):
                local = MODEL.replace(b"open_weights = false", b"open_weights = " + previous) + LOCAL_RESULTS
                upstream = MODEL.replace(b"open_weights = false", b"open_weights = " + incoming)
                updated, fields, conflicts = self.update(local, upstream)
                self.assertEqual(tomllib.loads(updated.decode())["open_weights"], incoming == b"true")
                self.assertEqual(fields, ["open_weights"])
                self.assertEqual(conflicts, {})
                self.assertEqual(benchmark_bytes(updated), benchmark_bytes(local))

    def test_multiline_strings_and_interleaved_tables_preserve_benchmark_text(self):
        description = b'''description = """Description with header-like text:
[[benchmarks]]
[limit]
"""'''
        local = MODEL.replace(b'description = "Example model"', description)
        local += LOCAL_RESULTS + b'\n[metadata]\nnote = "Keep"\n' + LOCAL_RESULTS
        incoming = MODEL.replace(b'"Example model"', b'"Updated model description"')
        updated, fields, conflicts = self.update(local, incoming)
        expected = tomllib.loads(local.decode())
        expected["description"] = "Updated model description"
        self.assertEqual(tomllib.loads(updated.decode()), expected)
        self.assertEqual(benchmark_bytes(updated), benchmark_bytes(local))
        self.assertEqual(fields, ["description"])
        self.assertEqual(conflicts, {})

    def test_inline_results_remain_at_root_when_adding_new_fields(self):
        local = b'benchmarks = [{ name = "Local", score = 42.10 }] # Keep\n' + MODEL
        incoming = b'family = "Example family"\n' + MODEL
        updated, fields, conflicts = self.update(local, incoming)
        self.assertIn(b'benchmarks = [{ name = "Local", score = 42.10 }] # Keep\n', updated)
        self.assertEqual(tomllib.loads(updated.decode())["family"], "Example family")
        self.assertEqual(fields, ["family"])
        self.assertEqual(conflicts, {})

    def test_missing_local_fields_are_restored_but_upstream_omissions_are_retained(self):
        incoming = MODEL.replace(b'[limit]', b'[limit]\ninput = 100_000')
        incoming = incoming.replace(b'output = 8_192\n', b'')
        updated, fields, conflicts = self.update(MODEL, incoming)
        limits = tomllib.loads(updated.decode())["limit"]
        self.assertEqual(limits, {"context": 128_000, "input": 100_000, "output": 8_192})
        self.assertEqual(fields, ["limit.input"])
        self.assertEqual(conflicts, {})

    def test_unknown_upstream_basic_fields_are_rejected_not_silently_dropped(self):
        with self.assertRaisesRegex(ValueError, "unsupported fields"):
            self.update(MODEL, b'unknown = true\n' + MODEL)

    def test_updating_inline_tables_and_arrays_preserves_local_comments(self):
        local = MODEL.replace(b'tools = { supported = false }', b'tools = { supported = false } # Keep support note')
        local += b'\n[[links]]\nurl = "https://example.com/old" # Keep link note\n' + LOCAL_RESULTS
        incoming = local.replace(b'tools = { supported = false }', b'tools = { supported = true, strict = true }')
        incoming = incoming.replace(b'https://example.com/old', b'https://example.com/new')
        updated, fields, conflicts = self.update(local, incoming)
        self.assertIn(b'# Keep support note', updated)
        self.assertIn(b'# Keep link note', updated)
        self.assertIn(LOCAL_RESULTS, updated)
        self.assertEqual(tomllib.loads(updated.decode())["links"][0]["url"], "https://example.com/new")
        self.assertEqual(set(fields), {"capabilities.tools.supported", "capabilities.tools.strict", "links"})
        self.assertEqual(conflicts, {})

    def test_crlf_benchmarks_and_missing_final_newline_remain_verbatim(self):
        for newline in (b"\n", b"\r\n"):
            for final_newline in (True, False):
                with self.subTest(newline=newline, final_newline=final_newline):
                    local = (MODEL + LOCAL_RESULTS).replace(b"\n", newline)
                    if not final_newline:
                        local = local.rstrip(b"\r\n")
                    incoming = MODEL.replace(b'output = 8_192', b'output = 16_384')
                    updated, fields, conflicts = self.update(local, incoming)
                    self.assertEqual(benchmark_bytes(updated), benchmark_bytes(local))
                    self.assertTrue(updated.endswith(LOCAL_RESULTS.replace(b"\n", newline).rstrip(b"\r\n")
                                                    + (newline if final_newline else b"")))
                    self.assertEqual(fields, ["limit.output"])
                    self.assertEqual(conflicts, {})


class ModelValidationTests(unittest.TestCase):
    def setUp(self):
        self.data = tomllib.loads(MODEL.decode())

    def test_matches_explicit_benchmark_definition(self):
        self.data["benchmarks"] = [RESULT]
        validate_model(self.data, [DEFINITION])

    def test_matches_only_explicitly_declared_compatible_version(self):
        definition = {**DEFINITION, "version": "5.0", "compatible_versions": ["5.0.1"]}
        result = {**RESULT, "version": "5.0.1"}
        self.data["benchmarks"] = [result]
        validate_model(self.data, [definition])
        self.data["benchmarks"] = [{**result, "version": "5.0.2"}]
        with self.assertRaisesRegex(ValueError, "mapping"):
            validate_model(self.data, [definition])

    def test_does_not_guess_name_metric_or_version(self):
        for field in ("name", "version", "metric"):
            with self.subTest(field=field):
                result = {**RESULT, field: "different"}
                self.data["benchmarks"] = [result]
                with self.assertRaisesRegex(ValueError, "mapping"):
                    validate_model(self.data, [DEFINITION])
        for field in ("version", "metric"):
            result = {k: v for k, v in RESULT.items() if k != field}
            self.data["benchmarks"] = [result]
            with self.assertRaisesRegex(ValueError, "mapping"):
                validate_model(self.data, [DEFINITION])

    def test_rejects_ambiguous_definitions(self):
        self.data["benchmarks"] = [RESULT]
        with self.assertRaisesRegex(ValueError, "ambiguous"):
            validate_model(self.data, [DEFINITION, DEFINITION])

    def test_rejects_duplicate_and_conflicting_records_but_keeps_conditions(self):
        for score in (42.10, 43):
            self.data["benchmarks"] = [RESULT, {**RESULT, "score": score}]
            with self.assertRaisesRegex(ValueError, "duplicate or conflicting"):
                validate_model(self.data, [DEFINITION])
        self.data["benchmarks"] = [RESULT, {**RESULT, "variant": "with tools"}]
        validate_model(self.data, [DEFINITION])

    def test_optional_effort_preserves_official_names_and_legacy_records(self):
        legacy = {**RESULT, "variant": "xhigh effort; without tools"}
        efforts = ("xhigh", "XHigh", "Adaptive/Max", "Vendor Tier 7", "default")
        self.data["benchmarks"] = [legacy] + [
            {**RESULT, "effort": effort, "variant": "without tools"} for effort in efforts
        ]
        before = json.dumps(self.data, sort_keys=True)
        validate_model(self.data, [DEFINITION])
        self.assertEqual(json.dumps(self.data, sort_keys=True), before)
        self.assertNotIn("effort", legacy)

    def test_effort_must_be_a_nonempty_string(self):
        for value in (42, True, [], {}, None, "", "   "):
            with self.subTest(value=value):
                self.data["benchmarks"] = [{**RESULT, "effort": value}]
                with self.assertRaisesRegex(ValueError, r"benchmark\.effort:"):
                    validate_model(self.data, [DEFINITION])

    def test_effort_is_part_of_duplicate_and_conflict_identity(self):
        for effort in (None, "xhigh", "Adaptive/Max"):
            result = {**RESULT, **({"effort": effort} if effort is not None else {})}
            for score in (42.10, 43):
                with self.subTest(effort=effort, score=score):
                    self.data["benchmarks"] = [result, {**result, "score": score}]
                    with self.assertRaisesRegex(ValueError, "duplicate or conflicting"):
                        validate_model(self.data, [DEFINITION])
        self.data["benchmarks"] = [RESULT, {**RESULT, "effort": "default"}, {**RESULT, "effort": "xhigh"},
                                   {**RESULT, "effort": "xhigh", "variant": "with tools"}]
        validate_model(self.data, [DEFINITION])

    def test_required_fields_types_and_dates(self):
        for field, value in (("schema", True), ("name", ""), ("open_weights", 1),
                             ("release_date", "2026-02-30"), ("last_updated", "bad"),
                             ("limit", {"output": -1}), ("modalities", []),
                             ("capabilities", {"tools": {"supported": False}})):
            with self.subTest(field=field):
                data = {**self.data, field: value}
                with self.assertRaises(ValueError):
                    validate_model(data, [])

    def test_optional_cost_validation_and_preservation(self):
        for cost, unit in ((0, "USD/task"), (3.6589264906126227, "USD/weighted task"),
                           (4718.65, "USD/evaluation"), (18.70, "USD/test")):
            self.data["benchmarks"] = [{**RESULT, "cost": cost, "cost_unit": unit,
                                        "cost_source": "https://example.com/costs"}]
            before = json.dumps(self.data, sort_keys=True)
            validate_model(self.data, [DEFINITION])
            self.assertEqual(json.dumps(self.data, sort_keys=True), before)
        for changes in ({"cost": 1}, {"cost_unit": "USD/task"},
                        {"cost_source": "https://example.com/costs"},
                        *({"cost": cost, "cost_unit": "USD/task"}
                          for cost in (-1, True, "1.2", float("nan"), float("inf"), -float("inf"))),
                        {"cost": 1, "cost_unit": ""}, {"cost": 1, "cost_unit": 42},
                        {"cost": 1, "cost_unit": "USD/task", "cost_source": "file:///costs"}):
            with self.subTest(changes=changes):
                self.data["benchmarks"] = [{**RESULT, **changes}]
                with self.assertRaisesRegex(ValueError, r"benchmark\.cost"):
                    validate_model(self.data, [DEFINITION])

    def test_cost_metadata_cannot_hide_duplicate_or_conflicting_scores(self):
        for score in (42.10, 43):
            for first in (RESULT, {**RESULT, "cost": 1, "cost_unit": "USD/task"}):
                self.data["benchmarks"] = [first, {**RESULT, "score": score, "cost": 2,
                                                  "cost_unit": "USD/test",
                                                  "cost_source": "https://example.com/costs"}]
                with self.assertRaisesRegex(ValueError, "duplicate or conflicting"):
                    validate_model(self.data, [DEFINITION])

    def test_bad_benchmark_values_and_missing_source(self):
        for changes in ({"score": True}, {"score": float("nan")}, {"source": "not a URL"},
                        {"source": ""}, {"date": "2026-02-30"}, {"extra": "unknown"}):
            self.data["benchmarks"] = [{**RESULT, **changes}]
            with self.assertRaises(ValueError):
                validate_model(self.data, [DEFINITION])
        self.data["benchmarks"] = [{k: v for k, v in RESULT.items() if k != "source"}]
        with self.assertRaisesRegex(ValueError, "source required"):
            validate_model(self.data, [DEFINITION])

    def test_string_scores_are_preserved_per_upstream_schema(self):
        self.data["benchmarks"] = [{**RESULT, "score": "42.1 ± 0.2"}]
        validate_model(self.data, [DEFINITION])


if __name__ == "__main__":
    unittest.main()
