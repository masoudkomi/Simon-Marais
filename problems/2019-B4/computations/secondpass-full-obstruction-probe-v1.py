#!/usr/bin/env python3
"""Targeted extension of exact obstruction data to test parity compression.

Enumerate only candidates starting RR, ending LL, avoiding all known shorter
minimal bad factors. A per-length node cap makes incomplete layers explicit.
"""
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


def compress(h):return "".join(c*(1+(len(list(g))-1)%2) for c,g in itertools.groupby(h))


p=argparse.ArgumentParser()
p.add_argument("--initial-probe",required=True)
p.add_argument("--max-n",type=int,default=24)
p.add_argument("--state-cap",type=int,default=20000)
p.add_argument("--output",required=True)
a=p.parse_args()
start=time.monotonic()
old=json.load(open(a.initial_probe))
completed_through=old["rows"][-1]["moves"]
bad=list(old["minimal_forbidden"])
rows=[]
new_all=[]
fully_completed=True
for n in range(completed_through+1,a.max_n+1):
    nodes=leaves=0
    new=[]
    capped=False
    # A suffix trie makes the rejection test independent of the number
    # of forbidden words sharing long prefixes.
    reverse_trie={}
    for row in bad:
        node=reverse_trie
        for c in reversed(row["larger"]):node=node.setdefault(c,{})
        node[None]=True
    def ends_bad(word):
        node=reverse_trie
        for c in reversed(word):
            if c not in node:return False
            node=node[c]
            if None in node:return True
        return False
    stack=["RR"]
    while stack:
        if nodes>=a.state_cap:
            capped=True
            fully_completed=False
            break
        h=stack.pop()
        nodes+=1
        if len(h)==n:
            leaves+=1
            u,v=probe.context(h)
            canonical=structure.lex_history(u,v)
            if canonical!=h:
                assert structure.lex_history(*probe.context(h[:-1]))==h[:-1]
                assert structure.lex_history(*probe.context(h[1:]))==h[1:]
                core=compress(h)
                core_small=structure.lex_history(*probe.context(core))
                core_minimal=(core_small!=core and
                              structure.lex_history(*probe.context(core[:-1]))==core[:-1] and
                              structure.lex_history(*probe.context(core[1:]))==core[1:])
                new.append({"larger":h,"smaller":canonical,"tapes":[u,v],
                            "compressed":core,"compressed_is_noncanonical":core_small!=core,
                            "compressed_is_minimal_bad":core_minimal})
            continue
        position=len(h)
        choices="RLL"[position-(n-3)] if position>=n-3 else "RL"
        for c in choices:
            word=h+c
            if not ends_bad(word):stack.append(word)
    row={"length":n,"nodes":nodes,"leaves":leaves,"complete":not capped,
         "new_minimal_count":len(new)}
    rows.append(row)
    new_all.extend(new)
    print(json.dumps({"checkpoint":row,"pid":os.getpid()}),flush=True)
    if capped:break
    bad.extend(new)
    completed_through=n
out={"status":"finite evidence only; incomplete layers are not exact counts",
     "parameters":vars(a),"completed_through":completed_through,
     "all_requested_lengths_completed":fully_completed,"rows":rows,
     "new_minimal_forbidden":new_all,"all_minimal_forbidden_in_complete_layers":bad,
     "compression_counterexamples":[r for r in new_all if not r["compressed_is_minimal_bad"]],
     "elapsed_seconds":time.monotonic()-start}
with open(a.output,"w") as f:
    json.dump(out,f,indent=2)
    f.write("\n")
print(json.dumps({"finished":True,"all_requested_lengths_completed":fully_completed,
                  "seconds":out["elapsed_seconds"]}),flush=True)
