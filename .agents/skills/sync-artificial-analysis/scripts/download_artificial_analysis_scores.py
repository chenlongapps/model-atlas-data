#!/usr/bin/env python3
"""下载 Artificial Analysis 模型名称、发布日期、综合分数和评测成本。

依赖：同目录 requirements.txt 中的 cryptography、tomli-w。
默认将 TOML 文件保存到数据仓库根目录的 temp/，不受当前工作目录影响。
输出字段：name、releaseDate、intelligenceIndex、cost，以及来源实际提供的 slug。
顶层 snapshot 表记录格式版本、下载时间、页面/清单 URL 和成本单位；不代表评测版本或日期。
按发布日期倒序排列，缺失日期的模型排在最后。
TOML 不支持 null；缺失字段会省略，但保留对应的模型记录。
cost 来自 intelligenceIndexCostPerTask.cost.total，口径为 USD/weighted task，
不做四舍五入。仅导出来源数值，不代表零成本已核实，也不自动导入模型成绩。
用法（SKILL_ROOT 为本 Skill 目录，DATA_ROOT 为数据仓库根目录）：
  python3 "$SKILL_ROOT/scripts/download_artificial_analysis_scores.py"
  python3 "$SKILL_ROOT/scripts/download_artificial_analysis_scores.py" --out "$DATA_ROOT/temp/"
"""

import argparse
import gzip
import hashlib
import io
import json
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

try:
    from cryptography.exceptions import InvalidTag
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except ImportError:
    AESGCM = None

try:
    import tomli_w
except ImportError:
    tomli_w = None


SKILL_ROOT = Path(__file__).resolve().parent.parent
DATA_ROOT = SKILL_ROOT.parents[2]
DEFAULT_OUTPUT_DIR = DATA_ROOT / "temp"
REQUIREMENTS_FILE = SKILL_ROOT / "scripts" / "requirements.txt"
SITE_URL = "https://artificialanalysis.ai/"
MODELS_PAGE_URL = urljoin(SITE_URL, "/models")
REQUEST_TIMEOUT = 30
MAX_MODELS_PAGE_BYTES = 4 * 1024 * 1024
MAX_ENCRYPTED_MANIFEST_BYTES = 16 * 1024 * 1024
MAX_DECOMPRESSED_MANIFEST_BYTES = 24 * 1024 * 1024
MANIFEST_PATTERN = re.compile(r'"manifest"\s*:\s*(?=\{)')
JSON_STRING_PATTERN = re.compile(r'"(?:[^"\\]|\\.)*"')
COST_UNIT = "USD/weighted task"


def parse_args():
    parser = argparse.ArgumentParser(
        description="下载模型名称、发布日期、intelligenceIndex 分数和评测成本（USD/weighted task），输出 TOML"
    )
    parser.add_argument(
        "-o", "--out",
        help="输出 TOML 文件或目录，默认为数据仓库根目录的 temp/；显式相对路径基于当前工作目录",
    )
    parser.add_argument("--pretty", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("-f", "--force", action="store_true", help="输出文件已存在时直接覆盖")
    return parser.parse_args()


def resolve_output_file(output):
    date = datetime.now(timezone.utc).date().isoformat()
    default_name = f"artificial-analysis-models-{date}.toml"
    if not output:
        return DEFAULT_OUTPUT_DIR / default_name

    target = Path(output).expanduser().resolve()
    is_directory = target.is_dir() if target.exists() else not target.suffix
    return target / default_name if is_directory else target


def fetch_buffer(url, maximum_bytes):
    request = Request(
        url,
        headers={
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "User-Agent": "Mozilla/5.0 ArtificialAnalysisDataFetcher/1.0",
        },
    )
    try:
        with urlopen(request, timeout=REQUEST_TIMEOUT) as response:
            content_length = response.headers.get("Content-Length")
            if content_length:
                try:
                    size = int(content_length)
                except ValueError:
                    size = 0
                if size > maximum_bytes:
                    raise ValueError(f"响应超过大小限制 {maximum_bytes} 字节")

            data = response.read(maximum_bytes + 1)
            if len(data) > maximum_bytes:
                raise ValueError(f"响应超过大小限制 {maximum_bytes} 字节")
            return data
    except HTTPError as error:
        raise RuntimeError(f"请求 {url} 失败：HTTP {error.code}") from error


def find_manifest_entries(html):
    # 同时支持普通 JSON 和 Next.js 等页面中的 JSON 字符串，按层解码，
    # 避免全局替换转义符破坏路径及嵌套字段。
    decoder = json.JSONDecoder()
    entries = []
    seen = set()
    pending = [html]
    for _ in range(5):
        nested = []
        for text in pending:
            for match in MANIFEST_PATTERN.finditer(text):
                try:
                    manifest, _ = decoder.raw_decode(text, match.end())
                except json.JSONDecodeError:
                    continue
                path, key = manifest.get("path"), manifest.get("key")
                if not isinstance(path, str) or not path.strip():
                    continue
                if not isinstance(key, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", key):
                    continue
                entry = (path, key.lower())
                if entry not in seen:
                    seen.add(entry)
                    entries.append(entry)
            for match in JSON_STRING_PATTERN.finditer(text):
                if "manifest" not in match.group():
                    continue
                try:
                    decoded = json.loads(match.group())
                except json.JSONDecodeError:
                    continue
                if decoded != "manifest":
                    nested.append(decoded)
        pending = nested
        if not pending:
            break

    if not entries:
        raise ValueError("模型页面中没有找到数据清单；网站页面结构可能已经变化")
    return entries


def decrypt_manifest(encrypted, key_hex):
    if len(encrypted) <= 16:
        raise ValueError("加密清单长度异常")

    key = bytes.fromhex(key_hex)
    iv = hashlib.sha256(key).digest()[:12]
    try:
        compressed = AESGCM(key).decrypt(iv, encrypted, None)
    except InvalidTag as error:
        raise ValueError("AES-GCM 认证失败") from error

    with gzip.GzipFile(fileobj=io.BytesIO(compressed)) as stream:
        decompressed = stream.read(MAX_DECOMPRESSED_MANIFEST_BYTES + 1)
    if len(decompressed) > MAX_DECOMPRESSED_MANIFEST_BYTES:
        raise ValueError(f"解压后数据超过大小限制 {MAX_DECOMPRESSED_MANIFEST_BYTES} 字节")
    return decompressed


def is_model_dataset(data):
    if not isinstance(data, dict) or not isinstance(data.get("models"), list) or not data["models"]:
        return False

    for model in data["models"]:
        if not isinstance(model, dict):
            return False
        if "name" not in model:
            return False
        if type(model.get("deprecated")) is not bool:
            return False
        if "price1mInputTokens" not in model or "price1mOutputTokens" not in model:
            return False
        has_headline = isinstance(model.get("headline"), dict) or (
            "headline" in model and model["headline"] is None
        )
        if not has_headline and not isinstance(model.get("timescaleData"), dict):
            return False
    # 单条配置可以没有分数，但整个数据集必须能识别 Index 字段。
    return any("intelligenceIndex" in model for model in data["models"])


def select_dataset(candidates):
    if not candidates:
        raise RuntimeError("没有找到包含模型和 Index 字段的主数据集")
    first = candidates[0]
    if any(candidate["data"] != first["data"] for candidate in candidates[1:]):
        urls = ", ".join(candidate["url"] for candidate in candidates)
        raise ValueError(f"主数据集存在歧义，不能按模型数量或出现顺序选择：{urls}")
    return first["data"], list(dict.fromkeys(candidate["url"] for candidate in candidates))


def optional_number(value, label, nonnegative=False):
    if value is None:
        return None
    if type(value) not in (int, float) or (
        isinstance(value, float) and not math.isfinite(value)
    ):
        raise ValueError(f"{label}: 必须是有限数值且不能是布尔值")
    if nonnegative and value < 0:
        raise ValueError(f"{label}: 成本不能为负数")
    return value


def optional_text(value, label):
    if value is not None and (not isinstance(value, str) or not value.strip()):
        raise ValueError(f"{label}: 必须是非空字符串")
    return value


def simplify_dataset(data):
    models = []
    for index, model in enumerate(data["models"]):
        label = f"models[{index}] ({model.get('name')!r})"
        name = optional_text(model.get("name"), f"{label}.name")
        if name is None:
            raise ValueError(f"{label}.name: 缺少模型名称")
        release_date = optional_text(model.get("releaseDate"), f"{label}.releaseDate")
        if release_date is not None:
            try:
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}(?:T.+)?", release_date):
                    raise ValueError
                datetime.fromisoformat(release_date)
            except ValueError:
                raise ValueError(f"{label}.releaseDate: 必须是 ISO 日期或日期时间") from None
        per_task = model.get("intelligenceIndexCostPerTask")
        if per_task is not None and not isinstance(per_task, dict):
            raise ValueError(f"{label}.intelligenceIndexCostPerTask: 必须是对象或 null")
        cost = per_task.get("cost") if isinstance(per_task, dict) else None
        if cost is not None and not isinstance(cost, dict):
            raise ValueError(f"{label}.intelligenceIndexCostPerTask.cost: 必须是对象或 null")
        models.append({
            "name": name,
            "slug": optional_text(model.get("slug"), f"{label}.slug"),
            "releaseDate": release_date,
            "intelligenceIndex": optional_number(
                model.get("intelligenceIndex"), f"{label}.intelligenceIndex"
            ),
            "cost": optional_number(
                cost.get("total") if isinstance(cost, dict) else None,
                f"{label}.intelligenceIndexCostPerTask.cost.total", nonnegative=True,
            ),
        })
    models.sort(key=lambda model: model["releaseDate"] or "", reverse=True)
    return {"models": models}


def serialize_toml(data):
    # TOML 无 null 类型，省略缺失字段，而不是将它们转换为 0 或字符串。
    models = [
        {key: value for key, value in model.items() if value is not None}
        for model in data["models"]
    ]
    return tomli_w.dumps({**data, "models": models}).encode("utf-8")


def summarize(models):
    return {
        "models": len(models),
        "scores": sum(model.get("intelligenceIndex") is not None for model in models),
        "costs_missing": sum(model.get("cost") is None for model in models),
        "costs_zero": sum(model.get("cost") == 0 for model in models),
    }


def save_output(path, output, force):
    path.parent.mkdir(parents=True, exist_ok=True)
    if force:
        path.write_bytes(output)
        return path

    # 独占创建文件，避免并发运行时覆盖已有数据。
    candidate = path
    index = 2
    while True:
        try:
            with candidate.open("xb") as file:
                file.write(output)
            return candidate
        except FileExistsError:
            candidate = path.with_name(f"{path.stem}-{index}{path.suffix}")
            index += 1


def main():
    options = parse_args()
    if AESGCM is None or tomli_w is None:
        raise RuntimeError(
            f"当前解释器 {sys.executable} 缺少下载依赖。"
            f"请按 SKILL.md 创建临时虚拟环境，安装 {REQUIREMENTS_FILE}，"
            "再用该环境的 Python 运行；不要向系统或已有环境直接安装。"
        )

    print("[ArtificialAnalysis] 正在读取模型页面…")
    models_page = fetch_buffer(MODELS_PAGE_URL, MAX_MODELS_PAGE_BYTES)
    entries = find_manifest_entries(models_page.decode("utf-8", errors="replace"))
    print(f"[ArtificialAnalysis] 找到 {len(entries)} 个加密清单")

    candidates = []
    for path, key in entries:
        manifest_url = urljoin(SITE_URL, path)
        try:
            encrypted = fetch_buffer(manifest_url, MAX_ENCRYPTED_MANIFEST_BYTES)
            raw = decrypt_manifest(encrypted, key)
            data = json.loads(raw.decode("utf-8"))
            if not is_model_dataset(data):
                print(f"[ArtificialAnalysis] 跳过 {path}：不是包含模型和 Index 字段的主数据集")
                continue
            print(f"[ArtificialAnalysis] 候选 {path}：{len(data['models'])} 个模型")
            candidates.append({"data": data, "url": manifest_url})
        except Exception as error:
            print(f"[ArtificialAnalysis] 跳过 {path}：{str(error) or type(error).__name__}", file=sys.stderr)

    data, manifest_urls = select_dataset(candidates)
    simplified = simplify_dataset(data)
    simplified = {
        "snapshot": {
            "format_version": 1,
            "downloaded_at": datetime.now(timezone.utc).isoformat(),
            "page_url": MODELS_PAGE_URL,
            "manifest_urls": manifest_urls,
            "cost_unit": COST_UNIT,
        },
        **simplified,
    }
    output = serialize_toml(simplified)
    output_file = save_output(resolve_output_file(options.out), output, options.force)

    summary = summarize(simplified["models"])
    digest = hashlib.sha256(output).hexdigest()
    print(f"[ArtificialAnalysis] 已保存 {summary['models']} 个模型 → {output_file}")
    print(f"[ArtificialAnalysis] 有效分数：{summary['scores']} 个；"
          f"成本缺失：{summary['costs_missing']} 个；零成本：{summary['costs_zero']} 个")
    print("[ArtificialAnalysis] cost 口径：USD/weighted task；来源零值未经核实，不自动导入成绩")
    print(f"[ArtificialAnalysis] 数据清单：{', '.join(manifest_urls)}")
    print(f"[ArtificialAnalysis] 文件大小：{len(output)} 字节")
    print(f"[ArtificialAnalysis] SHA-256：{digest}")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"[ArtificialAnalysis] 下载失败：{str(error) or type(error).__name__}", file=sys.stderr)
        sys.exit(1)
