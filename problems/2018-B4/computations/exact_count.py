#!/usr/bin/env python3
"""Finite evidence for 2018 B4; Python standard library only.

Run from repository root:
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 problems/2018-B4/computations/exact_count.py

The formula, direct matrix enumeration, prefix-inequality dynamic program,
bounded-composition dynamic program, and reflection-map checks use distinct
implementations. Finite agreement is evidence, not an unrestricted proof.
"""

from collections import defaultdict
from fractions import Fraction
from math import comb, factorial
from platform import python_implementation, python_version


def formula(m, n):
    assert m >= 1 and n >= 1
    if m == 1:
        return 0
    return sum(
        (-1) ** j * comb(m, j) * comb((m - 2 * j) * n + m - j - 2, m - 2)
        for j in range((m - 1) // 2 + 1)
    )


def composition_difference(m, n):
    """Multiply (1+x+...+x^(2n))^m by exact convolution."""
    c = [1]
    for _ in range(m):
        nxt = [0] * (len(c) + 2 * n)
        for degree, coefficient in enumerate(c):
            for a in range(2 * n + 1):
                nxt[degree + a] += coefficient
        c = nxt
    length = m * n
    return c[length] - c[length - 1]


def prefix_dp(m, n):
    """Count top-row multiplicities using all strict-column inequalities.

    If s is the number of top entries < k and a the number equal to k,
    all bottom entries <= k need top entries < k, giving 2*s+a >= 2*n*k.
    """
    length = m * n
    states = {0: 1}
    for k in range(1, m + 1):
        nxt = defaultdict(int)
        for s, count in states.items():
            for a in range(min(2 * n, length - s) + 1):
                if 2 * s + a >= 2 * n * k:
                    nxt[s + a] += count
        states = nxt
    return states.get(length, 0)


def allocations(m, cap, target, prefix=()):
    if m == 0:
        if target == 0:
            yield prefix
        return
    for a in range(max(0, target - cap * (m - 1)), min(cap, target) + 1):
        yield from allocations(m - 1, cap, target - a, prefix + (a,))


def rows_from_top(a, n):
    upper = tuple(i for i, copies in enumerate(a, 1) for _ in range(copies))
    lower = tuple(i for i, copies in enumerate(a, 1) for _ in range(2 * n - copies))
    return upper, lower


def good(upper, lower):
    return all(a < b for a, b in zip(upper, lower))


def reflection(upper, lower):
    # All indices here are zero based; proof.md uses one based indices.
    i = next(j for j, (a, b) in enumerate(zip(upper, lower)) if a >= b)
    return lower[: i + 1] + upper[i:], upper[:i] + lower[i + 1 :]


def inverse_reflection(longer, shorter):
    i = next((j for j, (q, p) in enumerate(zip(shorter, longer)) if q >= p), len(shorter))
    return shorter[:i] + longer[i + 1 :], longer[: i + 1] + shorter[i:]


def check_direct_and_reflection(m, n):
    length = m * n
    direct = 0
    images = set()
    for a in allocations(m, 2 * n, length):
        upper, lower = rows_from_top(a, n)
        if good(upper, lower):
            direct += 1
        else:
            longer, shorter = reflection(upper, lower)
            assert tuple(sorted(longer)) == longer and tuple(sorted(shorter)) == shorter
            assert len(longer) == length + 1 and len(shorter) == length - 1
            assert inverse_reflection(longer, shorter) == (upper, lower)
            assert (longer, shorter) not in images
            images.add((longer, shorter))
    targets = set()
    for a in allocations(m, 2 * n, length + 1):
        longer, shorter = rows_from_top(a, n)
        upper, lower = inverse_reflection(longer, shorter)
        assert not good(upper, lower)
        assert reflection(upper, lower) == (longer, shorter)
        targets.add((longer, shorter))
    assert images == targets
    return direct, len(images)


def multiply_affine(poly, intercept, slope):
    out = [Fraction(0)] * (len(poly) + 1)
    for k, c in enumerate(poly):
        out[k] += c * intercept
        out[k + 1] += c * slope
    return out


def exact_polynomial(m):
    """Coefficients in increasing powers of n, with rational arithmetic."""
    degree = m - 2
    result = [Fraction(0)] * (degree + 1)
    for j in range((m - 1) // 2 + 1):
        term = [Fraction((-1) ** j * comb(m, j), factorial(degree))]
        for r in range(degree):
            term = multiply_affine(term, m - j - 2 - r, m - 2 * j)
        result = [a + b for a, b in zip(result, term)]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def main():
    print(f"Runtime: {python_implementation()} {python_version()}; standard library only")
    cases = 0
    for m in range(1, 21):
        for n in range(1, 21):
            f, d, c = formula(m, n), prefix_dp(m, n), composition_difference(m, n)
            assert f == d == c, (m, n, f, d, c)
            cases += 1
    print(f"Formula = prefix DP = composition difference: {cases} cases, 1<=m,n<=20")
    direct_cases = 0
    bad_total = 0
    for m in range(1, 8):
        for n in range(1, 4):
            direct, bad = check_direct_and_reflection(m, n)
            assert direct == formula(m, n), (m, n, direct)
            direct_cases += 1
            bad_total += bad
    print(f"Direct matrices and both reflection inverses: {direct_cases} cases, 1<=m<=7, 1<=n<=3")
    print(f"Bad row pairs checked individually: {bad_total}")
    for n in range(1, 101):
        assert formula(5, n) == (5 * n * n + 5 * n + 2) // 2
    print("Official m=5 comparison: 1<=n<=100, all agree")
    print("Table: rows m=1..10; columns n=1..6")
    for m in range(1, 11):
        print(f"m={m}: " + ", ".join(str(formula(m, n)) for n in range(1, 7)))
    print("Exact polynomial coefficients [n^0,n^1,...] for m=2..10")
    for m in range(2, 11):
        p = exact_polynomial(m)
        for n in range(1, 31):
            assert sum(c * n**k for k, c in enumerate(p)) == formula(m, n)
        print(f"m={m}: [" + ", ".join(str(c) for c in p) + "]")
    print("All finite checks passed. These computations are evidence, not a general proof.")


if __name__ == "__main__":
    main()
