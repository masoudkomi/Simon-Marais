"""One-time review freeze and integrity check; not mathematical evidence."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/moment-tail-review-1-"


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
constructor_manifest = "problems/2019-B4/notes/coordinator-moment-regular-tail-freeze-v1.json"
constructor_manifest_check = check({
    "path": constructor_manifest,
    "sha256": "320264ddc543a1936329ac8ffe78c7336f6b2064e591ca8f892791d11787171c",
})
constructor = read_json(constructor_manifest)
constructor_checks = [check(row) for row in constructor["files"]]
assert len(constructor_checks) == 13
check({"path": "problems/2019-B4/notes/coordinator-moment-regular-tail-candidate-v1.md",
       "sha256": "29b02df71668db17b7111319d40ccdcdf798bed19dad4a8b76c7bcedaa332ef2"})

# Only compare the exact output fractions after the independent certificate.
author_arithmetic = read_json("problems/2019-B4/notes/coordinator-regular-tail-certificate-v1.json")
own_arithmetic = read_json(PREFIX + "certificate-output-v1.json")
for akey, bkey in [("E_G_r", "E_G_at_r"), ("E_P24_r", "E_P24_at_r")]:
    assert all(int(author_arithmetic[akey][part]) == own_arithmetic[bkey][part]
               for part in ["numerator", "denominator"])

prior_path = "problems/2022-B4/reviews/return-r3-review-1-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "83a5ec54620ef18a08a4cdfb459038467370e0a020ed972587da3844daff7fc1"})
prior = read_json(prior_path)
prior_checks = [check(row) for row in prior["records"]]
prior_validation = read_json("problems/2022-B4/reviews/return-r3-review-1-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 18
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "constructor_manifest": constructor_manifest_check,
    "constructor_records": constructor_checks,
    "all_thirteen_constructor_records_unchanged": True,
    "extra_read_inputs": [fingerprint("AGENTS.md"),
                          fingerprint("problems/2019-B4/statement.md")],
    "independent_arithmetic_reduced_fraction_comparisons": 2,
    "own_certificate_derived_and_run_before_reading_author_code_and_result": True,
    "older_own_packets": older,
    "all_nineteen_older_own_packets_unchanged": True,
    "new_peer_review_or_findings_read": False,
    "mathematical_history_factor_queue_or_automaton_enumeration": False,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "constructor_records_checked": 13,
    "older_own_packets_checked": 19,
    "all_fingerprints_match": True,
    "independent_fixed_trial_sign_certificate_passed": True,
    "new_peer_findings_read": False,
    "candidate_or_shared_mutation": False,
    "git_operations": False,
})
record_paths = [PREFIX + name for name in [
    "initial.md", "issues.md", "source-checks.md",
    "certificate-v1.py", "run-v1.py", "certificate-output-v1.json",
    "certificate-stderr-v1.txt", "job-start-v1.json", "job-v1.json",
    "freeze-v1.py",
]] + [validation_path, output_path]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "independent initially blind whole review; recommendation only; no promotion",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "constructor_candidate_sha256": "29b02df71668db17b7111319d40ccdcdf798bed19dad4a8b76c7bcedaa332ef2",
    "whole_claims": ["M1", "M2", "M3", "renewal and radius endpoints", "independent rational signs"],
    "substantive_objections": 0,
    "repair_requested": False,
    "peer_findings_read_before_freeze": False,
    "independent_arithmetic_scope": "one fixed rational certificate, no search or history enumeration",
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 24,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2019-B4/reviews/moment-tail-review-1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "constructor_records_checked": 13,
                  "older_own_packets_checked": 19}, indent=2))
