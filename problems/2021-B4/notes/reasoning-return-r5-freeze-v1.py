"""Exclusive R5 proof/source/hash freeze; administrative only, no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2021-B4/notes/reasoning-return-r5-"
SELF = "problems/2021-B4/reviews/reasoning-return-r5-constructor-self-check-v1.md"


def read_json(path):
    return json.loads((ROOT / path).read_text())


def row(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def check(expected):
    actual = row(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    return actual


def create(suffix, obj):
    path = PREFIX + suffix
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(obj, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    return row(path)


now = datetime.now(timezone.utc).isoformat()
accepted_specs = [
    ("notes/rational-witness-p-plus-one-reviewed-v1.2.md",
     "complete accepted normalization and rational/root-field distinction; direct R5A-C input"),
    ("notes/padic-rational-newton-reviewed-v1.1.md",
     "complete accepted general p+1 edge and multiplicity scope; direct R5C input"),
    ("notes/coordinator-newton-degeneration-reviewed-v1.1.md",
     "complete accepted small-cluster scope; context, not a substitute R5 inference"),
    ("notes/coordinator-three-rational-witnesses-reviewed-v1.1.md",
     "T1/T3 precise rational-cover and triple-zero factor scope; direct R5D-E and R5C corollary input"),
    ("notes/coordinator-three-complex-witnesses-reviewed-v1.1.md",
     "complete accepted complex three-cover scope; completed context only"),
    ("notes/coordinator-J16-exclusion-reviewed-v1.1.md",
     "complete accepted J16 exclusion scope; completed context, not R5 premise"),
    ("proofs/reviewed-reasoning-J15-v1.1.md",
     "complete D1-D5 and low-order-family boundary; D3 repeated-root setup and old conditional q0 form"),
    ("proofs/reviewed-J15-soleH2-v1.1.md",
     "complete necessary residue/actual witness roles; no row or mask exclusion"),
    ("proofs/reviewed-J15-soleH4-v1.1.md",
     "complete necessary residue/actual witness roles; no row or mask exclusion"),
    ("proofs/reviewed-return-r3-v1.1.md",
     "complete acceptance scope for seven exact mathematical bodies; RC2,TA1,G1 used at their actual hypotheses"),
    ("proofs/reviewed-odd-support-exclusion-v1.1.md",
     "complete PN1-PN4 proof/application scope; PN4 exact repeated-ladder conjunction"),
    ("notes/ghosh-source-reviewed-register-v1.1.md",
     "complete accepted narrow source-objection REGISTER; not a new full external-paper audit or universal theorem premise"),
]
accepted = [dict(row("problems/2021-B4/" + p), actual_read_scope=scope)
            for p, scope in accepted_specs]

return_specs = [
    ("reasoning-return-r3-candidate-v1.md", "0caf8d3f8df7144a7768230d566930da91ca107ab552935e9c2a73556f8aacc8"),
    ("reasoning-return-r3-mirror-candidate-v1.md", "20a72646d0e1bcfcf2ef3ca907d1363c6576a96df42dc2cb6909e11976e2945c"),
    ("reasoning-return-r3-collision-candidate-v1.md", "e7eab1257632a3d0e96c7e8eebcb9389197c7cd9041aca3dda6b5b463763c5ee"),
    ("reasoning-return-r3-parity-candidate-v1.md", "6506e371c2a3eb8506f75c55ef3d80be9933ecbcd187be21fe5bd18932fe8789"),
    ("reasoning-return-r3-sparse-descent-candidate-v1.md", "5c454767cda1bbbe4e4e4041256b837e6b0086c5489ad68007f522b24eccc864"),
    ("reasoning-return-r3-parity-barrier-candidate-v1.md", "284e7ddc5a3d26111d2af4bd169b7fc6d2739a169a70ae3d38ff68d3ac03ada5"),
    ("reasoning-return-r3-transfer-candidate-v1.md", "0bcc9898ff010abf489f7b4c58d4a5011e91df99ab680bd0094d76054b3e3961"),
]
seven = [check({"path": "problems/2021-B4/notes/" + name, "sha256": sha})
         for name, sha in return_specs]
assert len(seven) == 7
pn_raw = check({
    "path": "problems/2021-B4/notes/coordinator-odd-support-exclusion-candidate-v1.md",
    "sha256": "a7845441df7725edc5d30e28f7b8f28c529b0b710168ad4b068d279582c1857c",
})
pn_accepted_path = "problems/2021-B4/proofs/reviewed-odd-support-exclusion-v1.1.md"
assert (ROOT / pn_accepted_path).read_bytes().endswith((ROOT / pn_raw["path"]).read_bytes())

scope_paths = ["reviews/return-r3-acceptance.md", "reviews/odd-support-exclusion-acceptance.md",
               "reviews/J16-acceptance.json"]
scopes = [row("problems/2021-B4/" + p) for p in scope_paths]

additional_paths = [
    "proofs/initial-candidate-v1.md",
    "notes/padic-rational-newton-obstructions-v1.md",
    "notes/coordinator-newton-degeneration-v1.md",
    "notes/coordinator-three-rational-witnesses-v1.md",
    "notes/coordinator-three-complex-witnesses-v1.md",
    "notes/coordinator-three-complex-witnesses-v1-completion.md",
    "notes/coordinator-J16-coupled-leading-candidate-v1.md",
    "notes/coordinator-J16-coupled-digit-candidate-v1.md",
    "notes/owner-J16-Hensel-v1.md", "notes/owner-J16-Hensel-v2.md",
    "notes/coordinator-J15-triple-leading-candidate-v1.md",
    "notes/deep-literature-r1-report-v1.md", "notes/deep-literature-r1-sources-v1.json",
    "notes/coordinator-literature-frontier-recheck-v1.md",
    "notes/reasoning-return-r3-researchlog-v1.md",
    "notes/reasoning-return-r3-sources-v1.json",
    "notes/reasoning-return-r3-mirror-researchlog-v1.md",
    "notes/reasoning-return-r3-collision-researchlog-v1.md",
    "notes/reasoning-return-r3-parity-researchlog-v1.md",
    "notes/reasoning-return-r3-sparse-descent-sources-log-v1.md",
    "notes/reasoning-return-r3-parity-barrier-sources-log-v1.md",
    "notes/reasoning-return-r3-transfer-sources-log-v1.md",
]
additional = [row("problems/2021-B4/" + p) for p in additional_paths]
protocol = check({"path": "AGENTS.md", "bytes": 4707,
                  "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})
statement = row("problems/2021-B4/statement.md")
references = row("problems/2021-B4/references.md")
official = row(".cache/official/2021-paper_b.pdf")
clo = check({"path": ".cache/literature/2021/cited-66c5af6a0f0239f5.pdf",
             "bytes": 281743,
             "sha256": "d818747102d32060f43ae5f015f27065aadf38699b272a2367749db8b33fedbf"})

prior_path = "problems/2017-B4/reviews/allD-global-review-2-manifest-initial.json"
prior = check({"path": prior_path, "bytes": 2944,
               "sha256": "ef53fe377f92a876f71819741f5760db95146f05b5b7cedcacf1289298a5e152"})
earlier = {prior_path: prior}
for expected in read_json(prior_path)["artifacts"]:
    actual = check(expected)
    earlier[actual["path"]] = actual
for expected in read_json(
    "problems/2017-B4/reviews/allD-global-review-2-input-validation.json"
)["earlier_unique_records_preserved"]:
    actual = check(expected)
    if actual["path"] in earlier:
        assert earlier[actual["path"]] == actual
    earlier[actual["path"]] = actual
assert len(earlier) == 202

obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
for i in range(1, 31):
    assert f"| R5-{i:02d} |" in obligations
body = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
assert "Candidate proof - unverified" in body
assert "proves(6)+without" not in body
assert "some actually needed positive" not in body

sources = create("sources-v1.json", {
    "recorded_at_utc": now,
    "status": "candidate proof - unverified; complete R5A-E for two other fresh whole audits",
    "constructor": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "complete_accepted_bodies_and_registers_read": accepted,
    "all_seven_exact_accepted_return_mathematical_texts_read": seven,
    "PN_raw_body": pn_raw,
    "PN_complete_accepted_exact_suffix_verified": True,
    "complete_scope_records_read": scopes,
    "additional_complete_context_math_logs_source_maps_read": additional,
    "unverified_triple_leading_context_used_as_premise": False,
    "old_million_record_certificates_rerun_or_newly_independently_audited": False,
    "protocol": protocol, "official_statement": statement, "current_reference_map": references,
    "primary_sources": [
        {"title": "Official2021 Paper B", "url": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf",
         "read_scope": "complete B4 statement, part(b) only; no preliminary(a) proof investigated",
         "existing_cache": official, "fresh_viewer_byte_identity_claimed": False},
        {"title": "Castryck-Laterveer-Ounaies, Constraints on counterexamples to the Casas-Alvero conjecture, and a verification in degree12",
         "url": "https://arxiv.org/pdf/1208.5404",
         "read_scope": "Section3.4 equations9-10, full normalized root-factor discussion and Lemma17; nearby Section3.5 selector/divided-center context",
         "logical_role": "published normalized shape through accepted rational-affine map; not all-roots-rational Proposition19",
         "existing_cache": clo, "fresh_viewer_byte_identity_claimed": False},
        {"title": "Diaz-Lopez-Harris-Insko-Omar-Sagan, Descent polynomials",
         "url": "https://arxiv.org/html/1710.11033v2",
         "doi": "10.1016/j.disc.2019.01.034",
         "read_scope": "definition n>max I, Proposition2.1 and entire proof, Theorem2.2 polynomial extension",
         "logical_role": "classical recurrence, with exact R5 selector sign and positivity independently reconstructed",
         "new_download": False, "raw_viewer_hash": None},
        {"title": "Marashdeh, A descent-set obstruction for the Casas-Alvero conjecture",
         "url": "https://arxiv.org/html/2608.14726v1", "version": "v1,12August2026",
         "read_scope": "TheoremB and multi-root limit; Definition4.2,Corollary4.3,Theorem4.4/proof,Corollary4.6",
         "logical_role": "one-nonzero-root/MacMahon attribution only; no unrestricted multi-root theorem or maximal-count bound imported",
         "new_download": False, "raw_viewer_hash": None},
    ],
    "bounded_query": "Casas Alvero rational witnesses rational roots p-adic descent polynomial valuation",
    "nonprimary_results_used_as_mathematical_evidence": False,
    "novelty_or_current_complete_solution_claim": False,
    "new_math_program_CAS_scan_certificate_or_child": False,
    "last_direct_weekly_telemetry": {
        "at_utc": "2026-10-17 11:29:38 UTC", "total_used_percent": 34,
        "window_minutes": 10080, "reset_unix": 1792745187,
        "total_ceiling_percent": 90, "integration_reserve": True,
    },
})

validation = create("input-validation-v1.json", {
    "validated_at_utc": now,
    "metadata_not_mathematical_evidence": True,
    "complete_accepted_registers_and_bodies": accepted,
    "seven_accepted_return_texts_hash_checked": seven,
    "PN_raw_and_exact_accepted_suffix_checked": pn_raw,
    "scope_records": scopes,
    "additional_context_records": additional,
    "protocol_official_references_and_cache": [protocol, statement, references, official, clo],
    "earlier_unique_records_preserved": sorted(earlier.values(), key=lambda x: x["path"]),
    "earlier_unique_count": len(earlier),
    "thirty_proof_scope_obligations_present": True,
    "constructor_self_check_is_independent_audit": False,
    "new_math_program_CAS_scan_or_certificate_rerun": False,
    "only_new_assigned_r5_notes_and_constructor_review_prefixes_written": True,
    "shared_candidate_or_Git_mutation_spawning_contact_charge_or_bypass": False,
})
artifacts = [row(PREFIX + suffix) for suffix in [
    "candidate-v1.md", "obligations-v1.md", "source-audit-v1.md", "worklog-v1.md", "freeze-v1.py",
]] + [row(SELF), sources, validation]
assert len(artifacts) == 8
manifest = create("freeze-v1.json", {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; COMPLETE R5A-E checkpoint awaiting two other fresh initially blind whole audits",
    "constructor": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "claims": [
        "R5A every exact selector collapse q_I is nonzero signed descent count divided by p, with p^(nu_w+1) divisibility",
        "R5B uniform minimum positive selected-witness depth bound and nu_w<=10 at degree20; equal-valuation J15 nu<=10",
        "R5C symbolic p+1,J>=d/2 global long Eisenstein carrier is coprime to every derivative",
        "R5D exact repeated2R sole-H3 five-equation even-ladder subfamily is impossible by RC2+PN4",
        "R5E five odd units a5..a13 suffice for one higher even derivative with full monic gcd X-1; no a3 hypothesis",
    ],
    "whole_audit_obligations": 30,
    "selector_identified_with_unit_support": False,
    "all_possible_selector_parities_allowed": True,
    "minimum_bound_is_all_roots_or_height_bound": False,
    "carrier_quotient_asserted_Casas_Alvero": False,
    "full_J15_degree20_annual_classification_or_novelty_claim": False,
    "two_other_fresh_whole_nonconstructor_audits_required": True,
    "constructor_self_check_counted_as_one": False,
    "old_frozen_texts_or_scopes_overwritten": False,
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "mathematical_program_CAS_enumeration_scan_or_certificate_rerun": False,
    "shared_Git_spawning_contact_charges_or_access_bypass": False,
    "last_direct_weekly_telemetry": read_json(sources["path"])["last_direct_weekly_telemetry"],
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2021-B4/notes/reasoning-return-r5-freeze-v1.py",
    "artifacts": artifacts,
})
for expected in artifacts:
    check(expected)
print(json.dumps({"manifest": manifest, "artifacts": artifacts,
                  "earlier_unique_own_records_preserved": len(earlier),
                  "complete_accepted_registers_read": len(accepted),
                  "seven_exact_return_texts": len(seven),
                  "obligations": 30}, indent=2))
