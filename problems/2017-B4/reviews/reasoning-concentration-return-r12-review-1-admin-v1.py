#!/usr/bin/env python3
"""NEW R12 review1 documentary administration ONLY.

No mathematical computation, subprocess, network, author/old-code import
or peer inventory. prepare -> FULL MODEL readback of all payloads ->
freeze -> FULL manifest MODEL readback -> SEPARATE readonly verify.
Writes exclusively unused same-prefix baseline/manifest, refusing overwrite.
"""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path.cwd().resolve()
P = "problems/2017-B4/reviews/reasoning-concentration-return-r12-review-1-"
A = "problems/2017-B4/notes/reasoning-concentration-return-r12-"
AUTHOR_FREEZE = A + "freeze-v1.json"
OWN_PARENT = "problems/2019-B4/reviews/reasoning-area-return-r2-review-2-manifest-v1.json"
R11 = "problems/2017-B4/proofs/reviewed-reasoning-pressure-return-r11-v1.1.md"
R11MD = "problems/2017-B4/reviews/reasoning-pressure-return-r11-acceptance.md"
R11JSON = "problems/2017-B4/reviews/reasoning-pressure-return-r11-acceptance.json"
PAYLOADS = [P + s for s in ("initial-v1.md", "sources-v1.json", "admin-v1.py", "baseline-v1.json")]
EXPECTED = {
    "AGENTS.md": (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
    A + "candidate-v1.md": (19146, "aa79fe683e8cd7a7f63d5a3146b91f6cce294c1ceb1fb28e994e4d50071994d0"),
    AUTHOR_FREEZE: (3158, "6a6e5ccccbc9c5416aeeac4240a8a4f96bc44b90167d5275e8ab2bf563c17c1c"),
    R11: (26687, "56688cd6030db910fbbc9162436b25acbf61a69869e2501dbd6f50b088bc3b60"),
    OWN_PARENT: (2762, "5ad224e9efb9265c29d390032f39225d0a760eb8510c963f34fea30cc13a6276"),
}


def now():
    return datetime.now(timezone.utc).isoformat()


def safe(path):
    candidate = Path(path)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise RuntimeError("Unsafe documentary path")
    blocked = [
        "problems/2017-B4/reviews/reasoning-concentration-return-r12-review-2-",
        "problems/2019-B4/reviews/reasoning-area-return-r2-review-1-",
        "problems/2020-B4/reviews/reasoning-class-return-sq16-review-",
        "problems/2020-B4/reviews/reasoning-class-return-sq17-review-",
    ]
    if any(path.startswith(prefix) for prefix in blocked):
        raise RuntimeError("Corresponding NEW embargoed peer path refused")
    full = ROOT / candidate
    if not full.resolve().is_relative_to(ROOT):
        raise RuntimeError("Escaping documentary root")
    return full


def raw(path):
    return safe(path).read_bytes()


def load(path):
    return json.loads(raw(path))


def record(path):
    b = raw(path)
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def canonical(rows):
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
        if record(row["path"]) != row:
            raise RuntimeError("Preserved fingerprint changed: " + row["path"])


def save(suffix, value):
    path = P + suffix
    full = safe(path)
    if full.exists():
        raise RuntimeError("Refusing any overwrite: " + path)
    if not path.startswith(P):
        raise RuntimeError("Write escaped exclusive review prefix")
    full.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def labels():
    text = raw(P + "initial-v1.md").decode()
    found = re.findall(r"^\| CI12-(\d{2}) \|", text, flags=re.M)
    expected = [str(i).zfill(2) for i in range(1, 49)]
    if found != expected:
        raise RuntimeError("Missing/repeated/out-of-order literal documentary disposition")
    return len(found)


def guards():
    author = load(AUTHOR_FREEZE)
    if author["ENTIRE_files"] != 13 or author["whole_obligations"] != 48:
        raise RuntimeError("Author packet documentary shape mismatch")
    author_rows = author["payload_records"]
    if len(author_rows) != 12:
        raise RuntimeError("Author documentary payload count mismatch")
    checked(author_rows)
    direct_paths = [AUTHOR_FREEZE] + [row["path"] for row in author_rows] + [
        "AGENTS.md", "problems/2017-B4/statement.md", R11, R11MD, R11JSON, OWN_PARENT]
    direct = [record(path) for path in direct_paths]
    for path, wanted in EXPECTED.items():
        got = record(path)
        if (got["bytes"], got["sha256"]) != wanted:
            raise RuntimeError("Forwarded exact target/input fingerprint mismatch: " + path)
    rows = list(direct)
    bindings = []
    for path in direct_paths:
        if path.endswith(".json"):
            value = load(path)
            declared = records(value)
            checked(declared)
            rows.extend(declared)
            bindings.append({**record(path), "declared_occurrences_verified": len(declared),
                "declared_canonical_sha256": canonical(declared)})
    unique = {}
    for row in rows:
        if unique.setdefault(row["path"], row) != row:
            raise RuntimeError("Conflicting preserved documentary record")
    ordered = [unique[path] for path in sorted(unique)]
    parent = load(OWN_PARENT)
    if parent["older_plus_new_own_paths_bound_transitively"] != 967:
        raise RuntimeError("Own compact parent-count mismatch")
    authority = load(R11JSON)
    if not authority["whole_initials_blind"] or authority["unresolved_substantive_issues"] != 0:
        raise RuntimeError("R11 current authority shape mismatch")
    if not raw(R11).endswith(raw(authority["candidate"]["path"])):
        raise RuntimeError("R11 literal accepted suffix changed")
    labels()
    return {
        "direct_records": direct,
        "immutable_metadata_bindings": bindings,
        "all_guard_summary": {"occurrences": len(rows), "unique_paths": len(ordered),
            "canonical_deduplicated_sha256": canonical(ordered)},
        "own_immediate_parent": record(OWN_PARENT),
        "older_own_paths_bound_transitively": 967,
        "older_plus_new_own_paths_bound_transitively": 972,
        "compact_parent_binding_not_historical_inventory_copy": True,
        "all_declared_fingerprints_pass": True,
        "no_corresponding_NEW_peer_access": True,
    }


def prepare():
    guard = guards()
    save("baseline-v1.json", {"created_at_utc": now(), **guard,
        "documentary_administration_only": True,
        "ENTIRE_author13_full_model_read_and_ALL48_hand_reconstruction": True,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_readback": None,
        "no_mathprogram_CAS_scan_test_optimizer_author_source_old_replay": True,
        "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
        "exact_prepare_command": "python3 " + P + "admin-v1.py prepare",
        "exact_freeze_command": "python3 " + P + "admin-v1.py freeze",
        "exact_SEPARATE_readonly_verify_command": "python3 " + P + "admin-v1.py verify",
        "FULL_final_MODEL_readback_ALL4_payloads_then_freeze_required": True,
        "FULL_manifest_MODEL_readback_then_SEPARATE_verify_required": True})
    print(json.dumps({"action": "NEW documentary prepare", "all_pass": True,
        "guard_summary": guard["all_guard_summary"], "literal_dispositions": labels(),
        "baseline": record(P + "baseline-v1.json")}))


def match_baseline():
    old = load(P + "baseline-v1.json")
    guard = guards()
    for key, value in guard.items():
        if old[key] != value:
            raise RuntimeError("Frozen-input summary changed: " + key)
    return guard


def freeze():
    guard = match_baseline()
    for path in PAYLOADS:
        if path.endswith(".json"):
            load(path)
    save("manifest-v1.json", {
        "frozen_at_utc": now(), "reviewer": "/root/review_2022_complexity_r2",
        "role": "OTHER initially blind ENTIRE WHOLE1 of NEW CI12A--CI12D",
        "NEW_CI12_nonconstructor": True, "constructor_C_excluded": True,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_readback": None,
        "ENTIRE_author13_read_and_bound": True,
        "whole_obligations_and_separate_dispositions": labels(),
        "ALL48_issue_sourceMD_worklog_embedded_in_report": True,
        "substantive_defects": 0, "required_repairs": 0, "closed_scope_notes": 10,
        "corresponding_NEW_peer_finding_filename_inventory_file_hash_metadata_access": False,
        "findings_embargo_until_explicit_BOTH_ENTIRE_confirmation": True,
        "separate_AR_findings_still_embargoed": True,
        "FULL_final_MODEL_readback_ALL4_payloads_code_ALLmetadata_completed": True,
        "FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required": True,
        "all_guard_summary": guard["all_guard_summary"],
        "own_immediate_parent": guard["own_immediate_parent"],
        "older_own_paths_bound_transitively": 967,
        "older_plus_new_own_paths_bound_transitively": 972,
        "ENTIRE_files_including_this_manifest": 5,
        "no_mathprogram_CAS_scan_test_optimizer_author_source_old_replay": True,
        "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
        "global_base_improvement_value_effective_R_annual_priority_claim": False,
        "last_TOTAL_usage_percent": 62, "last_usage_at_utc": "2026-10-18 21:42:55 UTC",
        "authorized_reset": 1792874445, "TOTAL_ceiling_percent": 90,
        "integration_reserve": True, "automatic_later_window_spending": False,
        "payloads": [record(path) for path in PAYLOADS]})
    print(json.dumps({"action": "NEW documentary freeze", "all_pass": True,
        "manifest": record(P + "manifest-v1.json"), "report": record(P + "initial-v1.md"),
        "ENTIRE_files": 5, "literal_dispositions": labels()}))


def verify():
    guard = match_baseline()
    manifest = load(P + "manifest-v1.json")
    checked(manifest["payloads"])
    if manifest["all_guard_summary"] != guard["all_guard_summary"]:
        raise RuntimeError("Manifest guard summary changed")
    if [row["path"] for row in manifest["payloads"]] != PAYLOADS:
        raise RuntimeError("Wrong documentary payload inventory")
    for path in PAYLOADS:
        if path.endswith(".json"):
            load(path)
    print(json.dumps({"action": "SEPARATE read-only documentary verify", "verified_at_utc": now(),
        "all_pass": True, "ENTIRE_files": 5, "literal_dispositions": labels(),
        "guard_summary": guard["all_guard_summary"], "manifest": record(P + "manifest-v1.json"),
        "report": record(P + "initial-v1.md"), "write_performed": False}))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("prepare", "freeze", "verify"):
        raise SystemExit("Use prepare/freeze/verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[sys.argv[1]]()
