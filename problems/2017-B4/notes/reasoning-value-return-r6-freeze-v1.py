"""Administrative fingerprints only; no mathematical algorithm or test."""
from pathlib import Path
import datetime
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2017-B4/notes/reasoning-value-return-r6-'
PARENT = 'problems/2019-B4/reviews/coordinator-retained-core-gap-r1-review-2-manifest-v1.json'
PARENT_EXPECTED = (3495, 'c53e1f875b1c3cc6c2b3dbae1492829cdf9ef7778e96c249e3027cb92edb316d')
AUTHORITIES = [
    'problems/2017-B4/reviews/reasoning-value-return-r5-acceptance.json',
    'problems/2017-B4/reviews/reasoning-value-return-r4-acceptance.json',
    'problems/2017-B4/reviews/reasoning-value-return-r3-acceptance.json',
    'problems/2017-B4/reviews/allD-global-acceptance.json',
    'problems/2017-B4/reviews/allD-uniform-strict-acceptance.json',
    'problems/2017-B4/reviews/coarsening-acceptance.json',
]
EXPLICIT = ['AGENTS.md', 'problems/2017-B4/statement.md'] + [
    p[:-5] + '.md' for p in AUTHORITIES
] + ['problems/2017-B4/proofs/reviewed-global-value-return-r2-v1.1.md']
ARTIFACT_SUFFIXES = [
    'candidate-v1.md', 'obligations-v1.md', 'sources-v1.md',
    'failures-v1.md', 'worklog-v1.md', 'freeze-v1.py',
    'baseline-v1.json', 'metadata-v1.json', 'input-validation-v1.json',
]


def stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def path(rel):
    p = (ROOT / rel).resolve()
    assert p.is_relative_to(ROOT), rel
    return p


def fp(rel):
    data = path(rel).read_bytes()
    return {'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def check(record):
    assert fp(record['path']) == record, record['path']


def records(value):
    if isinstance(value, dict):
        if all(k in value for k in ('path', 'bytes', 'sha256')):
            yield {k: value[k] for k in ('path', 'bytes', 'sha256')}
        for child in value.values():
            yield from records(child)
    elif isinstance(value, list):
        for child in value:
            yield from records(child)


def collect_bound_records():
    bound = []
    for rel in [PARENT] + AUTHORITIES:
        bound.append(fp(rel))
        bound.extend(records(json.loads(path(rel).read_text())))
    bound.extend(fp(rel) for rel in EXPLICIT)
    return bound


def validate_bound(bound):
    unique = {}
    for row in bound:
        check(row)
        previous = unique.setdefault(row['path'], row)
        assert previous == row, row['path']
    return {'fingerprint_occurrences_verified': len(bound),
            'deduplicated_paths_verified': len(unique),
            'all_declared_fingerprints_match': True}


def write_new(suffix, value):
    rel = PREFIX + suffix
    assert rel.startswith(PREFIX)
    with path(rel).open('x') as stream:
        stream.write(json.dumps(value, indent=2) + '\n')


def obligations():
    text = path(PREFIX + 'obligations-v1.md').read_text()
    ids = re.findall(r'^\|PM-(\d\d)\|', text, re.M)
    assert ids == [f'{i:02d}' for i in range(1, 49)]
    return len(ids)


def suffix_check():
    accepted = path('problems/2017-B4/proofs/reviewed-reasoning-value-return-r5-v1.1.md').read_bytes()
    original = path('problems/2017-B4/notes/reasoning-value-return-r5-candidate-v1.md').read_bytes()
    assert accepted.endswith(original)


def prepare():
    parent = fp(PARENT)
    assert (parent['bytes'], parent['sha256']) == PARENT_EXPECTED
    bound = collect_bound_records()
    summary = validate_bound(bound)
    suffix_check()
    assert obligations() == 48
    baseline = {
        'prepared_at_utc': stamp(),
        'purpose': 'Compact immutable metadata binding; no historical inventory duplication.',
        'immutable_parent': parent,
        'earlier_own_paths_bound_by_parent': 465,
        'parent_history_not_recursively_rehashed_or_freshly_mathematically_reread': True,
        'authoritative_acceptance_metadata': [fp(rel) for rel in AUTHORITIES],
        'explicit_inputs': [fp(rel) for rel in EXPLICIT],
        'direct_declared_bindings_summary': summary,
        'GR_accepted_copy_has_exact_constructor_suffix': True,
    }
    write_new('baseline-v1.json', baseline)
    write_new('metadata-v1.json', {
        'created_at_utc': stamp(), 'status': 'candidate proof - unverified',
        'constructor': '/root/review_2017_coarsening_r1',
        'contributors_excluded_from_independent_whole_audits': [
            '/root/review_2017_coarsening_r1', '/root'],
        'two_OTHER_initially_blind_WHOLE_audits_required': True,
        'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
        'verified_effective_setting_readback': None,
        'direct_usage': {'observed_at_utc': '2026-10-17T20:37:10Z',
                         'total_weekly_used_percent': 64,
                         'window_minutes': 10080, 'resets_at': 1792745187,
                         'ordinary_usage_allowed': True, 'total_ceiling_percent': 90},
        'mathematical_code_CAS_scan_sign_child_or_theoretical_algorithm_execution': False,
        'cache_Git_shared_old_file_changes': False,
        'remote_pdf_download_or_binary_hash_claim': False,
        'pending_native_job_or_tool_approval': False,
        'upper_R_effective_rate_value_annual_or_novelty_claim': False,
        'compact_parent': parent,
    })
    write_new('input-validation-v1.json', {
        'validated_at_utc': stamp(), **summary,
        'compact_parent_identity_matches': True,
        'earlier_own_paths_bound_not_copied': 465,
        'all_48_obligation_tags_present_once_in_order': True,
        'GR_accepted_exact_constructor_suffix': True,
        'no_recursive_historical_inventory_replay': True,
        'checks_are_administrative_only': True,
    })
    print(json.dumps({'prepared': True, **summary, 'obligations': 48}))


def freeze():
    baseline = json.loads(path(PREFIX + 'baseline-v1.json').read_text())
    for row in [baseline['immutable_parent']] + baseline['authoritative_acceptance_metadata'] + baseline['explicit_inputs']:
        check(row)
    summary = validate_bound(collect_bound_records())
    assert summary == baseline['direct_declared_bindings_summary']
    suffix_check()
    assert obligations() == 48
    artifacts = [fp(PREFIX + suffix) for suffix in ARTIFACT_SUFFIXES]
    main = artifacts[0]
    write_new('freeze-v1.json', {
        'frozen_at_utc': stamp(), 'status': 'COMPLETE constructor checkpoint; candidate proof - unverified',
        'constructor': '/root/review_2017_coarsening_r1',
        'contributors_excluded': ['/root/review_2017_coarsening_r1', '/root'],
        'two_OTHER_initially_blind_WHOLE_audits_required': True,
        'main': main, 'whole_obligations': 48,
        'claims': ['PM1 exact local model and genuine finite upper certificates',
                   'PM2 actual Jordan plane patch full completion with total contents at most e/2',
                   'PM3 compact-strict plane-to-full upper counting interface only',
                   'PM4 actual D3 free entropy gap even at matching limiting tile composition'],
        'upper_R_two_sided_computability_value_annual_or_novelty_claim': False,
        **summary,
        'compact_immutable_own_parent': baseline['immutable_parent'],
        'earlier_own_paths_bound': 465,
        'own_paths_after_this_nine_artifact_plus_manifest_packet': 475,
        'mathematical_program_CAS_scan_or_source_binary_download': False,
        'artifacts': artifacts,
    })
    print(json.dumps({'freeze': fp(PREFIX + 'freeze-v1.json'), 'main': main, **summary, 'obligations': 48}))


if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in ('prepare', 'freeze')
    (prepare if sys.argv[1] == 'prepare' else freeze)()
