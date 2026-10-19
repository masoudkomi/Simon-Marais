"""NEW R26 documentary bytes/JSON/literal-label binding ONLY.
No coefficient expansion or congruence test. No old/source/author helper replay.
Final ALL4 payload MODEL readbacks precede freeze; FULL freeze MODEL readback
precedes a separate readonly verify invocation. Writes exclusive new files.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P='problems/2021-B4/notes/coordinator-dyadic-return-r26-'
PAYLOADS=[P+s for s in ['candidate-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]
BASE=P+'baseline-v1.json';FREEZE=P+'freeze-v1.json'
PARENT='problems/2021-B4/notes/coordinator-dyadic-depth-return-r25-freeze-v1.json'
EXPECTED={'problems/2021-B4/proofs/reviewed-reasoning-deep-return-r24-v1.1.md':'a52fcb31da9b494659d29b1ea0b587baba3a096264688ac6989e3d98ed578946','problems/2021-B4/proofs/reviewed-coordinator-dyadic-depth-return-r25-v1.1.md':'311568bc5ded810dfa823efedd968e9c0f05eb0ff129856499babb6785064c2e'}
def now():return datetime.now(timezone.utc).isoformat()
def fp(rel):
 assert not Path(rel).is_absolute() and '..' not in Path(rel).parts
 data=(ROOT/rel).read_bytes();return dict(path=rel,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
def read(rel):return json.loads((ROOT/rel).read_text())
def check(row):assert fp(row['path'])==row,row['path']
def create(rel,value):
 assert rel.startswith(P)
 with(ROOT/rel).open('x')as f:json.dump(value,f,indent=2);f.write('\n')
def labels():
 text=(ROOT/PAYLOADS[0]).read_text();assert re.findall(r'^\|O(\d\d)\|',text,re.M)==[f'{i:02}'for i in range(1,33)]
 assert read(PAYLOADS[1])['whole_obligations']==32
 return32=32
 return return32

def prepare():
 paths=['AGENTS.md','problems/2021-B4/statement.md',P+'exploration-unverified.md']
 for stem in ['reasoning-deep-return-r24','coordinator-dyadic-depth-return-r25']:
  js='problems/2021-B4/reviews/'+stem+'-acceptance.json';md=js[:-4]+'md';a=read(js)
  assert a['status']=='proved, independently reviewed scoped partial result';check(a['accepted_copy']);assert a['accepted_copy']['sha256']==EXPECTED[a['accepted_copy']['path']]
  paths += [a['accepted_copy']['path'],md,js]
 parent=read(PARENT);assert parent['ENTIRE_files']==5
 rows=[fp(x)for x in paths]+[fp(PARENT)]+parent['payloads'];assert len({x['path']for x in rows})==len(rows)
 for r in rows:check(r)
 labels();create(BASE,dict(created_UTC=now(),status='candidate proof - unverified',necessary_immutable_records=rows,guard_occurrences=len(rows),guard_unique_paths=len(rows),compact_own_parent=fp(PARENT),historical_parent_inventory_expanded=False,living_map_guards=False,new_R26_peer_access=False,requested=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),independent_effective_backend_readback=None,weekly=dict(usedPercent=80,observed_UTC='2026-10-19 02:17:03 UTC',resetsAt=1792874445,TOTAL_ceiling=90,reserve=True,automatic_later_window=False),mathematical_truth_checked_by_code=False))
 print(json.dumps(dict(prepared=fp(BASE),guards=len(rows))))
def freeze():
 b=read(BASE)
 for r in b['necessary_immutable_records']:check(r)
 labels();create(FREEZE,dict(frozen_UTC=now(),status='candidate proof - unverified',constructor='/root',constructor_excluded=True,TWO_OTHER_initially_blind_ENTIRE_whole_audits_required=True,ENTIRE_files=5,whole_obligations=32,payloads=[fp(x)for x in PAYLOADS],guard_occurrences=b['guard_occurrences'],guard_unique_paths=b['guard_unique_paths'],compact_own_parent=b['compact_own_parent'],FULL_final_ALL4_payload_MODEL_readbacks_completed=True,FULL_freeze_MODEL_readback_then_SEPARATE_readonly_verify_REQUIRED=True,new_R26_peer_access=False,no_mathematical_program_CAS_scan_test_oldreplay=True))
 print(json.dumps(dict(freeze=fp(FREEZE))))
def verify():
 f=read(FREEZE);b=read(BASE)
 for r in f['payloads']+b['necessary_immutable_records']:check(r)
 assert f['ENTIRE_files']==len(f['payloads'])+1==5 and labels()==f['whole_obligations']==32
 print(json.dumps(dict(SEPARATE_readonly_verify_UTC=now(),result='PASS',ENTIRE_files=5,literal_obligations=32,freeze=fp(FREEZE),writes=0,mathematical_truth_checked_by_code=False)))
if __name__=='__main__':
 assert len(sys.argv)==2 and sys.argv[1]in ['prepare','freeze','verify'];{'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
