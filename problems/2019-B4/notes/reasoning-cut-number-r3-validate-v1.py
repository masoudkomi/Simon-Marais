#!/usr/bin/env python3
"""Administrative metadata only. No mathematical example generation or tests."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/notes/reasoning-cut-number-r3-"
BASELINE = PREFIX + "baseline-v1.json"
INTEGRITY = PREFIX + "integrity-v1.json"
FREEZE = PREFIX + "freeze-v1.json"
PARENT = "problems/2024-B4/reviews/cofactor-dominant-r4-review-1-manifest-v1.json"
PARENT_EXPECTED = {
    "path": PARENT,
    "bytes": 7640,
    "sha256": "05e4eb5d531c0ed58d7059d573a50cd149578783ff54c3e4e0dff53eb325e3e1",
}
ACCEPTED = [
    ("reasoning-critical-return-r2", "reviewed-reasoning-critical-return-r2-v1.1.md", 26079,
     "e6f2d345c96cf0b080af9e42092dc13c66b69bfe0b70cd1bcab4b33f43106881", "CR1--CR5"),
    ("reasoning-return-r7", "reviewed-reasoning-return-r7-v1.1.md", 17727,
     "4fe222b8b1d89b6b3d66bb16c6a1985390d537eee55bb42bfefdb2d4821e351a", "R7 exact normalized-count scopes"),
    ("monotone-ratio", "reviewed-monotone-ratio-v1.1.md", 11402,
     "a87798e4df63ec2f76e83da9750f811b15fc6702533b4ca68bd8bd973ac3bac9", "MR1 and conditional MR2"),
    ("reasoning-growth-return-r1", "reviewed-reasoning-growth-return-r1-v1.1.md", 26251,
     "c43a76227937eb11ff8261cc34cece7a411f6637fc4794336c3161f05ba11ea3", "G1--G5 exact actual/conditional scopes"),
    ("walk-Frechet", "reviewed-walk-Frechet-v1.1.md", 18752,
     "c068f531fa9fa3c420867ae898291b6034cef7511e72ec6fd16f20ac3b023f44", "DG1--DG4; interpretation only"),
    ("auxiliary-presentation-r1", "reviewed-auxiliary-presentation-r1-v1.1.md", 11103,
     "fb315bd75a528bbfb7c98d0464ea667cd3e93ef88cd1251fff20c8a219270929", "AF context only; not a new proof premise"),
]
CONTEXT = [
    "AGENTS.md",
    "problems/2019-B4/statement.md",
    "problems/2019-B4/research.md",
    "problems/2019-B4/references.md",
    "problems/2019-B4/notes/secondpass-canonical-renewal.md",
    "problems/2019-B4/notes/secondpass-staircases-and-pumping.md",
    "problems/2019-B4/notes/coordinator-short-joining-research-v1.md",
    "problems/2019-B4/notes/coordinator-critical-code-countermodel-v1.md",
    "problems/2019-B4/notes/reasoning-critical-return-r2-sources-v1.md",
]
PAYLOAD_SUFFIXES = [
    "candidate-v1.md", "obligations-v1.md", "checks-v1.md", "failures-v1.md",
    "sources-v1.md", "worklog-v1.md", "code-record-v1.md", "validate-v1.py",
    "baseline-v1.json", "integrity-v1.json",
]


def stamp():
    return datetime.now(timezone.utc).isoformat()


def local_path(name):
    path = (ROOT / name).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError("Out-of-workspace reference: " + name)
    return path


def fingerprint(name):
    data = local_path(name).read_bytes()
    return {"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def read_json(name):
    return json.loads(local_path(name).read_text())


def write_new(name, value):
    if not name.startswith(PREFIX):
        raise ValueError("Write outside assigned prefix")
    with local_path(name).open("x") as out:
        json.dump(value, out, indent=2)
        out.write("\n")


def declared_records(value):
    found = []
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str) and isinstance(value.get("bytes"), int)
                and isinstance(value.get("sha256"), str) and len(value["sha256"]) == 64):
            found.append({key: value[key] for key in ("path", "bytes", "sha256")})
        for child in value.values():
            found.extend(declared_records(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(declared_records(child))
    return found


def checked(record):
    actual = fingerprint(record["path"])
    if actual != record:
        raise ValueError("Fingerprint mismatch: " + record["path"])
    return actual


def summary(records):
    unique = {}
    for record in records:
        checked(record)
        old = unique.setdefault(record["path"], record)
        if old != record:
            raise ValueError("Conflicting declared records: " + record["path"])
    serial = json.dumps([unique[key] for key in sorted(unique)], sort_keys=True,
                        separators=(",", ":")).encode()
    return {
        "fingerprint_occurrences_verified": len(records),
        "deduplicated_paths_verified": len(unique),
        "canonical_deduplicated_record_summary_sha256": hashlib.sha256(serial).hexdigest(),
    }


def collect_existing():
    parent = checked(PARENT_EXPECTED)
    parent_doc = read_json(PARENT)
    parent_records = declared_records(parent_doc)
    parent_summary = summary(parent_records)
    direct = [fingerprint(name) for name in CONTEXT]
    direct.extend([parent] + parent_doc["artifacts"])
    authorities = []
    current = list(direct) + parent_records
    for stem, body_name, size, sha, scope in ACCEPTED:
        authority_name = "problems/2019-B4/reviews/" + stem + "-acceptance.json"
        body_name = "problems/2019-B4/proofs/" + body_name
        doc = read_json(authority_name)
        body = {"path": body_name, "bytes": size, "sha256": sha}
        if doc["accepted_copy"] != body:
            raise ValueError("Accepted-body authority disagreement: " + stem)
        if doc.get("unresolved_substantive_issues") != 0 or doc.get("repair_required") is not False:
            raise ValueError("Accepted authority has an unresolved repair: " + stem)
        authority = fingerprint(authority_name)
        checked(body)
        records = declared_records(doc)
        entry = {
            "authority": authority,
            "accepted_body": body,
            "exact_read_scope": scope,
            "complete_accepted_body_and_authority_read": True,
            "declared_current_fingerprints": summary(records),
            "historical_coordinator_record_occurrences_bound_not_replayed": doc.get("record_occurrences_verified"),
            "historical_coordinator_paths_bound_not_replayed": doc.get("unique_paths_verified"),
            "transitive_inventory_not_recopied_or_recursively_reverified": True,
        }
        authorities.append(entry)
        direct.extend([authority, body])
        current.extend([authority, body] + records)
    current_summary = summary(current)
    return {
        "direct_inputs": direct,
        "accepted_inputs": authorities,
        "own_immutable_immediate_parent": {
            "manifest": parent,
            "manifest_declared_records": parent_summary,
            "old_reported_current_occurrences_bound": parent_doc["current_occurrences"],
            "old_reported_current_paths_bound": parent_doc["unique_paths"],
            "all_own_parent_payloads_checked": len(parent_doc["artifacts"]),
            "historical_inventory_not_recopied_or_recursively_reverified": True,
        },
        "current_existing_summary": current_summary,
    }, current


def make_baseline():
    data, _ = collect_existing()
    data.update({
        "created_utc": stamp(),
        "status": "compact constructor baseline; candidate proof - unverified",
        "all_direct_inputs_read_in_full_at_stated_source_scopes": True,
        "old_R7_authorship_and_other_old_review_roles_not_new_self_recertification": True,
        "no_new_queued_R5_or_ToddR12_peer_or_candidate_access": True,
        "only_assigned_new_prefix_written": True,
        "no_Git_shared_old_cache_mutation_or_math_code": True,
    })
    write_new(BASELINE, data)
    print(json.dumps({"mode": "baseline", "baseline": fingerprint(BASELINE),
                      "existing": data["current_existing_summary"]}))


def validate_baseline():
    doc = read_json(BASELINE)
    data, current = collect_existing()
    for key in ("direct_inputs", "accepted_inputs", "own_immutable_immediate_parent", "current_existing_summary"):
        if data[key] != doc[key]:
            raise ValueError("Baseline changed: " + key)
    return doc, current


def make_freeze():
    baseline, current = validate_baseline()
    integrity = {
        "checked_utc": stamp(),
        "status": "all necessary current declared fingerprints match; no mathematical code",
        "baseline": fingerprint(BASELINE),
        "existing_summary": summary(current),
        "accepted_authorities": len(ACCEPTED),
        "all6_authority_body_pairs_agree": True,
        "own_immediate_parent_and_all10_payloads_preserved": True,
        "compact_parents_not_recursively_replayed": True,
        "all48_author_obligations_and_full_proof_readback_complete": True,
        "independent_reviews_pending": 2,
    }
    write_new(INTEGRITY, integrity)
    payloads = [fingerprint(PREFIX + suffix) for suffix in PAYLOAD_SUFFIXES]
    all_current = current + payloads
    data = {
        "frozen_utc": stamp(),
        "status": "candidate proof - unverified; TWO OTHER initially blind ENTIRE WHOLE audits required",
        "constructor": "/root/review_2021_reasoning_j15_r2",
        "root_generic_assignment_only_no_new_mathematical_inference": True,
        "claims": ["CN1", "CN2", "CN3"],
        "all_author_obligations": 48,
        "full_main_ALL48_checks_failures_sources_log_code_baseline_integrity_complete": True,
        "exact_scope": "actual two-rate periods; balanced linear cut fibres despite bounded fixed-range pieces; constructed-flat rarity only",
        "actual_mean_or_renewal_regime_exact_lambda_numeric_improvement_annual_or_novelty_claim": False,
        "mathematical_program_CAS_scan_finite_example_generator_or_certificate_rerun": False,
        "prior_R7_authorship_and_review_roles_disclosed_not_new_self_recertification": True,
        "only_assigned_new_prefix_written_no_Git_shared_old_cache_spawn_contact_charge_bypass": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_setting_readback": None,
        "authoritative_weekly_telemetry": {
            "observed_utc": "2026-10-18 10:33:56 UTC",
            "method": "get_usage_limits and same-batch clock",
            "used_percent_TOTAL": 25,
            "window_minutes": 10080,
            "reset_unix": 1792874445,
            "ordinary_usage_allowed": True,
            "legacy_by_limit_agree": True,
            "account_suffix": "1334ac3a",
            "ceiling_TOTAL_percent": 90,
            "integration_reserve": True,
            "explicitly_authorized_current_window_only_no_automatic_later_window": True,
        },
        "main": fingerprint(PREFIX + "candidate-v1.md"),
        "baseline": fingerprint(BASELINE),
        "integrity": fingerprint(INTEGRITY),
        "own_immutable_immediate_parent": baseline["own_immutable_immediate_parent"],
        "current_inputs_and_payloads_summary": summary(all_current),
        "historical_inventories_bound_by_parent_fingerprints_not_copied_or_recursively_reverified": True,
        "payloads": len(payloads),
        "files_including_freeze": len(payloads) + 1,
        "artifacts": payloads,
        "generated_metadata_full_readback_and_separate_postverification_required": True,
    }
    write_new(FREEZE, data)
    print(json.dumps({"mode": "freeze", "freeze": fingerprint(FREEZE),
                      "main": data["main"], "current": data["current_inputs_and_payloads_summary"]}))


def verify():
    baseline, current = validate_baseline()
    doc = read_json(FREEZE)
    for record in doc["artifacts"]:
        checked(record)
    checked(doc["main"])
    checked(doc["baseline"])
    checked(doc["integrity"])
    if doc["own_immutable_immediate_parent"] != baseline["own_immutable_immediate_parent"]:
        raise ValueError("Parent binding changed")
    if summary(current + doc["artifacts"]) != doc["current_inputs_and_payloads_summary"]:
        raise ValueError("Current metadata summary changed")
    print(json.dumps({"mode": "verify", "all_match": True,
                      "freeze": fingerprint(FREEZE), "main": doc["main"],
                      "all48": True, "files": doc["files_including_freeze"],
                      "current": doc["current_inputs_and_payloads_summary"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    choices = parser.add_mutually_exclusive_group(required=True)
    choices.add_argument("--baseline", action="store_true")
    choices.add_argument("--freeze", action="store_true")
    choices.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.baseline:
        make_baseline()
    elif args.freeze:
        make_freeze()
    else:
        verify()
