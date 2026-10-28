"""Synthetic fixtures only: no test result may become a production seed."""

import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from build import build
from export_android import export_android
from release_archive import pack, unpack
from check_remote import verify_remote
from common import (
    DataError, ROOT, json_bytes, load_catalog, read_artifacts, read_json,
    sha256, validate_schema, validate_snapshot,
)


class PipelineTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="model-atlas-data-test-")
        self.addCleanup(self.temporary.cleanup)
        self.directory = Path(self.temporary.name)
        self.root = self.directory / "repository"
        self.output = self.directory / "output"
        shutil.copytree(ROOT / "schemas", self.root / "schemas")
        self.documents = {
            "benchmarks.json": {
                "schemaVersion": 1,
                "benchmarks": [{
                    "id": "synthetic-bench", "name": "Synthetic test only", "version": "test-v1",
                    "description": "Synthetic unit-test fixture, never publish as real data.",
                    "category": "other", "officialUrl": "https://example.org/benchmark",
                    "metric": "error", "unit": "points", "higherIsBetter": False,
                    "minimum": -10, "maximum": 10, "status": "approved",
                }],
            },
            "sources.json": {
                "schemaVersion": 1,
                "sources": [{
                    "id": "synthetic-source", "publisher": "Synthetic fixture",
                    "url": "https://example.org/results", "retrievedAt": "2026-10-28",
                    "publishedAt": "2026-10-27", "sourceType": "independent", "status": "approved",
                    "license": {
                        "name": "Synthetic permission", "url": "https://example.org/terms",
                        "licenseFile": "third_party/synthetic/LICENSE.txt", "redistribution": "allowed",
                        "attribution": "Unit-test fixture only", "notes": "Not a real evaluation.",
                    },
                }],
            },
            "model-mappings.json": {
                "schemaVersion": 1,
                "mappings": [{
                    "id": "synthetic-mapping", "sourceId": "synthetic-source", "sourceModelName": "Synthetic model",
                    "modelId": "test/model", "evidenceUrl": "https://example.org/model-version",
                    "catalogUrl": "https://example.org/catalog", "status": "approved", "notes": "Synthetic mapping.",
                }],
            },
            "results/synthetic-bench.json": {
                "schemaVersion": 1,
                "results": [{
                    "id": "synthetic-result", "benchmarkId": "synthetic-bench", "mappingId": "synthetic-mapping",
                    "score": 0, "sourceId": "synthetic-source", "sourceLocator": "table / row 1",
                    "collectedAt": "2026-10-28", "evaluatedAt": None, "subset": None,
                    "harness": "test-harness", "reasoningEffort": None, "toolsEnabled": False,
                    "status": "approved", "unrepresentedConditions": [], "notes": "Synthetic result.",
                }],
            },
        }
        license_file = self.root / "third_party/synthetic/LICENSE.txt"
        license_file.parent.mkdir(parents=True)
        license_file.write_text("Synthetic test permission, not a real source license.\n", encoding="utf-8")
        self.save()
        self.artifacts(self.root, {"schemaVersion": 1, "version": 1, "scores": []})

    @property
    def result(self):
        return self.documents["results/synthetic-bench.json"]["results"][0]

    @property
    def source(self):
        return self.documents["sources.json"]["sources"][0]

    @property
    def mapping(self):
        return self.documents["model-mappings.json"]["mappings"][0]

    @property
    def benchmark(self):
        return self.documents["benchmarks.json"]["benchmarks"][0]

    def save(self):
        for relative, data in self.documents.items():
            path = self.root / "data" / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(json_bytes(data))

    def artifacts(self, directory, snapshot):
        content = json_bytes(snapshot)
        path = directory / "benchmarks" / f"scores-v{snapshot['version']}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        manifest = {"schemaVersion": 1, "version": snapshot["version"],
                    "url": f"https://example.org/data/benchmarks/{path.name}", "sha256": sha256(content)}
        (directory / "manifest.json").write_bytes(json_bytes(manifest))

    def reject_catalog(self):
        self.save()
        with self.assertRaises(DataError):
            load_catalog(self.root)

    def test_release_matches_android_v1_and_preserves_unknowns_and_false(self):
        report = build(self.root, self.output, 2, release=True)
        manifest, snapshot = read_artifacts(self.output, self.root)
        score = snapshot["scores"][0]
        self.assertEqual(2, manifest["version"])
        self.assertEqual(["synthetic-result"], report["added"])
        self.assertEqual("test/model", score["modelId"])
        self.assertEqual(0, score["score"])
        self.assertIs(score["higherIsBetter"], False)
        self.assertIs(score["toolsEnabled"], False)
        self.assertIsNone(score["evaluatedAt"])
        self.assertIsNone(score["subset"])
        self.assertIsNone(score["cost"])
        self.assertEqual({"id", "modelId", "benchmarkId", "score", "metric", "unit", "higherIsBetter",
                          "subset", "harness", "reasoningEffort", "toolsEnabled", "sourceUrl", "sourceType", "evaluatedAt", "cost"}, set(score))
        self.assertEqual({"schemaVersion", "version", "url", "sha256"}, set(manifest))
        self.assertTrue((self.output / "attributions/v2.json").is_file())
        self.assertTrue((self.output / "third_party/synthetic/LICENSE.txt").is_file())

    def test_pending_data_is_excluded_and_empty_production_is_refused(self):
        self.result["status"] = "pending"
        self.save()
        report = build(self.root, self.output, 2)
        self.assertEqual(0, report["scoreCount"])
        self.assertEqual([{"id": "synthetic-result", "status": "pending"}], report["sourceSummary"]["excludedResults"])
        release_output = self.directory / "production"
        with self.assertRaisesRegex(DataError, "empty snapshots"):
            build(self.root, release_output, 2, release=True)
        self.assertFalse(release_output.exists())

    def test_rejected_results_are_excluded(self):
        self.result["status"] = "rejected"
        self.save()
        self.assertEqual([], load_catalog(self.root).publishable())

    def test_approved_result_cannot_depend_on_pending_entities(self):
        for item in (self.benchmark, self.source, self.mapping):
            with self.subTest(item=item["id"]):
                item["status"] = "pending"
                self.reject_catalog()
                item["status"] = "approved"

    def test_mapping_requires_canonical_id_and_both_evidence_links(self):
        for key in ("modelId", "evidenceUrl", "catalogUrl"):
            with self.subTest(key=key):
                original = self.mapping[key]
                self.mapping[key] = None
                self.reject_catalog()
                self.mapping[key] = original

    def test_unknown_references_and_cross_source_mappings_are_rejected(self):
        for key in ("benchmarkId", "mappingId", "sourceId"):
            with self.subTest(key=key):
                original = self.result[key]
                self.result[key] = "unknown"
                self.reject_catalog()
                self.result[key] = original
        other = copy.deepcopy(self.source)
        other["id"] = "other-source"
        self.documents["sources.json"]["sources"].append(other)
        self.mapping["sourceId"] = "other-source"
        self.reject_catalog()

    def test_license_requires_permission_and_evidence(self):
        for key, bad_value in (("redistribution", "pending"), ("redistribution", "prohibited"),
                               ("name", None), ("url", None), ("licenseFile", None),
                               ("licenseFile", "../secret"), ("licenseFile", "third_party/missing.txt")):
            with self.subTest(key=key, value=bad_value):
                original = self.source["license"][key]
                self.source["license"][key] = bad_value
                self.reject_catalog()
                self.source["license"][key] = original

    def test_license_symlink_cannot_escape_repository(self):
        outside = self.directory / "outside.txt"
        outside.write_text("outside", encoding="utf-8")
        path = self.root / "third_party/synthetic/escape.txt"
        path.symlink_to(outside)
        self.source["license"]["licenseFile"] = "third_party/synthetic/escape.txt"
        self.reject_catalog()

    def test_duplicate_ids_are_rejected_in_each_document(self):
        for relative, key in (("benchmarks.json", "benchmarks"), ("sources.json", "sources"),
                              ("model-mappings.json", "mappings"), ("results/synthetic-bench.json", "results")):
            with self.subTest(relative=relative):
                rows = self.documents[relative][key]
                rows.append(copy.deepcopy(rows[0]))
                self.reject_catalog()
                rows.pop()

    def test_duplicate_json_keys_nan_infinity_and_overflow_are_rejected(self):
        path = self.directory / "bad.json"
        for content in ('{"a":1,"a":2}', '{"a":{"b":1,"b":2}}', '{"score":NaN}',
                        '{"score":Infinity}', '{"score":-Infinity}', '{"score":1e9999}'):
            with self.subTest(content=content):
                path.write_text(content, encoding="utf-8")
                with self.assertRaises(DataError):
                    read_json(path)

    def test_score_ranges_are_benchmark_specific_and_boolean_is_not_number(self):
        for bad_value in (-11, 11, True, "0"):
            with self.subTest(value=bad_value):
                self.result["score"] = bad_value
                self.reject_catalog()
        self.result["score"] = -1
        self.save()
        self.assertEqual(-1, load_catalog(self.root).publishable()[0]["score"])

    def test_inverted_range_and_missing_direction_are_rejected(self):
        self.benchmark["minimum"] = 11
        self.reject_catalog()
        self.benchmark["minimum"] = -10
        self.benchmark["higherIsBetter"] = None
        self.reject_catalog()

    def test_unknown_fields_and_unrepresentable_conditions_cannot_silently_disappear(self):
        self.result["variant"] = "essential configuration"
        self.reject_catalog()
        del self.result["variant"]
        self.result["unrepresentedConditions"] = ["essential configuration without a v1 field"]
        self.reject_catalog()

    def test_test_source_and_bad_dates_are_rejected(self):
        self.source["sourceType"] = "test"
        self.reject_catalog()
        self.source["sourceType"] = "independent"
        self.result["evaluatedAt"] = "2026-02-30"
        self.reject_catalog()

    def test_result_filename_must_match_benchmark(self):
        source = self.root / "data/results/synthetic-bench.json"
        source.rename(source.with_name("wrong.json"))
        with self.assertRaisesRegex(DataError, "filename"):
            load_catalog(self.root)

    def test_non_https_credentials_and_whitespace_urls_are_rejected(self):
        for url in ("http://example.org", "https://user:password@example.org", "https://example.org/a b", "https://example.org:wrong"):
            with self.subTest(url=url):
                self.source["url"] = url
                self.reject_catalog()

    def test_manifest_version_hash_and_url_mismatches_are_rejected(self):
        build(self.root, self.output, 2)
        original = read_json(self.output / "manifest.json")
        for key, value in (("sha256", "0" * 64), ("url", "https://example.org/other.json"),
                           ("url", original["url"] + "?query=yes"), ("version", 1)):
            with self.subTest(key=key, value=value):
                manifest = {**original, key: value}
                (self.output / "manifest.json").write_bytes(json_bytes(manifest))
                with self.assertRaises(DataError):
                    read_artifacts(self.output, self.root)
        (self.output / "manifest.json").write_bytes(json_bytes(original))
        snapshot = read_json(self.output / "benchmarks/scores-v2.json")
        snapshot["version"] = 3
        content = json_bytes(snapshot)
        (self.output / "benchmarks/scores-v2.json").write_bytes(content)
        (self.output / "manifest.json").write_bytes(json_bytes({**original, "sha256": sha256(content)}))
        with self.assertRaisesRegex(DataError, "version mismatch"):
            read_artifacts(self.output, self.root)

    def test_old_versions_and_long_overflow_are_rejected(self):
        for version in (0, 1, -1, 2**63, True):
            with self.subTest(version=version), self.assertRaises(DataError):
                build(self.root, self.output, version)
        self.assertFalse(self.output.exists())

    def test_same_input_is_deterministic_and_build_is_idempotent(self):
        build(self.root, self.output, 2)
        first = {path.relative_to(self.output): path.read_bytes() for path in self.output.rglob("*") if path.is_file()}
        build(self.root, self.output, 2)
        second = {path.relative_to(self.output): path.read_bytes() for path in self.output.rglob("*") if path.is_file()}
        self.assertEqual(first, second)
        self.result["score"] = 1
        self.save()
        with self.assertRaisesRegex(DataError, "immutable artifact"):
            build(self.root, self.output, 2)
        self.assertEqual(first[Path("manifest.json")], (self.output / "manifest.json").read_bytes())

    def test_sorting_does_not_depend_on_source_order(self):
        another = {**self.result, "id": "a-result", "score": 1}
        rows = self.documents["results/synthetic-bench.json"]["results"]
        rows.append(another)
        self.save()
        build(self.root, self.output, 2)
        rows.reverse()
        self.save()
        second = self.directory / "other-output"
        build(self.root, second, 2)
        self.assertEqual((self.output / "benchmarks/scores-v2.json").read_bytes(), (second / "benchmarks/scores-v2.json").read_bytes())

    def test_history_is_preserved_and_versioned_corrections_report_changes(self):
        build(self.root, self.output, 2, release=True)
        original_snapshot = (self.output / "benchmarks/scores-v2.json").read_bytes()
        self.result["score"] = 1
        self.save()
        corrected = self.directory / "corrected"
        report = build(self.root, corrected, 3, baseline=self.output, release=True)
        self.assertEqual(["synthetic-result"], report["changed"])
        self.assertEqual(original_snapshot, (corrected / "benchmarks/scores-v2.json").read_bytes())
        self.assertEqual((self.root / "benchmarks/scores-v1.json").read_bytes(), (corrected / "benchmarks/scores-v1.json").read_bytes())
        self.assertTrue((corrected / "attributions/v2.json").exists())
        self.assertTrue((corrected / "attributions/v3.json").exists())

    def test_removals_require_explicit_reason_and_do_not_allow_empty_release(self):
        another = {**self.result, "id": "another-result"}
        rows = self.documents["results/synthetic-bench.json"]["results"]
        rows.append(another)
        self.save()
        build(self.root, self.output, 2, release=True)
        rows.pop()
        self.save()
        target = self.directory / "next"
        preview = build(self.root, self.directory / "removal-preview", 3, baseline=self.output)
        self.assertEqual(["another-result"], preview["removed"])
        for allow, reason in ((False, "reviewed"), (True, "")):
            with self.subTest(allow=allow, reason=reason), self.assertRaisesRegex(DataError, "removes scores"):
                build(self.root, target, 3, baseline=self.output, release=True, allow_removals=allow, reason=reason)
        self.assertFalse(target.exists())
        report = build(self.root, target, 3, baseline=self.output, release=True, allow_removals=True, reason="reviewed synthetic removal")
        self.assertEqual(["another-result"], report["removed"])
        rows.clear()
        self.save()
        with self.assertRaisesRegex(DataError, "empty snapshots"):
            build(self.root, self.directory / "empty", 4, baseline=target, release=True, allow_removals=True, reason="reviewed")

    def test_outputs_cannot_overwrite_sources_or_baseline(self):
        for output in (self.root, self.directory, self.root / "data/generated", self.root / "benchmarks/generated"):
            with self.subTest(output=output), self.assertRaises(DataError):
                build(self.root, output, 2)

    def test_byte_limits_and_duplicate_snapshot_ids(self):
        build(self.root, self.output, 2)
        with patch("common.MAX_MANIFEST_BYTES", 10), self.assertRaises(DataError):
            read_artifacts(self.output, self.root)
        with patch("common.MAX_SNAPSHOT_BYTES", 10), self.assertRaises(DataError):
            read_artifacts(self.output, self.root)
        snapshot = read_json(self.output / "benchmarks/scores-v2.json")
        snapshot["scores"].append(copy.deepcopy(snapshot["scores"][0]))
        with self.assertRaisesRegex(DataError, "duplicate score"):
            validate_snapshot(snapshot, self.root)

    def test_score_count_limit_and_legacy_contract_are_rejected(self):
        build(self.root, self.output, 2)
        snapshot = read_json(self.output / "benchmarks/scores-v2.json")
        snapshot["scores"] *= 100001
        with self.assertRaises(DataError):
            validate_snapshot(snapshot, self.root)
        for data, schema in (({"schemaVersion": 1, "results": []}, "snapshot-v1.schema.json"),
                             ({"schemaVersion": 1, "dataVersion": 1, "scores": {}}, "manifest-v1.schema.json")):
            with self.subTest(schema=schema), self.assertRaises(DataError):
                validate_schema(data, schema, self.root)

    def test_snapshot_test_source_cannot_be_published(self):
        build(self.root, self.output, 2)
        snapshot = read_json(self.output / "benchmarks/scores-v2.json")
        snapshot["scores"][0]["sourceType"] = "test"
        with self.assertRaises(DataError):
            validate_snapshot(snapshot, self.root)

    def test_protocol_versions_must_be_integer_tokens_not_decimal_or_boolean(self):
        for key in ("schemaVersion", "version"):
            for value in (True, 1.0):
                with self.subTest(key=key, value=value), self.assertRaises(DataError):
                    validate_snapshot({"schemaVersion": 1, "version": 1, "scores": [], key: value}, self.root)

    def test_cost_preserves_missing_null_zero_and_finite_values_through_build(self):
        missing = object()
        for index, value in enumerate((missing, None, 0, 0.003, -0.003)):
            with self.subTest(value="missing" if value is missing else value):
                self.result.pop("cost", None)
                if value is not missing:
                    self.result["cost"] = value
                self.save()
                output = self.output / str(index)
                build(self.root, output, 2, release=True)
                _, snapshot = read_artifacts(output, self.root)
                expected = None if value is missing else value
                self.assertEqual(expected, snapshot["scores"][0]["cost"])

    def test_cost_rejects_non_numeric_types_in_maintenance_and_snapshot(self):
        build(self.root, self.output, 2)
        snapshot = read_json(self.output / "benchmarks/scores-v2.json")
        for value in (True, False, "0.003", {}, []):
            with self.subTest(value=value):
                self.result["cost"] = value
                self.reject_catalog()
                snapshot["scores"][0]["cost"] = value
                with self.assertRaises(DataError):
                    validate_snapshot(snapshot, self.root)

    def test_cost_rejects_non_finite_json_in_maintenance_and_snapshot(self):
        build(self.root, self.output, 2)
        snapshot = read_json(self.output / "benchmarks/scores-v2.json")
        self.result["cost"] = "COST_TOKEN"
        snapshot["scores"][0]["cost"] = "COST_TOKEN"
        for token in ("NaN", "Infinity", "-Infinity", "1e9999"):
            with self.subTest(token=token):
                path = self.root / "data/results/synthetic-bench.json"
                path.write_text(json.dumps(self.documents["results/synthetic-bench.json"]).replace('"COST_TOKEN"', token), encoding="utf-8")
                with self.assertRaises(DataError):
                    load_catalog(self.root)
                # Keep the digest valid so the failure is specifically the cost value.
                content = json.dumps(snapshot).replace('"COST_TOKEN"', token).encode("utf-8")
                (self.output / "benchmarks/scores-v2.json").write_bytes(content)
                manifest = read_json(self.output / "manifest.json")
                manifest["sha256"] = sha256(content)
                (self.output / "manifest.json").write_bytes(json_bytes(manifest))
                with self.assertRaises(DataError):
                    read_artifacts(self.output, self.root)

    def test_cost_only_change_is_reported_without_rewriting_history(self):
        self.result["cost"] = 0.003
        self.save()
        build(self.root, self.output, 2, release=True)
        original = (self.output / "benchmarks/scores-v2.json").read_bytes()
        self.result["cost"] = 0.004
        self.save()
        corrected = self.directory / "cost-corrected"
        report = build(self.root, corrected, 3, baseline=self.output, release=True)
        self.assertEqual(["synthetic-result"], report["changed"])
        self.assertEqual(original, (corrected / "benchmarks/scores-v2.json").read_bytes())
        _, snapshot = read_artifacts(corrected, self.root)
        self.assertEqual(0.004, snapshot["scores"][0]["cost"])

    def test_legacy_snapshot_without_cost_remains_valid_and_unchanged(self):
        build(self.root, self.output, 2)
        snapshot = read_json(self.output / "benchmarks/scores-v2.json")
        del snapshot["scores"][0]["cost"]
        self.artifacts(self.output, snapshot)
        read_artifacts(self.output, self.root)
        original = (self.output / "benchmarks/scores-v2.json").read_bytes()
        updated = self.directory / "updated"
        build(self.root, updated, 3, baseline=self.output, release=True)
        self.assertEqual(original, (updated / "benchmarks/scores-v2.json").read_bytes())
        _, new_snapshot = read_artifacts(updated, self.root)
        self.assertIsNone(new_snapshot["scores"][0]["cost"])

    def test_android_export_is_exact_includes_license_and_checks_without_writing(self):
        build(self.root, self.output, 2, release=True)
        assets = self.directory / "android-assets"
        export_android(self.output, assets, root=self.root)
        self.assertEqual((self.output / "benchmarks/scores-v2.json").read_bytes(), (assets / "benchmarks.json").read_bytes())
        self.assertEqual((self.output / "third_party/synthetic/LICENSE.txt").read_bytes(), (assets / "third_party/synthetic/LICENSE.txt").read_bytes())
        self.assertEqual(2, read_json(assets / "benchmark-attributions.json")["version"])
        export_android(self.output, assets, check=True, root=self.root)
        (assets / "benchmarks.json").write_bytes(b"changed")
        with self.assertRaisesRegex(DataError, "differs"):
            export_android(self.output, assets, check=True, root=self.root)
        self.assertEqual(b"changed", (assets / "benchmarks.json").read_bytes())

    def test_android_export_refuses_preview_empty_missing_license_and_symlinks(self):
        build(self.root, self.output, 2)
        assets = self.directory / "android-assets"
        with self.assertRaisesRegex(DataError, "release build"):
            export_android(self.output, assets, root=self.root)
        self.assertFalse(assets.exists())
        build(self.root, self.output, 2, release=True)
        assets.mkdir()
        outside = self.directory / "outside.json"
        outside.write_bytes(b"untouched")
        (assets / "benchmarks.json").symlink_to(outside)
        with self.assertRaises(DataError):
            export_android(self.output, assets, root=self.root)
        self.assertEqual(b"untouched", outside.read_bytes())
        (self.output / "third_party/synthetic/LICENSE.txt").unlink()
        with self.assertRaises(DataError):
            export_android(self.output, self.directory / "missing-license", root=self.root)

    def test_release_archive_roundtrip_preserves_bytes_and_source_commit(self):
        build(self.root, self.output, 2, release=True)
        archive = self.directory / "site.zip"
        pack(self.output, archive, "a" * 40)
        restored = self.directory / "restored"
        unpack(archive, restored)
        self.assertEqual("a" * 40, (restored / "source-commit.txt").read_text().strip())
        for path in self.output.rglob("*"):
            if path.is_file():
                self.assertEqual(path.read_bytes(), (restored / path.relative_to(self.output)).read_bytes())
        with self.assertRaises(DataError):
            unpack(archive, restored)

    def test_release_archive_rejects_path_traversal_before_writing(self):
        from zipfile import ZipFile
        archive = self.directory / "unsafe.zip"
        with ZipFile(archive, "w") as output:
            output.writestr("../escape", "bad")
        restored = self.directory / "restored"
        with self.assertRaisesRegex(DataError, "unsafe"):
            unpack(archive, restored)
        self.assertFalse(restored.exists())

    def test_remote_smoke_check_consumes_release_bytes_and_rejects_bad_hash_and_version(self):
        build(self.root, self.output, 2, release=True)
        manifest = read_json(self.output / "manifest.json")
        snapshot = (self.output / "benchmarks/scores-v2.json").read_bytes()
        manifest_url = "https://chenlongapps.github.io/model-atlas-data/manifest.json"
        def fetch(url, limit):
            return json_bytes(manifest) if url == manifest_url else snapshot
        self.assertEqual(1, verify_remote(manifest_url, 2, fetch))
        with self.assertRaisesRegex(DataError, "version"):
            verify_remote(manifest_url, 3, fetch)
        manifest["sha256"] = "0" * 64
        with self.assertRaisesRegex(DataError, "SHA-256"):
            verify_remote(manifest_url, 2, fetch)


class RepositoryTest(unittest.TestCase):
    def test_repository_catalog_and_bootstrap_validate(self):
        catalog = load_catalog()
        self.assertEqual(len(catalog.results), catalog.summary()["results"])
        manifest, snapshot = read_artifacts(ROOT)
        self.assertEqual(manifest["version"], snapshot["version"])

    def test_cli_paths_do_not_depend_on_working_directory(self):
        with tempfile.TemporaryDirectory(prefix="model-atlas-cli-test-") as directory:
            output = Path(directory) / "preview"
            for command in (
                ["scripts/validate.py"],
                ["scripts/build.py", "--version", "2", "--output", str(output)],
                ["scripts/validate.py", "--artifacts", str(output)],
            ):
                result = subprocess.run([sys.executable, str(ROOT / command[0]), *command[1:]], cwd=directory, capture_output=True, text=True)
                self.assertEqual(0, result.returncode, result.stderr)


if __name__ == "__main__":
    unittest.main()
