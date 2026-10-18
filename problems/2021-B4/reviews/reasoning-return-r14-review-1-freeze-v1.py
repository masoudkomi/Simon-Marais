"""R14 WHOLE R1 metadata-only freeze. No mathematics or author rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2021-B4/reviews/reasoning-return-r14-review-1-"


def rec(path):
    assert not path.startswith("problems/2021-B4/reviews/reasoning-return-r14-review-2-")
    assert not path.startswith("problems/2022-B4/reviews/reasoning-complexity-return-r9-review-")
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def readj(path):
    return json.loads((ROOT / path).read_text())


def rows_in(obj):
    rows = []
    if isinstance(obj, dict):
        if all(k in obj for k in ("path", "bytes", "sha256")):
            rows.append({k: obj[k] for k in ("path", "bytes", "sha256")})
        for value in obj.values():
            rows.extend(rows_in(value))
    elif isinstance(obj, list):
        for value in obj:
            rows.extend(rows_in(value))
    return rows


def write_new(path, obj):
    with (ROOT / path).open("x") as stream:
        stream.write(json.dumps(obj, indent=2) + "\n")


validationp = P + "input-validation-v1.json"
manifestp = P + "manifest-v1.json"
assert not (ROOT / validationp).exists()
assert not (ROOT / manifestp).exists()
baseline = readj(P + "baseline-v1.json")
update = readj(P + "authority-update-v1.json")
rows = rows_in(baseline) + rows_in(update)
assert len(rows) == 31
unique = {}
for row in rows:
    assert rec(row["path"]) == row, row["path"]
    if row["path"] in unique:
        assert unique[row["path"]] == row
    unique[row["path"]] = row
assert len(unique) == 27
canonical = [unique[p] for p in sorted(unique)]
digest = hashlib.sha256(json.dumps(
    canonical, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

for version in (8, 12, 13):
    a = f"problems/2021-B4/proofs/reviewed-reasoning-return-r{version}-v1.1.md"
    b = f"problems/2021-B4/notes/reasoning-return-r{version}-candidate-v1.md"
    assert (ROOT / a).read_bytes().endswith((ROOT / b).read_bytes())
    authority = readj(f"problems/2021-B4/reviews/reasoning-return-r{version}-acceptance.json")
    assert authority["unresolved_substantive_issues"] == 0
    assert authority["repair_required"] is False
    assert rec(a) == authority["accepted_copy"]
    assert rec(b) == authority["candidate"]

ledger = (ROOT / (P + "ledger-v1.md")).read_text()
ids = re.findall(r"^\| (R14R1-\d\d) \|", ledger, re.M)
assert ids == [f"R14R1-{i:02d}" for i in range(1, 57)]
constructor_ids = re.findall(
    r"^\|(R14O\d\d)\|",
    (ROOT / "problems/2021-B4/notes/reasoning-return-r14-obligations-v1.md").read_text(),
    re.M)
assert constructor_ids == [f"R14O{i:02d}" for i in range(1, 57)]
notes = re.findall(
    r"\*\*R14R1-(N\d),",
    (ROOT / (P + "issues-v1.md")).read_text())
assert notes == [f"N{i}" for i in range(1, 7)]

payloads = ["baseline-v1.json", "authority-update-v1.json", "initial.md",
            "ledger-v1.md", "issues-v1.md", "source-checks-v1.md",
            "sources-v1.json", "worklog-v1.md", "freeze-v1.py"]
for suffix in payloads:
    assert (ROOT / (P + suffix)).is_file()
    if suffix.endswith(".json"):
        readj(P + suffix)

validation = {
    "checked_utc": datetime.now(timezone.utc).isoformat(),
    "operation": "ONLY file SHA/bytes/JSON/literal accepted suffixes/obligation labels",
    "mathematical_validation_or_finite_field_table_execution": False,
    "old_necessary_occurrences_verified": len(rows),
    "old_unique_paths_verified": len(unique),
    "canonical_deduplicated_summary_sha256": digest,
    "entire_R14_constructor_packet_hashes_verified": True,
    "accepted_R8_R12_R13_literal_suffixes_and_authority_verified": True,
    "R13_old_input_accepted_update_preserves_constructor_pending_wording": True,
    "review56_and_constructor56_label_bijection": True,
    "six_note_labels_present": True,
    "C_NEW_R14_findings_files_source_metadata_unread_unhashed": True,
    "irrelevant_A_old2022_review_ancestry_not_directly_opened_or_hashed": True,
    "no_historical_recursive_inventory_walk_or_copy": True,
    "deduplicated_current_records": canonical,
    "errors": []
}
write_new(validationp, validation)
artifacts = [rec(P + suffix) for suffix in payloads] + [rec(validationp)]
manifest = {
    "frozen_utc": datetime.now(timezone.utc).isoformat(),
    "status": "COMPLETE initially blind OTHER NONCONSTRUCTOR ENTIRE WHOLE R14 R1 initial",
    "reviewer": "/root/review_2022_complexity_r2",
    "exact_target": baseline["exact_target"],
    "constructor_freeze": baseline["constructor_freeze"],
    "entire_R14A_R14B_R14C_R14D_and_all56_obligations_reconstructed": True,
    "independent_hand_affine_zero_comparison_all_prefixes_cases_and10_products": True,
    "full_actual_valuation_domain_gcd_and_multiplicity_inferences_checked": True,
    "unresolved_substantive_issues": 0,
    "required_author_repairs": 0,
    "retained_nonblocking_scope_operational_notes": 6,
    "not_coordinator_promotion_or_external_validation": True,
    "R14D_conditional_implication_initially_checked_as_submitted": True,
    "R13_old_input_accepted_by_root_during_audit_exact_scope_now_available": True,
    "frozen_constructor_pending_language_unchanged": True,
    "no_full_m5_m3_m4_J15_degree20_annual_lift_height_or_novelty_claim": True,
    "C_NEW_R14_reports_findings_ledgers_source_metadata_unread_unhashed_through_ENTIRE_freeze": True,
    "A_sole_NEW_constructor_excluded": True,
    "B_supplied_no_NEW_R14_construction_or_repair": True,
    "old_B_review_roles_and_separate_R9_authorship_disclosed_no_recertification": True,
    "incidental_A_old2022_fingerprints_embedded_in_constructor_validation_seen_AFTER_B2022v3freeze": True,
    "actual_old2022_peer_review_open_or_direct_hash": False,
    "actual_primary_read_limits_and_truncation_repairs_recorded": True,
    "no_math_code_CAS_scan_author_rerun_old_certificate_or_native_child": True,
    "no_old_candidate_peer_shared_Git_cache_edit_spawn_contact_charge_or_bypass": True,
    "compact_own_parent": baseline["compact_own_parent"],
    "older_own_paths_bound_transitively": 553,
    "new_own_files_including_manifest": 11,
    "older_plus_new_own_paths_bound_transitively": 564,
    "fingerprint_occurrences_verified": len(rows),
    "unique_paths_verified": len(unique),
    "canonical_deduplicated_summary_sha256": digest,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "authoritative_weekly_telemetry": {
        "at_utc": "2026-10-18 06:16:40 UTC",
        "method": "mcp__codex_app__get_usage_limits({}); codex.primary and legacy agree",
        "account_label": "029a8928...1334ac3a", "used_percent_TOTAL": 10,
        "window_minutes": 10080, "reset_unix": 1792874445,
        "ordinary_usage_allowed": True, "current_window_explicitly_user_authorized": True,
        "ceiling_TOTAL_percent": 90, "integration_reserve": True,
        "automatic_further_reset_spending": False
    },
    "artifacts": artifacts
}
write_new(manifestp, manifest)
for row in rows + artifacts:
    assert rec(row["path"]) == row
assert readj(manifestp) == manifest
assert readj(validationp) == validation
print(json.dumps({
    "ENTIRE_blind_WHOLE_R14_R1_frozen": True,
    "initial": rec(P + "initial.md"), "manifest": rec(manifestp),
    "all56_obligations": True, "substantive_issues": 0, "repairs": 0,
    "retained_notes": 6, "R13_old_input_update_recorded": True,
    "metadata_occurrences": len(rows), "metadata_unique_paths": len(unique),
    "new_own_files": 11, "own_chain_total": 564,
    "postfreeze_metadata_errors": 0, "mathematical_validation": False
}, indent=2))
