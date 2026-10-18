#!/usr/bin/env python3
"""Whole review integrity only. No mathematical computation or peer access."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json, re

ROOT=Path.cwd().resolve()
P='problems/2021-B4/reviews/reasoning-unit-return-r15-review-1-'
T='problems/2021-B4/notes/reasoning-unit-return-r15-'
NOW=datetime.now(timezone.utc).isoformat()
def rec(path):
    assert not path.startswith('problems/2021-B4/reviews/reasoning-unit-return-r15-review-2-')
    raw=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(raw),sha256=sha256(raw).hexdigest())
def check(row):
    actual=rec(row['path'])
    assert actual=={k:row[k] for k in ('path','bytes','sha256')},row['path']
    return actual
def read(path):return json.loads((ROOT/path).read_text())
def out(suffix,obj):
    with (ROOT/(P+suffix)).open('x') as f:
        json.dump(obj,f,indent=2);f.write('\n')

target=check(dict(path=T+'candidate-v1.md',bytes=17560,
    sha256='48700c4ed0462f6e916228083ede2520efc8b435be1e8e11d07d3233827c893c'))
freeze=check(dict(path=T+'freeze-v1.json',bytes=6170,
    sha256='0d2e246accd461704850f34ca056576e2f64ca6247b2fd08538c935535f77f48'))
f=read(freeze['path']);records={freeze['path']:freeze}
for row in f['artifacts']:records[row['path']]=check(row)
assert len(records)==11
cb=read(T+'baseline-v1.json')
old=[check(row) for row in cb['deduplicated_rows']]
assert len(old)==28
for row in old:records[row['path']]=row
assert cb['deduplicated_summary_sha256']==sha256(json.dumps(
    old,sort_keys=True,separators=(',',':')).encode()).hexdigest()
for name in ['reasoning-return-r13','reasoning-return-r14']:
    ap='problems/2021-B4/reviews/'+name+'-acceptance.json'
    a=read(ap)
    assert a['unresolved_substantive_issues']==0 and a['repair_required'] is False
    for path in [ap,ap[:-5]+'.md']:records[path]=rec(path)
    for key in ['candidate','accepted_copy']:
        actual=check(a[key]);records[actual['path']]=actual
    assert (ROOT/a['accepted_copy']['path']).read_bytes().endswith(
        (ROOT/a['candidate']['path']).read_bytes())
for path in ['AGENTS.md','problems/2021-B4/statement.md']:records[path]=rec(path)
parent=check(dict(path='problems/2017-B4/notes/coordinator-weighted-cutpath-r1-freeze-v1.json',
    bytes=2672,sha256='2ff11ebea88c684a2d86be972ae6f937ec5aec95040904eb27fc5c392ad7b4d4'))
records[parent['path']]=parent
pf=read(parent['path'])
for row in pf['artifacts']:check(row)
author_labels=re.findall(r'^\| R15-(\d{2}) \|',(ROOT/(T+'obligations-v1.md')).read_text(),re.M)
own_labels=re.findall(r'^\| R15-(\d{2}) \| PASS\.',(ROOT/(P+'ledger-v1.md')).read_text(),re.M)
assert author_labels==own_labels==[f'{i:02}' for i in range(1,49)]
out('baseline-v1.json',dict(recorded_at_utc=NOW,administrative_integrity_only=True,
    exact_target=target,constructor_freeze=freeze,
    current_direct_records=[records[k] for k in sorted(records)],
    constructor_28_direct_inputs_verified=True,
    constructor_direct_input_summary=cb['deduplicated_summary_sha256'],
    compact_own_parent=parent,own_parent_payloads_verified=len(pf['artifacts']),
    no_historical_recursive_replay=True,
    NO_NEW_corresponding_R2_findings_files_hashes_metadata_opened=True))
out('metadata-v1.json',dict(recorded_at_utc=NOW,reviewer='/root',
    constructor='/root/review_2021_reasoning_j15_r2',OTHER_NEW_nonconstructor=True,
    root_assignment_only_no_NEW_R15_mathematical_inference=True,
    whole_obligations=48,all48_pass=True,
    ALL96_affine_zeros_and_nine_final_products_independently_hand_reconstructed=True,
    substantive_issues=0,required_repairs=0,closed_scope_notes=3,
    ENTIRE_report_ledger_issues_sources_log_code_ALL_metadata_frozen_together=True,
    NO_NEW_corresponding_R2_findings_files_hashes_metadata_opened=True,
    no_math_program_CAS_scan_sample_author_rerun=True,
    requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),
    independently_verified_effective_settings=None,
    candidate_promotion=False,whole_R2_and_reconciliation_still_required=True,
    annual_degree20_or_novelty_claim=False))
out('input-validation-v1.json',dict(validated_at_utc=NOW,
    administrative_integrity_only_not_proof=True,
    constructor_payloads=10,constructor_freeze_verified=True,
    constructor_direct_inputs_verified=28,
    current_authorities_and_exact_suffixes_verified=['R13','R14'],
    compact_own_parent_payloads_verified=len(pf['artifacts']),
    exact_48_author_and_review_labels=True,all_exact_inputs_unchanged=True,errors=[]))
suffixes=['initial-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md',
    'worklog-v1.md','freeze-v1.py','baseline-v1.json','metadata-v1.json',
    'input-validation-v1.json']
out('manifest-v1.json',dict(frozen_at_utc=NOW,
    status='ENTIRE initially blind OTHER WHOLE R15A-C review1',
    reviewer='/root',constructor='/root/review_2021_reasoning_j15_r2',
    exact_target=target,constructor_freeze=freeze,whole_obligations=48,
    all48_pass=True,substantive_issues=0,required_repairs=0,closed_scope_notes=3,
    ENTIRE_report_ledger_issues_sources_log_code_ALL_metadata_frozen=True,
    NO_NEW_corresponding_R2_findings_files_hashes_metadata_opened=True,
    compact_own_parent=parent,other_whole_R2_and_reconciliation_required=True,
    promotion=False,artifacts=[rec(P+s) for s in suffixes]))
for row in read(P+'manifest-v1.json')['artifacts']:check(row)
print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'),
    main_review=rec(P+'initial-v1.md'),whole_obligations=48,
    new_review_paths=10,no_mathematical_computation=True),indent=2))
