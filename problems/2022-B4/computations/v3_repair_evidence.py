#!/usr/bin/env python3
"""Finite exact evidence for the v3 repair; no unrestricted theorem proof.

The supervisor uses one targeted subprocess with a 40-second wall timeout.
No CAS, third-party package, process-wide kill, or network access is used.
"""
import argparse
import collections
import datetime
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
FROZEN = {
    "problems/2022-B4/proof.md":
        "8b35be18bb70f81b623f78e7dd1a148478c698c1f5ad32e4097def92ff75aed3",
    "problems/2022-B4/proof-extension-v2.md":
        "b41aff3fcfadd33f80fdec80570d5b2f61807a5b9e16a28becacefaa237743ed",
    "problems/2022-B4/reviews/review-1.md":
        "6f7f8fa9ce0bcc08ed0738f2db587ad2ef1e0c5f269d9aac975033c8cfe29e60",
    "problems/2022-B4/reviews/review-2.md":
        "1fe554ad4e5c77a1cad18a739a05b7ad1ceba4a8bce0beee91d6d34eedefbc04",
}


def fingerprints():
    paths = list(FROZEN) + ["problems/2022-B4/proof-extension-v3.md"]
    result = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
              for p in paths}
    for p, expected in FROZEN.items():
        assert result[p] == expected, (p, result[p], expected)
    return result


def transition(d, r, e):
    c = 3 * ((r + d) // 30)
    return d + 2 * (r // 20) - c, (6 * e + r + c) % 60


def policy_path(d, r, radius):
    length = 0
    while d:
        c = 3 * ((r + d) // 30)
        h = d + 2 * (r // 20) - c
        if h == 0:
            length += 1
            break
        low = 30 if h > 0 else 20
        s = low + ((r + c - low) % 6)
        e = ((s - r - c) // 6) % 10
        dn, rn = transition(d, r, e)
        assert (dn, rn) == (h, s)
        assert abs(dn) <= radius
        d, r = dn, rn
        length += 1
        assert length <= radius + 1
    return length


def minimum_abstract_hit(state):
    queue = collections.deque([(state, 0)])
    seen = {state}
    while queue:
        (d, r), depth = queue.popleft()
        if d == 0:
            return depth
        for e in range(10):
            nxt = transition(d, r, e)
            if nxt not in seen:
                seen.add(nxt)
                queue.append((nxt, depth + 1))
    return None


def local_bound(d):
    def length(h):
        return h if h > 0 else (0 if h == 0 else (-h + 1) // 2 + 1)
    return 1 + max(length(transition(d, r, 0)[0]) for r in range(60))


def worker():
    print(json.dumps({"meaning": "finite exact repair evidence only",
                      "python": platform.python_version(), "pid": os.getpid(),
                      "fingerprints": fingerprints()}, sort_keys=True), flush=True)
    count = 0
    for d in range(-10000, 10001):
        for r in range(60):
            u = (r + d) % 30
            v = r % 20
            dn = transition(d, r, 0)[0]
            assert 10 * dn == 9 * d + u - v
            assert 10 * abs(dn) <= 9 * abs(d) + 29
            count += 1
        if d in (-10000, -5000, 0, 5000, 10000):
            print(f"remainder checkpoint d={d} cases={count}", flush=True)
    print(f"exact remainder/bound cases={count}", flush=True)

    for radius in (29, 30, 60, 100, 333):
        maximum = 0
        states = 0
        for d in range(-radius, radius + 1):
            for r in range(60):
                dn = transition(d, r, 0)[0]
                assert abs(dn) <= radius
                maximum = max(maximum, policy_path(d, r, radius))
                states += 1
        print(json.dumps({"radius": radius, "states": states,
                          "uniform_K": radius + 1,
                          "maximum_observed_policy_length": maximum}), flush=True)

    witness_data = []
    for start, prefix_length, expected_state, expected_min, expected_old in (
            ((599, 600), 3, (3, 12), 4, 3),
            ((25, 24), 4, (6, 27), 5, 4)):
        a, b = start
        path = [(a, b)]
        for _ in range(prefix_length):
            assert a != b and a > 0 and b > 0 and a * b >= 600
            a, b = a + 2 * (b // 20), b + 3 * (a // 30)
            path.append((a, b))
        state = a - b, b % 60
        assert state == expected_state
        old = local_bound(start[0] - start[1])
        minimum = minimum_abstract_hit(state)
        assert old == expected_old and minimum == expected_min
        radius = max(abs(start[0] - start[1]), 29)
        witness_data.append({"actual_prefix": path, "old_local_K": old,
                             "reached_state": state, "minimum_further_hit": minimum,
                             "new_uniform_K": radius + 1,
                             "new_policy_further_length": policy_path(*state, radius)})
    print(json.dumps({"reviewer_witnesses": witness_data}), flush=True)

    bijections = 0
    classes = 0
    for d in (-1000000, -31, -1, 0, 1, 31, 1000000):
        for r in (0, 19, 20, 29, 30, 35, 59):
            for n in (1, 2, 3):
                words = set()
                modulus = 10**n
                for q_residue in range(modulus):
                    b = 60 * (q_residue + modulus * (abs(d) + 600)) + r
                    a = b + d
                    assert a > 0 and b > 0 and a * b >= 600
                    word = []
                    for _ in range(n):
                        word.append((b // 60) % 10)
                        a, b = a + 2 * (b // 20), b + 3 * (a // 30)
                    words.add(tuple(word))
                    classes += 1
                assert len(words) == modulus
                bijections += 1
    print(f"finite lifting bijections={bijections} quotient classes={classes}", flush=True)
    print(json.dumps({"completed": True, "fingerprints_after": fingerprints()}, sort_keys=True), flush=True)


def supervise(tag):
    assert re.fullmatch(r"[a-zA-Z0-9_-]+", tag), "unsafe output tag"
    log_path = HERE / f"{tag}-output.txt"
    job_path = HERE / f"{tag}-job.json"
    command = [sys.executable, "-u", str(Path(__file__).resolve()), "--worker"]
    before = fingerprints()
    started = time.monotonic()
    with log_path.open("x") as log:
        child = subprocess.Popen(command, cwd=ROOT, stdout=log,
                                 stderr=subprocess.STDOUT)
        job = {"command": command, "cwd": str(ROOT), "child_pid": child.pid,
               "timeout_seconds": 40, "log_path": str(log_path),
               "started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "parameters": {"remainder_difference_range": [-10000, 10000],
                              "radii": [29, 30, 60, 100, 333],
                              "lifting_lengths": [1, 2, 3]},
               "proof_fingerprints_before": before}
        with job_path.open("x") as out:
            json.dump(job, out, indent=2, sort_keys=True)
            out.write("\n")
        timed_out = False
        try:
            code = child.wait(timeout=40)
        except subprocess.TimeoutExpired:
            timed_out = True
            child.terminate()
            try:
                code = child.wait(timeout=2)
            except subprocess.TimeoutExpired:
                child.kill()
                code = child.wait(timeout=2)
        job.update({"timed_out": timed_out, "return_code": code,
                    "elapsed_seconds": time.monotonic() - started,
                    "proof_fingerprints_after": fingerprints()})
        job_path.write_text(json.dumps(job, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"job_path": str(job_path), "log_path": str(log_path),
                      "return_code": code, "timed_out": timed_out,
                      "elapsed_seconds": job["elapsed_seconds"]}, indent=2))
    return code if code else (1 if timed_out else 0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--tag", default="v3-repair")
    args = parser.parse_args()
    if args.worker:
        worker()
    else:
        raise SystemExit(supervise(args.tag))
