#!/usr/bin/env python3
"""NEW R21 reviewer2 documentary admin only; no mathematical computation.

Prepare creates one NEW baseline. Freeze follows actual FULL final MODEL
readback. A SEPARATE verify invocation is strictly read-only. No old or
shared file is written, and no corresponding NEW peer path is inventoried.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import argparse

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/reviews/reasoning-center-return-r21-review-2-"
AUTHOR = "problems/2021-B4/notes/reasoning-center-return-r21-"
AUTHOR_FREEZE = AUTHOR + "freeze-v1.json"
AUTHOR_ID = (3823, "04ea7e21dc8ace2654acdbda4b3c67973c49218d358aff6d80edfc46842d48fd")
MAIN = AUTHOR + "candidate-v1.md"
MAIN_ID = (15374, "27b372d98923309d2253cc491c641ab293ce10428d9b5e24589b1f2959399094")
PARENT = "problems/2020-B4/notes/reasoning-class-return-sq16-freeze-v1.json"
PARENT_ID = (4322, "29ed9edd4cea75a4248b9661f06518649c97e122c437262c4c7dd32750847087")
PAYLOADS = ["report-v1.md", "sources-v1.json", "admin-v1.py", "baseline-v1.json"]
BASELINE = PREFIX + "baseline-v1.json"
MANIFEST = PREFIX + "manifest-v1.json"
REQUESTED = {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True}


def stamp():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    target = (ROOT / path).resolve()
    assert target.is_relative_to(ROOT)
    return target.read_bytes()


def record(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def obj(path):
    return json.loads(raw(path))


def match(item):
    assert set(item) == {"path", "bytes", "sha256"}
    assert record(item["path"]) == item, "Changed input: " + item["path"]
    return item


def fixed(path, identity):
    return match({"path": path, "bytes": identity[0], "sha256": identity[1]})


def summary(rows):
    unique = {}
    for row in rows:
        if row["path"] in unique:
            assert row == unique[row["path"]]
        unique[row["path"]] = row
    data = json.dumps([unique[path] for path in sorted(unique)], sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(unique), "canonical_sha256": hashlib.sha256(data).hexdigest()}


def create(path, data):
    assert path.startswith(PREFIX)
    encoded = (json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode()
    with (ROOT / path).open("xb") as stream:
        stream.write(encoded)


def label_checks():
    text = raw(PREFIX + "report-v1.md").decode()
    ids = re.findall(r"^\|(R21-\d{2})\|", text, re.M)
    assert ids == [f"R21-{n:02d}" for n in range(1, 49)]
    notes = re.findall(r"^\|(R21R2-N\d+)\|", text, re.M)
    assert notes == [f"R21R2-N{n}" for n in range(1, 11)]
    source = obj(PREFIX + "sources-v1.json")
    assert source["independent_effective_readback"] is None
    assert source["nonconstructor"] is True
    assert source["independent_hand_dispositions"] == 48
    return {"whole_disposition_labels": 48, "closed_scope_note_labels": 10,
            "mathematical_truth_checked_by_code": False}


def inputs():
    frozen = obj(AUTHOR_FREEZE)
    author_rows = [fixed(AUTHOR_FREEZE, AUTHOR_ID)]
    assert len(frozen["payloads"]) == 14
    for item in frozen["payloads"]:
        assert item["path"].startswith(AUTHOR)
        author_rows.append(match(item))
    assert fixed(MAIN, MAIN_ID) in author_rows
    author_baseline = obj(AUTHOR + "baseline-v1.json")
    assert len(author_baseline["rows"]) == 38
    declared = [match(item) for item in author_baseline["rows"]]
    assert summary(declared)["unique_paths"] == 38

    direct = author_rows + [
        fixed("AGENTS.md", (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff")),
        record("problems/2021-B4/statement.md"),
        record("problems/2021-B4/notes/coordinator-frame-III-exploration-r1.md"),
        record("problems/2021-B4/notes/reasoning-center-return-r18-failures-v1.md")]
    authority_bindings = []
    for index in [18, 20]:
        authority_path = f"problems/2021-B4/reviews/reasoning-center-return-r{index}-acceptance.json"
        authority = obj(authority_path)
        direct.extend([record(authority_path),
                       record(f"problems/2021-B4/reviews/reasoning-center-return-r{index}-acceptance.md"),
                       match(authority["accepted_copy"])])
        candidate = match(authority["candidate"])
        assert raw(authority["accepted_copy"]["path"]).endswith(raw(candidate["path"]))
        authority_bindings.append({"immutable_current_authority": record(authority_path),
                                   "accepted_copy": authority["accepted_copy"],
                                   "candidate_suffix_byte_identical": True,
                                   "current_body_and_EACH_authority_MD_JSON_fresh_COMPLETE_read": True,
                                   "historical_root_verified_occurrences": authority["record_occurrences_verified"],
                                   "historical_root_verified_unique_paths": authority["unique_paths_verified"],
                                   "historical_inventory_not_recopied_or_independently_recertified": True})

    parent = obj(PARENT)
    parent_rows = [fixed(PARENT, PARENT_ID)]
    assert len(parent["payloads"]) == 11
    parent_rows.extend(match(item) for item in parent["payloads"])
    assert parent["older_plus_new_own_paths_bound_transitively"] == 944
    direct.append(parent_rows[0])
    all_checked = direct + declared + parent_rows
    return {"direct": direct, "author_declared": declared,
            "parent_rows": parent_rows, "all_checked_summary": summary(all_checked),
            "authority_bindings": authority_bindings,
            "author_baseline_identity": record(AUTHOR + "baseline-v1.json")}


def prepare():
    assert not (ROOT / MANIFEST).exists()
    data = inputs()
    checks = label_checks()
    create(BASELINE, {"prepared_at_utc": stamp(),
                      "scope": "Entire current author packet, necessary operative authorities and compact immutable own parent; no growing ancestry inventory",
                      "records": data["direct"], "direct_guard_summary": summary(data["direct"]),
                      "author_baseline_identity": data["author_baseline_identity"],
                      "author_baseline_38_declarations_checked_bound_not_recopied": summary(data["author_declared"]),
                      "immediate_own_parent": record(PARENT),
                      "own_parent11_payloads_checked_bound_not_recopied": summary(data["parent_rows"]),
                      "all_checked_summary": data["all_checked_summary"],
                      "current_authorities": data["authority_bindings"],
                      "older_own_paths_bound_transitively": 944,
                      "older_plus_new5_own_paths_bound_transitively": 949,
                      "literal_checks": checks,
                      "no_NEW_corresponding_peer_access": True,
                      "requested": REQUESTED, "independent_effective_readback": None,
                      "weekly": {"method": "coordinator authoritative meter", "TOTAL_used_percent": 58,
                                  "resetsAt": 1792874445, "TOTAL_ceiling_percent": 90,
                                  "integration_reserve": True, "automatic_later_window_spending": False},
                      "no_mathematical_program_or_old_source_author_freezer_replay": True})
    print(json.dumps({"prepare": "PASS", "author_ENTIRE_files": 15,
                      "all_checked_summary": data["all_checked_summary"], **checks}, indent=2))


def check_baseline():
    base = obj(BASELINE)
    for item in base["records"]:
        match(item)
    assert summary(base["records"]) == base["direct_guard_summary"]
    data = inputs()
    assert data["all_checked_summary"] == base["all_checked_summary"]
    assert data["author_baseline_identity"] == base["author_baseline_identity"]
    return base


def freeze(readback):
    assert readback, "Actually complete FULL final MODEL readback first"
    baseline = check_baseline()
    checks = label_checks()
    payload = [record(PREFIX + suffix) for suffix in PAYLOADS]
    create(MANIFEST, {"frozen_at_utc": stamp(),
                      "role": "OTHER initially blind ENTIRE WHOLE2 initial; findings embargoed",
                      "reviewer": "/root/review_2022_complexity_r2", "nonconstructor": True,
                      "NEW_contributors_excluded": ["/root/review_2021_reasoning_j15_r2", "/root"],
                      "target": fixed(MAIN, MAIN_ID), "author_freeze": fixed(AUTHOR_FREEZE, AUTHOR_ID),
                      "author_ENTIRE_files_read": 15, "whole_obligations": 48,
                      "separate_hand_dispositions": 48, "closed_scope_notes": 10,
                      "ENTIRE_review_files_including_manifest": 5,
                      "requested": REQUESTED, "independent_effective_readback": None,
                      "FULL_final_MODEL_readback_ALL4_payloads_code_generated_metadata_completed": True,
                      "FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required": True,
                      "all_checked_summary": baseline["all_checked_summary"],
                      "immediate_own_parent": record(PARENT),
                      "older_own_paths_bound_transitively": 944,
                      "older_plus_new_own_paths_bound_transitively": 949,
                      "no_NEW_corresponding_peer_finding_file_actual_inventory_hash_metadata_commentary_access": True,
                      "findings_embargoed_until_explicit_BOTH_ENTIRE_confirmation": True,
                      "literal_checks": checks,
                      "no_mathematical_program_CAS_scan_test_source_author_old_replay": True,
                      "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
                      "weekly": baseline["weekly"], "payloads": payload})
    print(json.dumps({"manifest": record(MANIFEST), "report": payload[0], "ENTIRE_files": 5}, indent=2))


def verify():
    baseline = check_baseline()
    frozen = obj(MANIFEST)
    assert len(frozen["payloads"]) == 4
    assert [x["path"] for x in frozen["payloads"]] == [PREFIX + x for x in PAYLOADS]
    for item in frozen["payloads"]:
        match(item)
    label_checks()
    assert frozen["all_checked_summary"] == baseline["all_checked_summary"]
    print(json.dumps({"SEPARATE_readonly_verify_at_utc": stamp(), "PASS": True,
                      "ENTIRE_files": 5, "whole_obligations": 48,
                      "all_checked_summary": baseline["all_checked_summary"],
                      "report": record(PREFIX + "report-v1.md"), "manifest": record(MANIFEST),
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
