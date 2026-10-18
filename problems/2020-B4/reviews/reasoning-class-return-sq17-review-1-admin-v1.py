#!/usr/bin/env python3
"""NEW SQ17 review documentary integrity only. No mathematical code.

prepare -> actual FULL model readback -> freeze -> actual manifest
readback -> SEPARATE readonly verify. Never execute author/old code.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/reviews/reasoning-class-return-sq17-review-1-"
AUTHOR = "problems/2020-B4/notes/reasoning-class-return-sq17-freeze-v1.json"
AUTHOR_ID = (3901, "d7b19f6e852178d83db1adad70e2fdb10c8dfa30d28b538e893cf1f0b567aab1")
PARENT = "problems/2017-B4/notes/reasoning-concentration-return-r12-freeze-v1.json"
PARENT_ID = (3158, "6a6e5ccccbc9c5416aeeac4240a8a4f96bc44b90167d5275e8ab2bf563c17c1c")
MAIN = PREFIX + "initial-v1.md"
HUMAN = [MAIN, PREFIX + "sources-v1.json", PREFIX + "admin-v1.py"]
GENERATED = [PREFIX + s for s in ["baseline-v1.json", "input-validation-v1.json", "metadata-v1.json"]]
MANIFEST = PREFIX + "manifest-v1.json"


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
    assert record(row["path"]) == row, "Changed input: " + row["path"]
    return row


def fixed(path, identity):
    return match({"path": path, "bytes": identity[0], "sha256": identity[1]})


def summary(rows):
    unique = {}
    for row in rows:
        if row["path"] in unique:
            assert unique[row["path"]] == row
        unique[row["path"]] = row
    data = json.dumps([unique[p] for p in sorted(unique)], sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(unique), "canonical_sha256": hashlib.sha256(data).hexdigest()}


def create(path, data):
    assert path.startswith(PREFIX)
    with (ROOT / path).open("xb") as stream:
        stream.write((json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode())


def inputs():
    author_row = fixed(AUTHOR, AUTHOR_ID)
    author = obj(AUTHOR)
    assert len(author["payloads"]) == 7
    author_rows = [author_row] + [match(row) for row in author["payloads"]]
    base = obj("problems/2020-B4/notes/reasoning-class-return-sq17-baseline-v1.json")
    declared = [match(row) for row in base["records"]]
    assert len(declared) == 12
    old_parent = obj(base["immediate_own_parent"]["path"])
    old_parent_rows = [match(base["immediate_own_parent"])] + [match(row) for row in old_parent["payloads"]]
    assert len(old_parent_rows) == 5
    assert summary(declared + old_parent_rows) == base["all_checked_summary"]
    parent_row = fixed(PARENT, PARENT_ID)
    parent = obj(PARENT)
    assert len(parent["payload_records"]) == 12
    own_parent_rows = [parent_row] + [match(row) for row in parent["payload_records"]]
    return author_rows, declared + old_parent_rows, own_parent_rows


def labels():
    text = raw(MAIN).decode()
    found = re.findall(r"^\|(SQ17-\d{2})\|", text, re.M)
    assert found == [f"SQ17-{i:02d}" for i in range(1, 41)]
    notes = re.findall(r"^\|(SQ17R1-N\d)\|CLOSED\|", text, re.M)
    assert notes == [f"SQ17R1-N{i}" for i in range(1, 9)]
    source = obj(PREFIX + "sources-v1.json")
    assert source["corresponding_NEW_peer_finding_file_inventory_hash_metadata_accessed"] is False
    assert source["root_separate_source_objection_accessed"] is False
    assert source["required_repairs"] == 0
    return {"whole_obligation_rows": 40, "closed_scope_notes": 8, "required_repairs": 0,
            "mathematical_truth_checked_by_code": False}


def prepare():
    author, declared, parent = inputs()
    rows = author + declared + parent
    checks = labels()
    create(GENERATED[0], {"prepared_utc": stamp(), "direct_author_records": author,
                         "author_declared_inputs_compact": {"baseline": record("problems/2020-B4/notes/reasoning-class-return-sq17-baseline-v1.json"), "summary": summary(declared), "all_declared_records_match": True},
                         "immediate_own_parent": parent[0], "own_parent_payloads_bound_not_recopied": summary(parent),
                         "all_guard_summary": summary(rows), "corresponding_NEW_peer_material_accessed": False,
                         "root_separate_objection_accessed": False})
    create(GENERATED[1], {"checked_utc": stamp(), "all_input_fingerprints_match": True,
                         "author_ENTIRE_files": 8, "all_guard_summary": summary(rows), "literal_labels": checks,
                         "scope": "SHA/JSON/path/label integrity only; no mathematical truth computation or author-code replay"})
    create(GENERATED[2], {"created_utc": stamp(), "reviewer": "/root/review_2017_coarsening_r1",
                         "status": "ENTIRE initially blind OTHER WHOLE1 initial; findings EMBARGOED until explicit BOTH",
                         "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
                         "independent_effective_readback": None,
                         "NEW_constructor": "/root/review_2022_complexity_r2", "reviewer_NEW_contribution": False,
                         "whole_obligations": 40, "required_repairs": 0, "closed_scope_notes": 8,
                         "old_own_roles_disclosed_not_self_recertified": True,
                         "root_separate_source_objection_accessed": False, "corresponding_NEW_peer_access": False,
                         "mathematical_program_CAS_scan_or_old_replay": False,
                         "pending_native_child_retrieval_approval": False,
                         "weekly": {"at_utc": "2026-10-18 18:39:52 UTC", "TOTAL_used_percent": 61, "window_minutes": 10080, "resetsAt": 1792874445, "ordinaryUsageAllowed": True, "ceiling_TOTAL_percent": 90, "integration_reserve": True, "automatic_later_window_authorized": False},
                         "immediate_own_parent": parent[0], "compact_preservation": True,
                         "ENTIRE_files_including_manifest": 7,
                         "FULL_final_ALL6_payload_model_readback_required_before_freeze": True,
                         "FULL_manifest_readback_then_SEPARATE_readonly_verify_required": True})
    print(json.dumps({"prepare": "PASS", "all_guard_summary": summary(rows), **checks}, indent=2))


def check():
    author, declared, parent = inputs()
    baseline = obj(GENERATED[0])
    assert author == baseline["direct_author_records"]
    assert summary(declared) == baseline["author_declared_inputs_compact"]["summary"]
    assert summary(parent) == baseline["own_parent_payloads_bound_not_recopied"]
    assert summary(author + declared + parent) == baseline["all_guard_summary"]
    labels()
    return baseline


def freeze(readback):
    assert readback, "Actual FULL final model readback must finish first"
    base = check()
    rows = [record(p) for p in HUMAN + GENERATED]
    create(MANIFEST, {"frozen_utc": stamp(), "reviewer": "/root/review_2017_coarsening_r1",
                      "status": "ENTIRE initially blind OTHER WHOLE1 initial; findings EMBARGOED until explicit BOTH",
                      "payload_records": rows, "ENTIRE_files": 7, "whole_obligations": 40,
                      "required_repairs": 0, "closed_scope_notes": 8,
                      "all_guard_summary": base["all_guard_summary"],
                      "immediate_own_parent": base["immediate_own_parent"],
                      "FULL_final_ALL6_payload_model_readback_completed": True,
                      "FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required": True,
                      "corresponding_NEW_peer_finding_file_inventory_hash_metadata_accessed": False,
                      "root_separate_source_objection_accessed": False,
                      "mathematical_program": False, "no_Git_shared_old_cache_mutation": True})
    print(json.dumps({"manifest": record(MANIFEST), "main": rows[0], "ENTIRE_files": 7}, indent=2))


def verify():
    base = check()
    manifest = obj(MANIFEST)
    assert [r["path"] for r in manifest["payload_records"]] == HUMAN + GENERATED
    for row in manifest["payload_records"]:
        match(row)
    assert manifest["all_guard_summary"] == base["all_guard_summary"]
    for path in [PREFIX + "sources-v1.json"] + GENERATED + [MANIFEST]:
        obj(path)
    print(json.dumps({"SEPARATE_readonly_verified_utc": stamp(), "PASS": True,
                      "ENTIRE_files": 7, "whole_obligations": 40,
                      "all_guard_summary": base["all_guard_summary"], "manifest": record(MANIFEST),
                      "main": record(MAIN), "mathematical_truth_checked_by_code": False}, indent=2))


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
