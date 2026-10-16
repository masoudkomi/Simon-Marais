#!/usr/bin/env python3
"""Necessary mod-p center scenarios in degree 20, with rational-root filter.

This is evidence for a restricted necessary-condition calculation, never a
search over all rational polynomials. All arithmetic uses Python integers.
"""
import argparse
import collections
import json
import math
import os
import subprocess
import sys
import time


def report(**record):
    print(json.dumps(record, sort_keys=True), flush=True)


def worker():
    d, p = 20, 19
    final_j = d-2
    choose = [[math.comb(j,k) % p for k in range(j+1)]
              for j in range(d)]
    weights = {j:(math.comb(d,j)//p) % p for j in range(2,d-1)}
    assert all(math.comb(d,j) % p == 0 for j in weights)
    a = [0]*(d-1)
    a[0], a[1] = 1, -1
    visited, passed = 0, 0
    residues = collections.Counter()
    examples = {}
    report(event="checkpoint", pid=os.getpid(), degree=d, prime=p,
           patterns=2**(d-3), python=sys.version.split()[0],
           parameters="each j=2..18: witness1 or witness divisible19")

    def visit(j, total, center_indices):
        nonlocal visited, passed
        if j == d-1:
            visited += 1
            if total % p == 1:
                passed += 1
                residues[a[final_j]] += 1
                examples.setdefault(a[final_j], list(center_indices))
            if visited % 16384 == 0:
                report(event="checkpoint", visited=visited, passed=passed)
            return
        a[j] = 0
        visit(j+1, total, center_indices)
        center_value = -(1-j+sum(choose[j][k]*a[k]
                                for k in range(2,j))) % p
        a[j] = center_value
        visit(j+1, total+weights[j]*center_value, center_indices+(j,))
        a[j] = 0

    visit(2, 0, ())
    assert visited == 2**(d-3)
    report(event="complete", visited=visited,
           passed_f1_over_p_mod_p=passed,
           a18_residue_histogram=dict(sorted(residues.items())),
           discarded_by_rational_witness_eisenstein=sum(
               count for residue,count in residues.items() if residue != 0),
           remaining_necessary_patterns=residues[0],
           example_center_j_by_a18_residue=examples,
           scope="necessary mod19 conditions only; no emptiness proof")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    args = parser.parse_args()
    if args.worker:
        worker()
        return
    command = [sys.executable, os.path.abspath(__file__), "--worker"]
    started = time.monotonic()
    child = subprocess.Popen(command)
    report(event="child_started", pid=child.pid, command=command, timeout_seconds=30)
    try:
        code = child.wait(timeout=30)
    except subprocess.TimeoutExpired:
        child.kill()
        child.wait()
        report(event="timeout", pid=child.pid)
        raise SystemExit(124)
    report(event="child_finished", pid=child.pid, exit_code=code,
           elapsed_seconds=round(time.monotonic()-started, 6))
    raise SystemExit(code)


if __name__ == "__main__":
    main()
