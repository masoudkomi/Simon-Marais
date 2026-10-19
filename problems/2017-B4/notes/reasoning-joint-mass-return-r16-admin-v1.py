#!/usr/bin/env python3
"""NEW documentary-only JM16 helper: exact bytes/JSON/labels, no mathematics.

Only this assigned prefix can be written. Accepted inputs are each guarded
ONCE; the immediate OWN frozen parent is bound without historical expansion.
No other script, mathematical executable, peer inventory or network is used.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/notes/reasoning-joint-mass-return-r16-"
BASELINE = PREFIX + "baseline-v1.json"
FREEZE = PREFIX + "freeze-v1.json"
PAYLOADS = [PREFIX + part for part in (
    "candidate-v1.md", "sources-v1.json", "admin-v1.py", "baseline-v1.json")]
PARENT = {
    "path": "problems/2025-B4/reviews/reasoning-exception-return-r12-review-1-manifest-v1.json",
    "bytes": 2377,
    "sha256": "ab8caabc5434667f83f27566e5d75eeb525435539671696d0470344b8a6638ef"}
EXPECTED_BODIES = {
    "reasoning-pressure-return-r11": (26687, "56688cd6030db910fbbc9162436b25acbf61a69869e2501dbd6f50b088bc3b60"),
    "reasoning-concentration-return-r12": (24123, "15823ad1a7c54b8e06de3692f19d3395d2458786dcb8d2d51a2eb3c592734554"),
    "reasoning-lower-return-r14": (24422, "88eed98d9ae634700fd23d571aad68cb4c59fd2fcd45e44dc48f9634c3d208c7"),
    "reasoning-joint-return-r15": (35630, "b35e0a5b0bbefbafece8467d010ffe6fdb33629ee45c76aeff78bfdef5e05569")}

def now():
    return datetime.now(timezone.utc).isoformat()

def load(path):
    return json.loads((ROOT / path).read_text())

def fp(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

def check(row):
    if fp(row["path"]) != row:
        raise RuntimeError("documentary mismatch: " + row["path"])

def write_new(path, obj):
    if not path.startswith(PREFIX):
        raise RuntimeError("exclusive-prefix write violation")
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")

def summary(rows):
    unique = {row["path"]: row for row in rows}
    raw = json.dumps([unique[p] for p in sorted(unique)],
                     sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(unique),
            "canonical_deduplicated_sha256": hashlib.sha256(raw).hexdigest()}

def labels():
    text = (ROOT / PAYLOADS[0]).read_text()
    rows = re.findall(r"^\| JM16-O(\d\d) \|", text, flags=re.M)
    if rows != [f"{n:02}" for n in range(1, 33)]:
        raise RuntimeError("documentary obligation labels missing/duplicate/out of order")
    return len(rows)

def init():
    check(PARENT)
    paths = ["AGENTS.md", "problems/2017-B4/statement.md"]
    for name, (size, sha) in EXPECTED_BODIES.items():
        body = "problems/2017-B4/proofs/reviewed-" + name + "-v1.1.md"
        check({"path": body, "bytes": size, "sha256": sha})
        authority = "problems/2017-B4/reviews/" + name + "-acceptance"
        paths += [body, authority + ".md", authority + ".json"]
        record = load(authority + ".json")
        if record["accepted_copy"] != {"path": body, "bytes": size, "sha256": sha}:
            raise RuntimeError("current accepted-copy metadata mismatch")
    paths += [PARENT["path"]]
    rows = [fp(path) for path in paths]
    parent = load(PARENT["path"])
    labels()
    load(PAYLOADS[1])
    write_new(BASELINE, {
        "created_UTC": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1",
        "constructor_excluded_from_two_OTHER_whole_audits": True,
        "ALL_obligations": 32, "necessary_guards_ONCE": rows,
        "guard_summary": summary(rows), "immediate_OWN_parent_manifest": PARENT,
        "parent_guard_summary_BOUND_NOT_EXPANDED": parent["guard_summary"],
        "parent_payloads_NOT_reinventoried_or_rehashed": True,
        "FULL_four_accepted_bodies_EACH_current_MDJSON_MODEL_read": True,
        "older_C_construction_review_roles_not_self_recertification": True,
        "root_NEW_inference_contribution": False,
        "mutable_research_maps_NOT_immutable_guards": True,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_backend_readback": None,
        "quota": {"usedPercent": 81, "observed_UTC": "2026-10-19 02:20:32 UTC",
                  "resetsAt": 1792874445, "windowDurationMins": 10080,
                  "ordinaryUsageAllowed": True, "legacy_by_limit_agree": True,
                  "TOTAL_ceiling": 90, "review_integration_reserve": True,
                  "automatic_later_window_spending": False},
        "NEW_ET12_peer_file_inventory_hash_metadata_access": False,
        "root_R13_tensor_or_R26_exploration_access": False,
        "mathematical_program_CAS_scan_test_optimizer_source_author_old_helper_certificate_replay": False,
        "Git_shared_old_cache_mutation_spawn_charge_contact_bypass": False})
    print(json.dumps({"baseline": fp(BASELINE), "guards": summary(rows),
                      "ALL_documentary_labels": 32}))

def freeze():
    if "--FULL-final-payload-MODEL-readbacks-completed" not in sys.argv:
        raise RuntimeError("FULL final model readbacks must precede freeze")
    base = load(BASELINE)
    for row in base["necessary_guards_ONCE"]:
        check(row)
    labels()
    write_new(FREEZE, {
        "frozen_UTC": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1",
        "constructor_excluded": True, "two_OTHER_ENTIRE_whole_audits_required": True,
        "claims": ["JM16A", "JM16B", "JM16C"],
        "ENTIRE_files": 5, "ALL_obligations": 32,
        "payloads": [fp(path) for path in PAYLOADS],
        "guard_summary": base["guard_summary"], "immediate_OWN_parent_manifest": PARENT,
        "FULL_final_ALL4_payload_MODEL_readbacks_completed": True,
        "FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED": True,
        "requested": base["requested"], "independent_effective_backend_readback": None,
        "quota": base["quota"], "root_NEW_inference_contribution": False,
        "NEW_ET12_peer_file_inventory_hash_metadata_access": False,
        "root_R13_tensor_or_R26_exploration_access": False,
        "no_mathematical_program_or_old_replay": True,
        "Git_shared_old_cache_mutation": False})
    print(json.dumps({"freeze": fp(FREEZE)}))

def verify():
    manifest = load(FREEZE)
    for row in manifest["payloads"]:
        check(row)
    base = load(BASELINE)
    for row in base["necessary_guards_ONCE"]:
        check(row)
    if summary(base["necessary_guards_ONCE"]) != manifest["guard_summary"]:
        raise RuntimeError("guard summary mismatch")
    if labels() != manifest["ALL_obligations"]:
        raise RuntimeError("documentary label count mismatch")
    load(PAYLOADS[1])
    print(json.dumps({"SEPARATE_readonly_verify_UTC": now(), "PASS": True,
                      "ENTIRE_files": 5, "ALL_obligations": 32,
                      "freeze": fp(FREEZE), "payloads": manifest["payloads"],
                      "guard_summary": manifest["guard_summary"]}))

if __name__ == "__main__":
    modes = {"init": init, "freeze": freeze, "verify": verify}
    if len(sys.argv) < 2 or sys.argv[1] not in modes:
        raise SystemExit("use init | freeze --FULL-final-payload-MODEL-readbacks-completed | verify")
    modes[sys.argv[1]]()
