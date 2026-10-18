#!/usr/bin/env python3
"""NEW D8 review documentary bytes/JSON/label checks only; no math execution."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2022-B4/reviews/reasoning-dynamics-return-r8-review-2-"
A = "problems/2022-B4/notes/reasoning-dynamics-return-r8-"
PARENT = "problems/2017-B4/reviews/reasoning-path-mass-return-r10-review-2-manifest-v1.json"
BASE, VALID, META, MAN = [P + name + "-v1.json" for name in
                         ("baseline", "input-validation", "metadata", "manifest")]
STATIC = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "sources-v1.md",
          "sources-v1.json", "worklog-v1.md", "admin-v1.py"]
PAYLOADS = [P + name for name in STATIC] + [BASE, VALID, META]
STEMS = ["reasoning-dynamics-return-r7", "reasoning-fiber-return-r5",
         "reasoning-complexity-return-r9-v3", "reasoning-dynamics-return-r6"]
DIRECT = ["AGENTS.md", "problems/2022-B4/statement.md"]
for stem in STEMS:
    version = "v3.1" if stem.endswith("-v3") else "v1.1"
    proof_stem = stem[:-3] if stem.endswith("-v3") else stem
    DIRECT.append("problems/2022-B4/proofs/reviewed-" + proof_stem + "-" + version + ".md")
    DIRECT.extend("problems/2022-B4/reviews/" + stem + "-acceptance." + ext
                  for ext in ("md", "json"))
DIRECT.extend("problems/2022-B4/notes/reasoning-dynamics-return-r7-" + name
              for name in ("failed-routes-v1.md", "sources-v1.md"))
EXPECTED = [
    {"path": A + "candidate-v1.md", "bytes": 18637,
     "sha256": "ea5c5b96714e0e12f10d6ce88bd4e8b7e89fcaf0baa64528e9fe5136e8f0c435"},
    {"path": A + "freeze-v1.json", "bytes": 3911,
     "sha256": "add639e38da1227a8382f8e5994dfeee78c414f53665b05d072b39251c7d77dd"},
    {"path": PARENT, "bytes": 3057,
     "sha256": "b0c542f29d0db3f1ce221218511685304f30a033545011bacad4a6f704b1d460"},
]


def utc():
    return datetime.now(timezone.utc).isoformat()


def path(rel):
    if "reasoning-dynamics-return-r8-review-" in rel and not rel.startswith(P):
        raise AssertionError("corresponding NEW root D8 access embargo")
    if "reasoning-center-return-r20-review-" in rel:
        raise AssertionError("unrelated R20 peer material not needed")
    pp = Path(rel)
    if pp.is_absolute() or ".." in pp.parts:
        raise AssertionError("exact workspace relative documentary path required")
    return ROOT / pp


def fp(rel):
    data = path(rel).read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def jread(rel):
    return json.loads(path(rel).read_text())


def check(row):
    expected = {key: row[key] for key in ("path", "bytes", "sha256")}
    if fp(row["path"]) != expected:
        raise AssertionError("immutable fingerprint mismatch: " + row["path"])


def summary(rows):
    unique = {}
    for row in rows:
        item = {key: row[key] for key in ("path", "bytes", "sha256")}
        old = unique.setdefault(item["path"], item)
        if old != item:
            raise AssertionError("conflicting current fingerprint")
    ordered = [unique[key] for key in sorted(unique)]
    data = json.dumps(ordered, sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(ordered),
            "canonical_sha256": hashlib.sha256(data).hexdigest()}


def check_all(rows):
    seen = set()
    for row in rows:
        if row["path"] not in seen:
            check(row)
            seen.add(row["path"])
    return summary(rows)


def labels():
    expected = ["D8-" + str(i).zfill(2) for i in range(1, 49)]
    ledger = re.findall(r"^\| (D8-\d\d) \| PASS \|", path(P + "ledger-v1.md").read_text(), re.M)
    author = re.findall(r"^\| (D8-\d\d) \|", path(A + "obligations-v1.md").read_text(), re.M)
    if ledger != expected or author != expected:
        raise AssertionError("exact ordered ALL48 labels required")


def snapshot():
    for row in EXPECTED:
        check(row)
    author = jread(A + "freeze-v1.json")
    if (author["ENTIRE_files"], author["whole_obligations"], len(author["payloads"])) != (14, 48, 13):
        raise AssertionError("author ENTIRE14/48 mismatch")
    author_rows = author["payloads"] + [fp(A + "freeze-v1.json")]
    check_all(author_rows)
    author_base = jread(A + "baseline-v1.json")
    guards = author_base["guards"]
    check_all(guards)
    parent = jread(PARENT)
    if parent["ENTIRE_files"] != 11 or len(parent["payloads"]) != 10:
        raise AssertionError("own immediate parent ENTIRE11 mismatch")
    parent_rows = parent["payloads"] + [fp(PARENT)]
    check_all(parent_rows)
    direct = [fp(rel) for rel in DIRECT]
    accepted = []
    for stem in STEMS:
        authority_path = "problems/2022-B4/reviews/" + stem + "-acceptance.json"
        authority = jread(authority_path)
        if authority["unresolved_substantive_issues"] != 0:
            raise AssertionError("accepted input status changed")
        check(authority["accepted_copy"])
        check(authority["candidate"])
        if not path(authority["accepted_copy"]["path"]).read_bytes().endswith(
                path(authority["candidate"]["path"]).read_bytes()):
            raise AssertionError("accepted exact suffix mismatch")
        accepted.append({"authority": fp(authority_path),
                         "accepted_copy": authority["accepted_copy"],
                         "exact_candidate_suffix": authority["candidate"]})
    protection = check_all(author_rows + guards + parent_rows + direct)
    labels()
    return {
        "author_manifest": fp(A + "freeze-v1.json"),
        "author_ENTIRE_summary": summary(author_rows),
        "author_input_baseline_binding": fp(A + "baseline-v1.json"),
        "author_necessary_guard_summary": summary(guards),
        "direct_current_inputs": direct,
        "accepted_exact_suffix_bindings": accepted,
        "immediate_own_parent": {"manifest": fp(PARENT),
            "ENTIRE_summary": summary(parent_rows),
            "historical_protected_summary_bound_not_reexpanded": parent["compact_current_protection"]},
        "all_current_protected_summary": protection,
        "compact_policy": "Necessary immutable current payloads checked, historical parent metadata/counts bound without expanding unrelated inventories or recertifying old mathematics",
    }


def write_new(rel, value):
    if not rel.startswith(P):
        raise AssertionError("write outside exclusive new review prefix")
    with path(rel).open("x", encoding="utf-8") as out:
        json.dump(value, out, ensure_ascii=False, indent=2)
        out.write("\n")


def validate():
    current = snapshot()
    if current != jread(BASE)["immutable_bindings"]:
        raise AssertionError("input bindings changed")
    return current


def prepare():
    for rel in (BASE, VALID, META, MAN):
        if path(rel).exists():
            raise AssertionError("exclusive new output already exists")
    for name in STATIC:
        fp(P + name)
    snap = snapshot()
    write_new(BASE, {"prepared_at_utc": utc(), "reviewer": "/root/review_2021_reasoning_j15_r2",
        "status": "OTHER initially blind ENTIRE WHOLE2 review; candidate unverified",
        "immutable_bindings": snap,
        "corresponding_NEW_root_D8_finding_inventory_file_hash_metadata_commentary_access": False,
        "coordinator_counts_times_only_received_not_inputs": True,
        "older_fingerprints_not_unrelated_fresh_mathematical_reads": True})
    write_new(VALID, {"validated_at_utc": utc(), "result": "PASS",
        "author_ENTIRE_files": 14, "ALL_obligations": 48,
        "author_payloads_and_necessary_frozen_inputs_match": True,
        "accepted_copies_exact_suffixes_match": True,
        "compact_current_protection": snap["all_current_protected_summary"],
        "mathematical_program_scan_CAS_author_source_old_replay": False})
    write_new(META, {"status": "OTHER initially blind ENTIRE WHOLE2 review; candidate unverified",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "constructor": "/root/review_2017_coarsening_r1",
        "reviewer_NEW_D8_constructive_contribution": False,
        "older_roles": "A D6 author and CF,Qv3,D7 whole reviewer; separately accepted inputs not independently self-recertified",
        "ALL_obligations_reconstructed": 48, "PASS_rows": 48,
        "substantive_defects": 0, "required_author_repairs": 0, "closed_scope_notes": 8,
        "recommendation": "Scoped D8A-D pass; TWO OTHER whole audits and root full reconciliation still required",
        "corresponding_NEW_root_D8_peer_content_accessed": False,
        "coordinator_administrative_times_counts_only_received": True,
        "findings_embargo_until_explicit_BOTH_ENTIRE": True,
        "fresh_full_accepted_bodies": ["D7", "CF", "Qv3"],
        "D6_current_authority_only_not_fresh_full_body": True,
        "CF6_or_D6_sparsity_used": False,
        "requested_inherited": {"model": "gpt-6.1-sol", "reasoning": "max"},
        "verified_effective_settings": None,
        "mathcode_CAS_scan_routine_test_author_source_old_replay": False,
        "ALL_final_payload_readback_then_manifest_readback_and_SEPARATE_verify_REQUIRED": True,
        "payload_files": 10, "ENTIRE_files": 11,
        "baseline": fp(BASE), "input_validation": fp(VALID),
        "weekly": {"at_utc": "2026-10-18 16:19:05 UTC", "TOTAL_used_percent": 51,
            "window_minutes": 10080, "reset": 1792874445, "ordinary_allowed": True,
            "legacy_by_limit_agree": True, "TOTAL_ceiling": 90, "reserve": True,
            "automatic_later_window": False}})
    print(json.dumps({"prepare": "PASS", "ALL48": True, **snap["all_current_protected_summary"]}))


def freeze():
    snap = validate()
    payloads = [fp(rel) for rel in PAYLOADS]
    write_new(MAN, {"frozen_at_utc": utc(), "status": "OTHER initially blind ENTIRE WHOLE2 review",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "ALL_obligations": 48,
        "payload_files": 10, "ENTIRE_files": 11,
        "FULL_final_ALL10_payload_model_readback_completed": True,
        "FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED": True,
        "findings_embargo_until_explicit_BOTH_ENTIRE": True,
        "corresponding_NEW_root_peer_content_access": False,
        "compact_baseline": fp(BASE),
        "compact_current_protection": snap["all_current_protected_summary"],
        "payloads": payloads})
    print(json.dumps({"freeze": fp(MAN), "ENTIRE_files": 11, "ALL48": True}))


def verify():
    snap = validate()
    manifest = jread(MAN)
    if (manifest["ENTIRE_files"], manifest["ALL_obligations"], len(manifest["payloads"])) != (11, 48, 10):
        raise AssertionError("ENTIRE11/48 count mismatch")
    check_all(manifest["payloads"])
    if manifest["compact_current_protection"] != snap["all_current_protected_summary"]:
        raise AssertionError("protected summary mismatch")
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "verified_at_utc": utc(),
        "manifest": fp(MAN), "initial": fp(P + "initial-v1.md"),
        "ENTIRE_files": 11, "ALL_obligations": 48,
        **snap["all_current_protected_summary"], "no_file_written": True}))


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) == 2 else ""
    if action not in ("prepare", "freeze", "verify"):
        raise SystemExit("usage: NEW D8 review admin prepare|freeze|verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[action]()
