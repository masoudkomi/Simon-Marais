#!/usr/bin/env python3
"""NEW SQ16 documentary administration only; no mathematical computation.

Only the assigned NEW SQ16 prefix may be created. No existing file is
overwritten. Modes: prepare; freeze --model-readback-complete; verify.
The final mode is read-only and is to be run in a SEPARATE invocation.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-class-return-sq16-"
PARENT = "problems/2022-B4/reviews/reasoning-dynamics-return-r9-review-2-manifest-v1.json"
PARENT_ID = (4383, "e0748765ecc179de716b5cf25ca86412de3ca866de10122bb9325b1bd4c60d8f")
HUMAN = ["candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
         "issues-failures-v1.md", "sources-v1.md", "sources-v1.json", "worklog-v1.md"]
PAYLOAD = HUMAN + ["admin-v1.py", "baseline-v1.json", "input-validation-v1.json", "metadata-v1.json"]
BASELINE = PREFIX + "baseline-v1.json"
VALIDATION = PREFIX + "input-validation-v1.json"
METADATA = PREFIX + "metadata-v1.json"
FREEZE = PREFIX + "freeze-v1.json"
REQUESTED = {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True}
WEEKLY = {"at_utc": "2026-10-18 17:53:49 UTC", "method": "own same-awaited clock/get_usage_limits",
          "TOTAL_used_percent": 57, "window_minutes": 10080, "resetsAt": 1792874445,
          "ordinaryUsageAllowed": True, "legacy_by_limit_agree": True,
          "account_label": "029a8928...1334ac3a", "TOTAL_ceiling_percent": 90,
          "integration_reserve": True, "automatic_later_window_spending": False}
SPECS = [
    {"name": "corrected INTEGRAL SQ14", "stem": "reasoning-arithmetic-return-r14",
     "acceptance": "reasoning-arithmetic-return-r14-repair-v1.1-acceptance",
     "copy": "proofs/reviewed-reasoning-arithmetic-return-r14-v1.2.md",
     "copy_id": (30567, "0b9f21290c5ecc7833645db76d74ef6def1bbb010bd205b2bc1d3514a6ef7c3f"),
     "candidate_id": (23705, "55afd51e3f83be9f7f1291a9817499bf863d5dbff6900211a93446f169f8f8f7")},
    {"name": "repaired INTEGRAL SQ15", "stem": "reasoning-class-return-sq15",
     "acceptance": "reasoning-class-return-sq15-acceptance",
     "copy": "proofs/reviewed-reasoning-class-return-sq15-v1.1.md",
     "copy_id": (31963, "7367a7ee4dd98bed7c42acb1974e5cdf30a1d274702335aa0fc8d056b9880bdc"),
     "candidate_id": (25788, "4d2696117fa8f8af5760e5034b83602c780f44f81b839fc4bcb6a3086c4825bd")}
]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    target = (ROOT / path).resolve()
    assert target.is_relative_to(ROOT), "Path escapes workspace"
    return target.read_bytes()


def record(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def matches(expected):
    actual = record(expected["path"])
    assert actual == expected, (expected["path"], "fingerprint changed")
    return actual


def fixed(path, identity):
    return matches({"path": path, "bytes": identity[0], "sha256": identity[1]})


def obj(path):
    return json.loads(raw(path))


def declarations(value):
    """Count immutable parent declarations WITHOUT recursively copying them."""
    found = []
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and isinstance(value.get("bytes"), int) and re.fullmatch(r"[0-9a-f]{64}", str(value.get("sha256", ""))):
            found.append(value)
        for item in value.values():
            found.extend(declarations(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(declarations(item))
    return found


def summary(records):
    unique = {}
    for item in records:
        if item["path"] in unique:
            assert unique[item["path"]] == item
        unique[item["path"]] = item
    canonical = json.dumps([unique[x] for x in sorted(unique)], sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(records), "unique_paths": len(unique), "canonical_sha256": hashlib.sha256(canonical).hexdigest()}


def create(path, value):
    assert path.startswith(PREFIX), "Write outside exclusive NEW prefix"
    target = ROOT / path
    data = (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()
    with target.open("xb") as stream:
        stream.write(data)


def literal_checks():
    expected = [f"SQ16-{j:02d}" for j in range(1, 49)]
    for suffix in ["obligations-v1.md", "constructor-checks-v1.md"]:
        found = re.findall(r"^\|(SQ16-\d{2})\|", raw(PREFIX + suffix).decode(), re.M)
        assert found == expected, (suffix, "ALL48 literal labels")
    main = raw(PREFIX + "candidate-v1.md").decode()
    for claim in ["SQ16A", "SQ16B", "SQ16C"]:
        assert "**" + claim + " —" in main
    source = obj(PREFIX + "sources-v1.json")
    assert source["independent_effective_readback"] is None
    assert source["constructor_excluded_from_TWO_OTHER_reviews"] is True
    return {"whole_obligation_labels": 48, "separate_author_check_labels": 48,
            "proposed_claim_labels": ["SQ16A", "SQ16B", "SQ16C"], "mathematical_truth_checked_by_code": False}


def current_inputs():
    guard = [fixed("AGENTS.md", (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff")),
             record("problems/2020-B4/statement.md")]
    parents = []
    for spec in SPECS:
        base = "problems/2020-B4/"
        authority_path = base + "reviews/" + spec["acceptance"] + ".json"
        authority = obj(authority_path)
        accepted = fixed(base + spec["copy"], spec["copy_id"])
        candidate_path = base + "notes/" + spec["stem"] + "-candidate-v1.1.md"
        candidate = fixed(candidate_path, spec["candidate_id"])
        assert authority["candidate"] == candidate
        assert authority["accepted_copy"] == accepted
        assert raw(accepted["path"]).endswith(raw(candidate_path)), "Accepted suffix changed"
        authority_record = record(authority_path)
        guard.extend([accepted, candidate, authority_record,
                      record(base + "reviews/" + spec["acceptance"] + ".md"),
                      record(base + "notes/" + spec["stem"] + "-sources-v1.1.md"),
                      record(base + "notes/" + spec["stem"] + "-freeze-v1.1.json")])
        declared = declarations(authority)
        parents.append({"name": spec["name"], "immutable_authority": authority_record,
                        "parent_declared_fingerprints_bound_not_recopied": summary(declared),
                        "fresh_COMPLETE_body_and_each_authority_MD_JSON": True,
                        "candidate_suffix_byte_identical": True,
                        "fresh_independent_recertification_of_older_own_work": False})
    own = fixed(PARENT, PARENT_ID)
    parent = obj(PARENT)
    assert len(parent["payloads"]) == 9
    guard.append(own)
    guard.extend(matches(item) for item in parent["payloads"])
    assert parent["older_plus_new_own_paths_bound_transitively"] == 932
    parents.append({"name": "immediate own frozen D9 WHOLE2 preservation parent; NOT mathematical premise",
                    "immutable_manifest": own, "all9_declared_payloads_directly_checked": True,
                    "older_own_paths_bound_transitively": 932,
                    "parent_guard_summary_bound_not_recopied": parent["guard_summary"]})
    return guard, parents


def prepare():
    assert not (ROOT / FREEZE).exists()
    guard, parents = current_inputs()
    checked = literal_checks()
    create(BASELINE, {"prepared_at_utc": now(), "scope": "Necessary current immutable inputs and own parent only; no growing historical inventory recopy",
                      "records": guard, "guard_summary": summary(guard), "parents": parents,
                      "mutable_coordinator_research_and_references_read_not_frozen_as_worker_property": True,
                      "older_own_paths_bound_transitively": 932,
                      "older_plus_new12_own_paths_bound_transitively": 944})
    create(VALIDATION, {"validated_at_utc": now(), "PASS": True, "guard_summary": summary(guard),
                        "literal_documentary_checks": checked,
                        "current_accepted_scopes": "corrected INTEGRAL SQ14v1.2; repaired SQ15v1.1",
                        "parent_declarations_bound_by_immutable_metadata_not_recopied": True,
                        "source_binary_download_or_raw_hash_claim": False,
                        "old_source_author_freezer_replay": False})
    create(METADATA, {"created_at_utc": now(), "status": "candidate proof - unverified",
                      "constructor": "/root/review_2022_complexity_r2", "constructor_excluded": True,
                      "required_OTHER_initially_blind_ENTIRE_WHOLE_reviews": 2,
                      "root_NEW_proof_inference": False, "requested": REQUESTED,
                      "independent_effective_readback": None, "whole_obligations": 48,
                      "separate_author_hand_checks": 48, "closed_author_boundary_notes": 8,
                      "recorded_failed_stronger_routes": 6,
                      "claims": ["SQ16A actual rational integral content", "SQ16B complete even-H balanced factor obstruction", "SQ16C actual q8 sharp denominator and unbalanced divisor diagnostic"],
                      "FULL_norm_q_mixed_realization_odd_H_class_unit_gap_open": True,
                      "annual_or_new_parameter_or_priority_claim": False,
                      "older_own_roles": "SQ14/TD/L13/R8 and other2020 construction, not fresh independent self-review",
                      "known_q8_fractional_diagnostic_attribution": "A original SQ15 review/root relay/C overlap; explicit expression and new hand consequences here",
                      "ENTIRE_payload_files_before_freeze": 11, "ENTIRE_files_including_freeze": 12,
                      "administration_only_not_mathematical_certificate": True,
                      "no_mathematical_program_CAS_scan_test_source_author_old_replay": True,
                      "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
                      "pending_native_child_or_retrieval": False,
                      "immediate_own_parent": record(PARENT), "older_own_paths_bound_transitively": 932,
                      "older_plus_new_own_paths_bound_transitively": 944,
                      "weekly": WEEKLY,
                      "FULL_final_MODEL_readback_ALL11_then_freeze_readback_then_SEPARATE_verify_required": True})
    print(json.dumps({"prepare": "PASS", "new_metadata_files": [BASELINE, VALIDATION, METADATA], "guard_summary": summary(guard), **checked}, indent=2))


def check_baseline():
    baseline = obj(BASELINE)
    for item in baseline["records"]:
        matches(item)
    assert summary(baseline["records"]) == baseline["guard_summary"]
    return baseline


def freeze(readback):
    assert readback, "Actual FULL final MODEL readback must have completed first"
    baseline = check_baseline()
    checked = literal_checks()
    payload = [record(PREFIX + suffix) for suffix in PAYLOAD]
    create(FREEZE, {"frozen_at_utc": now(), "status": "candidate proof - unverified",
                    "constructor": "/root/review_2022_complexity_r2", "constructor_excluded": True,
                    "TWO_OTHER_initially_blind_ENTIRE_WHOLE_reviews_required": True,
                    "root_NEW_proof_inference": False, "requested": REQUESTED,
                    "independent_effective_readback": None, "whole_obligations": 48,
                    "separate_author_hand_checks": 48, "ENTIRE_files_including_freeze": 12,
                    "FULL_final_MODEL_readback_ALL11_payloads_code_ALLgenerated_metadata_completed": True,
                    "FULL_freeze_MODEL_readback_then_SEPARATE_readonly_verify_required": True,
                    "guard_summary": baseline["guard_summary"],
                    "immediate_own_parent": record(PARENT),
                    "older_own_paths_bound_transitively": 932,
                    "older_plus_new_own_paths_bound_transitively": 944,
                    "literal_documentary_checks": checked,
                    "new_proofs_no_annual_new_parameter_or_priority_claim": True,
                    "no_mathematical_program_CAS_scan_test_source_author_old_replay": True,
                    "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
                    "weekly": WEEKLY, "payloads": payload})
    print(json.dumps({"freeze": record(FREEZE), "main": payload[0], "ENTIRE_files": 12}, indent=2))


def verify():
    baseline = check_baseline()
    frozen = obj(FREEZE)
    assert len(frozen["payloads"]) == 11
    assert [x["path"] for x in frozen["payloads"]] == [PREFIX + x for x in PAYLOAD]
    for item in frozen["payloads"]:
        matches(item)
    literal_checks()
    assert frozen["guard_summary"] == baseline["guard_summary"]
    for suffix in ["sources-v1.json", "baseline-v1.json", "input-validation-v1.json", "metadata-v1.json", "freeze-v1.json"]:
        obj(PREFIX + suffix)
    print(json.dumps({"SEPARATE_readonly_verify_at_utc": now(), "PASS": True,
                      "ENTIRE_files": 12, "whole_obligations": 48,
                      "guard_summary": baseline["guard_summary"],
                      "main": record(PREFIX + "candidate-v1.md"), "freeze": record(FREEZE),
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
