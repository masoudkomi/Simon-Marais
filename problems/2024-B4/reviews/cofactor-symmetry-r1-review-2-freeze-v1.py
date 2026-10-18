#!/usr/bin/env python3
"""Exclusive administrative review freeze; NO mathematical computation."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2024-B4/reviews/cofactor-symmetry-r1-review-2-'
C = 'problems/2024-B4/notes/cofactor-symmetry-r1-'
FORBIDDEN = 'problems/2024-B4/reviews/cofactor-symmetry-r1-review-1-'
assert ROOT.name == 'Website' and (ROOT/'AGENTS.md').is_file()
NOW = datetime.now(timezone.utc).isoformat()

def rec(path):
    assert not path.startswith(FORBIDDEN), 'NEW peer material forbidden'
    b = (ROOT/path).read_bytes()
    return dict(path=path, bytes=len(b), sha256=sha256(b).hexdigest())

def read(path):
    assert not path.startswith(FORBIDDEN)
    return json.loads((ROOT/path).read_text())

def out(suffix, obj):
    with (ROOT/(P+suffix)).open('x', encoding='utf-8') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
        f.write('\n')

records = {}
occurrences = []
def bind(path, label, expected=None):
    r = rec(path)
    if expected is not None:
        assert r == {k: expected[k] for k in ('path','bytes','sha256')}, path
    assert path not in records or records[path] == r, path
    records[path] = r
    occurrences.append(dict(label=label, path=path))
    return r

constructor_freeze = bind(C+'freeze-v1.json', 'ENTIRE constructor freeze', dict(
    path=C+'freeze-v1.json', bytes=2406,
    sha256='2fdb3fc025f2bf89e6d3bdf060373103fecf428db8ff4f407f170bed86bab327'))
cf = read(C+'freeze-v1.json')
assert len(cf['artifacts']) == 8 and cf['all_obligations'] == 48
for row in cf['artifacts']:
    assert row['path'].startswith(C)
    bind(row['path'], 'exact constructor artifact', row)
assert rec(C+'candidate-v1.md') == dict(path=C+'candidate-v1.md', bytes=14531,
    sha256='77eb040ac77e255d3b8e8b38e47d6329857fc8af0d31eeb49cd0880b2763fbc1')
cb = read(C+'baseline-v1.json')
assert cb['summary'] == cf['current_input_summary']
assert len(cb['records']) == cb['summary']['unique_paths'] == 18
assert len(cb['occurrence_labels']) == cb['summary']['occurrences'] == 18
assert sha256(json.dumps(cb['records'], sort_keys=True,
    separators=(',',':')).encode()).hexdigest() == cb['summary']['sha256']
for row in cb['records']:
    bind(row['path'], 'declared constructor old-input fingerprint', row)

own_parent_path = 'problems/2017-B4/notes/reasoning-global-return-r7-freeze-v1.json'
own_parent = bind(own_parent_path, 'compact immutable own parent', dict(
    path=own_parent_path, bytes=3015,
    sha256='545e1131036b4e298bfb2957584e2186e6b92a2f0c94ed3f2b4a4036653d9199'))
op = read(own_parent_path)
assert op['own_paths_after_this_packet'] == 612
for row in op['artifacts']:
    if row['path'].endswith(('metadata-v1.json','input-validation-v1.json')):
        bind(row['path'], 'necessary compact own-parent metadata', row)

for path,key,suffix_expected in [
    ('problems/2024-B4/reviews/coordinator-F8-pencil-r1-acceptance.json','accepted_copy',True),
    ('problems/2024-B4/reviews/structural-acceptance.json','accepted_proof',False),
    ('problems/2024-B4/reviews/coordinator-neighbor-Frobenius-r1-acceptance.json','accepted_copy',True)]:
    a = read(path)
    assert a.get('unresolved_substantive_issues', a.get('remaining_substantive_objections')) == 0
    assert rec(a[key]['path']) == {k:a[key][k] for k in ('path','bytes','sha256')}
    assert rec(a['candidate']['path']) == {k:a['candidate'][k] for k in ('path','bytes','sha256')}
    if suffix_expected:
        assert (ROOT/a[key]['path']).read_bytes().endswith(
            (ROOT/a['candidate']['path']).read_bytes())

ids = [f'{i:02d}' for i in range(1,49)]
for path in [C+'obligations-v1.md', P+'ledger-v1.md']:
    assert re.findall(r'^\|(\d{2})\|', (ROOT/path).read_text(), re.M) == ids
assert 'candidate proof - unverified' in (ROOT/(P+'initial-v1.md')).read_text()

ordered = [records[p] for p in sorted(records)]
summary = dict(occurrences=len(occurrences), unique_paths=len(ordered), sha256=sha256(
    json.dumps(ordered, sort_keys=True, separators=(',',':')).encode()).hexdigest())
assert len(occurrences) == len(ordered) == 30
out('baseline-v1.json', dict(captured_at_utc=NOW,
    operation='direct file bytes/SHA and named JSON; not mathematics',
    constructor_freeze=constructor_freeze, compact_own_parent=own_parent,
    own_historical_paths_bound_without_recursive_inventory=612,
    constructor_old_input_summary=cb['summary'], summary=summary,
    records=ordered, occurrence_labels=occurrences,
    NEW_corresponding_peer_material_read_or_hashed=False))

out('metadata-v1.json', dict(status='ENTIRE initially blind OTHER WHOLE review R2 frozen',
    reviewer='/root/review_2017_coarsening_r1', constructor='/root',
    new_constructor_excluded=True, old_roles_disclosed=True,
    no_NEW_problem_specific_construction_or_repair_contribution=True,
    requested_settings=dict(model='gpt-6.1-sol', reasoning='max', inherited=True),
    independently_verified_effective_settings=None,
    whole_obligations=48, all48_reconstructed=True,
    substantive_issues=0, required_mathematical_repairs=0,
    closed_nonblocking_operational_timestamp_notes=1,
    mathematical_verdict_withheld_until_BOTH_ENTIRE_initials_confirmed=True,
    NEW_corresponding_peer_files_findings_hashes_metadata_read=False,
    no_mathematical_program_CAS_scan_or_author_rerun=True,
    no_old_shared_Git_cache_mutation_spawn_contact_charge_or_bypass=True,
    source=dict(Fulton_5_4_Theorem2_entire_operative_proof_read=True,
        characteristic_2_hypotheses_checked=True, reduced_component_correction_explicit=True,
        no_full_book_or_new_source_binary_hash_claim=True),
    exact_domain=dict(q='8^k', k_minimum=2, q_minimum=64, n='7q+1',
        combined_family='7*2^a+1, a>=2, a!=3'),
    no_annual_solution_or_priority_promotion=True,
    compact_own_parent=own_parent, own_historical_paths_bound=612,
    new_packet_paths_including_manifest=10, own_paths_after_this_packet=622,
    fingerprint_summary=summary,
    latest_direct_weekly_telemetry=dict(observed_at_utc='2026-10-18 07:46:18 UTC',
        source='mcp__codex_app__get_usage_limits; legacy/by-limit primary agree',
        used_percent_TOTAL=14, window_minutes=10080, reset_unix=1792874445,
        ordinary_usage_allowed=True, current_window_explicitly_authorized=True,
        ceiling_percent_TOTAL_with_review_integration_reserve=90,
        automatic_later_window_spending=False)))

for path,row in records.items():
    assert rec(path) == row, path
out('input-validation-v1.json', dict(validated_at_utc=NOW,
    administrative_only_not_mathematical_validation=True,
    fingerprint_summary=summary, constructor_all9_artifacts_verified=True,
    constructor_all18_declared_old_input_fingerprints_verified=True,
    exact_accepted_FP_NF_candidate_suffixes_verified=True,
    T1_historical_heading_editorial_change_disclosed_no_literal_suffix_assertion=True,
    all48_author_and_review_ledger_IDs_once_in_order=True,
    compact_own_parent=own_parent, prior_own_paths_bound=612,
    no_recursive_old_inventory_copy_or_rehash=True,
    no_NEW_corresponding_peer_read_or_hash=True, errors=[]))

suffixes = ['initial-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md',
    'worklog-v1.md','freeze-v1.py','baseline-v1.json','metadata-v1.json',
    'input-validation-v1.json']
out('manifest-v1.json', dict(frozen_at_utc=NOW,
    status='ENTIRE OTHER initially blind WHOLE FS1–FS5 review R2',
    reviewer='/root/review_2017_coarsening_r1', whole_obligations=48,
    report_ALL48_ledger_issues_sources_worklog_code_ALL_metadata_frozen=True,
    no_NEW_corresponding_peer_material_read_or_hashed_before_ENTIRE_freeze=True,
    mathematical_verdict_withheld_until_BOTH_ENTIRE_initials=True,
    no_mathematical_code_or_proof_promotion=True,
    constructor_freeze=constructor_freeze, compact_own_parent=own_parent,
    prior_own_paths_bound=612, new_packet_paths_including_manifest=10,
    own_paths_after_this_packet=622, fingerprint_summary=summary,
    artifacts=[rec(P+s) for s in suffixes]))
for path,row in records.items():
    assert rec(path) == row, path
print(json.dumps(dict(manifest=rec(P+'manifest-v1.json'),
    report=rec(P+'initial-v1.md'), whole_obligations=48,
    input_summary=summary, mathematical_verdict='withheld pending both entire freezes'), indent=2))
