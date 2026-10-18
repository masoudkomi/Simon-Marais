#!/usr/bin/env python3
"""Metadata-only preservation for the R11 constructor packet. No mathematics runs."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-arithmetic-return-r11-"
PARENT = "problems/2017-B4/reviews/reasoning-global-return-r7-review-2-manifest-v1.json"
PARENT_BYTES = 5343
PARENT_SHA = "5717bd67ab617452e6416f139aa8ad8fcf98a7bc96c863c0b1f5123829031d7c"
PROOFS = {
    "reasoning-return-r7": "7517c6ffd5aff1135107020f9526922203496415515afb4bbd07176fb445d479",
    "reasoning-return-r8": "9003af18926d1fe49d3f997b40ed070ceefa37e42f73c5a98c32bbe7a2f3bfcb",
    "reasoning-arithmetic-return-r9": "ab2ee4e7a2dcfa464780c6144f996d683f08b7f04da63d2a77ee2fdd4ec922b8",
    "reasoning-arithmetic-return-r10": "dc540eef45a7c4054191a0fd9e723aa64e364163f04bf696450025ca3ca45f24",
}
PROTECTED = ["AGENTS.md", "problems/2020-B4/statement.md", PARENT]
for stem in PROOFS:
    PROTECTED.extend([
        f"problems/2020-B4/proofs/reviewed-{stem}-v1.1.md",
        f"problems/2020-B4/reviews/{stem}-acceptance.md",
        f"problems/2020-B4/reviews/{stem}-acceptance.json",
        f"problems/2020-B4/notes/{stem}-freeze-v1.json",
    ])
PROTECTED.extend([
    "problems/2020-B4/notes/reasoning-return-r8-source-audit-v1.md",
    "problems/2020-B4/notes/reasoning-arithmetic-return-r9-sources-v1.md",
    "problems/2020-B4/notes/reasoning-arithmetic-return-r10-sources-v1.md",
    "problems/2020-B4/notes/reasoning-return-r7-failed-routes-v1.md",
    "problems/2020-B4/notes/reasoning-return-r8-failed-routes-v1.md",
    "problems/2020-B4/notes/reasoning-arithmetic-return-r9-failed-routes-v1.md",
    "problems/2020-B4/notes/reasoning-arithmetic-return-r10-failed-routes-v1.md",
])
CONTEXT = ["problems/2020-B4/research.md", "problems/2020-B4/references.md"]
PAYLOADS = [
    "candidate-v1.md", "obligations-v1.md", "sources-v1.md", "sources-v1.json",
    "failed-routes-v1.md", "constructor-checks-v1.md", "worklog-v1.md",
    "baseline-v1.json", "freeze-v1.py", "input-validation-v1.json",
]


def now():
    return datetime.now(timezone.utc).isoformat()


def fp(path):
    content = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()}


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def new_json(path, value):
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def load(path):
    return json.loads((ROOT / path).read_text())


def baseline():
    old_parent = fp(PARENT)
    assert old_parent["bytes"] == PARENT_BYTES and old_parent["sha256"] == PARENT_SHA
    authority_summaries = []
    for stem, expected_sha in PROOFS.items():
        proof = fp(f"problems/2020-B4/proofs/reviewed-{stem}-v1.1.md")
        assert proof["sha256"] == expected_sha, proof
        authority_path = f"problems/2020-B4/reviews/{stem}-acceptance.json"
        authority = load(authority_path)
        assert authority["accepted_copy"] == proof
        authority_summaries.append({
            "authority": fp(authority_path),
            "accepted_copy": proof,
            "historical_declared_occurrences": authority["record_occurrences_verified"],
            "historical_declared_unique_paths": authority["unique_paths_verified"],
            "historical_inventory_recursively_replayed": False,
        })
    rows = [fp(path) for path in PROTECTED]
    assert len({row["path"] for row in rows}) == len(rows)
    record = {
        "recorded_utc": now(),
        "purpose": "compact necessary immutable inputs; no expanded historical inventory",
        "protected_fingerprint_occurrences": len(rows),
        "protected_unique_paths": len(rows),
        "protected": rows,
        "canonical_protected_summary_sha256": canonical(rows),
        "accepted_authority_summaries": authority_summaries,
        "immediate_own_parent": old_parent,
        "older_own_paths_bound_transitively": 594,
        "mutable_context_snapshots_not_required_unchanged": [fp(path) for path in CONTEXT],
        "NEW_prefix_unused_check": "rg --files problems/2020-B4/notes -g reasoning-arithmetic-return-r11-*; exit1/no matches before first new write",
        "mathematical_program": False,
    }
    new_json(PREFIX + "baseline-v1.json", record)
    print(json.dumps({"baseline": fp(PREFIX + "baseline-v1.json"), "protected": len(rows)}))


def verify_inputs():
    record = load(PREFIX + "baseline-v1.json")
    for row in record["protected"]:
        assert fp(row["path"]) == row, row["path"]
    assert canonical(record["protected"]) == record["canonical_protected_summary_sha256"]
    return record


def freeze():
    record = verify_inputs()
    obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
    checks = (ROOT / (PREFIX + "constructor-checks-v1.md")).read_text()
    expected = [f"R11-{i:02d}" for i in range(1, 61)]
    obligation_labels = re.findall(r"^\| (R11-\d\d) \|", obligations, re.M)
    check_labels = re.findall(r"^\| (R11-\d\d) \|", checks, re.M)
    assert obligation_labels == expected, obligation_labels
    assert check_labels == expected, check_labels
    validation = {
        "verified_utc": now(),
        "protected_fingerprint_occurrences_verified": record["protected_fingerprint_occurrences"],
        "protected_unique_paths_verified": record["protected_unique_paths"],
        "protected_inputs_unchanged": True,
        "canonical_protected_summary_sha256": record["canonical_protected_summary_sha256"],
        "obligation_labels_60_exact_once_in_order": True,
        "constructor_check_labels_60_exact_once_in_order": True,
        "label_checks_are_text_structure_only_not_proof": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "mathematical_code_CAS_scan_or_source_rerun": False,
        "no_Git_shared_old_cache_write_spawn_contact_charge_or_bypass": True,
        "source_primary_read_limits_explicit": True,
        "prior_own_files_bound_transitively": 594,
    }
    new_json(PREFIX + "input-validation-v1.json", validation)
    rows = [fp(PREFIX + suffix) for suffix in PAYLOADS]
    for suffix in ["sources-v1.json", "baseline-v1.json", "input-validation-v1.json"]:
        load(PREFIX + suffix)
    result = {
        "frozen_utc": now(),
        "status": "candidate proof - unverified; ENTIRE R11 constructor checkpoint",
        "constructor": "/root/review_2022_complexity_r2",
        "NEW_claims": ["A11A", "A11B", "A11C", "A11D", "A11E"],
        "all60_obligations_and_constructor_checks_complete": True,
        "TWO_OTHER_entire_blind_whole_audits_and_coordinator_reconciliation_REQUIRED": True,
        "constructor_excluded_from_independent_review_count": True,
        "root_supplied_generic_assignment_no_NEW_proof_inference": True,
        "no_new_numeric_taut_order_full_classification_or_novelty_claim": True,
        "accepted_input_old_authorship_not_self_recertified": True,
        "necessary_protected_occurrences": record["protected_fingerprint_occurrences"],
        "necessary_protected_unique_paths": record["protected_unique_paths"],
        "canonical_protected_summary_sha256": record["canonical_protected_summary_sha256"],
        "immediate_own_parent": record["immediate_own_parent"],
        "accepted_authority_summaries": record["accepted_authority_summaries"],
        "older_own_paths_bound_transitively": 594,
        "new_own_files_including_freeze": 11,
        "older_plus_new_own_paths_bound_transitively": 605,
        "no_recursive_historical_inventory_copy_or_reverify": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "authoritative_weekly_telemetry": {
            "observed_at_utc": "2026-10-18 08:05:41 UTC",
            "method": "mcp__codex_app__get_usage_limits and clock in same batch",
            "account_label": "029a8928...1334ac3a",
            "used_percent_TOTAL": 16,
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
        "artifacts": rows,
    }
    new_json(PREFIX + "freeze-v1.json", result)
    verify()


def verify():
    verify_inputs()
    manifest = load(PREFIX + "freeze-v1.json")
    for row in manifest["artifacts"]:
        assert fp(row["path"]) == row, row["path"]
    print(json.dumps({
        "postverified": True,
        "manifest": fp(PREFIX + "freeze-v1.json"),
        "candidate": fp(PREFIX + "candidate-v1.md"),
        "whole_obligations": 60,
        "new_files": 11,
        "protected_old_inputs_unchanged": len(PROTECTED),
        "status": "candidate proof - unverified",
    }))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["baseline", "freeze", "verify"])
    arguments = parser.parse_args()
    {"baseline": baseline, "freeze": freeze, "verify": verify}[arguments.operation]()
