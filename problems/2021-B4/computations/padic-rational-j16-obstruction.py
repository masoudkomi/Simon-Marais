#!/usr/bin/env python3
"""Finite arithmetic evidence for a candidate degree20/J16 Newton obstruction."""
import argparse
import json
import math
import os
import subprocess
import sys


def emit(**r):
    print(json.dumps(r,sort_keys=True),flush=True)


def worker():
    d,p=20,19
    a=[0]*19
    a[0],a[1]=1,-1
    bins=[[math.comb(j,k)%p for k in range(j+1)] for j in range(20)]
    weights={j:(math.comb(d,j)//p)%p for j in range(2,19)}
    all_masks=[]
    kept=[]
    excluded=[]
    emit(event='parameters',pid=os.getpid(),degree=d,prime=p,J=16,
         mask='bit j-2 selects center1 for D_j',
         candidate_condition='H2(1)=0 or H3(1)=0')

    def descend(j,total,mask):
        if j==19:
            if total%p==1 and max(k for k in range(2,19) if a[k])==16:
                all_masks.append(mask)
                if mask & ((1<<15)|(1<<16)):
                    kept.append(mask)
                else:
                    excluded.append(mask)
            return
        a[j]=0
        descend(j+1,total,mask)
        a[j]=-(1-j+sum(bins[j][k]*a[k] for k in range(2,j)))%p
        descend(j+1,total+weights[j]*a[j],mask|(1<<(j-2)))
        a[j]=0

    descend(2,0,0)
    assert len(all_masks)==887
    inv5=pow(5,-1,p)
    profiles=[]
    for b in range(1,p):
        alpha=-2*b*inv5%p
        beta=-3*b*inv5%p
        # q(T)=A+b*T+T^2 with these roots, so A=alpha*beta.
        A=alpha*beta%p
        f2=(A+3*b*alpha+6*alpha**2)%p
        f3alpha=(b+4*alpha)%p
        f3beta=(b+4*beta)%p
        assert f2==0 and f3alpha and f3beta
        profiles.append(dict(b=b,alpha=alpha,beta=beta,
                             H2_at_alpha=f2,H3_at_alpha=f3alpha,H3_at_beta=f3beta))
    emit(event='complete',binary_J16_patterns=len(all_masks),
         excluded_both_H2_H3_noncenter=len(excluded),
         remaining_J16_patterns=len(kept),remaining_center_masks=kept,
         excluded_center_masks=excluded,quadratic_initial_profiles=profiles,
         scope='candidate Newton obstruction plus finite exact arithmetic; not full degree proof')


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
