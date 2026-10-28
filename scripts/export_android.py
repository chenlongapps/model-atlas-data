"""Export one validated release as Android assets; --check never writes files."""

import argparse
from pathlib import Path
import sys

from common import DataError, ROOT, json_bytes, license_path, read_artifacts, read_json, require


def android_files(artifacts: Path, root: Path = ROOT) -> dict[str, bytes]:
    manifest, snapshot = read_artifacts(artifacts, root)
    report = read_json(artifacts / "report.json")
    require(report.get("mode") == "release" and report.get("version") == manifest["version"],
            "Android export requires a release build, not a preview/bootstrap")
    require(bool(snapshot["scores"]), "Android export refuses empty scores")
    attribution_path = artifacts / f"attributions/v{manifest['version']}.json"
    attributions = read_json(attribution_path)
    require(attributions.get("version") == manifest["version"] and bool(attributions.get("sources")),
            "missing or mismatched release attributions")
    files = {
        "benchmarks.json": (artifacts / f"benchmarks/scores-v{manifest['version']}.json").read_bytes(),
        "benchmark-manifest.json": json_bytes(manifest),
        "benchmark-attributions.json": json_bytes(attributions),
    }
    for source in attributions["sources"]:
        relative = source["license"]["licenseFile"]
        files[relative] = license_path(artifacts, relative).read_bytes()
    return files


def export_android(artifacts: Path, output: Path, check: bool = False, root: Path = ROOT) -> None:
    files = android_files(artifacts, root)
    output = output.resolve()
    require(not root.resolve().is_relative_to(output), "output cannot be the repository or its ancestor")
    require(not output.is_relative_to(root.resolve()) or output.is_relative_to(root.resolve() / "build"),
            "repository output must be under build/")
    # Validate every target before the first write. Never remove unrelated assets.
    for relative, content in files.items():
        target = output / relative
        require(not target.is_symlink() and target.resolve().is_relative_to(output), "asset symlink/escape forbidden")
        if check:
            require(target.is_file() and target.read_bytes() == content, f"Android asset differs: {target}")
    if not check:
        for relative, content in files.items():
            target = output / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_name(target.name + ".export-tmp")
            with temporary.open("xb") as handle:
                handle.write(content)
            temporary.replace(target)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifacts", type=Path, required=True)
    parser.add_argument("--output", type=Path, default=ROOT / "build/android-assets")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        export_android(args.artifacts, args.output, args.check)
        print(f"OK: Android assets {'match' if args.check else 'exported to'} {args.output}")
        return 0
    except (DataError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
