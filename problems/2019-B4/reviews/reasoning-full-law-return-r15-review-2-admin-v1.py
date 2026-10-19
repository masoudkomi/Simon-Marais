"""NEW documentary-only record preparation/seal/verify. No mathematical inference.
Run prepare once, seal only AFTER FULL final payload MODEL readbacks,
then FULL manifest MODEL readback and a SEPARATE verify invocation.
Only this review prefix can be created; all guard access is read-only.
No historical executable is imported or replayed; no peer is inventoried.
"""
from pathlib import Path
import hashlib, json, sys
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'problems/2019-B4/reviews'
P='reasoning-full-law-return-r15-review-2-'
AUTHOR=ROOT/'problems/2019-B4/notes/reasoning-full-law-return-r15-freeze-v1.json'
PARENT=ROOT/'problems/2022-B4/reviews/reasoning-critical-return-r11-review-1-manifest-v1.json'
def rec(p):
 b=p.read_bytes(); return {'path':str(p.relative_to(ROOT)), 'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def check(r):
 got=rec(ROOT/r['path'])
 assert got=={k:r[k] for k in ('path','bytes','sha256')},r['path']
def write(name,v):
 with (BASE/(P+name)).open('x') as f: f.write(json.dumps(v,indent=2)+'\n')
def summary(rows):
 d={}
 for r in rows:
  if r['path'] in d: assert d[r['path']]==r
  d[r['path']]=r
 canonical=[d[k] for k in sorted(d)]
 return {'occurrences':len(rows),'unique_paths':len(d),'canonical_deduplicated_sha256':hashlib.sha256(json.dumps(canonical,sort_keys=True,separators=(',',':')).encode()).hexdigest()}
def guard_rows():
 author=json.loads(AUTHOR.read_text()); parent=json.loads(PARENT.read_text())
 rows=[rec(AUTHOR)]+author['payload_records']+[rec(PARENT)]+parent['payload_records']
 baseline=ROOT/'problems/2019-B4/notes/reasoning-full-law-return-r15-baseline-v1.json'
 declared=json.loads(baseline.read_text())['immutable_guard_records']
 # These literal old author guards are admitted, not NEW corresponding peer rows.
 for r in declared: check(r)
 for r in declared:
  if r['path'].startswith('problems/2019-B4/') or r['path']=='AGENTS.md': rows.append(r)
 for r in rows: check(r)
 return rows,declared
mode=sys.argv[1]
if mode=='prepare':
 rows,declared=guard_rows()
 write('baseline-v1.json',{'created_utc':datetime.now(timezone.utc).isoformat(),'documentary_only':True,'immutable_guard_records':rows,'direct_guard_summary':summary(rows),'author_declared_guard_summary':summary(declared),'own_parent':rec(PARENT),'own_parent_older_summary_transitively_bound_NOT_replayed':json.loads(PARENT.read_text())['direct_guard_summary'],'historical_ancestry_traversed':False,'corresponding_NEW_peer_access':False,'mutable_maps_guarded':False})
elif mode=='seal':
 baseline=json.loads((BASE/(P+'baseline-v1.json')).read_text())
 for r in baseline['immutable_guard_records']:check(r)
 payload=[rec(BASE/(P+n)) for n in ('initial-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json')]
 write('manifest-v1.json',{'frozen_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root','NEW_constructor':'/root/review_2017_coarsening_r1','constructor_excluded':True,'ENTIRE_files':5,'whole_obligations':48,'initially_blind':True,'payload_records':payload,'direct_guard_summary':baseline['direct_guard_summary'],'author_declared_guard_summary':baseline['author_declared_guard_summary'],'FULL_final_MODEL_ALL4_payload_readback_completed':True,'FULL_manifest_MODEL_readback_then_SEPARATE_readonly_verify_required':True,'corresponding_NEW_peer_findings_files_actual_inventory_hash_metadata_access':False,'findings_sealed_until_explicit_BOTH':True})
elif mode=='verify':
 manifest=json.loads((BASE/(P+'manifest-v1.json')).read_text())
 baseline=json.loads((BASE/(P+'baseline-v1.json')).read_text())
 for r in manifest['payload_records']+baseline['immutable_guard_records']:check(r)
 _,declared=guard_rows()
 assert manifest['direct_guard_summary']==summary(baseline['immutable_guard_records'])
 assert manifest['author_declared_guard_summary']==summary(declared)
 assert manifest['whole_obligations']==48
 print(json.dumps({'verified_utc':datetime.now(timezone.utc).isoformat(),'read_only':True,'ENTIRE_files':5,'whole_obligations_label':48,'status':'PASS documentary identity only','guard_occurrences':len(baseline['immutable_guard_records']),'corresponding_NEW_peer_access':False}))
else: raise ValueError(mode)
