#!/usr/bin/env python3
"""Freeze R1 targeted re-audit manifest without changing any proof or old review."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
OUTPUT=HERE/"secondpass-review-1-reaudit-manifest.json"

def record(path):
    raw=path.read_bytes()
    return {"path":str(path.relative_to(ROOT)),"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}

old_review=record(HERE/"secondpass-review-1.md")
assert old_review["sha256"]=="13b22e6c664ea0880eb3508a6df06670caa84ffec18486f00696998c94d9cbc1"
expected={"macmahon":"a225f0042fc098d8a827093a3e680612848caf392db64cad24339d399769bcf0",
          "boundary-fiber":"e2891eafc6fa8449f6c70c817c2e21416a43f1893120929df02f2aa2dac86a8b",
          "periodic-grid":"1a6acb042e1e21bc0992cddbd7188c47e81249b5888faabaa4e73a45be0f5c6e"}
targets=[]
for claim,fingerprint in expected.items():
    p=ROOT/("problems/2017-B4/notes/author-repair-"+claim+"-candidate-v1.1.md")
    r=record(p);assert r["sha256"]==fingerprint;targets.append(r)
    targets.append(record(ROOT/("problems/2017-B4/notes/author-repair-"+claim+"-v1-to-v1.1.diff")))
for suffix in ("changelog-v1.1.md","manifest-v1.1.json","sources-v1.1.json","checkpoint-v1.1.json"):
    targets.append(record(ROOT/("problems/2017-B4/notes/author-repair-"+suffix)))
job=json.loads((HERE/"secondpass-review-1-reaudit-job.json").read_text())
assert job["status"]=="complete" and job["returncode"]==0
artifacts=[record(p) for p in sorted(HERE.glob("secondpass-review-1-reaudit*")) if p.is_file() and p!=OUTPUT]
manifest={
    "completed_utc":datetime.now(timezone.utc).isoformat(),
    "scope":"Targeted independent R1 re-audit of exact 2017 second-pass author repair v1.1",
    "requested_launch_settings":{"model":"gpt-6.1-sol","reasoning_effort":"max","launch_acceptance":"parent supplied existing context"},
    "verified_effective_settings":None,
    "other_reaudit_reports_or_conclusions_read":False,
    "author_changelog_read":True,
    "weekly_telemetry":{"authority":"mcp__codex_app__get_usage_limits","entry_used_percent_total":10,
        "finish_used_percent_total":10,"window_duration_minutes":10080,"resets_at":1792745187,
        "stop_percent_total":90},
    "verdict":"The changed v1.1 arguments resolve R1 objections; no remaining substantive objection identified in stated partial-result scope",
    "substantive_open_objections":[],
    "resolved_R1_points":["R1-G2-01","R1-G1-01","R1-F1-01","M2 odd full-ternary clarification"],
    "other_changed_arguments_audited":["F1 empty slots, connected exterior, facial port walk, Jordan regular-neighborhood disk",
        "F3 distinct transverse proper ports and F(empty)=1","G2 simultaneous fixed disks, recovery, simple partial input, tails, unchanged coefficient"],
    "old_R1_review":old_review,"audited_input_records":targets,
    "direct_byte_checks":{"supplied_diffs_equal_independent_four_context_line_regeneration":True,
        "M1_math_section_unchanged":True,"M3_math_section_unchanged":True,
        "author_preserved_input_hashes_verified":17,"author_checkpoint_file_hashes_verified":12,
        "source_pdf_and_page_image_hashes_verified":True},
    "finite_evidence":{"geometry_t_values":list(range(1,13))+[20],"new_patch_enumeration":False,
        "Q_3_3_unchanged":4419734746,"L4_count_used":False,"fixed_small_disk_radius":"1/1000",
        "test_support_shrink":"1/100","computation_status":"complete; finite evidence only"},
    "job":job,"artifacts":artifacts,
    "full_source_files_redistributed":False,"source_downloads":0,"proof_edits":False,
    "old_review_edits":False,"shared_log_edits":False,"commits_or_pushes":False,
    "candidate_statuses_promoted":False,"coordinator_and_other_reaudit_acceptance_still_required":True,
    "manifest_self_hash_excluded":True}
OUTPUT.write_text(json.dumps(manifest,indent=2)+"\n")
print(json.dumps({"report_sha256":record(HERE/"secondpass-review-1-reaudit.md")["sha256"],
                  "manifest_sha256":record(OUTPUT)["sha256"],"artifacts":len(artifacts),
                  "all_new_children_exited":True,"old_R1_review_unchanged":True},indent=2))
