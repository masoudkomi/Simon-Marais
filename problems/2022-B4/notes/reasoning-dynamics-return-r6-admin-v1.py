#!/usr/bin/env python3
"""D6 create-only metadata integrity; never computes an orbit or a proof."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2022-B4/notes/reasoning-dynamics-return-r6-"
YEAR = "problems/2022-B4/"
CF = YEAR + "reviews/reasoning-fiber-return-r5-acceptance.json"
DENSITY = YEAR + "reviews/acceptance.json"
PARENT = {
    "path": "problems/2020-B4/reviews/reasoning-arithmetic-return-r13-review-2-manifest-v1.json",
    "bytes": 4007,
    "sha256": "4d815040099e498128c3a3169c69e564d0c7ce976017a8aed6804c1f2d2b0262",
}
FORBIDDEN = (
    "problems/2024-B4/notes/reasoning-cofactor-return-r6-",
    "problems/2024-B4/reviews/reasoning-cofactor-return-r6-",
    "problems/2022-B4/reviews/reasoning-dynamics-return-r6-",
)
SUFFIXES = (
    "candidate-v1.md", "working-v1.md", "obligations-v1.md", "checks-v1.md",
    "failures-v1.md", "sources-v1.md", "sources-v1.json", "log-v1.md",
    "code-log-v1.md", "admin-v1.py", "baseline-v1.json",
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
    assert suffix in ("baseline-v1.json", "input-validation-v1.json", "metadata-v1.json", "freeze-v1.json")
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def protected():
    records = [fp("AGENTS.md"), fp(YEAR + "statement.md")]
    cf = obj(CF)
    assert cf["status"].startswith("proved, independently reviewed")
    cf_records = [fp(CF), fp(CF[:-5] + ".md")]
    cf_records += [check(cf["candidate"]), check(cf["accepted_copy"])]
    cf_records += [check(r) for r in cf["verification_metadata"]]
    assert len(cf["verification_metadata"]) == 15
    assert raw(cf["accepted_copy"]["path"]).endswith(raw(cf["candidate"]["path"]))
    cf_records += [fp(YEAR + "notes/reasoning-fiber-return-r5-" + suffix) for suffix in (
        "failed-routes-v1.md", "sources-v1.md", "sources-v1.json")]
    assert len(cf_records) == 22
    records += cf_records
    den = obj(DENSITY)
    assert den["status"].startswith("proved, independently reviewed")
    den_records = [fp(DENSITY), fp(DENSITY[:-5] + ".md")]
    for rel, sha in den["artifacts"].items():
        record = fp(YEAR + rel)
        assert record["sha256"] == sha, rel
        den_records.append(record)
    assert len(den["artifacts"]) == 10
    records += den_records
    check(PARENT)
    parent = obj(PARENT["path"])
    assert parent["ENTIRE_files"] == 11 and len(parent["payloads"]) == 10
    records.append(PARENT)
    records += [check(r) for r in parent["payloads"]]
    assert len(records) == 47
    unique = {}
    for r in records:
        assert r["path"] not in unique or unique[r["path"]] == r
        unique[r["path"]] = r
    unique = sorted(unique.values(), key=lambda r: r["path"])
    source = obj(P + "sources-v1.json")
    for read in source["accepted_whole_body_authority_reads"]:
        record = fp(read["body"])
        assert record["sha256"] == read["sha256"]
        if "bytes" in read:
            assert record["bytes"] == read["bytes"]
    parents = [
        {**fp(CF), "current_direct_declared_fingerprints_verified": 17,
         "historical_occurrences_bound_not_recopied": cf["record_occurrences_verified"],
         "historical_paths_bound_not_recopied": cf["unique_paths_verified"]},
        {**fp(DENSITY), "current_direct_declared_hashes_verified": 10,
         "historical_inventory_recopied_or_recursively_replayed": False},
        {**PARENT, "payloads_verified": 10, "ENTIRE_files": 11,
         "parent_protected_occurrences_bound_not_recopied": parent["protected_occurrences"],
         "parent_protected_unique_paths_bound_not_recopied": parent["protected_unique_paths"],
         "parent_protected_summary_sha256": parent["canonical_deduplicated_sha256"]},
    ]
    return records, unique, parents


def labels():
    for suffix in ("obligations-v1.md", "checks-v1.md"):
        text = raw(P + suffix).decode()
        assert [int(x) for x in re.findall(r"(?m)^(\d+)\. ", text)] == list(range(1, 65)), suffix
    main = raw(P + "candidate-v1.md").decode()
    assert "**Candidate proof - unverified.**" in main
    assert all("**D6" + letter in main for letter in "ABCD")
    source = obj(P + "sources-v1.json")
    assert source["whole_obligations"] == 64
    assert source["constructor_excluded_from_TWO_OTHER_whole_reviews"] is True
    assert source["root_NEW_inference_supplied"] is False
    assert source["CF6_tenfold_existence_assumed_or_proved_by_D6"] is False
    assert source["mathematical_program_CAS_scan_table_test_author_or_source_replay"] is False
    assert source["NEW2024R6_author_peer_or_future_D6_review_accessed"] is False
    assert source["independently_verified_effective_settings"] is None
    meter = source["authoritative_weekly_telemetry"]
    assert meter["reset_unix"] == 1792874445
    assert meter["used_percent_TOTAL"] < meter["ceiling_TOTAL_percent"] == 90
    return source


def prepare():
    records, unique, parents = protected()
    labels()
    put("baseline-v1.json", {
        "created_at_utc": now(),
        "purpose": "Necessary current declarations and compact immutable parents only; no mathematical proof",
        "protected_current_occurrences": len(records), "protected_current_unique_paths": len(unique),
        "canonical_deduplicated_sha256": digest(unique),
        "protected_fingerprints": unique,
        "groups": {"AGENTS_and_statement": 2, "CF_current_declared_plus_context": 22,
                   "old_density_current_declared_plus_authority": 12, "immediate_own_parent": 11},
        "compact_parent_metadata_bindings": parents,
        "historical_inventory_recopied_or_recursively_replayed": False,
        "forbidden_NEW_unrelated_author_and_peer_prefixes": list(FORBIDDEN),
    })
    put("input-validation-v1.json", {
        "verified_at_utc": now(), "metadata_ONLY_not_proof_or_review": True,
        "protected_current_occurrences_unchanged": len(records),
        "protected_current_unique_paths_unchanged": len(unique),
        "CF_exact_accepted_candidate_suffix_checked": True,
        "CF17_and_old_density10_direct_declarations_checked": True,
        "immediate_own_parent11_files_checked": True,
        "whole_obligation_and_constructor_labels_ordered1to64": True,
        "no_math_program_scan_CAS_author_or_source_rerun": True,
        "FULL_all_payload_readback_and_SEPARATE_verify_required_before_handoff": True,
    })
    put("metadata-v1.json", {
        "created_at_utc": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2021_reasoning_j15_r2", "claims": ["D6A", "D6B", "D6C", "D6D"],
        "whole_obligations": 64, "ENTIRE_files_including_freeze": 14,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_and_root_reconciliation_required": True,
        "constructor_excluded": True, "root_NEW_inference_supplied": False,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "new_claims_are_actual_ordinary_growth_not_canonical_fiber_count": True,
        "CF6_or_ordinary_infinite_lift_existence_assumed": False,
        "mathematical_program_CAS_scan_author_or_source_rerun": False,
        "NEW_metadata_code_only": True,
        "protected_current_occurrences": len(records), "protected_current_unique_paths": len(unique),
        "canonical_deduplicated_sha256": digest(unique),
        "FULL_model_readback_before_freeze_required": True,
        "freeze_FULL_readback_then_SEPARATE_verify_required": True,
    })
    print(json.dumps({"prepared": True, "protected_current_occurrences": len(records), "unique_paths": len(unique)}))


def baseline_check():
    records, unique, parents = protected()
    data = obj(P + "baseline-v1.json")
    assert data["protected_fingerprints"] == unique
    assert data["protected_current_occurrences"] == len(records)
    assert data["canonical_deduplicated_sha256"] == digest(unique)
    assert data["compact_parent_metadata_bindings"] == parents
    labels()
    return data


def freeze(readback_complete):
    assert readback_complete, "Finish FULL model readback of all13 payloads first"
    data = baseline_check()
    payloads = [fp(P + suffix) for suffix in SUFFIXES]
    put("freeze-v1.json", {
        "frozen_at_utc": now(), "status": "candidate proof - unverified",
        "claims": ["D6A", "D6B", "D6C", "D6D"], "whole_obligations": 64,
        "payload_files": 13, "ENTIRE_files_including_freeze": 14,
        "FULL_payload_model_readback_complete_before_freeze": True,
        "freeze_FULL_readback_and_SEPARATE_verify_required_before_handoff": True,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_reviews_required": True,
        "constructor_excluded": True, "root_NEW_inference_supplied": False,
        "old_finite_lifting_block_counting_methods_attributed_not_claimed_new": True,
        "actual_ordinary_growth_spectrum_not_hitting_or_canonical_multiplicity": True,
        "CF6_tenfold_or_infinite_ordinary_lift_existence_assumed": False,
        "no_math_program_CAS_scan_author_or_source_rerun": True,
        "compact_baseline": fp(P + "baseline-v1.json"),
        "protected_current_occurrences": data["protected_current_occurrences"],
        "protected_current_unique_paths": data["protected_current_unique_paths"],
        "canonical_deduplicated_sha256": data["canonical_deduplicated_sha256"],
        "compact_parent_metadata_bindings": data["compact_parent_metadata_bindings"],
        "payloads": payloads,
    })
    print(json.dumps({"freeze": fp(P + "freeze-v1.json"), "main": payloads[0], "ENTIRE_files": 14, "ALL_obligations": 64}))


def verify():
    data = baseline_check()
    frozen = obj(P + "freeze-v1.json")
    assert frozen["compact_baseline"] == fp(P + "baseline-v1.json")
    assert frozen["canonical_deduplicated_sha256"] == data["canonical_deduplicated_sha256"]
    assert [r["path"] for r in frozen["payloads"]] == [P + suffix for suffix in SUFFIXES]
    for r in frozen["payloads"]:
        check(r)
    print(json.dumps({
        "SEPARATE_postfreeze_verify": "PASS", "verified_at_utc": now(),
        "freeze": fp(P + "freeze-v1.json"), "main": frozen["payloads"][0],
        "ENTIRE_files": 14, "ALL_obligations": 64,
        "protected_current_occurrences": data["protected_current_occurrences"],
        "protected_current_unique_paths": data["protected_current_unique_paths"],
        "no_queued_NEW2024R6_author_peer_or_future_D6_review_access": True,
        "metadata_only_not_proof_or_independent_review": True,
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
