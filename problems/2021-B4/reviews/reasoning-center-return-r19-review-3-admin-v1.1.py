#!/usr/bin/env python3
"""Exclusive review byte/JSON administration only; no mathematical execution."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2021-B4/reviews/reasoning-center-return-r19-review-3-"
A = "problems/2021-B4/notes/reasoning-center-return-r19-"
OWN_PARENT = "problems/2024-B4/notes/reasoning-cofactor-return-r8-freeze-v1.json"
STATIC = ["initial-v1.1.md", "ledger-v1.1.md", "issues-v1.1.md",
          "sources-v1.1.md", "sources-v1.1.json", "worklog-v1.1.md",
          "code-log-v1.1.md", "admin-v1.1.py"]
GENERATED = ["baseline-v1.1.json", "input-validation-v1.1.json", "metadata-v1.1.json"]
AUTHOR = A + "freeze-v1.1.json"
ORIGINAL = A + "freeze-v1.json"
BUNDLES = [(AUTHOR, "payloads", 15), (ORIGINAL, "payloads", 12),
           (OWN_PARENT, "artifacts", 12)]
ACCEPTED = ["reasoning-center-return-r18", "reasoning-center-return-r17",
            "reasoning-return-r8", "reasoning-return-r5"]
DIRECT = ["AGENTS.md", "problems/2021-B4/statement.md", AUTHOR, ORIGINAL, OWN_PARENT]
for stem in ACCEPTED:
    DIRECT.append("problems/2021-B4/proofs/reviewed-" + stem + "-v1.1.md")
    DIRECT.extend("problems/2021-B4/reviews/" + stem + "-acceptance." + ext
                  for ext in ["md", "json"])
DIRECT.extend([
    "problems/2021-B4/notes/reasoning-center-return-r18-failures-v1.md",
    "problems/2021-B4/notes/reasoning-center-return-r17-failures-v1.md",
    "problems/2021-B4/notes/reasoning-return-r8-failed-routes-v1.md"])
EXPECTED = {
    A + "candidate-v1.1.md": (23302, "fd5a5399414c60c20797b63dfa9f55b8f66ac679fdd5458488c3250e3605a56a"),
    AUTHOR: (4753, "1b86a88b22a1cf755836900d314e26b7ac109f83e3031b03254a78a3d36f49fd"),
    A + "candidate-v1.md": (17591, "589eddbf5f305b3380ee2c499d774aff8bb1b4499aa46c15c3dbffcf1bd56462"),
    ORIGINAL: (3893, "dfe7b6b4f372b44a2806fc96ce41613bfc2fb7e8f5469fc2d10552aa83b835d3"),
    OWN_PARENT: (3554, "05075573ae2f40c214473d309de4c9490dbe0c404e60c8f1ddde5b9e2d79dbe3"),
    "problems/2021-B4/proofs/reviewed-reasoning-center-return-r18-v1.1.md":
        (26067, "f26de3a17895354408e514d6a0b0066715a1c0f0234d494fd53485ea3feb8284"),
    "problems/2021-B4/proofs/reviewed-reasoning-center-return-r17-v1.1.md":
        (23107, "8c8daa274ea6dcf95e25249e215b09646c3473c4ccd6320302a364b0af5b7797"),
    "problems/2021-B4/proofs/reviewed-reasoning-return-r8-v1.1.md":
        (19921, "33b8713d402d09f711d0096cdc4e8c00f9e622a5335f8e3345eb4f82ba0d359d"),
    "problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md":
        (23675, "f4f088adc133b0581520488cdbba30082c13b2402c96ae555142e5491ad4137d")
}


def utc():
    return datetime.now(timezone.utc).isoformat()


def allowed(path):
    if path.startswith("problems/2021-B4/reviews/reasoning-center-return-r19-review-"):
        if not path.startswith(P):
            raise ValueError("No corresponding NEW or old peer review path is opened by this script")
    return path


def fp(path):
    path = allowed(str(path))
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def read_json(path):
    return json.loads((ROOT / allowed(path)).read_text())


def check(row):
    if fp(row["path"]) != row:
        raise ValueError({"immutable_declared": row, "actual": fp(row["path"])})


def canonical(rows):
    unique = {}
    for row in rows:
        if row["path"] in unique and unique[row["path"]] != row:
            raise ValueError("conflicting immutable declaration")
        unique[row["path"]] = row
    ordered = [unique[path] for path in sorted(unique)]
    digest = hashlib.sha256(json.dumps(ordered, sort_keys=True,
        separators=(",", ":")).encode()).hexdigest()
    return ordered, digest


def verify_text_labels():
    text = (ROOT / (P + "ledger-v1.1.md")).read_text()
    if re.findall(r"(?m)^\|R19-(\d{2})\|", text) != [f"{i:02d}" for i in range(1, 65)]:
        raise ValueError("complete original64 reviewer rows required")
    if re.findall(r"(?m)^\|R19-FC(\d{2})\|", text) != [f"{i:02d}" for i in range(1, 13)]:
        raise ValueError("complete repair12 reviewer rows required")
    old = (ROOT / (A + "candidate-v1.md")).read_text()
    new = (ROOT / (A + "candidate-v1.1.md")).read_text()
    expected = "".join(difflib.unified_diff(old.splitlines(keepends=True),
        new.splitlines(keepends=True),
        fromfile="reasoning-center-return-r19-candidate-v1.md",
        tofile="reasoning-center-return-r19-candidate-v1.1.md"))
    if (ROOT / (A + "diff-v1-to-v1.1.patch")).read_text() != expected:
        raise ValueError("author textual diff mismatch")


def snapshot():
    for path, (size, sha) in EXPECTED.items():
        check({"path": path, "bytes": size, "sha256": sha})
    rows = [fp(path) for path in DIRECT]
    bindings = []
    for path, key, count in BUNDLES:
        obj = read_json(path)
        payload = obj[key]
        if len(payload) != count:
            raise ValueError("fixed parent payload count drift")
        for row in payload:
            check(row)
        unique, digest = canonical(payload)
        bindings.append({"parent": fp(path), "payload_key": key,
            "declared_payload_occurrences": count,
            "verified_unique_payload_paths": len(unique),
            "canonical_payload_sha256": digest,
            "no_recursive_historical_inventory_expansion": True})
        rows.extend(payload)
    for stem in ACCEPTED:
        authority = read_json("problems/2021-B4/reviews/" + stem + "-acceptance.json")
        check(authority["accepted_copy"])
        if authority["unresolved_substantive_issues"] != 0:
            raise ValueError("operative old input authority differs")
    verify_text_labels()
    unique, digest = canonical(rows)
    return {"direct_inputs": [fp(path) for path in DIRECT],
            "compact_parent_bindings": bindings,
            "necessary_guard_occurrences": len(rows),
            "necessary_guard_unique_paths": len(unique),
            "canonical_guard_sha256": digest,
            "necessary_guards": unique}


def write_new(suffix, obj):
    path = ROOT / (P + suffix)
    with path.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def prepare():
    snap = snapshot()
    for suffix in STATIC:
        fp(P + suffix)
    write_new("baseline-v1.1.json", {"created_at_utc": utc(),
        "scope": "necessary immutable inputs and compact parent bindings only",
        "mathematical_history_read_claim": False, **snap})
    write_new("input-validation-v1.1.json", {"verified_at_utc": utc(),
        "result": "PASS", "author_ENTIRE_files": 16,
        "original_author_ENTIRE_files": 13, "immediate_own_parent_ENTIRE_files": 13,
        "review_original_rows": 64, "review_repair_rows": 12,
        "exact_textual_diff_matches": True,
        "necessary_guard_occurrences": snap["necessary_guard_occurrences"],
        "necessary_guard_unique_paths": snap["necessary_guard_unique_paths"],
        "canonical_guard_sha256": snap["canonical_guard_sha256"],
        "corresponding_NEW_affected_peer_access": False,
        "mathematical_program_or_scan": False})
    write_new("metadata-v1.1.json", {"created_at_utc": utc(),
        "reviewer": "/root/review_2017_coarsening_r1",
        "status": "initial independent affected WHOLE3; findings EMBARGOED pending explicit release",
        "new_R19_constructor": False,
        "old_roles": "OLD R5/R17 constructor and OLD R8 reviewer, accepted dependencies only",
        "whole_obligations": 76, "original": 64, "repair": 12,
        "static_payload_files": len(STATIC),
        "total_payload_files": len(STATIC + GENERATED),
        "ENTIRE_files_with_manifest": len(STATIC + GENERATED) + 1,
        "source_binary_download_hashes": None,
        "requested_inherited": {"model": "gpt-6.1-sol", "reasoning": "max"},
        "verified_effective_readback": None,
        "corresponding_NEW_root_B_affected_access": False,
        "findings_release_before_explicit_confirmation": False,
        "FULL_final_ALL_files_model_readback_required": True,
        "SEPARATE_readonly_verify_required_after_manifest_readback": True,
        "authorized_weekly_reset_only": 1792874445,
        "TOTAL_ceiling": 90, "integration_reserve": True,
        "mathematical_program_CAS_scan_replay": False,
        "native_math_child_PID_or_pending_approval": None})
    print(json.dumps({"prepare": "PASS", "original": 64, "repair": 12,
        "guard_occurrences": snap["necessary_guard_occurrences"],
        "unique_paths": snap["necessary_guard_unique_paths"]}))


def validate():
    base = read_json(P + "baseline-v1.1.json")
    snap = snapshot()
    for key, value in snap.items():
        if base[key] != value:
            raise ValueError("immutable baseline drift: " + key)
    return snap


def freeze():
    snap = validate()
    payloads = [fp(P + suffix) for suffix in STATIC + GENERATED]
    for row in payloads:
        if row["path"].endswith(".json"):
            read_json(row["path"])
    write_new("manifest-v1.1.json", {"frozen_at_utc": utc(),
        "status": "independent affected WHOLE3 initial frozen; no promotion",
        "reviewer": "/root/review_2017_coarsening_r1", "new_constructor": False,
        "whole_obligations": 76, "original64": 64, "repair12": 12,
        "author": fp(A + "candidate-v1.1.md"), "author_manifest": fp(AUTHOR),
        "immediate_own_parent": fp(OWN_PARENT),
        "payload_files": len(payloads), "ENTIRE_files": len(payloads) + 1,
        "FULL_final_ALL11_payload_model_readback_completed": True,
        "FULL_final_manifest_readback_then_SEPARATE_verify_REQUIRED": True,
        "corresponding_NEW_root_B_affected_peer_access": False,
        "mathematical_findings_EMBARGOED_until_explicit_completion_release": True,
        "necessary_guard_occurrences": snap["necessary_guard_occurrences"],
        "necessary_guard_unique_paths": snap["necessary_guard_unique_paths"],
        "canonical_guard_sha256": snap["canonical_guard_sha256"],
        "mathematical_program_CAS_scan_replay": False,
        "payloads": payloads})
    print(json.dumps({"freeze": fp(P + "manifest-v1.1.json")}))


def verify():
    manifest = read_json(P + "manifest-v1.1.json")
    if (manifest["whole_obligations"], manifest["payload_files"], manifest["ENTIRE_files"]) != (76, 11, 12):
        raise ValueError("ENTIRE review count mismatch")
    for row in manifest["payloads"]:
        check(row)
    snap = validate()
    if manifest["canonical_guard_sha256"] != snap["canonical_guard_sha256"]:
        raise ValueError("manifest guard digest drift")
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "verified_at_utc": utc(),
        "ENTIRE_files": 12, "whole_obligations": 76,
        "necessary_guard_occurrences": snap["necessary_guard_occurrences"],
        "necessary_guard_unique_paths": snap["necessary_guard_unique_paths"],
        "main": fp(P + "initial-v1.1.md"),
        "manifest": fp(P + "manifest-v1.1.json")}, indent=2))


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) == 2 else ""
    if action not in {"prepare", "freeze", "verify"}:
        raise SystemExit("usage: admin-v1.1.py prepare|freeze|verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[action]()
