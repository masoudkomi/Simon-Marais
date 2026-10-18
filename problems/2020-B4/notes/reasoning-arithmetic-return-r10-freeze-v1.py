#!/usr/bin/env python3
"""Exclusive administrative byte/JSON freeze. No mathematical computation."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path.cwd().resolve()
assert ROOT.name == 'Website' and (ROOT / 'AGENTS.md').is_file()
P = 'problems/2020-B4/notes/reasoning-arithmetic-return-r10-'
NOW = datetime.now(timezone.utc).isoformat()


def rec(path):
    raw = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


rows = []
unique = {}


def bind(path, label, expected=None):
    actual = rec(path)
    if expected is not None:
        assert actual == {key: expected[key] for key in ('path', 'bytes', 'sha256')}, path
    assert path not in unique or unique[path] == actual
    unique[path] = actual
    rows.append({'label': label, **actual})
    return actual


def out(suffix, obj):
    with (ROOT / (P + suffix)).open('x', encoding='utf-8') as handle:
        json.dump(obj, handle, indent=2, ensure_ascii=False)
        handle.write('\n')


parent_path = 'problems/2017-B4/reviews/coordinator-plane-recovery-r1-review-1-manifest-v1.json'
parent_rec = bind(parent_path, 'immutable own ENTIRE whole-review parent', {
    'path': parent_path, 'bytes': 3036,
    'sha256': 'e19485cd578e4d994ec220b824c90cc308844597e1a5cc6c493cd0e2add5c173'})
parent = json.loads((ROOT / parent_path).read_text())
assert parent['own_paths_after_this_packet'] == 551
for ending in ('metadata-v1.json', 'input-validation-v1.json'):
    item = next(x for x in parent['artifacts'] if x['path'].endswith(ending))
    bind(item['path'], 'compact necessary own-parent metadata', item)

a9_path = 'problems/2020-B4/notes/reasoning-arithmetic-return-r9-freeze-v1.json'
bind(a9_path, 'immutable A9 context, NOT mathematical premise', {
    'path': a9_path, 'bytes': 2811,
    'sha256': 'c90992cdc72cc411b8dbec2b811bbd39fb3e9e948e1559dd4e6163487a4ec5ef'})

for path, label in (
    ('AGENTS.md', 'current protocol'),
    ('problems/2020-B4/statement.md', 'exact official-domain normalization'),
    ('problems/2020-B4/references.md', 'complete actual local source map'),
    ('problems/2020-B4/notes/deep-literature-r1-report-v1.md', 'complete deep-literature report reread'),
):
    bind(path, label)

for number in (7, 8):
    path = f'problems/2020-B4/reviews/reasoning-return-r{number}-acceptance.json'
    bind(path, f'accepted R{number} exact scope authority')
    authority = json.loads((ROOT / path).read_text())
    assert authority['unresolved_substantive_issues'] == 0 and not authority['repair_required']
    item = authority['accepted_copy']
    bind(item['path'], f'accepted R{number} main identity', item)

paper_path = '.cache/literature/2020/reasoning-arithmetic-return-r10-schmidt-class-1998.pdf'
paper = bind(paper_path, 'NEW ignored public primary paper, not tracked proof artifact', {
    'path': paper_path, 'bytes': 227434,
    'sha256': 'f97dd90e1c72ea1b3f8eefae5272b58068b4e15a5dc23578cd7d937dc56dbeb5'})
assert (ROOT / paper_path).read_bytes().startswith(b'%PDF-')

ordered = [unique[path] for path in sorted(unique)]
canonical_hash = sha256(json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
ids = re.findall(r'^\|(\d{2})\|', (ROOT / (P + 'obligations-v1.md')).read_text(), re.M)
assert ids == [f'{number:02d}' for number in range(1, 53)]
assert 'Candidate proof - unverified' in (ROOT / (P + 'candidate-v1.md')).read_text()

out('baseline-v1.json', {
    'captured_at_utc': NOW,
    'scope': 'compact selected immutable parent, accepted inputs, and ignored primary-source fingerprint',
    'immutable_own_parent': parent_rec,
    'historical_own_research_paths_bound': 551,
    'new_ignored_third_party_source_NOT_owned_proof_artifact': paper,
    'declared_occurrences_verified': len(rows),
    'deduplicated_paths_verified': len(ordered),
    'canonical_deduplicated_sha256': canonical_hash,
    'records': ordered,
    'occurrence_labels': [{'label': item['label'], 'path': item['path']} for item in rows],
    'old_history_recursively_rehashed_or_recopied': False,
})

out('metadata-v1.json', {
    'status': 'candidate proof - unverified; COMPLETE ENTIRE R10 constructor checkpoint',
    'constructor': '/root/review_2017_coarsening_r1',
    'requested_model': 'gpt-6.1-sol',
    'requested_reasoning': 'max',
    'independently_verified_effective_setting_readback': None,
    'root_generic_assignment_supplied_new_proof_inference': False,
    'old_C_roles_disclosed': True,
    'claims': ['M10A actual ideal-class/residue Chebotarev selection',
               'M10B actual minimal mixed type-image realization and O_F Weil atomicity',
               'M10C nontrivial minus group supplies a nonzero type image and infinite semiprime norms',
               'M10D exact weighted integral lift and binary defect',
               'M10E hand-complete quadratic mixed example and congruence-matching family'],
    'full_obligations': 52,
    'A9_unverified_constructor_not_a_mathematical_premise': True,
    'new_A9_peer_reports_findings_or_metadata_read': False,
    'new_R10_findings_withheld_until_root_A9_ENTIRE_initial_confirmed_frozen': True,
    'queued_NEW2022_target_and_peer_reviews_unread_before_R10_freeze': True,
    'actual_integral_generators_not_only_abstract_class_patterns': True,
    'atomicity_only_in_same_O_F_integer_norm_Weil_monoid': True,
    'no_control_N_equals_q0_or_full_composite_character_tuple': True,
    'published_classical_CFT_imports_attributed': True,
    'primary_1998_author_manuscript_ALL16_pages_actually_read_visually': True,
    'entire_CFT296page_foundation_reconstruction_claimed': False,
    'source_diagnostic_confined_to_literal_general_m_real_unit_claim_not_blanket_refutation': True,
    'no_mathcode_CAS_scan_classgroup_machine_calculation_author_rerun': True,
    'only_new_code_administrative_hash_JSON_or_source_copy': True,
    'public_download_max_seconds': 30,
    'download_and_all_source_render_jobs_completed_no_pending_job_or_approval': True,
    'no_old_cache_or_shared_Git_mutation_charge_contact_or_bypass': True,
    'two_OTHER_initially_blind_ENTIRE_WHOLE_audits_required': True,
    'no_new_taut_order_exclusion_annual_classification_or_novelty_claim': True,
    'latest_direct_budget': {'at_utc': '2026-10-18 01:32:57 UTC', 'used_percent_TOTAL': 8,
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
    'canonical_deduplicated_sha256': canonical_hash,
    'all_selected_declared_fingerprints_match_before_and_after_new_writes': True,
    'all52_obligation_IDs_present_in_order': True,
    'immutable_own_parent_historical_paths': 551,
    'ignored_public_source_hash_verified_separately': True,
    'old531_or551_path_inventory_fresh_recursive_rehash_claimed': False,
    'administrative_integrity_only_not_mathematical_testing_or_promotion': True,
})

suffixes = ['candidate-v1.md', 'obligations-v1.md', 'sources-v1.md', 'failed-routes-v1.md',
            'worklog-v1.md', 'freeze-v1.py', 'baseline-v1.json', 'metadata-v1.json',
            'input-validation-v1.json']
out('freeze-v1.json', {
    'frozen_at_utc': NOW,
    'status': 'COMPLETE ENTIRE M10A--M10E constructor checkpoint - candidate proof unverified',
    'full_obligations': 52,
    'TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required': True,
    'root_supplied_no_new_M10_proof_inference': True,
    'immutable_own_parent': parent_rec,
    'historical_own_paths_bound': 551,
    'this_packet_paths_including_freeze': 10,
    'own_research_paths_after_this_packet': 561,
    'separate_ignored_third_party_pdf_not_owned_proof_artifact': paper,
    'declared_occurrences_verified': len(rows),
    'deduplicated_paths_verified': len(ordered),
    'genuine_mixed_realization_with_exact_target_size_gap_retained': True,
    'no_annual_taut_order_numerical_exclusion_or_novelty_promotion': True,
    'artifacts': [rec(P + suffix) for suffix in suffixes],
})
for path, expected in unique.items():
    assert rec(path) == expected, path
print(json.dumps({'complete_freeze': rec(P + 'freeze-v1.json'),
                  'main': rec(P + 'candidate-v1.md'), 'obligations': 52,
                  'declared_occurrences_verified': len(rows),
                  'deduplicated_paths_verified': len(ordered),
                  'historical_own_paths_bound': 551,
                  'own_paths_after_this_packet': 561}, indent=2))
