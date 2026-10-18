"""New R18 root WHOLE1 documentary bytes/labels only, no mathematics."""
from pathlib import Path
import datetime,hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2020-B4/reviews/reasoning-actual-return-r18-review-1-'
A='problems/2020-B4/notes/reasoning-actual-return-r18-'
PAYLOADS=[P+s for s in ('report-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json')]
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def read(path):
 assert 'reasoning-actual-return-r18-review-2-' not in path
 assert not path.startswith('/') and '..' not in Path(path).parts
 return ROOT/path
def rec(path):
 b=read(path).read_bytes()
 return {'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(rows):
 for r in rows:assert rec(r['path'])==r,r['path']
def js(path):return json.loads(read(path).read_text())
def fresh(path,obj):
 assert path.startswith(P)
 with read(path).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
def inputs():
 freeze=js(A+'freeze-v1.json')
 assert rec(A+'freeze-v1.json')=={'path':A+'freeze-v1.json','bytes':2747,'sha256':'564db489529aa7030df95abbd6461fe82a5e1acf32d4499838f3472c6ae7e9be'}
 verify(freeze['payload_records'])
 direct=js(A+'baseline-v1.json')['direct_current_guard_records']
 verify(direct)
 return freeze['payload_records']+[rec(A+'freeze-v1.json')]+direct
def labels():
 s=read(P+'report-v1.md').read_text()
 assert re.findall(r'^\|(AR18-\d\d)\|PASS',s,re.M)==[f'AR18-{i:02d}'for i in range(1,65)]
 assert re.findall(r'^\|R18R1-N(\d+)\|CLOSED\|',s,re.M)==[str(i)for i in range(1,11)]
mode=sys.argv[1]
if mode=='baseline':
 labels();rows=inputs()
 fresh(P+'baseline-v1.json',{'created_at_utc':now(),'input_records':rows,
  'purpose':'necessary immutable author payloads and direct current input bytes; not source-reading evidence',
  'new_constructor':False,'reviewer':'/root','role':'OTHER initially blind ENTIRE WHOLE1',
  'whole_obligations':64,'closed_scope_notes':10,
  'corresponding_NEW_peer_findings_files_actual_inventory_hash_metadata_accessed':False,
  'requested_model':'inherited gpt-6.1-sol','requested_reasoning':'inherited max','effective_readback':None,
  'mathematical_program_or_old_replay':False})
 print({'baseline_created':True,'input_records':len(rows)})
elif mode=='freeze':
 baseline=js(P+'baseline-v1.json');verify(baseline['input_records']);assert inputs()==baseline['input_records'];labels()
 fresh(P+'manifest-v1.json',{'frozen_at_utc':now(),'reviewer':'/root','role':'OTHER initially blind ENTIRE WHOLE1',
  'whole_obligations':64,'ENTIRE_files':5,'payloads':[rec(p)for p in PAYLOADS],
  'FULL_final_ALL4_payload_model_readback_completed':True,
  'FULL_manifest_MODEL_readback_then_SEPARATE_verify_required':True,
  'corresponding_NEW_peer_findings_files_actual_inventory_hash_metadata_accessed':False,
  'findings_embargo_until_explicit_BOTH_ENTIRE':True,'mathematical_program_or_old_replay':False})
 print(rec(P+'manifest-v1.json'))
elif mode=='verify':
 manifest=js(P+'manifest-v1.json');verify(manifest['payloads']);verify(js(P+'baseline-v1.json')['input_records']);labels()
 print({'separate_readonly_verified_at_utc':now(),'all_match':True,'manifest':rec(P+'manifest-v1.json')})
else:raise SystemExit('baseline|freeze|verify only')
