"""Administrative integrity/JSON only. No mathematical computation."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/P2-critical-jet-review-2-"


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
    assert not (ROOT / (PREFIX + suffix)).exists(), "Never overwrite a frozen output"

target_path = "problems/2024-B4/notes/coordinator-P2-critical-jet-return-v1.md"
checked({"path": target_path, "bytes": 6774,
         "sha256": "fa5b79ce59303a06a61da18ee902235bc299add309aa0725846bbfd3a7716f26"})
target_manifest_path = "problems/2024-B4/notes/coordinator-P2-critical-jet-manifest-v1.json"
author = read_json(target_manifest_path)
assert author["whole_obligations"] == 6
assert len(author["records"]) == 3
assert author["unverified_critical_note_used_as_premise"] is False
target_records = unique_checked(author["records"] + [record(target_manifest_path)])
context = [record(path) for path in (
    "AGENTS.md", "problems/2024-B4/statement.md",
    "problems/2024-B4/reviews/generalized-Kasami-acceptance.md",
    "problems/2024-B4/notes/coordinator-P2-critical-fixed-return-v1.md",
    "problems/2024-B4/notes/coordinator-higher-family-composition-return-v1.md",
    ".cache/official/2024-paper_b.pdf")]
text = (ROOT / target_path).read_text()
assert re.findall(r"\((i|ii|iii|iv|v|vi)\)", text) == ["i", "ii", "iii", "iv", "v", "vi"]
ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert re.findall(r"^\| (CJ-R20[1-6]) \|", ledger, re.M) == [f"CJ-R20{i}" for i in range(1, 7)]

prior_path = "problems/2022-B4/reviews/reasoning-return-r5-review-2-manifest-v1.json"
checked({"path": prior_path, "bytes": 3166,
         "sha256": "43e1f39e8a2e3076db59a3d9df9e3ac1151c4121dadb44167d90516ee54a726f"})
prior = read_json(prior_path)
prior_validation = read_json("problems/2022-B4/reviews/reasoning-return-r5-review-2-input-validation-v1.json")
earlier = unique_checked(prior_validation["earlier_unique_records_preserved"]
                         + prior["artifacts"] + [record(prior_path)])
assert len(earlier) == 286

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
validation = {
    "validated_at_utc": now, "administrative_integrity_only": True,
    "exact_three_author_records_plus_manifest": target_records,
    "protocol_official_scope_and_UNVERIFIED_context_records": context,
    "all_six_author_and_review_obligations_present": True,
    "earlier_unique_records_preserved": earlier,
    "earlier_unique_count": len(earlier),
    "new_CJ1_nonconstructor": True,
    "old_CP_authorship_disclosed_not_independently_reaudited": True,
    "sole_logical_input_GK_recurrence_and_degrees": True,
    "unverified_critical_and_higher_notes_used_as_premise": False,
    "new_CJ1_peer_findings_read_before_initial_freeze": False,
    "mathematical_program_CAS_scan_sample_certificate_or_author_rerun": False,
    "shared_Git_spawning_contact_charge_bypass": False,
    "official_primary_url_directly_reopened": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf",
    "new_external_theorem_or_source_binary_download": False,
}
(ROOT / (PREFIX + "input-validation-v1.json")).write_text(json.dumps(validation, indent=2) + "\n")
artifacts = [record(PREFIX + suffix) for suffix in (
    "initial-v1.md", "issues-v1.md", "source-checks-v1.md",
    "freeze-v1.py", "input-validation-v1.json")]
manifest = {
    "frozen_at_utc": now,
    "status": "complete initially blind whole R2; all six CJ1 obligations pass in necessary-congruence scope, no substantive issue found; coordinator reconciliation pending",
    "reviewer": "/root/review_2017_coarsening_r1",
    "new_CJ1_constructor": False,
    "old_CP_authorship_disclosed_not_new_independent_self_reaudit": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": record(target_path), "target_manifest": record(target_manifest_path),
    "whole_author_obligations_audited": 6,
    "open_substantive_issues": 0,
    "exact_q_local_order_uniform_q5_jet_and_q4_outer_multiplicity_reconstructed": True,
    "zero_K_inseparable_H_and_j1_boundaries_checked": True,
    "coprime_product_and_monic_F2_descent_checked": True,
    "j2_endpoint_and_j3plus_insufficiency_scope_checked": True,
    "full_composition_factorization_annual_novelty_or_Ritt_theorem_claim": False,
    "new_CJ1_peer_findings_read_before_initial_freeze": False,
    "mathematical_program_CAS_scan_sample_certificate_or_author_rerun": False,
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "last_direct_weekly_telemetry": {
        "at_utc": "2026-10-17 13:11:25 UTC", "total_used_percent": 40,
        "window_minutes": 10080, "reset_unix": 1792745187,
        "total_ceiling_percent": 90, "integration_reserve": True},
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
manifest_path = PREFIX + "manifest-v1.json"
(ROOT / manifest_path).write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"manifest": record(manifest_path), "artifacts": artifacts,
                  "target_records_checked": len(target_records),
                  "old_own_paths_unchanged": len(earlier),
                  "whole_obligations": 6, "open_substantive_issues": 0}, indent=2))

