#!/usr/bin/env python3
"""Author spot-check through direct Hasse coefficients and exact QQ gcds.

This is not an independent agent review. It covers a selected 12 certificates,
including every case requiring prime109, and does not replace full review.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent


def emit(**r):
    print(json.dumps(r,sort_keys=True),flush=True)


def worker():
    import sympy as sp
    rows=[json.loads(line) for line in
          (HERE/'padic-rational-j17-certificates.jsonl').read_text().splitlines()]
    groups={}
    for index,row in enumerate(rows):
        key=str(row.get('prime',row['status']))
        groups.setdefault(key,[]).append(index)
    selected=set(groups['109'])
    for key,indices in groups.items():
        selected.update([indices[0],indices[-1]])
    emit(event='parameters',pid=os.getpid(),python=sys.version.split()[0],
         sympy=sp.__version__,selected_records=sorted(selected),
         method='direct Hasse recurrence for c_k, then exact QQ gcd')
    u=sp.Symbol('u')
    for index in sorted(selected):
        row=rows[index]
        mask,umask=row['center_mask'],row['u_mask']
        c={20:sp.Integer(1),19:sp.Integer(-20),1:sp.Integer(0),0:sp.Integer(0)}
        for order in range(18,1,-1):
            j=20-order
            witness=sp.Integer(1) if mask&(1<<(j-2)) else (
                u if umask&(1<<(j-2)) else sp.Integer(0))
            c[order]=-sp.expand(sum(math.comb(k,order)*c[k]*witness**(k-order)
                                    for k in range(order+1,21)))
        f1=sp.Poly(sum(c.values()),u,domain=sp.QQ)
        fu=sp.Poly(sp.expand(sum(value*u**k for k,value in c.items())),u,domain=sp.QQ)
        left=[int(f1.nth(k)) for k in range(f1.degree()+1)]
        right=[int(fu.nth(k)) for k in range(fu.degree()+1)]
        raw=json.dumps([mask,umask,left,right],separators=(',',':'))
        assert hashlib.sha256(raw.encode()).hexdigest()==row['polynomials_sha256']
        gcd=sp.gcd(f1,fu)
        assert gcd.degree()==0
        emit(event='certificate_checked',index=index,center_mask=mask,u_mask=umask,
             polynomial_hash_matches=True,exact_QQ_gcd=str(gcd.as_expr()))
    emit(event='complete',checked=len(selected),all_passed=True,
         scope='author spot-check only, not independent review')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--worker',action='store_true')
    args=parser.parse_args()
    if args.worker:
        worker()
        return
    command=[sys.executable,os.path.abspath(__file__),'--worker']
    child=subprocess.Popen(command)
    emit(event='child_started',pid=child.pid,command=command,timeout_seconds=30)
    try:
        code=child.wait(timeout=30)
    except subprocess.TimeoutExpired:
        child.kill()
        child.wait()
        emit(event='timeout',pid=child.pid)
        raise SystemExit(124)
    emit(event='child_finished',pid=child.pid,exit_code=code)
    raise SystemExit(code)


if __name__=='__main__':
    main()
