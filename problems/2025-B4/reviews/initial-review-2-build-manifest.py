#!/usr/bin/env python3
"""Hash only the R2 audit's own artifacts and directly used primary sources."""
import hashlib
import json
from pathlib import Path
import platform
import sys
from datetime import datetime, timezone
import pypdf

ROOT = Path(__file__).resolve().parents[3]
BASE = Path(__file__).resolve().parent

def entry(relative, **data):
    path = ROOT / relative
    raw = path.read_bytes()
    return {"path": relative, "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(), **data}

primary = [
    (".cache/official/2025-paper_b.pdf",
     "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf",
     "Official Paper B; B4(b) statement only, PDF page 2"),
    (".cache/official/2025-solutions.pdf",
     "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025solutions.pdf",
     "Unsolved-part remark on PDF page 20 only"),
    (".cache/literature/2025/bennett-levin-2015.pdf",
     "https://personal.math.ubc.ca/~bennett/BeLe-Mona-2015.pdf",
     "Author-posted published paper; equation (1), Proposition 1, Theorem 1 and context"),
    (".cache/literature/2025/bugeaud-mihailescu-2007.pdf",
     "https://journals.msp.org/mscand/article/download/659/658",
     "Primary journal paper; domain, Theorem NL, Theorems 1-2 and context"),
    (".cache/literature/2025/son-2026-A44.pdf",
     "https://math.colgate.edu/~integers/aa44/aa44.pdf",
     "Original journal paper, all five pages read"),
    (".cache/literature/2025/initial-review-1-chen-mihailescu-2026-complete.pdf",
     "https://camath.fudan.edu.cn/cambcn/ch/reader/create_pdf.aspx?file_no=47B208&flag=1",
     "Primary 24-page journal PDF only; no other review artifact was read"),
]

sources = [entry(p, url=u, use=use, primary_source=True,
                 redistribution="not verified; original paper retained only in ignored cache",
                 verification_utc_date="2026-10-16") for p, u, use in primary]
sources.append(entry(".cache/literature/2025/initial-review-2-wang-provider-snapshot.json",
    urls=["https://www.preprints.org/manuscript/202512.0286/v1",
          "https://www.preprints.org/manuscript/202512.0286/v1/download"],
    primary_source=True, format="provider-extracted primary HTML text snapshot, not original bytes",
    use="Full relevant Theorem 7 and 8 context; separately compared against provider PDF text",
    original_pdf_bytes_available=False,
    access_limit="Direct HTML and PDF curl requests returned HTTP 403; no bypass attempted",
    verification_utc_date="2026-10-16",
    redistribution="No original paper committed; extraction remains in ignored cache"))

author_paths = ["AGENTS.md", "problems/2025-B4/proof.md", "problems/2025-B4/statement.md",
                "problems/2025-B4/references.md", "problems/2025-B4/computations/literature-audit.md",
                "problems/2025-B4/computations/source-manifest.json", "problems/2025-B4/research.md"]
artifacts = []
for path in sorted(BASE.glob("initial-review-2*")):
    if path.is_file() and path.name != "initial-review-2-manifest.json":
        artifacts.append(entry(str(path.relative_to(ROOT))))

cache_artifacts = []
for path in sorted((ROOT / ".cache/literature/2025").glob("initial-review-2*")):
    if path.is_file():
        cache_artifacts.append(entry(str(path.relative_to(ROOT))))

proof_hash = next(x["sha256"] for x in map(entry, author_paths)
                  if x["path"] == "problems/2025-B4/proof.md")
assert proof_hash == "c422139567ee3e2f4eafd852c9a3f5fac73cb6c8e0bfdf9e2c9c5311a9348b0d"
manifest = {
    "review": "Independent blind R2, P2025-v1, partial candidate only",
    "generated_utc": datetime.now(timezone.utc).isoformat(),
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max",
                           "evidence": "coordinator launch request"},
    "effective_settings_readback": "unavailable; not inferred",
    "usage_readings": {"source": "authoritative get_usage_limits tool",
                       "weekly_used_percent": [9, 9], "weekly_reset_unix": 1792745187,
                       "project_stop_used_percent": 90},
    "primary_sources": sources,
    "author_inputs_unchanged_by_reviewer": list(map(entry, author_paths)),
    "review_artifacts": artifacts,
    "ignored_cache_artifacts": cache_artifacts,
    "runtime": {"executable": sys.executable, "python": sys.version,
                "platform": platform.platform(), "arithmetic_dependencies": "stdlib only",
                "pdf_extraction": {"package": "pypdf", "version": pypdf.__version__,
                                   "location": "bundled primary runtime"},
                "rendering": "bundled pdftoppm; version recorded separately in access log"},
    "independence": {"other_review_conclusions_read": False,
                     "shared_issue_or_progress_files_read": False,
                     "author_research_log_read": "only after independent C1-C4 reconstruction, for cited import restrictions"},
    "limitations": ["No unrestricted proof claimed", "No published theorem proof fully reconstructed",
                    "No original Wang PDF byte hash available; extracted source snapshot explicitly distinguished",
                    "No preliminary degree-three odd-exponent solution was investigated"],
}
target = BASE / "initial-review-2-manifest.json"
target.write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"manifest": str(target), "sources": len(sources),
                  "review_artifacts": len(artifacts), "proof_hash_unchanged": True}))
