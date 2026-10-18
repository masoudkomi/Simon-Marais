#!/usr/bin/env python3
"""R15 compact administrative freeze. No field arithmetic or mathematics runs."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-unit-return-r15-"
PARENT = "problems/2020-B4/reviews/reasoning-arithmetic-return-r11-review-2-manifest-v1.json"
PARENT_SHA = "bfe677f652eb530288dc647d45109d1c2c3b4d6d2ef7d21363f02822da415fd1"
PROOFS = {
    "reasoning-return-r13": "a29ecdb8002f3cbb4250e93f94c65ed83a67b086331fb3497d48ad740959ab6b",
    "reasoning-return-r14": "c574096c94bc4deaab81b54c5dd0599f3089e7122165312d9089ea28d2a9f880",
}
CURRENT = [
    "AGENTS.md", "problems/2021-B4/statement.md",
    "problems/2021-B4/notes/reasoning-return-r13-source-audit-v1.md",
    "problems/2021-B4/notes/reasoning-return-r13-failed-routes-v1.md",
    "problems/2021-B4/notes/reasoning-return-r14-source-audit-v1.md",
    "problems/2021-B4/notes/reasoning-return-r14-failed-routes-v1.md",
    "problems/2021-B4/notes/coordinator-literature-frontier-recheck-v1.md",
    "problems/2021-B4/proofs/reviewed-reasoning-return-r8-v1.1.md",
    "problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
]
PAYLOADS = ["candidate-v1.md", "obligations-v1.md", "hand-checks-v1.md", "failed-routes-v1.md", "sources-v1.md", "sources-v1.json", "worklog-v1.md", "freeze-v1.py", "baseline-v1.json", "input-validation-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def load(path):
    return json.loads((ROOT / path).read_text())


def fp(path):
    content = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()}


def check(row):
    assert fp(row["path"]) == row, row["path"]
    return row


def canonical(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def new_json(suffix, value):
    path = PREFIX + suffix
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def baseline():
    rows = [fp(path) for path in CURRENT]
    authorities = []
    for stem, expected in PROOFS.items():
        authority_path = f"problems/2021-B4/reviews/{stem}-acceptance.json"
        authority = load(authority_path)
        proof = check(authority["accepted_copy"])
        assert proof["sha256"] == expected
        candidate = check(authority["candidate"])
        assert (ROOT / proof["path"]).read_bytes().endswith((ROOT / candidate["path"]).read_bytes())
        freeze_path = f"problems/2021-B4/notes/{stem}-freeze-v1.json"
        freeze_binding = next(row for row in authority["verification_metadata"] if row["path"] == freeze_path)
        check(freeze_binding)
        rows += [proof, fp(authority_path), fp(f"problems/2021-B4/reviews/{stem}-acceptance.md"), candidate, freeze_binding]
        authorities.append({
            "authority": fp(authority_path), "accepted_copy": proof,
            "exact_candidate_suffix_verified": candidate, "constructor_freeze_bound": freeze_binding,
            "historical_occurrences_bound_not_replayed": authority["record_occurrences_verified"],
            "historical_paths_bound_not_replayed": authority["unique_paths_verified"],
        })
    parent = fp(PARENT)
    assert (parent["bytes"], parent["sha256"]) == (2930, PARENT_SHA)
    parent_record = load(PARENT)
    rows += [parent] + [check(row) for row in parent_record["artifacts"]]
    unique = {}
    for row in rows:
        assert row["path"] not in unique or unique[row["path"]] == row
        unique[row["path"]] = row
    new_json("baseline-v1.json", {
        "recorded_at_utc": now(), "purpose": "necessary current fingerprints plus compact immutable parent metadata; no historical recursion",
        "fingerprint_occurrences": len(rows), "unique_paths": len(unique),
        "deduplicated_rows": list(unique.values()), "deduplicated_summary_sha256": canonical(list(unique.values())),
        "accepted_authorities": authorities, "immediate_own_parent": parent,
        "immediate_own_parent_payloads_checked": len(parent_record["artifacts"]),
        "own_parent_historical_summary_bound_not_replayed": parent_record["current_input_summary"],
        "NEW_prefix_confirmed_unused_before_first_write": True,
        "new_R15_inference_from_root_or_other_worker": False,
        "corresponding_queued_NEW_2022_peer_files_or_hash_access": False,
        "mathematical_program": False,
    })
    print(json.dumps({"baseline": fp(PREFIX + "baseline-v1.json"), "occurrences": len(rows), "paths": len(unique)}))


def verify_inputs():
    record = load(PREFIX + "baseline-v1.json")
    for row in record["deduplicated_rows"]:
        check(row)
    assert canonical(record["deduplicated_rows"]) == record["deduplicated_summary_sha256"]
    return record


def freeze():
    record = verify_inputs()
    expected = [f"R15-{i:02d}" for i in range(1, 49)]
    for suffix in ["obligations-v1.md", "hand-checks-v1.md"]:
        text = (ROOT / (PREFIX + suffix)).read_text()
        assert re.findall(r"^\| (R15-\d\d) \|", text, re.M) == expected
    new_json("input-validation-v1.json", {
        "verified_at_utc": now(), "all_current_inputs_unchanged": True,
        "fingerprint_occurrences_verified": record["fingerprint_occurrences"], "unique_paths_verified": record["unique_paths"],
        "deduplicated_summary_sha256": record["deduplicated_summary_sha256"],
        "both_accepted_body_candidate_suffixes_exact": True,
        "all48_obligation_and_constructor_check_labels_exact_once_in_order": True,
        "label_checks_are_text_structure_only_not_proof": True,
        "immediate_own_parent_and_eight_payloads_unchanged": True,
        "old_historical_inventory_recursively_replayed": False,
        "no_mathematical_code_or_source_author_rerun": True,
    })
    for suffix in ["sources-v1.json", "baseline-v1.json", "input-validation-v1.json"]:
        load(PREFIX + suffix)
    artifacts = [fp(PREFIX + suffix) for suffix in PAYLOADS]
    new_json("freeze-v1.json", {
        "frozen_at_utc": now(), "status": "candidate proof - unverified; ENTIRE R15A-C constructor checkpoint",
        "constructor": "/root/review_2021_reasoning_j15_r2", "constructor_excluded_from_independent_review_count": True,
        "NEW_proposed_claims": ["R15A", "R15B", "R15C"], "all48_obligations_and_constructor_checks_complete": True,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_and_full_coordinator_reconciliation_required": True,
        "proposed_entire_actual_m5_exclusion_only_in_exact_double_s_domain": True,
        "full_J15_degree20_annual_or_novelty_claim": False,
        "root_or_other_worker_supplied_NEW_R15_inference": False,
        "old_accepted_authorship_not_freshly_self_recertified": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "authoritative_weekly_telemetry": {
            "observed_utc": "2026-10-18 08:43:52 UTC", "method": "direct mcp__codex_app__get_usage_limits and clock in same awaited batch",
            "TOTAL_used_percent": 18, "window_minutes": 10080, "reset_unix": 1792874445,
            "ordinary_usage_allowed": True, "legacy_and_by_limit_agree": True,
            "account_label": "029a8928...1334ac3a", "current_window_explicitly_authorized": True,
            "ceiling_TOTAL_percent": 90, "integration_reserve": True, "automatic_later_week_spending": False,
        },
        "mathematical_code_CAS_scan_table_generator_source_or_author_rerun": False,
        "new_field_certificate_hand_derived_and_proof_critical": True,
        "no_Git_shared_old_cache_write_spawn_contact_charge_or_bypass": True,
        "current_input_summary": {"occurrences": record["fingerprint_occurrences"], "unique_paths": record["unique_paths"], "sha256": record["deduplicated_summary_sha256"]},
        "compact_own_parent": record["immediate_own_parent"],
        "accepted_authorities": record["accepted_authorities"],
        "artifacts": artifacts,
    })
    verify()


def verify():
    record = verify_inputs()
    manifest = load(PREFIX + "freeze-v1.json")
    for row in manifest["artifacts"]:
        check(row)
    print(json.dumps({"postverified": True, "freeze": fp(PREFIX + "freeze-v1.json"), "candidate": fp(PREFIX + "candidate-v1.md"), "whole_obligations": 48, "constructor_files_including_freeze": 11, "current_fingerprint_occurrences": record["fingerprint_occurrences"], "current_paths": record["unique_paths"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["baseline", "freeze", "verify"])
    args = parser.parse_args()
    {"baseline": baseline, "freeze": freeze, "verify": verify}[args.operation]()
