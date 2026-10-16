#!/usr/bin/env python3
"""Independent exact finite evidence for P2025-v1; not an unrestricted proof.

The degree-3 odd-exponent preliminary slice is excluded from solution searches.
Pure Python standard library; run only through initial-review-1-run.py.
"""
from __future__ import annotations

import hashlib
import json
import math
import platform
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
COUNTS = Counter()
START = time.monotonic()
RESULT = {"status": "running", "purpose": "finite evidence only", "python": platform.python_version(),
          "dependencies": "Python standard library only", "started_utc": datetime.now(timezone.utc).isoformat(),
          "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "excluded_solution_slice": "degree=3 and odd q>=3"}


def g(x, m):
    return sum(x**k for k in range(m))


def vp(value, p):
    assert value != 0
    value = abs(value)
    e = 0
    while value % p == 0:
        value //= p
        e += 1
    return e


def checkpoint(stage):
    RESULT.update(stage=stage, counts=dict(COUNTS), elapsed_seconds=round(time.monotonic() - START, 6))
    (HERE / "initial-review-1-evidence.json").write_text(json.dumps(RESULT, indent=2) + "\n")
    print(json.dumps({"stage": stage, "elapsed_seconds": RESULT["elapsed_seconds"], "counts": dict(COUNTS)}), flush=True)


def root_exact(value, exponent):
    """Binary integer root, independent of FLINT/SymPy perfect-power routines."""
    assert value >= 0 and exponent >= 2
    low, high = 0, 1 << ((value.bit_length() + exponent - 1) // exponent)
    while low <= high:
        mid = (low + high) // 2
        power = mid**exponent
        if power == value:
            return mid, True
        if power < value:
            low = mid + 1
        else:
            high = mid - 1
    return high, False


def qring_mul(a, b):
    c, d = a
    e, f = b
    return (c*e + d*f, c*f + d*e + d*f)


def main():
    RESULT["parameters"] = {
        "C1_boundary": {"x": [-1, 0, 1], "degree": [2, 80], "q": [2, 12], "y": [-30, 30]},
        "C1_C2": {"x": [-96, 96], "term_count": [3, 80], "odd_primes": [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]},
        "C3": {"x": [-1000, 1000]},
        "C4": {"x": [-35, 35], "r": [1, 15], "s": [1, 15]},
        "solution_search": {"max_abs_x": 60, "degree": [2, 32], "q": "all possible q>=2 by abs(G).bit_length()-1"},
        "son_ring_coefficients": {"a": [-12, 12], "b": [-12, 12]}}
    checkpoint("start")
    for x in (-1, 0, 1):
        for n in range(2, 81):
            value = g(x, n+1)
            for q in range(2, 13):
                for y in range(-30, 31):
                    if n == 3 and q % 2:
                        COUNTS["boundary_preliminary_slice_skipped"] += 1
                        continue
                    if x == 0 or (x == -1 and n % 2 == 0):
                        expected = y == 1 or (y == -1 and q % 2 == 0)
                    elif x == -1:
                        expected = y == 0
                    else:
                        expected = abs(y) >= 2 and n == abs(y)**q-1 and (y > 0 or q % 2 == 0)
                    assert (value == y**q) == expected, (x, y, n, q, value)
                    COUNTS["boundary_quadruples"] += 1
    checkpoint("C1_boundary")
    primes = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
    for x in range(-96, 97):
        for m in range(3, 81):
            value = g(x, m)
            assert (x-1)*value == x**m-1
            assert math.gcd(value, x) == 1
            assert math.gcd(value, x-1) == math.gcd(m, x-1)
            COUNTS["gcd_and_identity_pairs"] += 1
            if abs(x) < 2:
                continue
            assert abs(value) > 1
            assert (value < 0) == (x < -1 and (m-1) % 2 == 1)
            COUNTS["nonboundary_sign_pairs"] += 1
            for p in primes:
                if (x-1) % p == 0:
                    assert vp(value, p) == vp(m, p)
                    COUNTS["odd_prime_LTE"] += 1
            if x % 2 and m % 2 == 0:
                assert vp(value, 2) == vp(x+1, 2) + vp(m, 2)-1
                COUNTS["two_adic_LTE"] += 1
            else:
                assert value % 2
                COUNTS["parity_odd"] += 1
    checkpoint("C1_C2")
    for x in range(-1000, 1001):
        value = g(x, 3)
        assert value == g(-x-1, 3)
        if x not in (-1, 0):
            t = max(x, -x-1)
            assert t >= 1 and t*t < value < (t+1)**2
            assert math.isqrt(value)**2 != value
            COUNTS["C3_nonsquares"] += 1
    checkpoint("C3")
    for x in range(-35, 36):
        for r in range(1, 16):
            a = g(x, r)
            for s in range(1, 16):
                b = g(x**r, s)
                assert g(x, r*s) == a*b
                assert math.gcd(a, b) == math.gcd(a, s)
                COUNTS["C4_factor_gcd_triples"] += 1
                if a == 0 or b == 0:
                    COUNTS["C4_zero_factor_triples"] += 1
                if abs(x) >= 2:
                    assert a and b
                    COUNTS["C4_nonzero_nonboundary_triples"] += 1
    for y in range(-20, 21):
        for q in range(2, 21):
            for ell in (2, 3, 5, 7, 11, 13, 17, 19):
                if q % ell == 0:
                    assert (y**(q//ell))**ell == y**q
                    COUNTS["C4_exponent_reductions"] += 1
    checkpoint("C4")
    hits = []
    for a in range(2, 61):
        for x in (-a, a):
            for n in range(2, 33):
                value = g(x, n+1)
                for q in range(2, abs(value).bit_length()):
                    if n == 3 and q % 2:
                        continue
                    if value < 0 and q % 2 == 0:
                        continue
                    root, exact = root_exact(abs(value), q)
                    COUNTS["independent_exact_root_tests"] += 1
                    if exact:
                        ys = (-root,) if value < 0 else ((root, -root) if q % 2 == 0 else (root,))
                        for y in ys:
                            assert y**q == value
                            hits.append([x, y, n, q])
                COUNTS["independent_solution_pairs"] += 1
        if a % 10 == 0:
            RESULT["last_completed_abs_x"] = a
            checkpoint("independent_roots")
    expected = [[-19, 7, 2, 3], [3, -11, 4, 2], [3, 11, 4, 2], [7, -20, 3, 2], [7, 20, 3, 2], [18, 7, 2, 3]]
    assert sorted(hits) == expected
    RESULT["solutions_in_finite_range"] = sorted(hits)
    assert g(-1, 5) == 1
    for a in range(-12, 13):
        for b in range(-12, 13):
            z = (a, b)
            actual = qring_mul((0, 1), qring_mul(qring_mul(z, z), z))
            expected_ring = (3*a*a*b + 3*a*b*b + 2*b**3, a**3 + 3*a*a*b + 6*a*b*b + 3*b**3)
            assert actual == expected_ring
            COUNTS["son_ring_exact_tests"] += 1
    special = qring_mul((0, 1), qring_mul(qring_mul((-1, 1), (-1, 1)), (-1, 1)))
    assert special == (2, -1)
    RESULT["son"] = {"boundary_counterexample": {"x": -1, "y": 1, "degree": 4, "term_count": 5, "q": 3},
                     "correct_rho_coefficient": "a^3+3*a^2*b+6*a*b^2+3*b^3",
                     "printed_rho_coefficient": "a^3+6*a^2*b+9*a*b^2+5*b^3",
                     "a_minus1_b1_ring_value": list(special), "printed_coefficient_at_same_pair": 1}
    t = Fraction(64)
    c = Fraction(65)
    RESULT["wang_eq33_identity_check"] = {"T": str(t), "c": str(c), "rho": "1/8",
        "correct_expression_squared": str(c*t), "printed_expression_squared": str(c/t),
        "square_ratio": str((c*t)/(c/t)), "general_correction": "sqrt(c)/rho = T*sqrt(c/T), rho=1/sqrt(T)"}
    RESULT.update(status="complete", finished_utc=datetime.now(timezone.utc).isoformat(), substantive_counterexamples=[])
    checkpoint("complete")


if __name__ == "__main__":
    main()
