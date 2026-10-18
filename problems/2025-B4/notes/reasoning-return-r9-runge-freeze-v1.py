"""Administrative integrity only; no mathematical computation or RR run."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2025-B4/notes/reasoning-return-r9-runge-"
PARENT = {
    "path": "problems/2025-B4/notes/reasoning-return-r9-freeze-v1.json",
    "bytes": 2790,
    "sha256": "93eed518f1584c8e4f1a7cbe4d6229c9532caae4269d18cf0393c1f0e934aa8f",
}
INPUTS = [
    {"path": "problems/2025-B4/proofs/reviewed-reasoning-return-r8-v1.1.md", "bytes": 28730,
     "sha256": "f00a2b2816f128df54060fd800cba83d726abf07303c1cc7c92688a61557ca15"},
    {"path": "problems/2025-B4/proofs/reviewed-reasoning-return-r6-v1.1.md", "bytes": 28748,
     "sha256": "4e157819789da12d6f26e89929d88ec886d52947405d836fe3957ab8ee727d3a"},
]


def fp(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(record):
    assert fp(record["path"]) == record, ("mismatch", record["path"])
    return record


def save(suffix, value):
    target = ROOT / (P + suffix)
    assert not target.exists(), "preserve immutable output; do not rerun"
    target.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def main():
    for suffix in ("baseline-v1.json", "metadata-v1.json", "input-validation-v1.json", "freeze-v1.json"):
        assert not (ROOT / (P + suffix)).exists(), "already frozen"
    verify(PARENT)
    parent = json.loads((ROOT / PARENT["path"]).read_text())
    assert parent["own_paths_after_this_packet"] == 496
    assert len(parent["artifacts"]) == 10
    declared = [PARENT, *parent["artifacts"], *INPUTS]
    unique = {}
    for record in declared:
        verify(record)
        old = unique.setdefault(record["path"], record)
        assert old == record
    save("baseline-v1.json", {
        "immutable_own_parent": PARENT,
        "historical_own_paths_bound": 496,
        "direct_parent_artifacts_verified": 10,
        "declared_occurrences_verified": len(declared),
        "deduplicated_paths_verified": len(unique),
        "records": list(unique.values()),
        "unverified_R9_parent_is_preservation_binding_NOT_mathematical_premise": True,
        "no_recursive_inventory_copy_or_unrelated_fresh_mathematical_reread": True,
    })
    save("metadata-v1.json", {
        "status": "candidate proof - unverified",
        "constructor": "/root/review_2017_coarsening_r1",
        "requested_model": "gpt-6.1-sol",
        "requested_reasoning": "max",
        "verified_effective_readback": "unavailable",
        "claims": ["RG1", "RG2", "RG3"],
        "whole_obligations": 34,
        "two_OTHER_initially_blind_WHOLE_audits_required": True,
        "NEW_source_method_attributed_to_classical_Runge_covering_literature": True,
        "actual_signed_diagonal_K_point_and_untwisted_normalization_required": True,
        "finite_basis_integral_family_coefficient_formula_fully_exposed": True,
        "numerical_RR_basis_or_M_or_B_computed": False,
        "new_method_fixed_p_finiteness_numeric_improvement_Diophantine_exclusion_or_annual_claim": False,
        "mathematical_code_CAS_scan_native_child": False,
        "older_C_roles_disclosed_no_self_recertification": True,
        "earlier_unverified_R9_claims_are_a_premise": False,
        "parent_R9_range_issue_received_but_no_v1_byte_changed": True,
        "budget": {"human_new_window_authorized": True, "latest_own_direct_TOTAL_percent": 2,
                   "reset": 1792874445, "stop_TOTAL_percent_with_reserve": 90},
    })
    save("input-validation-v1.json", {
        "all_declared_fingerprints_match": True,
        "declared_occurrences_verified": len(declared),
        "deduplicated_paths_verified": len(unique),
        "immutable_parent_and_all_10_direct_artifacts_preserved": True,
        "only_assigned_new_suffix_files_written": True,
        "administrative_hashing_only": True,
    })
    suffixes = ["candidate-v1.md", "obligations-v1.md", "sources-v1.md",
                "failures-worklog-v1.md", "freeze-v1.py", "baseline-v1.json",
                "metadata-v1.json", "input-validation-v1.json"]
    save("freeze-v1.json", {
        "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "COMPLETE distinct Runge-cover constructor checkpoint - candidate proof unverified",
        "constructor": "/root/review_2017_coarsening_r1",
        "whole_obligations": 34,
        "all_RG1_RG2_RG3_source_hypotheses_effectivity_limits_and_failures_recorded": True,
        "two_OTHER_initially_blind_WHOLE_audits_required": True,
        "immutable_own_parent": PARENT,
        "historical_own_paths_bound": 496,
        "own_paths_after_this_packet": 505,
        "declared_occurrences_verified": len(declared),
        "deduplicated_paths_verified": len(unique),
        "artifacts": [fp(P + suffix) for suffix in suffixes],
    })
    print(json.dumps({"main": fp(P + "candidate-v1.md"),
                      "manifest": fp(P + "freeze-v1.json"),
                      "artifacts": len(suffixes), "obligations": 34,
                      "all_match": True}, indent=2))


if __name__ == "__main__":
    main()
