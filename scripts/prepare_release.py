"""Build the reviewed data/release.json version locally. Does not publish anything."""

import argparse
from pathlib import Path
import sys

from build import build
from common import DataError, ROOT, read_json, validate_schema


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, default=ROOT / "build/site")
    args = parser.parse_args()
    try:
        release = read_json(ROOT / "data/release.json")
        validate_schema(release, "release.schema.json")
        report = build(ROOT, args.output, release["version"], baseline=args.baseline, release=True,
                       allow_removals=release["allowRemovals"], reason=release["reason"])
        print(f"OK: release v{report['version']}, {report['scoreCount']} scores; not deployed")
        return 0
    except (DataError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
