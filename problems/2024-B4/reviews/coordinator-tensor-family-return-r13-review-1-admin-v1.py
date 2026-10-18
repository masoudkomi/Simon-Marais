#!/usr/bin/env python3
"""NEW own R13 review documentary binding only; no mathematical code.

Never execute/import an author/source/old program. Exact declared guards
only: no directory/peer inventory. Writes are exclusive NEW own-prefix
JSON; verify is SEPARATE and read-only.
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/coordinator-tensor-family-return-r13-review-1-"
AUTHOR = "problems/2024-B4/notes/coordinator-tensor-family-return-r13-"
BASELINE = PREFIX + "baseline-v1.json"
MANIFEST = PREFIX + "manifest-v1.json"
PAYLOADS = [PREFIX + suffix for suffix in (
    "report-v1.md", "sources-v1.json", "admin-v1.py", "baseline-v1.json"
)]
TARGET = {
    "path": AUTHOR + "freeze-v1.json",
    "bytes": 1327,
    "sha256": "43ca5babe90e2dcc1638273f9ce67a3fee21fc30b9d720968a80d5dadcd4123a",
}
PARENT = {
    "path": "problems/2021-B4/notes/reasoning-negative-return-r23-freeze-v1.json",
    "bytes": 3187,
    "sha256": "4edff0c97b5d7a180cba0ae4a9975470d35f8542ccb6f841201855f7b2cd054a",
}
FORBIDDEN = (
    "problems/2024-B4/reviews/coordinator-tensor-family-return-r13-review-2-",
    "problems/2021-B4/reviews/reasoning-negative-return-r23-review-",
)


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def checked_path(path):
    if not isinstance(path, str) or path.startswith("/") or ".." in pathlib.PurePosixPath(path).parts:
        raise ValueError("Expected exact repository-relative path")
    if path.startswith(FORBIDDEN):
        raise RuntimeError("Corresponding NEW peer access prohibited")
    return ROOT / path


def read_json(path):
    return json.loads(checked_path(path).read_text())


def record(path):
    raw = checked_path(path).read_bytes()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def verify_record(item):
    actual = record(item["path"])
    if actual != {key: item[key] for key in ("path", "bytes", "sha256")}:
        raise RuntimeError("Immutable fingerprint changed: " + item["path"])
    return actual


def declared_records(value):
    if isinstance(value, dict):
        if all(key in value for key in ("path", "bytes", "sha256")):
            yield {key: value[key] for key in ("path", "bytes", "sha256")}
        for child in value.values():
            yield from declared_records(child)
    elif isinstance(value, list):
        for child in value:
            yield from declared_records(child)


def summary(rows):
    unique = {}
    for item in rows:
        if item["path"] in unique and unique[item["path"]] != item:
            raise RuntimeError("Conflicting immutable records: " + item["path"])
        unique[item["path"]] = item
    canonical = [unique[path] for path in sorted(unique)]
    raw = json.dumps(canonical, sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(canonical),
            "canonical_deduplicated_sha256": hashlib.sha256(raw).hexdigest()}


def create_json(path, value):
    if not path.startswith(PREFIX):
        raise RuntimeError("Write outside NEW own review prefix")
    with checked_path(path).open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def collect_guards():
    target = verify_record(TARGET)
    author = read_json(TARGET["path"])
    author_payloads = [verify_record(item) for item in author["payloads"]]
    author_inputs = [verify_record(item) for item in read_json(AUTHOR + "baseline-v1.json")["input_records"]]
    source_inputs = [verify_record(item) for item in read_json(AUTHOR + "sources-v1.json")["input_records"]]
    authority_rows = []
    for path in (
        "problems/2024-B4/reviews/reasoning-frobenius-return-r10-acceptance.json",
        "problems/2024-B4/reviews/coordinator-tensor-return-r12-acceptance.json",
    ):
        for item in declared_records(read_json(path)):
            authority_rows.append(verify_record(item))
    parent = verify_record(PARENT)
    parent_payloads = [verify_record(item) for item in read_json(PARENT["path"])["payloads"]]
    parent_baseline = read_json("problems/2021-B4/notes/reasoning-negative-return-r23-baseline-v1.json")
    parent_direct = [verify_record(item) for item in parent_baseline["direct_records"]]
    rows = [target] + author_payloads + author_inputs + source_inputs + authority_rows + [parent] + parent_payloads + parent_direct
    return {
        "target": target,
        "target_all_payloads_verified": len(author_payloads),
        "target_baseline_occurrences_verified": len(author_inputs),
        "target_source_declared_occurrences_verified": len(source_inputs),
        "necessary_direct_records": [target] + author_payloads + author_inputs,
        "current_authority_declared_summary": summary(authority_rows),
        "compact_parent_binding": {
            "immediate_own_parent": parent,
            "parent_all_payloads_verified": len(parent_payloads),
            "parent_direct_immutable_guards_verified": len(parent_direct),
            "parent_historical_effective_summary_bound_NOT_recopied": parent_baseline["effective_current_immutable_summary"],
            "mutable_maps_only_parent_historical_observations_NOT_current_guards": True,
            "R23_mathematics_not_R13_premise_or_new_self_review": True,
        },
        "effective_fresh_guard_summary": summary(rows),
        "internal_rows_not_recopied": rows,
    }


def obligations():
    text = checked_path(PREFIX + "report-v1.md").read_text()
    labels = re.findall(r"^\|R13-O(\d\d)\|", text, re.M)
    if labels != [f"{index:02}" for index in range(1, 33)]:
        raise RuntimeError("Expected exactly32 ordered distinct literal ledger labels")
    return len(labels)


def prepare():
    if checked_path(BASELINE).exists() or checked_path(MANIFEST).exists():
        raise RuntimeError("Already prepared/frozen: preserve every byte")
    guards = collect_guards()
    guards.pop("internal_rows_not_recopied")
    create_json(BASELINE, {
        "created_UTC": now(), "role": "OTHER initially blind ENTIRE WHOLE1",
        "whole_obligations": obligations(), **guards,
        "corresponding_NEW_B_R13_finding_file_actual_inventory_hash_metadata_public_commentary_accessed": False,
        "peer_completion_information": "count/time-only administration, no peer filename/hash/disposition",
        "root_R23_peer_material_accessed": False,
        "NEW_R13_constructive_contribution": False,
        "OLD_roles_disclosed_not_independent_self_recertification": True,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_setting_readback": None,
        "latest_root_weekly": {"usedPercent": 69, "observed_UTC": "2026-10-18 23:14:52 UTC", "resetsAt": 1792874445, "ordinaryUsageAllowed": True, "TOTAL_ceiling": 90, "integration_reserve": True, "automatic_later_window": False},
        "mathematical_program_CAS_scan_test_source_author_old_replay": False,
        "Git_shared_old_cache_writes": False,
    })
    print(json.dumps({"prepare": "PASS", "baseline": record(BASELINE), "guards": guards["effective_fresh_guard_summary"]}, indent=2))


def check_baseline():
    old = read_json(BASELINE)
    for item in old["necessary_direct_records"]:
        verify_record(item)
    fresh = collect_guards()
    if fresh["effective_fresh_guard_summary"] != old["effective_fresh_guard_summary"]:
        raise RuntimeError("Necessary immutable guard summary changed")
    return old, fresh


def seal():
    if checked_path(MANIFEST).exists():
        raise RuntimeError("Already frozen: preserve every byte")
    old, fresh = check_baseline()
    payloads = [record(path) for path in PAYLOADS]
    create_json(MANIFEST, {
        "frozen_UTC": now(), "reviewer": "/root/review_2021_reasoning_j15_r2",
        "role": "OTHER initially blind ENTIRE WHOLE1",
        "whole_obligations": obligations(), "payload_count": 4, "ENTIRE_files": 5,
        "payloads": payloads,
        "effective_fresh_guard_summary": old["effective_fresh_guard_summary"],
        "compact_parent_historical_summary_bound": old["compact_parent_binding"]["parent_historical_effective_summary_bound_NOT_recopied"],
        "FULL_final_ALL4_payload_model_readback_completed": True,
        "FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED": True,
        "corresponding_NEW_B_R13_finding_file_actual_inventory_hash_metadata_public_commentary_accessed": False,
        "peer_completion_information": "count/time-only administration, no peer filename/hash/disposition",
        "NEW_R13_constructive_contribution": False,
        "root_R23_peer_material_accessed": False,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_setting_readback": None,
        "mathematical_program_CAS_scan_test_source_author_old_replay": False,
        "findings_and_peer_access_require_explicit_BOTH_ENTIRE_confirmation": True,
        "status": "Independent whole review recommendation only; root reconciliation required",
    })
    print(json.dumps({"seal": "PASS", "manifest": record(MANIFEST)}, indent=2))


def verify():
    manifest = read_json(MANIFEST)
    for item in manifest["payloads"]:
        verify_record(item)
    old, fresh = check_baseline()
    if obligations() != manifest["whole_obligations"]:
        raise RuntimeError("Ledger labels changed")
    protected = fresh["internal_rows_not_recopied"] + manifest["payloads"] + [record(MANIFEST)]
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "verified_UTC": now(),
        "manifest": record(MANIFEST), "ENTIRE_files": 5, "whole_obligations": 32,
        "protected_summary": summary(protected), "writes_performed": False,
        "corresponding_NEW_peer_access": False, "mathematical_program_or_old_replay": False}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("prepare", "seal", "verify"):
        raise SystemExit("Usage: NEW-own-review-admin prepare|seal|verify")
    {"prepare": prepare, "seal": seal, "verify": verify}[sys.argv[1]]()
