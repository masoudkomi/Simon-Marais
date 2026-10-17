"""One-time whole initial-review freeze: byte checks and serialization only."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/reasoning-return-r3-review-2-"
PEER_PREFIX = "problems/2024-B4/reviews/reasoning-return-r3-review-1-"


def fingerprint(path):
    assert not path.startswith(PEER_PREFIX), path
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
    assert not path.startswith(PEER_PREFIX), path
    return json.loads((ROOT / path).read_text())


def create_json(suffix, value):
    path = PREFIX + suffix
    with (ROOT / path).open("x") as stream:
        json.dump(value, stream, indent=2)
        stream.write("\n")
    return path


def frozen_fingerprints(value):
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and isinstance(value.get("sha256"), str):
            assert len(value["sha256"]) == 64, value
            yield value
        for item in value.values():
            yield from frozen_fingerprints(item)
    elif isinstance(value, list):
        for item in value:
            yield from frozen_fingerprints(item)


now = datetime.now(timezone.utc).isoformat()
constructor_path = "problems/2024-B4/notes/reasoning-return-r3-freeze-v1.json"
constructor_fp = check({"path": constructor_path, "bytes": 4596,
                        "sha256": "e2c1b451f486db75597fbd6b99c970f85a7ed70528bebd032e2d7168fbcf7741"})
constructor_checks = [check(row) for row in read_json(constructor_path)["artifacts"]]
assert len(constructor_checks) == 15
main_fp = check({"path": "problems/2024-B4/notes/reasoning-return-r3-candidate-v1.md",
                 "bytes": 15010,
                 "sha256": "cff70e9b104a48613712d0f2920157f29a5c20b56fb26055de829984e11fb021"})
constructor_validation = read_json("problems/2024-B4/notes/reasoning-return-r3-input-validation-v1.json")
nested_checks = [check(row) for row in frozen_fingerprints(constructor_validation)]
assert len(constructor_validation["earlier_unique_records_preserved"]) == 165

criterion = check({"path": "problems/2024-B4/notes/zero-automaton-criterion-reviewed-v1.1.md",
                   "bytes": 16607,
                   "sha256": "362f2541b2bb1ab1e22ba768b41d55e7282f08631b0ad39522682244d213f226"})
criterion_acceptance = fingerprint("problems/2024-B4/reviews/criterion-acceptance.md")

prior_path = "problems/2017-B4/reviews/UR4-assembly-review-1-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "85afd2d30497a3e578b1b4d27a5e71836951b7590d81ac747322f1f1aa2792b0"})
prior_checks = [check(row) for row in read_json(prior_path)["records"]]
prior_validation = read_json("problems/2017-B4/reviews/UR4-assembly-review-1-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 32
older.append({"manifest": prior_fp, "checks": prior_checks})

ledger = read_json(PREFIX + "issues-v1.json")
assert len(ledger["checks"]) == 38
assert ledger["open_substantive_issues"] == []
assert ledger["required_author_repairs"] == []
covered = {obligation for row in ledger["checks"] for obligation in row["obligations"]}
assert covered == {f"CP-O{i}" for i in range(1, 17)}

job = read_json("problems/2024-B4/notes/reasoning-return-r3-kasami-target-job-v1.json")
completion = read_json("problems/2024-B4/notes/reasoning-return-r3-kasami-target-completion-v1.json")
assert job["child_pid"] == completion["child_pid"] == 95340
assert job["parent_pid"] == 95339 and job["timeout_seconds"] == 10
assert completion["return_code"] == 0 and completion["child_reaped"]
assert not completion["timed_out"]
for name in ["stdout", "stderr"]:
    fp = fingerprint(f"problems/2024-B4/notes/reasoning-return-r3-kasami-target-{name}-v1.txt")
    assert fp["sha256"] == completion[f"{name}_sha256"]

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "constructor_manifest": constructor_fp,
    "constructor_records": constructor_checks,
    "main_candidate": main_fp,
    "all_fifteen_constructor_artifacts_unchanged": True,
    "constructor_declared_nested_fingerprints": nested_checks,
    "constructor_earlier_unique_records_preserved": 165,
    "exact_accepted_phi13_criterion": criterion,
    "accepted_phi13_scope_record": criterion_acceptance,
    "older_own_packets": older,
    "all_thirty_three_older_own_packets_unchanged": True,
    "peer_CP_review_or_findings_read": False,
    "prior_T1_T4_C7_C11_authorship_disclosed": True,
    "new_CP_construction_contribution": False,
    "saved_q8_job_completion_hash_consistency_checked": True,
    "q8_math_code_rerun": False,
    "mathematical_program_enumeration_or_CAS": False,
    "source_byte_hashes_imply_full_text_read": False,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "constructor_records_checked": 15,
    "constructor_nested_fingerprint_rows_checked": len(nested_checks),
    "constructor_nested_unique_paths": len({row["path"] for row in nested_checks}),
    "older_own_packets_checked": 33,
    "ledger_rows": 38,
    "constructor_obligations_covered": 16,
    "all_fingerprints_match": True,
    "open_substantive_issues": [],
    "whole_initial_review_complete_before_disclosure": True,
    "peer_findings_read_before_freeze": False,
    "candidate_or_shared_mutation": False,
    "git_operations": False,
})
record_paths = [PREFIX + suffix for suffix in [
    "initial-v1.md", "issues-v1.json", "source-checks-v1.md", "freeze-v1.py",
]] + [validation_path, output_path]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "initially blind independent whole review; no substantive defect found in stated CP1–CP3",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": main_fp["sha256"],
    "constructor_manifest_sha256": constructor_fp["sha256"],
    "whole_claims": ["CP1 all odd d,n>=3 whole-divisor composition equivalence",
                     "CP2 all q=2^k,k>=1 Frobenius composition identity",
                     "CP3 qualifying k>=3 family and absence of whole phi13"],
    "per_inference_ledger_rows": 38,
    "constructor_obligations_covered": 16,
    "substantive_objections": [],
    "required_author_repairs": [],
    "prior_T1_T4_C7_C11_authorship_boundary_disclosed": True,
    "new_CP_constructor_or_contributor": False,
    "peer_findings_read_before_freeze": False,
    "q8_corroboration_used_as_unrestricted_proof": False,
    "original_absolute_factor_theorem_or_APN_classification_import": False,
    "all_factor_classification_arbitrary_m_or_novelty_claim": False,
    "mathematical_program_enumeration_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 30,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2024-B4/reviews/reasoning-return-r3-review-2-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "constructor_records_checked": 15,
                  "constructor_nested_rows_checked": len(nested_checks),
                  "older_own_packets_checked": 33}, indent=2))
