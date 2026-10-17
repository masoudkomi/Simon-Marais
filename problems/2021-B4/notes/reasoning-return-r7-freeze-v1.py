"""Administrative known-file hashes, JSON and preservation; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-return-r7-"


def fp(path):
    data = (ROOT / path).read_bytes()
    return {"path": str(path), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked(rec):
    actual = fp(rec["path"])
    if actual["bytes"] != rec["bytes"] or actual["sha256"] != rec["sha256"]:
        raise RuntimeError("Fingerprint mismatch: " + rec["path"])
    return dict(actual, matches=True)


def read_json(path):
    return json.loads((ROOT / path).read_text())


def all_fps(obj):
    if isinstance(obj, dict):
        if {"path", "bytes", "sha256"} <= obj.keys():
            yield obj
        for value in obj.values():
            yield from all_fps(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from all_fps(value)


def save(suffix, obj):
    path = ROOT / (PREFIX + suffix)
    if path.exists():
        raise RuntimeError("Refusing to overwrite: " + str(path))
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


now = datetime.now(timezone.utc).isoformat()
assert fp(PREFIX + "candidate-v1.md")["sha256"] == "8f4d1f71930b82e029066c4f4d249489c34e70b731e80a11458c833223fc18a6"
r6_accept_path = "problems/2021-B4/reviews/reasoning-return-r6-acceptance.json"
assert fp(r6_accept_path)["sha256"] == "18ba149e4cf902ee9cb57c869fa60d9758d67f1ed143deb83ddbf05e0a7fc333"
r6_authority = [checked(rec) for rec in all_fps(read_json(r6_accept_path))]
r6_manifest_path = "problems/2021-B4/notes/reasoning-return-r6-freeze-v1.json"
assert fp(r6_manifest_path)["sha256"] == "9c97c3b704fb2b53ce8108991ffca70e04a01760dcbadb8d2712ba339bc24538"
r6_artifacts = [checked(rec) for rec in read_json(r6_manifest_path)["records"]]
r6_old_input_path = "problems/2021-B4/notes/reasoning-return-r6-input-validation-v1.json"
r6_old_input_rows = [checked(rec) for rec in all_fps(read_json(r6_old_input_path))]
r6_old_source_path = "problems/2021-B4/notes/reasoning-return-r6-sources-v1.json"
r6_old_source_rows = [checked(rec) for rec in all_fps(read_json(r6_old_source_path))]

previous_input_path = "problems/2024-B4/reviews/P2-critical-jet-review-1-input-validation-v1.json"
previous_manifest_path = "problems/2024-B4/reviews/P2-critical-jet-review-1-manifest-v1.json"
assert fp(previous_manifest_path)["sha256"] == "a6f67056180221e2b3db20d5b987e36173eac55d5681b8036a0b33e33e5e2e3c"
previous_input = read_json(previous_input_path)
previous_manifest = read_json(previous_manifest_path)
older = []
for item in previous_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(previous_manifest_path),
              "checks": [checked(rec) for rec in previous_manifest["records"]]})
assert len(older) == 47
gk_addendum = checked(previous_input["GK_separate_telemetry_addendum_preserved"])

body_scopes = [
    ("problems/2021-B4/proofs/reviewed-reasoning-return-r6-v1.1.md",
     "COMPLETE accepted R6 body and scope; exact Euler estimate direct, new weighted extension not presumed accepted"),
    ("problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
     "COMPLETE R5A-E body; R5D first break and G1/R5C direct, minimum-depth bound context only"),
    ("problems/2021-B4/proofs/reviewed-reasoning-J15-v1.1.md",
     "COMPLETE D1-D5 and low-order family; actual versus repeated residue, local versus rational factor distinctions"),
    ("problems/2021-B4/notes/rational-witness-p-plus-one-reviewed-v1.2.md",
     "COMPLETE rational affine normalization and field distinction"),
    ("problems/2021-B4/notes/padic-rational-newton-reviewed-v1.1.md",
     "COMPLETE accepted Newton register; old certificates not rerun or newly recertified"),
    ("problems/2021-B4/notes/coordinator-three-rational-witnesses-reviewed-v1.1.md",
     "COMPLETE T1/T3 accepted register, lower bound on rational COVER"),
    ("problems/2021-B4/notes/coordinator-three-rational-witnesses-v1.md",
     "COMPLETE original mathematical proof/coverage; no large certificate replay"),
    ("problems/2021-B4/proofs/reviewed-return-r3-v1.1.md",
     "COMPLETE seven-return acceptance scope register"),
]
context_scopes = [
    ("problems/2021-B4/notes/reasoning-return-r3-candidate-v1.md", "G1/G2 complete relevant sections and higher-witness sectionW"),
    ("problems/2021-B4/notes/reasoning-return-r3-collision-candidate-v1.md", "Section6 RC3 and following source/qualification boundary; no claim of a fresh whole RC1/RC2 calculation read"),
    ("problems/2021-B4/notes/reasoning-return-r3-transfer-candidate-v1.md", "COMPLETE TA1/TA2 and critical-value boundary, old context"),
    ("problems/2021-B4/notes/reasoning-return-r3-mirror-candidate-v1.md", "COMPLETE old exact-mirror restriction, no new acceptance of larger branch"),
    ("problems/2021-B4/notes/reasoning-return-r3-parity-candidate-v1.md", "COMPLETE PP1/PP2 context, no new multi-root theorem"),
    ("problems/2021-B4/notes/reasoning-return-r3-sparse-descent-candidate-v1.md", "COMPLETE SD1 context"),
    ("problems/2021-B4/notes/reasoning-return-r3-parity-barrier-candidate-v1.md", "COMPLETE PB1 context, residue evidence not a rational lift"),
]
accepted_scope_paths = [
    "problems/2021-B4/reviews/reasoning-return-r6-acceptance.md",
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance.md",
    "problems/2021-B4/reviews/return-r3-acceptance.md",
]
usage = {"at_utc": "2026-10-17 13:39:33 UTC (paired clock and telemetry)",
         "total_used_percent": 42, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "ordinary_usage_allowed": True, "integration_reserve": True,
         "separately_billed_API": False}
primary = [
    {"title": "Official2021 Paper B, B4 hypothesis and(b)",
     "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
     "actual_read_scope": "Fresh actual B4 domain and(b); no preliminary proof investigation",
     "existing_ignored_cache": fp(".cache/official/2021-paper_b.pdf"),
     "fresh_viewer_cache_byte_identity_claimed": False},
    {"title": "CLO, Constraints on counterexamples to the Casas-Alvero conjecture, and a verification in degree12",
     "url": "https://arxiv.org/pdf/1208.5404",
     "actual_read_scope": "Type/scenario definitions; equation7; Section3.4 equations9-10/Lemma17; Proposition19 and following unramified qualification",
     "role": "normalization through accepted rational-affine project body; all-root theorem inapplicable",
     "existing_ignored_cache": fp(".cache/literature/2021/cited-66c5af6a0f0239f5.pdf"),
     "fresh_viewer_cache_byte_identity_or_new_whole_external_proof_claimed": False},
    {"title": "Marashdeh, A descent-set obstruction for the Casas-Alvero conjecture",
     "url": "https://arxiv.org/html/2608.14726v1",
     "actual_read_scope": "Support/vacuity formulation, displayed TheoremB and its one-root/multi-root boundary, TheoremC/D statements",
     "role": "attributed context only; no multi-root exclusion imported",
     "new_whole_paper_or_full_source_proof_read_claimed": False,
     "raw_web_hash": None, "new_download": False},
]
sources = {
    "recorded_at_utc": now, "status": "candidate proof - unverified",
    "constructor": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "protocol": fp("AGENTS.md"),
    "complete_accepted_bodies_and_registers_read": [dict(fp(path), actual_read_scope=scope) for path, scope in body_scopes],
    "old_mathematical_context_precise_read_scopes": [dict(fp(path), actual_read_scope=scope) for path, scope in context_scopes],
    "complete_acceptance_texts_read": [fp(path) for path in accepted_scope_paths],
    "primary_sources": primary,
    "new_results": ["R7A strict weighted quadratic comparison tau<nu", "R7B first-break essential-center or weighted triple fork", "R7C weaker paired valuation application", "R7D exact rational double-origin transport and deep triple invariance"],
    "old_RC3_essential_root_mechanism_not_claimed_new": True,
    "root_broad_essential_cover_lead_disclosed": True,
    "new_weighted_proof_or_triple_bounds_supplied_by_root": False,
    "requires_two_other_fresh_initially_blind_whole_audits": True,
    "new_external_theorem_or_multi_root_exclusion_imported": False,
    "old_large_certificates_rerun_or_newly_recertified": False,
    "mathematical_program_CAS_scan_enumeration_or_author_rerun": False,
    "queued_2024_DI_target_or_peer_findings_read_during_R7": False,
    "new_native_download_cache_mutation_or_tracked_third_party_paper": False,
    "full_branch_degree20_annual_rational_lift_or_novelty_claim": False,
    "latest_authoritative_weekly_usage": usage,
}
save("sources-v1.json", sources)

obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
labels = re.findall(r"\|R7O(\d\d)\|", obligations)
assert len(labels) == 36 and set(labels) == {str(i).zfill(2) for i in range(1, 37)}
validation = {
    "checked_at_utc": now, "metadata_only_not_mathematical_evidence": True,
    "accepted_R6_authority": fp(r6_accept_path),
    "accepted_R6_declared_records": r6_authority,
    "R6_constructor_manifest": fp(r6_manifest_path),
    "R6_eight_frozen_artifacts": r6_artifacts,
    "R6_old_input_declared_fingerprints": r6_old_input_rows,
    "R6_old_source_declared_fingerprints": r6_old_source_rows,
    "new_complete_accepted_bodies_and_context_records": [checked(rec) for rec in all_fps(sources)],
    "older_own_packets": older,
    "all_forty_seven_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "all36_obligation_labels_present": True,
    "actual_rational_witnesses_not_local_substitutes": True,
    "exact_delta_zero_and_arbitrary_finite_displacement_retained": True,
    "strict_tau_below_nu_not_unit_only_premise": True,
    "deep_alternative_and_nonunit_essential_center_not_excluded": True,
    "cubic_identity_only_formal_diagnostic_not_Q_or_Q19_lift": True,
    "essential_cover_observation_already_RC3_not_claimed_new": True,
    "root_broad_research_lead_disclosed_not_counted_as_fresh_review": True,
    "two_other_whole_nonconstructor_audits_required_before_any_promotion": True,
    "only_current_assigned_prefix_written": True,
    "old_candidate_review_shared_cache_or_Git_mutation": False,
    "mathematical_program_CAS_scan_enumeration_certificate_replay_or_author_rerun": False,
    "spawning_charge_contact_or_access_bypass": False,
    "queued_DI_or_UW_target_or_new_peer_findings_read": False,
}
save("input-validation-v1.json", validation)

output = {
    "checked_at_utc": now, "metadata_only_no_mathematical_computation": True,
    "candidate": fp(PREFIX + "candidate-v1.md"),
    "claims": ["R7A", "R7B", "R7C", "R7D"],
    "whole_obligations": 36,
    "accepted_R6_authority_declared_records_checked": len(r6_authority),
    "accepted_R6_frozen_artifacts_checked": len(r6_artifacts),
    "R6_old_input_record_occurrences_checked": len(r6_old_input_rows),
    "R6_old_input_unique_paths_checked": len({rec["path"] for rec in r6_old_input_rows}),
    "R6_old_source_fingerprint_occurrences_checked": len(r6_old_source_rows),
    "new_source_fingerprint_occurrences_checked": len(list(all_fps(sources))),
    "older_own_packets_unchanged": len(older), "all_hash_checks_passed": True,
    "status": "candidate proof - unverified; complete meaningful conceptual checkpoint",
    "first_break_alternatives_excluded_or_full_annual_solved": False,
    "latest_authoritative_weekly_usage": usage,
    "command": "python3 problems/2021-B4/notes/reasoning-return-r7-freeze-v1.py",
}
save("freeze-output-v1.json", output)
names = ["candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
         "worklog-v1.md", "source-audit-v1.md", "sources-v1.json",
         "freeze-v1.py", "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; complete R7 conceptual construction checkpoint",
    "constructor": "/root/review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "claims": ["R7A", "R7B", "R7C", "R7D"],
    "whole_independent_audit_obligations": 36,
    "requires_two_OTHER_fresh_initially_blind_nonconstructor_whole_audits": True,
    "root_broad_cover_lead_disclosed": True,
    "root_supplied_new_weighted_proof_or_triple_bounds": False,
    "old_RC3_mechanism_not_claimed_new": True,
    "strict_tau_nu_boundary_and_deep_triple_retained": True,
    "double_origin_involution_preserves_remaining_deep_alternative": True,
    "cubic_only_reduced_jet_no_actual_lift": True,
    "whole_branch_degree20_annual_rational_lift_or_novelty_claim": False,
    "mathematical_program_CAS_scan_enumeration_certificate_or_author_rerun": False,
    "old_shared_Git_cache_mutation_spawning_charge_contact_or_bypass": False,
    "queued_DI_and_UW_targets_or_new_peer_findings_read_before_freeze": False,
    "older_own_packets_unchanged": len(older),
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "artifacts": [fp(PREFIX + name) for name in names],
}
save("freeze-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "freeze-v1.json")), indent=2))
