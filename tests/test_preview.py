from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts import preview


class PreviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        model = self.root / "models/lab/example.toml"
        model.parent.mkdir(parents=True)
        model.write_text('schema = 2\nname = "Example"\n', encoding="utf-8")
        (self.root / "web").mkdir()
        (self.root / "web/index.html").write_text("preview", encoding="utf-8")
        (self.root / "LICENSE.models-dev").write_text("license", encoding="utf-8")

    def run_preview(self, *args):
        stdout, stderr = StringIO(), StringIO()
        with patch.object(preview, "ROOT", self.root), redirect_stdout(stdout), redirect_stderr(stderr):
            result = preview.main(list(args))
        return result, stdout.getvalue(), stderr.getvalue()

    def test_builds_and_serves_temporary_directory_then_cleans_up(self):
        test = self
        paths = []

        class Server:
            def __init__(self, address, handler):
                test.assertEqual(address, ("127.0.0.1", 0))
                self.server_port = 43210
                self.output = Path(handler.keywords["directory"])
                paths.append(self.output)

            def __enter__(self):
                return self

            def __exit__(self, *args):
                pass

            def serve_forever(self):
                test.assertEqual((self.output / "index.html").read_text(), "preview")
                test.assertEqual((self.output / "LICENSE.models-dev").read_text(), "license")
                models = json.loads((self.output / "models.json").read_text())
                test.assertEqual(models["lab/example"]["name"], "Example")
                test.assertTrue((self.output / "benchmarks.json").is_file())
                test.assertFalse((self.output / "manifest.json").exists())
                test.assertFalse((self.output / "models").exists())
                raise KeyboardInterrupt

        with patch.object(preview, "ThreadingHTTPServer", Server):
            code, stdout, stderr = self.run_preview("--port", "0")
        self.assertEqual(code, 0, stderr)
        self.assertIn("http://127.0.0.1:43210/", stdout)
        self.assertIn("预览已停止", stdout)
        self.assertEqual(len(paths), 1)
        self.assertFalse(paths[0].exists())

    def test_build_failure_does_not_start_server(self):
        (self.root / "models/lab/example.toml").write_text("invalid = [", encoding="utf-8")
        with patch.object(preview, "ThreadingHTTPServer") as server:
            code, stdout, stderr = self.run_preview()
        self.assertEqual(code, 1)
        self.assertIn("预览失败", stderr)
        server.assert_not_called()

    def test_server_failure_reports_error_and_cleans_up(self):
        paths = []

        def fail(address, handler):
            paths.append(Path(handler.keywords["directory"]))
            raise OSError("address in use")

        with patch.object(preview, "ThreadingHTTPServer", side_effect=fail):
            code, stdout, stderr = self.run_preview()
        self.assertEqual(code, 1)
        self.assertIn("address in use", stderr)
        self.assertFalse(paths[0].exists())

    def test_rejects_invalid_ports(self):
        for port in ("-1", "65536", "abc"):
            with self.subTest(port=port), redirect_stderr(StringIO()):
                with self.assertRaises(SystemExit) as error:
                    self.run_preview("--port", port)
                self.assertEqual(error.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
