#!/usr/bin/env python3
"""NEW R25 documentary integrity only; never mathematical computation.
prepare creates the exact five necessary immutable input bindings.
freeze requires prior FULL final ALL4 MODEL readbacks; FULL manifest
MODEL readback precedes a SEPARATE read-only verify invocation.
"""
from pathlib import Path
import datetime,hashlib,json,re,sys
ROOT=Path.cwd()
P='problems/2021-B4/notes/coordinator-dyadic-depth-return-r25-'
INPUTS=['AGENTS.md','problems/2021-B4/statement.md',
 'problems/2021-B4/proofs/reviewed-reasoning-deep-return-r24-v1.1.md',
 'problems/2021-B4/reviews/reasoning-deep-return-r24-acceptance.md',
 'problems/2021-B4/reviews/reasoning-deep-return-r24-acceptance.json']
FILES=[P+s for s in ['candidate-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def fp(p):
 assert not p.startswith('/') and '..' not in Path(p).parts
 b=(ROOT/p).read_bytes();return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(p):return json.loads((ROOT/p).read_text())
def check(r):assert fp(r['path'])==r,r['path']
def new(p,o):
 assert p.startswith(P)
 with (ROOT/p).open('x') as f:json.dump(o,f,indent=2);f.write(chr(10))
def validate():
 b=read(P+'baseline-v1.json')
 for r in b['necessary_immutable_records']:check(r)
 assert [line.split('|')[1].strip() for line in (ROOT/FILES[0]).read_text().splitlines() if line.startswith('| O')]==['O%02d'%i for i in range(1,29)]
 read(FILES[1]);return b
mode=sys.argv[1]
if mode=='prepare':
 new(P+'baseline-v1.json',dict(created_UTC=now(),constructor='/root',status='candidate proof - unverified',whole_obligations=28,necessary_immutable_records=[fp(p) for p in INPUTS],historical_parent_inventory_not_expanded=True,current_mutable_maps_not_immutable_guards=True,TWO_OTHER_initially_blind_whole_audits_required=True,constructor_excluded=True,mathematical_computation=False,quota=dict(usedPercent=76,observed_UTC='2026-10-19 00:48:00 UTC',resetsAt=1792874445,TOTAL_ceiling=90,reserve=True,automatic_later_window=False)))
 print(json.dumps(dict(prepared=True,baseline=fp(P+'baseline-v1.json'))))
elif mode=='freeze':
 assert '--FULL-final-ALL4-model-readbacks-complete' in sys.argv
 validate()
 new(P+'freeze-v1.json',dict(frozen_UTC=now(),status='candidate proof - unverified',constructor='/root',claims=['R25A','R25B attributed consequence'],whole_obligations=28,ENTIRE_files=5,payloads=[fp(p) for p in FILES],FULL_final_ALL4_MODEL_readbacks_complete=True,FULL_manifest_MODEL_readback_then_SEPARATE_verify_required=True,TWO_OTHER_whole_audits_required=True,constructor_excluded=True,mathematical_computation=False,unrelated_NEW_peer_access=False))
 print(json.dumps(dict(frozen=True,manifest=fp(P+'freeze-v1.json'))))
elif mode=='verify':
 m=read(P+'freeze-v1.json')
 assert fp(P+'freeze-v1.json')['sha256']==sys.argv[2]
 for r in m['payloads']:check(r)
 validate()
 print(json.dumps(dict(verified_UTC=now(),result='PASS',manifest=fp(P+'freeze-v1.json'),ENTIRE_files=5,whole_obligations=28,writes=0,mathematical_computation=False)))
else:raise ValueError(mode)
