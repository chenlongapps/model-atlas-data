from contextlib import redirect_stdout
from copy import deepcopy
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import tomllib
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "download_artificial_analysis_scores.py"
SPEC = importlib.util.spec_from_file_location("aa_downloader", SCRIPT)
aa = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(aa)


def model(**fields):
    return {
        "name": "Example",
        "deprecated": False,
        "price1mInputTokens": 1,
        "price1mOutputTokens": 2,
        "headline": None,
        "intelligenceIndex": 42.12345678901234,
        **fields,
    }


class DownloaderTests(unittest.TestCase):
    def test_manifest_order_extra_fields_escaping_and_duplicates(self):
        key = "AB" * 32
        entry = {"manifest": {"key": key, "extra": {"note": 'a "quote"'},
                              "path": "/data/file?x=1&y=2"}}
        raw = json.dumps(entry)
        html = "<script>" + raw + "</script>"
        for depth in range(5):
            with self.subTest(depth=depth):
                self.assertEqual(aa.find_manifest_entries(html + html),
                                 [("/data/file?x=1&y=2", key.lower())])
            html = json.dumps(html)

    def test_invalid_manifest_is_not_used(self):
        for entry in ({"path": "/data", "key": "bad"},
                      {"path": "", "key": "a" * 64}):
            with self.subTest(entry=entry), self.assertRaisesRegex(ValueError, "没有找到"):
                aa.find_manifest_entries(json.dumps({"manifest": entry}))

    def test_dataset_requires_target_fields_but_allows_missing_scores(self):
        missing_score = model()
        del missing_score["intelligenceIndex"]
        self.assertTrue(aa.is_model_dataset({"models": [model(intelligenceIndex=None), missing_score]}))
        self.assertFalse(aa.is_model_dataset({"models": [missing_score]}))
        missing_name = model()
        del missing_name["name"]
        self.assertFalse(aa.is_model_dataset({"models": [missing_name]}))
        self.assertFalse(aa.is_model_dataset({"models": []}))

    def test_different_candidates_are_ambiguous_regardless_of_size_or_order(self):
        first = {"url": "https://example.com/a", "data": {"models": [model()]}}
        for other in (model(intelligenceIndex=43), model(name="Other")):
            for records in ([other], [model(), other]):
                second = {"url": "https://example.com/b", "data": {"models": records}}
                for candidates in ([first, second], [second, first]):
                    with self.subTest(records=records), self.assertRaisesRegex(ValueError, "歧义"):
                        aa.select_dataset(candidates)

    def test_identical_candidates_retain_all_source_urls(self):
        data = {"models": [model()]}
        selected, urls = aa.select_dataset([
            {"data": data, "url": "https://example.com/a"},
            {"data": deepcopy(data), "url": "https://example.com/b"},
        ])
        self.assertEqual(selected, data)
        self.assertEqual(urls, ["https://example.com/a", "https://example.com/b"])
        with self.assertRaises(RuntimeError):
            aa.select_dataset([])

    def test_invalid_numbers_fail_with_model_and_field(self):
        for value in (True, False, "42", float("nan"), float("inf"), -float("inf")):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, r"Example.*intelligenceIndex"):
                    aa.simplify_dataset({"models": [model(intelligenceIndex=value)]})
                with self.assertRaisesRegex(ValueError, r"Example.*cost.total"):
                    aa.simplify_dataset({"models": [model(
                        intelligenceIndexCostPerTask={"cost": {"total": value}})]})
        with self.assertRaisesRegex(ValueError, "成本不能为负数"):
            aa.simplify_dataset({"models": [model(
                intelligenceIndexCostPerTask={"cost": {"total": -1}})]})

    def test_malformed_cost_objects_are_not_silent_missing_values(self):
        for value in ("bad", {"cost": False}):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "必须是对象"):
                aa.simplify_dataset({"models": [model(intelligenceIndexCostPerTask=value)]})

    def test_only_weighted_task_total_is_exported(self):
        record = model(
            intelligenceIndexCost={"total": 123},
            costPerTask={"total": 456},
            intelligenceIndexCostPerTask={"cost": {"total": 0.1234567890123456}},
        )
        result = aa.simplify_dataset({"models": [record]})["models"][0]
        self.assertEqual(result["cost"], 0.1234567890123456)
        del record["intelligenceIndexCostPerTask"]
        self.assertIsNone(aa.simplify_dataset({"models": [record]})["models"][0]["cost"])

    def test_invalid_names_dates_and_slugs_have_clear_errors(self):
        for field, values in (("name", (None, "", True)),
                              ("releaseDate", (123, "", "2026-02-30", "yesterday")),
                              ("slug", (False, ""))):
            for value in values:
                with self.subTest(field=field, value=value), self.assertRaisesRegex(ValueError, field):
                    aa.simplify_dataset({"models": [model(**{field: value})]})

    def test_sorting_and_roundtrip_preserve_zero_missing_and_precision(self):
        data = aa.simplify_dataset({"models": [
            model(name="Missing", intelligenceIndex=None),
            model(name="Older", releaseDate="2026-01-01", slug="actual-slug"),
            model(name="Zero", releaseDate="2026-11-01T00:00:00Z", intelligenceIndex=0,
                  intelligenceIndexCostPerTask={"cost": {"total": 0}}),
        ]})
        parsed = tomllib.loads(aa.serialize_toml(data).decode())
        zero, older, missing = parsed["models"]
        self.assertEqual([item["name"] for item in parsed["models"]], ["Zero", "Older", "Missing"])
        self.assertEqual((zero["intelligenceIndex"], zero["cost"]), (0, 0))
        self.assertEqual(older["intelligenceIndex"], 42.12345678901234)
        self.assertEqual(older["slug"], "actual-slug")
        self.assertNotIn("cost", older)
        self.assertNotIn("slug", zero)
        self.assertNotIn("intelligenceIndex", missing)
        self.assertEqual(aa.summarize(parsed["models"]),
                         {"models": 3, "scores": 2, "costs_missing": 2, "costs_zero": 1})

    def test_save_preserves_existing_file_unless_forced(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "snapshot.toml"
            self.assertEqual(aa.save_output(target, b"first", False), target)
            second = aa.save_output(target, b"second", False)
            third = aa.save_output(target, b"third", False)
            self.assertEqual(second.name, "snapshot-2.toml")
            self.assertEqual(third.name, "snapshot-3.toml")
            self.assertEqual(target.read_bytes(), b"first")
            self.assertEqual(second.read_bytes(), b"second")
            aa.save_output(target, b"replacement", True)
            self.assertEqual(target.read_bytes(), b"replacement")

    def test_dependency_error_identifies_interpreter_and_venv(self):
        with patch.object(aa, "AESGCM", None), patch.object(aa.sys, "argv", ["download"]), \
                self.assertRaises(RuntimeError) as caught:
            aa.main()
        self.assertIn(aa.sys.executable, str(caught.exception))
        self.assertIn("临时虚拟环境", str(caught.exception))
        self.assertNotIn("python3 -m pip install", str(caught.exception))

    def test_offline_download_decrypts_and_saves_provenance_and_digest(self):
        key = bytes.fromhex("ab" * 32)
        iv = hashlib.sha256(key).digest()[:12]
        encrypted = aa.AESGCM(key).encrypt(iv, gzip.compress(json.dumps({
            "models": [model(slug="provided-slug")],
        }).encode()), None)
        page = json.dumps({"manifest": {"key": key.hex(), "path": "/fixture"}}).encode()
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "snapshot.toml"
            stdout = io.StringIO()
            with patch.object(aa.sys, "argv", ["download", "--out", str(target)]), \
                    patch.object(aa, "fetch_buffer", side_effect=[page, encrypted]), \
                    redirect_stdout(stdout):
                aa.main()
            output = target.read_bytes()
            parsed = tomllib.loads(output.decode())
            self.assertEqual(parsed["models"][0]["slug"], "provided-slug")
            self.assertEqual(parsed["snapshot"]["format_version"], 1)
            self.assertEqual(parsed["snapshot"]["manifest_urls"], ["https://artificialanalysis.ai/fixture"])
            self.assertEqual(parsed["snapshot"]["page_url"], aa.MODELS_PAGE_URL)
            self.assertEqual(parsed["snapshot"]["cost_unit"], "USD/weighted task")
            self.assertIsNotNone(aa.datetime.fromisoformat(parsed["snapshot"]["downloaded_at"]).tzinfo)
            self.assertIn(hashlib.sha256(output).hexdigest(), stdout.getvalue())
            self.assertIn("成本缺失：1", stdout.getvalue())

    def test_authenticated_decryption_and_decompression_limit(self):
        key = bytes.fromhex("ab" * 32)
        iv = hashlib.sha256(key).digest()[:12]
        encrypted = aa.AESGCM(key).encrypt(iv, gzip.compress(b"12345"), None)
        with self.assertRaisesRegex(ValueError, "认证失败"):
            aa.decrypt_manifest(encrypted[:-1] + bytes([encrypted[-1] ^ 1]), key.hex())
        with patch.object(aa, "MAX_DECOMPRESSED_MANIFEST_BYTES", 4), \
                self.assertRaisesRegex(ValueError, "解压后数据超过"):
            aa.decrypt_manifest(encrypted, key.hex())


if __name__ == "__main__":
    unittest.main()
