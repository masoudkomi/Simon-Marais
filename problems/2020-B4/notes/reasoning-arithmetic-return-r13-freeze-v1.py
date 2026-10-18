#!/usr/bin/env python3
"""NEW R13 preservation metadata only; never a mathematical certificate."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-arithmetic-return-r13-"
PARENT = "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-2-reaudit-v2-manifest.json"
PARENT_EXPECTED = {
    "path": PARENT, "bytes": 5850,
    "sha256": "e2d3cb2fa85a32145f65509299a2686e4a8451b263181456b73d5cc380cce1af",
}
AUTHORITY_NAMES = (
    "reasoning-Todd-return-r12", "reasoning-arithmetic-return-r9",
    "reasoning-arithmetic-return-r11",
)
FAILURE_NOTES = (
    "problems/2020-B4/notes/reasoning-Todd-return-r12-failed-routes-v1.md",
    "problems/2020-B4/notes/reasoning-arithmetic-return-r11-failed-routes-v1.md",
    "problems/2020-B4/notes/reasoning-arithmetic-return-r9-failed-routes-v1.md",
)
FORBIDDEN = (
    "problems/2020-B4/reviews/reasoning-arithmetic-return-r13-",
    "problems/2025-B4/reviews/reasoning-branch-return-r4-",
)
PAYLOAD_SUFFIXES = (
    "candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "failed-routes-v1.md", "sources-v1.md", "sources-v1.json",
    "worklog-v1.md", "freeze-v1.py", "baseline-v1.json",
    "input-validation-v1.json",
)
BASELINE = PREFIX + "baseline-v1.json"
VALIDATION = PREFIX + "input-validation-v1.json"
FREEZE = PREFIX + "freeze-v1.json"


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert isinstance(path, str) and not path.startswith("/")
    assert ".." not in Path(path).parts
    assert not any(path.startswith(x) for x in FORBIDDEN), path
    return (ROOT / path).read_bytes()


def obj(path):
    return json.loads(raw(path))


def fp(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def check(record):
    expected = {k: record[k] for k in ("path", "bytes", "sha256")}
    assert fp(record["path"]) == expected, record["path"]
    return expected


def canonical_sha(value):
    data = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode()).hexdigest()


def put(path, data):
    assert path in (BASELINE, VALIDATION, FREEZE)
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def accepted_records():
    declared = {r["path"]: r for r in obj(PREFIX + "sources-v1.json")[
        "complete_current_accepted_bodies_and_MD_JSON_read"]}
    records, bindings = [], []
    for name in AUTHORITY_NAMES:
        authority = "problems/2020-B4/reviews/" + name + "-acceptance.json"
        authority_md = authority[:-5] + ".md"
        data = obj(authority)
        assert data["status"].startswith("proved, independently reviewed")
        body, candidate = data["accepted_copy"], data["candidate"]
        assert body["path"] in declared
        assert {k: declared[body["path"]][k] for k in ("path", "bytes", "sha256")} == body
        records += [fp(authority), fp(authority_md), check(body), check(candidate)]
        assert raw(body["path"]).endswith(raw(candidate["path"])), body["path"]
        bindings.append({
            "authority_json": authority, "authority_md": authority_md,
            "accepted_body": body["path"], "exact_candidate_suffix": candidate["path"],
            "historical_occurrences_bound_not_recopied_or_replayed": data["record_occurrences_verified"],
            "historical_paths_bound_not_recopied_or_replayed": data["unique_paths_verified"],
            "operative": name in AUTHORITY_NAMES[:2],
        })
    assert len(records) == 12
    return records, bindings


def parent_records():
    check(PARENT_EXPECTED)
    data = obj(PARENT)
    assert data["older_plus_new_own_paths_bound_transitively"] == 708
    assert len(data["artifacts"]) == 9
    records = [PARENT_EXPECTED]
    for record in data["artifacts"]:
        assert record["path"].startswith(
            "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-2-reaudit-v2-")
        records.append(check(record))
    return records


def current_records():
    accepted, bindings = accepted_records()
    records = accepted + parent_records()
    records += [fp("AGENTS.md"), fp("problems/2020-B4/statement.md")]
    records += [fp(path) for path in FAILURE_NOTES]
    assert len(records) == len({r["path"] for r in records}) == 27
    assert fp("AGENTS.md") == {
        "path": "AGENTS.md", "bytes": 4707,
        "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"}
    return sorted(records, key=lambda r: r["path"]), bindings


def baseline():
    records, bindings = current_records()
    value = {
        "created_at_utc": now(),
        "purpose": "NEW metadata-only necessary R13 preservation baseline, not mathematical evidence",
        "snapshot_stage": "after complete hand proofs and actual primary/accepted-input reads, before whole immutable freeze",
        "protected_fingerprint_occurrences": 27, "protected_unique_paths": 27,
        "canonical_protected_summary_sha256": canonical_sha(records),
        "protected_fingerprints": records,
        "accepted_bindings": bindings,
        "immediate_own_parent": PARENT_EXPECTED,
        "older_own_paths_bound_transitively": 708,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "mutable_landscape_snapshots_context_only": [
            fp("problems/2020-B4/research.md"), fp("problems/2020-B4/references.md")],
        "forbidden_NEW_peer_prefixes_never_read_or_hashed_by_this_code": list(FORBIDDEN),
        "mathematical_program_scan_or_author_source_rerun": False,
    }
    put(BASELINE, value)
    print(json.dumps({"baseline": fp(BASELINE), "protected_paths": 27}))


def check_baseline():
    data = obj(BASELINE)
    records, bindings = current_records()
    assert records == data["protected_fingerprints"]
    assert canonical_sha(records) == data["canonical_protected_summary_sha256"]
    assert bindings == data["accepted_bindings"]
    return data


def label_checks():
    for suffix in ("obligations-v1.md", "constructor-checks-v1.md"):
        content = raw(PREFIX + suffix).decode()
        assert [int(x) for x in re.findall(r"(?m)^(\d+)\. ", content)] == list(range(1, 65)), suffix
    main = raw(PREFIX + "candidate-v1.md").decode()
    assert "Candidate proof - unverified" in main
    assert all("**L13" + letter + ":" in main for letter in "ABCD")
    source = obj(PREFIX + "sources-v1.json")
    assert source["whole_obligations"] == 64
    assert source["TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required"] is True
    assert source["root_or_other_worker_NEW_proof_inference_contribution"] is False
    assert source["requested_settings"] == {
        "model": "gpt-6.1-sol", "reasoning": "max", "inherited": True}
    assert source["independently_verified_effective_settings"] is None
    meter = source["authoritative_weekly_telemetry"]
    assert meter["reset_unix"] == 1792874445
    assert meter["used_percent_TOTAL"] < meter["ceiling_TOTAL_percent"] == 90
    assert meter["automatic_later_reset_spending"] is False
    return source


def freeze():
    assert not (ROOT / FREEZE).exists()
    assert not (ROOT / VALIDATION).exists()
    data = check_baseline()
    source = label_checks()
    for suffix in PAYLOAD_SUFFIXES:
        if suffix != "input-validation-v1.json":
            assert raw(PREFIX + suffix)
    put(VALIDATION, {
        "verified_at_utc": now(),
        "metadata_ONLY_NOT_proof_or_independent_review": True,
        "necessary_protected_paths_unchanged": 27,
        "exact_current_accepted_body_candidate_suffix_MDJSON_bindings_checked": 3,
        "historical_inventory_recopied_or_recursively_replayed": False,
        "immediate_own_parent_plus_nine_payloads_unchanged": True,
        "whole_obligation_and_constructor_labels_ordered_1_to_64": True,
        "L13A_B_C_D_whole_main_present_and_unverified": True,
        "mathematical_or_author_source_old_certificate_code_executed": False,
        "ENTIRE_generated_metadata_readback_and_separate_postverify_required_before_handoff": True,
    })
    artifacts = [fp(PREFIX + suffix) for suffix in PAYLOAD_SUFFIXES]
    assert len(artifacts) == 10
    put(FREEZE, {
        "frozen_at_utc": now(),
        "status": "candidate proof - unverified",
        "whole_checkpoint": "ENTIRE L13A-L13D proofs/ALL64 obligations and dispositions/failures/sources/log/code/ALLmetadata",
        "constructor": "/root/review_2022_complexity_r2",
        "constructor_excluded_from_TWO_OTHER_whole_audits": True,
        "TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required": True,
        "root_or_other_worker_NEW_proof_inference_contribution": False,
        "older_roles_disclosed_not_fresh_self_review": source["older_roles_disclosed"],
        "requested_settings": source["requested_settings"],
        "independently_verified_effective_settings": None,
        "whole_obligations": 64,
        "actual_ideal_layers_and_integral_complement_domain_explicit": True,
        "unconditional_radical_and_actual_tail_quantifiers_distinct": True,
        "classical_Davenport_tools_attributed_and_fully_derived_for_needed_scope": True,
        "old_A9_explanatory_limit_explicit_ancestors_unchanged": True,
        "new_numeric_q_class_evaluation_or_annual_priority_claim": False,
        "no_NEW_BD_or_R13_peer_material_accessed": True,
        "no_math_program_CAS_scan_test_source_author_or_old_certificate_freezer_replay": True,
        "no_old_shared_Git_cache_edit_spawn_download_charge_contact_or_bypass": True,
        "accepted_operative_bindings": [r for r in data["accepted_bindings"] if r["operative"]],
        "accepted_comparison_bindings": [r for r in data["accepted_bindings"] if not r["operative"]],
        "compact_necessary_baseline": fp(BASELINE),
        "protected_fingerprint_occurrences": 27, "protected_unique_paths": 27,
        "canonical_protected_summary_sha256": data["canonical_protected_summary_sha256"],
        "immediate_own_parent": PARENT_EXPECTED,
        "older_own_paths_bound_transitively": 708,
        "new_constructor_files_including_freeze": 11,
        "older_plus_new_own_paths_bound_transitively": 719,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "authoritative_weekly_telemetry": source["authoritative_weekly_telemetry"],
        "artifacts": artifacts,
    })
    print(json.dumps({"freeze": fp(FREEZE), "main": artifacts[0], "new_files": 11}))


def verify():
    baseline_data = check_baseline()
    label_checks()
    data = obj(FREEZE)
    assert data["status"] == "candidate proof - unverified"
    assert data["compact_necessary_baseline"] == fp(BASELINE)
    assert data["canonical_protected_summary_sha256"] == baseline_data["canonical_protected_summary_sha256"]
    assert [r["path"] for r in data["artifacts"]] == [PREFIX + s for s in PAYLOAD_SUFFIXES]
    for record in data["artifacts"]:
        check(record)
    print(json.dumps({
        "separate_postfreeze_metadata_verification": "pass",
        "freeze": fp(FREEZE), "main": data["artifacts"][0],
        "new_files": 11, "protected_paths_unchanged": 27,
        "own_paths_bound_transitively": 719,
        "mathematical_certificate_or_independent_review": False,
        "no_NEW_peer_material_read_or_hashed": True,
    }))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("baseline", "freeze", "verify"))
    mode = parser.parse_args().mode
    {"baseline": baseline, "freeze": freeze, "verify": verify}[mode]()
