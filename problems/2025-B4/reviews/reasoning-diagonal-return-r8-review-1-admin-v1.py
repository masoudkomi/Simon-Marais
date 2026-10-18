#!/usr/bin/env python3
"""DR8 independent review1 documentary integrity only; verify is read-only."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/reasoning-diagonal-return-r8-review-1-"
AUTHOR = "problems/2025-B4/notes/reasoning-diagonal-return-r8-"
RELATED_REVIEWS = "problems/2025-B4/reviews/reasoning-diagonal-return-r8-review-"
TARGET = {
    "path": AUTHOR + "candidate-v1.md", "bytes": 15008,
    "sha256": "2e793eb556b4a3063dbdde1cf0b16b7f9f53eec4e36469adf31693b022b19a47",
}
AUTHOR_FREEZE = {
    "path": AUTHOR + "freeze-v1.json", "bytes": 3635,
    "sha256": "53ce3848114979fe2f882c7ef22ac3d97e4f79880a1abec92ddfcda4964d4323",
}
OWN_PARENT = {
    "path": "problems/2019-B4/notes/reasoning-occupation-return-r1-freeze-v1.json",
    "bytes": 4361,
    "sha256": "e4b6369f4733f2e418ecc43e24329b011aa538799f1afaeb9dcc667abfe75ee9",
}
SUFFIXES = [
    "initial-v1.md", "ledger-v1.md", "issues-v1.md", "sources-v1.md",
    "sources-v1.json", "worklog-v1.md", "admin-v1.py", "baseline-v1.json",
    "input-validation-v1.json",
]
BASELINE = PREFIX + "baseline-v1.json"
VALIDATION = PREFIX + "input-validation-v1.json"
MANIFEST = PREFIX + "manifest-v1.json"
EXTRA_INPUTS = [
    "AGENTS.md", "problems/2025-B4/statement.md",
    "problems/2025-B4/notes/reasoning-diagonal-return-r7-sources-v1.md",
    "problems/2025-B4/notes/reasoning-diagonal-return-r7-failed-routes-v1.md",
]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    if path.startswith(RELATED_REVIEWS) and not path.startswith(PREFIX):
        raise ValueError("corresponding NEW peer review embargo")
    p = Path(path)
    assert not p.is_absolute() and ".." not in p.parts
    return (ROOT / path).read_bytes()


def doc(path):
    return json.loads(raw(path))


def rec(path):
    data = raw(path)
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked(row):
    reduced = {key: row[key] for key in ("path", "bytes", "sha256")}
    assert rec(row["path"]) == reduced, ("declared bytes changed", row["path"])
    return reduced


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def records_in(value):
    """Declared documentary records only, not a filesystem inventory."""
    if isinstance(value, dict):
        if all(k in value for k in ("path", "bytes", "sha256")):
            return [checked(value)]
        result = []
        for child in value.values():
            result += records_in(child)
        return result
    if isinstance(value, list):
        result = []
        for child in value:
            result += records_in(child)
        return result
    return []


def labels():
    expected = [f"{i:02d}" for i in range(1, 65)]
    author = re.findall(r"(?m)^\|DR8-(\d{2})\|",
                        raw(AUTHOR + "obligations-v1.md").decode())
    own = re.findall(r"(?m)^\|DR8-(\d{2})\|",
                     raw(PREFIX + "ledger-v1.md").decode())
    assert author == expected and own == expected
    return {"author_labels": 64, "independent_separate_dispositions": 64,
            "exact_order_unique": True, "mathematical_validation_by_code": False}


def gather():
    rows = [checked(TARGET), checked(AUTHOR_FREEZE), checked(OWN_PARENT)]
    frozen = doc(AUTHOR_FREEZE["path"])
    assert frozen["ENTIRE_files"] == 14 and len(frozen["payloads"]) == 13
    assert frozen["whole_obligations"] == 64
    for row in frozen["payloads"]:
        assert row["path"].startswith(AUTHOR)
        rows.append(checked(row))
    author_baseline = doc(AUTHOR + "baseline-v1.json")
    bindings = author_baseline["compact_bindings"]
    rows += records_in(bindings)
    # Bind necessary old DR7 payloads, not its historical inventory.
    old_freeze = bindings["operative_DR7_original_ENTIRE14_binding"]
    old = doc(old_freeze["path"])
    old_rows = old.get("artifacts", old.get("payloads"))
    assert len(old_rows) == 13
    for row in old_rows:
        rows.append(checked(row))
    operative = bindings["operative_DR7"]
    current = doc(operative["authority_JSON"]["path"])
    assert current["status"] == "proved, independently reviewed scoped partial result"
    assert current["accepted_copy"] == operative["accepted_copy"]
    assert raw(current["accepted_copy"]["path"]).endswith(
        raw(current["candidate"]["path"]))
    for path in EXTRA_INPUTS:
        rows.append(rec(path))
    parent = doc(OWN_PARENT["path"])
    assert parent["ENTIRE_files_including_manifest"] == 12
    assert parent["older_plus_new_own_paths_bound_transitively"] == 912
    assert len(parent["payloads"]) == 11
    for row in parent["payloads"]:
        rows.append(checked(row))
    unique = {}
    for row in rows:
        if row["path"] in unique:
            assert unique[row["path"]] == row
        unique[row["path"]] = row
    ordered = [unique[path] for path in sorted(unique)]
    return {
        "exact_guard_records": ordered,
        "guard_summary": {
            "occurrences": len(rows), "unique_paths": len(ordered),
            "canonical_sha256": hashlib.sha256(canonical(ordered)).hexdigest(),
        },
        "author_ENTIRE14_and_all64_bound": True,
        "author_historical_protection_summary_not_reexpanded":
            frozen["current_frozen_protection"],
        "operative_DR7_current_authority": operative,
        "operative_DR7_ENTIRE14_bound_without_historical_inventory_expansion": True,
        "own_immediate_parent": OWN_PARENT,
        "own_parent_ENTIRE12_unchanged": True,
        "older_own_paths_bound_transitively": 912,
        "corresponding_NEW_peer_review_material_access_or_inventory": False,
        "old_author_source_freezer_or_mathematical_code_executed": False,
    }


def write_new(path, value):
    assert path in (BASELINE, VALIDATION, MANIFEST)
    assert path.startswith(PREFIX)
    assert not (ROOT / MANIFEST).exists(), "immutable own manifest already exists"
    assert not (ROOT / path).exists(), "new review file already exists"
    (ROOT / path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def validate_baseline():
    baseline = doc(BASELINE)
    for row in baseline["bindings"]["exact_guard_records"]:
        checked(row)
    rows = baseline["bindings"]["exact_guard_records"]
    assert hashlib.sha256(canonical(rows)).hexdigest() == \
        baseline["bindings"]["guard_summary"]["canonical_sha256"]
    labels()
    return baseline


def prepare():
    bindings = gather()
    coverage = labels()
    write_new(BASELINE, {"prepared_at_utc": now(),
        "purpose": "documentary byte protection only",
        "bindings": bindings})
    write_new(VALIDATION, {"validated_at_utc": now(), "status": "documentary PASS only",
        "coverage": coverage, "guard_summary": bindings["guard_summary"],
        "no_mathematical_program_or_old_replay": True,
        "no_corresponding_NEW_peer_material_access_or_inventory": True})
    print(json.dumps({"prepare": "PASS", "at_utc": now(),
                      "guard_summary": bindings["guard_summary"],
                      "whole_document_labels": 64}))


def freeze():
    baseline = validate_baseline()
    assert doc(VALIDATION)["guard_summary"] == baseline["bindings"]["guard_summary"]
    payloads = [rec(PREFIX + suffix) for suffix in SUFFIXES]
    manifest = {
        "frozen_at_utc": now(),
        "role": "OTHER initially blind ENTIRE WHOLE1 initial review, findings sealed",
        "reviewer": "/root/review_2022_complexity_r2",
        "nonconstructor": True, "constructor": "/root/review_2021_reasoning_j15_r2",
        "constructor_excluded": True, "root_supplied_new_inference": False,
        "target": TARGET, "author_freeze": AUTHOR_FREEZE,
        "author_ENTIRE_files_read": 14, "whole_obligations": 64,
        "separate_independent_hand_dispositions": 64,
        "ENTIRE_review_files_including_manifest": 10,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_readback": None,
        "FULL_final_model_readback_ALL9_payloads_code_generated_metadata_completed": True,
        "FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required": True,
        "guard_summary": baseline["bindings"]["guard_summary"],
        "immediate_own_parent": OWN_PARENT,
        "older_own_paths_bound_transitively": 912,
        "older_plus_new_own_paths_bound_transitively": 922,
        "no_NEW_corresponding_peer_finding_file_actual_inventory_hash_metadata_commentary_access": True,
        "findings_embargoed_until_explicit_BOTH_ENTIRE_confirmation": True,
        "no_mathematical_program_CAS_scan_test_old_author_source_freezer_replay": True,
        "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
        "weekly": doc(PREFIX + "sources-v1.json")["weekly"],
        "payloads": payloads,
    }
    write_new(MANIFEST, manifest)
    print(json.dumps({"freeze": "PASS", "identity": rec(MANIFEST),
        "main": rec(PREFIX + "initial-v1.md"), "at_utc": manifest["frozen_at_utc"],
        "ENTIRE_files": 10, "whole_obligations": 64,
        "administrative_only_handoff_until_BOTH": True}))


def verify():
    frozen = doc(MANIFEST)
    assert frozen["ENTIRE_review_files_including_manifest"] == 10
    assert frozen["whole_obligations"] == 64
    assert [r["path"] for r in frozen["payloads"]] == [PREFIX + s for s in SUFFIXES]
    for row in frozen["payloads"]:
        checked(row)
    baseline = validate_baseline()
    assert frozen["guard_summary"] == baseline["bindings"]["guard_summary"]
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "at_utc": now(),
        "ENTIRE_files": 10, "whole_obligations": 64, "identity": rec(MANIFEST),
        "main": rec(PREFIX + "initial-v1.md"),
        "guard_summary": frozen["guard_summary"], "no_file_written": True,
        "administrative_only_handoff_until_BOTH": True}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "freeze", "verify"))
    {"prepare": prepare, "freeze": freeze, "verify": verify}[parser.parse_args().mode]()
