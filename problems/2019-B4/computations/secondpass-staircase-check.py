#!/usr/bin/env python3
"""Bounded exact check of the closed staircase formula and forced-choice table."""
import argparse
import json
import os
import time


def count_histories(u,v):
    dp=[[0]*(len(v)+1) for _ in range(len(u)+1)]
    dp[0][0]=1
    for i in range(len(u)+1):
        for j in range(len(v)+1):
            bit=str((i+j)%2)
            if i<len(u) and u[i]==bit:dp[i+1][j]+=dp[i][j]
            if j<len(v) and v[j]==bit:dp[i][j+1]+=dp[i][j]
    return dp[-1][-1]


def make_formula(n):
    parts=[("RR","initial",None,1)]
    parts.extend(("LR"*j+"R","ascending",j,j+1) for j in range(1,n))
    parts.append(("LR"*(n-1)+"LL","central",None,n-1))
    parts.extend(("RL"*j+"L","descending",j,j-1) for j in range(n-1,0,-1))
    h=""
    entries={}
    for word,kind,j,other in parts:
        pos=len(h)+(0 if kind=="initial" else len(word)-2)
        entries[pos]={"kind":kind,"j":j,"expected_other_run":other}
        h+=word
    return h,entries


def remaining_run(word,i):
    if i==len(word):return 0
    j=i+1
    while j<len(word) and word[j]==word[i]:j+=1
    return j-i


p=argparse.ArgumentParser()
p.add_argument("--max-n",type=int,default=11)
p.add_argument("--state-cap",type=int,default=20000)
p.add_argument("--output",required=True)
a=p.parse_args()
start=time.monotonic()
rows=[]
for n in range(1,a.max_n+1):
    lengths=list(range(1,n+1))+list(range(n,0,-1))
    u="".join(str(i%2)*r for i,r in enumerate(lengths))
    assert (len(u)+1)**2<=a.state_cap
    h,table=make_formula(n)
    tapes=["",""]
    for t,c in enumerate(h):tapes[c=="R"]+=str(t%2)
    assert tapes==[u,u]
    assert len(h)==2*n*(n+1)
    indices=[0,0]
    checks=[]
    for t,c in enumerate(h):
        bit=str(t%2)
        chosen=c=="R"
        heads=[tapes[k][indices[k]:indices[k]+1] for k in range(2)]
        assert heads[chosen]==bit
        if heads==[bit,bit]:
            viable=[k for k in range(2) if indices[k]+1<len(tapes[k]) and tapes[k][indices[k]+1]!=bit]
            assert (viable==[0,1] if t==0 else viable==[chosen])
            assert t in table
        if t in table:
            row={"position":t,**table[t],"chosen":c,
                 "chosen_run":remaining_run(tapes[chosen],indices[chosen]),
                 "other_run":remaining_run(tapes[not chosen],indices[not chosen])}
            assert row["chosen_run"]==1
            assert row["other_run"]==row["expected_other_run"]
            assert indices[chosen]+1<len(tapes[chosen]) and tapes[chosen][indices[chosen]+1]!=bit
            assert not heads[not chosen] or heads[not chosen]==bit
            checks.append(row)
        indices[chosen]+=1
    count=count_histories(u,u)
    assert count==2
    row={"n":n,"root_length":len(u),"history_length":len(h),"history_count":count,
         "grid_states":(len(u)+1)**2,"formula_history":h,"table_checks":checks}
    rows.append(row)
    print(json.dumps({"checkpoint":"staircase_formula","n":n,"history_count":count,
                      "grid_states":row["grid_states"],"pid":os.getpid()}),flush=True)
out={"status":"bounded exact evidence; unrestricted proof requires separate audit",
     "parameters":vars(a),"rows":rows,"elapsed_seconds":time.monotonic()-start}
with open(a.output,"w") as f:
    json.dump(out,f,indent=2)
    f.write("\n")
print(json.dumps({"finished":True,"seconds":out["elapsed_seconds"]}),flush=True)
