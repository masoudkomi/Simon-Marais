#!/usr/bin/env python3
"""Review preservation only: hashes, JSON, suffixes and labels; no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2020-B4/reviews/reasoning-Todd-return-r12-review-2-"
T = "problems/2020-B4/notes/reasoning-Todd-return-r12-"
OWN_PARENT = "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-1-manifest-v1.json"
EXPECTED = [
    {"path": T + "candidate-v1.md", "bytes": 29251,
     "sha256": "a799aa9add5799c2f6c7c265bdc256a2c3946f482618e6e0d0d828efa5e88bb9"},
    {"path": T + "freeze-v1.json", "bytes": 9167,
     "sha256": "cac7580782285028c7e71207097a3566232306a764fa7d174a7a1fd21973dcc0"},
    {"path": OWN_PARENT, "bytes": 6800,
     "sha256": "b3af3d1cd3372c4181753c4cc3724b9c99300b596d5dcdebd3bd398374cd0667"},
]
CONTENT = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "sources-v1.md",
           "sources-v1.json", "worklog-v1.md", "freeze-v1.py"]
GENERATED = ["baseline-v1.json", "metadata-v1.json", "input-validation-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def path(name):
    assert "reasoning-Todd-return-r12-review-1-" not in name, name
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
    wanted = {key: row[key] for key in ("path", "bytes", "sha256")}
    assert fp(row["path"]) == wanted, row["path"]
    return wanted


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def declared(value):
    result = []
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str) and isinstance(value.get("bytes"), int)
                and isinstance(value.get("sha256"), str) and len(value["sha256"]) == 64):
            result.append({key: value[key] for key in ("path", "bytes", "sha256")})
        for child in value.values():
            result.extend(declared(child))
    elif isinstance(value, list):
        for child in value:
            result.extend(declared(child))
    return result


def summary(values):
    unique = {}
    for row in values:
        record = check(row)
        assert unique.setdefault(record["path"], record) == record
    return {"occurrences": len(values), "unique_paths": len(unique),
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
    assert author["whole_obligations"] == 72
    assert author["new_constructor_files_including_freeze"] == 11
    assert len(author["artifacts"]) == 10
    author_payloads = [check(row) for row in author["artifacts"]]
    old_rows = [check(row) for row in base["protected_rows"]]
    assert len(old_rows) == base["necessary_fingerprint_occurrences"] == 37
    assert len({row["path"] for row in old_rows}) == base["protected_unique_paths"] == 37
    assert digest(old_rows) == base["canonical_protected_summary_sha256"]
    assert digest(old_rows) == author["canonical_protected_summary_sha256"]
    authority_rows, bindings = [], []
    for binding in author["accepted_authorities"]:
        authority_record = check(binding["authority"])
        value = obj(authority_record["path"])
        assert value["unresolved_substantive_issues"] == 0
        assert value["repair_required"] is False
        body, candidate = check(value["accepted_copy"]), check(value["candidate"])
        assert body == check(binding["accepted_body"])
        assert candidate == check(binding["exact_candidate_suffix"])
        assert raw(body["path"]).endswith(raw(candidate["path"]))
        records = declared(value)
        authority_rows += records
        bindings.append({
            "authority": authority_record, "body": body, "candidate": candidate,
            "role": binding["role"], "current_declared_summary": summary(records),
            "old_coordinator_occurrences_bound_not_replayed": value["record_occurrences_verified"],
            "old_coordinator_paths_bound_not_replayed": value["unique_paths_verified"],
        })
    assert len(bindings) == 5
    parent = obj(OWN_PARENT)
    assert parent["all32_reconstructed"] is True
    assert parent["files_including_manifest"] == 11 and len(parent["artifacts"]) == 10
    parent_rows = [fp(OWN_PARENT)] + [check(row) for row in parent["artifacts"]]
    values = old_rows + [fp(T + "freeze-v1.json")] + author_payloads + authority_rows + parent_rows
    protected = {}
    for row in values:
        assert protected.setdefault(row["path"], row) == row
    result = {
        "target_main": fp(T + "candidate-v1.md"),
        "constructor_freeze": fp(T + "freeze-v1.json"),
        "all11_constructor_files_match": True,
        "author37_current_guard_rows_verified": {
            "occurrences": 37, "paths": 37, "sha256": digest(old_rows)},
        "accepted_current_bindings": bindings,
        "constructor_immutable_parent_bound": {
            "manifest": check(author["immediate_own_parent"]),
            "older_own_paths_bound_transitively": author["older_own_paths_bound_transitively"],
            "older_plus_new_paths_bound_transitively": author["older_plus_new_own_paths_bound_transitively"],
            "no_recursive_historical_inventory_replay": True,
        },
        "own_immutable_immediate_parent": {
            "manifest": fp(OWN_PARENT), "all11_summary": summary(parent_rows),
            "older_current_summary_bound": parent["current_inputs_and_payloads_summary"],
            "not_R12_mathematical_premise": True,
            "no_recursive_historical_inventory_replay": True,
        },
        "protected_current": [protected[key] for key in sorted(protected)],
        "current_summary": summary(values),
    }
    return result, values


def baseline():
    value, _ = current()
    value.update({"captured_utc": now(), "administrative_only": True,
                  "no_corresponding_NEW_root_Todd_R1_finding_file_hash_metadata_access": True,
                  "compact_parents_not_growing_historical_inventory_recopy": True})
    put("baseline-v1.json", value)
    print(json.dumps({"mode": "baseline", "baseline": fp(P + "baseline-v1.json"),
                      "current": value["current_summary"]}))


def validate_baseline():
    base = obj(P + "baseline-v1.json")
    value, values = current()
    for key in value:
        assert value[key] == base[key], key
    return base, values


def freeze():
    base, values = validate_baseline()
    expected_labels = [str(index) for index in range(1, 73)]
    for name in (T + "obligations-v1.md", T + "constructor-checks-v1.md", P + "ledger-v1.md"):
        assert re.findall(r"^(\d+)\. ", raw(name).decode(), re.M) == expected_labels, name
    assert obj(P + "sources-v1.json")["whole_obligations"] == 72
    put("metadata-v1.json", {
        "created_utc": now(), "administrative_only": True,
        "reviewer": "/root/review_2021_reasoning_j15_r2", "B_sole_NEW_constructor_excluded": True,
        "status": "ENTIRE initially blind OTHER WHOLE R2 recommendation; not promotion",
        "whole_obligations": 72, "substantive_defects": 0, "unresolved_issues": 0,
        "required_author_repairs": 0, "closed_scope_notes": 7,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "prior_input_review_roles_disclosed_not_fresh_self_recertification": True,
        "no_corresponding_NEW_root_Todd_R1_finding_file_hash_metadata_access_through_ENTIRE_freeze": True,
        "identity_only_until_BOTH_ENTIRE_initials_confirmed": True,
        "no_mathematical_executable_CAS_scan_class_computation_author_source_or_certificate_rerun": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass_tool_wait_or_native_job": True,
        "latest_authoritative_own_telemetry": obj(P + "sources-v1.json")["latest_own_authoritative_telemetry"],
    })
    put("input-validation-v1.json", {
        "checked_utc": now(), "administrative_only": True,
        "all_current_fingerprints_match": True, "current_summary": summary(values),
        "all11_author_files_37_old_guard_rows_five_accepted_suffixes_verified": True,
        "all72_author_constructor_and_reviewer_labels_once_in_order": True,
        "all_metadata_checks_are_NOT_mathematical_validation": True, "errors": [],
    })
    artifacts = [fp(P + suffix) for suffix in CONTENT + GENERATED]
    put("manifest-v1.json", {
        "frozen_utc": now(), "status": "ENTIRE initially blind OTHER WHOLE R2 recommendation; not promotion",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "B_sole_NEW_constructor_excluded": True,
        "target_main": base["target_main"], "target_constructor_freeze": base["constructor_freeze"],
        "whole_obligations": 72, "substantive_defects": 0, "unresolved_issues": 0,
        "required_author_repairs": 0, "closed_scope_notes": 7,
        "ENTIRE_initial_ALL72_ledger_issues_sources_MD_JSON_log_code_ALLmetadata_complete": True,
        "no_corresponding_NEW_root_Todd_R1_finding_file_hash_metadata_access_through_ENTIRE_freeze": True,
        "identity_only_until_BOTH_ENTIRE_initials_confirmed": True,
        "old_roles_disclosed_accepted_inputs_not_freshly_self_recertified": True,
        "exact_scope": "TD1-TD5 prime p=Phi3(q),q>=2,fixed odd T containing all prime factors; refined actual class, exact interval, signed count and actual primary minimality",
        "no_new_q_class_size_bound_automatic_even_unit_correction_composite_assembler_annual_or_novelty": True,
        "no_mathematical_code_CAS_scan_class_computation_author_source_or_certificate_rerun": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass_tool_wait_or_native_job": True,
        "baseline": fp(P + "baseline-v1.json"),
        "accepted_current_bindings": base["accepted_current_bindings"],
        "constructor_immutable_parent_bound": base["constructor_immutable_parent_bound"],
        "own_immutable_immediate_parent": base["own_immutable_immediate_parent"],
        "current_inputs_and_payloads_summary": summary(values + artifacts),
        "historical_inventories_bound_not_recopied_or_recursively_reverified": True,
        "payloads": len(artifacts), "files_including_manifest": len(artifacts) + 1,
        "artifacts": artifacts,
        "ENTIRE_generated_metadata_full_readback_then_SEPARATE_postverification_required": True,
    })
    print(json.dumps({"mode": "freeze", "manifest": fp(P + "manifest-v1.json"),
                      "initial": fp(P + "initial-v1.md"), "files": len(artifacts) + 1}))


def verify():
    base, values = validate_baseline()
    value = obj(P + "manifest-v1.json")
    assert len(value["artifacts"]) == 10 and value["files_including_manifest"] == 11
    for row in value["artifacts"]:
        check(row)
    assert summary(values + value["artifacts"]) == value["current_inputs_and_payloads_summary"]
    assert value["accepted_current_bindings"] == base["accepted_current_bindings"]
    print(json.dumps({"mode": "verify", "all_match": True, "all72": True,
                      "manifest": fp(P + "manifest-v1.json"), "initial": fp(P + "initial-v1.md"),
                      "files": value["files_including_manifest"],
                      "current": value["current_inputs_and_payloads_summary"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    choices = parser.add_mutually_exclusive_group(required=True)
    choices.add_argument("--baseline", action="store_true")
    choices.add_argument("--freeze", action="store_true")
    choices.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.baseline:
        baseline()
    elif args.freeze:
        freeze()
    else:
        verify()
