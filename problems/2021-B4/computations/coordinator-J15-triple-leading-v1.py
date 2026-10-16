#!/usr/bin/env python3
"""Candidate J=15, multiplicity-three projection. Constructor, not review.

Explicitly adapts the first-order method of coordinator-J16-coupled-leading-v1.py.
The new low-coefficient equations and quintic derivative ratios are separate
unreviewed mathematical claims. A passing residue need not lift.
"""
from collections import Counter
from itertools import product
from math import comb
from pathlib import Path
import datetime
import hashlib
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
PREFIX = 'coordinator-J15-triple-leading-v1'
SOURCE = HERE.parent / 'reviews/newton-review-1-extension-result.json'
P = 19
BETA = [0, 0] + [comb(20, j) // P for j in range(2, 19)]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def valuation(n):
    assert n
    v = 0
    while n % P == 0:
        v += 1
        n //= P
    return v


def child():
    masks = json.loads(SOURCE.read_text())['retained_masks']['15']
    rows, branches = [], []
    tests = 0
    for mask in masks:
        a = [1, -1] + [0] * 17
        active = []
        for j in range(2, 19):
            if mask & (1 << (j - 2)):
                a[j] = -sum(comb(j, k) * a[k] for k in range(j))
            elif a[j - 1] % P:
                active.append(j)
        q0 = -1 + sum(BETA[j] * a[j] for j in range(2, 19))
        assert q0 and q0 % P == 0
        assert a[15] % P and all(a[j] % P == 0 for j in (16, 17, 18))
        h3, h4 = bool(mask & (1 << 15)), bool(mask & (1 << 14))
        bound = valuation(q0)
        before = len(branches)
        mask_tests = 0
        if h3 or h4:
            for labels in product((0, 1, 2), repeat=len(active)):
                by_position = dict(zip(active, labels))
                A, B = [0] * 19, [0] * 19
                for j in range(2, 19):
                    if mask & (1 << (j - 2)):
                        A[j] = -sum(comb(j, k) * A[k] for k in range(j)) % P
                        B[j] = -sum(comb(j, k) * B[k] for k in range(j)) % P
                    elif by_position.get(j) == 1:
                        A[j] = -j * a[j - 1] % P
                    elif by_position.get(j) == 2:
                        B[j] = -j * a[j - 1] % P
                for nu in range(1, bound + 1):
                    q = P ** nu
                    if any(a[j] % q for j in (16, 17, 18)):
                        continue
                    c5 = BETA[15] * a[15] % P
                    eqs = [
                        [q0 // q, sum(BETA[j] * A[j] for j in range(2, 19)),
                         sum(BETA[j] * B[j] for j in range(2, 19))],
                        [a[18] // q, A[18], B[18]],
                        [a[17] // q, A[17], B[17]],
                        [BETA[16] * (a[16] // q), BETA[16] * A[16] + c5,
                         BETA[16] * B[16] + c5],
                    ]
                    mask_tests += 1
                    for U, V in product(range(P), repeat=2):
                        if U == V == 0 or any((c + x * U + y * V) % P for c, x, y in eqs):
                            continue
                        if not (h3 and h4):
                            if not U or not V:
                                continue
                            if h3:  # H4 noncenter: 0, u or v.
                                if all(t % P for t in (U + V, 4 * U - V, 4 * V - U)):
                                    continue
                            else:   # H3 noncenter: u or v; never 0.
                                if (2 * U - V) % P and (2 * V - U) % P:
                                    continue
                        branches.append({'mask': mask, 'active_positions': active,
                                         'active_labels': list(labels), 'nu': nu,
                                         'residue_U_V': [U, V], 'equations': eqs})
        tests += mask_tests
        row = {'mask': mask, 'H3_center': h3, 'H4_center': h4,
               'active_positions': active, 'q0': q0,
               'minimum_valuation_bound': bound, 'projected_tests': mask_tests,
               'passing_branches': len(branches) - before,
               'excluded_in_multiplicity_three': len(branches) == before}
        rows.append(row)
        print(json.dumps(row), flush=True)
    result = {'status': 'candidate projection, unverified; only the J15 triple-zero subcase',
              'prime': P, 'J': 15, 'zero_multiplicity': 3, 'initial_masks': len(masks),
              'projected_tests': tests, 'branch_count': len(branches),
              'excluded_subcase_masks': [r['mask'] for r in rows if r['excluded_in_multiplicity_three']],
              'retained_subcase_masks': [r['mask'] for r in rows if not r['excluded_in_multiplicity_three']],
              'nu_histogram': dict(Counter(str(b['nu']) for b in branches)),
              'rows': rows, 'branches': branches,
              'source_path': str(SOURCE.relative_to(HERE.parents[2])),
              'source_sha256': sha(SOURCE),
              'method_reuse': 'coordinator-J16-coupled-leading-v1.py',
              'method_source_sha256': sha(HERE / 'coordinator-J16-coupled-leading-v1.py')}
    (HERE / (PREFIX + '-result.json')).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ('rows', 'branches')}), flush=True)


def main():
    if '--child' in sys.argv:
        child()
        return
    out, err, job = [HERE / (PREFIX + s) for s in ('-output.txt', '-stderr.txt', '-job.json')]
    cmd = [sys.executable, '-u', str(Path(__file__).resolve()), '--child']
    rec = {'started_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
           'command': cmd, 'timeout_seconds': 30, 'status': 'launching',
           'source_sha256': sha(Path(__file__)), 'input_sha256': sha(SOURCE)}
    start = time.monotonic()
    with out.open('w') as f, err.open('w') as e:
        proc = subprocess.Popen(cmd, stdout=f, stderr=e)
        rec.update(pid=proc.pid, status='running')
        job.write_text(json.dumps(rec, indent=2) + '\n')
        print(json.dumps(rec), flush=True)
        try:
            proc.wait(timeout=30)
            rec['status'] = 'completed' if proc.returncode == 0 else 'failed'
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
            rec['status'] = 'incomplete_timeout'
        rec.update(exit_code=proc.returncode, elapsed_seconds=time.monotonic() - start,
                   reaped=True, completed_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        for suffix in ('-output.txt', '-stderr.txt', '-result.json'):
            path = HERE / (PREFIX + suffix)
            if path.exists():
                rec[suffix] = sha(path)
        job.write_text(json.dumps(rec, indent=2) + '\n')
        print(json.dumps(rec), flush=True)
    if rec['status'] != 'completed':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
