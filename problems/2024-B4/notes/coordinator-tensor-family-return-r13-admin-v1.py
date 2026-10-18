"""NEW R13 documentary byte binding only. No mathematical calculation."""
from pathlib import Path
import datetime,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
PREFIX='problems/2024-B4/notes/coordinator-tensor-family-return-r13-'
INPUTS=['AGENTS.md','problems/2024-B4/statement.md',
 'problems/2024-B4/proofs/reviewed-coordinator-tensor-return-r12-v1.1.md',
 'problems/2024-B4/reviews/coordinator-tensor-return-r12-acceptance.md',
 'problems/2024-B4/reviews/coordinator-tensor-return-r12-acceptance.json',
 'problems/2024-B4/proofs/reviewed-reasoning-frobenius-return-r10-v1.1.md',
 'problems/2024-B4/reviews/reasoning-frobenius-return-r10-acceptance.md',
 'problems/2024-B4/reviews/reasoning-frobenius-return-r10-acceptance.json',
 PREFIX+'exploration-v0.md']
PAYLOADS=[PREFIX+s for s in ('candidate-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json')]
BASELINE=ROOT/(PREFIX+'baseline-v1.json')
FREEZE=ROOT/(PREFIX+'freeze-v1.json')
def record(path):
 b=(ROOT/path).read_bytes()
 return {'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def verify(rows):
 for old in rows:
  assert record(old['path'])==old,old['path']
mode=sys.argv[1]
if mode=='baseline':
 assert not BASELINE.exists() and not FREEZE.exists()
 rows=[record(p)for p in INPUTS]
 BASELINE.write_text(json.dumps({'created_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
  'input_records':rows,'necessary_paths_only':True,'mathematical_code':False,
  'NEW_constructor':'/root','conceptual_trigger_excluded':'/root/review_2017_coarsening_r1',
  'requested_model':'inherited gpt-6.1-sol','requested_reasoning':'inherited max',
  'effective_setting_independent_readback':None,'all_old_bytes_must_remain':True},indent=2)+'\n')
 print('baseline created; final FULL model readback still required')
elif mode=='freeze':
 assert BASELINE.exists() and not FREEZE.exists()
 verify(json.loads(BASELINE.read_text())['input_records'])
 rows=[record(p)for p in PAYLOADS]
 FREEZE.write_text(json.dumps({'frozen_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
  'status':'candidate proof - unverified','whole_obligations':32,'payloads':rows,
  'FULL_final_payload_model_readback_required_before_freeze':True,
  'FULL_manifest_model_readback_then_SEPARATE_verify_required':True,
  'two_OTHER_initially_blind_ENTIRE_whole_audits_required':True,
  'NEW_contributors_excluded':['/root','/root/review_2017_coarsening_r1'],
  'mathematical_program_or_old_replay':False},indent=2)+'\n')
 print(json.dumps(record(PREFIX+'freeze-v1.json')))
elif mode=='verify':
 manifest=json.loads(FREEZE.read_text())
 verify(json.loads(BASELINE.read_text())['input_records']);verify(manifest['payloads'])
 print(json.dumps({'separate_read_only_verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
  'input_records':len(INPUTS),'payloads':len(PAYLOADS),'all_match':True,
  'freeze':record(PREFIX+'freeze-v1.json')}))
else:
 raise SystemExit('baseline|freeze|verify only')
