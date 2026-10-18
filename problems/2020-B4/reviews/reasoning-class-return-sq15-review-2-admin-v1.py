#!/usr/bin/env python3
"""SQ15 review2 documentary administration only; no mathematical code."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2020-B4/reviews/reasoning-class-return-sq15-review-2-"
AUTHOR = "problems/2020-B4/notes/reasoning-class-return-sq15-"
PARENT = "problems/2025-B4/notes/reasoning-diagonal-return-r7-freeze-v1.json"
BASE, VALID, META, MAN = [P + name + "-v1.json" for name in
                          ("baseline", "input-validation", "metadata", "manifest")]
STEMS = ["reasoning-arithmetic-return-r14", "reasoning-return-r8",
         "reasoning-Todd-return-r12"]
STATIC = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "sources-v1.md",
          "sources-v1.json", "worklog-v1.md", "admin-v1.py"]
PAYLOADS = [P + name for name in STATIC] + [BASE, VALID, META]
DIRECT = ["AGENTS.md", "problems/2020-B4/statement.md"]
for stem in STEMS:
    DIRECT.append("problems/2020-B4/proofs/reviewed-" + stem + "-v1.1.md")
    DIRECT.extend("problems/2020-B4/reviews/" + stem + "-acceptance." + ext
                  for ext in ("md", "json"))
DIRECT += [
    "problems/2020-B4/notes/reasoning-arithmetic-return-r14-sources-v1.md",
    "problems/2020-B4/notes/reasoning-arithmetic-return-r14-failed-routes-v1.md",
    "problems/2020-B4/notes/reasoning-Todd-return-r12-sources-v1.md",
    "problems/2020-B4/notes/deep-literature-r1-report-v1.md",
]
EXPECTED = [
    {"path": AUTHOR + "candidate-v1.md", "bytes": 20209,
     "sha256": "11182beb9e08841d8ecce07008caafe93ca65222fdd34937493bf9a4c9715e78"},
    {"path": AUTHOR + "freeze-v1.json", "bytes": 3677,
     "sha256": "bc7bb2ef06d6e90dc083841fac5853209b7a45e36bc0ae5b16e512efa7c94975"},
    {"path": PARENT, "bytes": 3663,
     "sha256": "5a029bb837c9fc8232f3364262d4d9ca66370e10d60e1dd545d5c5441798c412"},
]


def utc():
    return datetime.now(timezone.utc).isoformat()


def path(rel):
    if "reasoning-class-return-sq15-review-" in rel and not rel.startswith(P):
        raise AssertionError("corresponding NEW peer SQ15 material is embargoed")
    if "reasoning-center-return-r20-review-" in rel:
        raise AssertionError("separate NEW R20 peer content is not needed or accessed")
    pp = Path(rel)
    if pp.is_absolute() or ".." in pp.parts:
        raise AssertionError("exact relative documentary path required")
    return ROOT / pp


def fp(rel):
    data = path(rel).read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def jread(rel):
    return json.loads(path(rel).read_text())


def check(row):
    if fp(row["path"]) != row:
        raise AssertionError("immutable fingerprint mismatch: " + row["path"])


def summary(rows):
    unique = {}
    for row in rows:
        previous = unique.setdefault(row["path"], row)
        if previous != row:
            raise AssertionError("conflicting current fingerprint")
    ordered = [unique[key] for key in sorted(unique)]
    encoded = json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(ordered),
            "canonical_sha256": hashlib.sha256(encoded).hexdigest()}


def check_all(rows):
    seen = set()
    for row in rows:
        if row["path"] not in seen:
            check(row)
            seen.add(row["path"])
    return summary(rows)


def labels():
    found = re.findall(r"^\| (SQ15-[0-9]{2}) \|", path(P + "ledger-v1.md").read_text(), re.M)
    expected = ["SQ15-" + str(i).zfill(2) for i in range(1, 49)]
    if found != expected:
        raise AssertionError("exact ALL48 ordered ledger labels required")
    author = re.findall(r"^\|SQ15-([0-9]{2})\|", path(AUTHOR + "obligations-v1.md").read_text(), re.M)
    if author != [str(i).zfill(2) for i in range(1, 49)]:
        raise AssertionError("author ALL48 label mismatch")


def snapshot():
    for row in EXPECTED:
        check(row)
    author_manifest = jread(AUTHOR + "freeze-v1.json")
    if (author_manifest["ENTIRE_files"], author_manifest["whole_obligations"],
            len(author_manifest["payloads"])) != (13, 48, 12):
        raise AssertionError("author ENTIRE13/48 mismatch")
    author_rows = author_manifest["payloads"] + [fp(AUTHOR + "freeze-v1.json")]
    check_all(author_rows)
    author_base = jread(AUTHOR + "baseline-v1.json")
    guard_rows = author_base["necessary_guards"]
    check_all(guard_rows)
    own_parent = jread(PARENT)
    if own_parent["ENTIRE_files"] != 14 or len(own_parent["artifacts"]) != 13:
        raise AssertionError("immediate own parent count mismatch")
    parent_rows = own_parent["artifacts"] + [fp(PARENT)]
    check_all(parent_rows)
    direct = [fp(rel) for rel in DIRECT]
    suffixes = []
    for stem in STEMS:
        authority_path = "problems/2020-B4/reviews/" + stem + "-acceptance.json"
        authority = jread(authority_path)
        if authority["unresolved_substantive_issues"] != 0:
            raise AssertionError("accepted input authority changed")
        check(authority["accepted_copy"])
        check(authority["candidate"])
        if not path(authority["accepted_copy"]["path"]).read_bytes().endswith(
                path(authority["candidate"]["path"]).read_bytes()):
            raise AssertionError("accepted exact candidate suffix mismatch")
        suffixes.append({"authority": fp(authority_path),
                         "accepted_copy": authority["accepted_copy"],
                         "exact_candidate_suffix": authority["candidate"]})
    rows = author_rows + guard_rows + parent_rows + direct
    protection = check_all(rows)
    labels()
    return {
        "author_manifest": fp(AUTHOR + "freeze-v1.json"),
        "author_ENTIRE_summary": summary(author_rows),
        "author_input_baseline_binding": fp(AUTHOR + "baseline-v1.json"),
        "author_necessary_guard_summary": summary(guard_rows),
        "direct_current_operative_inputs": direct,
        "accepted_exact_suffix_bindings": suffixes,
        "immediate_own_parent": {"manifest": fp(PARENT),
            "ENTIRE_summary": summary(parent_rows),
            "historical_transitive_summary_bound_not_reexpanded": own_parent["protected_current_summary"]},
        "all_current_protected_summary": protection,
        "compact_policy": "Check necessary declared frozen current records; bind immutable metadata/counts without recopying giant historical inventories",
    }


def write_new(rel, value):
    if not rel.startswith(P):
        raise AssertionError("write outside exclusive review prefix")
    with path(rel).open("x", encoding="utf-8") as out:
        json.dump(value, out, ensure_ascii=False, indent=2)
        out.write("\n")


def validate():
    current = snapshot()
    base = jread(BASE)
    if current != base["immutable_bindings"]:
        raise AssertionError("review input bindings changed")
    return current


def prepare():
    for rel in (BASE, VALID, META, MAN):
        if path(rel).exists():
            raise AssertionError("exclusive new output already exists")
    for name in STATIC:
        fp(P + name)
    snap = snapshot()
    write_new(BASE, {"prepared_at_utc": utc(), "reviewer": "/root/review_2021_reasoning_j15_r2",
        "status": "initially blind ENTIRE WHOLE2 review; candidate unverified",
        "immutable_bindings": snap,
        "corresponding_NEW_root_peer_file_inventory_content_hash_metadata_commentary_access": False,
        "coordinator_counts_times_only_received_not_inputs": True,
        "old_parent_fingerprints_not_new_mathematical_read_claims": True})
    write_new(VALID, {"validated_at_utc": utc(), "result": "PASS",
        "author_ENTIRE_files": 13, "ALL_obligations": 48,
        "author_payloads_and_necessary_guards_match": True,
        "accepted_copies_exact_suffixes_match": True,
        "compact_current_protection": snap["all_current_protected_summary"],
        "math_program_scan_CAS_or_author_replay": False})
    write_new(META, {"status": "initially blind ENTIRE WHOLE2 review; candidate unverified",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "constructor": "/root/review_2017_coarsening_r1",
        "reviewer_NEW_constructive_contribution": False,
        "older_roles": "A whole-reviewed R8,TD and earlier2020 packets; not fresh independent recertification",
        "ALL_obligations_reconstructed": 48,
        "plain_PASS_rows": 42, "PASS_with_required_scope_issue_rows": 5, "OPEN_scope_row": 1,
        "required_issue": "SQ15R2-01: explicit INTEGRAL qualification for universal J/R/y claims",
        "additional_closed_scope_notes": 8,
        "additional_gap_in_integral_proof_found": False,
        "recommendation": "Full versioned author scope clarification and BOTH affected reaudits before promotion",
        "corresponding_NEW_root_peer_content_accessed": False,
        "coordinator_administrative_counts_times_only_received": True,
        "findings_embargo_until_explicit_BOTH_ENTIRE": True,
        "requested_inherited": {"model": "gpt-6.1-sol", "reasoning": "max"},
        "verified_effective_settings": None,
        "mathematical_program_CAS_scan_test_source_author_old_replay": False,
        "ALL_final_payload_model_readback_then_manifest_readback_and_SEPARATE_verify_required": True,
        "payload_files": 10, "ENTIRE_files": 11,
        "baseline": fp(BASE), "input_validation": fp(VALID),
        "weekly": {"at_utc": "2026-10-18 15:54:47 UTC", "TOTAL_used_percent": 49,
            "window_minutes": 10080, "reset": 1792874445, "ordinary_allowed": True,
            "TOTAL_ceiling": 90, "reserve": True, "automatic_later_window": False}})
    print(json.dumps({"prepare": "PASS", "ALL48": True, **snap["all_current_protected_summary"]}))


def freeze():
    snap = validate()
    payloads = [fp(rel) for rel in PAYLOADS]
    write_new(MAN, {"frozen_at_utc": utc(), "status": "initially blind ENTIRE WHOLE2 review",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "ALL_obligations": 48,
        "payload_files": 10, "ENTIRE_files": 11,
        "FULL_final_ALL10_payload_model_readback_completed": True,
        "FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED": True,
        "findings_embargo_until_explicit_BOTH_ENTIRE": True,
        "NEW_corresponding_root_peer_content_access": False,
        "compact_baseline": fp(BASE),
        "compact_current_protection": snap["all_current_protected_summary"],
        "payloads": payloads})
    print(json.dumps({"freeze": fp(MAN), "ENTIRE_files": 11, "ALL48": True}))


def verify():
    snap = validate()
    manifest = jread(MAN)
    if (manifest["ENTIRE_files"], manifest["ALL_obligations"], len(manifest["payloads"])) != (11, 48, 10):
        raise AssertionError("review entire count mismatch")
    check_all(manifest["payloads"])
    if manifest["compact_current_protection"] != snap["all_current_protected_summary"]:
        raise AssertionError("manifest protected summary mismatch")
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "verified_at_utc": utc(),
        "manifest": fp(MAN), "initial": fp(P + "initial-v1.md"),
        "ENTIRE_files": 11, "ALL_obligations": 48,
        **snap["all_current_protected_summary"], "no_file_written": True}))


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) == 2 else ""
    if action not in ("prepare", "freeze", "verify"):
        raise SystemExit("usage: new-review-admin prepare|freeze|verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[action]()
