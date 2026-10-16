#!/usr/bin/env python3
"""R1 independent checks. Never imports an author computation.

Commands: this file --task algebra|fibers|grid|finite-grid [--worker]
The driver writes task-specific PID/argv/timeout and incremental stdout.
Every mathematical computation uses Python integers/Fraction; decimals are
orientation only. Only a dedicated child can be terminated by the driver.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from functools import cache
from itertools import combinations
import hashlib
import json
from math import log, log2
from pathlib import Path
import platform
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
STATE_LIMIT = 180000


def renamed(w):
    table = {}
    ans = []
    for x in w:
        if x not in table:
            table[x] = len(table)
        ans.append(table[x])
    return tuple(ans)


@cache
def key(w):
    """A count cache key, never a quotient of counted patch arrangements."""
    if not w:
        return ()
    choices = []
    for a in (w, tuple(reversed(w))):
        for j in range(len(w)):
            choices.append(renamed(a[j:] + a[:j]))
    return min(choices)


def crossing_set(w):
    ports = {}
    for j, a in enumerate(w):
        ports.setdefault(a, []).append(j)
    result = set()
    for a, b in combinations(ports, 2):
        i, j = ports[a]
        k, l = ports[b]
        if (i < k < j) != (i < l < j):
            result.add(frozenset((a, b)))
    return result


@cache
def cut_count(w):
    if cut_count.cache_info().currsize >= STATE_LIMIT:
        raise RuntimeError("R1 state limit: incomplete, no count claimed")
    if len(w) < 4:
        return 1
    ports = {a: (w.index(a), len(w)-1-w[::-1].index(a)) for a in set(w)}
    edges = crossing_set(w)
    z = min(ports, key=lambda a: (sum(a in e for e in edges),
                                  max(ports[a][1]-ports[a][0]-1,
                                      len(w)-(ports[a][1]-ports[a][0])-1), a))
    lo, hi = ports[z]
    left = w[lo+1:hi]
    right = w[hi+1:] + w[:lo]
    neighbors = sorted(a for a in ports if frozenset((a,z)) in edges)
    before = {a: set() for a in neighbors}
    # Derive each mandatory precedence by testing the two induced four-port
    # half words. A noncrossing original pair may not cross in BOTH halves.
    for a, b in combinations(neighbors, 2):
        if frozenset((a,b)) in edges:
            continue
        valid_orders = []
        for order in ((a,b), (b,a)):
            wa = tuple(x for x in left if x in (a,b)) + order[::-1]
            wb = tuple(x for x in right if x in (a,b)) + order
            if not crossing_set(wa) and not crossing_set(wb):
                valid_orders.append(order)
        assert len(valid_orders) == 1
        earlier, later = valid_orders[0]
        before[later].add(earlier)

    def extensions(prefix, rest):
        if not rest:
            yield prefix
        for a in sorted(rest):
            if not before[a].intersection(rest):
                yield from extensions(prefix+(a,), rest-{a})

    total = 0
    for order in extensions((), set(neighbors)):
        total += cut_count(key(left+order[::-1])) * cut_count(key(right+order))
    return total


def paired_words(n):
    def recurse(w, unmatched, next_label):
        if len(w) == 2*n:
            yield w
            return
        for a in sorted(unmatched):
            yield from recurse(w+(a,), unmatched-{a}, next_label)
        if next_label < n:
            yield from recurse(w+(next_label,), unmatched|{next_label}, next_label+1)
    yield from recurse((), set(), 0)


def complete_patterns(n):
    """Independent direct packet CSP, lexicographic variables, no oracle."""
    triples = list(combinations(range(n), 3))
    index = {t:i for i,t in enumerate(triples)}
    packets = [tuple(index[t] for t in combinations(q,3))
               for q in combinations(range(n),4)]
    allowed = [tuple((mask>>i)&1 for i in range(4)) for mask in range(16)
               if sum(((mask>>i)&1) != ((mask>>(i+1))&1) for i in range(3)) <= 1]
    incident = [[] for _ in triples]
    for packet in packets:
        for i in packet:
            incident[i].append(packet)
    values = [-1]*len(triples)
    answer = []

    def search(i, bits):
        if i == len(triples):
            answer.append(bits)
            return
        for b in (0,1):
            values[i] = b
            if all(any(all(values[v] == -1 or values[v] == a[j]
                           for j,v in enumerate(packet)) for a in allowed)
                   for packet in incident[i]):
                search(i+1, bits|(b<<i))
        values[i] = -1
    search(0, 0)
    return triples, answer


def fiber_data(w):
    """Exact chord completion on a convex parabola, with a genericity check."""
    n = len(w)//2
    pairs = [tuple(i for i,x in enumerate(w) if x == a) for a in range(n)]
    for base in range(2,32):
        # The initial version base**i was NOT generic: three symmetric
        # endpoint pairs with equal index sums have equal products and
        # concurrent secants. Preserve that failed run; perturb independently.
        xx = [base**((i+1)**3)+i for i in range(2*n)]
        # y = s*x-p for the secant with endpoints (u,u^2), (v,v^2).
        lines = sorted((xx[i]+xx[j], xx[i]*xx[j], a)
                       for a,(i,j) in enumerate(pairs))
        assert len({s for s,p,a in lines}) == n
        at = {(a,b):Fraction(lines[a][1]-lines[b][1], lines[a][0]-lines[b][0])
              for a,b in combinations(range(n),2)}
        if all(at[a,b] != at[b,c] for a,b,c in combinations(range(n),3)):
            break
    else:
        raise RuntimeError("R1 completion genericity search failed")
    edges = crossing_set(w)
    free = fixed_value = 0
    for j,(a,b,c) in enumerate(combinations(range(n),3)):
        original = (lines[a][2], lines[b][2], lines[c][2])
        if all(frozenset(p) in edges for p in combinations(original,2)):
            free |= 1<<j
        fixed_value |= (at[a,b] > at[b,c])<<j
    fixed = ((1<<(n*(n-1)*(n-2)//6))-1)^free
    return fixed, fixed_value&fixed, free.bit_count(), len(edges), base


def macmahon(a,b,c):
    # Independent un-telescoped three-dimensional product.
    answer = Fraction(1)
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                answer *= Fraction(i+j+k-1, i+j+k-2)
    assert answer.denominator == 1
    return answer.numerator


def algebra():
    checked = 0
    best = (0,None)
    for a in range(1,15):
        for b in range(a,15):
            for c in range(b,15):
                value = macmahon(a,b,c)
                s = a*b+a*c+b*c
                assert value*value*16**s < 27**s
                ratio = log2(value)/(2*s)
                best = max(best,(ratio,(a,b,c)))
                checked += 1
        print("ALGEBRA checkpoint", a, checked, flush=True)
    print("ALGEBRA COMPLETE", checked, "best numerical", best, flush=True)
    kappa = 0.75*log(3)-log(2)
    worst = (-1,None)
    for i in range(1,300):
        for j in range(1,300-i):
            p,q,r = i/300,j/300,(300-i-j)/300
            aa = sum(x*x*log(x)-(1-x)**2*log(1-x) for x in (p,q,r))/2
            gap = aa-kappa*(1-p*p-q*q-r*r)
            worst = max(worst,(gap,(i,j,300-i-j)))
    print("SIMPLEX finite numerical evidence only: max(A-kappa denominator)",worst,flush=True)
    for n in (1,2,3,5,8,13):
        print("BALANCED", n, macmahon(n,n,n),flush=True)


def fibers():
    for n in range(1,8):
        triples, patterns = complete_patterns(n)
        print("FIBER signotopes ready", n,len(patterns),flush=True)
        cases = words = 0
        seen = set()
        salts = Counter()
        histogram = Counter()
        for w in paired_words(n):
            words += 1
            canon = key(w)
            if canon in seen:
                continue
            seen.add(canon)
            fixed, value, free_count, edge_count, base = fiber_data(canon)
            expected = sum((p&fixed)==value for p in patterns)
            actual = cut_count(canon)
            assert actual == expected, (n, canon, actual, expected)
            salts[base] += 1
            histogram[(edge_count,free_count)] += 1
            cases += 1
            if cases%1000 == 0:
                print("FIBER checkpoint",n,cases,"memo",cut_count.cache_info(),flush=True)
        print("FIBER COMPLETE", n, "paired_words",words,"canonical_cases",cases,
              "completion_bases",dict(salts),"memo",cut_count.cache_info(),flush=True)
    for sizes in ((1,1,1),(1,2,3),(2,2,2),(2,2,3),(3,3,3),(2,3,4)):
        a,b,c = sizes
        groups = [tuple(range(a)),tuple(range(a,a+b)),tuple(range(a+b,a+b+c))]
        w = sum(groups,())+sum((g[::-1] for g in groups),())
        count = cut_count(key(w))
        assert count == macmahon(a,b,c)
        print("MACMAHON boundary",sizes,count,flush=True)
    for w in ((0,1,0,2,1,3,2,3),(0,0,1,2,3,1,2,3)):
        print("DEGENERATE",w,"edges",len(crossing_set(w)),"F",cut_count(key(w)),flush=True)


def rectangle_word(L,H):
    x0,y0 = Fraction(1,10),Fraction(1,5)
    x1,y1 = x0+L,y0+H
    segments = []
    perimeter = []
    for A,B in ((1,0),(0,1),(-1,1),(1,1)):
        for C in range(-2*(L+H)-2,2*(L+H)+3):
            boundary = set()
            if B:
                for x in (x0,x1):
                    y = (C-A*x)/B
                    if y0 <= y <= y1:
                        boundary.add((x,y))
            if A:
                for y in (y0,y1):
                    x = (C-B*y)/A
                    if x0 <= x <= x1:
                        boundary.add((x,y))
            if not boundary:
                continue
            assert len(boundary) == 2
            label = len(segments)
            segments.append((A,B,C))
            for x,y in boundary:
                assert not (x in (x0,x1) and y in (y0,y1))
                if y == y0:
                    distance = x-x0
                elif x == x1:
                    distance = L+y-y0
                elif y == y1:
                    distance = L+H+x1-x
                else:
                    distance = 2*L+H+y1-y
                perimeter.append((distance,label))
    assert len({d for d,a in perimeter}) == len(perimeter)
    word = tuple(a for d,a in sorted(perimeter))
    crossing_points = {}
    crossing_pairs = 0
    for i,j in combinations(range(len(segments)),2):
        A,B,C = segments[i]
        D,E,F = segments[j]
        det = A*E-B*D
        if not det:
            continue
        x,y = Fraction(C*E-B*F,det),Fraction(A*F-C*D,det)
        if x0 < x < x1 and y0 < y < y1:
            crossing_points.setdefault((x,y),set()).update((i,j))
            crossing_pairs += 1
    assert len(crossing_set(word)) == crossing_pairs
    degrees = Counter(map(len,crossing_points.values()))
    return word, segments, crossing_pairs, dict(degrees)


def grid():
    for L in (1,2,3):
        w,lines,pairs,degrees = rectangle_word(L,L)
        print("GRID START",L,"word",w,"lines",lines,"pairs",pairs,"vertex_degrees",degrees,flush=True)
        assert len(lines) == 6*L and pairs == 7*L*L
        assert degrees == {4:L*L,2:L*L}
        count = cut_count(key(w))
        print("GRID COMPLETE",L,count,"entropy numerical",log2(count)/(L*L),
              "memo",cut_count.cache_info(),flush=True)
        assert count == {1:8,2:10442,3:4419734746}[L]
    for L,H in ((1,2),(2,1),(1,3),(3,1),(2,3),(3,2)):
        w,lines,pairs,degrees = rectangle_word(L,H)
        count = cut_count(key(w))
        assert len(lines)==3*(L+H) and pairs == 7*L*H
        assert degrees == {4:L*H,2:L*H}
        print("RECTANGLE COMPLETE",L,H,count,flush=True)
    print("COEFFICIENT numerical",(1+log2(4419734746)/9)/24,flush=True)


def finite_grid():
    for t in range(0,13):
        lines = [(A,B,C) for A,B in ((1,0),(0,1),(-1,1),(1,1))
                 for C in range(-t,t+1)]
        points = {}
        for i,j in combinations(range(len(lines)),2):
            A,B,C = lines[i]
            D,E,F = lines[j]
            det = A*E-B*D
            if det:
                point = Fraction(C*E-B*F,det),Fraction(A*F-C*D,det)
                points.setdefault(point,set()).update((i,j))
        degrees = Counter(map(len,points.values()))
        assert degrees[4] == 2*t*t+2*t+1
        assert degrees[3] == 2*t*t+2*t
        assert all(len(v)<=2 or (x.denominator==1 and y.denominator==1)
                   for (x,y),v in points.items())
        print("FINITE GRID COMPLETE",t,"m",2*t+1,"vertex_degrees",dict(degrees),flush=True)
    for t in (3,5,10,20,40,80):
        cells = 0
        for i in range(-t//3-2,t//3+3):
            for j in range(-t//3-2,t//3+3):
                if all(abs(Fraction(3*i,1)+dx)+abs(Fraction(3*j,1)+dy)<=t
                       for dx in (Fraction(1,10),Fraction(31,10))
                       for dy in (Fraction(1,5),Fraction(16,5))):
                    cells += 1
        lost_scaled = Fraction(2*t*t,9)-cells
        print("TILING density",t,"patches",cells,"area_over_9_minus_patches",str(lost_scaled),
              "lost_over_t",str(lost_scaled/t),flush=True)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--task",choices=("algebra","fibers","grid","finite-grid"),required=True)
    p.add_argument("--worker",action="store_true")
    p.add_argument("--timeout",type=float,default=55)
    args = p.parse_args()
    if args.worker:
        print("R1 independent code",platform.python_version(),"stdlib only",flush=True)
        print("Finite evidence, never an unrestricted proof",flush=True)
        {"algebra":algebra,"fibers":fibers,"grid":grid,"finite-grid":finite_grid}[args.task]()
        return
    stem = HERE/("secondpass-review-1-"+args.task)
    argv = [sys.executable,str(Path(__file__).resolve()),"--task",args.task,"--worker"]
    started = time.monotonic()
    with Path(str(stem)+".log").open("w") as output:
        child = subprocess.Popen(argv,cwd=ROOT,stdout=output,stderr=subprocess.STDOUT)
        job = {"started_utc":datetime.now(timezone.utc).isoformat(),"pid":child.pid,
               "argv":argv,"cwd":str(ROOT),"timeout_seconds":args.timeout,"state_limit":STATE_LIMIT,
               "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               "stdout":str(stem)+".log","status":"running"}
        Path(str(stem)+"-job.json").write_text(json.dumps(job,indent=2)+"\n")
        print(json.dumps(job),flush=True)
        try:
            code = child.wait(timeout=args.timeout)
            job["status"] = "complete" if code == 0 else "failed_incomplete"
        except subprocess.TimeoutExpired:
            child.terminate()
            try:
                code = child.wait(timeout=2)
            except subprocess.TimeoutExpired:
                child.kill()
                code = child.wait(timeout=2)
            job["status"] = "timeout_incomplete"
        job.update(returncode=code,elapsed_seconds=time.monotonic()-started,
                   finished_utc=datetime.now(timezone.utc).isoformat())
        Path(str(stem)+"-job.json").write_text(json.dumps(job,indent=2)+"\n")
        print(json.dumps(job),flush=True)
    if code != 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
