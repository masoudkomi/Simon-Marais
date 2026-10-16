#!/usr/bin/env python3
"""Cache official source PDFs and save a reproducible retrieval manifest.

Uses only Python's standard library. This downloads whole original source papers;
only their B4 statements and solution sections are within the research scope.
"""
import argparse
import concurrent.futures
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


def fetch(item):
    year, kind, url = item
    target = ROOT / ".cache" / "official" / f"{year}-{kind}.pdf"
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        data = target.read_bytes()
        disposition = "cached"
    else:
        request = Request(url, headers={"User-Agent": "SMMC-B4-source-verification/1.0"})
        with urlopen(request, timeout=60) as response:
            data = response.read()
        if not data.startswith(b"%PDF-"):
            raise ValueError(f"Expected PDF at {url}")
        target.write_bytes(data)
        disposition = "downloaded"
    if not data.startswith(b"%PDF-"):
        raise ValueError(f"Invalid cached PDF: {target}")
    return {"year": year, "kind": kind, "url": url,
            "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
            "cache_path": str(target.relative_to(ROOT)), "disposition": disposition}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--years", type=int, nargs="*")
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args()
    sources = json.loads((ROOT / "sources" / "official.json").read_text())
    items = [(s["year"], kind, s[kind]) for s in sources
             if not args.years or s["year"] in args.years
             for kind in ("paper_b", "solutions")]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        records = sorted(pool.map(fetch, items), key=lambda r: (r["year"], r["kind"]))
    output = ROOT / "sources" / "retrieval.json"
    previous = json.loads(output.read_text()) if output.exists() else {"records": []}
    merged = {(r["year"], r["kind"]): r for r in previous["records"]}
    merged.update({(r["year"], r["kind"]): r for r in records})
    output.write_text(json.dumps({"observed_at_utc": datetime.now(timezone.utc).isoformat(),
                                  "records": [merged[k] for k in sorted(merged)]}, indent=2) + "\n")
    print(f"Verified {len(records)} PDFs; wrote {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
