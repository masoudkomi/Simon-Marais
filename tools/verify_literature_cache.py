#!/usr/bin/env python3
"""Check local public-paper fingerprints; never fetch or redistribute papers."""
import hashlib
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "sources/literature-retrieval.json").read_text())
    verified = missing = mismatches = unavailable = 0
    for record in manifest["records"]:
        if record["status"] != "cached locally":
            unavailable += 1
            continue
        path = root / record["cache_path"]
        if not path.is_file():
            missing += 1
            print("LOCAL CACHE MISSING:", record["cache_path"])
            continue
        data = path.read_bytes()
        if not data.startswith(b"%PDF") or hashlib.sha256(data).hexdigest() != record["sha256"]:
            mismatches += 1
            print("FINGERPRINT MISMATCH:", record["cache_path"])
        else:
            verified += 1
    print(f"Verified={verified}; missing local cache={missing}; mismatches={mismatches}; recorded unavailable={unavailable}")
    print("Full papers stay in ignored local cache; a fresh clone normally lacks it.")
    print("See progress/permissions.md for the earlier 2018 PDFs retained in old Git history.")
    raise SystemExit(1 if mismatches else 0)


if __name__ == "__main__":
    main()
