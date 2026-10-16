#!/usr/bin/env python3
"""Bounded exact evidence for SMMC 2017 B4 (standard library only).

Enumerate reduced adjacent-swap words for reversal for 2 <= n <= 6.
Quotient by the complete crossing order on every labelled strand, not by
rotation/reflection and not by insertion history. Independently enumerate
binary signs on triples satisfying the one-sign-change condition on every
ordered four-set, for n <= 7. Equality with tilings uses published bijections;
these finite computations are evidence, not a proof of an asymptotic claim.

Invocation: python3 problems/2017-B4/computations/enumerate_small.py
No random choices. The watchdog aborts rather than reporting an incomplete
search as an exact answer. Each individual search has a 45 second limit.
"""

from collections import Counter
from itertools import combinations
from math import log2
import platform
from time import monotonic


def reduced_words(n, budget=45):
    start = monotonic()
    perm = list(range(n))
    histories = [[] for _ in range(n)]
    crossing_time = {}
    classes = Counter()
    signatures = set()
    triples = list(combinations(range(n), 3))
    total = 0
    nodes = 0

    def visit(depth):
        nonlocal total, nodes
        nodes += 1
        if nodes % 16384 == 0 and monotonic() - start > budget:
            raise TimeoutError(f"reduced-word search n={n} incomplete")
        if depth == n * (n - 1) // 2:
            total += 1
            key = tuple(tuple(h) for h in histories)
            classes[key] += 1
            signature = sum(
                (crossing_time[a, b] > crossing_time[b, c]) << i
                for i, (a, b, c) in enumerate(triples)
            )
            signatures.add(signature)
            return
        for i in range(n - 1):
            a, b = perm[i:i + 2]
            if a < b:
                perm[i], perm[i + 1] = b, a
                histories[a].append(b)
                histories[b].append(a)
                crossing_time[a, b] = depth
                visit(depth + 1)
                del crossing_time[a, b]
                histories[a].pop()
                histories[b].pop()
                perm[i], perm[i + 1] = a, b

    visit(0)
    histogram = dict(sorted(Counter(classes.values()).items()))
    return total, len(classes), histogram, signatures


def one_change_signs(n, budget=45):
    start = monotonic()
    # Old triples first, so constraints on a smaller initial interval close early.
    triples = sorted(combinations(range(n), 3), key=lambda t: (t[2], t))
    index = {t: i for i, t in enumerate(triples)}
    lex_index = {t: i for i, t in enumerate(combinations(range(n), 3))}
    packets = [tuple(index[t] for t in combinations(q, 3))
               for q in combinations(range(n), 4)]
    incident = [[] for _ in triples]
    for j, packet in enumerate(packets):
        for bit, var in enumerate(packet):
            incident[var].append((j, bit))
    allowed = [m for m in range(16)
               if sum(((m >> i) ^ (m >> (i + 1))) & 1
                      for i in range(3)) <= 1]
    compatible = {(mask, signs): any((a & mask) == signs for a in allowed)
                  for mask in range(16) for signs in range(16)
                  if signs & ~mask == 0}
    masks = [0] * len(packets)
    signs = [0] * len(packets)
    solutions = set()
    nodes = 0

    def visit(var, lex_signature):
        nonlocal nodes
        nodes += 1
        if nodes % 16384 == 0 and monotonic() - start > budget:
            raise TimeoutError(f"one-change search n={n} incomplete")
        if var == len(triples):
            solutions.add(lex_signature)
            return
        for value in (0, 1):
            valid = True
            for j, bit in incident[var]:
                masks[j] |= 1 << bit
                signs[j] |= value << bit
                valid &= compatible[masks[j], signs[j]]
            if valid:
                visit(var + 1, lex_signature |
                      (value << lex_index[triples[var]]))
            for j, bit in incident[var]:
                masks[j] &= ~(1 << bit)
                signs[j] &= ~(1 << bit)

    visit(0, 0)
    return solutions


def main():
    print(f"Python {platform.python_version()}; standard library only")
    print("Finite exhaustive computations; no symmetry quotient; no asymptotic proof")
    print("n reduced_words strand_order_classes triple_signs one_change_signs exact_set_match")
    for n in range(2, 8):
        signs = one_change_signs(n)
        if n <= 6:
            words, classes, histogram, reduced_signs = reduced_words(n)
            print(n, words, classes, len(reduced_signs), len(signs), reduced_signs == signs)
            print(f"  class_word_multiplicity_histogram={histogram}")
        else:
            print(n, "not_run", "not_run", "not_run", len(signs), "not_run")
        if n >= 3:
            all_triples = list(combinations(range(n), 3))
            old_positions = [i for i, t in enumerate(all_triples) if t[-1] < n - 1]
            children = Counter(sum(((s >> pos) & 1) << i
                                   for i, pos in enumerate(old_positions))
                               for s in signs)
            print(f"  one_change_extension_count: parents={len(children)} "
                  f"min={min(children.values())} max={max(children.values())} "
                  f"average={len(signs)/len(children):.12f}")
    # Published exact values, transcribed from SoCG 2024 Table 1, with 1,2
    # supplied by the convention for an empty/reversal network. Not newly enumerated.
    published = [1, 1, 2, 8, 62, 908, 24698, 1232944, 112018190,
                 18410581880, 5449192389984, 2894710651370536,
                 2752596959306389652, 4675651520558571537540,
                 14163808995580022218786390, 76413073725772593230461936736]
    print("Published C(n): n C(n) log2_C_over_n_squared [decimal is numerical evidence]")
    for n, count in enumerate(published, 1):
        print(n, count, f"{log2(count)/(n*n):.12f}")


if __name__ == "__main__":
    main()
