#!/usr/bin/env python3
"""Exact finite evidence for 2019 B4(b), using Python's standard library only.

Run from the repository root with the bundled Python named in README.md.
No unrestricted claim follows just from these finite enumerations.
"""
import argparse
from collections import Counter
from functools import lru_cache
from itertools import combinations
import json
import platform


def forward_counts(max_n):
    words = {1}
    counts = {}
    for n in range(1, max_n + 1):
        counts[n] = len(words)
        if n != max_n:
            bit = 1 - n % 2
            words = {(bit << n) | w for w in words} | {
                (w << 1) | bit for w in words
            }
    return counts


def accepted_by_deletion(w):
    """Independent interval recursion, with no call to the forward generator."""
    @lru_cache(None)
    def accepted(i, j):
        if j - i == 1:
            return w[i] == "1"
        expected = str((j - i) % 2)
        return ((w[i] == expected and accepted(i + 1, j)) or
                (w[j - 1] == expected and accepted(i, j - 1)))
    return accepted(0, len(w))


def context_rows(max_t, b):
    # At length t, encode (contextword, leftlength) as (leftlength << t)|word.
    # contextword is final-left followed by final-right, with the seed removed.
    contexts = {0}
    rows = []
    for t in range(max_t + 1):
        mask = (1 << t) - 1
        by_position = Counter(c >> t for c in contexts)
        max_count = max(by_position.values())
        maximizing_positions = sorted(p for p, c in by_position.items()
                                      if c == max_count)
        row = {"moves": t, "marked_contexts": len(contexts),
               "max_fixed_position_contexts": max_count,
               "maximizing_left_lengths": maximizing_positions,
               "position_counts": [by_position[p] for p in range(t + 1)]}
        if t + 1 in b:
            with_seed = set()
            for c in contexts:
                p, w = c >> t, c & mask
                right_len = t - p
                left, right = w >> right_len, w & ((1 << right_len) - 1)
                with_seed.add((((left << 1) | 1) << right_len) | right)
            assert len(with_seed) == b[t + 1], (t, len(with_seed), b[t + 1])
            row["distinct_words_after_seed_insertion"] = len(with_seed)
        rows.append(row)
        if t == max_t:
            break
        bit = t % 2  # first appended bit is 0
        new = set()
        for c in contexts:
            p, w = c >> t, c & mask
            new.add(((p + 1) << (t + 1)) | (bit << t) | w)
            new.add((p << (t + 1)) | (w << 1) | bit)
        contexts = new
    return rows


def fixed_split_by_subsets(t, p):
    """Independent exhaustive enumeration of which source positions go left.

    This uses chronological left order, not final left order; reversal is a
    bijection, so its count must agree with context_rows at leftlength p.
    """
    pairs = set()
    histories = 0
    for chosen in combinations(range(t), p):
        chosen_mask = sum(1 << i for i in chosen)
        left = right = 0
        for i in range(t):
            if chosen_mask & (1 << i):
                left = (left << 1) | (i % 2)
            else:
                right = (right << 1) | (i % 2)
        pairs.add((left << (t - p)) | right)
        histories += 1
    return {"moves": t, "left_length": p, "histories_examined": histories,
            "distinct_contexts": len(pairs)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=25)
    parser.add_argument("--max-t", type=int, default=24)
    parser.add_argument("--deletion-audit", type=int, default=14)
    parser.add_argument("--fixed-split", default="24,12")
    args = parser.parse_args()
    b = forward_counts(args.max_n)
    for n in range(1, args.deletion_audit + 1):
        accepted = sum(accepted_by_deletion(format(w, f"0{n}b"))
                       for w in range(1 << n))
        assert accepted == b[n], (n, accepted, b[n])
    rows = context_rows(args.max_t, b)
    t, p = map(int, args.fixed_split.split(","))
    independent = fixed_split_by_subsets(t, p)
    if t <= args.max_t:
        assert independent["distinct_contexts"] == rows[t]["position_counts"][p]
    print(json.dumps({"status": "finite computational evidence, not an unrestricted proof",
                      "python": platform.python_version(), "parameters": vars(args),
                      "b_n": b, "deletion_audit_through_n": args.deletion_audit,
                      "marked_context_rows": rows,
                      "independent_fixed_split": independent}, indent=2))


if __name__ == "__main__":
    main()
