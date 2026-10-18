#!/usr/bin/env python3
"""Administrative SHA/JSON preservation only. No mathematical computation."""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
BASE = "problems/2025-B4/notes/reasoning-Runge-return-r2-"
PARENT = "problems/2019-B4/notes/reasoning-growth-return-r1-freeze-v1.json"
PARENT_BYTES = 4377
PARENT_SHA = "25d04505390ddad2020300d6459445741967ad9142be311540a5f14e2690b4b7"
PROTECTED = [
    "AGENTS.md",
    "problems/2025-B4/statement.md",
    "problems/2025-B4/proofs/reviewed-original-weight-universal-v1.1.md",
    "problems/2025-B4/reviews/original-weight-universal-acceptance.md",
    "problems/2025-B4/reviews/original-weight-universal-acceptance.json",
    "problems/2025-B4/proofs/reviewed-reasoning-return-r6-v1.1.md",
    "problems/2025-B4/reviews/reasoning-return-r6-acceptance.md",
    "problems/2025-B4/reviews/reasoning-return-r6-acceptance.json",
    "problems/2025-B4/proofs/reviewed-reasoning-return-r8-v1.1.md",
    "problems/2025-B4/reviews/reasoning-return-r8-acceptance.md",
    "problems/2025-B4/reviews/reasoning-return-r8-acceptance.json",
    "problems/2025-B4/proofs/reviewed-reasoning-return-r9-v1.1.md",
    "problems/2025-B4/reviews/reasoning-return-r9-acceptance.md",
    "problems/2025-B4/reviews/reasoning-return-r9-acceptance.json",
    "problems/2025-B4/proofs/reviewed-reasoning-return-r9-runge-v1.1.md",
    "problems/2025-B4/reviews/reasoning-return-r9-runge-acceptance.md",
    "problems/2025-B4/reviews/reasoning-return-r9-runge-acceptance.json",
    "problems/2025-B4/notes/coordinator-Runge-quotient-r1-worklog-v1.md",
    "problems/2025-B4/notes/reasoning-return-r9-failed-routes-v1.1.md",
    "problems/2025-B4/notes/reasoning-return-r9-runge-sources-v1.md",
    "problems/2025-B4/notes/reasoning-return-r9-runge-failures-worklog-v1.md",
    PARENT,
]
CONTEXT_ONLY = ["problems/2025-B4/research.md", "problems/2025-B4/references.md"]
PAYLOAD_SUFFIXES = [
    "baseline-v1.json", "candidate-v1.md", "obligations-v1.md",
    "failed-routes-v1.md", "sources-v1.md", "sources-v1.json",
    "worklog-v1.md", "freeze-v1.py",
]


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def fp(rel):
    data = (ROOT / rel).read_bytes()
    return {"path": rel, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                         separators=(",", ":")).encode()).hexdigest()


def save_new(rel, value):
    assert rel.startswith(BASE), rel
    with (ROOT / rel).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def parent_record():
    rec = fp(PARENT)
    assert rec["bytes"] == PARENT_BYTES and rec["sha256"] == PARENT_SHA, rec
    old = json.loads((ROOT / PARENT).read_text())
    assert old["older_plus_new_own_paths_bound_transitively"] == 574
    return rec


def baseline():
    records = [fp(rel) for rel in PROTECTED]
    assert len({r["path"] for r in records}) == len(records) == 22
    parent = parent_record()
    save_new(BASE + "baseline-v1.json", {
        "observed_utc": now(),
        "purpose": "compact necessary OLD-input fingerprints; metadata only",
        "protected_inputs": records,
        "protected_unique_paths": len(records),
        "protected_declared_occurrences_including_parent_binding": len(records)+1,
        "canonical_protected_summary_sha256": canonical(records),
        "compact_immediate_own_parent": parent,
        "older_own_paths_bound_transitively": 574,
        "historical_inventory_not_recopied_or_reverified": True,
        "context_only_observed": [fp(rel) for rel in CONTEXT_ONLY],
        "context_note": "Coordinator-owned mutable landscape/reference observations, not frozen mathematical premises or a promise that other owners cannot update them.",
        "no_NEW_active_peer_review_material_read": True,
        "no_old_shared_Git_or_cache_write": True,
    })
    print(json.dumps({"baseline": fp(BASE + "baseline-v1.json")}))


def verify_old():
    old = json.loads((ROOT / (BASE + "baseline-v1.json")).read_text())
    mismatches = [rec["path"] for rec in old["protected_inputs"]
                  if fp(rec["path"]) != rec]
    assert not mismatches, mismatches
    assert canonical(old["protected_inputs"]) == old["canonical_protected_summary_sha256"]
    assert parent_record() == old["compact_immediate_own_parent"]
    return old


def finish():
    old = verify_old()
    main = (ROOT / (BASE + "candidate-v1.md")).read_text()
    ledger = (ROOT / (BASE + "obligations-v1.md")).read_text()
    labels = re.findall(r"^\| RS-(\d+) \|", ledger, re.M)
    assert labels == [f"{n:02d}" for n in range(1, 61)], labels
    assert "Candidate proof - unverified." in main
    for claim in ("RS1", "RS2", "RS3", "RS4"):
        assert claim in main
    for suffix in ("baseline-v1.json", "sources-v1.json"):
        json.loads((ROOT / (BASE + suffix)).read_text())
    payloads = [fp(BASE + suffix) for suffix in PAYLOAD_SUFFIXES]
    validation = {
        "verified_utc": now(),
        "kind": "metadata-only; NOT mathematical proof or tests",
        "all_22_necessary_protected_inputs_unchanged": True,
        "protected_occurrences_including_parent": 23,
        "compact_parent_exact_bytes_SHA_and_574_count_verified": True,
        "all_60_obligation_labels_present_in_order": True,
        "all_four_claim_labels_and_unverified_status_present": True,
        "new_JSON_parses": True,
        "payloads_before_validation": payloads,
        "no_expanded_historical_inventory_or_peer_findings_read": True,
    }
    save_new(BASE + "input-validation-v1.json", validation)
    records = payloads + [fp(BASE + "input-validation-v1.json")]
    manifest = {
        "frozen_utc": now(),
        "status": "COMPLETE constructor checkpoint; candidate proof - unverified",
        "scope": "2025 B4(b), RS1--RS4 ENTIRE main and ALL60 obligations",
        "constructor": "/root/review_2022_complexity_r2",
        "root_quotient_lead_is_constructive_contribution": True,
        "B_and_root_EXCLUDED_from_independent_auditor_count": True,
        "TWO_OTHER_fresh_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "coordinator_promotion": False,
        "new_proposed_content": "faithful p^2 integral norm; explicit original-weight support bounds/fixed-r obstruction; reconstructed degree-p quotient/genus/normalization; exact unresolved arithmetic boundary",
        "published_Louboutin_lower_bound_is_attributed_import": True,
        "Gauss_log_normalization_and_p_denominator_derived": True,
        "no_new_actual_Diophantine_exclusion_X_bound_annual_or_novelty_claim": True,
        "all60_obligations_and_full_sources_failures_worklog_present": True,
        "old_authorship_review_roles_disclosed_not_self_recertified": True,
        "no_NEW_active_peer_review_material_read": True,
        "no_math_code_CAS_scan_RR_L_value_certificate_or_author_rerun": True,
        "no_Git_shared_old_cache_write_spawn_contact_charge_or_bypass": True,
        "compact_necessary_input_baseline": fp(BASE + "baseline-v1.json"),
        "protected_input_unique_paths": 22,
        "protected_declared_occurrences_including_parent": 23,
        "context_only_mutable_observations": 2,
        "canonical_protected_summary_sha256": old["canonical_protected_summary_sha256"],
        "compact_immediate_own_parent": old["compact_immediate_own_parent"],
        "older_own_paths_bound_transitively": 574,
        "new_own_files_including_manifest": 10,
        "older_plus_new_own_paths_bound_transitively": 584,
        "historical_inventory_not_recopied_or_reverified": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "authoritative_weekly_telemetry": {
            "observed_at_utc": "2026-10-18 07:05:40 UTC",
            "method": "mcp__codex_app__get_usage_limits({}); clock in same independent batch",
            "account_label": "029a8928...1334ac3a",
            "used_percent_TOTAL": 13,
            "window_minutes": 10080,
            "reset_unix": 1792874445,
            "ordinary_usage_allowed": True,
            "current_window_explicitly_human_authorized": True,
            "ceiling_TOTAL_percent": 90,
            "integration_reserve": True,
            "automatic_further_reset_spending": False,
        },
        "artifacts": records,
    }
    save_new(BASE + "freeze-v1.json", manifest)
    verify()


def verify():
    verify_old()
    manifest = json.loads((ROOT / (BASE + "freeze-v1.json")).read_text())
    for rec in manifest["artifacts"]:
        assert fp(rec["path"]) == rec, rec["path"]
    assert len(manifest["artifacts"]) == 9
    print(json.dumps({"all_9_payload_fingerprints_postverified": True,
                      "all_22_necessary_old_inputs_unchanged": True,
                      "main": fp(BASE + "candidate-v1.md"),
                      "freeze": fp(BASE + "freeze-v1.json"),
                      "new_total_files_including_freeze": 10,
                      "own_paths_bound_transitively": 584}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("baseline", "finish", "verify"))
    mode = parser.parse_args().mode
    {"baseline": baseline, "finish": finish, "verify": verify}[mode]()
