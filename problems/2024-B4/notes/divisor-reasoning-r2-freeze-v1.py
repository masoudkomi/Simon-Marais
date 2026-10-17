"""Metadata-only one-time freeze. Does not rerun mathematical computations."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2024-B4/notes/divisor-reasoning-r2-"


def fingerprint(relative):
    data = (ROOT / relative).read_bytes()
    return {"path": relative, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def create_json(relative, value):
    if not relative.startswith(PREFIX):
        raise RuntimeError("Write outside assigned construction prefix")
    with (ROOT / relative).open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


previous = [
    "problems/2021-B4/reviews/reasoning-J15-review-2-manifest.json",
    "problems/2024-B4/notes/structural-reasoning-r2-manifest-v1.json",
    "problems/2017-B4/reviews/fixedD-structural-review-1-manifest-v1.json",
]
previous_checks = []
for relative in previous:
    old_manifest = json.loads((ROOT / relative).read_text())
    checks = []
    for expected in old_manifest["records"]:
        actual = fingerprint(expected["path"])
        actual["matches"] = all(actual[key] == expected[key] for key in ("bytes", "sha256"))
        if not actual["matches"]:
            raise RuntimeError(f"Older frozen record changed: {expected['path']}")
        checks.append(actual)
    previous_checks.append({"manifest": fingerprint(relative), "all_records_match": True, "checks": checks})
assert previous_checks[2]["manifest"]["sha256"] == "3b9b23ae55f9864c7f2e6e5122fe3d7de29e1be0b276ecb8e78e8ad6f2ece2d1"

sources = json.loads((ROOT / (PREFIX + "sources-v1.json")).read_text())
dependency_records = [fingerprint(path) for path in sources["local_dependencies"]]
thesis = fingerprint(".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995.pdf")
assert thesis["sha256"] == "d8e8e62d873c5ec69e2fd40473a9aee257bb8d4994cb5ffc1a42cb70f8bcbd24"
viewed_images = [fingerprint(f".cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-{page}.png") for page in (24, 25)]

job = json.loads((ROOT / (PREFIX + "phi11-job-v1.json")).read_text())
assert job["returncode"] == 0 and job["status"] == "completed"
assert job["child_pid"] == 75264 and job["timeout_seconds"] == 5.0
check_output = json.loads((ROOT / (PREFIX + "phi11-check-output-v1.json")).read_text())
certificate_record = fingerprint(PREFIX + "phi11-certificate-v1.json")
assert certificate_record["sha256"] == check_output["certificate_sha256"]
assert check_output["closed_graph_verified"] is True
assert check_output["index_scan_performed"] is False
for kind in ("stdout", "stderr"):
    data = Path(job[kind]["path"]).read_bytes()
    assert hashlib.sha256(data).hexdigest() == job[kind]["sha256"]

now = datetime.now(timezone.utc).isoformat()
validation_path = PREFIX + "input-validation-v1.json"
create_json(validation_path, {
    "checked_at_utc": now,
    "older_frozen_packet_records": previous_checks,
    "older_frozen_packets_unchanged": True,
    "local_dependency_records": dependency_records,
    "cached_primary_thesis": thesis,
    "viewed_cached_primary_pages": viewed_images,
    "certificate_hash_matches_completed_check": True,
    "finite_check_completed_successfully": True,
    "new_index_scan_or_CAS": False,
    "metadata_only_freeze": True,
})

freeze_output_path = PREFIX + "freeze-output-v1.json"
create_json(freeze_output_path, {
    "frozen_at_utc": now,
    "status": "candidate proof - unverified; ready for two fresh independent nonconstructor audits",
    "criteria": {"phi7_divides_phi_n": "odd n>=3 iff n=7", "phi11_divides_phi_n": "odd n>=3 iff n=11"},
    "phi7_proof": "Unrestricted analytic parameter-coefficient witness; no computation",
    "phi11_proof": "General Frobenius-section invariant and checked closed 15-state, 30-edge exact certificate",
    "older_frozen_packets_unchanged": True,
    "full_B4b_classification": False,
    "new_reducible_exponents_claimed": False,
    "novelty_claimed": False,
})

artifact_suffixes = [
    "candidate-v1.md",
    "source-audit-v1.md",
    "research-log-v1.md",
    "sources-v1.json",
    "phi11-certificate-v1.json",
    "phi11-check-v1.py",
    "phi11-run-v1.py",
    "phi11-check-output-v1.json",
    "phi11-job-v1.json",
    "phi11-stdout-v1.txt",
    "phi11-stderr-v1.txt",
    "freeze-v1.py",
    "input-validation-v1.json",
    "freeze-output-v1.json",
]
manifest = {
    "status": "candidate proof - unverified; immutable construction packet before fresh audits",
    "frozen_at_utc": now,
    "constructor": "review_2021_reasoning_j15_r2",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "candidate": fingerprint(PREFIX + "candidate-v1.md"),
    "proposed_results": [
        "C7: whole phi7 divides phi_n iff odd n>=3 equals 7; analytic proof",
        "C11: whole phi11 divides phi_n iff odd n>=3 equals 11; exact closed finite certificate",
        "G: common absolute components excluded using attributed JMW irreducibility",
        "Graded finite odd-polynomial sum divisibility corollary",
        "Attributed general fixed-factor function-field zero-set reduction from Derksen",
    ],
    "required_reviews": "Two fresh independent nonconstructors, initial reports blind to each other, one reconstructing the whole packet; coordinator alone promotes",
    "old_J15_2024structural_2017review_records_unchanged": True,
    "peer_2017_new_structural_review_read": False,
    "mathematical_index_scan_or_larger_enumeration_or_native_CAS": False,
    "finite_exact_certificate": {"states": 15, "edges": 30, "operator_columns": 48, "child_pid": 75264, "timeout_seconds": 5, "returncode": 0},
    "latest_weekly_total_used_percent": 19,
    "weekly_reset_unix": 1792745187,
    "full_B4b_solution": False,
    "priority_or_novelty_claimed": False,
    "command": ".venv/bin/python " + PREFIX + "freeze-v1.py",
    "records": [fingerprint(PREFIX + suffix) for suffix in artifact_suffixes],
}
manifest_path = PREFIX + "manifest-v1.json"
create_json(manifest_path, manifest)
print(json.dumps({
    "frozen_at_utc": now,
    "candidate": manifest["candidate"],
    "manifest": fingerprint(manifest_path),
    "older_frozen_packets_unchanged": True,
    "candidate_status": "unverified; needs two fresh nonconstructor audits",
}, indent=2))
