from pathlib import Path
import datetime,hashlib,json,sys
root=Path.cwd();pre='problems/2020-B4/reviews/reasoning-class-return-sq16-review-1-'
forbidden='problems/2020-B4/reviews/reasoning-class-return-sq16-review-2-'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def rec(p):
 assert not p.startswith(forbidden)
 b=(root/p).read_bytes();return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def obj(p):
 assert not p.startswith(forbidden)
 return json.loads((root/p).read_text())
def put(s,x):
 with(root/(pre+s)).open('x')as f:json.dump(x,f,indent=2);f.write('\n')
def check(rs):
 for r in rs:assert rec(r['path'])==r,r['path']
def sumrows(rs):
 rs=sorted(rs,key=lambda r:r['path']);return dict(unique_paths=len(rs),canonical_sha256=hashlib.sha256(json.dumps(rs,sort_keys=True,separators=(',',':')).encode()).hexdigest())
mode=sys.argv[1]
if mode=='prepare':
 author='problems/2020-B4/notes/reasoning-class-return-sq16-freeze-v1.json'
 assert rec(author)==dict(path=author,bytes=4322,sha256='29ed9edd4cea75a4248b9661f06518649c97e122c437262c4c7dd32750847087')
 a=obj(author);rows=[rec(author)]+a['payloads']
 rows+=obj('problems/2020-B4/notes/reasoning-class-return-sq16-baseline-v1.json')['records']
 parent='problems/2017-B4/reviews/reasoning-pressure-return-r11-review-1-manifest-v1.json'
 rows+=[rec(parent)]+obj(parent)['payloads'];check(rows)
 d={}
 for r in rows:
  assert r['path']not in d or d[r['path']]==r
  d[r['path']]=r
 rows=[d[p]for p in sorted(d)]
 put('baseline-v1.json',dict(prepared_utc=now(),records=rows,summary=sumrows(rows),
  author_ENTIRE12_and_ALL48_read=True,author_code_ALLmetadata_read=True,
  whole_review_new_constructor=False,NEW_peer_access=False,old_inputs_read_scope='literal in whole report',
  own_parent_R11_ENTIRE5_is_preservation_only=True,requested=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),effective_readback=None))
 print(json.dumps(dict(prepare='PASS',summary=sumrows(rows))))
elif mode=='freeze':
 b=obj(pre+'baseline-v1.json');check(b['records'])
 s=(root/(pre+'initial-v1.md')).read_text();labels=[l.split('|')[1]for l in s.splitlines()if l.startswith('|SQ16-R1-')]
 assert labels==['SQ16-R1-'+str(i).zfill(2)for i in range(1,49)]
 payload=[rec(pre+s)for s in ['initial-v1.md','admin-v1.py','baseline-v1.json']]
 put('manifest-v1.json',dict(frozen_utc=now(),reviewer='/root',role='OTHER initially blind WHOLE1',ENTIRE_files=4,ALL_obligations=48,payloads=payload,
  FULL_final_ALL3_payload_model_readback_complete=True,FULL_manifest_readback_then_SEPARATE_verify_required=True,
  explicit_BOTH_before_NEW_peer_findings_files_inventory_hash_metadata=True,NEW_peer_access=False,guard_summary=b['summary']))
 print(json.dumps(rec(pre+'manifest-v1.json')))
elif mode=='verify':
 m=obj(pre+'manifest-v1.json');check(m['payloads']);check(obj(pre+'baseline-v1.json')['records'])
 print(json.dumps(dict(SEPARATE_readonly_verify_utc=now(),PASS=True,ENTIRE_files=4,ALL_obligations=48,manifest=rec(pre+'manifest-v1.json'))))
else:raise ValueError(mode)
