"""Administrative integrity/JSON only; no mathematical computation."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/reviews/reasoning-return-r4-review-2-"


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def read_json(path):
    return json.loads((ROOT / path).read_text())


def checked(expected):
    actual = record(expected["path"])
    assert all(actual[key] == value for key, value in expected.items()), (expected, actual)
    return actual


def unique_checked(records):
    output = {}
    for expected in records:
        actual = checked(expected)
        if actual["path"] in output:
            assert output[actual["path"]] == actual
        output[actual["path"]] = actual
    return list(output.values())


for suffix in ("input-validation-v1.json", "manifest-v1.json"):
    assert not (ROOT / (PREFIX + suffix)).exists(), "Do not overwrite frozen review"

target_path = "problems/2020-B4/notes/reasoning-return-r4-candidate-v1.md"
target_manifest_path = "problems/2020-B4/notes/reasoning-return-r4-freeze-v1.json"
checked({"path": target_path, "bytes": 19691,
         "sha256": "685c38ed9f1754aca7613e7e6d74d628737fa3b7111c3f8b01c98005b9af6958"})
target_manifest = read_json(target_manifest_path)
assert target_manifest["author_obligations"] == 36
assert target_manifest["constructor"] == "review_2022_complexity_r2"
assert len(target_manifest["artifacts"]) == 7
target_records = unique_checked(target_manifest["artifacts"] + [record(target_manifest_path)])
source = read_json("problems/2020-B4/notes/reasoning-return-r4-sources-v1.json")
source_records = unique_checked(source["direct_full_local_document_or_register_reads"]
                                + source["existing_related_native_cache_fingerprints"])
obligation_text = (ROOT / "problems/2020-B4/notes/reasoning-return-r4-obligations-v1.md").read_text()
assert re.findall(r"\|(R4-O\d{2})\|", obligation_text) == [f"R4-O{i:02d}" for i in range(1, 37)]
ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert re.findall(r"^\| (R4-O\d{2}) \|", ledger, re.M) == [f"R4-O{i:02d}" for i in range(1, 37)]

prior_path = "problems/2025-B4/notes/reasoning-return-r4-freeze-v1.json"
checked({"path": prior_path, "bytes": 3437,
         "sha256": "1a2bb1af9a01a677dc68c8456067021f6cb9dd52113a2a50f5c09212e635b15b"})
prior = read_json(prior_path)
prior_validation = read_json("problems/2025-B4/notes/reasoning-return-r4-input-validation-v1.json")
earlier = unique_checked(prior_validation["earlier_unique_records_preserved"]
                         + prior["artifacts"] + [record(prior_path)])
assert len(earlier) == 253

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
validation = {
    "validated_at_utc": now,
    "administrative_integrity_only": True,
    "exact_target_all_seven_artifacts_and_freeze": target_records,
    "all_author_source_fingerprints": source_records,
    "all_36_author_obligations_present": True,
    "all_36_review_ledger_dispositions_present": True,
    "earlier_unique_records_preserved": earlier,
    "earlier_unique_count": len(earlier),
    "new_R4_nonconstructor": True,
    "old_repaired_R3_F1_F2_authorship_disclosed": True,
    "review_not_counted_as_new_independent_reaudit_of_own_old_input": True,
    "root_or_other_new_R4_peer_findings_read_before_initial_freeze": False,
    "mathematical_program_CAS_scan_certificate_replay_or_author_rerun": False,
    "shared_files_Git_spawning_contact_charge_or_bypass": False,
}
validation_path = PREFIX + "input-validation-v1.json"
(ROOT / validation_path).write_text(json.dumps(validation, indent=2) + "\n")
artifacts = [record(PREFIX + suffix) for suffix in (
    "initial-v1.md", "issues-v1.md", "source-checks-v1.md",
    "freeze-v1.py", "input-validation-v1.json")]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind whole review2; one auxiliary false assertion requires author correction; full E2 iff and R4A-R4D otherwise reconstruct",
    "reviewer": "/root/review_2017_coarsening_r1",
    "new_R4_constructor": False,
    "old_repaired_R3_F1_F2_constructor": True,
    "old_dependency_not_independently_reaudited_by_its_author": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": record(target_path),
    "target_manifest": record(target_manifest_path),
    "whole_author_obligations_audited": 36,
    "open_substantive_auxiliary_issues": 1,
    "issue": {
        "id": "R4R2-01",
        "scope": "R4E lines351-352 final-equation essential / earlier-equations insufficient assertion is false",
        "proof": "The last moment is k(k-1)=-1 automatically; the shorter moment list plus known mu(0)=k suffices by nonzero-point Vandermonde and the same small-count lifting",
        "full_E2_iff_and_R4A_R4D_invalidated": False,
        "author_versioned_correction_and_affected_review_required": True,
    },
    "Cohen_original_theorem_hypotheses_checked": True,
    "Cohen_complete_external_proof_reconstructed": False,
    "new_Diophantine_classification_unbounded_E2_solution_novelty_or_cutoff_claim": False,
    "peer_findings_read_before_initial_freeze": False,
    "mathematical_program_CAS_scan_certificate_or_author_rerun": False,
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "last_direct_weekly_telemetry": {
        "at_utc": "2026-10-17 12:29:29 UTC", "total_used_percent": 37,
        "window_minutes": 10080, "reset_unix": 1792745187,
        "total_ceiling_percent": 90, "integration_reserve": True,
    },
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
manifest_path = PREFIX + "manifest-v1.json"
(ROOT / manifest_path).write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"manifest": record(manifest_path), "artifacts": artifacts,
                  "target_manifest": record(target_manifest_path),
                  "target_records_checked": len(target_records),
                  "source_fingerprints_checked": len(source_records),
                  "earlier_unique_unchanged": len(earlier),
                  "whole_obligations": 36, "substantive_auxiliary_issues": 1}, indent=2))
