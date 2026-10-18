#!/usr/bin/env python3
"""Administrative preservation only: bytes/JSON/suffixes/labels, no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2022-B4/reviews/reasoning-fiber-return-r5-review-2-"
T = "problems/2022-B4/notes/reasoning-fiber-return-r5-"
PARENT = "problems/2020-B4/reviews/reasoning-Todd-return-r12-review-2-manifest-v1.json"
EXPECTED = [
    {"path": T + "candidate-v1.md", "bytes": 23177,
     "sha256": "789ed605351a9d913348add46b8b9c47734bb0809f8269798aa8d53760f46a7e"},
    {"path": T + "freeze-v1.json", "bytes": 2791,
     "sha256": "22283a8f95e7a2a489596a418b1dce4d9ab3f619296309b0ed33863fbd75c2ca"},
    {"path": PARENT, "bytes": 10534,
     "sha256": "78380846552c4da0202fb4b636674416d1bac2355fd4dacf8d1784e137d707aa"},
]
CONTENT = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "sources-v1.md",
           "sources-v1.json", "worklog-v1.md", "freeze-v1.py"]
GENERATED = ["baseline-v1.json", "metadata-v1.json", "input-validation-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def path(name):
    assert "reasoning-fiber-return-r5-review-1-" not in name, name
    value = (ROOT / name).resolve()
    assert value.is_relative_to(ROOT), name
    return value


def raw(name):
    return path(name).read_bytes()


def obj(name):
    return json.loads(raw(name))


def fp(name):
    data = raw(name)
    return {"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


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
    assert author["whole_obligations"] == 48
    assert author["constructor_file_count"] == 11 and len(author["artifacts"]) == 10
    author_rows = [fp(T + "freeze-v1.json")] + [check(row) for row in author["artifacts"]]
    old_rows = [check(row) for row in base["protected"]]
    assert len(old_rows) == base["protected_fingerprint_occurrences"] == 35
    assert len({row["path"] for row in old_rows}) == base["protected_unique_paths"] == 35
    assert digest(old_rows) == base["canonical_protected_summary_sha256"]
    accepted_rows, bindings = [], []
    for binding in base["accepted"]:
        authority = check(binding["authority"])
        body, candidate = check(binding["accepted_copy"]), check(binding["candidate"])
        assert raw(body["path"]).endswith(raw(candidate["path"]))
        md = fp(authority["path"].removesuffix(".json") + ".md")
        accepted_rows += [authority, md, body, candidate]
        bindings.append({"authority": authority, "authority_MD": md,
                         "accepted_copy": body, "candidate": candidate,
                         "exact_candidate_suffix": True})
    assert len(bindings) == 5
    parent = obj(PARENT)
    assert parent["whole_obligations"] == 72 and parent["files_including_manifest"] == 11
    assert len(parent["artifacts"]) == 10
    parent_rows = [fp(PARENT)] + [check(row) for row in parent["artifacts"]]
    all_rows = old_rows + author_rows + accepted_rows + parent_rows
    unique = {}
    for row in all_rows:
        assert unique.setdefault(row["path"], row) == row
    result = {
        "target_main": fp(T + "candidate-v1.md"),
        "constructor_freeze": fp(T + "freeze-v1.json"),
        "all11_constructor_files_exact": True,
        "author35_current_guard_rows": summary(old_rows),
        "accepted_current_bindings": bindings,
        "constructor_parent_bound_not_recursive": {
            "identity": check(author["immediate_own_parent"]),
            "declared_occurrences": base["compact_immutable_parent"]["declared_fingerprint_occurrences"],
            "deduplicated_paths": base["compact_immutable_parent"]["deduplicated_paths"],
            "sha256": base["compact_immutable_parent"]["canonical_summary_sha256"],
        },
        "own_immediate_parent_bound": {
            "identity": fp(PARENT), "all11_current_summary": summary(parent_rows),
            "older_summary_bound_not_replayed": parent["current_inputs_and_payloads_summary"],
            "not_CF_mathematical_premise": True,
        },
        "current_protected": [unique[key] for key in sorted(unique)],
        "current_summary": summary(all_rows),
    }
    return result, all_rows


def baseline():
    value, _ = current()
    value.update({"captured_utc": now(), "administrative_only": True,
                  "no_corresponding_NEW_root_CF_R1_access": True,
                  "compact_parents_no_growing_historical_inventory_recopy": True})
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
    wanted = [f"FR5-{index:02d}" for index in range(1, 49)]
    for name in (T + "obligations-v1.md", P + "ledger-v1.md"):
        assert re.findall(r"^\| (FR5-\d+) \|", raw(name).decode(), re.M) == wanted, name
    assert obj(P + "sources-v1.json")["whole_obligations"] == 48
    put("metadata-v1.json", {
        "created_utc": now(), "status": "ENTIRE initially blind OTHER WHOLE R2 recommendation; not promotion",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "C_sole_NEW_constructor_excluded": True,
        "whole_obligations": 48, "substantive_defects": 0, "unresolved_issues": 0,
        "required_author_repairs": 0, "closed_scope_notes": 7,
        "old_roles_disclosed_not_fresh_self_recertification": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "no_corresponding_NEW_root_CF_R1_finding_file_hash_metadata_access_through_ENTIRE_freeze": True,
        "identity_only_until_BOTH_ENTIRE_initials_confirmed": True,
        "no_math_code_CAS_scan_source_author_algorithm_certificate_rerun_or_native_child": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass_tool_wait_or_pending_job": True,
        "latest_own_authoritative_telemetry": obj(P + "sources-v1.json")["latest_own_authoritative_telemetry"],
    })
    put("input-validation-v1.json", {
        "checked_utc": now(), "administrative_only_not_mathematical_validation": True,
        "all11_author_files_35_current_guard_rows_five_accepted_suffixes_and_own_parent_verified": True,
        "all48_author_and_reviewer_FR5_labels_once_in_order": True,
        "current_summary": summary(rows), "errors": [],
    })
    artifacts = [fp(P + suffix) for suffix in CONTENT + GENERATED]
    put("manifest-v1.json", {
        "frozen_utc": now(), "status": "ENTIRE initially blind OTHER WHOLE R2 recommendation; not promotion",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "C_sole_NEW_constructor_excluded": True,
        "whole_obligations": 48, "substantive_defects": 0, "unresolved_issues": 0,
        "required_author_repairs": 0, "closed_scope_notes": 7,
        "target_main": base["target_main"], "target_constructor_freeze": base["constructor_freeze"],
        "exact_scope": "CF1-CF5 exact unconditional domains; CF6 ONLY under explicit tenfold FULL-canonical existence hypothesis",
        "no_termination_infinite_avoider_automatic_fiber_decidability_time_bound_canonical336_annual_or_novelty_claim": True,
        "ENTIRE_initial_ALL48_ledger_issues_sources_log_code_ALLmetadata_complete": True,
        "no_corresponding_NEW_root_CF_R1_finding_file_hash_metadata_access_through_ENTIRE_freeze": True,
        "identity_only_until_BOTH_ENTIRE_initials_confirmed": True,
        "old_roles_disclosed_no_fresh_self_recertification": True,
        "no_mathematical_executable_CAS_scan_author_source_or_certificate_rerun": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass_tool_wait_or_native_job": True,
        "baseline": fp(P + "baseline-v1.json"),
        "accepted_current_bindings": base["accepted_current_bindings"],
        "constructor_parent_bound_not_recursive": base["constructor_parent_bound_not_recursive"],
        "own_immediate_parent_bound": base["own_immediate_parent_bound"],
        "current_inputs_and_payloads_summary": summary(rows + artifacts),
        "compact_historical_parents_bound_not_recopied_or_recursively_reverified": True,
        "payloads": len(artifacts), "files_including_manifest": len(artifacts) + 1,
        "artifacts": artifacts,
        "ENTIRE_generated_metadata_full_readback_then_SEPARATE_postverification_required": True,
    })
    print(json.dumps({"mode": "freeze", "manifest": fp(P + "manifest-v1.json"),
                      "initial": fp(P + "initial-v1.md"), "files": len(artifacts) + 1}))


def verify():
    base, rows = validate_baseline()
    value = obj(P + "manifest-v1.json")
    assert value["whole_obligations"] == 48 and value["files_including_manifest"] == 11
    assert len(value["artifacts"]) == 10
    for row in value["artifacts"]:
        check(row)
    assert value["accepted_current_bindings"] == base["accepted_current_bindings"]
    assert summary(rows + value["artifacts"]) == value["current_inputs_and_payloads_summary"]
    print(json.dumps({"mode": "verify", "all_match": True, "all48": True,
                      "manifest": fp(P + "manifest-v1.json"), "initial": fp(P + "initial-v1.md"),
                      "files": value["files_including_manifest"],
                      "current": value["current_inputs_and_payloads_summary"]}))


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
