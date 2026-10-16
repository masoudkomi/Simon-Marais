#!/usr/bin/env python3
"""Independent reconstruction of all three new sentinels and accepted old one."""
from pathlib import Path
import hashlib
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True
base = Path(__file__).resolve().with_name("three-complex-review-2")
spec = importlib.util.spec_from_file_location("own_complex_review_r2",str(base)+"-independent.py")
own = importlib.util.module_from_spec(spec)
spec.loader.exec_module(own)
started = time.monotonic()
expected = {
    (117075,9220):([15,20],[83,3]),
    (117075,1548):([12,20],[44,79]),
    (117075,9356):([15,20],[97,124]),
    (6436,24785):([16,20],[8,102]),
}
results = []
for (mask,umask),(degrees,leading) in expected.items():
    c = [[0] for _ in range(21)]
    c[20],c[19] = [1],[-20]
    for l in range(18,1,-1):
        bit = 1 << (18-l)
        w = 1 if mask&bit else 2 if umask&bit else 0
        c[l] = own.solve_coefficient(c,l,w)
    P,Q = own.form_pair(c)
    assert degrees == [len(P)-1,len(Q)-1]
    trials = []
    for p in [101,103,107,109,127,131]:
        g = own.gcd_mod(P,Q,p)
        trial = {"prime":p,"prime_verified":own.prime(p),
                 "leading_residues":[P[-1]%p,Q[-1]%p],
                 "retained_degrees":[len(own.trim([n%p for n in poly]))-1 for poly in [P,Q]],
                 "gcd_degree":len(g)-1,"gcd_coefficients":g}
        trials.append(trial)
        if p == 131:
            assert trial["leading_residues"] == leading and trial["retained_degrees"] == degrees
            assert trial["gcd_degree"] == 0
        else:
            assert 0 in trial["leading_residues"] or trial["gcd_degree"] > 0
    record = {"center_mask":mask,"u_mask":umask,"P":P,"Q":Q}
    results.append({**record,"degrees":degrees,"trials":trials,
                    "raw_record_sha256":hashlib.sha256(json.dumps(record,sort_keys=True,separators=(",",":")).encode()).hexdigest(),
                    "polynomial_record_sha256":hashlib.sha256((json.dumps([mask,umask,P,Q],separators=(",",":"))+"\n").encode()).hexdigest()})
out = {"method":"ordinary Hasse exact integer construction, independent modular Euclidean gcd", "new_sentinels":3,"old_accepted_sentinel_rechecked":1,
       "cases":results,"seconds":time.monotonic()-started}
Path(str(base)+"-sentinels-result.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({k:v for k,v in out.items() if k != "cases"}),flush=True)
for r in results:
    print(json.dumps({"key":[r["center_mask"],r["u_mask"]],"degrees":r["degrees"],"leading_residues_131":r["trials"][-1]["leading_residues"],"gcd_131":r["trials"][-1]["gcd_coefficients"],"raw_record_sha256":r["raw_record_sha256"]}),flush=True)
