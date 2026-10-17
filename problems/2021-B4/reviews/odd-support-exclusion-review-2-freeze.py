"""Freeze a hand-reconstructed finite whole audit; no math program."""
from pathlib import Path
import json
import hashlib
import datetime

ROOT=Path(__file__).resolve().parents[3]
P="problems/2021-B4/reviews/odd-support-exclusion-review-2-"


def row(path):
    raw=(ROOT/path).read_bytes()
    return {"path":path,"bytes":len(raw),"sha256":hashlib.sha256(raw).hexdigest()}


def check(expected):
    actual=row(expected["path"])
    assert actual["sha256"]==expected["sha256"],actual
    if "bytes" in expected:
        assert actual["bytes"]==expected["bytes"],actual
    return actual


def write(suffix,obj):
    path=P+suffix
    with (ROOT/path).open("x",encoding="utf-8") as out:
        json.dump(obj,out,ensure_ascii=False,indent=2)
        out.write("\n")
    return row(path)


target=check({"path":"problems/2021-B4/notes/coordinator-odd-support-exclusion-candidate-v1.md","sha256":"a7845441df7725edc5d30e28f7b8f28c529b0b710168ad4b068d279582c1857c"})
source_manifest=check({"path":"problems/2021-B4/notes/coordinator-odd-support-exclusion-freeze-v1.json","sha256":"337a43225bd6637d666bc992738a49afab8e7b569f526281add45564ab17b592"})
source=json.loads((ROOT/source_manifest["path"]).read_text())
inputs=[check(r) for r in source["files"]]
inputs.append(check({"path":"AGENTS.md","sha256":"28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"}))
inputs.append(row("problems/2021-B4/statement.md"))
previous_manifest=check({"path":"problems/2017-B4/reviews/orientation-chart-review-1-manifest-initial.json","sha256":"35104507f2faffbd0444e727a1e97ed89e614584e910147b86653bd89b6c93d7"})
previous=json.loads((ROOT/previous_manifest["path"]).read_text())
preserved={previous_manifest["path"]:previous_manifest}
for r in previous["artifacts"]:
    a=check(r)
    preserved[a["path"]]=a
old=json.loads((ROOT/"problems/2017-B4/reviews/orientation-chart-review-1-input-validation.json").read_text())
for r in old["all_earlier_unique_frozen_records_preserved"]:
    a=check(r)
    preserved[a["path"]]=a
validation=write("input-validation.json",{
    "validated_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "candidate":target,"candidate_manifest":source_manifest,
    "declared_inputs_checked":inputs,
    "earlier_unique_records_preserved":sorted(preserved.values(),key=lambda r:r["path"]),
    "earlier_unique_count":len(preserved),
    "all64_hand_reconstructed":True,
    "constructor_code_rerun_or_output_used_as_proof":False,
    "mathematical_program_or_CAS":False,
    "no_peer_PN_review_read":True
})
artifacts=[row(P+s) for s in ["initial.md","issues.md","source-checks.md","freeze.py"]]+[validation]
manifest=write("manifest-initial.json",{
    "frozen_at_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status":"initially blind whole independent nonconstructor audit; no substantive defect found; no promotion",
    "reviewer":"review_2017_coarsening_r1",
    "requested_settings":{"model":"gpt-6.1-sol","reasoning":"max"},
    "verified_effective_settings":None,
    "candidate":target,"candidate_manifest":source_manifest,
    "whole_claims_reconstructed":["PN1 all64 supports","PN2 exact derivative/Taylor obstruction","PN3 accepted PP1 scope application","PN4 accepted PP2 scope application"],
    "substantive_issues":[],
    "peer_findings_read_before_initial_freeze":False,
    "constructed_argument":False,
    "artifacts":artifacts,
    "declared_constructor_records_verified":len(source["files"]),
    "earlier_unique_frozen_records_preserved":len(preserved),
    "all64_entries_independently_reconstructed_by_hand":True,
    "new_mathematical_program_CAS_or_author_rerun":False,
    "only_assigned_review_prefix_written":True,
    "git_shared_edits_spawning_contacts_charges_or_bypass":False,
    "reviewer_promotion":False,
    "full_degree20_masks_general_repeated_branch_or_annual_solution_claim":False,
    "latest_authoritative_weekly_total_used_percent":27,
    "telemetry_at_utc":"2026-10-17 06:44:58 UTC",
    "weekly_reset_unix":1792745187,
    "total_used_ceiling_percent":90
})
print(json.dumps({"manifest":manifest,"artifacts":artifacts,"earlier_unique_preserved":len(preserved)},indent=2))
