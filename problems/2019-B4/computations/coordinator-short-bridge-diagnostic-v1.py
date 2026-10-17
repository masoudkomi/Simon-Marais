"""One bounded counterexample probe for a specific <=3 bridge conjecture.

Not a new growth enumeration or proof of a uniform joining statement.
Parent runner imposes ten seconds and records this child PID.
"""
from pathlib import Path
import itertools,json,time,hashlib
start=time.monotonic()
source=Path('problems/2019-B4/computations/secondpass-full-obstruction24-v2.json')
data=json.loads(source.read_text())
forbidden=[x['larger'] for x in data['all_minimal_forbidden_in_complete_layers'] if len(x['larger'])<=19]
assert data['completed_through']==24
def hit(w):
 for f in forbidden:
  i=w.find(f)
  if i>=0:return dict(factor=f,offset=i)
 return None
words=[''.join(x)for x in itertools.product('LR',repeat=8)]
words=[w for w in words if hit(w)is None]
bridges=[''.join(x)for n in range(4)for x in itertools.product('LR',repeat=n)]
tested=0;found=None
for u in words:
 for v in words:
  tested+=1;failures=[]
  for b in bridges:
   h=hit(u+b+v)
   if h is None:break
   failures.append(dict(bridge=b,**h))
  else:
   found=dict(u=u,v=v,every_bridge_failure=failures);break
 if found:break
result=dict(status='finite diagnostic evidence only',hypothesis='Every two canonical histories have some canonical joining bridge of length at most3',fixed_word_lengths=[8,8],maximum_combined_length=19,accepted_forbidden_source=str(source),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),source_complete_through=24,pairs_examined=tested,counterexample=found,elapsed_seconds=time.monotonic()-start,no_absence_to_unrestricted_inference=True)
print(json.dumps(result,indent=2),flush=True)
