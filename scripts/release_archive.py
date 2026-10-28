"""Pack/restore immutable release baselines. Offline; never calls GitHub."""

import argparse
from pathlib import Path, PurePosixPath
import re
import stat
import sys
from zipfile import ZIP_DEFLATED, ZipFile

from common import DataError, read_artifacts, read_json, require


def pack(site: Path, archive: Path, commit: str) -> None:
    manifest, snapshot = read_artifacts(site)
    report = read_json(site / "report.json")
    require(report.get("mode") == "release" and report.get("version") == manifest["version"] and bool(snapshot["scores"]),
            "archive requires nonempty release artifacts")
    require(bool(re.fullmatch(r"[0-9a-f]{40}", commit)), "expected full source commit SHA")
    with ZipFile(archive, "x", compression=ZIP_DEFLATED) as output:
        for path in sorted(site.rglob("*")):
            require(not path.is_symlink(), "release archive forbids symlinks")
            if path.is_file():
                require(path.relative_to(site).as_posix() != "source-commit.txt", "reserved archive metadata")
                output.write(path, path.relative_to(site).as_posix())
        output.writestr("source-commit.txt", commit + "\n")


def unpack(archive: Path, output: Path) -> None:
    require(not output.exists(), "restore requires a fresh output directory")
    with ZipFile(archive) as source:
        entries = source.infolist()
        require(len(entries) == len({entry.filename for entry in entries}), "duplicate archive paths")
        require(sum(entry.file_size for entry in entries) <= 256 * 1024 * 1024, "archive exceeds restore limit")
        for entry in entries:
            path = PurePosixPath(entry.filename)
            require(not path.is_absolute() and ".." not in path.parts and "\\" not in entry.filename,
                    "unsafe archive path")
            require(not stat.S_ISLNK(entry.external_attr >> 16), "archive symlink forbidden")
        source.extractall(output)
    manifest, snapshot = read_artifacts(output)
    report = read_json(output / "report.json")
    require(report.get("mode") == "release" and report.get("version") == manifest["version"] and bool(snapshot["scores"]),
            "restored archive is not a nonempty release")
    require(bool(re.fullmatch(r"[0-9a-f]{40}\n?", (output / "source-commit.txt").read_text())), "invalid source commit")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--pack", type=Path)
    action.add_argument("--unpack", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--commit")
    args = parser.parse_args()
    try:
        if args.pack:
            pack(args.pack, args.output, args.commit or "")
        else:
            unpack(args.unpack, args.output)
        print(f"OK: release archive → {args.output}")
        return 0
    except (DataError, OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
