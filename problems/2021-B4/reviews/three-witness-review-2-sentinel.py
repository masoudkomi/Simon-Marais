#!/usr/bin/env python3
"""Supplementary independent sentinel reconstruction; own module only."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True
base = Path(__file__).resolve().with_name("three-witness-review-2")
spec = importlib.util.spec_from_file_location("own_review_r2",str(base)+"-independent.py")
own = importlib.util.module_from_spec(spec)
spec.loader.exec_module(own)
start = time.monotonic()
c = [[0] for _ in range(21)]
c[20],c[19] = [1],[-20]
mask,umask = 6436,24785
for l in range(18,1,-1):
    bit = 1 << (18-l)
    w = 1 if mask & bit else 2 if umask & bit else 0
    c[l] = own.solve_coefficient(c,l,w)
P,Q = own.form_pair(c)
trials = []
for p in [101,103,107,109,127,131]:
    g = own.gcd_mod(P,Q,p)
    trial = {"prime":p,"prime_verified":own.prime(p),"leading_residues":[P[-1]%p,Q[-1]%p],
             "retained_degrees":[len(own.trim([n%p for n in poly]))-1 for poly in [P,Q]],
             "gcd_degree":len(g)-1,"gcd_coefficients":g}
    trials.append(trial)
    if p != 131:
        assert 0 in trial["leading_residues"] or trial["gcd_degree"] > 0
    else:
        assert trial["leading_residues"] == [8,102] and trial["retained_degrees"] == [16,20] and trial["gcd_degree"] == 0
r = {"center_mask":mask,"u_mask":umask,"P":P,"Q":Q,"degrees":[len(P)-1,len(Q)-1],
     "trials":trials,"seconds":time.monotonic()-start,
     "canonical_polynomial_record_sha256":hashlib.sha256((json.dumps([mask,umask,P,Q],separators=(",",":"))+"\n").encode()).hexdigest()}
Path(str(base)+"-sentinel-result.json").write_text(json.dumps(r,indent=2)+"\n")
print(json.dumps(r),flush=True)
