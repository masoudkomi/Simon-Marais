#!/usr/bin/env python3
"""Independent R2 finite audit evidence; finite checks are not unrestricted proofs."""

from collections import defaultdict, deque
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import platform
import sys


ROOT = Path(__file__).resolve().parents[3]
TARGET = ROOT / "problems" / "2022-B4"


def D(d, r):
    return d + 2 * (r // 20) - 3 * ((r + d) // 30)


def successors(state):
    d, r = state
    h = D(d, r)
    base = r + 3 * ((r + d) // 30)
    return [(h, (base + 6 * e) % 60) for e in range(10)]


def L(h):
    return h if h > 0 else 0 if h == 0 else (-h + 1) // 2 + 1


def K(d):
    return 1 + max(L(D(d, r)) for r in range(60))


def actual(a, b):
    return a + 2 * (b // 20), b + 3 * (a // 30)


def lift_word(d, r, controls):
    """Use digit lifting, independently checking all earlier controls each time."""
    q = 0
    for m, desired in enumerate(controls):
        lifts = []
        for z in range(10):
            q0 = q + z * 10**m
            a, b = 60 * q0 + r + d, 60 * q0 + r
            seen = []
            for _ in range(m + 1):
                seen.append((b // 60) % 10)
                a, b = actual(a, b)
            if seen == controls[:m + 1]:
                lifts.append(q0)
        assert len(lifts) == 1, (d, r, controls, m, lifts)
        q = lifts[0]
    while 60 * q + r <= 0 or 60 * q + r + d <= 0 or (60 * q + r) * (60 * q + r + d) < 600:
        q += 10 ** len(controls)
    return q


def main():
    print("INDEPENDENT R2 FINITE EVIDENCE; not a proof of unrestricted claims", flush=True)
    print("python", sys.version.split()[0], "platform", platform.platform(), flush=True)
    for name in ("proof.md", "proof-extension-v2.md"):
        print("sha256", name, hashlib.sha256((TARGET / name).read_bytes()).hexdigest(), flush=True)

    # Finite arithmetic and shift checks, deliberately including negative quotients.
    formula_count = 0
    for d in range(-150, 151):
        for r in range(60):
            for q in (-100, -1, 0, 1, 17, 100):
                a, b = 60 * q + r + d, 60 * q + r
                ap, bp = actual(a, b)
                c = 3 * ((r + d) // 30)
                assert ap - bp == D(d, r)
                assert bp == 66 * q + r + c
                assert bp % 60 == (6 * (q % 10) + r + c) % 60
                for t in (-7, 3):
                    shifted = actual(a + 60 * t, b + 60 * t)
                    assert shifted == (ap + 66 * t, bp + 66 * t)
                formula_count += 1
    print("quotient/common-shift checks", formula_count, "PASS", flush=True)

    # Finite control-word bijection: independently enumerate all quotient classes.
    lifting_count = 0
    for d, r, n in [(-101, 0, 3), (-13, 59, 4), (1, 20, 4), (23, 35, 4), (123, 17, 3)]:
        words = set()
        for q in range(10**n):
            a, b = 60 * q + r + d, 60 * q + r
            word = []
            for _ in range(n):
                word.append((b // 60) % 10)
                a, b = actual(a, b)
            words.add(tuple(word))
        assert len(words) == 10**n
        lifting_count += 10**n
    print("finite lifting enumerated classes", lifting_count, "PASS", flush=True)

    # Check local abstract control inequalities over a finite range.
    for h in range(1, 10001):
        for s in range(30, 36):
            nxt = D(h, s)
            assert (nxt == 0 if h == 1 else 0 < nxt < h)
    for k in range(1, 10001):
        for s in range(20, 26):
            nxt = D(-k, s)
            assert nxt >= -k + 2
            assert nxt == {1: 1, 2: 0, 3: -1}[k] if k <= 3 else nxt < 0
    print("local extension control checks h,k <= 10000 PASS", flush=True)

    # Build the strip graph solely to seek finite counterexamples to claimed bounds.
    states = list(itertools.product(range(-13, 24), range(60)))
    reverse = defaultdict(list)
    for st in states:
        for nxt in successors(st):
            assert -13 <= nxt[0] <= 23
            reverse[nxt].append(st)
    dist = {st: 0 for st in states if st[0] == 0}
    queue = deque(dist)
    while queue:
        st = queue.popleft()
        for prev in reverse[st]:
            if prev not in dist:
                dist[prev] = dist[st] + 1
                queue.append(prev)
    assert len(dist) == len(states)
    print("strip graph states", len(states), "max shortest hit distance", max(dist.values()), flush=True)
    print("K(1)", K(1), flush=True)

    # A surviving prefix from difference 1 whose state cannot hit in K(1) more steps.
    seen = {(1, r): None for r in range(60)}
    queue = deque(seen)
    witness = None
    while queue:
        st = queue.popleft()
        if dist[st] > K(1):
            witness = st
            break
        if st[0] == 0:
            continue
        for e, nxt in enumerate(successors(st)):
            if nxt[0] != 0 and nxt not in seen:
                seen[nxt] = (st, e)
                queue.append(nxt)
    assert witness is not None
    path = [witness]
    controls = []
    while seen[path[-1]] is not None:
        prev, e = seen[path[-1]]
        controls.append(e)
        path.append(prev)
    path.reverse()
    controls.reverse()
    q = lift_word(1, path[0][1], controls)
    b = 60 * q + path[0][1]
    a = b + 1
    actual_path = []
    pairs = []
    for _ in range(len(path)):
        actual_path.append((a - b, b % 60))
        pairs.append((a, b))
        a, b = actual(a, b)
    assert actual_path == path
    print("uniform-bound counterexample", json.dumps({"K(1)": K(1), "path": path, "controls": controls,
          "ordinary_positive_integer_lift": pairs, "terminal_shortest_hit_distance": dist[witness]}), flush=True)

    # The same boundary start also refutes uniformity at a K(1)-block boundary.
    a, b = 25, 24
    block_pairs = [(a, b)]
    block_states = [(a - b, b % 60)]
    block_controls = []
    for _ in range(K(1)):
        block_controls.append((b // 60) % 10)
        a, b = actual(a, b)
        block_pairs.append((a, b))
        block_states.append((a - b, b % 60))
    block_witness = block_states[-1]
    assert block_witness == (6, 27) and dist[block_witness] == 5
    print("K-block-boundary counterexample", json.dumps({"K(1)": K(1), "ordinary_start": [25, 24],
          "initial_product": 600, "path": block_states, "pairs": block_pairs, "controls": block_controls,
          "terminal_shortest_hit_distance": dist[block_witness]}), flush=True)

    # Count complete control blocks following the block witness; no hitting extension is possible.
    frontier = {block_witness: 1}
    for step in range(1, K(1) + 1):
        future = defaultdict(int)
        hits = 0
        for st, multiplicity in frontier.items():
            for nxt in successors(st):
                if nxt[0] == 0:
                    hits += multiplicity
                else:
                    future[nxt] += multiplicity
        assert hits == 0
        frontier = dict(future)
        print("witness extension step", step, "surviving words", sum(frontier.values()), "hits", hits,
              "differences", sorted({st[0] for st in frontier}), flush=True)

    # Exact delay family arithmetic at finite sample points.
    delay_count = 0
    for nmax in range(1, 51):
        for t in (1, 7):
            for r in (0, 19):
                b = 60 * 10**nmax * t + r
                a = b + 1
                assert a * b >= 600
                for n in range(nmax + 1):
                    assert b == 60 * 11**n * 10**(nmax - n) * t + r
                    assert a == b + 1
                    a, b = actual(a, b)
                delay_count += 1
    print("delay family sampled starts", delay_count, "PASS", flush=True)

    # Verify the p-step affine formula on finite periodic h patterns; no inference from enumeration.
    affine_count = 0
    for p in range(1, 5):
        A, B = 11**p, 10**p
        for hs in itertools.product(range(-2, 3), repeat=p):
            H = sum(11**(p - 1 - i) * 10**i * h for i, h in enumerate(hs))
            for x0 in (-13, 0, 23):
                x = Fraction(x0)
                for h in hs:
                    x = (11 * x + h) / 10
                assert x == Fraction(A * x0 + H, B)
                affine_count += 1
    print("periodic affine composition checks", affine_count, "PASS", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
