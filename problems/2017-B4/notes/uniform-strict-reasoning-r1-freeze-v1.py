"""One-time construction checkpoint; metadata only, no mathematical calculation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/notes/uniform-strict-reasoning-r1-"


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
dependency_rows = [
    {"path": "problems/2017-B4/proofs/reviewed-annulus-v1.2.md",
     "sha256": "51c02b22a36705c736e4debefcfde0afbc1b2678a8d6092213d8ed00e6a75baf"},
    {"path": "problems/2017-B4/proofs/reviewed-lens-cutting-v1.1.md",
     "sha256": "81f175e2a0f10665e9228d18885180e91b4db6167001584182d9de4b9cb437fc"},
    {"path": "problems/2017-B4/proofs/reviewed-strict-transfer-v1.1.md",
     "sha256": "89f2bc8068a4f151621ed4cdcdfb0e6dc891d51d43452b5f176d41fa62a840eb"},
    {"path": "problems/2017-B4/proofs/reviewed-directed-geodesics-v1.1.md",
     "sha256": "061ae1749e938aad68f1824ab5f33583a3a1c58e556bd62649309c7cb12da9aa"},
    {"path": "problems/2017-B4/notes/coordinator-dimension-induction-program-v1.md",
     "sha256": "b499899787f8d8607ba030ec21173451267ea0b1dd6d419481a548a103c2f291"},
]
dependency_checks = [check(row) for row in dependency_rows]
prior_path = "problems/2021-B4/reviews/odd-support-exclusion-review-1-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "37c051970aebcdac696a5fcb71f1a8ad5327cc8bf6cad42663f1dc2ac2ec7e56"})
prior = read_json(prior_path)
prior_checks = [check(row) for row in prior["records"]]
prior_validation = read_json("problems/2021-B4/reviews/odd-support-exclusion-review-1-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 23
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "accepted_dependencies_and_unproved_inspiration": dependency_checks,
    "program_is_a_theorem_premise": False,
    "rank_mesh_is_a_theorem_premise": False,
    "additional_inputs": [fingerprint(path) for path in [
        "AGENTS.md", "problems/2017-B4/statement.md",
    ]],
    "older_own_packets": older,
    "all_twenty_four_older_own_packets_unchanged": True,
    "mathematical_program_enumeration_or_CAS": False,
    "new_source_download": False,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; complete scoped D4 construction checkpoint",
    "dependency_records_checked": 5,
    "older_own_packets_checked": 24,
    "all_fingerprints_match": True,
    "new_claims": ["US1 uniform digital frame constants", "US2 physical transfer", "US3 real strict finite-net local recovery"],
    "full_H_PR_fixedD_or_official_limit_claim": False,
    "all_D_extension_claim": False,
    "two_other_fresh_nonconstructor_whole_audits_required": True,
    "shared_mutation_or_Git": False,
})
record_paths = [PREFIX + name for name in [
    "candidate-v1.md", "researchlog-v1.md", "sources-v1.md", "freeze-v1.py",
]] + [validation_path, output_path]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified",
    "constructor": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "claims": ["US1", "US2", "US3"],
    "whole_fresh_nonconstructor_audits_required": 2,
    "D": 4,
    "strict_compact_domain_only": True,
    "physical_period_q_only_changes_scale_threshold": True,
    "parameter_order": ["target_loss", "uniform_epsilon", "finite_rational_net", "periods_and_phases", "maximum_finite_scale_threshold"],
    "no_global_H_PR_or_official_limit": True,
    "rank_mesh_dependency": False,
    "mathematical_program_enumeration_or_CAS": False,
    "shared_changes_or_Git": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 26,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2017-B4/notes/uniform-strict-reasoning-r1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "candidate": fingerprint(PREFIX + "candidate-v1.md"),
                  "records": len(record_paths),
                  "dependency_records_checked": 5,
                  "older_own_packets_checked": 24}, indent=2))
