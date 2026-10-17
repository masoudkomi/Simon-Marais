"""Administrative fingerprinting only; no mathematical computation."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/necessary-valuation-review-2-"


def read_json(path):
    return json.loads((ROOT / path).read_text())


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked(expected):
    actual = record(expected["path"])
    assert actual == {key: expected[key] for key in actual}, (expected, actual)
    return actual


def unique_checked(records):
    result = {}
    for expected in records:
        actual = checked(expected)
        if actual["path"] in result:
            assert result[actual["path"]] == actual
        result[actual["path"]] = actual
    return list(result.values())


target_path = "problems/2024-B4/notes/coordinator-Kasami-necessary-valuation-v1.md"
target_manifest_path = "problems/2024-B4/notes/coordinator-Kasami-necessary-valuation-manifest-v1.json"
checked({"path": target_path, "bytes": 3446,
         "sha256": "5b772b77f821c3e3b2f7b04a22c0f9d3609f85942e9cd3d3a0d13104cbc118a4"})
checked({"path": target_manifest_path, "bytes": 1363,
         "sha256": "005a5ea65ac2b7da94ec085c3b6d93ac7938f2102cd5b1af79f569012b6e2ac8"})
target_manifest = read_json(target_manifest_path)
target_records = unique_checked(target_manifest["records"] + [record(target_manifest_path)])
assert len(target_manifest["records"]) == 4
obligations = read_json("problems/2024-B4/notes/coordinator-Kasami-necessary-valuation-obligations-v1.json")
assert [r["id"] for r in obligations["obligations"]] == [f"O{i:02d}" for i in range(1, 12)]
source = read_json("problems/2024-B4/notes/coordinator-Kasami-necessary-valuation-sources-v1.json")
premises = unique_checked(source["input_fingerprints"])
scope_records = [record("AGENTS.md"), record("problems/2024-B4/statement.md")]

old_manifest_path = "problems/2021-B4/notes/reasoning-return-r5-freeze-v1.json"
checked({"path": old_manifest_path, "bytes": 3592,
         "sha256": "1626fa3981c78eb04f7fe41fc5a725b2500de0cf1647e7324941c6a5f3671533"})
old_manifest = read_json(old_manifest_path)
old_validation = read_json("problems/2021-B4/notes/reasoning-return-r5-input-validation-v1.json")
earlier = unique_checked(old_validation["earlier_unique_records_preserved"]
                         + old_manifest["artifacts"] + [record(old_manifest_path)])
assert len(earlier) == 211

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
validation = {
    "validated_at_utc": now,
    "administrative_integrity_only": True,
    "exact_target_and_all_four_declared_records": target_records,
    "complete_accepted_CP1_body_and_scope_read": premises,
    "protocol_and_official_normalization": scope_records,
    "eleven_submitted_obligations_present": True,
    "earlier_unique_records_preserved": earlier,
    "earlier_unique_count": len(earlier),
    "old_CP1_authorship_disclosed": True,
    "this_is_fresh_review_of_new_NV_not_old_CP1": True,
    "peer_new_NV_findings_read_before_initial_freeze": False,
    "separate_2025_candidate_started_before_this_freeze": False,
    "mathematical_program_CAS_scan_sampling_or_certificate_rerun": False,
    "shared_Git_spawning_contact_charge_or_bypass": False,
}
validation_path = PREFIX + "input-validation-v1.json"
(ROOT / validation_path).write_text(json.dumps(validation, indent=2) + "\n")
artifacts = [record(PREFIX + suffix) for suffix in
             ("initial-v1.md", "issues-v1.md", "source-checks-v1.md",
              "freeze-v1.py", "input-validation-v1.json")]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind whole review 2; no substantive objection found; coordinator reconciliation required",
    "reviewer": "/root/review_2017_coarsening_r1",
    "constructor_of_NEW_NV": False,
    "constructor_of_OLD_accepted_CP1_dependency": True,
    "old_dependency_not_independently_reaudited_by_its_author": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": record(target_path),
    "target_manifest": record(target_manifest_path),
    "whole_submitted_obligations_audited": 11,
    "open_substantive_issues": 0,
    "peer_findings_read_before_initial_freeze": False,
    "candidate_scope": "q=2^k,k>=2, odd n>=3: WHOLE phi_(q^2-q+1)|phi_n implies v2(n-1)=k",
    "converse_full_progression_annual_classification_or_novelty_claim": False,
    "mathematical_computation_or_CAS": False,
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "last_direct_weekly_telemetry": {"at_utc": "2026-10-17 11:29:38 UTC", "total_used_percent": 34,
                                      "reset_unix": 1792745187, "total_ceiling_percent": 90,
                                      "integration_reserve": True},
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
manifest_path = PREFIX + "manifest-v1.json"
(ROOT / manifest_path).write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"manifest": record(manifest_path), "artifacts": artifacts,
                  "earlier_unchanged": len(earlier), "whole_obligations": 11,
                  "substantive_issues": 0}, indent=2))
