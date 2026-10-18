#!/usr/bin/env python3
"""NEW RC10 documentary-only prepare/freeze/SEPARATE readonly verify.

No mathematical calculation, subprocess, network or author/old-code import.
Only literal label counts, JSON/byte/SHA integrity and compact parent binding.
All writes use unused exclusive-prefix paths and refuse every overwrite.
"""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd().resolve()
P = "problems/2022-B4/notes/reasoning-collision-return-r10-"
OWN_PARENT = "problems/2017-B4/reviews/reasoning-concentration-return-r12-review-1-manifest-v1.json"
PREMISES = [
    ("reasoning-dynamics-return-r9", "reviewed-reasoning-dynamics-return-r9-v1.1.md"),
    ("reasoning-dynamics-return-r7", "reviewed-reasoning-dynamics-return-r7-v1.1.md"),
    ("rational-base-shadow-return", "reviewed-rational-base-shadow-return-v1.1.md"),
    ("reasoning-return-r8", "reviewed-reasoning-return-r8-v1.1.md"),
]
INPUTS = ["AGENTS.md", "problems/2022-B4/statement.md"]
for stem, body in PREMISES:
    INPUTS.extend(["problems/2022-B4/proofs/" + body,
        "problems/2022-B4/reviews/" + stem + "-acceptance.md",
        "problems/2022-B4/reviews/" + stem + "-acceptance.json"])
INPUTS.append(OWN_PARENT)
PAYLOADS = [P + s for s in ("candidate-v1.md", "obligations-v1.md", "research-v1.md",
    "sources-v1.json", "admin-v1.py", "baseline-v1.json", "metadata-v1.json")]
EXPECTED = {
    "AGENTS.md": (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
    "problems/2022-B4/proofs/reviewed-reasoning-dynamics-return-r9-v1.1.md":
        (22645, "7cfa2c60557935261d7144576f0e39a509fbebb292fdd0027415efe411ae4c55"),
    "problems/2022-B4/proofs/reviewed-reasoning-dynamics-return-r7-v1.1.md":
        (21378, "75f12e12027c50df48eba74149bf4993edfd1ff922eac8a130dfc0655abfe98f"),
    "problems/2022-B4/proofs/reviewed-rational-base-shadow-return-v1.1.md":
        (27405, "f58c75a8bc975ab49073bf03ac5db4a55fa9b65458c2a61f4f5fd40b9be1be6e"),
    "problems/2022-B4/proofs/reviewed-reasoning-return-r8-v1.1.md":
        (20660, "f09e43748bdc2c8d1cd4b7bccdfd733265b4fe0b8f24986b00051fea7c799b9f"),
    OWN_PARENT: (2868, "ea15b59730d0e2f9d2bc1921ad1a766ad1720168070104f242383370264704a8"),
}


def now():
    return datetime.now(timezone.utc).isoformat()


def safe(path):
    candidate = Path(path)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise RuntimeError("Unsafe documentary relative path")
    forbidden = [
        "problems/2017-B4/reviews/reasoning-concentration-return-r12-review-2-",
        "problems/2024-B4/reviews/reasoning-frobenius-return-r11-review-",
        "problems/2022-B4/reviews/reasoning-collision-return-r10-review-",
    ]
    if any(path.startswith(prefix) for prefix in forbidden):
        raise RuntimeError("NEW corresponding peer path refused")
    full = ROOT / candidate
    if not full.resolve().is_relative_to(ROOT):
        raise RuntimeError("Escaping repository documentary path")
    return full


def raw(path):
    return safe(path).read_bytes()


def load(path):
    return json.loads(raw(path))


def rec(path):
    b = raw(path)
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def canon(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def records(value):
    result = []
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str) and isinstance(value.get("bytes"), int)
                and isinstance(value.get("sha256"), str) and len(value["sha256"]) == 64):
            result.append({key: value[key] for key in ("path", "bytes", "sha256")})
        for child in value.values():
            result.extend(records(child))
    elif isinstance(value, list):
        for child in value:
            result.extend(records(child))
    return result


def checked(rows):
    for row in rows:
        if rec(row["path"]) != row:
            raise RuntimeError("Preserved input fingerprint changed: " + row["path"])


def labels():
    text = raw(P + "obligations-v1.md").decode()
    ids = re.findall(r"^\| RC10-(\d{2}) \|", text, flags=re.M)
    if ids != [str(i).zfill(2) for i in range(1, 61)]:
        raise RuntimeError("Missing/repeated/out-of-order literal documentary label")
    return len(ids)


def save(suffix, value):
    path = P + suffix
    if not path.startswith(P):
        raise RuntimeError("Write escaped exclusive NEW prefix")
    full = safe(path)
    if full.exists():
        raise RuntimeError("Refusing ANY overwrite: " + path)
    full.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def guards():
    direct = [rec(path) for path in INPUTS]
    for path, wanted in EXPECTED.items():
        got = rec(path)
        if (got["bytes"], got["sha256"]) != wanted:
            raise RuntimeError("Exact preserved identity mismatch: " + path)
    rows, bindings = list(direct), []
    for path in INPUTS:
        if path.endswith(".json"):
            declared = records(load(path))
            checked(declared)
            rows.extend(declared)
            bindings.append({**rec(path), "declared_occurrences_verified": len(declared),
                "declared_canonical_sha256": canon(declared)})
    unique = {}
    for row in rows:
        if unique.setdefault(row["path"], row) != row:
            raise RuntimeError("Conflicting preserved fingerprint")
    ordered = [unique[path] for path in sorted(unique)]
    authority_checks = []
    for stem, body in PREMISES:
        jp = "problems/2022-B4/reviews/" + stem + "-acceptance.json"
        authority = load(jp)
        if not authority["whole_initials_blind"] or authority["unresolved_substantive_issues"] != 0:
            raise RuntimeError("Current accepted authority shape mismatch")
        bp = "problems/2022-B4/proofs/" + body
        if not raw(bp).endswith(raw(authority["candidate"]["path"])):
            raise RuntimeError("Accepted literal candidate suffix changed")
        authority_checks.append({"authority": jp, "literal_suffix_matches": True})
    parent = load(OWN_PARENT)
    if parent["older_plus_new_own_paths_bound_transitively"] != 972:
        raise RuntimeError("Compact own parent count mismatch")
    labels()
    return {"direct_records": direct, "immutable_metadata_bindings": bindings,
        "all_guard_summary": {"occurrences": len(rows), "unique_paths": len(ordered),
            "canonical_deduplicated_sha256": canon(ordered)},
        "current_accepted_body_literal_suffix_checks": authority_checks,
        "own_immediate_parent": rec(OWN_PARENT),
        "older_own_paths_bound_transitively": 972,
        "older_plus_new_own_paths_bound_transitively": 980,
        "compact_parent_metadata_no_growing_inventory_copy": True,
        "all_declared_fingerprints_pass": True,
        "no_NEW_peer_content_inventory_hash_metadata_access": True}


def prepare():
    g = guards()
    save("baseline-v1.json", {"created_at_utc": now(), **g,
        "documentary_administration_only": True,
        "literal_obligations": labels(),
        "exact_prepare_command": "python3 " + P + "admin-v1.py prepare",
        "exact_freeze_command": "python3 " + P + "admin-v1.py freeze",
        "exact_SEPARATE_readonly_verify_command": "python3 " + P + "admin-v1.py verify"})
    save("metadata-v1.json", {"created_at_utc": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2022_complexity_r2", "constructor_excluded": True,
        "root_NEW_construction_contribution": False, "TWO_OTHER_whole_audits_required": 2,
        "claims": ["RC10A", "RC10B", "RC10C", "RC10D", "RC10E"],
        "whole_obligations": 60, "ENTIRE_files_including_freeze": 8,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_readback": None,
        "all_NEW_mathematics_hand_reasoning": True,
        "no_mathprogram_CAS_scan_test_optimizer_author_source_old_replay": True,
        "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
        "NEW_FR11_peer_access": False,
        "R12_AR_dispositions_released_only_after_explicit_BOTH": True,
        "ordinary_infinite_avoider_termination_annual_priority_claim": False,
        "selected_branches_NOT_full_D9_classification": True,
        "FULL_final_MODEL_readback_ALL7_payloads_then_freeze_required": True,
        "FULL_freeze_MODEL_readback_then_SEPARATE_verify_required": True,
        "last_direct_TOTAL_percent": 64, "last_direct_UTC": "2026-10-18 22:06:26 UTC",
        "window_minutes": 10080, "authorized_reset": 1792874445,
        "ordinaryUsageAllowed": True, "legacy_by_limit_agree": True,
        "account_label": "029a8928…1334ac3a", "TOTAL_ceiling_percent": 90,
        "integration_reserve": True, "automatic_later_window_spending": False})
    print(json.dumps({"action": "NEW documentary prepare", "all_pass": True,
        "guard_summary": g["all_guard_summary"], "literal_obligations": labels(),
        "baseline": rec(P + "baseline-v1.json"), "metadata": rec(P + "metadata-v1.json")}))


def match_baseline():
    old, g = load(P + "baseline-v1.json"), guards()
    for key, value in g.items():
        if old[key] != value:
            raise RuntimeError("Bound input summary changed: " + key)
    return g


def freeze():
    g = match_baseline()
    for path in PAYLOADS:
        if path.endswith(".json"):
            load(path)
    save("freeze-v1.json", {"frozen_at_utc": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2022_complexity_r2", "constructor_excluded": True,
        "root_NEW_construction_contribution": False, "TWO_OTHER_whole_audits_required": 2,
        "claims": ["RC10A", "RC10B", "RC10C", "RC10D", "RC10E"],
        "whole_obligations": labels(), "ENTIRE_files_including_this_freeze": 8,
        "payloads": [rec(path) for path in PAYLOADS],
        "all_guard_summary": g["all_guard_summary"],
        "own_immediate_parent": g["own_immediate_parent"],
        "older_own_paths_bound_transitively": 972,
        "older_plus_new_own_paths_bound_transitively": 980,
        "FULL_final_MODEL_readback_ALL7_payloads_code_ALLmetadata_completed": True,
        "FULL_freeze_MODEL_readback_then_SEPARATE_readonly_verify_required": True,
        "no_NEW_peer_access_or_mathematical_program": True,
        "no_Git_shared_old_cache_mutation": True,
        "ordinary_infinite_avoider_termination_annual_priority_claim": False,
        "last_direct_TOTAL_percent": 64, "authorized_reset": 1792874445,
        "TOTAL_ceiling_percent": 90, "integration_reserve": True,
        "automatic_later_window_spending": False})
    print(json.dumps({"action": "NEW documentary freeze", "all_pass": True,
        "main": rec(P + "candidate-v1.md"), "freeze": rec(P + "freeze-v1.json"),
        "ENTIRE_files": 8, "literal_obligations": labels()}))


def verify():
    g = match_baseline()
    f = load(P + "freeze-v1.json")
    checked(f["payloads"])
    if [row["path"] for row in f["payloads"]] != PAYLOADS:
        raise RuntimeError("Wrong documentary payload inventory")
    if f["all_guard_summary"] != g["all_guard_summary"]:
        raise RuntimeError("Freeze guard summary changed")
    for path in PAYLOADS:
        if path.endswith(".json"):
            load(path)
    print(json.dumps({"action": "SEPARATE read-only documentary verify", "verified_at_utc": now(),
        "all_pass": True, "ENTIRE_files": 8, "literal_obligations": labels(),
        "guard_summary": g["all_guard_summary"], "main": rec(P + "candidate-v1.md"),
        "freeze": rec(P + "freeze-v1.json"), "write_performed": False}))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("prepare", "freeze", "verify"):
        raise SystemExit("Use prepare/freeze/verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[sys.argv[1]]()
