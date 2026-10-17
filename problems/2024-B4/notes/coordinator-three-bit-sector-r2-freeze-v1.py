"""Create-new administrative r2 freeze, no mathematical evaluation."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[3]
BASE='problems/2024-B4/'
PREFIX=BASE+'notes/coordinator-three-bit-sector-r2-'

def fp(path):
    assert not Path(path).is_absolute() and '..' not in Path(path).parts
    assert '/reviews/coordinator-three-bit-sector-' not in path
    b=(ROOT/path).read_bytes()
    return {'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def rows(value):
    if isinstance(value,dict):
        if (isinstance(value.get('path'),str) and isinstance(value.get('bytes'),int)
            and isinstance(value.get('sha256'),str)):
            yield value
        for child in value.values():yield from rows(child)
    elif isinstance(value,list):
        for child in value:yield from rows(child)

def write(suffix,value):
    with(ROOT/(PREFIX+suffix)).open('x')as f:
        json.dump(value,f,indent=2)
        f.write('\n')

if __name__=='__main__':
    assert not(ROOT/(PREFIX+'freeze-v1.json')).exists()
    expected={'candidate-v1.md','obligations-v1.md','sources-worklog-v1.md','freeze-v1.py'}
    assert {p.name.removeprefix(Path(PREFIX).name)
            for p in(ROOT/BASE/'notes').glob(Path(PREFIX).name+'*')}==expected
    labels=re.findall(r'^\|R2-(\d\d)\|',(ROOT/(PREFIX+'obligations-v1.md')).read_text(),re.M)
    assert labels==[f'{n:02d}'for n in range(1,45)]
    unique={}
    metadata=[]
    count=0
    for path in [BASE+'reviews/structural-acceptance.json',
                 BASE+'reviews/reasoning-sector3-return-r1-acceptance.json',
                 BASE+'notes/coordinator-three-bit-sector-r1-freeze-v1.json']:
        doc=json.loads((ROOT/path).read_bytes())
        local=0
        for old in rows(doc):
            actual=fp(old['path'])
            assert actual=={k:old[k]for k in actual},old['path']
            unique[actual['path']]=actual
            local+=1
        own=fp(path)
        unique[path]=own
        metadata.append({'metadata':own,'direct_fingerprints_verified':local})
        count+=local+1
    for path in ['AGENTS.md',BASE+'statement.md']:
        unique[path]=fp(path)
        count+=1
    stamp=datetime.now(timezone.utc).isoformat()
    write('inputs-v1.json',{
        'recorded_at_utc':stamp,'administrative_only':True,
        'accepted_authorities_and_unchanged_old_constructor':metadata,
        'current_record_occurrences_verified':count,
        'current_unique_paths_verified':len(unique),
        'records':[unique[path]for path in sorted(unique)],
        'r1_unaccepted_not_a_proof_premise':True,
        'no_new_peer_review_report_finding_or_metadata_in_constructor_inputs':True,
        'nested_historical_inventories_bound_not_expanded':True,
        'no_mathematical_program_CAS_scan_or_old_replay':True})
    suffixes=['candidate-v1.md','obligations-v1.md','sources-worklog-v1.md',
              'freeze-v1.py','inputs-v1.json']
    write('freeze-v1.json',{
        'frozen_at_utc':stamp,'status':'candidate proof - unverified; COMPLETE stronger constructor checkpoint',
        'constructor_excluded':'/root',
        'requested_settings':{'model':'gpt-6.1-sol','reasoning':'max'},
        'independently_verified_effective_settings':None,
        'whole_obligations':44,
        'two_OTHER_initially_blind_WHOLE_reviews_required':True,
        'whole_claim':'No official odd binary-weight3 exponent; residual1mod4 whole absolute irreducibility exceptn13, which is ordinary F2-irreducible',
        'n13_no_published_Kasami_component_formula_required':True,
        'r1_unaccepted_one_audit_does_not_count_for_r2':True,
        'full_annual_classification_new_qualifying_family_or_novelty_claim':False,
        'mathematical_program_CAS_scan_or_replay':False,
        'current_record_occurrences_verified':count,
        'current_unique_paths_verified':len(unique),
        'metadata':metadata,
        'artifacts':[fp(PREFIX+s)for s in suffixes]})
    for old in unique.values():assert fp(old['path'])==old
    print(json.dumps({'main':fp(PREFIX+'candidate-v1.md'),
                      'freeze':fp(PREFIX+'freeze-v1.json'),
                      'whole_obligations':44,'occurrences':count,
                      'unique_paths':len(unique)},indent=2))
