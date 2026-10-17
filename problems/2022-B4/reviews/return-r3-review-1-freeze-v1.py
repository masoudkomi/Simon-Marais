"""One-time administrative freeze. No mathematical computation is performed."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2022-B4/reviews/return-r3-review-1-"


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
    assert path.startswith(PREFIX)
    with (ROOT / path).open("x") as stream:
        json.dump(payload, stream, indent=2)
        stream.write("\n")
    return path


now = datetime.now(timezone.utc).isoformat()
base_path = "problems/2022-B4/notes/reasoning-return-r3-freeze-v1.json"
supp_path = "problems/2022-B4/notes/reasoning-return-r3-supplement-freeze-v1.json"
base = read_json(base_path)
supp = read_json(supp_path)
freeze_links = [
    check({"path": base_path,
           "sha256": "f97219fac5b001d981b64f1ce9be448f57c4ba8f977f3d09c29bf5b1d3f9d55a"}),
    check({"path": supp_path,
           "sha256": "0666852765586bf3316413c64436290cd1861ccaa9af36b00c584ffa9aad914b"}),
]
constructor_records = (base["artifacts"] + base["inputs"] + supp["artifacts"]
                       + [supp["base_freeze"]]
                       + base["existing_ignored_cached_primary_sources_verified"])
constructor_checks = [check(row) for row in constructor_records]
assert len(constructor_checks) == 20
for path, digest in [
    ("problems/2022-B4/notes/reasoning-return-r3-candidate-v1.md",
     "eb3d176680116595015069507f3904a0d048e44d3c2cde06965647010b82764e"),
    ("problems/2022-B4/notes/reasoning-return-r3-supplement-candidate-v1.md",
     "a0512f751dc5c648043025948a841fa4ecffb280785641c5e85f9fae5c99bca3"),
]:
    check({"path": path, "sha256": digest})

# Check only byte fingerprints of the reviewer's own earlier immutable work.
# No peer's new findings or review body is read by this procedure.
prior_path = "problems/2021-B4/notes/reasoning-return-r3-transfer-manifest-v1.json"
prior_fp = check({"path": prior_path,
                  "sha256": "b844f5934f35b1362ff7cbe811ed632fc2224894040e11015c8b0a0f499b3c19"})
prior = read_json(prior_path)
prior_checks = [check(row) for row in prior["records"]]
prior_validation = read_json(
    "problems/2021-B4/notes/reasoning-return-r3-transfer-input-validation-v1.json")
older = []
for packet in prior_validation["older_own_packets"]:
    older.append({"manifest": check(packet["manifest"]),
                  "checks": [check(row) for row in packet["checks"]]})
assert len(older) == 17
older.append({"manifest": prior_fp, "checks": prior_checks})

validation_path = create_json("input-validation-v1.json", {
    "checked_at_utc": now,
    "constructor_freeze_links": freeze_links,
    "constructor_record_checks": constructor_checks,
    "all_twenty_constructor_records_unchanged": True,
    "older_own_packets": older,
    "all_eighteen_older_own_packets_unchanged": True,
    "new_peer_review_bodies_or_findings_read": False,
    "metadata_only": True,
})
output_path = create_json("freeze-output-v1.json", {
    "frozen_at_utc": now,
    "constructor_records_checked": 20,
    "older_own_packets_checked": 18,
    "all_fingerprints_match": True,
    "mathematical_enumeration_or_CAS": False,
    "git_or_shared_file_mutation": False,
    "blind_whole_initial_review_complete": True,
})
record_paths = [
    PREFIX + "initial.md",
    PREFIX + "issues.md",
    PREFIX + "source-checks.md",
    PREFIX + "freeze-v1.py",
    validation_path,
    output_path,
]
manifest_path = create_json("manifest-v1.json", {
    "frozen_at_utc": now,
    "status": "independent initially blind whole review; recommendation only; no promotion",
    "reviewer": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "audited_constructor_hashes": {
        "candidate": "eb3d176680116595015069507f3904a0d048e44d3c2cde06965647010b82764e",
        "supplement": "a0512f751dc5c648043025948a841fa4ecffb280785641c5e85f9fae5c99bca3",
    },
    "whole_claims": ["R0", "R1", "R2", "R3", "S1", "S2", "source hypotheses"],
    "substantive_objections": 0,
    "nonblocking_scope_cautions": ["N1 positive ordinary lift wording", "N2 source final acceptance"],
    "peer_findings_read_before_freeze": False,
    "mathematical_program_enumeration_or_CAS": False,
    "candidate_or_shared_changes": False,
    "git_operations": False,
    "spawned_agents": False,
    "latest_weekly_total_used_percent": 23,
    "weekly_window_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "command": "python3 problems/2022-B4/reviews/return-r3-review-1-freeze-v1.py",
    "records": [fingerprint(path) for path in record_paths],
})
print(json.dumps({"frozen_at_utc": now,
                  "manifest": fingerprint(manifest_path),
                  "records": len(record_paths),
                  "constructor_records_checked": 20,
                  "older_own_packets_checked": 18}, indent=2))
