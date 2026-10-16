#!/usr/bin/env python3
"""Independent fixed-boundary patch counter and complete-arrangement fiber check.

Standard library only, Python 3.12. A driver launches one dedicated child with
an explicit wall-clock cap, preserves its PID/arguments, and records incremental
stdout. It terminates only that child on timeout. No files outside this year's
secondpass-* namespace are modified. The original enumerator is a read-only
oracle; bytecode writing is disabled.

The cut recurrence is independently implemented from the mathematical recipe
in Cortes Kuhnast et al., arXiv:2402.13107v2, Section 5.1. It counts boundary
labelled minimal chord arrangements, not insertion histories or symmetry
classes. Canonical rotations/reflections are used only to reuse equal COUNTS.

Default: exhaustive all paired boundary words through seven strands, plus
small MacMahon tests; one child, 90-second cap, 250000 memo states.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from functools import lru_cache
import hashlib
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import platform
import subprocess
import sys
from time import monotonic

sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
STATE_CAP = 250000


def normalize(word):
    labels = {}
    return tuple(labels.setdefault(x, len(labels)) for x in word)


def canonical(word):
    if not word:
        return ()
    word = tuple(word)
    return min(normalize(w[i:] + w[:i])
               for w in (word, word[::-1]) for i in range(len(word)))


@lru_cache(None)
def count_patch(word):
    if count_patch.cache_info().currsize > STATE_CAP:
        raise RuntimeError("memo-state cap exceeded; computation incomplete")
    if not word:
        return 1
    labels = sorted(set(word))
    candidates = []
    for z in labels:
        start, end = [i for i, x in enumerate(word) if x == z]
        arc_a = word[start + 1:end]
        arc_b = word[end + 1:] + word[:start]
        cross = [x for x in arc_a if arc_a.count(x) == 1]
        candidates.append(((len(cross), max(len(arc_a), len(arc_b))),
                           arc_a, arc_b, cross))
    _, arc_a, arc_b, cross = min(candidates, key=lambda t: t[0])
    # For a,b crossing z, if their order on the two boundary arcs is
    # reversed, they do not cross each other: their order along z is forced.
    positions_b = {x: arc_b.index(x) for x in cross}
    predecessor = {x: set() for x in cross}
    for i, a in enumerate(cross):
        for b in cross[i + 1:]:
            if positions_b[a] > positions_b[b]:
                predecessor[b].add(a)

    def extensions(prefix, remaining):
        if not remaining:
            yield prefix
        else:
            for a in sorted(remaining):
                if not (predecessor[a] & remaining):
                    yield from extensions(prefix + (a,), remaining - {a})

    total = 0
    for order in extensions((), set(cross)):
        side_a = canonical(arc_a + order[::-1])
        side_b = canonical(arc_b + order)
        total += count_patch(side_a) * count_patch(side_b)
    return total


def paired_words(n):
    word = [-1] * (2 * n)

    def visit(unused, label):
        if not unused:
            yield tuple(word)
            return
        first = unused[0]
        for j in unused[1:]:
            word[first] = word[j] = label
            yield from visit(tuple(x for x in unused[1:] if x != j), label + 1)
        word[first] = -1

    yield from visit(tuple(range(2 * n)), 0)


def chord_crosses(p, q):
    a, b = sorted(p)
    c, d = sorted(q)
    return (a < c < b) != (a < d < b)


def completion_fiber(word, complete_signatures):
    """Straight chords through convex parabola points give fixed outside data.

    Complete signatures use strand labels in increasing slope order. A triple
    is free exactly if all its three pair crossings lie inside the patch.
    Nonfree triple signs are fixed to this exact rational straight completion.
    The proposed fiber theorem is a candidate, not assumed without this check.
    """
    n = len(word) // 2
    original_positions = {x: tuple(i for i, y in enumerate(word) if x == y)
                          for x in range(n)}
    triples = list(combinations(range(n), 3))
    for salt in range(20):
        points_x = [1 << ((i + 1)**2 + salt * (i + 1)) for i in range(2 * n)]
        lines = []
        for x, (i, j) in original_positions.items():
            lines.append((points_x[i] + points_x[j], points_x[i] * points_x[j], x))
        lines.sort()
        crossing_x = {(i, j): Fraction(lines[i][1] - lines[j][1],
                                       lines[i][0] - lines[j][0])
                      for i, j in combinations(range(n), 2)}
        if all(crossing_x[a, b] != crossing_x[b, c] for a, b, c in triples):
            break
    else:
        raise RuntimeError("no nondegenerate exact completion found")
    positions = [original_positions[line[2]] for line in lines]
    pair_inside = {(i, j): chord_crosses(positions[i], positions[j])
                   for i, j in combinations(range(n), 2)}
    free = 0
    base = 0
    for bit, (a, b, c) in enumerate(triples):
        base |= (crossing_x[a, b] > crossing_x[b, c]) << bit
        if pair_inside[a, b] and pair_inside[a, c] and pair_inside[b, c]:
            free |= 1 << bit
    fixed = ((1 << len(triples)) - 1) ^ free
    count = sum((s & fixed) == (base & fixed) for s in complete_signatures)
    return count, free.bit_count(), sum(pair_inside.values())


def macmahon(a, b, c):
    result = Fraction(1)
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            result *= Fraction(i + j + c - 1, i + j - 1)
    assert result.denominator == 1
    return result.numerator


def bundle_word(sizes):
    first = []
    second = []
    start = 0
    for size in sizes:
        group = list(range(start, start + size))
        first.extend(group)
        second.extend(group[::-1])
        start += size
    return tuple(first + second)


def worker(max_n):
    source = BASE / "enumerate_small.py"
    spec = importlib.util.spec_from_file_location("firstpass_oracle", source)
    oracle = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(oracle)
    print(f"Python {platform.python_version()}; standard library only", flush=True)
    print("oracle_sha256=" + hashlib.sha256(source.read_bytes()).hexdigest(), flush=True)
    print("Exact finite evidence; candidate boundary-fiber theorem not thereby proved", flush=True)
    examples = {}
    for n in range(1, max_n + 1):
        signatures = oracle.one_change_signs(n)
        checked = 0
        unique = set()
        fiber_cache = {}
        for word in paired_words(n):
            key = canonical(word)
            value = count_patch(key)
            if key not in fiber_cache:
                fiber_cache[key] = completion_fiber(key, signatures)
            fiber, triangles, edges = fiber_cache[key]
            if value != fiber:
                print("MISMATCH", n, key, value, fiber, triangles, edges, flush=True)
                raise AssertionError("fiber comparison failed")
            examples.setdefault((n, edges), {}).setdefault(value, key)
            checked += 1
            unique.add(key)
        print(f"n={n} paired_words={checked} canonical_boundary_words={len(unique)} "
              f"all_cut_counts_equal_fiber_counts=True "
              f"memo_states={count_patch.cache_info().currsize}", flush=True)
    for sizes in ((1, 1, 1), (1, 2, 3), (2, 2, 2), (2, 2, 3), (3, 3, 3), (2, 3, 4)):
        value = count_patch(canonical(bundle_word(sizes)))
        exact = macmahon(*sizes)
        assert value == exact
        print(f"MacMahon sizes={sizes} count={value} equality=True "
              f"memo_states={count_patch.cache_info().currsize}", flush=True)
    for (n, edges), variants in sorted(examples.items()):
        if n == 4 and len(variants) > 1:
            print("same_strands_same_crossing_count_different_patch_counts", n, edges,
                  sorted(variants.items()), flush=True)
            break
    print("COMPLETE", flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--max-n", type=int, default=7)
    parser.add_argument("--timeout", type=float, default=90)
    args = parser.parse_args()
    if args.worker:
        worker(args.max_n)
        return
    command = [sys.executable, str(Path(__file__).resolve()), "--worker",
               "--max-n", str(args.max_n)]
    output_path = BASE / "secondpass-patchcount-output.txt"
    job_path = BASE / "secondpass-patchcount-job.json"
    start = monotonic()
    with output_path.open("w") as output:
        child = subprocess.Popen(command, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT)
        job = {"started_utc": datetime.now(timezone.utc).isoformat(),
               "pid": child.pid, "command": command, "cwd": str(ROOT),
               "timeout_seconds": args.timeout, "state_cap": STATE_CAP,
               "stdout": str(output_path), "status": "running"}
        job_path.write_text(json.dumps(job, indent=2) + "\n")
        print(f"child_pid={child.pid}; job={job_path}; stdout={output_path}", flush=True)
        try:
            code = child.wait(timeout=args.timeout)
            job["status"] = "complete" if code == 0 else "failed"
        except subprocess.TimeoutExpired:
            child.terminate()
            try:
                code = child.wait(timeout=2)
            except subprocess.TimeoutExpired:
                child.kill()
                code = child.wait(timeout=2)
            job["status"] = "timeout_incomplete"
        job["returncode"] = code
        job["elapsed_seconds"] = monotonic() - start
        job["finished_utc"] = datetime.now(timezone.utc).isoformat()
        job_path.write_text(json.dumps(job, indent=2) + "\n")
    print(json.dumps(job, sort_keys=True), flush=True)
    if job["status"] != "complete":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
