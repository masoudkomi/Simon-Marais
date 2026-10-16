#!/usr/bin/env python3
"""Exact GF(2) calculations for 2024 B4(b), not a general classification.

Sparse polynomials are sets of exponent tuples. No probabilistic steps.
Run from repository root: .venv/bin/python problems/2024-B4/computations/invariant_probe.py
"""
import json
import platform
from pathlib import Path

HERE = Path(__file__).resolve().parent
ZERO = frozenset()
ONE = frozenset({(0, 0, 0)})


def add(*ps):
    out = set()
    for p in ps:
        out.symmetric_difference_update(p)
    return frozenset(out)


def mul(a, b):
    out = set()
    for u in a:
        for v in b:
            w = tuple(x + y for x, y in zip(u, v))
            if w in out:
                out.remove(w)
            else:
                out.add(w)
    return frozenset(out)


def power(a, n):
    out = ONE
    while n:
        if n & 1:
            out = mul(out, a)
        a = frozenset(tuple(2 * x for x in u) for u in a)
        n >>= 1
    return out


def divrem(a, b):
    """Single-divisor division using lex monomial order."""
    assert b
    lead = max(b)
    q, r, work = set(), set(), set(a)
    while work:
        m = max(work)
        if all(i >= j for i, j in zip(m, lead)):
            t = tuple(i - j for i, j in zip(m, lead))
            q.add(t)
            work.symmetric_difference_update(tuple(i + j for i, j in zip(t, u)) for u in b)
        else:
            r.add(m)
            work.remove(m)
    return frozenset(q), frozenset(r)


def degree(p):
    return max((sum(u) for u in p), default=-1)


def evaluate(p, substitutions):
    out = ZERO
    for monomial in p:
        term = ONE
        for s, e in zip(substitutions, monomial):
            term = mul(term, power(s, e))
        out = add(out, term)
    return out


X, Y, Z = (frozenset({tuple(int(i == j) for i in range(3))}) for j in range(3))
Q = add(power(X, 2), power(Y, 2), power(Z, 2), mul(X, Y), mul(Y, Z), mul(Z, X))
R = mul(mul(add(X, Y), add(Y, Z)), add(Z, X))
D = mul(mul(mul(X, Y), Z), add(X, Y, Z))


def direct_phi(n):
    f = add(power(X, n), power(Y, n), power(Z, n), power(add(X, Y, Z), n))
    p, rem = divrem(f, R)
    assert not rem
    assert mul(R, p) == f
    return p


def invariant_powers(limit):
    """P_n/R in formal independent variables (Q,R,D), P_n=sum of root nth powers."""
    q, r, d = X, Y, Z
    # Generating function sum_{n>=3} (P_n/R)t^(n-3)=1/(1+Qt^2+Rt^3+Dt^4).
    h = [ONE]
    for j in range(1, limit - 2):
        h.append(add(mul(q, h[j-2]) if j >= 2 else ZERO,
                     mul(r, h[j-3]) if j >= 3 else ZERO,
                     mul(d, h[j-4]) if j >= 4 else ZERO))
    return {n: h[n-3] for n in range(3, limit+1)}


def polynomial_string(p, names=("Q", "R", "D")):
    if not p:
        return "0"
    terms = []
    for exps in sorted(p, reverse=True):
        factors = [v if e == 1 else f"{v}^{e}" for v,e in zip(names, exps) if e]
        terms.append("*".join(factors) or "1")
    return " + ".join(terms)


def main():
    print("Exact sparse GF(2) arithmetic; Python", platform.python_version())
    hs = invariant_powers(1025)
    for n in range(3, 66, 2):
        direct = direct_phi(n)
        assert evaluate(hs[n], (Q, R, D)) == direct
    print("Independent direct numerator/division and invariant recurrence agree for odd n=3..65.")
    print("Boundary n=1: numerator=0; n=3: phi=", polynomial_string(hs[3]))
    for n in (5, 7, 9, 11, 13, 17, 21, 25, 29):
        print(f"phi_{n} in invariants: {polynomial_string(hs[n])}")

    # Hernando--McGuire, arXiv:0903.2016v4, Section 6, displayed degree-10 factor.
    # Exponents copied from their affine polynomial, then homogenized to degree 10.
    affine_terms = [
        (10,0),(9,1),(9,0),(8,2),(8,1),(8,0),(6,4),(6,3),(6,2),(6,1),(6,0),
        (5,5),(5,0),(4,6),(4,4),(4,3),(4,2),(4,0),(3,6),(3,4),(3,3),(3,1),
        (2,8),(2,6),(2,4),(2,2),(2,0),(1,9),(1,8),(1,6),(1,3),(1,1),(1,0),
        (0,10),(0,9),(0,8),(0,6),(0,5),(0,4),(0,2),(0,1),(0,0)]
    published = frozenset((a,b,10-a-b) for a,b in affine_terms)
    basis = [(a,b,c) for a in range(6) for b in range(4) for c in range(3) if 2*a+3*b+4*c == 10]
    found = []
    for mask in range(1 << len(basis)):
        formal = frozenset(basis[i] for i in range(len(basis)) if (mask >> i) & 1)
        if evaluate(formal, (Q,R,D)) == published:
            found.append(formal)
    assert len(found) == 1
    A = found[0]
    print("Published n205 degree-10 factor compressed:", polynomial_string(A))
    cofactor, rem = divrem(hs[205], A)
    assert not rem
    assert mul(A, cofactor) == hs[205]
    print("n205 invariant division exact; factor formal terms", len(A), "cofactor terms", len(cofactor))
    phi205 = direct_phi(205)
    expanded_cofactor, rem = divrem(phi205, published)
    assert not rem
    assert mul(published, expanded_cofactor) == phi205
    print("n205 independent x,y,z multiply-back exact; degrees", degree(published), degree(expanded_cofactor),
          "term counts", len(published), len(expanded_cofactor), len(phi205))
    certificate = {
        "field": "GF(2)", "n": 205, "homogeneous_factor_xyz": sorted(published),
        "homogeneous_cofactor_xyz": sorted(expanded_cofactor),
        "invariant_factor_QRD": sorted(A), "invariant_cofactor_QRD": sorted(cofactor),
        "source": "Hernando and McGuire, arXiv:0903.2016v4, Section 6",
        "status": "exact finite identity checked; irreducibility not asserted by this script"}
    (HERE / "n205-certificate.json").write_text(json.dumps(certificate, indent=2) + "\n")
    # Bounded divisibility scan for this particular published factor, not a factorization/classification.
    hits = []
    for n in range(3, 1026, 2):
        _, rem = divrem(hs[n], A)
        if not rem:
            hits.append(n)
    print("Formal invariant A divisibility among odd n in [3,1025]:", hits)
    print("All scan exclusions concern this one formal invariant factor only, not reducibility.")


if __name__ == "__main__":
    main()
