#!/usr/bin/env python3
"""NEW SQ14 affected whole-review documentary administration; no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import difflib
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2020-B4/reviews/reasoning-arithmetic-return-r14-review-2-reaudit-v1.1-'
A = 'problems/2020-B4/notes/reasoning-arithmetic-return-r14-'
PARENT = 'problems/2024-B4/reviews/reasoning-cofactor-return-r9-review-2-manifest-v1.json'
AUTH = ['reasoning-Todd-return-r12', 'reasoning-arithmetic-return-r9']
PAYLOADS = ['report.md', 'ledger.md', 'issues.md', 'sources.md', 'sources.json',
            'worklog.md', 'admin.py', 'baseline.json', 'input-validation.json', 'metadata.json']
EXPECTED = {
    A+'freeze-v1.1.json': (7882, '6468e2ee52ca8d0ef18e27d65ce57cda932e3072eb8f95e2c3565233026395c9'),
    A+'candidate-v1.1.md': (23705, '55afd51e3f83be9f7f1291a9817499bf863d5dbff6900211a93446f169f8f8f7'),
    PARENT: (3631, '304bd12e24d555159b413a912a985b38311c5be19dba4c467f4f42183088133f'),
}


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    pp = Path(path)
    if pp.is_absolute() or '..' in pp.parts:
        raise ValueError('exact relative documentary path required')
    if path.startswith('problems/2020-B4/reviews/reasoning-arithmetic-return-r14-review-1-'):
        if 'reaudit' in path or 'v1.1' in path:
            raise ValueError('NEW corresponding affected peer is embargoed')
    if path.startswith('problems/2024-B4/reviews/reasoning-cofactor-return-r9-review-1-'):
        raise ValueError('separate NEW R9 peer is embargoed')
    return (ROOT / pp).read_bytes()


def record(path):
    data = raw(path)
    out = {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
    if path in EXPECTED and (out['bytes'], out['sha256']) != EXPECTED[path]:
        raise ValueError('exact assigned/parent identity mismatch: '+path)
    return out


def checked(item):
    if record(item['path']) != item:
        raise ValueError('immutable fingerprint mismatch: '+item['path'])
    return item


def obj(path):
    return json.loads(raw(path))


def summarize(rows):
    unique = {}
    for item in rows:
        if item['path'] in unique and unique[item['path']] != item:
            raise ValueError('conflicting preservation records')
        unique[item['path']] = item
    guards = [unique[path] for path in sorted(unique)]
    data = json.dumps(guards, sort_keys=True, separators=(',', ':')).encode()
    return guards, {'occurrences': len(rows), 'unique_paths': len(guards),
                    'canonical_deduplicated_sha256': hashlib.sha256(data).hexdigest()}


def exact_diff():
    pieces = []
    pairs = [(A+s+'-v1.md', A+s+'-v1.1.md') for s in
             ['candidate', 'obligations', 'constructor-checks', 'issues', 'failed-routes', 'sources', 'worklog']]
    pairs.append((A+'sources-v1.json', A+'sources-v1.1.json'))
    for left, right in pairs:
        pieces.extend(difflib.unified_diff(raw(left).decode().splitlines(True),
                                         raw(right).decode().splitlines(True),
                                         fromfile=left, tofile=right))
    return ''.join(pieces).encode()


def unchanged_spans():
    old, new = raw(A+'candidate-v1.md').decode(), raw(A+'candidate-v1.1.md').decode()
    def part(text, left, right):
        return text.split(left, 1)[1].split(right, 1)[0]
    result = {}
    for label, left, right in [('SQ14A_C_displayed_claims', '**SQ14A,', '**SQ14D,'),
                               ('main_sections1_3', '## 1.', '## 4.')]:
        before, after = part(old, left, right), part(new, left, right)
        if before != after:
            raise ValueError('declared unchanged text mismatch')
        data = before.encode()
        result[label] = {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                         'textually_identical': True, 'not_independent_mathematical_review': True}
    return result


def labels():
    expected = [f'SQ14-{i:02d}' for i in range(1, 65)] + [f'SQ14-R{i:02d}' for i in range(1, 13)]
    author = re.findall(r'^\| (SQ14-(?:R)?\d{2}) \|', raw(A+'obligations-v1.1.md').decode(), re.M)
    own = re.findall(r'^\|(SQ14-(?:R)?\d{2})\|', raw(P+'ledger.md').decode(), re.M)
    if author != expected or own != expected:
        raise ValueError('ALL64+12 separate dispositions mismatch')
    return {'original': 64, 'repair': 12, 'whole': 76, 'separate_reviewer_dispositions': 76,
            'mathematics_proved_by_code': False}


def gather():
    author = obj(A+'freeze-v1.1.json')
    if author['all_original64_plus_repair12'] != 76 or len(author['payloads']) != 13:
        raise ValueError('author ENTIRE14/76 coverage mismatch')
    rows = [record(A+'freeze-v1.1.json')] + [checked(x) for x in author['payloads']]
    baseline = obj(A+'baseline-v1.1.json')
    prior = [checked(x) for x in baseline['records']]
    _, prior_summary = summarize(prior)
    if prior_summary != baseline['detail']['summary'] or prior_summary != author['guard_detail']['summary']:
        raise ValueError('author compact historical guard mismatch')
    rows.extend(prior)
    if raw(A+'diff-v1.1.patch') != exact_diff():
        raise ValueError('eight-component documentary diff mismatch')
    spans = unchanged_spans()
    if spans != author['unchanged_mathematical_text']:
        raise ValueError('author unchanged span record mismatch')
    if not raw(A+'sources-v1.1.md').endswith(raw(A+'sources-v1.md')):
        raise ValueError('historical source archival suffix mismatch')
    bindings = []
    for stem in AUTH:
        path = 'problems/2020-B4/reviews/'+stem+'-acceptance.json'
        meta = obj(path)
        checked(meta['accepted_copy'])
        checked(meta['candidate'])
        if not raw(meta['accepted_copy']['path']).endswith(raw(meta['candidate']['path'])):
            raise ValueError('operative accepted candidate suffix mismatch')
        bindings.append({'authority': path, 'body': meta['accepted_copy'], 'exact_suffix': True,
                         'historical_inventory_reexpanded': False})
    parent = obj(PARENT)
    if parent['ENTIRE_files'] != 11 or len(parent['payloads']) != 10:
        raise ValueError('own parent ENTIRE11 mismatch')
    rows.append(record(PARENT))
    rows.extend(checked(x) for x in parent['payloads'])
    guards, summary = summarize(rows)
    detail = {'author_ENTIRE_files_verified': 14, 'author_compact_guard_summary': prior_summary,
              'operative_current_accepted_bindings': bindings, 'exact_eight_component_diff': True,
              'unchanged_spans': spans, 'historical_source_suffix_preserved': True,
              'old_SQ14_authority_role': 'historical false fractional scope not imported as valid',
              'own_original_literal_domain_miss_preserved_and_acknowledged': True,
              'own_immediate_parent_ENTIRE_files_verified': 11,
              'parent_guard_summary_bound_by_parent_identity': parent['guard_summary'],
              'historical_inventory_reexpanded_or_old_executable_replayed': False,
              'mathematical_instance_evaluated': False}
    return guards, summary, detail


def write(suffix, value):
    if suffix not in PAYLOADS+['manifest.json']:
        raise ValueError('exclusive assigned NEW output only')
    with (ROOT / (P+suffix)).open('x', encoding='utf-8') as out:
        json.dump(value, out, indent=2, ensure_ascii=False)
        out.write('\n')
    return record(P+suffix)


def prepare():
    guards, summary, detail = gather()
    ll = labels()
    write('baseline.json', {'captured_at_utc': now(), 'status': 'documentary integrity only',
                            'summary': summary, 'detail': detail, 'guards': guards})
    write('input-validation.json', {'validated_at_utc': now(), 'status': 'documentary PASS only',
                                   'author_ENTIRE14_preserved': True, 'own_parent_ENTIRE11_preserved': True,
                                   'all76_labels': ll, 'guard_summary': summary,
                                   'exact_eight_component_diff_and_unchanged_spans': True,
                                   'old_author_source_reviewer_executable_invoked': False})
    write('metadata.json', {
        'created_at_utc': now(), 'status': 'one initially peer-blind OTHER affected WHOLE audit',
        'reviewer': '/root/review_2017_coarsening_r1', 'SQ14_or_repair_constructor': False,
        'own_original_literal_scope_miss_acknowledged': True,
        'known_issue_exposure_disclosed': True, 'NEW_root_affected_peer_material_accessed': False,
        'separate_NEW2024R9_peer_material_accessed': False,
        'original_obligations': 64, 'repair_obligations': 12, 'whole_obligations': 76,
        'payload_files': 10, 'ENTIRE_files': 11,
        'BOTH_affected_whole_reviews_and_coordinator_reconciliation_required': True,
        'findings_embargoed_until_explicit_BOTH_entire_confirmation': True,
        'FULL_final_model_readback_ALL10_payloads_REQUIRED_before_freeze': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max', 'verified_effective_readback': None,
        'authorized_weekly_reset': 1792874445, 'last_direct_transition_TOTAL_percent': 52,
        'TOTAL_ceiling_percent': 90, 'integration_reserve': True, 'automatic_later_window': False,
        'mathematical_code_CAS_scan_test_optimizer_old_author_source_replay': False,
        'old_shared_Git_cache_mutation_spawn_charge_contact_bypass': False})
    print(json.dumps({'prepare': 'PASS', 'guards': summary, 'labels': ll}))


def protected():
    baseline = obj(P+'baseline.json')
    for item in baseline['guards']:
        checked(item)
    guards, summary, detail = gather()
    if (guards, summary, detail) != (baseline['guards'], baseline['summary'], baseline['detail']):
        raise ValueError('preservation baseline changed')
    labels()
    return baseline


def freeze(attest):
    if not attest:
        raise ValueError('FULL final all-payload model readback required')
    baseline = protected()
    payloads = [record(P+s) for s in PAYLOADS]
    for item in payloads:
        if item['path'].endswith('.json'):
            obj(item['path'])
    manifest = {'frozen_at_utc': now(), 'status': 'initially peer-blind affected whole review; not acceptance',
                'reviewer': '/root/review_2017_coarsening_r1', 'SQ14_or_repair_nonconstructor': True,
                'whole_obligations': 76, 'original': 64, 'repair': 12, 'separate_dispositions': 76,
                'payload_files': 10, 'ENTIRE_files': 11,
                'author': record(A+'freeze-v1.1.json'), 'immediate_own_parent': record(PARENT),
                'compact_baseline': record(P+'baseline.json'), 'guard_summary': baseline['summary'],
                'own_original_literal_scope_miss_acknowledged': True,
                'FULL_final_model_readback_ALL10_payloads_completed': True,
                'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
                'NEW_root_affected_peer_material_access_before_freeze': False,
                'findings_embargoed_until_explicit_BOTH_entire_confirmation': True,
                'mathematical_execution_or_old_author_source_replay': False,
                'payloads': payloads}
    print(json.dumps({'freeze': write('manifest.json', manifest), 'at_utc': manifest['frozen_at_utc']}))


def verify():
    manifest = obj(P+'manifest.json')
    if [x['path'] for x in manifest['payloads']] != [P+s for s in PAYLOADS]:
        raise ValueError('ENTIRE payload coverage mismatch')
    for item in manifest['payloads']:
        checked(item)
    baseline = protected()
    if manifest['guard_summary'] != baseline['summary'] or manifest['whole_obligations'] != 76:
        raise ValueError('manifest coverage/summary mismatch')
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'verified_at_utc': now(),
                      'ENTIRE_files': 11, 'ALL_obligations': 76, 'guard_summary': baseline['summary'],
                      'report': record(P+'report.md'), 'manifest': record(P+'manifest.json')}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['prepare', 'freeze', 'verify'])
    parser.add_argument('--attest-final-model-readback', action='store_true')
    args = parser.parse_args()
    if args.action == 'prepare':
        prepare()
    elif args.action == 'freeze':
        freeze(args.attest_final_model_readback)
    else:
        verify()
