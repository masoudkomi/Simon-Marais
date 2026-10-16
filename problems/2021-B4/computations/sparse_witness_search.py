"""Exact evidence for 2021 B4(b); this is not an unrestricted proof.

Centered monic f has f(0)=0 and c[d-1]=0.  At a nonzero coefficient
c[k], prescribe a nonzero rational/integer witness r[k].  Descending
Hasse equations force c[k] without division.  Coefficients outside
the support have witness zero.  All surviving f(r[k]) equations are
checked in integer arithmetic, or modulo the specified prime.
"""

from itertools import combinations, product
from math import comb, gcd
import argparse
import json
import platform
import sys
import time


def horner(coeff, x, modulus=None):
    out = 0
    for a in reversed(coeff):
        out = out * x + a
        if modulus:
            out %= modulus
    return out


def solve(d, support, roots, modulus=None):
    coeff = [0] * (d + 1)
    coeff[d] = 1
    for k, r in reversed(list(zip(support, roots))):
        c = -sum(coeff[j] * comb(j, k) * r ** (j-k)
                 for j in range(k + 1, d + 1))
        coeff[k] = c % modulus if modulus else c
        if not coeff[k]:
            return None  # this tuple belongs to a smaller support
    if any(horner(coeff, r, modulus) for r in set(roots)):
        return None
    # Independently check every required Hasse equation.
    witnesses = dict(zip(support, roots))
    for k in range(1, d):
        r = witnesses.get(k, 0)
        value = sum(coeff[j] * comb(j, k) * r ** (j-k)
                    for j in range(k, d + 1))
        if modulus:
            value %= modulus
        assert value == 0
        assert horner(coeff, r, modulus) == 0
    return coeff


def run(d, max_support, values, modulus=None, first=False):
    start = time.perf_counter()
    tested = 0
    primitive_tested = 0
    found = []
    for size in range(1, max_support + 1):
        for support in combinations(range(1, d-1), size):
            for roots in product(values, repeat=size):
                tested += 1
                if not modulus:
                    g = 0
                    for r in roots:
                        g = gcd(g, abs(r))
                    if g != 1:
                        continue
                    # Reflection is an exact affine symmetry.
                    if roots[0] < 0:
                        continue
                primitive_tested += 1
                coeff = solve(d, support, roots, modulus)
                if coeff is not None:
                    found.append({"support_exponents": support,
                                  "witnesses": roots,
                                  "coefficients_ascending": coeff})
                    if first:
                        return {"degree": d, "modulus": modulus,
                                "maximum_support": max_support,
                                "values": values, "tuples_visited": tested,
                                "tuples_solved": primitive_tested,
                                "search_complete": False, "examples": found,
                                "elapsed_seconds": round(time.perf_counter()-start, 4)}
    return {"degree": d, "modulus": modulus,
            "maximum_support": max_support, "values": values,
            "tuples_visited": tested, "tuples_solved": primitive_tested,
            "search_complete": True, "examples": found,
            "elapsed_seconds": round(time.perf_counter()-start, 4)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--degrees", type=int, nargs="+", default=[20, 24, 28, 30])
    parser.add_argument("--support", type=int, default=3)
    parser.add_argument("--primes", type=int, nargs="*", default=[])
    args = parser.parse_args()
    print(json.dumps({"python": sys.version, "platform": platform.platform(),
                      "dependencies": "Python standard library only",
                      "status": "finite exact computational evidence, not proof"}))
    if args.primes:
        for d in args.degrees:
            for p in args.primes:
                print(json.dumps(run(d, args.support, list(range(1,p)), p, first=True)))
    else:
        for d in args.degrees:
            print(json.dumps(run(d, args.support, [-2,-1,1,2])))
