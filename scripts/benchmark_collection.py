"""Generate benchmark collection progress documents from source TOML and model notes."""

from __future__ import annotations

import argparse
from calendar import monthrange
from datetime import date, datetime
import json
from pathlib import Path
import re
import tomllib
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "benchmark-collection"
MODEL_DOCS = DOCS / "models"
STATE_START = "<!-- benchmark-collection-state\n"
STATE_END = "\n-->"
RUN_START = "<!-- benchmark-collection-run\n"
RUN_END = "\n-->"
BENCHMARK_IDS = (
    "deepswe-v1.1",
    "swe-bench-pro-v2",
    "terminal-bench-v4",
    "terminal-bench-science-v0.1",
    "automationbench-v1.0.6",
    "osworld-v2.1",
    "chartography",
    "humanitys-last-exam",
    "artificial-analysis-intelligence-index-v5",
    "gdpval-aa-v2.1",
    "vals-index-v2.2",
)
DONE = {"已收录", "已存在", "未找到", "不适用"}
REVIEW = {"待核实", "冲突", "检查失败"}
FIRST_PASS_REVIEW = {"待核实", "冲突"}
SYMBOL = {
    "已收录": "✅", "已存在": "✅", "未找到": "❌", "检索中": "⏳",
    "待核实": "⏳", "冲突": "⚠️", "检查失败": "⚠️", "不适用": "➖", "未检查": "—",
}


def now_local() -> str:
    return datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="minutes")


def cell(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def model_doc_path(model_id: str) -> Path:
    lab, model = model_id.split("/", 1)
    return MODEL_DOCS / lab / f"{model}.md"


def read_state(path: Path) -> dict | None:
    if not path.is_file():
        return None
    content = path.read_text(encoding="utf-8")
    try:
        start = content.index(STATE_START) + len(STATE_START)
        end = content.index(STATE_END, start)
        result = json.loads(content[start:end])
    except (ValueError, json.JSONDecodeError) as error:
        raise ValueError(f"{path}: missing or invalid state block: {error}") from error
    if not isinstance(result, dict) or not isinstance(result.get("benchmarks"), dict):
        raise ValueError(f"{path}: state block must contain benchmarks")
    return result


def read_run_state() -> dict:
    path = DOCS / "STATUS.md"
    if not path.is_file():
        return {}
    content = path.read_text(encoding="utf-8")
    try:
        start = content.index(RUN_START) + len(RUN_START)
        end = content.index(RUN_END, start)
        result = json.loads(content[start:end])
        return result if isinstance(result, dict) else {}
    except (ValueError, json.JSONDecodeError):
        return {}


def load_sources():
    definitions = {}
    for path in sorted((ROOT / "benchmarks").glob("*.toml")):
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        definitions[data["id"]] = data

    models = []
    for path in (ROOT / "models").glob("*/*.toml"):
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        data["_id"] = f"{path.parent.name}/{path.stem}"
        data["_path"] = path
        models.append(data)
    dated = {}
    undated = []
    for model in models:
        release = model.get("release_date")
        if release is None:
            undated.append(model)
        else:
            dated.setdefault(release, []).append(model)
    models = []
    for release in sorted(dated, reverse=True):
        models.extend(sorted(dated[release], key=lambda item: item["_id"]))
    models.extend(sorted(undated, key=lambda item: item["_id"]))

    missing = set(BENCHMARK_IDS) - definitions.keys()
    if missing:
        raise ValueError(f"missing Benchmark definitions: {', '.join(sorted(missing))}")
    states = {model["_id"]: read_state(model_doc_path(model["_id"])) for model in models}
    return models, definitions, states


def window_members(models: list[dict], scope: dict | None) -> tuple[set[str], int, int]:
    if not scope:
        return set(), 0, 0
    first = date.fromisoformat(scope["from"])
    last = date.fromisoformat(scope["through"])
    member_ids: set[str] = set()
    precise = ambiguous = 0
    for model in models:
        release = model.get("release_date")
        if not isinstance(release, str):
            continue
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", release):
            released = date.fromisoformat(release)
            if first <= released <= last:
                member_ids.add(model["_id"])
                precise += 1
        elif re.fullmatch(r"\d{4}-\d{2}", release):
            year, month = map(int, release.split("-"))
            month_start = date(year, month, 1)
            month_end = date(year, month, monthrange(year, month)[1])
            if month_start <= last and month_end >= first:
                member_ids.add(model["_id"])
                ambiguous += 1
        elif re.fullmatch(r"\d{4}", release):
            year = int(release)
            year_start = date(year, 1, 1)
            year_end = date(year, 12, 31)
            if year_start <= last and year_end >= first:
                member_ids.add(model["_id"])
                ambiguous += 1
    return member_ids, precise, ambiguous


def matches(model: dict, definition: dict) -> list[dict]:
    if definition.get("version") == "unspecified":
        return [record for record in model.get("benchmarks", [])
                if record.get("name") == definition.get("name")
                and record.get("metric") == definition.get("metric")
                and record.get("version") in (None, "unspecified")]
    accepted_versions = {definition.get("version"), *definition.get("compatible_versions", [])}
    return [record for record in model.get("benchmarks", [])
            if record.get("name") == definition.get("name")
            and record.get("metric") == definition.get("metric")
            and record.get("version") in accepted_versions]


def related_records(model: dict, definition: dict) -> list[dict]:
    """Return raw source rows with this benchmark name, even if mapping needs review."""
    return [record for record in model.get("benchmarks", [])
            if record.get("name") == definition.get("name")]


def overall_status(state: dict | None) -> str:
    if not state:
        return "未开始"
    if state.get("overall_status") in {"进行中", "处理失败"}:
        return state["overall_status"]
    statuses = [state.get("benchmarks", {}).get(bid, {}).get("status", "未检查")
                for bid in BENCHMARK_IDS]
    if all(status in DONE for status in statuses):
        return "已完成"
    if all(status in DONE | REVIEW for status in statuses):
        return "待复核"
    if any(status in DONE | REVIEW for status in statuses):
        return "部分完成"
    return "未开始"


def first_pass_completed(state: dict | None) -> bool:
    if not state:
        return False
    return all(state.get("benchmarks", {}).get(bid, {}).get("status", "未检查")
               in DONE | FIRST_PASS_REVIEW for bid in BENCHMARK_IDS)


def score_summary(records: list[dict]) -> str:
    rendered = []
    for record in records:
        conditions = [f"{key}={record[key]}" for key in
                      ("metric", "version", "dataset", "effort", "variant", "harness") if key in record]
        rendered.append(str(record.get("score", "?")) +
                        (f" ({'; '.join(conditions)})" if conditions else ""))
    return "; ".join(rendered) if rendered else "—"


def render_model_doc(model: dict, state: dict, definitions: dict) -> str:
    model_id = model["_id"]
    state["model_id"] = model_id
    state.setdefault("benchmarks", {})
    state["overall_status"] = overall_status(state)
    state["first_pass_completed"] = first_pass_completed(state)
    record_count = sum(len(matches(model, definitions[bid])) for bid in BENCHMARK_IDS)
    lines = [
        f"# {cell(model.get('name', model_id))} Benchmark 收集记录",
        "",
        "文末 JSON 状态块是本模型的可恢复记录；本页状态表由该记录和模型源 TOML 派生。",
        "",
        "## 基本信息",
        "",
        f"- 模型 ID：{model_id}",
        f"- 模型名称：{model.get('name', model_id)}",
        f"- 发布日期：{model.get('release_date', '未提供')}",
        f"- 最近检查时间：{state.get('last_checked', '尚未检查')}",
        f"- 整体处理状态：{state['overall_status']}",
        f"- 新增成绩数量：{state.get('new_records', 0)}",
        f"- 更新成绩数量：{state.get('updated_records', 0)}",
        f"- 收集前已有成绩数量：{state.get('existing_records', 0)}",
        f"- 当前已收录的对应成绩数量：{record_count}",
        "",
    ]
    if state.get("model_notes"):
        lines.extend(["## 模型身份与范围说明", ""])
        lines.extend(f"- {cell(note)}" for note in state["model_notes"])
        lines.append("")
    lines.extend([
        "## 11 项 Benchmark 状态",
        "",
        "| Benchmark ID | 状态 | 成绩 | 来源 | 最近检查 |",
        "|---|---|---|---|---|",
    ])
    for bid in BENCHMARK_IDS:
        info = state["benchmarks"].get(bid, {})
        records = related_records(model, definitions[bid])
        sources = info.get("checked_sources", [])
        if not sources:
            sources = [{"url": record["source"]} for record in records if record.get("source")]
        source_text = ", ".join(f"[{cell(item.get('label', item.get('url', '来源')))}]({item.get('url', '')})"
                                for item in sources if item.get("url")) or "—"
        lines.append(f"| {bid} | {info.get('status', '未检查')} | {cell(score_summary(records))} | "
                     f"{source_text} | {info.get('checked_at') or '—'} |")

    lines.extend(["", "## 详细研究记录", ""])
    for bid in BENCHMARK_IDS:
        definition = definitions[bid]
        info = state["benchmarks"].get(bid, {})
        records = related_records(model, definition)
        mapped_records = matches(model, definition)
        lines.extend([f"### {definition['name']} ({bid})", ""])
        if records:
            for index, record in enumerate(records, start=1):
                lines.extend([f"#### 源 TOML 成绩记录 {index}", ""])
                for field in ("name", "score", "metric", "version", "dataset", "effort",
                              "variant", "harness", "source", "date"):
                    if field in record:
                        value = record[field]
                        value = f"[{value}]({value})" if field == "source" else cell(value)
                        lines.append(f"- {field}: {value}")
                if record in mapped_records:
                    lines.append("- 本地 Benchmark 定义映射：已匹配")
                else:
                    lines.append("- 本地 Benchmark 定义映射：待核实（覆盖率统计不计入该行）")
                lines.append("")
        elif info.get("status") == "未找到":
            lines.extend(["- 结论：未找到公开成绩。", ""])
        elif info.get("status") == "不适用":
            lines.extend(["- 结论：不适用。", ""])
        else:
            lines.extend([f"- 当前状态：{info.get('status', '未检查')}。", ""])

        if info.get("checked_sources"):
            lines.append("已检查的主要资料：")
            for item in info["checked_sources"]:
                lines.append(f"- [{cell(item.get('label', item['url']))}]({item['url']})")
            lines.append("")
        if info.get("notes"):
            lines.append("研究备注：")
            lines.extend(f"- {cell(note)}" for note in info["notes"])
            lines.append("")
        if info.get("unresolved"):
            lines.append("尚未解决的问题：")
            lines.extend(f"- {cell(issue)}" for issue in info["unresolved"])
            lines.append("")
        if info.get("checked_at"):
            lines.extend([f"最近核验时间：{info['checked_at']}", ""])
    lines.extend([
        STATE_START.rstrip("\n"),
        json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2),
        STATE_END,
    ])
    return "\n".join(lines).rstrip() + "\n"


def write_model_doc(model_id: str, state: dict) -> None:
    models, definitions, _ = load_sources()
    model = next((item for item in models if item["_id"] == model_id), None)
    if model is None:
        raise ValueError(f"unknown model ID: {model_id}")
    path = model_doc_path(model_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(render_model_doc(model, state, definitions), encoding="utf-8", newline="\n")


def refresh() -> None:
    models, definitions, states = load_sources()
    now = now_local()
    total = len(models)
    statuses = {name: sum(overall_status(states[m["_id"]]) == name for m in models)
                for name in ("未开始", "进行中", "已完成", "部分完成", "待复核", "处理失败")}
    first_pass_complete = sum(first_pass_completed(states[m["_id"]]) for m in models)
    existing_models = sum(bool(model.get("benchmarks")) for model in models)
    record_total = sum(len(model.get("benchmarks", [])) for model in models)
    run_state = read_run_state()
    scope = run_state.get("scope")
    scope_ids, scope_precise, scope_ambiguous = window_members(models, scope)
    scope_completed = sum(first_pass_completed(states[model["_id"]])
                          for model in models if model["_id"] in scope_ids)
    issue_models = sum(
        any((states[m["_id"]] or {}).get("benchmarks", {}).get(bid, {}).get("status") in REVIEW
            for bid in BENCHMARK_IDS)
        for m in models
    )

    overview = [
        "# Benchmark 收集总览", "",
        "统计由模型源 TOML、Benchmark 定义和单模型状态文档生成。覆盖率计入名称和指标匹配且版本精确一致或明确列入定义兼容版本的成绩；定义标为 unspecified 时，源记录可省略 version。", "",
        "## 总体统计", "",
        "| 指标 | 数值 |", "|---|---:|",
        f"| 模型总数 | {total} |",
        f"| 已完成首轮检查 | {first_pass_complete} |",
        f"| 正在处理 | {statuses['进行中']} |",
        f"| 尚未处理 | {statuses['未开始']} |",
        f"| 存在待核实问题的模型 | {issue_models} |",
        f"| 整体状态为待复核的模型 | {statuses['待复核']} |",
        f"| 已有 Benchmark 成绩的模型 | {existing_models} |",
        f"| 已收录的原始成绩条数 | {record_total} |",
        f"| Benchmark 定义总数 | {len(definitions)} |",
        f"| 最后更新时间 | {now}（Asia/Shanghai） |", "",
        "首轮检查完成表示 11 项都已尝试并形成结果；其中待核实或冲突的模型仍显示待复核。模型处理进度、Benchmark 检查进度与成绩覆盖率分别按队列状态、单模型状态和源 TOML 统计。", "",
        "## 11 项 Benchmark 覆盖统计", "",
        "已检查模型计入已收录、已存在、未找到、不适用等完成核验状态。待核实、冲突和失败单独列出。待检查表示尚未尝试；覆盖率 = 已收录模型 / 模型总数。", "",
        "| Benchmark | 已收录模型 | 已检查模型 | 待检查模型 | 检索中 | 待复核/失败 | 收录覆盖率 |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for bid in BENCHMARK_IDS:
        definition = definitions[bid]
        included = checked = review = active = 0
        for model in models:
            state = states[model["_id"]] or {}
            status = state.get("benchmarks", {}).get(bid, {}).get("status", "未检查")
            included += bool(matches(model, definition))
            checked += status in DONE
            review += status in REVIEW
            active += status == "检索中"
        pending = total - checked - review - active
        coverage = 100 * included / total if total else 0
        overview.append(f"| {definition['name']} ({bid}) | {included} | {checked} | {pending} | "
                        f"{active} | {review} | {coverage:.1f}% |")

    overview.extend([
        "", "## 全模型 Benchmark 状态矩阵", "",
        "图例：✅ 已收录或已核实存在；❌ 已检查未找到公开成绩；⏳ 正在检索或待核实；⚠️ 冲突或检查失败；➖ 不适用；— 尚未检查。状态来自单模型详细文档；表格不显示分数。", "",
        "| 模型 | 发布日期 | DeepSWE | SWE-Pro | TBench 4 | TBench Science | AutomationBench | OSWorld 2.1 | Chartography | HLE | AA Index V5 | GDPval-AA | Vals Index |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for model in models:
        state = states[model["_id"]]
        doc = model_doc_path(model["_id"])
        display = f"{cell(model.get('name', model['_id']))} ({model['_id']})"
        name = f"[{display}]({doc.relative_to(DOCS).as_posix()})" if state and doc.is_file() else display
        values = []
        for bid in BENCHMARK_IDS:
            status = (state or {}).get("benchmarks", {}).get(bid, {}).get("status", "未检查")
            values.append(SYMBOL.get(status, "—"))
        overview.append("| " + " | ".join([name, model.get("release_date", "未提供"), *values]) + " |")

    concerns = []
    for model in models:
        state = states[model["_id"]]
        if not state:
            continue
        notes = []
        for bid in BENCHMARK_IDS:
            info = state.get("benchmarks", {}).get(bid, {})
            if info.get("status") in REVIEW:
                text = f"{definitions[bid]['name']}: {info['status']}"
                if info.get("unresolved"):
                    text += " — " + "; ".join(info["unresolved"])
                notes.append(cell(text))
        if notes:
            path = model_doc_path(model["_id"])
            title = f"[{cell(model.get('name', model['_id']))} ({model['_id']})]({path.relative_to(DOCS).as_posix()})"
            concerns.append(f"- {title} — " + "; ".join(notes))
    overview.extend(["", "## 需要关注的问题", ""])
    overview.extend(concerns or ["- 目前没有记录待核实、冲突或检查失败的问题。"])
    overview_text = "\n".join(overview).rstrip() + "\n"

    active_models = [m["_id"] for m in models if overall_status(states[m["_id"]]) == "进行中"]
    current = active_models[0] if active_models else None
    unfinished_scope = any(
        model["_id"] in scope_ids and not first_pass_completed(states[model["_id"]])
        for model in models
    )
    next_candidate = next(
        (model["_id"] for model in models
         if (not unfinished_scope or model["_id"] in scope_ids)
         and overall_status(states[model["_id"]]) != "进行中"
         and not first_pass_completed(states[model["_id"]])),
        None,
    )
    next_model = next_candidate or (
        "当前优先范围模型处理中" if unfinished_scope else
        "当前批次仍在处理中" if active_models else
        "无（队列首轮已完成）"
    )
    run_state.setdefault("last_execution", "未记录")
    run_state["current_model"] = current
    run_state["current_models"] = active_models
    status = [
        RUN_START.rstrip("\n"), json.dumps(run_state, ensure_ascii=False, sort_keys=True, indent=2), RUN_END,
        "# Benchmark 收集任务队列与断点", "",
        f"模型总数：{total}<br>",
        f"已完成首轮检查：{first_pass_complete}<br>",
        f"待处理（尚未开始）：{statuses['未开始']}<br>",
        f"失败或中断：{statuses['处理失败']}<br>",
        f"最近执行时间：{run_state['last_execution']}<br>",
        f"当前正在处理：{', '.join(active_models) if active_models else '无'}<br>",
        f"下一待处理模型：{next_model}", "",
    ]
    if scope:
        scope_total = len(scope_ids)
        status.extend([
            f"本轮 release_date 范围：{scope['from']} 至 {scope['through']}<br>",
            f"范围候选模型：{scope_total}（精确日期 {scope_precise}，日期精度不足而保守纳入 {scope_ambiguous}）<br>",
            f"范围首轮完成：{scope_completed}<br>",
            f"范围待处理：{scope_total - scope_completed}",
            "",
        ])
    status.extend([
        "队列按 release_date 从新到旧；同日按模型 ID 字典序；缺少发布日期的模型置末。首轮检查完成要求 11 项都已尝试且无检查失败；待核实或冲突项会使模型状态保持待复核。已完成表示 11 项核验全部结束，不要求每项都有成绩。队列表中的已检查项目表示已尝试核验，包含待核实、冲突和失败项。", "",
        "| 模型 ID | 发布日期 | 处理状态 | 已检查项目 | 最近检查 |",
        "|---|---|---|---:|---|",
    ])
    for model in models:
        state = states[model["_id"]]
        doc = model_doc_path(model["_id"])
        model_id = model["_id"]
        label = f"[{model_id}]({doc.relative_to(DOCS).as_posix()})" if state and doc.is_file() else model_id
        checked = sum((state or {}).get("benchmarks", {}).get(bid, {}).get("status") in DONE | REVIEW | {"检查失败"}
                      for bid in BENCHMARK_IDS)
        last = (state or {}).get("last_checked", "—")
        status.append(f"| {label} | {model.get('release_date', '未提供')} | {overall_status(state)} | {checked}/11 | {last} |")

    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / "OVERVIEW.md").write_text(overview_text, encoding="utf-8", newline="\n")
    (DOCS / "STATUS.md").write_text("\n".join(status).rstrip() + "\n", encoding="utf-8", newline="\n")
    print(f"已刷新 OVERVIEW.md 和 STATUS.md：{total} 个模型，{len(definitions)} 个 Benchmark 定义")


def initialize_model(model_id: str, timestamp: str) -> None:
    models, _, states = load_sources()
    if model_id not in states:
        raise ValueError(f"unknown model ID: {model_id}")
    if states[model_id]:
        raise ValueError(f"model document already exists: {model_doc_path(model_id)}")
    state = {
        "model_id": model_id,
        "overall_status": "进行中",
        "last_checked": timestamp,
        "new_records": 0,
        "benchmarks": {
            bid: {
                "status": "检索中",
                "checked_at": None,
                "checked_sources": [],
                "notes": [],
                "unresolved": [],
            }
            for bid in BENCHMARK_IDS
        },
    }
    write_model_doc(model_id, state)
    run = read_run_state()
    run.update({"last_execution": timestamp, "current_model": model_id})
    write_run_state(run)


def write_run_state(run: dict) -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    path = DOCS / "STATUS.md"
    content = path.read_text(encoding="utf-8") if path.exists() else "# Benchmark 收集任务队列与断点\n"
    block = RUN_START + json.dumps(run, ensure_ascii=False, sort_keys=True, indent=2) + RUN_END
    if RUN_START in content:
        start = content.index(RUN_START)
        end = content.index(RUN_END, start) + len(RUN_END)
        content = content[:start] + block + content[end:]
    else:
        content = block + "\n" + content
    path.write_text(content, encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="regenerate OVERVIEW.md and STATUS.md")
    parser.add_argument("--init-model", help="create an in-progress detail document for a model ID")
    parser.add_argument("--render-model", help="regenerate one detail document from its state block and source TOML")
    parser.add_argument("--mark-run", help="record the model handled by this execution and its timestamp")
    parser.add_argument("--scope-from", help="inclusive release_date window start (YYYY-MM-DD)")
    parser.add_argument("--scope-through", help="inclusive release_date window end (YYYY-MM-DD)")
    parser.add_argument("--timestamp", help="local timestamp; defaults to Asia/Shanghai now")
    args = parser.parse_args()
    if bool(args.scope_from) != bool(args.scope_through):
        parser.error("--scope-from and --scope-through must be supplied together")
    if args.scope_from and args.scope_through:
        run = read_run_state()
        run["scope"] = {"from": args.scope_from, "through": args.scope_through}
        write_run_state(run)
    if args.mark_run:
        run = read_run_state()
        run.update({"last_execution": args.timestamp or now_local(), "current_model": args.mark_run})
        write_run_state(run)
    if args.init_model:
        initialize_model(args.init_model, args.timestamp or now_local())
    if args.render_model:
        path = model_doc_path(args.render_model)
        state = read_state(path)
        if state is None:
            raise ValueError(f"model detail state does not exist: {args.render_model}")
        write_model_doc(args.render_model, state)
    refresh()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
