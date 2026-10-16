#!/usr/bin/env python3
"""Independent R2 finite evidence: integrate normalized derivatives over F_19.

No import or execution of the author's filter. B_j'(x)=j B_{j-1}(x),
B_1=x-1. All degrees here are below 19, so integration is unique up to
the constant. Select that constant to make B_j(0)=0 or B_j(1)=0.
This tests necessary congruences only, never sufficiency or unrestricted CA.
"""

import collections
import hashlib
import json
import math
import os
import subprocess
import sys
import time


def emit(**record):
    print(json.dumps(record, sort_keys=True), flush=True)


def worker():
    p, d = 19, 20
    js = tuple(range(2, 19))
    # Ascending coefficient representation, independent of binomial recursion.
    integration_scales = {
        j: tuple((j * pow(i + 1, -1, p)) % p for i in range(j))
        for j in js
    }
    weights = {j: math.comb(d, j) // p for j in js}
    assert all(math.comb(d, j) % p == 0 for j in js)
    hist = collections.Counter()
    first_masks = {}
    accept_digest = hashlib.sha256()
    passed = 0
    emit(event="parameters", child_pid=os.getpid(), python=sys.version,
         degree=d, prime=p, masks=2 ** len(js),
         bit_definition="bit j-2 is 1 iff B_j(1)=0 is selected",
         algorithm="B_1=x-1; integrate B_j prime=j B_(j-1); choose constant")
    for mask in range(2 ** len(js)):
        poly = [p - 1, 1]
        total = 0
        for j in js:
            tail = [value * scale % p
                    for value, scale in zip(poly, integration_scales[j])]
            constant = -sum(tail) % p if mask & (1 << (j - 2)) else 0
            poly = [constant] + tail
            total += weights[j] * constant
        if (total - 1) % p == 0:
            passed += 1
            hist[poly[0]] += 1
            first_masks.setdefault(poly[0], mask)
            accept_digest.update(f"{mask}:{poly[0]}\n".encode("ascii"))
        if (mask + 1) % 16384 == 0:
            emit(event="checkpoint", visited=mask + 1, passed=passed)
    emit(event="complete", visited=2 ** len(js), passed=passed,
         a18_residue_histogram=dict(sorted(hist.items())),
         nonzero_a18_count=passed - hist[0], zero_a18_count=hist[0],
         accepted_mask_residue_sha256=accept_digest.hexdigest(),
         first_mask_by_a18_residue=dict(sorted(first_masks.items())),
         scope="finite necessary congruences; no lifting or sufficiency claim")


def main():
    if sys.argv[1:] == ["--worker"]:
        worker()
        return
    if sys.argv[1:]:
        raise SystemExit("usage: witness-review-2-filter.py [--worker]")
    command = [sys.executable, os.path.abspath(__file__), "--worker"]
    started = time.monotonic()
    child = subprocess.Popen(command)
    emit(event="child_started", child_pid=child.pid, command=command,
         timeout_seconds=30)
    try:
        code = child.wait(timeout=30)
    except subprocess.TimeoutExpired:
        child.kill()
        child.wait()
        emit(event="timeout", child_pid=child.pid,
             elapsed_seconds=time.monotonic() - started)
        raise SystemExit(124)
    emit(event="child_finished", child_pid=child.pid, exit_code=code,
         elapsed_seconds=time.monotonic() - started)
    raise SystemExit(code)


if __name__ == "__main__":
    main()
