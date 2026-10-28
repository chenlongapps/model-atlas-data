#!/usr/bin/env python3
"""Validate the hand-maintained ModelAtlas Benchmark JSON files offline."""

from __future__ import annotations

from datetime import date
import hashlib
import json
import math
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
MAX_MANIFEST_BYTES = 64 * 1024
MAX_SNAPSHOT_BYTES = 16 * 1024 * 1024
MAX_VERSION = 9_223_372_036_854_775_807
ID_RE = re.compile(r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$")
MODEL_ID_RE = re.compile(r"^[^\s/]+/[^\s]+$")
SHA_RE = re.compile(r"^[0-9a-fA-F]{64}$")
ANDROID_SCORE_KEYS = {
    "id", "modelId", "benchmarkId", "score", "cost", "metric", "unit",
    "higherIsBetter", "subset", "harness", "reasoningEffort", "toolsEnabled",
    "sourceUrl", "sourceType", "evaluatedAt",
}
SOURCE_TYPES = {"benchmark_author", "model_developer", "independent"}
STATUSES = {"pending", "approved"}


class DataError(ValueError):
    """An actionable data or publication error."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise DataError(message)


def _pairs(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _constant(value: str):
    raise DataError(f"non-finite JSON number: {value}")


def _finite(value) -> None:
    if isinstance(value, dict):
        for child in value.values():
            _finite(child)
    elif isinstance(value, list):
        for child in value:
            _finite(child)
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        try:
            require(math.isfinite(value), "number must be finite and representable as a Double")
        except OverflowError as error:
            raise DataError("number exceeds the Double range") from error


def read_json(path: Path, max_bytes: int | None = None):
    require(not path.is_symlink(), f"symlink is not allowed: {path}")
    try:
        content = path.read_bytes()
        if max_bytes is not None:
            require(len(content) <= max_bytes, f"{path}: exceeds {max_bytes} bytes")
        value = json.loads(content.decode("utf-8"), object_pairs_hook=_pairs, parse_constant=_constant)
        _finite(value)
        return value
    except DataError:
        raise
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError) as error:
        raise DataError(f"{path}: invalid JSON: {error}") from error


def json_bytes(value) -> bytes:
    _finite(value)
    return (json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def check_keys(value: dict, required: set[str], optional: set[str], label: str) -> None:
    require(isinstance(value, dict), f"{label}: expected an object")
    missing = required - value.keys()
    extra = value.keys() - required - optional
    require(not missing, f"{label}: missing fields {sorted(missing)}")
    require(not extra, f"{label}: unknown fields {sorted(extra)}")


def text(value, label: str) -> None:
    require(isinstance(value, str) and bool(value.strip()), f"{label}: expected non-empty text")


def optional_text(value, label: str) -> None:
    if value is not None:
        text(value, label)


def check_id(value, label: str) -> None:
    require(isinstance(value, str) and ID_RE.fullmatch(value) is not None, f"{label}: invalid stable ID {value!r}")


def check_date(value, label: str, optional: bool = False) -> None:
    if value is None and optional:
        return
    require(isinstance(value, str), f"{label}: expected ISO date")
    try:
        require(date.fromisoformat(value).isoformat() == value, f"{label}: expected YYYY-MM-DD")
    except ValueError as error:
        raise DataError(f"{label}: invalid date {value!r}") from error


def check_url(value, label: str, optional: bool = False) -> None:
    if value is None and optional:
        return
    require(isinstance(value, str), f"{label}: expected HTTPS URL")
    try:
        parsed = urlsplit(value)
        require(parsed.scheme == "https" and bool(parsed.hostname), f"{label}: expected absolute HTTPS URL")
        require(parsed.username is None and parsed.password is None, f"{label}: URL credentials are forbidden")
        require(not any(ch.isspace() or ord(ch) < 32 for ch in value), f"{label}: URL contains whitespace")
        parsed.port
    except ValueError as error:
        raise DataError(f"{label}: invalid HTTPS URL: {error}") from error


def check_number(value, label: str, optional: bool = False) -> None:
    if value is None and optional:
        return
    require(type(value) in (int, float), f"{label}: expected a finite number, not bool or text")
    try:
        require(math.isfinite(value), f"{label}: expected a finite number")
    except OverflowError as error:
        raise DataError(f"{label}: number exceeds the Double range") from error


def check_license_path(root: Path, value: str, label: str) -> Path:
    text(value, label)
    parts = Path(value).parts
    require(parts and parts[0] == "third_party" and ".." not in parts,
            f"{label}: license files must stay under third_party/")
    raw_path = root.joinpath(*parts)
    current = root
    for part in parts:
        current = current / part
        require(not current.is_symlink(), f"{label}: symlinks are forbidden in license paths")
    path = raw_path.resolve()
    require(path.is_relative_to((root / "third_party").resolve()), f"{label}: path escapes third_party/")
    require(path.is_file() and not path.is_symlink() and path.stat().st_size > 0,
            f"{label}: missing or empty file {value}")
    return path


def validate_benchmark(benchmark: dict, label: str) -> None:
    required = {"id", "name", "version", "description", "category", "officialUrl", "metric", "unit",
                "higherIsBetter", "minimum", "maximum", "status"}
    check_keys(benchmark, required, set(), label)
    check_id(benchmark["id"], f"{label}.id")
    for key in ("name", "description"):
        text(benchmark[key], f"{label}.{key}")
    optional_text(benchmark["version"], f"{label}.version")
    optional_text(benchmark["metric"], f"{label}.metric")
    optional_text(benchmark["unit"], f"{label}.unit")
    require(isinstance(benchmark["category"], str) and benchmark["category"] in {"coding", "agent", "knowledge_reasoning", "math", "multimodal", "professional", "science", "other"},
            f"{label}.category: invalid category")
    check_url(benchmark["officialUrl"], f"{label}.officialUrl")
    require(benchmark["higherIsBetter"] is None or type(benchmark["higherIsBetter"]) is bool,
            f"{label}.higherIsBetter: expected bool or null")
    check_number(benchmark["minimum"], f"{label}.minimum", optional=True)
    check_number(benchmark["maximum"], f"{label}.maximum", optional=True)
    require(benchmark["minimum"] is None or benchmark["maximum"] is None or benchmark["minimum"] <= benchmark["maximum"],
            f"{label}: minimum exceeds maximum")
    require(isinstance(benchmark["status"], str) and benchmark["status"] in STATUSES, f"{label}.status: expected pending or approved")
    if benchmark["status"] == "approved":
        require(all(benchmark[key] is not None for key in ("metric", "unit", "higherIsBetter")),
                f"{label}: approved Benchmark needs metric, unit, and direction")


def validate_source(score: dict, root: Path, label: str) -> None:
    source = score["source"]
    check_keys(source, {"publisher", "status", "license"}, {"retrievedAt", "publishedAt"}, f"{label}.source")
    text(source["publisher"], f"{label}.source.publisher")
    if "retrievedAt" in source:
        check_date(source["retrievedAt"], f"{label}.source.retrievedAt")
    if "publishedAt" in source:
        check_date(source["publishedAt"], f"{label}.source.publishedAt", optional=True)
    require(isinstance(source["status"], str) and source["status"] in STATUSES, f"{label}.source.status: expected pending or approved")
    check_url(score["sourceUrl"], f"{label}.sourceUrl")
    if "sourceType" in score:
        require(score["sourceType"] is None or
                isinstance(score["sourceType"], str) and score["sourceType"] in SOURCE_TYPES,
                f"{label}.sourceType: invalid source type")

    license_info = source["license"]
    check_keys(license_info, {"redistribution"}, {"name", "url", "licenseFile", "attribution", "notes"},
               f"{label}.source.license")
    if "name" in license_info:
        optional_text(license_info["name"], f"{label}.source.license.name")
    if "url" in license_info:
        check_url(license_info["url"], f"{label}.source.license.url", optional=True)
    if "licenseFile" in license_info:
        optional_text(license_info["licenseFile"], f"{label}.source.license.licenseFile")
        if license_info["licenseFile"] is not None:
            check_license_path(root, license_info["licenseFile"], f"{label}.source.license.licenseFile")
    require(isinstance(license_info["redistribution"], str) and license_info["redistribution"] in {"pending", "allowed", "prohibited"},
            f"{label}.source.license.redistribution: invalid permission state")
    for key in ("attribution", "notes"):
        if key in license_info:
            optional_text(license_info[key], f"{label}.source.license.{key}")
    if source["status"] == "approved":
        require(license_info["redistribution"] == "allowed", f"{label}: approved source lacks redistribution permission")
        require(all(license_info.get(key) for key in ("name", "url", "licenseFile", "attribution")),
                f"{label}: approved source needs license name, URL, local text, and attribution")


def validate_mapping(score: dict, label: str) -> None:
    mapping = score["modelMapping"]
    check_keys(mapping, {"status"}, {"evidenceUrl", "catalogUrl", "notes"}, f"{label}.modelMapping")
    require(isinstance(mapping["status"], str) and mapping["status"] in STATUSES, f"{label}.modelMapping.status: expected pending or approved")
    for key in ("evidenceUrl", "catalogUrl"):
        if key in mapping:
            check_url(mapping[key], f"{label}.modelMapping.{key}", optional=True)
    if "notes" in mapping:
        optional_text(mapping["notes"], f"{label}.modelMapping.notes")
    optional_text(score.get("sourceModelName"), f"{label}.sourceModelName")
    optional_text(score["modelId"], f"{label}.modelId")
    if score["modelId"] is not None:
        require(MODEL_ID_RE.fullmatch(score["modelId"]) is not None, f"{label}.modelId: invalid Models.dev ID")
    if score["modelId"] is None:
        require(bool(score.get("sourceModelName", "").strip()),
                f"{label}: keep sourceModelName when modelId is unknown")
    if mapping["status"] == "approved":
        require(score["modelId"] is not None, f"{label}: approved mapping needs a modelId")
        require(mapping.get("evidenceUrl") and mapping.get("catalogUrl"),
                f"{label}: approved mapping needs identity and catalog evidence")


def load_data(root: Path = ROOT) -> dict:
    benchmark_doc = read_json(root / "data/benchmarks.json")
    check_keys(benchmark_doc, {"schemaVersion", "benchmarks"}, set(), "data/benchmarks.json")
    require(type(benchmark_doc["schemaVersion"]) is int and benchmark_doc["schemaVersion"] == 1,
            "data/benchmarks.json.schemaVersion must be integer 1")
    require(isinstance(benchmark_doc["benchmarks"], list), "data/benchmarks.json.benchmarks must be an array")
    benchmarks = {}
    for index, benchmark in enumerate(benchmark_doc["benchmarks"]):
        label = f"benchmark[{index}]"
        validate_benchmark(benchmark, label)
        require(benchmark["id"] not in benchmarks, f"duplicate Benchmark ID: {benchmark['id']}")
        benchmarks[benchmark["id"]] = benchmark

    score_doc = read_json(root / "data/scores.json")
    check_keys(score_doc, {"scores"}, set(), "data/scores.json")
    require(isinstance(score_doc["scores"], list), "data/scores.json.scores must be an array")
    scores = []
    by_id = {}
    score_required = {
        "id", "modelId", "benchmarkId", "score", "sourceUrl", "status", "source", "modelMapping",
    }
    score_optional = {
        "sourceModelName", "sourceType", "cost", "metric", "unit", "higherIsBetter", "sourceLocator", "collectedAt",
        "evaluatedAt", "subset", "harness", "reasoningEffort", "toolsEnabled", "unrepresentedConditions", "notes",
    }
    for index, score in enumerate(score_doc["scores"]):
        label = f"score[{index}]"
        check_keys(score, score_required, score_optional, label)
        check_id(score["id"], f"{label}.id")
        require(score["id"] not in by_id, f"duplicate score ID: {score['id']}")
        by_id[score["id"]] = score
        check_id(score["benchmarkId"], f"{label}.benchmarkId")
        require(score["benchmarkId"] in benchmarks, f"{score['id']}: unknown Benchmark ID {score['benchmarkId']}")
        check_number(score["score"], f"{label}.score")
        if "cost" in score:
            check_number(score["cost"], f"{label}.cost", optional=True)
        if "collectedAt" in score:
            check_date(score["collectedAt"], f"{label}.collectedAt")
        if "evaluatedAt" in score:
            check_date(score["evaluatedAt"], f"{label}.evaluatedAt", optional=True)
        for key in ("metric", "unit", "subset", "harness", "reasoningEffort", "notes", "sourceLocator"):
            if key in score:
                optional_text(score[key], f"{label}.{key}")
        if "higherIsBetter" in score:
            require(score["higherIsBetter"] is None or type(score["higherIsBetter"]) is bool,
                    f"{label}.higherIsBetter: expected bool or null")
        if "toolsEnabled" in score:
            require(score["toolsEnabled"] is None or type(score["toolsEnabled"]) is bool,
                    f"{label}.toolsEnabled: expected bool or null")
        require(isinstance(score["status"], str) and score["status"] in STATUSES, f"{label}.status: expected pending or approved")
        if "unrepresentedConditions" in score:
            require(isinstance(score["unrepresentedConditions"], list) and
                    all(isinstance(item, str) and item.strip() for item in score["unrepresentedConditions"]),
                    f"{label}.unrepresentedConditions: expected an array of non-empty strings")
        validate_source(score, root, label)
        validate_mapping(score, label)

        benchmark = benchmarks[score["benchmarkId"]]
        require(benchmark["minimum"] is None or score["score"] >= benchmark["minimum"],
                f"{score['id']}: score below Benchmark minimum")
        require(benchmark["maximum"] is None or score["score"] <= benchmark["maximum"],
                f"{score['id']}: score above Benchmark maximum")
        if score["status"] == "approved":
            require(benchmark["status"] == "approved", f"{score['id']}: approved score uses an unapproved Benchmark")
            require(score["source"]["status"] == "approved", f"{score['id']}: approved score uses an unapproved source")
            require(score["source"]["license"]["redistribution"] == "allowed",
                    f"{score['id']}: approved score source is not cleared for redistribution")
            require(score.get("sourceType") is not None, f"{score['id']}: approved score needs a source type")
            require(score["modelMapping"]["status"] == "approved" and score["modelId"] is not None,
                    f"{score['id']}: approved score needs a verified model mapping")
            require(not score.get("unrepresentedConditions", []),
                    f"{score['id']}: important conditions cannot be expressed in Android v1")

        scores.append(score)
    return {"benchmarks": benchmarks, "scores": scores, "scoresById": by_id}


def validate_snapshot(snapshot: dict) -> None:
    check_keys(snapshot, {"schemaVersion", "version", "scores"}, set(), "snapshot")
    require(type(snapshot["schemaVersion"]) is int and snapshot["schemaVersion"] == 1,
            "snapshot.schemaVersion must be integer 1")
    require(type(snapshot["version"]) is int and 1 <= snapshot["version"] <= MAX_VERSION,
            "snapshot.version must be a positive Kotlin Long")
    require(isinstance(snapshot["scores"], list) and len(snapshot["scores"]) <= 100_000,
            "snapshot.scores must be an array of at most 100,000 entries")
    seen = set()
    for index, score in enumerate(snapshot["scores"]):
        label = f"snapshot.scores[{index}]"
        check_keys(score, {"id", "modelId", "benchmarkId", "score"}, ANDROID_SCORE_KEYS - {"id", "modelId", "benchmarkId", "score"}, label)
        text(score["id"], f"{label}.id")
        require(MODEL_ID_RE.fullmatch(score["modelId"]) is not None, f"{label}.modelId: invalid model ID")
        check_id(score["benchmarkId"], f"{label}.benchmarkId")
        check_number(score["score"], f"{label}.score")
        require(score["id"] not in seen, f"duplicate published score ID: {score['id']}")
        seen.add(score["id"])
        if "cost" in score:
            check_number(score["cost"], f"{label}.cost", optional=True)
        for key in ("metric", "unit", "subset", "harness", "reasoningEffort"):
            if key in score:
                optional_text(score[key], f"{label}.{key}")
        if "higherIsBetter" in score:
            require(score["higherIsBetter"] is None or type(score["higherIsBetter"]) is bool,
                    f"{label}.higherIsBetter: expected bool or null")
        if "toolsEnabled" in score:
            require(score["toolsEnabled"] is None or type(score["toolsEnabled"]) is bool,
                    f"{label}.toolsEnabled: expected bool or null")
        if "sourceUrl" in score:
            check_url(score["sourceUrl"], f"{label}.sourceUrl", optional=True)
        if "sourceType" in score:
            require(score["sourceType"] is None or score["sourceType"] in SOURCE_TYPES,
                    f"{label}.sourceType: invalid source type")
        if "evaluatedAt" in score:
            check_date(score["evaluatedAt"], f"{label}.evaluatedAt", optional=True)


def validate_manifest(manifest: dict) -> None:
    check_keys(manifest, {"schemaVersion", "version", "url", "sha256"}, set(), "manifest")
    require(type(manifest["schemaVersion"]) is int and manifest["schemaVersion"] == 1,
            "manifest.schemaVersion must be integer 1")
    require(type(manifest["version"]) is int and 1 <= manifest["version"] <= MAX_VERSION,
            "manifest.version must be a positive Kotlin Long")
    check_url(manifest["url"], "manifest.url")
    require(isinstance(manifest["sha256"], str) and SHA_RE.fullmatch(manifest["sha256"]) is not None,
            "manifest.sha256 must be 64 hexadecimal characters")
    parsed = urlsplit(manifest["url"])
    require(not parsed.query and not parsed.fragment and
            parsed.path.endswith(f"/benchmarks/scores-v{manifest['version']}.json"),
            "manifest.url must point to benchmarks/scores-v<version>.json")


def read_bundle(directory: Path) -> tuple[dict, dict, bytes]:
    manifest_path = directory / "manifest.json"
    manifest = read_json(manifest_path, MAX_MANIFEST_BYTES)
    validate_manifest(manifest)
    snapshot_path = directory / "benchmarks" / f"scores-v{manifest['version']}.json"
    snapshot = read_json(snapshot_path, MAX_SNAPSHOT_BYTES)
    snapshot_bytes = snapshot_path.read_bytes()
    require(len(snapshot_bytes) <= MAX_SNAPSHOT_BYTES, "snapshot exceeds Android 16 MiB limit")
    validate_snapshot(snapshot)
    require(snapshot["version"] == manifest["version"], "manifest/snapshot version mismatch")
    require(sha256(snapshot_bytes).lower() == manifest["sha256"].lower(), "snapshot SHA-256 mismatch")
    return manifest, snapshot, snapshot_bytes


def android_score(score: dict, benchmark: dict) -> dict:
    return {
        "id": score["id"],
        "modelId": score["modelId"],
        "benchmarkId": score["benchmarkId"],
        "score": score["score"],
        "cost": score.get("cost"),
        "metric": score.get("metric", benchmark["metric"]),
        "unit": score.get("unit", benchmark["unit"]),
        "higherIsBetter": score.get("higherIsBetter", benchmark["higherIsBetter"]),
        "subset": score.get("subset"),
        "harness": score.get("harness"),
        "reasoningEffort": score.get("reasoningEffort"),
        "toolsEnabled": score.get("toolsEnabled"),
        "sourceUrl": score["sourceUrl"],
        "sourceType": score.get("sourceType"),
        "evaluatedAt": score.get("evaluatedAt"),
    }


def android_scores(data: dict) -> list[dict]:
    approved = [score for score in data["scores"] if score["status"] == "approved"]
    return [android_score(score, data["benchmarks"][score["benchmarkId"]])
            for score in sorted(approved, key=lambda item: item["id"])]


def main() -> int:
    try:
        data = load_data(ROOT)
        manifest, snapshot, snapshot_bytes = read_bundle(ROOT)
        approved = sum(score["status"] == "approved" for score in data["scores"])
        pending = len(data["scores"]) - approved
        print(f"OK: {len(data['benchmarks'])} benchmarks; {len(data['scores'])} scores ({approved} approved, {pending} pending)")
        print(f"Pinned Android baseline: v{manifest['version']}, {len(snapshot['scores'])} scores, SHA-256 {sha256(snapshot_bytes)}")
        return 0
    except (DataError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
