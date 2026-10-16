#!/usr/bin/env python3
"""Independent, bounded, exact finite evidence for review 1; no unrestricted claim."""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
LOG = HERE / "review-1-evidence-output.txt"
JOB = HERE / "review-1-evidence-job.json"
TIMEOUT = 40


def checkpoint(name, **data):
    print(json.dumps({"check": name, **data}, sort_keys=True), flush=True)


def F(a, b):
    return a + 2 * (b // 20), b + 3 * (a // 30)


def c(d, r):
    return 3 * ((r + d) // 30)


def D(d, r):
    return d + 2 * (r // 20) - c(d, r)


def successors(state):
    d, r = state
    return [(D(d, r), (6 * e + r + c(d, r)) % 60) for e in range(10)]


def L(h):
    return h if h > 0 else 0 if h == 0 else ((-h + 1) // 2 + 1)


def K(d):
    return 1 + max(L(D(d, r)) for r in range(60))


def path(state):
    states, controls = [state], []
    while states[-1][0] != 0:
        d, r = states[-1]
        h = D(d, r)
        if h == 0:
            e = 0
        else:
            start = 30 if h > 0 else 20
            s = start + ((r + c(d, r) - start) % 6)
            e = ((s - r - c(d, r)) // 6) % 10
            assert (6 * e + r + c(d, r)) % 60 == s
        controls.append(e)
        states.append(successors((d, r))[e])
        assert len(controls) <= 1000
    return states, controls


def worker():
    checkpoint("environment", python=sys.version, platform=platform.platform(),
               dependency_note="Python standard library only; exact integer/Fraction arithmetic")
    expected = {
        "problems/2022-B4/proof.md": "8b35be18bb70f81b623f78e7dd1a148478c698c1f5ad32e4097def92ff75aed3",
        "problems/2022-B4/proof-extension-v2.md": "b41aff3fcfadd33f80fdec80570d5b2f61807a5b9e16a28becacefaa237743ed",
        ".cache/official/2022-paper_b.pdf": "33b15241e89b2e4db54f78d3a565ee01afe357ade786f8bb7602c0b7e89e4519",
        ".cache/official/2022-solutions.pdf": "3e1670aef22b83cd2be13d027728ebed119072011e4150d7c3aa8dba3101295f",
    }
    hashes = {name: sha256((ROOT / name).read_bytes()).hexdigest() for name in expected}
    assert hashes == expected, hashes
    checkpoint("input_hashes", hashes=hashes)

    checks = 0
    for d in range(-120, 121):
        for r in range(60):
            for q in (0, 1, 9, 10, 101):
                a, b = 60 * q + r + d, 60 * q + r
                aa, bb = F(a, b)
                assert aa - bb == D(d, r)
                assert bb == 66 * q + r + c(d, r)
                assert bb % 60 == (6 * (q % 10) + r + c(d, r)) % 60
                checks += 1
            ss = successors((d, r))
            assert len(set(ss)) == 10
            assert {s % 6 for h, s in ss} == {(r + c(d, r)) % 6}
    checkpoint("P1_quotient_and_successors", exact_samples=checks,
               d_range=[-120, 120], residues=60)

    shift_checks = 0
    for d in (-1000, -13, -1, 0, 1, 23, 1000):
        for r in (0, 19, 20, 29, 30, 39, 40, 59):
            for m in range(5):
                for z in (-3, -1, 0, 1, 7):
                    a, b = 6000000 + r + d, 6000000 + r
                    aa, bb = a + 60 * 10**m * z, b + 60 * 10**m * z
                    for i in range(m + 1):
                        shift = 60 * 11**i * 10**(m - i) * z
                        assert (aa - a, bb - b) == (shift, shift)
                        assert (aa - bb, bb % 60) == (a - b, b % 60)
                        a, b = F(a, b)
                        aa, bb = F(aa, bb)
                        shift_checks += 1
    checkpoint("P1_common_shift", exact_samples=shift_checks,
               m_range=[0, 4], z_values=[-3, -1, 0, 1, 7])

    cases = 0
    for d in (-1000, -13, -1, 1, 23, 1000):
        for r in range(60):
            for n in (1, 2, 3):
                words = set()
                for qclass in range(10**n):
                    a, b = 60 * (qclass + 100 * 10**n) + r + d, 60 * (qclass + 100 * 10**n) + r
                    word = []
                    for _ in range(n):
                        word.append((b // 60) % 10)
                        a, b = F(a, b)
                    words.add(tuple(word))
                assert len(words) == 10**n
                cases += 1
    checkpoint("P1_finite_lifting", cases=cases, lengths=[1, 2, 3],
               differences=[-1000, -13, -1, 1, 23, 1000], residues=60)

    strip_states = [(d, r) for d in range(-13, 24) for r in range(60)]
    lengths = [len(path(x)[1]) for x in strip_states]
    assert max(lengths) <= 24
    checkpoint("P2_strip_path", states=len(strip_states), max_length=max(lengths),
               length_counts=dict(sorted(Counter(lengths).items())))

    arbitrary_cases = 0
    test_h = set(range(-1000, 1001)) | {-10**12, -10**6, 10**6, 10**12}
    for h in test_h:
        if h > 0:
            for s in range(30, 36):
                v = D(h, s)
                assert v == 0 if h == 1 else 0 < v < h
        elif h < 0:
            k = -h
            for s in range(20, 26):
                v = D(h, s)
                assert v >= -k + 2
                assert v == {1: 1, 2: 0, 3: -1}[k] if k <= 3 else v < 0
        arbitrary_cases += 1
    max_bound_slack = 0
    for d in range(-100, 101):
        for r in range(60):
            length = len(path((d, r))[1])
            assert d == 0 or length <= 1 + L(D(d, r))
            max_bound_slack = max(max_bound_slack, K(d) - length)
    checkpoint("v2_local_control_bounds", h_samples=arbitrary_cases,
               d_range=[-100, 100], initial_states=201*60,
               max_observed_K_slack=max_bound_slack)

    reverse = {x: [] for x in strip_states}
    for x in strip_states:
        for y in successors(x):
            assert y in reverse
            reverse[y].append(x)
    distances = {x: 0 for x in strip_states if x[0] == 0}
    queue = deque(distances)
    while queue:
        x = queue.popleft()
        for y in reverse[x]:
            if y not in distances:
                distances[y] = distances[x] + 1
                queue.append(y)
    assert len(distances) == len(strip_states)
    checkpoint("independent_graph_distance_evidence", states=len(distances),
               counts=dict(sorted(Counter(distances.values()).items())),
               note="Finite graph evidence only; no infinite integer lift is inferred")

    a, b = 599, 600
    orbit = []
    for n in range(4):
        orbit.append({"n": n, "a": a, "b": b, "d": a-b, "r": b % 60,
                      "control": (b // 60) % 10})
        a, b = F(a, b)
    assert K(-1) == 3
    assert (orbit[-1]["d"], orbit[-1]["r"]) == (3, 12)
    assert distances[(3, 12)] == 4
    layer = {(3, 12)}
    layers = []
    for step in range(1, 5):
        layer = {y for x in layer for y in successors(x)}
        layers.append({"step": step, "states": len(layer),
                       "differences": sorted({d for d, r in layer}),
                       "has_equality": any(d == 0 for d, r in layer)})
    assert not any(x["has_equality"] for x in layers[:3])
    assert layers[3]["has_equality"]
    checkpoint("v2_counterexample_to_reused_K", K_initial=K(-1), orbit=orbit,
               extension_layers=layers, shortest_hitting_path=4,
               note="Refutes the stated bound after every surviving prefix, not the density theorem")

    delay_cases = 0
    for nmax in range(1, 9):
        for t in (1, 2, 5):
            for r in range(20):
                b = 60 * 10**nmax * t + r
                a = b + 1
                assert a > 0 and b > 0 and a * b >= 600
                for n in range(nmax + 1):
                    assert b == 60 * 11**n * 10**(nmax - n) * t + r
                    assert a == b + 1
                    a, b = F(a, b)
                delay_cases += 1
    checkpoint("P3_delay_family", cases=delay_cases, N_range=[1, 8],
               t_values=[1, 2, 5], r_range=[0, 19])

    periodic_checks = 0
    for p in range(1, 5):
        A, B = 11**p, 10**p
        for H in (-100, -1, 0, 1, 100):
            for x0 in (-5, 0, 1, 10):
                x = Fraction(x0)
                for j in range(6):
                    assert (A-B)*B**j*x == A**j*((A-B)*x0+H)-H*B**j
                    x = (A*x+H)/B
                    periodic_checks += 1
    checkpoint("P4_iterated_affine_identity", exact_samples=periodic_checks,
               note="Checks identity only; unbounded divisibility inference is audited in report")
    checkpoint("complete", status="finite evidence complete; v2 density argument has blocking bound gap")


def main():
    command = [sys.executable, "-u", str(Path(__file__).resolve()), "--worker"]
    started = time.time()
    with LOG.open("w") as output:
        process = subprocess.Popen(command, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT)
        job = {"command": command, "cwd": str(ROOT), "pid": process.pid,
               "started_unix": started, "timeout_seconds": TIMEOUT,
               "stdout": str(LOG), "arithmetic": "exact integers/Fraction"}
        JOB.write_text(json.dumps(job, indent=2) + "\n")
        print(json.dumps({"child_pid": process.pid, "timeout_seconds": TIMEOUT,
                          "log": str(LOG)}), flush=True)
        try:
            returncode = process.wait(timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            process.terminate()
            try:
                process.wait(timeout=3)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()
            returncode = 124
        job.update(returncode=returncode, elapsed_seconds=time.time()-started,
                   completed_unix=time.time())
        JOB.write_text(json.dumps(job, indent=2) + "\n")
    print(LOG.read_text(), end="")
    raise SystemExit(returncode)


if __name__ == "__main__":
    worker() if "--worker" in sys.argv else main()
