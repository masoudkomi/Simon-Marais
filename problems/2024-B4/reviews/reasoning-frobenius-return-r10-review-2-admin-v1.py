#!/usr/bin/env python3
"""NEW FR10 reviewer2 documentary administration, NEVER mathematical code.

prepare creates one exclusive-prefix baseline; freeze requires actual final
MODEL readback; verify is a SEPARATE read-only process. No old/source/author
helper, subprocess, network or mathematical library is invoked.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/reasoning-frobenius-return-r10-review-2-"
A = "problems/2024-B4/notes/reasoning-frobenius-return-r10-"
AUTHOR = A + "freeze-v1.json"
AUTHOR_ID = (3218, "226beec7d86256e4daed124fb3686be8b798aa75b0638aaabef6eaf7df500f65")
AUTHOR_MAIN_ID = (23051, "89dca5bac46c7601b8e64462783ba448d1a6aca5d4d5e393a6ff128898aebea5")
PARENT = "problems/2020-B4/notes/reasoning-class-return-sq17-freeze-v1.json"
PARENT_ID = (3901, "d7b19f6e852178d83db1adad70e2fdb10c8dfa30d28b538e893cf1f0b567aab1")
PAYLOAD_SUFFIXES = ["initial-v1.md", "sources-v1.json", "admin-v1.py", "baseline-v1.json"]
BASELINE = P + "baseline-v1.json"
MANIFEST = P + "manifest-v1.json"
SOURCE_STEMS = ["structural", "reasoning-cofactor-return-r6", "reasoning-cofactor-return-r7",
                "reasoning-cofactor-return-r8", "reasoning-cofactor-return-r9"]
BODY_EXPECTED = {
    "structural": (17079, "082dc054ce2cdaea80eee009f4c97c877c6968afb54b5a8f3141b7354031dd3f"),
    "reasoning-cofactor-return-r6": (20658, "fb988a13187b5765619532ad14077ae2f32a948e04704252e3d8981e10d65d98"),
    "reasoning-cofactor-return-r7": (22608, "b8e2cc3a37cf8c80c724c0d26f6768261e5d339fee073351e8b4c9b56b94cf72"),
    "reasoning-cofactor-return-r8": (19878, "acdfa8d740a762de8a4070867d6e9ebf68a1d54ff7a92e0a9126e2e339b19023"),
    "reasoning-cofactor-return-r9": (26416, "68a8b1d05a927ffecc13375ee5db5376c780acbf7e3cee3a6659c8c80caa876c")}


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert "reasoning-frobenius-return-r10-review-1-" not in path, "Embargoed NEW peer path"
    assert not Path(path).is_absolute() and ".." not in Path(path).parts
    return (ROOT / path).read_bytes()


def record(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def obj(path):
    return json.loads(raw(path))


def triple(row):
    return {key: row[key] for key in ["path", "bytes", "sha256"]}


def match(row):
    item = triple(row)
    assert record(item["path"]) == item, "Changed input: " + item["path"]
    return item


def fixed(path, identity):
    return match({"path": path, "bytes": identity[0], "sha256": identity[1]})


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def summary(rows):
    unique = {}
    for row in rows:
        item = triple(row)
        assert item["path"] not in unique or item == unique[item["path"]]
        unique[item["path"]] = item
    ordered = [unique[path] for path in sorted(unique)]
    return {"occurrences": len(rows), "unique_paths": len(ordered), "canonical_sha256": digest(ordered)}


def declared(value):
    out = []
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and isinstance(value.get("bytes"), int) and isinstance(value.get("sha256"), str) and len(value["sha256"]) == 64:
            out.append(triple(value))
        for child in value.values():
            out.extend(declared(child))
    elif isinstance(value, list):
        for child in value:
            out.extend(declared(child))
    return out


def create(path, value):
    assert path.startswith(P)
    with (ROOT / path).open("xb") as stream:
        stream.write((json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode())


def literal_checks():
    text = raw(P + "initial-v1.md").decode()
    rows = re.findall(r"^\|(FR10R2-\d{2})\|PASS", text, re.M)
    assert rows == [f"FR10R2-{i:02d}" for i in range(1, 65)]
    author_text = raw(A + "obligations-v1.md").decode()
    author_rows = re.findall(r"^\| (\d{2}) \|", author_text, re.M)
    assert author_rows == [f"{i:02d}" for i in range(1, 65)]
    source = obj(P + "sources-v1.json")
    assert source["independent_effective_readback"] is None
    assert source["NEW_FR10_nonconstructor"] is True
    assert source["corresponding_NEW_root_FR10_finding_filename_inventory_file_hash_metadata_access"] is False
    return {"author_obligation_labels": 64, "review_ALL64_separate_disposition_labels": 64,
            "mathematical_truth_or_source_hypotheses_checked_by_code": False}


def collect_inputs():
    author_manifest = fixed(AUTHOR, AUTHOR_ID)
    author = obj(AUTHOR)
    assert author["ENTIRE_files_including_this_freeze"] == 13 and author["whole_obligations"] == 64
    author_rows = [author_manifest] + [match(row) for row in author["payload_records"]]
    assert len(author_rows) == 13
    fixed(A + "candidate-v1.md", AUTHOR_MAIN_ID)

    # Reconstruct the author's declared byte/JSON guards independently;
    # NEVER run its helper. Historical rows are summarized, not recopied.
    author_base = obj(A + "baseline-v1.json")
    guard_rows = [match(row) for row in author_base["direct_inputs"]]
    for parent in author_base["immutable_parent_metadata"]:
        match(parent)
        rows = declared(obj(parent["path"]))
        assert len(rows) == parent["declared_fingerprint_occurrences_verified"]
        assert digest(rows) == parent["declared_records_canonical_sha256"]
        guard_rows.extend(match(row) for row in rows)
    guard_summary = summary(guard_rows)
    assert guard_summary["occurrences"] == author_base["direct_plus_declared_occurrences_verified"] == 54
    assert guard_summary["unique_paths"] == author_base["unique_guard_paths"] == 52
    assert guard_summary["canonical_sha256"] == author_base["deduplicated_guard_records_canonical_sha256"]

    direct = [fixed("AGENTS.md", (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff")),
              fixed("problems/2024-B4/statement.md", (2470, "60244f7752634772adb434efbdb41a63fb02029dc3be4238f3718c6e5ec84e5f"))]
    current_authorities = []
    for stem in SOURCE_STEMS:
        base = "problems/2024-B4/"
        authority_path = base + "reviews/" + stem + "-acceptance.json"
        authority = obj(authority_path)
        accepted = match(authority["accepted_proof" if stem == "structural" else "accepted_copy"])
        fixed(accepted["path"], BODY_EXPECTED[stem])
        candidate = match(authority["candidate"])
        suffix_match = stem != "structural"
        if suffix_match:
            assert raw(accepted["path"]).endswith(raw(candidate["path"]))
        current_authorities.append({"authority": record(authority_path),
                                   "accepted_body": accepted, "immutable_candidate": candidate,
                                   "candidate_suffix_test_applied": suffix_match,
                                   "structural_T1_body_unchanged_editorial_heading_elsewhere": stem == "structural"})
        direct.extend([accepted, record(authority_path), record(base + "reviews/" + stem + "-acceptance.md")])

    own_parent = fixed(PARENT, PARENT_ID)
    parent = obj(PARENT)
    assert parent["older_plus_new_own_paths_bound_transitively"] == 957
    own_rows = [own_parent] + [match(row) for row in parent["payloads"]]
    assert len(own_rows) == 8
    return {"author_rows": author_rows, "author_guard_summary": guard_summary,
            "direct_inputs": direct, "current_authorities": current_authorities,
            "own_parent": own_parent, "own_parent_summary": summary(own_rows),
            "all_guard_summary": summary(author_rows + guard_rows + direct + own_rows)}


def prepare():
    inputs = collect_inputs()
    literal = literal_checks()
    create(BASELINE, {"prepared_at_utc": now(),
                      "scope": "Compact independent documentary guard; no copied growing historical inventory",
                      "reviewer": "/root/review_2022_complexity_r2", "NEW_FR10_nonconstructor": True,
                      "author_ALL13_records": inputs["author_rows"],
                      "author_ALL54_declared_guard_occurrences_independently_verified_summary": inputs["author_guard_summary"],
                      "direct_current_inputs": inputs["direct_inputs"],
                      "current_immutable_authorities": inputs["current_authorities"],
                      "own_immediate_parent": inputs["own_parent"],
                      "own_parent_ALL8_files_directly_verified_not_recopied": inputs["own_parent_summary"],
                      "all_guard_summary": inputs["all_guard_summary"],
                      "older_own_paths_bound_transitively": 957,
                      "older_plus_new5_own_paths_bound_transitively": 962,
                      "literal_checks": literal,
                      "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
                      "independent_effective_readback": None,
                      "corresponding_NEW_peer_content_inventory_hash_metadata_access": False,
                      "no_mathprogram_CAS_scan_test_source_author_old_replay": True,
                      "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
                      "ENTIRE_review_files_including_manifest": 5,
                      "ALL64_source_MD_issue_ledger_worklog_embedded_in_full_report": True,
                      "FULL_final_MODEL_readback_ALL4_then_manifest_readback_SEPARATE_verify_required": True})
    print(json.dumps({"prepare": "PASS", "all_guard_summary": inputs["all_guard_summary"], **literal}, indent=2))


def check_baseline():
    base = obj(BASELINE)
    inputs = collect_inputs()
    assert base["author_ALL13_records"] == inputs["author_rows"]
    assert base["direct_current_inputs"] == inputs["direct_inputs"]
    assert base["current_immutable_authorities"] == inputs["current_authorities"]
    assert base["own_immediate_parent"] == inputs["own_parent"]
    assert base["own_parent_ALL8_files_directly_verified_not_recopied"] == inputs["own_parent_summary"]
    assert base["all_guard_summary"] == inputs["all_guard_summary"]
    assert base["author_ALL54_declared_guard_occurrences_independently_verified_summary"] == inputs["author_guard_summary"]
    literal_checks()
    return base


def freeze(readback):
    assert readback, "Actual FULL final MODEL readback is required before freeze"
    base = check_baseline()
    payloads = [record(P + suffix) for suffix in PAYLOAD_SUFFIXES]
    create(MANIFEST, {"frozen_at_utc": now(), "reviewer": "/root/review_2022_complexity_r2",
                      "role": "OTHER initially blind ENTIRE WHOLE2 of NEW FR10",
                      "NEW_FR10_nonconstructor": True, "constructor_C_excluded": True,
                      "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
                      "independent_effective_readback": None,
                      "author_ALL13_records_bound_by_baseline": True,
                      "whole_obligations_and_separate_dispositions": 64,
                      "ALL64_issue_sourceMD_worklog_in_full_report": True,
                      "closed_scope_notes": 10, "substantive_defects": 0, "required_author_repairs": 0,
                      "corresponding_NEW_peer_findings_filename_inventory_file_hash_metadata_access": False,
                      "findings_embargo_until_explicit_BOTH_ENTIRE_confirmation": True,
                      "FULL_final_MODEL_readback_ALL4_payloads_code_ALLmetadata_completed": True,
                      "FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required": True,
                      "all_guard_summary": base["all_guard_summary"],
                      "own_immediate_parent": base["own_immediate_parent"],
                      "older_own_paths_bound_transitively": 957,
                      "older_plus_new_own_paths_bound_transitively": 962,
                      "ENTIRE_files_including_this_manifest": 5,
                      "no_mathprogram_CAS_scan_test_source_author_old_replay": True,
                      "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
                      "no_annual_converse_priority_promotion": True,
                      "authorized_reset": 1792874445, "last_TOTAL_usage_percent": 61,
                      "last_usage_at_utc": "2026-10-18 18:36:00 UTC",
                      "TOTAL_ceiling_percent": 90, "integration_reserve": True,
                      "automatic_later_window_spending": False,
                      "payloads": payloads})
    print(json.dumps({"manifest": record(MANIFEST), "report": payloads[0], "ENTIRE_files": 5}, indent=2))


def verify():
    base = check_baseline()
    manifest = obj(MANIFEST)
    assert len(manifest["payloads"]) == 4
    assert [row["path"] for row in manifest["payloads"]] == [P + suffix for suffix in PAYLOAD_SUFFIXES]
    for row in manifest["payloads"]:
        match(row)
    assert manifest["all_guard_summary"] == base["all_guard_summary"]
    obj(P + "sources-v1.json")
    print(json.dumps({"SEPARATE_readonly_verify_at_utc": now(), "PASS": True,
                      "ENTIRE_files": 5, "whole_obligations": 64,
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
