"""Build JSON from source TOML using Python 3.11+ (no third-party dependencies)."""

import argparse
from collections import Counter
import json
import math
from pathlib import Path
import re
import sys
import tempfile
import tomllib
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parent.parent
SLUG = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
RESULT_TEXT_FIELDS = ("name", "metric", "version", "dataset", "variant", "harness", "source", "date")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def number(value):
    return type(value) in (int, float) and (type(value) is int or math.isfinite(value))


def fields(data, types, label):
    require(isinstance(data, dict), f"{label}: expected a table")
    for key, expected in types.items():
        if key in data:
            require(type(data[key]) is expected, f"{label}.{key}: expected {expected.__name__}")
            if expected is str:
                require(text(data[key]), f"{label}.{key}: expected a nonempty string")


def http_url(value):
    if not text(value):
        return False
    parsed = urlsplit(value)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def validate_model(data):
    """Basic structure checks only; preserve unknown JSON-compatible fields."""
    require(type(data.get("schema")) is int and data["schema"] == 2, "expected schema = 2")
    require(text(data.get("name")), "name: required nonempty string")
    fields(data, {**{key: str for key in ("description", "family", "type", "knowledge",
                                        "release_date", "last_updated", "license")},
                  "open_weights": bool, "v2_only": bool, "modalities": dict,
                  "capabilities": dict, "limit": dict, "metadata": dict,
                  "links": list, "weights": list, "benchmarks": list}, "model")
    for key, values in data.get("modalities", {}).items():
        if key in ("input", "output"):
            require(isinstance(values, list) and all(text(v) for v in values),
                    f"modalities.{key}: expected an array of strings")
    caps = data.get("capabilities", {})
    fields(caps, {"tools": dict, "reasoning": dict, "temperature": bool,
                  "top_p": bool, "top_k": bool}, "capabilities")
    for key in ("tools", "reasoning"):
        if key in caps:
            fields(caps[key], {"supported": bool}, f"capabilities.{key}")
    limits = data.get("limit", {})
    for key in ("context", "input", "output", "request_bytes"):
        if key in limits:
            require(number(limits[key]) and limits[key] >= 0, f"limit.{key}: invalid number")
    for key in ("links", "weights"):
        for entry in data.get(key, []):
            fields(entry, {field: str for field in ("url", "label", "type", "format", "quantization")}, key)
            require(http_url(entry.get("url")), f"{key}.url: expected an HTTP(S) URL")
    seen = set()
    for index, result in enumerate(data.get("benchmarks", [])):
        label = f"benchmarks[{index}]"
        fields(result, {key: str for key in RESULT_TEXT_FIELDS}, label)
        require(text(result.get("name")), f"{label}.name: required")
        score = result.get("score")
        require(number(score) or text(score), f"{label}.score: expected a finite number or nonempty string")
        if "source" in result:
            require(http_url(result["source"]), f"{label}.source: expected an HTTP(S) URL")
        # Include every known or future condition except the score; never select a higher score.
        identity = json.dumps({k: v for k, v in result.items() if k != "score"},
                              sort_keys=True, allow_nan=False)
        require(identity not in seen, f"{label}: duplicate or conflicting benchmark record")
        seen.add(identity)


def validate_definition(data):
    for key in ("id", "name", "version", "category", "metric", "unit"):
        require(text(data.get(key)), f"{key}: required nonempty string")
    require(SLUG.fullmatch(data["id"]), "id: invalid Benchmark ID")
    require(type(data.get("higher_is_better")) is bool, "higher_is_better: required boolean")
    fields(data, {key: str for key in ("description", "organization", "url", "methodology")}, "benchmark")
    for key in ("min_score", "max_score"):
        if key in data:
            require(number(data[key]), f"{key}: expected a finite number")
    for key in ("url", "methodology"):
        if key in data:
            require(http_url(data[key]), f"{key}: expected an HTTP(S) URL")


def load_sources(root):
    models, definitions, locales = {}, {}, {}
    errors = []
    for directory in ("models", "benchmarks", "i18n"):
        base = root / directory
        require(not base.is_symlink(), f"{directory}/: symlink not allowed")
        require(not base.exists() or base.is_dir(), f"{directory}/: expected a directory")
        for path in sorted(base.rglob("*.toml")):
            relative = path.relative_to(root)
            try:
                require(not any((root / p).is_symlink() for p in (relative, *relative.parents)),
                        "symlink not allowed")
                with path.open("rb") as source:
                    data = tomllib.load(source)
                if directory == "models":
                    require(len(relative.parts) == 3
                            and all(SLUG.fullmatch(v) for v in (relative.parts[1], path.stem)),
                            "expected models/<lab>/<model-id>.toml")
                    validate_model(data)
                    models[f"{relative.parts[1]}/{path.stem}"] = data
                elif directory == "benchmarks":
                    validate_definition(data)
                    identifier = data["id"]
                    require(identifier not in definitions, f"duplicate Benchmark ID: {identifier}")
                    definitions[identifier] = {k: v for k, v in data.items() if k != "id"}
                else:
                    require(len(relative.parts) == 2 and SLUG.fullmatch(path.stem),
                            "expected i18n/<language>.toml")
                    locales[path.stem] = data
            except (OSError, ValueError, TypeError) as error:
                errors.append(f"{relative.as_posix()}: {error}")
    if not models:
        errors.append("models/: 未找到有效模型文件。")
    require(not errors, "\n".join(errors))
    return models, definitions, locales


def check_references(models, definitions, locales):
    warnings = []
    mappings = Counter((d["name"], d["version"], d["metric"]) for d in definitions.values())
    unmatched = ambiguous = missing_source = 0
    for model in models.values():
        for result in model.get("benchmarks", []):
            count = mappings[tuple(result.get(k) for k in ("name", "version", "metric"))]
            unmatched += count == 0
            ambiguous += count > 1
            missing_source += "source" not in result
    if unmatched or ambiguous:
        warnings.append(f"Benchmark 定义映射：未匹配 {unmatched} 条，歧义 {ambiguous} 条"
                        "（要求 name/version/metric 精确匹配，不推断默认值；原始成绩全部保留）。")
    if missing_source:
        warnings.append(f"{missing_source} 条成绩未提供 source；原始成绩保留，来源需人工核实。")
    for language, data in locales.items():
        label = f"i18n/{language}.toml"
        fields(data, {"model": dict, "benchmark": dict}, label)
        for section, key, sources in (("model", "descriptions", models),
                                      ("benchmark", "description", definitions)):
            tables = data.get(section, {})
            fields(tables, {key: dict}, f"{label}:{section}")
            translations = tables.get(key, {})
            for identifier, value in translations.items():
                require(identifier in sources, f"{label}:{section}.{key}: unknown ID {identifier}")
                require(text(value), f"{label}:{section}.{key}.{identifier}: expected a nonempty string")
            missing = sum("description" in source and identifier not in translations
                          for identifier, source in sources.items())
            if missing:
                warnings.append(f"{label}: 缺少 {missing} 个 {section} 描述翻译（允许缺失，不填充回退值）。")
    return warnings


def build(root, output):
    models, definitions, locales = load_sources(root)
    warnings = check_references(models, definitions, locales)
    documents = {Path("models.json"): models, Path("benchmarks.json"): definitions}
    documents.update({Path("i18n") / f"{language}.json": data for language, data in locales.items()})
    # Serialize everything before touching existing output. Reject TOML dates and NaN/Infinity
    # rather than silently changing their types or emitting nonstandard JSON.
    serialized = {}
    for path, data in documents.items():
        try:
            serialized[path] = json.dumps(data, ensure_ascii=False, allow_nan=False,
                                          sort_keys=True, indent=2) + "\n"
        except (ValueError, TypeError) as error:
            raise ValueError(f"{path.as_posix()}: JSON serialization failed: {error}") from error
    require(not output.is_symlink(), f"{output}: symlink not allowed")
    require(not output.exists() or output.is_dir(), f"{output}: expected a directory")
    require(not (output / "i18n").is_symlink(), f"{output / 'i18n'}: symlink not allowed")
    require(not (output / "i18n").exists() or (output / "i18n").is_dir(),
            f"{output / 'i18n'}: expected a directory")
    # Refuse stale language artifacts instead of silently publishing them or deleting files.
    for path in sorted((output / "i18n").glob("*.json")):
        require(path.relative_to(output) in documents, f"{path}: 无对应语言源文件，请先移走旧产物。")
    for path in documents:
        target = output / path
        require(not target.is_symlink(), f"{target}: symlink not allowed")
        require(not target.exists() or target.is_file(), f"{target}: expected a file")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".model-atlas-build-", dir=output.parent) as staging:
        stage = Path(staging)
        for path, content in serialized.items():
            target = stage / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8", newline="\n")
        for path in documents:
            target = output / path
            target.parent.mkdir(parents=True, exist_ok=True)
            (stage / path).replace(target)
    return len(models), len(definitions), len(locales), warnings


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="source repository (default: script's repository)")
    parser.add_argument("--output", type=Path, help="output directory (default: <root>/dist)")
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        output = args.output.absolute() if args.output is not None else root / "dist"
        models, definitions, locales, warnings = build(root, output)
        for warning in warnings:
            print(f"警告：{warning}", file=sys.stderr)
        print(f"构建完成：{models} 个模型，{definitions} 个 Benchmark 定义，{locales} 个语言文件 → {output}")
        return 0
    except (OSError, ValueError, TypeError) as error:
        print(f"构建失败：{error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
