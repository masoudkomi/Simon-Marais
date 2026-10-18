#!/usr/bin/env python3
"""NEW review documentary integrity only; no mathematical evaluation/code replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2017-B4/reviews/reasoning-path-mass-return-r10-review-2-"
A = "problems/2017-B4/notes/reasoning-path-mass-return-r10-"
PARENT = "problems/2020-B4/reviews/reasoning-class-return-sq15-review-2-manifest-v1.json"
BASE, VALID, META, MAN = [P + name + "-v1.json" for name in
                         ("baseline", "input-validation", "metadata", "manifest")]
STATIC = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "sources-v1.md",
          "sources-v1.json", "worklog-v1.md", "admin-v1.py"]
PAYLOADS = [P + name for name in STATIC] + [BASE, VALID, META]
DIRECT = ["AGENTS.md", "problems/2017-B4/statement.md"]
INPUTS = [
    ("coordinator-path-moment-r3", "coordinator-path-moment-r3"),
    ("direction-coarsening", "coarsening"),
    ("allD-global", "allD-global"),
]
for proof, authority in INPUTS:
    DIRECT.append("problems/2017-B4/proofs/reviewed-" + proof + "-v1.1.md")
    DIRECT.extend("problems/2017-B4/reviews/" + authority + "-acceptance." + ext
                  for ext in ("md", "json"))
DIRECT.extend("problems/2017-B4/notes/coordinator-path-moment-r3-" + name
              for name in ("source-audit-v1.md", "failures-worklog-v1.md"))
EXPECTED_MAIN = {"path": A + "candidate-v1.md", "bytes": 19791,
                 "sha256": "a66251ca92893c795fe2f7b83bc63d9b435df38675b0dafd9ff7556e133b4a2b"}
EXPECTED_PARENT = {"path": PARENT, "bytes": 3018,
                   "sha256": "fa428e31f37892ef8ef61fb95a7b96156c4a3c07d26b123c9a6523096b0d8c22"}
UNRELATED = "problems/2021-B4/reviews/reasoning-center-return-r20-review-"


def utc():
    return datetime.now(timezone.utc).isoformat()


def path(rel):
    if "reasoning-path-mass-return-r10-review-" in rel and not rel.startswith(P):
        raise AssertionError("corresponding NEW root R10 peer access embargo")
    if rel.startswith(UNRELATED):
        raise AssertionError("unrelated R20 peer files not needed or accessed")
    pp = Path(rel)
    if pp.is_absolute() or ".." in pp.parts:
        raise AssertionError("exact workspace-relative documentary path required")
    return ROOT / pp


def fp(rel):
    data = path(rel).read_bytes()
    return {"path": rel, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def jread(rel):
    return json.loads(path(rel).read_text())


def check(row):
    expected = {key: row[key] for key in ("path", "bytes", "sha256")}
    if fp(row["path"]) != expected:
        raise AssertionError("frozen fingerprint mismatch: " + row["path"])


def summary(rows):
    unique = {}
    for row in rows:
        rr = {key: row[key] for key in ("path", "bytes", "sha256")}
        previous = unique.setdefault(rr["path"], rr)
        if previous != rr:
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
    expected = ["O" + str(i).zfill(2) for i in range(1, 61)]
    ledger = re.findall(r"^\| (O\d{2}) \| PASS \|", path(P + "ledger-v1.md").read_text(), re.M)
    author = re.findall(r"^(O\d{2})\.", path(A + "obligations-v1.md").read_text(), re.M)
    separate = re.findall(r"^(O\d{2}) — CHECKED\.", path(A + "constructor-checks-v1.md").read_text(), re.M)
    if ledger != expected or author != expected or separate != expected:
        raise AssertionError("exact ordered ALL60 labels required")


def snapshot():
    check(EXPECTED_MAIN)
    check(EXPECTED_PARENT)
    author = jread(A + "freeze-v1.json")
    if (author["ENTIRE_files_including_freeze"], author["whole_obligations"],
            len(author["payloads"])) != (11, 60, 10):
        raise AssertionError("author ENTIRE11/60 mismatch")
    author_rows = author["payloads"] + [fp(A + "freeze-v1.json")]
    check_all(author_rows)
    author_base = jread(A + "baseline-v1.json")
    declared = author_base["records"]
    necessary = [row for row in declared if not row["path"].startswith(UNRELATED)]
    historical = [row for row in declared if row["path"].startswith(UNRELATED)]
    if len(necessary) + len(historical) != len(declared):
        raise AssertionError("declaration split mismatch")
    check_all(necessary)
    parent = jread(PARENT)
    if parent["ENTIRE_files"] != 11 or len(parent["payloads"]) != 10:
        raise AssertionError("own immediate parent ENTIRE11 mismatch")
    parent_rows = parent["payloads"] + [fp(PARENT)]
    check_all(parent_rows)
    direct = [fp(rel) for rel in DIRECT]
    suffixes = []
    for proof, authority_name in INPUTS:
        authority_path = "problems/2017-B4/reviews/" + authority_name + "-acceptance.json"
        authority = jread(authority_path)
        if authority_name == "coarsening":
            if authority["unresolved_substantive_objections_to_accepted_claims"] != 0:
                raise AssertionError("accepted DC status mismatch")
            check(authority["accepted_proof"])
            suffixes.append({"authority": fp(authority_path),
                             "accepted_proof": authority["accepted_proof"],
                             "historical_conditional_transfer_not_current_G_status": True})
        else:
            if authority["unresolved_substantive_issues"] != 0:
                raise AssertionError("accepted input status mismatch")
            check(authority["candidate"])
            check(authority["accepted_copy"])
            if not path(authority["accepted_copy"]["path"]).read_bytes().endswith(
                    path(authority["candidate"]["path"]).read_bytes()):
                raise AssertionError("accepted exact candidate suffix mismatch")
            suffixes.append({"authority": fp(authority_path),
                             "accepted_copy": authority["accepted_copy"],
                             "exact_candidate_suffix": authority["candidate"]})
    protection = check_all(author_rows + necessary + parent_rows + direct)
    labels()
    return {
        "author_manifest": fp(A + "freeze-v1.json"),
        "author_ENTIRE_summary": summary(author_rows),
        "author_baseline_binding": fp(A + "baseline-v1.json"),
        "author_current_necessary_input_summary": summary(necessary),
        "quoted_unrelated_R20_parent_declaration_summary_NOT_directly_opened_or_hashed": summary(historical),
        "quoted_history_is_bound_by_author_baseline_not_revalidated": True,
        "direct_current_operative_inputs": direct,
        "accepted_exact_bindings": suffixes,
        "immediate_own_parent": {"manifest": fp(PARENT),
            "ENTIRE_summary": summary(parent_rows),
            "historical_current_summary_bound_not_reexpanded": parent["compact_current_protection"]},
        "all_current_protected_summary": protection,
        "compact_policy": "Necessary declared current payloads verified; unrelated ancestry bound through immutable author metadata, no giant recopy or peer file access",
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
        "status": "OTHER initially blind ENTIRE WHOLE2; candidate unverified",
        "immutable_bindings": snap,
        "NEW_corresponding_root_R10_finding_inventory_file_hash_metadata_commentary_access": False,
        "quoted_author_R20_ancestry_seen_but_peer_files_not_opened": True,
        "coordinator_R10_times_counts_only_received_not_inputs": True})
    write_new(VALID, {"validated_at_utc": utc(), "result": "PASS",
        "author_ENTIRE_files": 11, "ALL_obligations": 60,
        "author_payloads_necessary_inputs_and_accepted_exact_bindings_match": True,
        "compact_current_protection": snap["all_current_protected_summary"],
        "unrelated_R20_peer_parent_not_directly_revalidated": True,
        "mathematical_code_scan_CAS_or_author_source_old_replay": False})
    write_new(META, {"status": "OTHER initially blind ENTIRE WHOLE2; candidate unverified",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "constructor": "/root/review_2022_complexity_r2",
        "reviewer_NEW_R10_constructive_contribution": False,
        "older_roles": "A strict LOCAL/value author and allD global whole reviewer; separately accepted inputs not freshly self-recertified",
        "ALL_obligations_reconstructed": 60, "PASS_rows": 60,
        "substantive_defects": 0, "required_author_repairs": 0, "closed_scope_notes": 8,
        "recommendation": "Scoped R10A-E pass; TWO OTHER whole audits and root full reconciliation still required",
        "NEW_corresponding_root_R10_peer_content_accessed": False,
        "coordinator_times_counts_only_received": True,
        "findings_embargo_until_explicit_BOTH_ENTIRE": True,
        "quoted_author_R20_parent_records_seen": True,
        "direct_R20_peer_file_hash_inventory_access": False,
        "requested_inherited": {"model": "gpt-6.1-sol", "reasoning": "max"},
        "verified_effective_settings": None,
        "mathcode_CAS_scan_test_old_source_author_replay": False,
        "ALL_final_payload_readback_then_manifest_readback_and_SEPARATE_verify_REQUIRED": True,
        "payload_files": 10, "ENTIRE_files": 11,
        "baseline": fp(BASE), "input_validation": fp(VALID),
        "weekly": {"at_utc": "2026-10-18 16:09:40 UTC", "TOTAL_used_percent": 50,
            "window_minutes": 10080, "reset": 1792874445, "ordinary_allowed": True,
            "legacy_by_limit_agree": True, "TOTAL_ceiling": 90, "reserve": True,
            "automatic_later_window": False}})
    print(json.dumps({"prepare": "PASS", "ALL60": True, **snap["all_current_protected_summary"]}))


def freeze():
    snap = validate()
    payloads = [fp(rel) for rel in PAYLOADS]
    write_new(MAN, {"frozen_at_utc": utc(), "status": "OTHER initially blind ENTIRE WHOLE2 review",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "ALL_obligations": 60,
        "payload_files": 10, "ENTIRE_files": 11,
        "FULL_final_ALL10_payload_model_readback_completed": True,
        "FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED": True,
        "findings_embargo_until_explicit_BOTH_ENTIRE": True,
        "NEW_corresponding_root_peer_content_access": False,
        "compact_baseline": fp(BASE),
        "compact_current_protection": snap["all_current_protected_summary"],
        "payloads": payloads})
    print(json.dumps({"freeze": fp(MAN), "ENTIRE_files": 11, "ALL60": True}))


def verify():
    snap = validate()
    manifest = jread(MAN)
    if (manifest["ENTIRE_files"], manifest["ALL_obligations"], len(manifest["payloads"])) != (11, 60, 10):
        raise AssertionError("review ENTIRE11/60 count mismatch")
    check_all(manifest["payloads"])
    if manifest["compact_current_protection"] != snap["all_current_protected_summary"]:
        raise AssertionError("protected summary mismatch")
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "verified_at_utc": utc(),
        "manifest": fp(MAN), "initial": fp(P + "initial-v1.md"),
        "ENTIRE_files": 11, "ALL_obligations": 60,
        **snap["all_current_protected_summary"], "no_file_written": True}))


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) == 2 else ""
    if action not in ("prepare", "freeze", "verify"):
        raise SystemExit("usage: NEW review admin prepare|freeze|verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[action]()
