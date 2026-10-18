#!/usr/bin/env python3
"""Exact whole-review metadata only. Never mathematical code or peer access."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,re
ROOT=Path.cwd().resolve()
P='problems/2021-B4/reviews/reasoning-early-return-r16-review-1-'
T='problems/2021-B4/notes/reasoning-early-return-r16-'
NOW=datetime.now(timezone.utc).isoformat()
def rec(path):
    assert not path.startswith('problems/2021-B4/reviews/reasoning-early-return-r16-review-2-')
    assert not path.startswith('problems/2021-B4/reviews/reasoning-unit-return-r15-review-2-')
    b=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(b),sha256=sha256(b).hexdigest())
def read(path):return json.loads((ROOT/path).read_text())
def check(row):
    a=rec(row['path']);assert a=={k:row[k] for k in ('path','bytes','sha256')},row['path']
    return a
def out(suffix,value):
    with (ROOT/(P+suffix)).open('x') as f:json.dump(value,f,indent=2);f.write('\n')
target=check(dict(path=T+'candidate-v1.md',bytes=18818,
    sha256='d9765b700bf7f7a0c13bcb0b5729a38150e87fe847156df29d4c592abad0b2d1'))
freeze=check(dict(path=T+'freeze-v1.json',bytes=6387,
    sha256='8ff369c2ad1d306316599be62096001a50a2799f897b612df6e7c96a0aa731de'))
rows=[freeze]+[check(r) for r in read(freeze['path'])['artifacts']]
assert len(rows)==12
cb=read(T+'baseline-v1.json');old=[check(r) for r in cb['deduplicated_rows']]
assert len(old)==37
assert sha256(json.dumps(old,sort_keys=True,separators=(',',':')).encode()).hexdigest()==cb['deduplicated_summary_sha256']
rows+=old
authorities=[]
for name,expected in [
    ('reasoning-return-r8','33b8713d402d09f711d0096cdc4e8c00f9e622a5335f8e3345eb4f82ba0d359d'),
    ('reasoning-return-r5','f4f088adc133b0581520488cdbba30082c13b2402c96ae555142e5491ad4137d')]:
    ap='problems/2021-B4/reviews/'+name+'-acceptance.json';a=read(ap)
    assert a['unresolved_substantive_issues']==0 and a['repair_required'] is False
    pr=check(a['accepted_copy']);ca=check(a['candidate']);assert pr['sha256']==expected
    assert (ROOT/pr['path']).read_bytes().endswith((ROOT/ca['path']).read_bytes())
    bindings=[rec(ap),rec(ap[:-5]+'.md'),pr,ca];rows+=bindings
    authorities.append(dict(authority=bindings[0],accepted_body=pr,
        operative_complete_body_read=True,accepted_candidate_suffix_verified=True))
parent=check(dict(path='problems/2024-B4/notes/cofactor-dominant-r4-freeze-v1.json',
    bytes=3054,sha256='1d0c4e90c0b75a2417539401d4350e13dd29c9d3030fc06074f4cff18358371b'))
parent_payloads=[check(r) for r in read(parent['path'])['artifacts']]
assert len(parent_payloads)==10
rows+=[parent]+parent_payloads
unique={}
for row in rows:
    assert row['path'] not in unique or unique[row['path']]==row
    unique[row['path']]=row
ordered=[unique[k] for k in sorted(unique)]
expected=[str(i) for i in range(1,57)]
assert re.findall(r'^(\d+)\. ',(ROOT/(T+'obligations-v1.md')).read_text(),re.M)==expected
assert re.findall(r'^\| ER16-(\d{2}) \| PASS\.',(ROOT/(P+'ledger-v1.md')).read_text(),re.M)==[f'{i:02}' for i in range(1,57)]
out('baseline-v1.json',dict(captured_at_utc=NOW,administrative_integrity_only=True,
    target=target,constructor_freeze=freeze,accepted_authorities=authorities,
    current_occurrences=len(rows),deduplicated_paths=len(ordered),records=ordered,
    constructor_37_current_inputs_verified=True,
    own_parent=parent,own_parent_ten_payloads_verified=True,
    own_unrelated_2024_parent_NOT_a_2021_mathematical_premise=True,
    NO_NEW_corresponding_R16_R2_finding_file_hash_metadata_opened=True,
    NO_NEW_R15_R2_material_opened=True,no_recursive_historical_replay=True))
out('metadata-v1.json',dict(recorded_at_utc=NOW,reviewer='/root',
    constructor='/root/review_2021_reasoning_j15_r2',OTHER_NEW_nonconstructor=True,
    root_assignment_only_no_NEW_R16_inference=True,
    whole_obligations=56,all56_pass=True,
    all32_plus24_affine_E_zeros_and_all9_quartic_node_cases_independently_hand_reconstructed=True,
    substantive_issues=0,required_repairs=0,closed_scope_notes=5,
    ENTIRE_report_ledger_issues_sources_log_code_ALLmetadata_frozen_together=True,
    NO_NEW_corresponding_R2_finding_file_hash_metadata_opened=True,
    no_mathematical_program_CAS_scan_sample_author_source_or_freezer_rerun=True,
    requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),
    effective_settings_readback=None,candidate_promoted=False,
    OTHER_ENTIRE_R2_and_full_reconciliation_required=True,
    annual_degree20_fullm4_or_novelty_claim=False))
out('input-validation-v1.json',dict(validated_at_utc=NOW,
    administrative_integrity_only_not_proof=True,
    constructor_eleven_payloads_and_freeze_exact=True,
    all37_constructor_current_inputs_verified=True,
    two_current_accepted_authorities_and_suffixes_verified=True,
    own_parent_and_ten_payloads_unchanged=True,
    exact56_author_and_56_review_labels=True,
    current_occurrences=len(rows),deduplicated_paths=len(ordered),errors=[]))
suffixes=['initial-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md',
    'worklog-v1.md','freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
out('manifest-v1.json',dict(frozen_at_utc=NOW,
    status='ENTIRE initially blind OTHER WHOLE R16A-C review1',
    reviewer='/root',constructor='/root/review_2021_reasoning_j15_r2',
    exact_target=target,constructor_freeze=freeze,whole_obligations=56,
    all56_pass=True,substantive_issues=0,required_repairs=0,closed_scope_notes=5,
    ENTIRE_report_ledger_issues_source_log_code_ALLmetadata_frozen=True,
    NO_NEW_corresponding_R2_finding_file_hash_metadata_opened=True,
    own_parent=parent,other_ENTIRE_R2_and_full_reconciliation_required=True,
    promotion=False,artifacts=[rec(P+s) for s in suffixes]))
for row in read(P+'manifest-v1.json')['artifacts']:check(row)
for row in ordered:check(row)
print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'),report=rec(P+'initial-v1.md'),
    whole_obligations=56,new_review_files=10,current_occurrences=len(rows),
    deduplicated_paths=len(ordered),mathematical_computation=False),indent=2))
