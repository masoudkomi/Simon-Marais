#!/usr/bin/env python3
"""Seal R2's targeted v1.1 review before cross-review; no candidate mutations."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]


def record(path):
    data=path.read_bytes()
    return {"path":str(path.relative_to(ROOT)),"bytes":len(data),
            "sha256":hashlib.sha256(data).hexdigest()}


names=("author-repair-macmahon-candidate-v1.1.md",
       "author-repair-boundary-fiber-candidate-v1.1.md",
       "author-repair-periodic-grid-candidate-v1.1.md",
       "author-repair-macmahon-v1-to-v1.1.diff",
       "author-repair-boundary-fiber-v1-to-v1.1.diff",
       "author-repair-periodic-grid-v1-to-v1.1.diff",
       "author-repair-changelog-v1.1.md","author-repair-manifest-v1.1.json",
       "author-repair-sources-v1.1.json","author-repair-checkpoint-v1.1.json")
original=record(HERE/"secondpass-review-2-initial.md")
assert original["sha256"]=="1780d421be9d46158f02428ab4a46e0504f3fd3733e31c6e37a398c35cd32012"
seal={
    "frozen_utc":datetime.now(timezone.utc).isoformat(),
    "reviewer":"/root/review_2017_secondpass_r2",
    "status":"R2 targeted v1.1 re-audit complete; no unresolved objection in stated scope; no promotion",
    "other_targeted_reaudit_seen_before_freeze":False,
    "author_inputs":[record(ROOT/"problems/2017-B4/notes"/name) for name in names],
    "preserved_initial_R2_report":original,
    "reaudit_outputs":[record(path) for path in sorted(HERE.glob("secondpass-review-2-reaudit*"))
                       if path.is_file() and path.name!="secondpass-review-2-reaudit-freeze.json"],
    "independent_check_job":json.loads((HERE/"secondpass-review-2-reaudit-check-job.json").read_text()),
    "requested_settings":{"model":"gpt-6.1-sol","reasoning_effort":"max"},
    "verified_effective_settings":None,
    "authoritative_weekly_usage":{"total_used_percent":10,"reset_timestamp":1792745187,
        "window_duration_minutes":10080,"final_check_utc":"2026-10-16 16:10:22 UTC",
        "tool":"mcp__codex_app__get_usage_limits","stop_total_used_percent":90},
    "closed_for_R2_v1_1":["R2-G2-1","R2-G1-1","R2-F1-1","R2-F2-1","R2-F3-1"],
    "unresolved_objections":[],
    "scope_limits":"Partial 2017 results only; no exact B4 rates, novelty, stronger published-bound proof or L4 count"
}
target=HERE/"secondpass-review-2-reaudit-freeze.json"
target.write_text(json.dumps(seal,indent=2)+"\n")
print(json.dumps({"report":record(HERE/"secondpass-review-2-reaudit-v1.1.md"),
                  "seal":record(target),"frozen_utc":seal["frozen_utc"]},indent=2))
