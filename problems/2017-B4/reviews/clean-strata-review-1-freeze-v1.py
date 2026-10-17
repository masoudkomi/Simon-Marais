"""One-time metadata freeze of blind whole FL1/CL1/OB1 audit; no mathematics."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/clean-strata-review-1-"

def fingerprint(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}

def verify(expected):
    actual = fingerprint(expected["path"])
    assert all(actual[key] == expected[key] for key in ("bytes", "sha256")), expected["path"]
    return dict(actual, matches=True)

def create_json(path, data):
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")

constructor_path = "problems/2017-B4/notes/coordinator-stratum-clean-lens-freeze-v1.json"
constructor = json.loads((ROOT / constructor_path).read_text())
input_checks = [verify(entry) for entry in constructor["artifacts"]]
assert input_checks[0]["sha256"] == "aa4c79b1fb3136ecd3e7c5ab845733697cca925ba8203b2988fba5c9a793bd95"
accepted = []
for path, expected_hash in (
    ("problems/2017-B4/proofs/reviewed-fixedD-structural-v1.2.md", "421dc271ed65831e3aa70057a0d74c4d999ba8249dfa2b99066dfdc298f86868"),
    ("problems/2017-B4/proofs/reviewed-direction-coarsening-v1.1.md", "98c04673acdb4c59d44eb4d977f844d3f01ef27365399982e02df8cbaa4a6241"),
):
    actual = fingerprint(path)
    assert actual["sha256"] == expected_hash
    accepted.append(actual)
older_paths = [
    "problems/2021-B4/reviews/reasoning-J15-review-2-manifest.json",
    "problems/2024-B4/notes/structural-reasoning-r2-manifest-v1.json",
    "problems/2017-B4/reviews/fixedD-structural-review-1-manifest-v1.json",
    "problems/2024-B4/notes/divisor-reasoning-r2-manifest-v1.json",
    "problems/2017-B4/reviews/directed-geodesics-review-2-manifest-v1.json",
    "problems/2017-B4/reviews/annulus-review-1-manifest-v1.json",
    "problems/2017-B4/reviews/fixedD-structural-review-1-reaudit-manifest-v1.1.json",
    "problems/2017-B4/reviews/lens-cutting-review-1-manifest-v1.json",
    "problems/2017-B4/reviews/annulus-review-1-reaudit-manifest-v1.1.json",
]
older_checks = []
for path in older_paths:
    manifest = json.loads((ROOT / path).read_text())
    older_checks.append({"manifest": fingerprint(path), "checks": [verify(entry) for entry in manifest["records"]]})
assert older_checks[-1]["manifest"]["sha256"] == "45d6f2179ef0159551a6009c01faccd9252fcadb3b1e54c2a2968c7259fee5c3"
now = datetime.now(timezone.utc).isoformat()
validation_path = PREFIX + "input-validation-v1.json"
create_json(validation_path, {
    "checked_at_utc": now,
    "constructor_manifest": fingerprint(constructor_path),
    "input_checks": input_checks,
    "accepted_background": accepted,
    "local_dependencies": [fingerprint(path) for path in (
        "AGENTS.md", "problems/2017-B4/reviews/fixedD-structural-acceptance.json",
        "problems/2017-B4/reviews/coarsening-acceptance.json",
    )],
    "all_candidate_search_artifacts_and_background_match": True,
    "older_own_packets": older_checks,
    "all_older_own_records_unchanged": True,
    "peer_clean_strata_findings_read": False,
    "metadata_only": True,
})
output_path = PREFIX + "freeze-output-v1.json"
create_json(output_path, {
    "frozen_at_utc": now,
    "blind_whole_FL1_CL1_OB1_audit_complete": True,
    "substantive_objections": 0, "repair_requested": False,
    "no_peer_clean_strata_findings_read": True,
    "mathematical_program_run_enumeration_or_CAS": False,
    "candidate_and_all_older_own_records_unchanged": True,
    "H_EAI_PR_stratum_repair_or_full_solution_accepted": False,
})
records = [PREFIX + suffix for suffix in (
    "initial-v1.md", "issues-v1.json", "sources-v1.json", "freeze-v1.py",
    "input-validation-v1.json", "freeze-output-v1.json",
)]
manifest_path = PREFIX + "manifest-v1.json"
create_json(manifest_path, {
    "status": "initial blind whole FL1/CL1/OB1 audit complete; no substantive objection; no reviewer promotion",
    "frozen_at_utc": now, "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": input_checks[0]["sha256"],
    "nonconstructor": True, "whole_reconstruction": True,
    "no_peer_clean_strata_findings_read_before_freeze": True,
    "substantive_objections": 0, "repair_requested": False,
    "nonblocking_parameter_note": "Retain O(l^2 L) finite-scale boundary term in the final bad-cell leading order",
    "candidate_and_all_older_own_records_unchanged": True,
    "no_mathematical_program_rerun_enumeration_or_CAS": True,
    "no_H_EAI_PR_stratum_repair_or_full_solution_acceptance": True,
    "latest_weekly_total_used_percent": 21, "weekly_reset_unix": 1792745187,
    "command": ".venv/bin/python " + PREFIX + "freeze-v1.py",
    "records": [fingerprint(path) for path in records],
})
print(json.dumps({"frozen_at_utc": now,
    "report": fingerprint(PREFIX + "initial-v1.md"), "manifest": fingerprint(manifest_path),
    "substantive_objections": 0, "all_older_records_unchanged": True}, indent=2))
