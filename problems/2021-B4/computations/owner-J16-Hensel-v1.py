#!/usr/bin/env python3
"""Candidate, unverified J16 structured 19-adic lifts through precision four.

New constructor implementation. No imported mathematical helpers. The
leading branch list and previous digit stream are unreviewed inputs. An
independent whole-argument audit is still needed twice before promotion.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path
import datetime
import gzip
import hashlib
import json
import math
import os
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
P = 19
TARGET = 4
CAP = 1000000
LEADING = HERE / 'coordinator-J16-leading-branch-index-v1-result.json'
OLD_RESULT = HERE / 'coordinator-J16-second-digit-v1-result.json'
OLD_SOURCE = HERE / 'coordinator-J16-second-digit-v1.py'
T1_REGISTER = HERE.parent / 'notes/coordinator-three-rational-witnesses-reviewed-v1.1.md'
C = [[math.comb(j, k) for k in range(j + 1)] for j in range(21)]
BETA = {j: math.comb(20, j) // P for j in range(2, 19)}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def emit(row):
    print(json.dumps(row, sort_keys=True), flush=True)


def line(row):
    return (json.dumps(row, separators=(',', ':')) + '\n').encode()


class Stream:
    """Deterministic gzip chunks, with both compressed and plain hashes."""
    def __init__(self, stem):
        self.stem = stem
        self.chunks = []
        self.rows = 0
        self.digest = hashlib.sha256()
        self.raw = self.gz = None
        self.chunk_rows = 0

    def write(self, row):
        if self.gz is None:
            self.path = HERE / (self.stem + f'-{len(self.chunks) + 1:03}.jsonl.gz')
            self.raw = self.path.open('wb')
            self.gz = gzip.GzipFile(filename='', mode='wb', fileobj=self.raw, mtime=0)
        b = line(row)
        self.digest.update(b)
        self.gz.write(b)
        self.rows += 1
        self.chunk_rows += 1
        if self.chunk_rows == 60000:
            self.close_chunk()

    def flush(self):
        if self.gz:
            self.gz.flush()
            self.raw.flush()

    def close_chunk(self):
        if self.gz:
            self.gz.close()
            self.raw.close()
            self.chunks.append({'path': str(self.path.relative_to(ROOT)),
                                'rows': self.chunk_rows,
                                'bytes': self.path.stat().st_size,
                                'sha256': sha(self.path)})
            self.raw = self.gz = None
            self.chunk_rows = 0

    def finish(self):
        self.close_chunk()
        return {'rows': self.rows, 'plain_sha256': self.digest.hexdigest(),
                'chunks': self.chunks}


def read_stream(chunks):
    for chunk in chunks:
        path = ROOT / chunk['path']
        assert sha(path) == chunk['sha256']
        with gzip.open(path, 'rt') as f:
            n = 0
            for s in f:
                n += 1
                yield json.loads(s)
            assert n == chunk['rows']


def initial_nodes(source):
    for b in source['leading_branches']:
        mask = b['center_mask']
        fixed = dict(zip(b['active_positions'], b['active_labels']))
        inactive = b['inactive_positions']
        assert 3 ** len(inactive) == b['full_label_expansions']
        noncenter = [j for j in range(2, 19) if not mask & (1 << (j - 2))]
        assert sorted(fixed.keys() | set(inactive)) == noncenter
        for extra in product(range(3), repeat=len(inactive)):
            labels = fixed | dict(zip(inactive, extra))
            um = sum(1 << (j - 2) for j in noncenter if labels[j] == 1)
            vm = sum(1 << (j - 2) for j in noncenter if labels[j] == 2)
            yield [mask, um, vm, b['nu'], b['U'], b['V']]


def coefficient_data(key, k):
    """a_j modulo q*19^(k+1); every omitted term is zero at this modulus."""
    mask, um, vm, nu, u, v = key
    assert nu in (1, 2) and (u % P or v % P)
    q = P ** nu
    modulus = P ** (nu + k + 1)
    a = [1, modulus - 1] + [0] * 17
    # At a noncenter, w is q*U or q*V. Terms with nu*e >= nu+k+1
    # vanish, without making any assumption about the previous a_j.
    max_e = (nu + k) // nu
    wp = [[1], [1], [1]]
    for which, w in enumerate((0, q * u, q * v)):
        for e in range(1, max_e + 1):
            wp[which].append(wp[which][-1] * w % modulus)
    for j in range(2, 19):
        bit = 1 << (j - 2)
        if mask & bit:
            a[j] = -sum(C[j][h] * a[h] for h in range(j)) % modulus
        else:
            which = 1 if um & bit else 2 if vm & bit else 0
            a[j] = -sum(C[j][j-e] * a[j-e] * wp[which][e]
                        for e in range(1, min(j, max_e) + 1)) % modulus
    return a, modulus


def residual(key, k):
    """E evaluated modulo 19^(k+1), with exact quotient digits."""
    mask, um, vm, nu, u, v = key
    q = P ** nu
    emod = P ** (k + 1)
    a, amod = coefficient_data(key, k)
    ptilde = (-1 + sum(BETA[j] * a[j] for j in range(2, 19))) % amod
    assert ptilde % q == a[17] % q == a[18] % q == 0
    e0 = ptilde // q
    e1 = a[18] // q
    e2 = BETA[17] * (a[17] // q)
    s, t = (u + v) % emod, u * v % emod
    hprev, h = 0, 1
    invbeta18 = pow(BETA[18], -1, emod)
    # h_e is the X coefficient of X^e modulo X^2-sX+t at normalized
    # variables U,V. k_e=-t*h_(e-1). Units c19=-20,c20=1 are included.
    for e in range(2, 19):
        hprev, h = h, (s * h - t * hprev) % emod
        ke = -t * hprev % emod
        if e <= 16:
            b = BETA[18-e] * a[18-e]
            e1 += invbeta18 * b * pow(q, e-1, emod) * ke
            e2 += b * pow(q, e-2, emod) * h
        else:
            c = -20 if e == 17 else 1
            # q^r/P is an exact integer here, not a modular division.
            e1 += invbeta18 * c * (q ** (e-1) // P) * ke
            e2 += c * (q ** (e-2) // P) * h
    return [e0 % emod, e1 % emod, e2 % emod], a, amod


def jacobian(key):
    """Constant Jacobian mod 19 from complete label assignment."""
    mask, um, vm = key[:3]
    a = [1, -1] + [0] * 17
    au = [0] * 19
    av = [0] * 19
    for j in range(2, 19):
        bit = 1 << (j - 2)
        if mask & bit:
            a[j] = -sum(C[j][h] * a[h] for h in range(j)) % P
            au[j] = -sum(C[j][h] * au[h] for h in range(j)) % P
            av[j] = -sum(C[j][h] * av[h] for h in range(j)) % P
        else:
            if um & bit:
                au[j] = -j * a[j-1] % P
            if vm & bit:
                av[j] = -j * a[j-1] % P
    c4 = BETA[16] * a[16] % P
    return [(sum(BETA[j] * au[j] for j in range(2, 19)) % P,
             sum(BETA[j] * av[j] for j in range(2, 19)) % P),
            (au[18], av[18]),
            ((BETA[17] * au[17] + c4) % P,
             (BETA[17] * av[17] + c4) % P)]


def affine_digits(matrix, constants):
    """Solve all 19-adic next digits by 3x2 Gaussian elimination."""
    a = [[x % P, y % P, -c % P]
         for (x, y), c in zip(matrix, constants)]
    pivots = []
    for col in range(2):
        row = next((r for r in range(len(pivots), 3) if a[r][col]), None)
        if row is None:
            continue
        j = len(pivots)
        a[j], a[row] = a[row], a[j]
        inv = pow(a[j][col], -1, P)
        a[j] = [x * inv % P for x in a[j]]
        for r in range(3):
            if r != j:
                scale = a[r][col]
                a[r] = [(x - scale*y) % P for x, y in zip(a[r], a[j])]
        pivots.append(col)
    rank = len(pivots)
    if any(x == y == 0 and z for x, y, z in a):
        return rank, [], a
    free = [col for col in range(2) if col not in pivots]
    answer = []
    for vals in product(range(P), repeat=len(free)):
        sol = [0, 0]
        for col, val in zip(free, vals):
            sol[col] = val
        for r, col in enumerate(pivots):
            sol[col] = (a[r][2] - sum(a[r][j] * sol[j] for j in free)) % P
        assert all((x*sol[0] + y*sol[1] + c) % P == 0
                   for (x, y), c in zip(matrix, constants))
        answer.append(sol)
    return rank, answer, a


def exact_reference(key):
    """Untruncated integer construction and monic polynomial division."""
    mask, um, vm, nu, u, v = key
    q = P ** nu
    actual_u, actual_v = q * u, q * v
    a = [1, -1] + [0] * 17
    for j in range(2, 19):
        bit = 1 << (j - 2)
        w = 1 if mask & bit else actual_u if um & bit else actual_v if vm & bit else 0
        a[j] = -sum(C[j][h] * a[h] * w ** (j-h) for h in range(j))
    # F=f/X^2 has ascending coefficients, including the two unit terms.
    f = [math.comb(20, 18-e) * a[18-e] for e in range(17)] + [-20, 1]
    rr = f[:]
    s, t = actual_u + actual_v, actual_u * actual_v
    for e in range(18, 1, -1):
        c = rr[e]
        rr[e] = 0
        rr[e-1] += c * s
        rr[e-2] -= c * t
    ptilde = Fraction(sum(f), P)
    assert ptilde.denominator == 1
    return [ptilde / q, Fraction(rr[0], P*q*BETA[18]),
            Fraction(rr[1], P*q)], a, f, rr[:2]


def fraction_mod(x, mod):
    return x.numerator * pow(x.denominator, -1, mod) % mod


def self_test(source, prefix):
    cases = []
    # Include each nu, all three low-center possibilities, zero residues,
    # and both choices of missing label; then deterministic further cases.
    selected = {}
    for b in source['leading_branches']:
        mask = b['center_mask']
        fixed = dict(zip(b['active_positions'], b['active_labels']))
        for fill in (0, 1, 2):
            labels = fixed | dict.fromkeys(b['inactive_positions'], fill)
            um = sum(1 << (j-2) for j, v in labels.items() if v == 1)
            vm = sum(1 << (j-2) for j, v in labels.items() if v == 2)
            key = [mask, um, vm, b['nu'], b['U'], b['V']]
            sig = (b['nu'], bool(mask & 32768), bool(mask & 65536),
                   b['U'] == 0, b['V'] == 0, fill)
            selected.setdefault(sig, key)
    for key in selected.values():
        exact, a, f, r = exact_reference(key)
        assert all(x.denominator % P for x in exact)
        matrix = jacobian(key)
        modular = []
        for k in (1, 2, 3):
            e, aa, amod = residual(key, k)
            assert aa == [x % amod for x in a]
            assert e == [fraction_mod(x, P ** (k+1)) for x in exact]
            # Verify derivative reduction by a full modulus-p^(k+1)
            # finite difference, with a change of p^k in each variable.
            base = P ** k
            for col in range(2):
                shifted = key[:]
                shifted[4+col] += base
                es, _, _ = residual(shifted, k)
                for row in range(3):
                    diff = (es[row] - e[row]) % (base * P)
                    assert diff % base == 0
                    assert diff // base == matrix[row][col]
            modular.append({'k': k, 'E_mod': e, 'a_modulus': amod})
        constants = [(x % (P*P)) // P for x in modular[0]['E_mod']]
        assert all(x % P == 0 for x in modular[0]['E_mod'])
        rank, sols, rref = affine_digits(matrix, constants)
        brute = [[x, y] for x in range(P) for y in range(P)
                 if all((a*x+b*y+c) % P == 0
                        for (a, b), c in zip(matrix, constants))]
        assert sorted(sols) == brute
        cases.append({'key': key, 'integer_a': a, 'integer_F': f,
                      'integer_R0_R1': r,
                      'exact_E': [[x.numerator, x.denominator] for x in exact],
                      'modular': modular, 'jacobian': matrix,
                      'rank': rank, 'digit_solutions': sols, 'rref': rref})
    path = HERE / (prefix + '-self-test.json')
    path.write_text(json.dumps({'status': 'constructor cross-checks, not independent review',
                               'cases': cases, 'case_count': len(cases)}, indent=2) + '\n')
    emit({'self_test_cases': len(cases), 'status': 'passed'})
    return {'path': str(path.relative_to(ROOT)), 'sha256': sha(path), 'cases': len(cases)}


def child(benchmark):
    prefix = 'owner-J16-Hensel-v1' + ('-benchmark' if benchmark else '')
    source = json.loads(LEADING.read_text())
    old = json.loads(OLD_RESULT.read_text())
    assert len(source['leading_branches']) == 768
    assert source['expanded_label_residue_branches'] == old['visited'] == 840396
    assert len(set(source['retained_masks'])) == 70
    start = time.monotonic()
    info = {'status': 'running construction; unverified', 'pid': os.getpid(),
            'target_precision': TARGET, 'node_cap_per_level': CAP,
            'initial_expected_nodes': 840396, 'benchmark': benchmark,
            'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
            'effective_settings': 'not available from launch readback',
            'inputs_sha256': {p.name: sha(p) for p in
                             (LEADING, OLD_RESULT, OLD_SOURCE, T1_REGISTER)},
            'self_test': self_test(source, prefix), 'levels': []}
    checkpoint_path = HERE / (prefix + '-checkpoint.json')
    result_path = HERE / (prefix + '-result.json')
    nodes = initial_nodes(source)
    node_count = 840396
    matrices = {}
    old_iter = read_stream(old['chunks'])
    old_match = Counter()
    final_masks = None
    for k in range(1, TARGET):
        assert node_count <= CAP
        certs = Stream(prefix + f'-level-{k}-certificates')
        next_nodes = Stream(prefix + f'-precision-{k+1}-nodes')
        tally = Counter()
        masks = {m: [0, 0, 0] for m in source['retained_masks']}
        seen = generated = 0
        stopped = None
        level_start = time.monotonic()
        for key in nodes:
            mask, um, vm, nu, u, v = key
            seen += 1
            masks[mask][0] += 1
            family = (mask, um, vm)
            if family not in matrices:
                matrices[family] = jacobian(key)
            matrix = matrices[family]
            e, a, amod = residual(key, k)
            base = P ** k
            assert all(x % base == 0 for x in e), (key, k, e)
            constants = [x // base for x in e]
            rank, digits, rref = affine_digits(matrix, constants)
            tally[f'rank{rank}_consistent{bool(digits)}'] += 1
            prune = (um == 0 or vm == 0)
            if k == 1:
                previous = next(old_iter)
                assert previous[:6] == key
                assert previous[6:9] == constants
                assert previous[9:] == [rank, int(bool(digits))]
                old_match['rows_matched'] += 1
                old_match[f'rank{rank}_consistent{bool(digits)}'] += 1
            if prune:
                tally['pruned_by_accepted_T1_missing_label'] += 1
                digits = []
            if digits:
                masks[mask][1] += 1
            row = [key, amod, a, e, matrix, rank, rref,
                   'accepted_T1_missing_label' if prune else None, digits]
            certs.write(row)
            if generated + len(digits) > CAP:
                stopped = 'next-level node cap would be exceeded; no cap increase'
                tally['would_generate_at_stop'] = generated + len(digits)
                break
            for du, dv in digits:
                lifted = key[:4] + [u + base*du, v + base*dv]
                next_nodes.write(lifted)
                generated += 1
                masks[mask][2] += 1
            if seen % 8192 == 0:
                certs.flush()
                next_nodes.flush()
                checkpoint = {'precision': k, 'visited': seen,
                              'generated_next_precision': generated,
                              'elapsed_seconds': time.monotonic() - start,
                              'level_seconds': time.monotonic() - level_start,
                              'tally': dict(tally), 'pid': os.getpid()}
                checkpoint_path.write_text(json.dumps(checkpoint, indent=2) + '\n')
                emit(checkpoint)
            if benchmark and seen >= 8192:
                stopped = 'fixed 8192-initial-node benchmark; incomplete cover'
                break
        level = {'input_precision': k, 'input_expected_nodes': node_count,
                 'input_visited': seen, 'generated_nodes': generated,
                 'complete_input_traversal': seen == node_count and stopped is None,
                 'stopped': stopped, 'tally': dict(tally),
                 'per_mask_visited_passing_generated': masks,
                 'certificates': certs.finish(), 'nodes': next_nodes.finish(),
                 'elapsed_seconds': time.monotonic() - level_start}
        info['levels'].append(level)
        info['old_digit_stream_comparison'] = dict(old_match)
        if stopped:
            info['status'] = 'incomplete bounded construction; no new full-cover exclusions'
            break
        assert seen == node_count
        if k == 1:
            assert old_match['rows_matched'] == 840396
            assert next(old_iter, None) is None
        final_masks = sorted(m for m, (seen_mask, passing, gen) in masks.items() if gen)
        info['last_complete_precision'] = k + 1
        info['candidate_masks_at_last_complete_precision'] = final_masks
        info['status'] = 'complete necessary construction through recorded precision; unverified'
        info['elapsed_seconds'] = time.monotonic() - start
        result_path.write_text(json.dumps(info, indent=2) + '\n')
        emit({'level_complete': k, 'nodes_at_next_precision': generated,
              'candidate_masks': len(final_masks), 'tally': dict(tally),
              'elapsed_seconds': info['elapsed_seconds']})
        if not generated:
            break
        nodes = read_stream(level['nodes']['chunks'])
        node_count = generated
    info['elapsed_seconds'] = time.monotonic() - start
    result_path.write_text(json.dumps(info, indent=2) + '\n')
    emit({k: v for k, v in info.items()
          if k not in ('levels', 'inputs_sha256', 'self_test')})


def main():
    benchmark = '--benchmark' in sys.argv
    if '--child' in sys.argv:
        child(benchmark)
        return
    prefix = 'owner-J16-Hensel-v1' + ('-benchmark' if benchmark else '')
    timeout = 60 if benchmark else 300
    out, err, job = [HERE / (prefix+s) for s in ('-output.txt', '-stderr.txt', '-job.json')]
    cmd = [sys.executable, '-u', str(Path(__file__).resolve()), '--child']
    if benchmark:
        cmd.append('--benchmark')
    record = {'started_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'command': cmd, 'timeout_seconds': timeout,
              'node_cap_per_level': CAP, 'target_precision': TARGET,
              'benchmark': benchmark, 'status': 'launching',
              'source_sha256': sha(Path(__file__))}
    start = time.monotonic()
    with out.open('w') as f, err.open('w') as e:
        proc = subprocess.Popen(cmd, stdout=f, stderr=e)
        record.update(pid=proc.pid, status='running')
        job.write_text(json.dumps(record, indent=2) + '\n')
        emit(record)
        try:
            proc.wait(timeout=timeout)
            record['status'] = 'completed' if proc.returncode == 0 else 'failed'
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
            record['status'] = 'timeout; identified child reaped; incomplete construction'
        record.update(return_code=proc.returncode, elapsed_seconds=time.monotonic()-start)
    record['output_hashes'] = {p.name: sha(p) for p in (out, err,
                              HERE/(prefix+'-result.json'),
                              HERE/(prefix+'-checkpoint.json'),
                              HERE/(prefix+'-self-test.json')) if p.is_file()}
    job.write_text(json.dumps(record, indent=2) + '\n')
    emit(record)


if __name__ == '__main__':
    main()
