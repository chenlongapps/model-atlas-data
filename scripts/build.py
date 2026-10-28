"""Build an offline, deterministic full snapshot. Preview by default; no deployment."""

import argparse
from pathlib import Path
import sys
from urllib.parse import urlsplit

from common import (
    DEFAULT_BASE_URL, DataError, MAX_MANIFEST_BYTES, MAX_SNAPSHOT_BYTES, ROOT,
    https_url, json_bytes, license_path, load_catalog, read_artifacts, read_json,
    require, sha256, validate_schema, validate_snapshot,
)


def build(root: Path, output: Path, version: int, base_url: str = DEFAULT_BASE_URL,
          baseline: Path | None = None, release: bool = False,
          allow_removals: bool = False, reason: str = "") -> dict:
    root, output = root.resolve(), output.resolve()
    baseline = (baseline or root).resolve()
    require(not root.is_relative_to(output), "output must not be the repository or its ancestor")
    require(not output.is_relative_to(root) or output.is_relative_to(root / "build"), "repository output must be under build/, never data/ or benchmarks/")
    require(not output.is_relative_to(baseline) or baseline == root and output.is_relative_to(root / "build"), "output must not overwrite baseline/source directories; use build/ or an external directory")
    require(not baseline.is_relative_to(output), "output must not contain the baseline")
    base_url = base_url.rstrip("/")
    https_url(base_url)
    parsed_base = urlsplit(base_url)
    require(not parsed_base.query and not parsed_base.fragment, "base URL cannot contain query or fragment")
    require(not any(part in (".", "..") for part in parsed_base.path.split("/")), "base URL cannot contain traversal segments")
    catalog = load_catalog(root)
    old_manifest, old_snapshot = read_artifacts(baseline, root)
    require(type(version) is int and old_manifest["version"] < version <= 9223372036854775807, "version must be a positive Long greater than baseline version")

    scores = []
    used_sources = {}
    for result in catalog.publishable():
        benchmark = catalog.benchmarks[result["benchmarkId"]]
        source = catalog.sources[result["sourceId"]]
        mapping = catalog.mappings[result["mappingId"]]
        scores.append({
            "id": result["id"], "modelId": mapping["modelId"],
            "benchmarkId": benchmark["id"], "score": result["score"],
            "cost": result.get("cost"),
            "metric": benchmark["metric"], "unit": benchmark["unit"],
            "higherIsBetter": benchmark["higherIsBetter"],
            **{key: result[key] for key in ("subset", "harness", "reasoningEffort", "toolsEnabled", "evaluatedAt")},
            "sourceUrl": source["url"], "sourceType": source["sourceType"],
        })
        used_sources[source["id"]] = source

    snapshot = {"schemaVersion": 1, "version": version, "scores": scores}
    validate_snapshot(snapshot, root)
    snapshot_bytes = json_bytes(snapshot)
    require(len(snapshot_bytes) <= MAX_SNAPSHOT_BYTES, "snapshot exceeds Android byte limit")
    before = {score["id"]: score for score in old_snapshot["scores"]}
    after = {score["id"]: score for score in scores}
    removed = sorted(before.keys() - after.keys())
    report = {
        "mode": "release" if release else "preview",
        "baselineVersion": old_manifest["version"], "version": version,
        "sourceSummary": catalog.summary(),
        "scoreCount": len(scores),
        "added": sorted(after.keys() - before.keys()), "removed": removed,
        "changed": sorted(key for key in before.keys() & after.keys() if before[key] != after[key]),
        "reviewReason": reason,
    }
    if release:
        require(bool(scores), "release refused: no approved scores; empty snapshots would erase client data")
        require(not removed or allow_removals and bool(reason.strip()), "release removes scores: review report in preview, then use --allow-removals --reason")

    manifest = {
        "schemaVersion": 1, "version": version,
        "url": f"{base_url}/benchmarks/scores-v{version}.json", "sha256": sha256(snapshot_bytes),
    }
    validate_schema(manifest, "manifest-v1.schema.json", root)
    require(len(json_bytes(manifest)) <= MAX_MANIFEST_BYTES, "manifest exceeds Android byte limit")

    # Preserve all known snapshot bytes, not just the currently selected version.
    files = {}
    for path in sorted((baseline / "benchmarks").glob("scores-v*.json")):
        require(not path.is_symlink(), f"baseline symlink is forbidden: {path}")
        historical = read_json(path, MAX_SNAPSHOT_BYTES)
        validate_snapshot(historical, root)
        require(path.name == f"scores-v{historical['version']}.json", f"historical filename/version mismatch: {path}")
        require(historical["version"] <= old_manifest["version"], f"baseline contains a future snapshot: {path}")
        files[f"benchmarks/{path.name}"] = path.read_bytes()
    files[f"benchmarks/scores-v{version}.json"] = snapshot_bytes

    attributions = []
    for source in sorted(used_sources.values(), key=lambda source: source["id"]):
        license_info = source["license"]
        relative = license_info["licenseFile"]
        files[relative] = license_path(root, relative).read_bytes()
        attributions.append({"sourceId": source["id"], "publisher": source["publisher"], "url": source["url"], "license": license_info})
    files[f"attributions/v{version}.json"] = json_bytes({"version": version, "sources": attributions})
    # Keep historical attribution/license files alongside historical snapshots.
    for directory in ("attributions", "third_party"):
        for path in sorted((baseline / directory).rglob("*")):
            if path.is_file():
                require(not path.is_symlink(), f"baseline symlink is forbidden: {path}")
                relative = path.relative_to(baseline).as_posix()
                if relative in files:
                    require(files[relative] == path.read_bytes(), f"license/attribution changed at immutable path: {relative}")
                files[relative] = path.read_bytes()

    # All policy and immutable-file checks finish before the first write.
    for name in ("manifest.json", "report.json", ".nojekyll", ".manifest.json.tmp", ".report.json.tmp"):
        require(not (output / name).is_symlink(), f"output symlink is forbidden: {output / name}")
    require(not (output / ".manifest.json.tmp").exists() and not (output / ".report.json.tmp").exists(), "stale temporary output: inspect it before retrying")
    if (output / "manifest.json").exists():
        current, _ = read_artifacts(output, root)
        require(current["version"] <= version, "output already has a newer version; use a fresh directory")
    for relative, content in files.items():
        target = output / relative
        require(not target.is_symlink(), f"output symlink is forbidden: {target}")
        require(target.resolve().is_relative_to(output), f"output path escapes directory: {target}")
        if target.exists():
            require(target.read_bytes() == content, f"immutable artifact already exists with different bytes: {target}")
    for relative, content in files.items():
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists():
            with target.open("xb") as handle:
                handle.write(content)
    # The manifest is the last publication pointer. Filesystem failure cannot point to a partial snapshot.
    for name, content in (("report.json", json_bytes(report)), ("manifest.json", json_bytes(manifest))):
        target = output / name
        require(not target.is_symlink(), f"output symlink is forbidden: {target}")
        temporary = output / f".{name}.tmp"
        with temporary.open("xb") as handle:
            handle.write(content)
        temporary.replace(target)
    (output / ".nojekyll").touch()
    read_artifacts(output, root)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", type=int, required=True)
    parser.add_argument("--output", type=Path, help="default: build/preview or build/site")
    parser.add_argument("--baseline", type=Path, default=ROOT, help="last released artifacts; default: repository bootstrap")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--release", action="store_true", help="enforce production data gates; does not deploy")
    parser.add_argument("--allow-removals", action="store_true")
    parser.add_argument("--reason", default="")
    args = parser.parse_args()
    output = args.output or ROOT / "build" / ("site" if args.release else "preview")
    try:
        report = build(ROOT, output, args.version, args.base_url, args.baseline, args.release, args.allow_removals, args.reason)
        print(f"OK: {report['mode']} v{report['version']}, {report['scoreCount']} scores → {output}")
        print(f"Changes: +{len(report['added'])} / ~{len(report['changed'])} / -{len(report['removed'])}; excluded {len(report['sourceSummary']['excludedResults'])}")
        if not args.release:
            print("PREVIEW ONLY: not approved for deployment, even if JSON is valid")
        return 0
    except (DataError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
