#!/usr/bin/env python3
"""Review metadata only: file hashes/JSON/suffix/labels; no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-1-"
T = "problems/2024-B4/notes/cofactor-Frobenius-r5-"
AUTHOR_FREEZE = T + "freeze-v1.json"
OLD_PARENT = "problems/2024-B4/notes/cofactor-dominant-r4-freeze-v1.json"
OWN_PARENT = "problems/2019-B4/notes/reasoning-cut-number-r3-freeze-v1.json"
EXPECTED = [
    {"path": T + "candidate-v1.md", "bytes": 12486,
     "sha256": "ff29bb1757d3f24229cb138bdfcca02b4d45c457200afc2ecc78104918c823ee"},
    {"path": AUTHOR_FREEZE, "bytes": 3932,
     "sha256": "cda866d3b82dfe335c78643d15d857e21bcda5439c2ecf308956281b02a8b545"},
    {"path": OWN_PARENT, "bytes": 5393,
     "sha256": "4a172e842aabf71d774ee5c8cfca458135e571ce7328c98be0eee1b3d0279089"},
]
CONTENT = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "sources-v1.md",
           "sources-v1.json", "worklog-v1.md", "freeze-v1.py"]
META = ["baseline-v1.json", "metadata-v1.json", "input-validation-v1.json"]


def stamp():
    return datetime.now(timezone.utc).isoformat()


def path(name):
    value = (ROOT / name).resolve()
    assert value.is_relative_to(ROOT), name
    return value


def raw(name):
    return path(name).read_bytes()


def obj(name):
    return json.loads(raw(name))


def rec(name):
    data = raw(name)
    return {"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def check(row):
    expected = {key: row[key] for key in ("path", "bytes", "sha256")}
    assert rec(row["path"]) == expected, row["path"]
    return expected


def write_new(suffix, value):
    name = P + suffix
    assert name.startswith(P)
    with path(name).open("x") as output:
        json.dump(value, output, indent=2)
        output.write("\n")


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def rows(value):
    result = []
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str) and isinstance(value.get("bytes"), int)
                and isinstance(value.get("sha256"), str) and len(value["sha256"]) == 64):
            result.append({key: value[key] for key in ("path", "bytes", "sha256")})
        for child in value.values():
            result.extend(rows(child))
    elif isinstance(value, list):
        for child in value:
            result.extend(rows(child))
    return result


def summary(values):
    unique = {}
    for value in values:
        record = check(value)
        previous = unique.setdefault(record["path"], record)
        assert previous == record, record["path"]
    return {"occurrences": len(values), "unique_paths": len(unique),
            "sha256": canonical([unique[key] for key in sorted(unique)])}


def current():
    for record in EXPECTED:
        check(record)
    author = obj(AUTHOR_FREEZE)
    author_baseline = obj(T + "baseline-v1.json")
    assert author["files_including_freeze"] == 9 and len(author["artifacts"]) == 8
    for record in author["artifacts"]:
        check(record)
    parent = obj(OLD_PARENT)
    names = ["AGENTS.md", "problems/2024-B4/statement.md", OLD_PARENT,
             "problems/2024-B4/notes/cofactor-global-r2-source-audit-v1.md"]
    authority_bindings = []
    accepted_records = []
    for stem, expected_sha in [
        ("cofactor-global-r2", "fd110d1615e730d754063b157cc1906b418702f510b2640bfd1b5c63e898548d"),
        ("cofactor-dominant-r4", "14c47b6db082bee1d60bcf297c289fe949fdec9384cc8a159b199c56ba265838"),
    ]:
        authority_name = "problems/2024-B4/reviews/" + stem + "-acceptance.json"
        value = obj(authority_name)
        assert value["unresolved_substantive_issues"] == 0 and value["repair_required"] is False
        assert value["accepted_copy"]["sha256"] == expected_sha
        check(value["accepted_copy"])
        check(value["candidate"])
        assert raw(value["accepted_copy"]["path"]).endswith(raw(value["candidate"]["path"]))
        names += ["problems/2024-B4/reviews/" + stem + suffix for suffix in
                  ("-acceptance.md", "-acceptance.json", "-acceptance-integrity.json")]
        names += [value["accepted_copy"]["path"], value["candidate"]["path"]]
        declared = rows(value)
        accepted_records += declared
        authority_bindings.append({
            "authority": rec(authority_name), "accepted_body": value["accepted_copy"],
            "candidate": value["candidate"], "declared_current_summary": summary(declared),
            "old_coordinator_occurrences_bound_not_replayed": value["record_occurrences_verified"],
            "old_coordinator_paths_bound_not_replayed": value["unique_paths_verified"],
        })
    author_declared = [rec(name) for name in names] + parent["artifacts"]
    author_summary = summary(author_declared)
    assert author_summary == author["current_input_summary"] == author_baseline["current_input_summary"]
    assert canonical(author_baseline["protected"]) == author_summary["sha256"]
    for record in author_baseline["protected"]:
        check(record)
    own_parent = obj(OWN_PARENT)
    assert own_parent["files_including_freeze"] == 11 and len(own_parent["artifacts"]) == 10
    own_parent_records = [rec(OWN_PARENT)] + own_parent["artifacts"]
    own_parent_summary = summary(own_parent_records)
    values = author_declared + [rec(AUTHOR_FREEZE)] + author["artifacts"]
    values += accepted_records + own_parent_records
    protected = {}
    for record in values:
        check(record)
        previous = protected.setdefault(record["path"], record)
        assert previous == record
    data = {
        "target_main": rec(T + "candidate-v1.md"), "target_constructor_freeze": rec(AUTHOR_FREEZE),
        "all9_author_artifacts_verified": True,
        "author_current_24occ23paths_reconstructed": author_summary,
        "accepted_operative_bindings": authority_bindings,
        "own_immutable_immediate_parent": {
            "manifest": rec(OWN_PARENT), "own_all11_summary": own_parent_summary,
            "old_reported_occurrences_bound": own_parent["current_inputs_and_payloads_summary"]["fingerprint_occurrences_verified"],
            "old_reported_paths_bound": own_parent["current_inputs_and_payloads_summary"]["deduplicated_paths_verified"],
            "old_inventory_not_recopied_or_recursively_reverified": True,
        },
        "protected_current": [protected[key] for key in sorted(protected)],
        "current_summary": summary(values),
    }
    return data, values


def baseline():
    data, _ = current()
    data.update({"captured_utc": stamp(), "administrative_only": True,
                 "no_corresponding_NEW_R5_R2_material_access": True,
                 "compact_parents_no_recursive_historical_replay": True})
    write_new("baseline-v1.json", data)
    print(json.dumps({"mode": "baseline", "baseline": rec(P + "baseline-v1.json"),
                      "current": data["current_summary"]}))


def validate_baseline():
    base = obj(P + "baseline-v1.json")
    data, values = current()
    for key in data:
        assert data[key] == base[key], key
    return base, values


def freeze():
    base, values = validate_baseline()
    author_labels = re.findall(r"^\| (CF-\d{2}) \|", raw(T + "obligations-v1.md").decode(), re.M)
    own_labels = re.findall(r"^\| (CF-\d{2}) \|", raw(P + "ledger-v1.md").decode(), re.M)
    expected_labels = ["CF-" + str(index).zfill(2) for index in range(1, 33)]
    assert author_labels == own_labels == expected_labels
    write_new("metadata-v1.json", {
        "created_utc": stamp(), "administrative_only": True,
        "reviewer": "/root/review_2021_reasoning_j15_r2", "root_sole_NEW_constructor_excluded": True,
        "status": "ENTIRE initially blind OTHER WHOLE R1 recommendation; not promotion",
        "all32_reconstructed": True, "substantive_defects": 0,
        "required_mathematical_theorem_repairs": 0, "nonsubstantive_literal_errors_qualified": 2,
        "closed_notes": 6, "N1_N2_editorial_qualifications_required_in_reconciliation": True,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "old_roles_not_fresh_self_recertification": True,
        "no_corresponding_NEW_R2_R5_finding_file_hash_metadata_access": True,
        "findings_withheld_until_BOTH_ENTIRE_initials_confirmed": True,
        "no_mathematical_code_CAS_scan_optimizer_author_source_rerun": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass_or_wait": True,
        "latest_authoritative_own_telemetry": {
            "observed_utc": "2026-10-18 10:33:56 UTC", "used_percent_TOTAL": 25,
            "window_minutes": 10080, "reset_unix": 1792874445,
            "ordinary_usage_allowed": True, "legacy_by_limit_agree": True,
            "account_suffix": "1334ac3a", "ceiling_TOTAL_percent": 90,
            "integration_reserve": True, "authorized_current_window_only": True,
            "automatic_later_window_spending": False,
        },
    })
    write_new("input-validation-v1.json", {
        "checked_utc": stamp(), "administrative_only": True,
        "all_current_fingerprints_match": True, "current_summary": summary(values),
        "all9_constructor_files_and_both_current_accepted_body_suffixes_verified": True,
        "all32_author_and_reviewer_labels_once_in_order": True,
        "mathematics_not_validated_by_script": True, "errors": [],
    })
    artifacts = [rec(P + suffix) for suffix in CONTENT + META]
    write_new("manifest-v1.json", {
        "frozen_utc": stamp(), "status": "ENTIRE initially blind OTHER WHOLE R1 recommendation; not promotion",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "root_sole_NEW_constructor_excluded": True,
        "target_main": base["target_main"], "target_constructor_freeze": base["target_constructor_freeze"],
        "all32_reconstructed": True, "substantive_defects": 0,
        "required_mathematical_theorem_repairs": 0, "nonsubstantive_literal_errors_qualified": 2,
        "closed_notes": 6, "N1_N2_editorial_qualifications_required_in_reconciliation": True,
        "ENTIRE_report_ALL32_ledger_issues_sources_MD_JSON_log_code_ALLmetadata_complete": True,
        "no_corresponding_NEW_R2_R5_finding_file_hash_metadata_access_through_ENTIRE_freeze": True,
        "identity_only_completion_findings_withheld_until_BOTH_ENTIRE_confirmed": True,
        "old_roles_disclosed_no_fresh_self_recertification": True,
        "exact_scope": "R5A-D ordinary prime s>=5,k>=2; necessary strict-reverse test and whole Q32 all k>=2 only",
        "no_general_prime_s_k2_composite_s_s3_k1_annual_external_validation_or_novelty_claim": True,
        "no_mathematical_code_CAS_scan_optimizer_source_or_author_rerun": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass_or_wait": True,
        "baseline": rec(P + "baseline-v1.json"),
        "own_immutable_immediate_parent": base["own_immutable_immediate_parent"],
        "accepted_operative_bindings": base["accepted_operative_bindings"],
        "current_inputs_and_payloads_summary": summary(values + artifacts),
        "historical_inventories_bound_not_recopied_or_recursively_reverified": True,
        "payloads": len(artifacts), "files_including_manifest": len(artifacts) + 1,
        "artifacts": artifacts,
        "full_generated_metadata_readback_then_separate_postverification_required": True,
    })
    print(json.dumps({"mode": "freeze", "manifest": rec(P + "manifest-v1.json"),
                      "initial": rec(P + "initial-v1.md"), "files": len(artifacts) + 1}))


def verify():
    base, values = validate_baseline()
    manifest = obj(P + "manifest-v1.json")
    for record in manifest["artifacts"]:
        check(record)
    assert summary(values + manifest["artifacts"]) == manifest["current_inputs_and_payloads_summary"]
    assert manifest["own_immutable_immediate_parent"] == base["own_immutable_immediate_parent"]
    print(json.dumps({"mode": "verify", "all_match": True,
                      "manifest": rec(P + "manifest-v1.json"), "initial": rec(P + "initial-v1.md"),
                      "all32": True, "files": manifest["files_including_manifest"],
                      "current": manifest["current_inputs_and_payloads_summary"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--baseline", action="store_true")
    modes.add_argument("--freeze", action="store_true")
    modes.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.baseline:
        baseline()
    elif args.freeze:
        freeze()
    else:
        verify()
