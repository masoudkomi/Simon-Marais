"""Metadata-only immutable checkpoint; no math program, scan or validation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = "problems/2022-B4/notes/reasoning-complexity-return-r9-"


def rec(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def readj(path):
    return json.loads((ROOT / path).read_text())


def occurrences(obj):
    rows = []
    if isinstance(obj, dict):
        if all(k in obj for k in ("path", "bytes", "sha256")):
            rows.append({k: obj[k] for k in ("path", "bytes", "sha256")})
        for value in obj.values():
            rows.extend(occurrences(value))
    elif isinstance(obj, list):
        for value in obj:
            rows.extend(occurrences(value))
    return rows


def write_new(path, obj):
    with (ROOT / path).open("x") as stream:
        stream.write(json.dumps(obj, indent=2) + "\n")


validationp = BASE + "input-validation-v3.json"
manifestp = BASE + "freeze-v3.json"
assert not (ROOT / validationp).exists()
assert not (ROOT / manifestp).exists()
baseline = readj(BASE + "baseline-v3.json")
rows = occurrences(baseline)
assert len(rows) == 16
unique = {}
for row in rows:
    assert rec(row["path"]) == row, row["path"]
    if row["path"] in unique:
        assert unique[row["path"]] == row
    unique[row["path"]] = row
assert len(unique) == 14
assert baseline["older_own_paths_bound_transitively"] == 543
canonical = [unique[p] for p in sorted(unique)]
summary_sha = hashlib.sha256(json.dumps(
    canonical, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

oldmain = (ROOT / (BASE + "candidate-v2.md")).read_bytes()
newmain = (ROOT / (BASE + "candidate-v3.md")).read_bytes()
oldob = (ROOT / (BASE + "obligations-v2.md")).read_bytes()
newob = (ROOT / (BASE + "obligations-v3.md")).read_bytes()
assert len(oldmain) == 31982
assert hashlib.sha256(oldmain).hexdigest() == (
    "4d3d81540f7f928e4aff9f865e9384cab2c45ca2a7d4e28d971c1531c943c578")
assert newmain.endswith(oldmain)
assert newob.endswith(oldob)
text = newob.decode()
assert re.findall(r"^\| (QW3\d\d) \|", text, re.M) == [
    f"QW3{i:02d}" for i in range(1, 21)]
assert re.findall(r"^\| (QV2\d\d) \|", text, re.M) == [
    f"QV2{i:02d}" for i in range(1, 33)]
assert re.findall(r"^\| (QO\d\d) \|", text, re.M) == [
    f"QO{i:02d}" for i in range(1, 49)]

payloads = ["baseline-v3.json", "candidate-v3.md", "obligations-v3.md",
            "failed-routes-v3.md", "source-audit-v3.md", "sources-v3.json",
            "worklog-v3.md", "freeze-v3.py"]
for suffix in payloads:
    assert (ROOT / (BASE + suffix)).is_file()
    if suffix.endswith(".json"):
        readj(BASE + suffix)

validation = {
    "checked_utc": datetime.now(timezone.utc).isoformat(),
    "operation": "ONLY SHA/bytes/JSON/literal suffix/obligation labels",
    "mathematical_validation_enumeration_or_table_rerun": False,
    "current_fingerprint_occurrences": len(rows),
    "unique_paths_verified": len(unique),
    "canonical_deduplicated_summary_sha256": summary_sha,
    "literal_v2_whole_main_and80_obligation_suffixes_unchanged": True,
    "all100_labels_present_not_proof_validation": True,
    "compact_parent": baseline["compact_own_parent"],
    "no_NEW_A_C_R9_findings_or_metadata_read_or_hashed": True,
    "no_recursive_old_historical_rehash_or_inventory_copy": True,
    "deduplicated_current_records": canonical,
    "errors": []
}
write_new(validationp, validation)
artifacts = [rec(BASE + suffix) for suffix in payloads] + [rec(validationp)]
manifest = {
    "frozen_utc": datetime.now(timezone.utc).isoformat(),
    "status": "candidate proof - unverified; COMPLETE whole Q1--Q8 v3 extension",
    "constructor": "/root/review_2022_complexity_r2",
    "exact_whole_main": rec(BASE + "candidate-v3.md"),
    "new_claims": [
        "Q7 available-parent rank descent over full I and exact ordinary orphan iff",
        "Q8 exact universal equivalence with born/orphan singleton-next-output seeds"
    ],
    "complete_old_Q1_Q6_body_and80_obligations_as_literal_appendices": True,
    "old_self_authored_results_NOT_silently_accepted": True,
    "all_Q1_Q8_and_all100_obligations": True,
    "old80_plus_new20_obligations": True,
    "entire_proofs_failures_source_limits_worklog_preserved": True,
    "actual_both_double_parent_exceptions_deleted_and_explained": True,
    "both_born_and_orphan_unbounded_legal_remaining_families_preserved": True,
    "strict_unbounded_Sdagger_subset_Sstar_family_proved_by_hand": True,
    "no_future_hitting_survivor_finite_decision_annual_or_novelty_claim": True,
    "TWO_OTHER_initially_blind_WHOLE_Q1_Q8_audits_required": True,
    "root_supplied_no_new_Q1_Q8_inference": True,
    "no_NEW_A_C_R9_peer_findings_reports_source_or_metadata_read_or_hashed": True,
    "old_roles_disclosed_no_self_certification": True,
    "no_math_code_CAS_scan_table_program_author_rerun_or_certificate": True,
    "metadata_only_not_mathematical_validation": True,
    "no_old_shared_Git_cache_edit_spawn_contact_charge_paidAPI_or_bypass": True,
    "preliminary_a_proof_reproduced_or_investigated": False,
    "no_new_primary_theorem_or_fresh_whole_external_proof_claim": True,
    "compact_own_parent": baseline["compact_own_parent"],
    "older_own_paths_bound_transitively": 543,
    "new_own_files_including_manifest": 10,
    "older_plus_new_own_paths_bound_transitively": 553,
    "fingerprint_occurrences_verified": len(rows),
    "unique_paths_verified": len(unique),
    "canonical_deduplicated_summary_sha256": summary_sha,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "independently_verified_effective_settings": None,
    "authoritative_weekly_telemetry": {
        "at_utc": "2026-10-18 02:07:06 UTC",
        "method": "mcp__codex_app__get_usage_limits({}); codex.primary and legacy agree",
        "account_label": "029a8928...1334ac3a",
        "used_percent_TOTAL": 9, "window_minutes": 10080,
        "reset_unix": 1792874445, "ordinary_usage_allowed": True,
        "current_window_explicitly_user_authorized": True,
        "ceiling_TOTAL_percent": 90, "integration_reserve": True,
        "automatic_further_reset_spending": False
    },
    "artifacts": artifacts
}
write_new(manifestp, manifest)
for row in artifacts + rows:
    assert rec(row["path"]) == row
assert readj(manifestp) == manifest
assert readj(validationp) == validation
print(json.dumps({
    "complete_unverified_checkpoint": True, "mathematical_validation": False,
    "main": rec(BASE + "candidate-v3.md"), "manifest": rec(manifestp),
    "all100_obligation_labels": True, "old_occurrences_verified": len(rows),
    "old_unique_paths_verified": len(unique), "new_own_files_including_manifest": 10,
    "total_own_paths_bound_transitively": 553, "postfreeze_metadata_errors": 0
}, indent=2))
