#!/usr/bin/env python3
"""D6 R1 metadata ONLY; no trajectory/phase/growth/proof computation.

Creates only the NEW assigned review prefix, exclusively. --verify is
read-only. Corresponding NEW root D6 R2 paths are expressly forbidden.
"""
from pathlib import Path
import argparse
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2022-B4/reviews/reasoning-dynamics-return-r6-review-1-"
AUTHOR = "problems/2022-B4/notes/reasoning-dynamics-return-r6-"
PARENT = "problems/2017-B4/notes/reasoning-path-mass-return-r8-freeze-v1.json"
FORBIDDEN = "problems/2022-B4/reviews/reasoning-dynamics-return-r6-review-2-"

def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def read(path):
    assert isinstance(path, str) and not path.startswith("/")
    assert ".." not in Path(path).parts
    assert not path.startswith(FORBIDDEN), path
    return (ROOT / path).read_bytes()

def obj(path):
    return json.loads(read(path))

def fp(path):
    data = read(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

def check(rec):
    expected = {k: rec[k] for k in ("path", "bytes", "sha256")}
    assert fp(expected["path"]) == expected, expected["path"]
    return expected

def create_json(suffix, value):
    assert suffix in ("baseline-v1.json", "input-validation-v1.json", "metadata-v1.json", "manifest-v1.json")
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")

def labels():
    ids = re.findall(r"^\| (D6R1-[0-9]{2}) \|", read(P + "ledger-v1.md").decode(), re.MULTILINE)
    assert ids == [f"D6R1-{i:02d}" for i in range(1, 65)]
    author_ids = re.findall(r"^(\d+)\. ", read(AUTHOR + "obligations-v1.md").decode(), re.MULTILINE)
    assert author_ids == [str(i) for i in range(1, 65)]
    assert all("D6" + x in read(P + "initial-v1.md").decode() for x in "ABCD")
    return ids

KNOWN = [
    {"path": AUTHOR + "candidate-v1.md", "bytes": 19255,
     "sha256": "f7da37b6f8ed520b1932a2b55b7d52cad5c94c7926ae1b02132e31693e5e5dc8"},
    {"path": AUTHOR + "freeze-v1.json", "bytes": 5069,
     "sha256": "ab7d73318a784c821fb3e0f8142b671e735c583721e6a7e464dbe91981c2b3e4"},
    {"path": PARENT, "bytes": 2910,
     "sha256": "83c9efd6a2e47e0a169a8415256d40ee1d154c142cd37dee28e344ec67b248e3"},
]

DIRECT = [
    "AGENTS.md", "problems/2022-B4/statement.md",
    "problems/2022-B4/proofs/reviewed-reasoning-fiber-return-r5-v1.1.md",
    "problems/2022-B4/reviews/reasoning-fiber-return-r5-acceptance.md",
    "problems/2022-B4/reviews/reasoning-fiber-return-r5-acceptance.json",
    "problems/2022-B4/notes/reasoning-fiber-return-r5-failed-routes-v1.md",
    "problems/2022-B4/notes/reasoning-fiber-return-r5-sources-v1.md",
    "problems/2022-B4/notes/reasoning-fiber-return-r5-sources-v1.json",
    "problems/2022-B4/proofs/reviewed-density-v3.md",
    "problems/2022-B4/reviews/acceptance.md",
    "problems/2022-B4/reviews/acceptance.json",
]

def validate_inputs():
    records = [check(rec) for rec in KNOWN]
    frozen = obj(AUTHOR + "freeze-v1.json")
    assert frozen["whole_obligations"] == 64
    assert frozen["ENTIRE_files_including_freeze"] == 14
    assert len(frozen["payloads"]) == 13
    records.extend(check(rec) for rec in frozen["payloads"])
    author_baseline = obj(AUTHOR + "baseline-v1.json")
    old_checks = [check(rec) for rec in author_baseline["protected_fingerprints"]]
    assert len(old_checks) == author_baseline["protected_current_unique_paths"] == 46
    canonical = json.dumps(old_checks, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    assert hashlib.sha256(canonical.encode()).hexdigest() == author_baseline["canonical_deduplicated_sha256"]
    parent = obj(PARENT)
    parent_checks = [check(rec) for rec in parent["artifacts"]]
    assert len(parent_checks) + 1 == parent["all_artifacts_including_freeze"] == 11
    records.extend(fp(path) for path in DIRECT)
    cf = obj("problems/2022-B4/reviews/reasoning-fiber-return-r5-acceptance.json")
    assert cf["status"].startswith("proved, independently reviewed")
    check(cf["accepted_copy"])
    density = obj("problems/2022-B4/reviews/acceptance.json")
    assert density["status"].startswith("proved, independently reviewed")
    for rel, sha in density["artifacts"].items():
        assert fp("problems/2022-B4/" + rel)["sha256"] == sha
    unique = {}
    for rec in records:
        assert rec["path"] not in unique or rec == unique[rec["path"]]
        unique[rec["path"]] = rec
    return {
        "direct_fingerprint_occurrences": len(records),
        "direct_input_paths": [unique[path] for path in sorted(unique)],
        "compact_author_preservation_binding": {
            **fp(AUTHOR + "baseline-v1.json"),
            "declared_unique_paths_checked": len(old_checks),
            "declared_occurrences_bound": author_baseline["protected_current_occurrences"],
            "canonical_deduplicated_sha256": author_baseline["canonical_deduplicated_sha256"],
            "historical_inventory_recopied_or_recursive_replay": False,
        },
        "compact_immediate_own_parent_binding": {
            **fp(PARENT), "payloads_checked": len(parent_checks),
            "all_files": 11, "mathematical_premise": False,
        },
    }

SUFFIXES = [
    "initial-v1.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md",
    "sources-v1.json", "worklog-v1.md", "admin-v1.py", "baseline-v1.json",
    "input-validation-v1.json", "metadata-v1.json",
]

def create():
    ids = labels()
    validated = validate_inputs()
    create_json("baseline-v1.json", {"recorded_at_utc": now(),
        "metadata_only_not_mathematical_proof": True,
        **validated,
        "NEW_corresponding_peer_access_forbidden": FORBIDDEN})
    create_json("input-validation-v1.json", {"validated_at_utc": now(),
        "ALL14_constructor_artifacts_match": True,
        "all_necessary_direct_old_inputs_match": True,
        "author46_declared_old_paths_checked_without_recursive_replay": True,
        "immediate_own_parent_ALL11_match": True,
        "whole_obligation_labels": ids,
        "mathematical_program_run": False,
        "constructor_code_run": False,
        "corresponding_NEW_peer_accessed": False})
    create_json("metadata-v1.json", {"recorded_at_utc": now(),
        "reviewer": "/root/review_2017_coarsening_r1",
        "review": "OTHER initially blind ENTIRE WHOLE D6 R1 ALL64",
        "NEW_constructor": False,
        "OLD_CF_authorship_disclosed_no_self_recertification": True,
        "whole_obligations": len(ids),
        "substantive_defects": 0, "required_repairs": 0,
        "closed_scope_notes": 5,
        "initial_entire_blindness_preserved": True,
        "corresponding_NEW_root_D6_finding_file_hash_metadata_accessed": False,
        "root_identity_only_notice_supplied_NO_inference_or_disposition": True,
        "identity_ONLY_handoff_until_BOTH_ENTIRE_confirmation": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "verified_effective_readback": None,
        "authorized_reset": 1792874445,
        "latest_provided_authoritative_TOTAL_percent": 35,
        "ceiling_TOTAL_percent": 90, "integration_reserve": True,
        "no_automatic_later_window": True,
        "mathematical_code_CAS_scan_author_or_source_rerun": False,
        "promotion": False})
    create_json("manifest-v1.json", {"frozen_at_utc": now(),
        "status": "ENTIRE initially blind OTHER WHOLE D6 R1 checkpoint, not promotion",
        "reviewer": "/root/review_2017_coarsening_r1",
        "whole_obligations": len(ids), "all_files_including_manifest": 11,
        "author_freeze": fp(AUTHOR + "freeze-v1.json"),
        "immediate_own_parent": fp(PARENT),
        "corresponding_NEW_peer_accessed": False,
        "BOTH_entire_confirmation_REQUIRED_before_findings_release": True,
        "FULL_all11_readback_and_SEPARATE_verify_follow_immutable_freeze": True,
        "artifacts": [fp(P + suffix) for suffix in SUFFIXES]})
    print(json.dumps({"manifest": fp(P + "manifest-v1.json"),
                      "initial": fp(P + "initial-v1.md"),
                      "all_files": 11, "whole_obligations": len(ids),
                      "next": "FULL readback ALL11 then SEPARATE --verify; identity only"}, indent=2))

def verify():
    manifest = obj(P + "manifest-v1.json")
    for rec in manifest["artifacts"]:
        check(rec)
    baseline = obj(P + "baseline-v1.json")
    validated = validate_inputs()
    for key, value in validated.items():
        assert baseline[key] == value, key
    assert len(labels()) == manifest["whole_obligations"] == 64
    print(json.dumps({"status": "SEPARATE read-only postverification PASS",
                      "verified_at_utc": now(),
                      "manifest": fp(P + "manifest-v1.json"),
                      "initial": fp(P + "initial-v1.md"),
                      "all_files": 11, "whole_obligations": 64,
                      "corresponding_NEW_peer_accessed": False,
                      "mathematical_code_executed": False}, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    verify() if args.verify else create()
