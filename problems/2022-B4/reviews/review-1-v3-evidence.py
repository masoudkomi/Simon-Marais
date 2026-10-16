#!/usr/bin/env python3
"""Bounded exact finite evidence for R1's independent v3 re-audit."""

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import platform
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
LOG = HERE / "review-1-v3-evidence-output.txt"
JOB = HERE / "review-1-v3-evidence-job.json"
TIMEOUT = 45


def record(check, **data):
    print(json.dumps({"check": check, **data}, sort_keys=True), flush=True)


def F(a, b):
    return a + 2 * (b // 20), b + 3 * (a // 30)


def c(d, r):
    return 3 * ((r + d) // 30)


def D(d, r):
    return d + 2 * (r // 20) - c(d, r)


def successors(d, r):
    h = D(d, r)
    return [(h, (6 * e + r + c(d, r)) % 60) for e in range(10)]


def policy_path(d, r):
    states = [(d, r)]
    controls = []
    while d:
        h = D(d, r)
        if h:
            low = 30 if h > 0 else 20
            s = low + (r + c(d, r) - low) % 6
            e = ((s - r - c(d, r)) // 6) % 10
        else:
            e = 0
        d, r = successors(d, r)[e]
        controls.append(e)
        states.append((d, r))
        assert len(controls) <= 5000
    return states, controls


def survive_class(delta, r, qclass, n):
    b = 60 * (qclass + 100 * 10**n) + r
    a = b + delta
    assert a > 0 and b > 0 and a*b >= 600
    if a == b:
        return False
    for _ in range(n):
        a, b = F(a, b)
        if a == b:
            return False
    return True


def worker():
    record("environment", python=sys.version, platform=platform.platform(),
           dependencies="Python standard library only; exact integer arithmetic")
    expected = {
        "problems/2022-B4/proof-extension-v3.md": "0238f99a93b0ba1076484db1c16b173efcc02be4410e859f2c5bafc55f0f2a3f",
        "problems/2022-B4/proof.md": "8b35be18bb70f81b623f78e7dd1a148478c698c1f5ad32e4097def92ff75aed3",
        "problems/2022-B4/proof-extension-v2.md": "b41aff3fcfadd33f80fdec80570d5b2f61807a5b9e16a28becacefaa237743ed",
        "problems/2022-B4/reviews/review-1.md": "6f7f8fa9ce0bcc08ed0738f2db587ad2ef1e0c5f269d9aac975033c8cfe29e60",
        ".cache/official/2022-paper_b.pdf": "33b15241e89b2e4db54f78d3a565ee01afe357ade786f8bb7602c0b7e89e4519",
        ".cache/official/2022-solutions.pdf": "3e1670aef22b83cd2be13d027728ebed119072011e4150d7c3aa8dba3101295f",
    }
    actual = {name: sha256((ROOT / name).read_bytes()).hexdigest() for name in expected}
    assert actual == expected
    record("frozen_inputs", hashes=actual)

    samples = 0
    residual_range = set()
    ds = list(range(-10000, 10001)) + [-10**100-1, -10**100, 10**100, 10**100+1]
    for d in ds:
        for r in range(60):
            u = r+d-30*((r+d)//30)
            v = r-20*(r//20)
            assert 0 <= u <= 29 and 0 <= v <= 19
            assert 10*D(d, r) == 9*d+u-v
            assert 10*abs(D(d, r)) <= 9*abs(d)+29
            residual_range.add(u-v)
            samples += 1
    record("exact_remainders_and_radius_inequality", samples=samples,
           d_interval=[-10000, 10000], additional_d=[str(d) for d in ds[-4:]],
           observed_u_minus_v=[min(residual_range), max(residual_range)])

    radius_cases = []
    for M in (29, 30, 31, 100, 1000):
        maximum = 0
        for d in range(-M, M+1):
            for r in range(60):
                assert abs(D(d, r)) <= M
                maximum = max(maximum, abs(D(d, r)))
        radius_cases.append({"M": M, "states": (2*M+1)*60,
                             "max_successor_absolute_difference": maximum})
    record("all_states_in_selected_radii", cases=radius_cases)

    for h in list(range(1, 1001)) + [10**100]:
        for s in range(30, 36):
            value = D(h, s)
            assert value == 0 if h == 1 else 0 < value <= h-1
            assert 10*value >= 9*h-15
    for k in list(range(1, 1001)) + [10**100]:
        for s in range(20, 26):
            value = D(-k, s)
            assert value >= -k+2
            assert value == {1: 1, 2: 0, 3: -1}[k] if k <= 3 else value < 0
            assert 10*value < -9*k+30
    for M in range(29, 10001):
        assert (M+1)//2+1 <= M
    record("local_sign_bounds", positive_h_samples=1001, negative_k_samples=1001,
           checked_M_interval=[29, 10000], endpoints=[1, 2, 3, 4])

    path_cases = []
    for M in (29, 30, 31, 100):
        lengths = Counter()
        for d in range(-M, M+1):
            for r in range(60):
                states, controls = policy_path(d, r)
                assert len(controls) <= M+1
                assert all(abs(h) <= M for h, s in states)
                lengths[len(controls)] += 1
        path_cases.append({"M": M, "K": M+1, "states": sum(lengths.values()),
                           "maximum_policy_length": max(lengths)})
    huge_paths = []
    for delta in (-10**100, 10**100):
        M = max(abs(delta), 29)
        for r in (0, 19, 20, 29, 30, 39, 40, 59):
            states, controls = policy_path(delta, r)
            assert len(controls) <= M+1
            assert all(abs(h) <= M for h, s in states)
            huge_paths.append({"delta": str(delta), "r": r, "length": len(controls)})
    record("uniform_policy_path_evidence", finite_radii=path_cases,
           huge_difference_paths=huge_paths,
           note="Finite checks support, and are not premises of, the analytic all-prefix proof")

    lifting_cases = 0
    shifts_checked = 0
    for delta in (-1000, -29, -1, 0, 1, 29, 1000):
        for r in (0, 19, 20, 29, 30, 39, 40, 59):
            for n in range(5):
                words = set()
                for qclass in range(10**n):
                    b = 60*(qclass+100*10**n)+r
                    a = b+delta
                    aa, bb = a+60*10**n, b+60*10**n
                    word = []
                    for i in range(n+1):
                        assert (a-b, b % 60) == (aa-bb, bb % 60)
                        assert (aa-a, bb-b) == (60*11**i*10**(n-i),)*2
                        if i < n:
                            assert (b//60) % 10 == (bb//60) % 10
                            word.append((b//60) % 10)
                            a, b = F(a, b)
                            aa, bb = F(aa, bb)
                        shifts_checked += 1
                    words.add(tuple(word))
                assert len(words) == 10**n
                lifting_cases += 1
    record("finite_lifting_and_class_periodicity", cases=lifting_cases,
           word_lengths=[0, 1, 2, 3, 4], compared_states=shifts_checked,
           deltas=[-1000, -29, -1, 0, 1, 29, 1000],
           initial_residues=[0, 19, 20, 29, 30, 39, 40, 59])

    counting = []
    for delta in (-30, -1, 0, 1, 30):
        M = max(abs(delta), 29)
        K = M+1
        state_counts = {(delta, r): 1 for r in range(60)} if delta else {}
        A = [sum(state_counts.values())]
        for n in range(1, 2*K+1):
            next_counts = Counter()
            for (d, r), multiplicity in state_counts.items():
                assert abs(d) <= M
                for h, s in successors(d, r):
                    assert abs(h) <= M
                    if h:
                        next_counts[(h, s)] += multiplicity
            state_counts = next_counts
            A.append(sum(state_counts.values()))
        for n in range(K+1):
            assert A[n+K] <= (10**K-1)*A[n]
        for n in range(4):
            direct = sum(survive_class(delta, r, qclass, n)
                         for r in range(60) for qclass in range(10**n))
            assert direct == A[n]
        assert A[K] <= (10**K-1)*60
        assert A[2*K] <= (10**K-1)**2*60
        counting.append({"delta": delta, "M": M, "K": K,
                         "A_0": A[0], "A_K": A[K], "A_2K": A[2*K],
                         "class_enumeration_lengths": [0, 1, 2, 3],
                         "conditional_count_checked_for_N": [0, K]})
    record("exact_finite_class_counts", cases=counting,
           note="Dynamic counts are exact finite graph-word counts; direct initial-class counts cross-check lengths 0-3")

    witnesses = []
    for a0, b0, steps in ((599, 600, 3), (25, 24, 4)):
        a, b = a0, b0
        orbit = []
        M = max(abs(a-b), 29)
        for n in range(steps+1):
            assert a != b
            assert abs(a-b) <= M
            orbit.append([a, b, a-b, b % 60])
            if n < steps:
                a, b = F(a, b)
        states, controls = policy_path(a-b, b % 60)
        assert len(controls) <= M+1
        witnesses.append({"start": [a0, b0], "orbit_through_old_block": orbit,
                          "new_M": M, "new_K": M+1,
                          "continuation_policy_length": len(controls)})
    record("old_witnesses_under_repaired_bound", cases=witnesses)

    # Confirm that the frozen initial review and all proof versions stayed unchanged.
    final = {name: sha256((ROOT / name).read_bytes()).hexdigest() for name in expected}
    assert final == expected
    record("complete", status="all finite checks passed; no new objection found",
           frozen_input_hashes_unchanged=True)


def main():
    command = [sys.executable, "-u", str(Path(__file__).resolve()), "--worker"]
    start = time.time()
    with LOG.open("w") as output:
        child = subprocess.Popen(command, cwd=ROOT, stdout=output, stderr=subprocess.STDOUT)
        job = {"command": command, "cwd": str(ROOT), "pid": child.pid,
               "started_unix": start, "timeout_seconds": TIMEOUT,
               "stdout": str(LOG), "arithmetic": "exact integers"}
        JOB.write_text(json.dumps(job, indent=2)+"\n")
        print(json.dumps({"child_pid": child.pid, "timeout_seconds": TIMEOUT,
                          "log": str(LOG)}), flush=True)
        try:
            code = child.wait(timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            child.terminate()
            try:
                child.wait(timeout=3)
            except subprocess.TimeoutExpired:
                child.kill()
                child.wait()
            code = 124
        job.update(returncode=code, completed_unix=time.time(), elapsed_seconds=time.time()-start)
        JOB.write_text(json.dumps(job, indent=2)+"\n")
    print(LOG.read_text(), end="")
    raise SystemExit(code)


if __name__ == "__main__":
    worker() if "--worker" in sys.argv else main()
