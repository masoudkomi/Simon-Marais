#!/usr/bin/env python3
"""R2 independent finite checks, standard library only; never imports author code.

The mathematics of the cut recurrence is attributed to CKDFS (2024), 5.1.
Its implementation, exact clipping, straight completion, and sorting-network
enumeration here were written by R2. Computations are finite evidence only.
Run this file without arguments: it preserves the dedicated child PID, command,
60-second wall cap, 100000-state cap, and incremental stdout in this prefix.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction as R
from functools import lru_cache
from itertools import combinations
from math import ceil, floor, log2, prod
from pathlib import Path
import hashlib
import json
import platform
import random
import subprocess
import sys
import time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
CAP = 100000


def relabel(w):
    names = {}
    ans = []
    for letter in w:
        if letter not in names:
            names[letter] = len(names)
        ans.append(names[letter])
    return tuple(ans)


def key(w):
    w = tuple(w)
    if not w:
        return ()
    return min(relabel(t[j:] + t[:j])
               for t in (w, tuple(reversed(w))) for j in range(len(w)))


def positions(w):
    where = {}
    for j, a in enumerate(w):
        where.setdefault(a, []).append(j)
    assert all(len(x) == 2 for x in where.values())
    return where


def crosses(pa, pb):
    a, b = sorted(pa)
    return (a < pb[0] < b) ^ (a < pb[1] < b)


@lru_cache(None)
def patch(w):
    if patch.cache_info().currsize > CAP:
        raise RuntimeError("R2 memo cap; no result for current patch")
    if not w:
        return 1
    cuts = []
    for z, (i, j) in positions(w).items():
        left = w[i+1:j]
        right = w[j+1:] + w[:i]
        counts = Counter(left)
        split = tuple(a for a in left if counts[a] == 1)
        cuts.append(((len(split), abs(len(left)-len(right)), z), left, right, split))
    _, left, right, split = min(cuts)
    k = len(split)
    right_index = {a: right.index(a) for a in split}
    required = [0] * k
    for i in range(k):
        for j in range(i):
            # Reversed endpoint order on the complementary boundary arc means
            # noncrossing, so the corresponding crossing order on z is forced.
            if right_index[split[j]] > right_index[split[i]]:
                required[i] |= 1 << j
    full = (1 << k) - 1
    stack = [(0, ())]
    total = 0
    while stack:
        mask, order = stack.pop()
        if mask == full:
            total += patch(key(left + order[::-1])) * patch(key(right + order))
            continue
        for i, a in enumerate(split):
            if not mask & (1 << i) and required[i] & mask == required[i]:
                stack.append((mask | (1 << i), order + (a,)))
    return total


def rectangle(L, H):
    xmin, ymin = R(1, 10), R(1, 5)
    xmax, ymax = xmin + L, ymin + H
    corners = ((xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax))
    data = []
    ends = []
    for a, b in ((1, 0), (0, 1), (-1, 1), (1, 1)):
        values = [a*x + b*y for x, y in corners]
        for c in range(ceil(min(values)), floor(max(values)) + 1):
            points = set()
            if b:
                for x in (xmin, xmax):
                    y = (c-a*x) / b
                    if ymin <= y <= ymax:
                        points.add((x, y))
            if a:
                for y in (ymin, ymax):
                    x = (c-b*y) / a
                    if xmin <= x <= xmax:
                        points.add((x, y))
            if not points:
                continue
            assert len(points) == 2 and not points.intersection(corners)
            label = len(data)
            data.append((a, b, c))
            for x, y in points:
                if y == ymin:
                    t = x - xmin
                elif x == xmax:
                    t = L + y - ymin
                elif y == ymax:
                    t = L + H + xmax - x
                else:
                    assert x == xmin
                    t = 2*L + H + ymax - y
                ends.append((t, label))
    ends.sort()
    assert len(set(t for t, _ in ends)) == len(ends)
    return tuple(a for _, a in ends), data


def complete_patterns(n):
    """Enumerate actual reduced wiring words, quotient only by local orders."""
    p = list(range(n))
    local = [[] for _ in p]
    classes = set()
    triples = list(combinations(range(n), 3))
    full_length = n*(n-1)//2

    def search(length):
        if length == full_length:
            classes.add(tuple(tuple(row) for row in local))
            return
        for place in range(n-1):
            a, b = p[place:place+2]
            if a > b:
                continue
            p[place:place+2] = b, a
            local[a].append(b)
            local[b].append(a)
            search(length + 1)
            local[a].pop()
            local[b].pop()
            p[place:place+2] = a, b

    search(0)
    signs = set()
    for local_order in classes:
        signature = 0
        for j, (a, b, c) in enumerate(triples):
            signature |= (local_order[b].index(a) > local_order[b].index(c)) << j
        signs.add(signature)
    assert len(signs) == len(classes)
    return signs


def words(n):
    slots = [-1] * (2*n)

    def pair(free, name):
        if not free:
            yield tuple(slots)
            return
        first, *tail = free
        for last in tail:
            slots[first] = slots[last] = name
            yield from pair(tuple(i for i in tail if i != last), name+1)

    yield from pair(tuple(range(2*n)), 0)


def fiber(w, signatures):
    n = len(w)//2
    triples = list(combinations(range(n), 3))
    where = positions(w)
    rng = random.Random(int(hashlib.sha256(repr(w).encode()).hexdigest(), 16))
    for attempt in range(100):
        ts = sorted(rng.sample(range(1, 1 << 24), 2*n))
        # Points (t,t^2) on a convex curve. A chord through u,v lies on
        # y=(u+v)x-uv. Randomness chooses coordinates, never approximates them.
        lines = sorted((ts[i]+ts[j], ts[i]*ts[j], name)
                       for name, (i, j) in where.items())
        if len(set(a for a, _, _ in lines)) != n:
            continue
        at = {(i,j): R(lines[i][1]-lines[j][1], lines[i][0]-lines[j][0])
              for i,j in combinations(range(n), 2)}
        if any(at[a,b] == at[b,c] for a,b,c in triples):
            continue
        break
    else:
        raise RuntimeError("No generic completion within preset 100 exact attempts")
    inside = {(i,j): crosses(where[lines[i][2]], where[lines[j][2]])
              for i,j in combinations(range(n), 2)}
    fixed = 0
    prescribed = 0
    for bit, (a,b,c) in enumerate(triples):
        if not (inside[a,b] and inside[a,c] and inside[b,c]):
            fixed |= 1 << bit
            prescribed |= (at[a,b] > at[b,c]) << bit
    return sum(s & fixed == prescribed for s in signatures)


def worker():
    print("R2 finite evidence; Python", platform.python_version(), flush=True)
    print("No author modules imported; all geometry and integers exact", flush=True)
    for L in range(1, 6):
        for H in range(1, 6):
            w, data = rectangle(L, H)
            pos = positions(w)
            edge_count = sum(crosses(pos[a], pos[b]) for a,b in combinations(pos, 2))
            assert len(data) == 3*(L+H) and edge_count == 7*L*H
    print("Rectangle geometry L,H=1..5: strand and pair counts verified", flush=True)
    for side in (1,2,3):
        w, lines = rectangle(side, side)
        print("START square", side, "word", w, "lines", lines, flush=True)
        began = time.monotonic()
        count = patch(key(w))
        print("DONE square", side, "Q", count, "states", patch.cache_info().currsize,
              "seconds", time.monotonic()-began, flush=True)
    for n in range(1, 7):
        began = time.monotonic()
        signatures = complete_patterns(n)
        distinct = {key(w) for w in words(n)}
        for w in sorted(distinct):
            got, target = patch(w), fiber(w, signatures)
            assert got == target, (n,w,got,target)
        print("FIBER n", n, "actual wiring classes", len(signatures),
              "paired-word count classes", len(distinct),
              "all equal True seconds", time.monotonic()-began, flush=True)
    for t in range(1, 31):
        four = sum(abs(x)+abs(y) <= t for x in range(-t,t+1) for y in range(-t,t+1))
        three = (2*t+1)**2-four
        assert four == 2*t*t+2*t+1 and three == 2*t*t+2*t
    print("Finite bundle lattice counts t=1..30 verified", flush=True)
    cap = 12
    nchecks = 0
    for a,b,c in combinations(range(1, cap+3), 3):
        # Strictly increasing shifted indices parameterize all a<=b<=c<=12.
        b -= 1
        c -= 2
        val = prod(R(i+j+c-1, i+j-1) for i in range(1,a+1) for j in range(1,b+1))
        assert val.denominator == 1
        S = a*b+b*c+c*a
        assert val.numerator**2 * 16**S < 27**S
        nchecks += 1
    print("M1 exact finite checks", nchecks, "max coordinate", cap, flush=True)
    q = 4419734746
    print("G2 numerical coefficient", (1+log2(q)/9)/24, flush=True)
    print("COMPLETE", flush=True)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--worker":
        worker()
        return
    command = [sys.executable, str(Path(__file__).resolve()), "--worker"]
    output = HERE / "secondpass-review-2-check-output.txt"
    metadata = HERE / "secondpass-review-2-check-job.json"
    started = time.monotonic()
    job = {"started_utc": datetime.now(timezone.utc).isoformat(), "command": command,
           "timeout_seconds": 60, "memo_state_cap": CAP, "status": "running"}
    with output.open("w") as log:
        child = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)
        job["child_pid"] = child.pid
        metadata.write_text(json.dumps(job, indent=2)+"\n")
        print("child_pid", child.pid, "metadata", metadata, "output", output, flush=True)
        try:
            code = child.wait(timeout=60)
            job["status"] = "complete" if code == 0 else "failed"
        except subprocess.TimeoutExpired:
            child.terminate()
            try:
                code = child.wait(timeout=2)
            except subprocess.TimeoutExpired:
                child.kill()
                code = child.wait(timeout=2)
            job["status"] = "timeout_incomplete"
        job.update(returncode=code, elapsed_seconds=time.monotonic()-started,
                   finished_utc=datetime.now(timezone.utc).isoformat())
        metadata.write_text(json.dumps(job, indent=2)+"\n")
    print(json.dumps(job, sort_keys=True), flush=True)
    if job["status"] != "complete":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
