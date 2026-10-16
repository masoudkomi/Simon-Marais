#!/usr/bin/env python3
"""Exact integer inequalities for the candidate non-overlap renewal bound."""
import argparse
from fractions import Fraction
import json
import os
import time

p=argparse.ArgumentParser()
p.add_argument("--probe",required=True)
p.add_argument("--output",required=True)
a=p.parse_args()
start=time.monotonic()
d=json.load(open(a.probe))
N=d["rows"][-1]["moves"]
f=[0]*(N+1)
for x in d["minimal_forbidden"]:f[len(x["larger"])]+=1

def E(x):
    return Fraction(1)-Fraction(2*N,N+1)*x+sum(Fraction(N+1-n,N+1)*f[n]*x**n for n in range(N+1))

def as_json(x):return {"numerator":x.numerator,"denominator":x.denominator,"decimal":float(x)}

lo,hi=Fraction(1,2),Fraction(3,5)
for _ in range(70):
    mid=(lo+hi)/2
    if E(mid)>0:lo=mid
    else:hi=mid
# Choose a user-readable strict lower bound safely below the numerical root reciprocal.
lower_num=int(1/float(hi)*100000)-1
lower_den=100000
r0=Fraction(lower_den,lower_num)
assert E(r0)<0 and E(Fraction(3,5))<0
assert 395397*Fraction(3,5)**24>1
out={"status":"candidate proof - unverified; exact finite inequalities",
     "parameters":vars(a),"max_known_forbidden_length":N,"forbidden_counts":f,
     "E_definition":"1 - (2N/(N+1))x + sum((N+1-n)/(N+1)*f_n*x^n,n<=N)",
     "E_first_positive_root_numerical_bracket_only":[float(lo),float(hi)],
     "candidate_lambda_strict_lower_numerator":lower_num,"candidate_lambda_strict_lower_denominator":lower_den,
     "candidate_lambda_strict_lower_decimal":lower_num/lower_den,
     "r0":as_json(r0),"E_r0":as_json(E(r0)),"E_three_fifths":as_json(E(Fraction(3,5))),
     "accepted_lower_bound_implies_R_less_than_three_fifths":as_json(395397*Fraction(3,5)**24),
     "elapsed_seconds":time.monotonic()-start}
with open(a.output,"w") as f:
    json.dump(out,f,indent=2)
    f.write("\n")
print(json.dumps({"finished":True,"pid":os.getpid(),"seconds":out["elapsed_seconds"],
                  "candidate_lower_bound":out["candidate_lambda_strict_lower_decimal"]}),flush=True)
