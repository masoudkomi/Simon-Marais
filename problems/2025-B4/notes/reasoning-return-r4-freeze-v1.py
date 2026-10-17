"""Administrative fingerprints/JSON only; no mathematical computation."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/notes/reasoning-return-r4-"


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


for suffix in ("sources-v1.json", "input-validation-v1.json", "freeze-v1.json"):
    assert not (ROOT / (PREFIX + suffix)).exists(), "Do not overwrite frozen records"

prior_path = "problems/2024-B4/reviews/Kasami-whole-criterion-review-2-manifest-v1.json"
checked({"path": prior_path, "bytes": 2919,
         "sha256": "781dd7fb57677987f775251ef82a0b35cfd6dd307142bcb7b781a1bc94121449"})
prior = read_json(prior_path)
prior_validation = read_json("problems/2024-B4/reviews/Kasami-whole-criterion-review-2-input-validation-v1.json")
earlier = unique_checked(prior_validation["earlier_unique_records_preserved"]
                         + prior["artifacts"] + [record(prior_path)])
assert len(earlier) == 244

input_paths = (
    "AGENTS.md",
    "problems/2025-B4/statement.md",
    "problems/2025-B4/proof.md",
    "problems/2025-B4/proofs/reviewed-partial-v1.1.md",
    "problems/2025-B4/proofs/reviewed-power-gap-return-v1.1.md",
    "problems/2025-B4/proofs/reviewed-diagonal-firstcase-v1.1.md",
    "problems/2025-B4/proofs/reviewed-diagonal-moment-v1.1.md",
    "problems/2025-B4/notes/reviewed-literature-supplement-v1.md",
    "problems/2025-B4/reviews/strongfc-acceptance.md",
    "problems/2025-B4/notes/deep-literature-r1-report-v1.md",
    "problems/2025-B4/research.md",
    "problems/2025-B4/references.md",
    "problems/2025-B4/computations/literature-audit.md",
    "problems/2025-B4/notes/coordinator-diagonal-appendix-inspection-v1.md",
    "problems/2025-B4/notes/coordinator-diagonal-moment-separation-v1.3.md",
    "problems/2025-B4/notes/coordinator-diagonal-moment-sources-v1.json",
)
inputs = [record(path) for path in input_paths]
primary_pdf = checked({
    "path": ".cache/literature/deep-literature-r1/2025-bartolome-mihailescu-binary-thue-v2.pdf",
    "bytes": 300321,
    "sha256": "7108b665ebed8b2364c5a6629951d21abd400c96d4e7d5f4f81028f12ed424aa",
})
obligation_text = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
assert re.findall(r"^\| (FS\d{2}) \|", obligation_text, re.M) == [f"FS{i:02d}" for i in range(1, 41)]

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
sources = {
    "recorded_at_utc": now,
    "status": "candidate proof - unverified; attribution and read limits only",
    "official": {
        "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf",
        "actual_read_scope": "B4(b), primary PDF page2 reopened this return; signed integer domain and degree convention",
        "new_binary_hash": None,
        "hash_limit": "web PDF viewer, no new binary cached; earlier hash remains attributed in statement.md",
    },
    "original_diagonal": {
        "url": "https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren",
        "edition": "author-uploaded internal version2.0,2007-09-17; published2008",
        "actual_new_read_scope": "Section2.3 equations14-18 and complete Lemma3/proof; Section2.6 normalization and complete Lemmas6-7/proofs plus adjacent context",
        "prior_read_scope": "Relevant Section4.3, Fourier definition and paired selection/cancellation passages read during completed MS whole audit",
        "complete_Diophantine_proof_reconstructed": False,
        "binary_sha256": None,
        "hash_limit": "author-uploaded text viewer, no invented binary hash",
        "role": "definitions, exact original weight/selection interface and attribution of the already printed p-squared refinement",
    },
    "later_primary": {
        "url": "https://arxiv.org/pdf/1412.5798v2",
        "authors": ["B. Bartolome", "P. Mihailescu"],
        "title": "On the equation X^n-1=BZ^n",
        "edition": "internal version1.13,2021-11-02",
        "fingerprint": primary_pdf,
        "actual_new_read_scope": "Complete printed/PDFpp5-11 (definitions and Lemmas2.4-2.10 and start of application); complete Appendix5.2 acrosspp16-18 and referencesp19; page16 preceding Appendix5.1.1 ending",
        "complete_Diophantine_theorem_imported": False,
        "FS2_overlap": "Lemma2.7 already states the one-element selection conclusion; Appendix5.2 uses the product of action and inverse moments",
        "FS2_role": "Self-contained alternative proof for p>7, not a new existence theorem or novel method; nonexceptional domain and zero action moments handled explicitly",
        "small_prime_Lemma2_7_extension_imported": False,
        "binary_Thue_or_appendix_repair_imported": False,
    },
    "targeted_queries": [
        "Nagell Ljunggren diagonal x congruent 0 -1 p squared p-adic second case valuation",
        "Nagell Ljunggren equation negative x elementary p adic second case local solvability",
        "Fueter elements stabilizer order three Jacobi sums Stickelberger n squared n 1",
        "Jacobi sum stabilizer cubic roots unity Q zeta p a b Galois degree p minus 1 divided 3",
        "Fueter elements first third moment Stickelberger phi inverse moment stabilizer",
        '"Fueter" "moments" "Fermat"',
        '"Fueter" "stabilizer"',
        '"Fermat module" "weight" "moment"',
    ],
    "search_limit": "No additional applicable primary stabilizer theorem identified; no novelty or absence inference",
    "new_external_Diophantine_theorem": False,
    "FS1_FS3_priority": "unestablished; additional project deductions with full explicit proofs",
    "mathematical_program_CAS_scan_certificate_replay_or_sampling": False,
    "pypdf_role": "existing primary PDF text reading only",
    "download_purchase_contact_access_bypass": False,
    "complete_read_project_inputs": inputs,
}
sources_path = PREFIX + "sources-v1.json"
(ROOT / sources_path).write_text(json.dumps(sources, indent=2) + "\n")
validation = {
    "validated_at_utc": now,
    "administrative_integrity_only": True,
    "source_fingerprints": inputs + [primary_pdf],
    "earlier_unique_records_preserved": earlier,
    "earlier_unique_count": len(earlier),
    "forty_obligations_present": True,
    "all_files_written_under_assigned_new_prefix": True,
    "old_candidates_reviews_or_shared_files_edited": False,
    "next_2020_candidate_or_peer_findings_read_before_freeze": False,
    "constructor_self_check_not_independent_audit": True,
    "mathematical_computation_or_CAS": False,
    "Git_spawning_contact_charge_or_bypass": False,
}
validation_path = PREFIX + "input-validation-v1.json"
(ROOT / validation_path).write_text(json.dumps(validation, indent=2) + "\n")
artifacts = [record(PREFIX + suffix) for suffix in (
    "candidate-v1.md", "obligations-v1.md", "source-audit-v1.md",
    "worklog-v1.md", "constructor-check-v1.md", "sources-v1.json",
    "freeze-v1.py", "input-validation-v1.json")]
manifest = {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; complete algebraic checkpoint; two OTHER fresh initially blind whole audits required",
    "constructor": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "claims": {
        "FS1": "Exact Fueter stabilizer: trivial off t^2+t+1=0 for prime p>=5, exactly order3 on that locus; p3 excluded",
        "FS2": "For every prime p>7, one positive Fermat-module element of weight p-1 with nonzero inverse moment; attributed alternative proof of existing later Lemma2.7 selection route",
        "FS3": "For every prime p>7 and integer k>=2, k+1 pairwise nonconjugate free positive Fermat-module elements of common weight k(p-1), yielding disjoint full Fourier orbits",
    },
    "whole_obligations": 40,
    "external_Diophantine_exclusion_or_class_number_theorem_imported": False,
    "new_Diophantine_exclusion_full_source_repair_full_annual_or_novelty_claim": False,
    "remaining_gap": "Original-weight two-free-orbit selection OR complete higher-weight solution-specific interpolation, integrality, size, every-conjugate cancellation and nonzero delta; none supplied",
    "constructor_check_counts_as_independent_review": False,
    "mathematical_program_CAS_scan_certificate_rerun_or_sampling": False,
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "last_direct_weekly_telemetry": {
        "at_utc": "2026-10-17 12:21:14 UTC", "total_used_percent": 37,
        "window_minutes": 10080, "reset_unix": 1792745187,
        "total_ceiling_percent": 90, "integration_reserve": True,
    },
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
manifest_path = PREFIX + "freeze-v1.json"
(ROOT / manifest_path).write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"manifest": record(manifest_path), "artifacts": artifacts,
                  "earlier_unique_unchanged": len(earlier),
                  "whole_obligations": 40, "mathematical_computation": False}, indent=2))
