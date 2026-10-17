"""One-time targeted-review integrity/diff freeze; no mathematical calculation."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2020-B4/reviews/reasoning-return-r3-review-2-reaudit-"
AUTHOR = "problems/2020-B4/notes/reasoning-return-r3-"


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
constructor_path = AUTHOR + "freeze-v1.1.json"
constructor_fp = check({"path": constructor_path,
                        "sha256": "807827ddb14ace9a98f0c9f8bf7f63244129414d0a85cfcde4889ff84d7aa806"})
constructor = read_json(constructor_path)
constructor_checks = [check(row) for row in constructor["artifacts"]]
assert len(constructor_checks) == 8
assert constructor_checks[0]["sha256"] == "f6f9947b8140f9d4bafc01ec24bf68dcd7634df5ccba655f4e6cdab334bef467"
assert constructor_checks[1]["sha256"] == "12fabe3054a308bbb578bf59cdf9696f835eb5092558d8f2a90f2dc6cd678877"

declared = {}


def collect_and_check(value):
    if isinstance(value, dict):
        if (isinstance(value.get("path"), str)
                and isinstance(value.get("sha256"), str)
                and len(value["sha256"]) == 64):
            actual = check(value)
            previous = declared.get(actual["path"])
            assert previous is None or previous == actual
            declared[actual["path"]] = actual
        for item in value.values():
            collect_and_check(item)
    elif isinstance(value, list):
        for item in value:
            collect_and_check(item)


collect_and_check(read_json(AUTHOR + "input-validation-v1.1.json"))
original_fp = check({"path": AUTHOR + "freeze-v1.json",
                     "sha256": "413351e9d6d6b9e8c463ba6b3ad230f2d4440c5042711df882f879a7b82a02ed"})
original_checks = [check(row) for row in read_json(AUTHOR + "freeze-v1.json")["artifacts"]]
collect_and_check(read_json(AUTHOR + "input-validation-v1.json"))
initial_records = []
for number, key, sha in [
    (1, "files", "cf3dcc0cfe57356ec3b61f8898403a8c2a6d6f6661f579e43080bdf313c1d7d1"),
    (2, "records", "bbda561c3d8379666e92308ae851de4f46c042548f4d4e3bf6bcdc0ba01b07b6"),
]:
    path = f"problems/2020-B4/reviews/reasoning-return-r3-review-{number}-manifest-v1.json"
    initial_records.append({"manifest": check({"path": path, "sha256": sha}),
                            "records": [check(row) for row in read_json(path)[key]]})

old_main = (ROOT / (AUTHOR + "candidate-v1.md")).read_text()
new_main = (ROOT / (AUTHOR + "candidate-v1.1.md")).read_text()
exact_diff = "".join(difflib.unified_diff(
    old_main.splitlines(True), new_main.splitlines(True),
    fromfile="reasoning-return-r3-candidate-v1.md",
    tofile="reasoning-return-r3-candidate-v1.1.md"))
assert exact_diff == (ROOT / (AUTHOR + "diff-v1.1.patch")).read_text()

prior_path = "problems/2017-B4/reviews/single-pair-allD-review-1-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "ed7835d60efe1bae9e295b8bbbce0774953f16de3627059af2c56001712b47a2"})
prior_checks = [check(row) for row in read_json(prior_path)["records"]]
prior_validation = read_json("problems/2017-B4/reviews/single-pair-allD-review-1-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 28
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.1.json", {
    "checked_at_utc": now,
    "constructor_manifest": constructor_fp,
    "constructor_records": constructor_checks,
    "all_eight_constructor_records_unchanged": True,
    "original_constructor_manifest": original_fp,
    "original_constructor_records": original_checks,
    "both_original_audit_records": initial_records,
    "all_unique_author_declared_input_rows": sorted(declared.values(), key=lambda row: row["path"]),
    "unique_author_declared_rows_checked": len(declared),
    "exact_unified_diff_independently_recomputed": True,
    "author_builder_executed": False,
    "older_own_packets": older,
    "all_twenty_nine_older_own_packets_unchanged": True,
    "new_peer_targeted_review_or_findings_read": False,
    "mathematical_program_enumeration_or_CAS": False,
    "original_BBB_raw_pdf_hash_still_unresolved": True,
})
output_path = create_json("freeze-output-v1.1.json", {
    "frozen_at_utc": now,
    "constructor_records_checked": 8,
    "unique_author_declared_rows_checked": len(declared),
    "older_own_packets_checked": 29,
    "all_fingerprints_match": True,
    "closed_for_version1_1_only": ["2020R2-01"],
    "open_substantive_issues": [],
    "targeted_review_complete_before_new_peer_findings": True,
    "candidate_or_shared_mutation": False,
    "git_operations": False,
})
record_paths = [PREFIX + name for name in [
    "initial-v1.1.md", "issues-v1.1.json", "source-checks-v1.1.md", "freeze-v1.1.py",
]] + [validation_path, output_path]
manifest_path = create_json("manifest-v1.1.json", {
    "frozen_at_utc": now,
    "status": "complete affected reaudit; recommend close2020R2-01 for v1.1 only",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate_sha256": "f6f9947b8140f9d4bafc01ec24bf68dcd7634df5ccba655f4e6cdab334bef467",
    "per_inference_ledger_rows": 18,
    "recommend_closed_for_version1_1_only": ["2020R2-01"],
    "substantive_objections": [],
    "required_author_repairs": [],
    "full_repaired_main_ledger_diff_and_all_affected_uses_read": True,
    "original_false_inference_and_both_initials_preserved": True,
    "new_peer_findings_read_before_freeze": False,
    "mathematical_program_enumeration_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 28,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2020-B4/reviews/reasoning-return-r3-review-2-reaudit-freeze-v1.1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "constructor_records_checked": 8,
                  "unique_author_declared_rows_checked": len(declared),
                  "older_own_packets_checked": 29}, indent=2))
