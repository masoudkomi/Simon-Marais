#!/usr/bin/env python3
"""Exclusive review integrity freeze only; no mathematical code or author rerun."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path.cwd().resolve()
assert ROOT.name == 'Website' and (ROOT / 'AGENTS.md').is_file()
P = 'problems/2022-B4/reviews/reasoning-complexity-return-r9-review-2-'
TARGET = 'problems/2022-B4/notes/reasoning-complexity-return-r9-'
NOW = datetime.now(timezone.utc).isoformat()


def rec(path):
    raw = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


rows = []
unique = {}


def bind(expected, label):
    path = expected['path']
    actual = rec(path)
    assert actual == {key: expected[key] for key in ('path', 'bytes', 'sha256')}, (label, path)
    assert path not in unique or unique[path] == actual
    unique[path] = actual
    rows.append({'label': label, **actual})
    return actual


def out(suffix, obj):
    with (ROOT / (P + suffix)).open('x', encoding='utf-8') as handle:
        json.dump(obj, handle, indent=2, ensure_ascii=False)
        handle.write('\n')


target_freeze = bind({'path': TARGET + 'freeze-v1.json', 'bytes': 4389,
                     'sha256': '13f4c9b46055c02b5f535706aa338bcc5167ea719120075aa0616e1298669142'},
                    'exact assigned immutable constructor freeze')
target = json.loads((ROOT / target_freeze['path']).read_text())
for item in target['artifacts']:
    bind(item, 'complete constructor artifact, code read but not executed')
assert len(target['artifacts']) == 9
bind({'path': TARGET + 'candidate-v1.md', 'bytes': 16457,
      'sha256': '2fdb1a495afa4f607b9fb63b7a1535e7ba6797ae5b699fd9d25124b503bfe211'},
     'independent exact assigned main identity')

constructor_baseline = json.loads((ROOT / (TARGET + 'baseline-v1.json')).read_text())
constructor_validation = json.loads((ROOT / (TARGET + 'input-validation-v1.json')).read_text())
constructor_rows = []
for item in constructor_baseline['inputs']:
    constructor_rows.append(bind(item, 'declared direct constructor baseline input'))
for authority in constructor_validation['direct_current_authorities']:
    for item in authority['direct_records_verified']:
        constructor_rows.append(bind(item, 'declared direct accepted-authority input'))
assert len(constructor_rows) == 31
constructor_unique = {item['path']: item for item in constructor_rows}
constructor_canonical = [constructor_unique[path] for path in sorted(constructor_unique)]
constructor_digest = sha256(json.dumps(constructor_canonical, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
assert len(constructor_unique) == 27
assert constructor_digest == constructor_validation['canonical_deduplicated_summary_sha256']

parent_path = 'problems/2020-B4/notes/reasoning-arithmetic-return-r10-freeze-v1.json'
parent_rec = bind({'path': parent_path, 'bytes': 3016,
                   'sha256': '68dd827ca8c9f4156317022115f0981d818335508067299167cfd2d85541de43'},
                  'immutable own ENTIRE constructor parent')
parent = json.loads((ROOT / parent_path).read_text())
assert parent['own_research_paths_after_this_packet'] == 561
for ending in ('metadata-v1.json', 'input-validation-v1.json'):
    bind(next(item for item in parent['artifacts'] if item['path'].endswith(ending)),
         'compact necessary own-parent metadata')

ids = re.findall(r'^\|\s*(QO\d{2})\s*\|', (ROOT / (P + 'ledger-v1.md')).read_text(), re.M)
author_ids = re.findall(r'^\|\s*(QO\d{2})\s*\|', (ROOT / (TARGET + 'obligations-v1.md')).read_text(), re.M)
assert ids == author_ids == [f'QO{number:02d}' for number in range(1, 49)]
ordered = [unique[path] for path in sorted(unique)]
summary_hash = sha256(json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest()

out('baseline-v1.json', {
    'captured_at_utc': NOW,
    'scope': 'compact direct target/accepted authority inputs and immutable own parent only',
    'target_freeze': target_freeze,
    'immutable_own_parent': parent_rec,
    'historical_own_paths_bound': 561,
    'declared_occurrences_verified': len(rows),
    'deduplicated_paths_verified': len(ordered),
    'canonical_deduplicated_sha256': summary_hash,
    'constructor31_occurrences27_paths_digest_independently_matches': True,
    'records': ordered,
    'occurrence_labels': [{'label': item['label'], 'path': item['path']} for item in rows],
    'no_NEW_peer_R9_review_record_read_or_hashed': True,
    'old_history_recursively_rehashed_or_recopied': False,
})

out('metadata-v1.json', {
    'status': 'COMPLETE ENTIRE initially blind OTHER independent WHOLE R2',
    'reviewer': '/root/review_2017_coarsening_r1',
    'NEW_constructor': '/root/review_2022_complexity_r2',
    'constructor_excluded_from_OTHER_audit_count': True,
    'requested_model': 'gpt-6.1-sol',
    'requested_reasoning': 'max',
    'independently_verified_effective_setting_readback': None,
    'complete_target_all10_companions_read': True,
    'whole_author_obligations': 48,
    'whole_independent_ledger_rows': 48,
    'old_C_R4_R7_R8_authorship_and_other_review_roles_disclosed': True,
    'independent_NEW_proof_not_self_recertification_of_old_inputs': True,
    'official_and_primary_attributed_strip_context_read_no_preliminary_proof_reproduced': True,
    'no_NEW_peer_R9_report_findings_source_code_or_metadata_read_or_hashed': True,
    'no_premature_verdict_fragment_sent': True,
    'substantive_issues': 0,
    'requested_repairs': 0,
    'advisories': 0,
    'conclusion': 'no substantive defect identified in written Q1--Q4 inverse/conditional seed-reduction scope',
    'no_mathematical_code_CAS_orbit_scan_inverse_procedure_constructor_rerun': True,
    'only_new_code_is_administrative_byte_JSON_freezer': True,
    'no_download_cache_shared_Git_mutation_charge_contact_bypass_or_pending_job': True,
    'no_actual_survivor_residual_hitting_annual_or_novelty_promotion': True,
    'findings_withheld_until_other_ENTIRE_initial_freeze_confirmation': True,
    'coordinator_and_SECOND_OTHER_whole_audit_still_required': True,
    'latest_direct_budget': {'at_utc': '2026-10-18 01:43:37 UTC', 'used_percent_TOTAL': 9,
                             'window_duration_minutes': 10080, 'reset': 1792874445,
                             'ordinary_allowed': True, 'explicit_current_window_authorization': True,
                             'ceiling_TOTAL_with_reserve': 90, 'automatic_further_reset_spending': False},
})
for path, expected in unique.items():
    assert rec(path) == expected, path
out('input-validation-v1.json', {
    'verified_at_utc': NOW,
    'declared_occurrences_verified': len(rows),
    'deduplicated_paths_verified': len(ordered),
    'canonical_deduplicated_sha256': summary_hash,
    'target_freeze_and_all9_artifacts_match': True,
    'all_constructor31_direct_input_occurrences_match': True,
    'constructor27_path_canonical_digest_matches': True,
    'all_selected_inputs_unchanged_before_and_after_new_writes': True,
    'all48_author_IDs_equal_all48_review_ledger_IDs_in_order': True,
    'compact_own_parent_historical_paths': 561,
    'no_NEW_peer_review_material_read_or_hashed': True,
    'administrative_integrity_only_not_mathematical_testing': True,
})

suffixes = ['initial-v1.md', 'ledger-v1.md', 'issues-v1.md', 'source-checks-v1.md',
            'worklog-v1.md', 'freeze-v1.py', 'baseline-v1.json', 'metadata-v1.json',
            'input-validation-v1.json']
out('manifest-v1.json', {
    'frozen_at_utc': NOW,
    'status': 'ENTIRE initially blind OTHER independent WHOLE R2 frozen before any NEW peer material',
    'whole_author_obligations': 48,
    'complete_whole_review': True,
    'substantive_issues': 0,
    'requested_repairs': 0,
    'advisories': 0,
    'target_freeze': target_freeze,
    'immutable_own_parent': parent_rec,
    'historical_own_paths_bound': 561,
    'this_packet_paths_including_manifest': 10,
    'own_paths_after_this_packet': 571,
    'declared_occurrences_verified': len(rows),
    'deduplicated_paths_verified': len(ordered),
    'old_constructor_roles_disclosed_no_self_recertification': True,
    'no_NEW_peer_review_file_or_hash_accessed': True,
    'findings_withheld_until_other_ENTIRE_initial_confirmation': True,
    'no_coordinator_promotion_or_annual_claim': True,
    'artifacts': [rec(P + suffix) for suffix in suffixes],
})
for path, expected in unique.items():
    assert rec(path) == expected, path
print(json.dumps({'manifest': rec(P + 'manifest-v1.json'),
                  'whole_report': rec(P + 'initial-v1.md'),
                  'all48': True,
                  'declared_occurrences_verified': len(rows),
                  'deduplicated_paths_verified': len(ordered),
                  'peer_blind_through_ENTIRE_freeze': True}, indent=2))
