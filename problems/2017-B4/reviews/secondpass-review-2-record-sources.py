#!/usr/bin/env python3
"""Preserve R2 primary-source fingerprints and initial independent-report seal."""
from datetime import datetime, timezone
from pathlib import Path
from pypdf import PdfReader
import hashlib
import json
import platform
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def fingerprint(path):
    content = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(content),
            "sha256": hashlib.sha256(content).hexdigest()}


records = [
    (".cache/official/2017-paper_b.pdf",
     "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf",
     "B4 on p. 2; exact domain and target; other problems not investigated"),
    (".cache/official/2017-solutions.pdf",
     "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf",
     "p. 12: intended C(n) convention and published dictionary"),
    (".cache/literature/2017/cited-7f7251133b0c4ebc.pdf",
     "https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf",
     "Sections 1, 2, 4; marked convention; quadratic upper bound; pp. 11 product/completion"),
    (".cache/literature/2017/cited-b5bf6499a3fedd25.pdf",
     "https://arxiv.org/pdf/2402.13107",
     "Downloaded bytes identify arXiv v2; pp. 2-4, 12-14 and 19: conventions, simple partial input, tail disks, cut recurrence"),
    (".cache/literature/2017/secondpass-review-2-felsner-weil.pdf",
     "https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf",
     "Printed pp. 15 and 19 visually inspected: Theorems 7-8 and rank-three proof"),
    (".cache/literature/2017/cited-95c9ccd7e229423b.pdf",
     "https://arxiv.org/pdf/2503.02336",
     "pp. 2-3 only: consistency of marked wiring counts; not used to establish four-packet sufficiency"),
]
sources = []
for name, url, inspected in records:
    item = fingerprint(ROOT/name)
    item.update(url=url, inspected=inspected,
                redistribution_licence_verified_for_this_review=False,
                tracked_full_paper=False)
    sources.append(item)

# Preserve the exact unusable extraction that prompted visual inspection.
fw = PdfReader(ROOT/".cache/literature/2017/secondpass-review-2-felsner-weil.pdf")
raw = "\n".join("PAGE "+str(i+1)+"\n"+fw.pages[i].extract_text()
                for i in (12, 13, 14, 18))
raw_path = ROOT/".cache/literature/2017/secondpass-review-2-fw-unusable-pypdf.txt"
raw_path.write_text(raw)

manifest = {
    "recorded_utc": datetime.now(timezone.utc).isoformat(),
    "scope": "Independent R2 initial audit of exactly three frozen 2017 B4 second-pass packets",
    "reviewer": "/root/review_2017_secondpass_r2",
    "independence": "No other report or conclusion read; no cross-review before this seal",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning_effort": "max",
                           "launch_acceptance": "reported by coordinator"},
    "verified_effective_settings": None,
    "weekly_telemetry": {"tool": "mcp__codex_app__get_usage_limits",
                         "total_used_percent_first_check": 8,
                         "total_used_percent_final_check": 9,
                         "final_check_utc": "2026-10-16 15:42:26 UTC",
                         "window_duration_minutes": 10080, "reset_timestamp": 1792745187,
                         "stop_threshold_total_used_percent": 90},
    "dependencies": {"python_executable": sys.executable, "python_version": platform.python_version(),
                     "mathematical_checks": "Python standard library only; no author modules",
                     "source_inspection": "pypdf; pypdfium2 for rendered visual inspection"},
    "sources": sources,
    "rotation_system_reference": {
        "url": "https://jeffe.web.engr.illinois.edu/teaching/comptop/2023/notes/09-planar-graphs.html",
        "sections": ["Rotation systems", "Formalities and Trivialities"],
        "method": "Read via web tool; no byte-exact local HTML was downloaded",
        "sha256": None,
        "role": "Supplement to an elementary regular-neighborhood reconstruction in the review"
    },
    "source_failures_and_recovery": [
        {"command": "command -v pdftotext", "exit_code": 1,
         "output": "", "interpretation": "not on PATH; no installation attempted"},
        {"command": "curl -L --fail --silent --show-error --max-time 30 https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf -o .cache/literature/2017/secondpass-review-2-felsner-weil.pdf",
         "initial_exit_code": 6, "initial_output": "curl: (6) Could not resolve host: page.math.tu-berlin.de",
         "recovery": "Exact same public-cache command retried with require_escalated as required by sandbox policy; succeeded, exit 0",
         "download_process_session": 19206},
        {"operation": "pypdf extraction of Felsner-Weil PDF pages 13,14,15,19",
         "result": "Font-name/code strings, unusable for theorem verification",
         "raw_output": fingerprint(raw_path),
         "recovery": "Rendered pages 15 and 19 inspected visually; no mathematical inference from corrupt extraction"},
        {"operation": "First source-page render wrote R2-owned page PNGs in review directory",
         "child_pid": 32383, "status": "complete",
         "recovery": "Moved only these four R2-owned images to ignored .cache; corrected renderer output path; retained initial job/stdout",
         "final_render_child_pid": 32828}
    ],
    "cache_source_page_images": [fingerprint(p) for p in sorted(
        (ROOT/".cache/literature/2017").glob("secondpass-review-2-source-*.png"))],
    "frozen_candidate_inputs": [fingerprint(ROOT/name) for name in (
        "problems/2017-B4/notes/secondpass-macmahon-candidate-v1.md",
        "problems/2017-B4/notes/secondpass-boundary-fiber-candidate-v1.md",
        "problems/2017-B4/notes/secondpass-periodic-grid-candidate-v1.md")],
    "review_outputs": [fingerprint(p) for p in sorted(HERE.glob("secondpass-review-2*"))
                       if p.is_file() and p.suffix != ".png" and p.name not in (
                           "secondpass-review-2-sources.json", "secondpass-review-2-initial-freeze.json")],
    "mathematical_job": json.loads((HERE/"secondpass-review-2-check-job.json").read_text()),
    "render_job": json.loads((HERE/"secondpass-review-2-render-job.json").read_text()),
    "published_bound_scope": "0.2721 remains attributed stronger prior work; no new best bound or official entropy-limit proof",
    "open_substantive_objections": ["R2-G2-1: resolve every uncovered multicrossing before completion"],
}
target = HERE/"secondpass-review-2-sources.json"
target.write_text(json.dumps(manifest, indent=2)+"\n")
seal = {
    "frozen_utc": datetime.now(timezone.utc).isoformat(),
    "independent_initial_report": fingerprint(HERE/"secondpass-review-2-initial.md"),
    "source_and_execution_manifest": fingerprint(target),
    "no_crossreview_before_freeze": True,
    "no_other_reviewer_conclusions_read": True,
    "status": "Initial report frozen; G2 repair required; no coordinator promotion"
}
seal_path = HERE/"secondpass-review-2-initial-freeze.json"
seal_path.write_text(json.dumps(seal, indent=2)+"\n")
print(json.dumps(seal, indent=2))
