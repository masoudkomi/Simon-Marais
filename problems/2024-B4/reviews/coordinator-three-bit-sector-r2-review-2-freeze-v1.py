"""Create-new administrative WHOLE review freeze; no mathematical evaluation."""
from pathlib import Path
import datetime
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2024-B4/reviews/coordinator-three-bit-sector-r2-review-2-'
TARGET = 'problems/2024-B4/notes/coordinator-three-bit-sector-r2-'
PARENT = 'problems/2017-B4/notes/reasoning-value-return-r6-freeze-v1.json'
AUTHORITIES = ['problems/2024-B4/reviews/structural-acceptance.json',
               'problems/2024-B4/reviews/reasoning-sector3-return-r1-acceptance.json']
KNOWN = {
    TARGET+'candidate-v1.md': (17804, '59a3ec87e15f9238c5735cf2eb6fe650535fd7ddaf0a73c3f540fa08bf785163'),
    TARGET+'freeze-v1.json': (2773, '44882af00dd7165b42b9d619f326a06a90bf52febba8ca0379226c68bc4e243f'),
    PARENT: (3298, 'aba8108ec5191eb5c6d2702944d74c340c06ff949938bbe0bcd197b34998e9d4'),
}


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def path(rel):
    p = (ROOT/rel).resolve()
    assert p.is_relative_to(ROOT)
    if '/reviews/coordinator-three-bit-sector-r' in rel:
        assert rel.startswith(PREFIX), 'NEW peer audit is forbidden: '+rel
    return p


def fp(rel):
    data = path(rel).read_bytes()
    return {'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def rows(value):
    if isinstance(value, dict):
        if all(k in value for k in ('path', 'bytes', 'sha256')):
            yield {k:value[k] for k in ('path', 'bytes', 'sha256')}
        for child in value.values():
            yield from rows(child)
    elif isinstance(value, list):
        for child in value:
            yield from rows(child)


def check(row):
    assert fp(row['path']) == row, row['path']


def write_new(suffix, value):
    with path(PREFIX+suffix).open('x') as stream:
        stream.write(json.dumps(value, indent=2)+'\n')


if __name__ == '__main__':
    assert not path(PREFIX+'manifest-v1.json').exists()
    expected = {'initial-v1.md', 'issues-v1.md', 'ledger-v1.md',
                'sources-v1.md', 'worklog-v1.md', 'freeze-v1.py'}
    assert {p.name.removeprefix(Path(PREFIX).name)
            for p in path('problems/2024-B4/reviews').glob(Path(PREFIX).name+'*')} == expected
    for rel, (size, sha) in KNOWN.items():
        actual = fp(rel)
        assert (actual['bytes'], actual['sha256']) == (size, sha), rel

    immutable = [TARGET+'freeze-v1.json', TARGET+'inputs-v1.json', PARENT] + AUTHORITIES
    bound = []
    for rel in immutable:
        bound.append(fp(rel))
        bound.extend(rows(json.loads(path(rel).read_text())))
    bound.extend(fp(rel) for rel in ['AGENTS.md', 'problems/2024-B4/statement.md'])
    unique = {}
    for row in bound:
        check(row)
        previous = unique.setdefault(row['path'], row)
        assert previous == row, row['path']

    expected_ids = [f'{i:02d}' for i in range(1,45)]
    target_ids = re.findall(r'^\|R2-(\d\d)\|', path(TARGET+'obligations-v1.md').read_text(), re.M)
    own_ids = re.findall(r'^\|R2-(\d\d)\|', path(PREFIX+'ledger-v1.md').read_text(), re.M)
    assert target_ids == own_ids == expected_ids
    summary = {'fingerprint_occurrences_verified': len(bound),
               'deduplicated_paths_verified': len(unique),
               'all_declared_fingerprints_match': True}
    write_new('baseline-v1.json', {
        'prepared_at_utc': stamp(),
        'target_main': fp(TARGET+'candidate-v1.md'),
        'target_freeze': fp(TARGET+'freeze-v1.json'),
        'immutable_metadata': [fp(rel) for rel in immutable],
        'direct_bindings_summary': summary,
        'compact_immutable_own_parent': fp(PARENT),
        'earlier_own_paths_bound': 475,
        'historical_inventory_bound_not_copied_or_recursively_replayed': True,
        'all_NEW_peer_three_bit_v1_r2_audit_paths_forbidden': True,
    })
    write_new('metadata-v1.json', {
        'created_at_utc': stamp(),
        'reviewer': '/root/review_2017_coarsening_r1',
        'NEW_constructor': '/root',
        'OLD_C_root_S3_authorship_disclosed_not_independently_recertified': True,
        'NEW_peer_v1_r2_reports_findings_metadata_unread_through_ENTIRE_freeze': True,
        'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max'},
        'independently_verified_effective_settings': None,
        'mathematical_program_CAS_scan_author_rerun_or_saved_certificate': False,
        'no_Git_shared_old_or_cache_mutation': True,
        'budget_status': {
            'last_reliable_direct_own': {'at_utc':'2026-10-17T20:37:10Z',
                                       'weekly_total_used_percent':64,
                                       'window_minutes':10080,'resets_at':1792745187},
            'root_last_reliable': {'at_utc':'2026-10-17T20:40:00Z',
                                   'weekly_total_used_percent':65,
                                   'canonical_resets_at':1792745187},
            'anomalous_direct': {'at_utc':'2026-10-17T20:43:12Z',
                                 'weekly_total_used_percent':0,
                                 'window_minutes':10080,'resets_at':1792874445,
                                 'ordinary_usage_allowed':True},
            'automatic_new_window_spending_authorized':False,
            'root_authorized_only_already_started_whole_initial_freeze_from_reserve':True,
            'queued_research_on_HOLD_after_freeze':True,
            'total_ceiling_percent':90,
        },
    })
    write_new('input-validation-v1.json', {
        'validated_at_utc': stamp(), **summary,
        'exact_target_main_and_freeze_match_assignment': True,
        'all_six_constructor_files_fingerprinted_and_complete_packet_read': True,
        'all_44_target_and_own_ledger_tags_present_once_in_order': True,
        'compact_parent_identity_matches': True,
        'no_NEW_peer_audit_metadata_opened': True,
        'no_constructor_freezer_or_mathematical_program_executed': True,
        'checks_are_administrative_only': True,
    })

    for row in unique.values():
        check(row)
    suffixes = ['initial-v1.md', 'issues-v1.md', 'ledger-v1.md', 'sources-v1.md',
                'worklog-v1.md', 'freeze-v1.py', 'baseline-v1.json',
                'metadata-v1.json', 'input-validation-v1.json']
    write_new('manifest-v1.json', {
        'frozen_at_utc': stamp(),
        'status': 'COMPLETE initially blind ENTIRE WHOLE three-bit r2 R2 initial',
        'reviewer': '/root/review_2017_coarsening_r1',
        'NEW_constructor_excluded': '/root',
        'target_main': fp(TARGET+'candidate-v1.md'),
        'target_freeze': fp(TARGET+'freeze-v1.json'),
        'all_constructor_obligations_covered':44,
        'complete_self_contained_whole_reconstruction':True,
        'verdict':'no substantive defect in exact scoped r2 theorem relative to accepted inputs',
        'substantive_issues':0,'required_repairs':0,
        'OLD_C_root_S3_role_disclosed_no_independent_self_recertification':True,
        'NEW_peer_v1_r2_findings_reports_metadata_unread_until_ENTIRE_initial_frozen':True,
        'mathematical_program_CAS_scan_certificate_or_author_rerun':False,
        'no_annual_classification_weight_ge4_or_novelty_claim':True,
        **summary,
        'compact_immutable_own_parent':fp(PARENT),
        'earlier_own_paths_bound':475,
        'own_paths_after_this_packet':485,
        'budget_telemetry_anomaly_recorded_and_further_research_on_HOLD':True,
        'artifacts':[fp(PREFIX+suffix) for suffix in suffixes],
    })
    print(json.dumps({'manifest':fp(PREFIX+'manifest-v1.json'),
                      'report':fp(PREFIX+'initial-v1.md'),
                      'whole_obligations':44, **summary}, indent=2))
