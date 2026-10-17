"""Hash and freeze only this independent review's new outputs.

No mathematical search or constructor-code execution. Read-only validation
of supplied frozen inputs and earlier own frozen packets.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/reviews/divisor-review-1"


def record(path):
    raw = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def assert_record(row):
    actual = record(row["path"])
    assert actual == {key: row[key] for key in ("path", "bytes", "sha256")}, row["path"]
    return actual


def exact_hash(path, expected):
    row = record(path)
    assert row["sha256"] == expected, path
    return row


manifest_path = "problems/2024-B4/notes/divisor-reasoning-r2-manifest-v1.json"
manifest_record = exact_hash(manifest_path,
    "76143ab6f93a41f0fe5c3db8088e184f41c0159c8d61b089e0bdb66c3477b971")
candidate_manifest = json.loads((ROOT / manifest_path).read_text())
candidate_records = [assert_record(row) for row in candidate_manifest["records"]]
assert len(candidate_records) == 14
assert candidate_records[0]["sha256"] == \
    "48d2ca76b3492584b38d8798650e078c7c9771fea97bae8db4d7cd51b21e2fc4"

source_certificate = ROOT / "problems/2024-B4/notes/divisor-reasoning-r2-phi11-certificate-v1.json"
review_certificate = ROOT / (PREFIX + "-certificate-input.json")
assert source_certificate.read_bytes() == review_certificate.read_bytes()
out = json.loads((ROOT / (PREFIX + "-check-output.json")).read_text())
assert out["status"] == "all exact finite-certificate checks passed"
assert (len(out["operator_columns"]), len(out["states"]), len(out["transitions"])) == (48, 15, 30)
assert out["no_index_scan_or_CAS"] is True
job = json.loads((ROOT / (PREFIX + "-job.json")).read_text())
assert job["returncode"] == 0 and not job["timed_out"] and job["child_reaped"]
assert job["child_pid"] == 76805 and job["timeout_seconds"] == 10
assert not (ROOT / (PREFIX + "-stderr.txt")).read_bytes()

# Cross-check frozen constructor output only after the independent run.
old = json.loads((ROOT / "problems/2024-B4/notes/divisor-reasoning-r2-phi11-check-output-v1.json").read_text())
independent_columns = {(r, t): [] for r in range(2) for t in range(2)}
for column in out["operator_columns"]:
    independent_columns[column["r"], column["t"]].append(column["output_encoded"])
for (r, t), columns in independent_columns.items():
    assert columns == old["operator_columns"][f"{r}{t}"]
assert [row["vectors"] for row in out["states"]] == old["complete_vector_sets"]

prior_records = {}
prior_manifest_path = "problems/2024-B4/reviews/structural-review-1-manifest-initial.json"
prior_manifest_record = exact_hash(prior_manifest_path,
    "77c28831556074148c3c930e86041515838c909bab9f4242ecda52cc43baa3a4")
prior_records[prior_manifest_path] = prior_manifest_record
prior = json.loads((ROOT / prior_manifest_path).read_text())
for key in ("artifacts", "prior_own_frozen_packets_preserved"):
    for row in prior[key]:
        prior_records[row["path"]] = assert_record(row)

repair_manifest_path = "problems/2017-B4/notes/fixedD-reasoning-r1-freeze-v1.1.json"
repair_manifest_record = exact_hash(repair_manifest_path,
    "ea3f730889db04083940bccc2fb545cd3984557c9854e43a11791d75186fb51b")
prior_records[repair_manifest_path] = repair_manifest_record
repair = json.loads((ROOT / repair_manifest_path).read_text())
for key in ("artifacts", "v1_and_annulus_hashes_preserved"):
    for row in repair[key]:
        prior_records[row["path"]] = assert_record(row)

local_sources = [record(path) for path in [
    "AGENTS.md", "problems/2024-B4/statement.md",
    "problems/2024-B4/notes/zero-automaton-criterion-reviewed-v1.1.md",
    "problems/2024-B4/reviews/criterion-acceptance.md",
    ".cache/official/2024-paper_b.pdf",
    ".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995.pdf",
    ".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-20.png",
    ".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-21.png",
    ".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-24.png",
    ".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-25.png",
]]

validation = {
    "validated_at_utc": datetime.now(timezone.utc).isoformat(),
    "candidate_manifest": manifest_record,
    "candidate_artifact_count": len(candidate_records),
    "candidate_artifacts_all_match": True,
    "candidate_artifacts": candidate_records,
    "copied_certificate_matches_source": True,
    "independent_certificate_passed": True,
    "independent_columns_and_spaces_match_frozen_constructor_output": True,
    "constructor_code_not_executed_or_imported": True,
    "prior_own_frozen_packets_preserved": list(prior_records.values()),
    "local_source_and_accepted_dependency_hashes": local_sources,
    "no_peer_divisor_review_or_conclusions_before_initial_freeze": True,
}
with (ROOT / (PREFIX + "-input-validation.json")).open("x") as stream:
    json.dump(validation, stream, indent=2)
    stream.write("\n")

suffixes = ["-initial.md", "-issues.md", "-source-checks.md",
            "-certificate-input.json", "-check.py", "-run.py",
            "-check-output.json", "-job-start.json", "-job.json",
            "-stdout.txt", "-stderr.txt", "-freeze.py", "-input-validation.json"]
artifacts = [record(PREFIX + suffix) for suffix in suffixes]
frozen = {
    "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
    "status": "fresh blind whole independent initial audit frozen; no substantive issues found",
    "reviewer": "review_2017_coarsening_r1",
    "reviewer_did_not_construct": True,
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate": candidate_records[0], "candidate_manifest": manifest_record,
    "candidate_fourteen_artifacts_rehashed_and_preserved": True,
    "no_peer_divisor_review_or_conclusions_before_initial_freeze": True,
    "unresolved_substantive_objections": 0, "requested_author_repairs": 0,
    "recommendation": "Accept the stated partial fixed-divisor criteria and consequences after both independent audits; no full classification or novelty claim",
    "independent_finite_certificate": {
        "columns": 48, "complete_subspaces": 15, "entire_space_transitions": 30,
        "child_pid": job["child_pid"], "timeout_seconds": job["timeout_seconds"],
        "returncode": job["returncode"], "child_reaped": job["child_reaped"],
        "elapsed_seconds": job["elapsed_seconds"],
        "index_scan_or_CAS_or_constructor_code_execution": False,
    },
    "artifacts": artifacts,
    "prior_own_frozen_packets_rehashed_and_preserved": len(prior_records),
    "latest_authoritative_weekly_total_used_percent": 20,
    "weekly_reset_unix": 1792745187, "total_used_ceiling_percent": 90,
    "only_assigned_review_prefix_written": True,
    "git_shared_state_spawning_charges_or_access_bypass": False,
}
manifest_output = PREFIX + "-manifest-initial.json"
with (ROOT / manifest_output).open("x") as stream:
    json.dump(frozen, stream, indent=2)
    stream.write("\n")
print(json.dumps({"artifacts": artifacts, "manifest": record(manifest_output),
                  "prior_preserved": len(prior_records), "candidate_verified": 14}, indent=2))
