#!/usr/bin/env python3
"""Finite exact evidence for candidate-resultant-v0.1.md; not a proof.

Run from repository root:
  .venv/bin/python problems/2023-B4/computations/resultant_checks.py \
    > problems/2023-B4/computations/resultant_checks.stdout.txt

Dependencies: Python stdlib, SymPy (project requirements-research.txt).
No network, random sampling, paid API, or writes outside the redirected stdout.
"""

from fractions import Fraction
from math import gcd, isqrt
import platform
import sys

import sympy as sp


def lucas_polynomials(last, d, p):
    values = [sp.Integer(0), sp.Integer(1)]
    for _ in range(last - 1):
        values.append(sp.expand(d * values[-1] + p * values[-2]))
    return values


def fraction_square_root(value):
    if value < 0:
        return None
    a, b = isqrt(value.numerator), isqrt(value.denominator)
    if a * a == value.numerator and b * b == value.denominator:
        return Fraction(a, b)
    return None


def exact_fraction_lucas(last, d, p):
    values = [Fraction(0), Fraction(1)]
    for _ in range(last - 1):
        values.append(d * values[-1] + p * values[-2])
    return values


def sylvester_det(f, g, variable):
    """Standard determinant convention, independently of sp.resultant sign."""
    f, g = sp.Poly(f, variable), sp.Poly(g, variable)
    m, n = f.degree(), g.degree()
    rows = []
    for shift in range(n):
        rows.append([0] * shift + f.all_coeffs() + [0] * (n - 1 - shift))
    for shift in range(m):
        rows.append([0] * shift + g.all_coeffs() + [0] * (m - 1 - shift))
    return sp.Matrix(rows).det()


def main():
    print("Finite exact computation; evidence only, not an unrestricted proof.")
    print("Candidate: notes/candidate-resultant-v0.1.md")
    print("Python:", sys.version.split()[0], "platform:", platform.system())
    print("SymPy:", sp.__version__)
    d, p, n = sp.symbols("D P N")
    f = lucas_polynomials(30, d, p)

    checked = 0
    for even in range(4, 19, 2):
        for odd in range(3, even, 2):
            if gcd(even, odd) != 1:
                continue
            a = f[even] - f[odd]
            b = (d * d + 4 * p) * f[odd] ** 2 - 4 * n
            resultant = sp.Poly(sp.resultant(a, b, p), d, n)
            target = d ** (even * (odd - 1)) * (
                sp.Rational(even, 2) * d ** (even - odd)
                - 2 ** (even - odd - 1) * odd
            )
            constant = sp.expand(resultant.as_expr().subs(n, 0))
            constant_ok = (
                sp.expand(constant - target) == 0
                or sp.expand(constant + target) == 0
            )
            max_weight = max(
                i + 2 * odd * j for (i, j), _ in resultant.terms()
            )
            assert constant_ok, (even, odd, "constant-in-N identity")
            assert max_weight <= odd * (even - 1), (even, odd, "weight")
            print(
                f"resultant ({even},{odd}): N=0 identity up to sign OK; "
                f"max_weight={max_weight}; bound={odd*(even-1)}; "
                f"terms={len(resultant.terms())}"
            )
            checked += 1
    print("Resultant identity pairs checked:", checked)

    one_f = lucas_polynomials(30, sp.Integer(1), p)
    unit_checked = 0
    for even in range(2, 31, 2):
        for odd in range(3, even, 2):
            if gcd(even, odd) != 1:
                continue
            value = sp.resultant(one_f[even], one_f[odd], p)
            assert value in (-1, 1), (even, odd, value)
            unit_checked += 1
    print("Unit Lucas resultants checked:", unit_checked, "; all +1 or -1")

    # The proof uses the resultant only up to an overall sign. Check numerical
    # instances against a direct Sylvester determinant rather than assuming
    # a sign convention for a subresultant implementation.
    determinant_checks = 0
    for even, odd in [(4, 3), (6, 5), (8, 3), (8, 5)]:
        for dv, nv in [(Fraction(2, 3), 2), (Fraction(3, 5), 7)]:
            a = (f[even] - f[odd]).subs(d, sp.Rational(dv.numerator, dv.denominator))
            b = ((d * d + 4 * p) * f[odd] ** 2 - 4 * n).subs(
                {d: sp.Rational(dv.numerator, dv.denominator), n: nv}
            )
            determinant = sylvester_det(a, b, p)
            value = sp.resultant(a, b, p)
            assert determinant == value or determinant == -value
            determinant_checks += 1
    print("Direct Sylvester determinant checks up to sign:", determinant_checks)

    # Independent algebra check of the coordinator's restricted (4,3) formula.
    p43 = d ** 2 * (1 - d) / (2 * d - 1)
    n43 = d ** 8 * (3 - 2 * d) / (4 * (2 * d - 1) ** 3)
    assert sp.factor((f[4] - f[3]).subs(p, p43)) == 0
    assert sp.factor(((d*d + 4*p)*f[3]**2/4).subs(p, p43) - n43) == 0
    print("Coordinator (4,3) trace/norm formula: exact identities OK")

    traces_checked = 0
    rational_65 = []
    integer_hits = []
    # Every reduced trace 0<D<1 with denominator <=300. For (4,3), its
    # positive-P branch is unique; for (6,5), test all rational roots of
    # its quadratic in P by an exact rational-square discriminant test.
    for denominator in range(2, 301):
        for numerator in range(1, denominator):
            if gcd(numerator, denominator) != 1:
                continue
            dv = Fraction(numerator, denominator)
            traces_checked += 1
            if dv > Fraction(1, 2):
                pv = dv*dv*(1-dv)/(2*dv-1)
                nv = dv**8*(3-2*dv)/(4*(2*dv-1)**3)
                assert pv > 0
                if nv.denominator == 1:
                    integer_hits.append((4, 3, dv, pv, nv))

            discriminant_core = 4*dv**2 - 8*dv + 5
            root = fraction_square_root(discriminant_core)
            possible = []
            if 3*dv == 1:
                # (4D^3-3D^2)P+(D^5-D^4)=0.
                possible = [-(dv**5-dv**4)/(4*dv**3-3*dv**2)]
            elif root is not None:
                possible = [
                    dv*dv*(3-4*dv+sign*root)/(2*(3*dv-1))
                    for sign in (-1, 1)
                ]
            for pv in set(possible):
                if pv <= 0:
                    continue
                values = exact_fraction_lucas(6, dv, pv)
                assert values[6] == values[5], (dv, pv, values[6], values[5])
                nv = (dv*dv + 4*pv)*values[5]**2/4
                rational_65.append((dv, pv, nv))
                if nv.denominator == 1:
                    integer_hits.append((6, 5, dv, pv, nv))
    print("Exact reduced traces with denominator <=300:", traces_checked)
    print("Positive rational (6,5) branches found:", len(rational_65))
    for dv, pv, nv in rational_65:
        print(f"  D={dv}, P={pv}, derived N={nv}")
    print("Integer-N hits for (4,3),(6,5) in this trace range:", integer_hits)
    print("Limit: these finite searches do not exclude larger denominators or exponents.")
    print("All requested finite checks completed.")


if __name__ == "__main__":
    main()
