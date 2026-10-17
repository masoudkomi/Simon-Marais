"""Exclusive metadata/source checkpoint. No mathematical calculation or search."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/notes/allD-global-reasoning-r1-"


def fingerprint(path):
    payload = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(payload),
            "sha256": hashlib.sha256(payload).hexdigest()}


def check(expected):
    actual = fingerprint(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    return actual


def read_json(path):
    return json.loads((ROOT / path).read_text())


def create_json(suffix, payload):
    path = PREFIX + suffix
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    return path


now = datetime.now(timezone.utc).isoformat()
body_specs = [
    ("reviewed-fixedD-structural-v1.2.md",
     "421dc271ed65831e3aa70057a0d74c4d999ba8249dfa2b99066dfdc298f86868",
     "FD full dictionary/alphabet/gradient/K_D closure; no H/PR",
     "whole body read during immediately preceding whole audits; exact current hash checked"),
    ("reviewed-rank-mesh-v1.2.md",
     "791ed756bd0ad4ceeb8d98265d35e5dfffee95adcfdeebf156253872b4fdf634",
     "general RM1 disks/ports/diameter and aggregate perimeter/area only; no D4 RM2 or UR3 premise",
     "whole accepted body read during whole and repair audits and preceding G4 audit; exact current scope retained"),
    ("reviewed-orientation-charts-v1.1.md",
     "d15ed547defaffc617ffc6faf6df683c8473ecd9077be63e52d02bbb4edb4ca8",
     "OC1-3 fixed-D zero/antiparallel charts and exact full BALANCED transformations",
     "whole accepted body freshly reread for this construction"),
    ("reviewed-clean-strata-v1.1.md",
     "10a2efb8d11433726b7812e18217719ab24543887a2d01e0fd96ad51d96204b0",
     "FL1 general fixed-D rare count including L+1; no defective local CL1 extension",
     "whole body read during earlier whole and immediately preceding G4 audits; acceptance scope freshly reread"),
    ("reviewed-local-rank-mesh-v1.1.md",
     "67d6821f64c0be2a64bb49ccd595dd80105ca7ed913b2fd6be342b81cf756a10",
     "LW1 exact LOCAL code with one log R anchor and actual global retained faces",
     "whole accepted body freshly reread; historical RM1 conditional discharged"),
    ("reviewed-chart-window-v1.1.md",
     "f89e784c407f3c780d2ca9a95ea4f58e0cd71841f2855ffa7225465f9dd9abc1",
     "CW0-4 common offsets, whole-buffer winding, all-source recovery and exact fine inverse/dilation",
     "whole accepted body freshly reread for this construction"),
    ("reviewed-single-pair-allD-v1.1.md",
     "b66e494bab6ef872565d8f1574fb96094c5b0c7f5a59f7ba9d79c03d23a08c84",
     "SP1-3 one pair/D-2 singleton groups, closed cleanliness, every-M count bijection, actual small GE exterior",
     "whole accepted body and acceptance record freshly reread"),
    ("reviewed-allD-uniform-strict-v1.1.md",
     "a5ebfd81d59b26f301b1e105889451f4c86262da80e6e77e6913c045d71147d2",
     "S_D AD1-5/US_D1-3 each fixed D>=3 strict LOCAL only; quantitative tolerance caps precede periods",
     "raw whole body independently audited before construction; new accepted header read and entire suffix compared"),
    ("reviewed-remainder-padding-v1.1.md",
     "4b1742c46ddd120f935653538758fed41759187ad26cfed79b9bd86a48d99018",
     "RP1-3 balanced injection and ALL-large-multiples bounded-remainder passage",
     "whole body read in prior whole/preceding G4 audits; acceptance freshly reread"),
    ("reviewed-direction-coarsening-v1.1.md",
     "98c04673acdb4c59d44eb4d977f844d3f01ef27365399982e02df8cbaa4a6241",
     "DC1/DC2 finite full-count comparison, entropy error and H_D-to-official conditional passage",
     "whole accepted body and acceptance record freshly reread"),
]
accepted_bodies = []
for name, sha, role, scope in body_specs:
    row = check({"path": "problems/2017-B4/proofs/" + name, "sha256": sha})
    accepted_bodies.append(dict(row, role=role, actual_read_scope=scope,
                                separately_accepted=True))

acceptance_names = [
    "fixedD-structural", "rank-mesh", "orientation-charts", "clean-strata",
    "local-rank-mesh", "chart-window", "single-pair-allD",
    "allD-uniform-strict", "remainder-padding", "coarsening",
]
acceptance_records = [
    fingerprint("problems/2017-B4/reviews/" + name + "-acceptance.md")
    for name in acceptance_names
]

strict_raw_path = "problems/2017-B4/notes/allD-uniform-strict-reasoning-r1-candidate-v1.md"
strict_raw = check({"path": strict_raw_path, "bytes": 37267,
                    "sha256": "fc280881b1df650d07ab48f0f4c19d0e77f076e6b39a13f3a0b8d9969074a433"})
strict_accepted_path = "problems/2017-B4/proofs/reviewed-allD-uniform-strict-v1.1.md"
assert (ROOT / strict_accepted_path).read_bytes().endswith((ROOT / strict_raw_path).read_bytes())
strict_manifest_path = "problems/2017-B4/notes/allD-uniform-strict-reasoning-r1-manifest-v1.json"
strict_manifest = check({
    "path": strict_manifest_path,
    "sha256": "126fd14f143d6ab619c7aba5d57be968471080d7f07bb081805f6706434b1f18",
})
strict_submission_checks = [
    check(row) for row in read_json(strict_manifest_path)["records"]
]
assert len(strict_submission_checks) == 8

context = [
    dict(fingerprint("problems/2017-B4/notes/coordinator-allD-induction-draft-v1.md"),
         role="unverified strategy outline, fully read; NOT mathematical premise"),
    dict(check({
        "path": "problems/2017-B4/notes/coordinator-UR4-assembly-candidate-v1.md",
        "bytes": 22839,
        "sha256": "fa0bd05d345dee884335e3a5cd0e601ce08e8212da3d812227750f04c5113d0f",
    }), role="earlier D4 special-case research context, NOT theorem premise"),
    dict(check({
        "path": "problems/2017-B4/proofs/reviewed-UR4-assembly-v1.1.md",
        "sha256": "d57593f00439b76dcd283d0cd9487ccfce92782c137d2bc75f95db003179ffdc",
    }), role="D4 acceptance received during construction; NOT induction premise"),
    dict(fingerprint("problems/2017-B4/reviews/UR4-assembly-acceptance.md"),
         role="context status only; no all-D conclusion imported"),
]
protocol = [
    check({"path": "AGENTS.md",
           "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"}),
    check({"path": "problems/2017-B4/statement.md",
           "sha256": "e459750064b4e25e3eaa71f25f236c046548147e415b06d8bd097839020228f3"}),
    fingerprint("problems/2017-B4/references.md"),
    check({"path": ".cache/official/2017-paper_b.pdf",
           "sha256": "69d7cf84128c2464d962136ed613808b6c7a7b07122cfba9c06b5adf775e2a68"}),
]

prior_validation_path = "problems/2017-B4/reviews/allD-uniform-strict-review-2-input-checks-v1.json"
prior_manifest_path = "problems/2017-B4/reviews/allD-uniform-strict-review-2-manifest-v1.json"
check({"path": prior_manifest_path,
       "sha256": "d4e72df92c91ee1e46f5cbdd9a43acf5d57598f1ca7c81c413baccbc465d8a52"})
earlier = {}
for row in read_json(prior_validation_path)["earlier_own_records"]:
    earlier[row["path"]] = row
for row in read_json(prior_manifest_path)["records"] + [fingerprint(prior_manifest_path)]:
    if row["path"] in earlier:
        assert check(earlier[row["path"]]) == check(row)
    earlier[row["path"]] = row
earlier_checks = [check(row) for row in earlier.values()]
assert len(earlier_checks) == 138

candidate = fingerprint(PREFIX + "candidate-v1.md")
assert "Candidate proof - unverified" in (ROOT / candidate["path"]).read_text()
obligations = read_json(PREFIX + "obligations-v1.json")
assert len(obligations["new_inferences_for_complete_adversarial_review"]) == 40
assert obligations["required_other_initially_blind_whole_nonconstructor_audits"] == 2
assert obligations["all_named_local_inputs_separately_accepted_at_freeze"] is True

sources_path = create_json("sources-v1.json", {
    "recorded_at_utc": now,
    "status": "candidate proof - unverified; new global argument not yet reviewed",
    "logical_accepted_inputs": accepted_bodies,
    "acceptance_scope_fingerprints": acceptance_records,
    "strict_status_chronology": {
        "conditional_at_construction_start": True,
        "separate_local_acceptance_received_during_construction": True,
        "raw": strict_raw,
        "accepted": fingerprint(strict_accepted_path),
        "accepted_copy_has_entire_exact_raw_suffix": True,
        "mathematical_local_body_changed": False,
        "new_global_result_accepted": False,
    },
    "strict_original_manifest": strict_manifest,
    "strict_original_submission_records": strict_submission_checks,
    "research_context_NOT_premises": context,
    "protocol_official_records": protocol,
    "primary_attribution": {
        "official_paper": "https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf",
        "official_scope": "2017 B4 whole; integer n>=2, normalized scalar liminf and limsup; marked convention retained",
        "arc_source": "https://www.ifisica.uaslp.mx/~gsalazar/RESEARCH/levi.pdf",
        "arc_authors": "Arroyo, McQuillan, Richter, Salazar",
        "arc_author_date": "2015-11-20",
        "actual_read_scope": "Section2 arrangement definition, Lemma2.2 and induction proof printed pp4-5 directly read in preceding whole all-D strict audit on2026-10-17",
        "arc_raw_binary_hash": None,
        "arc_hash_limitation": "web viewer, no raw binary downloaded or invented",
        "logical_role": "underlying accepted strict DG/CUT geometry only; no external entropy input",
    },
    "new_global_proofs_in_candidate_not_external_import": True,
    "CKP_UR3_dimer_G4_or_dimension_outline_premise": False,
    "novelty_or_priority_claimed": False,
})

inputs = {}
for row in (accepted_bodies + acceptance_records + [strict_raw, strict_manifest]
            + strict_submission_checks + context + protocol):
    actual = check(row)
    if actual["path"] in inputs:
        assert inputs[actual["path"]] == actual
    inputs[actual["path"]] = actual
validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "metadata_only": True,
    "candidate": candidate,
    "exact_input_records": sorted(inputs.values(), key=lambda row: row["path"]),
    "unique_input_paths_verified": len(inputs),
    "strict_eight_artifact_submission_verified": True,
    "strict_accepted_suffix_verified": True,
    "earlier_own_paths_verified_unchanged": len(earlier_checks),
    "earlier_own_records": sorted(earlier_checks, key=lambda row: row["path"]),
    "new_math_computation_enumeration_CAS": False,
    "only_new_assigned_prefix_written": True,
    "old_candidate_review_source_shared_or_git_edits": False,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "candidate": candidate,
    "status": "candidate proof - unverified; COMPLETE new global construction checkpoint",
    "new_global_review_obligations": 40,
    "other_initially_blind_whole_audits_required": 2,
    "accepted_local_bodies_verified": len(accepted_bodies),
    "unique_input_paths_verified": len(inputs),
    "prior_own_paths_unchanged": len(earlier_checks),
    "strict_exact_local_acceptance_verified": True,
    "CKP_or_external_entropy_used": False,
    "mathematical_computation_enumeration_CAS": False,
    "constructor_or_coordinator_promotion": False,
    "numerical_official_value_or_full_annual_answer_claimed": False,
    "git_shared_edits_spawning_paid_api": False,
})
record_paths = [
    PREFIX + "candidate-v1.md", PREFIX + "researchlog-v1.md",
    PREFIX + "sources-v1.md", PREFIX + "obligations-v1.json",
    PREFIX + "freeze-v1.py", sources_path, validation_path, output_path,
]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; COMPLETE all-fixed-D global induction ready for TWO OTHER whole audits",
    "constructor": "/root/review_2022_complexity_r2",
    "co_constructor_strategy": "/root",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate": candidate,
    "claims": [
        "UR_D for every fixed integer D>=2 and fixed C>0 on exact GE class",
        "balanced full H_D existence at all integer sizes for every fixed D",
        "official scalar liminf equals limsup and ell_D tends to common value",
    ],
    "common_numerical_value_or_full_annual_answer_claimed": False,
    "novelty_or_priority_claimed": False,
    "all_named_local_premises_accepted_exact_scope": True,
    "new_global_result_independently_reviewed": False,
    "other_initially_blind_whole_nonconstructor_audits_required": 2,
    "constructor_and_root_inspection_count_as_independent_review": False,
    "whole_global_inference_obligations": 40,
    "UR2_unique_grid_base_no_CKP": True,
    "SP_exact_GE_lower_class_EVERY_integer_M_one_reference": True,
    "full_belt_domain_profile_Vitali_codes_and_physical_area_budgets_proved": True,
    "JOINT_conditioning_before_ONE_reference": True,
    "whole_original_source_recovery_and_exact_fine_pullbacks": True,
    "fixed_original_j_before_M_and_all_integer_RP": True,
    "D_grows_only_after_each_fixed_D_limit": True,
    "mathematical_computation_enumeration_CAS": False,
    "git_shared_edits_spawning_paid_api": False,
    "accepted_logical_bodies_verified": len(accepted_bodies),
    "unique_input_paths_verified": len(inputs),
    "earlier_own_paths_verified_unchanged": len(earlier_checks),
    "latest_authoritative_weekly_usage": {
        "used_percent": 31, "at_utc": "2026-10-17 10:48:51 UTC",
        "window_minutes": 10080, "reset_unix": 1792745187,
        "total_used_ceiling_percent": 90, "integration_reserve": True,
    },
    "command": "python3 problems/2017-B4/notes/allD-global-reasoning-r1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
for row in read_json(manifest_path)["records"]:
    check(row)
print(json.dumps({
    "frozen_at_utc": now,
    "candidate": candidate,
    "manifest": fingerprint(manifest_path),
    "records": len(record_paths),
    "new_inference_obligations": 40,
    "accepted_local_bodies": len(accepted_bodies),
    "unique_input_paths": len(inputs),
    "earlier_own_paths_verified_unchanged": len(earlier_checks),
}, indent=2))
