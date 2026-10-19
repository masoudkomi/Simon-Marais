"""NEW R29 documentary guard/freeze helper. NEVER executes mathematical code."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2021-B4/notes/coordinator-original-roots-r29-'
PAY=[P+s for s in ['candidate-v1.md','sources-v1.json','certificate-v1.py','admin-v1.py','baseline-v1.json']]
PARENT='problems/2021-B4/notes/coordinator-global-return-r28-freeze-v1.json'
NAMES=['reasoning-deep-return-r24','coordinator-dyadic-return-r26','coordinator-global-return-r28']
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads((ROOT/p).read_text())
def fp(p):
 b=(ROOT/p).read_bytes();return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(v):assert fp(v['path'])==v,v['path']
def new(p,v):
 assert p in [P+'baseline-v1.json',P+'freeze-v1.json']
 with(ROOT/p).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def labels():
 text=(ROOT/PAY[0]).read_text()
 for i in range(1,17):assert text.count('|R29-%02d|'%i)==1
def prepare():
 paths=['AGENTS.md','problems/2021-B4/statement.md']
 for n in NAMES:
  a='problems/2021-B4/reviews/'+n+'-acceptance.json';v=read(a);check(v['accepted_copy'])
  assert v['status']=='proved, independently reviewed scoped partial result'
  paths += [v['accepted_copy']['path'],a[:-4]+'md',a]
 paths.append(PARENT);assert len(paths)==len(set(paths))==12
 labels();new(P+'baseline-v1.json',dict(captured_UTC=now(),necessary_immutable_records=[fp(p)for p in paths],ONE_compact_OWN_parent=fp(PARENT),guard_occurrences=12,guard_unique_paths=12,recursive_inventory=False,mutable_map_guards=False,mathematics_certified_by_code=False))
 print(json.dumps(dict(prepared=fp(P+'baseline-v1.json'))))
def verify_base():
 b=read(P+'baseline-v1.json')
 for v in b['necessary_immutable_records']:check(v)
 return b
def freeze():
 assert '--FULL-final-ALL5-MODEL-readbacks-completed'in sys.argv
 b=verify_base();labels();new(P+'freeze-v1.json',dict(frozen_UTC=now(),status='candidate proof - unverified',constructor='/root',constructor_excluded=True,ENTIRE_files=6,ALL_obligations=16,payloads=[fp(p)for p in PAY],ONE_compact_OWN_parent=b['ONE_compact_OWN_parent'],FULL_final_ALL5_payload_MODEL_readbacks_completed=True,FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED=True,TWO_OTHER_initially_blind_ENTIRE_whole_audits_required=True,guard_occurrences=12,guard_unique_paths=12,requested=dict(model='gpt-6.1-sol',reasoning='max'),independent_effective_backend_readback=None,quota=dict(usedPercent=87,observed_UTC='2026-10-19 04:17:45 UTC',resetsAt=1792874445,TOTAL_ceiling=90,reserve=True,automatic_later_window=False)))
 print(json.dumps(dict(freeze=fp(P+'freeze-v1.json'))))
def verify():
 before=fp(P+'freeze-v1.json');f=read(P+'freeze-v1.json');verify_base();labels()
 for v in f['payloads']:check(v)
 assert fp(P+'freeze-v1.json')==before
 print(json.dumps(dict(SEPARATE_readonly_verify_UTC=now(),PASS=True,ENTIRE_files=6,ALL_obligations=16,freeze=before,writes=0,mathematical_code_executed=False)))
if __name__=='__main__':{'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
