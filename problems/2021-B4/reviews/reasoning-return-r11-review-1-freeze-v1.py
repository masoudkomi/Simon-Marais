"""Administrative-only R11 reviewer freeze; no mathematical computation.

Invocation: python3 problems/2021-B4/reviews/reasoning-return-r11-review-1-freeze-v1.py
Only writes this unused review prefix's validation and manifest, once.
Old constructor/parent programs are not run; historical rows are not expanded.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PRE = "problems/2021-B4/reviews/reasoning-return-r11-review-1-"


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(record):
    actual = fingerprint(record["path"])
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
assert fingerprint(baseline_path)["sha256"] == "b9d820af31966d278edfafa123c2f48972266f673e410707f43217c5f35ce0f7"
base = json.loads((ROOT / baseline_path).read_text())
records = [verify(record) for key in ("current_constructor_packet", "necessary_declared_input_occurrences", "prior_own_packet") for record in base[key]]
assert summary(records) == base["necessary_current_summary"]
assert len(records) == 56 and summary(records)["unique_paths"] == 54
candidate = base["current_constructor_packet"][1:]
target_path = "problems/2021-B4/notes/reasoning-return-r11-candidate-v1.md"
freeze_path = "problems/2021-B4/notes/reasoning-return-r11-freeze-v1.json"
assert fingerprint(target_path)["sha256"] == "3cdc672bb6974f6b274432eb4c8a202147ecefb676855ab9a1852352e33353b0"
assert fingerprint(freeze_path)["sha256"] == "c0b3a0650274e899fb97f84ec042e1edb9d5e6db0f603c7f22ee5bd691e12ca4"
ledger = (ROOT / (PRE + "ledger-v1.md")).read_text()
ids = re.findall(r"^\|(\d{2})\|", ledger, re.MULTILINE)
assert ids == [f"{i:02d}" for i in range(1, 57)]
issue = (ROOT / (PRE + "issues-v1.md")).read_text()
assert re.findall(r"^\|(R11R1-N\d+)\|", issue, re.MULTILINE) == ["R11R1-N1", "R11R1-N2", "R11R1-N3"]
sources = json.loads((ROOT / (PRE + "sources-v1.json")).read_text())
assert len(sources["public_primary_sources"]) == 7
assert sources["new_R11_peer_material_read"] is False
payload_suffixes = ["baseline-v1.json", "initial.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md", "sources-v1.json", "freeze-v1.py"]
payload = [fingerprint(PRE + suffix) for suffix in payload_suffixes]
assert all(record["bytes"] > 1000 for record in payload)
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
telemetry = {"at_utc": "2026-10-18 00:04:00 UTC", "method": "mcp__codex_app__get_usage_limits({}); rateLimitsByLimitId.codex.primary; legacy agrees", "account_label": "029a8928…1334ac3a", "used_percent_total": 1, "window_minutes": 10080, "reset_unix": 1792874445, "ordinary_usage_allowed": True, "new_window_explicitly_user_authorized_via_coordinator": True, "total_ceiling_percent": 90, "integration_reserve": True, "automatic_further_reset_spending": False}
validation = {"checked_at_utc": now, "administrative_only_no_mathematical_evidence": True, "baseline": fingerprint(baseline_path), "necessary_current_summary": summary(records), "all11_constructor_files_unchanged": True, "all36_selected_input_occurrences_unchanged": True, "all_nine_immediately_previous_own_files_unchanged": True, "constructor_history_bound_not_recopied": base["constructor_history_bound_not_recopied"], "prior_own_history": base["prior_own_history"], "all56_obligation_rows_present_once": True, "substantive_issues": 0, "required_repairs": 0, "retained_scope_notes": 3, "new_R11_peer_material_unread_through_entire_initial": True, "next2017R6_packet_unopened_through_entire_initial": True, "payload_records_before_validation": payload, "current_inputs_plus_payload_summary": summary(records + payload), "no_mathematical_code_scan_CAS_certificate_replay_or_author_rerun": True, "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True, "authoritative_weekly_telemetry": telemetry}
write_new("input-validation-v1.json", validation)
artifacts = payload + [fingerprint(PRE + "input-validation-v1.json")]
manifest = {"frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(), "status": "COMPLETE fresh initially blind NONCONSTRUCTOR WHOLE R1; no substantive defect found; not coordinator acceptance", "reviewer": "/root/review_2022_complexity_r2", "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"}, "independently_verified_effective_settings": None, "exact_target": fingerprint(target_path), "exact_constructor_freeze": fingerprint(freeze_path), "all56_obligations_and_whole_R11A_B_C_reconstructed": True, "substantive_issues": 0, "required_repairs": 0, "retained_scope_notes": 3, "new_R11_peer_findings_files_and_metadata_unread_through_entire_initial": True, "reviewer_did_not_construct_new_R11": True, "old_roles_disclosed_no_self_recertification": True, "another_OTHER_whole_initial_and_coordinator_reconciliation_required": True, "no_full_degree20_annual_classification_or_novelty_claim": True, "necessary_current_summary": summary(records), "constructor_history_bound_not_recopied": base["constructor_history_bound_not_recopied"], "compact_own_parent_manifest": base["prior_own_history"]["manifest"], "compact_own_parent_validation": base["prior_own_history"]["validation"], "older_own_paths_bound_transitively": 439, "new_own_files_including_manifest": 9, "older_plus_new_own_paths_bound_transitively": 448, "no_mathcode_scan_CAS_native_mathematical_child_or_author_rerun": True, "no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True, "next2017R6_packet_unopened_before_current_entire_freeze": True, "authoritative_weekly_telemetry": telemetry, "artifacts": artifacts}
write_new("manifest-v1.json", manifest)
for suffix in ["initial.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md", "input-validation-v1.json", "manifest-v1.json"]:
    print(json.dumps(fingerprint(PRE + suffix)))
