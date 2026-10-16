#!/usr/bin/env python3
"""Independent finite evidence for the v0.1 candidate; not a general proof.

Only Python's standard library is used. The resultant is computed from a
Sylvester determinant by a subset expansion, independently of the constructor's
CAS checks. All arithmetic is exact. Run this file with no arguments to launch
the worker with an explicit 55-second timeout and preserve a checkpoint log.
"""
from __future__ import annotations

import functools
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
CANDIDATE = HERE.parent / "notes" / "candidate-resultant-v0.1.md"
EXPECTED_SHA256 = "77d209d6a35ebf96a72d5d3a29f9f23d8f7456adae01d1572c180cf842c05365"
PAIRS = [(4, 3), (6, 5), (8, 3), (8, 5), (8, 7), (10, 3), (10, 7), (10, 9)]

# Sparse polynomials in D,N: {(exponent_D, exponent_N): integer coefficient}.
ZERO = {}
ONE = {(0, 0): 1}


def add(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, 0) + v
        if not c[k]:
            del c[k]
    return c


def mul(a, b):
    c = {}
    for (i, j), v in a.items():
        for (k, h), w in b.items():
            key = (i + k, j + h)
            c[key] = c.get(key, 0) + v * w
    return {k: v for k, v in c.items() if v}


def scale(a, k):
    return {ij: v * k for ij, v in a.items() if v * k}


# Polynomials in P are low-coefficient-first lists of sparse D,N polynomials.
def padd(a, b):
    return [add(a[i] if i < len(a) else ZERO,
                b[i] if i < len(b) else ZERO)
            for i in range(max(len(a), len(b)))]


def pmul(a, b):
    c = [ZERO for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] = add(c[i + j], mul(ai, bj))
    return c


def recurrence(limit):
    f = [[ZERO], [ONE]]
    for _ in range(2, limit + 1):
        f.append(padd([mul({(1, 0): 1}, c) for c in f[-1]],
                      [ZERO] + f[-2]))
    for p in f:
        while len(p) > 1 and not p[-1]:
            p.pop()
    return f


def resultant(a, b):
    m, n = len(a) - 1, len(b) - 1
    size = m + n
    matrix = []
    for shift in range(n):
        matrix.append([ZERO] * shift + list(reversed(a)) + [ZERO] * (n - shift - 1))
    for shift in range(m):
        matrix.append([ZERO] * shift + list(reversed(b)) + [ZERO] * (m - shift - 1))

    @functools.lru_cache(None)
    def determinant(mask):
        row = mask.bit_count()
        if row == size:
            return ONE
        answer = ZERO
        for col in range(size):
            if mask & (1 << col) or not matrix[row][col]:
                continue
            # Prior selected columns > col contribute permutation inversions.
            sign = -1 if (mask >> (col + 1)).bit_count() % 2 else 1
            term = mul(matrix[row][col], determinant(mask | (1 << col)))
            answer = add(answer, scale(term, sign))
        return answer

    return determinant(0)


def worker():
    print(json.dumps({"pid": os.getpid(), "python": sys.version,
                      "timeout_seconds": 55, "symbolic_pairs": PAIRS,
                      "modular_range": {"e_max": 256, "q_max": 8}}), flush=True)
    actual_hash = hashlib.sha256(CANDIDATE.read_bytes()).hexdigest()
    assert actual_hash == EXPECTED_SHA256, actual_hash
    print("candidate_sha256=" + actual_hash, flush=True)
    f = recurrence(10)
    for e, o in PAIRS:
        start = time.monotonic()
        de, do = (e - 2) // 2, (o - 1) // 2
        assert len(f[e]) - 1 == de and len(f[o]) - 1 == do
        assert f[e][-1] == {(1, 0): e // 2} and f[o][-1] == ONE
        unit = resultant(f[e], f[o])
        unit_expected = {((e - 1) * (o - 1) // 2, 0): 1}
        assert unit in (unit_expected, scale(unit_expected, -1)), (e, o, unit)
        a = padd(f[e], [scale(c, -1) for c in f[o]])
        b = pmul([{(2, 0): 1}, {(0, 0): 4}], pmul(f[o], f[o]))
        b[0] = add(b[0], {(0, 1): -4})
        r = resultant(a, b)
        limit = o * (e - 1)
        assert r and max(i + 2 * o * j for i, j in r) <= limit
        constant = {(i, 0): c for (i, j), c in r.items() if j == 0}
        base, delta = e * (o - 1), e - o
        expected = {(base + delta, 0): e // 2,
                    (base, 0): -(2 ** (delta - 1)) * o}
        assert constant in (expected, scale(expected, -1)), (e, o, constant)
        if (e, o) == (4, 3):
            # A degree drops at D=1/2; generic resultant still has the required
            # common-finite-root implication and need not vanish by the drop.
            from fractions import Fraction
            specialized = sum(Fraction(c, 2 ** i) for (i, j), c in r.items() if j == 0)
            assert abs(specialized) == Fraction(1, 128)
            print("degree_drop_e4_o3_D1/2_N0=" + str(specialized), flush=True)
        print(json.dumps({"symbolic_pair": [e, o], "unit_terms": len(unit),
                          "R_terms": len(r), "max_weight": max(i + 2 * o * j for i, j in r),
                          "L": limit, "elapsed_seconds": round(time.monotonic() - start, 4),
                          "status": "passed"}), flush=True)

    counts = {"triples_checked": 0, "delta_lt_2o_divisibility_survivors": 0,
              "delta_ge_2o_divisibility_survivors": 0,
              "combined_real_inequality_survivors": 0}
    first_survivors = []
    for e in range(4, 257, 2):
        for o in range(3, e, 2):
            if math.gcd(e, o) != 1:
                continue
            delta = e - o
            for q in range(2, 9):
                modulus = q ** (2 * o)
                for p in range(1, q):
                    if math.gcd(p, q) != 1:
                        continue
                    counts["triples_checked"] += 1
                    hmod = ((e // 2) * pow(p, delta, modulus)
                            - pow(2, delta - 1, modulus) * o * pow(q, delta, modulus)) % modulus
                    if hmod:
                        continue
                    if delta < 2 * o:
                        counts["delta_lt_2o_divisibility_survivors"] += 1
                    else:
                        counts["delta_ge_2o_divisibility_survivors"] += 1
                        if len(first_survivors) < 12:
                            first_survivors.append([e, o, p, q])
                        assert (e // 2) % modulus == 0
                        # The proof's derived real inequality (20).
                        if e > 2 ** (e - 3 * o):
                            counts["combined_real_inequality_survivors"] += 1
        if e % 64 == 0:
            print(json.dumps({"modular_checkpoint_e": e, **counts}), flush=True)
    assert counts["delta_lt_2o_divisibility_survivors"] == 0
    assert counts["combined_real_inequality_survivors"] == 0
    print(json.dumps({"modular_final": counts, "first_arithmetic_survivors": first_survivors}), flush=True)
    print("COMPLETED: finite evidence only; no unrestricted theorem inferred from enumeration.", flush=True)


def main():
    if sys.argv[1:] == ["--worker"]:
        worker()
        return
    if sys.argv[1:]:
        raise SystemExit("usage: review-1-checks.py [--worker]")
    output = HERE / "review-1-checks.log"
    with output.open("w") as log:
        child = subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "--worker"],
                                 stdout=log, stderr=subprocess.STDOUT)
        print(json.dumps({"child_pid": child.pid, "timeout_seconds": 55,
                          "log": str(output)}), flush=True)
        try:
            returncode = child.wait(timeout=55)
        except subprocess.TimeoutExpired:
            child.terminate()
            try:
                child.wait(timeout=2)
            except subprocess.TimeoutExpired:
                child.kill()
                child.wait(timeout=2)
            print("TIMEOUT: terminated only child pid " + str(child.pid), flush=True)
            raise SystemExit(124)
    print(output.read_text(), end="")
    raise SystemExit(returncode)


if __name__ == "__main__":
    main()
