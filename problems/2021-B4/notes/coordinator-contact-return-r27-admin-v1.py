"""NEW R27 documentary bytes/JSON/literal labels ONLY; no mathematics.
Exclusive new baseline/freeze; separate readonly verify. No old executable.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P='problems/2021-B4/notes/coordinator-contact-return-r27-'
PAYLOADS=[P+s for s in ['candidate-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]
BASE=P+'baseline-v1.json';FREEZE=P+'freeze-v1.json'
PARENT='problems/2021-B4/notes/coordinator-dyadic-return-r26-freeze-v1.json'
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads((ROOT/p).read_text())
def fp(p):
 b=(ROOT/p).read_bytes();return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(r):assert fp(r['path'])==r,r['path']
def new(p,v):
 assert p.startswith(P)
 with(ROOT/p).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
def labels():
 s=(ROOT/PAYLOADS[0]).read_text();assert re.findall(r'^\|O(\d\d)\|',s,re.M)==[f'{i:02}'for i in range(1,33)]
 assert read(PAYLOADS[1])['whole_obligations']==32
 return 32
def prepare():
 paths=['AGENTS.md','problems/2021-B4/statement.md',P+'exploration-unverified.md']
 for stem in ['reasoning-deep-return-r24','coordinator-dyadic-return-r26']:
  js='problems/2021-B4/reviews/'+stem+'-acceptance.json';a=read(js)
  assert a['status']=='proved, independently reviewed scoped partial result';check(a['accepted_copy'])
  paths +=[a['accepted_copy']['path'],js[:-4]+'md',js]
 paths.append(PARENT);assert len(paths)==len(set(paths));labels()
 new(BASE,dict(created_UTC=now(),status='candidate proof - unverified',necessary_immutable_records=[fp(p)for p in paths],guard_occurrences=len(paths),guard_unique_paths=len(paths),compact_own_parent=fp(PARENT),parent_inventory_NOT_expanded=True,living_map_guards=False,new_R27_peer_access=False,requested=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),effective_readback=None,quota=dict(usedPercent=83,observed_UTC='2026-10-19 02:41:34 UTC',resetsAt=1792874445,TOTAL_ceiling=90,reserve=True,automatic_later_window=False),mathematical_truth_checked_by_code=False))
 print(json.dumps(dict(prepared=fp(BASE),guards=len(paths))))
def freeze():
 assert '--FULL-final-ALL4-MODEL-readbacks-completed' in sys.argv
 b=read(BASE)
 for r in b['necessary_immutable_records']:check(r)
 labels();new(FREEZE,dict(frozen_UTC=now(),status='candidate proof - unverified',constructor='/root',constructor_excluded=True,claims=['R27A','R27B'],ENTIRE_files=5,whole_obligations=32,payloads=[fp(p)for p in PAYLOADS],guard_occurrences=b['guard_occurrences'],guard_unique_paths=b['guard_unique_paths'],compact_own_parent=b['compact_own_parent'],FULL_final_ALL4_payload_MODEL_readbacks_completed=True,FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED=True,TWO_OTHER_initially_blind_ENTIRE_whole_audits_required=True,new_R27_peer_access=False,no_mathematical_code_or_old_replay=True))
 print(json.dumps(dict(freeze=fp(FREEZE))))
def verify():
 f=read(FREEZE);b=read(BASE)
 for r in f['payloads']+b['necessary_immutable_records']:check(r)
 assert f['ENTIRE_files']==len(f['payloads'])+1==5 and f['whole_obligations']==labels()==32
 print(json.dumps(dict(SEPARATE_readonly_verify_UTC=now(),result='PASS',ENTIRE_files=5,literal_obligations=32,freeze=fp(FREEZE),writes=0,mathematics_certified=False)))
if __name__=='__main__':
 assert len(sys.argv)>=2 and sys.argv[1]in ['prepare','freeze','verify']
 {'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
