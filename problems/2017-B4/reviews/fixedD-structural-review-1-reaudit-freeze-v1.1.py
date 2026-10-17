"""One-time metadata freeze for targeted FD2-01 repair audit; no mathematics."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/fixedD-structural-review-1-reaudit-"


def fingerprint(relative):
    data = (ROOT / relative).read_bytes()
    return {"path": relative, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = fingerprint(expected["path"])
    actual["matches"] = all(actual[key] == expected[key] for key in ("bytes", "sha256"))
    assert actual["matches"], expected["path"]
    return actual


def create_json(relative, data):
    if not relative.startswith(PREFIX):
        raise RuntimeError("Write outside assigned re-audit prefix")
    with (ROOT / relative).open("x", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


constructor_path = "problems/2017-B4/notes/fixedD-reasoning-r1-freeze-v1.1.json"
constructor = json.loads((ROOT / constructor_path).read_text())
checks = {key: [verify(expected) for expected in constructor[key]] for key in (
    "artifacts", "v1_and_annulus_hashes_preserved", "review_report_and_issue_hashes_preserved",
)}
expected_hashes = [
    "06c6b5eb0f793be00c4dfa1784eb8987cdd415eb1247d708cc827727cd9b5e87",
    "212ad70f53b166bb23cb82ffae72dc38437d7a3f6cec54a7752b2d90a0f7791c",
    "cca69e6dbe4bc199c446142721b1e3f004fba1520ca9396028523bb0bab6fbb3",
]
assert [entry["sha256"] for entry in checks["artifacts"][:3]] == expected_hashes

older_paths = [
    "problems/2021-B4/reviews/reasoning-J15-review-2-manifest.json",
    "problems/2024-B4/notes/structural-reasoning-r2-manifest-v1.json",
    "problems/2017-B4/reviews/fixedD-structural-review-1-manifest-v1.json",
    "problems/2024-B4/notes/divisor-reasoning-r2-manifest-v1.json",
    "problems/2017-B4/reviews/directed-geodesics-review-2-manifest-v1.json",
    "problems/2017-B4/reviews/annulus-review-1-manifest-v1.json",
]
older_checks = []
for path in older_paths:
    manifest = json.loads((ROOT / path).read_text())
    older_checks.append({
        "manifest": fingerprint(path),
        "all_records_match": True,
        "checks": [verify(expected) for expected in manifest["records"]],
    })
assert older_checks[-1]["manifest"]["sha256"] == "ec84d96e034b1ec6e8c550b402c28c97960f636e3ccde321b82c2fcbfe076b87"

now = datetime.now(timezone.utc).isoformat()
validation_path = PREFIX + "input-validation-v1.1.json"
create_json(validation_path, {
    "checked_at_utc": now,
    "constructor_manifest": fingerprint(constructor_path),
    "all_constructor_and_preserved_entries_match": True,
    "checks": checks,
    "local_protocol": fingerprint("AGENTS.md"),
    "older_own_packets": older_checks,
    "all_older_own_records_unchanged": True,
    "peer_targeted_reaudit_contents_read": False,
    "metadata_only": True,
})
output_path = PREFIX + "freeze-output-v1.1.json"
create_json(output_path, {
    "frozen_at_utc": now,
    "targeted_FD2_01_audit_complete": True,
    "recommend_resolution_for_v1_1": True,
    "new_substantive_objections": 0,
    "original_reviewer1_miss_acknowledged": True,
    "original_review_bytes_preserved": True,
    "no_peer_targeted_reaudit_findings_read": True,
    "H_EAI_PR_or_full_solution_promoted": False,
    "mathematical_computation_or_CAS": False,
})
record_paths = [PREFIX + suffix for suffix in (
    "report-v1.1.md", "issues-v1.1.json", "sources-v1.1.json",
    "freeze-v1.1.py", "input-validation-v1.1.json", "freeze-output-v1.1.json",
)]
manifest_path = PREFIX + "manifest-v1.1.json"
create_json(manifest_path, {
    "status": "targeted FD2-01 repair audit complete; recommend coordinator resolution for v1.1; no promotion",
    "frozen_at_utc": now,
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "nonconstructor": True,
    "reviewed_v1_1_hashes": expected_hashes,
    "peer_original_report_read_after_both_initial_freezes": True,
    "no_peer_targeted_reaudit_findings_read": True,
    "new_substantive_objections": 0,
    "recommend_resolution_for_v1_1": True,
    "original_reviewer1_miss_acknowledged": True,
    "all_older_records_unchanged": True,
    "no_H_EAI_PR_or_full_solution_acceptance": True,
    "mathematical_enumeration_or_CAS": False,
    "latest_weekly_total_used_percent": 20,
    "weekly_reset_unix": 1792745187,
    "command": ".venv/bin/python " + PREFIX + "freeze-v1.1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({
    "frozen_at_utc": now,
    "report": fingerprint(PREFIX + "report-v1.1.md"),
    "manifest": fingerprint(manifest_path),
    "new_substantive_objections": 0,
    "recommend_resolution_for_v1_1": True,
    "all_older_records_unchanged": True,
}, indent=2))
