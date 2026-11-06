"""Import new Models.dev models and safely update existing model information."""

import argparse
from copy import deepcopy
from datetime import date
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import tomllib
from urllib.parse import urlsplit

import tomlkit
from tomlkit.exceptions import TOMLKitError


ROOT = Path(__file__).resolve().parent.parent
SLUG = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
MODEL_FIELDS = set("schema v2_only type name description family open_weights knowledge "
                   "release_date last_updated modalities capabilities limit license links "
                   "weights benchmarks metadata".split())
BENCHMARK_FIELDS = set("name score metric version dataset effort variant harness source date "
                       "cost cost_unit cost_source".split())
BENCHMARK_COST_FIELDS = {"cost", "cost_unit", "cost_source"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def table(value, allowed, label):
    require(isinstance(value, dict), f"{label}: expected a table")
    require(not value.keys() - allowed, f"{label}: unsupported fields {sorted(value.keys() - allowed)}")


def text(value):
    return isinstance(value, str) and bool(value.strip())


def number(value):
    return type(value) in (int, float) and math.isfinite(value)


def url(value):
    if not isinstance(value, str):
        return False
    parsed = urlsplit(value)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def calendar_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}(-\d{2})?", value):
        return False
    try:
        date.fromisoformat(value if len(value) == 10 else value + "-01")
        return True
    except ValueError:
        return False


def model_path(path):
    return (len(path.parts) == 3 and path.parts[0] == "models"
            and path.suffix == ".toml"
            and all(SLUG.fullmatch(part) for part in (path.parts[1], path.stem)))


def no_symlinks(base, relative):
    current = base
    for part in relative.parts:
        current /= part
        require(not current.is_symlink(), f"symlink not allowed: {current}")


def validate_model(data, definitions):
    """Conservative import checks, not a replacement for the complete upstream schema."""
    table(data, MODEL_FIELDS, "model")
    require(type(data.get("schema")) is int and data["schema"] == 2, "expected schema = 2")
    for key in ("name", "description"):
        require(text(data.get(key)), f"{key}: expected a nonempty string")
    for key in ("type", "family", "license"):
        if key in data:
            require(text(data[key]), f"{key}: expected a nonempty string")
    for key in ("open_weights", "v2_only"):
        if key == "open_weights" or key in data:
            require(type(data.get(key)) is bool, f"{key}: expected a boolean")
    for key in ("release_date", "last_updated", "knowledge"):
        if key == "release_date" or key in data:
            require(calendar_date(data.get(key)), f"{key}: invalid date string")
    modalities = data.get("modalities")
    table(modalities, {"input", "output"}, "modalities")
    for key in ("input", "output"):
        values = modalities.get(key)
        require(isinstance(values, list) and all(text(v) for v in values),
                f"modalities.{key}: expected an array of strings")
    caps = data.get("capabilities")
    table(caps, {"tools", "reasoning", "temperature", "top_p", "top_k"}, "capabilities")
    for key in ("temperature", "top_p", "top_k"):
        require(type(caps.get(key)) is bool, f"capabilities.{key}: expected a boolean")
    for key in ("tools", "reasoning"):
        support = caps.get(key)
        allowed = {"supported"}
        if key == "tools" and isinstance(support, dict) and support.get("supported") is True:
            allowed |= {"strict", "choice", "search", "freeform", "updates"}
        table(support, allowed, f"capabilities.{key}")
        require(type(support.get("supported")) is bool, f"{key}.supported: expected a boolean")
        for flag in ("strict", "search", "updates"):
            if flag in support:
                require(type(support[flag]) is bool, f"{key}.{flag}: expected a boolean")
        for field, options in (("choice", {"auto", "none", "required", "tool"}),
                               ("freeform", {"text", "lark", "regex"})):
            if field in support:
                values = support[field]
                require(isinstance(values, list) and all(isinstance(v, str) and v in options for v in values),
                        f"{key}.{field}: unsupported values")
    limits = data.get("limit")
    table(limits, {"context", "input", "output", "request_bytes", "image", "pdf"}, "limit")
    media_fields = {
        "image": set("max_per_message max_per_request max_bytes min_width min_height max_width max_height".split()),
        "pdf": {"max_per_request", "max_bytes", "max_pages"},
    }
    for key, value in limits.items():
        if key in media_fields:
            table(value, media_fields[key], f"limit.{key}")
            require(all(number(v) and v >= 0 for v in value.values()), f"limit.{key}: invalid number")
        else:
            require(number(value) and value >= 0, f"limit.{key}: invalid number")
    for key in ("links", "weights"):
        entries = data.get(key, [])
        require(isinstance(entries, list), f"{key}: expected an array")
        for entry in entries:
            fields = {"label", "url", "type"} if key == "links" else {"label", "url", "format", "quantization"}
            table(entry, fields, key)
            require(url(entry.get("url")), f"{key}.url: expected an HTTP(S) URL")
            require(all(text(v) for v in entry.values()), f"{key}: expected nonempty strings")
    if "metadata" in data:
        require(isinstance(data["metadata"], dict), "metadata: expected a table")
        json.dumps(data["metadata"], allow_nan=False)
    results = data.get("benchmarks", [])
    require(isinstance(results, list), "benchmarks: expected an array")
    seen = set()
    for result in results:
        table(result, BENCHMARK_FIELDS, "benchmark")
        require(text(result.get("name")), "benchmark.name: required")
        score = result.get("score")
        require(number(score) or text(score), "benchmark.score: expected a finite number or nonempty string")
        for key in BENCHMARK_FIELDS - {"score", "cost"}:
            if key in result:
                require(text(result[key]), f"benchmark.{key}: expected a nonempty string")
        require(url(result.get("source")), f"{result['name']}: verifiable HTTP(S) source required")
        if "date" in result:
            require(calendar_date(result["date"]), "benchmark.date: invalid date")
        require(("cost" in result) == ("cost_unit" in result),
                "benchmark.cost: cost and cost_unit must be supplied together")
        if "cost" in result:
            require(number(result["cost"]) and result["cost"] >= 0,
                    "benchmark.cost: expected a finite nonnegative number")
        if "cost_source" in result:
            require("cost" in result and url(result["cost_source"]),
                    "benchmark.cost_source: expected an HTTP(S) URL and cost")
        # Exact conditions include effort; omitted values are not default effort.
        # Costs and their provenance are observations, not distinct conditions.
        identity = tuple(result.get(key) for key in sorted(BENCHMARK_FIELDS - {"score"} - BENCHMARK_COST_FIELDS))
        require(identity not in seen, f"{result['name']}: duplicate or conflicting benchmark record")
        seen.add(identity)
        # No aliases, version normalization, or inferred metrics/default versions.
        # A definition may explicitly list compatible source versions.
        matches = [definition for definition in definitions
                   if result.get("name") == definition.get("name")
                   and result.get("metric") == definition.get("metric")
                   and result.get("version") in
                       (definition.get("version"), *definition.get("compatible_versions", []))]
        require(len(matches) == 1,
                f"{result['name']}: benchmark definition mapping is missing or ambiguous "
                "(exact name, explicit version and metric required)")


def benchmark_segments(content):
    """Split complete TOML statements, protecting benchmarks and leading comments."""
    source = content.decode("utf-8")
    tomllib.loads(source)
    tokens, pending = [], []
    root, section = True, False
    for line in source.splitlines(keepends=True):
        pending.append(line)
        statement = "".join(pending)
        try:
            parsed = tomllib.loads(statement)
        except tomllib.TOMLDecodeError:
            continue
        if statement.lstrip().startswith("["):
            root = False
            section = "benchmarks" in parsed
        tokens.append([statement, section or (root and "benchmarks" in parsed), root, not parsed])
        pending.clear()
    require(not pending, "cannot identify benchmark statements safely")
    # TOML parsers often attach comments before [[benchmarks]] to the preceding
    # table. Protect those too, so changing that table cannot drop result notes.
    for index in range(len(tokens) - 2, -1, -1):
        if tokens[index][3] and tokens[index + 1][1]:
            tokens[index][1:3] = tokens[index + 1][1:3]
    segments = []
    for text, protected, root, _ in tokens:
        if segments and segments[-1][1:] == (protected, root):
            segments[-1] = (segments[-1][0] + text, protected, root)
        else:
            segments.append((text, protected, root))
    return segments


def benchmark_bytes(content):
    # Blank separators before sections may be added by the editor; result text,
    # leading comments and internal spacing must otherwise remain byte-identical.
    return "".join(text.lstrip("\r\n") for text, protected, _ in benchmark_segments(content)
                   if protected).encode("utf-8")


def masked_document(content):
    """Keep benchmark blocks outside the editor, replacing them with placeholders."""
    prefix = "__model_atlas_protected_benchmark_"
    while prefix.encode() in content:
        prefix += "_"
    parts, replacements = [], []
    for text, protected, root in benchmark_segments(content):
        if protected:
            key = json.dumps(prefix + str(len(replacements)))
            marker = f"{key} = true\n" if root else f"[{key}]\n"
            parts.append(marker)
            replacements.append((marker, text))
        else:
            parts.append(text)
    return tomlkit.parse("".join(parts)), replacements


def information(data):
    return {key: value for key, value in data.items() if key != "benchmarks"}


def merge_information(local, upstream, translated=False):
    """Follow explicit upstream values, retaining fields absent upstream."""
    merged = deepcopy(local)
    changes, conflicts = [], {}

    def merge(target, incoming, prefix=()):
        for key, value in incoming.items():
            path = (*prefix, key)
            label = ".".join(path)
            if key not in target:
                target[key] = deepcopy(value)
                changes.append(path)
            elif isinstance(target[key], dict) and isinstance(value, dict):
                merge(target[key], value, path)
            elif target[key] == value:
                continue
            elif path == ("description",) and translated:
                conflicts[label] = "description has local translations; update them manually first"
            else:
                target[key] = deepcopy(value)
                changes.append(path)

    merge(merged, upstream)
    return merged, changes, conflicts


def edit_value(target, key, value):
    """Edit matching array/table shapes in place to retain their local comments."""
    exists = key in target if isinstance(target, dict) else key < len(target)
    if exists:
        current = target[key]
        if current == value:
            return
        if isinstance(current, dict) and isinstance(value, dict) and current.keys() <= value.keys():
            for child, item in value.items():
                edit_value(current, child, item)
            return
        if isinstance(current, list) and isinstance(value, list) and len(current) == len(value):
            for index, item in enumerate(value):
                edit_value(current, index, item)
            return
    target[key] = deepcopy(value)


def update_content(content, incoming, translated=False):
    data = tomllib.loads(content.decode("utf-8"))
    validate_model(information(data), [])
    validate_model(information(incoming), [])
    merged, changes, conflicts = merge_information(
        information(data), information(incoming), translated)
    validate_model(merged, [])
    if not changes:
        return content, [], conflicts
    document, replacements = masked_document(content)
    for path in changes:
        target, values = document, merged
        for key in path[:-1]:
            target, values = target[key], values[key]
        edit_value(target, path[-1], values[path[-1]])
    serialized = tomlkit.dumps(document)
    for marker, original in replacements:
        require(serialized.count(marker) == 1, "TOML editor changed a protected benchmark placeholder")
        serialized = serialized.replace(marker, original, 1)
    updated = serialized.encode("utf-8")
    expected = {**merged, **({"benchmarks": data["benchmarks"]} if "benchmarks" in data else {})}
    require(tomllib.loads(updated.decode("utf-8")) == expected, "TOML editing changed unexpected fields")
    require(benchmark_bytes(updated) == benchmark_bytes(content), "TOML editing changed benchmark text")
    return updated, [".".join(path) for path in changes], conflicts


def sync_models(upstream, root, dry_run=False):
    require((upstream / "LICENSE").read_bytes() == (root / "LICENSE.models-dev").read_bytes(),
            "upstream LICENSE changed; review the license before syncing")
    no_symlinks(upstream, Path("models"))
    no_symlinks(root, Path("models"))
    require((upstream / "models").is_dir(), "upstream models/ directory is missing")
    definitions = []
    for path in sorted((root / "benchmarks").rglob("*.toml")):
        with path.open("rb") as source:
            definitions.append(tomllib.load(source))
    translated = set()
    for path in sorted((root / "i18n").glob("*.toml")):
        no_symlinks(root, path.relative_to(root))
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        translated.update(data.get("model", {}).get("descriptions", {}))
    report = {"added": {}, "updated": {}, "existing": 0, "conflicts": {},
              "skipped": {}, "dry_run": dry_run}
    for source in sorted((upstream / "models").rglob("*.toml")):
        relative = source.relative_to(upstream)
        name = relative.as_posix()
        target = root / relative
        try:
            require(model_path(relative), "expected models/<lab>/<model-id>.toml")
            no_symlinks(upstream, relative)
            no_symlinks(root, relative)
            existing = target.exists()
            if existing:
                report["existing"] += 1
            content = source.read_bytes()
            incoming = tomllib.loads(content.decode("utf-8"))
            if existing:
                previous = target.read_bytes()
                content, fields, conflicts = update_content(
                    previous, incoming, translated="/".join(relative.with_suffix("").parts[1:]) in translated)
                if conflicts:
                    report["conflicts"][name] = conflicts
                if content == previous:
                    continue
            else:
                validate_model(incoming, definitions)
        except (ValueError, TypeError, OverflowError, TOMLKitError) as error:
            report["skipped"][name] = str(error)
            continue
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            no_symlinks(root, relative)
            if existing:
                with target.open("r+b") as output:
                    require(output.read() == previous, f"local model changed during sync: {name}")
                    output.seek(0)
                    output.write(content)
                    output.truncate()
            else:
                # Exclusive creation is the last line of defense against overwrites.
                with target.open("xb") as output:
                    output.write(content)
        digest = hashlib.sha256(content).hexdigest()
        if existing:
            report["updated"][name] = {"before": hashlib.sha256(previous).hexdigest(),
                                       "after": digest, "fields": fields}
        else:
            report["added"][name] = digest
    return report


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def check_staged(root, report):
    require(not report["dry_run"], "cannot commit a dry run")
    updated = report.get("updated", {})
    require(not report["added"].keys() & updated.keys(), "file reported as both added and updated")
    # Check NUL-separated raw paths; do not depend on Git's path quoting.
    records = git(root, "diff", "--cached", "--name-status", "--no-renames", "-z").split(b"\0")[:-1]
    require(len(records) % 2 == 0, "invalid staged diff")
    actual = set()
    for status, raw_path in zip(records[::2], records[1::2]):
        name = raw_path.decode("utf-8")
        require(status in (b"A", b"M") and model_path(Path(name)), f"unsupported staged change: {name}")
        expected = report["added"] if status == b"A" else updated
        require(name in expected, f"unexpected staged file: {name}")
        content = git(root, "show", f":{name}")
        digest = expected[name] if status == b"A" else expected[name]["after"]
        require(hashlib.sha256(content).hexdigest() == digest, f"staged content changed: {name}")
        if status == b"M":
            require(git(root, "ls-tree", "HEAD", "--", name).split()[0] == b"100644",
                    f"unexpected original file mode: {name}")
            previous = git(root, "show", f"HEAD:{name}")
            require(hashlib.sha256(previous).hexdigest() == updated[name]["before"],
                    f"model changed since comparison: {name}")
            require(benchmark_bytes(content) == benchmark_bytes(previous), f"benchmarks changed: {name}")
            before = tomllib.loads(previous.decode("utf-8"))
            after = tomllib.loads(content.decode("utf-8"))
            require(("benchmarks" in before) == ("benchmarks" in after)
                    and before.get("benchmarks") == after.get("benchmarks"), f"benchmarks changed: {name}")
        mode = git(root, "ls-files", "--stage", "--", name).split()[0]
        require(mode == b"100644", f"unexpected file mode: {name}")
        actual.add(name)
    require(actual == set(report["added"]) | set(updated), "staged files do not match sync report")
    require(not git(root, "diff", "--name-only"), "unstaged tracked changes detected")


def summary(report):
    lines = ["## Models.dev sync", "", f"Upstream commit: `{report['upstream_sha']}`",
             f"Dry run: {report['dry_run']}",
             f"Added: {len(report['added'])}; updated: {len(report.get('updated', {}))}; "
             f"existing: {report['existing']}; skipped: {len(report['skipped'])}",
             "", "New models include upstream benchmarks. Existing models keep their benchmark data and text unchanged.",
             "Existing model information follows explicit upstream values; fields absent upstream are retained.",
             "Translations are deferred for new models. Existing translated descriptions are protected.",
             "No source authenticity or full upstream schema validation is performed."]
    for name in report["added"]:
        lines.append(f"- Added: `{name}`")
    for name, update in report.get("updated", {}).items():
        fields = ", ".join(update["fields"]).replace("`", "'").replace("\n", " ").replace("\r", " ")
        lines.append(f"- Updated: `{name}` — `{fields}`")
    for name, conflicts in report.get("conflicts", {}).items():
        for field, reason in conflicts.items():
            detail = f"{field}: {reason}".replace("`", "'").replace("\n", " ").replace("\r", " ")
            lines.append(f"- Conflict retained: `{name}` — `{detail}`")
    for name, reason in report["skipped"].items():
        # Escape newlines/backticks from upstream content in the workflow summary.
        reason = reason.replace("`", "'").replace("\n", " ").replace("\r", " ")
        lines.append(f"- Skipped: `{name}` — `{reason}`")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    sync = commands.add_parser("sync")
    sync.add_argument("--upstream", type=Path, required=True, help="checkout of anomalyco/models.dev (dev)")
    sync.add_argument("--report", type=Path, required=True, help="JSON report outside the repository")
    sync.add_argument("--summary", type=Path)
    sync.add_argument("--dry-run", action="store_true")
    check = commands.add_parser("check-staged")
    check.add_argument("--report", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        if args.command == "check-staged":
            check_staged(root, json.loads(args.report.read_text(encoding="utf-8")))
        else:
            upstream = args.upstream.resolve()
            sha = git(upstream, "rev-parse", "HEAD").decode().strip()
            report = sync_models(upstream, root, args.dry_run)
            report["upstream_sha"] = sha
            args.report.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
            output = summary(report)
            print(output, end="")
            if args.summary:
                with args.summary.open("a", encoding="utf-8") as stream:
                    stream.write(output)
        return 0
    except (OSError, ValueError, TypeError, TOMLKitError, subprocess.CalledProcessError) as error:
        print(f"Sync failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
