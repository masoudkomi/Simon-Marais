"""NEW review documentary byte/JSON checks only. No mathematics or old execution."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
R=Path.cwd();P='problems/2024-B4/reviews/reasoning-frobenius-return-r10-review-1-'
A='problems/2024-B4/notes/reasoning-frobenius-return-r10-'
def now():return datetime.now(timezone.utc).isoformat()
def obj(p):return json.loads((R/p).read_text())
def rec(p):
 b=(R/p).read_bytes();return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def dig(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def write(s,x):
 p=R/(P+s);assert not p.exists(),p;p.write_text(json.dumps(x,indent=2)+'\n')
def declared(x):
 out=[]
 if isinstance(x,dict):
  if isinstance(x.get('path'),str)and isinstance(x.get('bytes'),int)and isinstance(x.get('sha256'),str)and len(x['sha256'])==64:
   out.append({k:x[k]for k in ['path','bytes','sha256']})
  for v in x.values():out+=declared(v)
 elif isinstance(x,list):
  for v in x:out+=declared(v)
 return out
def check(rows):
 for r in rows:
  assert not Path(r['path']).is_absolute()and'..'not in Path(r['path']).parts
  assert rec(r['path'])==r,r['path']
def guards(direct,bindings):
 check(direct);rows=list(direct)
 for b in bindings:
  check([b['metadata']]);own=declared(obj(b['metadata']['path']));check(own)
  assert len(own)==b['occurrences']and dig(own)==b['records_digest']
  rows+=own
 unique={}
 for r in rows:
  assert unique.setdefault(r['path'],r)==r
 ordered=[unique[p]for p in sorted(unique)]
 return len(rows),len(ordered),dig(ordered)
def ledger():
 return sum(1 for l in(R/(P+'report-v1.md')).read_text().splitlines()if l.startswith('|')and l[1:3].isdigit())
def prepare():
 freeze=A+'freeze-v1.json';fr=obj(freeze);check(fr['payload_records'])
 assert rec(freeze)['sha256']=='226beec7d86256e4daed124fb3686be8b798aa75b0638aaabef6eaf7df500f65'
 assert fr['ENTIRE_files_including_this_freeze']==13 and ledger()==64
 direct=[rec(freeze)]+fr['payload_records']
 direct +=[rec(p)for p in ['AGENTS.md','problems/2024-B4/statement.md',
 'problems/2024-B4/proofs/reviewed-reasoning-cofactor-return-r6-v1.1.md',
 'problems/2024-B4/reviews/reasoning-cofactor-return-r6-acceptance.md',
 'problems/2024-B4/reviews/reasoning-cofactor-return-r6-acceptance.json',
 'problems/2024-B4/proofs/reviewed-reasoning-cofactor-return-r9-v1.1.md',
 'problems/2024-B4/reviews/reasoning-cofactor-return-r9-acceptance.md',
 'problems/2024-B4/reviews/reasoning-cofactor-return-r9-acceptance.json']]
 parents=[A+'baseline-v1.json']+[r['path']for r in obj(A+'baseline-v1.json')['immutable_parent_metadata']]
 bindings=[]
 for p in parents:
  rows=declared(obj(p));check(rows);bindings.append(dict(metadata=rec(p),occurrences=len(rows),records_digest=dig(rows)))
 count,unique,digest=guards(direct,bindings)
 write('baseline-v1.json',dict(created_at_utc=now(),direct=direct,immutable_bindings=bindings,
  fingerprint_occurrences=count,unique_paths=unique,unique_records_digest=digest,
  administrative_only=True,no_recursive_unread_historical_content_claim=True,
  corresponding_NEW_review2_access=False))
 print(json.dumps(dict(action='prepare',PASS=True,fingerprint_occurrences=count,unique_paths=unique,whole_obligations=ledger())))
def validate():
 b=obj(P+'baseline-v1.json');c,u,d=guards(b['direct'],b['immutable_bindings'])
 assert(c,u,d)==(b['fingerprint_occurrences'],b['unique_paths'],b['unique_records_digest'])and ledger()==64
 return b
def freeze():
 b=validate();rows=[rec(P+s)for s in ['report-v1.md','admin-v1.py','baseline-v1.json']]
 write('manifest-v1.json',dict(frozen_at_utc=now(),status='initial whole review; EMBARGO until explicit BOTH ENTIRE',
  payloads=rows,ENTIRE_files=4,whole_obligations=64,reviewer='/root',constructor_excluded=True,
  independent_dispositions=64,unresolved_substantive_defects=0,required_repair=False,closed_scope_notes=8,
  fingerprint_occurrences=b['fingerprint_occurrences'],unique_paths=b['unique_paths'],
  FULL_final_payload_model_readback='actually completed before this freeze',
  full_manifest_readback_then_SEPARATE_verify_required=True,corresponding_NEW_review2_access=False))
 print(json.dumps(dict(action='freeze',record=rec(P+'manifest-v1.json'),ENTIRE=4,whole_obligations=64)))
def verify():
 b=validate();m=obj(P+'manifest-v1.json');check(m['payloads'])
 print(json.dumps(dict(action='SEPARATE read-only verify',verified_at_utc=now(),PASS=True,ENTIRE=4,whole_obligations=64,
  fingerprint_occurrences=b['fingerprint_occurrences'],unique_paths=b['unique_paths'],manifest=rec(P+'manifest-v1.json'))))
if __name__=='__main__':
 assert len(sys.argv)==2 and sys.argv[1]in('prepare','freeze','verify')
 {'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
