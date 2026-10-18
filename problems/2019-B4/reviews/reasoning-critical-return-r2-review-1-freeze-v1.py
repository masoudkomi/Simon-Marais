#!/usr/bin/env python3
"""Administrative integrity only; NO mathematical computation or peer access."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,re
ROOT=Path.cwd().resolve()
P='problems/2019-B4/reviews/reasoning-critical-return-r2-review-1-'
T='problems/2019-B4/notes/reasoning-critical-return-r2-'
NOW=datetime.now(timezone.utc).isoformat()
def rec(path):
    assert not path.startswith('problems/2019-B4/reviews/reasoning-critical-return-r2-review-2-')
    b=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(b),sha256=sha256(b).hexdigest())
def check(row):
    a=rec(row['path']);assert a=={k:row[k] for k in ('path','bytes','sha256')},row['path'];return a
def read(path):return json.loads((ROOT/path).read_text())
def out(suffix,value):
    with (ROOT/(P+suffix)).open('x') as f:json.dump(value,f,indent=2);f.write('\n')
target=check(dict(path=T+'candidate-v1.md',bytes=22291,
    sha256='1d672cc4eafde68da5d83cd4997dbee1a4e5274e4858bafbbc63479cc01b3de7'))
freeze=check(dict(path=T+'freeze-v1.json',bytes=6949,
    sha256='295feae2d5671960ad9d9ae3456abcd94850a2c2faec0ce42e024eb5d05b18c9'))
f=read(freeze['path']);records={freeze['path']:freeze}
for row in f['artifacts']:records[row['path']]=check(row)
assert len(records)==11
cb=read(T+'baseline-v1.json');old=[check(row) for row in cb['protected']]
assert len(old)==19
assert sha256(json.dumps(old,sort_keys=True,separators=(',',':')).encode()).hexdigest()==cb['canonical_protected_summary_sha256']
for row in old:records[row['path']]=row
for name in ['reasoning-return-r7','monotone-ratio','reasoning-growth-return-r1','walk-Frechet']:
    ap='problems/2019-B4/reviews/'+name+'-acceptance.json';a=read(ap)
    assert a['unresolved_substantive_issues']==0 and a['repair_required'] is False
    for path in [ap,ap[:-5]+'.md']:records[path]=rec(path)
    for key in ['candidate','accepted_copy']:
        actual=check(a[key]);records[actual['path']]=actual
    assert (ROOT/a['accepted_copy']['path']).read_bytes().endswith((ROOT/a['candidate']['path']).read_bytes())
ap='problems/2019-B4/reviews/secondpass-acceptance.json';a=read(ap)
assert a['substantive_repairs_required'] is False
records[ap]=rec(ap);records[ap[:-5]+'.md']=rec(ap[:-5]+'.md')
for row in cb['secondpass_exact_declared_hashes_checked']:
    check(row);local=row['path'].removeprefix('problems/2019-B4/')
    assert a['artifacts'][local]==row['sha256']
parent=check(dict(path='problems/2021-B4/reviews/reasoning-unit-return-r15-review-1-manifest-v1.json',
    bytes=3096,sha256='6abdeb4b5f8e918d6e4bf635661ebf33d27f6592041e77785c75c60ff18abb9b'))
records[parent['path']]=parent
pf=read(parent['path'])
for row in pf['artifacts']:check(row)
author_labels=[int(x) for x in re.findall(r'^(\d+)\. ',(ROOT/(T+'obligations-v1.md')).read_text(),re.M)]
own_labels=[int(x) for x in re.findall(r'^\| CR-R1-(\d{2}) \| PASS\.',(ROOT/(P+'ledger-v1.md')).read_text(),re.M)]
assert author_labels==own_labels==list(range(1,61))
out('baseline-v1.json',dict(recorded_at_utc=NOW,administrative_integrity_only=True,
    exact_target=target,constructor_freeze=freeze,
    current_direct_records=[records[k] for k in sorted(records)],
    constructor_19_fixed_inputs_verified=True,
    constructor_direct_summary=cb['canonical_protected_summary_sha256'],
    compact_own_parent=parent,own_parent_payloads_verified=len(pf['artifacts']),
    no_recursive_historical_replay=True,
    NO_NEW_corresponding_A_CR_findings_files_hashes_metadata_opened=True))
out('metadata-v1.json',dict(recorded_at_utc=NOW,reviewer='/root',
    constructor='/root/review_2022_complexity_r2',OTHER_NEW_nonconstructor=True,
    root_assignment_only_no_NEW_CR_inference=True,
    old_MR_DG_construction_R7_G_review_roles_not_fresh_self_certification=True,
    whole_obligations=60,all60_pass=True,substantive_issues=0,required_repairs=0,
    closed_scope_notes=4,ENTIRE_report_ledger_issues_sources_log_code_ALL_metadata_frozen_together=True,
    NO_NEW_corresponding_A_CR_findings_files_hashes_metadata_opened=True,
    peer_completion_identity_only_received_before_own_freeze=True,
    no_math_program_CAS_scan_sample_certificate_or_author_rerun=True,
    requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),
    independently_verified_effective_settings=None,
    actual_regime_exact_lambda_new_numerical_annual_or_priority_claim=False,
    candidate_promotion=False,other_whole_R2_and_reconciliation_still_required=True))
out('input-validation-v1.json',dict(validated_at_utc=NOW,
    administrative_integrity_only_not_proof=True,constructor_payloads=10,
    constructor_freeze_verified=True,constructor_fixed_inputs_verified=19,
    four_current_authorities_and_exact_candidate_suffixes_verified=True,
    operative_secondpass_register_declared_hashes_verified=4,
    compact_own_parent_payloads_verified=len(pf['artifacts']),
    exact_60_author_and_review_labels=True,all_exact_inputs_unchanged=True,errors=[]))
suffixes=['initial-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md',
    'worklog-v1.md','freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
out('manifest-v1.json',dict(frozen_at_utc=NOW,
    status='ENTIRE initially blind OTHER WHOLE CR1-CR5 review1',
    reviewer='/root',constructor='/root/review_2022_complexity_r2',
    exact_target=target,constructor_freeze=freeze,whole_obligations=60,all60_pass=True,
    substantive_issues=0,required_repairs=0,closed_scope_notes=4,
    ENTIRE_report_ledger_issues_sources_log_code_ALL_metadata_frozen=True,
    NO_NEW_corresponding_A_CR_findings_files_hashes_metadata_opened=True,
    compact_own_parent=parent,other_whole_R2_and_reconciliation_required=True,
    promotion=False,artifacts=[rec(P+s) for s in suffixes]))
for row in read(P+'manifest-v1.json')['artifacts']:check(row)
print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'),
    initial=rec(P+'initial-v1.md'),whole_obligations=60,new_review_paths=10,
    no_mathematical_computation=True),indent=2))
