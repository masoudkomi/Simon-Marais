"""NEW PH13 documentary helper only; never executes author/source/old code."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

ROOT=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
P='problems/2022-B4/reviews/reasoning-physical-return-r13-review-1-'
BASE=ROOT/(P+'baseline-v1.json')
MAN=ROOT/(P+'manifest-v1.json')
AUTHOR='problems/2022-B4/notes/reasoning-physical-return-r13-freeze-v1.json'
PARENT={'path':'problems/2024-B4/notes/reasoning-frontier-return-r15-freeze-v1.json','bytes':2505,'sha256':'d5d9804d237c368818cfaa7dcc9dda188cb474f7c4f5b7e97d50e1d561b283d2'}
AUTHOR_ID={'path':AUTHOR,'bytes':2526,'sha256':'256bedd300fa0ce8ebe1ee1f69d47e1246a7c5c2c50f802e6d3d2d2ce5e6c1c6'}
NAMES=['reasoning-itinerary-return-r12','reasoning-dynamics-return-r9','reasoning-fiber-return-r5']
PAY=[P+s for s in ['initial-v1.md','sources-v1.json','admin-v1.py','baseline-v1.json']]

def utc(): return datetime.now(timezone.utc).isoformat()
def rec(path):
    b=(ROOT/path).read_bytes()
    return {'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def new(path,data):
    with path.open('x') as f:
        json.dump(data,f,indent=2,ensure_ascii=False)
        f.write('\n')

def prepare():
    author=json.loads((ROOT/AUTHOR).read_text())
    paths=['AGENTS.md','problems/2022-B4/statement.md',AUTHOR]+[r['path'] for r in author['payloads']]
    pairs=[]
    for name in NAMES:
        body='problems/2022-B4/proofs/reviewed-'+name+'-v1.1.md'
        auth='problems/2022-B4/reviews/'+name+'-acceptance'
        paths.extend([body,auth+'.md',auth+'.json'])
        pairs.append((body,auth+'.json'))
    paths.append(PARENT['path'])
    rows=[rec(p) for p in paths]
    bypath={r['path']:r for r in rows}
    assert len(bypath)==len(rows)
    assert bypath[AUTHOR]==AUTHOR_ID
    assert bypath[PARENT['path']]==PARENT
    for row in author['payloads']: assert bypath[row['path']]==row
    for body,auth in pairs:
        assert bypath[body]==json.loads((ROOT/auth).read_text())['accepted_copy']
    summary={'occurrences':len(rows),'unique_paths':len(bypath),'canonical_deduplicated_sha256':hashlib.sha256(json.dumps(rows,sort_keys=True).encode()).hexdigest()}
    new(BASE,{'prepared_UTC':utc(),'necessary_immutable_guards_checked_ONCE':rows,'guard_summary':summary,
              'ONE_compact_OWN_parent':PARENT,'recursive_inventories_or_mutable_map_guards':False,
              'author_code_read_not_executed':True,'NEW_PH13_peer_access':False,
              'guard_scope':'Documentary hashes do not constitute mathematical MODEL reads.',
              'quota':{'start_usedPercent':84,'latest_usedPercent':85,'windowDurationMins':10080,'resetsAt':1792874445,'ordinaryUsageAllowed':True,'TOTAL_ceiling':90,'reserve':True,'automatic_later_window':False}})
    print(json.dumps({'baseline':rec(P+'baseline-v1.json'),'guard_summary':summary},indent=2))

def freeze():
    baseline=json.loads(BASE.read_text())
    text=(ROOT/PAY[0]).read_text()
    assert all('|PH13-'+str(i).zfill(2)+'|PASS|' in text for i in range(1,33))
    data={'frozen_UTC':utc(),'status':'SEALED immutable initially blind independent OTHER WHOLE1; coordinator pending',
          'reviewer':'/root/review_2021_reasoning_j15_r2','constructor':'C /root/review_2017_coarsening_r1',
          'constructor_excluded':True,'NEW_PH13_construction_contribution':False,'whole_obligations':32,'ENTIRE_files':5,
          'payloads':[rec(p) for p in PAY],'guard_summary':baseline['guard_summary'],'ONE_compact_OWN_parent':PARENT,
          'whole_hand_reconstruction':True,'unresolved_substantive_defects':0,'required_author_repairs':0,'closed_scope_notes':10,
          'FULL_final_ALL4_payload_MODEL_readbacks_completed':True,
          'FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED':True,
          'NEW_PH13_peer_finding_file_actual_inventory_hash_metadata_commentary_access':False,
          'findings_require_explicit_BOTH_release':True,'mathematical_truth_checked_by_code':False,
          'author_source_old_helper_certificate_freezer_executed':False,
          'Git_shared_old_cache_configuration_mutation':False,
          'requested':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},'independent_effective_backend_readback':None,
          'quota':baseline['quota']}
    new(MAN,data)
    print(json.dumps({'manifest':rec(P+'manifest-v1.json'),'frozen_UTC':data['frozen_UTC']},indent=2))

def verify():
    data=json.loads(MAN.read_text())
    for row in data['payloads']: assert rec(row['path'])==row
    baseline=json.loads(BASE.read_text())
    assert data['guard_summary']==baseline['guard_summary']
    assert data['ONE_compact_OWN_parent']==baseline['ONE_compact_OWN_parent']==PARENT
    assert data['whole_obligations']==32 and data['ENTIRE_files']==5
    print(json.dumps({'SEPARATE_readonly_documentary_verify':'PASS','verified_UTC':utc(),'manifest':rec(P+'manifest-v1.json'),
                      'payloads_match':4,'once_checked_guard_summary':data['guard_summary'],'mathematical_truth_check':False},indent=2))

if __name__=='__main__': {'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
