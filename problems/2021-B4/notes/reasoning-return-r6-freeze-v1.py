"""Administrative byte/JSON integrity only; performs no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-return-r6-"
ACTOR = "/root/review_2021_reasoning_j15_r2"
SETTINGS = {"model": "gpt-6.1-sol", "reasoning": "max"}


def fp(path):
    path = str(path)
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def checked(rec):
    actual = fp(rec["path"])
    same = (actual["bytes"] == rec["bytes"]
            and actual["sha256"] == rec["sha256"])
    if not same:
        raise RuntimeError("Fingerprint mismatch: " + rec["path"])
    return dict(actual, matches=True)


def read_json(path):
    return json.loads((ROOT / path).read_text())


def records(obj):
    if isinstance(obj, dict):
        if {"path", "bytes", "sha256"} <= obj.keys():
            yield obj
        for value in obj.values():
            yield from records(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from records(value)


def save(suffix, obj):
    path = ROOT / (PREFIX + suffix)
    if path.exists():
        raise RuntimeError("Refusing to overwrite: " + str(path))
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def scoped(path, scope):
    return dict(fp(path), actual_read_scope=scope)


now = datetime.now(timezone.utc).isoformat()
old_input_path = "problems/2019-B4/reviews/linear-output-return-r1-review-1-input-validation-v1.json"
old_manifest_path = "problems/2019-B4/reviews/linear-output-return-r1-review-1-manifest-v1.json"
old_input = read_json(old_input_path)
old_manifest = read_json(old_manifest_path)
older = []
for item in old_input["older_own_packets"]:
    older.append({"manifest": checked(item["manifest"]),
                  "checks": [checked(rec) for rec in item["checks"]]})
older.append({"manifest": fp(old_manifest_path),
              "checks": [checked(rec) for rec in old_manifest["records"]]})
assert len(older) == 42
gk_addendum = checked(old_input["GK_separate_telemetry_addendum_preserved"])

accepted = [
    scoped("problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
           "complete R5A-E accepted mathematical body; R5D and G1/R5C are direct R6 premises; depth bound is minimum-only context"),
    scoped("problems/2021-B4/notes/rational-witness-p-plus-one-reviewed-v1.2.md",
           "complete rational affine normalization and field distinction"),
    scoped("problems/2021-B4/notes/padic-rational-newton-reviewed-v1.1.md",
           "complete accepted register and its root multiplicity/width scopes; old certificates not rerun"),
    scoped("problems/2021-B4/notes/coordinator-three-rational-witnesses-reviewed-v1.1.md",
           "complete accepted T1/T3 register; exact rational witness cover requirement; old certificate not rerun"),
    scoped("problems/2021-B4/proofs/reviewed-reasoning-J15-v1.1.md",
           "complete D1-D5 body and low-order nonunit family; D1/D3 direct setup"),
    scoped("problems/2021-B4/proofs/reviewed-return-r3-v1.1.md",
           "complete accepted scope register for immutable seven texts; G1 and TA1 direct"),
    scoped("problems/2021-B4/proofs/reviewed-odd-support-exclusion-v1.1.md",
           "complete accepted PN1-PN4 body; matches R5D scope, old certificate not rerun"),
]
old_math = [
    scoped("problems/2021-B4/notes/reasoning-return-r3-candidate-v1.md",
           "complete G1/G2 and weighted-even body reread; G1 direct carrier premise"),
    scoped("problems/2021-B4/notes/reasoning-return-r3-mirror-candidate-v1.md",
           "complete mirror body reread; retained tied/exact-reflection boundary"),
    scoped("problems/2021-B4/notes/reasoning-return-r3-collision-candidate-v1.md",
           "complete collision body reread; Euler mechanism and RC2 scope; no new claim for old depth bound"),
    scoped("problems/2021-B4/notes/reasoning-return-r3-transfer-candidate-v1.md",
           "complete TA1/TA2 body reread; exact TA1 hypothesis is direct first-break premise"),
]
scope_mds = [
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance.md",
    "problems/2021-B4/reviews/return-r3-acceptance.md",
    "problems/2021-B4/reviews/reasoning-J15-acceptance.md",
    "problems/2021-B4/reviews/odd-support-exclusion-acceptance.md",
]
context = [
    scoped("problems/2021-B4/reviews/return-r3-review-1-issues-v1.json",
           "entire old whole issue ledger read; qualifications preserved, no active R6 peer exists"),
    scoped("problems/2021-B4/reviews/return-r3-review-2-issues.json",
           "entire old whole issue ledger read; accepted scope and reminders retained"),
    scoped("problems/2021-B4/notes/reasoning-return-r5-source-audit-v1.md",
           "complete R5 source audit read as provenance, not fresh full reading of every cited paper"),
    scoped("problems/2021-B4/notes/ghosh-source-reviewed-register-v1.1.md",
           "complete narrow accepted source-objection register only; universal theorem unresolved and not imported"),
]
authority_jsons = [
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance.json",
    "problems/2021-B4/reviews/reasoning-return-r5-acceptance-integrity.json",
    "problems/2021-B4/reviews/return-r3-acceptance.json",
    "problems/2021-B4/reviews/reasoning-J15-acceptance.json",
    "problems/2021-B4/reviews/odd-support-exclusion-acceptance.json",
    "problems/2021-B4/reviews/witness-acceptance.json",
    "problems/2021-B4/reviews/newton-acceptance.json",
    "problems/2021-B4/reviews/three-witness-acceptance.json",
]
authority_checks = []
for path in authority_jsons:
    authority_checks.append({"authority": fp(path),
                             "declared_fingerprints": [checked(rec) for rec in records(read_json(path))]})

r5_sources_path = "problems/2021-B4/notes/reasoning-return-r5-sources-v1.json"
r5_input_path = "problems/2021-B4/notes/reasoning-return-r5-input-validation-v1.json"
r5_freeze_path = "problems/2021-B4/notes/reasoning-return-r5-freeze-v1.json"
chain_checks = []
for path in [r5_sources_path, r5_input_path, r5_freeze_path]:
    chain_checks.append({"chain_record": fp(path),
                         "declared_fingerprints": [checked(rec) for rec in records(read_json(path))]})

r5_raw = "problems/2021-B4/notes/reasoning-return-r5-candidate-v1.md"
r5_accepted = "problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md"
pn_raw = "problems/2021-B4/notes/coordinator-odd-support-exclusion-candidate-v1.md"
pn_accepted = "problems/2021-B4/proofs/reviewed-odd-support-exclusion-v1.1.md"
suffixes = []
for original, accepted_copy in [(r5_raw, r5_accepted), (pn_raw, pn_accepted)]:
    match = (ROOT / accepted_copy).read_bytes().endswith((ROOT / original).read_bytes())
    if not match:
        raise RuntimeError("Accepted body suffix mismatch: " + original)
    suffixes.append({"original": fp(original), "accepted_copy": fp(accepted_copy),
                     "byte_identical_complete_suffix": True})

usage = {"at_utc": "2026-10-17 12:37:37 UTC (paired clock/telemetry check)",
         "total_used_percent": 38, "window_minutes": 10080,
         "reset_unix": 1792745187, "total_ceiling_percent": 90,
         "integration_reserve": True, "separate_billed_API": False}
sources = {
    "recorded_at_utc": now, "status": "candidate proof - unverified",
    "constructor": ACTOR, "requested_settings": SETTINGS,
    "verified_effective_settings": None,
    "protocol": fp("AGENTS.md"),
    "complete_accepted_bodies_and_registers": accepted,
    "relevant_complete_old_mathematical_bodies_reread": old_math,
    "complete_acceptance_MD_records_read": [fp(p) for p in scope_mds],
    "other_precise_context_read_scopes": context,
    "primary_sources": [
        {"title": "Official2021 Paper B, B4(b)",
         "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
         "read_at_utc": "2026-10-17", "read_scope": "B4 hypothesis and(b); no preliminary(a) proof",
         "existing_ignored_cache": fp(".cache/official/2021-paper_b.pdf"),
         "fresh_viewer_cache_byte_identity_claimed": False},
        {"title": "CLO, Constraints on counterexamples to the Casas-Alvero conjecture, and a verification in degree12",
         "url": "https://arxiv.org/pdf/1208.5404", "read_at_utc": "2026-10-17",
         "read_scope": "equation7,Section3.4 equations9-10/simple-center factor/Lemma17; Proposition19 and unramified-field scope",
         "role": "normalization via accepted rational-affine map; ALL-root theorem inapplicable",
         "existing_ignored_cache": fp(".cache/literature/2021/cited-66c5af6a0f0239f5.pdf"),
         "fresh_viewer_cache_byte_identity_claimed": False},
        {"title": "Marashdeh, A descent-set obstruction for the Casas-Alvero conjecture",
         "url": "https://arxiv.org/html/2608.14726v1", "read_at_utc": "2026-10-17",
         "read_scope": "centered support definitions and full displayed TheoremB, nonvanishing and multi-root limitation",
         "role": "attributed one-nonzero-recycled-root context only; no theorem imported into R6",
         "fresh_whole_paper_or_full_proof_read_claimed": False,
         "raw_web_hash": None, "new_download": False},
    ],
    "new_external_theorem_imported": False,
    "old_finite_certificates_rerun_or_newly_independently_recertified": False,
    "constructor_old_return_authorship_J15_PN_R5_review_roles_disclosed": True,
    "new_quadratic_comparison_or_nonunit_formulation_supplied_by_root": False,
    "two_other_fresh_initially_blind_whole_reviews_required": True,
    "new_mathematical_program_CAS_scan_or_enumeration": False,
    "last_direct_weekly_telemetry": usage,
}
save("sources-v1.json", sources)

obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
obligation_count = sum(line.startswith("| R6-") for line in obligations.splitlines())
assert obligation_count == 36
input_validation = {
    "checked_at_utc": now, "metadata_only": True,
    "accepted_inputs_and_actual_read_scopes": accepted,
    "complete_old_bodies": old_math,
    "acceptance_authority_checks": authority_checks,
    "R5_frozen_dependency_chain_checks": chain_checks,
    "accepted_complete_suffix_checks": suffixes,
    "older_own_packets": older,
    "all_forty_two_older_own_packets_unchanged": True,
    "GK_separate_telemetry_addendum_preserved": gk_addendum,
    "constructor_self_check_is_independent_review": False,
    "proof_obligations": obligation_count,
    "scope": "R6A quadratic jet, R6B first-break fork, R6C paired-OR nonunit essential center, exact repeated2R branch only",
    "all_proposed_new_claims_candidate_unverified": True,
    "new_peer_R6_review_or_findings_read": False,
    "queued_2025_FS_target_or_new_peer_findings_read": False,
    "mathematical_program_CAS_scan_enumeration_or_author_rerun": False,
    "only_current_assigned_prefix_written": True,
    "old_shared_candidate_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
}
save("input-validation-v1.json", input_validation)

occ = list(records(input_validation)) + list(records(sources))
output = {
    "checked_at_utc": now,
    "administrative_only_no_mathematical_program": True,
    "accepted_and_old_record_occurrences": len(occ),
    "accepted_and_old_unique_paths": len({r["path"] for r in occ}),
    "older_own_packet_count": len(older),
    "all_declared_hash_checks_passed": True,
    "old_R5_and_PN_complete_accepted_suffixes_match": True,
    "candidate": fp(PREFIX + "candidate-v1.md"),
    "proof_obligations": obligation_count,
    "new_claims": ["R6A", "R6B", "R6C"],
    "candidate_status": "candidate proof - unverified; two other whole reviews needed",
    "command": "python3 problems/2021-B4/notes/reasoning-return-r6-freeze-v1.py",
    "latest_authoritative_weekly_usage": usage,
    "math_code_CAS_scan_author_rerun_shared_edits_or_git": False,
}
save("freeze-output-v1.json", output)

artifact_names = ["candidate-v1.md", "source-audit-v1.md", "worklog-v1.md",
                  "obligations-v1.md", "freeze-v1.py", "sources-v1.json",
                  "input-validation-v1.json", "freeze-output-v1.json"]
manifest = {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified",
    "constructor": ACTOR, "requested_settings": SETTINGS,
    "verified_effective_settings": None,
    "whole_claims": ["R6A", "R6B", "R6C"],
    "proof_obligations": obligation_count,
    "other_fresh_initially_blind_nonconstructor_whole_reviews_required": 2,
    "constructor_self_audit_is_independent_review": False,
    "preserved_older_own_packets": len(older),
    "old_constructor_and_review_roles_disclosed": True,
    "coefficient_free_fork_claimed_only_in_actual_repeated_root_setting": True,
    "new_math_program_CAS_enumeration_scan_or_author_rerun": False,
    "old_shared_candidate_or_git_mutation": False,
    "spawning_contact_charge_or_access_bypass": False,
    "queued_2025_FS_target_and_new_findings_still_unread": True,
    "full_degree20_mask_branch_annual_solution_lift_or_novelty_claim": False,
    "latest_authoritative_weekly_usage": usage,
    "command": output["command"],
    "records": [fp(PREFIX + name) for name in artifact_names],
}
save("freeze-v1.json", manifest)
print(json.dumps(dict(output, manifest=fp(PREFIX + "freeze-v1.json")), indent=2))
