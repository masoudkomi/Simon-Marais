#!/usr/bin/env python3
"""R13 OTHER review2 compact integrity only; no mathematical executable."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2020-B4/reviews/reasoning-arithmetic-return-r13-review-2-"
AUTHOR = "problems/2020-B4/notes/reasoning-arithmetic-return-r13-"
FORBIDDEN = "problems/2020-B4/reviews/reasoning-arithmetic-return-r13-review-1-"
AUTHOR_MANIFEST = {
    "path": AUTHOR + "freeze-v1.json", "bytes": 6630,
    "sha256": "eba097f9c6bffc2549fef51ef74b99962b16affa86a7dcaf9679bab95ad8adbe",
}
PARENT = {
    "path": "problems/2021-B4/notes/reasoning-center-return-r18-freeze-v1.json",
    "bytes": 8034,
    "sha256": "14a572167f6ea76658d87a61c951b94f111adc437555f7388b7b0cf47b2829be",
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
    assert ".." not in Path(path).parts and not path.startswith(FORBIDDEN)
    return (ROOT / path).read_bytes()


def obj(path):
    return json.loads(raw(path))


def fp(path):
    value = raw(path)
    return {"path": path, "bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}


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
    records = [check(AUTHOR_MANIFEST)]
    author = obj(AUTHOR_MANIFEST["path"])
    assert author["whole_obligations"] == 64 and len(author["artifacts"]) == 10
    assert author["status"] == "candidate proof - unverified"
    records += [check(r) for r in author["artifacts"]]
    baseline = obj(AUTHOR + "baseline-v1.json")
    old = baseline["protected_fingerprints"]
    assert len(old) == 27
    assert digest(old) == baseline["canonical_protected_summary_sha256"]
    records += [check(r) for r in old]
    bindings = []
    for b in baseline["accepted_bindings"]:
        authority = obj(b["authority_json"])
        assert authority["status"].startswith("proved, independently reviewed")
        body = check(authority["accepted_copy"])
        candidate = check(authority["candidate"])
        assert body["path"] == b["accepted_body"]
        assert candidate["path"] == b["exact_candidate_suffix"]
        assert raw(body["path"]).endswith(raw(candidate["path"]))
        bindings.append({
            "authority_json": b["authority_json"], "authority_md": b["authority_md"],
            "accepted_body": body, "exact_candidate_suffix": candidate,
            "historical_occurrences_bound_not_recopied": b["historical_occurrences_bound_not_recopied_or_replayed"],
            "historical_paths_bound_not_recopied": b["historical_paths_bound_not_recopied_or_replayed"],
            "operative": b["operative"],
        })
    records.append(check(PARENT))
    parent = obj(PARENT["path"])
    assert parent["ENTIRE_files_including_this_freeze"] == 14
    assert len(parent["payloads"]) == 13
    records += [check(r) for r in parent["payloads"]]
    assert len(records) == 52
    dedup = {}
    for record in records:
        assert record["path"] not in dedup or dedup[record["path"]] == record
        dedup[record["path"]] = record
    unique = sorted(dedup.values(), key=lambda r: r["path"])
    parent_summary = {
        **PARENT, "payloads_verified": 13, "ENTIRE_files": 14,
        "parent_current_occurrences_bound_not_recopied": parent["current_declared_fingerprint_occurrences_verified"],
        "parent_current_unique_paths_bound_not_recopied": parent["current_deduplicated_paths_verified"],
        "parent_current_summary_sha256": parent["current_deduplicated_fingerprint_digest_sha256"],
    }
    return records, unique, bindings, parent_summary


def labels():
    content = raw(P + "ledger-v1.md").decode()
    assert [int(x) for x in re.findall(r"(?m)^(\d+)\. ", content)] == list(range(1, 65))
    assert len(re.findall(r"(?m)^\d+\. \*\*PASS", content)) == 64
    issues = raw(P + "issues-v1.md").decode()
    assert len(re.findall(r"(?m)^## R13A-N\d", issues)) == 7
    source = obj(P + "sources-v1.json")
    assert source["whole_obligations"] == 64
    assert source["substantive_defects"] == source["required_repairs"] == 0
    assert source["closed_scope_notes"] == 7
    exposure = source["peer_exposure"]
    for k in (
        "corresponding_NEW_root_R13_math_conclusion_or_finding_seen",
        "corresponding_NEW_root_R13_file_or_hash_record_read",
        "corresponding_NEW_root_R13_metadata_content_read",
        "new_root_user_commentary_opened_or_disposition_seen",
    ):
        assert exposure[k] is False
    assert exposure["administrative_assignment_guard_and_whole_freeze_dates_counts_seen"] is True
    meter = source["authoritative_weekly_telemetry"]
    assert meter["reset_unix"] == 1792874445
    assert meter["used_percent_TOTAL"] < meter["ceiling_TOTAL_percent"] == 90
    assert source["independently_verified_effective_settings"] is None
    assert source["mathematical_program_CAS_scan_test_certificate_author_or_source_replay"] is False
    return source


def prepare():
    records, unique, bindings, parent = protected()
    labels()
    put("baseline-v1.json", {
        "created_at_utc": now(),
        "purpose": "Necessary current fingerprints and compact parent bindings only; no mathematical proof",
        "protected_occurrences": len(records), "protected_unique_paths": len(unique),
        "canonical_deduplicated_sha256": digest(unique),
        "protected_fingerprints": unique,
        "groups": {"ENTIRE_author": 11, "author_necessary_old_declared": 27, "immediate_own_parent": 14},
        "accepted_bindings": bindings, "immediate_own_parent": parent,
        "author_historical_inventory_bound_not_recopied": {
            "baseline": fp(AUTHOR + "baseline-v1.json"),
            "declared_occurrences": 27, "declared_paths": 27,
            "summary_sha256": obj(AUTHOR + "baseline-v1.json")["canonical_protected_summary_sha256"],
        },
        "historical_inventory_recopied_or_recursively_replayed": False,
        "forbidden_NEW_peer_prefix_never_read_or_hashed": FORBIDDEN,
    })
    put("input-validation-v1.json", {
        "verified_at_utc": now(), "metadata_ONLY_not_mathematical_proof": True,
        "protected_occurrences_unchanged": len(records), "protected_unique_paths_unchanged": len(unique),
        "ENTIRE_author11_and_own_parent14_fingerprints_verified": True,
        "author_necessary_old_declared27_verified": True,
        "current_accepted_MDJSON_body_exact_suffix_bindings_checked": 3,
        "review_ledger_ordered1_to64_and_seven_scope_note_labels": True,
        "no_corresponding_NEW_root_R13_file_hash_or_findings_accessed": True,
        "all_payload_model_readback_and_separate_postfreeze_verify_required": True,
    })
    put("metadata-v1.json", {
        "created_at_utc": now(), "reviewer": "/root/review_2021_reasoning_j15_r2",
        "role": "OTHER initially blind ENTIRE WHOLE R13 review2", "whole_obligations": 64,
        "payloads_to_freeze": len(SUFFIXES), "ENTIRE_files_including_manifest": len(SUFFIXES) + 1,
        "substantive_defects": 0, "required_repairs": 0, "closed_scope_notes": 7,
        "recommendation_only_no_promotion": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "NEW_admin_code_only_no_math_or_author_rerun": True,
        "no_old_shared_Git_cache_write_spawn_contact_charge_or_bypass": True,
        "exposure_precision": "Administrative guard/freeze dates and counts received; no new corresponding math finding, file, hash record, metadata content or user disposition seen.",
        "protected_occurrences": len(records), "protected_unique_paths": len(unique),
        "canonical_deduplicated_sha256": digest(unique),
        "FULL_model_readback_before_manifest_required": True,
        "manifest_FULL_readback_then_SEPARATE_verify_required": True,
    })
    print(json.dumps({"prepared": True, "protected_occurrences": len(records), "protected_unique_paths": len(unique)}))


def check_baseline():
    records, unique, bindings, parent = protected()
    data = obj(P + "baseline-v1.json")
    assert data["protected_fingerprints"] == unique
    assert data["protected_occurrences"] == len(records)
    assert data["canonical_deduplicated_sha256"] == digest(unique)
    assert data["accepted_bindings"] == bindings and data["immediate_own_parent"] == parent
    labels()
    return data


def freeze(readback_complete):
    assert readback_complete, "Finish FULL model readback of all ten payloads first"
    data = check_baseline()
    payloads = [fp(P + suffix) for suffix in SUFFIXES]
    put("manifest-v1.json", {
        "frozen_at_utc": now(),
        "status": "initial OTHER ENTIRE WHOLE R13 review2 complete; coordinator decision pending",
        "whole_obligations": 64, "payload_files": 10, "ENTIRE_files": 11,
        "FULL_payload_model_readback_complete_before_manifest": True,
        "manifest_FULL_readback_and_SEPARATE_verify_required_before_identity_handoff": True,
        "substantive_defects": 0, "required_repairs": 0, "closed_scope_notes": 7,
        "candidate_remains_unpromoted_by_reviewer": True,
        "author_entire_freeze": AUTHOR_MANIFEST,
        "immediate_own_parent": data["immediate_own_parent"],
        "compact_baseline": fp(P + "baseline-v1.json"),
        "protected_occurrences": data["protected_occurrences"],
        "protected_unique_paths": data["protected_unique_paths"],
        "canonical_deduplicated_sha256": data["canonical_deduplicated_sha256"],
        "no_corresponding_NEW_root_R13_review_access_through_ENTIRE_initial": True,
        "identity_only_handoff_until_BOTH_ENTIRE_initials_confirmed": True,
        "no_mathematical_executable_scan_CAS_author_or_source_rerun": True,
        "payloads": payloads,
    })
    print(json.dumps({"manifest": fp(P + "manifest-v1.json"), "initial": payloads[0], "ENTIRE_files": 11, "whole_obligations": 64}))


def verify():
    data = check_baseline()
    manifest = obj(P + "manifest-v1.json")
    assert manifest["compact_baseline"] == fp(P + "baseline-v1.json")
    assert manifest["canonical_deduplicated_sha256"] == data["canonical_deduplicated_sha256"]
    assert [r["path"] for r in manifest["payloads"]] == [P + s for s in SUFFIXES]
    for record in manifest["payloads"]:
        check(record)
    print(json.dumps({
        "separate_postfreeze_verify": "PASS", "verified_at_utc": now(),
        "manifest": fp(P + "manifest-v1.json"), "initial": manifest["payloads"][0],
        "ENTIRE_files": 11, "ALL_obligations": 64,
        "protected_occurrences": data["protected_occurrences"], "protected_unique_paths": data["protected_unique_paths"],
        "no_NEW_corresponding_root_R13_review_read_or_hashed": True,
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
