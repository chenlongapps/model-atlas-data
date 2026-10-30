"""Check source TOML syntax using Python 3.11+ (no third-party dependencies)."""

from pathlib import Path
import sys
import tomllib


ROOT = Path(__file__).resolve().parent.parent
DATA_DIRS = ("models", "benchmarks", "i18n")


def main(root: Path = ROOT) -> int:
    files = sorted(
        path
        for directory in DATA_DIRS
        for path in (root / directory).rglob("*.toml")
        if path.is_file()
    )
    if not files:
        print("未找到 TOML 文件（models/、benchmarks/、i18n/）。", file=sys.stderr)
        return 1

    failed = 0
    for path in files:
        try:
            with path.open("rb") as source:
                tomllib.load(source)
        except (tomllib.TOMLDecodeError, UnicodeDecodeError, OSError) as error:
            failed += 1
            print(f"{path.relative_to(root)}: {error}", file=sys.stderr)

    print(f"检查 {len(files)} 个 TOML 文件：成功 {len(files) - failed}，失败 {failed}。")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
