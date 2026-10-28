"""Candidate report regressions, using synthetic fixtures only."""

import copy
from contextlib import redirect_stdout
import io
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import test_pipeline as pipeline
from build import build
from common import DataError, json_bytes, load_catalog, read_json, sha256
from preview_candidates import (
    REFRESH_VERSIONS, print_protection_notice, refresh_policy, review_candidates, staging_preview, write_preview,
)


class CandidateReviewTest(unittest.TestCase):
    def setUp(self):
        self.fixture = pipeline.PipelineTest(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.directory = self.root / "data/reviews/synthetic"
        self.directory.mkdir(parents=True)
        self.batch_path = self.directory / "batch.json"
        self.output = self.root / "build/candidate-only"
        build(self.root, self.fixture.output, 2, release=True)
        snapshot = read_json(self.fixture.output / "benchmarks/scores-v2.json")
        relative = "../model-atlas-android/app/src/main/assets/benchmarks.json"
        path = self.root / relative
        path.parent.mkdir(parents=True)
        path.write_bytes(json_bytes(snapshot))
        old_catalog = load_catalog(self.root)
        self.baseline = {
            "schemaVersion": 1, "batchId": "synthetic-review",
            "maintenanceResults": copy.deepcopy(old_catalog.results),
            "maintenanceEntities": {key: list(getattr(old_catalog, key).values()) for key in ("benchmarks", "sources", "mappings")},
            "androidSnapshot": {"path": relative, "version": 2, "sha256": sha256(path.read_bytes()), "scores": snapshot["scores"]},
            "protectedFiles": [
                {"path": relative, "sha256": sha256(path.read_bytes())},
                {"path": "manifest.json", "sha256": sha256((self.root / "manifest.json").read_bytes())},
            ],
        }
        self.scope = {
            "schemaVersion": 1, "batchId": "synthetic-review", "startDate": "2026-04-28", "cutoff": "2026-10-28",
            "retrievedAt": "2026-10-28T12:00:00Z", "sourceUrl": "https://example.org/models.json",
            "responseSha256": "a" * 64, "selectionPolicy": "Synthetic fixed release-date scope.",
            "models": [{"id": "test/new-model", "name": "Synthetic new model", "releaseDate": "2026-06-01"}],
            "dateIssues": [],
        }
        self.batch = {
            "schemaVersion": 1, "id": "synthetic-review", "scopeFile": "models.json", "baselineFile": "baseline.json",
            "evidenceFiles": ["evidence.json"], "targetIds": ["synthetic-target"],
            "candidateResultIds": ["candidate-result"], "notes": "Synthetic review, never publish.",
        }
        self.evidence = {
            "targets": [{"id": "synthetic-target", "benchmarkIds": ["candidate-bench"],
                         "officialUrls": ["https://example.org/benchmark"], "status": "collected",
                         "notes": "Synthetic evidence only.",
                         "searches": [{"tier": 1, "url": "https://example.org/results", "outcome": "Synthetic row."}]}],
            "evidence": [{"id": "synthetic-evidence", "sourceId": "candidate-source", "url": "https://example.org/results",
                          "retrievedAt": "2026-10-28T12:00:00Z", "responseSha256": None,
                          "locator": "row 1", "excerpt": "Synthetic new model: 0", "notes": "Test only."}],
            "systemOnly": [],
        }
        documents = self.fixture.documents
        for filename, key, new_id in (
            ("benchmarks.json", "benchmarks", "candidate-bench"),
            ("sources.json", "sources", "candidate-source"),
            ("model-mappings.json", "mappings", "candidate-mapping"),
        ):
            item = copy.deepcopy(documents[filename][key][0])
            item.update(id=new_id, status="pending")
            documents[filename][key].append(item)
        self.mapping = documents["model-mappings.json"]["mappings"][-1]
        self.mapping.update(sourceId="candidate-source", modelId="test/new-model")
        self.source = documents["sources.json"]["sources"][-1]
        self.source["license"].update(redistribution="pending", licenseFile=None)
        self.result = copy.deepcopy(self.fixture.result)
        self.result.update(id="candidate-result", benchmarkId="candidate-bench", sourceId="candidate-source",
                           mappingId="candidate-mapping", status="pending")
        documents["results/candidate-bench.json"] = {"schemaVersion": 1, "results": [self.result]}
        self.save()

    def save(self):
        self.fixture.save()
        for name, content in (("batch.json", self.batch), ("models.json", self.scope),
                              ("baseline.json", self.baseline), ("evidence.json", self.evidence)):
            (self.directory / name).write_bytes(json_bytes(content))

    def report(self, check_android=False):
        self.save()
        return review_candidates(self.root, self.batch_path, check_android)

    def test_two_baselines_pending_only_and_no_mutations(self):
        self.save()
        before = {path: path.read_bytes() for path in (self.root / "data").rglob("*.json")}
        report = write_preview(self.root, self.batch_path, self.output, check_android=True)
        self.assertEqual("candidate-only", report["mode"])
        self.assertIs(report["deployable"], False)
        self.assertIs(report["actualChangesApplied"], False)
        self.assertEqual(["synthetic-result"], report["maintenanceDiff"]["wouldRemove"])
        self.assertEqual(["synthetic-result"], report["androidDiff"]["wouldRemove"])
        self.assertEqual(["candidate-result"], report["maintenanceDiff"]["wouldAddPending"])
        self.assertEqual(0, report["summary"]["approvedNewResults"])
        self.assertEqual({"report.md", "report.json"}, {path.name for path in self.output.iterdir()})
        self.assertEqual(before, {path: path.read_bytes() for path in (self.root / "data").rglob("*.json")})
        self.assertEqual(["synthetic-result"], [row["id"] for row in load_catalog(self.root).publishable()])
        first = (self.output / "report.json").read_bytes()
        write_preview(self.root, self.batch_path, self.output, check_android=True)
        self.assertEqual(first, (self.output / "report.json").read_bytes())

    def test_legacy_results_cannot_be_candidates(self):
        self.batch["candidateResultIds"].append("synthetic-result")
        with self.assertRaisesRegex(DataError, "old baseline"):
            self.report()

    def test_explicit_membership_ignores_other_batches_and_requires_pending(self):
        other = {**self.result, "id": "another-batch-result"}
        self.fixture.documents["results/candidate-bench.json"]["results"].append(other)
        self.assertEqual(1, self.report()["summary"]["candidateResults"])
        self.result["status"] = "rejected"
        with self.assertRaisesRegex(DataError, "remain pending"):
            self.report()

    def test_unknown_batch_member_is_rejected(self):
        self.batch["candidateResultIds"].append("unknown-result")
        with self.assertRaisesRegex(DataError, "unknown candidate"):
            self.report()

    def test_old_maintenance_entities_and_results_are_protected(self):
        self.fixture.result["score"] = 1
        with self.assertRaisesRegex(DataError, "protected maintenance result changed"):
            self.report()
        self.fixture.result["score"] = 0
        self.fixture.benchmark["description"] = "Changed baseline definition."
        with self.assertRaisesRegex(DataError, "protected benchmarks entity"):
            self.report()

    def test_out_of_scope_and_unresolved_mapping_are_distinct(self):
        self.mapping["modelId"] = "test/old-model"
        with self.assertRaisesRegex(DataError, "outside frozen scope"):
            self.report()
        self.mapping["modelId"] = None
        self.mapping["evidenceUrl"] = None
        report = self.report()
        self.assertEqual(1, report["summary"]["unmappedCandidates"])
        self.assertIn("model-identity-unconfirmed", report["candidates"][0]["blockers"])
        self.assertEqual("not-collected", report["modelCoverage"][0]["targets"]["synthetic-target"]["status"])

    def test_unrepresented_conditions_and_license_are_blockers(self):
        self.result["unrepresentedConditions"] = ["Synthetic hardware budget cannot be represented."]
        blockers = self.report()["candidates"][0]["blockers"]
        self.assertIn("essential-conditions-not-representable-in-android-v1", blockers)
        self.assertIn("redistribution-and-client-attribution-unconfirmed", blockers)

    def test_refresh_does_not_attribute_default_fallback_to_single_model(self):
        self.batch["id"] = "benchmark-refresh-2026-10-28"
        self.scope["batchId"] = self.baseline["batchId"] = self.batch["id"]
        for condition in ("Default Fallback", "Opus 4.8 Fallback", "Opus 5 Fallback"):
            with self.subTest(condition=condition):
                self.result["unrepresentedConditions"] = [condition]
                with unittest.mock.patch("preview_candidates.refresh_policy"):
                    with self.assertRaisesRegex(DataError, "fallback system"):
                        self.report()

    def test_missing_evidence_and_target_membership_are_rejected(self):
        self.evidence["evidence"] = []
        with self.assertRaisesRegex(DataError, "source evidence missing"):
            self.report()
        self.evidence["targets"][0]["benchmarkIds"] = []
        with self.assertRaisesRegex(DataError, "outside target"):
            self.report()

    def test_duplicate_candidates_and_targets_are_rejected(self):
        self.batch["candidateResultIds"].append("candidate-result")
        with self.assertRaises(DataError):
            self.report()
        self.batch["candidateResultIds"].pop()
        self.evidence["targets"].append(copy.deepcopy(self.evidence["targets"][0]))
        with self.assertRaisesRegex(DataError, "duplicate review target"):
            self.report()

    def test_exact_window_and_partial_month_precision(self):
        model = self.scope["models"][0]
        for value in ("2026-04-27", "2026-10-29", "2026-04", "2026-10"):
            with self.subTest(value=value):
                model["releaseDate"] = value
                with self.assertRaisesRegex(DataError, "outside fixed window"):
                    self.report()
        for value in ("2026-04-28", "2026-10-28", "2026-06"):
            model["releaseDate"] = value
            self.report()

    def test_all_targets_must_have_investigation_outcomes(self):
        self.evidence["targets"][0]["searches"] = []
        with self.assertRaises(DataError):
            self.report()

    def test_protected_android_is_opt_in_and_detects_changes(self):
        self.assertEqual("not-checked", self.report()["protectedFiles"][0]["status"])
        android_path = self.root / self.baseline["androidSnapshot"]["path"]
        android_path.write_text("changed", encoding="utf-8")
        with self.assertRaisesRegex(DataError, "protected file changed"):
            self.report(check_android=True)

    def test_android_digest_consistency_is_checked_without_sibling(self):
        self.baseline["androidSnapshot"]["sha256"] = "b" * 64
        with self.assertRaisesRegex(DataError, "baseline hashes differ"):
            self.report()

    def test_unchecked_android_is_explicit_in_ci_notice(self):
        report = self.report()
        output = io.StringIO()
        with redirect_stdout(output):
            print_protection_notice(report)
        self.assertIn("Android protected files not checked", output.getvalue())
        output = io.StringIO()
        with redirect_stdout(output):
            print_protection_notice(self.report(check_android=True))
        self.assertEqual("", output.getvalue())

    def test_empty_candidates_are_not_deployable_and_do_not_erase_data(self):
        self.batch["candidateResultIds"] = []
        self.fixture.documents["results/candidate-bench.json"]["results"] = []
        self.evidence["targets"][0]["status"] = "blocked"
        report = self.report()
        self.assertEqual(0, report["summary"]["candidateResults"])
        self.assertFalse(report["deployable"])
        self.assertEqual(1, len(load_catalog(self.root).publishable()))

    def test_output_and_attachment_path_escape_are_rejected(self):
        self.save()
        for output in (self.root / "data/reports", self.root / "build", self.root.parent / "elsewhere"):
            with self.subTest(output=output), self.assertRaises(DataError):
                write_preview(self.root, self.batch_path, output)
        self.batch["scopeFile"] = "../models.json"
        with self.assertRaisesRegex(DataError, "escapes batch"):
            self.report()

    def test_output_symlink_is_rejected_before_writes(self):
        self.save()
        self.output.parent.mkdir(parents=True)
        self.output.symlink_to(self.directory, target_is_directory=True)
        with self.assertRaisesRegex(DataError, "must be under"):
            write_preview(self.root, self.batch_path, self.output)
        self.assertFalse((self.directory / "report.json").exists())

    def test_staging_preview_uses_isolated_plan_without_writing_repository(self):
        self.save()
        before = {path: path.read_bytes() for path in (self.root / "data").rglob("*.json")}
        captured = {}

        def plan(root, sandbox):
            captured["sandbox"] = sandbox
            self.assertFalse(sandbox.is_relative_to(root))

        def review(root, batch, check_android, android_root):
            self.assertEqual(root, captured["sandbox"])
            self.assertTrue(check_android)
            self.assertEqual(self.root.resolve().parent / "model-atlas-android", android_root)
            return {"notes": "test"}

        with patch("merge_candidate_staging.plan", side_effect=plan), patch("preview_candidates.review_candidates", side_effect=review):
            report = staging_preview(self.root, check_android=True)
        self.assertTrue(report["stagingOnly"])
        self.assertIn("not yet fully imported", report["notes"])
        self.assertEqual(before, {path: path.read_bytes() for path in (self.root / "data").rglob("*.json")})

    def test_existing_publication_or_other_batch_reports_cannot_be_overwritten(self):
        self.save()
        for name, files in (
            ("production", {"manifest.json": {}, "report.json": {"mode": "release"}}),
            ("preview", {"report.json": {"mode": "preview"}}),
            ("other-batch", {"report.json": {"mode": "candidate-only", "deployable": False, "batchId": "other"}}),
        ):
            with self.subTest(name=name):
                output = self.output / name
                output.mkdir(parents=True)
                for filename, data in files.items():
                    (output / filename).write_bytes(json_bytes(data))
                before = {path.name: path.read_bytes() for path in output.iterdir()}
                with self.assertRaises(DataError):
                    write_preview(self.root, self.batch_path, output)
                self.assertEqual(before, {path.name: path.read_bytes() for path in output.iterdir()})

    def test_atomic_replacement_does_not_truncate_hard_linked_files(self):
        self.save()
        write_preview(self.root, self.batch_path, self.output)
        source = self.root / "data/results/synthetic-bench.json"
        before = source.read_bytes()
        destination = self.output / "report.md"
        destination.unlink()
        os.link(source, destination)
        with self.assertRaisesRegex(DataError, "existing candidate report differs"):
            write_preview(self.root, self.batch_path, self.output)
        self.assertEqual(before, source.read_bytes())
        self.assertEqual(source.stat().st_ino, destination.stat().st_ino)

    def test_malformed_evidence_and_system_records_are_rejected(self):
        self.evidence["systemOnly"] = ["not a system record"]
        with self.assertRaises(DataError):
            self.report()
        self.evidence["systemOnly"] = []
        self.evidence["targets"][0]["officialUrls"] = ["http://example.org/insecure"]
        with self.assertRaises(DataError):
            self.report()

    def test_evidence_keeps_actual_retrieval_precision(self):
        self.evidence["evidence"][0]["retrievedAt"] = "2026-10-28"
        self.assertEqual("2026-10-28", self.report()["evidence"][0]["retrievedAt"])

    def test_refresh_policy_rejects_missing_targets_old_versions_and_date_drift(self):
        scope = {"startDate": "2026-04-28", "cutoff": "2026-10-28", "sourceUrl": "https://models.dev/models.json?type=all"}
        targets = [{"id": key, "benchmarkIds": ["policy-" + key]} for key in REFRESH_VERSIONS]
        benchmarks = {"policy-" + key: {"version": next(iter(versions))} for key, versions in REFRESH_VERSIONS.items()}
        next(target for target in targets if target["id"] == "swe-bench-pro")["benchmarkIds"] = ["swe-bench-pro-v2"]
        benchmarks["swe-bench-pro-v2"] = benchmarks.pop("policy-swe-bench-pro")
        batch_id = "benchmark-refresh-2026-10-28"
        refresh_policy(batch_id, scope, targets, benchmarks)
        with self.assertRaisesRegex(DataError, "all eleven"):
            refresh_policy(batch_id, scope, targets[:-1], benchmarks)
        with self.assertRaisesRegex(DataError, "fixed half-year"):
            refresh_policy(batch_id, {**scope, "startDate": "1900-01-01"}, targets, benchmarks)
        swe_target = next(target for target in targets if target["id"] == "swe-bench-pro")
        for excluded in ("swe-bench-pro-v2-commercial-private", "swe-bench-pro-v2-hard51"):
            swe_target["benchmarkIds"] = [excluded]
            benchmarks[excluded] = {"version": "2"}
            with self.assertRaisesRegex(DataError, "V2 public benchmark ID"):
                refresh_policy(batch_id, scope, targets, benchmarks)
        swe_target["benchmarkIds"] = ["swe-bench-pro-v2"]
        benchmarks["swe-bench-pro-v2"]["version"] = "1"
        with self.assertRaisesRegex(DataError, "outside approved refresh policy"):
            refresh_policy(batch_id, scope, targets, benchmarks)


if __name__ == "__main__":
    unittest.main()
