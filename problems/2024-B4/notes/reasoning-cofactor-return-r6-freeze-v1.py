#!/usr/bin/env python3
"""Administrative R6 freezer only: bytes, SHA, JSON and obligation labels.

No mathematical parameter, formula, field, polynomial or theorem is
evaluated. No old freezer/source/author program is imported or rerun.
Writes are exclusive and limited to this new assigned prefix.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2024-B4/notes/reasoning-cofactor-return-r6-'
PARENT = 'problems/2017-B4/reviews/coordinator-weighted-optimum-r2-review-2-manifest-v1.json'
PARENT_EXPECTED = (2983, '6fd3f0358279e95f7c76ca4b2dda1bb8162db43d49270d0ee561a26999f07750')
STATIC = [
    'candidate-v1.md', 'obligations-v1.md', 'constructor-checks-v1.md',
    'failed-routes-v1.md', 'source-audit-v1.md', 'sources-v1.json',
    'worklog-v1.md', 'freeze-v1.py',
]
GENERATED = ['baseline-v1.json', 'input-validation-v1.json', 'metadata-v1.json']
INPUTS = [
    'AGENTS.md',
    'problems/2024-B4/statement.md',
    'problems/2024-B4/proofs/reviewed-structural-v1.1.md',
    'problems/2024-B4/reviews/structural-acceptance.md',
    'problems/2024-B4/reviews/structural-acceptance.json',
    'problems/2024-B4/notes/structural-reasoning-r2-candidate-v1.md',
    'problems/2024-B4/proofs/reviewed-cofactor-dominant-r4-v1.1.md',
    'problems/2024-B4/reviews/cofactor-dominant-r4-acceptance.md',
    'problems/2024-B4/reviews/cofactor-dominant-r4-acceptance.json',
    'problems/2024-B4/notes/cofactor-dominant-r4-candidate-v1.md',
    'problems/2024-B4/proofs/reviewed-cofactor-global-r2-v1.1.md',
    'problems/2024-B4/reviews/cofactor-global-r2-acceptance.md',
    'problems/2024-B4/reviews/cofactor-global-r2-acceptance.json',
    'problems/2024-B4/notes/cofactor-global-r2-source-audit-v1.md',
    'problems/2024-B4/notes/cofactor-Frobenius-r5-candidate-v2.md',
    'problems/2024-B4/proofs/reviewed-cofactor-Frobenius-r5-v2.1.md',
    'problems/2024-B4/reviews/cofactor-Frobenius-r5-acceptance.md',
    'problems/2024-B4/reviews/cofactor-Frobenius-r5-acceptance.json',
    'problems/2024-B4/reviews/cofactor-Frobenius-r5-reconciliation-precision-v1.md',
    'problems/2024-B4/notes/cofactor-Frobenius-r5-sources-v1.md',
    'problems/2024-B4/notes/cofactor-literature-followup-r3-findings-v1.md',
    'problems/2024-B4/notes/cofactor-literature-followup-r3-retrieval-log-v1.md',
    PARENT,
]
EXPECTED = {
    'AGENTS.md': (4707, '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'),
    'problems/2024-B4/statement.md': (2470, '60244f7752634772adb434efbdb41a63fb02029dc3be4238f3718c6e5ec84e5f'),
    'problems/2024-B4/proofs/reviewed-structural-v1.1.md': (17079, '082dc054ce2cdaea80eee009f4c97c877c6968afb54b5a8f3141b7354031dd3f'),
    'problems/2024-B4/proofs/reviewed-cofactor-dominant-r4-v1.1.md': (18793, '14c47b6db082bee1d60bcf297c289fe949fdec9384cc8a159b199c56ba265838'),
    'problems/2024-B4/proofs/reviewed-cofactor-global-r2-v1.1.md': (19500, 'fd110d1615e730d754063b157cc1906b418702f510b2640bfd1b5c63e898548d'),
    'problems/2024-B4/notes/cofactor-Frobenius-r5-candidate-v2.md': (13006, '329b975a7f8fe7456f9794a2170dc443396fb1a2b0143cc61ac9ddd027beb47e'),
    'problems/2024-B4/proofs/reviewed-cofactor-Frobenius-r5-v2.1.md': (17704, 'aa7c3edba910270594302ede19cce7a8f530e21f3c5b17e4c64ddd387762bcf3'),
    PARENT: PARENT_EXPECTED,
}


def record(rel):
    data = (ROOT / rel).read_bytes()
    return {'path': rel, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def check(row):
    actual = record(row['path'])
    assert actual['bytes'] == row['bytes'], ('byte mismatch', row['path'])
    assert actual['sha256'] == row['sha256'], ('SHA mismatch', row['path'])
    return actual


def load(rel):
    return json.loads((ROOT / rel).read_text())


def write_new(suffix, obj):
    assert suffix in GENERATED + ['freeze-v1.json']
    rel = PREFIX + suffix
    with (ROOT / rel).open('x', encoding='utf-8') as handle:
        json.dump(obj, handle, ensure_ascii=False, indent=2)
        handle.write('\n')
    return record(rel)


def main():
    for suffix in GENERATED + ['freeze-v1.json']:
        assert not (ROOT / (PREFIX + suffix)).exists(), ('refuse overwrite', suffix)
    static_rows = [record(PREFIX + suffix) for suffix in STATIC]
    for suffix in ['sources-v1.json']:
        load(PREFIX + suffix)
    labels = re.findall(r'^\| (R6-\d\d) \|', (ROOT / (PREFIX + 'obligations-v1.md')).read_text(), re.M)
    assert len(labels) == 48 and len(set(labels)) == 48
    assert labels == ['R6-' + str(j).zfill(2) for j in range(1, 49)]

    input_rows = [record(rel) for rel in INPUTS]
    for rel, (size, digest) in EXPECTED.items():
        check({'path': rel, 'bytes': size, 'sha256': digest})

    parent = load(PARENT)
    assert parent['whole_obligations'] == 48
    parent_rows = [check(row) for row in parent['artifacts']]
    assert len(parent_rows) == 9
    # Bind the immutable immediate parent's full metadata by its own hash.
    # Do not recursively copy/replay its historical inventories or math.

    bindings = []
    for authority, field in [
        ('problems/2024-B4/reviews/structural-acceptance.json', 'accepted_proof'),
        ('problems/2024-B4/reviews/structural-acceptance.json', 'candidate'),
        ('problems/2024-B4/reviews/cofactor-dominant-r4-acceptance.json', 'accepted_copy'),
        ('problems/2024-B4/reviews/cofactor-dominant-r4-acceptance.json', 'candidate'),
        ('problems/2024-B4/reviews/cofactor-Frobenius-r5-acceptance.json', 'accepted_copy'),
        ('problems/2024-B4/reviews/cofactor-Frobenius-r5-acceptance.json', 'candidate'),
        ('problems/2024-B4/reviews/cofactor-global-r2-acceptance.json', 'accepted_copy'),
    ]:
        obj = load(authority)
        assert 'proved' in obj['status']
        bindings.append({'authority': authority, 'field': field, 'record': check(obj[field])})

    suffix_checks = []
    for accepted, author in [
        ('problems/2024-B4/proofs/reviewed-cofactor-dominant-r4-v1.1.md',
         'problems/2024-B4/notes/cofactor-dominant-r4-candidate-v1.md'),
        ('problems/2024-B4/proofs/reviewed-cofactor-Frobenius-r5-v2.1.md',
         'problems/2024-B4/notes/cofactor-Frobenius-r5-candidate-v2.md'),
    ]:
        assert (ROOT / accepted).read_bytes().endswith((ROOT / author).read_bytes())
        suffix_checks.append({'accepted_copy': accepted, 'literal_author': author, 'byte_identical_suffix': True})

    occurrences = input_rows + parent_rows + [row['record'] for row in bindings]
    by_path = {}
    for row in occurrences:
        if row['path'] in by_path:
            assert by_path[row['path']] == row
        by_path[row['path']] = row
    now = datetime.now(timezone.utc).isoformat()
    generated = []
    generated.append(write_new('baseline-v1.json', {
        'created_utc': now,
        'scope': 'Necessary direct old inputs and compact immutable parent only; no recursive historical inventory expansion',
        'immediate_own_parent': record(PARENT),
        'parent_direct_artifact_count_verified': len(parent_rows),
        'direct_input_records': input_rows,
        'necessary_fingerprint_occurrences_verified': len(occurrences),
        'deduplicated_paths_verified': len(by_path),
        'old_file_writes': 0,
    }))
    generated.append(write_new('input-validation-v1.json', {
        'created_utc': now,
        'status': 'PASS administrative integrity only; no mathematical theorem validation',
        'whole_obligation_labels': 48,
        'necessary_declared_authority_bindings': bindings,
        'literal_suffix_checks': suffix_checks,
        'T1_suffix_claim': 'None: accepted structural copy has its documented editorial heading change',
        'parent_direct_artifacts_verified': len(parent_rows),
        'necessary_fingerprint_occurrences_verified': len(occurrences),
        'deduplicated_paths_verified': len(by_path),
        'original_R5_v1_and_old_review_bytes_not_rewritten': True,
    }))
    generated.append(write_new('metadata-v1.json', {
        'created_utc': now,
        'status': 'candidate proof - unverified',
        'claims': ['R6A', 'R6B', 'R6C', 'R6D'],
        'whole_obligations': 48,
        'constructor': '/root/review_2017_coarsening_r1',
        'constructor_excluded_from_independent_audits': True,
        'root_generic_target_only_no_new_R6_inference': True,
        'two_OTHER_initially_blind_ENTIRE_whole_audits_required': True,
        'requested_model': 'gpt-6.1-sol',
        'requested_reasoning': 'max',
        'verified_effective_setting_readback': None,
        'latest_authoritative_weekly_total_used_percent': 33,
        'authorized_reset_unix_seconds': 1792874445,
        'ceiling_total_used_percent': 90,
        'review_integration_reserve_required': True,
        'automatic_later_window_authorization': False,
        'mathematical_code_CAS_scans_author_reruns': False,
        'administrative_code_only': True,
        'pending_jobs_processes_or_approvals': [],
        'old_shared_cache_Git_writes': False,
        'Ferard2017_body_read': False,
        'novelty_or_full_annual_classification_claimed': False,
        'FULL_readback_and_SEPARATE_readonly_verification_required_after_freeze': True,
        'immediate_own_parent': record(PARENT),
    }))

    # Recheck every required old/direct-parent guard after new metadata writes.
    for row in occurrences:
        check(row)
    for row in static_rows + generated:
        check(row)
    freeze = write_new('freeze-v1.json', {
        'frozen_utc': datetime.now(timezone.utc).isoformat(),
        'status': 'ENTIRE constructor candidate proof - unverified; not promotion',
        'whole_claims': ['R6A', 'R6B', 'R6C', 'R6D'],
        'whole_obligations': 48,
        'artifacts_including_freeze': 12,
        'immediate_own_parent': record(PARENT),
        'necessary_fingerprint_occurrences_verified': len(occurrences),
        'deduplicated_old_paths_verified': len(by_path),
        'TWO_OTHER_whole_audits_and_reconciliation_required': True,
        'FULL_readback_and_SEPARATE_readonly_verification_still_to_be_completed': True,
        'artifacts': [record(row['path']) for row in static_rows + generated],
    })
    print(json.dumps({'freeze': freeze, 'main': record(PREFIX + 'candidate-v1.md'),
                      'whole_obligations': 48,
                      'necessary_occurrences': len(occurrences), 'unique_old_paths': len(by_path)}, indent=2))


if __name__ == '__main__':
    main()
