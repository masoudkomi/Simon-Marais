"""Create-new ROOT R1 administrative freeze; no mathematical evaluation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[3]
BASE='problems/2020-B4/'
OWN=BASE+'reviews/reasoning-return-r8-review-1-'
AUTHOR=BASE+'notes/reasoning-return-r8-'
PEER=BASE+'reviews/reasoning-return-r8-review-2-'

def fp(path):
    assert isinstance(path,str) and not path.startswith(PEER)
    assert not Path(path).is_absolute() and '..' not in Path(path).parts
    b=(ROOT/path).read_bytes()
    return {'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def rows(value):
    if isinstance(value,dict):
        if (isinstance(value.get('path'),str) and isinstance(value.get('bytes'),int)
            and isinstance(value.get('sha256'),str)):
            yield value
        for v in value.values():yield from rows(v)
    elif isinstance(value,list):
        for v in value:yield from rows(v)

def write(suffix,value):
    with(ROOT/(OWN+suffix)).open('x')as f:
        json.dump(value,f,indent=2)
        f.write('\n')

if __name__=='__main__':
    assert not(ROOT/(OWN+'manifest-v1.json')).exists()
    assert fp(AUTHOR+'candidate-v1.md')=={
        'path':AUTHOR+'candidate-v1.md','bytes':25948,
        'sha256':'2eb3bbc51c282619a4bf0bf2b34f083c9c65abd7b27822355cd4973f391637d8'}
    assert fp(AUTHOR+'freeze-v1.json')=={
        'path':AUTHOR+'freeze-v1.json','bytes':5346,
        'sha256':'6f7d5060bf093304ec26a0268a8098942bd8021e99e056b1970dec12813d102e'}
    metadata=[AUTHOR+'freeze-v1.json',AUTHOR+'baseline-v1.json',
              AUTHOR+'input-validation-v1.json',AUTHOR+'sources-v1.json',
              BASE+'reviews/reasoning-return-r7-acceptance.json']
    unique={}
    counts=[]
    for path in metadata:
        n=0
        for expected in rows(json.loads((ROOT/path).read_bytes())):
            actual=fp(expected['path'])
            assert actual=={k:expected[k]for k in actual},expected['path']
            unique[actual['path']]=actual
            n+=1
        own=fp(path)
        unique[path]=own
        counts.append({'metadata':own,'direct_declared_occurrences_verified':n})
    parent='problems/2017-B4/reviews/reasoning-value-return-r5-review-1-manifest-v1.json'
    parentfp=fp(parent)
    unique[parent]=parentfp
    obs=(ROOT/(AUTHOR+'obligations-v1.md')).read_text()
    ledger=(ROOT/(OWN+'ledger-v1.md')).read_text()
    expected=[f'{i:02d}'for i in range(1,55)]
    assert re.findall(r'^\|R8-(\d\d)\|',obs,re.M)==expected
    assert re.findall(r'^\|R8-(\d\d)\|',ledger,re.M)==expected
    stamp=datetime.now(timezone.utc).isoformat()
    canonical=json.dumps([unique[p]for p in sorted(unique)],sort_keys=True,
                         separators=(',',':')).encode()
    total=sum(c['direct_declared_occurrences_verified']for c in counts)
    write('integrity-v1.json',{
        'verified_at_utc':stamp,'administrative_only':True,
        'all_necessary_declared_current_rows_match':True,
        'record_occurrences_verified':total,'unique_paths_verified':len(unique),
        'canonical_deduplicated_rows_sha256':hashlib.sha256(canonical).hexdigest(),
        'metadata':counts,'immutable_previous_own_root_review':parentfp,
        'old_historical_inventories_bound_not_recopied':True,
        'whole_checks':54,'all_constructor_obligations':54,
        'new_peer_R8_material_read_before_ENTIRE_freeze':False,
        'mathematical_program_scan_CAS_or_replay':False})
    suffixes=['initial-v1.md','ledger-v1.md','sources-worklog-v1.md',
              'freeze-v1.py','integrity-v1.json']
    write('manifest-v1.json',{
        'frozen_at_utc':stamp,'status':'COMPLETE initially blind NONCONSTRUCTOR WHOLE R1 initial',
        'reviewer':'/root','constructor_excluded':'/root/review_2022_complexity_r2',
        'requested_settings':{'model':'gpt-6.1-sol','reasoning':'max'},
        'independently_verified_effective_settings':None,
        'target_main':fp(AUTHOR+'candidate-v1.md'),
        'target_freeze':fp(AUTHOR+'freeze-v1.json'),
        'whole_checks':54,'all_author_obligations':54,
        'recommendation':'No substantive defect in exact conditional R8A--F; other whole audit and reconciliation still required',
        'substantive_open_issues':0,'required_repairs':0,
        'complete_initial_before_ANY_new_peer_R8_report_finding_ledger_or_metadata':True,
        'root_broad_assignment_only_no_new_R8_construction':True,
        'older_root_reviews_disclosed_not_self_recertification':True,
        'all_source_read_limits_and_source_typo_correctly_separated':True,
        'record_occurrences_verified':total,'unique_paths_verified':len(unique),
        'mathematical_program_scan_CAS_or_replay':False,
        'new_unconditional_order_classification_cutoff_or_novelty_claim':False,
        'weekly':{'observed_at_utc':'2026-10-17T20:25:32+00:00',
                  'total_used_percent':63,'reset_unix':1792745187,
                  'ceiling_total_percent':90,'integration_reserve':True},
        'artifacts':[fp(OWN+s)for s in suffixes]})
    for expectedrow in unique.values():assert fp(expectedrow['path'])==expectedrow
    for row in json.loads((ROOT/(OWN+'manifest-v1.json')).read_text())['artifacts']:
        assert fp(row['path'])==row
    print(json.dumps({'manifest':fp(OWN+'manifest-v1.json'),
                      'initial':fp(OWN+'initial-v1.md'),'whole_obligations':54,
                      'occurrences':total,'unique_paths':len(unique),
                      'math_program':False},indent=2))
