#!/usr/bin/env python3
"""NEW CT review1 compact integrity only; never a mathematical certificate."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2019-B4/reviews/reasoning-cut-transfer-r4-review-1-"
A = "problems/2019-B4/notes/reasoning-cut-transfer-r4-"
AUTHOR_FREEZE = {"path": A + "freeze-v1.json", "bytes": 2732,
    "sha256": "49123da7a3382b51694438f936965a24ce359f5fe4d0d3ea9549e20a037002c9"}
AUTHOR_MAIN = {"path": A + "candidate-v1.md", "bytes": 30084,
    "sha256": "05bbef77c012ee1e8dc516283e444f09b66ac184896d1d92651719ccf6f39648"}
OWN_WO = "problems/2017-B4/reviews/coordinator-weighted-optimum-r2-review-1-"
PARENT = {"path": OWN_WO + "manifest-v1.json", "bytes": 4968,
    "sha256": "6cbf7bc0f9c179f4c2fac6dc0e48e41b3dce177d3bf3725612c344b897b118ca"}
ACCEPTED = (
    ("reasoning-return-r7", 17727, "4fe222b8b1d89b6b3d66bb16c6a1985390d537eee55bb42bfefdb2d4821e351a", 5859, 1136),
    ("reasoning-critical-return-r2", 26079, "e6f2d345c96cf0b080af9e42092dc13c66b69bfe0b70cd1bcab4b33f43106881", 199, 68),
    ("reasoning-cut-number-r3", 24864, "639ce9d0b13ca53b33da927518ce0aee250d09d562e4ed67e9537cd88ebde6a9", 231, 95),
)
FORBIDDEN = (
    "problems/2025-B4/reviews/reasoning-branch-return-r4-",
    "problems/2020-B4/reviews/reasoning-arithmetic-return-r13-",
)
PAYLOAD = ("initial-v1.md", "ledger-v1.md", "issues-v1.md",
    "source-checks-v1.md", "sources-v1.json", "worklog-v1.md",
    "freeze-v1.py", "baseline-v1.json", "input-validation-v1.json")


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    assert isinstance(path, str) and not path.startswith("/")
    assert ".." not in Path(path).parts
    assert not any(path.startswith(prefix) for prefix in FORBIDDEN), path
    if path.startswith("problems/2019-B4/reviews/reasoning-cut-transfer-r4-"):
        assert path.startswith(P), path
    if path.startswith("problems/2017-B4/reviews/coordinator-weighted-optimum-r2-"):
        assert path.startswith(OWN_WO), path
    return (ROOT / path).read_bytes()


def obj(path):
    return json.loads(raw(path))


def fp(path):
    value = raw(path)
    return {"path": path, "bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}


def check(record):
    expected = {key: record[key] for key in ("path", "bytes", "sha256")}
    assert fp(record["path"]) == expected, record["path"]
    return expected


def digest(value):
    value = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(value.encode()).hexdigest()


def put(suffix, value):
    assert suffix in ("baseline-v1.json", "input-validation-v1.json", "manifest-v1.json")
    with (ROOT / (P + suffix)).open("x", encoding="utf-8") as handle:
        json.dump(value, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def records():
    check(AUTHOR_FREEZE)
    author = obj(AUTHOR_FREEZE["path"])
    assert author["whole_obligations"] == 64 and author["entire_file_count"] == 11
    assert author["main"] == author["artifacts"][0] == AUTHOR_MAIN
    assert len(author["artifacts"]) == 10
    rows = [AUTHOR_FREEZE] + [check(record) for record in author["artifacts"]]

    declared = obj(A + "baseline-v1.json")
    bound = declared["bound_inputs"]
    assert bound["direct_declared_fingerprint_occurrences"] == 47
    assert bound["all_necessary_occurrences_with_root_and_standalone"] == 58
    assert bound["deduplicated_necessary_paths"] == 58
    # Identity exposure occurs only INSIDE assigned author metadata. Never
    # open/hash the author's unrelated BD parent or any of its payloads.
    embedded_parent = author["immediate_own_parent"]
    assert embedded_parent == declared["immediate_own_parent"]
    assert embedded_parent == bound["root_bindings"][0]
    assert embedded_parent == obj(A + "metadata-v1.json")["immediate_own_parent"]
    assert embedded_parent["path"].startswith(FORBIDDEN[0])

    bindings = []
    for index, (name, size, sha, occurrences, paths) in enumerate(ACCEPTED, start=1):
        authority = "problems/2019-B4/reviews/" + name + "-acceptance.json"
        data = obj(authority)
        assert data["status"].startswith("proved, independently reviewed")
        assert not data["repair_required"] and data["unresolved_substantive_issues"] == 0
        assert data["record_occurrences_verified"] == occurrences and data["unique_paths_verified"] == paths
        body, candidate = check(data["accepted_copy"]), check(data["candidate"])
        assert body["bytes"] == size and body["sha256"] == sha
        assert raw(body["path"]).endswith(raw(candidate["path"]))
        authority_fp = fp(authority)
        assert bound["root_bindings"][index] == authority_fp
        suffix = bound["literal_accepted_suffixes"][index - 1]
        assert suffix["authority"] == authority and suffix["candidate"] == candidate
        assert suffix["accepted_copy"] == body and suffix["literal_suffix_pass"] is True
        rows += [authority_fp, fp(authority[:-5] + ".md"), body, candidate]
        bindings.append({"authority": authority, "body": body, "candidate": candidate,
                         "historical_occurrences_bound_not_replayed": occurrences,
                         "historical_paths_bound_not_replayed": paths})

    rows += [fp("AGENTS.md"), fp("problems/2019-B4/statement.md")]
    assert fp("AGENTS.md") == {"path": "AGENTS.md", "bytes": 4707,
        "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"}
    assert fp("problems/2019-B4/statement.md") == {
        "path": "problems/2019-B4/statement.md", "bytes": 1252,
        "sha256": "53d4201dca8bc4a77d995e3df14f95dd146e2df0c82d3b6447ad35a348e89de9"}

    check(PARENT)
    own = obj(PARENT["path"])
    assert own["older_plus_new_own_paths_bound_transitively"] == 729
    assert own["new_review_files_including_manifest"] == 10 and len(own["artifacts"]) == 9
    rows += [PARENT] + [check(record) for record in own["artifacts"]]
    assert len(rows) == len({row["path"] for row in rows}) == 35
    return sorted(rows, key=lambda row: row["path"]), bindings, embedded_parent


def baseline():
    rows, bindings, embedded = records()
    put("baseline-v1.json", {
        "captured_at_utc": now(),
        "purpose": "NEW metadata-only compact CT review preservation, not mathematical evidence",
        "stage": "after ENTIRE author/source reads and complete hand reconstruction, before immutable review freeze",
        "assigned_prefix_confirmed_unused_before_first_write": True,
        "protected_fingerprint_occurrences": 35, "protected_unique_paths": 35,
        "canonical_protected_summary_sha256": digest(rows), "protected_fingerprints": rows,
        "author_packet_files": 11, "whole_obligations": 64,
        "accepted_operative_bindings": bindings,
        "author_declared_58_paths_bound_inside_immutable_author_metadata_not_replayed": True,
        "incidental_embedded_unrelated_parent_identity_NOT_direct_file_access": embedded,
        "actual_author_BD_parent_file_or_payload_opened_or_hashed": False,
        "immediate_own_parent": PARENT, "older_own_paths_bound_transitively": 729,
        "no_giant_historical_inventory_recopy_or_recursive_replay": True,
        "mutable_landscape_snapshots_context_only_not_future_guards": [
            fp("problems/2019-B4/research.md"), fp("problems/2019-B4/references.md")],
        "corresponding_NEW_CT_or_WO_peer_material_read_or_hashed": False,
        "mathematical_code_or_constructor_freezer_executed": False,
    })
    print(json.dumps({"baseline": fp(P + "baseline-v1.json"), "protected_paths": 35}))


def check_baseline():
    data = obj(P + "baseline-v1.json")
    rows, bindings, embedded = records()
    assert data["protected_fingerprints"] == rows
    assert data["canonical_protected_summary_sha256"] == digest(rows)
    assert data["accepted_operative_bindings"] == bindings
    assert data["incidental_embedded_unrelated_parent_identity_NOT_direct_file_access"] == embedded
    return data


def labels():
    ledger = raw(P + "ledger-v1.md").decode()
    assert re.findall(r"(?m)^\|(CT-\d{2})\|PASS\.", ledger) == [f"CT-{i:02d}" for i in range(1, 65)]
    issues = raw(P + "issues-v1.md").decode()
    assert re.findall(r"(?m)^\|(CTR1-N\d)\|", issues) == [f"CTR1-N{i}" for i in range(1, 9)]
    main = raw(P + "initial-v1.md").decode()
    assert all(token in main for token in ("CT1", "CT2", "CT3", "CT4", "candidate proof -"))
    source = obj(P + "sources-v1.json")
    assert source["whole_obligations"] == 64
    assert source["substantive_defects"] == source["required_author_repairs"] == source["unresolved_issues"] == 0
    assert source["closed_scope_notes"] == 8
    assert source["root_or_reviewer_supplied_NEW_construction_inference"] is False
    assert source["corresponding_NEW_CT_or_WO_peer_material_read_or_hashed"] is False
    assert source["actual_BD_peer_file_or_payload_read_or_hashed"] is False
    assert source["requested_settings"] == {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True}
    assert source["independently_verified_effective_readback"] is None
    meter = source["authoritative_weekly_telemetry"]
    assert meter["reset_unix"] == 1792874445 and meter["used_percent_TOTAL"] < meter["TOTAL_ceiling"] == 90
    assert meter["automatic_later_window_spending"] is False
    return source


def freeze():
    data = check_baseline()
    source = labels()
    for suffix in PAYLOAD:
        if suffix != "input-validation-v1.json":
            assert raw(P + suffix)
    put("input-validation-v1.json", {
        "verified_at_utc": now(), "metadata_ONLY_NOT_mathematical_test_or_independent_review": True,
        "all35_necessary_protected_paths_unchanged": True,
        "ENTIRE11_author_files_and_ALL64_ordered_review_ledger_labels": True,
        "all8_closed_scope_note_labels_ordered": True,
        "all3_current_accepted_bodies_MDJSON_literal_candidate_suffixes_exact": True,
        "unrelated_author_parent_review_files_opened_or_hashed": False,
        "own_parent_manifest_plus_nine_payloads_unchanged": True,
        "historical_inventory_replayed_or_mathematical_program_executed": False,
        "FULL_generated_readback_and_SEPARATE_readonly_verify_required_before_handoff": True,
    })
    artifacts = [fp(P + suffix) for suffix in PAYLOAD]
    put("manifest-v1.json", {
        "frozen_at_utc": now(),
        "status": "ENTIRE initially blind OTHER WHOLE review1; not coordinator acceptance",
        "whole_obligations": 64,
        "ENTIRE_report_ALL64_ledger_issues_sources_log_code_ALLmetadata_frozen": True,
        "reviewer": "/root/review_2022_complexity_r2",
        "requested_settings": source["requested_settings"], "independently_verified_effective_readback": None,
        "sole_NEW_constructor": "/root/review_2017_coarsening_r1",
        "constructor_excluded": True, "root_supplied_NEW_inference": False,
        "reviewer_constructed_or_supplied_NEW_inference": False,
        "older_roles_disclosed_not_fresh_self_certification": source["older_roles_disclosed"],
        "corresponding_NEW_CT_or_WO_peer_material_read_or_hashed": False,
        "embedded_unrelated_BD_identity_exposure_disclosed_actual_file_not_opened_or_hashed": True,
        "initial_handoff_IDENTITY_ONLY_until_BOTH_ENTIRE_freezes_confirmed": True,
        "review_finding": {"substantive_defects": 0, "required_author_repairs": 0, "unresolved_issues": 0, "closed_scope_notes": 8},
        "high_cut_mass_selected_regime_exact_lambda_or_annual_claim": False,
        "author_main": AUTHOR_MAIN, "author_freeze": AUTHOR_FREEZE,
        "compact_necessary_baseline": fp(P + "baseline-v1.json"),
        "protected_fingerprint_occurrences": 35, "protected_unique_paths": 35,
        "canonical_protected_summary_sha256": data["canonical_protected_summary_sha256"],
        "accepted_operative_bindings": data["accepted_operative_bindings"],
        "immediate_own_parent": PARENT,
        "older_own_paths_bound_transitively": 729,
        "new_review_files_including_manifest": 10,
        "older_plus_new_own_paths_bound_transitively": 739,
        "no_historical_inventory_recopy_or_recursive_replay": True,
        "no_math_code_scan_CAS_test_optimizer_author_source_or_old_freezer_replay": True,
        "no_old_shared_Git_cache_mutation_spawn_download_charge_contact_or_bypass": True,
        "authoritative_weekly_telemetry": source["authoritative_weekly_telemetry"],
        "artifacts": artifacts,
    })
    print(json.dumps({"manifest": fp(P + "manifest-v1.json"), "report": artifacts[0], "new_files": 10}))


def verify():
    data = check_baseline()
    labels()
    manifest = obj(P + "manifest-v1.json")
    assert manifest["whole_obligations"] == 64
    assert manifest["compact_necessary_baseline"] == fp(P + "baseline-v1.json")
    assert manifest["canonical_protected_summary_sha256"] == data["canonical_protected_summary_sha256"]
    assert [row["path"] for row in manifest["artifacts"]] == [P + suffix for suffix in PAYLOAD]
    for record in manifest["artifacts"]:
        check(record)
    print(json.dumps({
        "SEPARATE_readonly_postfreeze_metadata_verification": "PASS",
        "manifest": fp(P + "manifest-v1.json"), "report": manifest["artifacts"][0],
        "whole_obligations": 64, "new_files": 10,
        "necessary_old_paths_unchanged": 35, "own_paths_bound_transitively": 739,
        "mathematical_test_certificate_or_another_review": False,
        "corresponding_NEW_CT_or_WO_or_actual_BD_peer_material_opened_or_hashed": False,
    }))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("baseline", "freeze", "verify"))
    {"baseline": baseline, "freeze": freeze, "verify": verify}[parser.parse_args().mode]()
