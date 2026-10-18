#!/usr/bin/env python3
"""Review integrity only: no math computation, author execution or peer access."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/cofactor-cubic-r3-review-1-"
C = "problems/2024-B4/notes/cofactor-cubic-r3-"
PEER = "problems/2024-B4/reviews/cofactor-cubic-r3-review-2-"
PARENT = "problems/2021-B4/notes/reasoning-early-return-r16-freeze-v1.json"
PARENT_SHA = "8ff369c2ad1d306316599be62096001a50a2799f897b612df6e7c96a0aa731de"
AUTH = "problems/2024-B4/reviews/cofactor-global-r2-acceptance.json"
MAIN_SHA = "153cbc7a070eb1bffdb62f351c64a79353d8dd41a3e5db03c051b4ed8041f0c4"
FREEZE_SHA = "fcb6f42f7aa824110a5bb60178b2f9db9dc80e37a5827dbc03895484957be263"
PAYLOADS = ["initial-v1.md", "issues-v1.md", "sources-v1.md", "sources-v1.json",
    "worklog-v1.md", "freeze-v1.py", "baseline-v1.json", "metadata-v1.json",
    "input-validation-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert not path.startswith(PEER), "NEW corresponding B review access forbidden"
    return (ROOT / path).read_bytes()


def fp(path):
    value = raw(path)
    return dict(path=path, bytes=len(value), sha256=hashlib.sha256(value).hexdigest())


def load(path):
    return json.loads(raw(path))


def check(row):
    wanted = {key: row[key] for key in ("path", "bytes", "sha256")}
    assert fp(wanted["path"]) == wanted, wanted["path"]
    return wanted


def digest(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def new_json(suffix, value):
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def authority():
    value = load(AUTH)
    assert value["unresolved_substantive_issues"] == 0
    assert value["repair_required"] is False and value["constructor_excluded"] is True
    assert value["proposed_claims_accepted"] == ["CG1", "CG2", "CG3"]
    proof, candidate = check(value["accepted_copy"]), check(value["candidate"])
    assert proof["sha256"] == "fd110d1615e730d754063b157cc1906b418702f510b2640bfd1b5c63e898548d"
    assert raw(proof["path"]).endswith(raw(candidate["path"]))
    return dict(authority=fp(AUTH), accepted_copy=proof, exact_candidate_suffix=candidate,
        operative_claims=["CG1", "CG2"], stronger_Section6_equation9_first_line_read=True,
        old_CG3_threshold_not_used=True,
        historical_occurrences_bound_not_replayed=value["record_occurrences_verified"],
        historical_paths_bound_not_replayed=value["unique_paths_verified"])


def baseline():
    target = fp(C + "freeze-v1.json")
    assert (target["bytes"], target["sha256"]) == (2786, FREEZE_SHA)
    target_data = load(target["path"])
    assert len(target_data["artifacts"]) == 9
    rows = [target] + [check(row) for row in target_data["artifacts"]]
    main = next(row for row in rows if row["path"] == C + "candidate-v1.md")
    assert (main["bytes"], main["sha256"]) == (9112, MAIN_SHA)
    author_base = load(C + "baseline-v1.json")
    assert len(author_base["protected"]) == author_base["protected_paths"] == 10
    rows += [check(row) for row in author_base["protected"]]
    binding = authority()
    parent = fp(PARENT)
    assert (parent["bytes"], parent["sha256"]) == (6387, PARENT_SHA)
    parent_data = load(PARENT)
    assert len(parent_data["artifacts"]) == 11
    rows += [parent] + [check(row) for row in parent_data["artifacts"]]
    unique = {}
    for row in rows:
        assert row["path"] not in unique or unique[row["path"]] == row
        unique[row["path"]] = row
    ordered = [unique[path] for path in sorted(unique)]
    new_json("baseline-v1.json", dict(captured_at_utc=now(),
        purpose="after full mathematical reconstruction/drafting; necessary current fingerprints only",
        NEW_assigned_review_prefix_confirmed_unused=True,
        target_constructor_freeze=target, target_main=main,
        all_ten_constructor_files_and_ten_protected_records_exact=True,
        fingerprint_occurrences=len(rows), unique_paths=len(ordered),
        deduplicated_summary_sha256=digest(ordered), deduplicated_rows=ordered,
        accepted_authority=binding, compact_immediate_own_parent=parent,
        own_parent_eleven_payloads_unchanged=True,
        own_parent_historical_summary_bound_not_expanded=parent_data["current_input_summary"],
        constructor_parent_bound_transitively=target_data["compact_own_parent"],
        recursive_historical_inventory_replayed=False,
        NEW_corresponding_B_R3_file_hash_or_finding_access=False,
        mathematical_program_CAS_scan_source_author_or_freezer_rerun=False))
    print(json.dumps(dict(baseline=fp(P + "baseline-v1.json"),
        occurrences=len(rows), paths=len(ordered))))


def verify_inputs():
    base = load(P + "baseline-v1.json")
    for row in base["deduplicated_rows"]:
        check(row)
    assert digest(base["deduplicated_rows"]) == base["deduplicated_summary_sha256"]
    assert authority() == base["accepted_authority"]
    return base


def freeze():
    base = verify_inputs()
    expected = [f"{i:02}" for i in range(1, 21)]
    assert re.findall(r"^\| CC-(\d{2}) \|", raw(C + "obligations-v1.md").decode(), re.M) == expected
    issues = raw(P + "issues-v1.md").decode()
    assert re.findall(r"^\| CC-(\d{2}) \| CLOSED\.", issues, re.M) == expected
    assert re.findall(r"^\*\*R3R1-N(\d):", issues, re.M) == [str(i) for i in range(1, 6)]
    load(P + "sources-v1.json")
    new_json("metadata-v1.json", dict(recorded_at_utc=now(),
        reviewer="/root/review_2021_reasoning_j15_r2", root_NEW_constructor_excluded=True,
        NEW_R3_construction_contribution=False,
        requested_settings=dict(model="gpt-6.1-sol", reasoning="max", inherited=True),
        independently_verified_effective_settings=None,
        ENTIRE_ten_file_constructor_all20_and_all_own_artifacts_read=True,
        entire_accepted_CG_body_current_MD_JSON_source_and_integrity_read=True,
        all_new_inferences_hand_reconstructed=True,
        old_roles="old T1/component author and CP/GK/NF/FP/FS reviewer; no NEW R3 contribution or fresh self-certification",
        corresponding_NEW_B_R3_findings_files_source_code_hash_or_metadata_access=False,
        mathematical_program_CAS_scan_sample_certificate_author_source_or_freezer_rerun=False,
        only_new_metadata_code_run=True,
        no_old_shared_cache_Git_write_spawn_contact_charge_bypass_or_native_math_child=True,
        direct_telemetry=dict(observed_utc="2026-10-18 09:30:18 UTC", TOTAL_used_percent=21,
            window_minutes=10080, reset_unix=1792874445, account_suffix="1334ac3a",
            ordinary_allowed=True, legacy_by_limit_agree=True,
            explicitly_authorized_current_window_only=True, ceiling_TOTAL_percent=90,
            integration_reserve=True, automatic_later_reset_spending=False),
        completion_IDENTITY_ONLY_until_both_ENTIRE_initials_confirmed=True))
    new_json("input-validation-v1.json", dict(verified_at_utc=now(),
        administrative_only_not_mathematical_validation=True,
        all_ten_constructor_files_and_ten_protected_records_unchanged=True,
        exact_accepted_CG_candidate_suffix_and_current_authority_verified=True,
        complete_own_R16_parent_eleven_payloads_unchanged=True,
        all20_constructor_and_CLOSED_review_labels_once_in_order=True,
        five_closed_scope_note_labels_once_in_order=True,
        fingerprint_occurrences=base["fingerprint_occurrences"], unique_paths=base["unique_paths"],
        deduplicated_summary_sha256=base["deduplicated_summary_sha256"],
        no_NEW_corresponding_B_access_or_recursive_inventory_replay=True))
    artifacts = [fp(P + suffix) for suffix in PAYLOADS]
    new_json("manifest-v1.json", dict(frozen_at_utc=now(),
        status="ENTIRE initially blind WHOLE OTHER R1 review recommendation; not promotion",
        reviewer="/root/review_2021_reasoning_j15_r2", root_NEW_constructor_excluded=True,
        target_main=base["target_main"], target_constructor_freeze=base["target_constructor_freeze"],
        all20_obligations_reconstructed_and_closed=True,
        substantive_defects_found=0, required_author_repairs=0, closed_scope_notes=5,
        ENTIRE_report_ledger_source_worklog_code_ALL_metadata_complete=True,
        no_NEW_corresponding_B_review_content_or_hash_access_through_ENTIRE_freeze=True,
        old_roles_disclosed_no_fresh_self_certification=True,
        exact_scope="R3A necessary bound and R3B explicit sufficient threshold/EVERY s>=3,k>=3 only",
        general_k2_k1_full_annual_classification_or_novelty_claim=False,
        mathematical_code_CAS_scan_author_source_or_freezer_rerun=False,
        current_input_summary=dict(occurrences=base["fingerprint_occurrences"], unique_paths=base["unique_paths"],
            sha256=base["deduplicated_summary_sha256"]),
        accepted_CG_authority=base["accepted_authority"],
        compact_immediate_own_parent=base["compact_immediate_own_parent"],
        payloads=9, files_including_manifest=10, artifacts=artifacts))
    verify()


def verify():
    base = verify_inputs()
    value = load(P + "manifest-v1.json")
    assert len(value["artifacts"]) == 9
    for row in value["artifacts"]:
        check(row)
    print(json.dumps(dict(postverified=True, manifest=fp(P + "manifest-v1.json"),
        report=fp(P + "initial-v1.md"), whole_obligations=20,
        files_including_manifest=10, current_occurrences=base["fingerprint_occurrences"],
        current_paths=base["unique_paths"])))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["baseline", "freeze", "verify"])
    args = parser.parse_args()
    {"baseline": baseline, "freeze": freeze, "verify": verify}[args.operation]()
