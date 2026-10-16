"""Separate blind R1 extension check: normalized residues modulo 19.

No coordinator code or old review checker is imported or executed.
The author uses ordinary c_t modulo 19^2. Here the normalized a_j
recurrence is derived directly from D_j(w)=0 modulo 19.
"""
from __future__ import annotations

import collections
import datetime
import hashlib
import json
import math
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
BASE = ROOT / "problems/2021-B4"
RESULT = BASE / "reviews/newton-review-1-extension-result.json"
CANDIDATE = BASE / "notes/coordinator-newton-degeneration-v1.md"
FROZEN_REPORT = BASE / "reviews/newton-review-1.md"
EXPECTED_CANDIDATE = "c38fbfa45e327c671c7737c03a4fdefb7407224445c4b8deb4761c4911a36a4f"
EXPECTED_FROZEN_REPORT = "41ded8b1f1f7541e6b97978008cea7342668bf4452b37615e75d6d07c137d088"


def emit(**record):
    print(json.dumps(record, sort_keys=True), flush=True)


def worker():
    started = time.monotonic()
    emit(event="worker_start", child_pid=os.getpid(), python=sys.version,
         method="normalized a_j modulo19, no author/old-checker import")
    assert hashlib.sha256(CANDIDATE.read_bytes()).hexdigest() == EXPECTED_CANDIDATE
    assert hashlib.sha256(FROZEN_REPORT.read_bytes()).hexdigest() == EXPECTED_FROZEN_REPORT
    # Complete raw-input integrity check; author code is hashed, not parsed.
    manifest_path = BASE / "notes/coordinator-newton-degeneration-v1-manifest.json"
    manifest = json.loads(manifest_path.read_text())
    checked = {}
    for record in manifest["artifacts"]:
        path = ROOT / record["path"]
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        assert digest == record["sha256"], record["path"]
        checked[record["path"]] = digest
    rows = [[math.comb(j, k) for k in range(j)] for j in range(2, 19)]
    weights = [math.comb(20, j) // 19 % 19 for j in range(2, 19)]
    assert all(math.comb(20, j) % 19 == 0 and math.comb(20, j) % 361 for j in range(2, 19))
    passing = {}
    for mask in range(1 << 17):
        residues = [1, -1]
        for offset, j in enumerate(range(2, 19)):
            value = (-sum(coefficient * residue
                          for coefficient, residue in zip(rows[offset], residues)) % 19
                     if mask & (1 << offset) else 0)
            residues.append(value)
        if (-1 + sum(weight * residue
                     for weight, residue in zip(weights, residues[2:]))) % 19 == 0:
            units = [j for j in range(2, 19) if residues[j]]
            assert units
            passing[mask] = max(units)
        if (mask + 1) % 16384 == 0:
            emit(event="pattern_checkpoint", visited=mask + 1,
                 passing=len(passing), elapsed_seconds=round(time.monotonic() - started, 3))
    histogram = collections.Counter(passing.values())
    initial = {j: sorted(mask for mask, unit_j in passing.items() if j == unit_j)
               for j in (15, 16, 17, 18)}
    # At d=20, h=20-J. Only h=2,3,4,5 use a verified good-prime input.
    flag_j = {18: [], 17: [18], 16: [17, 18], 15: [16, 17, 18]}
    retained, removed = {}, {}
    for j, masks in initial.items():
        flag_mask = sum(1 << (index - 2) for index in flag_j[j])
        retained[j] = [mask for mask in masks if mask & flag_mask]
        removed[j] = [mask for mask in masks if not (mask & flag_mask)]
    degeneration_only = sorted(mask for mask, j in passing.items()
                               if j < 15 or mask in retained[j])
    combined = sorted(mask for mask, j in passing.items()
                      if j < 15 or (j in (15, 16) and mask in retained[j]))
    assert len(passing) == 6680
    assert dict(histogram) == {6: 1, 7: 1, 8: 3, 9: 5, 10: 26, 11: 32,
                              12: 101, 13: 131, 14: 315, 15: 461, 16: 887,
                              17: 1674, 18: 3043}
    assert {j: len(masks) for j, masks in retained.items()} == {15: 69, 16: 88, 17: 73, 18: 0}
    assert len(removed[15]) == 392
    assert len(degeneration_only) == 845 and len(combined) == 772
    assert max(passing[mask] for mask in combined) == 16
    payload = {
        "observed_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "method": "normalized D_j residues modulo19; finite necessary filter only",
        "patterns_visited": 1 << 17,
        "passing_total": len(passing),
        "histogram": dict(sorted(histogram.items())),
        "initial_masks": initial,
        "center_derivative_degrees_required": flag_j,
        "retained_masks": retained,
        "removed_masks": removed,
        "degeneration_only_masks": degeneration_only,
        "degeneration_only_count": len(degeneration_only),
        "combined_with_prior_j17_exclusion_masks": combined,
        "combined_with_prior_j17_exclusion_count": len(combined),
        "combined_masks_sha256": hashlib.sha256(json.dumps(combined, separators=(",", ":")).encode()).hexdigest(),
        "candidate_sha256": EXPECTED_CANDIDATE,
        "frozen_old_report_sha256_unchanged": EXPECTED_FROZEN_REPORT,
        "candidate_manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
        "candidate_artifact_hashes_all_matched": checked,
    }
    RESULT.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    emit(event="worker_complete", passing_total=len(passing),
         j15_initial=len(initial[15]), j15_removed=len(removed[15]), j15_retained=len(retained[15]),
         j16_retained=len(retained[16]), j17_retained=len(retained[17]),
         degeneration_only_count=len(degeneration_only),
         combined_with_prior_j17_exclusion_count=len(combined),
         combined_masks_sha256=payload["combined_masks_sha256"],
         result_path=str(RESULT), result_sha256=hashlib.sha256(RESULT.read_bytes()).hexdigest(),
         frozen_old_report_unchanged=True,
         elapsed_seconds=round(time.monotonic() - started, 3))


if __name__ == "__main__":
    if "--worker" in sys.argv:
        worker()
    else:
        command = [sys.executable, "-u", str(pathlib.Path(__file__).resolve()), "--worker"]
        started = time.monotonic()
        child = subprocess.Popen(command, cwd=ROOT)
        emit(event="supervisor_start", pid=os.getpid(), child_pid=child.pid,
             timeout_seconds=30, command=command)
        try:
            code = child.wait(timeout=30)
        except subprocess.TimeoutExpired:
            child.kill()
            code = child.wait()
            emit(event="timeout", killed_only_child_pid=child.pid, exit_code=code)
            sys.exit(124)
        emit(event="supervisor_complete", child_pid=child.pid, exit_code=code,
             elapsed_seconds=round(time.monotonic() - started, 3))
        sys.exit(code)
