"""Administrative freeze of an initially blind whole orientation audit."""
from pathlib import Path
import hashlib
import json
import datetime

ROOT = Path(__file__).resolve().parents[3]
P = "problems/2017-B4/reviews/orientation-chart-review-1-"


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
        json.dump(obj, out, indent=2, ensure_ascii=False)
        out.write("\n")
    return row(path)


target = check({"path": "problems/2017-B4/notes/coordinator-orientation-charts-candidate-v1.md", "sha256": "a64eea09f6cab7ba86f158cc685ab20d35742c4d8dbfc3dfb60260a3b7ada552"})
source_manifest = check({"path": "problems/2017-B4/notes/coordinator-orientation-charts-freeze-v1.json", "sha256": "338a50e977061e29a379cf311273d5d8edada01ebf86891aa80d4afa74cd1da0"})
source_data = json.loads((ROOT/source_manifest["path"]).read_text())
inputs = [check(r) for r in source_data["files"]]
inputs.append(check({"path": "AGENTS.md", "sha256": "28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff"}))

previous_manifest = check({"path": "problems/2017-B4/notes/rank-mesh-reasoning-r1-freeze-v1.1.json", "sha256": "0273dd67122b549dbf7b9cf6dab57f6671aab52ed793e942524c1bd69718bb14"})
previous = json.loads((ROOT/previous_manifest["path"]).read_text())
preserved = {previous_manifest["path"]: previous_manifest}
for r in previous["artifacts"]:
    a = check(r)
    preserved[a["path"]] = a
older = json.loads((ROOT/"problems/2017-B4/notes/rank-mesh-reasoning-r1-input-validation-v1.1.json").read_text())
for r in older["all_prior_unique_records_preserved"]:
    a = check(r)
    preserved[a["path"]] = a
validation = write("input-validation.json", {
    "validated_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "candidate": target, "candidate_manifest": source_manifest,
    "declared_inputs": inputs,
    "all_earlier_unique_frozen_records_preserved": sorted(preserved.values(), key=lambda r:r["path"]),
    "earlier_unique_count": len(preserved),
    "no_peer_orientation_review_read": True,
    "constructed_OC_argument": False,
    "earlier_fixedD_rankmesh_authorship_disclosed": True,
    "mathematical_computation_or_CAS": False
})
artifacts = [row(P+s) for s in ["initial.md", "issues.md", "source-checks.md", "freeze.py"]]+[validation]
manifest = write("manifest-initial.json", {
    "frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "status": "initially blind independent whole nonconstructor audit; no substantive defect found; no promotion",
    "reviewer": "review_2017_coarsening_r1",
    "requested_settings": {"model":"gpt-6.1-sol", "reasoning":"max"},
    "verified_effective_settings": None,
    "candidate": target, "candidate_manifest": source_manifest,
    "whole_claims_reconstructed": ["OC1", "OC2", "OC3", "D4 stratum-type conclusion"],
    "substantive_issues": [],
    "peer_findings_read_before_initial_freeze": False,
    "constructed_argument": False,
    "prior_background_authorship_disclosed": True,
    "artifacts": artifacts,
    "candidate_and_declared_inputs_unchanged": True,
    "earlier_unique_frozen_records_preserved": len(preserved),
    "mathematical_enumeration_CAS_or_certificate": False,
    "only_assigned_review_prefix_written": True,
    "git_shared_edits_spawning_contacts_charges_or_bypass": False,
    "reviewer_promotion": False,
    "H_PR_global_chart_or_official_limit_claim": False,
    "latest_authoritative_weekly_total_used_percent": 27,
    "telemetry_at_utc": "2026-10-17 06:44:58 UTC",
    "weekly_reset_unix": 1792745187,
    "total_used_ceiling_percent": 90
})
print(json.dumps({"manifest":manifest,"artifacts":artifacts,"earlier_unique_preserved":len(preserved)},indent=2))
