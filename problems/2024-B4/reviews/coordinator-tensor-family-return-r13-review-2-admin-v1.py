#!/usr/bin/env python3
"""NEW R13 review2 documentary close only, never mathematical computation.

Only exact declared immutable paths are read. No peer inventory, old helper
execution, finite field/gcd/polynomial calculation or test occurs. Actual
FULL final MODEL ALL4 payload readback precedes freeze; full manifest
MODEL readback precedes a SEPARATE read-only verify call.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/coordinator-tensor-family-return-r13-review-2-"
A = "problems/2024-B4/notes/coordinator-tensor-family-return-r13-"
AF = A + "freeze-v1.json"
MAIN = A + "candidate-v1.md"
BASE = P + "baseline-v1.json"
MAN = P + "manifest-v1.json"
PARENT = "problems/2020-B4/notes/reasoning-actual-return-r18-freeze-v1.json"
PAYLOADS = [P + "initial-v1.md", P + "sources-v1.json", P + "admin-v1.py", BASE]
FIXED = {
    MAIN: (18156, "49b85dd188405691ca9146c27659130c0f1606015b31d22a753426a6891335f9"),
    AF: (1327, "43ca5babe90e2dcc1638273f9ce67a3fee21fc30b9d720968a80d5dadcd4123a"),
    PARENT: (2747, "564db489529aa7030df95abbd6461fe82a5e1acf32d4499838f3472c6ae7e9be"),
}
AUTHORITIES = [
    "problems/2024-B4/reviews/coordinator-tensor-return-r12-acceptance.json",
    "problems/2024-B4/reviews/reasoning-frobenius-return-r10-acceptance.json",
]


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def safe(path):
    assert isinstance(path, str) and not path.startswith("/")
    assert ".." not in Path(path).parts
    assert "coordinator-tensor-family-return-r13-review-1-" not in path
    return ROOT / path


def record(path):
    data = safe(path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked(rec):
    assert record(rec["path"]) == rec, rec["path"]
    return rec


def read_json(path):
    return json.loads(safe(path).read_text())


def summary(records):
    raw = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(records),
            "unique_paths": len({r["path"] for r in records}),
            "canonical_sha256": hashlib.sha256(raw).hexdigest()}


def exclusive_json(path, value):
    assert path.startswith(P)
    with safe(path).open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def inputs():
    for path, (size, sha) in FIXED.items():
        assert record(path) == {"path": path, "bytes": size, "sha256": sha}
    author = read_json(AF)
    assert author["whole_obligations"] == 32 and len(author["payloads"]) == 4
    author_records = [checked(r) for r in author["payloads"]] + [record(AF)]
    old = read_json(A + "baseline-v1.json")
    inputs_declared = [checked(r) for r in old["input_records"]]
    assert len(inputs_declared) == 9
    assert read_json(A + "sources-v1.json")["input_records"] == old["input_records"]
    extras = []
    for path in AUTHORITIES:
        authority = read_json(path)
        accepted = checked(authority["accepted_copy"])
        candidate = checked(authority["candidate"])
        assert safe(accepted["path"]).read_bytes().endswith(safe(candidate["path"]).read_bytes())
        first = authority["verification_metadata"][0]
        assert "freeze" in first["path"]
        extras += [candidate, checked(first)]
    parent = read_json(PARENT)
    assert parent["older_plus_NEW5_own_paths_bound_transitively"] == 1000
    parent_records = [checked(r) for r in parent["payload_records"]] + [record(PARENT)]
    assert len(parent_records) == 5
    # Immutable parent payloads bound only; do not rerun its older input guards
    # or confuse permitted coordinator living-map updates with proof mutation.
    records = author_records + inputs_declared + extras + parent_records
    return author_records, inputs_declared, extras, parent_records, records


def labels():
    expected = [f"R13-O{i:02d}" for i in range(1, 33)]
    author_ids = re.findall(r"^\|(R13-O\d\d)\|", safe(MAIN).read_text(), re.M)
    assert author_ids == expected
    text = safe(P + "initial-v1.md").read_text()
    own_ids = re.findall(r"^\|(R13-O\d\d)\|PASS[^|]*\|", text, re.M)
    assert own_ids == expected
    notes = re.findall(r"^\|R13R2-N(\d+)\|CLOSED", text, re.M)
    assert notes == [str(i) for i in range(1, 11)]
    src = read_json(P + "sources-v1.json")
    assert src["whole_obligations"] == 32 and src["closed_scope_notes"] == 10
    assert src["substantive_defects"] == 0 and src["required_author_repairs"] == 0
    assert src["corresponding_NEW_peer_finding_file_actualinventory_hash_metadata_commentary_accessed"] is False
    return {"author_literal_obligations": 32, "review_literal_dispositions": 32,
            "closed_scope_notes": 10, "mathematical_truth_checked_by_code": False}


def prepare():
    ars, direct, extras, parent_records, records = inputs()
    value = {
        "prepared_utc": now(), "scope": "NEW documentary preservation only",
        "author_ENTIRE_records": ars,
        "author_necessary_input_baseline": record(A + "baseline-v1.json"),
        "author_declared9_input_summary": summary(direct),
        "all_declared9_verified_including_exploration": True,
        "current_accepted_candidate_and_freeze_records": extras,
        "own_immediate_parent": record(PARENT),
        "own_parent_ENTIRE5_summary": summary(parent_records),
        "older_own_paths_bound_transitively": 1000,
        "older_plus_NEW5_own_paths_bound_transitively": 1005,
        "all_guard_summary": summary(records), "literal_checks": labels(),
        "historical_inventory_copied_or_old_code_executed": False,
        "mutable_living_maps_observed_not_strict_immutable_guards": [],
        "source_read_scopes": "full report Section7 and structured source JSON; not inferred from documentary fingerprints",
        "corresponding_NEW_peer_access": False,
        "weekly": {"authority": "root direct telemetry received",
                   "at_utc": "2026-10-18 22:45:30 UTC", "TOTAL_used_percent": 67,
                   "resetsAt": 1792874445, "TOTAL_ceiling": 90,
                   "integration_reserve": True, "automatic_later_window_spending": False}}
    exclusive_json(BASE, value)
    print(json.dumps({"prepared": record(BASE), "guard_summary": summary(records),
                      "literal_checks": value["literal_checks"]}, indent=2))


def freeze(full_model_readback):
    assert full_model_readback, "Actual FULL final MODEL ALL4 payload readback must precede freeze"
    _, _, _, _, records = inputs()
    baseline = read_json(BASE)
    assert baseline["all_guard_summary"] == summary(records)
    value = {
        "frozen_utc": now(), "role": "OTHER initially blind ENTIRE WHOLE2 R13A-D",
        "reviewer": "/root/review_2022_complexity_r2",
        "NEW_root_and_C_contributors_excluded": True,
        "whole_obligations": 32, "ENTIRE_files": 5,
        "payload_records": [record(path) for path in PAYLOADS],
        "author_main": record(MAIN), "author_freeze": record(AF),
        "all_guard_summary": summary(records), "own_immediate_parent": record(PARENT),
        "older_own_paths_bound_transitively": 1000,
        "older_plus_NEW5_own_paths_bound_transitively": 1005,
        "literal_checks": labels(),
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "effective_readback": None,
        "FULL_final_MODEL_ALL4_payload_readback_completed": True,
        "FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required": True,
        "corresponding_NEW_peer_access": False,
        "findings_EMBARGO_until_explicit_BOTH_ENTIRE": True,
        "mathematical_program_CAS_scan_test_source_author_old_replay": False,
        "Git_shared_old_cache_mutation_spawn_charge_contact_bypass": False,
        "weekly": baseline["weekly"]}
    exclusive_json(MAN, value)
    print(json.dumps({"frozen": record(MAN), "utc": value["frozen_utc"],
                      "ENTIRE_files": 5, "whole_obligations": 32}, indent=2))


def verify():
    value = read_json(MAN)
    assert value["ENTIRE_files"] == 5 and value["whole_obligations"] == 32
    assert [r["path"] for r in value["payload_records"]] == PAYLOADS
    for rec in value["payload_records"]:
        checked(rec)
    _, _, _, _, records = inputs()
    assert value["all_guard_summary"] == summary(records)
    assert value["literal_checks"] == labels()
    print(json.dumps({"verified_utc": now(), "status": "PASS",
                      "ENTIRE_files": 5, "whole_obligations": 32,
                      "guard_summary": summary(records), "manifest": record(MAN),
                      "report": record(P + "initial-v1.md"), "read_only": True,
                      "mathematical_program": False}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "freeze", "verify"))
    parser.add_argument("--full-model-readback", action="store_true")
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    elif args.mode == "freeze":
        freeze(args.full_model_readback)
    else:
        verify()
