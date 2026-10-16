#!/usr/bin/env python3
"""Independent arbitrary-precision E evaluator and complete digit fibers.

Written after reading only owner v1/v2 mathematical notes, before opening
their code, manifests, certificates or node serialization. Imports only
the independent R1 review helper. Constructor-format adapters are separate.
"""
import importlib.util
import itertools
from fractions import Fraction
from pathlib import Path

spec=importlib.util.spec_from_file_location("r1base",Path(__file__).with_name("J16-digits-review-1-verifier.py"))
base=importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
P=19
_multipliers={}


def scalar(key,k):
    mask,um,vm,nu,x,y=key
    q=P**nu
    mod=P**(nu+k+1)
    aa=[1,-1]
    for j in range(2,19):
        bit=1<<(j-2)
        w=1 if mask & bit else q*x if um & bit else q*y if vm & bit else 0
        if not w:
            aa.append(0)
            continue
        mk=(k,nu,w,j)
        if mk not in _multipliers:
            _multipliers[mk]=[(h,-base.CH[j][h]*pow(w,j-h,mod)%mod) for h in range(j)]
            _multipliers[mk]=[(h,c) for h,c in _multipliers[mk] if c]
        aa.append(sum(aa[h]*c for h,c in _multipliers[mk])%mod)
    return aa,mod


def evaluate(key,k):
    """Compute all E residues mod 19^(k+1) by full monic division."""
    mask,um,vm,nu,x,y=key
    q=P**nu
    aa,mod=scalar(key,k)
    rem_mod=P*mod
    pe=(-1+sum(base.BETA[j]*aa[j] for j in range(2,19)))%mod
    cc=[(P*base.BETA[18-e]*aa[18-e])%rem_mod for e in range(17)]+[-20%rem_mod,1]
    s,t=q*(x+y),q*q*x*y
    for e in range(18,1,-1):
        z=cc[e]
        cc[e-1]=(cc[e-1]+s*z)%rem_mod
        cc[e-2]=(cc[e-2]-t*z)%rem_mod
    assert pe%q==0 and cc[0]%(P*q)==0 and cc[1]%(P*q)==0
    e_mod=P**(k+1)
    ee=[(pe//q)%e_mod,
        (cc[0]//(P*q))*pow(base.BETA[18],-1,e_mod)%e_mod,
        (cc[1]//(P*q))%e_mod]
    return aa,mod,ee


def rref(matrix,constants):
    rr=[[x%P,y%P,-z%P] for (x,y),z in zip(matrix,constants)]
    rank=0
    for col in range(2):
        pivot=next((i for i in range(rank,3) if rr[i][col]),None)
        if pivot is None:continue
        rr[rank],rr[pivot]=rr[pivot],rr[rank]
        f=pow(rr[rank][col],-1,P)
        rr[rank]=[x*f%P for x in rr[rank]]
        for i in range(3):
            if i==rank:continue
            f=rr[i][col]
            rr[i]=[(x-f*y)%P for x,y in zip(rr[i],rr[rank])]
        rank+=1
    return rank,rr


def digits(matrix,constants):
    """Return every digit by Cramer or one free coordinate, independently of RREF."""
    rank,consistent=base.affine_cramer(matrix,constants)
    if not consistent:return rank,[]
    rhs=[-c%P for c in constants]
    if rank==2:
        for i,j in ((0,1),(0,2),(1,2)):
            a,b=matrix[i]
            c,d=matrix[j]
            det=(a*d-b*c)%P
            if det:
                inv=pow(det,-1,P)
                return rank,[[(rhs[i]*d-b*rhs[j])*inv%P,(a*rhs[j]-rhs[i]*c)*inv%P]]
    if rank==1:
        pivot=next(i for i,row in enumerate(matrix) if row[0] or row[1])
        a,b=matrix[pivot]
        if a:
            inv=pow(a,-1,P)
            return rank,sorted([[(rhs[pivot]-b*y)*inv%P,y] for y in range(P)])
        return rank,[[x,rhs[pivot]*pow(b,-1,P)%P] for x in range(P)]
    return rank,[[x,y] for x in range(P) for y in range(P)]


def lift(key,k,matrix):
    aa,mod,ee=evaluate(key,k)
    pk=P**k
    assert all(z%pk==0 for z in ee),("input-not-a-node",key,k,ee)
    constants=[z//pk for z in ee]
    rank,points=digits(matrix,constants)
    rank2,reduced=rref(matrix,constants)
    assert rank==rank2
    assert bool(points)==(not any(r[0]==r[1]==0 and r[2] for r in reduced))
    # T1 pruning applies to the entire assignment, independent of residues.
    pruned=not key[1] or not key[2]
    children=[] if pruned else [(*key[:4],key[4]+pk*x,key[5]+pk*y) for x,y in points]
    return dict(a=aa,modulus=mod,E=ee,constants=constants,matrix=matrix,
                rank=rank,rref=reduced,digits=points,pruned=bool(pruned),children=children)


def exact(key,k):
    """Untruncated integer Horner recurrence and exact long division."""
    mask,um,vm,nu,x,y=key
    q=P**nu
    aa=[1,-1]
    for j in range(2,19):
        bit=1<<(j-2)
        w=1 if mask&bit else q*x if um&bit else q*y if vm&bit else 0
        acc=0
        for h in range(j):
            acc=(acc+base.CH[j][h]*aa[h])*w
        aa.append(-acc)
    ff=[P*base.BETA[18-e]*aa[18-e] for e in range(17)]+[-20,1]
    ordinary=ff[:]
    s,t=q*(x+y),q*q*x*y
    for e in range(18,1,-1):
        z=ff[e]
        ff[e-1]+=s*z
        ff[e-2]-=t*z
    pe=-1+sum(base.BETA[j]*aa[j] for j in range(2,19))
    ee=[Fraction(pe,q),Fraction(ff[0],P*q*base.BETA[18]),Fraction(ff[1],P*q)]
    assert all(e.denominator%P for e in ee)
    e_mod=P**(k+1)
    residues=[e.numerator*pow(e.denominator,-1,e_mod)%e_mod for e in ee]
    return dict(a=aa,F=ordinary,R0=ff[0],R1=ff[1],Ptilde=pe,E_fraction=ee,E=residues)


def obstruction(matrix,constants):
    def det(a,b):return (a[0]*b[1]-a[1]*b[0])%P
    lam=[det(matrix[1],matrix[2]),det(matrix[2],matrix[0]),det(matrix[0],matrix[1])]
    assert any(lam)
    assert all(sum(lam[i]*matrix[i][j] for i in range(3))%P==0 for j in range(2))
    return lam,sum(a*b for a,b in zip(lam,constants))%P
