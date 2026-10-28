from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile

from scripts.build import build
from scripts.validate import DataError, load_data, read_bundle, read_json

ROOT = Path(__file__).resolve().parents[1]
V2_SHA256 = "9020d8b7cd82b510a3f1ba8256100972be30848d6bd4445683c9080b4dc2d63d"
V2_IDS = {
    "deepseek-r1-readme-distill-qwen-32b-math-500",
    "deepseek-r1-readme-r1-math-500",
    "deepseek-r1-readme-r1-mmlu-pro-em",
    "deepseek-r1-readme-v3-math-500",
    "deepseek-r1-readme-v3-mmlu-pro-em",
}


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def copy_fixture(destination: Path) -> Path:
    destination.mkdir(parents=True)
    for relative in ("data", "benchmarks", "attributions", "third_party"):
        shutil.copytree(ROOT / relative, destination / relative)
    shutil.copy2(ROOT / "manifest.json", destination / "manifest.json")
    return destination


class DataValidationTest(unittest.TestCase):
    def test_maintenance_data_is_valid(self):
        data = load_data(ROOT)
        self.assertTrue(data["scores"])
        self.assertTrue(data["benchmarks"])
        self.assertEqual(len(data["scores"]), len(data["scoresById"]))

    def test_android_v2_contract_and_published_bytes_are_pinned(self):
        manifest, snapshot, raw = read_bundle(ROOT)
        self.assertEqual(1, manifest["schemaVersion"])
        self.assertEqual(2, manifest["version"])
        self.assertEqual("https://chenlongapps.github.io/model-atlas-data/benchmarks/scores-v2.json", manifest["url"])
        self.assertEqual(V2_SHA256, hashlib.sha256(raw).hexdigest())
        self.assertEqual(V2_SHA256, manifest["sha256"])
        self.assertEqual(1, snapshot["schemaVersion"])
        self.assertEqual(V2_IDS, {score["id"] for score in snapshot["scores"]})
        self.assertTrue(all("cost" in score for score in snapshot["scores"]))

    def test_pre_refactor_archive_retains_review_inputs_and_orphan_sources(self):
        archive = ROOT / "archive/pre-refactor-2026-10-28.zip"
        with zipfile.ZipFile(archive) as zipped:
            names = set(zipped.namelist())
            self.assertIn("data/reviews/2026-10-28/decisions.json", names)
            self.assertIn("data/reviews/2026-10-28/staging-indices.json", names)
            self.assertIn("schemas/review-decisions.schema.json", names)
            self.assertIn("docs/candidate-review.md", names)
            self.assertIn("scripts/preview_candidates.py", names)
            self.assertIn("tests/test_candidate_review.py", names)
            legacy_sources = json.loads(zipped.read("data/sources.json"))
            legacy_mappings = json.loads(zipped.read("data/model-mappings.json"))
            self.assertGreater(len(legacy_sources["sources"]), 0)
            self.assertGreater(len(legacy_mappings["mappings"]), 0)

    def test_minimal_pending_score_needs_no_source_or_mapping_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            root = copy_fixture(Path(directory) / "repo")
            document = json.loads((root / "data/scores.json").read_text(encoding="utf-8"))
            document["scores"].append({
                "id": "minimal-pending-score",
                "modelId": None,
                "sourceModelName": "Unmatched original model name",
                "benchmarkId": "math-500",
                "score": 91.2,
                "sourceUrl": "https://example.org/results",
                "status": "pending",
                "source": {"publisher": "Example publisher", "status": "pending",
                           "license": {"redistribution": "pending"}},
                "modelMapping": {"status": "pending"},
            })
            dump(root / "data/scores.json", document)
            loaded = load_data(root)
            self.assertIn("minimal-pending-score", loaded["scoresById"])

    def test_duplicate_json_keys_and_non_finite_values_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text('{"scores": [], "scores": []}', encoding="utf-8")
            with self.assertRaisesRegex(DataError, "duplicate JSON key"):
                read_json(path)
            path.write_text('{"score": NaN}', encoding="utf-8")
            with self.assertRaisesRegex(DataError, "non-finite"):
                read_json(path)


class BuildTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = copy_fixture(Path(self.temp.name) / "repo")
        self.output = Path(self.temp.name) / "output"

    def scores(self):
        return json.loads((self.root / "data/scores.json").read_text(encoding="utf-8"))["scores"]

    def write_scores(self, scores):
        dump(self.root / "data/scores.json", {"scores": scores})

    def test_build_preserves_published_ids_and_sha(self):
        rows = self.scores()
        added = copy.deepcopy(next(row for row in rows if row["status"] == "approved"))
        added["id"] = "synthetic-build-check-score"
        added["score"] = 88.8
        rows.append(added)
        self.write_scores(rows)

        report = build(self.root, self.output, 3, baseline=self.root)
        manifest, snapshot, raw = read_bundle(self.output)
        self.assertEqual(3, manifest["version"])
        self.assertEqual(V2_SHA256, hashlib.sha256((self.output / "benchmarks/scores-v2.json").read_bytes()).hexdigest())
        self.assertEqual(V2_IDS | {"synthetic-build-check-score"}, {score["id"] for score in snapshot["scores"]})
        self.assertEqual(1, snapshot["schemaVersion"])
        self.assertEqual(3, snapshot["version"])
        self.assertEqual(hashlib.sha256(raw).hexdigest(), manifest["sha256"])
        self.assertEqual(["synthetic-build-check-score"], report["added"])
        self.assertEqual([], report["removed"])
        self.assertFalse({row["id"] for row in rows if row["status"] == "pending"} &
                         {row["id"] for row in snapshot["scores"]})

    def test_noop_or_same_version_release_is_refused(self):
        with self.assertRaisesRegex(DataError, "no Android-visible score changes"):
            build(self.root, self.output, 3, baseline=self.root)
        with self.assertRaisesRegex(DataError, "greater than published version"):
            build(self.root, self.output, 2, baseline=self.root)

    def test_approved_score_cannot_use_pending_redistribution_permission(self):
        rows = self.scores()
        approved = next(row for row in rows if row["status"] == "approved")
        approved["source"]["license"]["redistribution"] = "pending"
        self.write_scores(rows)
        with self.assertRaisesRegex(DataError, "approved source lacks redistribution permission"):
            load_data(self.root)

    def test_empty_snapshot_is_refused(self):
        rows = self.scores()
        for row in rows:
            if row["status"] == "approved":
                row["status"] = "pending"
        self.write_scores(rows)
        with self.assertRaisesRegex(DataError, "no approved scores"):
            build(self.root, self.output, 3, baseline=self.root)

    def test_published_score_deletion_needs_an_explicit_reason(self):
        rows = self.scores()
        rows.remove(next(row for row in rows if row["id"] in V2_IDS))
        self.write_scores(rows)
        with self.assertRaisesRegex(DataError, "would remove 1 published scores"):
            build(self.root, self.output, 3, baseline=self.root)
        result = build(self.root, self.output, 3, baseline=self.root,
                       allow_removals=True, reason="Synthetic test of explicit removal gate.")
        self.assertEqual(1, len(result["removed"]))

    def test_approved_source_not_in_android_bundle_is_blocked(self):
        rows = self.scores()
        added = copy.deepcopy(next(row for row in rows if row["status"] == "approved"))
        added["id"] = "synthetic-unbundled-source"
        added["score"] = 87.2
        added["sourceUrl"] = "https://example.org/synthetic-result"
        added["sourceType"] = "independent"
        added["source"] = copy.deepcopy(added["source"])
        added["source"].update({"publisher": "Synthetic source"})
        added["source"]["license"].update({
            "name": "Apache-2.0", "url": "https://example.org/LICENSE",
            "licenseFile": "third_party/mmlu-pro/APACHE-2.0.txt",
            "attribution": "Synthetic attribution for a local test only.",
            "notes": "Synthetic permission record; never shipped.",
        })
        rows.append(added)
        self.write_scores(rows)
        with self.assertRaisesRegex(DataError, "attribution bundle does not cover this source"):
            build(self.root, self.output, 3, baseline=self.root)


if __name__ == "__main__":
    unittest.main()
