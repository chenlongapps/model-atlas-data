"""Build the data and serve the Web Explorer locally (Python 3.11+)."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import shutil
import sys
import tempfile

if __package__:
    from .build import ROOT, build
else:
    from build import ROOT, build


def port_number(value):
    try:
        port = int(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("端口必须是 0 到 65535 之间的整数") from error
    if not 0 <= port <= 65535:
        raise argparse.ArgumentTypeError("端口必须是 0 到 65535 之间的整数")
    return port


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=port_number, default=8000,
                        help="local port (default: 8000; 0 selects an available port)")
    args = parser.parse_args(argv)

    try:
        with tempfile.TemporaryDirectory(prefix="model-atlas-preview-") as directory:
            output = Path(directory)
            models, definitions, locales, warnings = build(ROOT, output)
            for warning in warnings:
                print(f"警告：{warning}", file=sys.stderr)
            shutil.copy2(ROOT / "LICENSE.models-dev", output / "LICENSE.models-dev")
            shutil.copytree(ROOT / "web", output, dirs_exist_ok=True)
            handler = partial(SimpleHTTPRequestHandler, directory=str(output))
            with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
                print(f"构建完成：{models} 个模型，{definitions} 个 Benchmark 定义，{locales} 个语言文件")
                print(f"预览地址：http://127.0.0.1:{server.server_port}/ （按 Ctrl+C 停止）", flush=True)
                server.serve_forever()
    except KeyboardInterrupt:
        print("\n预览已停止。")
    except (OSError, ValueError, TypeError) as error:
        print(f"预览失败：{error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
