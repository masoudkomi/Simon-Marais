"""Freeze this blind analytic review; integrity hashing only, no math search."""

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = Path("problems/2021-B4/reviews/reasoning-J15-review-2")
CANDIDATE_MANIFEST = Path(
    "problems/2021-B4/notes/reasoning-J15-double-root-candidate-v1-manifest.json"
)
EXPECTED_PROOF_SHA = "e3da7a889e5937722546dab2596fdb2140597066584487ce15fb8c4e4fd8bbff"


def record(path):
    data = (ROOT / path).read_bytes()
    return {
        "path": str(path),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def save(suffix, value):
    destination = ROOT / (str(PREFIX) + suffix)
    destination.write_text(json.dumps(value, indent=2) + "\n")


def main():
    now = datetime.now(timezone.utc).isoformat()
    author_manifest = json.loads((ROOT / CANDIDATE_MANIFEST).read_text())
    checks = []
    for entry in author_manifest["records"] + author_manifest["accepted_dependencies"]:
        actual = record(Path(entry["path"]))
        actual["expected_bytes"] = entry["bytes"]
        actual["expected_sha256"] = entry["sha256"]
        actual["matches"] = (
            actual["bytes"] == entry["bytes"]
            and actual["sha256"] == entry["sha256"]
        )
        checks.append(actual)
    if checks[0]["sha256"] != EXPECTED_PROOF_SHA or not all(x["matches"] for x in checks):
        raise SystemExit("Frozen candidate/dependency integrity mismatch")

    sources = json.loads((ROOT / (str(PREFIX) + "-sources.json")).read_text())
    paths = [Path("AGENTS.md"), Path("problems/2021-B4/statement.md"), CANDIDATE_MANIFEST]
    paths.extend(Path(p) for p in sources["accepted_dependency_bodies"])
    paths.extend(Path(p) for p in sources["acceptance_registers_read"])
    paths = list(dict.fromkeys(paths))
    inputs = {
        "checked_at_utc": now,
        "purpose": "Integrity and exact dependency recording; not a mathematical computation",
        "candidate_manifest_entries": checks,
        "candidate_manifest_all_entries_match": True,
        "review_read_inputs": [record(p) for p in paths],
        "intuition_artifact": "Hashed only for manifest integrity; its table was not consulted as evidence",
    }
    save("-input-validation.json", inputs)

    artifacts = [
        Path(str(PREFIX) + suffix)
        for suffix in [
            ".md", "-issues.json", "-sources.json", "-input-validation.json", "-freeze.py"
        ]
    ]
    frozen = {
        "status": "initial blind whole mathematical review complete and frozen; no reviewer promotion",
        "frozen_at_utc": now,
        "reviewer": "review_2021_reasoning_j15_r2",
        "candidate_sha256": EXPECTED_PROOF_SHA,
        "requested_model": "gpt-6.1-sol",
        "requested_reasoning": "max",
        "verified_effective_settings": None,
        "independence": {
            "did_not_construct_candidate": True,
            "no_other_J15_review_files_or_conclusions_read_before_freeze": True,
            "initial_report_issues_sources_frozen_together": True,
            "accepted_earlier_dependency_proofs_and_acceptances_read": True,
        },
        "mathematical_scope": "Whole independent analytic reconstruction of D1-D5, all valuation partitions and degeneracies, exact discriminant sign, and all-rational low-order family",
        "substantive_issues": 0,
        "nonblocking_issues": 0,
        "repair_requested": False,
        "new_enumeration_or_CAS": False,
        "new_full_degree_or_mask_count_claim": False,
        "candidate_manifest_all_entries_match": True,
        "command": ".venv/bin/python problems/2021-B4/reviews/reasoning-J15-review-2-freeze.py",
        "records": [record(p) for p in artifacts],
    }
    save("-manifest.json", frozen)
    print(json.dumps({
        "frozen_at_utc": now,
        "candidate_manifest_entries_checked": len(checks),
        "all_entries_match": True,
        "review_artifacts_frozen": len(artifacts),
        "substantive_issues": 0,
        "manifest": str(PREFIX) + "-manifest.json",
    }))


if __name__ == "__main__":
    main()
