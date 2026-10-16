"""Review-1 checks for 2018 B4; Python standard library only.

No author computation was imported/read before constructing or running this file.
The direct counter builds actual columns with both row orders enforced.
It does not use bounded compositions, tableaux recurrences, or the reflection identity.
All checks are finite evidence, not a proof for unbounded parameters.
The known m=5 preliminary case is deliberately omitted from enumerations.
"""

from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
import hashlib
import json
import platform
import time


OUT = Path(__file__).resolve().parent / "independent-audit-results.json"
BEGIN = time.monotonic()
DEADLINE = BEGIN + 45
STATE_LIMIT = 1_000_000


def formula(m, n):
    if m == 1:
        return 0
    return sum(
        (-1) ** j * comb(m, j)
        * comb((m - 2 * j) * n + m - j - 2, m - 2)
        for j in range((m - 1) // 2 + 1)
    )


def direct_columns(m, n):
    """Count matrices by appending one legal column to a legal prefix."""
    visited = 0

    @lru_cache(None)
    def extend(top_min, bottom_min, remaining):
        nonlocal visited
        visited += 1
        if visited > STATE_LIMIT or (visited % 1024 == 0 and time.monotonic() > DEADLINE):
            raise TimeoutError("global 45-second/state budget reached")
        if not any(remaining):
            return 1
        # A smaller residual entry could fit neither future row.
        if any(remaining[:top_min - 1]):
            return 0
        count = 0
        for a in range(top_min, m + 1):
            if remaining[a - 1] == 0:
                continue
            for b in range(max(bottom_min, a + 1), m + 1):
                if remaining[b - 1] == 0:
                    continue
                rest = list(remaining)
                rest[a - 1] -= 1
                rest[b - 1] -= 1
                count += extend(a, b, tuple(rest))
        return count

    value = extend(1, 1, (2 * n,) * m)
    return value, visited


def forward(U, V):
    i = next(j for j, (u, v) in enumerate(zip(U, V)) if u >= v)
    return (V[:i + 1] + U[i:], U[:i] + V[i + 1:]), i + 1


def inverse(P, Q):
    L = len(P) - 1
    i = next((j for j in range(L - 1) if Q[j] >= P[j]), L - 1)
    return (Q[:i] + P[i + 1:], P[:i + 1] + Q[i:]), i + 1


def ordered(row):
    return all(a <= b for a, b in zip(row, row[1:]))


def test_reflection():
    counts = []
    for alphabet in range(1, 5):
        for L in range(1, 7):
            equal = list(combinations_with_replacement(range(1, alphabet + 1), L))
            bad = 0
            failure_indices = set()
            image = set()
            for U in equal:
                for V in equal:
                    if all(u < v for u, v in zip(U, V)):
                        continue
                    bad += 1
                    (P, Q), i = forward(U, V)
                    failure_indices.add(i)
                    assert len(P) == L + 1 and len(Q) == L - 1
                    assert ordered(P) and ordered(Q)
                    assert Counter(U + V) == Counter(P + Q)
                    assert inverse(P, Q) == ((U, V), i)
                    image.add((P, Q))
            tested_S = 0
            for P in combinations_with_replacement(range(1, alphabet + 1), L + 1):
                for Q in combinations_with_replacement(range(1, alphabet + 1), L - 1):
                    tested_S += 1
                    (U, V), i = inverse(P, Q)
                    assert len(U) == len(V) == L
                    assert ordered(U) and ordered(V)
                    assert Counter(U + V) == Counter(P + Q)
                    assert all(U[j] < V[j] for j in range(i - 1))
                    assert U[i - 1] >= V[i - 1]
                    assert forward(U, V) == ((P, Q), i)
                    assert (P, Q) in image
            assert len(image) == bad == tested_S
            counts.append({"alphabet": alphabet, "L": L, "bad_R": bad,
                           "S": tested_S, "first_failure_indices": sorted(failure_indices)})
    return counts


def test_truncation():
    checked = 0
    omitted = 0
    for m in range(2, 101):
        if m == 5:
            continue
        for n in range(1, 51):
            J = (m - 1) // 2
            for j in range(m + 1):
                in_coefficient_sum = (2 * n + 1) * j <= m * n
                if in_coefficient_sum:
                    assert j <= J
                if j <= J:
                    upper = (m - 2 * j) * n + m - j - 2
                    assert upper >= 0
                    if not in_coefficient_sum:
                        omitted += 1
                        assert upper < m - 2
                        assert comb(upper, m - 2) == 0
                checked += 1
    return {"m_range": [2, 100], "n_range": [1, 50], "m_excluded": [5],
            "index_checks": checked, "added_zero_terms": omitted}


def test_high_degree_cancellation():
    checked = []
    for m in range(3, 101):
        if m == 5:
            continue
        T = sum((-1) ** j * comb(m, j) * (m - 2 * j) ** (m - 2)
                for j in range((m - 1) // 2 + 1))
        assert T == 0
        checked.append(m)
    return {"m_tested": checked, "all_T_zero": True}


def main():
    cases = []
    cases += [(m, 1) for m in (1, 2, 3, 4, 6, 7, 8, 9, 10)]
    cases += [(m, n) for n in (2, 3, 4) for m in (1, 2, 3, 4, 6, 7)]
    cases += [(8, 2), (4, 5), (4, 10), (4, 20), (6, 5)]
    result = {"python": platform.python_version(), "dependencies": "standard library only",
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "proof_sha256": hashlib.sha256(Path(__file__).parents[2].joinpath("proof.md").read_bytes()).hexdigest(),
              "budget": {"seconds": 45, "max_states_per_case": STATE_LIMIT},
              "m5_preliminary_excluded": True, "direct_counts": [], "incomplete": []}
    try:
        result["reflection"] = test_reflection()
        result["truncation"] = test_truncation()
        result["degree_cancellation"] = test_high_degree_cancellation()
        for m, n in cases:
            if time.monotonic() > DEADLINE:
                result["incomplete"].append({"m": m, "n": n, "reason": "global deadline"})
                continue
            t0 = time.monotonic()
            try:
                actual, states = direct_columns(m, n)
            except TimeoutError as error:
                result["incomplete"].append({"m": m, "n": n, "reason": str(error)})
                continue
            expected = formula(m, n)
            assert actual == expected, (m, n, actual, expected)
            result["direct_counts"].append({"m": m, "n": n, "direct_column_count": actual,
                                            "candidate_formula": expected, "states": states,
                                            "seconds": round(time.monotonic() - t0, 6)})
        result["status"] = "all completed checks pass"
    except Exception as error:
        result["status"] = "failure"
        result["error"] = repr(error)
        raise
    finally:
        result["total_seconds"] = round(time.monotonic() - BEGIN, 6)
        OUT.write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
