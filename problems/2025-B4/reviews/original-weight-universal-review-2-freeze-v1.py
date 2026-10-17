"""Administrative UW review freeze. No mathematical program or author rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
ROOT=Path("/Users/uqmkamga/Documents/ChatGPT/Website")
BASE=Path("problems/2025-B4/reviews")
PRE="original-weight-universal-review-2"
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
def walk(value):
    if isinstance(value,dict):
        if {"path","bytes","sha256"}<=value.keys():
            yield {k:value[k] for k in ("path","bytes","sha256")}
        for child in value.values():
            yield from walk(child)
    elif isinstance(value,list):
        for child in value:
            yield from walk(child)

previous_manifest_record={
"path":"problems/2024-B4/reviews/P2-indecomposable-review-2-manifest-v1.json",
"bytes":2940,"sha256":"eb5de1a997dbd5393dcc086d859eeaa056ef1575705885890b337672e9dc5a05"}
check(previous_manifest_record)
previous_manifest=json.loads((ROOT/previous_manifest_record["path"]).read_text())
previous_validation_record=next(x for x in previous_manifest["artifacts"] if x["path"].endswith("-input-validation-v1.json"))
check(previous_validation_record)
previous_validation=json.loads((ROOT/previous_validation_record["path"]).read_text())
earlier=previous_validation["earlier_unique_records_preserved"]+previous_manifest["artifacts"]+[previous_manifest_record]
unique={}
for row in earlier:
    row={k:row[k] for k in ("path","bytes","sha256")}
    assert row["path"] not in unique or unique[row["path"]]==row
    unique[row["path"]]=row
preserved=[check(row) for row in unique.values()]
assert len(preserved)==307

author_manifest_record={
"path":"problems/2025-B4/notes/original-weight-universal-return-r1-manifest-v1.json",
"bytes":4060,"sha256":"96ea49d93cec3b08514c1d5d67704f72163332bdbe7feb354c86b821ee90c1a7"}
check(author_manifest_record)
author_manifest=json.loads((ROOT/author_manifest_record["path"]).read_text())
assert len(author_manifest["artifacts"])==8 and author_manifest["author_obligations"]==40
author_artifacts=[check(row) for row in author_manifest["artifacts"]]
target={
"path":"problems/2025-B4/notes/original-weight-universal-return-r1-candidate-v1.md",
"bytes":19429,"sha256":"89fb03923c61b7785dbcd2b4ff6e6b6f08e17b7fc1653be6ea72f004831040ed"}
assert author_artifacts[0]==check(target)
sources_path="problems/2025-B4/notes/original-weight-universal-return-r1-sources-v1.json"
author_sources=json.loads((ROOT/sources_path).read_text())
input_path="problems/2025-B4/notes/original-weight-universal-return-r1-input-validation-v1.json"
author_validation=json.loads((ROOT/input_path).read_text())
declared=[]
for document in (author_manifest,author_sources,author_validation):
    for row in walk(document):
        declared.append(check(row))
declared_unique={}
for row in declared:
    assert row["path"] not in declared_unique or declared_unique[row["path"]]==row
    declared_unique[row["path"]]=row

accepted=author_sources["complete_accepted_mathematical_bodies_reread"]
raw=author_sources["original_frozen_candidates_preserved_as_exact_suffixes"]
assert len(accepted)==len(raw)==3
for accepted_row,raw_row in zip(accepted,raw):
    check(accepted_row); check(raw_row)
    assert (ROOT/accepted_row["path"]).read_bytes().endswith((ROOT/raw_row["path"]).read_bytes())

ledger=(ROOT/BASE/(PRE+"-issues-v1.md")).read_text()
for i in range(1,41):
    assert "| UWR2-%02d |"%i in ledger
report=(ROOT/BASE/(PRE+"-initial-v1.md")).read_text()
for i in range(1,11):
    assert "## %d."%i in report

validation_path=BASE/(PRE+"-input-validation-v1.json")
validation={
"validated_at_utc":NOW,"administrative_integrity_only":True,
"exact_author_manifest":author_manifest_record,
"all_eight_author_artifacts":author_artifacts,
"author_declared_record_occurrences_checked":len(declared),
"author_declared_unique_paths_checked":len(declared_unique),
"author_declared_records_checked":sorted(declared_unique.values(),key=lambda x:x["path"]),
"all_three_accepted_bodies_exact_frozen_suffixes":True,
"all40_author_obligations_mapped_by40_new_ledger_rows":True,
"older_FS_authorship_not_new_independent_self_reaudit":True,
"original_primary_actual_read_scope":"Section2.3 definitions/full Lemma3 and COMPLETE Section4.3 printed19-24 through its ending, author-text version2.0 2007-09-17",
"later_cached_primary_actual_read_scope":"COMPLETE PDF pp5-18, definitions/Voronoi2.6/selection2.7, application and FULL Appendices5.1/5.1.1/5.2",
"new_UW_peer_findings_or_later_RK_candidate_read_before_freeze":False,
"mathematical_program_scan_CAS_sample_certificate_or_author_rerun":False,
"earlier_unique_records_preserved":sorted(preserved,key=lambda x:x["path"]),
"earlier_unique_record_count":len(preserved)}
put(validation_path,validation)
artifacts=[rec(BASE/(PRE+suffix)) for suffix in [
"-initial-v1.md","-issues-v1.md","-source-checks-v1.md","-freeze-v1.py","-input-validation-v1.json"]]
manifest={
"frozen_at_utc":NOW,
"status":"complete initially blind whole UW R2; all40 obligations pass in exact algebraic selection scope; coordinator reconciliation pending",
"reviewer":"/root/review_2017_coarsening_r1",
"new_UW_constructor_or_strategy_contributor":False,
"old_FS_authorship_and_MS_OW_audits_disclosed":True,
"new_independent_reaudit_of_own_old_FS_claim":False,
"requested_settings":{"model":"gpt-6.1-sol","reasoning":"max"},
"verified_effective_settings":None,
"target":target,"target_manifest":author_manifest_record,
"whole_author_obligations_audited":40,"independent_inference_rows":40,
"open_substantive_issues":0,"required_author_repairs":0,
"moment_constants_fibers_abstract_lemma_both_branches_and_Fourier_reconstructed":True,
"thresholds_repeated_fibers_zero_moments_and_actual_integer_positivity_checked":True,
"reciprocal_cross_set_or_higher_series_rank_or_Diophantine_exclusion_claim":False,
"new_UW_peer_findings_or_later_RK_candidate_read_before_initial_freeze":False,
"mathematical_program_scan_CAS_sample_certificate_or_author_rerun":False,
"author_record_occurrences_verified":len(declared),
"author_unique_record_paths_verified":len(declared_unique),
"earlier_frozen_and_context_records_verified_unchanged":len(preserved),
"last_direct_weekly_telemetry":{"at_utc":"2026-10-17 14:31:32 UTC",
"total_used_percent":45,"window_minutes":10080,"reset_unix":1792745187,
"total_ceiling_percent":90,"integration_reserve":True},
"administrative_command":"/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2025-B4/reviews/original-weight-universal-review-2-freeze-v1.py",
"artifacts":artifacts}
put(OUT,manifest)
print(json.dumps({"manifest":rec(OUT),"report":artifacts[0],
"artifacts":len(artifacts),"obligations":40,
"author_record_occurrences_verified":len(declared),
"author_unique_record_paths_verified":len(declared_unique),
"earlier_records_preserved":len(preserved),"status":manifest["status"]},indent=2))

