#!/usr/bin/env python3
"""Explore parity-preserving run inflation and staircase self-shuffle roots."""
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


def runs(word):return [(c,len(list(g))) for c,g in itertools.groupby(word)]
def compress(word):return "".join(c*(1+(n-1)%2) for c,n in runs(word))


def classify(word):
    small=structure.lex_history(*probe.context(word))
    canonical=small==word
    prefix=structure.lex_history(*probe.context(word[:-1]))
    suffix=structure.lex_history(*probe.context(word[1:]))
    minimal=not canonical and prefix==word[:-1] and suffix==word[1:]
    return {"noncanonical":not canonical,"minimal_bad":minimal,"canonical":small,
            "proper_prefix_canonical":prefix==word[:-1],"proper_suffix_canonical":suffix==word[1:]}


p=argparse.ArgumentParser()
p.add_argument("--probe",required=True)
p.add_argument("--inflations",type=int,default=4)
p.add_argument("--state-cap",type=int,default=20000)
p.add_argument("--max-staircase",type=int,default=8)
p.add_argument("--output",required=True)
a=p.parse_args()
start=time.monotonic()
data=json.load(open(a.probe))
known={x["larger"] for x in data["minimal_forbidden"]}
cores=sorted({compress(x) for x in known},key=lambda h:(len(h),h))
tested=0
new_minimal=[]
failed=[]
for base in cores:
    rr=runs(base)
    for i in range(1,len(rr)-1):
        for addition in range(1,a.inflations+1):
            assert tested<a.state_cap
            word="".join(c*(n+2*addition if j==i else n) for j,(c,n) in enumerate(rr))
            result=classify(word)
            assert result["noncanonical"], "run inflation failed to preserve this known collision"
            record={"base":base,"run_index":i,"addition_pairs":addition,"word":word,**result}
            if result["minimal_bad"] and word not in known:new_minimal.append(record)
            if not result["minimal_bad"] and "RRLL" not in word:
                failed.append(record)
            tested+=1
    print(json.dumps({"checkpoint":"inflations","core":base,"tested":tested,"pid":os.getpid()}),flush=True)
staircases=[]
for n in range(1,a.max_staircase+1):
    lengths=list(range(1,n+1))+list(range(n,0,-1))
    u="".join(str(i%2)*r for i,r in enumerate(lengths))
    small=structure.lex_history(u,u)
    count=family.history_count(u,u)
    large=None if small is None else small.translate(str.maketrans("LR","RL"))
    row={"n":n,"root":u,"run_lengths":lengths,"root_length":len(u),
         "history_count":count,"least_history":small,"largest_history_by_symmetry":large}
    if large is not None:row.update(classify(large))
    staircases.append(row)
    print(json.dumps({"checkpoint":"staircase","n":n,"history_count":count,
                      "minimal_bad":row.get("minimal_bad"),"pid":os.getpid()}),flush=True)
out={"status":"bounded evidence only; unrestricted conjectures not asserted",
     "parameters":vars(a),"compressed_known_cores":cores,"inflations_tested":tested,
     "new_minimal_by_single_run_inflation":new_minimal,
     "nonminimal_inflations_without_RRLL":failed,"staircases":staircases,
     "elapsed_seconds":time.monotonic()-start}
with open(a.output,"w") as f:
    json.dump(out,f,indent=2)
    f.write("\n")
print(json.dumps({"finished":True,"seconds":out["elapsed_seconds"],"states":tested}),flush=True)
