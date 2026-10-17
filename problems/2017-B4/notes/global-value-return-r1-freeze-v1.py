"""Administrative integrity/JSON only. No mathematical counting or search."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/notes/global-value-return-r1-"


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def read_json(path):
    return json.loads((ROOT / path).read_text())


def checked(expected):
    actual = record(expected["path"])
    for key in ("path", "bytes", "sha256"):
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


for suffix in ("sources-v1.json", "input-validation-v1.json", "manifest-v1.json"):
    assert not (ROOT / (PREFIX + suffix)).exists(), "Do not overwrite frozen output"

prior_path = "problems/2020-B4/reviews/reasoning-return-r4-review-2-manifest-v1.json"
checked({"path": prior_path, "bytes": 3301,
         "sha256": "7353007da13f3f563ebb67684dd2c5fc6a2313b58388d4fc659570a6a8940a07"})
prior = read_json(prior_path)
prior_validation = read_json("problems/2020-B4/reviews/reasoning-return-r4-review-2-input-validation-v1.json")
earlier = unique_checked(prior_validation["earlier_unique_records_preserved"]
                         + prior["artifacts"] + [record(prior_path)])
assert len(earlier) == 259

global_source_path = "problems/2017-B4/notes/allD-global-reasoning-r1-sources-v1.json"
global_source = read_json(global_source_path)
ten_interfaces = unique_checked(global_source["logical_accepted_inputs"])
assert len(ten_interfaces) == 10
dc = checked({"path": "problems/2017-B4/proofs/reviewed-direction-coarsening-v1.1.md",
              "bytes": 9175,
              "sha256": "98c04673acdb4c59d44eb4d977f844d3f01ef27365399982e02df8cbaa4a6241"})
cached_dallant = checked({
    "path": ".cache/literature/deep-literature-r2/2017-dallant-zone-2502.20909v2.pdf",
    "bytes": 618656,
    "sha256": "9ae4886f8b1fce91c6ae8e86c577c5690d0f2ef10355a6524235f95a18dfa03b"})
cached_official = checked({
    "path": ".cache/official/2017-paper_b.pdf", "bytes": 112458,
    "sha256": "69d7cf84128c2464d962136ed613808b6c7a7b07122cfba9c06b5adf775e2a68"})

direct_paths = [
    "AGENTS.md", "problems/2017-B4/statement.md",
    "problems/2017-B4/references.md", "problems/2017-B4/research.md",
    "problems/2017-B4/proofs/reviewed-direction-coarsening-v1.1.md",
    "problems/2017-B4/proofs/reviewed-allD-global-v1.1.md",
    "problems/2017-B4/proofs/reviewed-concavity-v1.1.md",
    "problems/2017-B4/notes/allD-global-reasoning-r1-sources-v1.md",
    global_source_path,
    "problems/2017-B4/notes/coordinator-global-limit-literature-recheck-v1.md",
    "problems/2017-B4/reviews/allD-global-acceptance.md",
    "problems/2017-B4/reviews/coarsening-acceptance.md",
    "problems/2017-B4/reviews/concavity-acceptance.md",
]
direct = [record(path) for path in direct_paths]
cache = [cached_official, record(".cache/official/2017-solutions.pdf"), cached_dallant]
obligations = (ROOT / (PREFIX + "obligations-v1.md")).read_text()
assert re.findall(r"^\| (GV-O\d{2}) \|", obligations, re.M) == [f"GV-O{i:02d}" for i in range(1, 41)]
main = (ROOT / (PREFIX + "candidate-v1.md")).read_text()
for marker in ("**V1", "**V2", "**V3", "**V4", "**(E)**", "**(R)**"):
    assert marker in main
assert "Neither (E) nor (R) is proved here." in main

now = datetime.datetime.now(datetime.timezone.utc).isoformat()
sources = {
    "recorded_at_utc": now,
    "status": "candidate proof - unverified; source scopes are not independent review",
    "direct_full_logical_or_protocol_context_reads": direct,
    "global_ten_accepted_transitive_interfaces_checked_against_frozen_source_hashes": ten_interfaces,
    "transitive_input_read_scope": "Complete global proof/source scope reread; ten local interfaces retain their exact accepted scopes and previously completed full reads/audits. This return does not claim a new independent re-audit of the constructor's older local input.",
    "existing_cache_fingerprints": cache,
    "primary_web_reads": [
        {
            "url": "https://arxiv.org/pdf/2502.20909v2",
            "title": "Justin Dallant, Improved Bound on the Number of Pseudoline Arrangements via the Zone Theorem, v2 (2025-03-07)",
            "read": "Introduction printed pp1-2 directly reopened; full older U packet source proof already separately reviewed",
            "role": "Dated primary marked convention/bounds/open-limit context only; no new theorem import",
            "full_new_binary_download": False,
        },
        {
            "url": "https://drops.dagstuhl.de/storage/00lipics/lipics-vol293-socg2024/LIPIcs.SoCG.2024.43/LIPIcs.SoCG.2024.43.pdf",
            "title": "Cortes Kuhnast, Dallant, Felsner, Scheucher, SoCG2024",
            "read": "Printed pp43:1-43:3, convention, Theorem1 and outline",
            "role": "Dated context; complete computational lower-bound proof and certificate not reconstructed or replayed",
            "full_new_binary_download": False,
        },
        {
            "url": "https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n3-p12-p.pdf",
            "title": "Hochman and Meyerovitch, A characterization of the entropies of multidimensional shifts of finite type (2010)",
            "doi": "10.4007/annals.2010.171.2011",
            "read": "Full relevant Sections1-3, printed pp2011-2021, including SFT/strong-irreducibility definitions and complete Theorem1.3 proof",
            "role": "Model-specific computability context; no SFT or strong-irreducibility application to L/ell_D",
            "web_viewer_binary_hash_available": False,
        },
    ],
    "failed_primary_retrieval": {
        "url": "https://doc.rero.ch/record/304204/files/S0022481200105663.pdf",
        "description": "Specker1949 primary scan located; web open internal error",
        "full_text_read": False, "theorem_imported": False,
    },
    "unestablished_effective_hypotheses": ["E: uniformly computable balanced excess envelope tending to zero", "R: uniformly computable convergent upper approximants to ell_D"],
    "new_computability_or_numerical_value_claim": False,
    "full_external_paper_redistribution_or_charge_or_contact_or_bypass": False,
}
(ROOT / (PREFIX + "sources-v1.json")).write_text(json.dumps(sources, indent=2) + "\n")

validation = {
    "validated_at_utc": now,
    "administrative_integrity_only": True,
    "direct_input_records": direct,
    "ten_transitive_exact_accepted_inputs": ten_interfaces,
    "existing_cache_records": cache,
    "all_40_author_obligations_present": True,
    "earlier_unique_records_preserved": earlier,
    "earlier_unique_count": len(earlier),
    "prior_manifest": record(prior_path),
    "new_claims_constructed_here": ["V1", "V2", "V3", "V4"],
    "new_independent_reviews_complete": 0,
    "two_OTHER_whole_initially_blind_audits_required": True,
    "mathematical_program_CAS_scan_simulation_certificate_replay_or_author_rerun": False,
    "Git_shared_write_spawning_contact_charge_or_bypass": False,
}
(ROOT / (PREFIX + "input-validation-v1.json")).write_text(json.dumps(validation, indent=2) + "\n")
artifacts = [record(PREFIX + suffix) for suffix in (
    "candidate-v1.md", "obligations-v1.md", "constructor-checks-v1.md",
    "source-checks-v1.md", "worklog-v1.md", "freeze-v1.py",
    "sources-v1.json", "input-validation-v1.json")]
manifest = {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; complete mathematical/source/failure checkpoint awaiting two OTHER whole audits",
    "constructor": "/root/review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "scope": "2017 B4 entire, marked count; sharper finite coarsening and fixed-D direction error, conditional effective bridge, abstract obstruction only",
    "proposed_results": {
        "V1": "C(n)<=B(m) product W_mi(n-mi)<=B(m) product C(mi)binom(n-1,mi-1)^mi",
        "V2": "ell_D<=L<=D/(D-1)(ell_D+h2(1/D)); 0<=L-ell_D<=h2(1/D)+U/D, U=324757/500000",
        "V3": "Explicit unestablished E gives left semicomputation; E+R gives computability; no unconditional E/R claim",
        "V4": "Computable integer abstract counts, exact quadratic replication and zero balanced deficit with noncomputable limit; not a tiling counterexample",
    },
    "author_obligations": 40,
    "new_independent_reviews_complete": 0,
    "two_OTHER_initially_blind_whole_nonconstructor_audits_required": True,
    "new_numerical_value_full_annual_solution_effective_p_rate_SFT_application_or_novelty": False,
    "unconditional_computability_or_noncomputability_of_actual_L_claimed": False,
    "earlier_unique_own_paths_verified_unchanged": len(earlier),
    "all_ten_accepted_transitive_input_hashes_checked": True,
    "mathematical_program_CAS_scan_simulation_certificate_replay_or_author_rerun": False,
    "last_direct_weekly_telemetry": {
        "at_utc": "2026-10-17 12:45:25 UTC", "total_used_percent": 38,
        "window_minutes": 10080, "reset_unix": 1792745187,
        "total_ceiling_percent": 90, "integration_reserve": True,
    },
    "administrative_command": "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 " + PREFIX + "freeze-v1.py",
    "artifacts": artifacts,
}
manifest_path = PREFIX + "manifest-v1.json"
(ROOT / manifest_path).write_text(json.dumps(manifest, indent=2) + "\n")
print(json.dumps({"manifest": record(manifest_path), "artifacts": artifacts,
                  "old_own_paths_verified_unchanged": len(earlier),
                  "transitive_accepted_inputs_verified": len(ten_interfaces),
                  "author_obligations": 40, "new_independent_reviews": 0}, indent=2))

