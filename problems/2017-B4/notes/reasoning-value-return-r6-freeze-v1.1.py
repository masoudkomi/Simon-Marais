"""Administrative full-version repair freeze; no mathematical program."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2017-B4/notes/reasoning-value-return-r6-"
PARENT = {
    "path": "problems/2025-B4/notes/reasoning-return-r9-runge-freeze-v1.json",
    "bytes": 2364,
    "sha256": "cb5073bbce53c07b12e5b253af51f278ebd6475c0600d700bef6a9064a7ec32b",
}
ORIGINAL = {
    "path": P + "freeze-v1.json", "bytes": 3298,
    "sha256": "aba8108ec5191eb5c6d2702944d74c340c06ff949938bbe0bcd197b34998e9d4",
}
ACCEPTED = [
    {"path": "problems/2017-B4/proofs/reviewed-direction-coarsening-v1.1.md", "bytes": 9175,
     "sha256": "98c04673acdb4c59d44eb4d977f844d3f01ef27365399982e02df8cbaa4a6241"},
    {"path": "problems/2017-B4/proofs/reviewed-allD-uniform-strict-v1.1.md", "bytes": 39136,
     "sha256": "a5ebfd81d59b26f301b1e105889451f4c86262da80e6e77e6913c045d71147d2"},
]


def fp(path):
    b = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(b), "sha256": hashlib.sha256(b).hexdigest()}


def verify(record):
    assert fp(record["path"]) == {k: record[k] for k in ("path", "bytes", "sha256")}, record["path"]


def save(suffix, value):
    target = ROOT / (P + suffix)
    assert not target.exists(), "preserve immutable output; do not rerun"
    target.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def main():
    output_suffixes = ["diff-v1-to-v1.1.patch", "baseline-v1.1.json", "metadata-v1.1.json",
                       "input-validation-v1.1.json", "freeze-v1.1.json"]
    for suffix in output_suffixes:
        assert not (ROOT / (P + suffix)).exists(), "already frozen"
    verify(PARENT)
    verify(ORIGINAL)
    parent = json.loads((ROOT / PARENT["path"]).read_text())
    original = json.loads((ROOT / ORIGINAL["path"]).read_text())
    assert parent["own_paths_after_this_packet"] == 505
    assert len(parent["artifacts"]) == 8
    assert len(original["artifacts"]) == 9
    review_paths = [
        "problems/2017-B4/reviews/reasoning-value-return-r6-review-1-manifest-v1.json",
        "problems/2017-B4/reviews/reasoning-value-return-r6-review-2-manifest-v1.json",
    ]
    review_manifests = []
    declared = [PARENT, *parent["artifacts"], ORIGINAL, *original["artifacts"], *ACCEPTED]
    for path in review_paths:
        record = fp(path)
        review = json.loads((ROOT / path).read_text())
        review_manifests.append(record)
        declared.extend([record, *review["artifacts"]])
    unique = {}
    for item in declared:
        verify(item)
        core = {key: item[key] for key in ("path", "bytes", "sha256")}
        prior = unique.setdefault(core["path"], core)
        assert prior == core
    original_main = (ROOT / (P + "candidate-v1.md")).read_text()
    new_main = (ROOT / (P + "candidate-v1.1.md")).read_text()
    assert original_main[original_main.index("## 1."):original_main.index("## 4.")] == new_main[new_main.index("## 1."):new_main.index("## 4.")]
    assert original_main[original_main.index("## 6."):] == new_main[new_main.index("## 6."):]
    diff = []
    for stem in ("candidate", "obligations", "sources", "failures", "worklog"):
        old_path = P + stem + "-v1.md"
        new_path = P + stem + "-v1.1.md"
        diff.extend(difflib.unified_diff((ROOT / old_path).read_text().splitlines(keepends=True),
                                         (ROOT / new_path).read_text().splitlines(keepends=True),
                                         fromfile=old_path, tofile=new_path))
    (ROOT / (P + "diff-v1-to-v1.1.patch")).write_text("".join(diff))
    save("baseline-v1.1.json", {
        "immutable_own_parent": PARENT,
        "historical_own_paths_bound": 505,
        "original_constructor_manifest": ORIGINAL,
        "both_original_whole_initial_manifests": review_manifests,
        "declared_occurrences_verified": len(declared),
        "deduplicated_paths_verified": len(unique),
        "records": list(unique.values()),
        "no_growing_historical_inventory_recopied_or_claimed_freshly_reread": True,
    })
    save("metadata-v1.1.json", {
        "status": "candidate proof - unverified, COMPLETE full author repair",
        "constructor": "/root/review_2017_coarsening_r1",
        "requested_model": "gpt-6.1-sol", "requested_reasoning": "max",
        "effective_setting_readback": "unavailable",
        "issue_addressed": "PMR2-01",
        "other_original_source_observation_preserved": "A N1 closed finite-proof qualification",
        "affected_claims": ["PM2", "PM3"],
        "original_whole_obligations": 48,
        "additional_affected_interface_checks": 12,
        "full_obligations": 60,
        "literal_finite_angle_source_domain_restored_by_only_finite_T_perturbation": True,
        "arbitrary_infinite_angle_extension_asserted": False,
        "published_embedded_corner_legality_attributed_with_actual_hypotheses": True,
        "both_OTHER_affected_reaudits_required": True,
        "root_C_contributors_excluded": True,
        "PM1_sections1_to3_and_PM4_section6_to_end_text_unchanged": True,
        "all_original_v1_and_both_whole_initial_bytes_preserved": True,
        "no_upper_R_value_annual_or_novelty_claim": True,
        "no_mathematical_code_scan_CAS_source_download_native_child": True,
        "budget": {"latest_direct_TOTAL_percent": 4, "at_utc": "2026-10-18 00:44:58 UTC",
                   "reset": 1792874445, "human_new_window_authorization": True,
                   "ordinary_usage_allowed": True, "stop_TOTAL_percent_with_reserve": 90},
    })
    save("input-validation-v1.1.json", {
        "all_necessary_declared_fingerprints_match": True,
        "declared_occurrences_verified": len(declared),
        "deduplicated_paths_verified": len(unique),
        "original_all_9_direct_artifacts_verified": True,
        "both_original_initial_artifact_sets_verified": True,
        "own_parent_all_8_artifacts_verified": True,
        "unchanged_PM1_PM4_text_checks_passed": True,
        "old_shared_Git_cache_file_written": False,
        "administrative_hash_diff_JSON_only": True,
    })
    suffixes = ["candidate-v1.1.md", "obligations-v1.1.md", "sources-v1.1.md",
                "failures-v1.1.md", "worklog-v1.1.md", "repair-ledger-v1.1.md",
                "diff-v1-to-v1.1.patch", "freeze-v1.1.py", "baseline-v1.1.json",
                "metadata-v1.1.json", "input-validation-v1.1.json"]
    save("freeze-v1.1.json", {
        "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "COMPLETE FULL version1.1 author repair - candidate proof unverified",
        "issue": "PMR2-01", "affected_claims": ["PM2", "PM3"],
        "full_obligations": 60,
        "all_original_v1_and_both_whole_initials_preserved": True,
        "both_OTHER_affected_reaudits_required_before_coordinator_promotion": True,
        "immutable_own_parent": PARENT,
        "historical_own_paths_bound": 505,
        "own_paths_after_this_packet": 517,
        "declared_occurrences_verified": len(declared),
        "deduplicated_paths_verified": len(unique),
        "artifacts": [fp(P + suffix) for suffix in suffixes],
    })
    print(json.dumps({"main": fp(P + "candidate-v1.1.md"),
                      "manifest": fp(P + "freeze-v1.1.json"),
                      "artifacts": len(suffixes), "obligations": 60,
                      "declared_occurrences": len(declared),
                      "declared_unique_paths": len(unique), "all_match": True}, indent=2))


if __name__ == "__main__":
    main()
