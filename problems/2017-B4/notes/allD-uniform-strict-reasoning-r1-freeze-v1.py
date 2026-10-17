"""One-time source/integrity checkpoint; no mathematical calculation or search."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/notes/allD-uniform-strict-reasoning-r1-"


def fingerprint(path):
    payload = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest()}


def check(expected):
    actual = fingerprint(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    return dict(actual, matches=True)


def read_json(path):
    return json.loads((ROOT / path).read_text())


def create_json(suffix, payload):
    path = PREFIX + suffix
    with (ROOT / path).open("x") as stream:
        json.dump(payload, stream, indent=2)
        stream.write("\n")
    return path


now = datetime.now(timezone.utc).isoformat()
body_specs = [
    ("proofs/reviewed-fixedD-structural-v1.2.md", "421dc271ed65831e3aa70057a0d74c4d999ba8249dfa2b99066dfdc298f86868", "accepted logical marked dictionary/gradient input"),
    ("proofs/reviewed-directed-geodesics-v1.1.md", "061ae1749e938aad68f1824ab5f33583a3a1c58e556bd62649309c7cb12da9aa", "accepted logical DG1/DG2 fixed-D full-tiling input"),
    ("proofs/reviewed-lens-cutting-v1.1.md", "81f175e2a0f10665e9228d18885180e91b4db6167001584182d9de4b9cb437fc", "accepted logical fixed-D CUT, constants reconstructed"),
    ("proofs/reviewed-annulus-v1.2.md", "51c02b22a36705c736e4debefcfde0afbc1b2678a8d6092213d8ed00e6a75baf", "D4 method/provenance only; all-D AD1-AD5 proved anew"),
    ("proofs/reviewed-strict-transfer-v1.1.md", "89f2bc8068a4f151621ed4cdcdfb0e6dc891d51d43452b5f176d41fa62a840eb", "D4 method/provenance, not a D>4 theorem premise"),
    ("proofs/reviewed-uniform-strict-v1.1.md", "096eeb2328483c17519528e801b479076e35f582d17e05479fc3def4a6a2804a", "own accepted D4 method, new extension requires two others"),
    ("statement.md", "e459750064b4e25e3eaa71f25f236c046548147e415b06d8bd097839020228f3", "official authorized problem/domain record"),
]
dependency_checks = []
source_rows = []
for relative, sha, role in body_specs:
    actual = check({"path": "problems/2017-B4/" + relative, "sha256": sha})
    dependency_checks.append(actual)
    source_rows.append(dict(actual, role=role, whole_body_read=True))
acceptance_checks = [fingerprint("problems/2017-B4/reviews/" + name) for name in [
    "fixedD-structural-acceptance.md", "directed-geodesics-acceptance.md",
    "lens-cutting-acceptance.md", "annulus-acceptance.md",
    "strict-transfer-acceptance.md", "uniform-strict-acceptance.md",
]]
program_check = check({
    "path": "problems/2017-B4/notes/coordinator-dimension-induction-program-v1.md",
    "sha256": "b499899787f8d8607ba030ec21173451267ea0b1dd6d419481a548a103c2f291",
})

prior_path = "problems/2017-B4/reviews/chart-window-review-1-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "ed3a03cf0c65121b25e0d70806e202052fcece684fad43ae5d563cfde6dd9b98"})
prior_checks = [check(row) for row in read_json(prior_path)["records"]]
prior_validation = read_json("problems/2017-B4/reviews/chart-window-review-1-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 30
older.append({"manifest": prior_fp, "checks": prior_checks})

main = fingerprint(PREFIX + "candidate-v1.md")
assert "Candidate proof - unverified" in (ROOT / main["path"]).read_text()
obligations = read_json(PREFIX + "obligations-v1.json")
assert obligations["independent_whole_nonconstructor_audits_required"] == 2
assert obligations["mathematical_program_enumeration_or_CAS"] is False

sources_path = create_json("sources-v1.json", {
    "recorded_at_utc": now,
    "status": "candidate proof - unverified",
    "local_records": source_rows,
    "acceptance_scopes_read": acceptance_checks,
    "dimension_program_motivation_not_premise": program_check,
    "primary_external_source": {
        "authors": "Alan Arroyo, Dan McQuillan, R. Bruce Richter, Gelasio Salazar",
        "title": "Levi's Lemma, pseudolinear drawings of K_n, and empty triangles",
        "author_version_date": "2015-11-20",
        "url": "https://www.ifisica.uaslp.mx/~gsalazar/RESEARCH/levi.pdf",
        "retrieved_date_utc": "2026-10-17",
        "access": "fresh complete primary PDF opened via web viewer, no native download",
        "pdf_pages": 22,
        "applicable_text_read": "Section2 complete arrangement-of-arcs definition, Lemma2.2 statement and induction proof, printed pp4-5",
        "parallel_disjoint_pairs_permitted": True,
        "raw_binary_sha256": None,
        "raw_binary_hash_limitation": "Web viewer supplies text without raw binary bytes; none invented",
        "logical_role": "published arc input behind accepted DG disk/cell adaptation",
        "full_external_paper_proof_claimed": False,
        "redistribution_or_charge": False,
    },
    "new_external_entropy_theorem": False,
    "CW_SP_RM_UR3_or_global_G4_premise": False,
    "global_G4_candidate_read_during_construction": False,
    "mathematical_program_enumeration_or_CAS": False,
})
validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "candidate": main,
    "accepted_body_checks": dependency_checks,
    "acceptance_scope_fingerprints": acceptance_checks,
    "all_seven_named_body_hashes_match": True,
    "dimension_program_motivation_not_premise": program_check,
    "older_own_packets": older,
    "all_thirty_one_older_own_packets_unchanged": True,
    "older_D4_accepted_bodies_modified": False,
    "whole_new_constructive_packet_completed_before_reassignment": True,
    "mathematical_program_enumeration_or_CAS": False,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "candidate": main,
    "named_body_checks": 7,
    "acceptance_scopes_recorded": 6,
    "older_own_packets_checked": 31,
    "all_fingerprints_match": True,
    "status": "candidate proof - unverified; complete local extension ready for two other whole audits",
    "author_identified_open_gap_in_stated_local_scope": None,
    "global_UR_D_H_PR_or_official_solution_claim": False,
    "candidate_or_shared_old_mutation": False,
    "git_operations": False,
})
record_paths = [PREFIX + name for name in [
    "candidate-v1.md", "researchlog-v1.md", "sources-v1.md",
    "obligations-v1.json", "freeze-v1.py",
]] + [sources_path, validation_path, output_path]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; complete fixed-D strict local extension",
    "constructor": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": main["sha256"],
    "candidate_bytes": main["bytes"],
    "dimension": "each fixed D>=3",
    "claims": ["AD1", "AD2", "AD3", "AD4", "AD5", "US_D1", "US_D2", "US_D3"],
    "independent_whole_nonconstructor_audits_required": 2,
    "coordinator_strategy_role_disclosed_not_independent_audit": True,
    "full_all_color_rank_phase_annulus_and_uniform_proofs_included": True,
    "denominators_change_L0_not_epsilon": True,
    "global_UR_D_H_PR_or_official_limit_claim": False,
    "own_old_D4_proof_or_other_frozen_packet_changed": False,
    "mathematical_program_enumeration_or_CAS": False,
    "git_shared_edits_or_spawning": False,
    "latest_weekly_total_used_percent": 29,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2017-B4/notes/allD-uniform-strict-reasoning-r1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "candidate": main,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "named_body_checks": 7,
                  "older_own_packets_checked": 31}, indent=2))
