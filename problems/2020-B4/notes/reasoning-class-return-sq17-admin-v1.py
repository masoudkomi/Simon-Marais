#!/usr/bin/env python3
"""NEW SQ17 documentary administration only; no mathematical operations.

Modes prepare; freeze --model-readback-complete; SEPARATE read-only verify.
Only NEW assigned-prefix files are created, with no overwrites. No old
author/source/freezer code, algebra program or search is executed.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-class-return-sq17-"
PARENT = "problems/2021-B4/reviews/reasoning-center-return-r21-review-2-manifest-v1.json"
PARENT_ID = (3231, "369b970ef7514db6ed6a97e4462c4567da53ee78b1874ef539d2b4228401bbbb")
PDF = ".cache/literature/coordinator-schmidt1998-class-r1.pdf"
PDF_ID = (227434, "f97dd90e1c72ea1b3f8eefae5272b58068b4e15a5dc23578cd7d937dc56dbeb5")
HUMAN = ["candidate-v1.md", "working-v1.md", "sources-v1.md", "sources-v1.json"]
PAYLOADS = HUMAN + ["admin-v1.py", "baseline-v1.json", "metadata-v1.json"]
BASELINE = PREFIX + "baseline-v1.json"
METADATA = PREFIX + "metadata-v1.json"
FREEZE = PREFIX + "freeze-v1.json"
REQUESTED = {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True}
WEEKLY = {"at_utc": "2026-10-18 18:23:40 UTC", "method": "own same-awaited clock/get_usage_limits",
          "TOTAL_used_percent": 60, "window_minutes": 10080, "resetsAt": 1792874445,
          "ordinaryUsageAllowed": True, "legacy_by_limit_agree": True,
          "account_label": "029a8928...1334ac3a", "TOTAL_ceiling_percent": 90,
          "integration_reserve": True, "automatic_later_window_spending": False}


def stamp():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    target = (ROOT / path).resolve()
    assert target.is_relative_to(ROOT)
    return target.read_bytes()


def record(path):
    data = raw(path)
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def obj(path):
    return json.loads(raw(path))


def match(expected):
    assert set(expected) == {"path", "bytes", "sha256"}
    assert record(expected["path"]) == expected, "Changed input: " + expected["path"]
    return expected


def fixed(path, identity):
    return match({"path": path, "bytes": identity[0], "sha256": identity[1]})


def summary(rows):
    unique = {}
    for row in rows:
        if row["path"] in unique:
            assert unique[row["path"]] == row
        unique[row["path"]] = row
    canonical = json.dumps([unique[p] for p in sorted(unique)], sort_keys=True, separators=(",", ":")).encode()
    return {"occurrences": len(rows), "unique_paths": len(unique), "canonical_sha256": hashlib.sha256(canonical).hexdigest()}


def create(path, data):
    assert path.startswith(PREFIX)
    with (ROOT / path).open("xb") as stream:
        stream.write((json.dumps(data, indent=2, ensure_ascii=False) + "\n").encode())


def labels():
    main = raw(PREFIX + "candidate-v1.md").decode()
    found = re.findall(r"^\|(SQ17-\d{2})\|", main, re.M)
    assert found == [f"SQ17-{n:02d}" for n in range(1, 41)]
    for name in ["SQ17A", "SQ17B", "SQ17C"]:
        assert "**" + name + "," in main
    source = obj(PREFIX + "sources-v1.json")
    assert source["independent_effective_readback"] is None
    assert source["constructor_excluded"] is True
    return {"whole_obligation_and_author_disposition_labels": 40,
            "open_research_gap_rows_not_claimed_theorems": ["SQ17-37", "SQ17-38"],
            "proposed_claim_labels": ["SQ17A", "SQ17B", "SQ17C"],
            "mathematical_truth_checked_by_code": False}


def current_inputs():
    rows = [fixed("AGENTS.md", (4707, "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff")),
            record("problems/2020-B4/statement.md"), fixed(PDF, PDF_ID)]
    authorities = []
    for stem, authority_stem, copy_suffix in [
        ("reasoning-arithmetic-return-r14", "reasoning-arithmetic-return-r14-repair-v1.1-acceptance", "v1.2"),
        ("reasoning-class-return-sq15", "reasoning-class-return-sq15-acceptance", "v1.1")]:
        base = "problems/2020-B4/"
        authority_path = base + "reviews/" + authority_stem + ".json"
        authority = obj(authority_path)
        accepted = match(authority["accepted_copy"])
        assert accepted["path"] == base + "proofs/reviewed-" + stem + "-" + copy_suffix + ".md"
        candidate = match(authority["candidate"])
        assert raw(accepted["path"]).endswith(raw(candidate["path"]))
        rows.extend([accepted, record(authority_path),
                     record(base + "reviews/" + authority_stem + ".md"),
                     record(base + "notes/" + stem + "-sources-v1.1.md")])
        authorities.append({"immutable_current_authority": record(authority_path),
                            "candidate_identity_bound_without_recopied_ancestry": candidate,
                            "accepted_suffix_byte_identical": True,
                            "COMPLETE_body_EACH_MD_JSON_sources_read_in_immediately_preceding_SQ16_rotation": True,
                            "fresh_independent_recertification_or_unrelated_ancestry_reread": False,
                            "historical_root_verified_occurrences": authority["record_occurrences_verified"],
                            "historical_root_verified_paths": authority["unique_paths_verified"]})
    parent = obj(PARENT)
    parent_rows = [fixed(PARENT, PARENT_ID)]
    assert len(parent["payloads"]) == 4
    parent_rows.extend(match(row) for row in parent["payloads"])
    assert parent["older_plus_new_own_paths_bound_transitively"] == 949
    rows.append(parent_rows[0])
    return rows, parent_rows, authorities


def prepare():
    assert not (ROOT / FREEZE).exists()
    rows, parent_rows, authorities = current_inputs()
    checks = labels()
    create(BASELINE, {"prepared_at_utc": stamp(), "scope": "Necessary current immutable authorities, exact source PDF and compact immediate own parent; no growing historical inventory recopy",
                      "records": rows, "direct_guard_summary": summary(rows),
                      "current_authorities": authorities,
                      "immediate_own_parent": record(PARENT),
                      "own_parent_ALL4_payloads_directly_verified_bound_not_recopied": summary(parent_rows),
                      "all_checked_summary": summary(rows + parent_rows),
                      "older_own_paths_bound_transitively": 949,
                      "older_plus_new8_own_paths_bound_transitively": 957,
                      "literal_checks": checks,
                      "source_visual_read_ALL16_pages": True,
                      "final_journal_typeset_version_or_possible_errata_verified": False,
                      "old_cache_PDF_unchanged_and_not_redistributed": True,
                      "no_NEW_SQ16_peer_access": True})
    create(METADATA, {"created_at_utc": stamp(), "status": "candidate proof - unverified; exact composite-conductor bridge obstruction",
                      "constructor": "/root/review_2022_complexity_r2", "constructor_excluded": True,
                      "TWO_OTHER_initially_blind_ENTIRE_WHOLE_reviews_required": True,
                      "root_NEW_math_inference": False, "requested": REQUESTED,
                      "independent_effective_readback": None,
                      "whole_obligations_and_author_dispositions": 40,
                      "open_actual_research_gap_rows": ["SQ17-37", "SQ17-38"],
                      "claims": ["SQ17A classical unit norm nonsquare mechanism", "SQ17B ALL-t actual-conductor integral same-ideal counterfamily", "SQ17C classical exact two-coset norm criterion"],
                      "classical_Hasse_TD_mechanism_claimed_new": False,
                      "counterfamily_is_compatible_Fourier_tuple_or_perfect_set": False,
                      "actual_odd_H_or_full_norm_q_realization_obstruction_obtained": False,
                      "no_annual_parameter_classification_or_priority_claim": True,
                      "ENTIRE_payloads_before_freeze": 7, "ENTIRE_files_including_freeze": 8,
                      "immediate_own_parent": record(PARENT),
                      "older_own_paths_bound_transitively": 949,
                      "older_plus_new_own_paths_bound_transitively": 957,
                      "no_mathematical_program_CAS_scan_test_source_author_old_replay": True,
                      "rendering_only_source_reading_not_mathcode": True,
                      "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
                      "pending_native_math_child_or_retrieval": False,
                      "weekly": WEEKLY,
                      "FULL_final_MODEL_readback_ALL7_then_freeze_readback_then_SEPARATE_verify_required": True})
    print(json.dumps({"prepare": "PASS", "all_checked_summary": summary(rows + parent_rows), **checks}, indent=2))


def check_baseline():
    base = obj(BASELINE)
    for row in base["records"]:
        match(row)
    assert summary(base["records"]) == base["direct_guard_summary"]
    rows, parent_rows, authorities = current_inputs()
    assert summary(rows + parent_rows) == base["all_checked_summary"]
    assert authorities == base["current_authorities"]
    return base


def freeze(readback):
    assert readback, "Actual FULL final MODEL readback must finish first"
    base = check_baseline()
    checks = labels()
    payloads = [record(PREFIX + suffix) for suffix in PAYLOADS]
    create(FREEZE, {"frozen_at_utc": stamp(), "status": "candidate proof - unverified",
                    "constructor": "/root/review_2022_complexity_r2", "constructor_excluded": True,
                    "TWO_OTHER_initially_blind_ENTIRE_WHOLE_reviews_required": True,
                    "root_NEW_math_inference": False, "requested": REQUESTED,
                    "independent_effective_readback": None,
                    "whole_obligations_and_author_dispositions": 40,
                    "open_actual_research_gap_rows_not_claimed_theorems": ["SQ17-37", "SQ17-38"],
                    "ENTIRE_files_including_freeze": 8,
                    "FULL_final_MODEL_readback_ALL7_payloads_code_ALLgenerated_metadata_completed": True,
                    "FULL_freeze_MODEL_readback_then_SEPARATE_readonly_verify_required": True,
                    "all_checked_summary": base["all_checked_summary"],
                    "immediate_own_parent": record(PARENT),
                    "older_own_paths_bound_transitively": 949,
                    "older_plus_new_own_paths_bound_transitively": 957,
                    "literal_checks": checks, "source_PDF": fixed(PDF, PDF_ID),
                    "source_version_and_unit_index_boundaries_preserved": True,
                    "no_actual_full_Fourier_odd_H_annual_or_priority_conclusion": True,
                    "no_mathematical_program_CAS_scan_test_source_author_old_replay": True,
                    "no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass": True,
                    "weekly": WEEKLY, "payloads": payloads})
    print(json.dumps({"freeze": record(FREEZE), "main": payloads[0], "ENTIRE_files": 8}, indent=2))


def verify():
    base = check_baseline()
    frozen = obj(FREEZE)
    assert len(frozen["payloads"]) == 7
    assert [row["path"] for row in frozen["payloads"]] == [PREFIX + suffix for suffix in PAYLOADS]
    for row in frozen["payloads"]:
        match(row)
    labels()
    assert frozen["all_checked_summary"] == base["all_checked_summary"]
    for suffix in ["sources-v1.json", "baseline-v1.json", "metadata-v1.json", "freeze-v1.json"]:
        obj(PREFIX + suffix)
    print(json.dumps({"SEPARATE_readonly_verify_at_utc": stamp(), "PASS": True,
                      "ENTIRE_files": 8, "whole_obligations": 40,
                      "all_checked_summary": base["all_checked_summary"],
                      "main": record(PREFIX + "candidate-v1.md"), "freeze": record(FREEZE),
                      "mathematical_truth_checked_by_code": False}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["prepare", "freeze", "verify"])
    parser.add_argument("--model-readback-complete", action="store_true")
    args = parser.parse_args()
    if args.mode == "prepare":
        prepare()
    elif args.mode == "freeze":
        freeze(args.model_readback_complete)
    else:
        verify()
