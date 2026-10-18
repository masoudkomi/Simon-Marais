#!/usr/bin/env python3
"""SQ15 exclusive byte/JSON administration; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2020-B4/notes/reasoning-class-return-sq15-"
PARENT = "problems/2021-B4/reviews/reasoning-center-return-r19-review-3-manifest-v1.1.json"
STEMS = ["reasoning-arithmetic-return-r14", "reasoning-return-r8", "reasoning-Todd-return-r12"]
STATIC = ["candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
          "failures-v1.md", "sources-v1.md", "sources-v1.json", "worklog-v1.md",
          "code-log-v1.md", "admin-v1.py"]
GENERATED = ["baseline-v1.json", "input-validation-v1.json", "metadata-v1.json"]
DIRECT = ["AGENTS.md", "problems/2020-B4/statement.md", PARENT]
for stem in STEMS:
    DIRECT.append("problems/2020-B4/proofs/reviewed-" + stem + "-v1.1.md")
    DIRECT.extend("problems/2020-B4/reviews/" + stem + "-acceptance." + ext
                  for ext in ["md", "json"])
DIRECT.extend([
    "problems/2020-B4/notes/reasoning-arithmetic-return-r14-sources-v1.md",
    "problems/2020-B4/notes/reasoning-arithmetic-return-r14-failed-routes-v1.md",
    "problems/2020-B4/notes/reasoning-Todd-return-r12-sources-v1.md",
    "problems/2020-B4/notes/deep-literature-r1-report-v1.md"])
EXPECTED = {
    "AGENTS.md": (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
    PARENT: (3803, "af2307566d3a2ee8b23ca40f0198f2aa97af4f6bb95840d4682b142dc1e8ece8"),
    "problems/2020-B4/proofs/reviewed-reasoning-arithmetic-return-r14-v1.1.md":
        (22470, "befc8237c23eaac3e210d0aa3f28eaef44a01d4e771e3a4d156b18fd6b6bedb5"),
    "problems/2020-B4/proofs/reviewed-reasoning-return-r8-v1.1.md":
        (29871, "9003af18926d1fe49d3f997b40ed070ceefa37e42f73c5a98c32bbe7a2f3bfcb"),
    "problems/2020-B4/proofs/reviewed-reasoning-Todd-return-r12-v1.1.md":
        (35569, "f1663778cf78c18b3cb30a4702d7fbff95be29ab73c5f8e4f74d344362c8fba6")
}


def utc():
    return datetime.now(timezone.utc).isoformat()


def safe(path):
    if "reasoning-class-return-sq15" in path and "/reviews/" in path:
        raise ValueError("future corresponding SQ15 peer access prohibited")
    return path


def fp(path):
    path = safe(str(path))
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def jread(path):
    return json.loads((ROOT / safe(path)).read_text())


def check(row):
    actual = fp(row["path"])
    if actual != row:
        raise ValueError({"declared": row, "actual": actual})


def canonical(rows):
    unique = {}
    for row in rows:
        if row["path"] in unique and unique[row["path"]] != row:
            raise ValueError("conflicting immutable guard")
        unique[row["path"]] = row
    ordered = [unique[path] for path in sorted(unique)]
    digest = hashlib.sha256(json.dumps(ordered, sort_keys=True,
        separators=(",", ":")).encode()).hexdigest()
    return ordered, digest


def labels():
    text = (ROOT / (P + "obligations-v1.md")).read_text()
    ids = re.findall(r"(?m)^\|SQ15-(\d{2})\|", text)
    if ids != [f"{i:02d}" for i in range(1, 49)]:
        raise ValueError("exact ALL48 obligation labels required")


def snapshot():
    for path, (size, sha) in EXPECTED.items():
        check({"path": path, "bytes": size, "sha256": sha})
    rows = [fp(path) for path in DIRECT]
    authorities = []
    for stem in STEMS:
        path = "problems/2020-B4/reviews/" + stem + "-acceptance.json"
        authority = jread(path)
        if authority["unresolved_substantive_issues"] != 0:
            raise ValueError("old operative acceptance differs")
        check(authority["accepted_copy"])
        check(authority["candidate"])
        if not (ROOT / authority["accepted_copy"]["path"]).read_bytes().endswith(
                (ROOT / authority["candidate"]["path"]).read_bytes()):
            raise ValueError("old accepted-copy exact suffix mismatch")
        rows.append(authority["candidate"])
        authorities.append({"authority": fp(path),
            "accepted_copy": authority["accepted_copy"],
            "exact_candidate_suffix": authority["candidate"],
            "historical_inventory_NOT_recursively_expanded": True})
    parent = jread(PARENT)
    payload = parent["payloads"]
    if len(payload) != 11 or parent["ENTIRE_files"] != 12:
        raise ValueError("own parent packet count drift")
    for row in payload:
        check(row)
    rows.extend(payload)
    parent_unique, parent_digest = canonical(payload)
    unique, digest = canonical(rows)
    labels()
    return {"direct_inputs": [fp(path) for path in DIRECT],
        "accepted_input_bindings": authorities,
        "compact_immediate_own_parent": {"manifest": fp(PARENT),
            "declared_payload_occurrences": len(payload),
            "verified_unique_payload_paths": len(parent_unique),
            "canonical_payload_sha256": parent_digest,
            "parent_guard_summary_preserved_by_manifest_identity_only": {
                "occurrences": parent["necessary_guard_occurrences"],
                "unique_paths": parent["necessary_guard_unique_paths"],
                "canonical_sha256": parent["canonical_guard_sha256"]},
            "no_fresh_recursive_historical_read_claim": True},
        "necessary_guard_occurrences": len(rows),
        "necessary_guard_unique_paths": len(unique),
        "canonical_guard_sha256": digest,
        "necessary_guards": unique}


def write_new(suffix, obj):
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def prepare():
    snap = snapshot()
    for suffix in STATIC:
        fp(P + suffix)
    write_new("baseline-v1.json", {"created_at_utc": utc(),
        "status": "candidate proof - unverified",
        "mutable_contexts_read_but_NOT_immutable_math_guards": [
            "README.md opening1--72", "problems/2020-B4/research.md",
            "problems/2020-B4/references.md"], **snap})
    write_new("input-validation-v1.json", {"checked_at_utc": utc(),
        "result": "PASS", "ALL_obligations": 48,
        "accepted_body_authority_candidate_suffixes_match": True,
        "immediate_own_parent_ENTIRE": 12,
        "necessary_guard_occurrences": snap["necessary_guard_occurrences"],
        "necessary_guard_unique_paths": snap["necessary_guard_unique_paths"],
        "canonical_guard_sha256": snap["canonical_guard_sha256"],
        "mathematical_program_or_scan": False})
    write_new("metadata-v1.json", {"created_at_utc": utc(),
        "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1", "constructor_excluded": True,
        "claims": ["SQ15A", "SQ15B", "SQ15C", "SQ15D"],
        "whole_obligations": 48,
        "root_supplied_new_proof_inference": False,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "actual_set_prime_conductor_q_ge3_only": True,
        "new_q_class_computation_annual_or_priority_claim": False,
        "source_body_unread_limit": "Schmidt1998 encoded; 2005 fixing and2018 larger theorem only literal partial reads",
        "mathematical_program_CAS_scan_author_source_old_replay": False,
        "native_child_PID_pending_approval_or_stall": None,
        "requested_inherited": {"model": "gpt-6.1-sol", "reasoning": "max"},
        "verified_effective_readback": None,
        "payload_files": len(STATIC + GENERATED),
        "ENTIRE_files_including_freeze": len(STATIC + GENERATED) + 1,
        "FULL_final_ALL_payload_model_readback_required": True,
        "FULL_freeze_readback_then_SEPARATE_verify_required": True,
        "authoritative_usage": {"at_utc": "2026-10-18 15:34:20 UTC",
            "TOTAL_used_percent": 47, "window_minutes": 10080,
            "resetsAt": 1792874445, "ordinary_usage_allowed": True,
            "legacy_by_limit_agree": True,
            "TOTAL_ceiling": 90, "integration_reserve": True,
            "no_automatic_later_window": True}})
    print(json.dumps({"prepare": "PASS", "ALL48": True,
        "guard_occurrences": snap["necessary_guard_occurrences"],
        "unique_paths": snap["necessary_guard_unique_paths"]}))


def validate():
    snap = snapshot()
    base = jread(P + "baseline-v1.json")
    for key, value in snap.items():
        if base[key] != value:
            raise ValueError("necessary immutable input drift: " + key)
    return snap


def freeze():
    snap = validate()
    payload = [fp(P + suffix) for suffix in STATIC + GENERATED]
    for row in payload:
        if row["path"].endswith(".json"):
            jread(row["path"])
    write_new("freeze-v1.json", {"frozen_at_utc": utc(),
        "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1", "constructor_excluded": True,
        "claims": ["SQ15A", "SQ15B", "SQ15C", "SQ15D"],
        "whole_obligations": 48,
        "root_supplied_new_proof_inference": False,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "immediate_own_parent": fp(PARENT),
        "compact_baseline": fp(P + "baseline-v1.json"),
        "payload_files": len(payload), "ENTIRE_files": len(payload) + 1,
        "FULL_final_ALL12_payload_model_readback_completed": True,
        "FULL_freeze_model_readback_then_SEPARATE_verify_REQUIRED": True,
        "necessary_guard_occurrences": snap["necessary_guard_occurrences"],
        "necessary_guard_unique_paths": snap["necessary_guard_unique_paths"],
        "canonical_guard_sha256": snap["canonical_guard_sha256"],
        "mathematical_program_CAS_scan_replay": False,
        "payloads": payload})
    print(json.dumps({"freeze": fp(P + "freeze-v1.json")}))


def verify():
    manifest = jread(P + "freeze-v1.json")
    if (manifest["whole_obligations"], manifest["payload_files"], manifest["ENTIRE_files"]) != (48, 12, 13):
        raise ValueError("ENTIRE packet count drift")
    for row in manifest["payloads"]:
        check(row)
    snap = validate()
    if manifest["canonical_guard_sha256"] != snap["canonical_guard_sha256"]:
        raise ValueError("guard digest drift")
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "verified_at_utc": utc(),
        "ENTIRE_files": 13, "ALL_obligations": 48,
        "necessary_guard_occurrences": snap["necessary_guard_occurrences"],
        "necessary_guard_unique_paths": snap["necessary_guard_unique_paths"],
        "main": fp(P + "candidate-v1.md"), "freeze": fp(P + "freeze-v1.json")}, indent=2))


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) == 2 else ""
    if action not in {"prepare", "freeze", "verify"}:
        raise SystemExit("usage: admin-v1.py prepare|freeze|verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[action]()
