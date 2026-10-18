"""Administrative-only immutable review freeze: SHA/JSON/labels/suffixes.

No orbit, formula evaluation, residue table, CAS, author program or
mathematical certificate is executed. Writes only new assigned R2-v3 files.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = "problems/2022-B4/reviews/reasoning-complexity-return-r9-review-2-v3-"
TARGET = "problems/2022-B4/notes/reasoning-complexity-return-r9-"


def rec(path):
    b = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def readj(path):
    return json.loads((ROOT / path).read_text())


def occurrences(obj):
    rows = []
    if isinstance(obj, dict):
        if {"path", "bytes", "sha256"} <= obj.keys():
            rows.append({k: obj[k] for k in ("path", "bytes", "sha256")})
        for value in obj.values():
            rows.extend(occurrences(value))
    elif isinstance(obj, list):
        for value in obj:
            rows.extend(occurrences(value))
    return rows


def newj(path, obj):
    with (ROOT / path).open("x") as stream:
        stream.write(json.dumps(obj, indent=2) + "\n")


for suffix in ("metadata-v1.json", "input-validation-v1.json", "manifest-v1.json"):
    assert not (ROOT / (BASE + suffix)).exists()
baseline = readj(BASE + "baseline-v1.json")
rows = occurrences(baseline)
unique = {}
for row in rows:
    assert rec(row["path"]) == row, row["path"]
    if row["path"] in unique:
        assert unique[row["path"]] == row
    unique[row["path"]] = row
    if row["path"].endswith(".json"):
        readj(row["path"])
assert len(rows) == 39
assert len(unique) == 36
assert baseline["historical_own_paths_bound"] == 571
assert readj(baseline["immutable_own_parent"]["path"])["own_paths_after_this_packet"] == 571
canonical = [unique[p] for p in sorted(unique)]
digest = hashlib.sha256(json.dumps(
    canonical, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

for newer, older in ((2, 1), (3, 2)):
    for kind in ("candidate", "obligations"):
        old = (ROOT / (TARGET + f"{kind}-v{older}.md")).read_bytes()
        new = (ROOT / (TARGET + f"{kind}-v{newer}.md")).read_bytes()
        assert new.endswith(old)
expected = ([f"QO{i:02d}" for i in range(1, 49)]
            + [f"QV2{i:02d}" for i in range(1, 33)]
            + [f"QW3{i:02d}" for i in range(1, 21)])
pattern = r"^\| (QO\d\d|QV2\d\d|QW3\d\d) \|"
author_ids = re.findall(pattern, (ROOT / (TARGET + "obligations-v3.md")).read_text(), re.M)
our_ids = re.findall(pattern, (ROOT / (BASE + "ledger-v1.md")).read_text(), re.M)
assert len(author_ids) == len(set(author_ids)) == 100
assert set(author_ids) == set(expected)
assert our_ids == expected

at = datetime.now(timezone.utc).isoformat()
validation = {
    "checked_utc": at,
    "operation": "administrative only: bytes/SHA/JSON/literal suffix/label checks",
    "mathematical_program_or_validation": False,
    "declared_fingerprint_occurrences_verified": len(rows),
    "deduplicated_paths_verified": len(unique),
    "canonical_deduplicated_summary_sha256": digest,
    "both_main_and_obligation_suffix_transitions_verified": True,
    "all100_author_and_reviewer_obligation_labels_once": True,
    "all_declared_target_artifacts_preserved": True,
    "immutable_own_parent": baseline["immutable_own_parent"],
    "no_NEW_A_v3_review_file_findings_source_code_or_metadata_read_or_hashed": True,
    "no_recursive_historical_inventory_copy_or_rehash": True,
    "errors": []
}
newj(BASE + "input-validation-v1.json", validation)
metadata = {
    "reviewer": "/root/review_2017_coarsening_r1",
    "review_scope": "ENTIRE Q1--Q8 v3, literal v2/v1 chain and all100 obligations",
    "whole_initial_completed_before_NEW_peer_material": True,
    "old_R4_R7_R8_constructor_and_v1_reviewer_roles_disclosed": True,
    "no_self_recertification_of_old_own_theorems": True,
    "substantive_defects_identified": 0,
    "requested_repairs": 0,
    "advisories": 0,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
    "verified_effective_setting_readback": None,
    "authoritative_weekly_telemetry": {
        "at_utc": "2026-10-18 06:27:10 UTC",
        "method": "mcp__codex_app__get_usage_limits; codex.primary and legacy agree",
        "used_percent_TOTAL": 11,
        "window_minutes": 10080,
        "reset_unix": 1792874445,
        "ordinary_usage_allowed": True,
        "human_authorized_current_window_through_TOTAL_percent": 90,
        "integration_reserve": True,
        "automatic_further_reset_spending": False
    },
    "no_mathematical_code_scan_CAS_certificate_or_author_rerun": True,
    "all20_interval_rows_reconstructed_by_hand": True,
    "no_Git_shared_old_cache_edit_spawn_charge_contact_or_bypass": True,
    "preliminary_proof_reproduced_or_investigated": False,
    "external_proof_import": "only attributed eventual-strip statement; no generic dynamics theorem",
    "target_manifests": baseline["target_manifests"],
    "compact_immutable_own_parent": baseline["immutable_own_parent"],
    "historical_own_paths_bound": 571,
    "new_packet_paths_including_manifest": 10,
    "own_paths_after_this_packet": 581,
    "deduplicated_inputs_summary_sha256": digest,
    "no_coordinator_promotion_survivor_termination_or_annual_claim": True
}
newj(BASE + "metadata-v1.json", metadata)
suffixes = ["initial-v1.md", "ledger-v1.md", "issues-v1.md",
            "source-checks-v1.md", "worklog-v1.md", "freeze-v1.py",
            "baseline-v1.json", "metadata-v1.json", "input-validation-v1.json"]
artifacts = [rec(BASE + suffix) for suffix in suffixes]
manifest = {
    "frozen_utc": datetime.now(timezone.utc).isoformat(),
    "status": "ENTIRE initially blind OTHER WHOLE Q1--Q8 v3 R2 frozen before NEW peer material",
    "target": rec(TARGET + "candidate-v3.md"),
    "target_freeze": rec(TARGET + "freeze-v3.json"),
    "whole_author_obligations": 100,
    "literal_v2_v1_chain_reconstructed": True,
    "substantive_issues": 0, "requested_repairs": 0, "advisories": 0,
    "no_NEW_peer_v3_file_or_hash_accessed": True,
    "findings_withheld_until_other_ENTIRE_initial_confirmation": True,
    "old_roles_disclosed_no_self_recertification": True,
    "immutable_own_parent": baseline["immutable_own_parent"],
    "historical_own_paths_bound": 571,
    "this_packet_paths_including_manifest": 10,
    "own_paths_after_this_packet": 581,
    "declared_occurrences_verified": len(rows),
    "deduplicated_paths_verified": len(unique),
    "no_mathematical_program_CAS_scan_or_author_rerun": True,
    "no_coordinator_promotion_or_annual_claim": True,
    "artifacts": artifacts
}
newj(BASE + "manifest-v1.json", manifest)
for row in rows + artifacts:
    assert rec(row["path"]) == row
assert readj(BASE + "metadata-v1.json") == metadata
assert readj(BASE + "input-validation-v1.json") == validation
assert readj(BASE + "manifest-v1.json") == manifest
print(json.dumps({
    "entire_whole_initial_frozen": True,
    "manifest": rec(BASE + "manifest-v1.json"),
    "whole_report": rec(BASE + "initial-v1.md"),
    "all100_obligations": True,
    "occurrences": len(rows), "deduplicated_paths": len(unique),
    "new_packet_paths_including_manifest": 10,
    "own_paths_after_this_packet": 581,
    "postfreeze_errors": 0,
    "mathematical_validation_by_code": False
}, indent=2))
