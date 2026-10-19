"""NEW R29 WHOLE1 documentary SHA/JSON/literal-label helper ONLY.
No mathematical verifier/author/source/old program execution or peer inventory.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json
import sys
ROOT=Path(__file__).resolve().parents[3]
P='problems/2021-B4/reviews/coordinator-original-roots-r29-review-1-'
AUTHOR='problems/2021-B4/notes/coordinator-original-roots-r29-freeze-v1.json'
PARENT='problems/2021-B4/reviews/coordinator-global-return-r28-review-1-manifest-v1.json'
NAMES=['reasoning-deep-return-r24','coordinator-dyadic-return-r26','coordinator-global-return-r28']
INPUTS=['AGENTS.md','problems/2021-B4/statement.md']
for n in NAMES:
    INPUTS+=['problems/2021-B4/proofs/reviewed-'+n+'-v1.1.md']
    INPUTS+=['problems/2021-B4/reviews/'+n+'-acceptance'+s for s in ['.md','.json']]
def now():return datetime.now(timezone.utc).isoformat()
def read(p):return json.loads((ROOT/p).read_text())
def fp(p):
    b=(ROOT/p).read_bytes();return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def check(r):
    actual=fp(r['path']);assert actual==r,(r,actual);return actual
def new(p,v):
    assert p.startswith(P)
    with (ROOT/p).open('x') as f:json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
def digest(rows):return hashlib.sha256(json.dumps(sorted(rows,key=lambda r:r['path']),sort_keys=True,separators=(',',':')).encode()).hexdigest()
def labels():
    text=(ROOT/(P+'initial-v1.md')).read_text()
    ids=[s.split('|')[1] for s in text.splitlines() if s.startswith('|R29-')]
    assert ids==['R29-'+str(i).zfill(2) for i in range(1,17)]
def prepare():
    ar=check(dict(path=AUTHOR,bytes=2043,sha256='0fff6336528e3cb971f23e89626fb293a4d5658cdc38bbc4ef5e1d986b584233'))
    a=read(AUTHOR);assert a['ENTIRE_files']==6 and a['ALL_obligations']==16
    rows=[ar]+[check(r) for r in a['payloads']]
    lookup={r['path']:r for r in read('problems/2021-B4/notes/coordinator-original-roots-r29-baseline-v1.json')['necessary_immutable_records']}
    rows += [check(lookup[p]) for p in INPUTS]
    parent=check(dict(path=PARENT,bytes=2862,sha256='6abb8d44f108787d8e7a6885d5e240a3bb6b612876e6253f03ae071032dd8dbb'))
    rows.append(parent);assert len(rows)==len({r['path'] for r in rows})==18
    bound={r['path']:r for r in rows}
    for n in NAMES:
        accepted=read('problems/2021-B4/reviews/'+n+'-acceptance.json')['accepted_copy'];assert accepted==bound[accepted['path']]
    v=dict(captured_UTC=now(),necessary_immutable_records=rows,guard_occurrences=18,guard_unique_paths=18,canonical_deduplicated_sha256=digest(rows),ONE_compact_OWN_parent=parent,recursive_inventory_expansion=False,mutable_map_guards=False,NEW_R29_peer_finding_file_actual_inventory_hash_metadata_commentary_access=False,documentary_code_certifies_mathematics=False)
    new(P+'baseline-v1.json',v);print(json.dumps(dict(prepared_UTC=v['captured_UTC'],guards=18,digest=digest(rows))))
def freeze():
    assert '--FULL-final-ALL5-MODEL-readbacks-completed' in sys.argv
    labels();b=read(P+'baseline-v1.json')
    paths=[P+s for s in ['initial-v1.md','sources-v1.json','certificate-v1.py','admin-v1.py','baseline-v1.json']]
    v=dict(frozen_UTC=now(),status='SEALED immutable initially blind independent OTHER WHOLE1; coordinator pending',reviewer='/root/review_2021_reasoning_j15_r2',constructor='/root',constructor_excluded=True,NEW_R29_construction_contribution=False,ENTIRE_files=6,whole_obligations=16,payloads=[fp(p) for p in paths],guard_summary=dict(occurrences=18,unique_paths=18,canonical_deduplicated_sha256=b['canonical_deduplicated_sha256']),ONE_compact_OWN_parent=b['ONE_compact_OWN_parent'],whole_hand_reconstruction=True,ONE_NEW_proof_critical_fixed29_verifier_executed=True,author_source_old_helper_certificate_freezer_executed=False,unresolved_substantive_defects=0,required_author_repairs=0,closed_scope_notes=10,FULL_final_ALL5_payload_MODEL_readbacks_completed=True,FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED=True,NEW_R29_peer_finding_file_actual_inventory_hash_metadata_commentary_access=False,prospective_R30_access=False,explicit_BOTH_release_required=True,Git_shared_old_cache_configuration_mutation=False,requested=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),independent_effective_backend_readback=None,quota=dict(start_usedPercent=87,start_observed_UTC='2026-10-19 04:20:17 UTC',windowDurationMins=10080,resetsAt=1792874445,TOTAL_ceiling=90,checkpoint_at_TOTAL=89,reserve=True,automatic_later_window=False))
    new(P+'manifest-v1.json',v);print(json.dumps(dict(frozen_UTC=v['frozen_UTC'],manifest=fp(P+'manifest-v1.json'))))
def verify():
    m=read(P+'manifest-v1.json');b=read(P+'baseline-v1.json')
    for r in m['payloads']+b['necessary_immutable_records']:check(r)
    assert digest(b['necessary_immutable_records'])==m['guard_summary']['canonical_deduplicated_sha256']
    assert m['ENTIRE_files']==6 and m['whole_obligations']==16;labels()
    print(json.dumps(dict(SEPARATE_readonly_verified_UTC=now(),PASS=True,payloads=5,necessary_immutable_paths=18,manifest=fp(P+'manifest-v1.json'),documentary_verification_executes_mathematics=False)))
if __name__=='__main__':{'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
