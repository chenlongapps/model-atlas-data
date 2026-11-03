"""Generate a release manifest for an already built Pages output directory."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parent.parent
SOURCE_PATHS = ("models", "benchmarks", "i18n", "scripts/build.py",
                "scripts/manifest.py", "LICENSE.models-dev")


def git(root, *args):
    try:
        result = subprocess.run(["git", *args], cwd=root, check=True, capture_output=True, text=True)
    except (OSError, subprocess.CalledProcessError) as error:
        raise ValueError(f"Git command failed: {error}") from error
    return result.stdout.strip()


def source_commit(root):
    top = Path(git(root, "rev-parse", "--show-toplevel")).resolve()
    if top != root.resolve():
        raise ValueError(f"{root}: expected the Git repository root")
    commit = git(root, "rev-parse", "--verify", "HEAD^{commit}")
    if not re.fullmatch(r"[0-9a-f]{40}|[0-9a-f]{64}", commit):
        raise ValueError("Git returned an invalid commit ID")
    if git(root, "status", "--porcelain", "--untracked-files=all", "--", *SOURCE_PATHS):
        raise ValueError("release sources have uncommitted changes; commit them before generating a manifest")
    return commit


def create_manifest(root, output):
    commit = source_commit(root)
    if output.is_symlink() or not output.is_dir():
        raise ValueError(f"{output}: expected a non-symlink directory")
    locales = root / "i18n"
    if locales.is_symlink() or (locales.exists() and not locales.is_dir()):
        raise ValueError(f"{locales}: expected a non-symlink directory")
    paths = {"models.json", "benchmarks.json", "LICENSE.models-dev"}
    paths.update(f"i18n/{path.stem}.json" for path in locales.glob("*.toml"))
    locale_output = output / "i18n"
    if locale_output.is_symlink() or (locale_output.exists() and not locale_output.is_dir()):
        raise ValueError(f"{locale_output}: expected a non-symlink directory")
    actual_json = {p.relative_to(output).as_posix() for p in output.rglob("*.json")
                   if p.relative_to(output).as_posix() != "manifest.json"}
    expected_json = paths - {"LICENSE.models-dev"}
    if actual_json != expected_json:
        raise ValueError(f"JSON files do not match expected outputs: missing={sorted(expected_json - actual_json)}, "
                         f"unexpected={sorted(actual_json - expected_json)}")
    files = {}
    for name in sorted(paths):
        path = output / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"{path}: expected a non-symlink file")
        content = path.read_bytes()
        if name == "LICENSE.models-dev" and content != (root / name).read_bytes():
            raise ValueError(f"{path}: license does not match the source repository")
        files[name] = {"sha256": hashlib.sha256(content).hexdigest(), "size": len(content)}
    # Hash the exact canonical UTF-8 JSON representation of the files object.
    canonical = json.dumps(files, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    manifest = {
        "schema_version": 1,
        "data_version": "sha256:" + hashlib.sha256(canonical).hexdigest(),
        "published_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "git_commit": commit,
        "files": files,
    }
    destination = output / "manifest.json"
    if destination.is_symlink() or (destination.exists() and not destination.is_file()):
        raise ValueError(f"{destination}: expected a non-symlink file")
    serialized = json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    with tempfile.TemporaryDirectory(prefix=".manifest-", dir=output.parent) as staging:
        temporary = Path(staging) / "manifest.json"
        temporary.write_text(serialized, encoding="utf-8", newline="\n")
        temporary.replace(destination)
    return manifest


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="source Git repository")
    parser.add_argument("--output", type=Path, help="built release directory (default: <root>/dist)")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    output = args.output or root / "dist"
    try:
        manifest = create_manifest(root, output)
    except (OSError, ValueError) as error:
        print(f"Manifest generation failed: {error}", file=sys.stderr)
        return 1
    print(f"Generated {output / 'manifest.json'} ({manifest['data_version']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
