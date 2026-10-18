#!/usr/bin/env python3
"""Exclusive review integrity records; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2022-B4/reviews/reasoning-seed-return-r1-review-1-'
T = 'problems/2022-B4/notes/reasoning-seed-return-r1-'
NOW = datetime.now(timezone.utc).isoformat()
assert ROOT.name == 'Website'

def rec(path):
    assert not path.startswith('problems/2022-B4/reviews/reasoning-seed-return-r1-review-2-')
    assert not path.startswith('problems/2024-B4/reviews/cofactor-global-r2-')
    raw = (ROOT/path).read_bytes()
    return dict(path=path, bytes=len(raw), sha256=sha256(raw).hexdigest())

def check(row):
    actual = rec(row['path'])
    assert actual == {k: row[k] for k in ('path','bytes','sha256')}, row['path']
    return actual

def read(path):
    rec(path)
    return json.loads((ROOT/path).read_text())

def out(suffix, obj):
    with (ROOT/(P+suffix)).open('x') as f:
        json.dump(obj, f, indent=2)
        f.write('\n')

target = check(dict(path=T+'candidate-v1.md', bytes=21030,
    sha256='a1caa31a57496ff17daaa78d8a085d9423801d2935a3476559c963b6c03f2584'))
freeze = check(dict(path=T+'freeze-v1.json', bytes=3871,
    sha256='78beb6e2f0f2ce43c51029f68bd42da1e9693cbcde63fa71c1d5df881443dccc'))
f = read(freeze['path'])
assert f['whole_obligations'] == 48
records = {freeze['path']:freeze}
for row in f['artifacts']:
    actual = check(row)
    records[actual['path']] = actual
assert len(records) == 10

cb = read(T+'baseline-v1.json')
old = [check(row) for row in cb['protected_direct_records']]
assert len(old) == 41 and len({row['path'] for row in old}) == 41
summary_hash = sha256(json.dumps(old, sort_keys=True, separators=(',',':')).encode()).hexdigest()
assert summary_hash == cb['summary']['canonical_record_array_sha256']
assert cb['summary'] == f['direct_fingerprint_summary']

for path in ['AGENTS.md','problems/2022-B4/statement.md']:
    records[path] = rec(path)
for stem in ['reasoning-return-r5','reasoning-complexity-return-r9-v3']:
    ap = 'problems/2022-B4/reviews/'+stem+'-acceptance.json'
    a = read(ap)
    assert a['unresolved_substantive_issues'] == 0 and a['repair_required'] is False
    for path in [ap,ap[:-5]+'.md']:
        records[path] = rec(path)
    for key in ['candidate','accepted_copy']:
        actual = check(a[key])
        records[actual['path']] = actual
    assert (ROOT/a['accepted_copy']['path']).read_bytes().endswith(
        (ROOT/a['candidate']['path']).read_bytes())

parent = check(dict(path='problems/2024-B4/notes/cofactor-global-r2-freeze-v1.json',
    bytes=2322,sha256='3e63984333d64dcfe8bb32395d28e948ab1023ce8f4ab367e0ea374d51dfeaef'))
records[parent['path']] = parent
parent_data = read(parent['path'])
for row in parent_data['artifacts']:
    check(row)
    if row['path'].endswith(('baseline-v1.json','metadata-v1.json','input-validation-v1.json')):
        records[row['path']] = rec(row['path'])

author_labels = re.findall(r'^\|SR-O(\d{2})\|', (ROOT/(T+'obligations-v1.md')).read_text(), re.M)
own_labels = re.findall(r'^\|SR-O(\d{2})\|PASS\.', (ROOT/(P+'ledger-v1.md')).read_text(), re.M)
assert author_labels == own_labels == [f'{i:02}' for i in range(1,49)]
out('baseline-v1.json',dict(captured_at_utc=NOW,administrative_integrity_only=True,
    exact_target=target,constructor_freeze=freeze,compact_own_parent=parent,
    direct_records=[records[k] for k in sorted(records)],
    constructor_old41_records_verified_one_level_not_copied=cb['summary'],
    historical_inventories_bound_not_recursively_replayed=True,
    NO_NEW_corresponding_R2_or_2024_CG_peer_material_opened=True))
out('metadata-v1.json',dict(recorded_at_utc=NOW,reviewer='/root',
    constructor='/root/review_2017_coarsening_r1',OTHER_nonconstructor_of_NEW_packet=True,
    old_root_F5_contribution_disclosed=True,whole_obligations=48,
    initial_independent=True,all48_pass=True,substantive_issues=0,required_repairs=0,
    closed_scope_notes=3,accepted_old_inputs_not_new_self_review=True,
    ENTIRE_report_ledger_issues_sources_worklog_code_ALL_metadata_frozen_together=True,
    NO_NEW_corresponding_R2_findings_files_hashes_metadata_opened=True,
    no_math_program_CAS_scan_sample_or_certificate_rerun=True,
    requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),
    independently_verified_effective_settings=None,
    candidate_promotion=False,complete_annual_answer_or_novelty_claim=False))
out('input-validation-v1.json',dict(validated_at_utc=NOW,
    administrative_integrity_only_not_proof=True,constructor_payloads=9,
    constructor_freeze_checked=True,constructor_direct_old_records_verified=41,
    compact_own_parent_artifacts_checked=len(parent_data['artifacts']),
    exact_48_author_and_review_labels=True,all_exact_records_unchanged=True,errors=[]))
suffixes=['initial-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md',
          'worklog-v1.md','freeze-v1.py','baseline-v1.json','metadata-v1.json',
          'input-validation-v1.json']
artifacts=[rec(P+s) for s in suffixes]
out('manifest-v1.json',dict(frozen_at_utc=NOW,
    status='ENTIRE initially blind OTHER WHOLE SR1-SR4 R1',reviewer='/root',
    constructor='/root/review_2017_coarsening_r1',exact_target=target,
    constructor_freeze=freeze,whole_obligations=48,all48_pass=True,
    substantive_issues=0,required_repairs=0,closed_scope_notes=3,
    compact_own_parent=parent,
    ENTIRE_report_ledger_issues_sources_worklog_code_ALL_metadata_frozen=True,
    NO_NEW_corresponding_R2_findings_files_hashes_metadata_opened=True,
    other_whole_R2_and_reconciliation_still_required=True,promotion=False,
    artifacts=artifacts))
final=read(P+'manifest-v1.json')
for row in final['artifacts']:
    check(row)
print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'),
    main_review=rec(P+'initial-v1.md'),whole_obligations=48,
    new_review_paths=10,no_math_computation=True),indent=2))
