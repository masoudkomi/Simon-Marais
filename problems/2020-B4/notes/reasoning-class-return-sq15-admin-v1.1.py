#!/usr/bin/env python3
"""NEW SQ15 v1.1 documentary administration only; no mathematical execution."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2020-B4/notes/reasoning-class-return-sq15-"
ORIGINAL = P + "freeze-v1.json"
PARENT = "problems/2022-B4/notes/reasoning-dynamics-return-r9-interim-freeze-v1.json"
REVIEW_PREFIXES = [
    "problems/2020-B4/reviews/reasoning-class-return-sq15-review-1-",
    "problems/2020-B4/reviews/reasoning-class-return-sq15-review-2-",
]
ACCEPTED = [
    ("reasoning-arithmetic-return-r14", "befc8237c23eaac3e210d0aa3f28eaef44a01d4e771e3a4d156b18fd6b6bedb5"),
    ("reasoning-return-r8", "9003af18926d1fe49d3f997b40ed070ceefa37e42f73c5a98c32bbe7a2f3bfcb"),
    ("reasoning-Todd-return-r12", "f1663778cf78c18b3cb30a4702d7fbff95be29ab73c5f8e4f74d344362c8fba6"),
]
SIX = [("candidate", "md"), ("obligations", "md"),
       ("constructor-checks", "md"), ("failures", "md"),
       ("sources", "md"), ("sources", "json")]
PAYLOADS = [
    "candidate-v1.1.md", "obligations-v1.1.md", "constructor-checks-v1.1.md",
    "failures-v1.1.md", "sources-v1.1.md", "sources-v1.1.json",
    "repair-ledger-v1.1.md", "issues-v1.1.md", "worklog-v1.1.md",
    "code-log-v1.1.md", "admin-v1.1.py", "diff-v1-to-v1.1.patch",
    "baseline-v1.1.json", "input-validation-v1.1.json", "metadata-v1.1.json",
]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(rel):
    pp = Path(rel)
    if pp.is_absolute() or ".." in pp.parts:
        raise ValueError("exact relative documentary path required")
    return (ROOT / pp).read_bytes()


def record(rel):
    b = raw(rel)
    return {"path": rel, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def checked(item):
    if record(item["path"]) != item:
        raise ValueError("fingerprint mismatch: " + item["path"])
    return item


def readjson(rel):
    return json.loads(raw(rel))


def write(suffix, value, text=False):
    if "v1.1" not in suffix:
        raise ValueError("NEW v1.1 write only")
    data = value if text else json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as out:
        out.write(data)
    return record(P + suffix)


def canonical(rows):
    b = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(b).hexdigest()


def labels():
    s = raw(P + "obligations-v1.1.md").decode()
    orig = re.findall(r"^\|SQ15-(\d{2})\|", s, re.M)
    repair = re.findall(r"^\|SQ15-R(\d{2})\|", s, re.M)
    if orig != [f"{i:02d}" for i in range(1, 49)]:
        raise ValueError("ALL48 original label/order mismatch")
    if repair != [f"{i:02d}" for i in range(1, 13)]:
        raise ValueError("ALL12 affected-repair label/order mismatch")
    return {"original": len(orig), "repair": len(repair), "whole": len(orig) + len(repair)}


def documentary_diff():
    chunks = []
    for stem, ext in SIX:
        old = P + stem + "-v1." + ext
        new = P + stem + "-v1.1." + ext
        chunks.extend(difflib.unified_diff(raw(old).decode().splitlines(True),
                                         raw(new).decode().splitlines(True),
                                         fromfile=old, tofile=new))
    return "".join(chunks)


def prepare():
    checked({"path": ORIGINAL, "bytes": 3677,
             "sha256": "bc7bb2ef06d6e90dc083841fac5853209b7a45e36bc0ae5b16e512efa7c94975"})
    checked({"path": P + "candidate-v1.md", "bytes": 20209,
             "sha256": "11182beb9e08841d8ecce07008caafe93ca65222fdd34937493bf9a4c9715e78"})
    checked({"path": PARENT, "bytes": 734,
             "sha256": "ebca4c438b6cbae4645c92f306a3fe479ecc73478ac0671f5ee608f507607591"})
    rows = []
    original = readjson(ORIGINAL)
    if (original["ENTIRE_files"], len(original["payloads"])) != (13, 12):
        raise ValueError("original SQ15 ENTIRE count mismatch")
    rows.append(record(ORIGINAL))
    rows.extend(checked(item) for item in original["payloads"])
    reviews = []
    for prefix in REVIEW_PREFIXES:
        path = prefix + "manifest-v1.json"
        m = readjson(path)
        if (m["ENTIRE_files"], len(m["payloads"])) != (11, 10):
            raise ValueError("original OTHER whole count mismatch")
        if m.get("whole_obligations", m.get("ALL_obligations")) != 48:
            raise ValueError("original OTHER whole48 mismatch")
        rows.append(record(path))
        rows.extend(checked(item) for item in m["payloads"])
        reviews.append({"manifest": record(path), "ENTIRE_files": 11,
                        "payloads_verified": 10, "historical_inventory_reexpanded": False})
    suffixes = []
    for stem, expected in ACCEPTED:
        authority = "problems/2020-B4/reviews/" + stem + "-acceptance"
        a = readjson(authority + ".json")
        body, candidate = checked(a["accepted_copy"]), checked(a["candidate"])
        if body["sha256"] != expected or not raw(body["path"]).endswith(raw(candidate["path"])):
            raise ValueError("accepted body/candidate suffix mismatch")
        rows.extend([record(authority + ".md"), record(authority + ".json"), body, candidate])
        suffixes.append({"authority": authority, "body_verified": True, "exact_suffix": True})
    rows.extend([record("AGENTS.md"), record("problems/2020-B4/statement.md")])
    parent = readjson(PARENT)
    if parent["ENTIRE_files"] != 2:
        raise ValueError("immediate own interim count mismatch")
    rows.extend([record(PARENT), checked(parent["payload"])])
    unique = {}
    for item in rows:
        if item["path"] in unique and unique[item["path"]] != item:
            raise ValueError("conflicting documentary guard")
        unique[item["path"]] = item
    guards = [unique[path] for path in sorted(unique)]
    counts = labels()
    write("diff-v1-to-v1.1.patch", documentary_diff(), text=True)
    b = {
        "prepared_at_utc": now(), "status": "candidate proof - unverified; full author repair",
        "original_SQ15": record(ORIGINAL), "original_ENTIRE13_payloads_verified": True,
        "both_original_OTHER_whole_packets": reviews,
        "immediate_own_parent": record(PARENT),
        "historical_original_guard_summary_bound_by_original_identity": {
            "occurrences": original["necessary_guard_occurrences"],
            "unique_paths": original["necessary_guard_unique_paths"],
            "canonical_sha256": original["canonical_guard_sha256"],
        },
        "historical_inventories_reexpanded_or_programs_replayed": False,
        "necessary_guard_occurrences": len(rows), "necessary_guard_unique_paths": len(guards),
        "canonical_guard_sha256": canonical(guards), "guards": guards,
    }
    write("baseline-v1.1.json", b)
    write("input-validation-v1.1.json", {
        "validated_at_utc": now(), "immutable_original_constructor": "ENTIRE13 PASS",
        "immutable_BOTH_original_reviews": "ENTIRE11+11 PASS",
        "current_accepted_body_candidate_checks": suffixes,
        "immediate_own_parent": "ENTIRE2 PASS", "labels": counts,
        "exact_six_file_text_diff": True, "mathematical_instance_evaluated": False,
    })
    write("metadata-v1.1.json", {
        "created_at_utc": now(), "status": "candidate proof - unverified; full versioned author repair",
        "constructor": "/root/review_2017_coarsening_r1", "constructor_excluded": True,
        "root_supplied_new_proof_inference": False,
        "reviewer_A_counterexample_attribution": "SQ15R2-01 q8/p73/s9 fractional principal norm2 diagnostic",
        "repair_issue": "SQ15R2-01", "original_v1_false_fractional_reading_acknowledged": True,
        "all_J_R_y_universal_order_clauses_INTEGRAL_only": True,
        "fractional_FIELD_norm_TD_rho_and_ordinary_groups_retained": True,
        "SQ15A_C_D_full_integral_proofs_retained": True,
        "original_obligations": 48, "additional_repair_obligations": 12, "whole_obligations": 60,
        "payload_files": 15, "ENTIRE_files": 16,
        "BOTH_affected_OTHER_ENTIRE_WHOLE_reaudits_required": True,
        "corresponding_future_affected_peer_material_accessed": False,
        "requested_model": "gpt-6.1-sol", "requested_reasoning": "max",
        "verified_effective_settings": None,
        "authorized_weekly_reset": 1792874445, "last_transition_TOTAL_percent": 50,
        "TOTAL_ceiling_percent": 90, "integration_reserve": True, "automatic_next_window": False,
        "mathematical_program_CAS_scan_test_old_source_author_replay": False,
        "Git_shared_cache_old_payload_write": False,
        "FULL_final_ALL15_payload_model_readback_REQUIRED_before_freeze": True,
        "FULL_freeze_model_readback_then_SEPARATE_readonly_verify_REQUIRED": True,
    })
    print(json.dumps({"prepare": "PASS", "ALL_obligations": counts,
                      "necessary_guard_occurrences": len(rows), "unique_paths": len(guards),
                      "canonical_guard_sha256": canonical(guards)}))


def baseline_check():
    b = readjson(P + "baseline-v1.1.json")
    for item in b["guards"]:
        checked(item)
    if canonical(b["guards"]) != b["canonical_guard_sha256"]:
        raise ValueError("baseline canonical mismatch")
    if raw(P + "diff-v1-to-v1.1.patch").decode() != documentary_diff():
        raise ValueError("exact documentary diff changed")
    labels()
    return b


def freeze():
    b = baseline_check()
    payloads = [record(P + suffix) for suffix in PAYLOADS]
    for item in payloads:
        if item["path"].endswith(".json"):
            readjson(item["path"])
    obj = {
        "frozen_at_utc": now(), "status": "candidate proof - unverified; full v1.1 author repair",
        "constructor": "/root/review_2017_coarsening_r1", "constructor_excluded": True,
        "repair_issue": "SQ15R2-01", "claims": ["SQ15A", "SQ15B INTEGRAL-only", "SQ15C", "SQ15D"],
        "original_obligations": 48, "additional_repair_obligations": 12, "whole_obligations": 60,
        "BOTH_affected_OTHER_ENTIRE_WHOLE_reaudits_required": True,
        "original_constructor": record(ORIGINAL), "immediate_own_parent": record(PARENT),
        "compact_baseline": record(P + "baseline-v1.1.json"),
        "payload_files": len(payloads), "ENTIRE_files": len(payloads) + 1,
        "FULL_final_ALL15_payload_model_readback_completed": True,
        "FULL_freeze_model_readback_then_SEPARATE_verify_REQUIRED": True,
        "necessary_guard_occurrences": b["necessary_guard_occurrences"],
        "necessary_guard_unique_paths": b["necessary_guard_unique_paths"],
        "canonical_guard_sha256": b["canonical_guard_sha256"],
        "mathematical_program_CAS_scan_or_old_replay": False,
        "payloads": payloads,
    }
    print(json.dumps({"freeze": write("freeze-v1.1.json", obj)}))


def verify():
    path = P + "freeze-v1.1.json"
    m = readjson(path)
    if [x["path"] for x in m["payloads"]] != [P + suffix for suffix in PAYLOADS]:
        raise ValueError("ENTIRE payload coverage mismatch")
    for item in m["payloads"]:
        checked(item)
    b = baseline_check()
    if m["whole_obligations"] != 60 or m["ENTIRE_files"] != 16:
        raise ValueError("whole count mismatch")
    if m["canonical_guard_sha256"] != b["canonical_guard_sha256"]:
        raise ValueError("freeze/baseline mismatch")
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "verified_at_utc": now(),
                      "ENTIRE_files": 16, "ALL_obligations": 60,
                      "necessary_guard_occurrences": b["necessary_guard_occurrences"],
                      "necessary_guard_unique_paths": b["necessary_guard_unique_paths"],
                      "main": record(P + "candidate-v1.1.md"), "freeze": record(path)}, indent=2))


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) == 2 else ""
    if action not in {"prepare", "freeze", "verify"}:
        raise SystemExit("choose prepare|freeze|verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[action]()
