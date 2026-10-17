"""Administrative byte freeze only; no mathematical search or certificate."""
from pathlib import Path
import datetime
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/notes/rank-mesh-reasoning-r1-"


def record(rel):
    data = (ROOT / rel).read_bytes()
    return {"path": rel, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(expected):
    actual = record(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    return actual


def write_new(suffix, value):
    rel = PREFIX + suffix
    with (ROOT / rel).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    return record(rel)


expected_inputs = [
    {"path": "AGENTS.md", "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"},
    {"path": "problems/2017-B4/statement.md", "sha256": "e459750064b4e25e3eaa71f25f236c046548147e415b06d8bd097839020228f3"},
    {"path": "problems/2017-B4/notes/coordinator-rank-mesh-strata-program-v1.md", "sha256": "da3c28d039cec64ef5936b2b4dc4f816b3ceac8996f614d672ced9b360da1820"},
    {"path": "problems/2017-B4/notes/coordinator-stratum-clean-lens-candidate-v1.md", "sha256": "aa4c79b1fb3136ecd3e7c5ab845733697cca925ba8203b2988fba5c9a793bd95"},
    {"path": "problems/2017-B4/notes/coordinator-stratum-clean-lens-freeze-v1.json", "sha256": "fb682945c60d8022dd633cf16ba50110488dd52490ffa21ba4c3c236fb26af46"},
]
inputs = [verify(row) for row in expected_inputs]

annulus_manifest = verify({
    "path": "problems/2017-B4/notes/annulus-reasoning-r1-freeze-v1.1.json",
    "sha256": "43ec9d1ce2e2f160658ed356cdf70a3429aa672bf28bf9af5832a9a813ccb4f9"})
annulus_data = json.loads((ROOT / annulus_manifest["path"]).read_text())
preserved = {annulus_manifest["path"]: annulus_manifest}
for row in annulus_data["artifacts"]:
    actual = verify(row)
    preserved[actual["path"]] = actual

old_validation_path = "problems/2017-B4/notes/annulus-reasoning-r1-input-validation-v1.1.json"
old_validation = json.loads((ROOT / old_validation_path).read_text())


def collect_frozen_rows(obj):
    if isinstance(obj, dict):
        if {"path", "sha256"}.issubset(obj):
            actual = verify(obj)
            prior = preserved.get(actual["path"])
            assert prior is None or prior == actual
            preserved[actual["path"]] = actual
        for value in obj.values():
            collect_frozen_rows(value)
    elif isinstance(obj, list):
        for value in obj:
            collect_frozen_rows(value)


collect_frozen_rows(old_validation)

new_suffixes = [
    "candidate-v1.md", "UR3-v1.md", "obligations-v1.md",
    "source-checks-v1.md", "worklog-v1.md", "sources-v1.json",
    "freeze-v1.py",
]
for suffix in new_suffixes:
    assert (ROOT / (PREFIX + suffix)).is_file()
for suffix in ["candidate-v1.md", "UR3-v1.md", "obligations-v1.md"]:
    assert "Candidate proof - unverified" in (ROOT / (PREFIX + suffix)).read_text()
sources = json.loads((ROOT / (PREFIX + "sources-v1.json")).read_text())
assert sources["mathematical_computation_enumeration_or_CAS"] is False
assert sources["verified_effective_settings"] is None

validation_record = write_new("input-validation-v1.json", {
    "validated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "new_program_inputs": inputs,
    "all_prior_frozen_rows_preserved": sorted(preserved.values(), key=lambda r: r["path"]),
    "unique_prior_records_preserved": len(preserved),
    "previous_candidate_and_peer_initial_bytes_unchanged": True,
    "new_mathematical_computation_or_CAS": False,
    "new_packet_status": "candidate proof - unverified",
    "parentheses": "Hashing earlier reviewer files does not read any new peer conclusions; prior annulus initial reviews were already authorized and read after their freezes."
})

artifacts = [record(PREFIX + suffix) for suffix in new_suffixes]
artifacts.append(validation_record)
manifest_record = write_new("freeze-v1.json", {
    "frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "candidate proof - unverified; construction checkpoint requiring two fresh independent whole audits",
    "constructor": "review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "claims": ["RM1", "RM1a", "scoped D4 RM2", "RM2a", "RM3", "proposed LC3", "proposed UR3-GE"],
    "scope_restrictions": [
        "Full marked zonogon arrangement, not an arbitrary incomplete window",
        "RM2 three-group D4 case: one merged pair and two singleton groups; or zero-color reduction",
        "All incident forbidden tiles excluded from the good closed selected face",
        "GE3 disks have fixed exteriors in O(r)-strand full three-direction zonogons",
        "UR3-GE source quantifiers and upper compact-cover derivation require audit; if LC3 fails retain conditional status",
        "No general multiple-nonsingleton-group port theorem, no H, no full official limit conclusion"
    ],
    "artifacts": artifacts,
    "inputs": inputs,
    "preserved_earlier_frozen_unique_records": len(preserved),
    "prior_frozen_bytes_unchanged": True,
    "mathematical_computation_enumeration_or_CAS": False,
    "source_full_paper_stream_sha256": "be2e7c17c1d9762bd454847658db9efcfe27724272debc1d8fe6a8d9483bb48f",
    "requires_two_fresh_independent_nonconstructor_whole_reviews": True,
    "no_git_shared_state_spawning_or_contacts": True,
    "only_assigned_rank_mesh_prefix_written": True,
    "latest_authoritative_weekly_total_used_percent": 24,
    "latest_telemetry_at_utc": "2026-10-17 05:51:41 UTC",
    "weekly_window_duration_minutes": 10080,
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90,
    "H_or_full_2017_solution_proved": False
})
print(json.dumps({"manifest": manifest_record, "artifacts": artifacts,
                  "prior_unique_records_preserved": len(preserved)}, indent=2))
