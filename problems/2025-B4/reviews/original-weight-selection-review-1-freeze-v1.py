"""Administrative integrity/JSON only; no mathematical computation."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/reviews/original-weight-selection-review-1-"


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def read_json(path):
    return json.loads((ROOT / path).read_text())


def checked(expected):
    actual = record(expected["path"])
    for key in ("bytes", "sha256"):
        if key in expected:
            assert actual[key] == expected[key], (expected, actual)
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
    assert not (ROOT / (PREFIX + suffix)).exists(), "Do not overwrite frozen output"

target_path = "problems/2025-B4/notes/coordinator-original-weight-selection-candidate-v1.md"
checked({"path": target_path, "bytes": 6934,
         "sha256": "ef41445567edb53e53980b9edfbba2739cb1879f048e19b9e64f48e2e684ad3e"})
target_manifest_path = "problems/2025-B4/notes/coordinator-original-weight-selection-manifest-v1.json"
checked({"path": target_manifest_path,
         "sha256": "f73e2c9152c196f1b39b360fa7c6fb4ba6d53dcf64a4abb7385c78ced8fc91a3"})
target_manifest = read_json(target_manifest_path)
assert target_manifest["author_obligations"] == 18
assert len(target_manifest["artifacts"]) == 3
assert len(target_manifest["inputs"]) == 5
assert target_manifest["FS2_unverified_universal_selection_used_as_premise"] is False
target_records = unique_checked(target_manifest["artifacts"] + [record(target_manifest_path)])
input_records = unique_checked(target_manifest["inputs"])
extra_records = [record("problems/2025-B4/reviews/diagonal-moment-acceptance.md")]
author_obligations = (ROOT / "problems/2025-B4/notes/coordinator-original-weight-selection-obligations-v1.md").read_text()
assert re.findall(r"^(\d+)\. ", author_obligations, re.M) == [str(i) for i in range(1, 19)]
ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert re.findall(r"^\| (OW-O\d{2}) \|", ledger, re.M) == [f"OW-O{i:02d}" for i in range(1, 19)]

prior_path = "problems/2020-B4/reviews/reasoning-return-r4-review-2-manifest-v1.1.json"
checked({"path": prior_path, "bytes": 3022,
         "sha256": "686eb6646c7de0e33a0d9ef88af63213b4e2c39bb3cec8ab47d4a5122142e227"})
prior = read_json(prior_path)
prior_validation = read_json("problems/2020-B4/reviews/reasoning-return-r4-review-2-input-validation-v1.1.json")
earlier = unique_checked(prior_validation["earlier_unique_records_preserved"]
                         + prior["artifacts"] + [record(prior_path)])
assert len(earlier) == 274

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
validation = {
    "validated_at_utc": now, "administrative_integrity_only": True,
    "exact_target_artifacts_and_manifest": target_records,
    "declared_input_and_context_records": input_records,
    "additional_accepted_scope_record": extra_records,
    "all_18_author_and_review_rows_present": True,
    "earlier_unique_records_preserved": earlier,
    "earlier_unique_count": len(earlier),
    "new_OW_nonconstructor": True,
    "older_FS_authorship_disclosed": True,
    "not_new_independent_reaudit_of_own_FS": True,
    "unverified_FS2_not_a_premise": True,
    "new_OW_peer_findings_read_before_initial_freeze": False,
    "old_FS_peer_findings_read_for_this_OW_audit": False,
    "mathematical_code_CAS_scan_table_certificate_or_author_rerun": False,
    "shared_Git_spawning_contact_charge_or_bypass": False,
    "primary_web_context": {
        "url": "https://arxiv.org/pdf/1412.5798v2",
        "internal_version": "1.13, 2021-11-02",
        "actual_read_scope": "Section2.4-2.5 direct definitions, printed pp5-7, module/inverse coefficient formulas/positivity/direct action and moment transformations",
        "full_external_Diophantine_proof_or_Appendix_reaudit_claimed": False,
        "new_raw_binary_hash_claimed": False,
    },
}
(ROOT / (PREFIX + "input-validation-v1.json")).write_text(json.dumps(validation, indent=2) + "\n")
artifacts = [record(PREFIX + suffix) for suffix in (
    "initial-v1.md", "issues-v1.md", "source-checks-v1.md",
    "freeze-v1.py", "input-validation-v1.json")]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind whole R1; OW1-OW3 pass in their explicit conditional algebraic scopes, no substantive issue found; coordinator reconciliation pending",
    "reviewer": "/root/review_2017_coarsening_r1",
    "new_OW_constructor": False, "older_FS_constructor": True,
    "old_FS_not_independently_reaudited_by_its_author": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": record(target_path), "target_manifest": record(target_manifest_path),
    "whole_author_obligations_audited": 18,
    "open_substantive_issues": 0,
    "actual_positivity_under_subtraction_and_original_weights_checked": True,
    "inverse_moment_and_integer_norm_orbit_separation_reconstructed": True,
    "iteration_uses_current_support_and_strict_threshold": True,
    "universal_starting_hypothesis_Diophantine_exclusion_reciprocal_transfer_or_novelty_claim": False,
    "new_OW_peer_findings_read_before_initial_freeze": False,
    "unverified_FS2_used_as_premise": False,
    "mathematical_program_CAS_scan_table_certificate_or_author_rerun": False,
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "last_direct_weekly_telemetry": {
        "at_utc": "2026-10-17 12:58:40 UTC", "total_used_percent": 39,
        "window_minutes": 10080, "reset_unix": 1792745187,
        "total_ceiling_percent": 90, "integration_reserve": True},
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
manifest_path = PREFIX + "manifest-v1.json"
(ROOT / manifest_path).write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"manifest": record(manifest_path), "artifacts": artifacts,
                  "target_records_verified": len(target_records),
                  "declared_inputs_verified": len(input_records),
                  "old_own_paths_unchanged": len(earlier),
                  "whole_obligations": 18, "open_substantive_issues": 0}, indent=2))

