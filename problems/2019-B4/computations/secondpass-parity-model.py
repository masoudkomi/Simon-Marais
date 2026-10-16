#!/usr/bin/env python3
"""Finite falsification tests for an independent even-run-inflation model."""
import argparse
import itertools
import json
import os
import sys
import time
from importlib.machinery import SourceFileLoader
sys.dont_write_bytecode=True
here=__file__.rsplit("/",1)[0]
probe=SourceFileLoader("frozen_probe",here+"/secondpass-probe.py").load_module()
structure=SourceFileLoader("frozen_structure",here+"/secondpass-structure.py").load_module()
family=SourceFileLoader("frozen_family",here+"/secondpass-family.py").load_module()


def runs(h):return [(c,len(list(g))) for c,g in itertools.groupby(h)]
def compress(h):return "".join(c*(1+(r-1)%2) for c,r in runs(h))
def minimal(h):
    return (structure.lex_history(*probe.context(h))!=h and
            structure.lex_history(*probe.context(h[:-1]))==h[:-1] and
            structure.lex_history(*probe.context(h[1:]))==h[1:])

p=argparse.ArgumentParser()
p.add_argument("--cores",required=True)
p.add_argument("--full",required=True)
p.add_argument("--state-cap",type=int,default=20000)
p.add_argument("--output",required=True)
a=p.parse_args()
start=time.monotonic()
cores=json.load(open(a.cores))["bounded_run_minimal_forbidden"]
full=json.load(open(a.full))["all_minimal_forbidden_in_complete_layers"]
tested=0
rows=[]
counter=[]
for rec in cores:
    h=rec["larger"]
    rr=runs(h)
    allowed=[]
    for i in range(len(rr)):
        pumped="".join(c*(r+2 if j==i else r) for j,(c,r) in enumerate(rr))
        assert tested<a.state_cap
        tested+=1
        if minimal(pumped):allowed.append(i)
    all_combinations=True
    for mask in range(1<<len(allowed)):
        chosen={allowed[j] for j in range(len(allowed)) if (mask>>j)&1}
        pumped="".join(c*(r+2 if j in chosen else r) for j,(c,r) in enumerate(rr))
        assert tested<a.state_cap
        tested+=1
        if not minimal(pumped):
            all_combinations=False
            counter.append({"core":h,"pumped":pumped,"inflated_run_indices":sorted(chosen)})
    rows.append({"core":h,"length":len(h),"allowed_single_run_indices":allowed,
                 "variable_count":len(allowed),"all_binary_inflation_combinations_minimal":all_combinations,
                 "core_history_count":family.history_count(*rec["tapes"])})
    print(json.dumps({"checkpoint":"parity_model","core_length":len(h),
                      "variables":len(allowed),"tested":tested,"pid":os.getpid()}),flush=True)
bycore={x["core"]:x for x in rows}
decomposition_counter=[]
for rec in full:
    h=rec["larger"]
    core=compress(h)
    if core not in bycore:
        decomposition_counter.append({"history":h,"compressed":core,"reason":"unknown compressed core"})
        continue
    inflated={i for i,((c,r),(cc,rr)) in enumerate(zip(runs(h),runs(core))) if r>rr}
    if not inflated.issubset(bycore[core]["allowed_single_run_indices"]):
        decomposition_counter.append({"history":h,"compressed":core,"reason":"joint inflation uses a forbidden single-run position"})
out={"status":"finite evidence only; no unrestricted independent-inflation grammar asserted",
     "parameters":vars(a),"states_tested":tested,"cores":rows,
     "joint_inflation_counterexamples":counter,"full_data_decomposition_counterexamples":decomposition_counter,
     "elapsed_seconds":time.monotonic()-start}
with open(a.output,"w") as f:
    json.dump(out,f,indent=2)
    f.write("\n")
print(json.dumps({"finished":True,"seconds":out["elapsed_seconds"],"states":tested}),flush=True)
