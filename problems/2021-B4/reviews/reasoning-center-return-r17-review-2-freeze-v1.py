#!/usr/bin/env python3
"""Preservation only: bytes, JSON, exact accepted suffixes and ordered labels."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2021-B4/reviews/reasoning-center-return-r17-review-2-"
T = "problems/2021-B4/notes/reasoning-center-return-r17-"
PARENT = "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-1-reaudit-v2-manifest.json"
EXPECTED = [
    {"path": T + "candidate-v1.md", "bytes": 18292,
     "sha256": "d5a11268bd506449f437cbe4fb4d281f26c2d8e1a0461d5bde7acd05b8a5784d"},
    {"path": T + "freeze-v1.json", "bytes": 3018,
     "sha256": "5e9d1e9fe34d7e5041f645700d2315e6a5fce38279be9cd9423ade4c7df8ca5f"},
    {"path": PARENT, "bytes": 7921,
     "sha256": "1f724dddd34742a46d5b9c51a9f4f4cebbf8ee57fa69b40ec116664e5ab11c12"},
]
CONTENT = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "sources-v1.md",
           "sources-v1.json", "worklog-v1.md", "freeze-v1.py"]
GENERATED = ["baseline-v1.json", "metadata-v1.json", "input-validation-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def path(name):
    assert "reasoning-center-return-r17-review-1-" not in name, name
    value = (ROOT / name).resolve()
    assert value.is_relative_to(ROOT), name
    return value


def raw(name):
    return path(name).read_bytes()


def obj(name):
    return json.loads(raw(name))


def fp(name):
    value = raw(name)
    return {"path": name, "bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}


def check(row):
    record = {key: row[key] for key in ("path", "bytes", "sha256")}
    assert fp(record["path"]) == record, record["path"]
    return record


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def summary(rows):
    unique = {}
    for row in rows:
        record = check(row)
        assert unique.setdefault(record["path"], record) == record
    return {"occurrences": len(rows), "unique_paths": len(unique),
            "sha256": digest([unique[key] for key in sorted(unique)])}


def put(suffix, value):
    with path(P + suffix).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


def current():
    for row in EXPECTED:
        check(row)
    author = obj(T + "freeze-v1.json")
    base = obj(T + "baseline-v1.json")
    assert author["whole_obligations"] == 60
    assert author["artifact_count_including_this_freeze"] == 12 and len(author["artifacts"]) == 11
    author_rows = [fp(T + "freeze-v1.json")] + [check(row) for row in author["artifacts"]]
    protected = [check(row) for row in base["protected"]]
    assert len(protected) == base["protected_fingerprint_occurrences"] == 43
    assert len({row["path"] for row in protected}) == base["protected_unique_paths"] == 43
    assert digest(protected) == base["canonical_protected_summary_sha256"]
    accepted_rows, bindings = [], []
    for binding in base["accepted_inputs"]:
        authority = check(binding["JSON_authority"])
        md = check(binding["MD_authority"])
        body = check(binding["accepted_copy"])
        candidate = check(binding["literal_immutable_candidate_suffix"])
        value = obj(authority["path"])
        assert value["status"] == "proved, independently reviewed scoped partial result"
        assert value["unresolved_substantive_issues"] == 0 and value["repair_required"] is False
        assert value["candidate"] == candidate and value["accepted_copy"] == body
        assert raw(body["path"]).endswith(raw(candidate["path"]))
        accepted_rows += [authority, md, body, candidate]
        bindings.append({"id": binding["id"], "JSON_authority": authority,
                         "MD_authority": md, "accepted_copy": body, "candidate": candidate,
                         "exact_candidate_suffix": True,
                         "historical_occurrences_bound_not_replayed": value["record_occurrences_verified"],
                         "historical_paths_bound_not_replayed": value["unique_paths_verified"]})
    assert len(bindings) == 7
    parent = obj(PARENT)
    assert parent["original_whole_obligations"] == 32 and parent["additional_repair_checks"] == 8
    assert parent["files_including_manifest"] == 11 and len(parent["artifacts"]) == 10
    parent_rows = [fp(PARENT)] + [check(row) for row in parent["artifacts"]]
    rows = protected + author_rows + accepted_rows + parent_rows
    result = {
        "target_main": fp(T + "candidate-v1.md"),
        "constructor_freeze": fp(T + "freeze-v1.json"),
        "all12_author_files_exact": True,
        "author43_necessary_current_guards": summary(protected),
        "accepted_current_bindings": bindings,
        "constructor_parent_bound_not_recursive": base["immediate_own_parent_compact_summary"],
        "own_immediate_parent_bound": {
            "identity": fp(PARENT), "all11_summary": summary(parent_rows),
            "older_summary_bound_not_replayed": parent["current_inputs_and_payloads_summary"],
            "not_R17_mathematical_premise": True,
        },
        "current_summary": summary(rows),
        "old_guard_details_preserved_in_exact_author_baseline_not_recopied": True,
    }
    return result, rows


def baseline():
    value, _ = current()
    value.update({"captured_utc": now(), "administrative_only": True,
                  "assigned_prefix_confirmed_unused_before_first_write": True,
                  "no_corresponding_NEW_root_R17_access": True,
                  "compact_parent_bindings_no_recursive_inventory_replay": True})
    put("baseline-v1.json", value)
    print(json.dumps({"mode": "baseline", "baseline": fp(P + "baseline-v1.json"),
                      "current": value["current_summary"]}))


def validate_baseline():
    base = obj(P + "baseline-v1.json")
    value, rows = current()
    for key in value:
        assert value[key] == base[key], key
    return base, rows


def freeze():
    base, rows = validate_baseline()
    wanted = [f"R17-{index:02d}" for index in range(1, 61)]
    for name in (T + "obligations-v1.md", P + "ledger-v1.md"):
        assert re.findall(r"^\|(R17-\d+)\|", raw(name).decode(), re.M) == wanted, name
    assert obj(P + "sources-v1.json")["whole_obligations"] == 60
    put("metadata-v1.json", {
        "created_utc": now(), "status": "ENTIRE initially blind OTHER WHOLE R2 recommendation; not promotion",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "C_sole_NEW_constructor_excluded": True,
        "whole_obligations": 60, "substantive_defects": 0, "unresolved_issues": 0,
        "required_author_repairs": 0, "closed_scope_dependency_notes": 8,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "old_authorship_review_roles_disclosed_no_fresh_self_recertification": True,
        "no_corresponding_NEW_root_R17_finding_file_hash_metadata_access_through_ENTIRE_freeze": True,
        "identity_only_until_BOTH_ENTIRE_initials_confirmed": True,
        "all48_affine_zeros_two_H7_products_and_actual_pullback_hand_reconstructed": True,
        "no_math_code_CAS_scan_source_author_algorithm_or_certificate_rerun": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass_wait_or_native_mathematical_job": True,
        "latest_own_authoritative_telemetry": obj(P + "sources-v1.json")["latest_own_authoritative_telemetry"],
    })
    put("input-validation-v1.json", {
        "checked_utc": now(), "administrative_only_not_mathematical_validation": True,
        "all12_author_files_43_current_guards_seven_accepted_suffixes_and_own_parent_verified": True,
        "all60_author_and_reviewer_labels_once_in_order": True,
        "current_summary": summary(rows), "errors": [],
    })
    artifacts = [fp(P + suffix) for suffix in CONTENT + GENERATED]
    put("manifest-v1.json", {
        "frozen_utc": now(), "status": "ENTIRE initially blind OTHER WHOLE R2 recommendation; not promotion",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "C_sole_NEW_constructor_excluded": True,
        "whole_obligations": 60, "substantive_defects": 0, "unresolved_issues": 0,
        "required_author_repairs": 0, "closed_scope_dependency_notes": 8,
        "ENTIRE_initial_ALL60_ledger_issues_sources_log_code_ALLmetadata_complete": True,
        "no_corresponding_NEW_root_R17_finding_file_hash_metadata_access_through_ENTIRE_freeze": True,
        "identity_only_until_BOTH_ENTIRE_initials_confirmed": True,
        "old_authorship_review_roles_disclosed_no_fresh_self_recertification": True,
        "exact_scope": "R17A strong pure-field support obstruction; R17B actual noQ* and forced middle unit; R17C entire actualm4T4/cubics excluded with EC8/9 refinement; R17D m3T4 needs unita10/H10 center without contradiction; exact(S),(W) throughout actual claims",
        "no_full_m3_m4_J15_degree20_annual_lift_height_or_priority_claim": True,
        "all48_affine_zeros_two_H7_products_and_actual_pullback_hand_reconstructed": True,
        "no_mathematical_code_CAS_scan_source_author_algorithm_or_certificate_rerun": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass_wait_or_native_mathematical_job": True,
        "baseline": fp(P + "baseline-v1.json"),
        "target_main": base["target_main"], "constructor_freeze": base["constructor_freeze"],
        "accepted_current_bindings": base["accepted_current_bindings"],
        "constructor_parent_bound_not_recursive": base["constructor_parent_bound_not_recursive"],
        "own_immediate_parent_bound": base["own_immediate_parent_bound"],
        "current_inputs_and_payloads_summary": summary(rows + artifacts),
        "compact_historical_guards_bound_by_exact_author_metadata_not_recopied": True,
        "payloads": len(artifacts), "files_including_manifest": len(artifacts) + 1,
        "artifacts": artifacts,
        "ENTIRE_generated_metadata_full_readback_then_SEPARATE_postverification_required": True,
    })
    print(json.dumps({"mode": "freeze", "manifest": fp(P + "manifest-v1.json"),
                      "initial": fp(P + "initial-v1.md"), "files": len(artifacts) + 1}))


def verify():
    base, rows = validate_baseline()
    value = obj(P + "manifest-v1.json")
    assert value["whole_obligations"] == 60 and value["files_including_manifest"] == 11
    assert len(value["artifacts"]) == 10
    for row in value["artifacts"]:
        check(row)
    assert value["accepted_current_bindings"] == base["accepted_current_bindings"]
    assert summary(rows + value["artifacts"]) == value["current_inputs_and_payloads_summary"]
    print(json.dumps({"mode": "verify", "all_match": True, "all60": True,
                      "manifest": fp(P + "manifest-v1.json"), "initial": fp(P + "initial-v1.md"),
                      "files": 11, "current": value["current_inputs_and_payloads_summary"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--baseline", action="store_true")
    group.add_argument("--freeze", action="store_true")
    group.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.baseline:
        baseline()
    elif args.freeze:
        freeze()
    else:
        verify()
