#!/usr/bin/env python3
"""Update the open-weight model parameter collection and sync status ledger."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from datetime import date
import json
from pathlib import Path
import re
import sys
import tomllib


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DOC = Path("docs/model-parameters-status.md")

GENERATED_START = "<!-- parameters-status:begin -->"
GENERATED_END = "<!-- parameters-status:end -->"
MANUAL_START = "<!-- parameters-status:manual:begin -->"
MANUAL_END = "<!-- parameters-status:manual:end -->"

COLLECTED = "✅ 已收集"
PARTIAL = "⚠️ 待核实"
PENDING = "❌ 待收集"
UNDISCLOSED = "🔒 官方未披露"
NOT_APPLICABLE = "➖ 不适用"
COLLECTION_STATUSES = (COLLECTED, PARTIAL, PENDING, UNDISCLOSED, NOT_APPLICABLE)

SYNC_PENDING = "待写入"
SYNC_STORED = "已入库"
SYNC_BUILT = "已构建"
SYNC_PUBLISHED = "已发布"
SYNC_UNVERIFIED = "未核验"
SYNC_STATUSES = (SYNC_PENDING, SYNC_STORED, SYNC_BUILT, SYNC_PUBLISHED, SYNC_UNVERIFIED)


@dataclass
class Model:
    model_id: str
    release_date: str | None
    parameters: dict
    total: float | int | None
    active: float | int | None
    components: list
    sources: list[str]
    has_notes: bool

    @property
    def has_parameters(self):
        return bool(self.parameters)


def load_models(root):
    models_dir = root / "models"
    if not models_dir.is_dir():
        raise ValueError(f"{models_dir}: models directory not found")
    paths = sorted(models_dir.rglob("*.toml"))
    if not paths:
        raise ValueError(f"{models_dir}: no model TOML files found")

    models = []
    for path in paths:
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, tomllib.TOMLDecodeError) as error:
            raise ValueError(f"{path}: {error}") from error
        if data.get("open_weights") is not True:
            continue

        metadata = data.get("metadata", {})
        if not isinstance(metadata, dict):
            raise ValueError(f"{path}: metadata must be a table")
        atlas = metadata.get("modelatlas", {})
        if not isinstance(atlas, dict):
            raise ValueError(f"{path}: metadata.modelatlas must be a table")
        parameters = atlas.get("parameters", {})
        if not isinstance(parameters, dict):
            raise ValueError(f"{path}: metadata.modelatlas.parameters must be a table")
        components = parameters.get("components", [])
        if not isinstance(components, list) or not all(isinstance(item, dict) for item in components):
            raise ValueError(f"{path}: metadata.modelatlas.parameters.components must be an array of tables")

        sources = []
        seen = set()
        for entry in [parameters, *components]:
            entry_sources = entry.get("sources", [])
            if not isinstance(entry_sources, list):
                raise ValueError(f"{path}: parameter sources must be an array")
            for source in entry_sources:
                if isinstance(source, str) and source not in seen:
                    seen.add(source)
                    sources.append(source)

        has_notes = bool(parameters.get("notes")) or any(
            bool(component.get("notes")) for component in components
        )
        release_date = data.get("release_date")
        if not isinstance(release_date, str) or not release_date:
            release_date = None

        model_id = path.relative_to(models_dir).with_suffix("").as_posix()
        models.append(Model(
            model_id=model_id,
            release_date=release_date,
            parameters=parameters,
            total=parameters.get("total_billion"),
            active=parameters.get("active_billion"),
            components=components,
            sources=sources,
            has_notes=has_notes,
        ))

    # Newest first; equal dates stay in model-id order instead of being reversed.
    models.sort(key=lambda model: model.model_id)
    models.sort(key=lambda model: model.release_date or "", reverse=True)
    return models, len(paths)


def load_overrides(text):
    pattern = re.compile(
        re.escape(MANUAL_START) + r"\s*```toml\s*\n(.*?)\n```\s*" + re.escape(MANUAL_END),
        re.DOTALL,
    )
    match = pattern.search(text)
    if match is None:
        raise ValueError("manual override block not found; add the parameters-status:manual markers")
    try:
        data = tomllib.loads(match.group(1))
    except tomllib.TOMLDecodeError as error:
        raise ValueError(f"manual override block: {error}") from error

    entries = data.get("model", [])
    if not isinstance(entries, list):
        raise ValueError("manual override block: model must be an array of tables")
    allowed = {"id", "status", "sync", "verified", "notes"}
    overrides = {}
    for index, entry in enumerate(entries):
        label = f"manual override model[{index}]"
        if not isinstance(entry, dict):
            raise ValueError(f"{label}: expected a table")
        unknown = set(entry) - allowed
        if unknown:
            raise ValueError(f"{label}: unsupported fields {sorted(unknown)}")
        model_id = entry.get("id")
        if not isinstance(model_id, str) or not model_id.strip():
            raise ValueError(f"{label}.id: expected a nonempty string")
        if model_id in overrides:
            raise ValueError(f"{label}.id: duplicate {model_id}")
        if "status" in entry and entry["status"] not in COLLECTION_STATUSES:
            raise ValueError(f"{label}.status: expected one of {COLLECTION_STATUSES}")
        if "sync" in entry and entry["sync"] not in SYNC_STATUSES:
            raise ValueError(f"{label}.sync: expected one of {SYNC_STATUSES}")
        if "verified" in entry:
            verified = entry["verified"]
            if not isinstance(verified, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", verified):
                raise ValueError(f"{label}.verified: expected YYYY-MM-DD")
            try:
                date.fromisoformat(verified)
            except ValueError as error:
                raise ValueError(f"{label}.verified: {error}") from error
        if "notes" in entry and (not isinstance(entry["notes"], str) or not entry["notes"].strip()):
            raise ValueError(f"{label}.notes: expected a nonempty string")
        overrides[model_id] = entry
    return overrides


def load_dist(path):
    if path is None or not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise ValueError(f"{path}: {error}") from error
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected a JSON object")
    return data


def default_status(model):
    if model.total is not None:
        return COLLECTED
    if model.active is not None:
        return PARTIAL
    if model.components:
        return UNDISCLOSED
    return PENDING


def status_for(model, overrides):
    override = overrides.get(model.model_id, {})
    return override.get("status", default_status(model))


def dist_parameters(dist, model_id):
    entry = dist.get(model_id) if dist else None
    if not isinstance(entry, dict):
        return None
    metadata = entry.get("metadata", {})
    if not isinstance(metadata, dict):
        return None
    atlas = metadata.get("modelatlas", {})
    if not isinstance(atlas, dict):
        return None
    parameters = atlas.get("parameters")
    return parameters if isinstance(parameters, dict) else None


def sync_for(model, overrides, dist):
    override = overrides.get(model.model_id, {})
    if "sync" in override:
        return override["sync"]
    if not model.has_parameters:
        return SYNC_UNVERIFIED
    if dist is not None and dist_parameters(dist, model.model_id) == model.parameters:
        return SYNC_BUILT
    return SYNC_STORED


def auto_note(model):
    if not model.has_parameters:
        return "尚无参数记录"
    parts = []
    if model.total is None and model.active is not None:
        parts.append("仅激活量")
    elif model.total is None and model.components:
        parts.append(f"仅组件 {len(model.components)} 项")
    if model.sources:
        parts.append(f"来源 {len(model.sources)}")
    else:
        parts.append("来源缺失")
    if model.total is not None and model.active is None:
        parts.append("未单列激活量")
    if model.has_notes:
        parts.append("TOML 备注")
    return "；".join(parts)


def note_for(model, overrides):
    override = overrides.get(model.model_id, {})
    parts = []
    if "verified" in override:
        parts.append(f"核验 {override['verified']}")
    if "notes" in override:
        parts.append(override["notes"].strip().rstrip("。."))
    parts.append(auto_note(model))
    return "；".join(part for part in parts if part)


def percent(count, total):
    return f"{count / total * 100:.1f}%" if total else "0.0%"


def render(models, scanned, overrides, dist):
    statuses = Counter(status_for(model, overrides) for model in models)
    sync_statuses = Counter(sync_for(model, overrides, dist) for model in models)
    total_models = len(models)
    completed = statuses[COLLECTED]
    partial = statuses[PARTIAL]
    pending = statuses[PENDING]
    undisclosed = statuses[UNDISCLOSED]
    not_applicable = statuses[NOT_APPLICABLE]
    resolved = completed + undisclosed + not_applicable
    total_fields = sum(model.total is not None for model in models)
    active_fields = sum(model.active is not None for model in models)
    component_fields = sum(bool(model.components) for model in models)
    total_without_active = sum(
        model.total is not None and model.active is None for model in models
    )

    lines = [
        "## 总体进度",
        "",
        f"> 自动统计当前 `models/` 目录：扫描 {scanned} 个模型 TOML，其中 {total_models} 个 "
        "`open_weights = true`。数值及来源以各模型 TOML 为准，本页不复制参数值。",
        "",
        "| 指标 | 数值 | 说明 |",
        "| --- | ---: | --- |",
        f"| 开放权重模型总数 | {total_models} | 当前追踪范围 |",
        f"| 已完成模型数 | {completed} | {COLLECTED}；`total_billion` 已记录 |",
        f"| 部分完成模型数 | {partial} | {PARTIAL}；缺完整总量，仅记录激活量 |",
        f"| 待收集模型数 | {pending} | {PENDING}；尚无任何参数量记录 |",
        f"| 无法获取参数的模型数 | {undisclosed} | {UNDISCLOSED}；仅组件等，完整总量未披露 |",
        f"| 不适用模型数 | {not_applicable} | {NOT_APPLICABLE}；人工确认无需收集 |",
        f"| 总参数量覆盖率 | {percent(total_fields, total_models)} | "
        f"`total_billion` 存在：{total_fields} / {total_models} |",
        f"| 激活参数量覆盖率 | {percent(active_fields, total_models)} | "
        f"`active_billion` 存在：{active_fields} / {total_models} |",
        f"| 总量已收集但激活量缺失 | {total_without_active} | "
        "已计入 ✅；不推定等于总参数量，按独立覆盖率统计 |",
        f"| 组件参数量记录数 | {percent(component_fields, total_models)} | "
        f"`components` 非空：{component_fields} / {total_models}；可选字段，不计入完成率 |",
        f"| 整体收集完成率 | {percent(completed, total_models)} | `{COLLECTED} / 总数` |",
        f"| 已确定率 | {percent(resolved, total_models)} | "
        f"`({COLLECTED} + {UNDISCLOSED} + {NOT_APPLICABLE}) / 总数`，表示无需继续收集 |",
        f"| 待处理率 | {percent(partial + pending, total_models)} | "
        f"`({PARTIAL} + {PENDING}) / 总数` |",
        "",
        "收集完成以 `total_billion` 为核心口径；`active_billion` 只在来源披露时记录，"
        "不推定等于总参数量，也不因缺失单独判为模型未完成。已收集总量但未单列激活量的模型仍计入 ✅，"
        "激活量缺口由单独的覆盖率反映，避免把稠密模型或来源未单列激活量的模型误判为未完成。",
        "",
        "同步状态分布：" + "，".join(
            f"{status} {sync_statuses[status]}" for status in SYNC_STATUSES
        ) + "。",
        "",
        "## 模型收集清单",
        "",
        "按 `release_date` 倒序；同日按模型 ID 升序。字段列中的 `✅` 表示 TOML 已有该字段，"
        "`—` 表示缺失，不代表 `0`，也不代表字段之间可以互相推算。",
        "",
        "| 模型 ID | 总参数量 | 激活参数量 | 组件参数量 | 收集状态 | 同步状态 | 备注 |",
        "| --- | :---: | :---: | :---: | --- | --- | --- |",
    ]

    for model in models:
        total_cell = "✅" if model.total is not None else "—"
        active_cell = "✅" if model.active is not None else "—"
        components_cell = "✅" if model.components else "—"
        note = note_for(model, overrides).replace("|", "\\|")
        lines.append(
            f"| `{model.model_id}` | {total_cell} | {active_cell} | {components_cell} | "
            f"{status_for(model, overrides)} | {sync_for(model, overrides, dist)} | {note} |"
        )

    return "\n".join(lines)


def update_document(root, doc, dist_path=None, check=False):
    root = Path(root)
    doc = Path(doc)
    if not doc.is_absolute():
        doc = root / doc
    if not doc.is_file():
        raise ValueError(f"{doc}: document not found")
    text = doc.read_text(encoding="utf-8")
    if GENERATED_START not in text or GENERATED_END not in text:
        raise ValueError(f"{doc}: generated section markers not found")
    if text.index(GENERATED_START) > text.index(GENERATED_END):
        raise ValueError(f"{doc}: generated section markers are out of order")

    models, scanned = load_models(root)
    overrides = load_overrides(text)
    known = {model.model_id for model in models}
    unknown = sorted(set(overrides) - known)
    if unknown:
        raise ValueError(f"{doc}: manual override references untracked models: {', '.join(unknown)}")

    dist = load_dist(dist_path)
    generated = render(models, scanned, overrides, dist)
    start = text.index(GENERATED_START) + len(GENERATED_START)
    end = text.index(GENERATED_END)
    new_text = text[:start] + "\n\n" + generated + "\n\n" + text[end:]

    statuses = Counter(status_for(model, overrides) for model in models)
    summary = (
        f"{len(models)} 个开放权重模型：{COLLECTED} {statuses[COLLECTED]}，"
        f"{PARTIAL} {statuses[PARTIAL]}，{PENDING} {statuses[PENDING]}，"
        f"{UNDISCLOSED} {statuses[UNDISCLOSED]}，{NOT_APPLICABLE} {statuses[NOT_APPLICABLE]}"
    )
    if check:
        if new_text != text:
            return False, f"{doc}: 需要更新（{summary}）。运行 scripts/parameters_status.py 写入。"
        return True, f"{doc}: 已是最新（{summary}）。"

    if new_text != text:
        doc.write_text(new_text, encoding="utf-8")
        return True, f"已更新 {doc}：{summary}。"
    return True, f"{doc}: 无需修改（{summary}）。"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root")
    parser.add_argument("--doc", type=Path, default=DEFAULT_DOC,
                        help="status document, relative to the repository root")
    parser.add_argument("--dist", type=Path, default=None,
                        help="optional models.json used to check the 已构建 state")
    parser.add_argument("--check", action="store_true",
                        help="report whether the document is current without writing")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    dist_path = args.dist
    if dist_path is not None and not dist_path.is_absolute():
        dist_path = root / dist_path

    try:
        ok, message = update_document(root, args.doc, dist_path, check=args.check)
    except (OSError, ValueError) as error:
        print(f"错误：{error}", file=sys.stderr)
        return 2
    print(message)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())