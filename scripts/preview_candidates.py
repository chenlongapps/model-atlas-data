"""Offline, candidate-only replacement report; never approve, build or export data."""

from __future__ import annotations

import argparse
from collections import Counter
from datetime import date, datetime
from pathlib import Path
import re
import sys

from common import (
    DataError, ROOT, check_urls, json_bytes, load_catalog, read_json, require,
    sha256, unique_index, validate_schema, validate_snapshot,
)


def attachment(directory: Path, relative: str) -> Path:
    path = directory / relative
    require(not Path(relative).is_absolute() and ".." not in Path(relative).parts,
            f"review attachment escapes batch: {relative}")
    require(not path.is_symlink() and path.resolve().is_relative_to(directory.resolve()),
            f"review attachment must be inside batch: {relative}")
    return path


def digest(value) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def model_scope(scope: dict, batch_id: str) -> dict:
    require(type(scope.get("schemaVersion")) is int and scope["schemaVersion"] == 1,
            "invalid model scope schemaVersion")
    require(scope.get("batchId") == batch_id, "model scope belongs to another batch")
    require(digest(scope.get("responseSha256")), "model scope needs original response SHA-256")
    start, end = date.fromisoformat(scope["startDate"]), date.fromisoformat(scope["cutoff"])
    require(start <= end, "inverted model date window")
    require(bool(scope.get("sourceUrl")) and bool(scope.get("selectionPolicy")), "missing scope provenance")
    datetime.fromisoformat(scope["retrievedAt"].replace("Z", "+00:00"))
    models = unique_index(scope["models"], "scope model")
    require(bool(models), "empty model scope")
    for model in models.values():
        require(bool(model.get("name")), "scope model needs a name")
        value = model["releaseDate"]
        if re.fullmatch(r"\d{4}-\d{2}", value):
            from calendar import monthrange
            year, month = map(int, value.split("-"))
            low, high = date(year, month, 1), date(year, month, monthrange(year, month)[1])
        else:
            low = high = date.fromisoformat(value)
        require(start <= low <= high <= end, f"{model['id']}: release date outside fixed window")
    require(isinstance(scope.get("dateIssues"), list), "scope must record date issues")
    check_urls(scope)
    return models


def baseline_check(root: Path, baseline: dict, catalog, batch_id: str,
                   check_external: bool) -> list[dict]:
    require(type(baseline.get("schemaVersion")) is int and baseline["schemaVersion"] == 1,
            "invalid baseline schemaVersion")
    require(baseline.get("batchId") == batch_id, "baseline belongs to another batch")
    current = unique_index(catalog.results, "result")
    for item in baseline["maintenanceResults"]:
        require(current.get(item["id"]) == item, f"protected maintenance result changed: {item['id']}")
    for key in ("benchmarks", "sources", "mappings"):
        for item in baseline["maintenanceEntities"][key]:
            require(getattr(catalog, key).get(item["id"]) == item,
                    f"protected {key} entity changed: {item['id']}")
    unique_index(baseline["maintenanceResults"], "baseline result")
    android = baseline["androidSnapshot"]
    require(digest(android.get("sha256")), "Android baseline needs SHA-256")
    validate_snapshot({"schemaVersion": 1, "version": android["version"], "scores": android["scores"]}, root)
    checks = []
    seen = set()
    for item in baseline["protectedFiles"]:
        relative = item["path"]
        require(relative not in seen, f"duplicate protected file: {relative}")
        seen.add(relative)
        require(digest(item.get("sha256")), f"invalid protected digest: {relative}")
        external = relative.startswith("../model-atlas-android/")
        relative_path = Path(relative)
        allowed_parts = relative_path.parts[2:] if external else relative_path.parts
        require(not relative_path.is_absolute() and ".." not in allowed_parts,
                f"invalid protected path: {relative}")
        path = root / relative
        allowed_root = root.parent / "model-atlas-android" if external else root
        require(not path.is_symlink() and path.resolve().is_relative_to(allowed_root.resolve()),
                f"protected path escapes allowed repository: {relative}")
        if external and not check_external:
            checks.append({"path": relative, "status": "not-checked", "reason": "use --check-android with sibling checkout"})
            continue
        require(path.is_file(), f"protected file missing: {relative}")
        require(sha256(path.read_bytes()) == item["sha256"], f"protected file changed: {relative}")
        if relative == android["path"]:
            require(item["sha256"] == android["sha256"], "Android baseline hashes differ")
            live = read_json(path)
            require(live["version"] == android["version"] and live["scores"] == android["scores"],
                    "Android baseline does not match protected snapshot")
        checks.append({"path": relative, "status": "verified"})
    require(android["path"] in seen, "Android snapshot must be a protected file")
    return checks


def review_candidates(root: Path, batch_path: Path, check_android: bool = False) -> dict:
    try:
        return _review_candidates(root, batch_path, check_android)
    except DataError:
        raise
    except (KeyError, TypeError, ValueError, AttributeError) as error:
        raise DataError(f"invalid review attachment: {error}") from error


def _review_candidates(root: Path, batch_path: Path, check_android: bool = False) -> dict:
    root, batch_path = root.resolve(), batch_path.resolve()
    require(batch_path.is_relative_to(root / "data" / "reviews"), "batch must be under data/reviews/")
    batch = read_json(batch_path)
    validate_schema(batch, "candidate-review.schema.json", root)
    directory = batch_path.parent
    scope = read_json(attachment(directory, batch["scopeFile"]))
    models = model_scope(scope, batch["id"])
    baseline = read_json(attachment(directory, batch["baselineFile"]))
    catalog = load_catalog(root)
    checks = baseline_check(root, baseline, catalog, batch["id"], check_android)
    targets, evidence, systems = [], [], []
    for relative in batch["evidenceFiles"]:
        document = read_json(attachment(directory, relative))
        check_urls(document)
        targets.extend(document["targets"])
        evidence.extend(document["evidence"])
        systems.extend(document["systemOnly"])
    target_index = unique_index(targets, "review target")
    require(set(target_index) == set(batch["targetIds"]), "target coverage does not match batch")
    unique_index(evidence, "evidence")
    benchmark_targets = {}
    evidence_sources = set()
    for entry in evidence:
        require(entry["sourceId"] in catalog.sources, f"unknown evidence source: {entry['sourceId']}")
        require(bool(entry.get("url")) and bool(entry.get("locator")) and bool(entry.get("excerpt")),
                f"{entry['id']}: incomplete evidence")
        require(entry.get("responseSha256") is None or digest(entry["responseSha256"]),
                f"{entry['id']}: invalid response digest")
        datetime.fromisoformat(entry["retrievedAt"].replace("Z", "+00:00"))
        evidence_sources.add(entry["sourceId"])
    for target in targets:
        require(target["status"] in ("collected", "blocked"), "invalid investigation status")
        require(bool(target["notes"]) and bool(target["officialUrls"]) and bool(target["searches"]),
                f"{target['id']}: missing investigation coverage")
        for search in target["searches"]:
            require(type(search["tier"]) is int and search["tier"] in (1, 2, 3, 4), "invalid source priority")
            require(bool(search["url"]) and bool(search["outcome"]), "missing search outcome")
        for benchmark_id in target["benchmarkIds"]:
            require(benchmark_id in catalog.benchmarks, f"unknown target benchmark: {benchmark_id}")
            require(benchmark_id not in benchmark_targets, f"benchmark assigned to multiple targets: {benchmark_id}")
            benchmark_targets[benchmark_id] = target["id"]
    all_results = unique_index(catalog.results, "result")
    old_ids = {row["id"] for row in baseline["maintenanceResults"]}
    candidate_ids = set(batch["candidateResultIds"])
    require(not old_ids & candidate_ids, "old baseline results cannot be new candidates")
    # Explicit membership avoids silently including the three pending legacy rows.
    new_ids = set(all_results) - old_ids
    require(candidate_ids == new_ids, "batch must account for every new maintenance result")
    candidates = []
    counts = Counter()
    represented_models = set()
    for result_id in sorted(candidate_ids):
        result = all_results[result_id]
        require(result["status"] == "pending", f"{result_id}: candidate must remain pending")
        require(result["benchmarkId"] in benchmark_targets, f"{result_id}: outside target benchmark list")
        benchmark = catalog.benchmarks[result["benchmarkId"]]
        source = catalog.sources[result["sourceId"]]
        mapping = catalog.mappings[result["mappingId"]]
        require(all(entity["status"] == "pending" for entity in (benchmark, source, mapping)),
                f"{result_id}: candidate dependencies must remain pending")
        require(source["id"] in evidence_sources, f"{result_id}: source evidence missing")
        model_id = mapping["modelId"]
        require(model_id is None or model_id in models, f"{result_id}: model outside frozen scope")
        blockers = ["maintenance-review-pending"]
        if not model_id or not mapping["evidenceUrl"] or not mapping["catalogUrl"]:
            blockers.append("model-identity-unconfirmed")
        license_info = source["license"]
        if license_info["redistribution"] != "allowed" or not all(license_info[key] for key in ("name", "url", "licenseFile")):
            blockers.append("redistribution-and-client-attribution-unconfirmed")
        if result["unrepresentedConditions"]:
            blockers.append("essential-conditions-not-representable-in-android-v1")
        target_id = benchmark_targets[benchmark["id"]]
        if model_id:
            represented_models.add(model_id)
            counts[model_id, target_id] += 1
        candidates.append({
            "result": result, "modelId": model_id, "sourceModelName": mapping["sourceModelName"],
            "targetId": target_id, "benchmark": benchmark, "source": source,
            "mapping": mapping, "blockers": blockers,
        })
    coverage = []
    for target_id in batch["targetIds"]:
        target = target_index[target_id]
        rows = [row for row in candidates if row["targetId"] == target_id]
        require((target["status"] == "collected") == bool(rows), f"{target_id}: investigation status contradicts candidate count")
        coverage.append({**target, "candidateCount": len(rows),
                         "matchedModelCount": len({row["modelId"] for row in rows if row["modelId"]})})
    android_ids = {row["id"] for row in baseline["androidSnapshot"]["scores"]}
    return {
        "mode": "candidate-only", "deployable": False, "actualChangesApplied": False,
        "batchId": batch["id"], "notes": batch["notes"],
        "scope": {key: scope[key] for key in ("sourceUrl", "responseSha256", "retrievedAt", "startDate", "cutoff", "dateIssues")},
        "summary": {"scopeModels": len(models), "investigatedTargets": len(coverage),
                    "candidateResults": len(candidates), "modelsWithCandidates": len(represented_models),
                    "unmappedCandidates": sum(row["modelId"] is None for row in candidates),
                    "systemOnlyRecords": len(systems), "approvedNewResults": 0},
        "maintenanceDiff": {"hypothetical": True, "beforeCount": len(old_ids),
                            "afterCandidateCount": len(candidates), "wouldRemove": sorted(old_ids),
                            "wouldAddPending": sorted(candidate_ids)},
        "androidDiff": {"hypothetical": True, "baselineKind": "bundled-assets-not-live-server",
                        "baselineVersion": baseline["androidSnapshot"]["version"],
                        "baselineSha256": baseline["androidSnapshot"]["sha256"],
                        "beforeCount": len(android_ids), "wouldRemove": sorted(android_ids),
                        "wouldConsiderAdding": sorted(candidate_ids),
                        "warning": "Not a wire snapshot: unresolved identity, licensing and protocol blockers must be reviewed before any export."},
        "coverage": coverage,
        "modelCoverage": [{**model, "targets": {
            target_id: {"candidateCount": counts[model_id, target_id],
                        "status": "candidate-found" if counts[model_id, target_id] else "not-collected",
                        "note": None if counts[model_id, target_id] else "本轮列明来源未收录；不是穷尽全网后认定无成绩。"}
            for target_id in batch["targetIds"]}} for model_id, model in sorted(models.items())],
        "candidates": candidates, "evidence": evidence, "systemOnly": systems,
        "protectedFiles": checks,
    }


def markdown(report: dict) -> str:
    def cell(value):
        return str(value if value is not None else "未知").replace("|", "\\|").replace("\n", " ")

    summary = report["summary"]
    lines = ["# Benchmark 候选替换预览", "", "**candidate-only：未批准、不可部署、未执行任何替换。**", "",
             f"批次：`{report['batchId']}`；模型发布日期窗口：{report['scope']['startDate']}～{report['scope']['cutoff']}（含两端）。",
             f"范围 {summary['scopeModels']} 个模型 ID、{summary['investigatedTargets']} 项；收录 {summary['candidateResults']} 条 pending 成绩，明确关联 {summary['modelsWithCandidates']} 个模型。", "",
             "所有原始指标保持原单位；不同版本／Agent／工具／预算不合并，不取最高分，不生成综合排名。",
             "没有候选仅表示本轮已列明来源未收录，不表示已逐模型穷尽全网。", "",
             "## 假设替换影响", "",
             "维护层和 Android 随包为两个不同基线；本报告不是线上站点验收。", "",
             "### 维护层拟移出（当前文件及审核状态均未改动）", ""]
    lines.extend(f"- `{result_id}`" for result_id in report["maintenanceDiff"]["wouldRemove"])
    lines.extend(["", f"### Android 随包 v{report['androidDiff']['baselineVersion']} 拟移出（未改 assets／设备）", ""])
    lines.extend(f"- `{result_id}`" for result_id in report["androidDiff"]["wouldRemove"])
    lines.extend(["", "候选拟加入集合见下表及 JSON 的 `candidates`。**并非全部可直接导出 Android**；无发布清单、无目标内容版本。", "",
                  "## 十一项调查覆盖", "", "| 项目 | 候选成绩 | 已关联模型 | 调查结论 |", "| --- | ---: | ---: | --- |"])
    for target in report["coverage"]:
        lines.append(f"| {cell(target['id'])} | {target['candidateCount']} | {target['matchedModelCount']} | {cell(target['notes'])} |")
    lines.extend(["", "## 原始候选成绩（全部 pending）", "",
                  "| 结果 ID | 规范模型 ID | 评测及版本 | 原值／指标／单位 | 配置 | 出处定位 | 阻塞 |",
                  "| --- | --- | --- | --- | --- | --- | --- |"])
    for row in report["candidates"]:
        result, benchmark = row["result"], row["benchmark"]
        fields = [result["id"], row["modelId"], f"{benchmark['name']} / {benchmark['version']}",
                  f"{result['score']} / {benchmark['metric']} / {benchmark['unit']}",
                  f"subset={result['subset']}; harness={result['harness']}; reasoning={result['reasoningEffort']}; tools={result['toolsEnabled']}",
                  f"{row['source']['url']} — {result['sourceLocator']}", "; ".join(row["blockers"])]
        lines.append("| " + " | ".join(cell(field) for field in fields) + " |")
    lines.extend(["", "## 模型覆盖矩阵", "", "零表示本轮未收录，不是模型分数为零。", "",
                  "| 模型 ID | " + " | ".join(target["id"] for target in report["coverage"]) + " |",
                  "| --- | " + " | ".join("---:" for _ in report["coverage"]) + " |"])
    for model in report["modelCoverage"]:
        lines.append("| " + cell(model["id"]) + " | " + " | ".join(str(value["candidateCount"]) for value in model["targets"].values()) + " |")
    lines.extend(["", "## 检索记录与缺口", ""])
    for target in report["coverage"]:
        lines.extend([f"### {target['id']}", ""])
        for search in target["searches"]:
            lines.append(f"- 来源优先级 {search['tier']}：{search['url']} — {search['outcome']}")
        lines.append("")
    lines.extend(["## 仅系统级记录", "", "多模型 fallback 不作为单个模型的候选成绩。完整原文依据及原因见 JSON 的 `systemOnly`。", "",
                  f"本轮记录 {summary['systemOnlyRecords']} 项。", "", "## 保护校验", ""])
    lines.extend(f"- `{entry['path']}`：{entry['status']}" for entry in report["protectedFiles"])
    lines.extend(["", "证据索引、精确模型映射及无法由 Android v1 表达的条件详见 JSON。公开可读不等于获准再分发。", ""])
    return "\n".join(lines)


def write_preview(root: Path, batch_path: Path, output: Path, check_android: bool = False) -> dict:
    root = root.resolve()
    output = output.absolute()
    require(not output.is_symlink() and output.resolve().is_relative_to(root / "build"),
            "candidate reports must be under repository build/")
    require(output.resolve() != root / "build", "use a dedicated candidate report directory")
    report = review_candidates(root, batch_path, check_android)
    # Never write manifest.json, scores-v*.json, release config or source data.
    for name in ("report.json", "report.md"):
        path = output / name
        require(not path.is_symlink() and path.resolve().is_relative_to((root / "build").resolve()),
                f"report output escapes build/: {path}")
    output.mkdir(parents=True, exist_ok=True)
    (output / "report.json").write_bytes(json_bytes(report))
    (output / "report.md").write_text(markdown(report), encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", type=Path, default=ROOT / "data/reviews/2026-10-28/batch.json")
    parser.add_argument("--output", type=Path, default=ROOT / "build/candidate-review-2026-10-28")
    parser.add_argument("--check-android", action="store_true", help="also verify protected files in sibling Android checkout")
    parser.add_argument("--check", action="store_true", help="validate review only, without writing reports")
    args = parser.parse_args()
    try:
        report = review_candidates(ROOT, args.batch, args.check_android) if args.check else write_preview(ROOT, args.batch, args.output, args.check_android)
        print(f"OK: candidate-only, {report['summary']['candidateResults']} pending results, no approval/export/deployment")
        if not args.check:
            print(f"Reports: {args.output / 'report.md'} and report.json")
        return 0
    except (DataError, OSError, KeyError, TypeError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
