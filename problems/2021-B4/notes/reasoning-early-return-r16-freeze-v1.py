#!/usr/bin/env python3
"""R16 metadata only: fixed bytes/JSON/suffixes/labels, never mathematical code."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2021-B4/notes/reasoning-early-return-r16-"
OWN_REVIEW = "problems/2019-B4/reviews/reasoning-critical-return-r2-review-2-manifest-v1.json"
OWN_REVIEW_SHA = "1d82777a13e1ea2a3180cdfc905844faabf00aa5a7b3d57dac4fa85cfe7c30f1"
R15 = "problems/2021-B4/notes/reasoning-unit-return-r15-freeze-v1.json"
R15_SHA = "0d2e246accd461704850f34ca056576e2f64ca6247b2fd08538c935535f77f48"
AUTH = {
    "reasoning-return-r8": "33b8713d402d09f711d0096cdc4e8c00f9e622a5335f8e3345eb4f82ba0d359d",
    "reasoning-return-r5": "f4f088adc133b0581520488cdbba30082c13b2402c96ae555142e5491ad4137d",
}
CONTEXT = [
    "problems/2021-B4/proofs/reviewed-reasoning-return-r12-v1.1.md",
    "problems/2021-B4/proofs/reviewed-reasoning-return-r13-v1.1.md",
    "problems/2021-B4/proofs/reviewed-reasoning-return-r14-v1.1.md",
    "problems/2021-B4/proofs/reviewed-reasoning-return-r10-v1.1.md",
    "problems/2021-B4/notes/reasoning-return-r8-sources-v1.json",
    "problems/2021-B4/notes/reasoning-return-r14-source-audit-v1.md",
]
PAYLOADS = ["candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "hand-checks-v1.md", "failed-routes-v1.md", "sources-v1.md", "sources-v1.json",
    "worklog-v1.md", "freeze-v1.py", "baseline-v1.json", "input-validation-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert not path.startswith("problems/2024-B4/reviews/cofactor-cubic-r3-review-")
    assert not path.startswith("problems/2024-B4/notes/cofactor-cubic-r3-")
    assert not path.startswith("problems/2021-B4/reviews/reasoning-unit-return-r15-review-")
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


def authorities():
    bindings, rows = [], []
    for stem, expected in AUTH.items():
        path = f"problems/2021-B4/reviews/{stem}-acceptance.json"
        value = load(path)
        assert value["unresolved_substantive_issues"] == 0
        assert value["repair_required"] is False
        proof, candidate = check(value["accepted_copy"]), check(value["candidate"])
        assert proof["sha256"] == expected
        assert raw(proof["path"]).endswith(raw(candidate["path"]))
        rows += [proof, candidate, fp(path), fp(path[:-5] + ".md")]
        bindings.append(dict(authority=fp(path), accepted_copy=proof,
            exact_candidate_suffix=candidate,
            historical_occurrences_bound_not_replayed=value["record_occurrences_verified"],
            historical_paths_bound_not_replayed=value["unique_paths_verified"]))
    return bindings, rows


def baseline():
    rows = [fp("AGENTS.md"), fp("problems/2021-B4/statement.md")]
    bindings, declared = authorities()
    rows += declared + [fp(path) for path in CONTEXT]
    parent = fp(OWN_REVIEW)
    assert (parent["bytes"], parent["sha256"]) == (6974, OWN_REVIEW_SHA)
    parent_data = load(OWN_REVIEW)
    assert len(parent_data["artifacts"]) == 9
    rows += [parent] + [check(row) for row in parent_data["artifacts"]]
    old_r15 = fp(R15)
    assert (old_r15["bytes"], old_r15["sha256"]) == (6170, R15_SHA)
    r15_data = load(R15)
    assert len(r15_data["artifacts"]) == 10
    assert r15_data["status"].startswith("candidate proof - unverified")
    rows += [old_r15] + [check(row) for row in r15_data["artifacts"]]
    unique = {}
    for row in rows:
        assert row["path"] not in unique or unique[row["path"]] == row
        unique[row["path"]] = row
    ordered = [unique[path] for path in sorted(unique)]
    new_json("baseline-v1.json", dict(captured_at_utc=now(),
        purpose="after mathematical reconstruction/drafting, before freeze; necessary current fingerprints only",
        NEW_assigned_prefix_confirmed_unused=True, accepted_authorities=bindings,
        fingerprint_occurrences=len(rows), unique_paths=len(ordered),
        deduplicated_summary_sha256=digest(ordered), deduplicated_rows=ordered,
        immediate_own_review_parent=parent,
        own_review_nine_payloads_verified_unchanged=True,
        own_review_historical_summary_bound_not_expanded=parent_data["current_input_summary"],
        own_R15_UNVERIFIED_not_premise=old_r15,
        own_R15_ten_payloads_verified_unchanged=True,
        own_R15_historical_summary_bound_not_expanded=r15_data["current_input_summary"],
        recursive_historical_inventory_replayed=False,
        new_R15_peer_or_queued2024_material_opened=False,
        no_mathematical_executable_CAS_scan_source_author_or_freezer_rerun=True))
    print(json.dumps(dict(baseline=fp(P + "baseline-v1.json"),
        occurrences=len(rows), paths=len(ordered))))


def verify_inputs():
    base = load(P + "baseline-v1.json")
    for row in base["deduplicated_rows"]:
        check(row)
    assert digest(base["deduplicated_rows"]) == base["deduplicated_summary_sha256"]
    bindings, unused = authorities()
    assert bindings == base["accepted_authorities"]
    return base


def freeze():
    base = verify_inputs()
    expected = [str(i) for i in range(1, 57)]
    for suffix in ("obligations-v1.md", "constructor-checks-v1.md"):
        assert re.findall(r"^(\d+)\. ", raw(P + suffix).decode(), re.M) == expected
    load(P + "sources-v1.json")
    main = raw(P + "candidate-v1.md").decode()
    for claim in ("R16A", "R16B", "R16C"):
        assert f"**{claim}," in main
    new_json("input-validation-v1.json", dict(verified_at_utc=now(),
        administrative_only_not_mathematical_validation=True,
        fingerprint_occurrences=base["fingerprint_occurrences"], unique_paths=base["unique_paths"],
        deduplicated_summary_sha256=base["deduplicated_summary_sha256"],
        two_direct_accepted_body_candidate_suffixes_exact=True,
        complete_R15_and_own_review_parents_unchanged=True,
        all56_obligation_and_constructor_check_labels_once_in_order=True,
        no_recursive_historical_replay_or_old_bytes_changed=True,
        no_mathematical_executable_or_author_source_freezer_rerun=True))
    artifacts = [fp(P + suffix) for suffix in PAYLOADS]
    new_json("freeze-v1.json", dict(frozen_at_utc=now(),
        status="candidate proof - unverified; ENTIRE R16A-C constructor checkpoint",
        constructor="/root/review_2021_reasoning_j15_r2",
        constructor_excluded_from_independent_review_count=True,
        all56_obligations_constructor_checks_and_entire_packet_complete=True,
        TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_and_full_root_reconciliation_required=True,
        requested_settings=dict(model="gpt-6.1-sol", reasoning="max", inherited=True),
        independently_verified_effective_settings=None,
        root_or_other_worker_supplied_NEW_R16_inference=False,
        old_roles_disclosed_no_fresh_self_recertification=True,
        proposed_actual_m4_cubic_exclusion_at_all_allowed_depths=True,
        Qstar_global_H11_unit_and_actual_a9_depth_claim=True,
        quartic_contact_claim_retains_EXTRA_unit_a8_and_actual_noncenter_hypotheses=True,
        EC_T4_m3_fullm4_J15_degree20_annual_lift_or_novelty_exclusion=False,
        R15_status_UNVERIFIED_not_premise=True,
        new_R15_peer_or_queued2024_material_opened=False,
        no_mathematical_executable_CAS_scan_certificate_generator_author_or_source_rerun=True,
        hand_certificates_proof_critical_not_routine_enlarged_mask_tables=True,
        no_Git_shared_old_cache_write_spawn_contact_charge_or_bypass=True,
        authoritative_weekly_telemetry=dict(observed_utc="2026-10-18 09:18:09 UTC",
            method="direct get_usage_limits plus clock in same awaited batch",
            TOTAL_used_percent=20, window_minutes=10080, reset_unix=1792874445,
            ordinary_allowed=True, legacy_by_limit_agree=True, account_suffix="1334ac3a",
            explicitly_authorized_current_window_only=True, ceiling_TOTAL_percent=90,
            integration_reserve=True, automatic_later_reset_spending=False),
        current_input_summary=dict(occurrences=base["fingerprint_occurrences"], unique_paths=base["unique_paths"],
            sha256=base["deduplicated_summary_sha256"]),
        compact_immediate_own_review_parent=base["immediate_own_review_parent"],
        compact_own_UNVERIFIED_R15_parent=base["own_R15_UNVERIFIED_not_premise"],
        accepted_authorities=base["accepted_authorities"],
        payloads=11, files_including_freeze=12, artifacts=artifacts))
    verify()


def verify():
    base = verify_inputs()
    value = load(P + "freeze-v1.json")
    assert len(value["artifacts"]) == 11
    for row in value["artifacts"]:
        check(row)
    print(json.dumps(dict(postverified=True, freeze=fp(P + "freeze-v1.json"),
        main=fp(P + "candidate-v1.md"), whole_obligations=56,
        files_including_freeze=12, current_occurrences=base["fingerprint_occurrences"],
        current_paths=base["unique_paths"])))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["baseline", "freeze", "verify"])
    args = parser.parse_args()
    {"baseline": baseline, "freeze": freeze, "verify": verify}[args.operation]()
