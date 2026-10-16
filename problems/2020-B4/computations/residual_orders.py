#!/usr/bin/env python3
"""Exact diagnostics for orders retained by the first bounded filter pass.

Imports only the accompanying standard-library exact_search.py.  No claim of
an unrestricted theorem or an independently audited computer proof is made.
"""

from collections import Counter
from datetime import datetime, timezone
from math import gcd
from pathlib import Path
import json
import platform

from exact_search import factor, generated_multipliers


def divisors(n):
    values = [1]
    for p, exponent in factor(n).items():
        values = [d * p ** a for d in values for a in range(exponent + 1)]
    return sorted(values)


def phi(n):
    result = n
    for p in factor(n):
        result = result // p * (p - 1)
    return result


def order(a, modulus):
    if modulus == 1:
        return 1
    assert gcd(a, modulus) == 1
    result = phi(modulus)
    for p in factor(result):
        while result % p == 0 and pow(a, result // p, modulus) == 1:
            result //= p
    return result


def orbit_histogram(q, group):
    """For d|v, units times v/d form phi(d)/|M mod d| orbits of that size."""
    v = q * q + q + 1
    hist = Counter()
    for d in divisors(v):
        length = len({m % d for m in group})
        assert phi(d) % length == 0
        hist[length] += phi(d) // length
    assert sum(length * count for length, count in hist.items()) == v
    return dict(sorted(hist.items()))


def subset_sum(hist, target):
    possible = 1
    mask = (1 << (target + 1)) - 1
    for length, count in hist.items():
        count = min(count, target // length)
        # Binary splitting is exact for bounded subset sums of equal weights.
        power = 1
        while count:
            take = min(power, count)
            possible |= possible << (take * length)
            possible &= mask
            count -= take
            power *= 2
    return bool((possible >> target) & 1)


def arasu_diagnostics(q):
    """Gordon 2020/2022 Theorem 3, tested with NONNEGATIVE a,b, including zero."""
    v, k = q * q + q + 1, q + 1
    results = []
    for p, exponent in factor(v).items():
        if exponent != 1:
            continue
        h = v // p
        assert gcd(p, h) == 1
        for m in factor(q):
            s = order(m, h)
            multiplier = pow(m, s, v)
            o = order(multiplier % p, p)
            if o <= 1:
                continue
            a_max = min(k // o, (p - 1) // (o * (o - 1)))
            solutions = []
            for a in range(a_max + 1):
                b = k - a * o
                if 0 <= b <= h and b * (b - 1) <= h - 1:
                    solutions.append([a, b])
            results.append({
                "p": p, "h": h, "m": m, "s": s,
                "m_to_s_mod_v": multiplier, "o": o,
                "nonnegative_solutions_a_b": solutions,
                "excluded": not solutions,
            })
    return results


def main():
    report = {
        "recorded_utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(),
        "dependencies": "Python standard library only",
        "results": [],
    }
    for q in (1944, 2304, 2435):
        group, complete = generated_multipliers(q)
        assert complete
        histogram = orbit_histogram(q, group)
        report["results"].append({
            "q": q, "n": q + 1, "v": q * q + q + 1,
            "q_factorization": factor(q), "v_factorization": factor(q * q + q + 1),
            "multiplier_group_order": len(group),
            "orbit_length_histogram": histogram,
            "size_q_plus_one_reachable": subset_sum(histogram, q + 1),
            "Arasu_Gordon_diagnostics": arasu_diagnostics(q),
        })
    encoded = json.dumps(report, indent=2, sort_keys=True) + "\n"
    prefix = Path(__file__).parent / "residual-orders"
    prefix.with_suffix(".json").write_text(encoded)
    prefix.with_suffix(".stdout").write_text(encoded)
    print(encoded, end="")


if __name__ == "__main__":
    main()
