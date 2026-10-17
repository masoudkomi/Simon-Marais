"""One-time metadata freeze for targeted annulus repair audit; no mathematics."""

from datetime import datetime, timezone
import difflib
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/reviews/annulus-review-1-reaudit-"


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
        raise RuntimeError("Write outside assigned annulus re-audit prefix")
    with (ROOT / relative).open("x", encoding="utf-8") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")


constructor_path = "problems/2017-B4/notes/annulus-reasoning-r1-freeze-v1.1.json"
assert fingerprint(constructor_path)["sha256"] == "43ec9d1ce2e2f160658ed356cdf70a3429aa672bf28bf9af5832a9a813ccb4f9"
constructor = json.loads((ROOT / constructor_path).read_text())
input_checks = [verify(expected) for expected in constructor["artifacts"]]
assert input_checks[0]["sha256"] == "c6da61f229ffa72dd830cd40132969717a395e3744b6d775cbe83a32bdd3747c"
assert input_checks[1]["sha256"] == "a0805df0cdc05f30ab8256fe9cf64ba466f932abc3cd97b45d68f1d98cae51b0"

v1 = ROOT / "problems/2017-B4/notes/annulus-reasoning-r1-candidate-v1.md"
v11 = ROOT / "problems/2017-B4/notes/annulus-reasoning-r1-candidate-v1.1.md"
diff_text = "".join(difflib.unified_diff(
    v1.read_text().splitlines(keepends=True),
    v11.read_text().splitlines(keepends=True),
    fromfile=v1.name, tofile=v11.name,
))
saved_diff = ROOT / "problems/2017-B4/notes/annulus-reasoning-r1-diff-v1.1.patch"
assert diff_text.encode("utf-8") == saved_diff.read_bytes()

original_path = "problems/2017-B4/notes/annulus-reasoning-r1-freeze-v1.json"
original = json.loads((ROOT / original_path).read_text())
original_checks = [verify(expected) for expected in original["artifacts"]]
peer_original_path = "problems/2017-B4/reviews/annulus-review-2-freeze-manifest.json"
peer_original = json.loads((ROOT / peer_original_path).read_text())
peer_checks = [verify(expected) for expected in peer_original["inputs"] + peer_original["artifacts"]]
source_path = "problems/2017-B4/notes/annulus-reasoning-r1-sources-v1.1.json"
source = json.loads((ROOT / source_path).read_text())
author_review_input_checks = [verify(expected) for expected in source["review_inputs"]]

older_paths = [
    "problems/2021-B4/reviews/reasoning-J15-review-2-manifest.json",
    "problems/2024-B4/notes/structural-reasoning-r2-manifest-v1.json",
    "problems/2017-B4/reviews/fixedD-structural-review-1-manifest-v1.json",
    "problems/2024-B4/notes/divisor-reasoning-r2-manifest-v1.json",
    "problems/2017-B4/reviews/directed-geodesics-review-2-manifest-v1.json",
    "problems/2017-B4/reviews/annulus-review-1-manifest-v1.json",
    "problems/2017-B4/reviews/fixedD-structural-review-1-reaudit-manifest-v1.1.json",
    "problems/2017-B4/reviews/lens-cutting-review-1-manifest-v1.json",
]
older_checks = []
for path in older_paths:
    manifest = json.loads((ROOT / path).read_text())
    older_checks.append({
        "manifest": fingerprint(path),
        "all_records_match": True,
        "checks": [verify(expected) for expected in manifest["records"]],
    })
assert older_checks[-1]["manifest"]["sha256"] == "f6c423730d9388ff331a0931cfcd5909e23afb10e65e7a8160bdd929ff8e525b"

now = datetime.now(timezone.utc).isoformat()
validation_path = PREFIX + "input-validation-v1.1.json"
create_json(validation_path, {
    "checked_at_utc": now,
    "constructor_manifest": fingerprint(constructor_path),
    "all_constructor_entries_match": True,
    "input_checks": input_checks,
    "saved_diff_exactly_matches_regenerated_diff": True,
    "original_annulus_manifest": fingerprint(original_path),
    "original_annulus_artifacts": original_checks,
    "peer_original_manifest": fingerprint(peer_original_path),
    "peer_original_inputs_and_artifacts": peer_checks,
    "author_review_input_hashes": author_review_input_checks,
    "all_original_annulus_candidates_and_initial_reviews_unchanged": True,
    "local_protocol": fingerprint("AGENTS.md"),
    "older_own_packets": older_checks,
    "all_older_own_records_unchanged": True,
    "peer_targeted_reaudit_findings_read": False,
    "metadata_only": True,
})
output_path = PREFIX + "freeze-output-v1.1.json"
create_json(output_path, {
    "frozen_at_utc": now,
    "targeted_AR1_01_ANN2_N1_N2_audit_complete": True,
    "recommend_resolution_for_v1_1": True,
    "new_substantive_objections": 0,
    "no_peer_targeted_reaudit_findings_read": True,
    "original_candidate_and_initial_review_bytes_preserved": True,
    "DG_CUT_or_height_only_conversion_used_as_premise": False,
    "H_EAI_PR_full_solution_or_novelty_accepted": False,
    "mathematical_computation_or_CAS": False,
})
record_paths = [PREFIX + suffix for suffix in (
    "report-v1.1.md", "issues-v1.1.json", "sources-v1.1.json",
    "freeze-v1.1.py", "input-validation-v1.1.json", "freeze-output-v1.1.json",
)]
manifest_path = PREFIX + "manifest-v1.1.json"
create_json(manifest_path, {
    "status": "targeted annulus v1.1 repair audit complete; recommend coordinator resolution; no promotion",
    "frozen_at_utc": now,
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_v1_1_sha256": input_checks[0]["sha256"],
    "repair_ledger_sha256": input_checks[1]["sha256"],
    "nonconstructor": True,
    "both_original_whole_reports_read_after_initial_freezes": True,
    "no_peer_targeted_reaudit_findings_read": True,
    "repair_ids": ["AR1-01", "ANN2-N1", "ANN2-N2"],
    "recommend_resolution_for_v1_1": True,
    "new_substantive_objections": 0,
    "all_older_records_unchanged": True,
    "no_DG_CUT_premise": True,
    "no_H_EAI_PR_full_solution_or_novelty_acceptance": True,
    "mathematical_enumeration_or_CAS": False,
    "latest_weekly_total_used_percent": 21,
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
