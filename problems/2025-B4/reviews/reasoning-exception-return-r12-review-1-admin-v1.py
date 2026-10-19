#!/usr/bin/env python3
"""NEW documentary-only ET12 whole1 helper. No mathematical execution.

Writes exclusively this assigned review prefix. Reads exact author/current
input paths and the immediate OWN parent manifest; never inventories peers.
No constructor/source/old executable is invoked. Hashes/JSON/labels only.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/reasoning-exception-return-r12-review-1-"
BASELINE = PREFIX + "baseline-v1.json"
MANIFEST = PREFIX + "manifest-v1.json"
PAYLOADS = [PREFIX + x for x in (
    "initial-v1.md", "sources-v1.json", "admin-v1.py", "baseline-v1.json")]
AUTHOR = {
    "path": "problems/2025-B4/notes/reasoning-exception-return-r12-freeze-v1.json",
    "bytes": 2517,
    "sha256": "79e7c6bd6746a38b1cceb44a773f7b267795560ed7439a88564994ec93e3d68b"}
PARENT = {
    "path": "problems/2019-B4/notes/reasoning-critical-law-return-r16-freeze-v1.json",
    "bytes": 2415,
    "sha256": "b293b0aba2ac626219e7e4fd170d6a9780528446a860d7cada5edee81cc3ccda"}

def now():
    return datetime.now(timezone.utc).isoformat()

def read_json(path):
    return json.loads((ROOT / path).read_text())

def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}

def check(row):
    actual = fingerprint(row["path"])
    if actual != row:
        raise RuntimeError("documentary fingerprint mismatch: " + row["path"])
    return actual

def write_new(path, obj):
    if not path.startswith(PREFIX):
        raise RuntimeError("write outside exclusive review prefix")
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")

def digest(rows):
    unique = {row["path"]: row for row in rows}
    ordered = [unique[key] for key in sorted(unique)]
    raw = json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(unique),
            "canonical_deduplicated_sha256": hashlib.sha256(raw).hexdigest()}

def labels():
    text = (ROOT / PAYLOADS[0]).read_text()
    rows = re.findall(r"^\| ET12-O(\d\d) \|", text, flags=re.M)
    if rows != [f"{n:02}" for n in range(1, 37)]:
        raise RuntimeError("missing, duplicate or unordered documentary obligation label")
    return len(rows)

def init():
    check(AUTHOR)
    check(PARENT)
    author = read_json(AUTHOR["path"])
    author_baseline = read_json("problems/2025-B4/notes/reasoning-exception-return-r12-baseline-v1.json")
    parent = read_json(PARENT["path"])
    guards = [AUTHOR] + author["payloads"] + author_baseline["necessary_immutable_guards"] + [PARENT]
    for row in guards:
        check(row)
    labels()
    read_json(PAYLOADS[1])
    write_new(BASELINE, {
        "created_UTC": now(),
        "status": "independent initial review; coordinator reconciliation pending",
        "reviewer": "/root/review_2017_coarsening_r1",
        "constructor": "/root/review_2022_complexity_r2",
        "ALL_obligations": 36,
        "ENTIRE_author_files": 5,
        "necessary_immutable_guards_ONCE": guards,
        "guard_summary": digest(guards),
        "immediate_OWN_parent_manifest": PARENT,
        "parent_guard_summary_BOUND_NOT_EXPANDED": {
            "occurrences": parent["guard_occurrences"],
            "unique_paths": parent["guard_unique_paths"],
            "canonical_deduplicated_sha256": parent["guard_digest_sha256"]},
        "parent_payloads_not_reinventoried_or_rehashed": True,
        "mutable_maps_NOT_immutable_guards": True,
        "ENTIRE_author5_MODEL_read_including_code_ALLmetadata": True,
        "FULL_R10_GR11_bodies_EACH_current_MDJSON_MODEL_read": True,
        "old_C_R10_constructor_GR11_reviewer_NOT_NEW_self_recertification": True,
        "NEW_ET12_peer_finding_file_inventory_hash_metadata_access": False,
        "findings_EMBARGOED_until_explicit_BOTH_ENTIRE_confirmation": True,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_backend_readback": None,
        "quota": {"usedPercent": 79, "observed_UTC": "2026-10-19 02:07:53 UTC",
                  "resetsAt": 1792874445, "windowDurationMins": 10080,
                  "ordinaryUsageAllowed": True, "legacy_by_limit_agree": True,
                  "TOTAL_ceiling": 90, "review_integration_reserve": True,
                  "automatic_later_window_spending": False},
        "mathematical_program_CAS_scan_test_old_author_source_helper_freezer_replay": False,
        "Git_shared_old_cache_mutation_spawn_charge_contact_bypass": False})
    print(json.dumps({"baseline": fingerprint(BASELINE), "guards": digest(guards),
                      "ALL_obligation_labels": 36}))

def freeze():
    if "--FULL-final-payload-MODEL-readbacks-completed" not in sys.argv:
        raise RuntimeError("FULL final model readbacks must precede manifest creation")
    base = read_json(BASELINE)
    for row in base["necessary_immutable_guards_ONCE"]:
        check(row)
    labels()
    write_new(MANIFEST, {
        "frozen_UTC": now(),
        "status": "independent initial review; coordinator reconciliation pending",
        "reviewer": "/root/review_2017_coarsening_r1",
        "review_number": 1,
        "ENTIRE_files": 5,
        "ALL_obligations": 36,
        "payloads": [fingerprint(path) for path in PAYLOADS],
        "guard_summary": base["guard_summary"],
        "immediate_OWN_parent_manifest": PARENT,
        "FULL_final_ALL4_payload_MODEL_readbacks_completed": True,
        "FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED": True,
        "NEW_ET12_peer_finding_file_inventory_hash_metadata_access": False,
        "findings_EMBARGOED_until_explicit_BOTH_ENTIRE_confirmation": True,
        "requested": base["requested"],
        "independent_effective_backend_readback": None,
        "quota": base["quota"],
        "no_mathematical_program_or_old_replay": True,
        "Git_shared_old_cache_mutation": False})
    print(json.dumps({"manifest": fingerprint(MANIFEST)}))

def verify():
    manifest = read_json(MANIFEST)
    for row in manifest["payloads"]:
        check(row)
    base = read_json(BASELINE)
    for row in base["necessary_immutable_guards_ONCE"]:
        check(row)
    if digest(base["necessary_immutable_guards_ONCE"]) != manifest["guard_summary"]:
        raise RuntimeError("guard summary mismatch")
    if labels() != manifest["ALL_obligations"]:
        raise RuntimeError("obligation-label mismatch")
    read_json(PAYLOADS[1])
    print(json.dumps({"SEPARATE_readonly_documentary_verify_UTC": now(),
                      "PASS": True, "ENTIRE_files": 5, "ALL_obligations": 36,
                      "guards": manifest["guard_summary"],
                      "manifest": fingerprint(MANIFEST),
                      "payloads": manifest["payloads"],
                      "NEW_ET12_peer_access": False}))

if __name__ == "__main__":
    modes = {"init": init, "freeze": freeze, "verify": verify}
    if len(sys.argv) < 2 or sys.argv[1] not in modes:
        raise SystemExit("use init | freeze --FULL-final-payload-MODEL-readbacks-completed | verify")
    modes[sys.argv[1]]()
