#!/usr/bin/env python3
"""Check official open designations, inspecting only B4 on page 2; requires pypdf."""
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
import pypdf

ROOT = Path(__file__).resolve().parents[1]
records = []
for source in json.loads((ROOT / "sources/official.json").read_text()):
    year = source["year"]
    path = ROOT / ".cache/official" / f"{year}-paper_b.pdf"
    reader = pypdf.PdfReader(path)
    text = reader.pages[source["b4_page"] - 1].extract_text()
    marker = re.search(r"B\s*4\b", text)
    if marker is None:
        raise ValueError(f"Missing B4 marker in {year}")
    b4 = re.sub(r"\s+", " ", text[marker.start():])
    if year <= 2018:
        evidence = "no solution is currently known"
        target = "whole problem" if year == 2017 else "general enumeration; known m=5 case excluded"
    elif year <= 2020:
        evidence = "no solution is currently known to part (b)"
        target = "part (b) only"
    else:
        evidence = "the answer to part (b) is not currently known"
        target = "part (b) only"
    if evidence not in b4:
        raise ValueError(f"Official designation mismatch for {year}: expected {evidence!r}")
    records.append({"year": year, "paper_url": source["paper_b"], "page": source["b4_page"],
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "designation_excerpt": evidence, "authorized_research_target": target,
                    "designation_is_as_issued_not_a_current_literature_claim": True})
output = ROOT / "sources/open-scope-audit.json"
output.write_text(json.dumps({"checked_at_utc": datetime.now(timezone.utc).isoformat(),
                              "pypdf_version": pypdf.__version__, "records": records}, indent=2) + "\n")
print(f"Verified {len(records)} official B4 open designations; 2019-2025 are part (b) only.")
