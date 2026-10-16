#!/usr/bin/env python3
"""Independent R2 checks. No imports from any author/reviewer program."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import time


def tapes(history: str) -> tuple[tuple[int, ...], tuple[int, ...]]:
    left, right = [], []
    for t, side in enumerate(history):
        (left if side == "L" else right).append(t % 2)
    return tuple(left), tuple(right)


def least_for_pair(left: tuple[int, ...], right: tuple[int, ...]) -> str | None:
    """Backward feasibility table, followed by lexicographic greedy path."""
    p, q = len(left), len(right)
    feasible = [bytearray(q + 1) for _ in range(p + 1)]
    feasible[p][q] = 1
    for i in range(p, -1, -1):
        for j in range(q, -1, -1):
            if i == p and j == q:
                continue
            bit = (i + j) % 2
            if i < p and left[i] == bit and feasible[i + 1][j]:
                feasible[i][j] = 1
            elif j < q and right[j] == bit and feasible[i][j + 1]:
                feasible[i][j] = 1
    if not feasible[0][0]:
        return None
    answer = []
    i = j = 0
    while i < p or j < q:
        bit = (i + j) % 2
        if i < p and left[i] == bit and feasible[i + 1][j]:
            answer.append("L")
            i += 1
        else:
            assert j < q and right[j] == bit and feasible[i][j + 1]
            answer.append("R")
            j += 1
    return "".join(answer)


def canonical(history: str) -> bool:
    return least_for_pair(*tapes(history)) == history


def path_count(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    """Independent forward counting recurrence, including odd total lengths."""
    p, q = len(left), len(right)
    rows = [[0] * (q + 1) for _ in range(p + 1)]
    rows[0][0] = 1
    for i in range(p + 1):
        for j in range(q + 1):
            value = rows[i][j]
            if not value:
                continue
            wanted = (i + j) % 2
            if i < p and left[i] == wanted:
                rows[i + 1][j] += value
            if j < q and right[j] == wanted:
                rows[i][j + 1] += value
    return rows[p][q]


def emit(value: object) -> None:
    print(json.dumps(value, sort_keys=True), flush=True)


def enumerate_factors(maximum: int, bounded_runs: bool = False) -> dict:
    """Induct on length, avoiding only already proved shorter bad factors.

    RR/LL restriction is from the independently audited cancellation lemma.
    A proper bad factor contains an earlier minimal bad factor, so each new
    noncanonical survivor is minimal. Both longest proper factors are also
    checked afresh without relying on the pruning argument.
    """
    known: dict[int, set[str]] = {}
    layers = []
    for n in range(4, maximum + 1):
        prior_lengths = tuple(sorted(known))
        found = []
        visited = 0
        tested = 0
        start = time.monotonic()

        def walk(prefix: str) -> None:
            nonlocal visited, tested
            visited += 1
            if visited % 100000 == 0:
                emit({"checkpoint_length": n, "visited": visited, "tested": tested})
            m = len(prefix)
            if m >= n - 2:
                choices = "L"
            else:
                choices = "LR"
            for side in choices:
                word = prefix + side
                k = len(word)
                if bounded_runs and k >= 3 and word[-3:] in ("LLL", "RRR"):
                    continue
                if any(k >= j and word[-j:] in known[j] for j in prior_lengths):
                    continue
                if k < n:
                    walk(word)
                else:
                    tested += 1
                    if not canonical(word):
                        assert canonical(word[:-1]) and canonical(word[1:]), word
                        found.append(word)

        walk("RR")
        if found:
            known[n] = set(found)
        row = {"n": n, "count": len(found), "visited": visited,
               "tested": tested, "seconds": time.monotonic() - start,
               "factors": sorted(found)}
        layers.append(row)
        emit({k: v for k, v in row.items() if k != "factors"})
    all_words = sorted((w for values in known.values() for w in values), key=lambda w: (len(w), w))
    overlaps = []
    containments = []
    for a in all_words:
        for b in all_words:
            if a != b and a in b:
                containments.append([a, b])
            for k in range(1, min(len(a), len(b))):
                if a[-k:] == b[:k]:
                    overlaps.append([a, b, k])
    assert not overlaps and not containments
    return {"layers": layers, "total": len(all_words), "bounded_runs": bounded_runs, "overlaps": overlaps,
            "proper_containments": containments, "all_words": all_words}


def brute_small(maximum: int) -> dict:
    """Enumerate every history in lex order and group by raw output pair.

    This checks the DP against a different method, including lengths < 4,
    and gives canonical counts to check the reciprocal coefficients.
    """
    data = []
    discovered = set()
    for n in range(maximum + 1):
        by_pair = {}
        minima = []
        for mask in range(1 << n):
            word = "".join("R" if mask >> (n - 1 - i) & 1 else "L" for i in range(n))
            pair = tapes(word)
            by_pair.setdefault(pair, word)
            assert canonical(word) == (by_pair[pair] == word), (n, word)
            if by_pair[pair] != word and not any(f in word for f in discovered):
                assert canonical(word[:-1]) and canonical(word[1:])
                minima.append(word)
        discovered.update(minima)
        data.append({"n": n, "canonical_count": len(by_pair), "minimal_bad": minima})
        emit({"brute_length": n, "canonical_count": len(by_pair), "minimal_bad_count": len(minima)})
    return {"rows": data}


def exact_signs(counts: dict[int, int]) -> dict:
    def p(x: Fraction) -> Fraction:
        return sum((m * x**n for n, m in counts.items()), Fraction())
    def dp(x: Fraction) -> Fraction:
        return sum((n * m * x**(n-1) for n, m in counts.items()), Fraction())
    def e(x: Fraction) -> Fraction:
        return 1 - Fraction(48, 25) * x + sum((Fraction(25-n, 25)*m*x**n for n, m in counts.items()), Fraction())
    def encode(x: Fraction) -> dict:
        return {"numerator": str(x.numerator), "denominator": str(x.denominator), "sign": (x > 0) - (x < 0)}
    lower_x = Fraction(100000, 176521)
    upper_x = Fraction(100000000, 183516197)
    value = {"counts": counts, "E_at_lower_x": encode(e(lower_x)),
             "E_at_three_fifths": encode(e(Fraction(3, 5))),
             "D_at_upper_x": encode(1 - 2*upper_x + p(upper_x)),
             "Dprime_at_upper_x": encode(-2 + dp(upper_x)),
             "accepted_radius_anchor": encode(395397 * Fraction(3, 5)**24 - 1)}
    assert value["E_at_lower_x"]["sign"] == -1
    assert value["E_at_three_fifths"]["sign"] == -1
    assert value["D_at_upper_x"]["sign"] == 1
    assert value["Dprime_at_upper_x"]["sign"] == -1
    assert value["accepted_radius_anchor"]["sign"] == 1
    return value


def family_checks() -> dict:
    rigid = []
    for p in range(1, 11):
        for q in range(1, 11):
            u = tuple(map(int, "01" + "10"*q + "01"))
            v = tuple(map(int, "01" + "10"*p + "01"))
            k = "LLR" + "L"*(2*q) + "RL" + "R"*(2*p) + "LRR"
            h = "RRL" + "R"*(2*p) + "LR" + "L"*(2*q) + "RLL"
            assert tapes(k) == tapes(h) == (u, v)
            assert path_count(u, v) == 2
            assert least_for_pair(u, v) == k
            assert canonical(h[:-1]) and canonical(h[1:])
            rigid.append([p, q, len(h)])
    stairs = []
    for n in range(1, 16):
        runs = list(range(1, n + 1)) + list(range(n, 0, -1))
        word = tuple(bit for i, r in enumerate(runs) for bit in [i % 2]*r)
        h = "RR" + "".join("LR"*j + "R" for j in range(1, n)) + "LR"*(n-1) + "LL" + "".join("RL"*j + "L" for j in range(n-1, 0, -1))
        other = h.translate(str.maketrans("LR", "RL"))
        assert len(h) == 2*n*(n+1)
        assert tapes(h) == tapes(other) == (word, word)
        assert path_count(word, word) == 2
        assert least_for_pair(word, word) == other
        assert canonical(h[:-1]) and canonical(h[1:])
        # Determine every local branch, and count remaining equal-bit runs.
        i = j = 0
        decisions = []
        for t, side in enumerate(h):
            bit = t % 2
            if i < len(word) and j < len(word) and word[i] == word[j] == bit:
                def remaining(start: int) -> int:
                    stop = start
                    while stop < len(word) and word[stop] == bit:
                        stop += 1
                    return stop-start
                a, b = remaining(i), remaining(j)
                decisions.append({"t": t, "side": side, "chosen_run": a if side == "L" else b,
                                  "other_run": b if side == "L" else a,
                                  "other_total": len(word) - (j if side == "L" else i)})
                assert h[t:t+2] == side*2
                assert (a if side == "L" else b) == 1
                if t:
                    r = b if side == "L" else a
                    total = len(word) - (j if side == "L" else i)
                    assert r >= 2 or (r == 1 and total == 1)
            if side == "L":
                i += 1
            else:
                j += 1
        stairs.append({"n": n, "history_length": len(h), "branch_locations": decisions})
    return {"rigid_parameter_rows": rigid, "staircase_rows": stairs}


def certificate_comparison(enumeration_path: str) -> dict:
    """Read raw certificates only after the independent enumeration exists."""
    problem = Path(__file__).resolve().parents[1]
    own = json.loads(Path(enumeration_path).read_text())["result"]
    full = json.loads((problem / "computations/secondpass-full-obstruction24-v2.json").read_text())
    initial = json.loads((problem / "computations/secondpass-probe20.json").read_text())
    # Do not depend on an author program or inferred JSON structure.
    emit({"author_initial_keys": sorted(initial), "author_full_keys": sorted(full)})
    author_words = [x["larger"] for x in full["new_minimal_forbidden"]]
    initial_rows = initial.get("minimal_forbidden", initial.get("minimal_bad_factors"))
    if initial_rows is None:
        raise ValueError("Inspect initial certificate key before comparing")
    author_words += [x["larger"] if isinstance(x, dict) else x for x in initial_rows]
    assert set(author_words) == set(own["all_words"])
    assert len(author_words) == len(set(author_words)) == 143
    suffix = "-final" if Path(enumeration_path).stem.endswith("-final") else ""
    signs = json.loads((Path(__file__).resolve().parent / f"secondpass-review-2-signs{suffix}.json").read_text())["result"]
    author_signs = json.loads((problem / "computations/secondpass-renewal24.json").read_text())
    comparisons = {"E_at_lower_x": "E_lower_r0", "E_at_three_fifths": "E_three_fifths",
                   "D_at_upper_x": "D_upper_x", "Dprime_at_upper_x": "D_derivative_upper_x"}
    for a, b in comparisons.items():
        assert int(signs[a]["numerator"]) == author_signs[b]["numerator"]
        assert int(signs[a]["denominator"]) == author_signs[b]["denominator"]
    brute = json.loads((Path(__file__).resolve().parent / f"secondpass-review-2-brute{suffix}.json").read_text())["result"]["rows"]
    coefficients = [1]
    f = Counter(map(len, own["all_words"]))
    for n in range(1, 25):
        coefficients.append(2*coefficients[-1] - sum(f[j]*coefficients[n-j] for j in range(1, n+1)))
    assert all(coefficients[row["n"]] == row["canonical_count"] for row in brute)
    return {"exact_word_sets_agree": True, "number_of_words": 143,
            "four_rational_values_agree": True, "renewal_coefficients": coefficients,
            "brute_coefficients_agree_through": max(row["n"] for row in brute)}


def extra_checks(enumeration_path: str) -> dict:
    def bits(text: str) -> tuple[int, ...]:
        return tuple(map(int, text))
    forced = []
    for p in range(11):
        for q in range(11):
            u = bits("011" + "01"*p + "00" + "01"*q)
            v = bits("011" + "01"*(p+q+1))
            # A=LL, B=LR, C=RL, D=RR at even pair boundaries.
            witness = "LL" + "RL" + "LL"*p + "LR"*2 + "LL"*q + "RR"*(p+q+1)
            assert tapes(witness) == (u, v)
            assert path_count(u, v) > 0
            assert path_count(u, v[2:]) == 0
            forced.append([p, q])
    first_u, first_v = bits("0100"), bits("01100111")
    assert path_count(first_u, first_v) > 0
    assert path_count(first_u[2:], first_v) == 0
    a, b, c = bits("000"), bits("010111101"), bits("011001111")
    assert path_count(a, b) > 0 and path_count(a, c) == 0
    def stats(word: tuple[int, ...]) -> list:
        level = 0
        levels = [0]
        for bit in word:
            level += 1 if bit == 0 else -1
            levels.append(level)
        return [len(word), level, min(levels), max(levels), word[0], word[-1]]
    assert stats(b) == stats(c)
    h = "RRLRRLRLLRLRLLRLL"
    inflated = "RRLRRLRLLRLLLRLLRLL"
    assert not canonical(h) and canonical(h[:-1]) and canonical(h[1:])
    assert not canonical(inflated)
    smaller_proper_prefixes = [{"prefix": inflated[:j], "witness": least_for_pair(*tapes(inflated[:j]))}
                              for j in range(1, len(inflated)) if not canonical(inflated[:j])]
    assert smaller_proper_prefixes
    full = json.loads(Path(enumeration_path).read_text())["result"]
    suffix = "-final" if Path(enumeration_path).stem.endswith("-final") else ""
    bounded = json.loads((Path(__file__).resolve().parent / f"secondpass-review-2-bounded{suffix}.json").read_text())["result"]
    assert len(bounded["all_words"]) == 14
    assert all(path_count(*tapes(w)) == 2 for w in bounded["all_words"])
    import itertools
    compressed = []
    for word in full["all_words"]:
        compressed_word = "".join(side*(1 + (sum(1 for _ in group)-1) % 2)
                                  for side, group in itertools.groupby(word))
        assert compressed_word in full["all_words"]
        compressed.append(compressed_word)
    return {"fixed_window_parameters_checked": forced,
            "small_greedy_counterexample": {"u": first_u, "v": first_v,
                "witness": least_for_pair(first_u, first_v)},
            "range_counterexample_statistics": {"left": stats(a), "right": stats(b)},
            "inflation_counterexample_noncanonical_proper_prefixes": smaller_proper_prefixes,
            "parity_compressed_minimal_factors": sorted(set(compressed), key=lambda w: (len(w), w)),
            "all_143_compress_to_minimal": True, "bounded_14_all_have_two_histories": True}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["enumerate", "brute", "signs", "families", "compare", "extras"])
    parser.add_argument("output")
    parser.add_argument("--maximum", type=int, default=24)
    parser.add_argument("--enumeration")
    parser.add_argument("--bounded-runs", action="store_true")
    args = parser.parse_args()
    source_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    emit({"start": True, "pid": os.getpid(), "mode": args.mode, "maximum": args.maximum,
          "python": sys.version, "platform": platform.platform(), "source_sha256": source_sha256})
    start = time.monotonic()
    if args.mode == "enumerate":
        result = enumerate_factors(args.maximum, args.bounded_runs)
    elif args.mode == "brute":
        result = brute_small(args.maximum)
    elif args.mode == "signs":
        source = json.loads(Path(args.enumeration).read_text())
        counts = {row["n"]: row["count"] for row in source["result"]["layers"] if row["count"]}
        result = exact_signs(counts)
    elif args.mode == "families":
        result = family_checks()
    elif args.mode == "compare":
        result = certificate_comparison(args.enumeration)
    else:
        result = extra_checks(args.enumeration)
    wrapped = {"mode": args.mode, "python": sys.version, "source_sha256": source_sha256,
               "elapsed_seconds": time.monotonic()-start, "result": result}
    Path(args.output).write_text(json.dumps(wrapped, indent=2, sort_keys=True) + "\n")
    emit({"completed": True, "seconds": wrapped["elapsed_seconds"], "output": args.output,
          "sha256": hashlib.sha256(Path(args.output).read_bytes()).hexdigest()})


if __name__ == "__main__":
    main()
