#!/usr/bin/env python3
"""Finite overlap/series data and symbolic certificate polynomial."""
import argparse
import json
import os
import time

p=argparse.ArgumentParser()
p.add_argument("--probe",required=True)
p.add_argument("--certificate",required=True)
p.add_argument("--output",required=True)
a=p.parse_args()
start=time.monotonic()
probe=json.load(open(a.probe))
forbidden=[x["larger"] for x in probe["minimal_forbidden"]]
overlaps=[]
for left in forbidden:
    for right in forbidden:
        for k in range(1,min(len(left),len(right))):
            if left[-k:]==right[:k]:
                overlaps.append({"left":left,"right":right,"overlap":k,
                                 "combined_length":len(left)+len(right)-k})
print(json.dumps({"checkpoint":"overlaps","count":len(overlaps),"pid":os.getpid()}),flush=True)
counts=[r["contexts"] for r in probe["rows"]]
inverse=[1]
for n in range(1,len(counts)):
    inverse.append(-sum(counts[i]*inverse[n-i] for i in range(1,n+1)))
charpoly=None
try:
    import sympy as s
    cert=json.load(open(a.certificate))["automata"][0]
    n=len(cert["transitions_LR"])
    mat=s.zeros(n)
    for i,row in enumerate(cert["transitions_LR"]):
        for j in row:
            if j is not None:mat[i,j]+=1
    x=s.Symbol("x")
    charpoly=str(s.factor(mat.charpoly(x).as_expr()))
    print(json.dumps({"checkpoint":"symbolic_charpoly","polynomial":charpoly}),flush=True)
except ImportError as e:
    charpoly={"unavailable":str(e)}
out={"status":"finite evidence and exact symbolic polynomial; no completeness claim",
     "parameters":vars(a),"overlaps":sorted(overlaps,key=lambda x:x["combined_length"]),
     "context_series_coefficients":counts,"reciprocal_series_coefficients":inverse,
     "family_automaton_characteristic_polynomial":charpoly,"elapsed_seconds":time.monotonic()-start}
with open(a.output,"w") as f:
    json.dump(out,f,indent=2)
    f.write("\n")
print(json.dumps({"finished":True,"seconds":out["elapsed_seconds"]}),flush=True)
