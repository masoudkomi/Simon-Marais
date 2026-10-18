"""NEW RC10 WHOLE2 documentary freeze; no mathematical code or old replay."""
from pathlib import Path
import datetime,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
STEM='reasoning-collision-return-r10-review-2-'
MANIFEST=HERE/(STEM+'manifest-v1.json')
PAYLOADS=[HERE/(STEM+s)for s in ('report-v1.md','sources-v1.json','admin-v1.py')]
AUTHOR=ROOT/'problems/2022-B4/notes/reasoning-collision-return-r10-freeze-v1.json'
def fp(p):
 b=p.read_bytes();return dict(path=str(p.relative_to(ROOT)),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(row):
 assert not row['path'].startswith('problems/2022-B4/reviews/reasoning-collision-return-r10-review-1-')
 assert fp(ROOT/row['path'])==row,row['path']
def inputs():
 a=json.loads(AUTHOR.read_text())
 for row in a['payloads']:check(row)
 paths=[AUTHOR]+[ROOT/x['path']for x in a['payloads']]+[ROOT/'AGENTS.md',ROOT/'problems/2022-B4/statement.md']
 paths.append(ROOT/'problems/2022-B4/proofs/reviewed-reasoning-dynamics-return-r9-v1.1.md')
 for stem in ('reasoning-dynamics-return-r9','reasoning-dynamics-return-r7','rational-base-shadow-return','reasoning-return-r8'):
  for ext in ('md','json'):paths.append(ROOT/f'problems/2022-B4/reviews/{stem}-acceptance.{ext}')
 return [fp(p)for p in paths]
if sys.argv[1:]==['freeze']:
 assert not MANIFEST.exists()
 s=json.loads(PAYLOADS[1].read_text());assert not s['corresponding_NEW_peer_findings_files_actualinventory_hash_metadata_accessed']
 v=dict(frozen_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),reviewer='/root',role='OTHER initially blind WHOLE2',whole_obligations=60,ENTIRE_files=4,payloads=[fp(p)for p in PAYLOADS],inputs=inputs(),FULL_final_ALL3_payload_model_readback_completed=True,FULL_manifest_model_readback_then_SEPARATE_verify_required=True,NEW_peer_findings_files_actual_inventory_hash_metadata_accessed=False,substantive_defects_repair_required=False,all_60_issues_sources_log_code_metadata_complete=True,mathematical_program_CAS_scan_test_old_replay=False)
 MANIFEST.write_text(json.dumps(v,indent=2)+'\n');print(json.dumps(fp(MANIFEST)))
elif sys.argv[1:]==['verify']:
 v=json.loads(MANIFEST.read_text())
 for row in v['payloads']+v['inputs']:check(row)
 assert inputs()==v['inputs']
 print(json.dumps(dict(separate_verify_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),status='PASS',ENTIRE_files=4,whole_obligations=60,manifest=fp(MANIFEST))))
else:raise SystemExit('freeze or verify only; documentary checks')
