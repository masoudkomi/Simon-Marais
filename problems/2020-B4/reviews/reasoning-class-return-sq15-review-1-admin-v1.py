"""NEW SQ15 review1 exclusive byte/JSON/label administration; no math."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2020-B4/reviews/reasoning-class-return-sq15-review-1-'
A='problems/2020-B4/notes/reasoning-class-return-sq15-'
PARENT='problems/2021-B4/reviews/reasoning-center-return-r20-review-1-manifest-v1.json'
STEMS=['reasoning-arithmetic-return-r14','reasoning-return-r8','reasoning-Todd-return-r12']
STATIC=['report-v1.md','ledger-v1.md','issues-v1.md','sources-v1.md','sources-v1.json','worklog-v1.md','admin-v1.py']
GENERATED=['baseline-v1.json','input-validation-v1.json','metadata-v1.json']
def now():return datetime.now(timezone.utc).isoformat()
def path(p):
 assert not Path(p).is_absolute() and '..' not in Path(p).parts
 assert not p.startswith('problems/2020-B4/reviews/reasoning-class-return-sq15-review-2-')
 return ROOT/p
def fp(p):
 b=path(p).read_bytes();return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def obj(p):return json.loads(path(p).read_text())
def check(r):assert fp(r['path'])=={k:r[k] for k in ['path','bytes','sha256']},r['path']
def put(s,v):
 with path(P+s).open('x') as f:json.dump(v,f,indent=2);f.write('\n')
def snap():
 check(dict(path=A+'candidate-v1.md',bytes=20209,sha256='11182beb9e08841d8ecce07008caafe93ca65222fdd34937493bf9a4c9715e78'))
 check(dict(path=A+'freeze-v1.json',bytes=3677,sha256='bc7bb2ef06d6e90dc083841fac5853209b7a45e36bc0ae5b16e512efa7c94975'))
 check(dict(path=PARENT,bytes=2623,sha256='4872dae3dee517ee88c0d22e2dac43e00f1c51577e56113bb994b0163edf2847'))
 author=obj(A+'freeze-v1.json');assert author['ENTIRE_files']==13 and author['whole_obligations']==48
 rows=[fp(A+'freeze-v1.json')]
 for row in author['payloads']:check(row);rows.append(fp(row['path']))
 rows.extend(fp(p) for p in ['AGENTS.md','problems/2020-B4/statement.md',PARENT,
  'problems/2020-B4/notes/reasoning-arithmetic-return-r14-sources-v1.md',
  'problems/2020-B4/notes/reasoning-arithmetic-return-r14-failed-routes-v1.md',
  'problems/2020-B4/notes/reasoning-Todd-return-r12-sources-v1.md'])
 for stem in STEMS:
  authority='problems/2020-B4/reviews/'+stem+'-acceptance.json';v=obj(authority)
  assert v['unresolved_substantive_issues']==0
  check(v['accepted_copy']);check(v['candidate'])
  assert path(v['accepted_copy']['path']).read_bytes().endswith(path(v['candidate']['path']).read_bytes())
  rows.extend([fp(authority),fp(authority[:-4]+'md'),fp(v['accepted_copy']['path']),fp(v['candidate']['path'])])
 for p in [A+'obligations-v1.md',P+'ledger-v1.md']:
  ids=re.findall(r'(?m)^\|SQ15-(\d{2})\|',path(p).read_text());assert ids==[f'{i:02d}' for i in range(1,49)]
 unique={r['path']:r for r in rows};ordered=[unique[p] for p in sorted(unique)]
 return dict(fingerprints=ordered,record_occurrences=len(rows),unique_paths=len(ordered),all13_author_bound=True,all48_labels=True,accepted_three_suffixes_verified=True,own_immediate_parent_only_no_recursive_expansion=fp(PARENT),administration_only=True)
def prepare():
 s=snap()
 for suffix in STATIC:fp(P+suffix)
 put('baseline-v1.json',dict(at_utc=now(),**s))
 put('input-validation-v1.json',dict(at_utc=now(),result='PASS',whole_obligations=48,record_occurrences=s['record_occurrences'],unique_paths=s['unique_paths'],administration_only=True))
 put('metadata-v1.json',dict(at_utc=now(),reviewer='/root',C_constructor_excluded=True,whole_obligations=48,ENTIRE_files=11,no_NEW_corresponding_peer_SQ15_filename_finding_file_hash_metadata_commentary_access=True,FULL_final_ALL11_readback_then_SEPARATE_verify_required=True,requested_inherited=dict(model='gpt-6.1-sol',reasoning='max'),independent_effective_readback=None,authorized_reset_only=1792874445,TOTAL_ceiling=90,integration_reserve=True,no_mathcode_or_old_replay=True))
 print(json.dumps(dict(prepare='PASS',record_occurrences=s['record_occurrences'],unique_paths=s['unique_paths'])))
def validate():
 s=snap();b=obj(P+'baseline-v1.json');assert all(b[k]==v for k,v in s.items());return s
def freeze():
 s=validate();put('manifest-v1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind OTHER WHOLE1;findings embargoed',whole_obligations=48,ENTIRE_files=11,FULL_final_ALL10_payload_model_readback_complete=True,FULL_manifest_readback_then_SEPARATE_verify_required=True,explicit_BOTH_required_before_NEW_peer_access_or_release=True,no_NEW_corresponding_peer_filename_finding_file_hash_metadata_commentary_access=True,record_occurrences=s['record_occurrences'],unique_paths=s['unique_paths'],payloads=[fp(P+p) for p in STATIC+GENERATED]));print(json.dumps(dict(freeze=fp(P+'manifest-v1.json'))))
def verify():
 s=validate();m=obj(P+'manifest-v1.json');assert m['whole_obligations']==48 and len(m['payloads'])==10
 for r in m['payloads']:check(r)
 print(json.dumps(dict(SEPARATE_readonly_verify='PASS',at_utc=now(),ENTIRE_files=11,whole_obligations=48,record_occurrences=s['record_occurrences'],unique_paths=s['unique_paths'],manifest=fp(P+'manifest-v1.json'),report=fp(P+'report-v1.md')),indent=2))
if __name__=='__main__':
 mode=sys.argv[1] if len(sys.argv)==2 else '';assert mode in ['prepare','freeze','verify'];dict(prepare=prepare,freeze=freeze,verify=verify)[mode]()
