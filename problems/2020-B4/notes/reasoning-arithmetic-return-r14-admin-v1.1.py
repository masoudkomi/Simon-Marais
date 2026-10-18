#!/usr/bin/env python3
"""SQ14 author-repair documentary metadata; no mathematical execution."""
import argparse
import difflib
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2020-B4/notes/reasoning-arithmetic-return-r14-'
BASELINE = P + 'baseline-v1.1.json'
VALIDATION = P + 'input-validation-v1.1.json'
MANIFEST = P + 'freeze-v1.1.json'
DIFF = P + 'diff-v1.1.patch'
OLD_AUTHOR = P + 'freeze-v1.json'
OLD_REVIEWS = [
    'problems/2020-B4/reviews/reasoning-arithmetic-return-r14-review-1-manifest-v1.json',
    'problems/2020-B4/reviews/reasoning-arithmetic-return-r14-review-2-manifest-v1.json',
]
PARENT = 'problems/2024-B4/notes/reasoning-cofactor-return-r9-freeze-v1.json'
AUTHORITIES = [
    'problems/2020-B4/reviews/reasoning-Todd-return-r12-acceptance.json',
    'problems/2020-B4/reviews/reasoning-arithmetic-return-r9-acceptance.json',
]
HISTORICAL_AUTHORITY = 'problems/2020-B4/reviews/reasoning-arithmetic-return-r14-acceptance.json'
EXPECTED = {
    'AGENTS.md': (4707, '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'),
    OLD_AUTHOR: (7060, 'e10b1b5ed9b573e181846b4403d1dbda20515fab3ff39091ce1c8c51124919d5'),
    OLD_REVIEWS[0]: (2582, 'd5e2d5db18d2ce837c86953822e4b015935436b74617667565079b57da78537d'),
    OLD_REVIEWS[1]: (3068, 'd91bb80ed5b7ee9b55e1bf308ac8cac3eff3750897cd4a06291a3d4f9d23c535'),
    PARENT: (9271, 'baad7591162df50c28cc4d20794616d165d622ae8c6abc0bb9f699e255d2147d'),
    P + 'candidate-v1.md': (16951, '673bcde7cadb391baf6a8362295bc4ba833e40a69dd4836725b5b3de2015df7f'),
    'problems/2020-B4/proofs/reviewed-reasoning-arithmetic-return-r14-v1.1.md':
        (22470, 'befc8237c23eaac3e210d0aa3f28eaef44a01d4e771e3a4d156b18fd6b6bedb5'),
    'problems/2020-B4/proofs/reviewed-reasoning-Todd-return-r12-v1.1.md':
        (35569, 'f1663778cf78c18b3cb30a4702d7fbff95be29ab73c5f8e4f74d344362c8fba6'),
    'problems/2020-B4/proofs/reviewed-reasoning-arithmetic-return-r9-v1.1.md':
        (24622, 'ab2ee4e7a2dcfa464780c6144f996d683f08b7f04da63d2a77ee2fdd4ec922b8'),
}
TEXT_PAIRS = ['candidate', 'obligations', 'constructor-checks', 'issues',
              'failed-routes', 'sources', 'worklog']
PAYLOADS = [
    'candidate-v1.1.md', 'obligations-v1.1.md', 'constructor-checks-v1.1.md',
    'repair-v1.1.md', 'issues-v1.1.md', 'failed-routes-v1.1.md',
    'sources-v1.1.md', 'sources-v1.1.json', 'worklog-v1.1.md',
    'diff-v1.1.patch', 'admin-v1.1.py', 'baseline-v1.1.json',
    'input-validation-v1.1.json',
]


def now():
    return datetime.now(timezone.utc).isoformat()


def raw(path):
    p = Path(path)
    assert not p.is_absolute() and '..' not in p.parts and '.git' not in p.parts
    assert 'sq15' not in path.lower()
    if 'reasoning-arithmetic-return-r14-review-' in path:
        assert 'v1.1' not in path and 'reaudit' not in path
    return (ROOT / p).read_bytes()


def fp(path):
    data = raw(path)
    value = {'path': path, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}
    if path in EXPECTED:
        assert (value['bytes'], value['sha256']) == EXPECTED[path], path
    return value


def match(rec):
    value = fp(rec['path'])
    assert value['bytes'] == rec['bytes'] and value['sha256'] == rec['sha256'], rec['path']
    return value


def obj(path):
    return json.loads(raw(path))


def doc_summary(records):
    unique = {}
    for rec in records:
        if rec['path'] in unique:
            assert rec == unique[rec['path']]
        unique[rec['path']] = rec
    canonical = json.dumps([unique[k] for k in sorted(unique)], sort_keys=True,
                           separators=(',', ':')).encode()
    return {'occurrences': len(records), 'unique_paths': len(unique),
            'canonical_deduplicated_sha256': hashlib.sha256(canonical).hexdigest()}


def guard():
    records = [fp('AGENTS.md'), fp('problems/2020-B4/statement.md')]
    old = obj(OLD_AUTHOR)
    assert len(old['payloads']) == 11
    records.append(fp(OLD_AUTHOR))
    records.extend(match(rec) for rec in old['payloads'])
    for path in OLD_REVIEWS:
        meta = obj(path)
        children = meta.get('payloads', meta.get('artifacts'))
        assert len(children) == 10
        records.append(fp(path))
        records.extend(match(rec) for rec in children)
    historical = obj(HISTORICAL_AUTHORITY)
    records.extend([fp(HISTORICAL_AUTHORITY), fp(HISTORICAL_AUTHORITY[:-5] + '.md')])
    records.extend([match(historical['accepted_copy']), match(historical['candidate'])])
    assert raw(historical['accepted_copy']['path']).endswith(raw(historical['candidate']['path']))
    accepted = []
    for path in AUTHORITIES:
        meta = obj(path)
        records.extend([fp(path), fp(path[:-5] + '.md'),
                        match(meta['accepted_copy']), match(meta['candidate'])])
        assert raw(meta['accepted_copy']['path']).endswith(raw(meta['candidate']['path']))
        accepted.append({'authority': fp(path), 'body': meta['accepted_copy'],
                         'historical_occurrences_bound_not_expanded': meta['record_occurrences_verified'],
                         'historical_unique_paths_bound_not_expanded': meta['unique_paths_verified']})
    records.append(fp('problems/2020-B4/notes/reasoning-Todd-return-r12-sources-v1.md'))
    parent = obj(PARENT)
    assert parent['older_plus_new_own_paths_bound_transitively'] == 886
    assert len(parent['payloads']) == 10
    records.append(fp(PARENT))
    records.extend(match(rec) for rec in parent['payloads'])
    detail = {
        'summary': doc_summary(records), 'old_author_ENTIRE12_unchanged': True,
        'both_old_initials_ENTIRE22_unchanged': True,
        'historical_R14_accepted_copy_and_records_preserved_not_used_to_validate_false_fractional_scope': True,
        'operative_TD_A9_exact_accepted_bindings': accepted,
        'own_immediate_parent_ENTIRE11_unchanged': True,
        'older_own_paths_bound_transitively': 886,
        'historical_inventory_recopied_or_old_code_executed': False,
        'SQ15_peer_or_NEW_affected_review_material_opened': False,
    }
    return records, detail


def unchanged_spans():
    old = raw(P + 'candidate-v1.md').decode()
    new = raw(P + 'candidate-v1.1.md').decode()
    def part(text, left, right):
        return text.split(left, 1)[1].split(right, 1)[0]
    spans = {
        'SQ14A_C_displayed_claims': (part(old, '**SQ14A,', '**SQ14D,'),
                                    part(new, '**SQ14A,', '**SQ14D,')),
        'main_sections1_3': (part(old, '## 1.', '## 4.'), part(new, '## 1.', '## 4.')),
    }
    result = {}
    for key, (a, b) in spans.items():
        assert a == b, key
        data = a.encode()
        result[key] = {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                       'textually_identical': True, 'not_independent_mathematical_review': True}
    return result


def labels():
    expected = [f'SQ14-{i:02d}' for i in range(1, 65)] + [f'SQ14-R{i:02d}' for i in range(1, 13)]
    for suffix in ['obligations-v1.1.md', 'constructor-checks-v1.1.md']:
        actual = re.findall(r'^\| (SQ14-(?:R)?\d{2}) \|', raw(P + suffix).decode(), re.M)
        assert actual == expected, suffix
    source = obj(P + 'sources-v1.1.json')
    assert source['whole_obligations'] == 76 and source['constructor_excluded'] is True
    return {'original': 64, 'repair': 12, 'whole': 76, 'separate_author_dispositions': 76,
            'labels_exact_and_unique': True, 'mathematics_proved_by_code': False}


def exact_diff():
    pieces = []
    pairs = [(P + stem + '-v1.md', P + stem + '-v1.1.md') for stem in TEXT_PAIRS]
    pairs.append((P + 'sources-v1.json', P + 'sources-v1.1.json'))
    for a, b in pairs:
        pieces.extend(difflib.unified_diff(raw(a).decode().splitlines(keepends=True),
                                            raw(b).decode().splitlines(keepends=True),
                                            fromfile=a, tofile=b))
    return ''.join(pieces).encode()


def write_new(path, value, replace_provisional=False):
    assert path.startswith(P) and 'v1.1.' in path
    if replace_provisional:
        assert path in [DIFF, BASELINE, VALIDATION]
        assert not (ROOT / MANIFEST).exists(), 'Frozen packets cannot be regenerated'
    with (ROOT / path).open('wb' if replace_provisional else 'xb') as out:
        if isinstance(value, bytes):
            out.write(value)
        else:
            out.write((json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode())


def prepare():
    records, detail = guard()
    identity = unchanged_spans()
    coverage = labels()
    write_new(DIFF, exact_diff(), replace_provisional=True)
    write_new(BASELINE, {'captured_at_utc': now(), 'records': records,
                         'detail': detail, 'unchanged_mathematical_text': identity}, replace_provisional=True)
    write_new(VALIDATION, {'validated_at_utc': now(), 'status': 'documentary PASS only',
                           'coverage': coverage, 'guard_summary': detail['summary'],
                           'unchanged_mathematical_text': identity,
                           'exact_FULL_eight_text_component_diff': fp(DIFF),
                           'old_source_ledger_archival_suffix_unchanged':
                           raw(P + 'sources-v1.1.md').endswith(raw(P + 'sources-v1.md'))}, replace_provisional=True)
    assert obj(VALIDATION)['old_source_ledger_archival_suffix_unchanged']
    print(json.dumps({'prepare': 'PASS', 'guard': detail['summary'],
                      'labels': coverage, 'diff': fp(DIFF)}))


def check():
    baseline = obj(BASELINE)
    for rec in baseline['records']:
        match(rec)
    records, detail = guard()
    assert records == baseline['records'] and detail == baseline['detail']
    assert unchanged_spans() == baseline['unchanged_mathematical_text']
    assert raw(DIFF) == exact_diff()
    assert obj(VALIDATION)['coverage'] == labels()
    return baseline


def freeze(attest):
    assert attest, 'FULL final model readback ALL13 payloads must precede freeze'
    baseline = check()
    source = obj(P + 'sources-v1.1.json')
    value = {
        'frozen_at_utc': now(), 'status': 'candidate proof - unverified, FULL author repair v1.1',
        'constructor': '/root/review_2022_complexity_r2', 'constructor_excluded': True,
        'substantive_literal_v1_fractional_scope_defect_acknowledged': True,
        'corrected_D_E_J_R_y_r_powers_orders_applications_INTEGRAL_only': True,
        'TD1_fractional_construction_and_actual_diagnostic_retained': True,
        'all_original64_plus_repair12': 76, 'constructor_hand_dispositions': 76,
        'TWO_OTHER_initially_blind_ENTIRE_affected_WHOLE_audits_required': True,
        'coordinator_promotion_or_independent_self_review': False,
        'requested': source['requested'], 'independent_effective_readback': None,
        'ENTIRE_files_including_manifest': 14,
        'old_author_freeze': fp(OLD_AUTHOR),
        'old_initial_review_manifests': [fp(p) for p in OLD_REVIEWS],
        'immediate_own_parent': fp(PARENT),
        'older_own_paths_bound_transitively': 886,
        'older_plus_new_own_paths_bound_transitively': 900,
        'guard_detail': baseline['detail'],
        'unchanged_mathematical_text': baseline['unchanged_mathematical_text'],
        'FULL_final_model_readback_ALL13_payloads_diff_code_generated_metadata_attested': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_required': True,
        'no_SQ15_peer_finding_files_filename_inventory_hash_metadata_access': True,
        'explicit_root_relay_of_diagnostic_disclosed': True,
        'no_NEW_affected_peer_review_material_access': True,
        'no_mathematical_program_CAS_scan_test_optimizer_old_author_source_replay': True,
        'no_Git_shared_old_cache_mutation_spawn_charge_contact_bypass': True,
        'weekly_telemetry': source['weekly_telemetry'],
        'payloads': [fp(P + suffix) for suffix in PAYLOADS],
    }
    write_new(MANIFEST, value)
    print(json.dumps({'freeze': 'PASS', 'at_utc': value['frozen_at_utc'],
                      'main': value['payloads'][0], 'manifest': fp(MANIFEST)}))


def verify():
    meta = obj(MANIFEST)
    assert len(meta['payloads']) == 13
    for rec in meta['payloads']:
        match(rec)
    baseline = check()
    assert meta['guard_detail'] == baseline['detail']
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'at_utc': now(),
                      'ENTIRE_files': 14, 'whole_obligations': 76,
                      'guard': baseline['detail']['summary'],
                      'main': meta['payloads'][0], 'manifest': fp(MANIFEST)}))


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
