"""Create-new administrative freeze: SHA/JSON/labels only, no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[3]
BASE='problems/2024-B4/'
PREFIX=BASE+'notes/coordinator-three-bit-sector-r1-'

def fp(path):
    data=(ROOT/path).read_bytes()
    return {'path':path,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}

def rows(value):
    if isinstance(value,dict):
        if (isinstance(value.get('path'),str)
            and isinstance(value.get('bytes'),int)
            and isinstance(value.get('sha256'),str)):
            yield value
        for child in value.values():
            yield from rows(child)
    elif isinstance(value,list):
        for child in value:
            yield from rows(child)

def write(suffix,value):
    with (ROOT/(PREFIX+suffix)).open('x') as stream:
        json.dump(value,stream,indent=2)
        stream.write('\n')

if __name__=='__main__':
    assert not (ROOT/(PREFIX+'freeze-v1.json')).exists()
    permitted={'candidate-v1.md','obligations-v1.md','sources-v1.md','freeze-v1.py'}
    existing={p.name.removeprefix(Path(PREFIX).name)
              for p in (ROOT/BASE/'notes').glob(Path(PREFIX).name+'*')}
    assert existing==permitted,existing
    authorities=[BASE+'reviews/'+name+'-acceptance.json' for name in
                 ['structural','reasoning-components-r1','reasoning-sector3-return-r1']]
    unique={}
    occurrences=0
    parents=[]
    for path in authorities:
        parent=json.loads((ROOT/path).read_bytes())
        assert parent['status'].startswith('proved, independently reviewed')
        count=0
        for expected in rows(parent):
            actual=fp(expected['path'])
            assert actual=={k:expected[k] for k in actual},expected['path']
            unique[actual['path']]=actual
            occurrences+=1
            count+=1
        own=fp(path)
        unique[path]=own
        occurrences+=1
        parents.append({'metadata':own,'direct_declared_rows_verified':count})
    for path in ['AGENTS.md',BASE+'statement.md']:
        unique[path]=fp(path)
        occurrences+=1
    obligations=(ROOT/(PREFIX+'obligations-v1.md')).read_text()
    labels=re.findall(r'^\|TB-(\d\d)\|',obligations,re.M)
    assert labels==[f'{n:02d}' for n in range(1,37)]
    main=(ROOT/(PREFIX+'candidate-v1.md')).read_text()
    assert 'Candidate proof - unverified' in main
    stamp=datetime.now(timezone.utc).isoformat()
    write('inputs-v1.json',{
        'recorded_at_utc':stamp,'administrative_only':True,
        'immutable_accepted_parents':parents,
        'declared_occurrences_verified':occurrences,
        'unique_paths_verified':len(unique),
        'records':[unique[p] for p in sorted(unique)],
        'older_nested_historical_inventories_bound_not_expanded':True,
        'old_math_certificate_or_program_replay':False})
    suffixes=['candidate-v1.md','obligations-v1.md','sources-v1.md',
              'freeze-v1.py','inputs-v1.json']
    write('freeze-v1.json',{
        'frozen_at_utc':stamp,'status':'candidate proof - unverified; complete constructor checkpoint',
        'constructor_excluded':'/root',
        'requested_settings':{'model':'gpt-6.1-sol','reasoning':'max'},
        'independently_verified_effective_settings':None,
        'two_OTHER_initially_blind_WHOLE_audits_required':True,
        'whole_obligations':36,
        'claims':['TB1 complete possible-intersection set',
                  'TB2 absolute sufficient tests and degree-product budget',
                  'TB3 ordinary-only sufficient inequality',
                  'TB4 two explicit infinite exclusion families'],
        'full_classification_new_qualifying_family_or_priority_claim':False,
        'mathematical_code_CAS_scan_or_replay':False,
        'accepted_parents':parents,
        'current_record_occurrences_verified':occurrences,
        'current_unique_paths_verified':len(unique),
        'artifacts':[fp(PREFIX+s) for s in suffixes]})
    for expected in unique.values():
        assert fp(expected['path'])==expected
    print(json.dumps({'main':fp(PREFIX+'candidate-v1.md'),
                      'freeze':fp(PREFIX+'freeze-v1.json'),
                      'obligations':36,'occurrences':occurrences,
                      'unique_paths':len(unique)},indent=2))
