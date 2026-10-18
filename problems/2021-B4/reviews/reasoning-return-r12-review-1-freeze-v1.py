#!/usr/bin/env python3
"""Administrative preservation only: no mathematical computation or replay."""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2021-B4/reviews/reasoning-return-r12-review-1-'
BASELINE = ROOT / (PREFIX + 'baseline-v1.json')
VALIDATION = ROOT / (PREFIX + 'input-validation-v1.json')
MANIFEST = ROOT / (PREFIX + 'manifest-v1.json')

def stamp():
    return datetime.now(timezone.utc).isoformat()

def record(path):
    raw = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

def check(expected):
    actual = record(expected['path'])
    assert actual == expected, (expected['path'], expected, actual)
    return actual

def dump_new(path, value):
    with path.open('x', encoding='utf-8') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')

def fingerprints(node):
    out = []
    if isinstance(node, dict):
        if (isinstance(node.get('path'), str) and isinstance(node.get('bytes'), int)
                and isinstance(node.get('sha256'), str)
                and re.fullmatch('[0-9a-f]{64}', node['sha256'])):
            out.append({k: node[k] for k in ('path', 'bytes', 'sha256')})
        for v in node.values():
            out.extend(fingerprints(v))
    elif isinstance(node, list):
        for v in node:
            out.extend(fingerprints(v))
    return out

def deduplicate(records):
    rows = {}
    for r in records:
        if r['path'] in rows:
            assert rows[r['path']] == r
        rows[r['path']] = r
    return [rows[p] for p in sorted(rows)]

def digest(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

assert not VALIDATION.exists() and not MANIFEST.exists(), 'freeze outputs already exist'
base = json.loads(BASELINE.read_text())
constructor = check(base['constructor_freeze'])
constructor_json = json.loads((ROOT / constructor['path']).read_text())
constructor_rows = [constructor] + constructor_json['artifacts']
assert len(constructor_rows) == 11
for row in constructor_rows:
    check(row)
assert constructor_json['whole_obligations'] == 60
assert constructor_json['root_supplied_NO_new_R12_mathematical_inference']

input_meta = check(base['constructor_current_input_metadata'])
input_json = json.loads((ROOT / input_meta['path']).read_text())
input_rows = fingerprints(input_json)
input_unique = deduplicate(input_rows)
assert len(input_rows) == 55 and len(input_unique) == 48
assert digest(input_unique) == base['necessary_current_summary']['canonical_deduplicated_summary_sha256']
for row in input_unique:
    assert not row['path'].startswith('problems/2021-B4/reviews/reasoning-return-r12-review-2-')
    check(row)

parent = check(base['immediate_own_parent_manifest'])
parent_json = json.loads((ROOT / parent['path']).read_text())
parent_rows = [parent] + parent_json['artifacts']
assert len(parent_rows) == 9
for row in parent_rows:
    check(row)
assert parent_json['older_plus_new_own_paths_bound_transitively'] == 475

all_rows = constructor_rows + input_rows + parent_rows
all_unique = deduplicate(all_rows)
for row in all_unique:
    check(row)

ledger = (ROOT / (PREFIX + 'ledger-v1.md')).read_text()
tags = re.findall(r'^\|R12-(\d{2})\|Pass\|', ledger, re.M)
assert tags == [f'{j:02d}' for j in range(1, 61)]
assert 'Unresolved substantive issues: 0' in (ROOT / (PREFIX + 'issues-v1.md')).read_text()

validation = {
    'verified_at_utc': stamp(),
    'administrative_only_no_mathcode_CAS_scan_or_certificate_replay': True,
    'constructor_manifest_and_payloads_verified': len(constructor_rows),
    'necessary_current_declared_fingerprint_occurrences_verified': len(input_rows),
    'necessary_current_unique_paths_verified': len(input_unique),
    'necessary_current_deduplicated_summary_sha256': digest(input_unique),
    'immediate_own_parent_manifest_and_payloads_verified': len(parent_rows),
    'all_current_fingerprint_occurrences_verified': len(all_rows),
    'all_current_unique_paths_verified': len(all_unique),
    'all_current_deduplicated_summary_sha256': digest(all_unique),
    'all60_whole_ledger_tags_present_once_in_order': True,
    'unresolved_substantive_issues': 0,
    'required_repairs': 0,
    'resolved_scope_notes': 4,
    'older_own_paths_bound_transitively_without_inventory_recopy': 475,
    'new_own_files_including_manifest': 9,
    'older_plus_new_own_paths_bound_transitively': 484,
    'immutable_constructor_parent_bound_not_historical_inventory_rewalked': constructor,
    'immutable_necessary_input_parent_bound_not_copied': input_meta,
    'immutable_immediate_own_parent_bound_not_historical_inventory_rewalked': parent,
    'all_old_target_shared_cache_and_Git_bytes_unmodified': True,
    'NEW_root_R12_peer_files_findings_source_or_metadata_unopened_before_ENTIRE_initial': True,
    'root_completion_identity_received_without_findings': True,
    'no_queued_2017_or_2025_repairs_opened_before_current_entire_freeze': True,
    'another_OTHER_whole_initial_and_root_reconciliation_required': True,
    'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max', 'inherited': True},
    'independently_verified_effective_settings': None,
    'telemetry': base['telemetry'],
}
dump_new(VALIDATION, validation)
payload_names = ['baseline-v1.json', 'initial.md', 'ledger-v1.md', 'issues-v1.md',
                 'source-checks-v1.md', 'sources-v1.json', 'freeze-v1.py', 'input-validation-v1.json']
payloads = [record(PREFIX + x) for x in payload_names]
manifest = {
    'frozen_at_utc': stamp(),
    'status': 'COMPLETE fresh initially blind NONCONSTRUCTOR WHOLE R12 initial review1; no substantive defect found; not coordinator promotion',
    'reviewer': '/root/review_2022_complexity_r2',
    'exact_target': base['exact_target'],
    'exact_constructor_freeze': constructor,
    'whole_claims': ['R12A', 'R12B', 'R12C'],
    'all60_obligations_and_every_new_hand_certificate_reconstructed': True,
    'unresolved_substantive_issues': 0,
    'required_author_repairs': 0,
    'resolved_scope_notes': 4,
    'root_supplied_NO_new_R12_mathematical_inference': True,
    'B_did_not_construct_NEW_R12': True,
    'A_NEW_constructor_excluded': True,
    'B_old_2021_R9_authorship_and_prior_review_roles_disclosed_no_self_recertification': True,
    'NEW_root_R12_peer_files_findings_source_or_metadata_unopened_through_ENTIRE_initial': True,
    'root_completion_identity_received_without_findings': True,
    'another_OTHER_whole_initial_and_coordinator_full_reconciliation_required': True,
    'no_full_J15_degree20_annual_rational_lift_height_or_novelty_claim': True,
    'no_mathcode_scan_CAS_native_mathematical_child_author_rerun_or_old_certificate_replay': True,
    'no_old_shared_Git_cache_edit_spawn_contact_charge_or_bypass': True,
    'precise_actual_source_and_accepted_premise_read_scopes_recorded': True,
    'necessary_current_summary': base['necessary_current_summary'],
    'compact_own_parent_manifest': parent,
    'older_own_paths_bound_transitively': 475,
    'new_own_files_including_manifest': 9,
    'older_plus_new_own_paths_bound_transitively': 484,
    'no_historical_inventory_recopied_or_recursively_rehashed': True,
    'requested_settings': validation['requested_settings'],
    'independently_verified_effective_settings': None,
    'authoritative_weekly_telemetry': base['telemetry'],
    'artifacts': payloads,
}
dump_new(MANIFEST, manifest)
for row in payloads + constructor_rows + input_unique + parent_rows:
    check(row)
print(json.dumps({'complete': True, 'manifest': record(PREFIX + 'manifest-v1.json'),
                  'validation': record(PREFIX + 'input-validation-v1.json'),
                  'whole_obligations': 60, 'issues': 0, 'repairs': 0,
                  'verified_occurrences': len(all_rows), 'unique_paths': len(all_unique),
                  'source_and_prior_bytes_preserved': True}, indent=2))
