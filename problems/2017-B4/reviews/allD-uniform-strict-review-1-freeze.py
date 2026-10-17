"""One-time blind whole-audit freeze: byte checks only, no math program."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/allD-uniform-strict-review-1-"
TARGET = "problems/2017-B4/notes/allD-uniform-strict-reasoning-r1-"


def row(path):
    raw = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def check(expected):
    actual = row(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    return actual


def read(path):
    return json.loads((ROOT / path).read_text())


def write(suffix, obj):
    path = PREFIX + suffix
    with (ROOT / path).open("x", encoding="utf-8") as out:
        json.dump(obj, out, indent=2, ensure_ascii=False)
        out.write("\n")
    return row(path)


candidate = check({"path": TARGET + "candidate-v1.md", "bytes": 37267,
                   "sha256": "fc280881b1df650d07ab48f0f4c19d0e77f076e6b39a13f3a0b8d9969074a433"})
target_manifest = check({"path": TARGET + "manifest-v1.json",
                         "sha256": "126fd14f143d6ab619c7aba5d57be968471080d7f07bb081805f6706434b1f18"})
declared = [check(expected) for expected in read(target_manifest["path"])["records"]]
assert len(declared) == 8
source_metadata = read(TARGET + "sources-v1.json")
accepted_inputs = [check(expected) for expected in source_metadata["local_records"]]
acceptances = [check(expected) for expected in source_metadata["acceptance_scopes_read"]]
assert len(accepted_inputs) == 7 and len(acceptances) == 6
protocol = check({"path": "AGENTS.md", "bytes": 4707,
                  "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"})

constructor_occurrences = []
constructor_unique = {}


def verify_rows(obj):
    if isinstance(obj, dict):
        if (isinstance(obj.get("path"), str)
                and isinstance(obj.get("sha256"), str)
                and re.fullmatch("[0-9a-f]{64}", obj["sha256"])):
            actual = check(obj)
            constructor_occurrences.append(actual)
            if actual["path"] in constructor_unique:
                assert constructor_unique[actual["path"]] == actual
            constructor_unique[actual["path"]] = actual
        for value in obj.values():
            verify_rows(value)
    elif isinstance(obj, list):
        for value in obj:
            verify_rows(value)


verify_rows(read(TARGET + "input-validation-v1.json"))

old_path = "problems/2024-B4/notes/reasoning-return-r3-freeze-v1.json"
old_manifest = check({"path": old_path, "bytes": 4596,
                      "sha256": "e2c1b451f486db75597fbd6b99c970f85a7ed70528bebd032e2d7168fbcf7741"})
preserved = {old_path: old_manifest}
for expected in read(old_path)["artifacts"]:
    actual = check(expected)
    preserved[actual["path"]] = actual
for expected in read("problems/2024-B4/notes/reasoning-return-r3-input-validation-v1.json")["earlier_unique_records_preserved"]:
    actual = check(expected)
    if actual["path"] in preserved:
        assert preserved[actual["path"]] == actual
    preserved[actual["path"]] = actual
assert len(preserved) == 181, len(preserved)
official = check(read("problems/2017-B4/reviews/local-rank-mesh-review-1-input-validation.json")["cached_official_pdf"])

validation = write("input-validation.json", {
    "validated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "candidate": candidate,
    "candidate_manifest": target_manifest,
    "all_eight_declared_candidate_records": declared,
    "all_seven_source_named_local_records": accepted_inputs,
    "six_full_acceptance_scope_records": acceptances,
    "protocol": protocol,
    "cached_official_pdf": official,
    "constructor_input_hash_occurrences_checked": len(constructor_occurrences),
    "constructor_input_unique_records_checked": sorted(constructor_unique.values(), key=lambda r: r["path"]),
    "constructor_input_unique_count": len(constructor_unique),
    "earlier_unique_records_preserved": sorted(preserved.values(), key=lambda r: r["path"]),
    "earlier_unique_count": len(preserved),
    "hashing_old_review_files_is_not_reading_conclusions": True,
    "peer_allD_strict_findings_read_before_freeze": False,
    "new_allD_construction_contributed_by_reviewer": False,
    "prior_annulus_fixedD_rankmesh_authorship_disclosed": True,
    "independent_reaudit_of_reviewers_own_old_inputs_claimed": False,
    "mathematical_program_enumeration_CAS_certificate_or_author_rerun": False,
})
artifacts = [row(PREFIX + suffix) for suffix in [
    "initial.md", "issues.md", "source-checks.md", "freeze.py"
]] + [validation]
manifest = write("manifest-initial.json", {
    "frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "initially blind whole independent new-construction audit; no substantive defect found in stated strict local scope; no promotion",
    "reviewer": "review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate": candidate,
    "candidate_manifest": target_manifest,
    "whole_claims_reconstructed": ["AD1", "AD2", "AD3", "AD4", "AD5", "fixed-D CUT interface", "US_D1", "US_D2", "US_D3"],
    "inference_ledger_rows": 40,
    "substantive_issues": [],
    "nonblocking_author_changes_requested": [],
    "dimension": "each fixed D>=3, compact strictly positive ordered-minor tangent set only",
    "all_pairs_global_poset_rank_box_seams_and_common_phase_reconstructed": True,
    "q_independent_event_lobe_geometry_and_code_constants_checked": True,
    "every_m_supremum_upper_bound_same_e_and_fixed_original_lens_M_limit_checked": True,
    "epsilon_first_net_second_periods_third_max_threshold_last_checked": True,
    "prior_own_annulus_background_not_independently_reaudited": True,
    "constructed_new_allD_argument": False,
    "peer_allD_strict_findings_read_before_freeze": False,
    "artifacts": artifacts,
    "declared_candidate_records_verified": len(declared),
    "source_named_local_records_verified": len(accepted_inputs),
    "acceptance_scope_records_verified": len(acceptances),
    "constructor_input_hash_occurrences_checked": len(constructor_occurrences),
    "constructor_input_unique_count": len(constructor_unique),
    "earlier_unique_frozen_own_records_preserved": len(preserved),
    "H_PR_UR_D_global_induction_or_official_limit_claim": False,
    "reviewer_promotion": False,
    "mathematical_program_enumeration_CAS_certificate_or_author_rerun": False,
    "only_assigned_review_prefix_written": True,
    "git_shared_mutation_spawning_contacts_charges_or_bypass": False,
    "direct_weekly_total_used_percent_during_audit": 30,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
})
print(json.dumps({"manifest": manifest, "artifacts": artifacts,
                  "constructor_input_hash_occurrences_checked": len(constructor_occurrences),
                  "constructor_input_unique_count": len(constructor_unique),
                  "earlier_unique_frozen_own_records_preserved": len(preserved)}, indent=2))
