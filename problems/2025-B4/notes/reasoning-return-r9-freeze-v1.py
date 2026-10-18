"""Administrative freeze only: no mathematical program or constructor rerun."""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2025-B4/notes/reasoning-return-r9-"
PARENT = {
    "path": "problems/2024-B4/reviews/coordinator-three-bit-sector-r2-review-2-manifest-v1.json",
    "bytes": 3637,
    "sha256": "df5e3b97dab03c7d3aa547d0e2a42534c5ce524662f28230476f3cd99f12065e",
}
R8 = {
    "path": "problems/2025-B4/proofs/reviewed-reasoning-return-r8-v1.1.md",
    "bytes": 28730,
    "sha256": "f00a2b2816f128df54060fd800cba83d726abf07303c1cc7c92688a61557ca15",
}
R6 = {
    "path": "problems/2025-B4/proofs/reviewed-reasoning-return-r6-v1.1.md",
    "bytes": 28748,
    "sha256": "4e157819789da12d6f26e89929d88ec886d52947405d836fe3957ab8ee727d3a",
}


def fp(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(record):
    actual = fp(record["path"])
    assert actual == {key: record[key] for key in ("path", "bytes", "sha256")}, (
        "fingerprint mismatch", record, actual
    )
    return actual


def records(value):
    if isinstance(value, dict):
        if all(key in value for key in ("path", "bytes", "sha256")):
            yield {key: value[key] for key in ("path", "bytes", "sha256")}
        for child in value.values():
            yield from records(child)
    elif isinstance(value, list):
        for child in value:
            yield from records(child)


def save(suffix, value):
    path = ROOT / (PREFIX + suffix)
    assert not path.exists(), ("preserve immutable output", str(path))
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def main():
    for suffix in ("baseline-v1.json", "input-validation-v1.json", "metadata-v1.json", "freeze-v1.json"):
        assert not (ROOT / (PREFIX + suffix)).exists(), "already frozen; do not rerun"
    verify(PARENT)
    parent = json.loads((ROOT / PARENT["path"]).read_text())
    assert parent["own_paths_after_this_packet"] == 485
    assert len(parent["artifacts"]) == 9
    acceptance_path = "problems/2025-B4/reviews/reasoning-return-r8-acceptance.json"
    acceptance = json.loads((ROOT / acceptance_path).read_text())
    assert acceptance["status"] == "proved, independently reviewed scoped partial result"
    required = [PARENT, *parent["artifacts"], R8, R6, *records(acceptance)]
    unique = {}
    for item in required:
        verified = verify(item)
        previous = unique.setdefault(verified["path"], verified)
        assert previous == verified
    current_read_paths = [
        "AGENTS.md", "problems/2025-B4/statement.md", acceptance_path,
        "problems/2025-B4/notes/deep-literature-r1-report-v1.md",
        "problems/2025-B4/notes/reasoning-return-r8-worklog-v1.md",
        "problems/2025-B4/notes/reasoning-return-r7-failed-routes-v1.md",
    ]
    baseline = {
        "immutable_own_parent": PARENT,
        "parent_direct_artifacts_verified": len(parent["artifacts"]),
        "historical_own_paths_bound_by_parent": 485,
        "declared_occurrences_verified": len(required),
        "deduplicated_declared_paths_verified": len(unique),
        "declared_records": list(unique.values()),
        "other_actual_read_inputs": [fp(path) for path in current_read_paths],
        "scope": "compact parent binding, no claim of fresh recursive reread or rehash of the entire historical inventory",
    }
    save("baseline-v1.json", baseline)
    save("input-validation-v1.json", {
        "all_necessary_declared_fingerprints_match": True,
        "declared_occurrences_verified": len(required),
        "deduplicated_declared_paths_verified": len(unique),
        "parent_direct_artifacts_verified": 9,
        "historical_own_paths_bound": 485,
        "no_old_file_written": True,
        "mathematical_program_scan_CAS_author_rerun": False,
        "administrative_script_only": True,
    })
    save("metadata-v1.json", {
        "constructor": "/root/review_2017_coarsening_r1",
        "requested_model": "gpt-6.1-sol",
        "requested_reasoning": "max",
        "effective_readback": "unavailable",
        "status": "candidate proof - unverified",
        "official_scope": "2025 B4(b), signed prime diagonal p>=37 and |X|>=2; R9A/B additionally q_p>=32",
        "claims": ["R9A", "R9B", "R9C", "R9D", "R9E", "R9F"],
        "whole_obligations": 48,
        "two_OTHER_initially_blind_WHOLE_audits_required": True,
        "root_generic_prompt_supplied_new_proof_inference": False,
        "OLD_C_R6_FS_authorship_and_other_review_roles_disclosed": True,
        "ordinary_solution_or_Diophantine_exclusion_or_annual_claim": False,
        "published_theorem_refuted_by_conditional_or_model_data": False,
        "both_arithmetic_branches_retained_with_dense_support": True,
        "finite2_weight6_NOT_original_weight": True,
        "source_v1_and_CURRENT_v4_distinguished": True,
        "mathematical_code_or_native_child": False,
        "paid_API_contact_bypass": False,
        "budget": {
            "explicit_human_new_window_authorization_relayed_by_root": True,
            "reset": 1792874445,
            "latest_direct_TOTAL_used_percent": 2,
            "ordinary_usage_allowed": True,
            "stop_TOTAL_percent_with_reserve": 90,
        },
        "immutable_parent": PARENT,
    })
    suffixes = [
        "live-log-v1.md", "candidate-v1.md", "obligations-v1.md", "failed-routes-v1.md",
        "sources-v1.md", "worklog-v1.md", "freeze-v1.py", "baseline-v1.json",
        "input-validation-v1.json", "metadata-v1.json",
    ]
    artifacts = [fp(PREFIX + suffix) for suffix in suffixes]
    assert len(artifacts) == 10
    save("freeze-v1.json", {
        "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "COMPLETE coherent constructor checkpoint - candidate proof unverified",
        "constructor": "/root/review_2017_coarsening_r1",
        "whole_obligations": 48,
        "full_proofs_sources_readlimits_failures_both_branches_recorded": True,
        "two_OTHER_initially_blind_WHOLE_audits_required": True,
        "no_Diophantine_exclusion_annual_or_source_final_theorem_refutation_claim": True,
        "immutable_own_parent": PARENT,
        "historical_own_paths_bound": 485,
        "own_paths_after_this_packet": 496,
        "declared_occurrences_verified": len(required),
        "deduplicated_declared_paths_verified": len(unique),
        "artifacts": artifacts,
    })
    print(json.dumps({
        "manifest": fp(PREFIX + "freeze-v1.json"),
        "main": fp(PREFIX + "candidate-v1.md"),
        "artifacts": len(artifacts),
        "obligations": 48,
        "declared_occurrences": len(required),
        "declared_unique_paths": len(unique),
        "all_match": True,
    }, indent=2))


if __name__ == "__main__":
    main()
