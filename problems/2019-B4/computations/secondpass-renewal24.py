#!/usr/bin/env python3
"""Exact scalar upper/lower certificates using fully enumerated F through 24."""
import argparse
from fractions import Fraction
import json
import math
import os
import time

p=argparse.ArgumentParser()
p.add_argument("--full",required=True)
p.add_argument("--output",required=True)
a=p.parse_args()
start=time.monotonic()
data=json.load(open(a.full))
N=data["completed_through"]
assert data["all_requested_lengths_completed"]
words=[r["larger"] for r in data["all_minimal_forbidden_in_complete_layers"]]
f=[0]*(N+1)
for h in words:f[len(h)]+=1
for h in words:
    for g in words:
        assert not (h!=g and (h in g or g in h))
        assert not any(h[-k:]==g[:k] for k in range(1,min(len(h),len(g))))

def D(x):return Fraction(1)-2*x+sum(f[n]*x**n for n in range(N+1))
def derivative_D(x):return Fraction(-2)+sum(n*f[n]*x**(n-1) for n in range(1,N+1))
def E(x):return Fraction(1)-Fraction(2*N,N+1)*x+sum(Fraction(N+1-n,N+1)*f[n]*x**n for n in range(N+1))
def pack(x):return {"numerator":x.numerator,"denominator":x.denominator,"decimal":float(x)}
def root(fn):
    lo,hi=Fraction(1,2),Fraction(3,5)
    for _ in range(65):
        mid=(lo+hi)/2
        if fn(mid)>0:lo=mid
        else:hi=mid
    return lo,hi

rootD=root(D)
q_num=math.ceil(1/float(rootD[0])*10**8)+1
q_den=10**8
x=Fraction(q_den,q_num)
assert D(x)>0 and derivative_D(x)<0
rootE=root(E)
lower_num=math.floor(1/float(rootE[1])*100000)-1
lower_den=100000
r0=Fraction(lower_den,lower_num)
assert E(r0)<0 and E(Fraction(3,5))<0
assert 395397*Fraction(3,5)**24>1
out={"status":"candidate proof - unverified; exact scalar sign certificates",
     "parameters":vars(a),"N":N,"minimal_forbidden_count":len(words),"forbidden_counts":f,
     "finite_forbidden_set_factor_free_and_nonoverlapping":True,
     "strict_upper_q":pack(Fraction(q_num,q_den)),"upper_x":pack(x),"D_upper_x":pack(D(x)),
     "D_derivative_upper_x":pack(derivative_D(x)),
     "strict_lower_lambda":pack(Fraction(lower_num,lower_den)),"lower_r0":pack(r0),
     "E_lower_r0":pack(E(r0)),"E_three_fifths":pack(E(Fraction(3,5))),
     "numerical_roots_evidence_only":{"D":[float(v) for v in rootD],"E":[float(v) for v in rootE]},
     "elapsed_seconds":time.monotonic()-start}
with open(a.output,"w") as out_file:
    json.dump(out,out_file,indent=2)
    out_file.write("\n")
print(json.dumps({"finished":True,"pid":os.getpid(),"seconds":out["elapsed_seconds"],
                  "candidate_enclosure":[lower_num/lower_den,q_num/q_den]}),flush=True)
