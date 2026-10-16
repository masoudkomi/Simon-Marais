"""Blind R1 audit. No author module is imported or executed.

The binary filter and all rational families are reconstructed from ordinary
coefficients c_t and H_r(f)(w)=sum_{t>=r} binom(t,r)c_t w^(t-r).
The full certificate audit uses SymPy's separate finite-field gcd code.
Run this file without arguments for a bounded child and JSONL checkpoints.
"""
from __future__ import annotations

import collections
import hashlib
import json
import math
import os
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[3]
PROBLEM = ROOT / "problems/2021-B4"
MOD = 19**2
FULL_MASK = (1 << 17) - 1


def emit(**record):
    print(json.dumps(record, sort_keys=True), flush=True)


def trimmed(poly):
    result = list(poly)
    while result and not result[-1]:
        result.pop()
    return result


def accumulate(target, source, multiplier=1, shift=0):
    if not source:
        return
    needed = len(source) + shift
    target.extend([0] * max(0, needed - len(target)))
    for k, coefficient in enumerate(source):
        target[k + shift] += multiplier * coefficient


def direct_family(center_mask, u_mask):
    """Solve for c_18,c_17,...,c_2 without the normalized a_j recurrence."""
    ordinary = [[] for _ in range(21)]
    ordinary[20] = [1]
    ordinary[19] = [-20]
    for r in range(18, 1, -1):
        flag = 1 << (18 - r)
        if not ((center_mask | u_mask) & flag):
            continue  # H_r(0)=c_r=0.
        value = []
        for t in range(r + 1, 21):
            accumulate(value, ordinary[t], -math.comb(t, r),
                       t - r if u_mask & flag else 0)
        ordinary[r] = trimmed(value)
    p_poly, q_poly = [], []
    for t, coefficient in enumerate(ordinary):
        accumulate(p_poly, coefficient)
        accumulate(q_poly, coefficient, shift=t)
    return trimmed(p_poly), trimmed(q_poly), ordinary


def binary_patterns():
    """Traverse all flags using c_t modulo 19^2 rather than a_j modulo 19."""
    ordinary = [0] * 21
    ordinary[20], ordinary[19] = 1, -20 % MOD
    passing = {}
    visited = 0

    def visit(r, mask):
        nonlocal visited
        if r == 1:
            visited += 1
            if sum(ordinary) % MOD == 0:
                unit_j = [20 - t for t in range(2, 19) if ordinary[t] % MOD]
                assert unit_j
                passing[mask] = max(unit_j)
            return
        ordinary[r] = 0
        visit(r - 1, mask)
        ordinary[r] = -sum(math.comb(t, r) * ordinary[t]
                           for t in range(r + 1, 21)) % MOD
        assert ordinary[r] % 19 == 0
        visit(r - 1, mask | (1 << (18 - r)))
        ordinary[r] = 0

    visit(18, 0)
    assert visited == 2**17
    j17 = sorted(mask for mask, j in passing.items()
                 if j == 17 and mask & (1 << 16))
    j16 = sorted(mask for mask, j in passing.items()
                 if j == 16 and mask & ((1 << 16) | (1 << 15)))
    survivors = sorted(mask for mask, j in passing.items()
                       if j < 16 or (j == 16 and mask in j16))
    histogram = dict(sorted(collections.Counter(passing.values()).items()))
    emit(event="binary_complete", visited=visited, passing=len(passing),
         j_histogram=histogram, j17_h2_retained=len(j17),
         j16_h2_or_h3_retained=len(j16), combined_survivors=len(survivors),
         j17_center_masks=j17, j16_retained_masks=j16,
         survivors_sha256=hashlib.sha256(json.dumps(survivors).encode()).hexdigest())
    assert len(passing) == 6680
    assert histogram[18] == 3043 and histogram[17] == 1674 and histogram[16] == 887
    assert len(j17) == 73 and len(j16) == 88 and len(survivors) == 1164
    assert all(mask & (1 << 15) for mask in j17)
    return j17


def all_refinements(center_masks):
    result = set()
    for center in center_masks:
        available = FULL_MASK ^ center
        u = available
        while True:
            result.add((center, u))
            if u == 0:
                break
            u = (u - 1) & available
    return result


def audit_certificates(expected):
    import sympy
    from sympy.polys.domains import ZZ
    from sympy.polys.galoistools import gf_gcd

    path = PROBLEM / "computations/padic-rational-j17-certificates.jsonl"
    assert hashlib.sha256(path.read_bytes()).hexdigest() == (
        "9676e4885d670a23ea1fb1b0a151ec1f9a8cece8532a1dd43277450b3a7a7fc3")
    seen, histogram = set(), collections.Counter()
    independent_stream = hashlib.sha256()
    author_stream = hashlib.sha256()
    audit_started = time.monotonic()
    degrees = collections.Counter()
    for count, line in enumerate(path.open(), start=1):
        record = json.loads(line)
        key = record["center_mask"], record["u_mask"]
        assert key in expected and key not in seen, (count, key)
        seen.add(key)
        assert not (key[0] & key[1]) and not ((key[0] | key[1]) & ~FULL_MASK)
        p_poly, q_poly, ordinary = direct_family(*key)
        assert p_poly and q_poly
        actual_degrees = [len(p_poly) - 1, len(q_poly) - 1]
        assert actual_degrees == record["degrees"], (key, actual_degrees, record)
        degrees[tuple(actual_degrees)] += 1
        # Every c_(20-j) must be exactly divisible coefficientwise by binom(20,j).
        # This cross-checks the author's normalized-polynomial convention.
        for r in range(2, 19):
            assert all(c % math.comb(20, r) == 0 for c in ordinary[r]), (key, r)
        # Only the serialization lines (97-101) of the author's file were read
        # after implementing direct_family. No generation/gcd code was read.
        raw = json.dumps([*key, p_poly, q_poly], separators=(",", ":"))
        assert hashlib.sha256(raw.encode()).hexdigest() == record["polynomials_sha256"], key
        author_stream.update((raw + "\n").encode())
        independent_stream.update(json.dumps({"key": key, "P": p_poly, "Q": q_poly},
                                            sort_keys=True, separators=(",", ":")).encode())
        independent_stream.update(b"\n")
        if record["status"] == "constant_nonzero":
            assert len(p_poly) == 1 and p_poly[0] != 0
            assert record["constant"] == p_poly[0]
            histogram["constant_nonzero"] += 1
        else:
            assert record["status"] == "coprime_mod_prime"
            prime = record["prime"]
            assert prime in (101, 103, 107, 109) and sympy.isprime(prime)
            residues = [p_poly[-1] % prime, q_poly[-1] % prime]
            assert all(residues) and residues == record["leading_residues"]
            left = [value % prime for value in reversed(p_poly)]
            right = [value % prime for value in reversed(q_poly)]
            divisor = gf_gcd(left, right, prime, ZZ)
            assert divisor == [1], (key, prime, divisor)
            assert record["gcd_degree"] == 0
            histogram[f"coprime_mod_{prime}"] += 1
        if count % 512 == 0:
            emit(event="certificate_checkpoint", checked=count,
                 elapsed_seconds=round(time.monotonic() - audit_started, 3),
                 counts=dict(histogram))
    assert seen == expected
    assert count == 29928
    assert dict(histogram) == {"constant_nonzero": 73, "coprime_mod_101": 28583,
                               "coprime_mod_103": 1213, "coprime_mod_107": 55,
                               "coprime_mod_109": 4}
    assert author_stream.hexdigest() == "47a5b912863c67f22fed42daaf92b72949a06164966037ac97e4ad8afd22395b"
    emit(event="certificates_complete", checked=count, all_expected_pairs_seen=True,
         counts=dict(histogram), degree_histogram={str(k): v for k, v in sorted(degrees.items())},
         independent_polynomial_stream_sha256=independent_stream.hexdigest(),
         author_polynomial_stream_sha256=author_stream.hexdigest(),
         author_hash_encoding="compact JSON [center_mask,u_mask,P,Q]", sympy_version=sympy.__version__,
         elapsed_seconds=round(time.monotonic() - audit_started, 3))


def initial_forms():
    # Normalize C=1 and test all nonzero B/C residues, deriving A from alpha.
    rows = []
    inv5 = pow(5, -1, 19)
    for b in range(1, 19):
        alpha, beta = -2 * b * inv5 % 19, -3 * b * inv5 % 19
        a = -(b * alpha + alpha**2) % 19
        assert a and alpha and beta and alpha != beta
        assert (a + 3*b*alpha + 6*alpha**2) % 19 == 0
        assert (a + b*beta + beta**2) % 19 == 0
        h3a, h3b = (b + 4*alpha) % 19, (b + 4*beta) % 19
        assert h3a == -3*b*inv5 % 19 and h3a
        assert h3b == -7*b*inv5 % 19 and h3b
        rows.append([b, a, alpha, beta, h3a, h3b])
    emit(event="j16_initial_forms_complete", column_order=["B/C", "A/C", "alpha", "beta", "H3alpha/C", "H3beta/C"], rows=rows)


def worker():
    emit(event="worker_start", pid=os.getpid(), python=sys.version,
         method="ordinary Hasse c_r equations; binary modulo 361; SymPy GF gcd",
         imported_author_code=False)
    masks = binary_patterns()
    expected = all_refinements(masks)
    assert len(expected) == 29928
    emit(event="refinement_coverage_derived", expected_count=len(expected))
    initial_forms()
    audit_certificates(expected)
    emit(event="worker_complete", elapsed_seconds=round(time.monotonic() - started, 3))


started = time.monotonic()
if __name__ == "__main__":
    if "--worker" in sys.argv:
        worker()
    else:
        command = [sys.executable, "-u", str(pathlib.Path(__file__).resolve()), "--worker"]
        process = subprocess.Popen(command, cwd=ROOT)
        emit(event="supervisor_start", pid=os.getpid(), child_pid=process.pid,
             timeout_seconds=180, command=command)
        try:
            returncode = process.wait(timeout=180)
        except subprocess.TimeoutExpired:
            process.kill()
            returncode = process.wait()
            emit(event="timeout", killed_only_child_pid=process.pid, returncode=returncode)
            sys.exit(124)
        emit(event="supervisor_complete", child_pid=process.pid, returncode=returncode,
             elapsed_seconds=round(time.monotonic() - started, 3))
        sys.exit(returncode)
