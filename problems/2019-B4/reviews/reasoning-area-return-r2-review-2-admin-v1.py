#!/usr/bin/env python3
"""NEW AR reviewer2 documentary admin ONLY; no mathematical operations.

Only exclusive-prefix files are created, without overwrite. No network,
subprocess, source/author/old helper or mathematical library is invoked.
Actual full MODEL readback must precede freeze; verify is separately read-only.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2019-B4/reviews/reasoning-area-return-r2-review-2-"
A = "problems/2019-B4/notes/reasoning-area-return-r2-"
AUTHOR = A + "freeze-v1.json"
AUTHOR_ID = (3299, "4aac68a1c6a818030c70066019828eee565d60bffdacb14487dd9e9c972f346d")
MAIN_ID = (20227, "e7b173d7226641e9251502c10228faab72f91ee8c61c621686f9e793fb4be18c")
PARENT = "problems/2024-B4/reviews/reasoning-frobenius-return-r10-review-2-manifest-v1.json"
PARENT_ID = (2749, "c1c6021985cb039e7059320e5107013276cae7548ecc3fda5021d49a3d33174d")
AU_ANCESTOR = "problems/2019-B4/reviews/reasoning-occupation-return-r1-review-2-baseline-v1.json"
PAYLOADS = ["initial-v1.md", "sources-v1.json", "admin-v1.py", "baseline-v1.json"]
BASELINE = P + "baseline-v1.json"
MANIFEST = P + "manifest-v1.json"
SOURCE_STEMS = ["reasoning-return-r7", "reasoning-cut-transfer-r6", "reasoning-occupation-return-r1"]
BODY_EXPECTED = {
    "reasoning-return-r7": (17727, "4fe222b8b1d89b6b3d66bb16c6a1985390d537eee55bb42bfefdb2d4821e351a"),
    "reasoning-cut-transfer-r6": (25072, "f43bd14fbec8b827dadbdbc33161e34aad3082f946a858bbf8d78880d0024ff8"),
    "reasoning-occupation-return-r1": (28991, "1fa9770945b5e1b74f6ef7e6016cdf6804a73034b17433251e9a62a2895f2004")}


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert not Path(path).is_absolute() and ".." not in Path(path).parts
    for forbidden in ["reasoning-area-return-r2-review-1-", "reasoning-frobenius-return-r10-review-1-",
                      "problems/2020-B4/reviews/reasoning-class-return-sq16-review-"]:
        assert forbidden not in path, "Embargoed NEW peer path"
    return (ROOT / path).read_bytes()


def record(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def obj(path):
    return json.loads(raw(path))


def clean(row):
    return {key: row[key] for key in ["path", "bytes", "sha256"]}


def match(row):
    item = clean(row)
    assert record(item["path"]) == item, "Changed input: " + item["path"]
    return item


def fixed(path, identity):
    return match({"path": path, "bytes": identity[0], "sha256": identity[1]})


def summary(rows):
    unique = {}
    for row in rows:
        item = clean(row)
        assert item["path"] not in unique or item == unique[item["path"]]
        unique[item["path"]] = item
    ordered = [unique[path] for path in sorted(unique)]
    data = json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(ordered),
            "canonical_deduplicated_sha256": hashlib.sha256(data).hexdigest()}


def create(path, value):
    assert path.startswith(P)
    with (ROOT / path).open("xb") as stream:
        stream.write((json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode())


def literal_checks():
    report = raw(P + "initial-v1.md").decode()
    assert re.findall(r"^\|(ARR2-\d{2})\|PASS", report, re.M) == [f"ARR2-{i:02d}" for i in range(1, 49)]
    ledger = raw(A + "obligations-v1.md").decode()
    assert re.findall(r"^\| (AR2-O\d{2}) \|", ledger, re.M) == [f"AR2-O{i:02d}" for i in range(1, 49)]
    source = obj(P + "sources-v1.json")
    assert source["NEW_AR_nonconstructor"] and source["independent_effective_readback"] is None
    assert not source["corresponding_NEW_root_AR_finding_filename_inventory_file_hash_metadata_commentary_access"]
    return {"author_obligation_labels": 48, "review_separate_whole_disposition_labels": 48,
            "mathematical_truth_checked_by_code": False}


def collect():
    author_manifest = fixed(AUTHOR, AUTHOR_ID)
    author = obj(AUTHOR)
    assert author["ENTIRE_files"] == 11 and author["whole_obligations"] == 48
    author_rows = [author_manifest] + [match(row) for row in author["payloads"]]
    assert len(author_rows) == 11
    fixed(A + "candidate-v1.md", MAIN_ID)

    # Independent byte reconstruction of compact author guards, no old code execution.
    author_base = obj(A + "baseline-v1.json")
    author_direct = [match(row) for row in author_base["direct_records"]]
    assert summary(author_direct) == author_base["direct_summary"]
    parent_id = match(author_base["parent_metadata_identity"])
    historical = obj(parent_id["path"])
    old_rows = [match(row) for row in historical["direct_records"]]
    old_rows.extend(match(row) for row in obj(AU_ANCESTOR)["records"])
    assert summary(old_rows) == historical["effective_guard_summary"] == author_base["parent_historical_guard_summary"]
    author_guards = author_direct + old_rows
    assert summary(author_guards) == author_base["effective_guard_summary"] == author["effective_guard_summary"]

    direct = [record("AGENTS.md"), fixed("problems/2019-B4/statement.md",
              (1252, "53d4201dca8bc4a77d995e3df14f95dd146e2df0c82d3b6447ad35a348e89de9"))]
    authorities = []
    for stem in SOURCE_STEMS:
        base = "problems/2019-B4/"
        path = base + "reviews/" + stem + "-acceptance.json"
        authority = obj(path)
        accepted = match(authority["accepted_copy"])
        fixed(accepted["path"], BODY_EXPECTED[stem])
        candidate = match(authority["candidate"])
        assert raw(accepted["path"]).endswith(raw(candidate["path"]))
        direct.extend([accepted, record(path), record(base + "reviews/" + stem + "-acceptance.md")])
        authorities.append({"authority": record(path), "accepted_body": accepted,
                            "immutable_candidate": candidate, "candidate_suffix_byte_identical": True})

    own_parent = fixed(PARENT, PARENT_ID)
    own = obj(PARENT)
    assert own["older_plus_new_own_paths_bound_transitively"] == 962
    own_rows = [own_parent] + [match(row) for row in own["payloads"]]
    assert len(own_rows) == 5
    return {"author_records": author_rows, "author_guard_summary": summary(author_guards),
            "author_immutable_parent_metadata": parent_id, "direct": direct,
            "authorities": authorities, "own_parent": own_parent,
            "own_parent_summary": summary(own_rows),
            "all_guard_summary": summary(author_rows + author_guards + direct + own_rows)}


def prepare():
    inputs = collect()
    literal = literal_checks()
    create(BASELINE, {"prepared_at_utc": now(), "reviewer": "/root/review_2022_complexity_r2",
                      "scope": "Compact independent documentary guards; no growing historical inventory recopy",
                      "author_ALL11_records": inputs["author_records"],
                      "author_ALL245_guard_occurrences_independently_verified_not_recopied": inputs["author_guard_summary"],
                      "author_immutable_parent_metadata": inputs["author_immutable_parent_metadata"],
                      "direct_current_inputs": inputs["direct"], "current_immutable_authorities": inputs["authorities"],
                      "own_immediate_parent": inputs["own_parent"],
                      "own_parent_ALL5_files_directly_verified_not_recopied": inputs["own_parent_summary"],
                      "all_guard_summary": inputs["all_guard_summary"],
                      "older_own_paths_bound_transitively": 962,
                      "older_plus_new5_own_paths_bound_transitively": 967,
                      "literal_checks": literal,
                      "NEW_AR_nonconstructor": True, "constructor_A_excluded": True,
                      "no_corresponding_NEW_peer_finding_filename_inventory_file_hash_metadata_access": True,
                      "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
                      "independent_effective_readback": None,
                      "ALL48_issue_sourceMD_worklog_embedded_in_report": True,
                      "ENTIRE_review_files_including_manifest": 5,
                      "no_mathprogram_CAS_scan_test_source_author_old_replay": True,
                      "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
                      "FULL_final_MODEL_readback_ALL4_then_manifest_readback_SEPARATE_verify_required": True})
    print(json.dumps({"prepare": "PASS", "all_guard_summary": inputs["all_guard_summary"], **literal}, indent=2))


def check_baseline():
    base = obj(BASELINE)
    inputs = collect()
    assert base["author_ALL11_records"] == inputs["author_records"]
    assert base["author_ALL245_guard_occurrences_independently_verified_not_recopied"] == inputs["author_guard_summary"]
    assert base["author_immutable_parent_metadata"] == inputs["author_immutable_parent_metadata"]
    assert base["direct_current_inputs"] == inputs["direct"]
    assert base["current_immutable_authorities"] == inputs["authorities"]
    assert base["own_immediate_parent"] == inputs["own_parent"]
    assert base["own_parent_ALL5_files_directly_verified_not_recopied"] == inputs["own_parent_summary"]
    assert base["all_guard_summary"] == inputs["all_guard_summary"]
    literal_checks()
    return base


def freeze(readback):
    assert readback, "FULL final ALL4 MODEL readback must actually finish before freeze"
    base = check_baseline()
    payloads = [record(P + suffix) for suffix in PAYLOADS]
    create(MANIFEST, {"frozen_at_utc": now(), "reviewer": "/root/review_2022_complexity_r2",
                      "role": "OTHER initially blind ENTIRE WHOLE2 of NEW AR1--AR4",
                      "NEW_AR_nonconstructor": True, "constructor_A_excluded": True,
                      "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
                      "independent_effective_readback": None,
                      "ENTIRE_author11_read_and_bound": True,
                      "whole_obligations_and_separate_dispositions": 48,
                      "ALL48_issue_sourceMD_worklog_embedded_in_report": True,
                      "substantive_defects": 0, "required_repairs": 0, "closed_scope_notes": 10,
                      "corresponding_NEW_peer_finding_filename_inventory_file_hash_metadata_access": False,
                      "findings_embargo_until_explicit_BOTH_ENTIRE_confirmation": True,
                      "FULL_final_MODEL_readback_ALL4_payloads_code_ALLmetadata_completed": True,
                      "FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required": True,
                      "all_guard_summary": base["all_guard_summary"],
                      "own_immediate_parent": base["own_immediate_parent"],
                      "older_own_paths_bound_transitively": 962,
                      "older_plus_new_own_paths_bound_transitively": 967,
                      "ENTIRE_files_including_this_manifest": 5,
                      "no_mathprogram_CAS_scan_test_source_author_old_replay": True,
                      "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
                      "full_RN_area_upper_regime_value_annual_priority_claim": False,
                      "last_TOTAL_usage_percent": 61, "last_usage_at_utc": "2026-10-18 18:46:00 UTC",
                      "authorized_reset": 1792874445, "TOTAL_ceiling_percent": 90,
                      "integration_reserve": True, "automatic_later_window_spending": False,
                      "payloads": payloads})
    print(json.dumps({"manifest": record(MANIFEST), "report": payloads[0], "ENTIRE_files": 5}, indent=2))


def verify():
    base = check_baseline()
    manifest = obj(MANIFEST)
    assert len(manifest["payloads"]) == 4
    assert [row["path"] for row in manifest["payloads"]] == [P + suffix for suffix in PAYLOADS]
    for row in manifest["payloads"]:
        match(row)
    assert manifest["all_guard_summary"] == base["all_guard_summary"]
    obj(P + "sources-v1.json")
    print(json.dumps({"SEPARATE_readonly_verify_at_utc": now(), "PASS": True,
                      "ENTIRE_files": 5, "whole_obligations": 48,
                      "all_guard_summary": base["all_guard_summary"],
                      "manifest": record(MANIFEST), "report": record(P + "initial-v1.md"),
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
