#!/usr/bin/env python3
"""R6 OTHER review2 current-fingerprint metadata only, never mathematics."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/reasoning-cofactor-return-r6-review-2-"
AUTHOR = "problems/2024-B4/notes/reasoning-cofactor-return-r6-"
FORBIDDEN = (
    "problems/2024-B4/reviews/reasoning-cofactor-return-r6-review-1-",
    "problems/2022-B4/reviews/reasoning-dynamics-return-r6-",
)
AUTHOR_FREEZE = {
    "path": AUTHOR + "freeze-v1.json", "bytes": 3001,
    "sha256": "ea0a7c41741ca3655c36825a6a299c1859505855c786ea7494a9204995a0b8a9",
}
PARENT = {
    "path": "problems/2022-B4/notes/reasoning-dynamics-return-r6-freeze-v1.json",
    "bytes": 5069,
    "sha256": "ab7d73318a784c821fb3e0f8142b671e735c583721e6a7e464dbe91981c2b3e4",
}
SUFFIXES = (
    "initial-v1.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md",
    "sources-v1.json", "worklog-v1.md", "admin-v1.py", "baseline-v1.json",
    "input-validation-v1.json", "metadata-v1.json",
)


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert isinstance(path, str) and not path.startswith("/")
    assert ".." not in Path(path).parts
    assert not any(path.startswith(x) for x in FORBIDDEN), path
    return (ROOT / path).read_bytes()


def obj(path):
    return json.loads(raw(path))


def fp(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def check(record):
    expected = {k: record[k] for k in ("path", "bytes", "sha256")}
    assert fp(record["path"]) == expected, record["path"]
    return expected


def digest(value):
    canonical = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode()).hexdigest()


def put(suffix, value):
    assert suffix in ("baseline-v1.json", "input-validation-v1.json", "metadata-v1.json", "manifest-v1.json")
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def protected():
    records = [check(AUTHOR_FREEZE)]
    frozen = obj(AUTHOR_FREEZE["path"])
    assert frozen["whole_obligations"] == 48 and len(frozen["artifacts"]) == 11
    records += [check(r) for r in frozen["artifacts"]]
    baseline = obj(AUTHOR + "baseline-v1.json")
    old = [check(r) for r in baseline["direct_input_records"]]
    validation = obj(AUTHOR + "input-validation-v1.json")
    old += [check(b["record"]) for b in validation["necessary_declared_authority_bindings"]]
    author_parent = baseline["immediate_own_parent"]
    check(author_parent)
    parent_obj = obj(author_parent["path"])
    old += [check(r) for r in parent_obj["artifacts"]]
    assert len(old) == 39 and len({r["path"] for r in old}) == 32
    records += old
    accepted_bindings = []
    for name, field in (
        ("structural", "accepted_proof"),
        ("cofactor-dominant-r4", "accepted_copy"),
        ("cofactor-global-r2", "accepted_copy"),
        ("cofactor-Frobenius-r5", "accepted_copy"),
    ):
        authority = "problems/2024-B4/reviews/" + name + "-acceptance.json"
        data = obj(authority)
        assert data["status"].startswith("proved, independently reviewed")
        body, candidate = check(data[field]), check(data["candidate"])
        if name != "structural":
            assert raw(body["path"]).endswith(raw(candidate["path"]))
        if name == "cofactor-global-r2":
            records.append(candidate)
        accepted_bindings.append({
            "authority": fp(authority), "body": body, "candidate": candidate,
            "literal_suffix_asserted": name != "structural",
            "operative": name in ("structural", "cofactor-dominant-r4"),
        })
    records.append(check(PARENT))
    parent = obj(PARENT["path"])
    assert parent["ENTIRE_files_including_freeze"] == 14 and len(parent["payloads"]) == 13
    records += [check(r) for r in parent["payloads"]]
    assert len(records) == 66
    unique = {}
    for r in records:
        assert r["path"] not in unique or unique[r["path"]] == r
        unique[r["path"]] = r
    unique = sorted(unique.values(), key=lambda r: r["path"])
    source = obj(P + "sources-v1.json")
    for read in source["complete_accepted_bodies_and_MDJSON_read"]:
        assert fp(read["body"])["sha256"] == read["sha256"]
        assert fp(read["body"])["bytes"] == read["bytes"]
    parents = [
        {**AUTHOR_FREEZE, "ENTIRE_files_verified": 12,
         "author_necessary_current_occurrences_verified": 39,
         "author_necessary_current_paths_verified": 32,
         "author_parent": author_parent, "author_parent_direct_artifacts_verified": 9},
        {**PARENT, "ENTIRE_files_verified": 14,
         "parent_protected_occurrences_bound_not_recopied": parent["protected_current_occurrences"],
         "parent_protected_paths_bound_not_recopied": parent["protected_current_unique_paths"],
         "parent_protected_summary_sha256": parent["canonical_deduplicated_sha256"]},
    ]
    return records, unique, accepted_bindings, parents


def labels():
    ledger = raw(P + "ledger-v1.md").decode()
    assert [int(x) for x in re.findall(r"(?m)^(\d+)\. ", ledger)] == list(range(1, 49))
    assert len(re.findall(r"(?m)^\d+\. \*\*PASS", ledger)) == 48
    assert len(re.findall(r"(?m)^## R6R2-N\d", raw(P + "issues-v1.md").decode())) == 6
    source = obj(P + "sources-v1.json")
    assert source["whole_obligations"] == 48
    assert source["substantive_defects"] == source["required_repairs"] == 0
    assert source["closed_scope_notes"] == 6
    exposure = source["peer_exposure"]
    assert exposure["corresponding_NEW_root_R6_math_finding_or_disposition_seen"] is False
    assert exposure["corresponding_NEW_root_R6_file_hash_record_or_metadata_read"] is False
    assert exposure["root_new_user_commentary_disposition_opened"] is False
    assert exposure["administrative_assignment_and_whole_freeze_date_counts_received"] is True
    assert source["mathematical_program_CAS_scan_table_test_certificate_author_or_source_replay"] is False
    assert source["independently_verified_effective_settings"] is None
    meter = source["authoritative_weekly_telemetry"]
    assert meter["reset_unix"] == 1792874445
    assert meter["used_percent_TOTAL"] < meter["ceiling_TOTAL_percent"] == 90
    return source


def prepare():
    records, unique, bindings, parents = protected()
    labels()
    put("baseline-v1.json", {
        "created_at_utc": now(), "purpose": "Necessary current declarations and compact parent integrity only",
        "protected_current_occurrences": len(records), "protected_current_unique_paths": len(unique),
        "canonical_deduplicated_sha256": digest(unique), "protected_fingerprints": unique,
        "groups": {"ENTIRE_author": 12, "author_current_necessary_occurrences": 39,
                   "additional_CG_candidate_binding": 1, "immediate_own_parent": 14},
        "accepted_bindings": bindings, "compact_parent_bindings": parents,
        "historical_inventory_recopied_or_recursively_replayed": False,
        "forbidden_NEW_peer_prefixes_never_read_or_hashed": list(FORBIDDEN),
    })
    put("input-validation-v1.json", {
        "verified_at_utc": now(), "metadata_ONLY_not_mathematics_or_review": True,
        "protected_current_occurrences_unchanged": len(records), "protected_current_unique_paths_unchanged": len(unique),
        "ENTIRE_author12_and_own_parent14_verified": True,
        "author_necessary39occurrences32paths_verified": True,
        "current_accepted_body_candidate_bindings_checked": 4,
        "T1_editorial_heading_change_no_false_literal_suffix_claim": True,
        "review_ledger_ordered1to48_and_six_closed_scope_notes": True,
        "no_NEW_corresponding_root_R6_or_future_D6_review_access": True,
        "FULL_all_payload_readback_and_SEPARATEverify_required": True,
    })
    put("metadata-v1.json", {
        "created_at_utc": now(), "role": "OTHER initially blind ENTIRE WHOLE R6 review2",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "whole_obligations": 48,
        "payload_files": 10, "ENTIRE_files_including_manifest": 11,
        "substantive_defects": 0, "required_repairs": 0, "closed_scope_notes": 6,
        "recommendation_only_no_promotion": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "NEW_code_metadata_only_no_math_scan_author_or_source_rerun": True,
        "protected_current_occurrences": len(records), "protected_current_unique_paths": len(unique),
        "canonical_deduplicated_sha256": digest(unique),
        "FULL_model_readback_before_manifest_required": True,
        "manifest_FULL_readback_and_SEPARATEverify_required": True,
    })
    print(json.dumps({"prepared": True, "protected_current_occurrences": len(records), "unique_paths": len(unique)}))


def baseline_check():
    records, unique, bindings, parents = protected()
    baseline = obj(P + "baseline-v1.json")
    assert baseline["protected_fingerprints"] == unique
    assert baseline["protected_current_occurrences"] == len(records)
    assert baseline["canonical_deduplicated_sha256"] == digest(unique)
    assert baseline["accepted_bindings"] == bindings and baseline["compact_parent_bindings"] == parents
    labels()
    return baseline


def freeze(readback_complete):
    assert readback_complete, "Finish FULL model readback of all10 payloads first"
    baseline = baseline_check()
    payloads = [fp(P + suffix) for suffix in SUFFIXES]
    put("manifest-v1.json", {
        "frozen_at_utc": now(), "status": "OTHER initial ENTIRE WHOLE R6 review2 complete; root reconciliation pending",
        "whole_obligations": 48, "payload_files": 10, "ENTIRE_files": 11,
        "FULL_payload_model_readback_complete_before_manifest": True,
        "manifest_FULL_readback_and_SEPARATEverify_required_before_identity_handoff": True,
        "substantive_defects": 0, "required_repairs": 0, "closed_scope_notes": 6,
        "candidate_unpromoted_by_reviewer": True,
        "author_entire_freeze": AUTHOR_FREEZE, "immediate_own_parent": PARENT,
        "compact_baseline": fp(P + "baseline-v1.json"),
        "protected_current_occurrences": baseline["protected_current_occurrences"],
        "protected_current_unique_paths": baseline["protected_current_unique_paths"],
        "canonical_deduplicated_sha256": baseline["canonical_deduplicated_sha256"],
        "no_NEW_corresponding_root_R6_review_or_future_D6_review_access": True,
        "identity_only_until_BOTH_ENTIRE_initials_confirmed": True,
        "no_math_program_CAS_scan_author_or_source_rerun": True,
        "payloads": payloads,
    })
    print(json.dumps({"manifest": fp(P + "manifest-v1.json"), "initial": payloads[0], "ENTIRE_files": 11, "ALL_obligations": 48}))


def verify():
    baseline = baseline_check()
    manifest = obj(P + "manifest-v1.json")
    assert manifest["compact_baseline"] == fp(P + "baseline-v1.json")
    assert manifest["canonical_deduplicated_sha256"] == baseline["canonical_deduplicated_sha256"]
    assert [r["path"] for r in manifest["payloads"]] == [P + suffix for suffix in SUFFIXES]
    for record in manifest["payloads"]:
        check(record)
    print(json.dumps({
        "SEPARATE_postfreeze_verify": "PASS", "verified_at_utc": now(),
        "manifest": fp(P + "manifest-v1.json"), "initial": manifest["payloads"][0],
        "ENTIRE_files": 11, "ALL_obligations": 48,
        "protected_current_occurrences": baseline["protected_current_occurrences"],
        "protected_current_unique_paths": baseline["protected_current_unique_paths"],
        "no_NEW_corresponding_root_R6_review_or_future_D6_review_access": True,
        "metadata_only_not_mathematical_proof": True,
    }))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "freeze", "verify"))
    parser.add_argument("--readback-complete", action="store_true")
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    elif args.mode == "freeze":
        freeze(args.readback_complete)
    else:
        verify()
