"""NEW R10 review1 exclusive byte/JSON/label administration; no math."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2017-B4/reviews/reasoning-path-mass-return-r10-review-1-'
A='problems/2017-B4/notes/reasoning-path-mass-return-r10-'
PARENT='problems/2025-B4/reviews/reasoning-diagonal-return-r7-review-1-manifest-v1.json'
STEMS=['coordinator-path-moment-r3','allD-global']
STATIC=['report-v1.md','ledger-v1.md','issues-v1.md','sources-v1.md','sources-v1.json','worklog-v1.md','admin-v1.py']
GENERATED=['baseline-v1.json','input-validation-v1.json','metadata-v1.json']
def now():return datetime.now(timezone.utc).isoformat()
def path(p):
 assert not Path(p).is_absolute() and '..' not in Path(p).parts
 for banned in ['problems/2017-B4/reviews/reasoning-path-mass-return-r10-review-2-','problems/2025-B4/reviews/reasoning-diagonal-return-r7-review-2-','problems/2020-B4/reviews/reasoning-class-return-sq15-review-2-']:assert not p.startswith(banned)
 return ROOT/p
def fp(p):
 b=path(p).read_bytes();return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def obj(p):return json.loads(path(p).read_text())
def check(r):assert fp(r['path'])=={k:r[k] for k in ['path','bytes','sha256']},r['path']
def put(s,v):
 with path(P+s).open('x') as f:json.dump(v,f,indent=2);f.write('\n')
def snap():
 check(dict(path=A+'candidate-v1.md',bytes=19791,sha256='a66251ca92893c795fe2f7b83bc63d9b435df38675b0dafd9ff7556e133b4a2b'))
 check(dict(path=A+'freeze-v1.json',bytes=4859,sha256='8eaf21309963d0c7d6b12aa3be03e957989d598bb13dd1fea6d4979ab33d5441'))
 check(dict(path=PARENT,bytes=2652,sha256='0a51df9b44a5fe2ca77be5c5acd77b0ba56786897c648aca9506d512faec7729'))
 author=obj(A+'freeze-v1.json');assert author['ENTIRE_files_including_freeze']==11 and author['whole_obligations']==60
 rows=[fp(A+'freeze-v1.json')]
 for row in author['payloads']:check(row);rows.append(fp(row['path']))
 rows.extend(fp(p) for p in ['AGENTS.md','problems/2017-B4/statement.md',PARENT])
 for stem in STEMS:
  authority='problems/2017-B4/reviews/'+stem+'-acceptance.json';v=obj(authority)
  assert v['unresolved_substantive_issues']==0
  check(v['accepted_copy']);check(v['candidate'])
  assert path(v['accepted_copy']['path']).read_bytes().endswith(path(v['candidate']['path']).read_bytes())
  rows.extend([fp(authority),fp(authority[:-4]+'md'),fp(v['accepted_copy']['path']),fp(v['candidate']['path'])])
 dc='problems/2017-B4/reviews/coarsening-acceptance.json';v=obj(dc);assert v['unresolved_substantive_objections_to_accepted_claims']==0;check(v['accepted_proof'])
 rows.extend([fp(dc),fp(dc[:-4]+'md'),fp(v['accepted_proof']['path'])])
 ids=re.findall(r'(?m)^(O\d{2})\.',path(A+'obligations-v1.md').read_text());assert ids==[f'O{i:02d}' for i in range(1,61)]
 ids=re.findall(r'(?m)^(O\d{2}) — PASS',path(P+'ledger-v1.md').read_text());assert ids==[f'O{i:02d}' for i in range(1,61)]
 unique={r['path']:r for r in rows};ordered=[unique[p] for p in sorted(unique)]
 return dict(fingerprints=ordered,record_occurrences=len(rows),unique_paths=len(ordered),all11_author_bound=True,all60_labels=True,two_accepted_suffixes_and_DC_exposition_verified=True,own_immediate_parent_only_no_recursive_expansion=fp(PARENT),administration_only=True)
def prepare():
 s=snap()
 for suffix in STATIC:fp(P+suffix)
 put('baseline-v1.json',dict(at_utc=now(),**s))
 put('input-validation-v1.json',dict(at_utc=now(),result='PASS',whole_obligations=60,record_occurrences=s['record_occurrences'],unique_paths=s['unique_paths'],administration_only=True))
 put('metadata-v1.json',dict(at_utc=now(),reviewer='/root',B_constructor_excluded=True,whole_obligations=60,ENTIRE_files=11,no_NEW_corresponding_peer_R10_filename_finding_file_hash_metadata_commentary_access=True,FULL_final_ALL11_readback_then_SEPARATE_verify_required=True,requested_inherited=dict(model='gpt-6.1-sol',reasoning='max'),independent_effective_readback=None,authorized_reset_only=1792874445,TOTAL_ceiling=90,integration_reserve=True,no_mathcode_or_old_replay=True))
 print(json.dumps(dict(prepare='PASS',record_occurrences=s['record_occurrences'],unique_paths=s['unique_paths'])))
def validate():
 s=snap();b=obj(P+'baseline-v1.json');assert all(b[k]==v for k,v in s.items());return s
def freeze():
 s=validate();put('manifest-v1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind OTHER WHOLE1;findings embargoed',whole_obligations=60,ENTIRE_files=11,FULL_final_ALL10_payload_model_readback_complete=True,FULL_manifest_readback_then_SEPARATE_verify_required=True,explicit_BOTH_required_before_NEW_peer_access_or_release=True,no_NEW_corresponding_peer_filename_finding_file_hash_metadata_commentary_access=True,record_occurrences=s['record_occurrences'],unique_paths=s['unique_paths'],payloads=[fp(P+p) for p in STATIC+GENERATED]));print(json.dumps(dict(freeze=fp(P+'manifest-v1.json'))))
def verify():
 s=validate();m=obj(P+'manifest-v1.json');assert m['whole_obligations']==60 and len(m['payloads'])==10
 for r in m['payloads']:check(r)
 print(json.dumps(dict(SEPARATE_readonly_verify='PASS',at_utc=now(),ENTIRE_files=11,whole_obligations=60,record_occurrences=s['record_occurrences'],unique_paths=s['unique_paths'],manifest=fp(P+'manifest-v1.json'),report=fp(P+'report-v1.md')),indent=2))
if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)==2 else '';assert mode in ['prepare','freeze','verify'];dict(prepare=prepare,freeze=freeze,verify=verify)[mode]()
