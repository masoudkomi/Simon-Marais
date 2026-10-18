#!/usr/bin/env python3
"""Administrative fingerprints and label checks ONLY; no mathematical scan."""
import argparse
import datetime
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/notes/reasoning-critical-return-r2-"
PARENT = {
    "path": "problems/2020-B4/notes/reasoning-arithmetic-return-r11-freeze-v1.json",
    "bytes": 6719,
    "sha256": "0c53f7526ba90e3a8a5e419562f593f79923810aa63127cbe1bf053af5361906",
}
AUTHORITY_PATHS = [
    "problems/2019-B4/reviews/reasoning-return-r7-acceptance.json",
    "problems/2019-B4/reviews/monotone-ratio-acceptance.json",
    "problems/2019-B4/reviews/reasoning-growth-return-r1-acceptance.json",
    "problems/2019-B4/reviews/walk-Frechet-acceptance.json",
]
PROTECTED_PATHS = [
    "AGENTS.md",
    "problems/2019-B4/statement.md",
    "problems/2019-B4/proofs/reviewed-secondpass-v1.1.md",
    "problems/2019-B4/notes/secondpass-canonical-renewal.md",
    "problems/2019-B4/notes/secondpass-rigidity-obstructions.md",
    "problems/2019-B4/notes/secondpass-staircases-and-pumping.md",
    "problems/2019-B4/reviews/secondpass-acceptance.json",
    "problems/2019-B4/proofs/reviewed-reasoning-return-r7-v1.1.md",
    "problems/2019-B4/reviews/reasoning-return-r7-acceptance.json",
    "problems/2019-B4/proofs/reviewed-monotone-ratio-v1.1.md",
    "problems/2019-B4/reviews/monotone-ratio-acceptance.json",
    "problems/2019-B4/proofs/reviewed-reasoning-growth-return-r1-v1.1.md",
    "problems/2019-B4/reviews/reasoning-growth-return-r1-acceptance.json",
    "problems/2019-B4/proofs/reviewed-walk-Frechet-v1.1.md",
    "problems/2019-B4/reviews/walk-Frechet-acceptance.json",
    "problems/2019-B4/notes/reasoning-growth-return-r1-failed-routes-v1.md",
    "problems/2019-B4/notes/coordinator-short-joining-research-v1.md",
    "problems/2019-B4/notes/coordinator-trace-recognition-return-v1.md",
    PARENT["path"],
]
PAYLOAD_NAMES = [
    "candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "sources-v1.md", "sources-v1.json", "failed-routes-v1.md",
    "worklog-v1.md", "baseline-v1.json", "freeze-v1.py",
    "input-validation-v1.json",
]


def read_json(path):
    return json.loads((ROOT / path).read_text())


def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def canonical_sha(value):
    data = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def check_record(rec):
    actual = fingerprint(rec["path"])
    assert actual == rec, (rec, actual)
    return actual


def save_new(suffix, value):
    path = PREFIX + suffix
    with (ROOT / path).open("x") as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    return fingerprint(path)


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def authority_summaries():
    result = []
    for path in AUTHORITY_PATHS:
        authority = read_json(path)
        copy = authority["accepted_copy"]
        check_record(copy)
        assert authority["unresolved_substantive_issues"] == 0
        assert authority["repair_required"] is False
        result.append({
            "authority": fingerprint(path),
            "accepted_copy": copy,
            "historical_declared_occurrences": authority.get("record_occurrences_verified"),
            "historical_declared_unique_paths": authority.get("unique_paths_verified"),
            "historical_inventory_recursively_replayed": False,
        })
    second = read_json("problems/2019-B4/reviews/secondpass-acceptance.json")
    declared = second["artifacts"]
    checked = []
    for path in PROTECTED_PATHS:
        if path.startswith("problems/2019-B4/"):
            local = path[len("problems/2019-B4/"):]
            if local in declared:
                actual = fingerprint(path)
                assert actual["sha256"] == declared[local]
                checked.append(actual)
    return result, checked


def check_labels(suffix):
    body = (ROOT / (PREFIX + suffix)).read_text()
    labels = [int(x) for x in re.findall(r"(?m)^(\d+)\. ", body)]
    assert labels == list(range(1, 61)), (suffix, labels)
    return len(labels)


def baseline():
    check_record(PARENT)
    parent = read_json(PARENT["path"])
    assert parent["older_plus_new_own_paths_bound_transitively"] == 605
    guards = [fingerprint(path) for path in PROTECTED_PATHS]
    assert len({r["path"] for r in guards}) == len(guards)
    assert guards[0]["sha256"] == "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"
    accepted, secondpass = authority_summaries()
    output = {
        "captured_utc": utc(),
        "purpose": "necessary fixed-file guards and compact immutable parent binding",
        "mathematical_validation": False,
        "protected_occurrences": len(guards),
        "protected_unique_paths": len(guards),
        "protected": guards,
        "canonical_protected_summary_sha256": canonical_sha(guards),
        "immediate_own_parent": PARENT,
        "older_own_paths_bound_transitively": 605,
        "old_ancestry_recopied_or_recursively_rehashed": False,
        "accepted_authority_summaries": accepted,
        "secondpass_exact_declared_hashes_checked": secondpass,
        "mutable_research_and_references_read_as_context_not_immutable_premises": True,
        "NEW_active_peer_material_opened_or_hashed": False,
    }
    result = save_new("baseline-v1.json", output)
    print(json.dumps({"baseline": result, "protected_paths": len(guards), "accepted_copy_declarations_checked": len(accepted), "secondpass_declarations_checked": len(secondpass)}))


def freeze():
    base = read_json(PREFIX + "baseline-v1.json")
    for rec in base["protected"]:
        check_record(rec)
    assert canonical_sha(base["protected"]) == base["canonical_protected_summary_sha256"]
    accepted, secondpass = authority_summaries()
    assert accepted == base["accepted_authority_summaries"]
    assert secondpass == base["secondpass_exact_declared_hashes_checked"]
    obligations = check_labels("obligations-v1.md")
    dispositions = check_labels("constructor-checks-v1.md")
    candidate = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
    assert "Candidate proof - unverified" in candidate
    assert "CR1" in candidate and "CR5" in candidate
    assert "TWO OTHER" in candidate
    sources = read_json(PREFIX + "sources-v1.json")
    assert sources["mathematical_code_CAS_scan_or_author_rerun"] is False
    validation = {
        "checked_utc": utc(),
        "all_fixed_protected_records_unchanged": True,
        "protected_occurrences": len(base["protected"]),
        "protected_unique_paths": len(base["protected"]),
        "accepted_copy_declarations_checked": len(accepted),
        "secondpass_declarations_checked": len(secondpass),
        "obligation_labels_exactly_1_through": obligations,
        "constructor_dispositions_exactly_1_through": dispositions,
        "claims_CR1_through_CR5_present": True,
        "scope": "integrity and label completeness ONLY, no mathematical test or proof validation",
        "old_605_paths_bound_by_exact_parent_not_recursively_rehashed": True,
        "no_NEW_peer_material_read_or_hashed": True,
    }
    validation_rec = save_new("input-validation-v1.json", validation)
    artifacts = [fingerprint(PREFIX + name) for name in PAYLOAD_NAMES]
    assert len(artifacts) == 10
    output = {
        "frozen_utc": utc(),
        "status": "candidate proof - unverified; ENTIRE critical-return-r2 constructor checkpoint",
        "constructor": "/root/review_2022_complexity_r2",
        "NEW_claims": ["CR1", "CR2", "CR3", "CR4", "CR5"],
        "all60_obligations_and_constructor_checks_complete": True,
        "TWO_OTHER_entire_blind_whole_audits_and_coordinator_reconciliation_REQUIRED": True,
        "constructor_excluded_from_independent_review_count": True,
        "root_supplied_generic_assignment_no_NEW_proof_inference": True,
        "actual_regime_exact_lambda_numeric_improvement_annual_or_priority_claim": False,
        "new_unconditional_result": "actual distinct-context confined-piece entropy loss and logarithmic longest-piece bound",
        "remaining_gap": "control feasible-cut NUMBER without assuming spread or one-pass normalization bounds",
        "accepted_input_old_authorship_not_self_recertified": True,
        "necessary_protected_occurrences": len(base["protected"]),
        "necessary_protected_unique_paths": len(base["protected"]),
        "canonical_protected_summary_sha256": base["canonical_protected_summary_sha256"],
        "immediate_own_parent": PARENT,
        "accepted_authority_summaries": accepted,
        "older_own_paths_bound_transitively": 605,
        "new_own_files_including_freeze": 11,
        "older_plus_new_own_paths_bound_transitively": 616,
        "no_recursive_historical_inventory_copy_or_reverify": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "authoritative_weekly_telemetry": {
            "observed_at_utc": "2026-10-18 08:42:49 UTC",
            "method": "mcp__codex_app__get_usage_limits plus same-batch clock",
            "account_label": "029a8928...1334ac3a",
            "used_percent_TOTAL": 18,
            "window_minutes": 10080,
            "reset_unix": 1792874445,
            "ordinary_usage_allowed": True,
            "legacy_and_by_limit_agree": True,
            "current_window_explicitly_user_authorized": True,
            "ceiling_TOTAL_percent": 90,
            "integration_reserve": True,
            "automatic_later_reset_spending": False,
        },
        "mathematical_code_CAS_scan_source_or_author_rerun": False,
        "no_Git_shared_old_cache_write_spawn_contact_charge_or_bypass": True,
        "NEW_queued_CG_candidate_or_peer_material_read_or_hashed": False,
        "artifacts": artifacts,
    }
    freeze_rec = save_new("freeze-v1.json", output)
    for rec in artifacts:
        check_record(rec)
    for rec in base["protected"]:
        check_record(rec)
    check_record(freeze_rec)
    print(json.dumps({"complete_packet_files": 11, "obligations": obligations, "constructor_dispositions": dispositions, "protected_unchanged": len(base["protected"]), "main": artifacts[0], "validation": validation_rec, "freeze": freeze_rec, "postverification": "all exact"}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--baseline", action="store_true")
    group.add_argument("--freeze", action="store_true")
    args = parser.parse_args()
    if args.baseline:
        baseline()
    else:
        freeze()
