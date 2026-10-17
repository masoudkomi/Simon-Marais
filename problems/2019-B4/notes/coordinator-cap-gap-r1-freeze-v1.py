"""Administrative one-time freezer; never executes a mathematical program."""
from pathlib import Path
from datetime import datetime, timezone
import json, hashlib

root=Path('/Users/uqmkamga/Documents/ChatGPT/Website')
prefix='problems/2019-B4/notes/coordinator-cap-gap-r1-'
def fp(path):
    b=(root/path).read_bytes()
    return {'path':path,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def save(suffix,obj):
    p=root/(prefix+suffix)
    assert not p.exists(), f'frozen path already exists: {p}'
    p.write_text(json.dumps(obj,indent=2)+'\n')

freeze_path=root/(prefix+'freeze-v1.json')
assert not freeze_path.exists(), 'Do not rerun a completed freezer'
stamp=datetime.now(timezone.utc).isoformat()
known={
 'problems/2019-B4/proofs/reviewed-separation-scale-v1.1.md':'40776fab233b7503a1c79e91959692dc8dd09d4d116f68831007278bb054d2a6',
 'problems/2019-B4/notes/thirdpass-bounded-separation-v1.md':'3364e8c6cf23ba3ecb250f13a5873732c108b6904a68126f52f5d7234eb916d4',
}
paths=[
 'AGENTS.md',
 'problems/2019-B4/statement.md',
 'problems/2019-B4/proofs/reviewed-secondpass-v1.1.md',
 'problems/2019-B4/reviews/secondpass-acceptance.md',
 'problems/2019-B4/reviews/secondpass-acceptance.json',
 'problems/2019-B4/proofs/reviewed-thirdpass-v1.1.md',
 'problems/2019-B4/notes/thirdpass-bounded-separation-v1.md',
 'problems/2019-B4/reviews/thirdpass-acceptance.md',
 'problems/2019-B4/reviews/thirdpass-acceptance.json',
 'problems/2019-B4/reviews/thirdpass-acceptance-integrity.json',
 'problems/2019-B4/computations/thirdpass-delay7-exact.json',
 'problems/2019-B4/computations/thirdpass-crosscheck15.json',
 'problems/2019-B4/proofs/reviewed-moment-tail-v1.1.md',
 'problems/2019-B4/reviews/moment-tail-acceptance.md',
 'problems/2019-B4/reviews/moment-tail-acceptance.json',
 'problems/2019-B4/proofs/reviewed-separation-scale-v1.1.md',
 'problems/2019-B4/reviews/coordinator-separation-scale-r1-acceptance.md',
 'problems/2019-B4/reviews/coordinator-separation-scale-r1-acceptance.json',
 'problems/2019-B4/notes/coordinator-separation-scale-r1-freeze-v1.json',
 'problems/2019-B4/notes/coordinator-separation-scale-r1-input-validation-v1.json',
 'problems/2019-B4/reviews/nonregularity-return-acceptance.md',
]
records=[fp(p) for p in paths]
for r in records:
    if r['path'] in known:
        assert r['sha256']==known[r['path']], r['path']
parentpaths=[
 'problems/2019-B4/reviews/coordinator-separation-scale-r1-acceptance.json',
 'problems/2019-B4/notes/coordinator-separation-scale-r1-freeze-v1.json',
 'problems/2019-B4/notes/coordinator-separation-scale-r1-input-validation-v1.json',
]
save('input-validation-v1.json',{
 'at_utc':stamp,'status':'all explicit input identities bound; known immutable hashes match',
 'record_occurrences':len(records),'unique_paths':len(set(paths)),
 'records':records,
 'compact_immutable_parents':[fp(p) for p in parentpaths],
 'historical_inventory_rows_copied':False,
 'math_certificate_or_old_program_replayed_by_this_freezer':False,
 'integrity_is_not_independent_mathematical_review':True,
})
save('sources-v1.json',{
 'at_utc':stamp,'new_external_theorem_imports':[],
 'source_scope':'all new premises are exact accepted project results; see source-audit-v1.md',
 'fresh_complete_mathematical_reads':[
  'accepted third-pass exposition and acceptance',
  'accepted moment-tail exposition',
  'complete SS submission and acceptance',
  'NR acceptance',
 ],
 'retained_earlier_complete_reads_not_claimed_fresh':[
  'second-pass canonical dictionary/rigidity/renewal',
  'NR whole mathematical body',
 ],
 'new_old_all_row_verification_claim':False,
 'old_cap_certificate_role':'accepted all-state positive-vector inequality bounds rho7 itself',
 'constructor_older_roles_disclosed':True,
 'compact_immutable_parents':[fp(p) for p in parentpaths],
})
job=json.loads((root/(prefix+'certificate-job-v1.json')).read_text())
assert job['reaped'] and job['exit_code']==0 and not job['timed_out']
assert (root/(prefix+'certificate-stderr-v1.txt')).read_text()==''
certificate=json.loads((root/(prefix+'certificate-output-v1.json')).read_text())
assert certificate['all_assertions_passed']
assert int(certificate['strict_endpoint_slack']['numerator'])>0
for r in records:
    assert fp(r['path'])==r
suffixes=[
 'candidate-v1.md','obligations-v1.md','worklog-v1.md','source-audit-v1.md',
 'certificate-v1.py','certificate-output-v1.json','certificate-stderr-v1.txt',
 'certificate-job-v1.json','input-validation-v1.json','sources-v1.json','freeze-v1.py',
]
save('freeze-output-v1.json',{
 'at_utc':stamp,'status':'all inputs unchanged and fixed rational certificate complete',
 'explicit_input_records':len(records),'known_expected_hashes_matched':len(known),
 'certificate_child_pid':job['pid'],'certificate_child_reaped':True,
 'freezer_mathematical_code_replay':False,
})
suffixes.append('freeze-output-v1.json')
save('freeze-v1.json',{
 'frozen_at_utc':stamp,'status':'candidate proof - unverified; COMPLETE constructor checkpoint',
 'constructor':'/root','requested_settings':{'model':'gpt-6.1-sol','reasoning':'max','inherited':True},
 'independently_verified_effective_settings':None,
 'whole_obligations':24,
 'claims':['CG1 exact rigid widths and sharper odd cap agreement','CG2 exact known omitted rigid tail',
  'CG3 quantitative lower cap error','CG4 proposed1.765224<lambda<1.834847'],
 'requires_two_OTHER_fresh_initially_blind_nonconstructor_WHOLE_audits':True,
 'old_roles_disclosed':True,
 'new_math_execution':'one fixed rational sign certificate only; no enumeration/old replay',
 'certificate_job':fp(prefix+'certificate-job-v1.json'),
 'compact_input_validation':fp(prefix+'input-validation-v1.json'),
 'artifacts':[fp(prefix+s) for s in suffixes],
 'annual_answer_actual_moment_regime_or_novelty_claim':False,
})
print(json.dumps({'status':'frozen unverified','main':fp(prefix+'candidate-v1.md'),
 'freeze':fp(prefix+'freeze-v1.json'),'artifacts':len(suffixes),'obligations':24},indent=2))
