"""Independent blind R1 finite checks. No author/reviewer code is imported.

Uses only the standard library. The outer runner supplies the hard timeout.
Full minimal-factor discovery is inductive, with exact tape-grid path counts;
the smaller unrestricted history enumeration uses a different partition method.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import platform
import re
import time
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

BASE = Path("problems/2019-B4")
OUT = BASE / "reviews/secondpass-review-1-evidence.json"
START = time.monotonic()
RESULT = {"status": "in progress; bounded finite evidence only", "python": platform.python_version()}


def checkpoint(label):
    RESULT["elapsed_seconds"] = time.monotonic() - START
    OUT.write_text(json.dumps(RESULT, indent=2) + "\n")
    print(label, "elapsed", round(RESULT["elapsed_seconds"], 3), flush=True)


def context(h):
    return tuple(bytes(i & 1 for i, side in enumerate(h) if side == s) for s in "LR")


def paths(u, v):
    """Backward exact counts at consumed-prefix vertices, then lex-first path."""
    m, n = len(u), len(v)
    grid = [[0] * (n + 1) for _ in range(m + 1)]
    grid[m][n] = 1
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i == m and j == n:
                continue
            bit = (i + j) & 1
            grid[i][j] = ((grid[i + 1][j] if i < m and u[i] == bit else 0)
                          + (grid[i][j + 1] if j < n and v[j] == bit else 0))
    if not grid[0][0]:
        return None, 0
    i = j = 0
    h = []
    while i + j < m + n:
        bit = (i + j) & 1
        if i < m and u[i] == bit and grid[i + 1][j]:
            h.append("L")
            i += 1
        else:
            assert j < n and v[j] == bit and grid[i][j + 1]
            h.append("R")
            j += 1
    return "".join(h), grid[0][0]


def least(h):
    return paths(*context(h))[0]


def automaton(forbidden):
    # States are proper forbidden prefixes. Construct transitions directly by
    # longest-suffix search, without using an author trie/failure implementation.
    prefixes = {""}
    for f in forbidden:
        prefixes.update(f[:j] for j in range(1, len(f)))
    words = sorted(prefixes)
    index = {w: i for i, w in enumerate(words)}
    moves = []
    for w in words:
        row = []
        for x in "LR":
            t = w + x
            if any(t.endswith(f) for f in forbidden):
                row.append(-1)
                continue
            while t not in prefixes:
                t = t[1:]
            row.append(index[t])
        moves.append(row)
    return moves, index[""]


def discover(maximum, bounded=False):
    found = []
    layers = []
    records = []
    for n in range(4, maximum + 1):
        trans, initial = automaton(found)
        stack = [("", initial)]
        nodes = leaves = 0
        new = []
        while stack:
            h, state = stack.pop()
            nodes += 1
            assert nodes <= 2_000_000, (n, nodes)
            if len(h) == n:
                leaves += 1
                witness, count = paths(*context(h))
                assert witness is not None
                if witness != h:
                    # Independently check actual minimality rather than rely
                    # only on the inductive shorter-factor pruning argument.
                    assert least(h[:-1]) == h[:-1]
                    assert least(h[1:]) == h[1:]
                    new.append(h)
                    records.append({"history": h, "canonical": witness, "history_count": count})
                continue
            pos = len(h)
            choices = "R" if pos < 2 else "L" if pos >= n - 2 else "LR"
            for x in reversed(choices):
                if bounded and len(h) >= 2 and h[-2:] == x * 2:
                    continue
                dest = trans[state][x == "R"]
                if dest >= 0:
                    stack.append((h + x, dest))
        found.extend(new)
        layers.append({"n": n, "nodes": nodes, "candidate_tapes": leaves, "new_count": len(new)})
        print("bounded" if bounded else "full", n, "new", len(new), "nodes", nodes, "leaves", leaves, flush=True)
    return found, layers, records


full, layers, records = discover(24)
RESULT["full_obstructions"] = {"maximum": 24, "total": len(full), "layers": layers, "records": records}
checkpoint("full discovery complete")

# Completely unrestricted enumeration of histories to length 16, quotienting
# by literal tape pairs. This does not use the prefix/suffix restriction or DP.
brute_f = []
brute_rows = []
for n in range(17):
    first = {}
    new = []
    for letters in itertools.product("LR", repeat=n):
        h = "".join(letters)
        tape_pair = context(h)
        if tape_pair not in first:
            first[tape_pair] = h
        elif not any(f in h for f in brute_f):
            new.append(h)
    brute_f.extend(new)
    brute_rows.append({"n": n, "contexts": len(first), "minimal_bad": len(new)})
assert sorted(brute_f) == sorted(h for h in full if len(h) <= 16)
RESULT["unrestricted_histories_through_16"] = brute_rows
checkpoint("unrestricted comparison complete")

# No proper factor containment or overlaps, including self overlaps.
assert len(set(full)) == len(full)
for a in full:
    for b in full:
        assert a == b or a not in b
        assert all(a[-j:] != b[:j] for j in range(1, min(len(a), len(b))))
RESULT["factor_free_and_nonoverlapping"] = True

# Exact formal reciprocal coefficients. Compare through 16 with the direct
# context enumeration, including both odd and even lengths.
fn = Counter(map(len, full))
cn = [1]
for n in range(1, 41):
    cn.append(2 * cn[-1] - sum(v * cn[n - j] for j, v in fn.items() if j <= n))
assert cn[:17] == [r["contexts"] for r in brute_rows]
RESULT["finite_reciprocal_coefficients_through_40"] = cn

def P(x):
    return sum((v * x**n for n, v in fn.items()), Q(0))

def Pprime(x):
    return sum((n * v * x**(n - 1) for n, v in fn.items()), Q(0))

def D(x):
    return 1 - 2*x + P(x)

def E(x):
    return 1 - Q(48, 25)*x + sum((Q(25-n, 25)*v*x**n for n, v in fn.items()), Q(0))

points = {"D_upper": D(Q(100000000, 183516197)),
          "Dprime_upper": -2 + Pprime(Q(100000000, 183516197)),
          "E_lower": E(Q(100000, 176521)),
          "E_three_fifths": E(Q(3, 5)),
          "accepted_lower_implies_R_lt_three_fifths": 395397*Q(3, 5)**24}
assert points["D_upper"] > 0
assert points["Dprime_upper"] < 0
assert points["E_lower"] < 0
assert points["E_three_fifths"] < 0
assert points["accepted_lower_implies_R_lt_three_fifths"] > 1
RESULT["exact_signs"] = {k: {"numerator": v.numerator, "denominator": v.denominator, "decimal_evidence": float(v)} for k, v in points.items()}
RESULT["full_counts"] = dict(sorted(fn.items()))
checkpoint("rational signs complete")

# Reconstruct both displayed collision histories from the blocked formula.
generator = {"A": "LL", "B": "LR", "C": "RL", "D": "RR"}
def unblock(s):
    return "".join(generator[x] for x in s)

families = []
for p in range(1, 10):
    for q in range(1, 10):
        u, v = bytes(map(int, "01" + "10"*q + "01")), bytes(map(int, "01" + "10"*p + "01"))
        k = unblock("AC" + "A"*(q-1) + "BB" + "D"*(p-1) + "CD")
        h = unblock("DB" + "D"*(p-1) + "CC" + "A"*(q-1) + "BA")
        canonical, count = paths(u, v)
        assert count == 2 and canonical == k and context(h) == (u, v)
        assert k == "LLR" + "L"*(2*q) + "RL" + "R"*(2*p) + "LRR"
        assert h == "RRL" + "R"*(2*p) + "LR" + "L"*(2*q) + "RLL"
        assert least(h[:-1]) == h[:-1] and least(h[1:]) == h[1:]
        families.append({"p": p, "q": q, "histories": count})
RESULT["rigid_family_1_to_9"] = families

stairs = []
for n in range(1, 14):
    runs = list(range(1, n+1)) + list(range(n, 0, -1))
    u = bytes(b for run, k in enumerate(runs) for b in [run & 1] * k)
    h = ("RR" + "".join("LR"*j + "R" for j in range(1, n)) + "LR"*(n-1) + "LL"
         + "".join("RL"*j + "L" for j in range(n-1, 0, -1)))
    k = h.translate(str.maketrans("LR", "RL"))
    canonical, count = paths(u, u)
    assert count == 2 and canonical == k and context(h) == (u, u)
    assert least(h[:-1]) == h[:-1] and least(h[1:]) == h[1:]
    assert "LLL" not in h and "RRR" not in h
    # Audit every simultaneous-head choice along the explicit history. At
    # every noninitial choice, the rejected side exposes the same bit or
    # exhausts while the other head has that bit; these are dead after 1 move.
    i = j = 0
    choices = []
    for t, side in enumerate(h):
        bit = t & 1
        if i < len(u) and j < len(u) and u[i] == u[j] == bit:
            chosen = i if side == "L" else j
            other = j if side == "L" else i
            a = next((z-chosen for z in range(chosen+1, len(u)) if u[z] != bit), len(u)-chosen)
            b = next((z-other for z in range(other+1, len(u)) if u[z] != bit), len(u)-other)
            assert a == 1 and chosen+1 < len(u)
            if t:
                assert b >= 2 or other+1 == len(u)
            choices.append({"t": t, "side": side, "chosen_run": a, "other_run": b, "other_tape_remaining": len(u)-other})
        if side == "L":
            assert u[i] == bit
            i += 1
        else:
            assert u[j] == bit
            j += 1
    stairs.append({"n": n, "history_length": len(h), "histories": count, "both_head_choices": choices})
RESULT["staircase_1_to_13"] = stairs
checkpoint("unbounded-family finite stress tests complete")

# Exhaustive bounded-run check is a separate induction: every factor of a
# bounded-run word is itself bounded-run. It is not used for the full counts.
bounded, bounded_layers, bounded_records = discover(26, bounded=True)
assert sorted(h for h in bounded if len(h) <= 24) == sorted(h for h in full if "LLL" not in h and "RRR" not in h)
RESULT["bounded_run_through_26"] = {"total": len(bounded), "layers": bounded_layers, "records": bounded_records}
checkpoint("bounded-run enumeration complete")

counterexamples = []
for h in ["RRLRRLRLLRLRLLRLL", "RRLRRLRLLRLLLRLLRLL"]:
    canonical, count = paths(*context(h))
    counterexamples.append({"history": h, "canonical": canonical, "histories": count,
                            "proper_prefix_canonical": least(h[:-1]) == h[:-1],
                            "proper_suffix_canonical": least(h[1:]) == h[1:]})
assert counterexamples[0]["proper_prefix_canonical"] and counterexamples[0]["proper_suffix_canonical"]
assert not counterexamples[1]["proper_prefix_canonical"]
RESULT["inflation_counterexample"] = counterexamples

# Independently test the explicitly quoted failed-conjecture witnesses.
def bits(s):
    return bytes(map(int, s))

failed_stats = []
for u, v, expected in [("000", "010111101", True), ("000", "011001111", False),
                        ("0100", "01100111", True), ("00", "01100111", False)]:
    witness, count = paths(bits(u), bits(v))
    assert bool(count) is expected
    failed_stats.append({"left": u, "right": v, "histories": count, "canonical": witness})
root = bits("011000111001")
canonical, count = paths(root, root)
quoted = "LLRLLRLRLLRLRLRRLRLRRLRR"
assert count == 2 and context(quoted) == (root, root)
assert any(root[j:j+2] not in (bits("01"), bits("10")) for j in range(2, len(root)-2, 2))
RESULT["failed_conjecture_witnesses"] = failed_stats
RESULT["self_shuffle_witness"] = {"root": "011000111001", "histories": count, "quoted_history_valid": True}

window_checks = []
for p, q in itertools.product(range(7), repeat=2):
    u, v = bits("011"+"01"*p+"00"+"01"*q), bits("011"+"01"*(p+q+1))
    explicit = unblock("AC"+"A"*p+"BB"+"A"*q+"D"*(p+q+1))
    assert context(explicit) == (u, v)
    # Consuming D first is an even pair removal and leaves phase zero.
    assert paths(u, v[2:])[1] == 0
    assert len(u) == len(v) and u[:2*p+3] == v[:2*p+3]
    assert q == 0 or u[-2*q:] == v[-2*q:]
    window_checks.append({"p": p, "q": q, "wrong_first_D_histories": 0})
RESULT["fixed_window_family_0_to_6"] = window_checks

# A bounded direct test of the bridge construction, including boundary-crossing
# forbidden occurrences. The proof for arbitrary words is audited in the report.
short_words = ["".join(xs) for n in range(8) for xs in itertools.product("LR", repeat=n)]
avoids = [w for w in short_words if all(f not in w for f in full)]
bridge = "RL" * 24
assert all(not any(f in a+bridge+b for f in full) for a in avoids for b in avoids)
RESULT["finite_bridge_test"] = {"words_length_at_most": 7, "avoiding_words": len(avoids), "pairs_checked": len(avoids)**2, "bridge_length": 48}

# Compare author raw data only after complete independent discovery and signs.
author0 = json.loads((BASE / "computations/secondpass-probe20.json").read_text())
author1 = json.loads((BASE / "computations/secondpass-full-obstruction24-v2.json").read_text())
RESULT["author_data_top_level_keys"] = {"through20": list(author0), "through24": list(author1)}
known = author0.get("minimal_forbidden", author0.get("minimal_bad_factors", []))
if known:
    author_words = [x["larger"] if isinstance(x, dict) else x for x in known]
    author_words += [x["larger"] for x in author1["new_minimal_forbidden"]]
    assert sorted(author_words) == sorted(full)
    RESULT["author_full_word_set_matches"] = True
else:
    RESULT["author_full_word_set_matches"] = "not compared: unexpected checkpoint-1 key"

hashfiles = ["notes/secondpass-checkpoint-2.md", "notes/secondpass-checkpoint-2-sha256.txt", "notes/secondpass-checkpoint-1-sha256.txt",
             "notes/secondpass-canonical-renewal.md", "notes/secondpass-rigidity-obstructions.md", "notes/secondpass-staircases-and-pumping.md",
             "computations/secondpass-probe20.json", "computations/secondpass-full-obstruction24-v2.json", "computations/secondpass-renewal24.json",
             "proof.md", "statement.md"]
RESULT["input_sha256"] = {str(BASE/p): hashlib.sha256((BASE/p).read_bytes()).hexdigest() for p in hashfiles}
manifest_records = []
for name in ["secondpass-checkpoint-1-sha256.txt", "secondpass-checkpoint-2-sha256.txt"]:
    matches = re.findall(r"^([0-9a-f]{64})  (.+)$", (BASE / "notes" / name).read_text(), re.MULTILINE)
    for expected, filename in matches:
        actual = hashlib.sha256(Path(filename).read_bytes()).hexdigest()
        assert actual == expected, (filename, expected, actual)
    manifest_records.append({"manifest": name, "verified_entries": len(matches)})
RESULT["frozen_manifest_checks"] = manifest_records
official = Path(".cache/official/2019-paper_b.pdf")
RESULT["cached_official_paper_sha256"] = hashlib.sha256(official.read_bytes()).hexdigest()
RESULT["status"] = "all independent assertions passed; bounded finite evidence only"
checkpoint("ALL CHECKS COMPLETE")
