"""Independent bounded exact checks of 2018 B4 candidate v1.0.

Designed by reviewer 2 without reading author/reviewer-1 computations.
Computational evidence only; no assertion of proof by finite testing.
The known m=5 preliminary case is deliberately excluded.
"""

from collections import Counter
from functools import lru_cache
from itertools import combinations_with_replacement, product
from math import comb
from pathlib import Path
from time import perf_counter
import platform


def formula(m, n):
    if m == 1:
        return 0
    return sum(
        (-1) ** j * comb(m, j)
        * (comb((m - 2 * j) * n + m - j - 2, m - 2)
           if (m - 2 * j) * n + m - j - 2 >= m - 2 else 0)
        for j in range((m - 1) // 2 + 1)
    )


def literal_column_count(m, n):
    """Append actual strict columns in row-monotone order, with no symmetry weights."""
    calls = 0

    @lru_cache(None)
    def visit(remaining, last_top, last_bottom):
        nonlocal calls
        calls += 1
        if calls > 500_000:
            raise RuntimeError(f"explicit state cap exceeded at m={m}, n={n}")
        if not any(remaining):
            return 1
        # Every later top is >= last_top, and every later bottom > last_top.
        if any(remaining[a] for a in range(last_top)):
            return 0
        count = 0
        for a in range(last_top, m):
            if remaining[a] == 0:
                continue
            for b in range(max(last_bottom, a + 1), m):
                if remaining[b] == 0:
                    continue
                rest = list(remaining)
                rest[a] -= 1
                rest[b] -= 1
                count += visit(tuple(rest), a, b)
        return count

    answer = visit((2 * n,) * m, 0, 0)
    return answer, visit.cache_info().currsize


def forward(u, v):
    k = next(k for k, (a, b) in enumerate(zip(u, v)) if a >= b)
    return v[: k + 1] + u[k:], u[:k] + v[k + 1:]


def inverse(p, q):
    length = len(q) + 1
    k = next((k for k in range(length - 1) if q[k] >= p[k]), length - 1)
    return q[:k] + p[k + 1:], p[: k + 1] + q[k:]


def sorted_row(row):
    return all(a <= b for a, b in zip(row, row[1:]))


def reflection_exhaustion():
    # All contents, not just equal contents, stress empty pieces and equality.
    total_bad = total_s = 0
    boundary_counts = Counter()
    for m in range(1, 5):
        for length in range(1, 7):
            rows = list(combinations_with_replacement(range(1, m + 1), length))
            image = set()
            bad = 0
            for u, v in product(rows, repeat=2):
                failures = [k for k, (a, b) in enumerate(zip(u, v)) if a >= b]
                if not failures:
                    continue
                bad += 1
                k = failures[0]
                boundary_counts["i=1"] += (k == 0)
                boundary_counts["i=L"] += (k == length - 1)
                boundary_counts["L=1"] += (length == 1)
                p, q = forward(u, v)
                assert (len(p), len(q)) == (length + 1, length - 1)
                assert sorted_row(p) and sorted_row(q)
                assert Counter(p + q) == Counter(u + v)
                assert inverse(p, q) == (u, v)
                image.add((p, q))
            targets = set(product(
                combinations_with_replacement(range(1, m + 1), length + 1),
                combinations_with_replacement(range(1, m + 1), length - 1),
            ))
            assert len(image) == bad
            assert image == targets
            for p, q in targets:
                u, v = inverse(p, q)
                assert len(u) == len(v) == length
                assert sorted_row(u) and sorted_row(v)
                assert Counter(p + q) == Counter(u + v)
                assert any(a >= b for a, b in zip(u, v))
                assert forward(u, v) == (p, q)
            total_bad += bad
            total_s += len(targets)
    return total_bad, total_s, dict(boundary_counts)


def main():
    lines = ["2018 B4 reviewer 2 independent exact evidence", platform.python_version(),
             "m=5 excluded from research checks; no author/reviewer-1 code imported.",
             "Method: append actual (top,bottom) columns subject to weak rows, strict columns, exact global content."]
    start = perf_counter()
    for m in (1, 2, 3, 4, 6, 7, 8):
        values = []
        states = []
        for n in range(1, 4):
            direct, state_count = literal_column_count(m, n)
            expected = formula(m, n)
            assert direct == expected, (m, n, direct, expected)
            values.append(direct)
            states.append(state_count)
        lines.append(f"m={m}, n=1..3: counts={values}; memo states={states}; formula agrees")
    for m, n in ((2, 20), (3, 15), (4, 10), (6, 5), (7, 4), (9, 1), (10, 1)):
        direct, state_count = literal_column_count(m, n)
        assert direct == formula(m, n)
        lines.append(f"m={m}, n={n}: count={direct}; memo states={state_count}; formula agrees")
    bad, target, boundaries = reflection_exhaustion()
    lines.append(f"Reflection exhaustion: alphabets m=1..4, L=1..6, all combined contents.")
    lines.append(f"Bad/source pairs={bad}; S/target pairs={target}; both compositions, lengths, monotonicity and content checked.")
    lines.append(f"Boundary incidences (overlap permitted): {boundaries}")
    cancellation = []
    for m in range(3, 41):
        if m == 5:
            continue
        half = sum((-1) ** j * comb(m, j) * (m - 2 * j) ** (m - 2)
                   for j in range((m - 1) // 2 + 1))
        assert half == 0
        cancellation.append(m)
    lines.append(f"Optional leading-coefficient cancellation exact checks: m={cancellation}; all zero.")
    lines.append(f"Completed in {perf_counter() - start:.3f} seconds.")
    lines.append("All tests passed. Finite computations are evidence, not proof of the unrestricted formula.")
    output = "\n".join(lines) + "\n"
    Path(__file__).with_name("review2_exact-output.txt").write_text(output)
    print(output, end="")


if __name__ == "__main__":
    main()
