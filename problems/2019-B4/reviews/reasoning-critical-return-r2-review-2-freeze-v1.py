#!/usr/bin/env python3
"""Metadata-only CR R2 preservation: no math, scan, source or author execution."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2019-B4/reviews/reasoning-critical-return-r2-review-2-"
C = "problems/2019-B4/notes/reasoning-critical-return-r2-"
PEER = "problems/2019-B4/reviews/reasoning-critical-return-r2-review-1-"
PARENT = "problems/2022-B4/reviews/reasoning-seed-return-r1-review-2-manifest-v1.json"
PARENT_SHA = "2ad1045496a16ec6c8d6f9fb0afbc22fda10abd318e91e17eaf399303c853f0c"
TARGET_SHA = "295feae2d5671960ad9d9ae3456abcd94850a2c2faec0ce42e024eb5d05b18c9"
MAIN_SHA = "1d672cc4eafde68da5d83cd4997dbee1a4e5274e4858bafbbc63479cc01b3de7"
AUTH = {
    "reasoning-return-r7": "4fe222b8b1d89b6b3d66bb16c6a1985390d537eee55bb42bfefdb2d4821e351a",
    "monotone-ratio": "a87798e4df63ec2f76e83da9750f811b15fc6702533b4ca68bd8bd973ac3bac9",
    "reasoning-growth-return-r1": "c43a76227937eb11ff8261cc34cece7a411f6637fc4794336c3161f05ba11ea3",
    "walk-Frechet": "c068f531fa9fa3c420867ae898291b6034cef7511e72ec6fd16f20ac3b023f44",
}
PAYLOADS = ["initial-v1.md", "issues-v1.md", "sources-v1.md", "sources-v1.json", "worklog-v1.md", "freeze-v1.py", "baseline-v1.json", "metadata-v1.json", "input-validation-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert not path.startswith(PEER), "NEW corresponding peer review access forbidden"
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
    path = P + suffix
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def authorities():
    result, extra = [], []
    for stem, expected in AUTH.items():
        path = f"problems/2019-B4/reviews/{stem}-acceptance.json"
        value = load(path)
        assert value["unresolved_substantive_issues"] == 0
        assert value["repair_required"] is False
        proof, candidate = check(value["accepted_copy"]), check(value["candidate"])
        assert proof["sha256"] == expected
        assert raw(proof["path"]).endswith(raw(candidate["path"]))
        extra += [candidate, fp(path[:-5] + ".md")]
        result.append(dict(authority=fp(path), accepted_copy=proof, exact_candidate_suffix=candidate,
            historical_occurrences_bound_not_replayed=value["record_occurrences_verified"],
            historical_paths_bound_not_replayed=value["unique_paths_verified"]))
    second_path = "problems/2019-B4/reviews/secondpass-acceptance.json"
    second = load(second_path)
    wanted_paths = ["proofs/reviewed-secondpass-v1.1.md", "notes/secondpass-canonical-renewal.md",
        "notes/secondpass-rigidity-obstructions.md", "notes/secondpass-staircases-and-pumping.md"]
    linked = []
    for relative in wanted_paths:
        row = fp("problems/2019-B4/" + relative)
        assert row["sha256"] == second["artifacts"][relative]
        linked.append(row)
    md = fp("problems/2019-B4/reviews/secondpass-acceptance.md")
    assert md["sha256"] == second["artifacts"]["reviews/secondpass-acceptance.md"]
    extra += [md]
    return result, linked, extra


def baseline():
    target = fp(C + "freeze-v1.json")
    assert (target["bytes"], target["sha256"]) == (6949, TARGET_SHA)
    manifest = load(target["path"])
    assert len(manifest["artifacts"]) == 10
    rows = [target] + [check(row) for row in manifest["artifacts"]]
    main = next(row for row in rows if row["path"] == C + "candidate-v1.md")
    assert (main["bytes"], main["sha256"]) == (22291, MAIN_SHA)
    declared = load(C + "baseline-v1.json")
    assert len(declared["protected"]) == declared["protected_unique_paths"] == 19
    assert digest(declared["protected"]) == declared["canonical_protected_summary_sha256"]
    rows += [check(row) for row in declared["protected"]]
    bindings, linked, extra = authorities()
    rows += extra
    parent = fp(PARENT)
    assert (parent["bytes"], parent["sha256"]) == (5215, PARENT_SHA)
    parent_record = load(PARENT)
    rows += [parent] + [check(row) for row in parent_record["artifacts"]]
    assert len(parent_record["artifacts"]) == 9
    unique = {}
    for row in rows:
        assert row["path"] not in unique or unique[row["path"]] == row
        unique[row["path"]] = row
    ordered = [unique[path] for path in sorted(unique)]
    new_json("baseline-v1.json", dict(captured_at_utc=now(),
        purpose="necessary direct fingerprints and compact immutable parent; integrity only",
        target_constructor_freeze=target, target_main=main,
        entire_constructor_eleven_files_and_all19_declared_inputs_checked=True,
        fingerprint_occurrences=len(rows), unique_paths=len(ordered),
        deduplicated_summary_sha256=digest(ordered), deduplicated_rows=ordered,
        accepted_authorities=bindings, secondpass_linked_declarations_exact=linked,
        compact_immediate_own_parent=parent, own_parent_nine_payloads_unchanged=True,
        own_parent_historical_summary_bound_not_expanded=parent_record["current_input_summary"],
        constructor_parent_bound_transitively=manifest["immediate_own_parent"],
        recursive_historical_inventory_replayed=False, NEW_prefix_confirmed_unused=True,
        corresponding_NEW_root_CR_R1_file_or_hash_access=False,
        mathematical_program_CAS_scan_author_or_freezer_rerun=False))
    print(json.dumps(dict(baseline=fp(P + "baseline-v1.json"), occurrences=len(rows), paths=len(ordered))))


def verify_inputs():
    value = load(P + "baseline-v1.json")
    for row in value["deduplicated_rows"]:
        check(row)
    assert digest(value["deduplicated_rows"]) == value["deduplicated_summary_sha256"]
    bindings, linked, extra = authorities()
    assert bindings == value["accepted_authorities"]
    assert linked == value["secondpass_linked_declarations_exact"]
    return value


def freeze():
    base = verify_inputs()
    for suffix in ("obligations-v1.md", "constructor-checks-v1.md"):
        assert re.findall(r"^(\d+)\. ", raw(C + suffix).decode(), re.M) == [str(i) for i in range(1, 61)]
    issues = raw(P + "issues-v1.md").decode()
    assert re.findall(r"^\| (CR-O\d\d) \| CLOSED\.", issues, re.M) == [f"CR-O{i:02d}" for i in range(1, 61)]
    assert re.findall(r"^\*\*CR2-N(\d):", issues, re.M) == [str(i) for i in range(1, 7)]
    load(P + "sources-v1.json")
    new_json("metadata-v1.json", dict(recorded_at_utc=now(),
        reviewer="/root/review_2021_reasoning_j15_r2", nonconstructor_of_NEW_CR=True,
        requested_settings=dict(model="gpt-6.1-sol", reasoning="max", inherited=True),
        independently_verified_effective_settings=None,
        ENTIRE_main_all60_ledger_sources_failures_checks_log_code_ALL_metadata_read=True,
        full_operative_accepted_bodies_and_current_authorities_read=True,
        all_new_inferences_hand_reconstructed=True,
        prior_roles="A OLD R7/NR construction, MR/G/DG and other reviews; not NEW CR contribution or fresh old self-certification",
        corresponding_NEW_root_CR_R1_findings_files_source_code_or_hash_access_before_ENTIRE_freeze=False,
        mathematical_program_CAS_scan_sample_finite_certificate_author_or_freezer_rerun=False,
        only_metadata_code_run=True, no_native_math_child_or_pending_approval=True,
        no_old_shared_cache_Git_write_spawn_contact_charge_or_bypass=True,
        direct_telemetry=dict(observed_utc="2026-10-18 09:04:53 UTC", TOTAL_used_percent=20,
            window_minutes=10080, reset_unix=1792874445, account_suffix="1334ac3a",
            ordinary_allowed=True, legacy_by_limit_agree=True,
            explicitly_authorized_current_window_only=True, ceiling_TOTAL_percent=90,
            integration_reserve=True, automatic_later_reset_spending=False),
        completion_identity_only_until_both_ENTIRE_initials_confirmed=True))
    new_json("input-validation-v1.json", dict(verified_at_utc=now(),
        administrative_only_not_mathematical_validation=True,
        entire_constructor_eleven_files_unchanged=True, all19_declared_direct_inputs_exact=True,
        four_accepted_candidate_copy_suffixes_exact=True,
        secondpass_register_and_three_linked_hashes_exact=True,
        immediate_own_parent_and_nine_payloads_unchanged=True,
        all60_obligations_constructor_labels_and_closed_review_labels_once_in_order=True,
        six_scope_note_labels_once_in_order=True,
        fingerprint_occurrences=base["fingerprint_occurrences"], unique_paths=base["unique_paths"],
        deduplicated_summary_sha256=base["deduplicated_summary_sha256"],
        no_NEW_corresponding_peer_access=True, no_recursive_historical_replay=True))
    artifacts = [fp(P + suffix) for suffix in PAYLOADS]
    new_json("manifest-v1.json", dict(frozen_at_utc=now(),
        status="ENTIRE initially blind WHOLE nonconstructor review recommendation; not promotion",
        reviewer="/root/review_2021_reasoning_j15_r2", constructor_B_excluded=True,
        target_constructor_freeze=base["target_constructor_freeze"], target_main=base["target_main"],
        all60_obligations_reconstructed_and_closed=True, substantive_defects_found=0,
        required_author_repairs=0, closed_scope_notes=6,
        entire_report_ledger_sources_worklog_code_ALL_metadata_complete=True,
        no_corresponding_NEW_peer_access_through_ENTIRE_initial_freeze=True,
        old_roles_disclosed_no_fresh_old_self_certification=True,
        exact_scope="CR1--CR5 only; actual contexts, stated tilted/random-length measures, exact feasible-cut fibers and conditional regime consequences; cut NUMBER bridge remains open",
        no_actual_regime_exact_lambda_numeric_improvement_annual_or_priority_claim=True,
        no_mathematical_code_CAS_scan_author_or_freezer_rerun=True,
        current_input_summary=dict(occurrences=base["fingerprint_occurrences"], unique_paths=base["unique_paths"], sha256=base["deduplicated_summary_sha256"]),
        compact_immediate_own_parent=base["compact_immediate_own_parent"],
        accepted_authorities_bound_not_recursively_expanded=base["accepted_authorities"],
        payloads=9, files_including_manifest=10, artifacts=artifacts))
    verify()


def verify():
    base = verify_inputs()
    value = load(P + "manifest-v1.json")
    for row in value["artifacts"]:
        check(row)
    print(json.dumps(dict(postverified=True, manifest=fp(P + "manifest-v1.json"),
        report=fp(P + "initial-v1.md"), whole_obligations=60,
        files_including_manifest=10, current_occurrences=base["fingerprint_occurrences"],
        current_paths=base["unique_paths"])))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["baseline", "freeze", "verify"])
    args = parser.parse_args()
    {"baseline": baseline, "freeze": freeze, "verify": verify}[args.operation]()
