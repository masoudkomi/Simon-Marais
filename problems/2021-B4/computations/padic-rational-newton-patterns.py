#!/usr/bin/env python3
"""Exact degree-20 necessary center patterns grouped by the last unit index.

The new Newton lemmas are candidate proofs, not validated theorems. Counts
below are finite evidence for their possible use. Standard library only.
"""
import argparse
import collections
import json
import math
import os
import subprocess
import sys
import time


def emit(**r):
    print(json.dumps(r, sort_keys=True), flush=True)


def worker():
    d, p = 20, 19
    a = [0]*(d-1)
    a[0], a[1] = 1, -1
    bins = [[math.comb(j,k) % p for k in range(j+1)] for j in range(d)]
    weights = {j:(math.comb(d,j)//p) % p for j in range(2,d-1)}
    histogram = collections.Counter()
    remaining = collections.Counter()
    masks_j17 = []
    discarded_j17 = []
    visited = 0
    emit(event="parameters", pid=os.getpid(), degree=d, prime=p,
         patterns=2**17, mask="bit j-2 selects center for normalized D_j",
         scope="necessary conditions; candidate Newton constraints")

    def visit(j, total, mask):
        nonlocal visited
        if j == d-1:
            visited += 1
            if total % p != 1:
                return
            J = max(k for k in range(2,d-1) if a[k] % p)
            histogram[J] += 1
            if J == 18:
                return
            if J == 17:
                if not mask & (1 << 16):
                    discarded_j17.append(mask)
                    return
                masks_j17.append(mask)
            remaining[J] += 1
            return
        a[j] = 0
        visit(j+1,total,mask)
        a[j] = -(1-j+sum(bins[j][k]*a[k] for k in range(2,j))) % p
        visit(j+1,total+weights[j]*a[j],mask | (1 << (j-2)))
        a[j] = 0

    visit(2,0,0)
    emit(event="complete", visited=visited,
         f1_mod_p_squared_survivors_by_J=dict(sorted(histogram.items())),
         J18_Eisenstein_discarded=histogram[18],
         J17_noncenter_H2_discarded=len(discarded_j17),
         remaining_by_J=dict(sorted(remaining.items())),
         remaining_total=sum(remaining.values()),
         J17_remaining_center_masks=masks_j17,
         J17_discarded_center_masks=discarded_j17)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    args=parser.parse_args()
    if args.worker:
        worker()
        return
    command=[sys.executable,os.path.abspath(__file__),"--worker"]
    started=time.monotonic()
    child=subprocess.Popen(command)
    emit(event="child_started",pid=child.pid,command=command,timeout_seconds=30)
    try:
        code=child.wait(timeout=30)
    except subprocess.TimeoutExpired:
        child.kill()
        child.wait()
        emit(event="timeout",pid=child.pid)
        raise SystemExit(124)
    emit(event="child_finished",pid=child.pid,exit_code=code,
         elapsed_seconds=round(time.monotonic()-started,6))
    raise SystemExit(code)


if __name__=="__main__":
    main()
