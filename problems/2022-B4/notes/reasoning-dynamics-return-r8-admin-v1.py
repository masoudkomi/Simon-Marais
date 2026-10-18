#!/usr/bin/env python3
"""NEW D8 byte/JSON/label administration only; no mathematical execution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/notes/reasoning-dynamics-return-r8-"
PARENT = "problems/2020-B4/notes/reasoning-class-return-sq15-freeze-v1.json"
PARENT_EXPECTED = (3677, "bc7bb2ef06d6e90dc083841fac5853209b7a45e36bc0ae5b16e512efa7c94975")
PAYLOADS = [
    "candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "failed-routes-v1.md", "issues-v1.md", "sources-v1.md",
    "sources-v1.json", "worklog-v1.md", "code-log-v1.md", "admin-v1.py",
    "baseline-v1.json", "input-validation-v1.json", "metadata-v1.json",
]
ACCEPTED = [
    ("D7", "problems/2022-B4/reviews/reasoning-dynamics-return-r7-acceptance",
     "75f12e12027c50df48eba74149bf4993edfd1ff922eac8a130dfc0655abfe98f"),
    ("CF", "problems/2022-B4/reviews/reasoning-fiber-return-r5-acceptance",
     "ab4158f60b3412ace615be689cd61d9384f753319c312e776831392f97a37ef8"),
    ("Qv3", "problems/2022-B4/reviews/reasoning-complexity-return-r9-v3-acceptance",
     "18e681d69b29d3495fea0cc2a29dbcb8a9c34db60644b981b3f653d666bef4ad"),
    ("D6", "problems/2022-B4/reviews/reasoning-dynamics-return-r6-acceptance",
     "a9f9e12a3c814a4c1098778acaec1bfd13eb631be0837b5550d767715d19b0c8"),
]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    p = (ROOT / path).resolve()
    if not p.is_relative_to(ROOT):
        raise ValueError("outside workspace")
    return p.read_bytes()


def record(path):
    b = raw(path)
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def checked(item):
    actual = record(item["path"])
    if actual != item:
        raise ValueError(f"fingerprint mismatch: {item['path']}")
    return actual


def readjson(path):
    return json.loads(raw(path))


def write(suffix, obj):
    path = PREFIX + suffix
    data = (json.dumps(obj, ensure_ascii=False, indent=2) + "\n").encode()
    with (ROOT / path).open("xb") as f:
        f.write(data)
    return record(path)


def label_check():
    text = raw(PREFIX + "obligations-v1.md").decode()
    labels = re.findall(r"^\| (D8-\d\d) \|", text, re.M)
    expected = [f"D8-{i:02d}" for i in range(1, 49)]
    if labels != expected:
        raise ValueError("ALL48 exact obligation label/order mismatch")
    return labels


def canonical(rows):
    data = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(data).hexdigest()


def prepare():
    checked({"path": PARENT, "bytes": PARENT_EXPECTED[0], "sha256": PARENT_EXPECTED[1]})
    parent = readjson(PARENT)
    if parent["ENTIRE_files"] != 13 or len(parent["payloads"]) != 12:
        raise ValueError("immediate own parent coverage mismatch")
    guard_occurrences = []
    guard_occurrences.append(record("AGENTS.md"))
    if guard_occurrences[0]["sha256"] != "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff":
        raise ValueError("AGENTS fingerprint changed")
    guard_occurrences.append(record("problems/2022-B4/statement.md"))
    accepted_checks = []
    for name, authority, expected_sha in ACCEPTED:
        guard_occurrences.extend([record(authority + ".md"), record(authority + ".json")])
        obj = readjson(authority + ".json")
        body = checked(obj["accepted_copy"])
        if body["sha256"] != expected_sha:
            raise ValueError(f"wrong accepted body: {name}")
        candidate = checked(obj["candidate"])
        if not raw(body["path"]).endswith(raw(candidate["path"])):
            raise ValueError(f"accepted-copy suffix mismatch: {name}")
        guard_occurrences.extend([body, candidate])
        accepted_checks.append({"name": name, "authority": authority,
                                "accepted_body_verified": True,
                                "candidate_suffix_verified": True})
    guard_occurrences.extend([
        record("problems/2022-B4/notes/reasoning-dynamics-return-r7-failed-routes-v1.md"),
        record("problems/2022-B4/notes/reasoning-dynamics-return-r7-sources-v1.md"),
        record(PARENT),
    ])
    guard_occurrences.extend(checked(item) for item in parent["payloads"])
    unique = {}
    for item in guard_occurrences:
        if item["path"] in unique and unique[item["path"]] != item:
            raise ValueError("inconsistent duplicate guard")
        unique[item["path"]] = item
    rows = [unique[p] for p in sorted(unique)]
    labels = label_check()
    baseline = {
        "prepared_at_utc": now(), "status": "candidate proof - unverified",
        "immediate_own_parent": record(PARENT),
        "parent_ENTIRE_files": 13, "parent_payloads_verified": 12,
        "parent_historical_guard_inventory_recopied_or_rerun": False,
        "parent_historical_guard_summary_bound_by_parent_identity": {
            "occurrences": parent["necessary_guard_occurrences"],
            "unique_paths": parent["necessary_guard_unique_paths"],
            "canonical_sha256": parent["canonical_guard_sha256"],
        },
        "necessary_guard_occurrences": len(guard_occurrences),
        "necessary_guard_unique_paths": len(rows),
        "canonical_guard_sha256": canonical(rows), "guards": rows,
    }
    write("baseline-v1.json", baseline)
    write("input-validation-v1.json", {
        "validated_at_utc": now(), "necessary_guard_fingerprints": "PASS",
        "accepted_body_and_candidate_suffix_checks": accepted_checks,
        "immediate_own_parent_payloads": "12/12 PASS",
        "literal_obligations": len(labels), "mathematical_instance_evaluated": False,
    })
    write("metadata-v1.json", {
        "created_at_utc": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1", "constructor_excluded": True,
        "root_supplied_new_proof_inference": False,
        "claims": ["D8A", "D8B", "D8C", "D8D"], "whole_obligations": 48,
        "requested_model": "gpt-6.1-sol", "requested_reasoning": "max",
        "independently_verified_effective_settings": None,
        "authorized_weekly_reset": 1792874445, "TOTAL_weekly_ceiling_percent": 90,
        "last_transition_TOTAL_percent": 48, "automatic_next_window_authorized": False,
        "new_external_theorem_imported": False, "CF6_used": False,
        "mathematical_program_CAS_scan_old_replay": False,
        "only_NEW_assigned_prefix_written": True, "pending_tool_native_child": False,
        "NEW_corresponding_peer_material_accessed": False,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "FULL_final_ALL13_payload_model_readback_REQUIRED_before_freeze": True,
        "FULL_freeze_model_readback_then_SEPARATE_verify_REQUIRED": True,
    })
    print(json.dumps({"prepare": "PASS", "guards": len(rows),
                      "occurrences": len(guard_occurrences),
                      "canonical_guard_sha256": canonical(rows)}))


def baseline_check():
    b = readjson(PREFIX + "baseline-v1.json")
    for item in b["guards"]:
        checked(item)
    if canonical(b["guards"]) != b["canonical_guard_sha256"]:
        raise ValueError("baseline canonical mismatch")
    label_check()
    return b


def freeze():
    b = baseline_check()
    records = [record(PREFIX + suffix) for suffix in PAYLOADS]
    for item in records:
        if item["path"].endswith(".json"):
            readjson(item["path"])
    obj = {
        "frozen_at_utc": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1", "constructor_excluded": True,
        "claims": ["D8A", "D8B", "D8C", "D8D"], "whole_obligations": 48,
        "root_supplied_new_proof_inference": False,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "immediate_own_parent": record(PARENT),
        "compact_baseline": record(PREFIX + "baseline-v1.json"),
        "payload_files": len(records), "ENTIRE_files": len(records) + 1,
        "FULL_final_ALL13_payload_model_readback_completed": True,
        "FULL_freeze_model_readback_then_SEPARATE_verify_REQUIRED": True,
        "necessary_guard_occurrences": b["necessary_guard_occurrences"],
        "necessary_guard_unique_paths": b["necessary_guard_unique_paths"],
        "canonical_guard_sha256": b["canonical_guard_sha256"],
        "mathematical_program_CAS_scan_replay": False,
        "new_external_theorem_imported": False, "payloads": records,
    }
    item = write("freeze-v1.json", obj)
    print(json.dumps({"freeze": item}))


def verify():
    path = PREFIX + "freeze-v1.json"
    f = readjson(path)
    expected_paths = [PREFIX + suffix for suffix in PAYLOADS]
    if [x["path"] for x in f["payloads"]] != expected_paths:
        raise ValueError("ENTIRE payload coverage mismatch")
    for item in f["payloads"]:
        checked(item)
    b = baseline_check()
    if f["canonical_guard_sha256"] != b["canonical_guard_sha256"]:
        raise ValueError("freeze/baseline mismatch")
    if f["whole_obligations"] != 48 or f["ENTIRE_files"] != 14:
        raise ValueError("ENTIRE count mismatch")
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "verified_at_utc": now(),
                      "ENTIRE_files": 14, "ALL_obligations": 48,
                      "necessary_guard_occurrences": b["necessary_guard_occurrences"],
                      "necessary_guard_unique_paths": b["necessary_guard_unique_paths"],
                      "main": record(PREFIX + "candidate-v1.md"),
                      "freeze": record(path)}, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in {"prepare", "freeze", "verify"}:
        raise SystemExit("choose prepare|freeze|verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[sys.argv[1]]()
