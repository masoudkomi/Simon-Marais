#!/usr/bin/env python3
"""Bounded-separation competing histories. Finite evidence / candidate certificates.

Only writes an explicit output path; caps every automaton construction.
"""
from __future__ import annotations
import argparse, collections, json, os, time


def complement(w):
    return w.translate(str.maketrans('01','10'))


def successors(state, h, delay):
    """Pending L and R tapes normalized by the next source bit."""
    u,v=state
    d=len(u)
    out=[]
    if h=='R':
        # g chooses L: separation rises by one.
        if d<delay:
            out.append((complement(u+'0'),complement(v+'0')))
        # g chooses R: consume the first pending R symbol, append h's bit.
        if v.startswith('0'):
            out.append((complement(u),complement(v[1:]+'0')))
    else:
        # g chooses L: consume the first pending L symbol, append g's bit.
        if u.startswith('0'):
            out.append((complement(u[1:]+'0'),complement(v)))
        # g chooses R: both queues lose their first symbol.
        if u.startswith('0') and v.startswith('0'):
            if d==1:
                return None  # A strictly upper path has rejoined h.
            out.append((complement(u[1:]),complement(v[1:])))
    return out


def monitor(delay,cap):
    """Reachable subset monitor; no rejecting sink is stored."""
    start=frozenset()
    states=[start]
    ids={start:0}
    edges=[]
    for i,s in enumerate(states):
        row=[]
        for h in 'LR':
            new=set()
            if h=='R':
                new.add(('1','1'))  # begin competing at this factor position
            rejecting=False
            for q in s:
                step=successors(q,h,delay)
                if step is None:
                    rejecting=True
                    break
                new.update(step)
            if rejecting:
                row.append(-1)
                continue
            new=frozenset(new)
            if new not in ids:
                if len(states)>=cap:
                    return None, {'state_cap':cap,'states':len(states),'complete':False}
                ids[new]=len(states)
                states.append(new)
            row.append(ids[new])
        edges.append(row)
        if i and i%10000==0:
            print(json.dumps({'checkpoint':'subset monitor','delay':delay,'processed':i,
                              'discovered':len(states),'pid':os.getpid()}),flush=True)
    return (states,edges), {'states':len(states),'complete':True,
                           'max_active_competitors':max(map(len,states)),
                           'individual_competitors':len(set().union(*states))}


def minimize(edges):
    # Add a rejecting sink and refine by exact transition signatures.
    n=len(edges)
    complete=[[(j if j>=0 else n) for j in row] for row in edges]+[[n,n]]
    block=[0]*n+[1]
    while True:
        ids={}
        new=[]
        for i,row in enumerate(complete):
            sig=(i==n, *(block[j] for j in row))
            if sig not in ids: ids[sig]=len(ids)
            new.append(ids[sig])
        if new==block: break
        block=new
    reject=block[n]
    kept=sorted(set(block[:-1])-{reject})
    remap={b:i for i,b in enumerate(kept)}
    representative={block[i]:i for i in range(n)}
    out=[]
    for b in kept:
        out.append([remap.get(block[j],-1) for j in complete[representative[b]]])
    return out,remap[block[0]]


def counts(edges,start,n):
    vector=[0]*len(edges)
    vector[start]=1
    ans=[1]
    for t in range(n):
        out=[0]*len(edges)
        for i,row in enumerate(edges):
            for j in row:
                if j>=0: out[j]+=vector[i]
        vector=out
        ans.append(sum(vector))
    return ans


def power_bounds(edges,steps):
    # A all-positive starting vector gives directly rigorous rational
    # Collatz bounds, retained as fractions of integers in the output.
    vector=[1]*len(edges)
    lower=upper=None
    rows=[]
    for t in range(1,steps+1):
        nxt=[sum(vector[j] for j in row if j>=0) for row in edges]
        lower=min((nxt[i],vector[i]) for i in range(len(vector)) if vector[i])
        # min/max pairs must use rational comparison, not tuple order.
        lo=min(range(len(vector)),key=lambda i: nxt[i]/vector[i])
        hi=max(range(len(vector)),key=lambda i: nxt[i]/vector[i])
        if t in (10,50,steps):
            rows.append({'iteration':t,'lower':[nxt[lo],vector[lo]],
                         'upper':[nxt[hi],vector[hi]],
                         'approx_lower':nxt[lo]/vector[lo],
                         'approx_upper':nxt[hi]/vector[hi]})
        vector=nxt
    return rows,vector


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--delay',type=int,default=3)
    p.add_argument('--state-cap',type=int,default=5000)
    p.add_argument('--count-length',type=int,default=30)
    p.add_argument('--power-steps',type=int,default=200)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    assert 1<=a.delay<=10 and 1<=a.state_cap<=1000000 and 1<=a.power_steps<=1000
    begun=time.monotonic()
    automaton,meta=monitor(a.delay,a.state_cap)
    out={'status':'finite computational evidence; theorem pending independent reviews',
         'parameters':vars(a),'construction':meta,'pid':os.getpid()}
    if automaton:
        states,edges=automaton
        reduced,start=minimize(edges)
        print(json.dumps({'checkpoint':'minimized','delay':a.delay,
                          'states':len(reduced),'pid':os.getpid()}),flush=True)
        bounds,vector=power_bounds(reduced,a.power_steps)
        out.update({'minimal_states':len(reduced),'edges':reduced,'start':start,
                    'counts':counts(reduced,start,a.count_length),'power_bounds':bounds,
                    'positive_vector':vector,
                    'individual_competitors':sorted(set().union(*states))})
    out['elapsed_seconds']=time.monotonic()-begun
    with open(a.output,'w') as f:
        json.dump(out,f,indent=2)
        f.write('\n')
    print(json.dumps({'finished':True,'output':a.output,'seconds':out['elapsed_seconds']}),flush=True)

if __name__=='__main__':main()
