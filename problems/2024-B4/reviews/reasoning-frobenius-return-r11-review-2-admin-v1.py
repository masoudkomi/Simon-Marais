#!/usr/bin/env python3
"""NEW FR11 review2 documentary identity only; no mathematics or old replay.

Prepare immutable input bindings; after ACTUAL full model readback freeze
the four review payloads; after ACTUAL manifest readback verify read-only.
No source/author/old executable is imported or run. No peer inventory.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/reasoning-frobenius-return-r11-review-2-"
A = "problems/2024-B4/notes/reasoning-frobenius-return-r11-"
AFREEZE = A + "freeze-v1.json"
AFID = (3460, "90ba8a8a0d07918bc738696b9619cef07b3577c85af5fea82766f322c6af2e38")
AMID = (14297, "a74932fc593ccb7ed8ae08992a60b6d8bf77548ef04b44104fea682c74616740")
PARENT = "problems/2022-B4/notes/reasoning-collision-return-r10-freeze-v1.json"
PID = (2891, "63f7e02fde4454421e66126bd4ba8decdd23c7dfe24367bed2f132710d30d4f4")
FR10 = "problems/2024-B4/reviews/reasoning-frobenius-return-r10-acceptance.json"
F10ID = (27940, "ce9a3c9e00ce931716fe00d6ea0a605167ddf58a29779d459a62cbc9dd04d173")
HUMAN = ["initial-v1.md", "sources-v1.json", "admin-v1.py"]
PAYLOAD = HUMAN + ["baseline-v1.json"]
MANIFEST = P + "manifest-v1.json"


def stamp():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert not path.startswith("problems/2024-B4/reviews/reasoning-frobenius-return-r11-review-1-")
    assert not path.startswith("problems/2024-B4/notes/coordinator-tensor-return-r12-")
    assert not path.startswith("problems/2024-B4/reviews/coordinator-tensor-return-r12-")
    target = (ROOT / path).resolve()
    assert target.is_relative_to(ROOT)
    return target.read_bytes()


def obj(path):
    return json.loads(raw(path))


def rec(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def match(row):
    assert set(row) == {"path", "bytes", "sha256"}
    assert rec(row["path"]) == row, "Changed frozen document: " + row["path"]
    return row


def fixed(path, ident):
    return match({"path": path, "bytes": ident[0], "sha256": ident[1]})


def summary(rows):
    unique = {}
    for row in rows:
        if row["path"] in unique:
            assert unique[row["path"]] == row
        unique[row["path"]] = row
    data = json.dumps([unique[p] for p in sorted(unique)], sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(unique),
            "canonical_sha256": hashlib.sha256(data).hexdigest()}


def inputs():
    af = fixed(AFREEZE, AFID)
    frozen = obj(AFREEZE)
    assert frozen["ENTIRE_files"] == 13 and frozen["whole_obligations"] == 48
    author = [af] + [match(r) for r in frozen["payload_records"]]
    assert len(author) == 13
    fixed(A + "candidate-v1.md", AMID)
    base = obj(A + "baseline-v1.json")
    guard = [match(r) for r in base["direct_operative_and_comparison_records"]]
    aparent = match(base["immediate_own_parent"])
    aparent_rows = [aparent] + [match(r) for r in obj(aparent["path"])["payload_records"]]
    assert summary(aparent_rows) == base["parent_payload_binding_compact"]
    guard += aparent_rows
    assert summary(guard) == base["all_guard_summary"] == frozen["all_guard_summary"]
    validation = obj(A + "input-validation-v1.json")
    assert validation["all_declared_fingerprints_match"] is True
    assert validation["all_guard_summary"] == summary(guard)
    assert validation["literal_checks"]["whole_obligation_labels"] == 48
    for suffix in ["sources-v1.json", "metadata-v1.json"]:
        obj(A + suffix)
    accepted = obj(FR10)
    abody = match(accepted["accepted_copy"])
    assert (abody["bytes"], abody["sha256"]) == F10ID
    acandidate = match(accepted["candidate"])
    assert raw(abody["path"]).endswith(raw(acandidate["path"]))
    extras = [rec("problems/2024-B4/reviews/reasoning-cofactor-return-r6-acceptance.md"),
              rec("problems/2024-B4/reviews/reasoning-cofactor-return-r6-acceptance.json")]
    for part in ["r6", "r7", "r8", "r9"]:
        authority = obj("problems/2024-B4/reviews/reasoning-cofactor-return-" + part + "-acceptance.json")
        extras.append(match(authority["accepted_copy"]))
    parent = fixed(PARENT, PID)
    po = obj(PARENT)
    assert po["older_plus_new_own_paths_bound_transitively"] == 980
    parent_rows = [parent] + [match(r) for r in po["payloads"]]
    assert len(parent_rows) == 8
    return author, guard, extras, parent_rows


def labels():
    author = raw(A + "obligations-v1.md").decode()
    report = raw(P + "initial-v1.md").decode()
    expected = [f"FR11-{i:02d}" for i in range(1, 49)]
    assert re.findall(r"^\|(FR11-\d{2})\|", author, re.M) == expected
    assert re.findall(r"^\|(FR11-\d{2})\|PASS[^|]*\|", report, re.M) == expected
    notes = re.findall(r"^\|(FR11R2-N\d+)\|CLOSED", report, re.M)
    assert notes == [f"FR11R2-N{i}" for i in range(1, 11)]
    source = obj(P + "sources-v1.json")
    assert source["whole_obligations"] == 48
    assert source["independent_effective_readback"] is None
    assert source["reviewer_NEW_construction_contribution"] is False
    assert source["corresponding_NEW_FR11_peer_finding_file_actualinventory_hash_metadata_commentary_accessed"] is False
    return {"author_literal_obligations": 48, "review_literal_dispositions": 48,
            "review_closed_scope_notes": 10, "mathematical_truth_checked_by_code": False}


def create(suffix, value):
    with (ROOT / (P + suffix)).open("xb") as stream:
        stream.write((json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode())


def prepare():
    author, guard, extras, parent = inputs()
    checked = labels()
    rows = author + guard + extras + parent
    create("baseline-v1.json", {"prepared_utc": stamp(),
        "author_ENTIRE13_records": author, "author_compact_guard_summary": summary(guard),
        "additional_current_comparison_records": extras,
        "own_immediate_parent": parent[0], "own_parent_payload_summary": summary(parent),
        "all_current_necessary_guard_summary": summary(rows),
        "older_own_paths_bound_transitively": 980,
        "older_plus_NEW5_own_paths_bound_transitively": 985,
        "accepted_FR10_candidate_suffix_identical": True,
        "metadata_only_comparison_body_fingerprints_not_fresh_proof_reads": True,
        "literal_checks": checked,
        "source_raw_PDF_binary_hashes": None,
        "NEW_peer_access": False, "growing_historical_inventory_recopied": False})
    print(json.dumps({"NEW_documentary_prepare": "PASS", "guard": summary(rows), **checked}))


def check():
    author, guard, extras, parent = inputs()
    baseline = obj(P + "baseline-v1.json")
    assert author == baseline["author_ENTIRE13_records"]
    assert summary(guard) == baseline["author_compact_guard_summary"]
    assert extras == baseline["additional_current_comparison_records"]
    assert parent[0] == baseline["own_immediate_parent"]
    assert summary(parent) == baseline["own_parent_payload_summary"]
    assert summary(author + guard + extras + parent) == baseline["all_current_necessary_guard_summary"]
    assert labels() == baseline["literal_checks"]
    return baseline


def freeze(readback):
    assert readback, "ACTUAL FULL final MODEL readback of ALL4 payloads must finish first"
    base = check()
    payload = [rec(P + suffix) for suffix in PAYLOAD]
    create("manifest-v1.json", {"frozen_utc": stamp(),
        "role": "OTHER initially blind ENTIRE WHOLE2 of NEW FR11A-D",
        "reviewer": "/root/review_2022_complexity_r2", "constructor_excluded": True,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_readback": None,
        "whole_obligations": 48, "ENTIRE_files_including_manifest": 5,
        "payload_records": payload,
        "author_main": fixed(A + "candidate-v1.md", AMID), "author_freeze": fixed(AFREEZE, AFID),
        "all_current_necessary_guard_summary": base["all_current_necessary_guard_summary"],
        "own_immediate_parent": base["own_immediate_parent"],
        "older_own_paths_bound_transitively": 980, "older_plus_NEW5_own_paths_bound_transitively": 985,
        "literal_checks": base["literal_checks"],
        "FULL_final_MODEL_ALL4_payload_readback_completed": True,
        "FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required": True,
        "corresponding_NEW_peer_access": False,
        "findings_EMBARGO_until_explicit_BOTH_ENTIRE": True,
        "old_shared_Git_cache_mutation_mathematical_program_CAS_scan_test_replay": False,
        "weekly": obj(P + "sources-v1.json")["weekly"]})
    print(json.dumps({"NEW_documentary_freeze": "PASS", "ENTIRE_files": 5,
                      "whole_obligations": 48, "report": payload[0], "manifest": rec(MANIFEST)}))


def verify():
    baseline = check()
    frozen = obj(MANIFEST)
    assert [r["path"] for r in frozen["payload_records"]] == [P + suffix for suffix in PAYLOAD]
    for row in frozen["payload_records"]:
        match(row)
    assert frozen["all_current_necessary_guard_summary"] == baseline["all_current_necessary_guard_summary"]
    assert frozen["FULL_final_MODEL_ALL4_payload_readback_completed"] is True
    assert frozen["corresponding_NEW_peer_access"] is False
    print(json.dumps({"SEPARATE_readonly_verified_utc": stamp(), "PASS": True,
        "ENTIRE_files": 5, "whole_obligations": 48,
        "report": rec(P + "initial-v1.md"), "manifest": rec(MANIFEST),
        "all_current_necessary_guard_summary": baseline["all_current_necessary_guard_summary"],
        "mathematical_truth_checked_by_code": False, "write_performed": False}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["prepare", "freeze", "verify"])
    parser.add_argument("--full-model-readback", action="store_true")
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    elif args.mode == "freeze":
        freeze(args.full_model_readback)
    else:
        verify()
