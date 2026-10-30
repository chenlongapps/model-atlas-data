from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.validate import main


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)

    def validate(self):
        stdout, stderr = StringIO(), StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            code = main(self.root)
        return code, stdout.getvalue(), stderr.getvalue()

    def test_valid_files_in_all_source_directories(self):
        self.write("models/lab/model.toml", b"schema = 2\n")
        self.write("benchmarks/example.toml", b'name = "Example"\n')
        self.write("i18n/zh-CN.toml", 'description = "中文"\n'.encode())
        self.write("dist/ignored.toml", b"invalid = [")
        self.write("models/ignored.txt", b"invalid = [")

        code, stdout, stderr = self.validate()

        self.assertEqual(code, 0)
        self.assertIn("检查 3 个 TOML 文件：成功 3，失败 0", stdout)
        self.assertEqual(stderr, "")

    def test_reports_all_syntax_errors_and_continues(self):
        self.write("models/lab/invalid.toml", b"valid = 1\nbroken = ]\n")
        self.write("benchmarks/duplicate.toml", b"score = 1\nscore = 2\n")
        self.write("i18n/valid.toml", b"valid = true\n")

        code, stdout, stderr = self.validate()

        self.assertEqual(code, 1)
        self.assertIn("成功 1，失败 2", stdout)
        self.assertIn("models/lab/invalid.toml:", stderr)
        self.assertIn("benchmarks/duplicate.toml:", stderr)
        self.assertIn("line 2", stderr)

    def test_invalid_utf8_is_a_failure(self):
        self.write("i18n/invalid.toml", b'name = "\xff"\n')

        code, stdout, stderr = self.validate()

        self.assertEqual(code, 1)
        self.assertIn("失败 1", stdout)
        self.assertIn("i18n/invalid.toml:", stderr)
        self.assertIn("utf-8", stderr)

    def test_read_error_is_a_failure(self):
        self.write("models/lab/model.toml", b"schema = 2\n")

        with patch.object(Path, "open", side_effect=PermissionError("denied")):
            code, stdout, stderr = self.validate()

        self.assertEqual(code, 1)
        self.assertIn("失败 1", stdout)
        self.assertIn("models/lab/model.toml: denied", stderr)

    def test_no_files_is_a_failure(self):
        code, stdout, stderr = self.validate()

        self.assertEqual(code, 1)
        self.assertEqual(stdout, "")
        self.assertIn("未找到 TOML 文件", stderr)


if __name__ == "__main__":
    unittest.main()
