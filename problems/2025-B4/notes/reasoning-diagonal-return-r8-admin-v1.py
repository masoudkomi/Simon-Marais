#!/usr/bin/env python3
"""DR8 documentary administration only: bytes, JSON and obligation labels."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2025-B4/notes/reasoning-diagonal-return-r8-"
OLD = "problems/2025-B4/notes/reasoning-diagonal-return-r7-freeze-v1.json"
PARENT = "problems/2020-B4/reviews/reasoning-class-return-sq15-review-2-reaudit-manifest-v1.1.json"
KINDS = [("candidate", "md"), ("obligations", "md"),
         ("constructor-checks", "md"), ("failed-routes", "md"),
         ("issues", "md"), ("sources", "md"), ("sources", "json"),
         ("worklog", "md"), ("code-record", "md"), ("admin", "py"),
         ("baseline", "json"), ("input-validation", "json"), ("metadata", "json")]
EXPECTED = {
    OLD: (3663, "5a029bb837c9fc8232f3364262d4d9ca66370e10d60e1dd545d5c5441798c412"),
    PARENT: (3205, "9df5acb146237cad4c9207c195dbb9d606df15ddcc61b4e9074a78fb230b7f5d"),
    "problems/2025-B4/proofs/reviewed-reasoning-diagonal-return-r7-v1.1.md":
        (18636, "e648b92125ea3571aeed8d8557d6ac43d7ac8fc65598fd6d4cc411b280ed58d4"),
    "AGENTS.md": (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"),
}


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(rel):
    p = Path(rel)
    if p.is_absolute() or ".." in p.parts:
        raise ValueError("not a declared relative path")
    if rel.startswith("problems/2025-B4/reviews/reasoning-diagonal-return-r8-review-"):
        raise ValueError("future OTHER DR8 review embargo")
    return (ROOT / rel).read_bytes()


def obj(rel):
    return json.loads(raw(rel))


def rec(rel):
    b = raw(rel)
    return {"path": rel, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def checked(r):
    actual = rec(r["path"])
    if actual != {k: r[k] for k in ("path", "bytes", "sha256")}:
        raise ValueError("immutable declared bytes changed: " + r["path"])
    return actual


def summary(records):
    unique = {}
    for r in records:
        if r["path"] in unique and unique[r["path"]] != r:
            raise ValueError("inconsistent declarations")
        unique[r["path"]] = r
    ordered = [unique[k] for k in sorted(unique)]
    return {"occurrences": len(records), "unique_paths": len(ordered),
            "canonical_sha256": hashlib.sha256(json.dumps(
                ordered, sort_keys=True, separators=(",", ":")).encode()).hexdigest()}


def output(kind, ext="json"):
    return P + kind + "-v1." + ext


def write(kind, value):
    with (ROOT / output(kind)).open("x", encoding="utf-8") as f:
        f.write(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def accepted(stem):
    path = "problems/2025-B4/reviews/" + stem + "-acceptance.json"
    j = obj(path)
    body, candidate = checked(j["accepted_copy"]), checked(j["candidate"])
    if not raw(body["path"]).endswith(raw(candidate["path"])):
        raise ValueError("accepted exact suffix mismatch")
    return {"authority_MD": rec(path[:-4] + "md"), "authority_JSON": rec(path),
            "accepted_copy": body, "exact_candidate_suffix": candidate}


def inputs():
    for path, (size, sha) in EXPECTED.items():
        checked({"path": path, "bytes": size, "sha256": sha})
    old = obj(OLD)
    old_records = [rec(OLD)] + [checked(r) for r in old["artifacts"]]
    if len(old_records) != 14:
        raise ValueError("old DR7 ENTIRE14 mismatch")
    parent = obj(PARENT)
    parent_records = [rec(PARENT)] + [checked(r) for r in parent["payloads"]]
    if len(parent_records) != 11:
        raise ValueError("own immediate parent ENTIRE11 mismatch")
    operative = accepted("reasoning-diagonal-return-r7")
    context = [accepted("reasoning-diagonal-return-r6"),
               accepted("reasoning-diagonal-return-r5")]
    direct = [rec("AGENTS.md"), rec("problems/2025-B4/statement.md"),
              rec("problems/2025-B4/proofs/reviewed-power-gap-return-v1.1.md"),
              rec("problems/2025-B4/reviews/power-gap-return-acceptance.md")]
    records = old_records + parent_records + list(operative.values()) + direct
    for x in context:
        records += list(x.values())
    return {"operative_DR7": operative,
            "operative_DR7_original_ENTIRE14_binding": rec(OLD),
            "operative_DR7_original_ENTIRE_summary": summary(old_records),
            "operative_DR7_historical_protection_summary_bound_not_reexpanded": old["protected_current_summary"],
            "comparison_only_DR6_RD": context,
            "direct_AGENTS_statement_and_PG_comparison": direct,
            "own_immediate_parent_manifest": rec(PARENT),
            "own_parent_ENTIRE_summary": summary(parent_records),
            "own_parent_historical_protection_summary_bound_not_reexpanded": parent["compact_current_protection"],
            "current_frozen_protection": summary(records),
            "historical_inventories_recopied_or_old_programs_replayed": False,
            "future_NEW_DR8_peer_review_access": False}


def labels():
    s = raw(output("obligations", "md")).decode()
    if re.findall(r"^\|DR8-(\d{2})\|", s, re.M) != [f"{i:02d}" for i in range(1,65)]:
        raise ValueError("ALL64 documentary labels/order mismatch")


def prepare():
    details = inputs()
    labels()
    write("baseline", {"prepared_at_utc": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2021_reasoning_j15_r2", "compact_bindings": details,
        "mutable_status_observation_not_immutable_guard": rec("problems/2025-B4/research.md"),
        "historical_map_observations_not_asserted_current": True})
    write("input-validation", {"validated_at_utc": now(), "old_DR7_ENTIRE14": "PASS",
        "own_immediate_parent_ENTIRE11": "PASS", "accepted_exact_suffixes": "ALL3 PASS",
        "documentary_obligation_labels": 64,
        "current_frozen_protection": details["current_frozen_protection"],
        "mathematical_instance_evaluated": False, "future_NEW_DR8_peer_access": False})
    write("metadata", {"status": "candidate proof - unverified", "constructor": "/root/review_2021_reasoning_j15_r2",
        "claims": ["DR8A", "DR8B", "DR8C"], "whole_obligations": 64,
        "sole_constructor_excluded_from_required_TWO_OTHER_whole_reviews": True,
        "root_supplied_NEW_proof_inference": False,
        "operative_accepted_input": "DR7A/DR7D exact actual signed residual p>=37 sector",
        "older_DR6_DR7_authorship_not_fresh_self_recertification": True,
        "actual_factorization_and_full_prime_powers": True,
        "both_signed_bases_and_centres": True,
        "count_is_of_Phi_p_Y_not_Y": True,
        "upper_cofactor_prime_or_support_bound_or_annual_or_priority_claim": False,
        "math_executable_CAS_scan_test_author_source_old_replay": False,
        "requested_inherited": {"model": "gpt-6.1-sol", "reasoning": "max"},
        "independent_effective_readback": None,
        "weekly": {"at_utc": "2026-10-18 16:54:44 UTC", "TOTAL_used_percent": 53,
            "window_minutes": 10080, "reset": 1792874445, "ordinary_allowed": True,
            "legacy_by_limit_agree": True, "TOTAL_ceiling": 90, "reserve": True,
            "automatic_later_window": False},
        "payload_files": 13, "ENTIRE_files": 14,
        "FULL_final_ALL13_payload_model_readback_REQUIRED_before_freeze": True,
        "FULL_freeze_model_readback_then_SEPARATE_readonly_verify_REQUIRED": True,
        "baseline": rec(output("baseline")), "input_validation": rec(output("input-validation"))})
    print(json.dumps({"prepared_at_utc": now(), "current_frozen_protection": details["current_frozen_protection"]}))


def validate():
    labels()
    actual = inputs()
    if actual != obj(output("baseline"))["compact_bindings"]:
        raise ValueError("necessary immutable bindings changed")
    return actual


def freeze():
    if sys.argv[2:] != ["--FULL-final-ALL13-payload-model-readback-complete"]:
        raise ValueError("author must assert completed FULL final ALL13 payload model readback")
    details = validate()
    payloads = [rec(output(k, ext)) for k, ext in KINDS]
    write("freeze", {"frozen_at_utc": now(), "status": "candidate proof - unverified",
        "constructor": "/root/review_2021_reasoning_j15_r2", "constructor_excluded": True,
        "claims": ["DR8A", "DR8B", "DR8C"], "whole_obligations": 64,
        "payload_files": 13, "ENTIRE_files": 14,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "FULL_final_ALL13_payload_model_readback_completed": True,
        "FULL_freeze_model_readback_then_SEPARATE_readonly_verify_REQUIRED": True,
        "compact_baseline": rec(output("baseline")),
        "current_frozen_protection": details["current_frozen_protection"],
        "no_mathematical_program_scan_CAS_test_or_old_replay": True,
        "payloads": payloads})
    print(json.dumps({"freeze": rec(output("freeze")), "at_utc": now(),
                      "FULL_freeze_model_readback_then_SEPARATE_verify_still_required": True}))


def verify():
    details = validate()
    frozen = obj(output("freeze"))
    for r in frozen["payloads"]:
        checked(r)
    if len(frozen["payloads"]) != 13 or frozen["whole_obligations"] != 64:
        raise ValueError("own ENTIRE14/ALL64 mismatch")
    print(json.dumps({"SEPARATE_readonly_verified_at_utc": now(), "status": "PASS",
        "ENTIRE_files": 14, "whole_obligations": 64,
        "current_frozen_protection": details["current_frozen_protection"],
        "freeze": rec(output("freeze")), "main": rec(output("candidate", "md")),
        "no_file_written": True, "no_mathematical_instance_evaluated": True}))


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in {"prepare", "freeze", "verify"}:
        raise SystemExit("prepare | freeze --FULL-final-ALL13-payload-model-readback-complete | verify")
    {"prepare": prepare, "freeze": freeze, "verify": verify}[sys.argv[1]]()
