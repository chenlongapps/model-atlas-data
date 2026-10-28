#!/usr/bin/env python3
"""Build an immutable, full Android-compatible Benchmark release bundle."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

try:
    from .validate import (
        DataError, MAX_MANIFEST_BYTES, MAX_SNAPSHOT_BYTES, MAX_VERSION,
        android_scores, json_bytes, load_data, read_bundle, read_json, require,
        sha256, validate_manifest, validate_snapshot,
    )
except ImportError:
    from validate import (
        DataError, MAX_MANIFEST_BYTES, MAX_SNAPSHOT_BYTES, MAX_VERSION,
        android_scores, json_bytes, load_data, read_bundle, read_json, require,
        sha256, validate_manifest, validate_snapshot,
    )

DEFAULT_BASE_URL = "https://chenlongapps.github.io/model-atlas-data"
VERSION_FILE_RE = re.compile(r"^scores-v([0-9]+)\.json$")
ATTRIBUTION_FILE_RE = re.compile(r"^v([0-9]+)\.json$")


def safe_relative_path(value: str) -> Path:
    path = Path(value)
    require(not path.is_absolute() and ".." not in path.parts and "\\" not in value,
            f"unsafe artifact path: {value}")
    require(path.parts and path.parts[0] in {"third_party"},
            f"license path must stay under third_party/: {value}")
    return path


def read_attributions(path: Path, expected_version: int) -> dict:
    document = read_json(path, MAX_MANIFEST_BYTES)
    require(isinstance(document, dict) and document.get("version") == expected_version,
            f"{path}: attribution version mismatch")
    require(isinstance(document.get("sources"), list), f"{path}: sources must be an array")
    for source in document["sources"]:
        require(isinstance(source, dict), f"{path}: source attribution must be an object")
        require(all(key in source for key in ("sourceId", "publisher", "url", "license")),
                f"{path}: source attribution is incomplete")
        require(isinstance(source["sourceId"], str) and isinstance(source["publisher"], str),
                f"{path}: invalid source identity")
        require(isinstance(source["url"], str) and isinstance(source["license"], dict),
                f"{path}: invalid source URL or license")
    return document


def baseline_files(baseline: Path) -> tuple[dict, dict, dict[int, bytes], dict[int, bytes], dict[str, bytes]]:
    manifest, current, _ = read_bundle(baseline)
    latest = manifest["version"]
    snapshots: dict[int, bytes] = {}
    attributions: dict[int, bytes] = {}
    licenses: dict[str, bytes] = {}

    for path in sorted((baseline / "benchmarks").glob("scores-v*.json")):
        require(not path.is_symlink(), f"baseline symlink is forbidden: {path}")
        match = VERSION_FILE_RE.fullmatch(path.name)
        require(match is not None, f"invalid historical snapshot filename: {path.name}")
        version = int(match.group(1))
        content = path.read_bytes()
        snapshot = read_json(path, MAX_SNAPSHOT_BYTES)
        validate_snapshot(snapshot)
        require(snapshot["version"] == version, f"snapshot filename/version mismatch: {path.name}")
        require(version <= latest, f"future snapshot in baseline: {path.name}")
        snapshots[version] = content
    require(latest in snapshots, "baseline current snapshot is missing")
    require(set(snapshots) == set(range(2, latest + 1)),
            "baseline must retain every published snapshot from v2 through the current version")

    for path in sorted((baseline / "attributions").glob("v*.json")):
        require(not path.is_symlink(), f"baseline symlink is forbidden: {path}")
        match = ATTRIBUTION_FILE_RE.fullmatch(path.name)
        if match is None:
            continue
        version = int(match.group(1))
        require(version in snapshots, f"attribution has no matching published snapshot: {path.name}")
        content = path.read_bytes()
        read_attributions(path, version)
        attributions[version] = content
    require(set(attributions) == set(snapshots), "baseline must retain each versioned attribution file")

    for content in attributions.values():
        doc = json.loads(content.decode("utf-8"))
        for source in doc["sources"]:
            relative = source["license"].get("licenseFile")
            if relative is None:
                continue
            safe = safe_relative_path(relative)
            license_path = baseline
            for part in safe.parts:
                license_path = license_path / part
                require(not license_path.is_symlink(), f"baseline license symlink is forbidden: {relative}")
            require(license_path.is_file(), f"baseline is missing attributed license {relative}")
            license_bytes = license_path.read_bytes()
            require(bool(license_bytes), f"baseline attributed license is empty: {relative}")
            if relative in licenses:
                require(licenses[relative] == license_bytes, f"historical license changed: {relative}")
            licenses[relative] = license_bytes
    return manifest, current, snapshots, attributions, licenses


def current_android_attributions(root: Path) -> tuple[dict, set[tuple[str, str]], list[dict]]:
    path = root / "attributions/v2.json"
    attrs = read_attributions(path, 2)
    baseline = read_json(root / "benchmarks/scores-v2.json", MAX_SNAPSHOT_BYTES)
    validate_snapshot(baseline)
    require(baseline["version"] == 2, "Android attribution baseline must match bundled v2")
    score_sources = {(score.get("sourceUrl"), score.get("sourceType")) for score in baseline["scores"]}
    return attrs, score_sources, attrs["sources"]


def add_file(files: dict[str, bytes], relative: str, content: bytes) -> None:
    require(relative not in files or files[relative] == content, f"conflicting immutable artifact: {relative}")
    files[relative] = content


def build(root: Path, output: Path, version: int, baseline: Path | None = None,
          base_url: str = DEFAULT_BASE_URL, allow_removals: bool = False, reason: str = "") -> dict:
    root = root.resolve()
    output = Path(output)
    require(not output.is_symlink(), f"output symlink is forbidden: {output}")
    output = output.resolve()
    baseline = (baseline or root).resolve()
    require(type(version) is int and 1 <= version <= MAX_VERSION, "version must be a positive Kotlin Long")
    require(not root.is_relative_to(output), "output cannot be the repository or its ancestor")
    if output.is_relative_to(root):
        require(output.is_relative_to(root / "build"), "repository output must stay under build/")
    require(not output.is_relative_to(baseline) or (baseline == root and output.is_relative_to(root / "build")),
            "output cannot overwrite the baseline")
    require(not baseline.is_relative_to(output), "output cannot contain the baseline")
    if allow_removals:
        require(bool(reason.strip()), "--allow-removals requires a non-empty --reason")
    require(not reason.strip() or allow_removals, "--reason is only valid with --allow-removals")

    data = load_data(root)
    base = base_url.rstrip("/")
    try:
        parsed = urlsplit(base)
        require(parsed.scheme == "https" and parsed.hostname and not parsed.query and not parsed.fragment,
                "base URL must be absolute HTTPS without query or fragment")
        parsed.port
    except ValueError as error:
        raise DataError(f"invalid base URL: {error}") from error

    old_manifest, old_snapshot, old_history, old_attributions, old_licenses = baseline_files(baseline)
    require(version > old_manifest["version"],
            f"version {version} must be greater than published version {old_manifest['version']}")
    scores = android_scores(data)
    require(bool(scores), "release refused: no approved scores; an empty full snapshot would erase client data")

    _, client_source_pairs, allowed_sources = current_android_attributions(root)
    used_sources = {}
    for score in data["scores"]:
        if score["status"] != "approved":
            continue
        source = score["source"]
        matches = [attribution for attribution in allowed_sources
                   if attribution["publisher"] == source["publisher"]
                   and attribution["url"] == score["sourceUrl"]
                   and attribution["license"] == source["license"]]
        require(len(matches) == 1,
                f"{score['id']}: current Android v2 attribution bundle does not cover this source exactly")
        require((score["sourceUrl"], score["sourceType"]) in client_source_pairs,
                f"{score['id']}: current Android v2 snapshot does not contain this source type")
        attribution = matches[0]
        source_key = attribution["sourceId"]
        previous = used_sources.get(source_key)
        require(previous is None or previous == attribution, f"inconsistent source attribution for {source_key}")
        used_sources[source_key] = attribution

    current_ids = {score["id"] for score in old_snapshot["scores"]}
    new_ids = {score["id"] for score in scores}
    removed = sorted(current_ids - new_ids)
    added = sorted(new_ids - current_ids)
    old_by_id = {score["id"]: score for score in old_snapshot["scores"]}
    new_by_id = {score["id"]: score for score in scores}
    changed = sorted(score_id for score_id in old_by_id.keys() & new_by_id.keys()
                     if old_by_id[score_id] != new_by_id[score_id])
    require(not removed or allow_removals,
            f"release would remove {len(removed)} published scores; review and use --allow-removals --reason")
    require(scores != old_snapshot["scores"], "release contains no Android-visible score changes; do not issue a no-op version")

    snapshot = {"schemaVersion": 1, "version": version, "scores": scores}
    validate_snapshot(snapshot)
    snapshot_bytes = json_bytes(snapshot)
    require(len(snapshot_bytes) <= MAX_SNAPSHOT_BYTES, "snapshot exceeds Android 16 MiB limit")
    manifest = {
        "schemaVersion": 1,
        "version": version,
        "url": f"{base}/benchmarks/scores-v{version}.json",
        "sha256": sha256(snapshot_bytes),
    }
    validate_manifest(manifest)
    manifest_bytes = json_bytes(manifest)
    require(len(manifest_bytes) <= MAX_MANIFEST_BYTES, "manifest exceeds Android 64 KiB limit")

    files: dict[str, bytes] = {}
    for old_version, content in old_history.items():
        add_file(files, f"benchmarks/scores-v{old_version}.json", content)
    add_file(files, f"benchmarks/scores-v{version}.json", snapshot_bytes)
    for old_version, content in old_attributions.items():
        add_file(files, f"attributions/v{old_version}.json", content)
    attribution_doc = {"version": version, "sources": [used_sources[key] for key in sorted(used_sources)]}
    add_file(files, f"attributions/v{version}.json", json_bytes(attribution_doc))
    for relative, content in old_licenses.items():
        add_file(files, relative, content)
    for score in data["scores"]:
        if score["status"] != "approved":
            continue
        relative = score["source"]["license"]["licenseFile"]
        license_path = root / safe_relative_path(relative)
        content = license_path.read_bytes()
        add_file(files, relative, content)
    files[".nojekyll"] = b""

    # Reject stale output files rather than silently deploying a mixed site.
    if output.exists():
        allowed_files = set(files) | {"manifest.json"}
        for existing in output.rglob("*"):
            if existing.is_dir():
                continue
            require(not existing.is_symlink(), f"output symlink is forbidden: {existing}")
            relative = existing.relative_to(output).as_posix()
            require(relative in allowed_files, f"unexpected file in output directory: {relative}; use a fresh directory")

    # Check all paths and existing immutable bytes before writing anything.
    for relative, content in files.items():
        path = output / relative
        require(not path.is_symlink(), f"output symlink is forbidden: {path}")
        require(path.resolve().is_relative_to(output), f"output path escapes destination: {relative}")
        if path.exists():
            require(path.read_bytes() == content, f"immutable artifact already exists with different bytes: {relative}")
    manifest_path = output / "manifest.json"
    require(not manifest_path.is_symlink(), f"output symlink is forbidden: {manifest_path}")
    if manifest_path.exists():
        existing_manifest = read_json(manifest_path, MAX_MANIFEST_BYTES)
        require(existing_manifest == manifest, "output already contains a different manifest; use a fresh directory")

    for relative, content in files.items():
        path = output / relative
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("xb") as handle:
                handle.write(content)
    if not manifest_path.exists():
        output.mkdir(parents=True, exist_ok=True)
        temporary = output / ".manifest.json.tmp"
        require(not temporary.exists() and not temporary.is_symlink(), "stale temporary manifest; inspect output")
        with temporary.open("xb") as handle:
            handle.write(manifest_bytes)
        temporary.replace(manifest_path)
    read_bundle(output)
    return {"version": version, "scoreCount": len(scores), "added": added,
            "changed": changed, "removed": removed, "sha256": manifest["sha256"], "output": output}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", type=int, required=True, help="positive integer greater than the latest published version")
    parser.add_argument("--output", type=Path, help="default: build/site-v<version>")
    parser.add_argument("--baseline", type=Path, help="default: pinned manifest and history in the repository")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--allow-removals", action="store_true", help="allow explicitly reviewed removals of published score IDs")
    parser.add_argument("--reason", default="", help="required explanation when --allow-removals is used")
    args = parser.parse_args()
    output = args.output or ROOT / "build" / f"site-v{args.version}"
    try:
        result = build(ROOT, output, args.version, args.baseline, args.base_url, args.allow_removals, args.reason)
        print(f"OK: v{result['version']} with {result['scoreCount']} scores; SHA-256 {result['sha256']}")
        print(f"Changes: +{len(result['added'])} / ~{len(result['changed'])} / -{len(result['removed'])}; output {result['output']}")
        print("Not deployed; this command only writes a local static snapshot bundle.")
        return 0
    except (DataError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
