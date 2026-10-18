#!/usr/bin/env python3
"""RD OTHER whole2 metadata only; no mathematical evaluation or replay."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2025-B4/reviews/reasoning-diagonal-return-r5-review-2-"
AUTHOR = "problems/2025-B4/notes/reasoning-diagonal-return-r5-"
FORBIDDEN = (
    "problems/2025-B4/reviews/reasoning-diagonal-return-r5-review-1-",
    "problems/2022-B4/reviews/reasoning-dynamics-return-r6-",
)
AUTHOR_FREEZE = {
    "path": AUTHOR + "freeze-v1.json", "bytes": 8179,
    "sha256": "b81f17c54ed4df58c1d2ee32a8123c6d0e46aa9f8d05d9df23e5aa06d1c6b6c2",
}
PARENT = {
    "path": "problems/2024-B4/reviews/reasoning-cofactor-return-r6-review-2-manifest-v1.json",
    "bytes": 3679,
    "sha256": "5ca938aebb500ed567173682bc501d8c88b327dad6d0e8c724591d4852039a97",
}
SUFFIXES = (
    "initial-v1.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md",
    "sources-v1.json", "worklog-v1.md", "admin-v1.py", "baseline-v1.json",
    "input-validation-v1.json", "metadata-v1.json",
)


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert isinstance(path, str) and not Path(path).is_absolute()
    assert ".." not in Path(path).parts
    assert not any(path.startswith(x) for x in FORBIDDEN), path
    return (ROOT / path).read_bytes()


def obj(path):
    return json.loads(raw(path))


def fp(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def check(record):
    expected = {key: record[key] for key in ("path", "bytes", "sha256")}
    assert fp(record["path"]) == expected, record["path"]
    return expected


def digest(value):
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode()).hexdigest()


def put(suffix, value):
    assert suffix in ("baseline-v1.json", "input-validation-v1.json", "metadata-v1.json", "manifest-v1.json")
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def protected():
    records = [check(AUTHOR_FREEZE)]
    frozen = obj(AUTHOR_FREEZE["path"])
    assert frozen["whole_obligations"] == 48
    assert frozen["ENTIRE_files_including_freeze"] == 11 and len(frozen["payloads"]) == 10
    records += [check(record) for record in frozen["payloads"]]
    old_baseline = obj(AUTHOR + "baseline-v1.json")
    old = [check(record) for record in old_baseline["protected_inputs"]]
    assert len(old) == 35 and len({record["path"] for record in old}) == 35
    assert old_baseline["canonical_protected_summary_sha256"] == digest(old)
    assert frozen["canonical_protected_summary_sha256"] == digest(old)
    records += old
    bindings = []
    for name in (
        "reasoning-branch-return-r4", "reasoning-Runge-return-r3",
        "reasoning-Runge-return-r2", "reasoning-return-r6",
    ):
        path = "problems/2025-B4/reviews/" + name + "-acceptance.json"
        authority = obj(path)
        assert authority["status"] == "proved, independently reviewed scoped partial result"
        body, candidate = check(authority["accepted_copy"]), check(authority["candidate"])
        assert raw(body["path"]).endswith(raw(candidate["path"]))
        bindings.append({
            "authority": fp(path), "accepted_body": body, "literal_candidate_suffix": candidate,
            "historical_occurrences_bound_not_replayed": authority["record_occurrences_verified"],
            "historical_paths_bound_not_replayed": authority["unique_paths_verified"],
        })
    records.append(check(PARENT))
    parent = obj(PARENT["path"])
    assert parent["ENTIRE_files"] == 11 and len(parent["payloads"]) == 10
    records += [check(record) for record in parent["payloads"]]
    assert len(records) == 57
    unique = {}
    for record in records:
        assert record["path"] not in unique or unique[record["path"]] == record
        unique[record["path"]] = record
    unique = sorted(unique.values(), key=lambda record: record["path"])
    source = obj(P + "sources-v1.json")
    for read in source["complete_accepted_bodies_and_MDJSON_read"]:
        assert fp(read["body"])["bytes"] == read["bytes"]
        assert fp(read["body"])["sha256"] == read["sha256"]
    parents = [
        {**AUTHOR_FREEZE, "ENTIRE_files_verified": 11,
         "necessary_current_inputs_verified": 35,
         "older_author_paths_bound_transitively_not_recopied": frozen["older_plus_new_own_paths_bound_transitively"],
         "author_current_deduplicated_summary_sha256": frozen["canonical_protected_summary_sha256"]},
        {**PARENT, "ENTIRE_files_verified": 11,
         "parent_protected_occurrences_bound_not_recopied": parent["protected_current_occurrences"],
         "parent_protected_paths_bound_not_recopied": parent["protected_current_unique_paths"],
         "parent_protected_summary_sha256": parent["canonical_deduplicated_sha256"]},
    ]
    return records, unique, bindings, parents


def labels():
    ledger = raw(P + "ledger-v1.md").decode()
    expected = [f"{i:02}" for i in range(1, 49)]
    assert re.findall(r"(?m)^(\d{2})\. ", ledger) == expected
    assert re.findall(r"(?m)^(\d{2})\. \*\*PASS", ledger) == expected
    assert len(re.findall(r"(?m)^## RDR2-N\d", raw(P + "issues-v1.md").decode())) == 6
    source = obj(P + "sources-v1.json")
    assert source["whole_obligations"] == 48
    assert source["substantive_defects"] == source["required_repairs"] == 0
    assert source["closed_scope_notes"] == 6
    exposure = source["peer_exposure"]
    for key in (
        "corresponding_NEW_root_RD_conclusion_finding_or_disposition_seen",
        "corresponding_NEW_root_RD_file_hash_record_or_metadata_read",
        "corresponding_NEW_root_RD_user_commentary_opened",
        "future_2022_D6_review_access",
    ):
        assert exposure[key] is False
    assert exposure["administrative_other_whole_freeze_existence_dates_counts_received"] is True
    assert source["mathematical_code_CAS_scan_test_table_optimizer_certificate_author_source_or_old_freezer_replay"] is False
    assert source["independently_verified_effective_settings"] is None
    meter = source["authoritative_weekly_telemetry"]
    assert meter["reset_unix"] == 1792874445
    assert meter["TOTAL_used_percent"] < meter["TOTAL_ceiling_percent"] == 90
    return source


def prepare():
    records, unique, bindings, parents = protected()
    labels()
    put("baseline-v1.json", {
        "created_at_utc": now(), "purpose": "Necessary current fingerprints and compact immediate parent binding only",
        "protected_current_occurrences": len(records), "protected_current_unique_paths": len(unique),
        "canonical_deduplicated_sha256": digest(unique), "protected_fingerprints": unique,
        "groups": {"ENTIRE_author": 11, "author_necessary_current_inputs": 35, "immediate_own_parent": 11},
        "current_accepted_bindings": bindings, "compact_parent_bindings": parents,
        "historical_inventory_recopied_or_recursively_replayed": False,
        "forbidden_NEW_peer_prefixes_never_read_or_hashed": list(FORBIDDEN),
    })
    put("input-validation-v1.json", {
        "verified_at_utc": now(), "metadata_ONLY_not_math_or_independent_review": True,
        "protected_current_occurrences_unchanged": len(records), "protected_current_unique_paths_unchanged": len(unique),
        "ENTIRE_author11_and_own_parent11_verified": True,
        "author_all35_necessary_current_inputs_verified": True,
        "four_current_accepted_body_candidate_suffixes_checked": True,
        "review_ledger_ordered01to48_and_six_closed_notes": True,
        "no_NEW_corresponding_root_RD_or_future_D6_review_access": True,
        "FULL_model_readback_and_SEPARATEverify_required": True,
    })
    put("metadata-v1.json", {
        "created_at_utc": now(), "role": "OTHER initially blind ENTIRE WHOLE RD review2",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "whole_obligations": 48,
        "payload_files": 10, "ENTIRE_files_including_manifest": 11,
        "substantive_defects": 0, "required_repairs": 0, "closed_scope_notes": 6,
        "recommendation_only_no_promotion": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "NEW_code_metadata_only_no_math_scan_author_source_or_old_replay": True,
        "protected_current_occurrences": len(records), "protected_current_unique_paths": len(unique),
        "canonical_deduplicated_sha256": digest(unique),
        "FULL_payload_model_readback_before_manifest_required": True,
        "manifest_FULLreadback_and_SEPARATEverify_required": True,
    })
    print(json.dumps({"prepared": True, "protected_occurrences": len(records), "unique_paths": len(unique)}))


def baseline_check():
    records, unique, bindings, parents = protected()
    baseline = obj(P + "baseline-v1.json")
    assert baseline["protected_fingerprints"] == unique
    assert baseline["protected_current_occurrences"] == len(records)
    assert baseline["canonical_deduplicated_sha256"] == digest(unique)
    assert baseline["current_accepted_bindings"] == bindings
    assert baseline["compact_parent_bindings"] == parents
    labels()
    return baseline


def freeze(readback_complete):
    assert readback_complete, "Finish FULL model readback of ALL10 payloads before freeze"
    baseline = baseline_check()
    payloads = [fp(P + suffix) for suffix in SUFFIXES]
    put("manifest-v1.json", {
        "frozen_at_utc": now(), "status": "OTHER initially blind ENTIRE WHOLE RD review2 complete; root reconciliation pending",
        "whole_obligations": 48, "payload_files": 10, "ENTIRE_files": 11,
        "FULL_payload_model_readback_complete_before_manifest": True,
        "manifest_FULLreadback_and_SEPARATEverify_required_before_identity_handoff": True,
        "substantive_defects": 0, "required_repairs": 0, "closed_scope_notes": 6,
        "candidate_unpromoted_by_reviewer": True,
        "author_entire_freeze": AUTHOR_FREEZE, "immediate_own_parent": PARENT,
        "compact_baseline": fp(P + "baseline-v1.json"),
        "protected_current_occurrences": baseline["protected_current_occurrences"],
        "protected_current_unique_paths": baseline["protected_current_unique_paths"],
        "canonical_deduplicated_sha256": baseline["canonical_deduplicated_sha256"],
        "no_NEW_corresponding_root_RD_review_or_future_D6_review_access": True,
        "identity_only_until_explicit_BOTH_ENTIRE_confirmation": True,
        "no_mathematical_program_CAS_scan_author_source_or_old_replay": True,
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
        "no_NEW_corresponding_root_RD_review_or_future_D6_review_access": True,
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
