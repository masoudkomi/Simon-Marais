"""Administrative freeze of the full versioned rank-mesh scope repair."""
from pathlib import Path
import json
import hashlib
import datetime
import difflib

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2017-B4/notes/rank-mesh-reasoning-r1-"


def row(path):
    raw = (ROOT/path).read_bytes()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def check(expected):
    actual = row(expected["path"])
    assert actual["sha256"] == expected["sha256"], actual
    if "bytes" in expected:
        assert actual["bytes"] == expected["bytes"], actual
    return actual


def write(suffix, obj):
    path = P+suffix
    with (ROOT/path).open("x", encoding="utf-8") as out:
        json.dump(obj, out, ensure_ascii=False, indent=2)
        out.write("\n")
    return row(path)


old_main = check({"path": P+"candidate-v1.md", "sha256": "e0f2e55e62aabe5547120f4fc72c506c3f680844a90aa98ece7147d404178d27"})
old_ur = check({"path": P+"UR3-v1.md", "sha256": "40ad9b252b6c34f5dee5c8cd3eedea8e8feeabb0cec1497b224bf5c32ba58aab"})
old_manifest = check({"path": P+"freeze-v1.json", "sha256": "7173ee9db5d7990af60ca0731a301d9017691e42f9c741efce1e81a7d90de747"})
preserved = {}


def preserve(expected):
    actual = check(expected)
    previous = preserved.get(actual["path"])
    assert previous is None or previous == actual
    preserved[actual["path"]] = actual
    return actual


return_manifest = preserve({"path": "problems/2020-B4/notes/reasoning-return-r3-freeze-v1.json", "sha256": "413351e9d6d6b9e8c463ba6b3ad230f2d4440c5042711df882f879a7b82a02ed"})
return_data = json.loads((ROOT/return_manifest["path"]).read_text())
for r in return_data["artifacts"]:
    preserve(r)
return_validation = json.loads((ROOT/"problems/2020-B4/notes/reasoning-return-r3-input-validation-v1.json").read_text())
for r in return_validation["earlier_own_frozen_unique_records_preserved"]:
    preserve(r)
for r in return_validation["accepted_2020_artifacts_preserved"]:
    preserve(r)
for r in return_validation["deep_literature_artifacts_preserved"]:
    preserve(r)

review_manifests = []
review_rows = []
for path, sha in [
    ("problems/2017-B4/reviews/rank-mesh-review-1-manifest-v1.json", "e76dde7938e9e5a7e48ba6b8eea6cee6e4fa695cf898dcc44973df3d25aeb328"),
    ("problems/2017-B4/reviews/rank-mesh-review-2-manifest-v1.json", "7f591a955988bc30e867b8928d530b6e22926ecd8170987b1a6e3e13fa522dcb"),
]:
    rec = preserve({"path": path, "sha256": sha})
    review_manifests.append(rec)
    obj = json.loads((ROOT/path).read_text())
    review_rows.extend(preserve(r) for r in obj["records"])

old = (ROOT/(P+"candidate-v1.md")).read_text()
new = (ROOT/(P+"candidate-v1.1.md")).read_text()
patch = "".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                   fromfile="rank-mesh-reasoning-r1-candidate-v1.md",
                                   tofile="rank-mesh-reasoning-r1-candidate-v1.1.md"))
assert patch == (ROOT/(P+"diff-v1.1.patch")).read_text()
assert "one rectifiable Jordan curve" in new
assert "O_D(r sum_j P_j+M r^2)" in new
assert "the binom(D,2) finite tile types" in new
assert "the six finite tile types" not in new
assert "Candidate proof - unverified" in new
assert row(P+"UR3-v1.md") == old_ur

validation = write("input-validation-v1.1.json", {
    "validated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "original_main": old_main,
    "unchanged_analytic_supplement": old_ur,
    "original_manifest": old_manifest,
    "review_manifests": review_manifests,
    "both_full_initial_records_preserved": review_rows,
    "both_initials_read_only_after_their_freezes": True,
    "all_prior_unique_records_preserved": sorted(preserved.values(), key=lambda r: r["path"]),
    "prior_unique_record_count": len(preserved),
    "full_candidate_exact_diff_verified": True,
    "no_mathematical_computation_or_CAS": True
})
suffixes = ["candidate-v1.1.md", "repair-v1.1.md", "worklog-v1.1.md",
            "sources-v1.1.json", "diff-v1.1.patch", "build-v1.1.py",
            "freeze-v1.1.py"]
artifacts = [row(P+s) for s in suffixes]+[validation]
manifest = write("freeze-v1.1.json", {
    "frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "candidate proof - unverified; full versioned author repair awaiting both affected reaudits",
    "constructor": "review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "repair_ids": ["RMR1-01", "RM2-01", "N1"],
    "repair_scope": "One rectifiable Jordan window and actual summed costs; general-D alphabet wording; no other extension",
    "artifacts": artifacts,
    "original_main": old_main,
    "unchanged_analytic_supplement": old_ur,
    "original_packet_and_both_initial_audits_unchanged": True,
    "prior_unique_records_preserved": len(preserved),
    "both_exact_counterexamples_preserved": True,
    "requires_both_original_auditors_affected_reaudits": True,
    "author_promotion": False,
    "no_new_analytic_theorem_or_general_window_extension": True,
    "no_mathematical_computation_enumeration_or_CAS": True,
    "no_git_shared_edits_spawning_contacts_charges_or_bypass": True,
    "only_assigned_new_rank_mesh_prefix_written": True,
    "H_or_full_2017_solution_proved": False,
    "latest_authoritative_weekly_total_used_percent": 27,
    "latest_telemetry_at_utc": "2026-10-17 06:44:58 UTC",
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90
})
print(json.dumps({"manifest": manifest, "artifacts": artifacts,
                  "prior_unique_records_preserved": len(preserved)}, indent=2))
