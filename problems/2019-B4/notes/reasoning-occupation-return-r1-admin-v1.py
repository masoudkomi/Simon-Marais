#!/usr/bin/env python3
"""AU documentary integrity ONLY: no mathematics, words, scans or old code.

Writes only this NEW prefix. 'verify' is read-only. Historical metadata
is bound compactly; no recursive historical inventory is copied.
"""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/notes/reasoning-occupation-return-r1-"
SUFFIXES = [
    "candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "issues-v1.md", "failed-routes-v1.md", "sources-v1.md",
    "sources-v1.json", "worklog-v1.md", "admin-v1.py",
    "baseline-v1.json", "input-validation-v1.json",
]
BASELINE = PREFIX + "baseline-v1.json"
VALIDATION = PREFIX + "input-validation-v1.json"
FREEZE = PREFIX + "freeze-v1.json"
PARENT = {
    "path": "problems/2020-B4/notes/reasoning-arithmetic-return-r14-freeze-v1.1.json",
    "bytes": 7882,
    "sha256": "6468e2ee52ca8d0ef18e27d65ce57cda932e3072eb8f95e2c3565233026395c9",
}
AUTHORITY_NAMES = [
    "reasoning-return-r7", "reasoning-cut-number-r3",
    "reasoning-cut-transfer-r4", "reasoning-cut-transfer-r6",
    "reasoning-cut-transfer-r5", "reasoning-growth-return-r1",
    "reasoning-critical-return-r2",
]
EXACT_INPUTS = [
    "AGENTS.md", "problems/2019-B4/statement.md",
    "problems/2019-B4/proofs/reviewed-reasoning-return-r7-v1.1.md",
    "problems/2019-B4/proofs/reviewed-reasoning-cut-number-r3-v1.1.md",
    "problems/2019-B4/proofs/reviewed-reasoning-cut-transfer-r4-v1.2.md",
    "problems/2019-B4/proofs/reviewed-reasoning-cut-transfer-r6-v1.1.md",
    "problems/2019-B4/proofs/reviewed-reasoning-cut-transfer-r5-v1.1.md",
    "problems/2019-B4/proofs/reviewed-reasoning-growth-return-r1-v1.1.md",
    "problems/2019-B4/proofs/reviewed-reasoning-critical-return-r2-v1.1.md",
    "problems/2019-B4/reviews/reasoning-cut-transfer-r4-presentation-erratum-v1.md",
    "problems/2019-B4/reviews/reasoning-cut-transfer-r4-presentation-erratum-v1.json",
    "problems/2019-B4/proofs/reviewed-linear-output-return-v1.1.md",
    "problems/2019-B4/notes/linear-output-return-r1-source-audit-v1.md",
    "problems/2019-B4/notes/reasoning-cut-transfer-r6-failed-routes-v1.md",
]
for _stem in AUTHORITY_NAMES:
    EXACT_INPUTS.extend([
        "problems/2019-B4/reviews/" + _stem + "-acceptance.md",
        "problems/2019-B4/reviews/" + _stem + "-acceptance.json",
    ])


def now():
    return datetime.now(timezone.utc).isoformat()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def fingerprint(path):
    p = ROOT / path
    assert p.is_file(), ("missing documentary input", path)
    data = p.read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def match(record):
    assert fingerprint(record["path"]) == {
        k: record[k] for k in ("path", "bytes", "sha256")
    }, ("fingerprint changed", record["path"])


def read_json(path):
    return json.loads((ROOT / path).read_text())


def write_new(path, value):
    assert path.startswith(PREFIX), ("write outside exclusive prefix", path)
    assert path in (BASELINE, VALIDATION, FREEZE)
    if path != FREEZE:
        assert not (ROOT / FREEZE).exists(), "frozen bytes cannot be rewritten"
    else:
        assert not (ROOT / path).exists(), "freeze already exists"
    (ROOT / path).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def labels():
    out = {}
    for suffix in ("obligations-v1.md", "constructor-checks-v1.md"):
        data = (ROOT / (PREFIX + suffix)).read_text()
        found = re.findall(r"(?m)^(\d{2})\. ", data)
        expected = [f"{i:02d}" for i in range(1, 65)]
        assert found == expected, ("document-label coverage", suffix, found)
        out[suffix] = {"separate_unique_document_labels": len(found),
                       "exactly_01_through_64": True}
    return out


def gather_inputs():
    """Read ONLY explicit inputs/accepted pointers/own immediate parent."""
    rows = [fingerprint(path) for path in EXACT_INPUTS]
    summaries = []
    for name in AUTHORITY_NAMES:
        authority_path = "problems/2019-B4/reviews/" + name + "-acceptance.json"
        doc = read_json(authority_path)
        assert doc["status"] == "proved, independently reviewed scoped partial result"
        accepted = doc["accepted_copy"]
        match(accepted)
        rows.append(accepted)
        candidate = doc.get("candidate")
        if candidate:
            match(candidate)
            rows.append(candidate)
            assert (ROOT / accepted["path"]).read_bytes().endswith(
                (ROOT / candidate["path"]).read_bytes()
            ), ("accepted suffix mismatch", accepted["path"])
        summaries.append({
            "authority": fingerprint(authority_path),
            "body_declared_by_authority": accepted,
            "historical_occurrences_bound_not_expanded":
                doc.get("record_occurrences_verified"),
            "historical_unique_paths_bound_not_expanded":
                doc.get("unique_paths_verified"),
        })
    erratum = read_json(
        "problems/2019-B4/reviews/reasoning-cut-transfer-r4-presentation-erratum-v1.json"
    )
    for key in ("old_accepted_copy", "operative_accepted_copy",
                "unchanged_candidate_suffix", "historical_authority"):
        match(erratum[key])
        rows.append(erratum[key])
    operative = erratum["operative_accepted_copy"]["path"]
    raw = erratum["unchanged_candidate_suffix"]["path"]
    assert (ROOT / operative).read_bytes().endswith((ROOT / raw).read_bytes())
    match(PARENT)
    parent = read_json(PARENT["path"])
    assert parent["ENTIRE_files_including_manifest"] == 14
    assert parent["older_plus_new_own_paths_bound_transitively"] == 900
    rows.append(PARENT)
    for record in parent["payloads"]:
        match(record)
        rows.append(record)
    assert len(parent["payloads"]) == 13
    unique = {}
    for record in rows:
        reduced = {k: record[k] for k in ("path", "bytes", "sha256")}
        if record["path"] in unique:
            assert unique[record["path"]] == reduced
        unique[record["path"]] = reduced
    dedup = [unique[p] for p in sorted(unique)]
    summary = {
        "occurrences": len(rows), "unique_paths": len(dedup),
        "canonical_deduplicated_sha256": hashlib.sha256(canonical(dedup)).hexdigest(),
    }
    return dedup, summary, summaries


def check_baseline():
    baseline = read_json(BASELINE)
    for record in baseline["exact_guard_records"]:
        match(record)
    assert baseline["immediate_own_parent"] == PARENT
    assert baseline["older_own_paths_bound_transitively"] == 900
    digest = hashlib.sha256(canonical(baseline["exact_guard_records"])).hexdigest()
    assert digest == baseline["summary"]["canonical_deduplicated_sha256"]
    return baseline


def prepare():
    assert not (ROOT / FREEZE).exists(), "already frozen"
    if (ROOT / BASELINE).exists():
        check_baseline()
    records, summary, authorities = gather_inputs()
    coverage = labels()
    sources = read_json(PREFIX + "sources-v1.json")
    assert sources["new_external_mathematical_theorem_imported"] is False
    baseline = {
        "prepared_at_utc": now(),
        "role": "documentary byte guards only; no mathematical evaluation",
        "exact_guard_records": records,
        "summary": summary,
        "operative_authority_summaries": authorities,
        "CT_v1_2_erratum_and_exact_body_bound": True,
        "immediate_own_parent": PARENT,
        "older_own_paths_bound_transitively": 900,
        "parent_ENTIRE14_unchanged": True,
        "historical_inventory_recopied_or_old_code_executed": False,
        "corresponding_NEW_peer_material_opened_or_inventoried": False,
    }
    write_new(BASELINE, baseline)
    write_new(VALIDATION, {
        "validated_at_utc": now(), "status": "documentary PASS only",
        "whole_obligations": 64, "separate_author_dispositions": 64,
        "coverage": coverage, "guard_summary": summary,
        "mathematics_proved_by_code": False,
        "parent_ENTIRE14_unchanged": True,
        "historical_inventory_expanded": False,
    })
    print(json.dumps({"prepare": "PASS", "at_utc": now(),
                      "guard_summary": summary, "whole_labels": 64}))


def freeze():
    baseline = check_baseline()
    labels()
    validation = read_json(VALIDATION)
    assert validation["guard_summary"] == baseline["summary"]
    payloads = [fingerprint(PREFIX + suffix) for suffix in SUFFIXES]
    doc = {
        "frozen_at_utc": now(),
        "status": "candidate proof - unverified",
        "claims": ["AU1", "AU2", "AU3", "AU4"],
        "constructor": "/root/review_2022_complexity_r2",
        "constructor_excluded": True,
        "root_generic_target_new_inference": False,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "whole_obligations": 64, "constructor_hand_dispositions": 64,
        "ENTIRE_files_including_manifest": len(payloads) + 1,
        "requested": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independent_effective_readback": None,
        "FULL_final_model_readback_ALL11_payloads_code_generated_metadata_attested": True,
        "FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required": True,
        "guard_summary": baseline["summary"],
        "immediate_own_parent": PARENT,
        "older_own_paths_bound_transitively": 900,
        "older_plus_new_own_paths_bound_transitively": 900 + len(payloads) + 1,
        "no_corresponding_NEW_peer_review_material_access_or_inventory": True,
        "no_mathematical_program_CAS_scan_test_optimizer_old_author_source_replay": True,
        "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
        "actual_fixed_positive_area_density_upper_mass_control_proved": False,
        "actual_renewal_regime_or_new_lambda_bound_annual_priority_claim": False,
        "weekly_telemetry": {
            "at_utc": "2026-10-18 17:09:01 UTC",
            "method": "own same-awaited clock/get_usage_limits",
            "TOTAL_used_percent": 54, "window_minutes": 10080,
            "resetsAt": 1792874445, "ordinaryUsageAllowed": True,
            "legacy_by_limit_agree": True,
            "account_label": "029a8928...1334ac3a",
            "TOTAL_ceiling_percent": 90, "integration_reserve": True,
            "automatic_later_window_spending": False,
        },
        "payloads": payloads,
    }
    write_new(FREEZE, doc)
    print(json.dumps({"freeze": "PASS", "identity": fingerprint(FREEZE),
                      "at_utc": doc["frozen_at_utc"],
                      "ENTIRE": len(payloads) + 1, "whole_obligations": 64}))


def verify():
    doc = read_json(FREEZE)
    assert doc["whole_obligations"] == 64
    assert doc["ENTIRE_files_including_manifest"] == 12
    assert len(doc["payloads"]) == len(SUFFIXES)
    assert [r["path"] for r in doc["payloads"]] == [PREFIX + s for s in SUFFIXES]
    for record in doc["payloads"]:
        match(record)
    baseline = check_baseline()
    assert doc["guard_summary"] == baseline["summary"]
    labels()
    print(json.dumps({"SEPARATE_readonly_verify": "PASS", "at_utc": now(),
                      "ENTIRE_files": 12, "whole_obligations": 64,
                      "identity": fingerprint(FREEZE),
                      "guard_summary": baseline["summary"],
                      "writes_in_verify": False}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "freeze", "verify"))
    args = parser.parse_args()
    {"prepare": prepare, "freeze": freeze, "verify": verify}[args.mode]()
