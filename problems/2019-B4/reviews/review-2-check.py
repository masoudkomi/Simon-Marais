"""Independent review R2 checks, 2019 B4(b), standard library only.

This does not import or execute the author's computation programs.  It audits
proof version 1, computes the suffix automaton from forbidden strings, checks
finite cases by exhaustive histories, and independently enumerates C_12 by
splitting the 24-move source into two directly enumerated 12-move halves.
All finite output is evidence, not proof of an unrestricted assertion.
"""
import hashlib
import itertools
import json
import os
import platform
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
YEAR = ROOT / "problems/2019-B4"
OUT = YEAR / "reviews/review-2-evidence.json"
FORBIDDEN = ("RRLL", "RRLRRLRLLRLL")
REPLACEMENTS = ((FORBIDDEN[0], "LLRR"),
                (FORBIDDEN[1], "LLRLLRLRRLRR"))


def checkpoint(message):
    print(f"{time.monotonic() - START:.3f}s {message}", flush=True)


def context(history, first_bit=0):
    source = [str(first_bit ^ (i % 2)) for i in range(len(history))]
    left = [source[i] for i, side in enumerate(history) if side == "L"]
    right = [source[i] for i, side in enumerate(history) if side == "R"]
    return "".join(reversed(left)), "".join(right)


def compose(a, b):
    return b[0] + a[0], a[1] + b[1]


def word(pair):
    return pair[0] + "1" + pair[1]


def auto_step(state, letter, states):
    extended = state + letter
    if any(extended.endswith(f) for f in FORBIDDEN):
        return None
    return max((s for s in states if extended.endswith(s)), key=len)


def check_certificate():
    cert = json.loads((YEAR / "computations/upper-certificate-2026-10-16.json").read_text())
    states = sorted({f[:i] for f in FORBIDDEN for i in range(len(f))},
                    key=lambda s: (len(s), s))
    assert all(not any(f in s for f in FORBIDDEN) for s in states)
    assert states == cert["states"]
    rows = []
    transitions = []
    for state in states:
        row = [0] * len(states)
        trans = {}
        for letter in "LR":
            target = auto_step(state, letter, states)
            trans[letter] = target
            if target is not None:
                row[states.index(target)] += 1
        rows.append(row)
        transitions.append(trans)
    assert rows == cert["matrix"]
    assert transitions == cert["transitions"]
    v = cert["positive_integer_weights"]
    assert len(v) == len(rows) and min(v) > 0
    av = [sum(x * y for x, y in zip(row, v)) for row in rows]
    num, den = cert["q_numerator"], cert["q_denominator"]
    slacks = [num * x - den * y for x, y in zip(v, av)]
    assert slacks == cert["strict_integer_slacks"]
    assert min(slacks) > 0
    ratios = [Fraction(y, x) for x, y in zip(v, av)]
    qp = max(ratios)
    assert qp < Fraction(num, den)
    relations = []
    for before, after in REPLACEMENTS:
        assert after < before and len(before) == len(after)
        pairs = []
        for bit in (0, 1):
            a, b = context(before, bit), context(after, bit)
            assert a == b
            pairs.append(list(a))
        relations.append({"before": before, "after": after,
                          "contexts_first_0_and_1": pairs})
    counts, vector = [], [1] * len(states)
    for t in range(17):
        counts.append(vector[0])
        vector = [sum(x * y for x, y in zip(row, vector)) for row in rows]
    checkpoint("exact automaton and integer weight certificate verified")
    return {"states": states, "matrix": rows, "transitions": transitions,
            "relations": relations, "strict_integer_slacks": slacks,
            "q_prime_exact": f"{qp.numerator}/{qp.denominator}",
            "q_prime_decimal_evidence_only": float(qp),
            "q_prime_maximizing_state_indices": [i for i, r in enumerate(ratios) if r == qp],
            "avoiding_counts_t_0_through_16": counts}


def check_small_cases(automaton):
    by_t, words_by_n, histories_by_n = {}, {}, {}
    rows = []
    for t in range(17):
        marked = set()
        minima = {}
        avoiding = 0
        for letters in itertools.product("LR", repeat=t):
            h = "".join(letters)
            pair = context(h)
            marked.add(pair)
            w = word(pair)
            minima.setdefault(w, h)
            avoiding += not any(f in h for f in FORBIDDEN)
        assert all(not any(f in h for f in FORBIDDEN) for h in minima.values())
        assert avoiding == automaton["avoiding_counts_t_0_through_16"][t]
        assert len(minima) <= avoiding
        fibre = Counter(word(pair) for pair in marked)
        assert max(fibre.values()) <= t + 1
        for w in minima:
            for p in range(t + 1):
                if w[p] == "1" and (w[:p], w[p + 1:]) in marked:
                    assert (w[:p], w[p + 1:]) in marked
        by_t[t] = marked
        words_by_n[t + 1] = set(minima)
        histories_by_n[t + 1] = minima
        rows.append({"moves": t, "marked": len(marked), "words": len(minima),
                     "max_fibre": max(fibre.values()), "avoiding_histories": avoiding})
    for k in range(5):
        for j in range(5 - k):
            composed = {compose(a, b) for a in by_t[2 * k] for b in by_t[2 * j]}
            assert composed == by_t[2 * (k + j)]
    injection_cases = 0
    for k in range(1, 4):
        groups = defaultdict(list)
        for pair in by_t[2 * k]:
            groups[len(pair[0])].append(pair)
        for p, group in groups.items():
            for q in range(1, 4):
                seen = set()
                for seq in itertools.product(group, repeat=q):
                    final = ("", "")
                    for pair in seq:
                        final = compose(final, pair)
                    w = word(final)
                    assert w not in seen
                    seen.add(w)
                    l, r = w[:q * p], w[q * p + 1:]
                    if p:
                        left_parts = [l[i * p:(i + 1) * p] for i in range(q)][::-1]
                    else:
                        left_parts = [""] * q
                    width = 2 * k - p
                    if width:
                        right_parts = [r[i * width:(i + 1) * width] for i in range(q)]
                    else:
                        right_parts = [""] * q
                    assert tuple(zip(left_parts, right_parts)) == seq
                injection_cases += 1
    substitution_cases = 0
    for m in (1, 3, 5, 7):
        for n in range(1, 9):
            groups = defaultdict(list)
            for y, h in histories_by_n[n].items():
                groups[h.count("L")].append(y)
            p, group = max(groups.items(), key=lambda kv: len(kv[1]))
            assert n * len(group) >= len(words_by_n[n])
            seen = set()
            for x in words_by_n[m]:
                for y in group:
                    w = y[:p] + x + y[p + 1:]
                    assert w in words_by_n[m + n - 1]
                    assert w not in seen
                    seen.add(w)
                    assert w[p:p + m] == x
                    assert w[:p] + "1" + w[p + m:] == y
            substitution_cases += 1
    checkpoint("all-history finite counterexample search through 16 moves completed")
    return {"all_history_rows": rows,
            "composition_k_plus_j_at_most": 4,
            "fixed_position_injectivity_cases": injection_cases,
            "fixed_position_test_parameters": {"k": [1, 2, 3], "q": [1, 2, 3], "positions": "all"},
            "odd_seed_substitution_cases": substitution_cases,
            "odd_seed_substitution_parameters": {"m": [1, 3, 5, 7], "n_min": 1, "n_max": 8}}


def intbits(bits):
    value = 0
    for bit in bits:
        value = 2 * value + bit
    return value


def direct_half_contexts():
    groups = [set() for _ in range(13)]
    for mask in range(1 << 12):
        chosen = [i % 2 for i in range(12) if (mask >> i) & 1]
        other = [i % 2 for i in range(12) if not ((mask >> i) & 1)]
        groups[mask.bit_count()].add((intbits(reversed(chosen)), intbits(other)))
    checkpoint(f"all 4096 12-move histories independently give {sum(map(len, groups))} contexts")
    return groups


def count_24_contexts():
    groups = direct_half_contexts()
    counts, hashes, candidate_pairs = [], [], []
    for p in range(25):
        seen = set()
        candidates = 0
        for p1 in range(max(0, p - 12), min(12, p) + 1):
            p2 = p - p1
            for l1, r1 in groups[p1]:
                for l2, r2 in groups[p2]:
                    # Twelve source moves in each half: parity restarts at 0.
                    # Pack the final left/right words, with external split p.
                    left = (l2 << p1) | l1
                    right = (r1 << (12 - p2)) | r2
                    seen.add((left << (24 - p)) | right)
                    candidates += 1
        digest = hashlib.sha256()
        for value in sorted(seen):
            digest.update(value.to_bytes(3, "big"))
        counts.append(len(seen))
        hashes.append(digest.hexdigest())
        candidate_pairs.append(candidates)
        checkpoint(f"24 moves, left length {p}: {len(seen)} distinct / {candidates} half-context pairs")
    assert sum(counts) == 2985943
    assert max(counts) == 395397
    assert [i for i, n in enumerate(counts) if n == max(counts)] == [12]
    return {"method": "direct 12-move history subsets, then independent two-half composition; fixed-split packed context integers",
            "half_history_count": 4096, "half_position_counts": list(map(len, groups)),
            "half_distinct_contexts": sum(map(len, groups)),
            "moves": 24, "position_counts": counts, "total": sum(counts),
            "maximum": max(counts), "maximizing_left_lengths": [12],
            "candidate_half_context_pairs_by_position": candidate_pairs,
            "sorted_three_byte_context_sha256_by_position": hashes,
            "lower_root_decimal_evidence_only": max(counts) ** (1 / 24),
            "upper_root_decimal_evidence_only": sum(counts) ** (1 / 24)}


if __name__ == "__main__":
    START = time.monotonic()
    checkpoint(f"PID={os.getpid()} Python={platform.python_version()}")
    result = {"status": "independent R2 finite evidence; no unrestricted claim proved by tests",
              "python": platform.python_version(), "child_pid": os.getpid(),
              "proof_sha256": hashlib.sha256((YEAR / "proof.md").read_bytes()).hexdigest()}
    result["certificate"] = check_certificate()
    result["finite_counterexample_search"] = check_small_cases(result["certificate"])
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    result["24_move_enumeration"] = count_24_contexts()
    result["elapsed_seconds"] = time.monotonic() - START
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    checkpoint(f"all checks passed; output {OUT}")
