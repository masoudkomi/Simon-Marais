"""NEW R28 WHOLE1 documentary SHA/JSON/literal-label helper ONLY.
Never executes mathematical verifier, author/source/old code, or peer inventory.
All writes exclusive NEW own prefix. verify is a separate read-only pass.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json
import sys

ROOT=Path(__file__).resolve().parents[3]
P='problems/2021-B4/reviews/coordinator-global-return-r28-review-1-'
AUTHOR='problems/2021-B4/notes/coordinator-global-return-r28-freeze-v1.json'
PARENT='problems/2025-B4/reviews/reasoning-joint-trace-return-r13-review-2-manifest-v1.json'
NAMES=['reasoning-deep-return-r24','coordinator-dyadic-return-r26','coordinator-contact-return-r27']
INPUTS=['AGENTS.md','problems/2021-B4/statement.md']
for name in NAMES:
    INPUTS += ['problems/2021-B4/proofs/reviewed-'+name+'-v1.1.md']
    INPUTS += ['problems/2021-B4/reviews/'+name+'-acceptance'+suffix for suffix in ['.md','.json']]

def now():return datetime.now(timezone.utc).isoformat()
def read(path):return json.loads((ROOT/path).read_text())
def fp(path):
    data=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
def checked(record):
    actual=fp(record['path'])
    assert actual==record,(record,actual)
    return actual
def new(path,obj):
    assert path.startswith(P)
    with (ROOT/path).open('x') as f:json.dump(obj,f,indent=2,ensure_ascii=False);f.write('\n')
def digest(records):return hashlib.sha256(json.dumps(sorted(records,key=lambda r:r['path']),sort_keys=True,separators=(',',':')).encode()).hexdigest()
def labels():
    lines=(ROOT/(P+'initial-v1.md')).read_text().splitlines()
    actual=[line.split('|')[1] for line in lines if line.startswith('|R28-')]
    assert actual==['R28-'+str(i).zfill(2) for i in range(1,25)]

def prepare():
    author=checked(dict(path=AUTHOR,bytes=2159,sha256='c2818ceba47100e3276c85d3937bd3a3f4ac887343c52b1fa96114d2a2743029'))
    m=read(AUTHOR)
    assert m['ENTIRE_files']==6 and m['whole_obligations']==24
    rows=[author]+[checked(r) for r in m['payloads']]
    author_base=read('problems/2021-B4/notes/coordinator-global-return-r28-baseline-v1.json')
    lookup={r['path']:r for r in author_base['necessary_immutable_records']}
    rows += [checked(lookup[path]) for path in INPUTS]
    parent=checked(dict(path=PARENT,bytes=2711,sha256='0a8db05737753bcfebee2607dcec8007c72ad61634c27be6e2d1bdd7c1efb0c2'))
    rows.append(parent)
    assert len(rows)==len({r['path'] for r in rows})==18
    bound={r['path']:r for r in rows}
    for name in NAMES:
        accepted=read('problems/2021-B4/reviews/'+name+'-acceptance.json')['accepted_copy']
        assert accepted==bound[accepted['path']]
    obj=dict(captured_UTC=now(),necessary_immutable_records=rows,guard_occurrences=18,guard_unique_paths=18,canonical_deduplicated_sha256=digest(rows),ONE_compact_OWN_parent=parent,recursive_inventory_expansion=False,mutable_map_guards=False,author_or_old_code_executed=False,NEW_R28_peer_finding_file_actual_inventory_hash_metadata_commentary_access=False,documentary_code_checks_mathematical_truth=False)
    new(P+'baseline-v1.json',obj)
    print(json.dumps(dict(prepared_UTC=obj['captured_UTC'],guards=18,digest=digest(rows))))

def freeze():
    assert '--FULL-final-ALL5-MODEL-readbacks-completed' in sys.argv
    labels();base=read(P+'baseline-v1.json')
    paths=[P+s for s in ['initial-v1.md','sources-v1.json','certificate-v1.py','admin-v1.py','baseline-v1.json']]
    obj=dict(frozen_UTC=now(),status='SEALED immutable independent initially blind OTHER WHOLE1; coordinator pending',reviewer='/root/review_2021_reasoning_j15_r2',constructor='/root',constructor_excluded=True,NEW_R28_construction_contribution=False,ENTIRE_files=6,whole_obligations=24,payloads=[fp(path) for path in paths],guard_summary=dict(occurrences=18,unique_paths=18,canonical_deduplicated_sha256=base['canonical_deduplicated_sha256']),ONE_compact_OWN_parent=base['ONE_compact_OWN_parent'],whole_hand_reconstruction=True,ONE_new_independent_finite_certificate_executed=True,author_source_old_helper_certificate_freezer_executed=False,unresolved_substantive_defects=0,required_author_repairs=0,closed_scope_notes=10,FULL_final_ALL5_payload_MODEL_readbacks_completed=True,FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_REQUIRED=True,NEW_R28_peer_finding_file_actual_inventory_hash_metadata_commentary_access=False,prospective_R29_access=False,explicit_BOTH_release_required=True,Git_shared_old_cache_configuration_mutation=False,requested=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),independent_effective_backend_readback=None,quota=dict(start_usedPercent=86,start_observed_UTC='2026-10-19 04:00:14 UTC',windowDurationMins=10080,resetsAt=1792874445,TOTAL_ceiling=90,reserve=True,automatic_later_window=False))
    new(P+'manifest-v1.json',obj)
    print(json.dumps(dict(frozen_UTC=obj['frozen_UTC'],manifest=fp(P+'manifest-v1.json'))))

def verify():
    m=read(P+'manifest-v1.json');base=read(P+'baseline-v1.json')
    for row in m['payloads']+base['necessary_immutable_records']:checked(row)
    assert digest(base['necessary_immutable_records'])==m['guard_summary']['canonical_deduplicated_sha256']
    assert m['ENTIRE_files']==6 and m['whole_obligations']==24
    labels()
    print(json.dumps(dict(SEPARATE_readonly_verified_UTC=now(),PASS=True,payloads=5,necessary_immutable_paths=18,manifest=fp(P+'manifest-v1.json'),documentary_verification_executes_mathematics=False)))

if __name__=='__main__':{'prepare':prepare,'freeze':freeze,'verify':verify}[sys.argv[1]]()
