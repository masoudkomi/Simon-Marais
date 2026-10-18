#!/usr/bin/env python3
"""NEW R10 review2 documentary close only; no mathematical calculation.

This file reads only explicitly declared paths. It never inventories a peer
review, imports another helper, or executes constructor/old/source code.
prepare creates one NEW baseline; freeze needs actual final MODEL readback
of all four payloads; verify is a separate read-only call after manifest
MODEL readback. Fingerprints/literal labels are not mathematical evidence.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2025-B4/reviews/reasoning-compatible-return-r10-review-2-"
A = "problems/2025-B4/notes/reasoning-compatible-return-r10-"
MAIN = A + "candidate-v1.md"
AF = A + "freeze-v1.json"
BASE = P + "baseline-v1.json"
MAN = P + "manifest-v1.json"
PARENT = "problems/2024-B4/reviews/coordinator-tensor-return-r12-review-2-manifest-v1.json"
PAYLOADS = [P + "initial-v1.md", P + "sources-v1.json",
            P + "admin-v1.py", BASE]
FIXED = {
    MAIN: (20135, "3820e0f7677ee8879da687a4d294ead1b5aaa9f0cc44d110de2e576158468107"),
    AF: (3692, "167e4721b87d245a4dc82e5ffcc11d4fdd1dfad702785906fc732b7cd5f8b306"),
    PARENT: (2972, "e3bd98207b6eda0a2b884b73d0e43805788c93272cd8dca3e4465bcf75999ce2"),
}
EXTRAS = [
    "problems/2025-B4/reviews/reasoning-return-r9-acceptance.md",
    "problems/2025-B4/reviews/reasoning-return-r9-acceptance.json",
    "problems/2025-B4/reviews/reasoning-return-r6-acceptance.md",
    "problems/2025-B4/reviews/reasoning-return-r6-acceptance.json",
]
AUTHOR_GUARD = {"occurrences": 37, "unique_paths": 37,
                "canonical_sha256": "0a6e69586519ea7a7da97010f5cdac95090e688d8599bdb3806fbe2f35412a12"}


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def safe(path):
    assert isinstance(path, str)
    assert not path.startswith("/") and ".." not in Path(path).parts
    # Corresponding NEW review1 path access is strictly forbidden.
    assert "reasoning-compatible-return-r10-review-1-" not in path
    return ROOT / path


def record(path):
    data = safe(path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked(rec):
    assert record(rec["path"]) == rec, rec["path"]
    return rec


def read_json(path):
    return json.loads(safe(path).read_text())


def summary(records):
    # Explicit NEW documentary convention; not an older helper replay.
    raw = json.dumps(records, sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(records),
            "unique_paths": len({r["path"] for r in records}),
            "canonical_sha256": hashlib.sha256(raw).hexdigest()}


def exclusive_json(path, value):
    assert path.startswith(P)
    with safe(path).open("x") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def inputs():
    for path, (size, sha) in FIXED.items():
        assert record(path) == {"path": path, "bytes": size, "sha256": sha}
    author = read_json(AF)
    assert author["whole_obligations"] == 64 and author["ENTIRE_files"] == 14
    assert len(author["payload_records"]) == 13
    author_records = [checked(r) for r in author["payload_records"]] + [record(AF)]
    old = read_json(A + "baseline-v1.json")
    assert old["guard_summary"] == AUTHOR_GUARD
    assert author["guard_summary"] == AUTHOR_GUARD
    assert read_json(A + "input-validation-v1.json")["guard_summary"] == AUTHOR_GUARD
    old_records = [checked(r) for r in old["guard_records"]]
    assert len(old_records) == 37 and len({r["path"] for r in old_records}) == 37
    parent = read_json(PARENT)
    parent_records = [checked(r) for r in parent["payload_records"]] + [record(PARENT)]
    assert len(parent_records) == 5
    assert parent["older_plus_NEW5_own_paths_bound_transitively"] == 990
    extras = [record(path) for path in EXTRAS]
    records = author_records + old_records + parent_records + extras
    # Exact accepted DR8 suffix, checked as bytes rather than an authority inference.
    candidate = safe("problems/2025-B4/notes/reasoning-diagonal-return-r8-candidate-v1.md").read_bytes()
    accepted = safe("problems/2025-B4/proofs/reviewed-reasoning-diagonal-return-r8-v1.1.md").read_bytes()
    assert accepted.endswith(candidate)
    return author_records, old_records, parent_records, extras, records


def labels():
    expected = [f"R10-{i:02d}" for i in range(1, 65)]
    for suffix in ("obligations-v1.md", "checks-v1.md"):
        ids = re.findall(r"^\| (R10-\d\d) \|", safe(A + suffix).read_text(), re.M)
        assert ids == expected, (suffix, ids)
    report = safe(P + "initial-v1.md").read_text()
    ids = re.findall(r"^\|(R10-\d\d)\|PASS[^|]*\|", report, re.M)
    assert ids == expected, ids
    notes = re.findall(r"^\|R10R2-N(\d+)\|CLOSED", report, re.M)
    assert notes == [str(i) for i in range(1, 13)], notes
    src = read_json(P + "sources-v1.json")
    assert src["whole_obligations"] == 64 and src["closed_scope_notes"] == 12
    assert src["substantive_defects"] == 0 and src["required_author_repairs"] == 0
    assert src["corresponding_NEW_R10_peer_finding_file_actualinventory_hash_metadata_commentary_accessed"] is False
    return {"author_literal_obligations": 64, "author_literal_checks": 64,
            "review_literal_dispositions": 64, "closed_scope_notes": 12,
            "mathematical_truth_checked_by_code": False}


def prepare():
    ars, ors, prs, extras, records = inputs()
    literal = labels()
    baseline = {
        "prepared_utc": now(), "scope": "NEW documentary preservation only",
        "author_ENTIRE_records": ars,
        "author_37_guards_bound_by_immutable_baseline": {
            "baseline": record(A + "baseline-v1.json"),
            "declared_summary": AUTHOR_GUARD,
            "all_37_current_bytes_verified": True,
            "historical_inventory_copied_or_old_code_run": False},
        "extra_current_authority_records": extras,
        "own_immediate_parent": record(PARENT),
        "own_parent_ENTIRE5_summary": summary(prs),
        "older_own_paths_bound_transitively": 990,
        "older_plus_NEW5_own_paths_bound_transitively": 995,
        "all_guard_summary": summary(records), "literal_checks": literal,
        "author_current_math_read_limits": "report and structured sources; fingerprinting alone is not a fresh source read",
        "no_corresponding_NEW_peer_file_inventory_hash_metadata_access": True,
        "root_current_weekly_TOTAL_percent": 66,
        "authorized_reset_only": 1792874445, "TOTAL_ceiling": 90,
        "integration_reserve": True, "automatic_later_window_spending": False}
    exclusive_json(BASE, baseline)
    print(json.dumps({"prepared": record(BASE), "guard_summary": summary(records),
                      "literal_checks": literal}, indent=2))


def freeze(full_model_readback):
    assert full_model_readback, "Actual FULL final MODEL ALL4 payload readback must precede freeze"
    _, _, _, _, records = inputs()
    baseline = read_json(BASE)
    assert summary(records) == baseline["all_guard_summary"]
    for rec in baseline["extra_current_authority_records"]:
        checked(rec)
    literal = labels()
    manifest = {
        "frozen_utc": now(), "role": "OTHER initially blind ENTIRE WHOLE2 R10A-D",
        "reviewer": "/root/review_2022_complexity_r2", "C_constructor_excluded": True,
        "whole_obligations": 64, "ENTIRE_files": 5,
        "payload_records": [record(path) for path in PAYLOADS],
        "author_main": record(MAIN), "author_freeze": record(AF),
        "all_guard_summary": summary(records), "own_immediate_parent": record(PARENT),
        "older_own_paths_bound_transitively": 990,
        "older_plus_NEW5_own_paths_bound_transitively": 995,
        "literal_checks": literal,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "effective_readback": None,
        "FULL_final_MODEL_ALL4_payload_readback_completed": True,
        "FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required": True,
        "corresponding_NEW_peer_access": False,
        "findings_EMBARGO_until_explicit_BOTH_ENTIRE": True,
        "mathematical_program_CAS_scan_test_old_replay": False,
        "old_shared_Git_cache_mutation": False,
        "weekly": {"authority": "root direct telemetry received",
                   "at_utc": "2026-10-18 22:27 UTC", "TOTAL_used_percent": 66,
                   "resetsAt": 1792874445, "ceiling_TOTAL_percent": 90,
                   "integration_reserve": True, "automatic_later_window_spending": False}}
    exclusive_json(MAN, manifest)
    print(json.dumps({"frozen": record(MAN), "utc": manifest["frozen_utc"],
                      "ENTIRE_files": 5, "whole_obligations": 64}, indent=2))


def verify():
    manifest = read_json(MAN)
    assert manifest["ENTIRE_files"] == 5 and manifest["whole_obligations"] == 64
    assert [r["path"] for r in manifest["payload_records"]] == PAYLOADS
    for rec in manifest["payload_records"]:
        checked(rec)
    _, _, _, _, records = inputs()
    assert summary(records) == manifest["all_guard_summary"]
    assert labels() == manifest["literal_checks"]
    for rec in read_json(BASE)["extra_current_authority_records"]:
        checked(rec)
    print(json.dumps({"verified_utc": now(), "status": "PASS",
                      "ENTIRE_files": 5, "whole_obligations": 64,
                      "guard_summary": summary(records),
                      "manifest": record(MAN),
                      "report": record(P + "initial-v1.md"),
                      "read_only": True, "mathematical_program": False}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "freeze", "verify"))
    parser.add_argument("--full-model-readback", action="store_true")
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    elif args.mode == "freeze":
        freeze(args.full_model_readback)
    else:
        verify()
