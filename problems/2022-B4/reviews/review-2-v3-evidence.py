#!/usr/bin/env python3
"""Independent R2 v3 finite checks. Evidence only, not unrestricted proof."""

from collections import defaultdict, deque
import hashlib
import itertools
from pathlib import Path
import platform
import sys


ROOT = Path(__file__).resolve().parents[3]
PROBLEM = ROOT / "problems" / "2022-B4"


def D(d, r):
    return d + 2 * (r // 20) - 3 * ((r + d) // 30)


def successor(d, r, e):
    return D(d, r), (6 * e + r + 3 * ((r + d) // 30)) % 60


def actual(a, b):
    return a + 2 * (b // 20), b + 3 * (a // 30)


def policy_path(d, r):
    path = [(d, r)]
    controls = []
    while d != 0:
        h = D(d, r)
        if h == 0:
            e = 0
        else:
            lo = 30 if h > 0 else 20
            base = r + 3 * ((r + d) // 30)
            s = lo + (base - lo) % 6
            e = ((s - base) % 60) // 6
            assert 0 <= e < 10
            assert successor(d, r, e) == (h, s)
        controls.append(e)
        d, r = successor(d, r, e)
        path.append((d, r))
        assert len(controls) <= 10000, "Unexpected policy nontermination"
    return path, controls


def main():
    print("INDEPENDENT R2 V3 FINITE EVIDENCE; not a proof of unrestricted claims", flush=True)
    print("python", sys.version.split()[0], "platform", platform.platform(), flush=True)
    for name in ("proof.md", "proof-extension-v2.md", "proof-extension-v3.md", "reviews/review-2.md"):
        print("sha256", name, hashlib.sha256((PROBLEM / name).read_bytes()).hexdigest(), flush=True)

    # Include negative floor arguments and both remainder endpoints.
    cases = 0
    remainder_ranges = [30, -1, 20, -1]
    for d in range(-2000, 2001):
        for r in range(60):
            u = r + d - 30 * ((r + d) // 30)
            v = r - 20 * (r // 20)
            assert 0 <= u <= 29 and 0 <= v <= 19
            assert 10 * D(d, r) == 9 * d + u - v
            assert 10 * abs(D(d, r)) <= 9 * abs(d) + 29
            remainder_ranges = [min(remainder_ranges[0], u), max(remainder_ranges[1], u),
                                min(remainder_ranges[2], v), max(remainder_ranges[3], v)]
            cases += 1
    print("remainder identity/absolute bound", cases, "cases PASS; extrema", remainder_ranges, flush=True)

    # Invariance and the actual policy bound for selected full finite radii.
    for M in (29, 30, 31, 60, 123):
        max_policy = 0
        for d, r in itertools.product(range(-M, M + 1), range(60)):
            assert abs(D(d, r)) <= M
            path, controls = policy_path(d, r)
            assert all(abs(st[0]) <= M for st in path)
            assert len(controls) <= M + 1
            max_policy = max(max_policy, len(controls))
        print("radius", M, "states", (2 * M + 1) * 60, "invariance PASS; max sampled policy length",
              max_policy, "versus K", M + 1, flush=True)
    assert D(29, 0) == 29  # Positive endpoint equality in the invariant-radius bound.
    print("radius endpoint saturation D(29,0)=29 PASS", flush=True)

    # Boundaries from v3's local positive and negative estimates.
    for h in range(1, 10001):
        for s in range(30, 36):
            nxt = D(h, s)
            assert nxt <= h - 1
            assert nxt == 0 if h == 1 else 0 < nxt
    for k in range(1, 10001):
        for s in range(20, 26):
            nxt = D(-k, s)
            assert nxt >= -k + 2
            assert nxt == {1: 1, 2: 0, 3: -1}[k] if k <= 3 else nxt < 0
    print("local control inequalities h,k<=10000 PASS", flush=True)
    print("small cases", {h: [D(h, s) for s in range(30, 36)] for h in (1, 2)},
          {k: [D(-k, s) for s in range(20, 26)] for k in (1, 2, 3, 4)}, flush=True)

    # A graph confined to M=29 is only a finite supplementary check.
    states = list(itertools.product(range(-29, 30), range(60)))
    reverse = defaultdict(list)
    for d, r in states:
        for e in range(10):
            nxt = successor(d, r, e)
            assert abs(nxt[0]) <= 29
            reverse[nxt].append((d, r))
    distance = {st: 0 for st in states if st[0] == 0}
    queue = deque(distance)
    while queue:
        nxt = queue.popleft()
        for prev in reverse[nxt]:
            if prev not in distance:
                distance[prev] = distance[nxt] + 1
                queue.append(prev)
    assert len(distance) == len(states)
    assert max(distance.values()) <= 30
    print("M=29 graph", len(states), "states; max shortest hit length", max(distance.values()), "<=30 PASS", flush=True)

    # Reproduce both previous audits' examples directly from their integer starts.
    for start, length, old_K, expected in [((599, 600), 3, 3, (3, 12)), ((25, 24), 4, 4, (6, 27))]:
        a, b = start
        delta = a - b
        M = max(abs(delta), 29)
        K = M + 1
        pairs = [(a, b)]
        for _ in range(length):
            a, b = actual(a, b)
            pairs.append((a, b))
        st = (a - b, b % 60)
        assert st == expected and all(a != b for a, b in pairs)
        path, controls = policy_path(*st)
        assert distance[st] > old_K and len(controls) <= K
        print("old witness", start, "initial product", start[0] * start[1], "actual prefix", pairs,
              "terminal", st, "shortest hitting length", distance[st], "old K", old_K,
              "v3 M,K", (M, K), "policy hitting length", len(controls), "path", path, flush=True)
    print("old one-step R2 state (3,24) shortest length", distance[(3, 24)], "<= v3 K 30 PASS", flush=True)

    # Finite lifting uses the exact, unshifted modulus 60*10^N.
    total_classes = 0
    for delta, r, n in [(-61, 59, 4), (-1, 0, 4), (1, 24, 4), (1000, 15, 3)]:
        observed = set()
        for q in range(10**n):
            a, b = 60 * q + r + delta, 60 * q + r
            word = []
            state_path = []
            for _ in range(n):
                word.append((b // 60) % 10)
                state_path.append((a - b, b % 60))
                a, b = actual(a, b)
            state_path.append((a - b, b % 60))
            observed.add(tuple(word))
            # A full modulus shift preserves every state through time N.
            ash, bsh = 60 * (q + 10**n) + r + delta, 60 * (q + 10**n) + r
            shifted_path = []
            for _ in range(n):
                shifted_path.append((ash - bsh, bsh % 60))
                ash, bsh = actual(ash, bsh)
            shifted_path.append((ash - bsh, bsh % 60))
            assert shifted_path == state_path
        assert len(observed) == 10**n
        total_classes += 10**n
        print("lifting delta,r,N", (delta, r, n), "bijective classes", len(observed), "modulus",
              60 * 10**n, "PASS", flush=True)
    print("total finite lifting classes", total_classes, "PASS", flush=True)
    print("No attempt to enumerate 10^30 control blocks; the unrestricted block count is audited analytically.", flush=True)
    print("DONE", flush=True)


if __name__ == "__main__":
    main()
