#!/usr/bin/env python3
"""R18 whole OTHER R2 byte preservation only, never mathematical proof."""
import argparse,hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
PRE='problems/2021-B4/reviews/reasoning-center-return-r18-review-2-'
AUTHOR='problems/2021-B4/notes/reasoning-center-return-r18-'
MAN=AUTHOR+'freeze-v1.json'
EXPECTED={'path':MAN,'bytes':8034,'sha256':'14a572167f6ea76658d87a61c951b94f111adc437555f7388b7b0cf47b2829be'}
NAMES=('reasoning-center-return-r17','reasoning-return-r8','reasoning-return-r5')
FORBIDDEN='problems/2021-B4/reviews/reasoning-center-return-r18-review-1-'
PAYLOADS=('report-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md',
 'sources-v1.json','worklog-v1.md','freeze-v1.py','baseline-v1.json',
 'metadata-v1.json','input-validation-v1.json')
def now():return datetime.now(timezone.utc).isoformat()
def raw(p):
 assert isinstance(p,str) and not p.startswith('/') and '..' not in Path(p).parts
 assert not p.startswith(FORBIDDEN),p
 return(ROOT/p).read_bytes()
def obj(p):return json.loads(raw(p))
def fp(p):
 b=raw(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(row):
 expected={k:row[k]for k in ('path','bytes','sha256')}
 assert fp(row['path'])==expected,row['path']
 return expected
def put(s,o):
 assert s in ('baseline-v1.json','metadata-v1.json','input-validation-v1.json','manifest-v1.json')
 with(ROOT/(PRE+s)).open('x',encoding='utf-8')as f:json.dump(o,f,indent=2,ensure_ascii=False);f.write('\n')
def inputs():
 rows=[check(EXPECTED)];a=obj(MAN)
 assert a['whole_obligations']==64 and len(a['payloads'])==13
 for row in a['payloads']:
  assert row['path'].startswith(AUTHOR);rows.append(check(row))
 bindings=[]
 for name in NAMES:
  path='problems/2021-B4/reviews/'+name+'-acceptance.json';v=obj(path)
  assert v['status'].startswith('proved, independently reviewed')
  body,candidate=v['accepted_copy'],v['candidate']
  rows += [fp(path),fp(path[:-5]+'.md'),check(body),check(candidate)]
  assert raw(body['path']).endswith(raw(candidate['path']))
  bindings.append(dict(authority=path,accepted_body=body,candidate_suffix=candidate,
   historical_occurrences_NOT_recursively_replayed=v['record_occurrences_verified'],
   historical_paths_NOT_recursively_replayed=v['unique_paths_verified']))
 rows += [fp('AGENTS.md'),fp('problems/2021-B4/statement.md')]
 assert len(rows)==len({x['path']for x in rows})==28
 return sorted(rows,key=lambda x:x['path']),bindings
def labels():
 s=raw(PRE+'ledger-v1.md').decode()
 assert [int(x)for x in re.findall(r'(?m)^(\d+)\. PASS',s)]==list(range(1,65))
 v=obj(PRE+'sources-v1.json')
 assert v['whole_obligations']==64 and v['constructor_excluded'] is True
 assert v['root_NEW_construction_contribution'] is False
 assert v['no_corresponding_NEW_B_R18_finding_file_hash_or_metadata_accessed'] is True
 assert all('R18'+i in raw(PRE+'report-v1.md').decode()for i in ('A','B','C'))
def baseline():
 rows,bindings=inputs();labels()
 put('baseline-v1.json',dict(created_at_utc=now(),purpose='R18 OTHER whole R2 integrity only',
  protected_paths=28,fingerprints=rows,current_accepted_bindings=bindings,
  no_recursive_historical_or_mutable_guard_replay=True,
  corresponding_NEW_peer_prefix_never_opened_or_hashed=FORBIDDEN))
 print(json.dumps(dict(baseline=fp(PRE+'baseline-v1.json'),protected_paths=28)))
def preserved():
 v=obj(PRE+'baseline-v1.json');rows,bindings=inputs();labels()
 assert rows==v['fingerprints'] and bindings==v['current_accepted_bindings']
def freeze():
 preserved()
 put('metadata-v1.json',dict(created_at_utc=now(),role='OTHER initially blind ENTIRE whole review2',
  reviewer='/root',constructor='/root/review_2021_reasoning_j15_r2',constructor_excluded=True,
  root_NEW_construction_contribution=False,whole_obligations_reconstructed=64,
  substantive_defects=0,required_mathematical_author_repairs=0,closed_scope_notes=7,
  no_corresponding_NEW_peer_finding_file_hash_or_metadata_accessed=True,
  requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),
  independently_verified_effective_settings=None,metadata_only_NOT_mathematical_proof=True))
 put('input-validation-v1.json',dict(verified_at_utc=now(),ENTIRE_author_14_hashes_checked=True,
  current_accepted_body_candidate_suffix_MD_JSON_bindings_checked=3,protected_paths=28,
  ALL64_ordered_review_labels_present=True,no_NEW_peer_access_or_hash=True,
  no_math_source_author_or_old_freezer_execution=True,
  FULL_readback_and_SEPARATE_verify_required_before_handoff=True))
 artifacts=[fp(PRE+s)for s in PAYLOADS]
 put('manifest-v1.json',dict(frozen_at_utc=now(),status='initially blind OTHER whole review, not acceptance',
  whole_checkpoint='ENTIRE R18A-R18C ALL64/report/ledger/issues/sources/log/code/ALLmetadata',
  reviewer='/root',constructor_excluded=True,root_NEW_construction_contribution=False,
  whole_obligations=64,substantive_defects=0,required_mathematical_author_repairs=0,
  closed_scope_notes=7,no_corresponding_NEW_peer_access_or_hash=True,
  BOTH_entire_initials_required_before_findings_release=True,protected_paths=28,artifacts=artifacts))
 print(json.dumps(dict(manifest=fp(PRE+'manifest-v1.json'),files=11,report=artifacts[0],whole_obligations=64)))
def verify():
 preserved();v=obj(PRE+'manifest-v1.json')
 assert v['whole_obligations']==64
 assert [x['path']for x in v['artifacts']]==[PRE+s for s in PAYLOADS]
 for row in v['artifacts']:check(row)
 print(json.dumps(dict(separate_postverify='pass',files=11,whole_obligations=64,protected_paths=28,
  manifest=fp(PRE+'manifest-v1.json'),report=v['artifacts'][0],no_NEW_peer_read_or_hash=True)))
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('mode',choices=('baseline','freeze','verify'))
 mode=parser.parse_args().mode;dict(baseline=baseline,freeze=freeze,verify=verify)[mode]()
