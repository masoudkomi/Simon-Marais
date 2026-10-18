#!/usr/bin/env python3
"""NEW R5 R2 preservation only; no mathematical evaluation or source rerun."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-2-"
A = "problems/2024-B4/notes/cofactor-Frobenius-r5-"
PEER = "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-1-"
PARENT = "problems/2020-B4/notes/reasoning-Todd-return-r12-freeze-v1.json"
PARENT_SHA = "cac7580782285028c7e71207097a3566232306a764fa7d174a7a1fd21973dcc0"
AUTHOR_SHA = "cda866d3b82dfe335c78643d15d857e21bcda5439c2ecf308956281b02a8b545"
MAIN_SHA = "ff29bb1757d3f24229cb138bdfcca02b4d45c457200afc2ecc78104918c823ee"
T1 = "problems/2024-B4/proofs/reviewed-structural-v1.1.md"
T1_SHA = "082dc054ce2cdaea80eee009f4c97c877c6968afb54b5a8f3141b7354031dd3f"
AUTHORITIES = [
    ("cofactor-global-r2", "fd110d1615e730d754063b157cc1906b418702f510b2640bfd1b5c63e898548d"),
    ("cofactor-dominant-r4", "14c47b6db082bee1d60bcf297c289fe949fdec9384cc8a159b199c56ba265838"),
]
CONTENT = ["initial-v1.md", "ledger-v1.md", "issues-v1.md", "source-checks-v1.md",
           "sources-v1.json", "worklog-v1.md", "freeze-v1.py"]
PAYLOADS = CONTENT + ["baseline-v1.json", "input-validation-v1.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert not path.startswith(PEER), "Corresponding NEW peer R5 access forbidden"
    return (ROOT / path).read_bytes()


def fp(path):
    data = raw(path)
    return dict(path=path, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def obj(path):
    return json.loads(raw(path))


def check(row):
    wanted = {key: row[key] for key in ("path", "bytes", "sha256")}
    assert fp(wanted["path"]) == wanted, wanted["path"]
    return wanted


def canonical(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def put(suffix, value):
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def accepted():
    rows, bindings = [], []
    for stem, expected in AUTHORITIES:
        prefix = "problems/2024-B4/reviews/" + stem + "-acceptance"
        value = obj(prefix + ".json")
        assert value["status"] == "proved, independently reviewed scoped partial result"
        assert value["unresolved_substantive_issues"] == 0
        assert value["repair_required"] is False
        body, candidate = check(value["accepted_copy"]), check(value["candidate"])
        assert body["sha256"] == expected
        assert raw(body["path"]).endswith(raw(candidate["path"]))
        authority = fp(prefix + ".json")
        rows += [fp(prefix + ".md"), authority, fp(prefix + "-integrity.json"), body, candidate]
        bindings.append(dict(authority=authority, accepted_body=body, exact_candidate_suffix=candidate,
            historical_occurrences_bound_not_recopied_or_replayed=value["record_occurrences_verified"],
            historical_paths_bound_not_recopied_or_replayed=value["unique_paths_verified"]))
    return bindings, rows


def author():
    freeze = obj(A + "freeze-v1.json")
    record = fp(A + "freeze-v1.json")
    assert (record["bytes"], record["sha256"]) == (3932, AUTHOR_SHA)
    assert len(freeze["artifacts"]) == 8 and freeze["whole_obligations"] == 32
    payloads = [check(row) for row in freeze["artifacts"]]
    main = fp(A + "candidate-v1.md")
    assert (main["bytes"], main["sha256"]) == (12486, MAIN_SHA)
    base = obj(A + "baseline-v1.json")
    guards = [check(row) for row in base["protected"]]
    assert len(guards) == 23
    assert canonical(guards) == base["current_input_summary"]["sha256"]
    assert base["current_input_summary"] == freeze["current_input_summary"]
    labels = re.findall(r"^\| (CF-\d{2}) \|", raw(A + "obligations-v1.md").decode(), re.M)
    assert labels == [f"CF-{i:02d}" for i in range(1, 33)]
    return record, payloads, dict(
        author_current_input_summary=base["current_input_summary"],
        eight_payload_plus_23_guard_occurrences_independently_verified=31,
        protected_guard_paths=23, all_nine_author_files_fully_read=True,
        all_author_code_and_metadata_read_but_not_executed=True,
        historical_rows_bound_in_author_baseline_not_recopied=True)


def baseline():
    present = {str(path.relative_to(ROOT)) for path in (ROOT / "problems/2024-B4/reviews").glob(
        "cofactor-Frobenius-r5-review-2-*")}
    assert present == {P + suffix for suffix in CONTENT}, present
    constructor, payloads, summary = author()
    bindings, rows = accepted()
    rows += [constructor] + payloads
    rows += [fp("AGENTS.md"), fp("problems/2024-B4/statement.md")]
    rows += [fp("problems/2024-B4/notes/cofactor-global-r2-source-audit-v1.md"),
             fp("problems/2024-B4/notes/cofactor-dominant-r4-sources-v1.md")]
    t1auth = "problems/2024-B4/reviews/structural-acceptance.json"
    structural = obj(t1auth)
    proof = check(structural["accepted_proof"])
    assert proof["path"] == T1 and proof["sha256"] == T1_SHA
    assert structural["remaining_substantive_objections"] == 0
    rows += [proof, fp(t1auth), fp(t1auth[:-5] + ".md")]
    parent = fp(PARENT)
    assert (parent["bytes"], parent["sha256"]) == (9167, PARENT_SHA)
    previous = obj(PARENT)
    assert previous["older_plus_new_own_paths_bound_transitively"] == 677
    assert len(previous["artifacts"]) == 10
    rows += [parent] + [check(row) for row in previous["artifacts"]]
    unique = {}
    for row in rows:
        assert row["path"] not in unique or unique[row["path"]] == row
        unique[row["path"]] = row
    guards = [unique[path] for path in sorted(unique)]
    put("baseline-v1.json", dict(captured_at_utc=now(), administrative_only=True,
        prefix_confirmed_unused_before_first_write=True,
        protected_fingerprint_occurrences=len(rows), protected_unique_paths=len(guards),
        canonical_protected_summary_sha256=canonical(guards), protected_rows=guards,
        exact_constructor_freeze=constructor, constructor_summary=summary,
        accepted_operative_bindings=bindings,
        operative_claims=["CG1", "CG2", "R4A", "R4B", "R4C"],
        T1_header_domain_entire_Section1_and_current_authority_read=True,
        T1_old_documented_editorial_change_no_whole_suffix_assertion=True,
        immediate_own_parent=parent, parent_ten_payloads_unchanged=True,
        older_own_paths_bound_transitively=677,
        parent_previous_input_summary_bound_without_recursion=dict(
            paths=previous["protected_unique_paths"], sha256=previous["canonical_protected_summary_sha256"]),
        no_historical_inventory_recopy_or_recursive_replay=True,
        no_corresponding_NEW_R5_review1_findings_files_hashes_metadata_accessed=True))
    print(json.dumps(dict(baseline=fp(P + "baseline-v1.json"),
        protected_occurrences=len(rows), protected_unique_paths=len(guards))))


def inputs():
    base = obj(P + "baseline-v1.json")
    for row in base["protected_rows"]:
        check(row)
    assert canonical(base["protected_rows"]) == base["canonical_protected_summary_sha256"]
    assert accepted()[0] == base["accepted_operative_bindings"]
    assert author()[2] == base["constructor_summary"]
    return base


def freeze():
    base = inputs()
    labels = re.findall(r"^\| (CF-\d{2}) \|", raw(P + "ledger-v1.md").decode(), re.M)
    assert labels == [f"CF-{i:02d}" for i in range(1, 33)]
    notes = re.findall(r"^## CFR5R2-N(\d+) ", raw(P + "issues-v1.md").decode(), re.M)
    assert notes == [str(i) for i in range(1, 7)]
    source = obj(P + "sources-v1.json")
    assert source["whole_obligations"] == 32
    assert source["substantive_defects"] == source["required_mathematical_author_repairs"] == 0
    put("input-validation-v1.json", dict(checked_at_utc=now(), administrative_only=True,
        all_protected_bytes_exact=True,
        protected_fingerprint_occurrences=base["protected_fingerprint_occurrences"],
        protected_unique_paths=base["protected_unique_paths"],
        canonical_protected_summary_sha256=base["canonical_protected_summary_sha256"],
        author_nine_files_plus_guard_summary_verified=True,
        CG_R4_exact_accepted_body_candidate_suffixes_verified=True,
        all32_ledger_labels_once_in_order=True, all_six_issue_note_labels_once_in_order=True,
        parent_ten_payloads_unchanged=True, no_mathematical_validation_by_script=True))
    put("manifest-v1.json", dict(frozen_at_utc=now(),
        status="ENTIRE initially blind WHOLE R5A-D independent review2 frozen",
        reviewer="/root/review_2022_complexity_r2", constructor="/root", constructor_excluded=True,
        reviewer_NEW_construction_contribution=False,
        requested_settings=dict(model="gpt-6.1-sol", reasoning="max", inherited=True),
        independently_verified_effective_settings=None,
        whole_obligations=32, entire_report_ALL32_sources_issues_log_code_ALLmetadata_complete=True,
        whole_disposition=source["whole_disposition"], substantive_defects=0,
        required_mathematical_author_repairs=0, unresolved_mathematical_objections=0,
        nonblocking_editorial_arithmetic_notes=1, additional_closed_scope_notes=5,
        printed_wrong_residue_explicitly_flagged_not_silently_verified=True,
        no_corresponding_NEW_R5_review1_findings_files_hashes_metadata_accessed=True,
        completion_identity_only_until_BOTH_entire_initials_confirmed=True,
        no_mathematical_program_CAS_scan_test_optimizer_source_author_or_certificate_rerun=True,
        no_old_shared_Git_cache_edit_spawn_download_charge_contact_or_bypass=True,
        older_roles_disclosed_not_fresh_self_recertification=True,
        accepted_operative_bindings=base["accepted_operative_bindings"],
        exact_constructor_freeze=base["exact_constructor_freeze"],
        compact_necessary_baseline=fp(P + "baseline-v1.json"),
        protected_fingerprint_occurrences=base["protected_fingerprint_occurrences"],
        protected_unique_paths=base["protected_unique_paths"],
        canonical_protected_summary_sha256=base["canonical_protected_summary_sha256"],
        immediate_own_parent=base["immediate_own_parent"], older_own_paths_bound_transitively=677,
        new_review_files_including_manifest=10, older_plus_new_own_paths_bound_transitively=687,
        no_historical_inventory_recopy_or_recursive_replay=True,
        authoritative_weekly_telemetry=source["authoritative_weekly_telemetry"],
        artifacts=[fp(P + suffix) for suffix in PAYLOADS]))
    verify()


def verify():
    inputs()
    value = obj(P + "manifest-v1.json")
    assert len(value["artifacts"]) == 9
    for row in value["artifacts"]:
        check(row)
    print(json.dumps(dict(postverified=True, administrative_only=True,
        whole_obligations=32, files_including_manifest=10,
        initial=fp(P + "initial-v1.md"), manifest=fp(P + "manifest-v1.json"),
        protected_occurrences=value["protected_fingerprint_occurrences"],
        protected_paths=value["protected_unique_paths"], own_transitive_paths=687)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["baseline", "freeze", "verify"])
    args = parser.parse_args()
    {"baseline": baseline, "freeze": freeze, "verify": verify}[args.operation]()
