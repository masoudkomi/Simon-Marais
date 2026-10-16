#!/usr/bin/env python3
"""Exact bounded tests of structural conjectures, not asymptotic proofs."""
from __future__ import annotations
import argparse
import itertools
import json
import os
import time


def lex_history(u: str, v: str):
    m,n = len(u),len(v)
    good = [[False]*(n+1) for _ in range(m+1)]
    good[m][n] = True
    for i in range(m,-1,-1):
        for j in range(n,-1,-1):
            if i == m and j == n:
                continue
            expected = str((i+j)%2)
            good[i][j] = ((i<m and u[i] == expected and good[i+1][j]) or
                          (j<n and v[j] == expected and good[i][j+1]))
    if not good[0][0]:
        return None
    i=j=0
    history=[]
    while i+j < m+n:
        expected = str((i+j)%2)
        if i<m and u[i] == expected and good[i+1][j]:
            i+=1
            history.append("L")
        else:
            assert j<n and v[j] == expected and good[i][j+1]
            j+=1
            history.append("R")
    return "".join(history)


def signature(w):
    h=lo=hi=0
    for c in w:
        h += 1 if c == "0" else -1
        lo=min(lo,h)
        hi=max(hi,h)
    return len(w),h,lo,hi,w[:1],w[-1:]


def pair_greedy(u,v):
    i=j=0
    history=[]
    while i+j<len(u)+len(v):
        bit=str((i+j)%2)
        left=i<len(u) and u[i]==bit
        right=j<len(v) and v[j]==bit
        if left and right:
            # Either choice must immediately consume the opposite bit on
            # the same tape. Prefer the left tape if both permit that.
            if i+1<len(u) and u[i+1]!=bit:
                chosen="L"
            elif j+1<len(v) and v[j+1]!=bit:
                chosen="R"
            else:
                return None
        elif left:chosen="L"
        elif right:chosen="R"
        else:return None
        history.append(chosen)
        if chosen=="L":i+=1
        else:j+=1
    return "".join(history)


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--max-root-length",type=int,default=12)
    p.add_argument("--balanced-total",type=int,default=12)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    start=time.monotonic()
    rows=[]
    counter=[]
    for length in range(a.max_root_length+1):
        accepted=0
        mismatches=[]
        for cs in itertools.product("01",repeat=length):
            u="".join(cs)
            h=lex_history(u,u)
            hypothesized=(length == 0 or u == "01" or
                          (length>=4 and u[:2] == u[-2:] == "01" and
                           all(u[i:i+2] in ("01","10") for i in range(0,length,2))))
            accepted += h is not None
            if (h is not None) != hypothesized:
                mismatches.append({"word":u,"history":h,"hypothesis":hypothesized})
        rows.append({"root_length":length,"accepted_roots":accepted,
                     "hypothesis_mismatches":len(mismatches)})
        counter.extend(mismatches[:3])
        print(json.dumps({"checkpoint":"self_shuffle",**rows[-1],"pid":os.getpid()}),flush=True)
    seen={}
    range_counter=None
    greedy_counter=None
    pair_prefix_counter=None
    total=a.balanced_total
    examined=0
    for zeros in itertools.combinations(range(total),total//2):
        word=["1"]*total
        for i in zeros:
            word[i]="0"
        word="".join(word)
        for split in range(total+1):
            u,v=word[:split],word[split:]
            h=lex_history(u,v)
            k=signature(u),signature(v)
            accepted=h is not None
            g=pair_greedy(u,v)
            if accepted != (g is not None) and greedy_counter is None:
                greedy_counter={"u":u,"v":v,"canonical":h,"greedy":g}
            if accepted and u.startswith("01") and v.startswith("01") and lex_history(u[2:],v) is None and pair_prefix_counter is None:
                pair_prefix_counter={"u":u,"v":v,"canonical":h,"after_left_01":False}
            if k in seen and seen[k][0] != accepted and range_counter is None:
                old=seen[k]
                range_counter={"signature":k,"first":{"accepted":old[0],"u":old[1],"v":old[2],"history":old[3]},
                               "second":{"accepted":accepted,"u":u,"v":v,"history":h}}
            else:
                seen[k]=(accepted,u,v,h)
            examined+=1
    monoid_slice=[]
    for q in range(1,11):
        h="RRLR"+"RL"*q+"LRLL" # D B C^q B A
        u=v=""
        for i,c in enumerate(h):
            if c=="L":u+=str(i%2)
            else:v+=str(i%2)
        small=lex_history(u,v)
        monoid_slice.append({"q":q,"history":h,"tapes":[u,v],"canonical":small,"is_canonical":small==h})
    out={"status":"finite computational evidence only","parameters":vars(a),
         "self_shuffle_rows":rows,"self_shuffle_hypothesis_counterexamples":counter,
         "balanced_pairs_examined":examined,"range_signature_counterexample":range_counter,
         "two_step_greedy_counterexample":greedy_counter,
         "common_01_prefix_consumption_counterexample":pair_prefix_counter,
         "slice_D_B_Cpower_B_A":monoid_slice,"elapsed_seconds":time.monotonic()-start}
    with open(a.output,"w") as f:
        json.dump(out,f,indent=2)
        f.write("\n")
    print(json.dumps({"finished":True,"seconds":out["elapsed_seconds"]}),flush=True)


if __name__=="__main__":main()
