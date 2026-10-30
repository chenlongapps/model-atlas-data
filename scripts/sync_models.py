"""Add Models.dev lab files without changing any existing model (Python 3.11+)."""

import argparse
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


ROOT = Path(__file__).resolve().parent.parent
SLUG = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")
MODEL_FIELDS = set("schema v2_only type name description family open_weights knowledge "
                   "release_date last_updated modalities capabilities limit license links "
                   "weights benchmarks metadata".split())
BENCHMARK_FIELDS = set("name score metric version dataset variant harness source date".split())


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
        for key in BENCHMARK_FIELDS - {"score"}:
            if key in result:
                require(text(result[key]), f"benchmark.{key}: expected a nonempty string")
        require(url(result.get("source")), f"{result['name']}: verifiable HTTP(S) source required")
        if "date" in result:
            require(calendar_date(result["date"]), "benchmark.date: invalid date")
        identity = tuple(result.get(key) for key in sorted(BENCHMARK_FIELDS - {"score"}))
        require(identity not in seen, f"{result['name']}: duplicate or conflicting benchmark record")
        seen.add(identity)
        # No aliases, version normalization, or inferred metrics/default versions.
        matches = [definition for definition in definitions
                   if all(result.get(key) is not None and result[key] == definition.get(key)
                          for key in ("name", "version", "metric"))]
        require(len(matches) == 1,
                f"{result['name']}: benchmark definition mapping is missing or ambiguous "
                "(exact name, explicit version and metric required)")


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
    report = {"added": {}, "existing": 0, "skipped": {}, "dry_run": dry_run}
    for source in sorted((upstream / "models").rglob("*.toml")):
        relative = source.relative_to(upstream)
        name = relative.as_posix()
        target = root / relative
        try:
            require(model_path(relative), "expected models/<lab>/<model-id>.toml")
            no_symlinks(upstream, relative)
            no_symlinks(root, relative)
            if target.exists():
                report["existing"] += 1
                continue
            content = source.read_bytes()
            validate_model(tomllib.loads(content.decode("utf-8")), definitions)
        except (ValueError, TypeError, OverflowError) as error:
            report["skipped"][name] = str(error)
            continue
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            # Exclusive creation is the last line of defense against overwrites.
            with target.open("xb") as output:
                output.write(content)
        report["added"][name] = hashlib.sha256(content).hexdigest()
    return report


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def check_staged(root, report):
    require(not report["dry_run"], "cannot commit a dry run")
    # Check NUL-separated raw paths; do not depend on Git's path quoting.
    records = git(root, "diff", "--cached", "--name-status", "--no-renames", "-z").split(b"\0")[:-1]
    require(len(records) % 2 == 0, "invalid staged diff")
    actual = set()
    for status, raw_path in zip(records[::2], records[1::2]):
        name = raw_path.decode("utf-8")
        require(status == b"A" and model_path(Path(name)), f"non-additive staged change: {name}")
        require(name in report["added"], f"unexpected staged file: {name}")
        content = git(root, "show", f":{name}")
        require(hashlib.sha256(content).hexdigest() == report["added"][name], f"staged content changed: {name}")
        mode = git(root, "ls-files", "--stage", "--", name).split()[0]
        require(mode == b"100644", f"unexpected file mode: {name}")
        actual.add(name)
    require(actual == set(report["added"]), "staged files do not match sync report")
    require(not git(root, "diff", "--name-only"), "unstaged tracked changes detected")


def summary(report):
    lines = ["## Models.dev sync", "", f"Upstream commit: `{report['upstream_sha']}`",
             f"Dry run: {report['dry_run']}",
             f"Added: {len(report['added'])}; existing: {report['existing']}; skipped: {len(report['skipped'])}",
             "", "Translations are intentionally deferred. No source authenticity or full upstream schema validation is performed."]
    for name in report["added"]:
        lines.append(f"- Added: `{name}`")
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
    except (OSError, ValueError, TypeError, subprocess.CalledProcessError) as error:
        print(f"Sync failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
