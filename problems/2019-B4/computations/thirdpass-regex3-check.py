#!/usr/bin/env python3
"""Exact DFA/NFA language-equivalence check for the proposed delay-3 grammar."""
import argparse,collections,json,time,os
p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
t=time.monotonic();d=json.load(open(a.input))
trans=collections.defaultdict(lambda:collections.defaultdict(set));next_id=3
start,accept,loop=0,1,2

def path(src,word,dst):
 global next_id
 for i,c in enumerate(word):
  target=dst if i==len(word)-1 else next_id
  if i<len(word)-1:next_id+=1
  trans[src][c].add(target);src=target

path(start,'RRLL',accept)
path(start,'RRLRRLRL',loop)
for block in ('RRLRL','LRLRL','LRLRRLRL'):path(loop,block,loop)
path(loop,'LRLL',accept)
seen={(d['start'],frozenset({start}))};queue=collections.deque(seen)
while queue:
 q,S=queue.popleft()
 assert (q==d['terminal'])==(accept in S),(q,S)
 for c in 'LR':
  q1=-1 if q<0 else d['edges'][q][c=='R']
  T=frozenset().union(*(trans[s][c] for s in S))
  pair=(q1,T)
  if pair not in seen:seen.add(pair);queue.append(pair)
out={'status':'exact finite language-equivalence certificate; not independent agent review',
     'regular_expression':'RRLL | RRLRRLRL (RRLRL | LRLRL | LRLRRLRL)* LRLL',
     'input':a.input,'nfa_states':next_id,'product_states_checked':len(seen),
     'equal_languages':True,'elapsed_seconds':time.monotonic()-t}
with open(a.output,'w') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2))
