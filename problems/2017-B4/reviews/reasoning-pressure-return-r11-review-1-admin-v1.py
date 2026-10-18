"""Compact NEW R11 root audit integrity; no mathematical instance evaluation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys

P='problems/2017-B4/reviews/reasoning-pressure-return-r11-review-1-'
A='problems/2017-B4/notes/reasoning-pressure-return-r11-'
AF=A+'freeze-v1.json'
PARENT='problems/2022-B4/reviews/reasoning-dynamics-return-r9-review-1-manifest-v1.json'
EXPECTED={AF:(3407,'041cd6fa331d5737b71b721247b3d7706ecdf88edd115c7387055b840d0fe5e3'),
          PARENT:(2777,'3bf00e1f339875118bce573bdc69fbdbafb7ae32620f6a053744fed75dbee027')}
SUFFIXES=['initial-v1.md','admin-v1.py','baseline-v1.json','input-validation-v1.json']

def now():return datetime.now(timezone.utc).isoformat()
def raw(p):
 assert not Path(p).is_absolute() and '..' not in Path(p).parts
 assert not p.startswith('problems/2017-B4/reviews/reasoning-pressure-return-r11-review-2-')
 return Path(p).read_bytes()
def obj(p):return json.loads(raw(p))
def rec(p):
 b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(r):
 r={k:r[k] for k in ['path','bytes','sha256']};assert rec(r['path'])==r,r['path'];return r
def put(s,x):
 with Path(P+s).open('x') as f:json.dump(x,f,indent=2);f.write('\n')
def summary(rows):
 u={}
 for r in rows:
  r=check(r)
  if r['path'] in u:assert u[r['path']]==r
  u[r['path']]=r
 order=[u[k] for k in sorted(u)]
 return dict(occurrences=len(rows),unique_paths=len(order),canonical_sha256=hashlib.sha256(json.dumps(order,sort_keys=True,separators=(',',':')).encode()).hexdigest())
def labels():
 t=raw(P+'initial-v1.md').decode()
 assert re.findall(r'^\|R11-(\d{2})\|',t,re.M)==['%02d'%i for i in range(1,65)]
 return 64
def inputs():
 for p,(n,h) in EXPECTED.items():check(dict(path=p,bytes=n,sha256=h))
 a=obj(AF);assert len(a['payloads'])+1==a['ENTIRE_files']==13
 author=[rec(AF)]+[check(r) for r in a['payloads']]
 b=obj(A+'baseline-v1.json');guards=[check(r) for r in b['records']]
 assert len(guards)==28
 par=obj(PARENT);own=[rec(PARENT)]+[check(r) for r in par['payloads']]
 assert len(own)==11
 records=[rec(AF),rec(A+'baseline-v1.json'),rec(PARENT)]
 return dict(direct_bindings=records,author_ENTIRE13=summary(author),author_direct28=summary(guards),
             own_D9_parent_ENTIRE11=summary(own),combined=summary(author+guards+own),
             historical_inventories_recopied=False,new_R11_peer_access=False)
def prepare():
 x=inputs();assert labels()==64
 put('baseline-v1.json',dict(prepared_at_utc=now(),status='one OTHER initially blind whole audit, not acceptance',
     reviewer='/root',NEW_R11_constructor=False,older_WC_WO_PM9_root_constructor=True,
     older_inputs_independently_self_recertified=False,bindings=x,
     fresh_COMPLETE_body_and_EACH_current_authority_MDJSON=['WC','WO','PM8','PM9'],
     source_record=[
       dict(url='https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf',read='B4 extracted48--57'),
       dict(url='https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf',read='56--214 including161--164 exact fiber;313--322 operative rotation proof',whole12page_audit=False),
       dict(url='https://arxiv.org/pdf/2502.20909v2',read='149--457 including282--315 exact rotation/zone deduction',whole12page_or_new_optimizer_audit=False)],
     R10_body_read='historical prior audit/context only, not newly repeated full read',
     requested_model='gpt-6.1-sol',requested_reasoning='max',verified_effective_readback=None,
     authorized_reset=1792874445,TOTAL_ceiling=90,reserve=True,automatic_later_window=False,
     no_NEW_peer_findings_files_inventory_hash_metadata_commentary_access=True,
     audit_MD_embeds_ALL64_issues_sources_worklog=True,ENTIRE_files=5,
     no_mathematical_program_CAS_scan_test_or_old_replay=True))
 put('input-validation-v1.json',dict(validated_at_utc=now(),documentary_only=True,labels=64,
     bindings=x,all_explicit_declared_bytes_preserved=True,mathematical_validation_by_code=False))
 print(json.dumps(dict(prepared=True,ENTIRE_files=5,labels=64,protection=x['combined'])))
def validate():
 b=obj(P+'baseline-v1.json');assert inputs()==b['bindings'];assert labels()==64
 assert obj(P+'input-validation-v1.json')['bindings']==b['bindings']
 return b
def freeze():
 assert sys.argv[2:]==['--FULL-final-ALL4-payload-model-readback-complete']
 b=validate()
 put('manifest-v1.json',dict(frozen_at_utc=now(),status='OTHER initially blind ENTIRE WHOLE1, findings EMBARGOED',
     reviewer='/root',NEW_R11_constructor=False,ALL_obligations=64,ENTIRE_files=5,
     FULL_final_ALL4_payload_model_readback_complete=True,
     FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required=True,
     explicit_BOTH_required_before_NEW_peer_finding_file_inventory_hash_metadata_or_commentary=True,
     no_NEW_corresponding_peer_access=True,protection=b['bindings']['combined'],
     payloads=[rec(P+s) for s in SUFFIXES]))
 print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'),ENTIRE_files=5,ALL64=True)))
def verify():
 m=obj(P+'manifest-v1.json');assert len(m['payloads'])+1==5 and m['ALL_obligations']==64
 for r in m['payloads']:check(r)
 b=validate();assert m['protection']==b['bindings']['combined']
 print(json.dumps(dict(SEPARATE_readonly_verify='PASS',at_utc=now(),ENTIRE_files=5,ALL64=True,
     manifest=rec(P+'manifest-v1.json'),main=rec(P+'initial-v1.md'),no_write=True)))
if __name__=='__main__':
 assert len(sys.argv)>=2
 {'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
