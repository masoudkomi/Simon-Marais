#!/usr/bin/env python3
"""Freeze only R2's report and actual examined inputs; no research computation."""

from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CACHE = ROOT/".cache/literature/2020/initial-review-2"
EXPECTED = "f53945e49bd626847e52a61f7e39e96defd2ae44900f9d235c2c14e720f41525"


def info(path):
    return {"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


target = ROOT/"problems/2020-B4/proofs/partial-v1.md"
assert info(target)["sha256"] == EXPECTED
inputs = [
    "AGENTS.md", "problems/2020-B4/proofs/partial-v1.md",
    "problems/2020-B4/statement.md", "problems/2020-B4/references.md",
    "problems/2020-B4/computations/README.md",
    "problems/2020-B4/computations/residual_orders.py",
    "problems/2020-B4/computations/residual-orders.json",
    "problems/2020-B4/computations/quotient-counts.json",
    "problems/2020-B4/computations/orbit-examples.json",
    ".cache/official/2020-paper_b.pdf", ".cache/official/2020-solutions.pdf",
]
own = [path for path in sorted(HERE.glob("initial-review-2*"))
       if path.is_file() and path.name != "initial-review-2-manifest.json"]
cache = [path for path in sorted(CACHE.iterdir()) if path.is_file()]
job = json.loads((HERE/"initial-review-2-job.json").read_text())
evidence = json.loads((HERE/"initial-review-2-evidence.json").read_text())
assert job["returncode"] == 0 and not job["timed_out"]
assert evidence["all_checks_passed"]
assert info(HERE/"initial-review-2-check.py")["sha256"] == job["child_script_sha256"]
issues = json.loads((HERE/"initial-review-2-issues.json").read_text())
assert issues["unresolved_substantive_objections"] == []
manifest = {
    "frozen_utc": datetime.now(timezone.utc).isoformat(),
    "candidate_sha256": EXPECTED,
    "initial_report_blind": True,
    "other_reviewer_material_read": False,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "effective_settings_readback": None,
    "weekly_telemetry": {"used_percent": 12, "window_duration_mins": 10080,
        "resets_at": 1792745187, "checked_utc_approx": "2026-10-16T16:48:33Z"},
    "own_review_files": [info(path) for path in own],
    "examined_author_or_official_inputs": [info(ROOT/path) for path in inputs],
    "own_ignored_source_cache": [info(path) for path in cache],
    "source_access_limits": ["Original Jungnickel-Vedder/Wilbrink full PDFs HTTP403",
        "Original imported proofs not reconstructed; exact Gordon1994 statements checked",
        "Optional renderer exitcode and OSprocesscleanup not verified"],
    "finite_job": {"pid": job["child_pid"], "returncode": job["returncode"],
        "timed_out": job["timed_out"], "timeout_seconds": job["timeout_seconds"],
        "started_utc": job["started_utc"], "finished_utc": job["finished_utc"]},
    "verdict": issues["verdict"],
    "promotion": "None by reviewer; coordinator only after both independent audits",
    "manifest_self_hash": "Excluded to avoid self-reference; all own review files otherwise hashed",
}
output = HERE/"initial-review-2-manifest.json"
output.write_text(json.dumps(manifest, indent=2, sort_keys=True)+"\n")
print(json.dumps({"manifest": str(output), "candidate_sha256": EXPECTED,
    "own_files": len(own), "input_files": len(inputs), "cache_files": len(cache),
    "report_sha256": info(HERE/"initial-review-2.md")["sha256"]}, sort_keys=True))
