#!/usr/bin/env python3
"""Freeze R2's blind report, after rechecking immutable candidate artifacts."""
import hashlib
import json
from pathlib import Path
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PREFIX='J16-digits-review-2'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
full=json.loads((HERE/(PREFIX+'-artifact-full-result.json')).read_text())
for path,a in full['integrity_after']['files'].items():
    p=ROOT/path
    assert p.stat().st_size==a['bytes'] and sha(p)==a['sha256'],path
freeze=json.loads((HERE/(PREFIX+'-predata-freeze.json')).read_text())
for a in freeze['files']:
    assert sha(ROOT/a['path'])==a['sha256'],a['path']
files=[]
for p in sorted(HERE.glob(PREFIX+'*')):
    if p.is_file() and p.name!=PREFIX+'-manifest.json':
        files.append({'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)})
result={
 'utc_frozen':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
 'status':'initial blind independent R2 audit frozen; no unresolved substantive objection; coordinator promotion only after two whole audits',
 'scope':'rational degree20 J=16 exclusion L1-L4 only',
 'requested_settings':{'model':'gpt-6.1-sol','reasoning':'max'},
 'effective_setting_readback':None,
 'peer_J16_output_read':False,
 'constructor_code_data_opened_after_predata_freeze':True,
 'all_113_candidate_artifacts_unchanged_at_final_freeze':True,
 'weekly_total_used_percent':13,
 'weekly_resets_at':1792745187,
 'artifact_count':len(files),'artifacts':files,
 'candidate_manifests':full['integrity_after']['manifests'],
 'source_version_binding':{
  'artifact_attempt1':PREFIX+'-artifact-audit-attempt1.py',
  'artifact_benchmark':PREFIX+'-artifact-audit-benchmark-v1.py',
  'artifact_full':PREFIX+'-artifact-audit.py',
  'metadata_v1':PREFIX+'-metadata-audit-v1.py',
  'metadata_final':PREFIX+'-metadata-audit.py'},
 'operational_note':'First inline final-freeze command used a relative parent root and failed before writing manifest; corrected by this absolute __file__ root discovery. No candidate or frozen mathematical source changed.'}
path=HERE/(PREFIX+'-manifest.json')
path.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'manifest':str(path),'sha256':sha(path),'artifact_count':len(files),
                 'bytes':sum(a['bytes'] for a in files),
                 'report_sha256':sha(HERE/(PREFIX+'.md')),
                 'issues_sha256':sha(HERE/(PREFIX+'-issues.md')),
                 'utc_frozen':result['utc_frozen']},indent=2),flush=True)
