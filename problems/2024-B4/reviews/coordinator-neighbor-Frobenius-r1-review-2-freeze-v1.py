"""Administrative-only NF whole R2 freeze; no mathematical computation.

Invocation: python3 problems/2024-B4/reviews/coordinator-neighbor-Frobenius-r1-review-2-freeze-v1.py
Only creates this prefix's NEW validation and manifest. Never runs an
author program, enumerates mathematics, or recursively copies history.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PRE = "problems/2024-B4/reviews/coordinator-neighbor-Frobenius-r1-review-2-"


def fp(path):
    raw = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def verify(record):
    actual = fp(record["path"])
    assert actual == record, (record, actual)
    return actual


def summary(records):
    unique = {}
    for record in records:
        if record["path"] in unique:
            assert unique[record["path"]] == record
        unique[record["path"]] = record
    rows = [unique[path] for path in sorted(unique)]
    digest = hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    return {"occurrences": len(records), "unique_paths": len(rows), "canonical_deduplicated_summary_sha256": digest}


def write_new(suffix, data):
    with (ROOT / (PRE + suffix)).open("x") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


assert not (ROOT / (PRE + "input-validation-v1.json")).exists()
assert not (ROOT / (PRE + "manifest-v1.json")).exists()
baseline_path = PRE + "baseline-v1.json"
assert fp(baseline_path)["sha256"] == "d8232f0d7ce21c6760d8ebce4afda6d5208fad6538f2ebc9f9ae9b66c2445a9e"
base = json.loads((ROOT / baseline_path).read_text())
records = [verify(record) for key in ("current_constructor_packet", "declared_current_context_records", "immediately_previous_own_packet") for record in base[key]]
assert summary(records) == base["necessary_current_summary"]
assert len(records) == 30
target = "problems/2024-B4/notes/coordinator-neighbor-Frobenius-r1-candidate-v1.md"
constructor_freeze = "problems/2024-B4/notes/coordinator-neighbor-Frobenius-r1-freeze-v1.json"
assert fp(target) == {"path": target, "bytes": 13799, "sha256": "775501d763a46b8411a6509c7da06d3a7fc3dacb3b27141881b80de2ea37f9d4"}
assert fp(constructor_freeze) == {"path": constructor_freeze, "bytes": 2492, "sha256": "f97a4dc9eb21dea3e4e4e94d42ba7f3bdf09ddf3555e2defcab19c4ec5812671"}
ledger = (ROOT / (PRE + "ledger-v1.md")).read_text()
assert re.findall(r"^\|(NF-\d{2})\|", ledger, re.MULTILINE) == [f"NF-{i:02d}" for i in range(1, 37)]
issues = (ROOT / (PRE + "issues-v1.md")).read_text()
assert re.findall(r"^\|(NFR2-N\d+)\|", issues, re.MULTILINE) == [f"NFR2-N{i}" for i in range(1, 5)]
sources = json.loads((ROOT / (PRE + "sources-v1.json")).read_text())
assert len(sources["public_source_records"]) == 5
assert sources["new_A_NF_peer_report_findings_ledger_source_or_metadata_opened"] is False
assert sources["queued_R9_packet_and_peer_files_opened"] is False
payload_suffixes = ["baseline-v1.json", "initial.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md", "sources-v1.json", "freeze-v1.py"]
payload = [fp(PRE + suffix) for suffix in payload_suffixes]
assert all(record["bytes"] > 1000 for record in payload)
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
telemetry = sources["authoritative_weekly_telemetry"]
validation = {"checked_at_utc": now, "administrative_only_no_mathematical_evidence": True, "baseline": fp(baseline_path), "necessary_current_summary": summary(records), "all_seven_constructor_files_unchanged": True, "all14_declared_current_context_records_unchanged": True, "all_nine_immediately_preceding_own_files_unchanged": True, "prior_own_history": base["prior_own_history"], "all36_obligation_rows_present_once": True, "substantive_issues": 0, "required_repairs": 0, "retained_scope_notes": 4, "whole_NF1_NF2_NF3_reconstructed": True, "new_A_NF_files_findings_source_ledger_or_metadata_unopened_through_entire_initial": True, "queued_R9_packet_and_peer_material_unopened_through_entire_initial": True, "payload_records_before_validation": payload, "current_inputs_plus_payload_summary": summary(records + payload), "no_mathcode_CAS_scan_certificate_replay_or_author_rerun": True, "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True, "authoritative_weekly_telemetry": telemetry}
write_new("input-validation-v1.json", validation)
artifacts = payload + [fp(PRE + "input-validation-v1.json")]
manifest = {"frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "status": "COMPLETE fresh initially blind NONCONSTRUCTOR WHOLE R2; no substantive defect found; not coordinator acceptance", "reviewer": "/root/review_2022_complexity_r2", "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"}, "independently_verified_effective_settings": None, "exact_target": fp(target), "exact_constructor_freeze": fp(constructor_freeze), "all36_obligations_and_whole_NF1_NF2_NF3_reconstructed": True, "substantive_issues": 0, "required_repairs": 0, "retained_scope_notes": 4, "root_sole_NEW_constructor_excluded": True, "reviewer_did_not_construct_NEW_NF_argument": True, "old_B_structural_sector3_GK_CP_three_bit_review_roles_disclosed": True, "accepted_context_not_self_recertified_or_silently_used_as_premise": True, "new_A_NF_files_findings_source_ledger_or_metadata_unopened_through_entire_initial": True, "another_OTHER_complete_initial_and_coordinator_reconciliation_required": True, "no_annual_all_four_bit_or_novelty_claim": True, "actual_source_read_scopes_and_bounded_Fulton_fetch_failures_recorded": True, "no_complete_original_book_or_unread_Jedlicka_2026_proof_claim": True, "necessary_current_summary": summary(records), "compact_own_parent_manifest": base["prior_own_history"]["manifest"], "compact_own_parent_validation": base["prior_own_history"]["validation"], "older_own_paths_bound_transitively": 457, "new_own_files_including_manifest": 9, "older_plus_new_own_paths_bound_transitively": 466, "no_historical_inventory_recopied_or_recursively_rehashed": True, "no_mathcode_scan_CAS_native_mathematical_child_or_author_rerun": True, "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True, "queued_R9_packet_and_peer_material_unopened_before_current_entire_freeze": True, "authoritative_weekly_telemetry": telemetry, "artifacts": artifacts}
write_new("manifest-v1.json", manifest)
for suffix in ["initial.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md", "sources-v1.json", "input-validation-v1.json", "manifest-v1.json"]:
    print(json.dumps(fp(PRE + suffix)))
