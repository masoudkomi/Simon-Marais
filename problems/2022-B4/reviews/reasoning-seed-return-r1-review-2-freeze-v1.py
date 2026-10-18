#!/usr/bin/env python3
"""SR R2 metadata-only preservation. No mathematical execution or author rerun."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2022-B4/reviews/reasoning-seed-return-r1-review-2-"
C = "problems/2022-B4/notes/reasoning-seed-return-r1-"
FORBIDDEN = "problems/2022-B4/reviews/reasoning-seed-return-r1-review-1-"
CONSTRUCTOR_SHA = "78beb6e2f0f2ce43c51029f68bd42da1e9693cbcde63fa71c1d5df881443dccc"
CANDIDATE_SHA = "a1caa31a57496ff17daaa78d8a085d9423801d2935a3476559c963b6c03f2584"
PARENT = "problems/2021-B4/notes/reasoning-unit-return-r15-freeze-v1.json"
PARENT_SHA = "0d2e246accd461704850f34ca056576e2f64ca6247b2fd08538c935535f77f48"
PAYLOADS = ["initial-v1.md", "issues-v1.md", "sources-v1.md", "sources-v1.json", "worklog-v1.md", "freeze-v1.py", "baseline-v1.json", "metadata-v1.json", "input-validation-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert not path.startswith(FORBIDDEN), "NEW peer SR review is forbidden"
    return (ROOT / path).read_bytes()


def fp(path):
    data = raw(path)
    return dict(path=path, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def load(path):
    return json.loads(raw(path))


def check(row):
    expected = {key: row[key] for key in ("path", "bytes", "sha256")}
    assert fp(expected["path"]) == expected, expected["path"]
    return expected


def digest(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def new_json(suffix, obj):
    path = P + suffix
    assert path.startswith(P)
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(obj, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def check_authorities():
    bindings = []
    for stem, expected_sha in [
        ("reasoning-return-r5", "1a2544cb8ced3bba9cc6efed1870c242c652b3e6029f39881028d4637d7c6da6"),
        ("reasoning-complexity-return-r9-v3", "18e681d69b29d3495fea0cc2a29dbcb8a9c34db60644b981b3f653d666bef4ad"),
    ]:
        path = f"problems/2022-B4/reviews/{stem}-acceptance.json"
        authority = load(path)
        assert authority["unresolved_substantive_issues"] == 0
        assert authority["repair_required"] is False
        candidate, proof = check(authority["candidate"]), check(authority["accepted_copy"])
        assert proof["sha256"] == expected_sha
        assert raw(proof["path"]).endswith(raw(candidate["path"]))
        bindings.append(dict(authority=fp(path), accepted_copy=proof,
            exact_candidate_suffix=candidate,
            historical_occurrences_bound_not_replayed=authority["record_occurrences_verified"],
            historical_paths_bound_not_replayed=authority["unique_paths_verified"]))
    return bindings


def baseline():
    freeze_path = C + "freeze-v1.json"
    freeze_row = fp(freeze_path)
    assert (freeze_row["bytes"], freeze_row["sha256"]) == (3871, CONSTRUCTOR_SHA)
    constructor = load(freeze_path)
    assert constructor["whole_obligations"] == 48
    rows = [freeze_row] + [check(row) for row in constructor["artifacts"]]
    assert len(constructor["artifacts"]) == 9
    main = next(row for row in rows if row["path"] == C + "candidate-v1.md")
    assert (main["bytes"], main["sha256"]) == (21030, CANDIDATE_SHA)

    source_baseline = load(C + "baseline-v1.json")
    direct = source_baseline["protected_direct_records"]
    summary = source_baseline["summary"]
    assert len(direct) == summary["unique_paths"] == 41
    assert digest(direct) == summary["canonical_record_array_sha256"]
    rows += [check(row) for row in direct]
    assert summary == constructor["direct_fingerprint_summary"]
    source_bindings = check_authorities()

    parent = fp(PARENT)
    assert (parent["bytes"], parent["sha256"]) == (6170, PARENT_SHA)
    parent_manifest = load(PARENT)
    rows += [parent] + [check(row) for row in parent_manifest["artifacts"]]
    assert len(parent_manifest["artifacts"]) == 10
    unique = {}
    for row in rows:
        assert row["path"] not in unique or unique[row["path"]] == row
        unique[row["path"]] = row
    deduplicated = [unique[path] for path in sorted(unique)]
    new_json("baseline-v1.json", dict(
        captured_at_utc=now(), operation="metadata-only exact bytes/SHA; NO mathematics",
        target_constructor_freeze=freeze_row, target_main=main,
        all_constructor_ten_files_and_all41_declared_direct_fingerprints_checked=True,
        fingerprint_occurrences=len(rows), unique_paths=len(deduplicated),
        deduplicated_summary_sha256=digest(deduplicated), deduplicated_rows=deduplicated,
        accepted_authorities=source_bindings,
        compact_immediate_own_parent=parent,
        own_parent_ten_payloads_unchanged=True,
        own_parent_historical_summary_bound_not_recursively_replayed=parent_manifest["current_input_summary"],
        constructor_immediate_parent_bound_transitively=constructor["compact_immediate_own_parent"],
        recursive_historical_inventory_copy_or_rehash=False,
        new_assigned_review_prefix_confirmed_unused=True,
        corresponding_NEW_root_SR_R1_file_content_or_hash_access=False,
        mathematical_program_CAS_scan_author_or_freezer_rerun=False))
    print(json.dumps(dict(baseline=fp(P + "baseline-v1.json"), occurrences=len(rows), unique_paths=len(deduplicated))))


def verify_inputs():
    base = load(P + "baseline-v1.json")
    for row in base["deduplicated_rows"]:
        check(row)
    assert digest(base["deduplicated_rows"]) == base["deduplicated_summary_sha256"]
    assert check_authorities() == base["accepted_authorities"]
    return base


def freeze():
    base = verify_inputs()
    expected = [f"SR-O{i:02d}" for i in range(1, 49)]
    assert re.findall(r"^\|(SR-O\d\d)\|", raw(C + "obligations-v1.md").decode(), re.M) == expected
    assert re.findall(r"^\| (SR-O\d\d) \| CLOSED\.", raw(P + "issues-v1.md").decode(), re.M) == expected
    notes = re.findall(r"^\*\*SR2-N(\d):", raw(P + "issues-v1.md").decode(), re.M)
    assert notes == [str(i) for i in range(1, 8)]
    load(P + "sources-v1.json")
    new_json("metadata-v1.json", dict(
        recorded_at_utc=now(), reviewer="/root/review_2021_reasoning_j15_r2",
        nonconstructor_of_NEW_SR=True, requested_settings=dict(model="gpt-6.1-sol", reasoning="max", inherited=True),
        independently_verified_effective_settings=None,
        whole_reconstruction="ENTIRE SR1A/SR1B/SR2/SR3/SR4 and all48 obligations",
        both_ordinary_directions_and_all_endpoint_exit_groups_hand_checked=True,
        all_constructor_main_companions_code_and_ALL_metadata_read=True,
        all_operative_F5_Q_accepted_bodies_and_authorities_read=True,
        primary_read_limits_in_source_companions=True,
        prior_roles="A OLD F5/Q and other whole reviews/R6 construction, not NEW SR contribution or fresh self-certification",
        corresponding_NEW_root_SR_R1_file_finding_ledger_source_code_or_hash_access_before_ENTIRE_freeze=False,
        root_sent_completion_identity_only=True,
        mathematical_program_CAS_scan_sample_certificate_author_or_freezer_rerun=False,
        only_metadata_code_run=True,
        no_Git_old_shared_cache_write_spawn_charge_contact_or_bypass=True,
        direct_telemetry=dict(observed_utc="2026-10-18 08:53:31 UTC", TOTAL_used_percent=19,
            window_minutes=10080, reset_unix=1792874445, ordinary_allowed=True,
            legacy_by_limit_agree=True, account_suffix="1334ac3a", current_window_explicitly_authorized=True,
            ceiling_TOTAL_percent=90, reserve=True, automatic_later_week_spending=False),
        completion_identity_only_until_both_ENTIRE_initials_confirmed=True))
    new_json("input-validation-v1.json", dict(
        verified_at_utc=now(), administrative_only_not_mathematical_validation=True,
        target_ten_file_constructor_unchanged=True, all41_constructor_direct_fingerprints_exact=True,
        own_R15_parent_and_ten_payloads_unchanged=True,
        fingerprint_occurrences=base["fingerprint_occurrences"], unique_paths=base["unique_paths"],
        deduplicated_summary_sha256=base["deduplicated_summary_sha256"],
        accepted_F5_Q_body_candidate_suffixes_exact=True,
        all48_ledger_labels_closed_once_in_order=True, seven_scope_note_labels_once_in_order=True,
        text_label_checks_do_not_prove_mathematics=True,
        no_recursive_historical_inventory_replay=True, no_NEW_corresponding_peer_access=True))
    artifacts = [fp(P + suffix) for suffix in PAYLOADS]
    new_json("manifest-v1.json", dict(
        frozen_at_utc=now(), status="ENTIRE initially blind WHOLE nonconstructor review recommendation; not promotion",
        reviewer="/root/review_2021_reasoning_j15_r2", new_constructor_excluded=True,
        target_constructor_freeze=base["target_constructor_freeze"], target_main=base["target_main"],
        all48_author_obligations_independently_closed=True,
        substantive_defects_found=0, author_repairs_required=0, closed_scope_notes=7,
        all_main_ledger_source_worklog_code_ALL_metadata_complete=True,
        peer_blindness_through_ENTIRE_initial_freeze=True,
        prior_roles_disclosed_no_fresh_old_self_certification=True,
        no_mathematical_computation_or_author_rerun=True,
        exact_scope="SR1A/SR1B/SR2/SR3/SR4 partials only; no infinite official survivor, universal hitting, fiber existence/exclusion or novelty",
        current_input_summary=dict(occurrences=base["fingerprint_occurrences"], unique_paths=base["unique_paths"], sha256=base["deduplicated_summary_sha256"]),
        compact_immediate_own_parent=base["compact_immediate_own_parent"],
        historical_accepted_authorities_bound_not_replayed=base["accepted_authorities"],
        payloads=9, files_including_manifest=10, artifacts=artifacts))
    verify()


def verify():
    base = verify_inputs()
    manifest = load(P + "manifest-v1.json")
    for row in manifest["artifacts"]:
        check(row)
    print(json.dumps(dict(postverified=True, manifest=fp(P + "manifest-v1.json"),
        report=fp(P + "initial-v1.md"), whole_obligations=48,
        review_files_including_manifest=10, current_occurrences=base["fingerprint_occurrences"],
        current_paths=base["unique_paths"])))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["baseline", "freeze", "verify"])
    args = parser.parse_args()
    {"baseline": baseline, "freeze": freeze, "verify": verify}[args.operation]()
