"""NEW documentary exact SHA/JSON/literal-row helper, not mathematics.
Author code NEVER executed; no old replay/network/subprocess/Git/peer scan.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2022-B4/reviews/reasoning-physical-return-r13-review-2-'
PAYLOADS=[P+s for s in ['initial-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]
BASE=P+'baseline-v1.json';MANIFEST=P+'manifest-v1.json'
AUTHOR='problems/2022-B4/notes/reasoning-physical-return-r13-freeze-v1.json'
PARENT='problems/2025-B4/notes/reasoning-joint-trace-return-r13-freeze-v1.json'
STEMS=['reasoning-itinerary-return-r12','reasoning-dynamics-return-r9','reasoning-fiber-return-r5']
def now():return datetime.now(timezone.utc).isoformat()
def fp(rel):
 b=(ROOT/rel).read_bytes();return dict(path=rel,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(rel):return json.loads((ROOT/rel).read_text())
def check(record):assert fp(record['path'])==record,record['path']
def new(rel,value):
 assert rel in [BASE,MANIFEST]
 with(ROOT/rel).open('x')as out:out.write(json.dumps(value,indent=2,ensure_ascii=False)+'\n')
def labels():
 s=(ROOT/PAYLOADS[0]).read_text()
 for i in range(1,33):assert s.count(f'|PH13R2-{i:02d}|')==1
 assert read(PAYLOADS[1])['ALL_obligations']==32
 return 32
def prepare():
 a=fp(AUTHOR)
 assert a['bytes']==2526 and a['sha256']=='256bedd300fa0ce8ebe1ee1f69d47e1246a7c5c2c50f802e6d3d2d2ce5e6c1c6'
 author=read(AUTHOR)
 assert author['ENTIRE_files']==5 and author['ALL_obligations']==32
 for record in author['payloads']:check(record)
 paths=['AGENTS.md','problems/2022-B4/statement.md',AUTHOR]+[r['path']for r in author['payloads']]
 for stem in STEMS:
  js='problems/2022-B4/reviews/'+stem+'-acceptance.json';value=read(js)
  assert value['status']=='proved, independently reviewed scoped partial result'
  check(value['accepted_copy']);paths +=[value['accepted_copy']['path'],js[:-4]+'md',js]
 paths.append(PARENT);assert len(paths)==len(set(paths))==17
 parent=fp(PARENT)
 assert parent['bytes']==2115 and parent['sha256']=='c797b85ac45ac25e2c8155a62c2d768f721538650d97c925dcd1210502a22075'
 labels();new(BASE,dict(captured_UTC=now(),necessary_immutable_records=[fp(p)for p in paths],guard_occurrences=17,guard_unique_paths=17,ONE_exact_OWN_parent=parent,recursive_inventory_expansion=False,living_map_guards=False,corresponding_NEW_PH13_peer_access=False,mathematics_checked_by_code=False))
 print(json.dumps(dict(baseline=fp(BASE),necessary_paths=17)))
def check_base():
 b=read(BASE)
 for record in b['necessary_immutable_records']:check(record)
 return b
def freeze():
 assert '--FULL-final-ALL4-MODEL-readbacks-completed' in sys.argv
 b=check_base();count=labels()
 new(MANIFEST,dict(frozen_UTC=now(),status='sealed OTHER independent WHOLE2 initial; not promotion',reviewer='/root/review_2022_complexity_r2',constructor_excluded=True,claims=['PH13A','PH13B','PH13C','PH13D'],ENTIRE_files=5,ALL_obligations=count,payloads=[fp(p)for p in PAYLOADS],guard_occurrences=17,guard_unique_paths=17,ONE_exact_OWN_parent=b['ONE_exact_OWN_parent'],FULL_final_ALL4_payload_MODEL_readbacks_completed=True,FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED=True,findings_sealed_until_explicit_BOTH=True,corresponding_NEW_peer_access=False,no_mathematical_executable_or_old_replay=True,requested=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),independent_effective_backend_readback=None,quota=dict(usedPercent=85,observed_UTC='2026-10-19 03:48:10 UTC',resetsAt=1792874445,TOTAL_ceiling=90,reserve=True,automatic_later_window=False)))
 print(json.dumps(dict(manifest=fp(MANIFEST))))
def verify():
 before=fp(MANIFEST);f=read(MANIFEST);check_base()
 for record in f['payloads']:check(record)
 assert f['ALL_obligations']==labels()==32 and f['ENTIRE_files']==5
 assert fp(MANIFEST)==before
 print(json.dumps(dict(SEPARATE_readonly_verify_UTC=now(),status='PASS',ENTIRE_files=5,literal_obligations=32,necessary_paths=17,manifest=before,writes=0,mathematics_certified=False)))
if __name__=='__main__':
 assert len(sys.argv)>1 and sys.argv[1]in['prepare','freeze','verify']
 {'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
