#!/usr/bin/env python3
"""Administrative byte freeze only. No mathematical computation or search."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path.cwd().resolve()
assert ROOT.name == 'Website' and (ROOT / 'AGENTS.md').is_file()
PREFIX = 'problems/2020-B4/notes/reasoning-arithmetic-return-r9-'
NOW = datetime.now(timezone.utc).isoformat()


def record(path):
    raw = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


occurrences = []
unique = {}


def bind(path, label, expected=None):
    actual = record(path)
    if expected is not None:
        assert actual == {k: expected[k] for k in ('path', 'bytes', 'sha256')}, (label, actual, expected)
    if path in unique:
        assert unique[path] == actual
    unique[path] = actual
    occurrences.append({'label': label, **actual})
    return actual


def write_new(suffix, obj):
    path = ROOT / (PREFIX + suffix)
    with path.open('x', encoding='utf-8') as out:
        json.dump(obj, out, indent=2, ensure_ascii=False)
        out.write('\n')


parent_path = 'problems/2025-B4/notes/reasoning-return-r9-freeze-v1.1.json'
parent_expected = {'path': parent_path, 'bytes': 3132,
                   'sha256': '45767fbfab81b90bd6aeb2610fd205408f91330482718a5957608144d9205e8c'}
parent_record = bind(parent_path, 'immutable own parent; transitive preservation only', parent_expected)
parent = json.loads((ROOT / parent_path).read_text())
assert parent['own_paths_after_interlude_and_this_packet'] == 530
for name in ('metadata-v1.1.json', 'input-validation-v1.1.json'):
    path = 'problems/2025-B4/notes/reasoning-return-r9-' + name
    declared = next(x for x in parent['artifacts'] if x['path'] == path)
    bind(path, 'necessary immutable parent metadata', declared)

interlude = bind('problems/2025-B4/notes/reasoning-return-r9-positive-live-v2.md',
                 'separate prior interim file, not a mathematical premise')

for path, label in (
    ('AGENTS.md', 'current protocol'),
    ('problems/2020-B4/statement.md', 'complete exact open domain'),
    ('problems/2020-B4/references.md', 'complete local source map'),
    ('problems/2020-B4/notes/deep-literature-r1-manifest-v1.json', 'immutable literature parent'),
    ('problems/2020-B4/notes/reasoning-return-r8-source-audit-v1.md', 'complete accepted operative source audit'),
):
    bind(path, label)

deep = json.loads((ROOT / 'problems/2020-B4/notes/deep-literature-r1-manifest-v1.json').read_text())
report = next(x for x in deep['artifacts'] if x['path'].endswith('-report-v1.md'))
bind(report['path'], 'complete deep-literature report', report)

for number in range(4, 9):
    path = f'problems/2020-B4/reviews/reasoning-return-r{number}-acceptance.json'
    bind(path, f'accepted R{number} coordinator authority; not a new review')
    acceptance = json.loads((ROOT / path).read_text())
    accepted = acceptance['accepted_copy']
    bind(accepted['path'], f'COMPLETE accepted R{number} body/header', accepted)

r8_authority = json.loads((ROOT / 'problems/2020-B4/reviews/reasoning-return-r8-acceptance.json').read_text())
for ending in ('reasoning-return-r8-freeze-v1.json', 'reasoning-return-r8-sources-v1.json'):
    expected = next(x for x in r8_authority['verification_metadata'] if x['path'].endswith(ending))
    bind(expected['path'], 'necessary original R8 declared source/freeze fingerprint', expected)

# Explicit prior handoff identities are independently checked in addition
# to the coordinator's current accepted-copy declarations.
bind('problems/2020-B4/proofs/reviewed-reasoning-return-r8-v1.1.md',
     'prior assigned exact R8 identity',
     {'path': 'problems/2020-B4/proofs/reviewed-reasoning-return-r8-v1.1.md',
      'bytes': 29871, 'sha256': '9003af18926d1fe49d3f997b40ed070ceefa37e42f73c5a98c32bbe7a2f3bfcb'})
bind('problems/2020-B4/proofs/reviewed-reasoning-return-r7-v1.1.md',
     'prior assigned exact R7 identity',
     {'path': 'problems/2020-B4/proofs/reviewed-reasoning-return-r7-v1.1.md',
      'bytes': 23717, 'sha256': '7517c6ffd5aff1135107020f9526922203496415515afb4bbd07176fb445d479'})

ordered = [unique[path] for path in sorted(unique)]
summary_hash = sha256(json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
ids = [int(x) for x in re.findall(r'^\|(\d{2})\|', (ROOT / (PREFIX + 'obligations-v1.md')).read_text(), re.M)]
assert ids == list(range(1, 57)), ids
assert 'Candidate proof - unverified' in (ROOT / (PREFIX + 'candidate-v1.md')).read_text()

write_new('baseline-v1.json', {
    'captured_at_utc': NOW,
    'scope': 'compact selected-input validation; transitive old preservation, no recursive inventory copy',
    'immutable_own_parent': parent_record,
    'historical_own_paths_bound_by_parent': 530,
    'separate_prior_interim_path': interlude,
    'prior_own_paths_after_interim': 531,
    'declared_occurrences': len(occurrences),
    'deduplicated_paths': len(ordered),
    'canonical_deduplicated_summary_sha256': summary_hash,
    'records': ordered,
    'occurrence_labels': [{'label': x['label'], 'path': x['path']} for x in occurrences],
})

write_new('metadata-v1.json', {
    'status': 'candidate proof - unverified; COMPLETE constructor checkpoint',
    'constructor': '/root/review_2017_coarsening_r1',
    'requested_model': 'gpt-6.1-sol',
    'requested_reasoning': 'max',
    'independently_verified_effective_setting_readback': None,
    'claims': ['A9A known published bound, prime-case reconstruction',
               'A9B arbitrary supported norm/unit correction',
               'A9C compulsory minus-class orders',
               'A9D both easy R8 tests imply primepower',
               'A9E actual squarefree minimal class cancellation',
               'A9F exact small-multiplier gap'],
    'full_obligations': 56,
    'root_generic_assignment_supplied_new_proof_inference': False,
    'old_C_R3_R6_construction_and_R4_R5_R7_review_roles_disclosed': True,
    'source_and_full_proof_read_limits': PREFIX + 'sources-v1.md',
    'known_Leung_Schmidt_bound_and_classical_norm_theorems_attributed': True,
    'two_OTHER_initially_blind_ENTIRE_WHOLE_audits_required': True,
    'new_numerical_order_scan_CAS_classgroup_calculation_or_author_rerun': False,
    'only_python_is_this_administrative_freezer': True,
    'no_download_cache_mutation_contact_charge_bypass_or_pending_approval': True,
    'mixed_actual_class_cancellation_still_open': True,
    'unrestricted_even_class_composite_modulus_or_classicality_conclusion': False,
    'new_taut_order_annual_solution_or_novelty_claim': False,
    'latest_direct_budget': {
        'at_utc': '2026-10-18 01:13:51 UTC',
        'used_percent_TOTAL': 7,
        'window_duration_minutes': 10080,
        'reset': 1792874445,
        'ordinary_allowed': True,
        'explicit_new_window_authorization': True,
        'ceiling_TOTAL_with_reserve': 90,
        'automatic_further_reset_spending': False,
    },
})

for path, expected in unique.items():
    assert record(path) == expected, path
write_new('input-validation-v1.json', {
    'validated_at_utc': NOW,
    'declared_occurrences_verified': len(occurrences),
    'deduplicated_paths_verified': len(ordered),
    'canonical_deduplicated_summary_sha256': summary_hash,
    'all_selected_declared_fingerprints_match_before_and_after_new_writes': True,
    'all56_obligation_IDs_present_in_order': True,
    'compact_parent_declared_historical_paths': 530,
    'separate_prior_interim_paths': 1,
    'fresh_full_rehash_of_all531_unrelated_historical_paths_claimed': False,
    'administrative_validation_not_mathematical_testing_or_promotion': True,
})

suffixes = ['candidate-v1.md', 'obligations-v1.md', 'sources-v1.md',
            'failed-routes-v1.md', 'worklog-v1.md', 'freeze-v1.py',
            'baseline-v1.json', 'metadata-v1.json', 'input-validation-v1.json']
write_new('freeze-v1.json', {
    'frozen_at_utc': NOW,
    'status': 'COMPLETE ENTIRE arithmetic R9 constructor checkpoint - candidate proof unverified',
    'claims': 'A9A--A9F in exact stated restricted domains',
    'published_small_norm_bound_attributed_not_new': True,
    'full_obligations': 56,
    'two_OTHER_initially_blind_ENTIRE_WHOLE_audits_required': True,
    'constructor_cannot_promote': True,
    'immutable_own_parent': parent_record,
    'historical_own_paths_bound': 530,
    'separate_prior_interim_paths': 1,
    'prior_own_paths': 531,
    'this_packet_paths_including_freeze': 10,
    'own_paths_after_this_packet': 541,
    'declared_occurrences_verified': len(occurrences),
    'deduplicated_paths_verified': len(ordered),
    'mixed_actual_cancellation_unrestricted_primepower_and_annual_open': True,
    'artifacts': [record(PREFIX + suffix) for suffix in suffixes],
})
print(json.dumps({'complete_freeze': record(PREFIX + 'freeze-v1.json'),
                  'main': record(PREFIX + 'candidate-v1.md'),
                  'obligations': 56,
                  'declared_occurrences_verified': len(occurrences),
                  'deduplicated_paths_verified': len(ordered),
                  'old_own_paths_bound': 531,
                  'own_paths_after_new_packet': 541}, indent=2))
