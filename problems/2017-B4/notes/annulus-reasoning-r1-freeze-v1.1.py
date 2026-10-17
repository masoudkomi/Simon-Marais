"""Freeze complete author repair without editing any earlier packet.

All operations below are administrative hashes, JSON validation, or a
textual diff. No mathematical enumeration, test, or CAS is performed.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import difflib

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2017-B4/notes/annulus-reasoning-r1-"


def record(path):
    data = (ROOT / path).read_bytes()
    return {"path": path, "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def verify(row):
    actual = record(row["path"])
    assert actual == {key: row[key] for key in ("path", "bytes", "sha256")}, row["path"]
    return actual


def verify_manifest(path, expected_hash, key):
    header = record(path)
    assert header["sha256"] == expected_hash, path
    data = json.loads((ROOT / path).read_text())
    return header, [verify(row) for row in data[key]]


old_manifest, old_artifacts = verify_manifest(PREFIX + "freeze-v1.json",
    "958640fdb6a6f30b17306b3ba01014431e26fc544a26ab06f186f4e2a4f8e6cc", "artifacts")
first_manifest, first_records = verify_manifest(
    "problems/2017-B4/reviews/annulus-review-1-manifest-v1.json",
    "ec84d96e034b1ec6e8c550b402c28c97960f636e3ccde321b82c2fcbfe076b87", "records")
second_manifest, second_records = verify_manifest(
    "problems/2017-B4/reviews/annulus-review-2-freeze-manifest.json",
    "c92593a87bcba497f5f5562440c08d499e9f479f77b2baf34d685b7a45ba2d9b", "artifacts")

divisor_path = "problems/2024-B4/reviews/divisor-review-1-manifest-initial.json"
divisor_manifest, divisor_records = verify_manifest(divisor_path,
    "4295019c96eb5e7803e71f4206c963742d6023e8cd163c42ed0c93e8fd9c3157", "artifacts")
divisor_validation = json.loads((ROOT / "problems/2024-B4/reviews/divisor-review-1-input-validation.json").read_text())
earlier_own = [verify(row) for row in divisor_validation["prior_own_frozen_packets_preserved"]]
assert len(earlier_own) == 33
source_record = json.loads((ROOT / (PREFIX + "sources-v1.1.json")).read_text())
source_review_inputs = [verify(row) for row in source_record["review_inputs"]]

before = (ROOT / (PREFIX + "candidate-v1.md")).read_text().splitlines(keepends=True)
after = (ROOT / (PREFIX + "candidate-v1.1.md")).read_text().splitlines(keepends=True)
text_diff = "".join(difflib.unified_diff(before, after,
    fromfile="annulus-reasoning-r1-candidate-v1.md",
    tofile="annulus-reasoning-r1-candidate-v1.1.md"))
# This diff is an unfrozen new author artifact, refreshed once before freeze.
(ROOT / (PREFIX + "diff-v1.1.patch")).write_text(text_diff)

validation = {
    "validated_at_utc": datetime.now(timezone.utc).isoformat(),
    "original_annulus_manifest": old_manifest,
    "original_annulus_artifacts": old_artifacts,
    "first_initial_review_manifest": first_manifest,
    "first_initial_review_records_preserved": first_records,
    "second_initial_review_manifest": second_manifest,
    "second_initial_review_records_preserved": second_records,
    "first_and_second_initials_read_only_after_their_freezes": True,
    "source_review_input_hashes_verified": source_review_inputs,
    "divisor_review_manifest": divisor_manifest,
    "divisor_review_records_preserved": divisor_records,
    "earlier_own_frozen_records_preserved": earlier_own,
    "source_protocol_and_statement": [record("AGENTS.md"), record("problems/2017-B4/statement.md")],
    "diff_is_exact_full_candidate_difference": True,
    "diff_lines": len(text_diff.splitlines()),
    "mathematical_enumeration_or_CAS": False,
}
with (ROOT / (PREFIX + "input-validation-v1.1.json")).open("x") as stream:
    json.dump(validation, stream, indent=2)
    stream.write("\n")

artifacts = [record(PREFIX + suffix) for suffix in [
    "candidate-v1.1.md", "repair-v1.1.md", "worklog-v1.1.md", "sources-v1.1.json",
    "diff-v1.1.patch", "freeze-v1.1.py", "input-validation-v1.1.json",
]]
manifest = {
    "frozen_at_utc": datetime.now(timezone.utc).isoformat(),
    "status": "candidate proof - unverified; full annulus v1.1 author repair pending both targeted re-audits",
    "constructor": "review_2017_coarsening_r1",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "repair_ids": ["AR1-01", "ANN2-N1", "ANN2-N2"],
    "author_disposition": "repair proposed; reviewers and coordinator retain resolution authority",
    "requires_both_targeted_independent_reaudits": True,
    "artifacts": artifacts,
    "original_annulus_v1_and_both_initial_audits_unchanged": True,
    "divisor_review1_and_earlier_own_33_frozen_files_unchanged": True,
    "no_mathematical_computation_or_CAS": True,
    "no_DG_or_CUT_or_height_only_conversion_premise": True,
    "only_assigned_new_annulus_prefix_written": True,
    "git_shared_status_or_spawning": False,
    "H_or_full_2017_solution_proved": False,
    "new_external_theorem_or_novelty_claim": False,
    "latest_authoritative_weekly_total_used_percent": 21,
    "weekly_reset_unix": 1792745187, "total_used_ceiling_percent": 90,
}
output = PREFIX + "freeze-v1.1.json"
with (ROOT / output).open("x") as stream:
    json.dump(manifest, stream, indent=2)
    stream.write("\n")
print(json.dumps({"artifacts": artifacts, "manifest": record(output),
                  "initial_review_records_preserved": len(first_records) + len(second_records),
                  "earlier_own_records_preserved": len(earlier_own)}, indent=2))
