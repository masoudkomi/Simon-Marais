#!/usr/bin/env python3
"""Freeze this initially blind R1 audit without reading any peer material."""
import hashlib
import json
import time
from pathlib import Path

here=Path(__file__).resolve().parent
root=here.parents[2]
prefix='thirdpass-review-1'
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

author_path=root/'problems/2019-B4/notes/thirdpass-v1-manifest.json'
author=json.loads(author_path.read_text())
assert sha(author_path)=='ed672a1a68874ea44c2c4752dad7f1f7ef5e27e496ed4cf40d4f633cc2364b6b'
assert len(author['files'])==70
for row in author['files']:
    p=root/row['path']
    assert sha(p)==row['sha256'] and p.stat().st_size==row['bytes'],row['path']
hashlist=root/'problems/2019-B4/notes/thirdpass-v1-sha256.txt'
listed={line.split('  ',1)[1]:line.split('  ',1)[0] for line in hashlist.read_text().splitlines()}
assert listed=={row['path']:row['sha256'] for row in author['files']}
for label in ('before','after'):
    frozen=json.loads((here/f'{prefix}-{label}-freeze.json').read_text())
    assert frozen['all_match'] and frozen['file_count']==70
    assert frozen['manifest_sha256']==sha(author_path)

exclude={f'{prefix}-manifest.json',f'{prefix}-sha256.txt'}
files=[]
for p in sorted(here.glob(prefix+'*')):
    if p.is_file() and p.name not in exclude:
        files.append({'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':sha(p)})
report=here/f'{prefix}.md'
manifest={'status':'initial blind independent R1 review frozen; coordinator promotion pending',
          'reviewer':'review_2019_thirdpass_r1',
          'frozen_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
          'peer_thirdpass_conclusions_read_before_freeze':False,
          'requested_settings':{'model':'gpt-6.1-sol','reasoning':'max'},
          'effective_settings_independent_readback':None,
          'author_manifest_sha256':sha(author_path),'author_manifest_all_70_match_now':True,
          'author_companion_hash_list_sha256':sha(hashlist),'author_companion_hash_list_all_70_match':True,
          'initial_report_sha256':sha(report),'file_count':len(files),'files':files,
          'exclusions':'This manifest and its companion hash list are excluded to avoid self-reference.'}
target=here/f'{prefix}-manifest.json'
target.write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
(here/f'{prefix}-sha256.txt').write_text(''.join(row['sha256']+'  '+row['path']+'\n' for row in files))
print(json.dumps({'initial_report_sha256':sha(report),'review_manifest_sha256':sha(target),
                  'review_file_count':len(files),'author_files_all_70_match':True,
                  'frozen_utc':manifest['frozen_utc']}))
