#!/usr/bin/env python3
"""Blind R1 reproduction of the d=20 necessary filter, standard library only.

This implementation was written before reading the candidate author's script.
The child enumerates a binary tree, retaining exact integer Appell coefficients
instead of reducing them during the recursion. It tests f(1) modulo 19**2.
The parent supplies a real subprocess timeout and records the child PID.
"""
import collections
import hashlib
import json
import math
import os
import platform
import subprocess
import sys
import time


def emit(event, **values):
    print(json.dumps({"event": event, **values}, sort_keys=True), flush=True)


def child():
    p, d = 19, 20
    choose = [[math.comb(j, k) for k in range(j + 1)] for j in range(d + 1)]
    assert all(choose[d][j] % p == 0 and choose[d][j] % (p * p) != 0
               for j in range(2, d - 1))
    residues = [choose[d][j] // p % p for j in range(2, d - 1)]
    emit("parameters", p=p, d=d, choices=list(range(2, d - 1)),
         patterns=2 ** (d - 3), binomial_quotient_residues=residues,
         test="exact integer f(1) divisible by p**2",
         normalized_monic_derivative="P_j=sum_k binom(j,k) a_k x**(j-k)")
    a = [1, -1] + [0] * (d - 3)
    histogram = collections.Counter()
    visited = 0
    passing = []
    samples = {"a18_zero": [], "a18_nonzero": []}

    def visit(j, mask, f_one):
        nonlocal visited
        if j == d - 1:
            visited += 1
            assert f_one % p == 0
            # This integer equation uses the full binomial coefficients.
            if f_one % (p * p) == 0:
                last = a[d - 2] % p
                histogram[last] += 1
                passing.append((mask, last))
                key = "a18_zero" if last == 0 else "a18_nonzero"
                if len(samples[key]) < 3:
                    samples[key].append({"mask": mask,
                                         "center_indices": [k for k in range(2, d - 1)
                                                            if mask & (1 << (k - 2))],
                                         "a_mod_p": [v % p for v in a],
                                         "f_one": f_one})
            if visited % 16384 == 0:
                emit("checkpoint", visited=visited, passing=len(passing))
            return

        # A non-center rational witness is 0 modulo p. For the exact binary
        # specialization used only in this count, its witness is literally 0.
        a[j] = 0
        visit(j + 1, mask, f_one)
        # The monic derivative P_j must vanish at its selected center, 1.
        a[j] = -sum(choose[j][k] * a[k] for k in range(j))
        assert sum(choose[j][k] * a[k] for k in range(j + 1)) == 0
        visit(j + 1, mask | (1 << (j - 2)), f_one + choose[d][j] * a[j])
        a[j] = 0

    visit(2, 0, 1 - d)
    canonical = "".join(f"{m}:{r}\n" for m, r in sorted(passing)).encode("ascii")
    emit("result", visited=visited, passing=len(passing),
         rejected=visited - len(passing), a18_zero=histogram[0],
         a18_nonzero=len(passing) - histogram[0],
         a18_residue_histogram={str(k): histogram[k] for k in range(p)},
         canonical_survivor_mask_residue_sha256=hashlib.sha256(canonical).hexdigest(),
         samples=samples)
    assert visited == 131072
    assert len(passing) == 6680
    assert histogram[0] == 3637
    assert len(passing) - histogram[0] == 3043
    emit("assertions", status="all passed; necessary filter only, no lifting or classification")


if __name__ == "__main__":
    if sys.argv[1:] == ["--child"]:
        child()
    else:
        started = time.monotonic()
        command = [sys.executable, os.path.abspath(__file__), "--child"]
        emit("launch", parent_pid=os.getpid(), timeout_seconds=30,
             python=platform.python_version(), command=command,
             source_sha256=hashlib.sha256(open(__file__, "rb").read()).hexdigest())
        process = subprocess.Popen(command)
        emit("child", pid=process.pid)
        try:
            returncode = process.wait(timeout=30)
        except subprocess.TimeoutExpired:
            emit("timeout", pid=process.pid, action="terminate this child only")
            process.terminate()
            try:
                returncode = process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
                returncode = process.wait(timeout=2)
            emit("completion", returncode=returncode, timed_out=True,
                 seconds=time.monotonic() - started)
            raise SystemExit(124)
        emit("completion", returncode=returncode, timed_out=False,
             seconds=time.monotonic() - started)
        raise SystemExit(returncode)
