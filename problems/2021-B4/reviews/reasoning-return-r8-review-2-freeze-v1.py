"""Administrative R8 whole-review integrity only; no mathematical code.

Does not execute author programs, read a new peer report, or mutate inputs.
Outputs are confined to the new assigned review prefix and refuse overwrite.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/reviews/reasoning-return-r8-review-2-"
PEER_PREFIX = "problems/2021-B4/reviews/reasoning-return-r8-review-1-"

def rec(path):
    assert not path.startswith(PEER_PREFIX), "blind-review guard"
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}

def verify(expected):
    actual = rec(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual["path"]
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual["path"]
    return actual

def write_new(suffix, value):
    path = ROOT / (PREFIX + suffix)
    with path.open("x", encoding="utf-8") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")

stamp = datetime.now(timezone.utc).isoformat()
target = verify({
    "path": "problems/2021-B4/notes/reasoning-return-r8-candidate-v1.md",
    "bytes": 16961,
    "sha256": "6bffa3b70e9d228b09e0a2ee3f049d7f5261fb98d484ebacff7abcbfde5eea26",
})
target_freeze = verify({
    "path": "problems/2021-B4/notes/reasoning-return-r8-freeze-v1.json",
    "bytes": 3602,
    "sha256": "9d366b0c0eee1a56dae269a2aeb197627516d00f2d87d17a4d6c93304b1919b8",
})
author_manifest = json.loads((ROOT / target_freeze["path"]).read_text())
author_artifacts = [verify(item) for item in author_manifest["artifacts"]]
assert len(author_artifacts) == 9
author_sources = json.loads((ROOT / "problems/2021-B4/notes/reasoning-return-r8-sources-v1.json").read_text())
author_validation = json.loads((ROOT / "problems/2021-B4/notes/reasoning-return-r8-input-validation-v1.json").read_text())

# Verify fingerprint records only. Do not execute author freezer or inspect peers.
declared = {}
occurrences = [0]
def walk(value):
    if isinstance(value, dict):
        if isinstance(value.get("path"), str) and isinstance(value.get("sha256"), str):
            actual = verify(value)
            occurrences[0] += 1
            if actual["path"] in declared:
                assert declared[actual["path"]] == actual
            declared[actual["path"]] = actual
        for child in value.values():
            walk(child)
    elif isinstance(value, list):
        for child in value:
            walk(child)
for obj in (author_manifest, author_sources, author_validation):
    walk(obj)

accepted_paths = [
    "problems/2021-B4/proofs/reviewed-reasoning-return-r7-v1.1.md",
    "problems/2021-B4/proofs/reviewed-reasoning-return-r6-v1.1.md",
    "problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
    "problems/2021-B4/proofs/reviewed-return-r3-v1.1.md",
]
accepted = [rec(p) for p in accepted_paths]
context = [rec(p) for p in [
    "AGENTS.md", "problems/2021-B4/statement.md",
    ".cache/official/2021-paper_b.pdf",
]]

old_freeze_path = "problems/2020-B4/notes/reasoning-return-r6-freeze-v1.json"
old_freeze_rec = verify({
    "path": old_freeze_path, "bytes": 3821,
    "sha256": "d0f3c1f2697af5198971034696c77cac542d3553bc429aab31c1ce7428605f29",
})
old_freeze = json.loads((ROOT / old_freeze_path).read_text())
old_validation = json.loads((ROOT / "problems/2020-B4/notes/reasoning-return-r6-input-validation-v1.json").read_text())
old_records = old_validation["earlier_unique_records_preserved"] + old_freeze["artifacts"] + [old_freeze_rec]
prior = {}
for item in old_records:
    actual = verify(item)
    if actual["path"] in prior:
        assert prior[actual["path"]] == actual
    prior[actual["path"]] = actual
assert len(prior) == 344

integrity = {
    "validated_at_utc": stamp,
    "administrative_identity_only_not_mathematical_proof": True,
    "target_nine_artifacts_and_freeze": author_artifacts + [target_freeze],
    "declared_author_fingerprint_occurrences_verified": occurrences[0],
    "declared_author_unique_paths_verified": [declared[p] for p in sorted(declared)],
    "complete_accepted_bodies_read": accepted,
    "protocol_official_cache_context": context,
    "earlier_unique_records_preserved": [prior[p] for p in sorted(prior)],
    "earlier_unique_record_count": len(prior),
    "reviewer_is_NEW_R8_constructor_or_contributor": False,
    "OLD_R5_authorship_and_single_center_PN_review_roles_disclosed": True,
    "new_peer_or_root_R8_manifest_report_issues_or_findings_read_before_freeze": False,
    "blind_guard_prefix": PEER_PREFIX,
    "primary_reads_and_limits": [
        {"url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
         "read": "page2 B4 hypothesis and(b), actual rational coefficients and rational derivative witnesses; no preliminary research"},
        {"url": "https://arxiv.org/pdf/1208.5404",
         "read": "Section3.4 normalization equations9-10 and Lemma17 with surrounding derivation; complete Proposition19 proof and following unramified-field remark; Hasse/affine context",
         "full_paper_or_computational_certificate_audit": False,
         "stronger_all_root_or_unramified_conclusion_imported": False},
        {"url": "https://arxiv.org/html/2608.14726v1",
         "read": "Intro definitions/scenarios, TheoremB context, TheoremsC/D statements and explicit multi-root limitation",
         "context_only_no_new_four_value_or_universal_proof_import": True,
         "full_source_proofs_reconstructed": False},
    ],
    "new_native_source_download_binary_hash_or_live_cache_identity_claimed": False,
    "all_new_mathematical_inferences_and_nine_pair_certificate_reconstructed_by_hand": True,
    "mathematical_program_CAS_scan_table_certificate_or_author_rerun": False,
    "native_mathematical_job_or_pending_tool_call": False,
    "shared_Git_cache_mutation_spawning_charge_contact_or_bypass": False,
}

ledger = (ROOT / (PREFIX + "issues-v1.md")).read_text()
assert sum(line.startswith("|R8-O") for line in ledger.splitlines()) == 40
assert all(("|R8-O%02d|PASS|" % i) in ledger for i in range(1, 41))
write_new("input-validation-v1.json", integrity)
suffixes = ["initial-v1.md", "issues-v1.md", "source-checks-v1.md",
            "freeze-v1.py", "input-validation-v1.json"]
artifacts = [rec(PREFIX + suffix) for suffix in suffixes]
manifest = {
    "frozen_at_utc": stamp,
    "status": "COMPLETE initially blind WHOLE R8 R2; no substantive scoped defect or required repair; coordinator reconciliation pending",
    "reviewer": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "target": target, "target_manifest": target_freeze,
    "whole_author_obligations": 40, "independent_inference_rows": 40,
    "open_substantive_issues": 0, "required_author_repairs": 0,
    "NEW_R8_constructor_or_contributor": False,
    "OLD_R5_authorship_and_single_center_PN_review_roles_disclosed": True,
    "arbitrary_nu_sigma_zero_coefficients_and_exact_delta0_reconstructed": True,
    "all_nine_cubic_cases_actual_witness_assignments_exact_zeros_and_both_frames_reconstructed": True,
    "remaining_alternative_excluded_or_Q19_Q_lift_degree20_annual_novelty_claim": False,
    "new_peer_or_root_R8_findings_read_before_initial_freeze": False,
    "mathematical_program_CAS_scan_certificate_or_author_rerun": False,
    "declared_author_fingerprint_occurrences_verified": occurrences[0],
    "declared_author_unique_paths_verified": len(declared),
    "earlier_frozen_context_records_verified_unchanged": len(prior),
    "last_direct_weekly_telemetry": {
        "at_utc": "2026-10-17 about15:54UTC group transition",
        "total_used_percent": 49, "window_minutes": 10080,
        "reset_unix": 1792745187, "total_ceiling_percent": 90,
        "review_integration_reserve": True,
    },
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2021-B4/reviews/reasoning-return-r8-review-2-freeze-v1.py",
    "artifacts": artifacts,
}
write_new("manifest-v1.json", manifest)
print(json.dumps({
    "frozen_at_utc": stamp, "artifacts": len(artifacts),
    "obligations": 40, "substantive_issues": 0,
    "declared_author_occurrences": occurrences[0],
    "declared_author_unique_paths": len(declared),
    "earlier_records_preserved": len(prior),
    "report": artifacts[0], "manifest": rec(PREFIX + "manifest-v1.json"),
}, indent=2))
