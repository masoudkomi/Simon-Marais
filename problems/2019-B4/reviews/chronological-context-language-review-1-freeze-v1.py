"""Administrative freeze only; no mathematical computation."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/chronological-context-language-review-1-"


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


target_path = "problems/2019-B4/notes/coordinator-chronological-context-language-candidate-v1.md"
target_manifest_path = "problems/2019-B4/notes/coordinator-chronological-context-language-manifest-v1.json"
checked({"path": target_path, "bytes": 6235,
         "sha256": "6d9446e4bb4fb81457eb8882b498c073353eaf93a546e8b56007a0adf0e613da"})
checked({"path": target_manifest_path,
         "sha256": "38fb9ca9e5db47d97c18cbfc6fd5f52283b8896e0f8637dd802da4c532d56e8c"})
target_manifest = read_json(target_manifest_path)
target_records = unique_checked(target_manifest["records"] + [record(target_manifest_path)])
assert len(target_manifest["records"]) == 3
obligations = read_json("problems/2019-B4/notes/coordinator-chronological-context-language-obligations-v1.json")
assert [r["id"] for r in obligations["obligations"]] == [f"CCL{i:02d}" for i in range(1, 16)]
context = [record(path) for path in (
    "AGENTS.md", "problems/2019-B4/statement.md",
    "problems/2019-B4/proofs/candidate-v1.1.md",
    "problems/2019-B4/proofs/reviewed-secondpass-v1.1.md",
    "problems/2019-B4/proofs/reviewed-thirdpass-v1.1.md",
    "problems/2019-B4/proofs/reviewed-nonregularity-return-v1.1.md")]

old_manifest_path = "problems/2025-B4/reviews/diagonal-moment-review-2-manifest-v1.json"
checked({"path": old_manifest_path, "bytes": 2973,
         "sha256": "11ac73101fe6033c042b5de021a68131de1d73fe7f4d41fd861108dec191c7ca"})
old_manifest = read_json(old_manifest_path)
old_validation = read_json("problems/2025-B4/reviews/diagonal-moment-review-2-input-validation-v1.json")
earlier = unique_checked(old_validation["earlier_unique_records_preserved"]
                         + old_manifest["artifacts"] + [record(old_manifest_path)])
assert len(earlier) == 223

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
validation = {
    "validated_at_utc": now,
    "administrative_integrity_only": True,
    "exact_target_and_all_three_declared_records": target_records,
    "protocol_official_and_dictionary_context": context,
    "context_read_limits": "Complete statement and short accepted register; original section1, thirdpass input/path sections and nonregularity-return acceptance/model sections; not a fresh whole audit of unrelated cap arguments",
    "fifteen_submitted_obligations_present": True,
    "earlier_unique_records_preserved": earlier,
    "earlier_unique_count": len(earlier),
    "constructor_of_CCL": False,
    "peer_new_CCL_findings_read_before_initial_freeze": False,
    "separate_linear_output_construction_started_before_initial_freeze": False,
    "mathematical_program_CAS_scan_or_author_rerun": False,
    "shared_Git_spawning_contact_charge_or_bypass": False,
}
validation_path = PREFIX + "input-validation-v1.json"
(ROOT / validation_path).write_text(json.dumps(validation, indent=2) + "\n")
artifacts = [record(PREFIX + suffix) for suffix in
             ("initial-v1.md", "issues-v1.md", "source-checks-v1.md",
              "freeze-v1.py", "input-validation-v1.json")]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind whole review1; no substantive objection found; coordinator reconciliation required",
    "reviewer": "/root/review_2017_coarsening_r1",
    "constructor_of_CCL": False,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": record(target_path),
    "target_manifest": record(target_manifest_path),
    "whole_submitted_obligations_audited": 15,
    "open_substantive_issues": 0,
    "peer_findings_read_before_initial_freeze": False,
    "candidate_scope": "The precise u#v serialization of finite chronological alternating-source routing pairs is not context-free",
    "original_output_language_canonical_history_algebraicity_exact_growth_or_novelty_claim": False,
    "fixed_two_tape_hardness_imported": False,
    "separate_linear_output_construction_started_before_initial_freeze": False,
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
                  "earlier_unchanged": len(earlier), "whole_obligations": 15,
                  "substantive_issues": 0}, indent=2))
