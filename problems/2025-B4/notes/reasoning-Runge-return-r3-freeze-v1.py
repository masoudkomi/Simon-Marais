"""METADATA ONLY. No mathematical program, scan, CAS or source replay.

Create only unused reasoning-Runge-return-r3-* files. Bind necessary
immutable old inputs and compact parents; never recopy/replay history.
Commands: python3 THIS --baseline; python3 THIS --freeze.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/notes/reasoning-Runge-return-r3"
PARENT = "problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-review-2-manifest-v1.json"
GUARDS = [
    "AGENTS.md",
    "problems/2025-B4/statement.md",
    "problems/2025-B4/proofs/reviewed-reasoning-Runge-return-r2-v1.1.md",
    "problems/2025-B4/reviews/reasoning-Runge-return-r2-acceptance.md",
    "problems/2025-B4/reviews/reasoning-Runge-return-r2-acceptance.json",
    "problems/2025-B4/notes/reasoning-Runge-return-r2-freeze-v1.json",
    "problems/2025-B4/notes/reasoning-Runge-return-r2-candidate-v1.md",
    "problems/2025-B4/notes/reasoning-Runge-return-r2-sources-v1.md",
    "problems/2025-B4/notes/reasoning-Runge-return-r2-sources-v1.json",
    "problems/2025-B4/notes/reasoning-Runge-return-r2-failed-routes-v1.md",
    "problems/2025-B4/proofs/reviewed-reasoning-return-r6-v1.1.md",
    "problems/2025-B4/reviews/reasoning-return-r6-acceptance.md",
    "problems/2025-B4/reviews/reasoning-return-r6-acceptance.json",
    "problems/2025-B4/proofs/reviewed-reasoning-return-r9-runge-v1.1.md",
    "problems/2025-B4/reviews/reasoning-return-r9-runge-acceptance.md",
    "problems/2025-B4/reviews/reasoning-return-r9-runge-acceptance.json",
    "problems/2025-B4/proofs/reviewed-reasoning-return-r9-v1.1.md",
    "problems/2025-B4/reviews/reasoning-return-r9-acceptance.md",
    "problems/2025-B4/notes/coordinator-Runge-quotient-r1-worklog-v1.md",
    PARENT,
]
EXPECTED_SHA = {
    "AGENTS.md": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff",
    "problems/2025-B4/proofs/reviewed-reasoning-Runge-return-r2-v1.1.md": "33222ffbc2a756fe5f7a9641c248654b0d5626e8283d3d054624b69496c658a3",
    "problems/2025-B4/proofs/reviewed-reasoning-return-r6-v1.1.md": "4e157819789da12d6f26e89929d88ec886d52947405d836fe3957ab8ee727d3a",
    "problems/2025-B4/proofs/reviewed-reasoning-return-r9-runge-v1.1.md": "4ae442f75a8ec6a3cc370e92ade90a9ed126367e873588e83d6b2e72702afdf1",
    PARENT: "3fa70a3b55a0c1dfdd983826bb1d23722d12305ccf164c3d4534184ff626e14f",
}
AUTHORITIES = [
    "problems/2025-B4/reviews/reasoning-Runge-return-r2-acceptance.json",
    "problems/2025-B4/reviews/reasoning-return-r6-acceptance.json",
    "problems/2025-B4/reviews/reasoning-return-r9-runge-acceptance.json",
]
CONTEXT = ["problems/2025-B4/research.md", "problems/2025-B4/references.md"]
SUFFIXES = [
    "candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
    "sources-v1.md", "sources-v1.json", "worklog-v1.md",
    "freeze-v1.py", "baseline-v1.json", "input-validation-v1.json",
]
TELEMETRY = {
    "observed_at_utc": "2026-10-18 09:31:00 UTC",
    "method": "get_usage_limits and clock in same independent batch",
    "account_label": "029a8928...1334ac3a",
    "used_percent_TOTAL": 21, "window_minutes": 10080,
    "reset_unix": 1792874445, "ordinary_usage_allowed": True,
    "legacy_by_limit_agree": True,
    "human_authorized_current_window_ONLY": True,
    "ceiling_TOTAL_percent": 90, "integration_reserve": True,
    "automatic_later_reset_spending": False,
}


def now():
    return datetime.now(timezone.utc).isoformat()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": digest(data)}


def read_json(path):
    return json.loads((ROOT / path).read_text())


def put_new(path, obj):
    assert path.startswith(PREFIX + "-")
    with (ROOT / path).open("x") as out:
        json.dump(obj, out, indent=2, ensure_ascii=False)
        out.write("\n")


def verify(rec):
    assert record(rec["path"]) == rec, rec["path"]


def declared_summary(path):
    rows = []

    def visit(obj):
        if isinstance(obj, dict):
            if isinstance(obj.get("path"), str) and isinstance(obj.get("bytes"), int) and isinstance(obj.get("sha256"), str):
                rows.append({key: obj[key] for key in ("path", "bytes", "sha256")})
            for value in obj.values():
                visit(value)
        elif isinstance(obj, list):
            for value in obj:
                visit(value)

    visit(read_json(path))
    distinct = {canonical(row) for row in rows}
    return {
        "immutable_parent": record(path),
        "declared_fingerprint_occurrences": len(rows),
        "deduplicated_paths": len({row["path"] for row in rows}),
        "canonical_deduplicated_record_summary_sha256": digest(b"\n".join(sorted(distinct))),
        "historical_inventory_rows_not_copied_or_recursively_reverified": True,
    }


def accepted_checks():
    rows = []
    for path in AUTHORITIES:
        obj = read_json(path)
        rec = obj["accepted_copy"]
        verify(rec)
        assert obj["status"] == "proved, independently reviewed scoped partial result"
        assert obj["unresolved_substantive_issues"] == 0
        rows.append({"authority": record(path), "accepted_body": rec})
    # The original RS main is the exact accepted-copy suffix, not a repair.
    rs = read_json(AUTHORITIES[0])
    verify(rs["candidate"])
    assert (ROOT / rs["accepted_copy"]["path"]).read_bytes().endswith((ROOT / rs["candidate"]["path"]).read_bytes())
    return rows


def baseline():
    guards = [record(path) for path in GUARDS]
    assert len({rec["path"] for rec in guards}) == len(guards)
    for rec in guards:
        if rec["path"] in EXPECTED_SHA:
            assert rec["sha256"] == EXPECTED_SHA[rec["path"]], rec["path"]
    parents = [declared_summary(path) for path in AUTHORITIES + ["problems/2025-B4/notes/reasoning-Runge-return-r2-freeze-v1.json", PARENT]]
    parent = read_json(PARENT)
    assert parent["older_plus_new_own_paths_bound_transitively"] == 636
    obj = {
        "created_utc": now(), "status": "metadata-only constructor baseline",
        "prefix_confirmed_unused_before_first_write": True,
        "protected": guards,
        "protected_occurrences": len(guards), "protected_unique_paths": len(guards),
        "canonical_protected_summary_sha256": digest(canonical(guards)),
        "accepted_pointer_checks": accepted_checks(),
        "compact_immutable_parents": parents,
        "immediate_own_parent": record(PARENT),
        "older_own_paths_bound_transitively": 636,
        "context_only_mutable_observations_NOT_premises_or_immutable_guards": [record(path) for path in CONTEXT],
        "no_mathematical_program_scan_CAS_or_author_rerun": True,
        "no_old_shared_Git_cache_write": True,
    }
    path = PREFIX + "-baseline-v1.json"
    put_new(path, obj)
    print(json.dumps({"baseline": record(path), "protected": len(guards), "accepted_pointers": 3}))


def freeze():
    base_path = PREFIX + "-baseline-v1.json"
    base = read_json(base_path)
    for rec in base["protected"]:
        verify(rec)
    pointers = accepted_checks()
    ledger = (ROOT / (PREFIX + "-obligations-v1.md")).read_text()
    labels = re.findall(r"\| (R3O-\d{2}) \|", ledger)
    assert labels == [f"R3O-{i:02d}" for i in range(1, 61)]
    sources = read_json(PREFIX + "-sources-v1.json")
    assert sources["B_constructor_excluded"] is True
    main = (ROOT / (PREFIX + "-candidate-v1.md")).read_text()
    assert "Candidate proof - unverified" in main
    assert all(f"**BR{i}:" in main for i in range(1, 6))
    val_path = PREFIX + "-input-validation-v1.json"
    validation = {
        "verified_utc": now(), "metadata_only_NOT_mathematical_evidence": True,
        "all_protected_unchanged": len(base["protected"]),
        "accepted_pointers_exact": len(pointers),
        "RS_unchanged_candidate_is_accepted_copy_suffix": True,
        "all60_constructor_hand_obligations_present_once_in_order": True,
        "source_JSON_parsed_and_scope_disclosed": True,
        "no_historical_inventory_copy_recursive_replay_or_new_peer_material": True,
        "no_math_code_scan_CAS_tests_certificate_or_author_rerun": True,
        "authoritative_weekly_telemetry": TELEMETRY,
    }
    put_new(val_path, validation)
    artifacts = [record(PREFIX + "-" + suffix) for suffix in SUFFIXES]
    manifest = {
        "frozen_utc": now(), "status": "ENTIRE constructor checkpoint; candidate proof - unverified",
        "scope": "2025 B4(b) signed prime diagonal p>=37; BR1--BR5 ENTIRE and ALL60",
        "constructor": "/root/review_2022_complexity_r2",
        "constructor_EXCLUDED_from_independent_auditor_count": True,
        "TWO_OTHER_fresh_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "root_NEW_mathematical_contribution": False,
        "older_root_RS_quotient_contribution_and_B_roles_disclosed": True,
        "coordinator_promotion_external_validation_annual_solution_or_priority_claim": False,
        "proposed_actual_sector_exclusions_not_unrestricted_prime_bound": True,
        "weighted_integrality_at_ALL_finite_primes_including_p": True,
        "actual_ideal_nonzero_argument_and_residual_both_center_proof": True,
        "full_candidate_obligations_sources_failures_worklog_present": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "compact_necessary_baseline": record(base_path),
        "protected_input_occurrences": len(base["protected"]),
        "protected_input_unique_paths": len(base["protected"]),
        "canonical_protected_summary_sha256": base["canonical_protected_summary_sha256"],
        "accepted_pointer_checks": pointers,
        "compact_immutable_parents": base["compact_immutable_parents"],
        "immediate_own_parent": base["immediate_own_parent"],
        "older_own_paths_bound_transitively": 636,
        "new_own_files_including_manifest": 10,
        "older_plus_new_own_paths_bound_transitively": 646,
        "historical_inventory_not_recopied_or_recursively_reverified": True,
        "no_NEW_active_peer_review_material_read": True,
        "no_corresponding_C_NEW_WC_files_findings_hashes_or_metadata_read": True,
        "WC_mathematical_findings_still_withheld_until_BOTH_entire_initials_confirmed": True,
        "no_math_code_CAS_scan_tests_source_certificate_or_author_rerun": True,
        "no_Git_shared_old_cache_write_spawn_contact_charge_or_bypass": True,
        "authoritative_weekly_telemetry": TELEMETRY,
        "artifacts": artifacts,
    }
    man_path = PREFIX + "-freeze-v1.json"
    put_new(man_path, manifest)
    for rec in artifacts + base["protected"]:
        verify(rec)
    assert len(artifacts) + 1 == 10
    print(json.dumps({
        "entire_constructor_files": 10, "whole_obligations": 60,
        "protected_unchanged": len(base["protected"]),
        "accepted_pointers_exact": len(pointers),
        "main": record(PREFIX + "-candidate-v1.md"),
        "freeze": record(man_path),
        "postverification": "all exact; candidate remains unverified",
    }))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--baseline", action="store_true")
    group.add_argument("--freeze", action="store_true")
    args = parser.parse_args()
    baseline() if args.baseline else freeze()
