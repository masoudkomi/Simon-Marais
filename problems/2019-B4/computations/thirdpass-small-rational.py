#!/usr/bin/env python3
"""Compute the delay-3 rational functions from its finite transfer matrix."""
import argparse,json,time,os
import sympy as s
p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
t=time.monotonic();d=json.load(open(a.input));edges=d['edges'];n=len(edges)
assert n<=40
z=s.symbols('z');M=s.eye(n)
for i,row in enumerate(edges):
 for j in row:
  if j>=0:M[i,j]-=z
print(json.dumps({'checkpoint':'matrix constructed','dimension':n,'pid':os.getpid()}),flush=True)
x=s.linsolve((M,s.ones(n,1)));C=s.factor(list(x)[0][d['start']]);F=s.factor(1/C-1+2*z)
out={'input':a.input,'dimension':n,'C':str(C),'F':str(F),'F_series':str(s.series(F,z,0,45)),
     'elapsed_seconds':time.monotonic()-t,'sympy_version':s.__version__,'status':'finite symbolic evidence; candidate theorem pending review'}
with open(a.output,'w') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2))
