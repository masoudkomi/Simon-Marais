#!/usr/bin/env python3
"""Exact rational arithmetic for the published three-bundle construction.

MacMahon's product is reproduced from Felsner--Valtr, Section 4, Eq. (11):
https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf
This checks finite values and published asymptotic coefficients numerically.
It does not prove the product formula, gluing injection, or limiting estimate.
Standard library only. Bounded parameters m <= 16.
"""
from fractions import Fraction
from math import log2
import platform


def macmahon_equal(m):
    # The product over k telescopes, leaving m^2 exact rational factors.
    result = Fraction(1)
    for i in range(1, m + 1):
        for j in range(1, m + 1):
            result *= Fraction(i + j + m - 1, i + j - 1)
    assert result.denominator == 1
    return result.numerator


print(f"Python {platform.python_version()}; fractions.Fraction; no random choices")
print("Published product reproduction; finite evidence, not a new proof")
print("m PP(m,m,m) log2_PP/(9*m*m)")
for m in (1, 2, 3, 4, 8, 16):
    count = macmahon_equal(m)
    print(m, count, f"{log2(count)/(9*m*m):.12f}")
print(f"Published three-bundle coefficient: {log2(3)/2-2/3:.12f}")
print(f"Published recursively amplified coefficient: {3*log2(3)/4-1:.12f}")
