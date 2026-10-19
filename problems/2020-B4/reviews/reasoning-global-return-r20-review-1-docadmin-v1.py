#!/usr/bin/env python3
"""NEW documentary-only R20 review admin. No mathematical computation.

init: one-time exact guard baseline, binding ONE OWN parent only.
freeze: only after final ALL4 payload MODEL readbacks.
verify: separate read-only check after FULL manifest MODEL readback.
No author/old helper imports, mathematical operations, scans, or peer access.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2020-B4/reviews/reasoning-global-return-r20-review-1-'
NAMES = ['initial-v1.md', 'sources-v1.json', 'docadmin-v1.py', 'baseline-v1.json']
BASE = ROOT / (PREFIX + 'baseline-v1.json')
MANIFEST = ROOT / (PREFIX + 'manifest-v1.json')
PARENT = 'problems/2017-B4/notes/reasoning-joint-mass-return-r16-freeze-v1.json'
EXPECTED = [
 ('AGENTS.md',4707,'28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'),
 ('problems/2020-B4/statement.md',2006,'91c9e7e86eef7bc6a68770f6ee730d18618443304ac3aace5541b42170ac64cc'),
 ('problems/2020-B4/notes/reasoning-global-return-r20-candidate-v1.md',24526,'f424c011ac4c397898b39e2488e736728a73b57fcda5d60adaa0f348c0c2e71a'),
 ('problems/2020-B4/notes/reasoning-global-return-r20-sources-v1.json',5157,'a1c69242d744832e2faacfc2d4ae2255a1d66b26f38e24239e5e3fda193f11b5'),
 ('problems/2020-B4/notes/reasoning-global-return-r20-admin-v1.py',12134,'927dac809decf82edeed2fb5ef8d0296ed80d97b71a6e11a6c72b8126b94652e'),
 ('problems/2020-B4/notes/reasoning-global-return-r20-baseline-v1.json',3487,'5489a344fd6d6ffeef050d858c621e5683c7b8e28bcd29add62e949f85ef158a'),
 ('problems/2020-B4/notes/reasoning-global-return-r20-freeze-v1.json',1776,'ba2ea31635915d211efac6fc28024e6fefebe0f07e59df7eca31c6a52c831664'),
 ('problems/2020-B4/proofs/reviewed-reasoning-actual-return-r18-v1.1.md',43966,'f38609238baaa9909dfd7655220794a89bf7e00a5f128253d56167507f2d48cf'),
 ('problems/2020-B4/reviews/reasoning-actual-return-r18-acceptance.md',7410,'6a13746486597ada30dc1d0212292c51f6c74274c1b1eb2e45f50fb7b8a870e5'),
 ('problems/2020-B4/reviews/reasoning-actual-return-r18-acceptance.json',3719,'cfab20bed65e85423975e628bf9c1231e769d46feb9b0fcb7d5abf6dd5e723bf'),
 ('problems/2020-B4/proofs/reviewed-reasoning-realization-return-r19-v1.1.md',36261,'1318589dd05ccf4b1a78e8200b87e9f77148eacbe27c485358a81a10698ef7a2'),
 ('problems/2020-B4/reviews/reasoning-realization-return-r19-acceptance.md',5074,'954bba83096cce29784ab34da06f1e8221aeb77a8a2a42d5f5c2b3f75a3ad753'),
 ('problems/2020-B4/reviews/reasoning-realization-return-r19-acceptance.json',3438,'8a9a598569c1605a6a5132e15e9552d5ca9326d6e7b271666c22451c7e7381c4'),
 (PARENT,2455,'487d92acc4bb6fe433b656473e487f88bcf17cf6341d9a15364ed6f9be3571ef')
]

def stamp():
    return datetime.now(timezone.utc).isoformat()

def record(path):
    data = (ROOT / path).read_bytes()
    return {'path':path, 'bytes':len(data), 'sha256':hashlib.sha256(data).hexdigest()}

def compact_digest(rows):
    canonical = json.dumps(sorted(rows,key=lambda x:x['path']),sort_keys=True,separators=(',',':')).encode()
    return hashlib.sha256(canonical).hexdigest()

def exact_guards():
    rows = []
    for path,size,digest in EXPECTED:
        row = record(path)
        assert row['bytes']==size and row['sha256']==digest, 'Changed guard: '+path
        rows.append(row)
    assert len(rows)==14 and len({r['path'] for r in rows})==14
    return rows

def exact_labels():
    text = (ROOT / (PREFIX+'initial-v1.md')).read_text()
    labels = re.findall(r'^\|(GR20-\d{2})\|',text,re.M)
    assert labels==['GR20-%02d'%i for i in range(1,41)], labels
    return len(labels)

mode = sys.argv[1] if len(sys.argv)>1 else ''
if mode=='init':
    assert not BASE.exists() and not MANIFEST.exists(), 'Refuse overwrite'
    rows=exact_guards()
    parent=json.loads((ROOT/PARENT).read_text())
    data={
      'schema':'R20-independent-review-compact-baseline-v1',
      'created_UTC':stamp(),
      'immutable_guards':rows,
      'guard_occurrences':14,
      'deduplicated_paths':14,
      'canonical_deduplicated_sha256':compact_digest(rows),
      'ONE_OWN_immediate_parent_manifest':record(PARENT),
      'parent_declared_summary':{'ENTIRE_files':parent['ENTIRE_files'],'ALL_obligations':parent['ALL_obligations'],'guard_occurrences':parent['guard_summary']['occurrences'],'guard_unique_paths':parent['guard_summary']['unique_paths']},
      'parent_payload_or_recursive_inventory_expansion':False,
      'mutable_research_map_snapshots_added_as_guards':False,
      'corresponding_NEW_R20_peer_access':False,
      'historical_CM16_identity_only_exposure':'Visible in unchanged author baseline; no actual peer file open/inventory/hash. Root confirmed prior BOTH release and acceptance; not an R20 premise.',
      'mathematical_executable_or_old_replay':False
    }
    BASE.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({'initialized':str(BASE.relative_to(ROOT)),'guards':len(rows),'literal_obligations':exact_labels()}))
elif mode=='freeze':
    assert BASE.exists() and not MANIFEST.exists(), 'Require baseline and no old manifest'
    rows=exact_guards()
    baseline=json.loads(BASE.read_text())
    assert baseline['immutable_guards']==rows
    count=exact_labels()
    payloads=[record(PREFIX+n) for n in NAMES]
    data={
      'schema':'R20-independent-whole-review1-entire-freeze-v1',
      'frozen_UTC':stamp(),
      'reviewer':'C /root/review_2017_coarsening_r1',
      'status':'sealed independent whole initial; explicit BOTH release required',
      'ALL_obligations':count,
      'ENTIRE_files':5,
      'payloads':payloads,
      'guard_summary':{'occurrences':14,'unique_paths':14,'canonical_deduplicated_sha256':compact_digest(rows)},
      'ONE_OWN_parent_manifest':record(PARENT),
      'FULL_final_ALL4_payload_MODEL_readbacks_completed_before_manifest':True,
      'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_required':True,
      'corresponding_NEW_peer_access_before_entire_freeze':False,
      'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
      'independent_effective_backend_readback':None,
      'last_own_direct_quota':{'usedPercent':82,'observed_UTC':'2026-10-19 02:31:48 UTC','resetsAt':1792874445,'windowDurationMins':10080,'ordinaryUsageAllowed':True,'legacy_by_limit_agree':True,'TOTAL_ceiling':90,'reserve_required':True,'automatic_later_window_spending':False},
      'mathematical_program_CAS_scan_test_or_old_replay':False,
      'Git_shared_old_cache_mutation':False
    }
    MANIFEST.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(record(PREFIX+'manifest-v1.json')))
elif mode=='verify':
    data=json.loads(MANIFEST.read_text())
    assert data['ENTIRE_files']==5 and data['ALL_obligations']==exact_labels()==40
    for row in data['payloads']:
        assert record(row['path'])==row, 'Changed payload: '+row['path']
    rows=exact_guards()
    assert json.loads(BASE.read_text())['immutable_guards']==rows
    assert data['guard_summary']['canonical_deduplicated_sha256']==compact_digest(rows)
    assert data['ONE_OWN_parent_manifest']==record(PARENT)
    print(json.dumps({'SEPARATE_readonly_verify_UTC':stamp(),'PASS':True,'ENTIRE_files':5,'ALL_obligations':40,'guards':14,'manifest':record(PREFIX+'manifest-v1.json')}))
else:
    raise SystemExit('Use init, freeze, or verify; documentary operations only.')
