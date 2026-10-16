#!/usr/bin/env python3
"""Fresh R2 finite audit of the frozen criterion; Python stdlib only.

No import or execution of the proof author's builder, verifier, or renderer.
Automaton state vectors are full Laurent supports, not author RREF rows.
The graph JSON is read only after the Laurent orbit has been reconstructed.
All range tests are finite evidence, separate from the general proof audit.
"""

from __future__ import annotations

from collections import Counter, deque
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import sys
import time


BASE = Path(__file__).resolve().parents[1]
OUT = Path(__file__).with_name("criterion-review-2-check.json")
T0 = time.monotonic()
INTERNAL_LIMIT_SECONDS = 35
MAX_ORBIT_STATES = 256
RECURRENCE_MAX_J = 65535
EXPECTED_HASHES = {
    "notes/zero-automaton-criterion-v1.md": "59e3bb1f9aba8162ea5b79f0ccec5f56b6f2cb0cc7917cfe81f4aff196ff6ab4",
    "notes/zero-automaton-certificate-v1.md": "b384ed3c0b51572e729b1e5486847ebcc5d964f4afa64c43e60a76910ad0ddd3",
    "notes/zero-automaton-v1-manifest.json": "41fef0ca55da72d8efc8fb04f3b0180f77fc43edf28b276a87f7bd033b6687f2",
    "computations/zero-automaton-v1-graph.json": "ee818f60e68da70ae2f0f7fa84a2c4dec740d10d03908359a271e354a1a0ce4e",
}


def checkpoint(label, **data):
    assert time.monotonic() - T0 < INTERNAL_LIMIT_SECONDS, "internal audit budget"
    print(json.dumps({"checkpoint": label, "elapsed_seconds": time.monotonic() - T0, **data}, sort_keys=True), flush=True)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def plus(*polys):
    """Addition of F2 support polynomials in any fixed exponent rank."""
    ans = frozenset()
    for p in polys:
        ans = ans.symmetric_difference(p)
    return ans


def times(p, q):
    ans = set()
    for a in p:
        for b in q:
            c = tuple(x + y for x, y in zip(a, b))
            if c in ans:
                ans.remove(c)
            else:
                ans.add(c)
    return frozenset(ans)


def power(p, n):
    rank = len(next(iter(p)))
    ans = frozenset({(0,) * rank})
    while n:
        if n & 1:
            ans = times(ans, p)
        n //= 2
        if n:
            p = frozenset(tuple(2 * a for a in mon) for mon in p)
    return ans


ONE3 = frozenset({(0, 0, 0)})
X = frozenset({(1, 0, 0)})
Y = frozenset({(0, 1, 0)})
Z = frozenset({(0, 0, 1)})
W = plus(X, Y, Z)
Q = plus(power(X, 2), power(Y, 2), power(Z, 2), times(X, Y), times(Y, Z), times(Z, X))
R = times(times(plus(X, Y), plus(Y, Z)), plus(Z, X))
D = times(times(times(X, Y), Z), W)


def algebra_identities():
    # Compute all elementary symmetric coefficients, including multiplicity,
    # by multiplying (1+a*t), with t degree held in a separate Python list.
    elementary = [ONE3]
    for root in (X, Y, Z, W):
        nxt = [frozenset() for _ in range(len(elementary) + 1)]
        for k, coeff in enumerate(elementary):
            nxt[k] = plus(nxt[k], coeff)
            nxt[k + 1] = plus(nxt[k + 1], times(coeff, root))
        elementary = nxt
    assert elementary == [ONE3, frozenset(), Q, R, D]

    square_relations = []
    for root in (X, Y, Z):
        val = plus(power(root, 8), times(power(Q, 2), power(root, 4)), times(power(R, 2), power(root, 2)), power(D, 2))
        assert not val
        square_relations.append(True)
    leading = [list(max(p)) for p in (Q, power(R, 2), D)]
    assert leading == [[2, 0, 0], [4, 2, 0], [2, 1, 1]]
    a, b, c = leading
    det = (a[0] * (b[1] * c[2] - b[2] * c[1])
           - b[0] * (a[1] * c[2] - a[2] * c[1])
           + c[0] * (a[1] * b[2] - a[2] * b[1]))
    assert det == 4

    # P_j evaluated at (Q,R^2,D), obtained directly from the formal recurrence.
    pj = []
    q2, r2, d2 = power(Q, 2), power(R, 2), power(D, 2)
    checked_n = []
    for j in range(31):
        val = {0: ONE3, 1: Q, 2: D}.get(j, frozenset())
        if j >= 2:
            val = plus(val, times(q2, pj[j - 2]))
        if j >= 3:
            val = plus(val, times(r2, pj[j - 3]))
        if j >= 4:
            val = plus(val, times(d2, pj[j - 4]))
        pj.append(val)
        n = 2 * j + 3
        f = plus(power(X, n), power(Y, n), power(Z, n), power(W, n))
        assert f == times(R, val)
        assert (n - 1, 1, 0) in f
        checked_n.append(n)
    actual_A = plus(power(Q, 5), times(Q, power(D, 2)), times(power(R, 2), D))
    assert pj[5] == actual_A
    assert all(sum(e) == 10 for e in actual_A)
    assert plus(X, Y, Z, W) == frozenset()  # f_1=0, excluded by theorem.
    assert pj[0] == ONE3  # phi_3=1.

    # Formal P5 in three independent variables; no substitution assumption.
    q, u, d = X, Y, Z
    abstract = []
    for j in range(6):
        val = {0: ONE3, 1: q, 2: d}.get(j, frozenset())
        if j >= 2:
            val = plus(val, times(power(q, 2), abstract[j - 2]))
        if j >= 3:
            val = plus(val, times(u, abstract[j - 3]))
        if j >= 4:
            val = plus(val, times(power(d, 2), abstract[j - 4]))
        abstract.append(val)
    assert abstract[5] == frozenset({(5, 0, 0), (1, 0, 2), (0, 1, 1)})
    return {
        "elementary_symmetric_coefficients_match": True,
        "squared_root_relations_match": square_relations,
        "lex_leading_monomials": leading,
        "integer_exponent_determinant": det,
        "direct_R_Pj_equals_fn_checked_n": checked_n,
        "abstract_P5_support_qud": sorted(abstract[5]),
        "actual_phi13_support": sorted(actual_A),
        "phi3_is_one_and_f1_is_zero": True,
    }


# Laurent polynomial supports below are ordered pairs (z exponent,b exponent).
MONOMIALS = tuple((i, h) for i in range(4) for h in range(-1, 3))
MSET = frozenset(MONOMIALS)
K = frozenset({(0, 0), (2, 0), (3, -1), (3, 1), (4, 2)})
P = frozenset({(0, 0), (1, 0), (2, 1)})
ZERO = frozenset()


def section(poly, r, t):
    # Python modulo gives residues 0,1 even for negative b exponents.
    return frozenset(((i - r) // 2, (h - t) // 2)
                     for i, h in poly if i % 2 == r and h % 2 == t)


def laurent_map(poly, r, t):
    ans = section(times(poly, K), r, t)
    assert ans <= MSET, "Cartier map escaped the proposed 16-dimensional space"
    return ans


def vector_span(polys):
    """Full set of supports, using symmetric difference; no row reduction."""
    space = {ZERO}
    for poly in polys:
        if poly not in space:
            space.update(p.symmetric_difference(poly) for p in tuple(space))
    assert len(space) <= 65536
    return frozenset(space)


def successor(space, r):
    return vector_span(laurent_map(poly, r, t) for poly in space for t in (0, 1))


def encode(poly):
    return sum(1 << MONOMIALS.index(mon) for mon in poly)


def decode(mask):
    assert 0 <= mask < (1 << 16)
    return frozenset(mon for bit, mon in enumerate(MONOMIALS) if mask & (1 << bit))


def accepting(space):
    return all(all(i > 0 for i, h in poly) for poly in space)


def reconstruct_graph():
    # Start with P, then generate states solely from raw polynomial multiplication.
    states = [vector_span([P])]
    labels = {states[0]: 0}
    queue = deque([0])
    transitions = []
    while queue:
        v = queue.popleft()
        assert v == len(transitions)
        targets = []
        for r in (0, 1):
            nxt = successor(states[v], r)
            if nxt not in labels:
                assert len(states) < MAX_ORBIT_STATES
                labels[nxt] = len(states)
                states.append(nxt)
                queue.append(len(states) - 1)
            targets.append(labels[nxt])
        transitions.append(targets)
    flags = [accepting(space) for space in states]
    assert len(states) == len(transitions) == 48
    checkpoint("raw Laurent orbit closed", states=len(states), accepting=sum(flags), max_full_space_size=max(map(len, states)))
    return states, transitions, flags


QUOTIENT_MEMBERS = {
    "S": [0], "A": [2], "B": [5, 36], "C": [12], "D": [21],
    "E": [31], "Z": [35, 39, 43],
    "X": [1, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20,
          22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 37, 38, 40,
          41, 42, 44, 45, 46, 47],
}
QUOTIENT_TRANSITIONS = {
    "S": ["X", "A"], "A": ["B", "X"], "B": ["X", "C"],
    "C": ["D", "X"], "D": ["E", "X"], "E": ["Z", "B"],
    "Z": ["Z", "X"], "X": ["X", "X"],
}
ACCEPT_CLASSES = frozenset({"C", "D", "E", "Z"})


def verify_graph_certificate(states, transitions, flags):
    # Read author certificate only after the independently built orbit is closed.
    graph = json.loads((BASE / "computations/zero-automaton-v1-graph.json").read_text())
    assert graph["initial_state"] == 0
    assert graph["complete"] is True
    assert graph["monomial_bit_order"] == [list(mon) for mon in MONOMIALS]
    assert {tuple(mon) for mon in graph["k_monomials"]} == K
    for r in (0, 1):
        for t in (0, 1):
            actual = [encode(laurent_map(frozenset({mon}), r, t)) for mon in MONOMIALS]
            assert actual == graph["operators_columns"][f"{r}{t}"]
    assert len(graph["states_rref"]) == 48
    for v, rows in enumerate(graph["states_rref"]):
        assert vector_span(decode(mask) for mask in rows) == states[v]
        assert len(states[v]) == (1 << len(rows))  # No linear dependence.
        pivots = [mask.bit_length() - 1 for mask in rows]
        assert pivots == sorted(pivots, reverse=True)
        assert len(pivots) == len(set(pivots))
        for row, pivot in zip(rows, pivots):
            assert all(not (other >> pivot & 1) for other in rows if other != row)
    assert graph["transitions"] == transitions
    assert graph["accepting"] == flags
    assert len(set(states)) == 48
    assert graph["discovered_state_count"] == graph["processed_state_count"] == 48
    assert graph["accepting_state_count"] == sum(flags) == 6
    assert Counter(map(lambda s: len(s).bit_length() - 1, states)) == Counter({1: 1, 2: 3, 3: 9, 4: 17, 5: 12, 6: 6})

    # Check the readable certificate independently of the JSON rendering claim.
    readable = (BASE / "notes/zero-automaton-certificate-v1.md").read_text()
    col_rows = []
    state_rows = []
    for line in readable.splitlines():
        fields = [f.strip() for f in line.split("|")[1:-1]]
        if len(fields) == 7 and fields[0].isdigit():
            col_rows.append([int(v) for v in fields])
        elif len(fields) == 6 and fields[0].isdigit():
            state_rows.append(fields)
    assert len(col_rows) == 16
    for row in col_rows:
        bit, i, h, *cols = row
        assert (i, h) == MONOMIALS[bit]
        assert cols == [encode(laurent_map(frozenset({(i, h)}), r, t)) for r, t in ((0, 0), (0, 1), (1, 0), (1, 1))]
    assert len(state_rows) == 48
    cls = {v: c for c, members in QUOTIENT_MEMBERS.items() for v in members}
    assert sorted(cls) == list(range(48))
    assert sum(map(len, QUOTIENT_MEMBERS.values())) == 48
    for row in state_rows:
        v = int(row[0])
        rows = [int(s.strip()) for s in row[1].split(",")]
        assert vector_span(decode(mask) for mask in rows) == states[v]
        assert list(map(int, row[2:4])) == transitions[v]
        assert (row[4] == "yes") == flags[v]
        assert row[5] == cls[v]
    for v in range(48):
        assert [cls[a] for a in transitions[v]] == QUOTIENT_TRANSITIONS[cls[v]]
        assert flags[v] == (cls[v] in ACCEPT_CLASSES)
    checkpoint("all certificate maps, states, transitions, outputs and quotient checked", matrix_columns=64, transitions=96)
    return cls


def state_at_index(j, transitions):
    v = 0
    # Empty word at 0 is intentional; adding binary leading zeros is separate.
    while j:
        v = transitions[v][j & 1]
        j >>= 1
    return v


def finite_series_check(transitions, flags):
    # Encode b exponents h as bit h+offset in a Python nonnegative integer.
    # For j<=J, every exponent satisfies |h|<=j: each denominator monomial
    # has |h|<=its positive z degree, and the numerator satisfies this too.
    # Consequently offset=J+4 prevents any loss from the right shift for b^-1.
    J = RECURRENCE_MAX_J
    offset = J + 4
    unit = 1 << offset
    last_four = [0, 0, 0, 0]
    zeros = []
    first_supports = {}
    lengths = Counter()
    for j in range(J + 1):
        val = unit if j in (0, 1) else ((unit << 1) if j == 2 else 0)
        if j >= 2:
            val ^= last_four[(j - 2) % 4]
        if j >= 3:
            p = last_four[(j - 3) % 4]
            val ^= (p << 1) ^ (p >> 1)
        if j >= 4:
            val ^= last_four[(j - 4) % 4] << 2
        last_four[j % 4] = val
        assert (val == 0) == flags[state_at_index(j, transitions)]
        word = bin(j)[2:][::-1] if j else ""
        regex_accept = re.fullmatch(r"101(?:0011)*0*", word) is not None
        assert regex_accept == (val == 0)
        if val == 0:
            zeros.append(j)
        if j <= 12:
            first_supports[str(j)] = [k - offset for k in range(offset - 12, offset + 13) if val >> k & 1]
        if j and j % 16384 == 0:
            checkpoint("direct Laurent recurrence", checked_through_j=j)
    expected = []
    m = 0
    while True:
        n = (32 * 16 ** m - 7) // 5
        assert (32 * 16 ** m - 7) % 5 == 0
        if n > J:
            break
        expected.append(n)
        m += 1
    assert zeros == expected == [5, 101, 1637, 26213]

    # Exhaust every finite word of length <=16, including leading zeros,
    # independently computing its integer and using graph transitions.
    word_checks = 0
    paths = [("", 0, 0)]
    for k in range(17):
        nxt = []
        for word, state, value in paths:
            assert flags[state] == (re.fullmatch(r"101(?:0011)*0*", word) is not None)
            assert flags[state] == flags[state_at_index(value, transitions)]
            word_checks += 1
            if k < 16:
                for r in (0, 1):
                    nxt.append((word + str(r), transitions[state][r], value + r * (1 << k)))
        paths = nxt
    assert word_checks == (1 << 17) - 1
    checkpoint("finite recurrence and all short words checked", j_max=J, all_words_max_length=16, words_checked=word_checks)
    return {"finite_evidence_only": True, "recurrence_max_j": J, "zero_indices": zeros,
            "initial_coefficient_b_supports": first_supports,
            "all_finite_words_max_length": 16, "words_checked": word_checks,
            "recurrence_automaton_and_regex_agree": True,
            "leading_zero_invariance_checked_in_this_range": True}


def main():
    hashes = {}
    for rel, expected in EXPECTED_HASHES.items():
        actual = sha(BASE / rel)
        assert actual == expected, f"frozen input mismatch: {rel}"
        hashes[rel] = actual
    # Bytehash every constructor-manifest entry without loading any program
    # as code or treating its output as mathematical validation.
    author_manifest = json.loads((BASE / "notes/zero-automaton-v1-manifest.json").read_text())
    for rel, expected in author_manifest["files_sha256"].items():
        actual = sha(BASE / rel)
        assert actual == expected, f"author manifest mismatch: {rel}"
        hashes[rel] = actual
    checkpoint("frozen inputs verified", files=len(hashes), pid=os.getpid())
    algebra = algebra_identities()
    checkpoint("direct polynomial identities checked", finite_fn_checks=len(algebra["direct_R_Pj_equals_fn_checked_n"]))
    states, transitions, flags = reconstruct_graph()
    classes = verify_graph_certificate(states, transitions, flags)
    finite = finite_series_check(transitions, flags)
    result = {
        "status": "all fresh independent finite checks passed; not a substitute for general proof audit",
        "reviewer": "criterion R2; blind initial audit",
        "date": "2026-10-16",
        "dependencies": "Python standard library only",
        "python": platform.python_version(),
        "pid": os.getpid(),
        "parameters": {"internal_limit_seconds": INTERNAL_LIMIT_SECONDS, "orbit_state_cap": MAX_ORBIT_STATES, "recurrence_max_j": RECURRENCE_MAX_J},
        "input_hashes": hashes,
        "algebra_identities": algebra,
        "reconstruction": {
            "raw_Laurent_supports_no_RREF": True,
            "builder_and_author_verifier_neither_imported_nor_executed": True,
            "graph_read_after_independent_orbit_closed": True,
            "states": len(states), "distinct": len(set(states)),
            "matrix_columns_checked": 64, "outgoing_transitions_checked": len(transitions) * 2,
            "all_state_vectors": [sorted(map(encode, space)) for space in states],
            "transitions": transitions,
            "accepting": flags,
            "classes": [classes[v] for v in range(len(states))],
            "quotient_transitions": QUOTIENT_TRANSITIONS,
            "readable_certificate_matches": True,
            "closed": True,
        },
        "finite_sanity_evidence": finite,
        "elapsed_seconds": time.monotonic() - T0,
        "script_sha256": sha(Path(__file__)),
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    checkpoint("audit finite checks passed", output=str(OUT), output_sha256=sha(OUT))


if __name__ == "__main__":
    main()
