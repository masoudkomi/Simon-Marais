"""Targeted counterexample search only: local interval coarsening surjectivity.
No finite success proves unrestricted lifting or an entropy theorem."""
from functools import lru_cache
from itertools import permutations
import json,time

def inv(w):
 return frozenset((w[j],w[i]) for i in range(len(w)) for j in range(i+1,len(w)) if w[i]>w[j])
def group(w,mp):return tuple(mp[x] for x in w)
def event(w,k,d):
 counts=[0]*d
 for a in w[:k]:counts[a]+=1
 return tuple(counts)+(w[k],w[k+1])
def signatures(p,q):
 d=max(q)+1; target=inv(q)
 @lru_cache(None)
 def solve(w):
  if w==q:return frozenset([frozenset()])
  out=set()
  for k in range(len(w)-1):
   if w[k]<w[k+1] and (w[k],w[k+1]) in target:
    z=list(w);z[k],z[k+1]=z[k+1],z[k];z=tuple(z)
    e=event(w,k,d)
    for s in solve(z):out.add(s|{e})
  return frozenset(out)
 return solve(p)
def projected_signatures(p,q,mp):
 d=max(mp.values())+1; target=inv(q)
 @lru_cache(None)
 def solve(w):
  if w==q:return frozenset([frozenset()])
  out=set()
  for k in range(len(w)-1):
   if w[k]<w[k+1] and (w[k],w[k+1]) in target:
    z=list(w);z[k],z[k+1]=z[k+1],z[k];z=tuple(z)
    e=None if mp[w[k]]==mp[w[k+1]] else event(group(w,mp),k,d)
    for s in solve(z):out.add(s if e is None else s|{e})
  return frozenset(out)
 return solve(p)
started=time.time(); tested=0
for counts in [(2,1,2),(2,2,1),(1,2,2),(2,1,1,1)]:
 n=sum(counts);mp={};i=0
 for g,c in enumerate(counts):
  for _ in range(c):mp[i]=g;i+=1
 ps=list(permutations(range(n)));ivs={p:inv(p) for p in ps}
 for p in ps:
  for q in ps:
   if not ivs[p]<=ivs[q] or len(ivs[q])-len(ivs[p])>8:continue
   a,b=group(p,mp),group(q,mp)
   if a==b:continue
   tested+=1
   fine=projected_signatures(p,q,mp); coarse=signatures(a,b)
   missing=coarse-fine
   if missing:
    result={'status':'counterexample_found','counts':counts,'p':p,'q':q,'coarse_p':a,'coarse_q':b,'fine_projected_tiling_count':len(fine),'coarse_tiling_count':len(coarse),'missing_signature':sorted(next(iter(missing))),'all_projected_signatures':[sorted(s) for s in fine],'tested_intervals':tested,'elapsed':time.time()-started}
    print(json.dumps(result),flush=True);raise SystemExit
 print(json.dumps({'checkpoint_counts':counts,'tested_intervals':tested,'elapsed':time.time()-started}),flush=True)
print(json.dumps({'status':'no_counterexample_in_finite_scope','tested_intervals':tested,'elapsed':time.time()-started,'not_unrestricted_proof':True}),flush=True)
