"""Synthetic safety tests; the review integration is exercised separately."""

import copy
from contextlib import redirect_stderr, redirect_stdout
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import merge_candidate_staging as merge
from common import DataError


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value), encoding="utf-8")


def fixture_objects():
    benchmark = {"id": "bench", "name": "Bench", "version": "1", "description": "test", "category": "other", "officialUrl": "https://example.com", "metric": "accuracy", "unit": "%", "higherIsBetter": True, "minimum": 0, "maximum": 100, "status": "pending"}
    source = {"id": "source", "publisher": "Example", "url": "https://example.com", "retrievedAt": "2026-10-28", "publishedAt": None, "sourceType": "independent", "license": {"name": None, "url": None, "licenseFile": None, "redistribution": "pending", "attribution": "Example", "notes": "pending"}, "status": "pending"}
    mapping = {"id": "mapping", "sourceId": "source", "sourceModelName": "Model", "modelId": None, "evidenceUrl": None, "catalogUrl": None, "status": "pending", "notes": "unknown"}
    result = {"id": "candidate", "benchmarkId": "bench", "mappingId": "mapping", "score": 25, "sourceId": "source", "sourceLocator": "table", "collectedAt": "2026-10-28", "evaluatedAt": None, "subset": None, "harness": None, "reasoningEffort": None, "toolsEnabled": None, "status": "pending", "unrepresentedConditions": [], "notes": "test"}
    return {"benchmarks": [benchmark], "sources": [source], "mappings": [mapping], "results": [result]}


class MergeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        shutil.copytree(ROOT / "schemas", self.root / "schemas")
        for folder in ("data/results", "third_party", "benchmarks"):
            (self.root / folder).mkdir(parents=True)
        for rel in merge.SCRIPT_INPUTS:
            (self.root / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / rel, self.root / rel)
        write(self.root / "manifest.json", {})
        for key, name in merge.DOCUMENTS.items():
            write(self.root / "data" / name, {"schemaVersion": 1, key: []})
        self.objects = fixture_objects()
        for name in merge.STAGING:
            self.stage(name, {key: [] for key in self.objects})
        self.stage(merge.STAGING[0], self.objects)
        for i, name in enumerate(merge.EVIDENCE):
            targets = [{"id": merge.TARGETS[0], "benchmarkIds": ["bench"], "officialUrls": ["https://example.com"],
                        "status": "collected", "notes": "test", "searches": [{"tier": 1, "url": "https://example.com", "outcome": "test"}]}] if i == 0 else []
            write(self.root / merge.REVIEW / name, {"targets": targets, "evidence": [], "systemOnly": []})
        self.review = patch.object(merge, "review_candidates", return_value={})
        self.review.start()
        self.addCleanup(self.review.stop)

    def stage(self, name, obj):
        write(self.root / merge.REVIEW / name, obj)

    def read(self, rel):
        return json.loads((self.root / rel).read_text())

    def test_check_apply_and_idempotence(self):
        before = (self.root / "data/benchmarks.json").read_bytes()
        self.assertGreater(merge.run(self.root), 0)
        self.assertEqual(before, (self.root / "data/benchmarks.json").read_bytes())
        merge.run(self.root, True)
        batch = self.read(merge.REVIEW / "batch.json")
        self.assertEqual(batch["targetIds"], list(merge.TARGETS))
        self.assertEqual(batch["candidateResultIds"], ["candidate"])
        self.assertEqual(batch["evidenceFiles"], list(merge.EVIDENCE))
        self.assertEqual(merge.run(self.root, True), 0)
        self.assertTrue((self.root / merge.REVIEW / merge.STAGING[0]).exists())
        self.assertFalse((self.root / "data/release.json").exists())

    def test_existing_result_and_source_preserved(self):
        old = copy.deepcopy(self.objects["results"][0])
        old["id"] = "old"
        write(self.root / "data/results/bench.json", {"schemaVersion": 1, "results": [old]})
        merge.run(self.root, True)
        self.assertEqual(self.read("data/results/bench.json")["results"], [old, self.objects["results"][0]])

    def test_conflicts_and_pending_rejected_without_writes(self):
        for mutate in ("conflict", "approved", "unknown", "range", "batch"):
            with self.subTest(mutate=mutate):
                obj = copy.deepcopy(self.objects)
                if mutate == "conflict":
                    duplicate = copy.deepcopy(obj)
                    duplicate["sources"][0]["publisher"] = "Different"
                    self.stage(merge.STAGING[1], duplicate)
                elif mutate == "approved":
                    obj["sources"][0]["status"] = "approved"
                elif mutate == "unknown":
                    obj["results"][0]["mappingId"] = "unknown"
                elif mutate == "range":
                    obj["results"][0]["score"] = 101
                else:
                    write(self.root / merge.REVIEW / "batch.json", {"different": True})
                self.stage(merge.STAGING[0], obj)
                before = (self.root / "data/benchmarks.json").read_bytes()
                with self.assertRaises(DataError):
                    merge.run(self.root, True)
                self.assertEqual(before, (self.root / "data/benchmarks.json").read_bytes())
                self.stage(merge.STAGING[1], {key: [] for key in obj})
                (self.root / merge.REVIEW / "batch.json").unlink(missing_ok=True)

    def test_duplicate_objects_idempotent(self):
        self.stage(merge.STAGING[1], self.objects)
        evidence = self.read(merge.REVIEW / merge.EVIDENCE[0])
        write(self.root / merge.REVIEW / merge.EVIDENCE[1], evidence)
        merge.run(self.root, True)
        self.assertEqual(self.read(merge.REVIEW / "batch.json")["candidateResultIds"], ["candidate"])
        self.assertEqual(len(self.read("data/results/bench.json")["results"]), 1)

    def test_symlink_rejected(self):
        target = self.root / "data/results/bench.json"
        target.symlink_to(self.root / "manifest.json")
        with self.assertRaises(DataError):
            merge.run(self.root, True)
        self.assertEqual(self.read("manifest.json"), {})

    def test_existing_hardlink_is_not_truncated(self):
        target = self.root / "data/benchmarks.json"
        other = Path(self.temp.name) / "original-hardlink.json"
        os.link(target, other)
        before = other.read_bytes()
        merge.run(self.root, True)
        self.assertEqual(other.read_bytes(), before)
        self.assertNotEqual(target.read_bytes(), before)

    def test_review_failure_and_rollback(self):
        before = (self.root / "data/benchmarks.json").read_bytes()
        with patch.object(merge, "review_candidates", side_effect=DataError("bad evidence")):
            with self.assertRaises(DataError):
                merge.run(self.root, True)
        self.assertEqual(before, (self.root / "data/benchmarks.json").read_bytes())
        original = merge.os.replace
        calls = 0

        def fail_once(src, dst):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("simulated failure")
            return original(src, dst)

        with patch.object(merge.os, "replace", side_effect=fail_once):
            with self.assertRaises(OSError):
                merge.run(self.root, True)
        self.assertEqual(before, (self.root / "data/benchmarks.json").read_bytes())
        self.assertFalse((self.root / merge.REVIEW / "batch.json").exists())

    def test_link_success_then_temp_unlink_failure_rolls_back_all_targets(self):
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        original = Path.unlink
        failed = False

        def fail_once(path, *args, **kwargs):
            nonlocal failed
            if not failed and path.name.startswith(".candidate-merge-"):
                failed = True
                raise OSError("simulated unlink after link")
            return original(path, *args, **kwargs)

        with patch.object(Path, "unlink", fail_once):
            with self.assertRaisesRegex(OSError, "simulated unlink after link"):
                merge.run(self.root, True)
        self.assertTrue(failed)
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(after, before)

    def test_scope_closure_rejects_unrelated_objects(self):
        for key in ("benchmarks", "sources", "mappings"):
            with self.subTest(key=key):
                obj = copy.deepcopy(self.objects)
                extra = copy.deepcopy(obj[key][0])
                extra["id"] = "unrelated"
                obj[key].append(extra)
                self.stage(merge.STAGING[0], obj)
                with self.assertRaisesRegex(DataError, f"unrelated {key} id"):
                    merge.run(self.root, True)
                self.assertFalse((self.root / "data/results/bench.json").exists())

    def test_scope_source_evidence_and_system_reference(self):
        obj = copy.deepcopy(self.objects)
        source = copy.deepcopy(obj["sources"][0])
        source["id"] = "system-source"
        obj["sources"].append(source)
        self.stage(merge.STAGING[0], obj)
        path = self.root / merge.REVIEW / merge.EVIDENCE[0]
        evidence = self.read(merge.REVIEW / merge.EVIDENCE[0])
        evidence["systemOnly"] = [{"id": "system", "url": "https://example.com", "sourceModelName": "system", "reason": "multiple models"}]
        write(path, evidence)
        with self.assertRaisesRegex(DataError, "unrelated sources id: system-source"):
            merge.run(self.root)
        evidence["systemOnly"][0]["sourceId"] = "system-source"
        write(path, evidence)
        self.assertGreater(merge.run(self.root), 0)
        evidence["systemOnly"][0]["sourceId"] = "missing"
        obj["sources"].pop()
        self.stage(merge.STAGING[0], obj)
        write(path, evidence)
        with self.assertRaisesRegex(DataError, "unknown referenced sources"):
            merge.run(self.root)

    def test_evidence_only_source_is_in_closure(self):
        obj = copy.deepcopy(self.objects)
        extra = copy.deepcopy(obj["sources"][0])
        extra["id"] = "evidence-source"
        obj["sources"].append(extra)
        self.stage(merge.STAGING[0], obj)
        evidence = self.read(merge.REVIEW / merge.EVIDENCE[0])
        evidence["evidence"] = [{"id": "ev", "sourceId": "evidence-source", "url": "https://example.com", "retrievedAt": "2026-10-28T00:00:00Z", "responseSha256": None, "locator": "table", "excerpt": "test", "notes": "test"}]
        write(self.root / merge.REVIEW / merge.EVIDENCE[0], evidence)
        self.assertGreater(merge.run(self.root), 0)

    def test_scope_is_per_staging_and_target(self):
        self.stage(merge.STAGING[1], self.objects)
        with self.assertRaisesRegex(DataError, "outside evidence targets"):
            merge.run(self.root)
        evidence = self.read(merge.REVIEW / merge.EVIDENCE[0])
        evidence["targets"][0]["id"] = "not-an-approved-target"
        write(self.root / merge.REVIEW / merge.EVIDENCE[0], evidence)
        with self.assertRaisesRegex(DataError, "unrelated target"):
            merge.run(self.root)

    def test_checkpoint_cli_requires_matching_complete_input_snapshot(self):
        def cli(args):
            out, err = io.StringIO(), io.StringIO()
            with patch.object(merge, "ROOT", self.root), patch.object(sys, "argv", ["merge"] + args), redirect_stdout(out), redirect_stderr(err):
                try:
                    code = merge.main()
                except SystemExit as error:
                    code = error.code
            return code, out.getvalue(), err.getvalue()

        code, out, _ = cli(["--check"])
        self.assertEqual(code, 0)
        self.assertIn('"data/benchmarks.json"', out)
        self.assertIn('"scripts/preview_candidates.py"', out)
        digest = next(line.split()[1] for line in out.splitlines() if line.startswith("snapshot-sha256 "))
        self.assertEqual(cli(["--apply"])[0], 2)
        self.assertEqual(cli(["--check", "--expected-sha256", digest])[0], 2)
        before = (self.root / "data/benchmarks.json").read_bytes()
        extra = self.root / "data/extra.txt"
        extra.write_text("changed")
        code, _, err = cli(["--apply", "--expected-sha256", digest])
        self.assertEqual(code, 1)
        self.assertIn("does not match", err)
        self.assertEqual((self.root / "data/benchmarks.json").read_bytes(), before)
        extra.unlink()
        script = self.root / merge.SCRIPT_INPUTS[0]
        script_bytes = script.read_bytes()
        script.write_bytes(script_bytes + b"\n# changed\n")
        self.assertEqual(cli(["--apply", "--expected-sha256", digest])[0], 1)
        script.write_bytes(script_bytes)
        self.assertEqual(cli(["--apply", "--expected-sha256", digest])[0], 0)

    def test_real_review_is_required_and_android_is_not(self):
        self.review.stop()
        with self.assertRaises(DataError):
            merge.run(self.root, True)  # Missing scope/evidence, not Android.
        self.assertFalse((self.root / merge.REVIEW / "batch.json").exists())

    def test_actual_review_scope_and_android_optional(self):
        self.review.stop()
        obj = copy.deepcopy(self.objects)
        obj["benchmarks"][0]["version"] = "5.0"
        obj["mappings"][0]["modelId"] = "example/in-scope"
        self.stage(merge.STAGING[0], obj)
        batch_id = "benchmark-refresh-2026-10-28"
        write(self.root / merge.REVIEW / "models.json", {
            "schemaVersion": 1, "batchId": batch_id, "responseSha256": "0" * 64,
            "startDate": "2026-04-28", "cutoff": "2026-10-28",
            "sourceUrl": "https://models.dev/models.json?type=all", "selectionPolicy": "test",
            "retrievedAt": "2026-10-28T00:00:00Z", "dateIssues": [],
            "models": [{"id": "example/in-scope", "name": "Example", "releaseDate": "2026-05-01"}],
        })
        android_path = "../model-atlas-android/assets/benchmarks.json"
        write(self.root / merge.REVIEW / "baseline.json", {
            "schemaVersion": 1, "batchId": batch_id, "maintenanceResults": [],
            "maintenanceEntities": {"benchmarks": [], "sources": [], "mappings": []},
            "androidSnapshot": {"path": android_path, "sha256": "1" * 64, "version": 1, "scores": []},
            "protectedFiles": [{"path": android_path, "sha256": "1" * 64}],
        })
        targets = [{"id": target, "benchmarkIds": ["bench"] if i == 0 else [],
                    "officialUrls": ["https://example.com"], "status": "collected" if i == 0 else "blocked",
                    "notes": "test", "searches": [{"tier": 1, "url": "https://example.com", "outcome": "test"}]}
                   for i, target in enumerate(merge.TARGETS)]
        evidence = [{"id": "evidence", "sourceId": "source", "url": "https://example.com", "retrievedAt": "2026-10-28T00:00:00Z", "responseSha256": None, "locator": "table", "excerpt": "test", "notes": "test"}]
        for i, name in enumerate(merge.EVIDENCE):
            write(self.root / merge.REVIEW / name, {"targets": targets if i == 0 else [], "evidence": evidence if i == 0 else [], "systemOnly": []})
        self.assertGreater(merge.run(self.root), 0)  # no sibling Android checkout
        obj["mappings"][0]["modelId"] = "example/out-of-scope"
        self.stage(merge.STAGING[0], obj)
        with self.assertRaisesRegex(DataError, "outside frozen scope"):
            merge.run(self.root, True)
        self.assertFalse((self.root / merge.REVIEW / "batch.json").exists())


if __name__ == "__main__":
    unittest.main()
