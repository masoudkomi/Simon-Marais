#!/usr/bin/env python3
"""Affected review preservation only; no mathematical program or author rerun."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-1-reaudit-v2-"
T = "problems/2024-B4/notes/cofactor-Frobenius-r5-"
OLD = "problems/2024-B4/reviews/cofactor-Frobenius-r5-review-1-manifest-v1.json"
PARENT = "problems/2022-B4/reviews/reasoning-fiber-return-r5-review-2-manifest-v1.json"
EXPECTED = [
    {"path": T + "candidate-v2.md", "bytes": 13006,
     "sha256": "329b975a7f8fe7456f9794a2170dc443396fb1a2b0143cc61ac9ddd027beb47e"},
    {"path": T + "repair-freeze-v2.json", "bytes": 8397,
     "sha256": "aaa1da5e9143787046b0286dc7de75f04107d8ec209deadda65d53b5e1cc9885"},
    {"path": OLD, "bytes": 6800,
     "sha256": "b3af3d1cd3372c4181753c4cc3724b9c99300b596d5dcdebd3bd398374cd0667"},
    {"path": PARENT, "bytes": 10070,
     "sha256": "3b031cd70d87370a1ad636d0c26273992d26401b62954dcb1cff5b31a64a7a96"},
]
HEADER = "> Author repair v2, 18 October2026 UTC: candidate proof - unverified\n> pending BOTH affected reaudits. Corrects the odd-s residue from2 to1\n> modulo3, and assigns the s3 failure to the off-diagonal coprimality\n> step; its diagonal exclusion still holds. R1 N1/N2 and R2 N1 supplied\n> these corrective observations after BOTH entire blind audits froze.\n> No theorem/domain/threshold is strengthened. All original bytes remain.\n\n"
CHANGES = [
    ("Since s is odd,2^s-1 is2 modulo3. The order3 cannot divide Q-1;",
     "Since s is odd,2^s is2 modulo3, so2^s-1 is1 modulo3. The order3 cannot divide Q-1;"),
    ("need not have length1 or s; for s3 a permutation can have order3\nand the diagonal cube-root obstruction changes. No such case is\nsilently included.",
     "need not have length1 or s; for s3 a permutation can have order3\nand the off-diagonal coprimality step fails. The diagonal cube-root\nexclusion still holds at s3, since3 does not divide7. No such case is\nsilently included."),
]
LOG_CHANGE = ("   permutation argument and diagonal cube-root obstruction change.",
              "   permutation argument fails; the diagonal cube-root exclusion still holds.")
CONTENT = ["initial.md", "ledger.md", "issues.md", "sources.md", "sources.json", "worklog.md", "freeze.py"]
GENERATED = ["baseline.json", "metadata.json", "input-validation.json"]


def now():
    return datetime.now(timezone.utc).isoformat()


def path(name):
    assert "cofactor-Frobenius-r5-review-2-reaudit" not in name, name
    value = (ROOT / name).resolve()
    assert value.is_relative_to(ROOT), name
    return value


def raw(name):
    return path(name).read_bytes()


def obj(name):
    return json.loads(raw(name))


def fp(name):
    value = raw(name)
    return {"path": name, "bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}


def check(row):
    record = {key: row[key] for key in ("path", "bytes", "sha256")}
    assert fp(record["path"]) == record, record["path"]
    return record


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def summary(rows):
    unique = {}
    for row in rows:
        record = check(row)
        assert unique.setdefault(record["path"], record) == record
    return {"occurrences": len(rows), "unique_paths": len(unique),
            "sha256": digest([unique[key] for key in sorted(unique)])}


def put(suffix, value):
    with path(P + suffix).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")


def text_diff_checks():
    value = raw(T + "candidate-v1.md").decode()
    for old, new in CHANGES:
        assert value.count(old) == 1
        value = value.replace(old, new)
    assert raw(T + "candidate-v2.md").decode() == HEADER + value
    value = raw(T + "failures-worklog-v1.md").decode()
    assert value.count(LOG_CHANGE[0]) == 1
    assert raw(T + "failures-worklog-v2.md").decode() == HEADER + value.replace(*LOG_CHANGE)
    return {"complete_main_header_plus_exactly_two_changes": True,
            "complete_log_header_plus_exactly_one_change": True,
            "no_author_code_executed": True}


def current():
    for row in EXPECTED:
        check(row)
    author = obj(T + "repair-freeze-v2.json")
    original = obj(T + "freeze-v1.json")
    old_base = obj(T + "baseline-v1.json")
    assert author["original_whole_obligations"] == 32 and len(author["artifacts"]) == 4
    old_rows = [check(row) for row in author["old_current_guards"]]
    assert len(old_rows) == 30 and len({row["path"] for row in old_rows}) == author["old_guard_paths"] == 30
    original_rows = [fp(T + "freeze-v1.json")] + [check(row) for row in original["artifacts"]]
    assert len(original_rows) == 9
    protected = [check(row) for row in old_base["protected"]]
    assert len(protected) == 23
    new_rows = [fp(T + "repair-freeze-v2.json")] + [check(row) for row in author["artifacts"]]
    bindings, accepted_rows = [], []
    for binding in old_base["accepted_operative_bindings"]:
        authority, body, candidate = (check(binding[key]) for key in ("authority", "accepted_body", "candidate"))
        md = fp(authority["path"].removesuffix(".json") + ".md")
        assert raw(body["path"]).endswith(raw(candidate["path"]))
        value = obj(authority["path"])
        assert value["unresolved_substantive_issues"] == 0 and value["repair_required"] is False
        accepted_rows += [authority, md, body, candidate]
        bindings.append({"authority": authority, "authority_MD": md, "accepted_body": body,
                         "candidate": candidate, "exact_candidate_suffix": True,
                         "historical_occurrences_bound_not_replayed": value["record_occurrences_verified"],
                         "historical_paths_bound_not_replayed": value["unique_paths_verified"]})
    assert len(bindings) == 2
    parent = obj(PARENT)
    assert parent["whole_obligations"] == 48 and len(parent["artifacts"]) == 10
    parent_rows = [fp(PARENT)] + [check(row) for row in parent["artifacts"]]
    original_own = obj(OLD)
    own_rows = [fp(OLD)] + [check(row) for row in original_own["artifacts"]]
    assert len(own_rows) == 11
    all_rows = old_rows + original_rows + protected + new_rows + accepted_rows + parent_rows + own_rows
    result = {
        "target_full_v2": fp(T + "candidate-v2.md"),
        "author_five_file_repair_freeze": fp(T + "repair-freeze-v2.json"),
        "all_five_author_repair_files_exact": True,
        "author_thirty_old_guards": summary(old_rows),
        "original_nine_author_files": summary(original_rows),
        "original_twenty_three_necessary_current_guards": summary(protected),
        "exact_text_diff_checks": text_diff_checks(),
        "accepted_current_bindings": bindings,
        "original_own_whole_R1_bound": {"identity": fp(OLD), "all11_summary": summary(own_rows),
            "older_summary_bound_not_replayed": original_own["current_inputs_and_payloads_summary"]},
        "immediate_own_CF_parent_bound": {"identity": fp(PARENT), "all11_summary": summary(parent_rows),
            "older_summary_bound_not_replayed": parent["current_inputs_and_payloads_summary"],
            "not_R5_mathematical_premise": True},
        "current_summary": summary(all_rows),
        "all_old_guard_details_remain_in_exact_bound_author_metadata_not_recopied": True,
    }
    return result, all_rows


def baseline():
    value, _ = current()
    value.update({"captured_utc": now(), "administrative_only": True,
                  "no_corresponding_NEW_R2_reaudit_access": True,
                  "compact_immutable_parent_bindings_no_recursive_inventory_replay": True})
    put("baseline.json", value)
    print(json.dumps({"mode": "baseline", "baseline": fp(P + "baseline.json"), "current": value["current_summary"]}))


def validate_baseline():
    base = obj(P + "baseline.json")
    value, rows = current()
    for key in value:
        assert base[key] == value[key], key
    return base, rows


def freeze():
    base, rows = validate_baseline()
    wanted = [f"CF-{index:02d}" for index in range(1, 33)]
    for name in (T + "obligations-v1.md", P + "ledger.md"):
        assert re.findall(r"^\| (CF-\d+) \|", raw(name).decode(), re.M) == wanted
    assert re.findall(r"^\| (RV2-\d+) \|", raw(P + "ledger.md").decode(), re.M) == [f"RV2-{index:02d}" for index in range(1, 9)]
    put("metadata.json", {
        "created_utc": now(), "status": "ENTIRE affected OTHER WHOLE R1 recommendation; not promotion",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "root_sole_NEW_constructor_excluded": True,
        "original_whole_obligations": 32, "additional_repair_checks": 8,
        "both_original_literal_notes_resolved_in_AUTHOR_v2": True,
        "substantive_defects": 0, "unresolved_issues": 0, "further_required_author_repairs": 0,
        "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max", "inherited": True},
        "independently_verified_effective_settings": None,
        "no_corresponding_NEW_R2_reaudit_finding_file_hash_metadata_access_through_ENTIRE_freeze": True,
        "identity_only_until_BOTH_ENTIRE_affected_packets_confirmed": True,
        "old_roles_disclosed_no_fresh_self_recertification": True,
        "no_math_code_CAS_scan_author_source_or_certificate_rerun_or_native_mathematical_child": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass_tool_wait_or_pending_job": True,
        "latest_own_authoritative_telemetry": obj(P + "sources.json")["latest_own_authoritative_telemetry"],
    })
    put("input-validation.json", {
        "checked_utc": now(), "administrative_only_not_mathematical_validation": True,
        "all_five_author_repair_files_thirty_old_guards_original_nine_twenty_three_current_guards_exact": True,
        "two_accepted_suffixes_original_own_R1_and_own_CF_parent_exact": True,
        "all32_original_labels_and_eight_repair_labels_once_in_order": True,
        "exact_full_main_and_log_diff": base["exact_text_diff_checks"],
        "current_summary": summary(rows), "errors": [],
    })
    artifacts = [fp(P + suffix) for suffix in CONTENT + GENERATED]
    put("manifest.json", {
        "frozen_utc": now(), "status": "ENTIRE affected OTHER WHOLE R1 recommendation; not promotion",
        "reviewer": "/root/review_2021_reasoning_j15_r2", "root_sole_NEW_constructor_excluded": True,
        "original_whole_obligations": 32, "additional_repair_checks": 8,
        "both_original_literal_notes_resolved_in_AUTHOR_v2": True,
        "substantive_defects": 0, "unresolved_issues": 0, "further_required_author_repairs": 0,
        "exact_scope": "unchanged R5A-R5D for ordinary PRIME s>=5,k>=2; Q32 everyk>=2 whole absolute irreducibility; only strict reverse of sufficient bound",
        "no_s3_composite_k1_all_prime_k2_general_annual_or_novelty_claim": True,
        "ENTIRE_report_ALL32_plus8_ledger_issues_sources_log_code_ALLmetadata_complete": True,
        "no_corresponding_NEW_R2_reaudit_finding_file_hash_metadata_access_through_ENTIRE_freeze": True,
        "identity_only_until_BOTH_ENTIRE_affected_packets_confirmed": True,
        "old_roles_disclosed_no_fresh_self_recertification": True,
        "no_mathematical_code_CAS_scan_author_source_or_certificate_rerun": True,
        "no_Git_shared_old_cache_write_spawn_charge_contact_bypass_wait_or_native_mathematical_child": True,
        "baseline": fp(P + "baseline.json"), "target_full_v2": base["target_full_v2"],
        "author_repair_freeze": base["author_five_file_repair_freeze"],
        "exact_text_diff_checks": base["exact_text_diff_checks"],
        "accepted_current_bindings": base["accepted_current_bindings"],
        "original_own_whole_R1_bound": base["original_own_whole_R1_bound"],
        "immediate_own_CF_parent_bound": base["immediate_own_CF_parent_bound"],
        "compact_old_guard_summaries_and_details_bound_by_exact_author_metadata": True,
        "current_inputs_and_payloads_summary": summary(rows + artifacts),
        "payloads": len(artifacts), "files_including_manifest": len(artifacts) + 1,
        "artifacts": artifacts,
        "ENTIRE_generated_metadata_full_readback_then_SEPARATE_postverification_required": True,
    })
    print(json.dumps({"mode": "freeze", "manifest": fp(P + "manifest.json"),
                      "initial": fp(P + "initial.md"), "files": len(artifacts) + 1}))


def verify():
    base, rows = validate_baseline()
    value = obj(P + "manifest.json")
    assert value["original_whole_obligations"] == 32 and value["additional_repair_checks"] == 8
    assert value["files_including_manifest"] == 11 and len(value["artifacts"]) == 10
    for row in value["artifacts"]:
        check(row)
    assert value["exact_text_diff_checks"] == text_diff_checks()
    assert value["accepted_current_bindings"] == base["accepted_current_bindings"]
    assert value["current_inputs_and_payloads_summary"] == summary(rows + value["artifacts"])
    print(json.dumps({"mode": "verify", "all_match": True, "all32_plus8": True,
                      "manifest": fp(P + "manifest.json"), "initial": fp(P + "initial.md"),
                      "files": 11, "current": value["current_inputs_and_payloads_summary"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--baseline", action="store_true")
    group.add_argument("--freeze", action="store_true")
    group.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    if args.baseline:
        baseline()
    elif args.freeze:
        freeze()
    else:
        verify()
