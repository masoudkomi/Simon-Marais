"""Administrative RK whole-review freeze; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
ROOT=Path("/Users/uqmkamga/Documents/ChatGPT/Website")
BASE=Path("problems/2025-B4/reviews")
PRE="reciprocal-kernel-review-2"
OUT=BASE/(PRE+"-manifest-v1.json")
assert not (ROOT/OUT).exists()
NOW=datetime.now(timezone.utc).isoformat()
def rec(path):
    path=str(path); data=(ROOT/path).read_bytes()
    return {"path":path,"bytes":len(data),"sha256":hashlib.sha256(data).hexdigest()}
def check(expected):
    actual=rec(expected["path"])
    assert actual=={k:expected[k] for k in ("path","bytes","sha256")}, (expected,actual)
    return actual
def put(path,obj):
    (ROOT/path).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+"\n")

previous_manifest_record={
"path":"problems/2025-B4/reviews/original-weight-universal-review-2-manifest-v1.json",
"bytes":3203,"sha256":"2a57f089737aab5364d3e0329ba07ddfb38dab246b4a92f0fee47afe3abf6bd8"}
check(previous_manifest_record)
previous_manifest=json.loads((ROOT/previous_manifest_record["path"]).read_text())
previous_validation_record=next(x for x in previous_manifest["artifacts"] if x["path"].endswith("-input-validation-v1.json"))
check(previous_validation_record)
previous_validation=json.loads((ROOT/previous_validation_record["path"]).read_text())
items=previous_validation["earlier_unique_records_preserved"]+previous_manifest["artifacts"]+[previous_manifest_record]
unique={}
for item in items:
    row={k:item[k] for k in ("path","bytes","sha256")}
    assert row["path"] not in unique or unique[row["path"]]==row
    unique[row["path"]]=row
preserved=[check(row) for row in unique.values()]
assert len(preserved)==313

target={
"path":"problems/2025-B4/notes/coordinator-reciprocal-kernel-return-v1.md",
"bytes":9541,"sha256":"4c752f3ca4699ea0c184dbb79d79f9f192182cc91aeac7fd8a459b7b8bea49b8"}
check(target)
author_manifest_path="problems/2025-B4/notes/coordinator-reciprocal-kernel-manifest-v1.json"
author_manifest_record=rec(author_manifest_path)
author_manifest=json.loads((ROOT/author_manifest_path).read_text())
assert len(author_manifest["records"])==4 and author_manifest["whole_obligations"]==8
author_records=[check(row) for row in author_manifest["records"]]
assert author_records[0]==target
uw_context={
"path":"problems/2025-B4/notes/original-weight-universal-return-r1-candidate-v1.md",
"bytes":19429,"sha256":"89fb03923c61b7785dbcd2b4ff6e6b6f08e17b7fc1653be6ea72f004831040ed"}
check(uw_context)
context=[rec(path) for path in [
"AGENTS.md","problems/2025-B4/statement.md",
".cache/official/2025-paper_b.pdf",".cache/official/2025-solutions.pdf"]]+[uw_context,previous_manifest_record]
image_records=[]
printed=[(274,275),(276,277),(278,279),(280,281)]
for index,pages in enumerate(printed,1):
    path=Path("/private/tmp/smmc-hasse-%d.png"%index)
    data=path.read_bytes()
    assert data[:8]==b"\x89PNG\r\n\x1a\n"
    image_records.append({
        "image_path":str(path),"bytes":len(data),
        "sha256":hashlib.sha256(data).hexdigest(),
        "printed_pages_in_spread":list(pages),
        "Hasse_pages_actually_read":[page for page in pages if 275<=page<=280],
        "existing_read_only_render_not_new_output":True})
ledger=(ROOT/BASE/(PRE+"-issues-v1.md")).read_text()
for i in range(1,23):
    assert "| RKR2-%02d |"%i in ledger
report=(ROOT/BASE/(PRE+"-initial-v1.md")).read_text()
for i in range(1,9):
    assert "## %d."%i in report

validation_path=BASE/(PRE+"-input-validation-v1.json")
validation={
"validated_at_utc":NOW,"administrative_integrity_only":True,
"exact_four_author_records_plus_manifest":author_records+[author_manifest_record],
"protocol_official_and_conditional_context":context,
"all8_author_obligations_covered_by22_inference_rows":True,
"Hasse_scanned_primary_visual_read":{
"article":"H. Hasse, On a question of S. Chowla, Acta Arith.18(1971),275-280",
"doi":"10.4064/aa-18-1-275-280",
"publisher_issue_url":"https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/18",
"all_six_Hasse_pages_read_at_original_detail":True,
"adjacent274_281_not_imported":True,
"read_only_render_images":image_records,
"OCR_or_empty_extraction_claimed_as_read":False,
"full_underlying_analytic_class_number_proof_reconstructed":False},
"Hamahata_primary_crosscheck":{
"url":"https://www.jstage.jst.go.jp/article/kyushujm/74/2/74_429/_pdf/-char/en",
"doi":"10.2206/kyushujm.74.429",
"read":"Introduction/Theorem1.1 and COMPLETE Section2.1 Theorem2.1/displayed proof",
"specialization":"r=1,k=1,q=p,K=Q,T=1..(p-1)/2",
"unseen_r1_reference_proof_or_stronger_theorem_imported":False,
"new_binary_hash":None},
"PDF_skill":{"skill_path":"/Users/uqmkamga/.codex/plugins/cache/openai-primary-runtime/pdf/26.1013.11914/skills/pdf/SKILL.md",
"operation":"read-only existing scanned images; no PDF creation/editing/authoring marker"},
"UW_initial_completely_frozen_before_RK_target_opened":True,
"new_RK_peer_findings_read_before_freeze":False,
"mathematical_program_CAS_scan_sample_certificate_or_author_rerun":False,
"earlier_unique_records_preserved":sorted(preserved,key=lambda x:x["path"]),
"earlier_unique_record_count":len(preserved)}
put(validation_path,validation)
artifacts=[rec(BASE/(PRE+suffix)) for suffix in [
"-initial-v1.md","-issues-v1.md","-source-checks-v1.md","-freeze-v1.py","-input-validation-v1.json"]]
manifest={
"frozen_at_utc":NOW,
"status":"complete initially blind whole RK R2; all8 obligations pass in exact rational-kernel/fixed-complement/conditional application scopes; coordinator reconciliation pending",
"reviewer":"/root/review_2017_coarsening_r1","new_RK_constructor":False,
"older_FS_authorship_and_MS_OW_UW_review_roles_disclosed":True,
"requested_settings":{"model":"gpt-6.1-sol","reasoning":"max"},
"verified_effective_settings":None,
"target":target,"target_manifest":author_manifest_record,
"whole_author_obligations_audited":8,"independent_inference_rows":22,
"open_substantive_issues":0,"required_author_repairs":0,
"whole_Hasse_six_pages_and_general_cotangent_scope_visually_read":True,
"rational_odd_even_kernel_both_directions_p3_and_p5plus_checked":True,
"all_c_d_fixed_complement_equality_and_Galois_prefactor_checked":True,
"UW_application_explicitly_conditional":True,
"higher_jet_or_Diophantine_or_novelty_or_whole_classical_reproof_claim":False,
"new_RK_peer_findings_read_before_initial_freeze":False,
"mathematical_program_CAS_scan_sample_certificate_or_author_rerun":False,
"earlier_frozen_and_context_records_verified_unchanged":len(preserved),
"last_direct_weekly_telemetry":{"at_utc":"2026-10-17 14:31:32 UTC",
"total_used_percent":45,"window_minutes":10080,"reset_unix":1792745187,
"total_ceiling_percent":90,"integration_reserve":True},
"administrative_command":"/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2025-B4/reviews/reciprocal-kernel-review-2-freeze-v1.py",
"artifacts":artifacts}
put(OUT,manifest)
print(json.dumps({"manifest":rec(OUT),"report":artifacts[0],
"artifacts":len(artifacts),"obligations":8,"inference_rows":22,
"earlier_records_preserved":len(preserved),"status":manifest["status"]},indent=2))

