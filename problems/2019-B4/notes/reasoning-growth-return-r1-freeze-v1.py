"""Metadata-only freezer/reader. Never runs mathematical code or parent jobs."""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/notes/reasoning-growth-return-r1-"
PAYLOAD_SUFFIXES = [
    "baseline-v1.json", "candidate-v1.md", "obligations-v1.md",
    "failed-routes-v1.md", "sources-v1.md", "sources-v1.json",
    "worklog-v1.md", "freeze-v1.py", "input-validation-v1.json",
]
MANIFEST = ROOT / (PREFIX + "freeze-v1.json")
VALIDATION = ROOT / (PREFIX + "input-validation-v1.json")


def fingerprint(relative):
    path = ROOT / relative
    data = path.read_bytes()
    return {"path": relative, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def exclusive_write(path, value):
    assert str(path.relative_to(ROOT)).startswith(PREFIX)
    with path.open("xb") as output:
        output.write(json_bytes(value))


def check_inputs_and_schema():
    baseline = json.loads((ROOT / (PREFIX + "baseline-v1.json")).read_text())
    inputs = baseline["inputs"]
    assert len(inputs) == 20
    assert len({row["path"] for row in inputs}) == 20
    current = [fingerprint(row["path"]) for row in inputs]
    assert current == inputs, "A necessary protected input changed"
    parent = baseline["immediate_own_parent"]
    assert parent == inputs[-1]
    assert parent["bytes"] == 5273
    assert parent["sha256"] == "5d3059a5075867e28b47a6af91db8d4d1a6505199d19dd8043cbb4f46b0fa1e4"
    parent_json = json.loads((ROOT / parent["path"]).read_text())
    assert parent_json["older_plus_new_own_paths_bound_transitively"] == 564
    assert baseline["older_own_paths_bound_transitively"] == 564
    obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
    labels = re.findall(r"^\| (G\d{2}) \|", obligations, flags=re.MULTILINE)
    assert labels == [f"G{i:02d}" for i in range(1, 61)]
    main = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
    assert "Candidate proof - unverified" in main
    for label in ["**G1.", "**G2.", "**G3.", "**G4.", "**G5."]:
        assert label in main
    source = json.loads((ROOT / (PREFIX + "sources-v1.json")).read_text())
    assert len(source["external_sources"]) == 4
    assert not source["native_pdf_downloads"]
    summary = hashlib.sha256(json.dumps(current, sort_keys=True,
                            separators=(",", ":")).encode()).hexdigest()
    return baseline, summary


def freeze():
    assert not MANIFEST.exists() and not VALIDATION.exists(), "Frozen bytes exist"
    baseline, summary = check_inputs_and_schema()
    expected_now = {PREFIX + suffix for suffix in PAYLOAD_SUFFIXES[:-1]}
    actual_now = {str(path.relative_to(ROOT)) for path in MANIFEST.parent.glob(
        "reasoning-growth-return-r1-*")}
    assert actual_now == expected_now, "Unexpected new-prefix file"
    validation = {
        "checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "purpose": "metadata integrity ONLY; not independent mathematical verification",
        "baseline": fingerprint(PREFIX + "baseline-v1.json"),
        "all20_necessary_input_fingerprints_match": True,
        "unique_paths_verified": 20,
        "declared_occurrences_verified_in_baseline": 21,
        "occurrence_count_note": "20 inputs plus duplicate immediate-parent record",
        "canonical_input_summary_sha256": summary,
        "immediate_own_parent_verified_without_recursive_inventory_walk": True,
        "older_own_paths_bound_transitively": 564,
        "all60_obligation_labels_and_all5_claim_labels_present": True,
        "all_sources_JSON_records_parse": True,
        "mathematical_proof_checked_by_program": False,
        "mathematical_executable_CAS_scan_author_rerun_certificate_replay": False,
        "mismatches": [],
    }
    exclusive_write(VALIDATION, validation)
    artifacts = [fingerprint(PREFIX + suffix) for suffix in PAYLOAD_SUFFIXES]
    manifest = {
        "frozen_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "COMPLETE constructor checkpoint; candidate proof - unverified",
        "constructor": "/root/review_2022_complexity_r2",
        "scope": "2019 B4(b), complete G1--G5 and all60 whole obligations",
        "two_OTHER_fresh_initially_blind_WHOLE_audits_required": True,
        "coordinator_promotion": False,
        "root_generic_assignment_and_typo_correction_supplied_no_NEW_inference": True,
        "old_B_input_review_roles_disclosed_not_recertified": True,
        "new_actual_obstruction_imbalance_moment_bound": "W(R)<=2R",
        "finite_critical_profile_and_pressure_claims_EXPLICITLY_conditional": True,
        "no_actual_regime_selected_or_new_numeric_or_annual_or_novelty_claim": True,
        "all60_whole_obligations_present": True,
        "full_proof_failures_sources_worklog_and_compact_preservation_present": True,
        "no_NEW_active_peer_review_material_read": True,
        "no_math_code_CAS_scan_old_certificate_or_author_rerun": True,
        "no_Git_shared_old_cache_write_spawn_contact_charge_or_bypass": True,
        "compact_necessary_input_baseline": fingerprint(PREFIX + "baseline-v1.json"),
        "protected_input_unique_paths": 20,
        "declared_occurrences_verified_in_baseline": 21,
        "canonical_input_summary_sha256": summary,
        "compact_immediate_own_parent": baseline["immediate_own_parent"],
        "older_own_paths_bound_transitively": 564,
        "new_own_files_including_manifest": 10,
        "older_plus_new_own_paths_bound_transitively": 574,
        "historical_inventory_not_recopied_or_reverified": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "authoritative_weekly_telemetry": {
            "observed_at_utc": "2026-10-18 06:43:29 UTC",
            "method": "mcp__codex_app__get_usage_limits({}); clock immediately afterward",
            "account_label": "029a8928...1334ac3a",
            "used_percent_TOTAL": 12,
            "window_minutes": 10080,
            "reset_unix": 1792874445,
            "ordinary_usage_allowed": True,
            "current_window_explicitly_human_authorized": True,
            "ceiling_TOTAL_percent": 90,
            "integration_reserve": True,
            "automatic_further_reset_spending": False,
        },
        "artifacts": artifacts,
    }
    exclusive_write(MANIFEST, manifest)
    verify()


def verify():
    baseline, summary = check_inputs_and_schema()
    manifest = json.loads(MANIFEST.read_text())
    assert manifest["canonical_input_summary_sha256"] == summary
    assert manifest["compact_immediate_own_parent"] == baseline["immediate_own_parent"]
    assert manifest["older_plus_new_own_paths_bound_transitively"] == 574
    expected = {PREFIX + suffix for suffix in PAYLOAD_SUFFIXES}
    assert {row["path"] for row in manifest["artifacts"]} == expected
    for row in manifest["artifacts"]:
        assert fingerprint(row["path"]) == row, "Frozen payload changed"
    actual = {str(path.relative_to(ROOT)) for path in MANIFEST.parent.glob(
        "reasoning-growth-return-r1-*")}
    assert actual == expected | {str(MANIFEST.relative_to(ROOT))}
    print(json.dumps({
        "status": "metadata postfreeze verification passed; NOT mathematical acceptance",
        "main": fingerprint(PREFIX + "candidate-v1.md"),
        "freeze": fingerprint(PREFIX + "freeze-v1.json"),
        "payload_files": 9,
        "necessary_inputs": 20,
        "whole_obligations": 60,
        "own_paths_transitively_bound": 574,
    }, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["freeze", "verify"])
    arguments = parser.parse_args()
    if arguments.mode == "freeze":
        freeze()
    else:
        verify()
