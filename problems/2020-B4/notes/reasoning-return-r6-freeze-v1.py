"""Administrative integrity only: no mathematical calculation or source replay.

Creates ONLY new reasoning-return-r6-* JSON records. Refuses overwrites.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/notes/reasoning-return-r6-"

def record(path):
    p = ROOT / path
    data = p.read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}

def verified(expected):
    actual = record(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual["path"]
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual["path"]
    return actual

def write_new(suffix, value):
    path = ROOT / (PREFIX + suffix)
    if path.exists():
        # Resume an interrupted administrative freeze without changing bytes.
        assert json.loads(path.read_text()) == value, str(path)
        return
    with path.open("x", encoding="utf-8") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")

source_path = ROOT / (PREFIX + "sources-v1.json")
stamp = (json.loads(source_path.read_text())["recorded_at_utc"]
         if source_path.exists() else datetime.now(timezone.utc).isoformat())
old_manifest_path = "problems/2022-B4/reviews/reasoning-return-r6-review-2-manifest-v1.json"
verified({"path": old_manifest_path, "bytes": 3386,
          "sha256": "a94543c127fe98fdc5a44e6bf047245677b81fef5a2c65aee5d607f9e6e1fe27"})
old_manifest = json.loads((ROOT / old_manifest_path).read_text())
old_validation_path = "problems/2022-B4/reviews/reasoning-return-r6-review-2-input-validation-v1.json"
old_validation = json.loads((ROOT / old_validation_path).read_text())
old_records = old_validation["earlier_unique_records_preserved"]
assert len(old_records) == 328
old_records += old_manifest["artifacts"] + [record(old_manifest_path)]
prior = {}
for item in old_records:
    current = verified(item)
    if current["path"] in prior:
        assert prior[current["path"]] == current
    prior[current["path"]] = current
assert len(prior) == 334

accepted_paths = [
    "problems/2020-B4/proofs/reviewed-partial-v1.1.md",
    "problems/2020-B4/proofs/partial-v1.md",
    "problems/2020-B4/proofs/reviewed-return-r3-v1.2.md",
    "problems/2020-B4/proofs/reviewed-reasoning-return-r4-v1.2.md",
    "problems/2020-B4/proofs/reviewed-reasoning-return-r5-v1.1.md",
]
context_paths = [
    "AGENTS.md", "problems/2020-B4/statement.md",
    "problems/2020-B4/references.md",
    "problems/2020-B4/notes/reasoning-return-r5-source-audit-v1.md",
    "problems/2020-B4/notes/reasoning-return-r5-sources-v1.json",
    "problems/2020-B4/notes/deep-literature-r1-report-v1.md",
    "problems/2020-B4/notes/deep-literature-r1-sources-v1.json",
    "problems/2020-B4/notes/coordinator-quadratic-character-matrix-lead-v1.md",
]
cache_paths = [
    ".cache/official/2020-paper_b.pdf",
    ".cache/official/2020-solutions.pdf",
    ".cache/literature/2020/initial-review-2/gordon-small-lambda-v1.pdf",
    ".cache/literature/2020/reasoning-return-r5/HuangSchmidt2008.pdf",
    ".cache/literature/2020/reasoning-return-r5/Xia2023v7.pdf",
]
accepted = [record(p) for p in accepted_paths]
context = [record(p) for p in context_paths]
caches = [record(p) for p in cache_paths]
assert all((ROOT / p).read_bytes().startswith(b"%PDF-") for p in cache_paths)

sources = {
    "recorded_at_utc": stamp,
    "status": "candidate proof - unverified; complete constructor checkpoint",
    "constructor": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "older_repaired_R3_F1_F2_authorship_disclosed": True,
    "older_R4_R5_review_roles_not_new_self_audits": True,
    "new_mathematical_contribution_from_another_agent_used": False,
    "two_OTHER_initially_blind_whole_audits_required": True,
    "complete_accepted_bodies_read": accepted,
    "context_read_not_all_linked_external_proofs_reconstructed": context,
    "separate_matrix_lead_unverified_and_NOT_a_premise": True,
    "existing_native_cache_records_PDF_magic_verified": caches,
    "new_native_download_or_live_extraction_binary_identity_claimed": False,
    "primary_reads": [
        {"id": "OFF2020", "urls": [
            "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-paper-b_1.pdf",
            "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2020-solutions_1.pdf"],
         "scope": "page2 B4(b), printedp27 discussion; exact n>=2 target and attributed Singer existence context only",
         "preliminary_or_other_problem_investigated": False,
         "individual_setter_credit_verified": False},
        {"id": "COHEN1989", "title": "Generators in Cyclic Difference Sets",
         "url": "https://www.researchgate.net/publication/220077727_Generators_in_cyclic_difference_sets",
         "doi": "10.1016/0097-3165(89)90047-2",
         "actual_read": "Original definition, Theorem1, exact two literal exceptions, translation warning, order21 discussion and character-sieve context",
         "used": "Attributed accepted unit theorem, now with exact literal exceptions for relative order4 residual",
         "full_sieve_proof_or_exceptional_parameter_analysis_newly_certified": False,
         "native_binary_hash": None},
        {"id": "GORDON2020v1", "title": "On difference sets with small lambda",
         "url": "https://arxiv.org/pdf/2007.07292",
         "actual_read": "Introduction, complete applicable Section2 Lemma2/Theorem3, Theorems4/5 and proof contexts, Section3 table context",
         "used": "Arasu-method attribution and exact scope comparison; no general direct-product theorem imported beyond its hypotheses",
         "large_computation_or_heuristic_replayed_or_promoted": False,
         "native_cache": caches[2]},
        {"id": "BBB1990_1991", "title": "Hermitian unitals are code words",
         "url": "https://aeb.win.tue.nl/preprints/hermitian1.pdf",
         "actual_read": "Complete applicable Section2 pp1-2, normalized setting, involution and Lemmas1/2",
         "used": "Classical background for separately accepted F2; no general collineation or unital/code import",
         "native_binary_hash": None,
         "historical_stalled_native_hash_retrieval_retried_or_claimed_complete": False},
        {"id": "HUANG_SCHMIDT2008", "title": "Uniqueness of Some Cyclic Projective Planes",
         "url": "https://personal.ntu.edu.sg/bernhard/Publications/pub/Singer.pdf",
         "actual_read": "Introductory definitions, known Singer existence and separate conjecture context, supplementing prior accepted source reads",
         "used": "Attributed actual q5/q16 existence context only; no construction reproduced",
         "uniqueness_search_or_external_conjugacy_proof_imported": False,
         "native_cache": caches[3]},
        {"id": "XIA2023v7", "title": "New necessary conditions for finite non-Desarguesian flag-transitive projective planes",
         "url": "https://arxiv.org/pdf/1707.05486v7",
         "actual_read": "Definitions, Conjecture1.1, complete Proposition1.2/Theorem1.3 statements and necessary-system scope",
         "used": "Exact accepted R5 boundary only: ACTUAL non-Desarguesian FLAG-transitive reverse reduction",
         "CFSG_proof_or_finite_elimination_certificate_newly_imported_or_rerun": False,
         "native_cache": caches[4]},
    ],
    "search_queries_actual": [
        '"planar difference set" "prime order" "fixed" multiplier subplane bound',
        '"projective plane" "fixed subplane" "prime order" inequality',
        '"Baer subplane" "pointwise" "involution" collineation',
        '"multiplier" "q+m+1" difference set',
        '"difference sets" "fixed subgroup" "prime order" multipliers inequality',
        '"planar difference sets" "fixed" "prime" "trace"',
        '"Baer" "multiplier" "order" difference sets',
    ],
    "source_search_establishes_novelty_or_exhaustive_current_status": False,
    "full_classification_saturation_abstract_realization_or_cutoff_claim": False,
    "mathematical_program_CAS_scan_certificate_or_author_rerun": False,
    "native_mathematical_job_or_pending_approval": False,
    "charges_contacts_bypass_or_full_third_party_paper_tracked": False,
}
write_new("sources-v1.json", sources)

validation = {
    "validated_at_utc": stamp,
    "administrative_integrity_only": True,
    "accepted_bodies": accepted,
    "context_not_all_external_proofs_newly_read": context,
    "existing_primary_cache_records": caches,
    "earlier_unique_records_preserved": [prior[p] for p in sorted(prior)],
    "earlier_unique_record_count": len(prior),
    "queued_2021_R8_candidate_or_new_peer_findings_read_before_constructor_freeze": False,
    "mathematical_program_or_native_job": False,
}
write_new("input-validation-v1.json", validation)

artifact_suffixes = [
    "candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
    "constructor-checks-v1.md", "source-audit-v1.md", "worklog-v1.md",
    "sources-v1.json", "freeze-v1.py", "input-validation-v1.json",
]
artifacts = [record(PREFIX + suffix) for suffix in artifact_suffixes]
main = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
assert main.startswith("# Actual residual sets")
assert "**Candidate proof - unverified.**" in main
obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
assert sum(line.startswith("| O") for line in obligations.splitlines()) == 54

freeze = {
    "frozen_at_utc": stamp,
    "status": "candidate proof - unverified; COMPLETE R6A-R6D constructor checkpoint",
    "constructor": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "two_OTHER_initially_blind_whole_audits_required": True,
    "main_claims": [
        "R6A exact arbitrary cyclic coinvariant fiber energy, overlap c retained, orbit bound and prime-order equality defect",
        "R6B numerical common pointwise stabilizer at actual Baer fixed size has order2",
        "R6C nontrivial residual kernel forces actual smaller plane, r<=5 and s<=12; s>12 yields faithful residual and r>=3log_3(s)",
        "R6C4 attributed actual q16 example makes faithfulness threshold s>12 sharp",
        "R6D nonsquare q=1mod3 full/known multiplier size obeys3s<=q-2+2sqrt(q)",
    ],
    "whole_obligations": 54,
    "older_R3_authorship_and_R4_R5_review_roles_disclosed": True,
    "new_proof_contribution_from_another_agent_used": False,
    "new_peer_2020_R6_findings_or_queued_2021_R8_material_read": False,
    "mathematical_program_CAS_scan_table_certificate_or_author_rerun": False,
    "current_native_job_or_pending_tool_call": False,
    "earlier_frozen_context_records_verified_unchanged": len(prior),
    "last_direct_weekly_telemetry": {
        "at_utc": "2026-10-17 15:39:49 UTC; later direct check again48%",
        "total_used_percent": 48, "window_minutes": 10080,
        "reset_unix": 1792745187, "total_ceiling_percent": 90,
        "review_integration_reserve": True,
    },
    "unproved": [
        "universal S0 saturation (actually false for known q5 classical example)",
        "nonsaturated large-residual incidence/phase exclusion",
        "unrestricted prime-power or official taut classification",
        "novelty or improved published verification cutoff",
    ],
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2020-B4/notes/reasoning-return-r6-freeze-v1.py",
    "artifacts": artifacts,
}
write_new("freeze-v1.json", freeze)
print(json.dumps({
    "frozen_at_utc": stamp,
    "artifacts": len(artifacts), "whole_obligations": 54,
    "earlier_records_preserved": len(prior),
    "candidate": artifacts[0],
    "freeze": record(PREFIX + "freeze-v1.json"),
}, indent=2))
