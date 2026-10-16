#!/usr/bin/env python3
"""Exact finite evidence for 2025 B4(b), never an unrestricted proof.

The already known preliminary part (degree 3, odd q >= 3) is excluded.
Only this year's directory is written. No network or subprocess calls.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import flint
import sympy
from flint import fmpz
from sympy import perfect_power

HERE = Path(__file__).resolve().parent


def geometric_sum(x: int, n: int) -> int:
    s = 1
    for _ in range(n):
        s = s * x + 1
    return s


def solution_powers(value: int, degree: int) -> list[tuple[int, int]]:
    """Return all (y,q) for |value|>1; all arithmetic is exact."""
    magnitude = abs(value)
    if not fmpz(magnitude).is_perfect_power():
        return []
    b, e = perfect_power(magnitude, big=True)
    b, e = int(b), int(e)
    assert b**e == magnitude and b >= 2
    result = []
    for q in range(2, e + 1):
        if e % q or (degree == 3 and q % 2):
            continue
        if value < 0:
            if q % 2:
                result.append((-b ** (e // q), q))
        else:
            root = b ** (e // q)
            result.append((root, q))
            if q % 2 == 0:
                result.append((-root, q))
    for y, q in result:
        assert y**q == value
    return result


def valuation(v: int, p: int) -> int:
    assert v
    v = abs(v)
    result = 0
    while v % p == 0:
        result += 1
        v //= p
    return result


def elementary_checks() -> dict:
    counts = {"geometric_identity": 0, "gcd_with_x": 0,
              "gcd_with_x_minus_one": 0, "odd_prime_lte": 0,
              "two_adic_lte": 0, "sign": 0, "trivial_domain": 0,
              "degree_two_symmetry": 0, "independent_root_crosscheck": 0}
    primes = (3, 5, 7, 11, 13, 17, 19)
    # These are counterexample tests of written lemmas, not mathematical proofs.
    for x in range(-100, 101):
        for n in range(2, 101):
            m = n + 1
            s = geometric_sum(x, n)
            if x != 1:
                assert (x - 1) * s == x**m - 1
                counts["geometric_identity"] += 1
            assert math.gcd(s, x) == 1
            counts["gcd_with_x"] += 1
            assert math.gcd(s, x - 1) == math.gcd(m, x - 1)
            counts["gcd_with_x_minus_one"] += 1
            if abs(x) >= 2:
                assert abs(s) > 1
                assert (s < 0) == (x < 0 and n % 2 == 1)
                counts["sign"] += 1
            if x not in (-1, 1):
                for p in primes:
                    if (x - 1) % p == 0:
                        assert valuation(s, p) == valuation(m, p)
                        counts["odd_prime_lte"] += 1
                if x % 2 and m % 2 == 0:
                    assert valuation(s, 2) == valuation(x + 1, 2) + valuation(m, 2) - 1
                    counts["two_adic_lte"] += 1
            if x in (-1, 0, 1):
                expected = 1 if x == 0 else (m if x == 1 else (1 if n % 2 == 0 else 0))
                assert s == expected
                counts["trivial_domain"] += 1
        assert geometric_sum(x, 2) == geometric_sum(-x - 1, 2)
        counts["degree_two_symmetry"] += 1
    # Independent small-range check: enumerate every exponent using exact roots.
    # The preliminary degree-3 odd-exponent equation is excluded from both sides.
    for x in range(-25, 26):
        if abs(x) < 2:
            continue
        for n in range(2, 17):
            s = geometric_sum(x, n)
            brute = []
            for q in range(2, abs(s).bit_length()):
                if n == 3 and q % 2:
                    continue
                if s < 0 and q % 2 == 0:
                    continue
                root, exact = sympy.integer_nthroot(abs(s), q)
                if exact:
                    if s < 0:
                        brute.append((-int(root), q))
                    else:
                        brute.append((int(root), q))
                        if q % 2 == 0:
                            brute.append((-int(root), q))
            assert sorted(brute) == sorted(solution_powers(s, n))
            counts["independent_root_crosscheck"] += 1
    known = [(3, 11, 4, 2), (3, -11, 4, 2),
             (7, 20, 3, 2), (7, -20, 3, 2),
             (18, 7, 2, 3), (-19, 7, 2, 3)]
    for x, y, n, q in known:
        assert geometric_sum(x, n) == y**q
    # Audit a printed algebraic formula in Son 2026, Case 2, equation (6).
    a, b, rho = sympy.symbols("a b rho")
    reduced = sympy.rem(rho * (a + b*rho)**3, rho**2-rho-1, rho)
    constant = sympy.expand(reduced).coeff(rho, 0)
    coefficient = sympy.expand(reduced).coeff(rho, 1)
    printed = a**3 + 6*a*a*b + 9*a*b*b + 5*b**3
    difference = sympy.expand(printed - coefficient)
    assert difference != 0
    return {"ranges": {"x": [-100, 100], "degree": [2, 100]},
            "passed_counts": counts, "known_quadruples_checked": known,
            "son_theorem3_counterexample": {
                "x": -1, "y": 1, "term_count": 5, "degree": 4, "q": 3,
                "numerator": (-1)**5 - 1, "denominator": -1 - 1,
                "polynomial_value": geometric_sum(-1, 4),
                "rhs": 1**3, "quotient_defined": True},
            "son_case2_symbolic_audit": {
                "relation": "rho^2=rho+1", "expression": "rho*(a+b*rho)^3",
                "constant": str(constant), "rho_coefficient": str(coefficient),
                "printed_coefficient": str(printed), "printed_minus_correct": str(difference),
                "a_minus1_b1_correct_coefficient": int(coefficient.subs({a: -1, b: 1})),
                "a_minus1_b1_printed_coefficient": int(printed.subs({a: -1, b: 1})),
                "a_minus1_b1_constant": int(constant.subs({a: -1, b: 1}))}}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-abs-x", type=int, default=10000)
    parser.add_argument("--max-degree", type=int, default=128)
    parser.add_argument("--max-seconds", type=float, default=120)
    parser.add_argument("--output", default="initial-results.json")
    args = parser.parse_args()
    assert args.max_abs_x >= 2 and args.max_degree >= 2
    output = HERE / args.output
    assert output.resolve().is_relative_to(HERE)
    started = time.monotonic()
    metadata = {"status": "running", "purpose": "finite computational evidence only",
                "utc_started": datetime.now(timezone.utc).isoformat(),
                "command": " ".join(sys.argv),
                "python": platform.python_version(), "sympy": sympy.__version__,
                "python_flint": flint.__version__,
                "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                "parameters": vars(args),
                "scope": "2<=abs(x)<=X, 2<=degree<=N; all q>=2 by maximal perfect-power exponent",
                "excluded_preliminary": "degree=3 and odd q>=3 are never reported or independently investigated",
                "method": "FLINT exact perfect-power screen; SymPy maximal exponent; exact substitution of every hit",
                "elementary_counterexample_checks": elementary_checks(),
                "pairs_checked": 0, "perfect_power_magnitudes": 0,
                "last_completed_abs_x": 1, "solutions": []}
    stop = False
    for a in range(2, args.max_abs_x + 1):
        for x in (-a, a):
            s = 1
            for n in range(1, args.max_degree + 1):
                s = s*x + 1
                if n < 2:
                    continue
                # For degree 3, only the open square/even-exponent portion is screened.
                if n == 3:
                    if s > 1 and fmpz(s).is_square():
                        hits = solution_powers(s, n)
                        assert hits
                        metadata["perfect_power_magnitudes"] += 1
                        metadata["solutions"].extend([x, y, n, q] for y, q in hits)
                    metadata["pairs_checked"] += 1
                    continue
                hits = solution_powers(s, n)
                if hits:
                    metadata["perfect_power_magnitudes"] += 1
                    metadata["solutions"].extend([x, y, n, q] for y, q in hits)
                metadata["pairs_checked"] += 1
        metadata["last_completed_abs_x"] = a
        if a % 1000 == 0 or a == args.max_abs_x:
            metadata["elapsed_seconds"] = round(time.monotonic() - started, 6)
            output.write_text(json.dumps(metadata, indent=2) + "\n")
            print(f"checkpoint abs(x)<={a}; pairs={metadata['pairs_checked']}; elapsed={metadata['elapsed_seconds']}s", flush=True)
        if time.monotonic() - started > args.max_seconds:
            stop = True
            break
    metadata["status"] = "incomplete_time_limit" if stop else "complete"
    metadata["solutions"] = sorted(metadata["solutions"])
    metadata["utc_finished"] = datetime.now(timezone.utc).isoformat()
    metadata["elapsed_seconds"] = round(time.monotonic() - started, 6)
    output.write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps({k: metadata[k] for k in ("status", "last_completed_abs_x", "pairs_checked", "elapsed_seconds", "solutions")}, indent=2))


if __name__ == "__main__":
    main()
