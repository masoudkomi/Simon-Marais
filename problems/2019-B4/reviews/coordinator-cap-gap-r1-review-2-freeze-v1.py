#!/usr/bin/env python3
"""Create-new compact integrity freeze. No mathematical child is rerun.

Only JSON/bytes/hashes/obligation labels/lifecycle records are checked.
The one independent fixed-integer sign is already saved separately.
No histories, caps, transfer matrices, old programs or CAS are evaluated.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/coordinator-cap-gap-r1-review-2-"
BASELINE = {"path": PREFIX+"baseline-v1.json", "bytes":5231,
    "sha256":"d6f47e0830b50c81e12923f2d6149fee8ee8194fbe46b2a713d41c014e7a612d"}
STAMP = datetime.now(timezone.utc).isoformat()
TELEMETRY = {"at_utc":"2026-10-17 19:44:02 UTC", "total_used_percent":60,
    "window_minutes":10080, "reset_unix":1792745187,
    "ordinary_usage_allowed":True, "spend_control_reached":False,
    "rate_limit_reached_type":None, "total_ceiling_percent":90,
    "review_integration_reserve":True}
inventory = {}
occurrences = 0


def record(path):
    absolute = (ROOT/path).resolve()
    if not absolute.is_relative_to(ROOT):
        raise SystemExit("Outside workspace: "+path)
    path = str(absolute.relative_to(ROOT))
    if path.startswith("problems/2019-B4/reviews/coordinator-cap-gap-r1-review-") and not path.startswith(PREFIX):
        raise SystemExit("New cap-gap peer files forbidden: "+path)
    if path.startswith("problems/2021-B4/reviews/reasoning-return-r10-review-"):
        raise SystemExit("Queued R10 peer findings forbidden")
    data = absolute.read_bytes()
    return {"path":path, "bytes":len(data), "sha256":hashlib.sha256(data).hexdigest()}


def verify(expected):
    global occurrences
    actual = record(expected["path"])
    if actual["sha256"] != expected["sha256"]:
        raise SystemExit("Immutable SHA changed: "+actual["path"])
    if expected.get("bytes") is not None and actual["bytes"] != expected["bytes"]:
        raise SystemExit("Immutable length changed: "+actual["path"])
    if actual["path"] in inventory and inventory[actual["path"]] != actual:
        raise SystemExit("Conflicting immutable records")
    inventory[actual["path"]] = actual
    occurrences += 1
    return actual


def load(row):
    return json.loads((ROOT/verify(row)["path"]).read_text())


def summary(rows):
    ordered = sorted({r["path"]:{k:r[k] for k in ("path","bytes","sha256")}
                      for r in rows}.values(),key=lambda r:r["path"])
    data = json.dumps(ordered,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
    return {"unique_paths":len(ordered),
        "canonical_sorted_record_array_sha256":hashlib.sha256(data).hexdigest()}


def declared_rows(obj):
    if isinstance(obj,dict):
        if isinstance(obj.get("path"),str) and re.fullmatch("[0-9a-f]{64}",str(obj.get("sha256",""))):
            yield obj
        for value in obj.values():
            yield from declared_rows(value)
    elif isinstance(obj,list):
        for value in obj:
            yield from declared_rows(value)


def write_new(suffix,obj):
    path = PREFIX+suffix
    with (ROOT/path).open("x") as stream:
        json.dump(obj,stream,ensure_ascii=False,indent=2);stream.write("\n")
    return record(path)


for suffix in ("sources-v1.json","input-validation-v1.json",
               "freeze-output-v1.json","manifest-v1.json"):
    if (ROOT/(PREFIX+suffix)).exists():
        raise SystemExit("Refusing frozen output overwrite: "+suffix)
baseline = load(BASELINE)
assert baseline["assigned_prefix_unused_before_first_write"]
packet = [verify(r) for r in baseline["constructor_packet_records"]]
assert len(packet)==13
assert packet[0]["sha256"]=="0e8afb24ec9e58004ee9464de327b309d834058b277eae4a2608d0d7afde5f33"
assert packet[-1]["sha256"]=="9b3751764cb2ba0177f3b8ff9e5f90721acf134f3e92c42cf4be67e5179d3d49"
constructor = json.loads((ROOT/packet[-1]["path"]).read_text())
for row in constructor["artifacts"]:
    verify(row)
assert len(constructor["artifacts"])==12
constructor_validation = load(baseline["constructor_input_validation"])
inputs = [verify(r) for r in constructor_validation["records"]]
assert len(inputs)==21
assert summary(inputs)==baseline["constructor21_input_summary"]
for row in constructor_validation["compact_immutable_parents"]:
    verify(row)
core = [verify(r) for r in baseline["exact_secondpass_linked_operative_bodies"]]
for row in baseline["other_read_input_records"]:
    verify(row)

parent = load(baseline["compact_immutable_own_parent"])
parent_validation = load(baseline["compact_immutable_own_parent_validation"])
parent_rows = [verify(r) for r in parent["artifacts"]]
parent_rows.append(verify(baseline["compact_immutable_own_parent"]))
assert len(parent_rows)==9
assert summary(parent_rows)==baseline["own_parent9_direct_artifact_manifest_summary"]
oldbinding = parent_validation["compact_immutable_parent_binding"]
assert oldbinding["older_own_paths_bound_transitively"]==376
verify(oldbinding["immutable_parent_manifest"])
verify(oldbinding["immutable_parent_validation"])
assert baseline["older_own_paths_bound_transitively"]==385

authorities = []
for stem in ("secondpass","thirdpass","moment-tail","coordinator-separation-scale-r1"):
    path = "problems/2019-B4/reviews/"+stem+"-acceptance.json"
    row = next(r for r in inputs if r["path"]==path)
    doc = load(row)
    declared = [verify(r) for r in declared_rows(doc)]
    if stem=="secondpass":
        for r in core:
            key = r["path"].split("problems/2019-B4/")[1]
            assert doc["artifacts"][key]==r["sha256"]
    authorities.append({"immutable_acceptance":row,
        "necessary_declared_fingerprint_occurrences_reverified":len(declared),
        "necessary_declared_deduplicated_summary":summary(declared),
        "prior_full_inventory_occurrences_recorded_not_replayed":doc.get("record_occurrences_verified",doc.get("verified_record_occurrences")),
        "prior_full_inventory_paths_recorded_not_replayed":doc.get("unique_paths_verified",doc.get("verified_unique_paths"))})

third = (ROOT/"problems/2019-B4/proofs/reviewed-thirdpass-v1.1.md").read_bytes()
third_original = (ROOT/"problems/2019-B4/notes/thirdpass-bounded-separation-v1.md").read_bytes()
math_marker = b"## 1. Inputs, scope and proposed conclusions"
assert third[third.index(math_marker):] == third_original[third_original.index(math_marker):]
sspath = next(r for r in inputs if r["path"]=="problems/2019-B4/notes/coordinator-separation-scale-r1-freeze-v1.json")
ss = load(sspath)
ssmain = verify(ss["artifacts"][0])
assert (ROOT/"problems/2019-B4/proofs/reviewed-separation-scale-v1.1.md").read_bytes().endswith((ROOT/ssmain["path"]).read_bytes())

ids = re.findall(r"^\|CGR2-(\d\d)\|",(ROOT/(PREFIX+"issues-v1.md")).read_text(),re.M)
assert ids==["%02d"%i for i in range(1,25)]
assert "Complete whole initial" in (ROOT/(PREFIX+"initial-v1.md")).read_text()
assert "Unresolved substantive issues0" in (ROOT/(PREFIX+"issues-v1.md")).read_text()

sign_suffixes = ("sign-v1.py","sign-run-v1.py","sign-output-v1.json",
                 "sign-stderr-v1.txt","sign-start-v1.json","sign-completion-v1.json")
sign_records = [record(PREFIX+s) for s in sign_suffixes]
start = json.loads((ROOT/(PREFIX+"sign-start-v1.json")).read_text())
end = json.loads((ROOT/(PREFIX+"sign-completion-v1.json")).read_text())
sign = json.loads((ROOT/(PREFIX+"sign-output-v1.json")).read_text())
assert start["pid"]==end["pid"]==37328
assert end["reaped"] and not end["timed_out"] and end["exit_code"]==0
assert end["external_timeout_seconds"]==10
assert (ROOT/(PREFIX+"sign-stderr-v1.txt")).read_bytes()==b""
assert sign["N_positive"] and sign["all_denominators_positive"]
assert sign["all_six_serialized_constructor_fractions_match"]
assert not sign["constructor_or_old_program_executed"]
prose = [record(PREFIX+s) for s in ("initial-v1.md","issues-v1.md","source-checks-v1.md")]

sources = write_new("sources-v1.json",{
    "recorded_at_utc":STAMP,
    "fresh_initially_blind_NONCONSTRUCTOR_WHOLE_R2":True,
    "official_url":"https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf",
    "official_read_scope":"PDFpage2 B4(b), distinct-string definition and root-rate target",
    "official_new_download_or_local_web_hash":None,
    "fresh_complete_accepted_bodies":[
        "secondpass register and three linked canonical-renewal/rigidity/staircase texts",
        "thirdpass accepted exposition, acceptance and cap-seven norm argument",
        "moment-tail accepted exposition and acceptance",
        "separation-scale accepted exposition and acceptance",
        "NR acceptance only",
        "thirdpass-literature scope record, not its entire original-paper bibliography"],
    "other_exact_read":"proof.md lines1--85 marked-fiber/root-rate bridge",
    "new_external_paper_theorem_imports":[],
    "old_cap_matrix_all11662_rows_newly_audited_or_replayed":False,
    "old_cap_exact_certificate_role":"accepted all-state positive v, Av<Uv; analytical norm consequence bounds rho7 itself",
    "constructor_all12_artifacts_and_freeze_read":True,
    "constructor_declared_input_record_summary":summary(inputs),
    "exact_secondpass_core_bodies":core,
    "immutable_accepted_authorities":authorities,
    "one_independent_new_fixed_sign_records":sign_records,
    "sign_child_lifecycle":end,
    "fixed_sign_scope":"one homogeneous-integer numerator; all six constructor serialized fractions compared after independent derivation",
    "author_or_old_program_execution":False,
    "mathematical_scan_history_cap_matrix_enumeration_CAS_or_source_download":False,
    "new_cap_gap_peer_files_or_findings_read":False,
    "root_constructor_excluded_from_independent_count":True,
    "reviewer_old_roles_disclosed_no_new_construction_contribution":True,
    "requested_settings":{"model":"gpt-6.1-sol","reasoning":"max","inherited":True},
    "independently_verified_effective_settings":None,
})

validation = write_new("input-validation-v1.json",{
    "checked_at_utc":STAMP,"administrative_only_not_mathematical_evidence":True,
    "baseline":BASELINE,
    "constructor_packet_records":packet,
    "all12_constructor_artifacts_plus_freeze_reverified":True,
    "constructor21_declared_input_records_reverified":True,
    "constructor_input_validation":baseline["constructor_input_validation"],
    "constructor21_input_deduplicated_summary":summary(inputs),
    "additional_secondpass_bodies":core,
    "accepted_authority_compact_summaries":authorities,
    "accepted_thirdpass_exact_mathematical_body_from_section1_verified":True,
    "thirdpass_preamble_status_and_review_sentences_are_accepted_editorial_replacements":True,
    "accepted_SS_exact_original_suffix_verified":True,
    "compact_immutable_parent_binding":{
        "immutable_parent_manifest":baseline["compact_immutable_own_parent"],
        "immutable_parent_validation":baseline["compact_immutable_own_parent_validation"],
        "direct9_old_artifact_manifest_summary":summary(parent_rows),
        "earlier376_paths_bound_by_exact_parent":True,
        "older_own_paths_bound_transitively":385,
        "all_historical_own_paths_rehashed_this_audit":False,
        "historical_inventory_not_copied":True,
        "reproduction":"Follow exact sector3 R1 manifest/validation to2025R8 and its earlier chain;376 earlier paths plus sector3 eight artifacts/manifest give385."},
    "necessary_current_fingerprint_occurrences_reverified":occurrences,
    "current_verified_records_deduplicated_summary":summary(list(inventory.values())),
    "new_prose_records":prose,
    "one_fixed_integer_sign_records":sign_records,
    "sign_external_timeout_PID_reap_checked":True,
    "sign_mathematics_not_rerun_by_freezer":True,
    "all24_author_obligation_rows_once":ids,
    "whole_claims":["CG1","CG2","CG3","CG4"],
    "substantive_issues_remaining":0,"required_repairs":0,
    "new_peer_cap_gap_files_or_findings_read":False,
    "no_old_shared_Git_cache_edit_scan_CAS_author_rerun_spawn_contact_charge_or_bypass":True,
    "sources_record":sources,"direct_weekly_telemetry":TELEMETRY,
})
output = write_new("freeze-output-v1.json",{
    "COMPLETE_initially_blind_NONCONSTRUCTOR_WHOLE_R2":True,
    "all24_author_obligations":True,"substantive_issue_or_required_repair":False,
    "constructor_main":packet[0],"constructor_freeze":packet[-1],
    "input_validation":validation,
    "one_fixed_sign_child_pid":37328,"sign_child_reaped":True,
    "old_author_program_or_math_scan":False,
    "necessary_fingerprint_occurrences":occurrences,"necessary_unique_paths":len(inventory),
    "older_own_paths_bound_transitively":385,"new_peer_findings_read":False,
})
suffixes = ("initial-v1.md","issues-v1.md","source-checks-v1.md","baseline-v1.json",
            *sign_suffixes,"freeze-v1.py","sources-v1.json",
            "input-validation-v1.json","freeze-output-v1.json")
artifacts = [record(PREFIX+s) for s in suffixes]
assert len(artifacts)==14 and artifacts[-1]==output and artifacts[-2]==validation
for row in inventory.values():
    if record(row["path"])!=row:
        raise SystemExit("Input changed during final freeze: "+row["path"])
manifest = write_new("manifest-v1.json",{
    "frozen_at_utc":STAMP,
    "status":"COMPLETE initially blind NONCONSTRUCTOR WHOLE R2 initial; no promotion",
    "reviewer":"/root/review_2022_complexity_r2",
    "new_candidate_constructed_or_contributed_by_reviewer":False,
    "root_constructor_excluded_from_independent_count":True,
    "older_independent_review_roles_disclosed_no_fresh_self_recertification":True,
    "requested_settings":{"model":"gpt-6.1-sol","reasoning":"max","inherited":True},
    "independently_verified_effective_settings":None,
    "constructor_main":packet[0],"constructor_freeze":packet[-1],
    "whole_claims":["CG1","CG2","CG3","CG4"],
    "all24_author_obligations_reconstructed":True,
    "substantive_issues_remaining":0,"required_repair":False,
    "initial_full_report_ledger_sources_before_peer_comparison":True,
    "new_peer_cap_gap_files_or_findings_read":False,
    "old_cap_exact_all_state_certificate_imported_not_rerun":True,
    "one_independent_fixed_integer_sign":True,
    "sign_child_pid":37328,"sign_external_timeout_seconds":10,
    "sign_exit_code":0,"sign_reaped":True,
    "all_six_serialized_constructor_fractions_match":True,
    "no_exact_lambda_actual_renewal_regime_annual_answer_or_novelty_claim":True,
    "compact_own_parent_manifest":baseline["compact_immutable_own_parent"],
    "compact_own_parent_validation":baseline["compact_immutable_own_parent_validation"],
    "older_own_paths_bound_transitively":385,
    "historical_inventory_not_copied_or_claimed_freshly_reread":True,
    "constructor21_declared_fingerprints_reverified":True,
    "necessary_current_fingerprint_occurrences":occurrences,
    "necessary_current_unique_paths":len(inventory),
    "no_math_scan_CAS_author_rerun_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass":True,
    "direct_weekly_telemetry":TELEMETRY,
    "command":"python3 "+PREFIX+"freeze-v1.py",
    "artifacts":artifacts,
})
print(json.dumps({"COMPLETE":True,"manifest":manifest,"report":artifacts[0],
    "ledger":artifacts[1],"sources":artifacts[2],"input_validation":validation,
    "artifacts":len(artifacts),"fingerprint_occurrences":occurrences,
    "unique_paths":len(inventory),"substantive_issues_remaining":0,
    "new_peer_findings_read":False}))
