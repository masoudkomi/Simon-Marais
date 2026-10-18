#!/usr/bin/env python3
"""NEW review byte/JSON/label/diff administration only; no mathematics or replay."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2020-B4/reviews/reasoning-class-return-sq15-review-2-reaudit-"
A = "problems/2020-B4/notes/reasoning-class-return-sq15-"
AUTHOR = A + "freeze-v1.1.json"
PARENT = "problems/2022-B4/reviews/reasoning-dynamics-return-r8-review-2-manifest-v1.json"
EXPECTED = {
    AUTHOR: (4621, "b84c394b1d1e7feb1b351e59bd2f91e4f08aaea232f0537083cf73be8f3a3e9e"),
    A + "candidate-v1.1.md": (25788, "4d2696117fa8f8af5760e5034b83602c780f44f81b839fc4bcb6a3086c4825bd"),
    PARENT: (3035, "f8f7c11aaeecc66a8c4522bee70bfab3baed0b4d674dc6775e586a6b6ed9b8b4"),
    "AGENTS.md": (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
}
KINDS = [("initial", "md"), ("ledger", "md"), ("issues", "md"),
         ("sources", "md"), ("sources", "json"), ("worklog", "md"),
         ("admin", "py"), ("baseline", "json"),
         ("input-validation", "json"), ("metadata", "json")]
ACCEPTED = ["reasoning-arithmetic-return-r14", "reasoning-return-r8",
            "reasoning-Todd-return-r12"]
SIX = [("candidate", "md"), ("obligations", "md"),
       ("constructor-checks", "md"), ("failures", "md"),
       ("sources", "md"), ("sources", "json")]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(rel):
    p = Path(rel)
    if p.is_absolute() or ".." in p.parts:
        raise ValueError("not a repository-relative declared path")
    # The released ORIGINAL v1 root packet is allowed. No NEW repair peer is.
    peer = "problems/2020-B4/reviews/reasoning-class-return-sq15-review-1-"
    if rel.startswith(peer) and not re.search(r"-v1\.(md|json|py)$", rel):
        raise ValueError("NEW root repair peer embargo")
    return (ROOT / rel).read_bytes()


def rec(rel):
    b = raw(rel)
    return {"path": rel, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def checked(r):
    actual = rec(r["path"])
    if actual != {k: r[k] for k in ("path", "bytes", "sha256")}:
        raise ValueError("frozen byte mismatch: " + r["path"])
    return actual


def obj(rel):
    return json.loads(raw(rel))


def walk_records(x):
    if isinstance(x, dict):
        if all(k in x for k in ("path", "bytes", "sha256")):
            yield {k: x[k] for k in ("path", "bytes", "sha256")}
        for v in x.values():
            yield from walk_records(v)
    elif isinstance(x, list):
        for v in x:
            yield from walk_records(v)


def summary(records):
    unique = {}
    for r in records:
        if r["path"] in unique and unique[r["path"]] != r:
            raise ValueError("conflicting literal declarations")
        unique[r["path"]] = r
    ordered = [unique[k] for k in sorted(unique)]
    return {"occurrences": len(records), "unique_paths": len(ordered),
            "canonical_sha256": hashlib.sha256(json.dumps(
                ordered, sort_keys=True, separators=(",", ":")).encode()).hexdigest()}


def output(kind, ext="json"):
    return P + kind + "-v1.1." + ext


def write(kind, value):
    path = ROOT / output(kind)
    with path.open("x", encoding="utf-8") as f:
        f.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def accepted():
    result, records = [], []
    for stem in ACCEPTED:
        authority = "problems/2020-B4/reviews/" + stem + "-acceptance.json"
        j = obj(authority)
        body, candidate = checked(j["accepted_copy"]), checked(j["candidate"])
        if not raw(body["path"]).endswith(raw(candidate["path"])):
            raise ValueError("accepted suffix mismatch")
        md = authority[:-4] + "md"
        item = {"authority_MD": rec(md), "authority_JSON": rec(authority),
                "accepted_copy": body, "exact_candidate_suffix": candidate}
        records.extend(item.values())
        result.append(item)
    return result, records


def inputs():
    for rel, (size, sha) in EXPECTED.items():
        checked({"path": rel, "bytes": size, "sha256": sha})
    author = obj(AUTHOR)
    author_records = [rec(AUTHOR)] + [checked(r) for r in author["payloads"]]
    if len(author_records) != 16:
        raise ValueError("author ENTIRE16 mismatch")
    author_baseline = obj(A + "baseline-v1.1.json")
    guard_records = [checked(r) for r in author_baseline["guards"]]
    if len(guard_records) != 51:
        raise ValueError("author necessary guard count mismatch")
    parent = obj(PARENT)
    parent_records = [rec(PARENT)] + [checked(r) for r in parent["payloads"]]
    if len(parent_records) != 11:
        raise ValueError("immediate own parent ENTIRE11 mismatch")
    # Validate all literal parent-baseline declarations, binding their inventory
    # compactly rather than recopying it or recursively executing anything.
    parent_baseline = parent["compact_baseline"]["path"]
    parent_literals = [checked(r) for r in walk_records(obj(parent_baseline))]
    accepted_items, accepted_records = accepted()
    direct = accepted_records + [rec("AGENTS.md"), rec("problems/2020-B4/statement.md")]
    all_records = author_records + guard_records + parent_records + direct
    current = summary(all_records)
    documentary = []
    for stem, ext in SIX:
        old, new = A + stem + "-v1." + ext, A + stem + "-v1.1." + ext
        documentary.extend(difflib.unified_diff(
            raw(old).decode().splitlines(True), raw(new).decode().splitlines(True),
            fromfile=old, tofile=new))
    if "".join(documentary) != raw(A + "diff-v1-to-v1.1.patch").decode():
        raise ValueError("six-file documentary diff mismatch")
    s = raw(A + "obligations-v1.1.md").decode()
    if re.findall(r"^\|SQ15-(\d{2})\|", s, re.M) != [f"{i:02d}" for i in range(1,49)]:
        raise ValueError("author original48 documentary labels")
    if re.findall(r"^\|SQ15-R(\d{2})\|", s, re.M) != [f"{i:02d}" for i in range(1,13)]:
        raise ValueError("author repair12 documentary labels")
    details = {
        "author_manifest": rec(AUTHOR), "author_ENTIRE_summary": summary(author_records),
        "author_guard_baseline_binding": rec(A + "baseline-v1.1.json"),
        "author_necessary_guards_verified": summary(guard_records),
        "accepted_exact_suffix_bindings": accepted_items,
        "own_immediate_parent_manifest": rec(PARENT),
        "own_parent_ENTIRE_summary": summary(parent_records),
        "own_parent_baseline_binding": rec(parent_baseline),
        "own_parent_literal_declarations_verified": summary(parent_literals),
        "own_parent_historical_current_protection": parent["compact_current_protection"],
        "direct_AGENTS_statement": direct[-2:], "current_protection": current,
        "giant_historical_inventory_recopied": False,
        "NEW_root_repair_peer_access": False,
        "accepted_SQ14D_E_unqualified_universal_clauses_operative": False,
    }
    return details


def prepare():
    details = inputs()
    baseline = {"prepared_at_utc": now(), "reviewer": "/root/review_2021_reasoning_j15_r2",
                "status": "OTHER affected ENTIRE WHOLE2; candidate unverified",
                "compact_immutable_bindings": details}
    write("baseline", baseline)
    write("input-validation", {
        "validated_at_utc": now(), "author_ENTIRE16": "PASS",
        "author_necessary51_guards": "PASS", "own_parent_ENTIRE11": "PASS",
        "parent_literal_declarations": details["own_parent_literal_declarations_verified"],
        "current_protection": details["current_protection"],
        "accepted_body_candidate_suffixes": "ALL3 PASS",
        "exact_six_file_documentary_diff": "PASS", "author_labels48_plus12": "PASS",
        "mathematical_instance_evaluated": False, "NEW_root_repair_peer_access": False})
    write("metadata", {
        "status": "OTHER affected ENTIRE WHOLE2; scoped pass recommendation only",
        "reviewer": "/root/review_2021_reasoning_j15_r2",
        "sole_constructor": "/root/review_2017_coarsening_r1",
        "reviewer_NEW_SQ15_or_author_repair_contribution": False,
        "reviewer_original_SQ15R2_01_counterexample_role_disclosed": True,
        "older_R8_TD_review_roles_not_fresh_self_recertification": True,
        "ALL_obligations": 60, "PASS_original_rows": 48, "PASS_repair_rows": 12,
        "SQ15R2_01_status": "CLOSED by explicit INTEGRAL-only full v1.1 repair",
        "additional_substantive_issues": 0, "additional_required_author_repairs": 0,
        "closed_scope_notes": 8, "root_only_promotion_after_BOTH_and_reconciliation": True,
        "NEW_root_v1_1_repair_finding_inventory_file_hash_meta_commentary_access": False,
        "original_v1_packets_released_and_preserved": True,
        "findings_embargo_until_explicit_BOTH_ENTIRE": True,
        "mathematics": "hand reconstruction only",
        "mathcode_CAS_scan_routine_test_author_source_old_replay": False,
        "fresh_operative_input_reads": {"R8": "1-175 and458-488",
            "TD": "253-410; earlier clipped opening not counted",
            "SQ14": "opening through160 and140-325; universal D/E held/unused"},
        "current_EACH_acceptance_MD_JSON_read": ["SQ14", "R8", "TD"],
        "historical_original_initial_COMPLETE_accepted_body_reads_retained": True,
        "requested_inherited": {"model": "gpt-6.1-sol", "reasoning": "max"},
        "verified_effective_settings": None,
        "weekly": {"at_utc": "2026-10-18 16:30:30 UTC", "TOTAL_used_percent": 52,
            "window_minutes": 10080, "reset": 1792874445, "ordinary_allowed": True,
            "legacy_by_limit_agree": True, "TOTAL_ceiling": 90, "reserve": True,
            "automatic_later_window": False},
        "payload_files": 10, "ENTIRE_files": 11,
        "FULL_final_ALL_payload_model_readback_REQUIRED_before_freeze": True,
        "FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED": True,
        "baseline": rec(output("baseline")),
        "input_validation": rec(output("input-validation"))})
    print(json.dumps({"prepared_at_utc": now(), "current_protection": details["current_protection"],
                      "parent_literals": details["own_parent_literal_declarations_verified"]}))


def own_labels():
    ledger = raw(output("ledger", "md")).decode()
    if re.findall(r"^\|SQ15-(\d{2})\|PASS\|", ledger, re.M) != [f"{i:02d}" for i in range(1,49)]:
        raise ValueError("own ALL48 PASS documentary labels")
    if re.findall(r"^\|SQ15-R(\d{2})\|PASS\|", ledger, re.M) != [f"{i:02d}" for i in range(1,13)]:
        raise ValueError("own ALL12 PASS documentary labels")


def validate_baseline():
    current = inputs()
    expected = obj(output("baseline"))["compact_immutable_bindings"]
    if current != expected:
        raise ValueError("current immutable binding changed")
    own_labels()
    return current


def freeze():
    if sys.argv[2:] != ["--FULL-final-payload-model-readback-complete"]:
        raise ValueError("explicit reviewer FULL final payload readback assertion required")
    details = validate_baseline()
    payloads = [rec(output(k, ext)) for k, ext in KINDS]
    write("manifest", {"frozen_at_utc": now(), "reviewer": "/root/review_2021_reasoning_j15_r2",
        "status": "OTHER affected ENTIRE WHOLE2 review; candidate unverified",
        "ALL_obligations": 60, "original_rows": 48, "repair_rows": 12,
        "payload_files": 10, "ENTIRE_files": 11,
        "FULL_final_ALL10_payload_model_readback_completed": True,
        "FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED": True,
        "corresponding_NEW_root_v1_1_repair_peer_content_access": False,
        "findings_embargo_until_explicit_BOTH_ENTIRE": True,
        "compact_baseline": rec(output("baseline")),
        "compact_current_protection": details["current_protection"],
        "payloads": payloads})
    print(json.dumps({"manifest": rec(output("manifest")), "at_utc": now(),
                      "status": "FULL manifest model readback and SEPARATE verify still required"}))


def verify():
    details = validate_baseline()
    manifest = obj(output("manifest"))
    for r in manifest["payloads"]:
        checked(r)
    if len(manifest["payloads"]) != 10 or manifest["ALL_obligations"] != 60:
        raise ValueError("own ENTIRE11/ALL60 mismatch")
    print(json.dumps({"SEPARATE_readonly_verify_at_utc": now(), "status": "PASS",
        "ENTIRE_files": 11, "ALL_obligations": 60,
        "current_protection": details["current_protection"],
        "manifest": rec(output("manifest")), "report": rec(output("initial", "md")),
        "no_file_written_in_verify": True, "NEW_root_repair_peer_access": False}))


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in {"prepare", "freeze", "verify"}:
        raise SystemExit("prepare | freeze --FULL-final-payload-model-readback-complete | verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[sys.argv[1]]()
