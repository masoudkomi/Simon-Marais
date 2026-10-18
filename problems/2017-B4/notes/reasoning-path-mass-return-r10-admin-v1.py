#!/usr/bin/env python3
"""NEW R10 metadata only: no mathematical claim is evaluated or executed.

prepare writes compact baseline/validation; freeze requires explicit final
payload model-readback attestation; verify is a separate read-only mode.
Only this exact NEW prefix can be written, with exclusive-create semantics.
No directory inventory, old code import, subprocess, network or cache write.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/notes/reasoning-path-mass-return-r10-"
PARENT = {
    "path": "problems/2021-B4/reviews/reasoning-center-return-r20-review-2-manifest.json",
    "bytes": 4659,
    "sha256": "1875bf9fe5df4f6ca7fff4a25d5ae6e27efd3d06ebfb137544b05c89792af71b",
}
PM9_FREEZE = {
    "path": "problems/2017-B4/notes/coordinator-path-moment-r3-freeze-v2.json",
    "bytes": 4093,
    "sha256": "7210932f81b90afa8197fb40fe6c7cc3603fbfc85c39b58c67df4f36728b185d",
}
PM9_AUTH = "problems/2017-B4/reviews/coordinator-path-moment-r3-acceptance.json"
SCALAR_AUTH = "problems/2017-B4/reviews/allD-global-acceptance.json"
DC_AUTH = "problems/2017-B4/reviews/coarsening-acceptance.json"
EXACT_ACCEPTED = [
    {
        "path": "problems/2017-B4/proofs/reviewed-coordinator-path-moment-r3-v1.1.md",
        "bytes": 17529,
        "sha256": "a02b6edeed84cb984749a4418c8c02a67a7fffb3f8098523231757d07ee9c2bb",
    },
    {
        "path": "problems/2017-B4/proofs/reviewed-allD-global-v1.1.md",
        "bytes": 50352,
        "sha256": "47bc1477db5c54c0b40565460fb95a2a6a1c6da8368b054cbc9c61f1615ee14c",
    },
    {
        "path": "problems/2017-B4/proofs/reviewed-direction-coarsening-v1.1.md",
        "bytes": 9175,
        "sha256": "98c04673acdb4c59d44eb4d977f844d3f01ef27365399982e02df8cbaa4a6241",
    },
]
CORE = [
    "AGENTS.md",
    "problems/2017-B4/statement.md",
    "problems/2017-B4/reviews/coordinator-path-moment-r3-acceptance.md",
    PM9_AUTH,
    "problems/2017-B4/reviews/allD-global-acceptance.md",
    SCALAR_AUTH,
    "problems/2017-B4/reviews/coarsening-acceptance.md",
    DC_AUTH,
]
PAYLOAD_SUFFIXES = [
    "candidate-v1.md",
    "obligations-v1.md",
    "constructor-checks-v1.md",
    "issues-failures-v1.md",
    "source-audit-v1.md",
    "sources-v1.json",
    "worklog-v1.md",
    "admin-v1.py",
    "baseline-v1.json",
    "input-validation-v1.json",
]


def now():
    return datetime.now(timezone.utc).isoformat()


def source_path(rel):
    p = ROOT / rel
    if p.resolve().is_relative_to(ROOT) is False:
        raise ValueError("outside workspace")
    return p


def record(rel):
    data = source_path(rel).read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def read_json(rel):
    return json.loads(source_path(rel).read_text())


def check_record(expected):
    actual = record(expected["path"])
    assert actual == {k: expected[k] for k in ("path", "bytes", "sha256")}, expected["path"]
    return actual


def write_new(suffix, value):
    rel = PREFIX + suffix
    assert rel.startswith(PREFIX)
    with source_path(rel).open("x", encoding="utf-8") as f:
        f.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def canonical_digest(records):
    by_path = {}
    for r in records:
        if r["path"] in by_path:
            assert by_path[r["path"]] == r
        by_path[r["path"]] = r
    ordered = [by_path[p] for p in sorted(by_path)]
    data = json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()
    return len(ordered), hashlib.sha256(data).hexdigest()


def obligation_labels():
    obligations = source_path(PREFIX + "obligations-v1.md").read_text()
    checks = source_path(PREFIX + "constructor-checks-v1.md").read_text()
    expected = [f"O{i:02d}" for i in range(1, 61)]
    assert re.findall(r"^(O\d{2})\.", obligations, flags=re.M) == expected
    assert re.findall(r"^(O\d{2}) — CHECKED\.", checks, flags=re.M) == expected
    return {"whole_obligations": 60, "separate_constructor_hand_dispositions": 60}


def gather_inputs():
    records = [record(p) for p in CORE]
    records.extend(check_record(r) for r in EXACT_ACCEPTED)
    records.append(check_record(PM9_FREEZE))
    pm9 = read_json(PM9_AUTH)
    scalar = read_json(SCALAR_AUTH)
    dc = read_json(DC_AUTH)
    for auth in (pm9, scalar):
        c = check_record(auth["candidate"])
        a = check_record(auth["accepted_copy"])
        records.extend((c, a))
        assert source_path(a["path"]).read_bytes().endswith(source_path(c["path"]).read_bytes())
        assert auth["unresolved_substantive_issues"] == 0
    records.append(check_record(dc["accepted_proof"]))
    # Verify only this immediate operative PM9 frozen packet; no recursive
    # expanding historical inventory or old mathematical recertification.
    frozen = read_json(PM9_FREEZE["path"])
    records.extend(check_record(r) for r in frozen["payloads"])
    parent = read_json(PARENT["path"])
    records.append(check_record(PARENT))
    records.extend(check_record(r) for r in parent["payloads"])
    assert parent["older_plus_new_own_paths_bound_transitively"] == 854
    unique, digest = canonical_digest(records)
    summary = {
        "fingerprint_occurrences": len(records),
        "unique_paths": unique,
        "canonical_sha256": digest,
        "accepted_PM9_and_scalar_copy_suffixes_match_frozen_mains": True,
        "current_DC_accepted_body_fingerprint_verified": True,
        "PM9_ENTIRE16_frozen_files_verified": True,
        "PM9_authority_stored_history_summary_bound_only": {
            "occurrences": pm9["record_occurrences_verified"],
            "unique_paths": pm9["unique_paths_verified"],
        },
        "scalar_authority_stored_history_summary_bound_only": {
            "occurrences": scalar["record_occurrences_verified"],
            "unique_paths": scalar["unique_paths_verified"],
        },
        "own_immediate_parent_payloads_verified": len(parent["payloads"]),
        "older_own_paths_bound_transitively": 854,
        "no_unrelated_historical_mathematical_read_or_recertification_claim": True,
        "mathematical_assertions_evaluated_by_code": False,
    }
    return records, summary


def prepare():
    records, summary = gather_inputs()
    labels = obligation_labels()
    write_new("baseline-v1.json", {
        "at_utc": now(),
        "kind": "compact necessary current inputs plus immediate immutable own parent",
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_readback": None,
        "parent": PARENT,
        "summary": summary,
        "records": records,
    })
    write_new("input-validation-v1.json", {
        "at_utc": now(), "result": "PASS", **labels,
        "guard_summary": summary,
        "only_assigned_NEW_prefix_written": True,
        "mathematical_execution": False,
    })
    print(json.dumps({"mode": "prepare", "result": "PASS", **labels, **summary}))


def guard_baseline():
    baseline = read_json(PREFIX + "baseline-v1.json")
    records = [check_record(r) for r in baseline["records"]]
    unique, digest = canonical_digest(records)
    assert (len(records), unique, digest) == (
        baseline["summary"]["fingerprint_occurrences"],
        baseline["summary"]["unique_paths"], baseline["summary"]["canonical_sha256"])
    return baseline


def freeze(attested):
    assert attested, "FULL final model readback of all10 payloads required first"
    baseline = guard_baseline()
    labels = obligation_labels()
    payloads = [record(PREFIX + s) for s in PAYLOAD_SUFFIXES]
    write_new("freeze-v1.json", {
        "frozen_at_utc": now(),
        "status": "ENTIRE constructor checkpoint; candidate proof - unverified",
        "constructor": "/root/review_2022_complexity_r2",
        "constructor_excluded_from_TWO_OTHER_whole_reviews": True,
        "root_NEW_mathematical_contribution": False,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_readback": None,
        "claims": ["R10A", "R10B", "R10C", "R10D", "R10E"],
        **labels,
        "ENTIRE_files_including_freeze": 11,
        "immediate_own_parent": PARENT,
        "older_own_paths_bound_transitively": 854,
        "older_plus_new_own_paths_bound_transitively": 865,
        "guard_summary": baseline["summary"],
        "FULL_final_model_readback_ALL10_payloads_code_generated_metadata_attested": True,
        "FULL_manifest_model_readback_then_SEPARATE_readonly_verification_required": True,
        "mathematical_program_scan_CAS_optimizer_test_or_old_source_replay": False,
        "old_Git_shared_cache_mutation_spawn_charge_contact_bypass": False,
        "no_corresponding_NEW_SQ15_or_DR7_peer_paths_findings_hashes_metadata_accessed": True,
        "official_value_matching_lower_typical_separation_effective_R_annual_priority_claim": False,
        "authoritative_weekly_telemetry": {
            "at_utc": "2026-10-18 15:45:27 UTC",
            "method": "own same-awaited clock/get_usage_limits",
            "TOTAL_used_percent": 48, "window_minutes": 10080,
            "resetsAt": 1792874445, "ordinary_usage_allowed": True,
            "legacy_by_limit_agree": True, "account_label": "029a8928...1334ac3a",
            "TOTAL_ceiling_percent": 90, "integration_reserve": True,
            "human_authorized_current_window_only": True,
            "automatic_later_window_spending": False,
        },
        "payloads": payloads,
    })
    print(json.dumps({"mode": "freeze", "result": "PASS", "manifest": record(PREFIX + "freeze-v1.json")}))


def verify():
    manifest = read_json(PREFIX + "freeze-v1.json")
    assert len(manifest["payloads"]) == 10
    for r in manifest["payloads"]:
        check_record(r)
    guard_baseline()
    labels = obligation_labels()
    print(json.dumps({"at_utc": now(), "mode": "SEPARATE read-only verify", "result": "PASS",
                      **labels, "files_including_freeze": 11,
                      "guard_summary": manifest["guard_summary"],
                      "manifest": record(PREFIX + "freeze-v1.json"),
                      "main": record(PREFIX + "candidate-v1.md")}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "freeze", "verify"))
    parser.add_argument("--attest-final-model-readback", action="store_true")
    args = parser.parse_args()
    {"prepare": prepare, "freeze": lambda: freeze(args.attest_final_model_readback), "verify": verify}[args.mode]()
