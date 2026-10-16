#!/usr/bin/env python3
"""Blind reviewer R1 checks for the frozen 2024 B4(b) family, v1.

This script was written without reading the constructor's certificate code
or either independent review. It uses only Python's standard library.
In particular, K^15 is expanded by the INTEGER MULTINOMIAL THEOREM over
all five-term compositions, followed by reduction modulo two. It does
not use repeated K multiplication or its binary/Frobenius factorization.

The symbolic identities checked here are finite identities over a
Laurent polynomial ring, with indeterminate b; they are not parameter
sampling. The separate bounded recurrence checks are only evidence.
The unrestricted m argument is audited in the accompanying report.
"""

from collections import defaultdict
from datetime import datetime, timezone
from functools import reduce
from itertools import combinations
from math import factorial
import hashlib
import json
from pathlib import Path
import sys
import time


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).with_name("family-review-1-independent-check.json")
START = time.monotonic()
RESULT = {
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "python": sys.version,
    "dependencies": "Python standard library only; no native CAS",
    "requested_settings": {"model": "gpt-6.1-sol", "reasoning": "max"},
    "verified_effective_settings": None,
    "independence": "No constructor script or other review read before this check",
    "proof_sha256": hashlib.sha256(
        (ROOT / "problems/2024-B4/proofs/fixed-factor-family-v1.md").read_bytes()
    ).hexdigest(),
}


def checkpoint(message):
    print(f"{time.monotonic()-START:.3f}s {message}", flush=True)


def xor(*polys):
    out = set()
    for poly in polys:
        out.symmetric_difference_update(poly)
    return out


def product(a, b):
    """Sparse exact multiplication in F2[variables]."""
    out = set()
    for ma in a:
        for mb in b:
            m = tuple(x + y for x, y in zip(ma, mb))
            if m in out:
                out.remove(m)
            else:
                out.add(m)
    return out


def power(a, k):
    if k < 0:
        raise ValueError(k)
    nvars = len(next(iter(a)))
    out = {(0,) * nvars}
    for _ in range(k):
        out = product(out, a)
    return out


def shift(a, monomial):
    return {tuple(x + y for x, y in zip(m, monomial)) for m in a}


def exact_divide(dividend, divisor):
    """Single-divisor lexicographic long division, halting on an obstruction."""
    leading = max(divisor)
    remainder = set(dividend)
    quotient = set()
    steps = 0
    while remainder:
        lead = max(remainder)
        if any(a < b for a, b in zip(lead, leading)):
            raise AssertionError({"nonzero_remainder_leading_term": lead})
        delta = tuple(a - b for a, b in zip(lead, leading))
        quotient.add(delta)
        remainder.symmetric_difference_update(shift(divisor, delta))
        steps += 1
        if steps > 100000:
            raise RuntimeError("Bounded exact division exceeded 100000 steps")
    assert product(quotient, divisor) == dividend
    return quotient, steps


def laurent_shift(exponents, amount):
    return {e + amount for e in exponents}


def laurent_repr(exponents):
    return sorted(exponents)


def select_times_numerator(h, numerator, residue):
    # h and numerator have monomials (z exponent, b exponent).
    accum = set()
    for zh, bh in h:
        for zn, bn in numerator:
            z, b = zh + zn, bh + bn
            if z % 16 == residue:
                monomial = ((z - residue) // 16, b)
                if monomial in accum:
                    accum.remove(monomial)
                else:
                    accum.add(monomial)
    coefficients = defaultdict(set)
    for z, b in accum:
        coefficients[z].add(b)
    return [coefficients[i] for i in range(4)], accum


# Exact K^15 expansion. Five terms, exponents (z,b):
# 1, z^2, b*z^3, b^(-1)*z^3, b^2*z^4.
h = set()
composition_count = 0
odd_multinomial_count = 0
for a in range(16):
    for bb in range(16 - a):
        for c in range(16 - a - bb):
            for d in range(16 - a - bb - c):
                e = 15 - a - bb - c - d
                multinomial = factorial(15) // (
                    factorial(a) * factorial(bb) * factorial(c)
                    * factorial(d) * factorial(e)
                )
                composition_count += 1
                if multinomial % 2:
                    odd_multinomial_count += 1
                    monomial = (2 * bb + 3 * c + 3 * d + 4 * e,
                                c - d + 2 * e)
                    if monomial in h:
                        h.remove(monomial)
                    else:
                        h.add(monomial)
assert composition_count == 3876
L = {-7, -5, -3, -1, 1, 3, 5, 7}
M = {-6, -4, -2, 0, 2, 6, 8}
J = {-12, -6, -4, -2, 0, 2, 4, 6, 8}
assert J == xor(M, {4, -12})
identities = [
    ("(9)", {(0, 0), (1, 0), (2, 1)}, 5,
     [set(), xor(L, M), xor(L, J), laurent_shift(xor(L, J), 16)]),
    ("(10)", {(1, 0)}, 6,
     [set(), L, L, laurent_shift(L, 16)]),
    ("(11)", {(2, 0), (3, 1)}, 6,
     [set(), M, J, laurent_shift(J, 16)]),
]
identity_results = []
for label, numerator, residue, expected in identities:
    actual, monomials = select_times_numerator(h, numerator, residue)
    assert actual == expected, label
    assert all(0 <= z <= 3 for z, b in monomials)
    identity_results.append({
        "label": label,
        "residue": residue,
        "numerator": sorted(numerator),
        "actual_coefficients_as_b_exponents": list(map(laurent_repr, actual)),
        "expected_coefficients_as_b_exponents": list(map(laurent_repr, expected)),
        "exact_laurent_identity_pass": True,
    })
RESULT["cartier_symbolic"] = {
    "method": "integer five-term multinomial expansion, then parity reduction",
    "compositions": composition_count,
    "odd_multinomial_count": odd_multinomial_count,
    "K15_monomial_count": len(h),
    "K15_monomials_z_b": sorted(h),
    "identities": identity_results,
}
checkpoint("all three full Laurent-polynomial Cartier identities pass")


# The coefficient field scalar is not subjected to Frobenius. This gives
# a concrete symbolic discriminator: C6(b*z/K)=b*C6(z/K), and replacing
# b by b^16 as an external scalar would yield a different nonzero series.
scaled_actual, _ = select_times_numerator(h, {(1, 1)}, 6)
scaled_expected = [set(), laurent_shift(L, 1), laurent_shift(L, 1),
                   laurent_shift(L, 17)]
wrong_scalar = [set(), laurent_shift(L, 16), laurent_shift(L, 16),
                laurent_shift(L, 32)]
assert scaled_actual == scaled_expected
assert scaled_actual != wrong_scalar
RESULT["scalar_discriminator"] = {
    "correct_external_scalar": "b",
    "incorrect_external_scalar": "b^16",
    "symbolically_distinguished": True,
}


# Direct recurrence from K*F=1+z+b*z^2, over F2[b,b^-1].
# These checks are deliberately labelled bounded evidence, not induction.
limit = 1637
series = []
for j in range(limit + 1):
    value = ({0} if j in (0, 1) else {1} if j == 2 else set())
    if j >= 2:
        value = xor(value, series[j - 2])
    if j >= 3:
        value = xor(value, laurent_shift(series[j - 3], 1),
                    laurent_shift(series[j - 3], -1))
    if j >= 4:
        value = xor(value, laurent_shift(series[j - 4], 2))
    series.append(value)
    if j in (5, 101, 1637):
        assert not value
        checkpoint(f"bounded Laurent coefficient at j={j} is zero")
RESULT["bounded_series_evidence"] = {
    "highest_index_computed": limit,
    "target_coefficients": {str(j): sorted(series[j]) for j in (5, 101, 1637)},
    "nearby_nonzero_coefficients": {
        str(j): sorted(series[j]) for j in (4, 6, 100, 102)
    },
    "not_a_proof_for_unbounded_m": True,
}


# Independently check the elementary symmetric expressions and P5
# directly in the original polynomial ring F2[x,y,z].
one = {(0, 0, 0)}
x, y, z = {(1, 0, 0)}, {(0, 1, 0)}, {(0, 0, 1)}
w = xor(x, y, z)
Q = xor(product(x, x), product(y, y), product(z, z),
        product(x, y), product(y, z), product(z, x))
R = reduce(product, (xor(x, y), xor(y, z), xor(z, x)))
D = reduce(product, (x, y, z, w))
elementary = [set() for _ in range(5)]
elementary[0] = one
for number, a in enumerate((x, y, z, w), 1):
    for k in range(number, 0, -1):
        elementary[k] = xor(elementary[k], product(elementary[k - 1], a))
assert elementary == [one, set(), Q, R, D]


def original_f(n):
    # Frobenius only in the ORIGINAL defining polynomial. Each binary
    # digit contributes one of three pure powers to (x+y+z)^n.
    out = one
    for k in range(n.bit_length()):
        if n & (1 << k):
            out = product(out, {(1 << k, 0, 0), (0, 1 << k, 0),
                                (0, 0, 1 << k)})
    return xor(out, {(n, 0, 0), (0, n, 0), (0, 0, n)})


phi13 = xor(power(Q, 5), product(Q, power(D, 2)),
            product(power(R, 2), D))
f13 = original_f(13)
assert product(R, phi13) == f13
phi13_division, phi13_steps = exact_divide(f13, R)
assert phi13_division == phi13
assert {sum(mon) for mon in phi13} == {10}
assert not original_f(1)
assert original_f(3) == R
RESULT["original_ring_checks"] = {
    "elementary_symmetric_coefficients_match": True,
    "R_times_A_substituted_equals_original_f13": True,
    "phi13_monomials_xyz": sorted(phi13),
    "phi13_total_degree": 10,
    "phi13_nonzero": True,
    "boundary_f1_zero_f3_R": True,
}
checkpoint("elementary symmetric expressions and phi13 identity pass in F2[x,y,z]")


# Reconstruct the formal P_j recurrence without using the generating
# code supplied by the author. Tuple order here is (q,u,d).
q, u, d = {(1, 0, 0)}, {(0, 1, 0)}, {(0, 0, 1)}
p = []
for j in range(102):
    value = one if j == 0 else q if j == 1 else d if j == 2 else set()
    if j >= 2:
        value = xor(value, shift(p[j - 2], (2, 0, 0)))
    if j >= 3:
        value = xor(value, shift(p[j - 3], (0, 1, 0)))
    if j >= 4:
        value = xor(value, shift(p[j - 4], (0, 0, 2)))
    p.append(value)
    assert all(2 * a + 6 * b + 4 * c == 2 * j for a, b, c in value)
A = {(5, 0, 0), (1, 0, 2), (0, 1, 1)}
assert p[5] == A
B1, b1_steps = exact_divide(p[101], A)
assert all(2 * a + 6 * b + 4 * c == 192 for a, b, c in B1)
RESULT["bounded_invariant_ring_evidence"] = {
    "P5_equals_A": True,
    "P101_monomial_count": len(p[101]),
    "P101_division_by_A_remainder_zero": True,
    "B1_monomial_count": len(B1),
    "B1_monomials_q_u_d": sorted(B1),
    "B1_weight": 192,
    "division_steps": b1_steps,
    "not_a_proof_for_unbounded_m": True,
}
checkpoint("direct invariant recurrence and exact P101/A division pass")


# A direct original-polynomial check of the first nontrivial family
# exponent. Since f205=f13*H, cancelling the common nonzero R gives
# phi205=phi13*H. This is independent finite evidence, not the general
# argument. No computer factorization is called.
cofactor205, division_steps = exact_divide(original_f(205), f13)
assert cofactor205 and {sum(mon) for mon in cofactor205} == {192}
RESULT["direct_n205_evidence"] = {
    "original_f205_divided_by_original_f13_remainder_zero": True,
    "cofactor_degree": 192,
    "cofactor_monomial_count": len(cofactor205),
    "division_steps": division_steps,
    "cofactor_monomials_sha256": hashlib.sha256(
        json.dumps(sorted(cofactor205), separators=(",", ":")).encode()
    ).hexdigest(),
    "not_a_proof_for_unbounded_m": True,
}
checkpoint("direct f205/f13 exact division passes")


# Independently transcribed from Hernando--McGuire, section 6, printed
# page 18; not from the constructor's n205 certificate.
published_pairs = {
    (10,0),(9,1),(9,0),(8,2),(8,1),(8,0),(6,4),(6,3),(6,2),(6,1),(6,0),
    (5,5),(5,0),(4,6),(4,4),(4,3),(4,2),(4,0),(3,6),(3,4),(3,3),(3,1),
    (2,8),(2,6),(2,4),(2,2),(2,0),(1,9),(1,8),(1,6),(1,3),(1,1),(1,0),
    (0,10),(0,9),(0,8),(0,6),(0,5),(0,4),(0,2),(0,1),(0,0),
}
dehomogenized = set()
for a, b, c in phi13:
    pair = (a, b)
    if pair in dehomogenized:
        dehomogenized.remove(pair)
    else:
        dehomogenized.add(pair)
assert dehomogenized == published_pairs
RESULT["published_attribution_check"] = {
    "source": "Hernando--McGuire arXiv:0903.2016v4, section 6, printed p18",
    "printed_factor_equal_phi13_at_z1": True,
    "factor_monomial_count": len(published_pairs),
}


digits = []
for m in range(13):
    jm = 5 + sum(6 * 16 ** k for k in range(1, m + 1))
    assert 5 * jm == 32 * 16 ** m - 7
    nm = 2 * jm + 3
    assert 5 * nm == 64 * 16 ** m + 1
    assert nm % 2 == 1
    assert format(jm, "x") == "6" * m + "5"
    digits.append({"m": m, "j": jm, "j_hex": format(jm, "x"), "n": nm})
RESULT["bounded_digit_arithmetic_evidence"] = digits
RESULT["elapsed_seconds"] = time.monotonic() - START
RESULT["all_checks_pass"] = True
OUT.write_text(json.dumps(RESULT, indent=2) + "\n")
checkpoint(f"all checks complete; evidence saved to {OUT.relative_to(ROOT)}")
