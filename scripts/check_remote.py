"""Read-only HTTPS smoke check after publication; never writes local or remote data."""

import argparse
import sys
from urllib.error import URLError
from urllib.request import HTTPRedirectHandler, Request, build_opener

from common import (
    DEFAULT_BASE_URL, MAX_MANIFEST_BYTES, MAX_SNAPSHOT_BYTES, DataError, decode_json,
    https_url, require, sha256, validate_schema, validate_snapshot,
)


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, file, code, message, headers, new_url):
        return None


def download(url: str, limit: int) -> bytes:
    https_url(url)
    request = Request(url, headers={"User-Agent": "ModelAtlas-Data-Check/1", "Cache-Control": "no-cache"})
    with build_opener(NoRedirect()).open(request, timeout=60) as response:
        require(response.status == 200 and response.url == url, "expected direct HTTPS 200 without redirect")
        content = response.read(limit + 1)
        require(len(content) <= limit, "remote file exceeds Android byte limit")
        return content


def verify_remote(manifest_url: str, expected_version: int, fetch=download) -> int:
    https_url(manifest_url)
    header = fetch(manifest_url, MAX_MANIFEST_BYTES)
    require(len(header) <= MAX_MANIFEST_BYTES, "manifest exceeds byte limit")
    manifest = decode_json(header)
    validate_schema(manifest, "manifest-v1.schema.json")
    require(manifest["version"] == expected_version, "published manifest version differs from release")
    expected_url = manifest_url.rsplit("/", 1)[0] + f"/benchmarks/scores-v{expected_version}.json"
    require(manifest["url"] == expected_url, "unexpected published snapshot URL")
    content = fetch(manifest["url"], MAX_SNAPSHOT_BYTES)
    require(len(content) <= MAX_SNAPSHOT_BYTES, "snapshot exceeds byte limit")
    require(sha256(content).lower() == manifest["sha256"].lower(), "remote SHA-256 mismatch")
    snapshot = decode_json(content)
    validate_snapshot(snapshot)
    require(snapshot["version"] == expected_version and bool(snapshot["scores"]), "mismatched or empty remote snapshot")
    return len(snapshot["scores"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest-url", default=DEFAULT_BASE_URL + "/manifest.json")
    parser.add_argument("--expected-version", type=int, required=True)
    args = parser.parse_args()
    try:
        count = verify_remote(args.manifest_url, args.expected_version)
        print(f"OK: direct HTTPS 200, v{args.expected_version}, {count} scores, SHA-256 verified")
        return 0
    except (DataError, OSError, URLError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
