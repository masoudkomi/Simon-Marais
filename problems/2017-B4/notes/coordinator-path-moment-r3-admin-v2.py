#!/usr/bin/env python3
"""PM9 v2 checklist-only snapshot; metadata checks, never mathematics."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
PRE='problems/2017-B4/notes/coordinator-path-moment-r3-'
OLD=dict(path=PRE+'freeze-v1.json',bytes=2896,sha256='d8afeae6a1bc2e73d89ee6773823fcbbba72491674aabaf3f60eabe0473f1ab7')
NEW=('obligations-v2.md','notation-note-v1.md','admin-v2.py')
def now():return datetime.now(timezone.utc).isoformat()
def raw(p):
 assert p=='AGENTS.md' or p.startswith('problems/2017-B4/')
 assert '..'not in Path(p).parts and not p.startswith('/')
 return(ROOT/p).read_bytes()
def fp(p):
 b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def obj(p):return json.loads(raw(p))
def check(x):
 y={k:x[k]for k in('path','bytes','sha256')};assert fp(x['path'])==y,x['path'];return y
def inputs():
 check(OLD);v=obj(OLD['path']);assert len(v['payloads'])==11 and v['whole_obligations']==48
 rows=[check(x)for x in v['payloads']]+[check(OLD)]
 b=obj(PRE+'baseline-v1.json');assert len(b['fingerprints'])==21
 for x in b['fingerprints']:check(x)
 ids=re.findall(r'(?m)^\| PM9-(\d{2}) \|',raw(PRE+'obligations-v2.md').decode())
 assert ids==[f'{i:02d}'for i in range(1,49)]
 rows += [fp(PRE+s)for s in NEW]
 assert len(rows)==len({x['path']for x in rows})==15
 return rows
def freeze():
 rows=inputs();v=dict(frozen_at_utc=now(),status='ENTIRE operative PM9 v2 checklist snapshot; candidate proof - unverified',constructor='/root',constructor_excluded_from_TWO_OTHER_whole_audits=True,whole_obligations=48,ENTIRE_files_including_freeze=16,all12_original_frozen_files_preserved=True,main_mathematical_body_changed=False,operative_obligation_checklist=PRE+'obligations-v2.md',correction_scope='Explicit punctuation in all48 checklist rows; unchanged candidate mathematical body; before first review handoff.',TWO_OTHER_initially_blind_ENTIRE_WHOLE_reviews_and_full_root_reconciliation_required=True,FULL_final_model_readback_ALL16_then_SEPARATE_verify_required=True,mathematical_computation=False,old_freeze=OLD,payloads=rows)
 with(ROOT/(PRE+'freeze-v2.json')).open('x')as f:json.dump(v,f,indent=2);f.write('\n')
 print(json.dumps(dict(freeze=fp(PRE+'freeze-v2.json'),main=fp(PRE+'candidate-v1.md'),ENTIRE_files=16,whole_obligations=48)))
def verify():
 rows=inputs();v=obj(PRE+'freeze-v2.json');assert v['payloads']==rows and v['ENTIRE_files_including_freeze']==16
 print(json.dumps(dict(SEPARATE_postfreeze_verify='PASS',at_utc=now(),freeze=fp(PRE+'freeze-v2.json'),main=fp(PRE+'candidate-v1.md'),ENTIRE_files=16,whole_obligations=48,all12_original_files_unchanged=True,administrative_not_proof=True)))
if __name__=='__main__':dict(freeze=freeze,verify=verify)[sys.argv[1]]()
