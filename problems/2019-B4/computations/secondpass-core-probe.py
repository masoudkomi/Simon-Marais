#!/usr/bin/env python3
"""Exact minimal bad factors with all runs <=2, within explicit node cap.

No inference that arbitrary minimal factors reduce to these cores is made.
"""
import argparse
import json
import os
import sys
import time
from importlib.machinery import SourceFileLoader
sys.dont_write_bytecode=True
here=__file__.rsplit("/",1)[0]
probe=SourceFileLoader("frozen_probe",here+"/secondpass-probe.py").load_module()
structure=SourceFileLoader("frozen_structure",here+"/secondpass-structure.py").load_module()

p=argparse.ArgumentParser()
p.add_argument("--max-n",type=int,default=26)
p.add_argument("--state-cap",type=int,default=20000)
p.add_argument("--output",required=True)
a=p.parse_args()
start=time.monotonic()
bad=[]
rows=[]
finished=True
for n in range(4,a.max_n+1):
    nodes=0
    leaves=0
    new=[]
    capped=False
    stack=["RR"]
    while stack:
        if nodes>=a.state_cap:
            capped=True
            finished=False
            break
        h=stack.pop()
        nodes+=1
        if len(h)==n:
            leaves+=1
            u,v=probe.context(h)
            canonical=structure.lex_history(u,v)
            if canonical!=h:
                # Shorter minimal factors in this bounded-run class were
                # all found at previous lengths, and have been excluded.
                assert structure.lex_history(*probe.context(h[:-1]))==h[:-1]
                assert structure.lex_history(*probe.context(h[1:]))==h[1:]
                new.append({"larger":h,"smaller":canonical,"tapes":[u,v]})
            continue
        position=len(h)
        if n==4:
            choices="L"
        elif position>=n-3:
            choices="RLL"[position-(n-3)]
        else:
            choices="RL" # L is popped first
        for c in choices:
            word=h+c
            if len(word)>=3 and word[-3:]==c*3:continue
            if any(word.endswith(x["larger"]) for x in bad):continue
            stack.append(word)
    row={"length":n,"nodes":nodes,"leaves":leaves,"complete":not capped,
         "new_core_count":len(new)}
    rows.append(row)
    bad.extend(new)
    print(json.dumps({"checkpoint":row,"pid":os.getpid()}),flush=True)
    if capped:break
out={"status":"finite evidence only; bounded-run class, not full obstruction language",
     "parameters":vars(a),"all_requested_lengths_completed":finished,"rows":rows,
     "bounded_run_minimal_forbidden":bad,"elapsed_seconds":time.monotonic()-start}
with open(a.output,"w") as f:
    json.dump(out,f,indent=2)
    f.write("\n")
print(json.dumps({"finished":True,"all_requested_lengths_completed":finished,
                  "seconds":out["elapsed_seconds"]}),flush=True)
