from contextlib import redirect_stderr, redirect_stdout
import hashlib
from io import StringIO
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from scripts.manifest import create_manifest, main


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        self.output = Path(self.temp.name) / "release"
        self.output.mkdir()
        self.git("init", "-q")
        self.write(self.root / "models/lab/model.toml", b"schema = 2\n")
        self.write(self.root / "i18n/zh-CN.toml", b"# locale\n")
        self.write(self.root / "LICENSE.models-dev", b"license\n")
        self.git("add", ".")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.com",
                 "-c", "commit.gpgsign=false", "commit", "-qm", "fixture")
        self.write(self.output / "models.json", b'{"model": 1}\n')
        self.write(self.output / "benchmarks.json", b'{}\n')
        self.write(self.output / "i18n/zh-CN.json", '"中文"\n'.encode())
        self.write(self.output / "LICENSE.models-dev", b"license\n")

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, capture_output=True,
                              text=True, check=True).stdout.strip()

    def write(self, path, contents):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(contents)

    def test_manifest_contains_exact_files_hashes_and_checked_out_commit(self):
        manifest = create_manifest(self.root, self.output)
        self.assertEqual(manifest, json.loads((self.output / "manifest.json").read_text()))
        self.assertEqual(manifest["schema_version"], 1)
        self.assertEqual(manifest["git_commit"], self.git("rev-parse", "HEAD"))
        self.assertRegex(manifest["published_at"], r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        self.assertEqual(set(manifest["files"]), {"models.json", "benchmarks.json",
                                                   "i18n/zh-CN.json", "LICENSE.models-dev"})
        for name, info in manifest["files"].items():
            contents = (self.output / name).read_bytes()
            self.assertEqual(info, {"sha256": hashlib.sha256(contents).hexdigest(), "size": len(contents)})
        canonical = json.dumps(manifest["files"], sort_keys=True, ensure_ascii=False,
                               separators=(",", ":")).encode("utf-8")
        self.assertEqual(manifest["data_version"], "sha256:" + hashlib.sha256(canonical).hexdigest())

    def test_version_changes_with_content_but_not_commit_or_time(self):
        first = create_manifest(self.root, self.output)
        self.write(self.root / "unrelated.txt", b"new commit")
        self.git("add", "unrelated.txt")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.com",
                 "-c", "commit.gpgsign=false", "commit", "-qm", "unrelated")
        second = create_manifest(self.root, self.output)
        self.assertNotEqual(first["git_commit"], second["git_commit"])
        self.assertEqual(first["data_version"], second["data_version"])
        self.write(self.output / "models.json", b'{"model": 2}\n')
        third = create_manifest(self.root, self.output)
        self.assertNotEqual(first["data_version"], third["data_version"])

    def test_missing_or_extra_output_does_not_replace_manifest(self):
        create_manifest(self.root, self.output)
        before = (self.output / "manifest.json").read_bytes()
        (self.output / "models.json").unlink()
        with self.assertRaisesRegex(ValueError, "missing=.*models.json"):
            create_manifest(self.root, self.output)
        self.assertEqual((self.output / "manifest.json").read_bytes(), before)
        self.write(self.output / "models.json", b"{}\n")
        self.write(self.output / "i18n/stale.json", b"{}\n")
        with self.assertRaisesRegex(ValueError, "unexpected=.*stale.json"):
            create_manifest(self.root, self.output)
        self.assertEqual((self.output / "manifest.json").read_bytes(), before)

    def test_dirty_or_untracked_sources_are_rejected(self):
        self.write(self.root / "models/lab/model.toml", b"changed\n")
        with self.assertRaisesRegex(ValueError, "uncommitted changes"):
            create_manifest(self.root, self.output)
        self.write(self.root / "models/lab/model.toml", b"schema = 2\n")
        self.write(self.root / "models/lab/new.toml", b"new\n")
        with self.assertRaisesRegex(ValueError, "uncommitted changes"):
            create_manifest(self.root, self.output)

    def test_license_mismatch_is_rejected(self):
        self.write(self.output / "LICENSE.models-dev", b"wrong")
        with self.assertRaisesRegex(ValueError, "license does not match"):
            create_manifest(self.root, self.output)

    def test_symlinks_are_rejected(self):
        (self.output / "models.json").unlink()
        (self.output / "models.json").symlink_to(self.output / "benchmarks.json")
        with self.assertRaisesRegex(ValueError, "non-symlink file"):
            create_manifest(self.root, self.output)

    def test_not_git_root_and_cli_failure(self):
        with self.assertRaisesRegex(ValueError, "Git repository root"):
            create_manifest(self.root / "models", self.output)
        stderr = StringIO()
        with redirect_stderr(stderr), redirect_stdout(StringIO()):
            code = main(["--root", str(self.root), "--output", str(self.output / "missing")])
        self.assertEqual(code, 1)
        self.assertIn("Manifest generation failed", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
