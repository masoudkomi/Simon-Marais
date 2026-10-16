#!/usr/bin/env python3
"""Exact constructor post-check of all 90 precision-four nodes; unreviewed."""
from collections import Counter
from fractions import Fraction
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
PREFIX = 'owner-J16-Hensel-v1-postcheck'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def child():
    start = time.monotonic()
    source = HERE / 'owner-J16-Hensel-v1-result.json'
    data = json.loads(source.read_text())
    assert data['last_complete_precision'] == 4
    last = data['levels'][-1]['nodes']
    assert last['rows'] == 90
    keys = []
    for chunk in last['chunks']:
        path = ROOT / chunk['path']
        assert sha(path) == chunk['sha256']
        with gzip.open(path, 'rt') as f:
            keys += [json.loads(row) for row in f]
    assert len(keys) == len(set(map(tuple, keys))) == 90
    frozen = []
    mask_counts = Counter()
    delta_valuations = Counter()
    for key in keys:
        mask, um, vm, nu, U, V = key
        assert um and vm and not mask & (um | vm) and not um & vm
        q = 19 ** nu
        u, v = q * U, q * V
        a = [1, -1]
        # Horner evaluation of each derivative condition, untruncated.
        for j in range(2, 19):
            bit = 1 << (j-2)
            w = 1 if mask & bit else u if um & bit else v if vm & bit else 0
            value = 0
            for k in range(j):
                value = (value + math.comb(j, k) * a[k]) * w
            a.append(-value)
        f = [math.comb(20, 18-e) * a[18-e] for e in range(17)] + [-20, 1]
        # Horner evaluation in Z[X]/(X^2-(u+v)X+uv), with two scalar states.
        r1 = r0 = 0
        for c in reversed(f):
            r1, r0 = r0 + (u+v)*r1, c - u*v*r1
        E = [Fraction(sum(f), 19*q), Fraction(r0, 19*q*10), Fraction(r1, 19*q)]
        assert all(x.denominator % 19 and x.numerator % (19**4) == 0 for x in E)
        aa = [1, -1] + [0]*17
        au = [0]*19
        av = [0]*19
        for j in range(2, 19):
            bit = 1 << (j-2)
            if mask & bit:
                aa[j] = -sum(math.comb(j, k)*aa[k] for k in range(j)) % 19
                au[j] = -sum(math.comb(j, k)*au[k] for k in range(j)) % 19
                av[j] = -sum(math.comb(j, k)*av[k] for k in range(j)) % 19
            elif um & bit:
                au[j] = -j*aa[j-1] % 19
            elif vm & bit:
                av[j] = -j*aa[j-1] % 19
        beta = {j: math.comb(20,j)//19 for j in range(2,19)}
        c4 = beta[16]*aa[16] % 19
        matrix = [[sum(beta[j]*au[j] for j in range(2,19)) % 19,
                   sum(beta[j]*av[j] for j in range(2,19)) % 19],
                  [au[18], av[18]],
                  [(beta[17]*au[17]+c4) % 19, (beta[17]*av[17]+c4) % 19]]
        minors = [(i,j,(matrix[i][0]*matrix[j][1]-matrix[i][1]*matrix[j][0])%19)
                  for i in range(3) for j in range(i+1,3)]
        assert any(d for i,j,d in minors)
        delta = U-V
        if delta:
            val = 0
            while delta % 19 == 0:
                val += 1
                delta //= 19
            delta_valuations[val] += 1
        else:
            delta_valuations['finite_representatives_equal'] += 1
        mask_counts[mask] += 1
        frozen.append({'key': key, 'integer_a': a, 'integer_F': f,
                       'integer_R0_R1': [r0,r1],
                       'exact_E': [[x.numerator,x.denominator] for x in E],
                       'jacobian_mod19': matrix, 'two_by_two_minors': minors,
                       'rank': 2})
    # Every swapped root-label/state is also present in the candidate cover.
    keyset = set(map(tuple,keys))
    assert all((m,vm,um,nu,V,U) in keyset for m,um,vm,nu,U,V in keys)
    result = {'status':'constructor exact post-check; unverified',
              'source_sha256':sha(source), 'pid':os.getpid(),
              'precision':4, 'nodes':90, 'all_rank_two':True,
              'mask_counts':dict(mask_counts),
              'valuation_U_minus_V':dict(delta_valuations),
              'swap_closure':True, 'states':frozen,
              'elapsed_seconds':time.monotonic()-start}
    target = HERE / (PREFIX+'-result.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='states'}),flush=True)


def main():
    if '--child' in sys.argv:
        child()
        return
    out,err,job=[HERE/(PREFIX+s) for s in ('-output.txt','-stderr.txt','-job.json')]
    cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--child']
    record={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'command':cmd,'timeout_seconds':30,'status':'launching',
            'source_sha256':sha(Path(__file__))}
    start=time.monotonic()
    with out.open('w') as f,err.open('w') as e:
        proc=subprocess.Popen(cmd,stdout=f,stderr=e)
        record.update(pid=proc.pid,status='running')
        job.write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps(record),flush=True)
        try:
            proc.wait(timeout=30)
            record['status']='completed' if proc.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:
            proc.kill();proc.wait()
            record['status']='timeout; identified child reaped; incomplete'
        record.update(return_code=proc.returncode,elapsed_seconds=time.monotonic()-start)
    record['output_hashes']={p.name:sha(p) for p in (out,err,HERE/(PREFIX+'-result.json')) if p.is_file()}
    job.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record),flush=True)


if __name__=='__main__':
    main()
