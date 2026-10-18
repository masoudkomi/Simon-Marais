#!/usr/bin/env python3
"""FR10 NEW administrative byte/JSON freezer only; NO mathematical code.

Commands, run from the repository root:
 python3 problems/2024-B4/notes/reasoning-frobenius-return-r10-integrity-v1.py prepare
 python3 problems/2024-B4/notes/reasoning-frobenius-return-r10-integrity-v1.py freeze
 python3 problems/2024-B4/notes/reasoning-frobenius-return-r10-integrity-v1.py verify

No network, subprocess, imports from old/source/author code or mathematical
library. Writes ONLY the exclusive same-prefix JSON metadata on prepare/freeze.
The separate verify action is read-only. SHA agreement is not a proof check.
"""
import hashlib
import json
from pathlib import Path
import sys
from datetime import datetime, timezone

ROOT = Path.cwd().resolve()
P = "problems/2024-B4/notes/reasoning-frobenius-return-r10-"
DIRECT = [
    "AGENTS.md",
    "problems/2024-B4/statement.md",
    "problems/2024-B4/proofs/reviewed-reasoning-cofactor-return-r6-v1.1.md",
    "problems/2024-B4/reviews/reasoning-cofactor-return-r6-acceptance.md",
    "problems/2024-B4/reviews/reasoning-cofactor-return-r6-acceptance.json",
    "problems/2024-B4/proofs/reviewed-reasoning-cofactor-return-r9-v1.1.md",
    "problems/2024-B4/reviews/reasoning-cofactor-return-r9-acceptance.md",
    "problems/2024-B4/reviews/reasoning-cofactor-return-r9-acceptance.json",
    "problems/2021-B4/reviews/reasoning-center-return-r21-review-1-manifest-v1.json",
]
EXPECTED = {
    "AGENTS.md": (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
    DIRECT[2]: (20658, "fb988a13187b5765619532ad14077ae2f32a948e04704252e3d8981e10d65d98"),
    DIRECT[5]: (26416, "68a8b1d05a927ffecc13375ee5db5376c780acbf7e3cee3a6659c8c80caa876c"),
    DIRECT[8]: (3354, "8ffd67896301221c73b5f262a60c52a995f6ca91bd1886e9c3078930831ddbd5"),
}
PAYLOAD_SUFFIXES = [
    "candidate-v1.md", "obligations-v1.md", "issues-v1.md",
    "sources-v1.md", "sources-v1.json", "failures-v1.md",
    "worklog-v1.md", "code-v1.md", "integrity-v1.py",
    "baseline-v1.json", "input-validation-v1.json", "metadata-v1.json",
]


def now():
    return datetime.now(timezone.utc).isoformat()


def record(path):
    raw = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def write(suffix, value):
    target = ROOT / (P + suffix)
    if target.exists():
        raise RuntimeError("Refusing to overwrite: " + str(target))
    target.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def declared_records(value):
    found = []
    if isinstance(value, dict):
        path = value.get("path")
        sha = value.get("sha256")
        size = value.get("bytes")
        if isinstance(path, str) and isinstance(sha, str) and len(sha) == 64 and isinstance(size, int):
            found.append({"path": path, "bytes": size, "sha256": sha})
        for child in value.values():
            found.extend(declared_records(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(declared_records(child))
    return found


def verify_rows(rows):
    for row in rows:
        path = row["path"]
        if Path(path).is_absolute() or ".." in Path(path).parts:
            raise RuntimeError("Unsafe metadata path: " + path)
        actual = record(path)
        if actual != row:
            raise RuntimeError("Fingerprint mismatch: " + path)


def row_count():
    text = (ROOT / (P + "obligations-v1.md")).read_text()
    return sum(1 for line in text.splitlines() if line.startswith("| ") and line[2:4].isdigit())


def prepare():
    rows = [record(path) for path in DIRECT]
    for row in rows:
        if row["path"] in EXPECTED:
            expected_size, expected_sha = EXPECTED[row["path"]]
            if row["bytes"] != expected_size or row["sha256"] != expected_sha:
                raise RuntimeError("Declared expected input mismatch: " + row["path"])
    declared = []
    parent_bindings = []
    for path in DIRECT:
        if path.endswith(".json"):
            value = json.loads((ROOT / path).read_text())
            own = declared_records(value)
            verify_rows(own)
            declared.extend(own)
            parent_bindings.append({
                **record(path),
                "declared_fingerprint_occurrences_verified": len(own),
                "declared_records_canonical_sha256": digest(own),
            })
    unique = {}
    for row in rows + declared:
        old = unique.setdefault(row["path"], row)
        if old != row:
            raise RuntimeError("Conflicting preserved metadata: " + row["path"])
    ordered = [unique[path] for path in sorted(unique)]
    if row_count() != 64:
        raise RuntimeError("Wrong literal obligations count")
    write("baseline-v1.json", {
        "created_utc": now(), "status": "administrative input binding only",
        "direct_inputs": rows, "immutable_parent_metadata": parent_bindings,
        "direct_plus_declared_occurrences_verified": len(rows) + len(declared),
        "unique_guard_paths": len(ordered),
        "deduplicated_guard_records_canonical_sha256": digest(ordered),
        "historical_inventory_duplicated": False,
        "mathematical_program_executed": False,
    })
    write("input-validation-v1.json", {
        "validated_utc": now(), "direct_inputs": len(rows),
        "direct_expected_fingerprints_passed": len(EXPECTED),
        "declared_fingerprint_occurrences_verified": len(declared),
        "unique_guard_paths": len(ordered), "all_pass": True,
        "literal_obligation_rows": 64,
        "only_bytes_hash_json_literal_row_count": True,
        "no_old_freezer_source_author_execution": True,
    })
    write("metadata-v1.json", {
        "created_utc": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1",
        "requested_model": "gpt-6.1-sol", "requested_reasoning_effort": "max",
        "effective_setting_readback": "unavailable",
        "claims": ["FR10A", "FR10B", "FR10C", "FR10D"],
        "whole_obligations": 64, "OTHER_whole_audits_required": 2,
        "constructor_excluded": True,
        "old_roles": "C authored accepted R6/R7/R8, reviewed R9; not independent recertification",
        "root_new_construction_inference": False,
        "root_degree_gap_note_used": False,
        "mathematical_computation": False, "pending_native_child_or_approval": False,
        "raw_primary_PDF_downloaded": False,
        "authorized_weekly_reset": 1792874445, "total_ceiling_percent": 90,
        "last_direct_usage": {"utc": "2026-10-18T18:18:21Z", "used_percent": 59, "window_minutes": 10080},
        "commands": [
            "python3 " + P + "integrity-v1.py prepare",
            "python3 " + P + "integrity-v1.py freeze",
            "python3 " + P + "integrity-v1.py verify",
        ],
        "full_final_model_readback_required_before_freeze": True,
        "full_freeze_model_readback_then_separate_readonly_verify_required": True,
        "annual_or_priority_claim": False,
    })
    print(json.dumps({"action": "prepare", "all_pass": True,
        "direct_plus_declared_occurrences_verified": len(rows) + len(declared),
        "unique_guard_paths": len(ordered), "literal_obligation_rows": 64}))


def check_baseline():
    baseline = json.loads((ROOT / (P + "baseline-v1.json")).read_text())
    verify_rows(baseline["direct_inputs"])
    declared = []
    for parent in baseline["immutable_parent_metadata"]:
        value = json.loads((ROOT / parent["path"]).read_text())
        own = declared_records(value)
        if len(own) != parent["declared_fingerprint_occurrences_verified"] or digest(own) != parent["declared_records_canonical_sha256"]:
            raise RuntimeError("Changed immutable parent record shape")
        verify_rows(own)
        declared.extend(own)
    unique = {r["path"]: r for r in baseline["direct_inputs"] + declared}
    ordered = [unique[path] for path in sorted(unique)]
    if len(ordered) != baseline["unique_guard_paths"] or digest(ordered) != baseline["deduplicated_guard_records_canonical_sha256"]:
        raise RuntimeError("Changed deduplicated guard summary")
    if row_count() != 64:
        raise RuntimeError("Changed literal obligation count")
    return baseline


def freeze():
    baseline = check_baseline()
    rows = [record(P + suffix) for suffix in PAYLOAD_SUFFIXES]
    for row in rows:
        if row["path"].endswith(".json"):
            json.loads((ROOT / row["path"]).read_text())
    write("freeze-v1.json", {
        "frozen_utc": now(), "status": "candidate proof - unverified",
        "payload_records": rows, "payload_files": len(rows), "ENTIRE_files_including_this_freeze": len(rows) + 1,
        "whole_obligations": 64, "OTHER_whole_audits_required": 2,
        "constructor_excluded": True,
        "input_guards_all_pass": True,
        "direct_plus_declared_occurrences_verified": baseline["direct_plus_declared_occurrences_verified"],
        "unique_guard_paths": baseline["unique_guard_paths"],
        "deduplicated_guard_records_canonical_sha256": baseline["deduplicated_guard_records_canonical_sha256"],
        "mathematical_computation": False,
        "full_final_model_readback": "Performed before this freeze action; all payloads including generated metadata must actually have been read",
        "separate_readonly_verify_required_after_full_freeze_readback": True,
    })
    print(json.dumps({"action": "freeze", "record": record(P + "freeze-v1.json"), "payloads": len(rows), "ENTIRE": len(rows) + 1}))


def verify():
    baseline = check_baseline()
    frozen = json.loads((ROOT / (P + "freeze-v1.json")).read_text())
    verify_rows(frozen["payload_records"])
    for row in frozen["payload_records"]:
        if row["path"].endswith(".json"):
            json.loads((ROOT / row["path"]).read_text())
    print(json.dumps({"action": "SEPARATE read-only verify", "verified_utc": now(), "all_pass": True,
        "ENTIRE_files": frozen["ENTIRE_files_including_this_freeze"], "literal_obligation_rows": row_count(),
        "input_occurrences_verified": baseline["direct_plus_declared_occurrences_verified"],
        "unique_guard_paths": baseline["unique_guard_paths"],
        "freeze_record": record(P + "freeze-v1.json"), "main_record": record(P + "candidate-v1.md")}))


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ("prepare", "freeze", "verify"):
        raise SystemExit("Use prepare, freeze, or verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[sys.argv[1]]()
