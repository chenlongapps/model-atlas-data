"""Check TOML syntax and optionally verify the generated Benchmark results."""

import argparse
from pathlib import Path
import sys
import tomllib

if __package__:
    from . import benchmark_results
    from .build import load_sources
else:
    import benchmark_results
    from build import load_sources

ROOT = Path(__file__).resolve().parent.parent
DATA_DIRS = ("models", "benchmarks", "i18n", benchmark_results.DIRECTORY)


def main(root: Path = ROOT, *, check_results=False) -> int:
    files = sorted(
        path
        for directory in DATA_DIRS
        for path in (root / directory).rglob("*.toml")
        if path.is_file()
    )
    if not files:
        print(f"未找到 TOML 文件（{', '.join(DATA_DIRS)}）。", file=sys.stderr)
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
    if failed:
        return 1
    if check_results:
        try:
            models, definitions, _ = load_sources(root)
            results, _ = benchmark_results.collect_results(models, definitions)
            expected = benchmark_results.toml_documents(results)
            actual = benchmark_results.existing_toml(root / benchmark_results.DIRECTORY)
        except (OSError, ValueError, TypeError) as error:
            print(f"Benchmark 成绩校验失败：{error}", file=sys.stderr)
            return 1
        differing = sorted(path for path in expected.keys() | actual.keys()
                           if expected.get(path) != actual.get(path))
        if differing:
            print("汇总结果与源数据不一致，请运行 python3 scripts/build.py。", file=sys.stderr)
            for path in differing:
                print(f"{benchmark_results.DIRECTORY}/{path.as_posix()}", file=sys.stderr)
            return 1
        print(f"Benchmark 汇总校验通过：{len(expected)} 个 TOML 文件与源数据一致。")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-results", action="store_true", help="verify benchmark-results/ against source data")
    sys.exit(main(check_results=parser.parse_args().check_results))
