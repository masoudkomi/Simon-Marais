"""NEW documentary identity only; prepare/seal/SEPARATE verify.
No mathematical program or historical executable is run or imported.
Full final payload MODEL reads must precede seal; full manifest MODEL
read must precede separate verify and corresponding NEW peer access.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'problems/2020-B4/reviews'
P='reasoning-realization-return-r19-review-1-'
AUTHOR=ROOT/'problems/2020-B4/notes/reasoning-realization-return-r19-freeze-v1.json'
AB=ROOT/'problems/2020-B4/notes/reasoning-realization-return-r19-baseline-v1.json'
PARENT=ROOT/'problems/2019-B4/reviews/reasoning-full-law-return-r15-review-2-manifest-v1.json'
def record(p):
 b=p.read_bytes();return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def check(r):assert record(ROOT/r['path'])=={k:r[k]for k in ('path','bytes','sha256')},r['path']
def summary(rows):
 d={}
 for r in rows:
  if r['path']in d:assert d[r['path']]==r
  d[r['path']]=r
 return {'occurrences':len(rows),'unique_paths':len(d),'canonical_deduplicated_sha256':hashlib.sha256(json.dumps([d[k]for k in sorted(d)],sort_keys=True,separators=(',',':')).encode()).hexdigest()}
def save(name,data):
 with (BASE/(P+name)).open('x')as f:f.write(json.dumps(data,indent=2)+'\n')
def guards():
 a=json.loads(AUTHOR.read_text());old=json.loads(PARENT.read_text());ab=json.loads(AB.read_text())
 rows=[record(AUTHOR)]+a['payload_records']+[record(PARENT)]+old['payload_records']+ab['direct_guard_records']
 for r in rows:check(r)
 return rows,ab['direct_guard_summary']
mode=sys.argv[1]
if mode=='prepare':
 rows,author_summary=guards()
 save('baseline-v1.json',{'created_utc':datetime.now(timezone.utc).isoformat(),'documentary_only':True,'immutable_guard_records':rows,'direct_guard_summary':summary(rows),'author_declared_guard_summary':author_summary,'own_parent':record(PARENT),'own_parent_older_summary_transitively_bound_NOT_replayed':json.loads(PARENT.read_text())['direct_guard_summary'],'corresponding_NEW_peer_access':False,'historical_ancestry_traversed':False,'mutable_maps_guarded':False})
elif mode=='seal':
 b=json.loads((BASE/(P+'baseline-v1.json')).read_text())
 for r in b['immutable_guard_records']:check(r)
 rows=[record(BASE/(P+n))for n in ('initial-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json')]
 save('manifest-v1.json',{'frozen_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root','constructor':'/root/review_2022_complexity_r2','constructor_excluded':True,'ENTIRE_files':5,'whole_obligations':48,'initially_blind':True,'payload_records':rows,'direct_guard_summary':b['direct_guard_summary'],'author_declared_guard_summary':b['author_declared_guard_summary'],'FULL_final_MODEL_ALL4_payload_readback_completed':True,'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required':True,'corresponding_NEW_peer_findings_files_actual_inventory_hash_metadata_access':False,'findings_sealed_until_explicit_BOTH':True})
elif mode=='verify':
 m=json.loads((BASE/(P+'manifest-v1.json')).read_text());b=json.loads((BASE/(P+'baseline-v1.json')).read_text())
 for r in m['payload_records']+b['immutable_guard_records']:check(r)
 rows,a=guards();assert summary(rows)==m['direct_guard_summary'];assert a==m['author_declared_guard_summary']
 print(json.dumps({'verified_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS documentary identity only','read_only':True,'ENTIRE_files':5,'whole_obligations_label':48,'direct_guard_occurrences':len(rows),'corresponding_NEW_peer_access':False}))
else:raise ValueError(mode)
