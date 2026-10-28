"""Validate source data and the selected local manifest/snapshot; never fetch URLs."""

import argparse
from pathlib import Path
import sys

from common import DataError, ROOT, load_catalog, read_artifacts, read_json, validate_schema
from preview_candidates import print_protection_notice, review_candidates


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifacts", type=Path, default=ROOT, help="artifact directory (default: repository bootstrap)")
    args = parser.parse_args()
    try:
        catalog = load_catalog()
        validate_schema(read_json(ROOT / "data/release.json"), "release.schema.json")
        manifest, snapshot = read_artifacts(args.artifacts)
        summary = catalog.summary()
        print(f"OK: {summary['benchmarks']} benchmarks, {summary['results']} results, {summary['approvedResults']} approved")
        print(f"OK: artifact version {manifest['version']}, {len(snapshot['scores'])} scores, SHA-256 verified")
        if summary["excludedResults"]:
            print(f"NOTICE: {len(summary['excludedResults'])} pending/rejected results are excluded from builds")
        if not snapshot["scores"]:
            print("NOTICE: empty bootstrap/preview is NOT a production release")
        for batch in sorted((ROOT / "data/reviews").glob("*/batch.json")):
            report = review_candidates(ROOT, batch)
            print(f"OK: {report['batchId']}: {report['summary']['candidateResults']} pending candidates; not deployable")
            print_protection_notice(report)
        return 0
    except DataError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
