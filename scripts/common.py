"""Shared, offline validation for maintenance data and Android artifacts."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
from pathlib import Path
from urllib.parse import urlsplit

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
MAX_MANIFEST_BYTES = 64 * 1024
MAX_SNAPSHOT_BYTES = 16 * 1024 * 1024
DEFAULT_BASE_URL = "https://chenlongapps.github.io/model-atlas-data"


class DataError(ValueError):
    """An actionable data or artifact validation error."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise DataError(message)


def _pairs(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _constant(value: str) -> None:
    raise DataError(f"non-finite JSON number: {value}")


def _finite(value) -> None:
    if isinstance(value, dict):
        for item in value.values():
            _finite(item)
    elif isinstance(value, list):
        for item in value:
            _finite(item)
    elif isinstance(value, (int, float)) and not isinstance(value, bool):
        try:
            require(math.isfinite(value), "number cannot be represented as a finite Double")
        except OverflowError as error:
            raise DataError("number exceeds the Double range") from error


def decode_json(content: bytes):
    try:
        data = json.loads(content.decode("utf-8"), object_pairs_hook=_pairs, parse_constant=_constant)
        _finite(data)
        return data
    except (UnicodeError, ValueError, RecursionError) as error:
        raise DataError(f"invalid JSON: {error}") from error


def read_json(path: Path, max_bytes: int | None = None):
    try:
        if max_bytes is not None:
            require(path.stat().st_size <= max_bytes, f"{path}: exceeds {max_bytes} bytes")
        return decode_json(path.read_bytes())
    except (OSError, UnicodeError, ValueError, RecursionError) as error:
        raise DataError(f"{path}: {error}") from error


def json_bytes(data) -> bytes:
    _finite(data)
    return (json.dumps(data, ensure_ascii=False, allow_nan=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def https_url(value: str) -> None:
    try:
        parsed = urlsplit(value)
        require(parsed.scheme == "https" and bool(parsed.hostname), f"not an absolute HTTPS URL: {value}")
        require(parsed.username is None and parsed.password is None, f"URL credentials are forbidden: {value}")
        require(not any(character.isspace() or ord(character) < 32 for character in value), f"URL contains whitespace: {value}")
        parsed.port  # Validate the port, including malformed/non-numeric ports.
    except ValueError as error:
        raise DataError(f"invalid HTTPS URL: {value}: {error}") from error


def check_urls(data) -> None:
    if isinstance(data, dict):
        for key, value in data.items():
            if key.lower().endswith("url") and isinstance(value, str):
                https_url(value)
            check_urls(value)
    elif isinstance(data, list):
        for value in data:
            check_urls(value)


def validate_schema(data, schema_name: str, root: Path = ROOT, definition: str | None = None) -> None:
    if isinstance(data, dict):
        # JSON Schema treats 1.0 as an integer; Kotlin's Int/Long wire tokens do not.
        for key in (("schemaVersion", "version") if schema_name != "source-data.schema.json" else ("schemaVersion",)):
            if key in data:
                require(type(data[key]) is int, f"{key} must be an integer JSON token, not boolean or decimal")
    schema = read_json(root / "schemas" / schema_name)
    Draft202012Validator.check_schema(schema)
    if definition:
        schema = {**schema, "oneOf": [{"$ref": f"#/$defs/{definition}"}]}
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(data), key=lambda error: str(list(error.absolute_path)))
    if errors:
        error = errors[0]
        location = ".".join(map(str, error.absolute_path)) or "<root>"
        # oneOf wraps useful leaf errors; include the first failing field too.
        detail = error.context[0].message if error.context else error.message
        raise DataError(f"{schema_name} at {location}: {error.message}; {detail}")
    _finite(data)
    check_urls(data)


def unique_index(items: list[dict], label: str) -> dict[str, dict]:
    index = {}
    for item in items:
        require(item["id"] not in index, f"duplicate {label} id: {item['id']}")
        index[item["id"]] = item
    return index


def license_path(root: Path, relative: str) -> Path:
    parts = Path(relative).parts
    require(parts and parts[0] == "third_party" and ".." not in parts, f"licenseFile must be under third_party/: {relative}")
    path = (root / relative).resolve()
    require(path.is_relative_to(root.resolve() / "third_party"), f"licenseFile escapes third_party/: {relative}")
    require(path.is_file() and path.stat().st_size > 0, f"missing or empty licenseFile: {relative}")
    return path


@dataclass
class Catalog:
    benchmarks: dict[str, dict]
    sources: dict[str, dict]
    mappings: dict[str, dict]
    results: list[dict]

    def publishable(self) -> list[dict]:
        return sorted((result for result in self.results if result["status"] == "approved"), key=lambda result: result["id"])

    def summary(self) -> dict:
        return {
            "benchmarks": len(self.benchmarks),
            "sources": len(self.sources),
            "mappings": len(self.mappings),
            "results": len(self.results),
            "approvedResults": len(self.publishable()),
            "excludedResults": [{"id": result["id"], "status": result["status"]} for result in sorted(self.results, key=lambda result: result["id"]) if result["status"] != "approved"],
        }


def load_catalog(root: Path = ROOT) -> Catalog:
    def document(relative: str, key: str, definition: str) -> list:
        data = read_json(root / "data" / relative)
        validate_schema(data, "source-data.schema.json", root, definition)
        return data[key]

    benchmarks = unique_index(document("benchmarks.json", "benchmarks", "benchmarkDocument"), "benchmark")
    sources = unique_index(document("sources.json", "sources", "sourceDocument"), "source")
    mappings = unique_index(document("model-mappings.json", "mappings", "mappingDocument"), "mapping")
    results = []
    for path in sorted((root / "data" / "results").glob("*.json")):
        rows = document(f"results/{path.name}", "results", "resultDocument")
        require(all(result["benchmarkId"] == path.stem for result in rows), f"{path}: filename must match benchmarkId")
        results.extend(rows)
    unique_index(results, "result")

    for benchmark in benchmarks.values():
        low, high = benchmark["minimum"], benchmark["maximum"]
        require(low is None or high is None or low <= high, f"{benchmark['id']}: inverted score range")
        if benchmark["status"] == "approved":
            require(all(benchmark[key] is not None for key in ("metric", "unit", "higherIsBetter")), f"{benchmark['id']}: approved benchmark needs metric, unit and direction")

    for source in sources.values():
        license_info = source["license"]
        if license_info["licenseFile"] is not None:
            license_path(root, license_info["licenseFile"])
        if source["status"] == "approved":
            require(license_info["redistribution"] == "allowed", f"{source['id']}: redistribution is not approved")
            require(all(license_info[key] for key in ("name", "url", "licenseFile")), f"{source['id']}: missing license evidence")

    for mapping in mappings.values():
        require(mapping["sourceId"] in sources, f"{mapping['id']}: unknown sourceId")
        if mapping["status"] == "approved":
            require(all(mapping[key] for key in ("modelId", "evidenceUrl", "catalogUrl")), f"{mapping['id']}: approved mapping needs modelId and evidence URLs")

    for result in results:
        label = result["id"]
        require(result["benchmarkId"] in benchmarks, f"{label}: unknown benchmarkId")
        require(result["sourceId"] in sources, f"{label}: unknown sourceId")
        require(result["mappingId"] in mappings, f"{label}: unknown mappingId")
        benchmark = benchmarks[result["benchmarkId"]]
        source = sources[result["sourceId"]]
        mapping = mappings[result["mappingId"]]
        require(mapping["sourceId"] == source["id"], f"{label}: mapping belongs to another source")
        low, high = benchmark["minimum"], benchmark["maximum"]
        require(low is None or result["score"] >= low, f"{label}: score below benchmark minimum")
        require(high is None or result["score"] <= high, f"{label}: score above benchmark maximum")
        if result["status"] == "approved":
            require(all(item["status"] == "approved" for item in (benchmark, source, mapping)), f"{label}: approved result has unapproved dependencies")
            require(not result["unrepresentedConditions"], f"{label}: v1 cannot represent essential conditions")

    return Catalog(benchmarks, sources, mappings, results)


def validate_snapshot(snapshot: dict, root: Path = ROOT) -> None:
    if isinstance(snapshot, dict) and isinstance(snapshot.get("scores"), list):
        require(len(snapshot["scores"]) <= 100_000, "snapshot exceeds Android limit of 100,000 scores")
    validate_schema(snapshot, "snapshot-v1.schema.json", root)
    unique_index(snapshot["scores"], "score")
    require(len(json_bytes(snapshot)) <= MAX_SNAPSHOT_BYTES, "serialized snapshot exceeds Android byte limit")


def read_artifacts(directory: Path, root: Path = ROOT) -> tuple[dict, dict]:
    manifest = read_json(directory / "manifest.json", MAX_MANIFEST_BYTES)
    validate_schema(manifest, "manifest-v1.schema.json", root)
    parsed = urlsplit(manifest["url"])
    relative = f"benchmarks/scores-v{manifest['version']}.json"
    require(parsed.path.endswith("/" + relative) and not parsed.query and not parsed.fragment, "manifest URL must end in /benchmarks/scores-v<version>.json without query or fragment")
    path = directory / relative
    snapshot = read_json(path, MAX_SNAPSHOT_BYTES)
    validate_snapshot(snapshot, root)
    require(manifest["version"] == snapshot["version"], "manifest/snapshot version mismatch")
    require(sha256(path.read_bytes()).lower() == manifest["sha256"].lower(), "snapshot SHA-256 mismatch")
    return manifest, snapshot
