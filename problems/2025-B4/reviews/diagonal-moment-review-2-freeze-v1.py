"""Administrative review freeze only; no mathematical computation."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/diagonal-moment-review-2-"


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


target_path = "problems/2025-B4/notes/coordinator-diagonal-moment-candidate-v2.md"
target_manifest_path = "problems/2025-B4/notes/coordinator-diagonal-moment-manifest-v1.json"
checked({"path": target_path, "bytes": 7096,
         "sha256": "dae1907e2c3afe744ede7ffc89321d560ebbfab326afd78786f30dac960fcb2f"})
checked({"path": target_manifest_path, "bytes": 1545,
         "sha256": "5d0d897d3ff89828e26d16919357bf0d283866bb3bb97b7aa9f1277b3a3d3654"})
target_manifest = read_json(target_manifest_path)
target_records = unique_checked(target_manifest["records"] + [record(target_manifest_path)])
assert len(target_manifest["records"]) == 4
obligations = read_json("problems/2025-B4/notes/coordinator-diagonal-moment-obligations-v1.json")
assert [r["id"] for r in obligations["obligations"]] == [f"O{i:02d}" for i in range(1, 15)]
source = read_json("problems/2025-B4/notes/coordinator-diagonal-moment-sources-v1.json")
source_records = unique_checked(source["input_fingerprints"])
assert len(source_records) == 6
assert source["original"]["binary_sha256"] is None
assert source["new_external_theorem"] is False
local_context = [record(path) for path in (
    "AGENTS.md", "problems/2025-B4/statement.md", "problems/2025-B4/references.md",
    "problems/2025-B4/proofs/reviewed-diagonal-firstcase-v1.1.md")]

old_manifest_path = "problems/2024-B4/reviews/necessary-valuation-review-2-manifest-v1.json"
checked({"path": old_manifest_path, "bytes": 2771,
         "sha256": "9ffe5ba81c38ef6152de5370a094d81d34e70093f665477e4df25dcd254bc65b"})
old_manifest = read_json(old_manifest_path)
old_validation = read_json("problems/2024-B4/reviews/necessary-valuation-review-2-input-validation-v1.json")
earlier = unique_checked(old_validation["earlier_unique_records_preserved"]
                         + old_manifest["artifacts"] + [record(old_manifest_path)])
assert len(earlier) == 217

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
validation = {
    "validated_at_utc": now,
    "administrative_integrity_only": True,
    "exact_target_and_all_four_declared_records": target_records,
    "four_earlier_moment_notes_appendix_and_cached_primary_PDF": source_records,
    "complete_read_local_context": local_context,
    "fourteen_submitted_obligations_present": True,
    "earlier_unique_records_preserved": earlier,
    "earlier_unique_count": len(earlier),
    "original_author_upload_binary_hash": None,
    "original_web_viewer_hash_not_invented": True,
    "later_primary_cache_identity_checked": True,
    "constructor_of_MS1_to_MS5": False,
    "peer_new_moment_findings_read_before_initial_freeze": False,
    "prior_NV_initial_frozen_before_this_task_started": True,
    "mathematical_program_CAS_scan_sampling_or_certificate_rerun": False,
    "read_only_PDF_text_extraction_is_not_math_computation": True,
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
    "constructor_of_MS1_to_MS5": False,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": record(target_path),
    "target_manifest": record(target_manifest_path),
    "whole_submitted_obligations_audited": 14,
    "open_substantive_issues": 0,
    "peer_findings_read_before_initial_freeze": False,
    "prior_NV_initial_frozen_before_starting_this_separate_review": True,
    "claims_reviewed": ["MS1 reciprocal residue separation", "MS2 Fourier faithfulness and cross-list sets",
                        "MS3 inverse moment sufficient for freeness", "MS4 exact Fuchsian inverse moment",
                        "MS5 two concrete first-case elements at p>7"],
    "second_case_selection_singular_system_cancellation_delta_or_Diophantine_exclusion_accepted": False,
    "full_annual_classification_or_novelty_claim": False,
    "mathematical_computation_or_CAS": False,
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "last_direct_weekly_telemetry": {"at_utc": "2026-10-17 11:36:42 UTC",
                                      "total_used_percent": 34, "window_minutes": 10080,
                                      "reset_unix": 1792745187, "total_ceiling_percent": 90,
                                      "integration_reserve": True},
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
manifest_path = PREFIX + "manifest-v1.json"
(ROOT / manifest_path).write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"manifest": record(manifest_path), "artifacts": artifacts,
                  "earlier_unchanged": len(earlier), "whole_obligations": 14,
                  "substantive_issues": 0}, indent=2))
