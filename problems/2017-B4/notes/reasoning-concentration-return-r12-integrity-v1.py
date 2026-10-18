#!/usr/bin/env python3
"""NEW CI12 administrative byte/JSON freezer; NO mathematical program.

Use prepare, freeze, then a SEPARATE read-only verify invocation, all
from repository root. No network/subprocess/old code/source execution.
Only same-prefix NEW JSON is written, refusing every overwrite.
"""
import hashlib
import json
from pathlib import Path
import sys
from datetime import datetime, timezone

ROOT = Path.cwd().resolve()
P = "problems/2017-B4/notes/reasoning-concentration-return-r12-"
INPUTS = [
    "AGENTS.md", "problems/2017-B4/statement.md",
    "problems/2017-B4/proofs/reviewed-reasoning-pressure-return-r11-v1.1.md",
    "problems/2017-B4/reviews/reasoning-pressure-return-r11-acceptance.md",
    "problems/2017-B4/reviews/reasoning-pressure-return-r11-acceptance.json",
    "problems/2024-B4/notes/reasoning-frobenius-return-r10-freeze-v1.json",
]
EXPECTED = {
    INPUTS[0]: (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
    INPUTS[2]: (26687, "56688cd6030db910fbbc9162436b25acbf61a69869e2501dbd6f50b088bc3b60"),
    INPUTS[5]: (3218, "226beec7d86256e4daed124fb3686be8b798aa75b0638aaabef6eaf7df500f65"),
}
PAYLOADS = ["candidate-v1.md", "obligations-v1.md", "issues-v1.md",
    "failures-v1.md", "sources-v1.md", "sources-v1.json", "worklog-v1.md",
    "code-v1.md", "integrity-v1.py", "baseline-v1.json",
    "input-validation-v1.json", "metadata-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def rec(path):
    if Path(path).is_absolute() or ".." in Path(path).parts:
        raise RuntimeError("Unsafe relative metadata path")
    raw = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def canon(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def save(suffix, value):
    path = ROOT / (P + suffix)
    if path.exists():
        raise RuntimeError("Refusing overwrite: " + str(path))
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def records(value):
    found = []
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str) and isinstance(value.get("bytes"), int)
                and isinstance(value.get("sha256"), str) and len(value["sha256"]) == 64):
            found.append({k: value[k] for k in ("path", "bytes", "sha256")})
        for child in value.values():
            found.extend(records(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(records(child))
    return found


def checked(rows):
    for row in rows:
        if rec(row["path"]) != row:
            raise RuntimeError("Fingerprint mismatch: " + row["path"])


def labels():
    text = (ROOT / (P + "obligations-v1.md")).read_text()
    count = sum(line.startswith("| ") and line[2:4].isdigit() for line in text.splitlines())
    if count != 48:
        raise RuntimeError("Wrong literal documentary obligation count")
    return count


def guards():
    direct = [rec(path) for path in INPUTS]
    for row in direct:
        if row["path"] in EXPECTED and (row["bytes"], row["sha256"]) != EXPECTED[row["path"]]:
            raise RuntimeError("Expected input identity mismatch")
    bindings, declared = [], []
    for path in INPUTS:
        if path.endswith(".json"):
            own = records(json.loads((ROOT / path).read_text()))
            checked(own)
            declared.extend(own)
            bindings.append({**rec(path), "declared_occurrences_verified": len(own), "declared_canonical_sha256": canon(own)})
    unique = {}
    for row in direct + declared:
        if unique.setdefault(row["path"], row) != row:
            raise RuntimeError("Conflicting old fingerprint")
    ordered = [unique[path] for path in sorted(unique)]
    labels()
    return {"direct_inputs": direct, "immutable_parent_metadata": bindings,
        "guard_occurrences_verified": len(direct) + len(declared),
        "unique_guard_paths": len(ordered), "deduplicated_canonical_sha256": canon(ordered)}


def prepare():
    guard = guards()
    save("baseline-v1.json", {"created_utc": now(), **guard,
        "compact_binding_no_historical_inventory_copy": True, "administrative_only": True})
    save("input-validation-v1.json", {"validated_utc": now(), "all_pass": True,
        "direct_expected_identities_passed": len(EXPECTED), "literal_obligations": 48,
        "guard_occurrences_verified": guard["guard_occurrences_verified"],
        "unique_guard_paths": guard["unique_guard_paths"], "no_mathematical_program": True})
    save("metadata-v1.json", {"created_utc": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1", "constructor_excluded": True,
        "claims": ["CI12A", "CI12B", "CI12C", "CI12D"], "whole_obligations": 48,
        "OTHER_whole_audits_required": 2, "requested_model": "gpt-6.1-sol",
        "requested_reasoning_effort": "max", "effective_setting_readback": "unavailable",
        "old_role": "C constructed accepted R11; no independent self-recertification",
        "root_new_inference_contribution": False, "NEW_FR10_peer_access": False,
        "mathematical_program_scan_test_CAS": False, "pending_native_child_approval": False,
        "authorized_weekly_reset": 1792874445, "TOTAL_ceiling_percent": 90,
        "last_direct_transition_percent": 60,
        "commands": ["python3 " + P + "integrity-v1.py " + action for action in ("prepare", "freeze", "verify")],
        "full_final_model_readback_required": True, "separate_readonly_verify_required": True,
        "global_base_value_effectiveR_annual_priority_claim": False})
    print(json.dumps({"action": "prepare", "all_pass": True,
        "guard_occurrences_verified": guard["guard_occurrences_verified"],
        "unique_guard_paths": guard["unique_guard_paths"], "literal_obligations": labels()}))


def match_baseline():
    old = json.loads((ROOT / (P + "baseline-v1.json")).read_text())
    current = guards()
    for key, value in current.items():
        if old[key] != value:
            raise RuntimeError("Preserved input summary changed: " + key)
    return current


def freeze():
    guard = match_baseline()
    rows = [rec(P + suffix) for suffix in PAYLOADS]
    for row in rows:
        if row["path"].endswith(".json"):
            json.loads((ROOT / row["path"]).read_text())
    save("freeze-v1.json", {"frozen_utc": now(), "status": "candidate proof - unverified",
        "payload_records": rows, "ENTIRE_files": len(rows) + 1, "whole_obligations": 48,
        "OTHER_whole_audits_required": 2, "constructor_excluded": True,
        "input_guard_occurrences_verified": guard["guard_occurrences_verified"],
        "unique_guard_paths": guard["unique_guard_paths"],
        "deduplicated_guard_canonical_sha256": guard["deduplicated_canonical_sha256"],
        "all_input_guards_pass": True, "mathematical_program": False,
        "FULL_final_model_payload_readback": "Completed before this action; actual whole readback required",
        "FULL_freeze_readback_then_SEPARATE_readonly_verify_required": True})
    print(json.dumps({"action": "freeze", "freeze_record": rec(P + "freeze-v1.json"), "ENTIRE_files": len(rows) + 1}))


def verify():
    guard = match_baseline()
    frozen = json.loads((ROOT / (P + "freeze-v1.json")).read_text())
    checked(frozen["payload_records"])
    for row in frozen["payload_records"]:
        if row["path"].endswith(".json"):
            json.loads((ROOT / row["path"]).read_text())
    print(json.dumps({"action": "SEPARATE read-only verify", "verified_utc": now(), "all_pass": True,
        "ENTIRE_files": frozen["ENTIRE_files"], "literal_obligations": labels(),
        "guard_occurrences_verified": guard["guard_occurrences_verified"],
        "unique_guard_paths": guard["unique_guard_paths"],
        "freeze_record": rec(P + "freeze-v1.json"), "main_record": rec(P + "candidate-v1.md")}))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("prepare", "freeze", "verify"):
        raise SystemExit("Use prepare/freeze/verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[sys.argv[1]]()
