#!/usr/bin/env python3
"""Freeze initial blind review artifacts without touching unrelated files."""
import datetime
import hashlib
import json
import pathlib

here = pathlib.Path(__file__).resolve().parent
root = here.parents[2]
manifest_path = here/'thirdpass-review-2-manifest.json'
assert not manifest_path.exists(), 'Initial blind manifest is immutable; use an addendum.'
files = []
for path in sorted(here.glob('thirdpass-review-2*')):
    if path == manifest_path or not path.is_file():
        continue
    data = path.read_bytes()
    files.append({'path': str(path.relative_to(root)), 'bytes': len(data),
                  'sha256': hashlib.sha256(data).hexdigest()})
candidate = root/'problems/2019-B4/notes/thirdpass-bounded-separation-v1.md'
source_manifest = root/'problems/2019-B4/notes/thirdpass-v1-manifest.json'
out = {'status': 'initial independent blind review and issue record frozen; no promotion',
       'frozen_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'reviewer': '/root/review_2019_thirdpass_r2',
       'requested_model': 'gpt-6.1-sol', 'requested_reasoning_effort': 'max',
       'effective_settings_readback': None, 'peer_report_contents_read_before_freeze': False,
       'candidate_sha256': hashlib.sha256(candidate.read_bytes()).hexdigest(),
       'source_manifest_sha256': hashlib.sha256(source_manifest.read_bytes()).hexdigest(),
       'unresolved_substantive_issues': 0, 'files': files}
manifest_path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'manifest': str(manifest_path), 'sha256': hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
                  'files': len(files), 'frozen_utc': out['frozen_utc']}))
