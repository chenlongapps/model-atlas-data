from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

from scripts.build import ROOT, main


MODEL = '''schema = 2
name = "Example"
description = "Example model"
open_weights = false
release_date = "2026-10-01"

[modalities]
input = ["text", "image/png"]
output = ["text"]

[capabilities]
tools = { supported = true }
reasoning = { supported = false }
temperature = true

[limit]
context = 128_000
output = 8_192
'''
RESULT = '''
[[benchmarks]]
name = "Example Bench"
score = 42.10
version = "1.0"
metric = "accuracy"
dataset = "full set"
variant = "without tools"
harness = "Example Harness"
source = "https://example.com/results"
date = "2026-10-01"
'''
DEFINITION = '''id = "example-bench"
name = "Example Bench"
version = "1.0"
category = "reasoning"
description = "Example benchmark"
metric = "accuracy"
unit = "percent"
higher_is_better = true
url = "https://example.com/bench"
'''
LOCALE = '''[model.descriptions]
"lab/example" = "模型描述。"
[benchmark.description]
"example-bench" = "评测描述。"
'''


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "repo"
        self.output = self.root / "dist"
        self.write("models/lab/example.toml", MODEL + RESULT)
        self.write("benchmarks/filename-need-not-match-id.toml", DEFINITION)
        self.write("i18n/zh-CN.toml", LOCALE)

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            target.write_bytes(content)
        else:
            target.write_text(content, encoding="utf-8")
        return target

    def run_build(self, *args):
        stdout, stderr = StringIO(), StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = main(["--root", str(self.root), *args])
        return code, stdout.getvalue(), stderr.getvalue()

    def read_json(self, path, output=None):
        return json.loads(((output or self.output) / path).read_text(encoding="utf-8"))

    def assert_failure(self, message):
        # Validation/serialization failures must not replace even one existing artifact.
        old = self.write("dist/models.json", b"old models\n")
        code, stdout, stderr = self.run_build()
        self.assertEqual(code, 1, stderr)
        self.assertEqual(stdout, "")
        self.assertIn(message, stderr)
        self.assertEqual(old.read_bytes(), b"old models\n")
        self.assertFalse((self.output / "benchmarks.json").exists())
        return stderr

    def test_builds_direct_id_maps_and_separate_localization(self):
        code, stdout, stderr = self.run_build()
        self.assertEqual(code, 0, stderr)
        self.assertIn("1 个模型，1 个 Benchmark 定义，1 个语言文件", stdout)
        self.assertEqual(stderr, "")
        model = tomllib.loads(MODEL + RESULT)
        self.assertEqual(self.read_json("models.json"), {"lab/example": model})
        definition = tomllib.loads(DEFINITION)
        del definition["id"]
        self.assertEqual(self.read_json("benchmarks.json"), {"example-bench": definition})
        self.assertEqual(self.read_json("i18n/zh-CN.json"), tomllib.loads(LOCALE))
        raw = (self.output / "i18n/zh-CN.json").read_bytes()
        self.assertIn("模型描述。".encode(), raw)
        self.assertTrue(raw.endswith(b"\n"))
        self.assertNotIn(b"\r", raw)

    def test_preserves_all_result_conditions_order_unknown_fields_and_missing_values(self):
        content = MODEL.replace('name = "Example"', 'name = "Example"\nfuture_field = { enabled = true }')
        content += RESULT + RESULT.replace("42.10", "39.125").replace("without tools", "with tools")
        self.write("models/lab/example.toml", content)
        self.assertEqual(self.run_build()[0], 0)
        model = self.read_json("models.json")["lab/example"]
        self.assertEqual(model, tomllib.loads(content))
        self.assertNotIn("input", model["limit"])
        self.assertNotIn("i18n", model)
        self.assertNotIn("results", self.read_json("benchmarks.json")["example-bench"])

    def test_repeated_build_has_identical_bytes_and_leaves_unrelated_files_alone(self):
        self.write("dist/keep.txt", "not a generated file")
        self.assertEqual(self.run_build()[0], 0)
        before = {p.relative_to(self.output): p.read_bytes() for p in self.output.rglob("*") if p.is_file()}
        self.assertEqual(self.run_build()[0], 0)
        after = {p.relative_to(self.output): p.read_bytes() for p in self.output.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        self.assertEqual(list(self.base.glob(".model-atlas-build-*")), [])
        self.assertEqual(list(self.root.glob(".model-atlas-build-*")), [])

    def test_sorts_map_keys_but_not_source_arrays(self):
        self.write("models/aaa/z.toml", MODEL)
        self.assertEqual(self.run_build()[0], 0)
        self.assertEqual(list(self.read_json("models.json")), ["aaa/z", "lab/example"])
        self.assertEqual(self.read_json("models.json")["lab/example"]["modalities"]["input"],
                         ["text", "image/png"])

    def test_custom_output_and_execution_from_another_directory(self):
        destination = self.base / "custom" / "data"
        result = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/build.py"),
                                 "--root", str(self.root), "--output", str(destination)],
                                cwd=self.base, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("lab/example", self.read_json("models.json", destination))
        self.assertFalse(self.output.exists())

    def test_default_root_is_the_script_repository(self):
        with patch("scripts.build.ROOT", self.root), redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            self.assertEqual(main([]), 0)
        self.assertIn("lab/example", self.read_json("models.json"))

    def test_multiple_language_files_keep_their_source_structure(self):
        self.write("i18n/en.toml", LOCALE.replace("模型描述。", "Model description.")
                   .replace("评测描述。", "Benchmark description."))
        self.assertEqual(self.run_build()[0], 0)
        source = tomllib.loads((self.root / "i18n/en.toml").read_text())
        self.assertEqual(self.read_json("i18n/en.json"), source)
        self.assertEqual(self.read_json("i18n/zh-CN.json"), tomllib.loads(LOCALE))

    def test_reports_all_toml_and_encoding_errors(self):
        self.write("models/lab/broken.toml", "invalid = [")
        self.write("i18n/broken.toml", b'name = "\xff"')
        stderr = self.assert_failure("models/lab/broken.toml:")
        self.assertIn("i18n/broken.toml:", stderr)

    def test_read_error_is_reported_without_writing_output(self):
        with patch.object(Path, "open", side_effect=PermissionError("denied")):
            code, _, stderr = self.run_build()
        self.assertEqual(code, 1)
        self.assertIn("models/lab/example.toml: denied", stderr)
        self.assertFalse(self.output.exists())

    def test_source_directory_cannot_be_a_regular_file(self):
        (self.root / "benchmarks/filename-need-not-match-id.toml").unlink()
        (self.root / "benchmarks").rmdir()
        self.write("benchmarks", "not a directory")
        self.assert_failure("benchmarks/: expected a directory")

    def test_bad_model_path_schema_and_field_types(self):
        for path, content, message in (
            ("models/wrong.toml", MODEL, "expected models/<lab>/<model-id>.toml"),
            ("models/lab/example.toml", MODEL.replace("schema = 2", "schema = true"), "schema = 2"),
            ("models/lab/example.toml", MODEL.replace("open_weights = false", 'open_weights = "false"'), "model.open_weights"),
            ("models/lab/example.toml", MODEL.replace('input = ["text", "image/png"]', 'input = [42]'), "modalities.input"),
            ("models/lab/example.toml", MODEL.replace("context = 128_000", "context = true"), "limit.context"),
        ):
            with self.subTest(message=message):
                target = self.write(path, content)
                self.assert_failure(message)
                if path != "models/lab/example.toml":
                    target.unlink()
                self.write("models/lab/example.toml", MODEL + RESULT)

    def test_no_models_is_an_error(self):
        (self.root / "models/lab/example.toml").unlink()
        self.assert_failure("未找到有效模型")

    def test_duplicate_or_conflicting_results_are_not_silently_merged(self):
        for extra in (RESULT, RESULT.replace("42.10", "99.0")):
            with self.subTest(extra=extra):
                self.write("models/lab/example.toml", MODEL + RESULT + extra)
                self.assert_failure("duplicate or conflicting benchmark record")

    def test_result_required_fields_types_and_source_url(self):
        for old, new, message in (
            ('name = "Example Bench"', '', '.name: required'),
            ('score = 42.10', '', '.score:'),
            ('score = 42.10', 'score = true', '.score:'),
            ('metric = "accuracy"', 'metric = 42', '.metric:'),
            ('https://example.com/results', 'file:///results', '.source:'),
        ):
            with self.subTest(message=message):
                self.write("models/lab/example.toml", MODEL + RESULT.replace(old, new))
                self.assert_failure(message)

    def test_string_scores_are_preserved(self):
        self.write("models/lab/example.toml", MODEL + RESULT.replace("42.10", '"42.1 ± 0.2"'))
        self.assertEqual(self.run_build()[0], 0)
        self.assertEqual(self.read_json("models.json")["lab/example"]["benchmarks"][0]["score"], "42.1 ± 0.2")

    def test_invalid_or_duplicate_definitions_fail(self):
        path = "benchmarks/filename-need-not-match-id.toml"
        for old, new, message in (
            ('metric = "accuracy"', '', 'metric: required'),
            ('higher_is_better = true', 'higher_is_better = "true"', 'higher_is_better:'),
            ('id = "example-bench"', 'id = "../unsafe"', 'id: invalid'),
        ):
            with self.subTest(message=message):
                self.write(path, DEFINITION.replace(old, new))
                self.assert_failure(message)
        self.write(path, DEFINITION)
        self.write("benchmarks/duplicate.toml", DEFINITION)
        self.assert_failure("duplicate Benchmark ID")

    def test_unmatched_and_ambiguous_mappings_warn_and_preserve_results(self):
        content = MODEL + RESULT.replace('version = "1.0"\n', '')
        self.write("models/lab/example.toml", content)
        code, _, stderr = self.run_build()
        self.assertEqual(code, 0, stderr)
        self.assertIn("未匹配 1 条，歧义 0 条", stderr)
        result = self.read_json("models.json")["lab/example"]["benchmarks"][0]
        self.assertNotIn("version", result)
        self.assertEqual(result, tomllib.loads(content)["benchmarks"][0])
        self.write("models/lab/example.toml", MODEL + RESULT)
        self.write("benchmarks/other.toml", DEFINITION.replace('id = "example-bench"', 'id = "other"'))
        code, _, stderr = self.run_build()
        self.assertEqual(code, 0, stderr)
        self.assertIn("未匹配 0 条，歧义 1 条", stderr)

    def test_absent_optional_source_and_translation_warn_without_filling(self):
        self.write("models/lab/example.toml", MODEL + RESULT.replace('source = "https://example.com/results"\n', ''))
        self.write("i18n/zh-CN.toml", "[model.descriptions]\n[benchmark.description]\n")
        code, _, stderr = self.run_build()
        self.assertEqual(code, 0, stderr)
        self.assertIn("1 条成绩未提供 source", stderr)
        self.assertIn("缺少 1 个 model 描述翻译", stderr)
        self.assertIn("缺少 1 个 benchmark 描述翻译", stderr)
        self.assertEqual(self.read_json("i18n/zh-CN.json"), {"model": {"descriptions": {}}, "benchmark": {"description": {}}})

    def test_invalid_localization_shape_values_or_dangling_keys_fail(self):
        for content, message in (
            ('model = "wrong"', 'expected dict'),
            ('[model]\ndescriptions = []', 'expected dict'),
            (LOCALE.replace('"lab/example"', '"lab/missing"'), 'unknown ID lab/missing'),
            (LOCALE.replace('"example-bench"', '"missing"'), 'unknown ID missing'),
            (LOCALE.replace('"模型描述。"', '42'), 'expected a nonempty string'),
        ):
            with self.subTest(message=message):
                self.write("i18n/zh-CN.toml", content)
                self.assert_failure(message)

    def test_non_json_toml_values_fail_before_writes(self):
        for value in ("nan", "inf", "-inf", "2026-10-01", "12:30:00"):
            with self.subTest(value=value):
                content = MODEL.replace('name = "Example"', f'name = "Example"\nfuture = {value}') + RESULT
                self.write("models/lab/example.toml", content)
                self.assert_failure("models.json: JSON serialization failed")

    def test_optional_directories_can_be_absent(self):
        (self.root / "benchmarks/filename-need-not-match-id.toml").unlink()
        (self.root / "benchmarks").rmdir()
        (self.root / "i18n/zh-CN.toml").unlink()
        (self.root / "i18n").rmdir()
        code, _, stderr = self.run_build()
        self.assertEqual(code, 0, stderr)
        self.assertEqual(self.read_json("benchmarks.json"), {})
        self.assertFalse((self.output / "i18n").exists())

    def test_stale_locale_requires_manual_removal(self):
        stale = self.write("dist/i18n/removed.json", "old translation")
        self.assert_failure("无对应语言源文件")
        self.assertEqual(stale.read_text(), "old translation")

    def test_invalid_output_directory_shape_fails_before_replacements(self):
        self.write("dist/i18n", "not a directory")
        self.assert_failure("expected a directory")

    def test_symlinked_input_or_output_is_rejected_without_overwriting_target(self):
        source = self.root / "models/lab/example.toml"
        source.unlink()
        outside = self.base / "outside.toml"
        outside.write_text(MODEL + RESULT)
        source.symlink_to(outside)
        self.assert_failure("symlink not allowed")
        source.unlink()
        self.write("models/lab/example.toml", MODEL + RESULT)
        (self.output / "models.json").unlink()
        (self.output / "models.json").symlink_to(outside)
        code, _, stderr = self.run_build()
        self.assertEqual(code, 1)
        self.assertIn("symlink not allowed", stderr)
        self.assertEqual(outside.read_text(), MODEL + RESULT)

    def test_staging_write_failure_leaves_existing_outputs_untouched(self):
        old = self.write("dist/models.json", "old models")
        with patch.object(Path, "write_text", side_effect=OSError("disk full")):
            code, _, stderr = self.run_build()
        self.assertEqual(code, 1)
        self.assertIn("disk full", stderr)
        self.assertEqual(old.read_text(), "old models")
        self.assertFalse((self.output / "benchmarks.json").exists())
        self.assertEqual(list(self.root.glob(".model-atlas-build-*")), [])


if __name__ == "__main__":
    unittest.main()
