#!/usr/bin/env python3
"""Own R16 review integrity only. Contains no mathematical evaluation."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2021-B4/reviews/reasoning-early-return-r16-review-2-"
T = "problems/2021-B4/notes/reasoning-early-return-r16-"
PARENT = "problems/2024-B4/reviews/cofactor-cubic-r3-review-2-manifest-v1.json"
PARENT_SHA = "1c76011a1234a5690370d4d2b256eb788e014523d2e8634e9baa7890484822f1"
MAIN_SHA = "d9765b700bf7f7a0c13bcb0b5729a38150e87fe847156df29d4c592abad0b2d1"
PAYLOADS = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md",
            "sources-v1.json", "worklog-v1.md", "freeze-v1.py",
            "baseline-v1.json", "input-validation-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert not path.startswith("problems/2021-B4/reviews/reasoning-early-return-r16-review-1-")
    return (ROOT / path).read_bytes()


def fp(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def obj(path):
    return json.loads(raw(path))


def check(row):
    expected = {k: row[k] for k in ("path", "bytes", "sha256")}
    assert fp(expected["path"]) == expected, expected["path"]
    return expected


def digest(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def put(suffix, data):
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write("\n")


def accepted():
    bindings = []
    for stem, wanted in [
        ("reasoning-return-r8", "33b8713d402d09f711d0096cdc4e8c00f9e622a5335f8e3345eb4f82ba0d359d"),
        ("reasoning-return-r5", "f4f088adc133b0581520488cdbba30082c13b2402c96ae555142e5491ad4137d"),
    ]:
        path = f"problems/2021-B4/reviews/{stem}-acceptance.json"
        authority = obj(path)
        assert authority["unresolved_substantive_issues"] == 0
        assert authority["repair_required"] is False
        body = check(authority["accepted_copy"])
        candidate = check(authority["candidate"])
        assert body["sha256"] == wanted
        assert raw(body["path"]).endswith(raw(candidate["path"]))
        bindings.append(dict(authority=fp(path), accepted_body=body,
            exact_candidate_suffix=candidate,
            historical_occurrences_bound_not_replayed=authority["record_occurrences_verified"],
            historical_paths_bound_not_replayed=authority["unique_paths_verified"]))
    return bindings


def baseline():
    constructor = obj(T + "freeze-v1.json")
    assert len(constructor["artifacts"]) == 11
    assert (fp(T + "candidate-v1.md")["bytes"], fp(T + "candidate-v1.md")["sha256"]) == (18818, MAIN_SHA)
    prior = obj(T + "baseline-v1.json")
    assert len(prior["deduplicated_rows"]) == 37
    assert digest(prior["deduplicated_rows"]) == prior["deduplicated_summary_sha256"]
    parent = fp(PARENT)
    assert (parent["bytes"], parent["sha256"]) == (7949, PARENT_SHA)
    parent_data = obj(PARENT)
    assert len(parent_data["artifacts"]) == 9
    assert parent_data["older_plus_new_own_paths_bound_transitively"] == 656
    rows = [fp("AGENTS.md"), fp("problems/2021-B4/statement.md"), fp(T + "freeze-v1.json")]
    rows += [check(row) for row in constructor["artifacts"]]
    rows += [check(row) for row in prior["deduplicated_rows"]]
    rows += [parent] + [check(row) for row in parent_data["artifacts"]]
    unique = {}
    for row in rows:
        assert row["path"] not in unique or unique[row["path"]] == row
        unique[row["path"]] = row
    ordered = [unique[k] for k in sorted(unique)]
    put("baseline-v1.json", dict(captured_at_utc=now(),
        administrative_only_not_mathematical_validation=True,
        assigned_prefix_confirmed_unused_before_first_write=True,
        target_main=fp(T + "candidate-v1.md"), target_freeze=fp(T + "freeze-v1.json"),
        protected_fingerprint_occurrences=len(rows), protected_unique_paths=len(ordered),
        canonical_protected_summary_sha256=digest(ordered), protected_rows=ordered,
        constructor_current_summary_bound=constructor["current_input_summary"],
        constructor_baseline_all37_declared_current_fingerprints_verified=True,
        accepted_operative_bindings=accepted(),
        immediate_own_parent=parent, immediate_own_parent_nine_payloads_unchanged=True,
        older_own_paths_bound_transitively=656,
        parent_historical_summaries_bound_not_expanded=parent_data["compact_immutable_parent_summaries"],
        no_historical_inventory_recopy_or_recursive_replay=True,
        no_corresponding_NEW_root_R16_review_findings_files_hash_or_metadata_accessed=True))
    print(json.dumps(dict(baseline=fp(P + "baseline-v1.json"), occurrences=len(rows), paths=len(ordered))))


def verify_inputs():
    base = obj(P + "baseline-v1.json")
    for row in base["protected_rows"]:
        check(row)
    assert digest(base["protected_rows"]) == base["canonical_protected_summary_sha256"]
    assert accepted() == base["accepted_operative_bindings"]
    return base


def freeze():
    base = verify_inputs()
    ledger = raw(P + "ledger-v1.md").decode()
    assert re.findall(r"^(\d+)\. PASS", ledger, re.M) == [str(i) for i in range(1, 57)]
    assert re.findall(r"^### R16R2-N(\d+)", raw(P + "issues-v1.md").decode(), re.M) == [str(i) for i in range(1, 7)]
    obj(P + "sources-v1.json")
    report = raw(P + "initial-v1.md").decode()
    for claim in ("R16A", "R16B", "R16C"):
        assert claim in report
    put("input-validation-v1.json", dict(postchecked_at_utc=now(),
        administrative_only_not_mathematical_validation=True,
        protected_fingerprint_occurrences=base["protected_fingerprint_occurrences"],
        protected_unique_paths=base["protected_unique_paths"],
        canonical_protected_summary_sha256=base["canonical_protected_summary_sha256"],
        entire_constructor_twelve_files_exact=True,
        all37_constructor_current_declared_fingerprints_unchanged=True,
        two_accepted_body_suffixes_exact=True,
        all56_reviewer_ledger_labels_once_in_order=True,
        six_closed_note_labels_once_in_order=True,
        immediate_own_parent_nine_payloads_unchanged=True,
        no_math_code_CAS_scan_author_source_freezer_or_certificate_rerun=True,
        no_corresponding_NEW_root_R16_review_findings_files_hash_or_metadata_accessed=True))
    put("manifest-v1.json", dict(frozen_at_utc=now(),
        status="ENTIRE initially blind OTHER NONCONSTRUCTOR WHOLE R16A-C review2 initial frozen",
        reviewer="/root/review_2022_complexity_r2", constructor="/root/review_2021_reasoning_j15_r2",
        reviewer_new_constructive_contribution=False, constructor_excluded=True,
        requested_settings=dict(model="gpt-6.1-sol", reasoning="max", inherited=True),
        independently_verified_effective_settings=None,
        target_main=base["target_main"], target_freeze=base["target_freeze"],
        entire_twelve_file_constructor_packet_read=True, whole_obligations=56,
        whole_independent_ledger_checks=56,
        substantive_proof_defects_found=0, unresolved_proof_objections=0,
        required_mathematical_repairs=0, closed_scope_dependency_notes=6,
        no_corresponding_NEW_root_R16_review_findings_files_hash_or_metadata_accessed=True,
        completion_IDENTITY_ONLY_until_BOTH_entire_initials_confirmed=True,
        accepted_operative_bindings=base["accepted_operative_bindings"],
        compact_necessary_baseline=fp(P + "baseline-v1.json"),
        protected_fingerprint_occurrences=base["protected_fingerprint_occurrences"],
        protected_unique_paths=base["protected_unique_paths"],
        canonical_protected_summary_sha256=base["canonical_protected_summary_sha256"],
        immediate_own_parent=base["immediate_own_parent"],
        older_own_paths_bound_transitively=656, new_review_files_including_manifest=10,
        older_plus_new_own_paths_bound_transitively=666,
        constructor_current_summary_bound=base["constructor_current_summary_bound"],
        no_historical_inventory_recopy_or_recursive_replay=True,
        no_math_code_CAS_scan_certificate_or_author_rerun=True,
        no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass=True,
        coordinator_promotion_full_m4_degree20_annual_or_novelty_claim=False,
        authoritative_weekly_telemetry=obj(P + "sources-v1.json")["authoritative_weekly_telemetry"],
        artifacts=[fp(P + suffix) for suffix in PAYLOADS]))
    verify()


def verify():
    verify_inputs()
    value = obj(P + "manifest-v1.json")
    assert len(value["artifacts"]) == 9
    for row in value["artifacts"]:
        check(row)
    print(json.dumps(dict(postverified=True, whole_obligations=56, files_including_manifest=10,
        report=fp(P + "initial-v1.md"), manifest=fp(P + "manifest-v1.json"),
        protected_unique_paths=value["protected_unique_paths"], own_transitive_paths=666)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", choices=["baseline", "freeze", "verify"])
    args = parser.parse_args()
    {"baseline": baseline, "freeze": freeze, "verify": verify}[args.operation]()
