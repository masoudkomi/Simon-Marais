"""Administrative record/hash preservation only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT=Path("/Users/uqmkamga/Documents/ChatGPT/Website")
BASE=Path("problems/2024-B4/reviews")
PRE="P2-indecomposable-review-2"
OUT=BASE/(PRE+"-manifest-v1.json")
assert not (ROOT/OUT).exists(), "Refuse to overwrite frozen report."
NOW=datetime.now(timezone.utc).isoformat()
def rec(path):
    path=str(path); data=(ROOT/path).read_bytes()
    return {"path":path,"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}
def check(expected):
    actual=rec(expected["path"])
    assert actual=={key:expected[key] for key in ("path","bytes","sha256")}, (expected,actual)
    return actual
def put(path,obj):
    (ROOT/path).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n")

old_manifest_record={
"path":"problems/2017-B4/notes/global-value-return-r2-manifest-v1.json",
"bytes":3351,"sha256":"05b38b4c3af797def7910863d731b72e6d747b1fd945a4167a6e994270d892e6"}
check(old_manifest_record)
old_manifest=json.loads((ROOT/old_manifest_record["path"]).read_text())
old_validation_record=next(x for x in old_manifest["artifacts"] if x["path"].endswith("-input-validation-v1.json"))
check(old_validation_record)
old_validation=json.loads((ROOT/old_validation_record["path"]).read_text())
items=old_validation["earlier_unique_records_preserved"]+old_manifest["artifacts"]+[old_manifest_record]
unique={}
for item in items:
    item={key:item[key] for key in ("path","bytes","sha256")}
    assert item["path"] not in unique or unique[item["path"]]==item
    unique[item["path"]]=item
old_preserved=[check(item) for item in unique.values()]
assert len(old_preserved)==301

target={
"path":"problems/2024-B4/notes/coordinator-P2-indecomposable-return-v1.md",
"bytes":8550,"sha256":"44a91d25943bb3d25f3c4a9c7fc2c2b7f498692889bf82b7dabbdb610b57c957"}
check(target)
author_manifest_path="problems/2024-B4/notes/coordinator-P2-indecomposable-manifest-v1.json"
author_manifest_record=rec(author_manifest_path)
author_manifest=json.loads((ROOT/author_manifest_path).read_text())
assert author_manifest["whole_obligations"]==8 and len(author_manifest["records"])==3
author_records=[check(x) for x in author_manifest["records"]]
assert author_records[0]==target
context=[rec(x) for x in [
"AGENTS.md","problems/2024-B4/statement.md",".cache/official/2024-paper_b.pdf",
"problems/2024-B4/reviews/P2-critical-jet-review-2-manifest-v1.json"]]
initial_path=BASE/(PRE+"-initial-v1.md")
ledger_path=BASE/(PRE+"-issues-v1.md")
ledger=(ROOT/ledger_path).read_text()
for i in range(1,19):
    assert "| DIR2-%02d |"%i in ledger
initial=(ROOT/initial_path).read_text()
for marker in ("## 1.","## 2.","## 3.","## 4.","## 5.","## 6.","## 7.","## 8."):
    assert marker in initial

validation_path=BASE/(PRE+"-input-validation-v1.json")
validation={
"validated_at_utc":NOW,"administrative_integrity_only":True,
"exact_three_author_records_plus_manifest":author_records+[author_manifest_record],
"protocol_official_and_own_old_context":context,
"primary_source":{
"url":"https://nyjm.albany.edu/j/2015/21-45p.pdf",
"read":"Abstract/introduction, complete Section2 printed990-991 and characteristic-zero Section3 boundary",
"role":"Related critical-outer-fiber method only; no theorem imported as DI premise",
"binary_hash":None,
"screenshot_limit":"One requested page returned cache-miss; usable read is primary web text, no visual claim"},
"all8_author_obligations_covered_by18_inference_rows":True,
"new_DI_peer_findings_read_before_freeze":False,
"mathematical_program_CAS_scan_sample_or_author_rerun":False,
"earlier_unique_records_preserved":sorted(old_preserved,key=lambda x:x["path"]),
"earlier_unique_record_count":len(old_preserved)}
put(validation_path,validation)
artifacts=[rec(BASE/(PRE+suffix)) for suffix in [
"-initial-v1.md","-issues-v1.md","-source-checks-v1.md","-freeze-v1.py","-input-validation-v1.json"]]
manifest={
"frozen_at_utc":NOW,
"status":"complete initially blind whole R2; all8 DI obligations pass in composition scope; coordinator reconciliation pending",
"reviewer":"/root/review_2017_coarsening_r1","new_DI_constructor":False,
"old_CP_authorship_and_related_KC_NV_CJ_audits_disclosed":True,
"new_independent_reaudit_of_own_older_CP_claim":False,
"requested_settings":{"model":"gpt-6.1-sol","reasoning":"max"},
"verified_effective_settings":None,
"target":target,"target_manifest":author_manifest_record,
"whole_author_obligations_audited":8,"independent_inference_rows":18,
"open_substantive_issues":0,"required_author_repairs":0,
"arbitrary_characteristic_local_fiber_and_exact_q_order_reconstructed":True,
"composite_degree_and_transcendental_coefficient_extension_scope_checked":True,
"multiplicative_irreducibility_full_factorization_annual_or_novelty_claim":False,
"new_DI_peer_findings_read_before_initial_freeze":False,
"mathematical_program_CAS_scan_sample_certificate_or_author_rerun":False,
"earlier_frozen_and_context_records_verified_unchanged":len(old_preserved),
"last_direct_weekly_telemetry":{"total_used_percent":44,"window_minutes":10080,
"reset_unix":1792745187,"total_ceiling_percent":90,"integration_reserve":True},
"administrative_command":"/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2024-B4/reviews/P2-indecomposable-review-2-freeze-v1.py",
"artifacts":artifacts}
put(OUT,manifest)
print(json.dumps({"manifest":rec(OUT),"report":artifacts[0],
"artifacts":len(artifacts),"obligations":8,"inference_rows":18,
"earlier_records_preserved":len(old_preserved),"status":manifest["status"]},indent=2))

