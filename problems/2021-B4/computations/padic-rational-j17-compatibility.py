#!/usr/bin/env python3
"""Exact univariate checks for the 73 candidate degree20/J17 center patterns.

For each pattern choose 0 or u for every noncenter witness. Coefficients are
constructed over Z[u], with u an indeterminate. A nonzero resultant modulo
a prime, certified by coprime reductions with preserved degrees, proves
coprimality over Q. This is a finite algebraic family check, not a height box.
The reduction to these families remains a candidate proof pending review.
"""
import argparse
import collections
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
PRIMES=(101,103,107,109,127)


def emit(**r):
    print(json.dumps(r,sort_keys=True),flush=True)


def trim(poly):
    while len(poly)>1 and poly[-1]==0:
        poly.pop()
    return poly


def add_scaled(target,source,scale,shift=0):
    needed=len(source)+shift
    if len(target)<needed:
        target.extend([0]*(needed-len(target)))
    for k,value in enumerate(source):
        target[k+shift]+=scale*value


def mod_gcd(left,right,prime):
    left=trim([c%prime for c in left])
    right=trim([c%prime for c in right])
    while right!=[0]:
        inverse=pow(right[-1],-1,prime)
        while left!=[0] and len(left)>=len(right):
            shift=len(left)-len(right)
            ratio=left[-1]*inverse%prime
            for i,value in enumerate(right):
                left[i+shift]=(left[i+shift]-ratio*value)%prime
            trim(left)
        left,right=right,left
    return len(left)-1 if left!=[0] else -1


def worker():
    source=HERE/'padic-rational-newton-patterns.jsonl'
    source_bytes=source.read_bytes()
    data=next(r for r in map(json.loads,source_bytes.splitlines())
              if r['event']=='complete')
    masks=data['J17_remaining_center_masks']
    assert len(masks)==73 and len(set(masks))==73
    assert all(m & (1<<15) and m & (1<<16) for m in masks)
    expected=sum(2**(17-m.bit_count()) for m in masks)
    assert expected==29928
    output=HERE/'padic-rational-j17-certificates.jsonl'
    a=[[0] for _ in range(19)]
    a[0],a[1]=[1],[-1]
    bins=[[math.comb(j,k) for k in range(j+1)] for j in range(21)]
    visited=0
    successes=collections.Counter()
    unresolved=[]
    digest=hashlib.sha256()
    started=time.monotonic()
    emit(event='parameters',pid=os.getpid(),degree=20,last_unit_index=17,
         center_patterns=len(masks),refinements=expected,primes=PRIMES,
         source_sha256=hashlib.sha256(source_bytes).hexdigest(),
         certificate_path=str(output),
         mask='bit j-2 marks center1; u_mask marks the other nonzero witness',
         normalization='D_j=sum binom(j,k)*a_k*x^(j-k), a0=1,a1=-1',
         scope='candidate reduction plus exact Z[u] family compatibility')

    with output.open('w') as cert:
        def finish(mask,u_mask):
            nonlocal visited
            at_one=[-19]
            at_u=[0]*21
            at_u[20],at_u[19]=1,-20
            for j in range(2,19):
                add_scaled(at_one,a[j],bins[20][j])
                add_scaled(at_u,a[j],bins[20][j],20-j)
            trim(at_one)
            trim(at_u)
            visited+=1
            raw=json.dumps([mask,u_mask,at_one,at_u],separators=(',',':'))
            digest.update((raw+'\n').encode())
            record={'center_mask':mask,'u_mask':u_mask,
                    'degrees':[len(at_one)-1,len(at_u)-1],
                    'polynomials_sha256':hashlib.sha256(raw.encode()).hexdigest()}
            if at_one!=[0] and len(at_one)==1:
                record.update(status='constant_nonzero',constant=at_one[0])
                successes['constant_nonzero']+=1
            else:
                for prime in PRIMES:
                    # Both integer degrees are retained modulo this prime.
                    if at_one[-1]%prime==0 or at_u[-1]%prime==0:
                        continue
                    degree=mod_gcd(at_one,at_u,prime)
                    if degree==0:
                        record.update(status='coprime_mod_prime',prime=prime,
                                      gcd_degree=0,
                                      leading_residues=[at_one[-1]%prime,
                                                        at_u[-1]%prime])
                        successes[str(prime)]+=1
                        break
                else:
                    record.update(status='unresolved',f1=at_one,fu=at_u)
                    unresolved.append(record)
            cert.write(json.dumps(record,sort_keys=True)+'\n')
            if visited%1024==0:
                cert.flush()
                emit(event='checkpoint',visited=visited,unresolved=len(unresolved),
                     elapsed_seconds=round(time.monotonic()-started,3))

        def descend(j,mask,u_mask):
            if j==19:
                finish(mask,u_mask)
                return
            if mask & (1<<(j-2)):
                value=[0]
                for k in range(j):
                    add_scaled(value,a[k],-bins[j][k])
                a[j]=trim(value)
                descend(j+1,mask,u_mask)
            else:
                a[j]=[0]
                descend(j+1,mask,u_mask)
                value=[0]
                for k in range(j):
                    add_scaled(value,a[k],-bins[j][k],j-k)
                a[j]=trim(value)
                descend(j+1,mask,u_mask | (1<<(j-2)))
            a[j]=[0]

        for mask in masks:
            descend(2,mask,0)

    assert visited==expected
    emit(event='complete',visited=visited,resolved=sum(successes.values()),
         resolution_histogram=dict(successes),unresolved=len(unresolved),
         polynomial_stream_sha256=digest.hexdigest(),
         certificate_file_sha256=hashlib.sha256(output.read_bytes()).hexdigest(),
         elapsed_seconds=round(time.monotonic()-started,6),
         scope='finite complete selected family; no classification of all degrees')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--worker',action='store_true')
    args=parser.parse_args()
    if args.worker:
        worker()
        return
    command=[sys.executable,os.path.abspath(__file__),'--worker']
    child=subprocess.Popen(command)
    emit(event='child_started',pid=child.pid,command=command,timeout_seconds=90)
    try:
        code=child.wait(timeout=90)
    except subprocess.TimeoutExpired:
        child.kill()
        child.wait()
        emit(event='timeout',pid=child.pid)
        raise SystemExit(124)
    emit(event='child_finished',pid=child.pid,exit_code=code)
    raise SystemExit(code)


if __name__=='__main__':
    main()
