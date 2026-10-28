"""Merge the fixed review's staging documents, without approving or publishing.

Staging is retained as an input/audit record, not another maintenance source.
The caller must stop other writers during both --check and --apply. The digest
links their separate snapshots but is not a lock; rollback is best effort, not
a filesystem-wide transaction or a guarantee of atomicity after a crash.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile

from common import DataError, ROOT, json_bytes, load_catalog, read_json, require, unique_index, validate_schema
from preview_candidates import review_candidates

REVIEW = Path("data/reviews/2026-10-28")
STAGING = ("staging-verified-indices.json", "staging-coding-science.json", "staging-agent-knowledge.json")
EVIDENCE = ("evidence-indices.json", "evidence-coding-science.json", "evidence-agent-knowledge.json")
TARGETS = ("aa-intelligence-index", "vals-index", "terminal-bench", "deepswe", "swe-bench-pro", "osworld", "automationbench", "hle", "gdpval-aa", "chartography", "terminal-bench-science")
DOCUMENTS = {"benchmarks": "benchmarks.json", "sources": "sources.json", "mappings": "model-mappings.json"}
SCRIPT_INPUTS = tuple(Path("scripts") / name for name in ("common.py", "preview_candidates.py", "merge_candidate_staging.py"))
NOTES = "Pending candidates from the three retained staging inputs; staging is not a maintenance source. No approval or publication."


def safe_path(root: Path, relative: Path) -> Path:
    require(not relative.is_absolute() and ".." not in relative.parts, f"unsafe path: {relative}")
    path = root
    for part in relative.parts:
        path = path / part
        require(not path.is_symlink(), f"symlink forbidden: {path}")
    return path


def read_optional(path: Path) -> bytes | None:
    if not path.exists():
        return None
    require(path.is_file(), f"not a regular file: {path}")
    return path.read_bytes()


def copy_inputs(root: Path, dest: Path) -> dict[Path, bytes]:
    """Snapshot inputs to an external directory and reject links, even in parents."""
    snapshot = {}
    for folder in ("data", "schemas", "third_party", "benchmarks"):
        base = safe_path(root, Path(folder))
        require(base.is_dir(), f"missing input directory: {base}")
        for current, dirs, files in os.walk(base, followlinks=False):
            for name in dirs + files:
                path = Path(current) / name
                require(not path.is_symlink(), f"symlink forbidden: {path}")
            for name in files:
                path = Path(current) / name
                require(path.is_file(), f"not a regular file: {path}")
                rel = path.relative_to(root)
                content = path.read_bytes()
                snapshot[rel] = content
                target = dest / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
    for rel in (Path("manifest.json"), *SCRIPT_INPUTS):
        path = safe_path(root, rel)
        require(path.is_file(), f"missing input: {path}")
        snapshot[rel] = path.read_bytes()
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(snapshot[rel])
    return snapshot


def snapshot_digest(snapshot: dict[Path, bytes]) -> str:
    """Hash a sorted, unambiguous list of relative paths and content hashes."""
    entries = [{"path": path.as_posix(), "sha256": hashlib.sha256(data).hexdigest()}
               for path, data in sorted(snapshot.items(), key=lambda item: item[0].as_posix())]
    return hashlib.sha256(json_bytes(entries)).hexdigest()


def report_snapshot(snapshot: dict[Path, bytes], digest: str) -> None:
    for path, content in sorted(snapshot.items(), key=lambda item: item[0].as_posix()):
        print(f"input-sha256 {hashlib.sha256(content).hexdigest()} {json.dumps(path.as_posix(), ensure_ascii=True)}")
    print(f"snapshot-sha256 {digest}")


def check_scope(sandbox: Path, staging: list[dict]) -> None:
    """Reject unreferenced imports instead of silently discarding staged objects."""
    all_mappings = {}
    canonical = read_json(sandbox / "data/model-mappings.json")
    for row in canonical["mappings"]:
        all_mappings[row["id"]] = row
    for obj in staging:
        for mapping in obj["mappings"]:
            require(isinstance(mapping, dict) and isinstance(mapping.get("id"), str), "invalid staging mapping")
            if mapping["id"] in all_mappings:
                require(json_bytes(all_mappings[mapping["id"]]) == json_bytes(mapping), f"conflicting mappings id: {mapping['id']}")
            all_mappings[mapping["id"]] = mapping

    known_sources = {row["id"] for row in read_json(sandbox / "data/sources.json")["sources"]}
    for obj in staging:
        for source in obj["sources"]:
            require(isinstance(source, dict) and isinstance(source.get("id"), str), "invalid staging source")
            known_sources.add(source["id"])

    for name, obj, evidence_name in zip(STAGING, staging, EVIDENCE):
        evidence = read_json(sandbox / REVIEW / evidence_name)
        validate_schema(evidence, "candidate-evidence.schema.json", sandbox)
        allowed_benchmarks = set()
        for target in evidence["targets"]:
            require(target["id"] in TARGETS, f"{evidence_name}: unrelated target {target['id']}")
            allowed_benchmarks.update(target["benchmarkIds"])
        sources = {entry["sourceId"] for entry in evidence["evidence"]}
        for system in evidence["systemOnly"]:
            if "sourceId" in system:
                source_id = system["sourceId"]
                require(isinstance(source_id, str) and bool(source_id), f"{evidence_name}: invalid system sourceId")
                sources.add(source_id)
        mapping_ids = set()
        for result in obj["results"]:
            require(isinstance(result, dict), f"{name}: invalid result")
            benchmark_id = result.get("benchmarkId")
            require(benchmark_id in allowed_benchmarks, f"{name}: result outside evidence targets: {benchmark_id}")
            mapping_id = result.get("mappingId")
            require(isinstance(mapping_id, str) and mapping_id in all_mappings, f"{name}: unknown result mapping: {mapping_id}")
            mapping_ids.add(mapping_id)
            source_id = result.get("sourceId")
            require(isinstance(source_id, str), f"{name}: invalid result sourceId")
            sources.add(source_id)
            mapping_source = all_mappings[mapping_id].get("sourceId")
            require(isinstance(mapping_source, str), f"{name}: invalid mapping sourceId")
            sources.add(mapping_source)
        for key, allowed in (("benchmarks", allowed_benchmarks), ("mappings", mapping_ids), ("sources", sources)):
            for row in obj[key]:
                require(isinstance(row, dict) and isinstance(row.get("id"), str), f"{name}: invalid {key} object")
                require(row["id"] in allowed, f"{name}: unrelated {key} id: {row['id']}")
        require(sources <= known_sources, f"{evidence_name}: unknown referenced sources: {sorted(sources - known_sources)}")


def merge_rows(existing: list, incoming: list, label: str) -> None:
    index = unique_index(existing, label)
    for row in incoming:
        require(isinstance(row, dict) and isinstance(row.get("id"), str), f"invalid {label} object")
        require(row.get("status") == "pending", f"{label} {row['id']}: only pending staging objects allowed")
        if row["id"] in index:
            require(json_bytes(index[row["id"]]) == json_bytes(row), f"conflicting {label} id: {row['id']}")
        else:
            existing.append(row)
            index[row["id"]] = row


def plan(root: Path, sandbox: Path) -> tuple[dict[Path, bytes], dict[Path, bytes]]:
    snapshot = copy_inputs(root, sandbox)
    staging = []
    for name in STAGING:
        obj = read_json(sandbox / REVIEW / name)
        require(isinstance(obj, dict) and set(obj) == {"benchmarks", "sources", "mappings", "results"}, f"{name}: invalid staging keys")
        for key in ("benchmarks", "sources", "mappings", "results"):
            require(isinstance(obj[key], list), f"{name}: {key} must be an array")
        staging.append(obj)

    check_scope(sandbox, staging)

    outputs = {}
    for key, filename in DOCUMENTS.items():
        rel = Path("data") / filename
        document = read_json(sandbox / rel)
        definition = {"benchmarks": "benchmarkDocument", "sources": "sourceDocument", "mappings": "mappingDocument"}[key]
        validate_schema(document, "source-data.schema.json", sandbox, definition)
        for obj in staging:
            merge_rows(document[key], obj[key], key)
        outputs[rel] = json_bytes(document)

    result_dir = sandbox / "data/results"
    all_results = []
    docs = {}
    for path in sorted(result_dir.glob("*.json")):
        document = read_json(path)
        validate_schema(document, "source-data.schema.json", sandbox, "resultDocument")
        require(all(row["benchmarkId"] == path.stem for row in document["results"]), f"{path}: filename must match benchmarkId")
        docs[path.stem] = document
        all_results.extend(document["results"])
    index = unique_index(all_results, "result")
    candidate_ids = []
    seen = {}
    for obj in staging:
        for row in obj["results"]:
            require(isinstance(row, dict) and isinstance(row.get("id"), str), "invalid result")
            ident, benchmark = row["id"], row.get("benchmarkId")
            require(row.get("status") == "pending", f"{ident}: only pending staging results allowed")
            require(isinstance(benchmark, str) and re.fullmatch(r"[a-z0-9]+(?:[.-][a-z0-9]+)*", benchmark), f"{ident}: invalid benchmark filename")
            if ident in seen:
                require(json_bytes(seen[ident]) == json_bytes(row), f"conflicting result id: {ident}")
                continue
            seen[ident] = row
            candidate_ids.append(ident)
            if ident in index:
                require(json_bytes(index[ident]) == json_bytes(row), f"conflicting result id: {ident}")
                continue
            doc = docs.setdefault(benchmark, {"schemaVersion": 1, "results": []})
            doc["results"].append(row)
            index[ident] = row
            outputs[Path("data/results") / (benchmark + ".json")] = json_bytes(doc)

    batch = {"schemaVersion": 1, "id": "benchmark-refresh-2026-10-28", "scopeFile": "models.json", "baselineFile": "baseline.json", "evidenceFiles": list(EVIDENCE), "targetIds": list(TARGETS), "candidateResultIds": candidate_ids, "notes": NOTES}
    batch_rel = REVIEW / "batch.json"
    if batch_rel in snapshot:
        require(json_bytes(read_json(sandbox / batch_rel)) == json_bytes(batch), "existing batch.json differs")
    else:
        outputs[batch_rel] = json_bytes(batch)

    # Do not rewrite unchanged files, including existing formatting and hard links.
    outputs = {p: content for p, content in outputs.items() if p not in snapshot or json_bytes(read_json(sandbox / p)) != content}
    for rel, content in outputs.items():
        target = sandbox / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    load_catalog(sandbox)
    review_candidates(sandbox, sandbox / batch_rel, check_android=False)
    return outputs, snapshot


def verify_snapshot(root: Path, snapshot: dict[Path, bytes], outputs: dict[Path, bytes], temporary: set[Path] | None = None) -> None:
    # Compare names too: newly created catalog files could change validation.
    for folder in ("data", "schemas", "third_party", "benchmarks"):
        base = safe_path(root, Path(folder))
        for current, dirs, files in os.walk(base, followlinks=False):
            for name in dirs + files:
                path = Path(current) / name
                require(not path.is_symlink(), f"symlink forbidden: {path}")
            for name in files:
                rel = (Path(current) / name).relative_to(root)
                require(rel in snapshot or rel in (temporary or set()), f"input added during validation: {rel}")
    for rel, old in snapshot.items():
        require(read_optional(safe_path(root, rel)) == old, f"input changed during validation: {rel}")
    for rel in outputs:
        path = safe_path(root, rel)
        require(read_optional(path) == snapshot.get(rel), f"output changed during validation: {rel}")
        require(path.parent.is_dir(), f"missing output directory: {path.parent}")


def install(root: Path, outputs: dict[Path, bytes], snapshot: dict[Path, bytes]) -> None:
    verify_snapshot(root, snapshot, outputs)
    prepared = {}
    installed = []
    try:
        for rel, content in outputs.items():
            path = safe_path(root, rel)
            fd, name = tempfile.mkstemp(prefix=".candidate-merge-", dir=path.parent)
            prepared[rel] = Path(name)
            with os.fdopen(fd, "wb") as stream:
                stream.write(content)
                stream.flush()
                os.fsync(stream.fileno())
            if rel in snapshot:
                os.chmod(name, stat.S_IMODE(path.stat().st_mode))
        verify_snapshot(root, snapshot, outputs, {p.relative_to(root) for p in prepared.values()})
        for rel, content in outputs.items():
            path = safe_path(root, rel)
            require(read_optional(path) == snapshot.get(rel), f"output changed before install: {rel}")
            if rel in snapshot:
                os.replace(prepared[rel], path)
                installed.append(rel)
            else:
                # Exclusive creation: never replace a file that appeared meanwhile.
                os.link(prepared[rel], path)
                installed.append(rel)
                prepared[rel].unlink()
    except BaseException as error:
        failures = []
        for rel in reversed(installed):
            try:
                path = safe_path(root, rel)
                require(read_optional(path) == outputs[rel], f"rollback skipped modified output: {rel}")
                if rel not in snapshot:
                    path.unlink()
                else:
                    fd, name = tempfile.mkstemp(prefix=".candidate-rollback-", dir=path.parent)
                    try:
                        with os.fdopen(fd, "wb") as stream:
                            stream.write(snapshot[rel])
                        os.chmod(name, stat.S_IMODE(path.stat().st_mode))
                        os.replace(name, path)
                    finally:
                        if os.path.exists(name):
                            os.unlink(name)
            except (OSError, DataError) as rollback_error:
                failures.append(str(rollback_error))
        if failures:
            raise DataError(f"{error}; rollback incomplete: {'; '.join(failures)}") from error
        raise
    finally:
        for path in prepared.values():
            path.unlink(missing_ok=True)


def run(root: Path, apply: bool = False, expected_sha256: str | None = None, checkpoint=None) -> int:
    root = root.resolve()
    # Explicitly require an external sandbox, even if TMPDIR points into the repo.
    with tempfile.TemporaryDirectory() as name:
        sandbox = Path(name).resolve()
        require(not sandbox.is_relative_to(root), "temporary directory must be outside repository")
        outputs, snapshot = plan(root, sandbox)
        digest = snapshot_digest(snapshot)
        if expected_sha256 is not None:
            require(digest == expected_sha256, "input snapshot SHA-256 does not match --expected-sha256")
        if apply:
            install(root, outputs, snapshot)
        else:
            verify_snapshot(root, snapshot, outputs)
            if checkpoint is not None:
                checkpoint(snapshot, digest)
        return len(outputs)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="validate in isolation without writing")
    group.add_argument("--apply", action="store_true", help="apply validated changes; stop other writers first")
    parser.add_argument("--expected-sha256", help="snapshot-sha256 printed by a successful --check (required for --apply)")
    args = parser.parse_args()
    if args.apply and (not args.expected_sha256 or not re.fullmatch(r"[0-9a-f]{64}", args.expected_sha256)):
        parser.error("--apply requires --expected-sha256 with the 64-character lowercase digest from --check")
    if args.check and args.expected_sha256 is not None:
        parser.error("--expected-sha256 is only valid with --apply")
    try:
        count = run(ROOT, apply=args.apply, expected_sha256=args.expected_sha256, checkpoint=report_snapshot if args.check else None)
    except (DataError, OSError, ValueError, KeyError, TypeError) as error:
        print(f"merge refused: {error}", file=sys.stderr)
        return 1
    print(f"{'Applied' if args.apply else 'Validated'} {count} changed files; staging retained, no approval or publication.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
