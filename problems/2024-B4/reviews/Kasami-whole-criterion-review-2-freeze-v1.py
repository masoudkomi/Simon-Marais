"""Administrative hashes/JSON only; no mathematical computation."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/Kasami-whole-criterion-review-2-"


def read_json(path):
    return json.loads((ROOT / path).read_text())


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked(expected):
    actual = record(expected["path"])
    assert all(actual[key] == value for key, value in expected.items()), (expected, actual)
    return actual


def unique_checked(records):
    result = {}
    for expected in records:
        actual = checked(expected)
        if actual["path"] in result:
            assert result[actual["path"]] == actual
        result[actual["path"]] = actual
    return list(result.values())


target_path = "problems/2024-B4/notes/coordinator-Kasami-whole-criterion-candidate-v1.md"
target_manifest_path = "problems/2024-B4/notes/coordinator-Kasami-whole-criterion-manifest-v1.json"
checked({"path": target_path, "bytes": 7192,
         "sha256": "390d795343eb32a9496aa9a64c054b4809bd400c37c8195264053d343ba180bf"})
checked({"path": target_manifest_path, "bytes": 1202,
         "sha256": "f08044ef0a1a9d8fa38e26f50e2b261d46ef761e68604060f918c5119816a3f3"})
target_manifest = read_json(target_manifest_path)
target_records = unique_checked(target_manifest["records"] + [record(target_manifest_path)])
assert len(target_manifest["records"]) == 4
obligations = read_json("problems/2024-B4/notes/coordinator-Kasami-whole-criterion-obligations-v1.json")
assert [r["id"] for r in obligations["obligations"]] == [f"KC{i:02d}" for i in range(1, 27)]
source = read_json("problems/2024-B4/notes/coordinator-Kasami-whole-criterion-sources-v1.json")
source_records = unique_checked(source["fingerprints"])
assert len(source_records) == 8
additional_scope = [record(path) for path in (
    "problems/2024-B4/reviews/composition-Kasami-acceptance.md",
    "problems/2024-B4/reviews/generalized-Kasami-acceptance.md")]

old_manifest_path = "problems/2019-B4/notes/linear-output-return-r1-freeze-v1.json"
checked({"path": old_manifest_path, "bytes": 3511,
         "sha256": "b1728d67d1101e3c9207fc935919c0cc4bf7c148f3af3220344729e5554b2deb"})
old_manifest = read_json(old_manifest_path)
old_validation = read_json("problems/2019-B4/notes/linear-output-return-r1-input-validation-v1.json")
earlier = unique_checked(old_validation["earlier_unique_records_preserved"]
                         + old_manifest["artifacts"] + [record(old_manifest_path)])
assert len(earlier) == 238

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
validation = {
    "validated_at_utc": now,
    "administrative_integrity_only": True,
    "exact_target_and_all_four_declared_records": target_records,
    "all_eight_author_source_fingerprints": source_records,
    "additional_complete_read_scope_records": additional_scope,
    "complete_CP_and_GK_bodies_read": True,
    "twenty_six_submitted_obligations_present": True,
    "earlier_unique_records_preserved": earlier,
    "earlier_unique_count": len(earlier),
    "old_CP1_authorship_disclosed": True,
    "fresh_review_of_NEW_KC_not_old_CP1": True,
    "peer_new_KC_findings_read_before_initial_freeze": False,
    "next_2025_return_research_started_before_initial_freeze": False,
    "mathematical_program_CAS_scan_sampling_or_author_rerun": False,
    "shared_Git_spawning_contact_charge_or_bypass": False,
}
validation_path = PREFIX + "input-validation-v1.json"
(ROOT / validation_path).write_text(json.dumps(validation, indent=2) + "\n")
artifacts = [record(PREFIX + suffix) for suffix in
             ("initial-v1.md", "issues-v1.md", "source-checks-v1.md",
              "freeze-v1.py", "input-validation-v1.json")]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind whole review2; no substantive objection found; coordinator reconciliation required",
    "reviewer": "/root/review_2017_coarsening_r1",
    "constructor_of_NEW_KC": False,
    "constructor_of_OLD_accepted_CP1_dependency": True,
    "old_dependency_not_independently_reaudited_by_its_author": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": record(target_path),
    "target_manifest": record(target_manifest_path),
    "whole_submitted_obligations_audited": 26,
    "open_substantive_issues": 0,
    "peer_findings_read_before_initial_freeze": False,
    "scope": "Every k>=2,q=2^k,odd n>=3: WHOLE phi_(q^2-q+1)|phi_n overF2 iff n=(q^(2r+1)+1)/(q+1),r>=1; accepted CP1/GK inputs",
    "arbitrary_component_full_reducibility_annual_or_novelty_claim": False,
    "external_monodromy_factor_or_group_theorem_imported": False,
    "mathematical_computation_or_CAS": False,
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "last_direct_weekly_telemetry": {"at_utc": "2026-10-17 11:59:03 UTC",
                                      "total_used_percent": 36, "window_minutes": 10080,
                                      "reset_unix": 1792745187, "total_ceiling_percent": 90,
                                      "integration_reserve": True},
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
manifest_path = PREFIX + "manifest-v1.json"
(ROOT / manifest_path).write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"manifest": record(manifest_path), "artifacts": artifacts,
                  "earlier_unchanged": len(earlier), "whole_obligations": 26,
                  "substantive_issues": 0}, indent=2))
