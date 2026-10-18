#!/usr/bin/env python3
"""FR11 NEW documentary preservation only; no mathematical computation.

Only exact-path bytes/SHA/JSON and literal labels are checked. Never run
author/old scripts. Actual FULL MODEL readback is a separate human-model
step required before freeze, followed by SEPARATE read-only verification.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/notes/reasoning-frobenius-return-r11-"
PARENT = "problems/2020-B4/reviews/reasoning-class-return-sq17-review-1-manifest-v1.json"
PARENT_ID = (2345, "7e65b63a7bb91ffa33d5a4be2312b904761c49bda7496aec8ac2c2717ad993a4")
AUTHORITY = "problems/2024-B4/reviews/reasoning-frobenius-return-r10-acceptance.json"
FR10_ID = (27940, "ce9a3c9e00ce931716fe00d6ea0a605167ddf58a29779d459a62cbc9dd04d173")
HUMAN = ["candidate-v1.md", "obligations-v1.md", "issues-v1.md", "failures-v1.md",
         "sources-v1.md", "sources-v1.json", "worklog-v1.md", "code-v1.md", "integrity-v1.py"]
GENERATED = ["baseline-v1.json", "input-validation-v1.json", "metadata-v1.json"]
FREEZE = PREFIX + "freeze-v1.json"


def stamp():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    target = (ROOT / path).resolve()
    assert target.is_relative_to(ROOT)
    return target.read_bytes()


def obj(path):
    return json.loads(raw(path))


def record(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def match(row):
    assert set(row) == {"path", "bytes", "sha256"}
    assert record(row["path"]) == row, "Changed immutable input: " + row["path"]
    return row


def fixed(path, identity):
    return match({"path": path, "bytes": identity[0], "sha256": identity[1]})


def summary(rows):
    unique = {}
    for row in rows:
        if row["path"] in unique:
            assert unique[row["path"]] == row
        unique[row["path"]] = row
    serial = json.dumps([unique[p] for p in sorted(unique)], sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(unique), "canonical_sha256": hashlib.sha256(serial).hexdigest()}


def create(suffix, data):
    path = PREFIX + suffix
    with (ROOT / path).open("xb") as stream:
        stream.write((json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode())


def labels():
    text = raw(PREFIX + "obligations-v1.md").decode()
    found = re.findall(r"^\|(FR11-\d{2})\|", text, re.M)
    assert found == [f"FR11-{i:02d}" for i in range(1, 49)]
    main = raw(PREFIX + "candidate-v1.md").decode()
    for claim in ["FR11A", "FR11B", "FR11C", "FR11D"]:
        assert "**" + claim in main
    source = obj(PREFIX + "sources-v1.json")
    assert source["constructor_excluded"] is True
    assert source["independent_effective_readback"] is None
    assert source["root_NEW_math_inference"] is False
    return {"whole_obligation_labels": 48, "claims": ["FR11A", "FR11B", "FR11C", "FR11D"],
            "mathematical_truth_checked_by_code": False}


def inputs():
    rows = [fixed("AGENTS.md", (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff")),
            record("problems/2024-B4/statement.md")]
    authority = obj(AUTHORITY)
    accepted = match(authority["accepted_copy"])
    assert (accepted["bytes"], accepted["sha256"]) == FR10_ID
    candidate = match(authority["candidate"])
    assert raw(accepted["path"]).endswith(raw(candidate["path"]))
    frozen = match(authority["verification_metadata"][0])
    rows += [accepted, record(AUTHORITY), record("problems/2024-B4/reviews/reasoning-frobenius-return-r10-acceptance.md"), candidate, frozen]
    for stem in ["reasoning-cofactor-return-r7", "reasoning-cofactor-return-r8", "reasoning-cofactor-return-r9"]:
        base = "problems/2024-B4/reviews/" + stem + "-acceptance"
        rows += [record(base + ".md"), record(base + ".json")]
    parent = fixed(PARENT, PARENT_ID)
    parent_obj = obj(PARENT)
    assert len(parent_obj["payload_records"]) == 6
    parent_rows = [parent] + [match(row) for row in parent_obj["payload_records"]]
    return rows, parent_rows


def prepare():
    rows, parent = inputs()
    checks = labels()
    create("baseline-v1.json", {"prepared_utc": stamp(), "direct_operative_and_comparison_records": rows,
                               "immediate_own_parent": parent[0], "parent_payload_binding_compact": summary(parent),
                               "all_guard_summary": summary(rows + parent),
                               "accepted_FR10_suffix_identical_to_candidate": True,
                               "new_peer_FR11_access": False, "growing_ancestry_recopied": False})
    create("input-validation-v1.json", {"checked_utc": stamp(), "all_declared_fingerprints_match": True,
                                       "all_guard_summary": summary(rows + parent), "literal_checks": checks,
                                       "scope": "Documentary identity only; no mathematical count, field or polynomial evaluation"})
    create("metadata-v1.json", {"created_utc": stamp(), "status": "candidate proof - unverified",
                               "constructor": "/root/review_2017_coarsening_r1", "constructor_excluded": True,
                               "OTHER_initially_blind_ENTIRE_whole_audits_required": 2,
                               "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
                               "independent_effective_readback": None, "root_NEW_math_inference": False,
                               "whole_obligations": 48, "claims": checks["claims"],
                               "ENTIRE_payloads": 12, "ENTIRE_files_with_freeze": 13,
                               "immediate_own_parent": parent[0], "all_guard_summary": summary(rows + parent),
                               "mathematical_program_CAS_scan_test_old_replay": False,
                               "pending_native_math_child_retrieval_approval": False,
                               "Git_shared_old_cache_mutation_spawn_charge_contact_bypass": False,
                               "annual_converse_priority_or_external_validation_claim": False,
                               "weekly": obj(PREFIX + "sources-v1.json")["weekly"],
                               "FULL_final_MODEL_ALL12_readback_required_before_freeze": True,
                               "FULL_freeze_readback_then_SEPARATE_readonly_verify_required": True})
    print(json.dumps({"prepare": "PASS", "all_guard_summary": summary(rows + parent), **checks}, indent=2))


def check():
    rows, parent = inputs()
    baseline = obj(PREFIX + "baseline-v1.json")
    assert rows == baseline["direct_operative_and_comparison_records"]
    assert parent[0] == baseline["immediate_own_parent"]
    assert summary(parent) == baseline["parent_payload_binding_compact"]
    assert summary(rows + parent) == baseline["all_guard_summary"]
    labels()
    return baseline


def freeze(readback):
    assert readback, "Actual FULL final model readback of ALL12 payloads must complete first"
    baseline = check()
    payloads = [record(PREFIX + s) for s in HUMAN + GENERATED]
    create("freeze-v1.json", {"frozen_utc": stamp(), "status": "candidate proof - unverified",
                              "constructor": "/root/review_2017_coarsening_r1", "constructor_excluded": True,
                              "OTHER_whole_audits_required": 2, "whole_obligations": 48,
                              "payload_records": payloads, "ENTIRE_files": 13,
                              "all_guard_summary": baseline["all_guard_summary"],
                              "immediate_own_parent": baseline["immediate_own_parent"],
                              "root_NEW_math_inference": False,
                              "FULL_final_MODEL_ALL12_payload_readback_completed": True,
                              "FULL_freeze_readback_then_SEPARATE_readonly_verify_required": True,
                              "mathematical_program": False, "old_shared_Git_cache_bytes_changed": False,
                              "new_peer_FR11_findings_files_inventory_hash_metadata_accessed": False})
    print(json.dumps({"freeze": record(FREEZE), "main": payloads[0], "ENTIRE_files": 13}, indent=2))


def verify():
    baseline = check()
    frozen = obj(FREEZE)
    assert [r["path"] for r in frozen["payload_records"]] == [PREFIX + s for s in HUMAN + GENERATED]
    for row in frozen["payload_records"]:
        match(row)
    assert frozen["all_guard_summary"] == baseline["all_guard_summary"]
    for suffix in ["sources-v1.json"] + GENERATED + ["freeze-v1.json"]:
        obj(PREFIX + suffix)
    print(json.dumps({"SEPARATE_readonly_verified_utc": stamp(), "PASS": True,
                      "ENTIRE_files": 13, "whole_obligations": 48,
                      "all_guard_summary": baseline["all_guard_summary"],
                      "main": record(PREFIX + "candidate-v1.md"), "freeze": record(FREEZE),
                      "mathematical_truth_checked_by_code": False}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["prepare", "freeze", "verify"])
    parser.add_argument("--model-readback-complete", action="store_true")
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    elif args.mode == "freeze":
        freeze(args.model_readback_complete)
    else:
        verify()
