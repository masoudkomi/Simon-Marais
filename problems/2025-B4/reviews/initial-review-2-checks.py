#!/usr/bin/env python3
"""Independent finite evidence for P2025-v1; never an unrestricted proof.

Run only through initial-review-2-run.py, which records the child PID and timeout.
No scan of the preliminary degree-three odd-exponent problem is performed.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
DEST = Path(__file__).with_name("initial-review-2-results.json")
start = time.monotonic()
result = {
    "evidence_only": True,
    "pid": os.getpid(),
    "python": sys.version,
    "platform": platform.platform(),
    "dependencies": "Python standard library only",
    "proof_sha256": hashlib.sha256((ROOT / "problems/2025-B4/proof.md").read_bytes()).hexdigest(),
    "checkpoints": [],
}

def checkpoint(name, **data):
    row = {"name": name, "elapsed_seconds": time.monotonic() - start, **data}
    result["checkpoints"].append(row)
    DEST.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(row), flush=True)

def geometric(x, m):
    # Horner evaluation avoids dividing by x-1 at boundary values.
    value = 0
    for _ in range(m):
        value = value * x + 1
    return value

def valuation(a, p):
    a = abs(a)
    assert a != 0
    count = 0
    while a % p == 0:
        a //= p
        count += 1
    return count

def exact_positive_root(a, q):
    assert a >= 0 and q >= 2
    if a <= 1:
        return a
    low, high = 0, 1 << ((a.bit_length() + q - 1) // q)
    while low <= high:
        middle = (low + high) // 2
        power = middle ** q
        if power == a:
            return middle
        if power < a:
            low = middle + 1
        else:
            high = middle - 1
    return None

checkpoint("start", policy="skip n=3 odd q in nontrivial perfect-power enumeration")

boundary_cases = 0
for x in [-1, 0, 1]:
    for n in range(2, 33):
        value = geometric(x, n + 1)
        for q in range(2, 13):
            actual = [y for y in range(-40, 41) if y ** q == value]
            if x == 0 or (x == -1 and n % 2 == 0):
                expected = [-1, 1] if q % 2 == 0 else [1]
            elif x == -1:
                expected = [0]
            else:
                root = exact_positive_root(n + 1, q)
                expected = ([] if root is None else
                            ([-root, root] if q % 2 == 0 else [root]))
            assert actual == expected, (x, n, q, actual, expected)
            boundary_cases += 1

sign_cases = 0
gcd_cases = 0
odd_lte_cases = 0
two_lte_cases = 0
primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
for x in range(-120, 121):
    for m in range(3, 73):
        value = geometric(x, m)
        assert math.gcd(value, x) == 1, (x, m)
        assert math.gcd(value, x - 1) == math.gcd(m, x - 1), (x, m)
        gcd_cases += 1
        if abs(x) < 2:
            continue
        assert abs(value) > 1
        assert (value < 0) == (x < 0 and m % 2 == 0)
        sign_cases += 1
        for p in primes:
            if (x - 1) % p == 0:
                assert valuation(value, p) == valuation(m, p), (x, m, p)
                odd_lte_cases += 1
        if x % 2 and m % 2 == 0:
            assert valuation(value, 2) == valuation(x + 1, 2) + valuation(m, 2) - 1, (x, m)
            two_lte_cases += 1
        else:
            assert value % 2 == 1, (x, m)
checkpoint("C1-C2", boundary_triples=boundary_cases, boundary_root_scan=[-40, 40],
           boundary_n=[2, 32], boundary_q=[2, 12], gcd_pairs=gcd_cases,
           sign_pairs=sign_cases, x=[-120, 120], term_count=[3, 72],
           odd_lte_checks=odd_lte_cases, odd_primes=primes, two_lte_checks=two_lte_cases)

square_cases = 0
for x in range(-2000, 2001):
    value = geometric(x, 3)
    is_square = math.isqrt(value) ** 2 == value
    assert is_square == (x in [-1, 0]), x
    if x not in [-1, 0]:
        t = max(x, -x - 1)
        assert t >= 1
        assert t * t < value < (t + 1) ** 2
    square_cases += 1
checkpoint("C3", x=[-2000, 2000], square_checks=square_cases)

factor_cases = 0
zero_cases = 0
for x in range(-80, 81):
    sums = [0] + [geometric(x, m) for m in range(1, 145)]
    for r in range(1, 13):
        for s in range(1, 13):
            if r * s < 3:
                continue
            left = sums[r]
            right = geometric(x ** r, s)
            assert sums[r * s] == left * right, (x, r, s)
            assert math.gcd(left, right) == math.gcd(left, s), (x, r, s)
            if left == 0 or right == 0:
                zero_cases += 1
            if abs(x) >= 2:
                assert left != 0 and right != 0
            factor_cases += 1
checkpoint("C4-factorization", x=[-80, 80], r=[1, 12], s=[1, 12],
           restricted_to="r*s>=3", factorization_gcd_checks=factor_cases,
           zero_factor_cases=zero_cases)

hits = []
root_checks = 0
factor_power_cases = 0
reduction_cases = 0
screened_pairs = 0
for x in list(range(-60, -1)) + list(range(2, 61)):
    for n in range(2, 21):
        m = n + 1
        value = geometric(x, m)
        screened_pairs += 1
        for q in range(2, abs(value).bit_length()):
            if n == 3 and q % 2:
                continue
            if value < 0 and q % 2 == 0:
                continue
            root_checks += 1
            root = exact_positive_root(abs(value), q)
            if root is None:
                continue
            ys = ([-root] if value < 0 else
                  ([-root, root] if q % 2 == 0 else [root]))
            for y in ys:
                assert y ** q == value
                hits.append([x, y, n, q])
                for ell in range(2, q + 1):
                    if q % ell != 0 or any(ell % d == 0 for d in range(2, math.isqrt(ell) + 1)):
                        continue
                    assert (y ** (q // ell)) ** ell == value
                    reduction_cases += 1
            for r in range(1, m + 1):
                if m % r:
                    continue
                s = m // r
                A, B = geometric(x, r), geometric(x ** r, s)
                if math.gcd(A, B) == 1:
                    assert exact_positive_root(abs(A), q) is not None
                    assert exact_positive_root(abs(B), q) is not None
                    factor_power_cases += 1
expected_hits = [[-19, 7, 2, 3], [3, -11, 4, 2], [3, 11, 4, 2],
                 [7, -20, 3, 2], [7, 20, 3, 2], [18, 7, 2, 3]]
assert hits == expected_hits, hits
checkpoint("independent-small-search", x_negative=[-60, -2], x_positive=[2, 60],
           official_degree=[2, 20], q="all q with 2<=q<bit_length(abs(G)); no y bound",
           preliminary_exclusion="n=3 odd q skipped", pairs=screened_pairs,
           exact_root_checks=root_checks, hits=hits, prime_exponent_checks=reduction_cases,
           coprime_factor_power_checks=factor_power_cases)

# Exact arithmetic in Z[rho], rho^2=rho+1. Multiplication of coefficient pairs.
def ring_mul(v, w):
    a, b = v
    c, d = w
    return (a*c+b*d, a*d+b*c+b*d)

son_checks = 0
for a in range(-10, 11):
    for b in range(-10, 11):
        cube = ring_mul(ring_mul((a, b), (a, b)), (a, b))
        rho_cube = ring_mul((0, 1), cube)
        correct = (3*a*a*b + 3*a*b*b + 2*b**3,
                   a**3 + 3*a*a*b + 6*a*b*b + 3*b**3)
        assert rho_cube == correct
        son_checks += 1
witness = ring_mul((0, 1), ring_mul(ring_mul((-1, 1), (-1, 1)), (-1, 1)))
printed_rho_coefficient = (-1)**3 + 6*(-1)**2 + 9*(-1) + 5
assert witness == (2, -1)
assert printed_rho_coefficient == 1
assert geometric(-1, 5) == 1
checkpoint("Son-paper-algebra", parameter_pairs=son_checks, a=[-10, 10], b=[-10, 10],
           witness={"a": -1, "b": 1, "rho_cube_pair": witness,
                    "printed_rho_coefficient": printed_rho_coefficient,
                    "x": -1, "y": 1, "term_count": 5, "G": geometric(-1, 5)})

# Wang's equality compared after squaring positive radical terms, all rational.
# This tests an algebraic substitution, not a counterexample to its abc theorem.
wang_samples = []
for T in [36, 40, 144, 10000]:
    c = T + 1
    true_square = c * T  # (sqrt(c)/rho)^2 with rho=1/sqrt(T)
    printed_square_numerator, printed_square_denominator = c, T
    assert true_square * printed_square_denominator != printed_square_numerator
    assert true_square * T == c * T * T
    wang_samples.append({"T": T, "c": c, "true_term_squared": true_square,
                         "printed_term_squared": f"{c}/{T}", "missing_factor": T})
checkpoint("Wang-paper-algebra", samples=wang_samples,
           interpretation="identity-only diagnostic; no ABC triple or conjecture counterexample asserted")
result["completed"] = True
checkpoint("complete", assertions_failed=0)
