"""NEW documentary bytes/JSON/literal-label helper, not mathematical code.
No peer inventory, source/author/old executable, subprocess, network or Git.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2025-B4/notes/reasoning-joint-trace-return-r13-'
PAYLOADS=[P+s for s in ['candidate-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]
BASE=P+'baseline-v1.json';FREEZE=P+'freeze-v1.json'
PARENT='problems/2021-B4/reviews/coordinator-contact-return-r27-review-2-manifest-v1.json'
STEMS=['reasoning-exception-return-r12','reasoning-compatible-return-r10','reasoning-global-return-r11']
def now():return datetime.now(timezone.utc).isoformat()
def read(rel):return json.loads((ROOT/rel).read_text())
def fp(rel):
 b=(ROOT/rel).read_bytes();return dict(path=rel,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(record):assert fp(record['path'])==record,record['path']
def new(rel,value):
 assert rel in [BASE,FREEZE]
 with(ROOT/rel).open('x')as out:out.write(json.dumps(value,indent=2,ensure_ascii=False)+'\n')
def labels():
 text=(ROOT/PAYLOADS[0]).read_text()
 for i in range(1,33):assert text.count(f'|JT13-{i:02d}|')==1
 assert read(PAYLOADS[1])['whole_obligations']==32
 return 32
def prepare():
 paths=['AGENTS.md','problems/2025-B4/statement.md']
 for stem in STEMS:
  auth='problems/2025-B4/reviews/'+stem+'-acceptance.json';value=read(auth)
  assert value['status']=='proved, independently reviewed scoped partial result'
  check(value['accepted_copy']);paths += [value['accepted_copy']['path'],auth[:-4]+'md',auth]
 paths.append(PARENT);assert len(paths)==len(set(paths))==12
 parent=fp(PARENT)
 assert parent['bytes']==2134 and parent['sha256']=='8ba9e8f4dc2812b4bfe44f714f8cfd43b96b3cd9123add1048c61ed7c2b3dcc0'
 labels();new(BASE,dict(captured_UTC=now(),necessary_immutable_records=[fp(r)for r in paths],guard_occurrences=12,guard_unique_paths=12,ONE_exact_OWN_parent=parent,recursive_inventory_expansion=False,living_map_guards=False,no_PH13_peer_access=True,mathematical_truth_checked_by_code=False))
 print(json.dumps(dict(baseline=fp(BASE),necessary_paths=12)))
def verify_base():
 b=read(BASE)
 for record in b['necessary_immutable_records']:check(record)
 return b
def freeze():
 assert '--FULL-final-ALL4-MODEL-readbacks-completed' in sys.argv
 b=verify_base();count=labels()
 new(FREEZE,dict(frozen_UTC=now(),status='candidate proof - unverified',constructor='/root/review_2022_complexity_r2',constructor_excluded=True,root_NEW_inference=False,claims=['JT1','JT2'],ENTIRE_files=5,ALL_obligations=count,payloads=[fp(p)for p in PAYLOADS],guard_occurrences=12,guard_unique_paths=12,ONE_exact_OWN_parent=b['ONE_exact_OWN_parent'],FULL_final_ALL4_payload_MODEL_readbacks_completed=True,FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED=True,TWO_OTHER_initially_blind_ENTIRE_whole_audits_required=True,new_exclusion_or_useful_height_improvement=False,no_PH13_peer_access=True,no_mathematical_executable_or_old_replay=True,requested=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),independent_effective_backend_readback=None,quota=dict(usedPercent=84,observed_UTC='2026-10-19 03:44:32 UTC',resetsAt=1792874445,TOTAL_ceiling=90,reserve=True,automatic_later_window=False)))
 print(json.dumps(dict(freeze=fp(FREEZE))))
def verify():
 before=fp(FREEZE);f=read(FREEZE);verify_base()
 for record in f['payloads']:check(record)
 assert f['ALL_obligations']==labels()==32 and f['ENTIRE_files']==5
 assert fp(FREEZE)==before
 print(json.dumps(dict(SEPARATE_readonly_verify_UTC=now(),status='PASS',ENTIRE_files=5,literal_obligations=32,necessary_paths=12,freeze=before,writes=0,mathematics_certified=False)))
if __name__=='__main__':
 assert len(sys.argv)>1 and sys.argv[1]in['prepare','freeze','verify']
 {'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
