from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
import json
from pathlib import Path
import subprocess
import tempfile
import tomllib
import unittest
from unittest.mock import patch

from scripts.sync_models import ROOT, check_staged, main, sync_models, validate_model


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

    def test_existing_files_are_never_parsed_or_modified(self):
        local = b"# Locally verified benchmarks and comments\nlocal = true\n"
        target = self.write(self.root, "models/lab/existing.toml", local)
        self.write(self.upstream, "models/lab/existing.toml", b"invalid = [")
        before = target.stat().st_mtime_ns

        report = sync_models(self.upstream, self.root)

        self.assertEqual(report["existing"], 1)
        self.assertEqual(report["added"], {})
        self.assertEqual(target.read_bytes(), local)
        self.assertEqual(target.stat().st_mtime_ns, before)

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
        with self.assertRaisesRegex(ValueError, "non-additive"):
            check_staged(self.root, report)
        (self.root / "models/lab/existing.toml").unlink()
        self.git("add", "models/")
        with self.assertRaisesRegex(ValueError, "non-additive"):
            check_staged(self.root, report)

    def test_staged_guard_rejects_extra_files(self):
        report = self.stage_new_model()
        self.write(self.root, "extra.txt", b"extra")
        self.git("add", "extra.txt")
        with self.assertRaisesRegex(ValueError, "non-additive"):
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
        self.git("add", "models/")
        self.assertEqual(main(["--root", str(self.root), "check-staged", "--report", str(report_path)]), 0)

    def test_cli_failure_returns_nonzero(self):
        with redirect_stderr(StringIO()) as stderr:
            code = main(["--root", str(self.root), "check-staged", "--report", str(self.base / "missing.json")])
        self.assertEqual(code, 1)
        self.assertIn("Sync failed", stderr.getvalue())


class ModelValidationTests(unittest.TestCase):
    def setUp(self):
        self.data = tomllib.loads(MODEL.decode())

    def test_matches_explicit_benchmark_definition(self):
        self.data["benchmarks"] = [RESULT]
        validate_model(self.data, [DEFINITION])

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

    def test_required_fields_types_and_dates(self):
        for field, value in (("schema", True), ("name", ""), ("open_weights", 1),
                             ("release_date", "2026-02-30"), ("last_updated", "bad"),
                             ("limit", {"output": -1}), ("modalities", []),
                             ("capabilities", {"tools": {"supported": False}})):
            with self.subTest(field=field):
                data = {**self.data, field: value}
                with self.assertRaises(ValueError):
                    validate_model(data, [])

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
