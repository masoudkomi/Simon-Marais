"""One-time blind whole-review freeze; administrative hashes only."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/generalized-Kasami-review-1-"
PEER = "problems/2024-B4/reviews/generalized-Kasami-review-2-"


def fingerprint(path):
    assert not path.startswith(PEER), path
    assert "allD-global" not in path and "global-induction" not in path, path
    payload = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest()}


def check(expected):
    actual = fingerprint(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    return dict(actual, matches=True)


def read_json(path):
    assert not path.startswith(PEER), path
    return json.loads((ROOT / path).read_text())


def create_json(suffix, payload):
    path = PREFIX + suffix
    with (ROOT / path).open("x") as stream:
        json.dump(payload, stream, indent=2)
        stream.write("\n")
    return path


now = datetime.now(timezone.utc).isoformat()
constructor_path = "problems/2024-B4/notes/coordinator-generalized-Kasami-r1-manifest-v1.json"
constructor_fp = check({"path": constructor_path, "bytes": 2042,
                        "sha256": "50c3269d28a49327e28e216a857fdb711dae8875cab127645bc4081f2ac9ec65"})
constructor_checks = [check(row) for row in read_json(constructor_path)["records"]]
assert len(constructor_checks) == 6
assert constructor_checks[0]["sha256"] == "f99bae5f5d3877e556a30347a38616daf6b54fde300ae60543f849893a7dc4b8"
constructor_validation = read_json("problems/2024-B4/notes/coordinator-generalized-Kasami-r1-input-validation-v1.json")
nested_checks = [check(row) for row in constructor_validation["records"]]
assert len(nested_checks) == 417
assert len({row["path"] for row in nested_checks}) == 214
cache_check = check(constructor_validation["motivation_cache_only_not_new_theorem_premise"])

cp_path = "problems/2024-B4/proofs/reviewed-composition-Kasami-v1.1.md"
cp_check = check({"path": cp_path,
                  "sha256": "f1e82d443b5ac997889c7a7f7f340437f8401516cccf9516eac132558df220c5"})
cp_old = "problems/2024-B4/notes/reasoning-return-r3-candidate-v1.md"
assert (ROOT / cp_path).read_bytes().endswith((ROOT / cp_old).read_bytes())
phi13_check = check({"path": "problems/2024-B4/notes/zero-automaton-criterion-reviewed-v1.1.md",
                     "sha256": "362f2541b2bb1ab1e22ba768b41d55e7282f08631b0ad39522682244d213f226"})
scope_checks = [fingerprint("problems/2024-B4/reviews/" + name) for name in [
    "composition-Kasami-acceptance.md", "composition-Kasami-acceptance.json",
    "criterion-acceptance.md", "criterion-acceptance.json",
]]

prior_path = "problems/2019-B4/notes/reasoning-return-r3-manifest-v1.json"
prior_fp = check({"path": prior_path, "bytes": 3091,
                  "sha256": "6e9dd78603daa564999d083f4234f2e83d6aa063d738c6936704eaca3f33b9cb"})
prior_checks = [check(row) for row in read_json(prior_path)["records"]]
prior_validation = read_json("problems/2019-B4/notes/reasoning-return-r3-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 34
older.append({"manifest": prior_fp, "checks": prior_checks})

ledger = read_json(PREFIX + "issues-v1.json")
assert len(ledger["checks"]) == 30
assert ledger["open_substantive_issues"] == []
assert ledger["required_author_repairs"] == []
covered = {obligation for row in ledger["checks"] for obligation in row["obligations"]}
assert covered == {f"GK-O{i}" for i in range(1, 17)}

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "constructor_manifest": constructor_fp,
    "constructor_records": constructor_checks,
    "constructor_declared_input_records": nested_checks,
    "constructor_input_occurrences": 417,
    "constructor_input_unique_paths": 214,
    "motivation_cache_byte_check_not_theorem_import": cache_check,
    "accepted_CP_complete_body": cp_check,
    "accepted_CP_exact_original_suffix": True,
    "accepted_phi13_complete_body": phi13_check,
    "accepted_scope_records": scope_checks,
    "older_own_packets": older,
    "all_thirty_five_older_own_packets_unchanged": True,
    "peer_GK_findings_read": False,
    "future_allD_global_packet_read": False,
    "prior_T1_T4_C7_C11_and_CP_R2_role_disclosed": True,
    "new_GK_contribution": False,
    "mathematical_code_CAS_scan_or_certificate_rerun": False,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "constructor_records_checked": 6,
    "constructor_input_occurrences_checked": 417,
    "constructor_input_paths_checked": 214,
    "separate_motivation_cache_record_checked": True,
    "older_own_packets_checked": 35,
    "ledger_rows": 30,
    "constructor_obligations_covered": 16,
    "all_fingerprints_match": True,
    "open_substantive_issues": [],
    "complete_whole_initial_before_disclosure": True,
    "peer_findings_read_before_freeze": False,
    "candidate_shared_or_old_file_mutation": False,
    "git_operations_or_spawning": False,
})
records = [PREFIX + name for name in [
    "initial-v1.md", "issues-v1.json", "source-checks-v1.md", "freeze-v1.py",
]] + [validation_path, output_path]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "initially blind whole independent review; no substantive defect found in stated GK1–GK3",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": "f99bae5f5d3877e556a30347a38616daf6b54fde300ae60543f849893a7dc4b8",
    "constructor_manifest_sha256": constructor_fp["sha256"],
    "whole_claims": ["GK1 all-q all-index recurrence and polynomial degrees",
                     "GK2 genuine fixed-q infinite whole-divisor families",
                     "GK3 exact scoped absence of whole phi13"],
    "per_inference_ledger_rows": 30,
    "constructor_obligations_covered": 16,
    "substantive_objections": [],
    "required_author_repairs": [],
    "prior_T1_T4_C7_C11_authorship_and_CP_R2_role_disclosed": True,
    "new_GK_constructor_or_contributor": False,
    "peer_findings_read_before_freeze": False,
    "future_allD_global_packet_read": False,
    "mathematical_code_CAS_scan_or_certificate_rerun": False,
    "external_factor_monodromy_APN_theorem_import": False,
    "full_classification_or_novelty_claim": False,
    "candidate_shared_old_files_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "weekly_total_used_percent": 31,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2024-B4/reviews/generalized-Kasami-review-1-freeze-v1.py",
    "records": [fingerprint(path) for path in records],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(records),
                  "constructor_records_checked": 6,
                  "input_occurrences_checked": 417,
                  "older_own_packets_preserved": 35}, indent=2))
