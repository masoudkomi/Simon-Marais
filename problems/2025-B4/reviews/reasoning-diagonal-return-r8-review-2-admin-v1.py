#!/usr/bin/env python3
"""NEW documentary-only DR8 WHOLE2 integrity. No mathematical execution."""
from datetime import datetime, timezone
import argparse
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2025-B4/reviews/reasoning-diagonal-return-r8-review-2-'
A = 'problems/2025-B4/notes/reasoning-diagonal-return-r8-'
AF = A + 'freeze-v1.json'
AF_EXPECT = (3635, '53ce3848114979fe2f882c7ef22ac3d97e4f79880a1abec92ddfcda4964d4323')
AM = A + 'candidate-v1.md'
AM_EXPECT = (15008, '2e793eb556b4a3063dbdde1cf0b16b7f9f53eec4e36469adf31693b022b19a47')
PARENT = 'problems/2022-B4/notes/reasoning-dynamics-return-r9-freeze-v1.json'
PARENT_EXPECT = (3635, '4427de51ab82207eb673d983f9abfedec5553f783bbd1093e29f6ca49659036a')
PAYLOADS = [P + x for x in [
    'report-v1.md', 'ledger-v1.md', 'issues-v1.md', 'sources-v1.md',
    'sources-v1.json', 'worklog-v1.md', 'admin-v1.py', 'baseline-v1.json',
    'input-validation-v1.json', 'metadata-v1.json']]
MANIFEST = P + 'manifest-v1.json'

def now():
    return datetime.now(timezone.utc).isoformat()

def raw(path):
    p = Path(path)
    assert not p.is_absolute() and '..' not in p.parts
    assert not path.startswith('problems/2025-B4/reviews/reasoning-diagonal-return-r8-review-1-'), 'NEW OTHER peer embargo'
    return (ROOT / path).read_bytes()

def rec(path):
    b = raw(path)
    return {'path': path, 'bytes': len(b), 'sha256': hashlib.sha256(b).hexdigest()}

def obj(path):
    return json.loads(raw(path))

def checked(r):
    got = rec(r['path'])
    assert got == {k: r[k] for k in ('path', 'bytes', 'sha256')}, r['path']
    return got

def expected(path, value):
    return checked({'path': path, 'bytes': value[0], 'sha256': value[1]})

def summary(rows):
    unique = {}
    for r in rows:
        if r['path'] in unique:
            assert unique[r['path']] == r
        unique[r['path']] = r
    ordered = sorted(unique.values(), key=lambda r: r['path'])
    blob = json.dumps(ordered, sort_keys=True, separators=(',', ':')).encode()
    return {'occurrences': len(rows), 'unique_paths': len(ordered),
            'canonical_deduplicated_sha256': hashlib.sha256(blob).hexdigest()}, ordered

def author_direct_bindings():
    b = obj(A + 'baseline-v1.json')['compact_bindings']
    old = obj(b['operative_DR7_original_ENTIRE14_binding']['path'])
    old_rows = [checked(b['operative_DR7_original_ENTIRE14_binding'])] + [checked(r) for r in old['artifacts']]
    assert len(old_rows) == 14
    ap = obj(b['own_immediate_parent_manifest']['path'])
    ap_rows = [checked(b['own_immediate_parent_manifest'])] + [checked(r) for r in ap['payloads']]
    assert len(ap_rows) == 11
    rows = old_rows + ap_rows
    for group in [b['operative_DR7']] + b['comparison_only_DR6_RD']:
        rows += [checked(r) for r in group.values()]
        assert raw(group['accepted_copy']['path']).endswith(raw(group['exact_candidate_suffix']['path']))
    rows += [checked(r) for r in b['direct_AGENTS_statement_and_PG_comparison']]
    actual, _ = summary(rows)
    wanted = b['current_frozen_protection']
    assert (actual['occurrences'], actual['unique_paths'], actual['canonical_deduplicated_sha256']) == (
        wanted['occurrences'], wanted['unique_paths'], wanted['canonical_sha256'])
    return rows, {'occurrences': actual['occurrences'], 'unique_paths': actual['unique_paths'],
                  'canonical_sha256': actual['canonical_deduplicated_sha256']}

def inputs():
    expected(AM, AM_EXPECT)
    rows = [expected(AF, AF_EXPECT)]
    author = obj(AF)
    assert author['ENTIRE_files'] == 14 and len(author['payloads']) == 13
    rows += [checked(r) for r in author['payloads']]
    direct, direct_summary = author_direct_bindings()
    rows += direct
    rows += [expected(PARENT, PARENT_EXPECT)]
    parent = obj(PARENT)
    assert parent['ENTIRE_files'] == 12 and len(parent['payloads']) == 11
    rows += [checked(r) for r in parent['payloads']]
    return rows, {
        'author_ENTIRE_files_verified': 14,
        'author_necessary_direct_bindings_verified': direct_summary,
        'own_immediate_parent_ENTIRE_files_verified': 12,
        'own_parent_historical_guard_summary_bound_not_recopied': parent['guard_summary'],
        'author_mutable_research_observation_not_asserted_current': True,
        'historical_inventories_recursively_copied': False,
        'old_author_source_executable_or_mathematical_instance_run': False,
        'NEW_OTHER_DR8_peer_material_access': False}

def labels():
    text = raw(P + 'ledger-v1.md').decode()
    found = re.findall(r'^\|(DR8-\d{2})\|', text, flags=re.M)
    assert found == ['DR8-%02d' % i for i in range(1, 65)]
    return {'whole_obligations': 64, 'separate_dispositions': 64,
            'label_check_not_mathematical_proof': True}

def write_new(path, data):
    with (ROOT / path).open('x') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')

def prepare():
    assert not (ROOT / MANIFEST).exists()
    rows, detail = inputs()
    totals, unique = summary(rows)
    write_new(P + 'baseline-v1.json', {'prepared_at_utc': now(),
        'status': 'documentary integrity only', 'guard_summary': totals,
        'detail': detail, 'guards': unique})
    write_new(P + 'input-validation-v1.json', {'validated_at_utc': now(),
        'status': 'documentary PASS only', 'author_ENTIRE14_preserved': True,
        'author_necessary_direct_declarations_verified': True,
        'own_D9_parent_ENTIRE12_preserved': True, 'labels': labels(),
        'guard_summary': totals, 'NEW_peer_access': False,
        'mathematical_program_or_old_author_source_replay': False})
    write_new(P + 'metadata-v1.json', {'created_at_utc': now(),
        'status': 'one OTHER initially blind ENTIRE WHOLE audit, not acceptance',
        'reviewer': '/root/review_2017_coarsening_r1',
        'NEW_DR8_constructor_or_contributor': False, 'NEW_DR7_constructor': False,
        'older_roles_disclosed_no_self_recertification': True,
        'NEW_OTHER_peer_material_access': False, 'whole_obligations': 64,
        'payload_files': 10, 'ENTIRE_files': 11,
        'findings_EMBARGOED_until_explicit_BOTH_ENTIRE_confirmation': True,
        'FULL_final_ALL10_payload_model_readback_REQUIRED_before_freeze': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
        'verified_effective_readback': None,
        'authorized_weekly_reset': 1792874445, 'last_direct_TOTAL_percent': 54,
        'TOTAL_ceiling_percent': 90, 'integration_reserve': True,
        'automatic_later_window': False,
        'mathematical_code_CAS_scan_test_source_author_old_replay': False,
        'old_shared_Git_cache_mutation_spawn_charge_contact_bypass': False})
    print(json.dumps({'prepared': True, 'guards': totals, 'labels': labels()}))

def validate():
    b = obj(P + 'baseline-v1.json')
    for r in b['guards']:
        checked(r)
    rows, detail = inputs()
    totals, unique = summary(rows)
    assert totals == b['guard_summary'] and unique == b['guards'] and detail == b['detail']
    assert obj(P + 'input-validation-v1.json')['labels'] == labels()
    return b

def freeze(attested):
    assert attested, 'FULL final model readback must be completed first'
    b = validate()
    write_new(MANIFEST, {'frozen_at_utc': now(),
        'status': 'initially peer-blind OTHER whole audit; not acceptance',
        'reviewer': '/root/review_2017_coarsening_r1',
        'NEW_DR8_constructor_or_contributor': False, 'whole_obligations': 64,
        'payload_files': 10, 'ENTIRE_files': 11,
        'author': rec(AF), 'immediate_own_parent': rec(PARENT),
        'guard_summary': b['guard_summary'],
        'FULL_final_model_readback_ALL10_payloads_completed': True,
        'FULL_manifest_model_readback_then_SEPARATE_readonly_verify_REQUIRED': True,
        'NEW_OTHER_peer_material_access_before_freeze': False,
        'findings_EMBARGOED_until_explicit_BOTH_ENTIRE_confirmation': True,
        'mathematical_execution_or_old_author_source_replay': False,
        'payloads': [rec(p) for p in PAYLOADS]})
    print(json.dumps({'manifest': rec(MANIFEST), 'frozen_at_utc': obj(MANIFEST)['frozen_at_utc']}))

def verify():
    m = obj(MANIFEST)
    assert m['ENTIRE_files'] == len(m['payloads']) + 1 == 11
    assert {r['path'] for r in m['payloads']} == set(PAYLOADS)
    for r in m['payloads']:
        checked(r)
    b = validate()
    assert b['guard_summary'] == m['guard_summary']
    print(json.dumps({'SEPARATE_readonly_verify': 'PASS', 'verified_at_utc': now(),
        'ENTIRE_files': 11, 'whole_obligations': 64, 'guard_summary': b['guard_summary'],
        'report': rec(P + 'report-v1.md'), 'manifest': rec(MANIFEST)}, indent=2))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['prepare', 'freeze', 'verify'])
    parser.add_argument('--attest-final-model-readback', action='store_true')
    args = parser.parse_args()
    if args.mode == 'prepare':
        prepare()
    elif args.mode == 'freeze':
        freeze(args.attest_final_model_readback)
    else:
        verify()
