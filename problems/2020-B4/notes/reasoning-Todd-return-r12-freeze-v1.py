#!/usr/bin/env python3
"""Todd R12 preservation only: no mathematical algorithms or tests."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2020-B4/notes/reasoning-Todd-return-r12-"
PARENT = "problems/2021-B4/reviews/reasoning-early-return-r16-review-2-manifest-v1.json"
PARENT_SHA = "49dc167e24c9f2a9ac156ad690e8c34c71c7bddddd4126d37e8f76e39570f1b9"
AUTHORITIES = [
    ("reasoning-arithmetic-return-r11", "d40873d12db5edb0870867e392fcc2d547f9bc68f19a4cc73a389ac951245079", "comparison"),
    ("reasoning-return-r8", "9003af18926d1fe49d3f997b40ed070ceefa37e42f73c5a98c32bbe7a2f3bfcb", "operative"),
    ("reasoning-arithmetic-return-r9", "ab2ee4e7a2dcfa464780c6144f996d683f08b7f04da63d2a77ee2fdd4ec922b8", "operative"),
    ("reasoning-return-r7", "7517c6ffd5aff1135107020f9526922203496415515afb4bbd07176fb445d479", "operative"),
    ("reasoning-arithmetic-return-r10", "dc540eef45a7c4054191a0fd9e723aa64e364163f04bf696450025ca3ca45f24", "background_only"),
]
OLD_FILES = [
    "problems/2020-B4/notes/reasoning-arithmetic-return-r11-failed-routes-v1.md",
    "problems/2020-B4/notes/reasoning-arithmetic-return-r11-sources-v1.md",
    "problems/2020-B4/notes/reasoning-return-r8-failed-routes-v1.md",
    "problems/2020-B4/notes/reasoning-arithmetic-return-r9-failed-routes-v1.md",
    "problems/2020-B4/notes/reasoning-arithmetic-return-r10-failed-routes-v1.md",
]
PAYLOADS = ["candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "failed-routes-v1.md", "sources-v1.md", "sources-v1.json", "worklog-v1.md",
    "freeze-v1.py", "baseline-v1.json", "input-validation-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert not path.startswith("problems/2024-B4/reviews/cofactor-Frobenius-r5-review-")
    assert not path.startswith("problems/2024-B4/notes/cofactor-Frobenius-r5-")
    assert not path.startswith("problems/2021-B4/reviews/reasoning-early-return-r16-review-1-")
    return (ROOT / path).read_bytes()


def fp(path):
    value = raw(path)
    return dict(path=path, bytes=len(value), sha256=hashlib.sha256(value).hexdigest())


def obj(path):
    return json.loads(raw(path))


def check(row):
    wanted = {key: row[key] for key in ("path", "bytes", "sha256")}
    assert fp(wanted["path"]) == wanted, wanted["path"]
    return wanted


def digest(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def put(suffix, data):
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def authorities():
    bindings, rows = [], []
    for stem, expected, role in AUTHORITIES:
        path = f"problems/2020-B4/reviews/{stem}-acceptance.json"
        value = obj(path)
        assert value["unresolved_substantive_issues"] == 0
        assert value["repair_required"] is False
        body, candidate = check(value["accepted_copy"]), check(value["candidate"])
        assert body["sha256"] == expected
        assert raw(body["path"]).endswith(raw(candidate["path"]))
        rows += [fp(path), fp(path[:-5] + ".md"), body, candidate]
        bindings.append(dict(authority=fp(path), accepted_body=body,
            exact_candidate_suffix=candidate, role=role,
            historical_fingerprint_occurrences_bound_not_replayed=value["record_occurrences_verified"],
            historical_paths_bound_not_replayed=value["unique_paths_verified"]))
    return bindings, rows


def baseline():
    bindings, rows = authorities()
    rows += [fp("AGENTS.md"), fp("problems/2020-B4/statement.md")]
    rows += [fp(path) for path in OLD_FILES]
    parent = fp(PARENT)
    assert (parent["bytes"], parent["sha256"]) == (6643, PARENT_SHA)
    previous = obj(PARENT)
    assert previous["older_plus_new_own_paths_bound_transitively"] == 666
    assert len(previous["artifacts"]) == 9
    rows += [parent] + [check(row) for row in previous["artifacts"]]
    unique = {}
    for row in rows:
        assert row["path"] not in unique or unique[row["path"]] == row
        unique[row["path"]] = row
    ordered = [unique[k] for k in sorted(unique)]
    contexts = [fp("problems/2020-B4/research.md"), fp("problems/2020-B4/references.md")]
    put("baseline-v1.json", dict(captured_at_utc=now(),
        administrative_only_not_mathematical_validation=True,
        assigned_prefix_confirmed_unused_before_first_write=True,
        necessary_fingerprint_occurrences=len(rows), protected_unique_paths=len(ordered),
        canonical_protected_summary_sha256=digest(ordered), protected_rows=ordered,
        accepted_authorities=bindings,
        mutable_context_snapshots_not_operative_or_immutability_guards=contexts,
        immediate_own_parent=parent, parent_nine_payloads_verified_unchanged=True,
        older_own_paths_bound_transitively=666,
        previous_parent_current_summary_bound_without_recursion=dict(
            occurrences=previous["protected_fingerprint_occurrences"],
            paths=previous["protected_unique_paths"],
            sha256=previous["canonical_protected_summary_sha256"]),
        no_historical_inventory_recopy_or_recursive_replay=True,
        no_corresponding_NEW_peer_Todd_or_queued2024R5_review_material_accessed=True))
    print(json.dumps(dict(baseline=fp(P + "baseline-v1.json"), current_paths=len(ordered))))


def verify_inputs():
    base = obj(P + "baseline-v1.json")
    for row in base["protected_rows"]:
        check(row)
    assert digest(base["protected_rows"]) == base["canonical_protected_summary_sha256"]
    assert authorities()[0] == base["accepted_authorities"]
    return base


def freeze():
    base = verify_inputs()
    expected = [str(i) for i in range(1, 73)]
    for suffix in ("obligations-v1.md", "constructor-checks-v1.md"):
        assert re.findall(r"^(\d+)\. ", raw(P + suffix).decode(), re.M) == expected
    main = raw(P + "candidate-v1.md").decode()
    assert "Candidate proof - unverified" in main
    for i in range(1, 6):
        assert f"**TD{i}," in main
    source = obj(P + "sources-v1.json")
    assert source["whole_obligations"] == 72
    put("input-validation-v1.json", dict(verified_at_utc=now(),
        administrative_only_not_mathematical_validation=True,
        necessary_fingerprint_occurrences=base["necessary_fingerprint_occurrences"],
        protected_unique_paths=base["protected_unique_paths"],
        canonical_protected_summary_sha256=base["canonical_protected_summary_sha256"],
        all_five_current_accepted_body_candidate_suffixes_exact=True,
        all72_obligation_and_constructor_check_labels_once_in_order=True,
        immediate_own_parent_nine_payloads_unchanged=True,
        mutable_context_not_falsely_asserted_immutable=True,
        no_mathematical_executable_CAS_scan_source_author_or_certificate_rerun=True,
        no_historical_inventory_recopy_or_recursive_replay=True))
    put("freeze-v1.json", dict(frozen_at_utc=now(),
        status="candidate proof - unverified; ENTIRE TD1-TD5 constructor checkpoint",
        constructor="/root/review_2022_complexity_r2", constructor_excluded=True,
        requested_settings=dict(model="gpt-6.1-sol", reasoning="max", inherited=True),
        independently_verified_effective_settings=None,
        TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_and_coordinator_reconciliation_required=True,
        whole_obligations=72, entire_candidate_sources_failures_log_code_metadata_complete=True,
        root_NEW_inference_contribution=False, other_worker_NEW_inference_contribution=False,
        old_roles_disclosed_not_fresh_self_recertification=True,
        proposed_canonical_relative_class_retains_even_class_unit_defect=True,
        proposed_parity_free_exact_interval_at_original_norm_q=True,
        proposed_exact_actual_sign_cube_and_fixed_even_slice_counts=True,
        proposed_actual_primary_minimal_zero_sum_all_positive_exponents=True,
        actual_new_q_small_H_instance_or_class_size_upper_bound_verified=False,
        automatic_even_class_correction_or_entire_polarized_group_identification=False,
        full_taut_annual_classification_composite_assembler_or_priority_claim=False,
        no_mathematical_executable_CAS_scan_class_computation_tests_author_or_source_rerun=True,
        no_old_shared_Git_cache_write_spawn_contact_charge_or_bypass=True,
        no_corresponding_NEW_peer_Todd_or_queued2024R5_review_material_accessed=True,
        accepted_authorities=base["accepted_authorities"],
        compact_necessary_baseline=fp(P + "baseline-v1.json"),
        protected_unique_paths=base["protected_unique_paths"],
        canonical_protected_summary_sha256=base["canonical_protected_summary_sha256"],
        immediate_own_parent=base["immediate_own_parent"],
        older_own_paths_bound_transitively=666, new_constructor_files_including_freeze=11,
        older_plus_new_own_paths_bound_transitively=677,
        no_historical_inventory_recopy_or_recursive_replay=True,
        authoritative_weekly_telemetry=source["authoritative_weekly_telemetry"],
        artifacts=[fp(P + suffix) for suffix in PAYLOADS]))
    verify()


def verify():
    verify_inputs()
    value = obj(P + "freeze-v1.json")
    assert len(value["artifacts"]) == 10
    for row in value["artifacts"]:
        check(row)
    print(json.dumps(dict(postverified=True, files_including_freeze=11, whole_obligations=72,
        candidate=fp(P + "candidate-v1.md"), freeze=fp(P + "freeze-v1.json"),
        protected_paths=value["protected_unique_paths"], own_transitive_paths=677)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["baseline", "freeze", "verify"])
    args = parser.parse_args()
    {"baseline": baseline, "freeze": freeze, "verify": verify}[args.operation]()
