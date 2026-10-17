"""ADMINISTRATIVE fingerprints/JSON only; no mathematical calculation.

Writes only reasoning-return-r10-* files. No Git, source download,
mathematical executable, old certificate replay, scan or author rerun.
Run --prepare before the complete constructor checkpoint, then --freeze.
The frozen v1 manifest is never overwritten.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2021-B4/notes/reasoning-return-r10-'
HEX64 = re.compile(r'^[0-9a-f]{64}$')

KNOWN = [
    ('AGENTS.md', 4707,
     '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'),
    ('problems/2021-B4/proofs/reviewed-reasoning-return-r8-v1.1.md', 19921,
     '33b8713d402d09f711d0096cdc4e8c00f9e622a5335f8e3345eb4f82ba0d359d'),
    ('problems/2021-B4/proofs/reviewed-reasoning-return-r9-v1.1.md', 22183,
     '9cac411e50b28dd30bd961afc4fb1902556d716154c2d75a64a618115f7ec384'),
    ('problems/2021-B4/proofs/reviewed-odd-support-exclusion-v1.1.md', 8176,
     '56274936ab198f01cb38b1701fdec7907860eb654fd2bc79c3b2d0e03054a271'),
    ('problems/2021-B4/proofs/reviewed-reasoning-J15-v1.1.md', 18931,
     'fbc5d212b5b560c8e4e42397d19663f3fc882fa8f206bdcbb4ed897c715627f6'),
    ('problems/2021-B4/proofs/reviewed-reasoning-return-r5-v1.1.md', 23675,
     'f4f088adc133b0581520488cdbba30082c13b2402c96ae555142e5491ad4137d'),
    ('problems/2019-B4/reviews/coordinator-separation-scale-r1-review-1-manifest-v1.json', 4959,
     '7268fc828f2b066569daf08da5606351b5f71b7e27078cc6f4a7c898667d191e'),
]

AUTHORITY_STEMS = [
    'reasoning-J15', 'odd-support-exclusion',
    'reasoning-return-r5', 'reasoning-return-r8', 'reasoning-return-r9',
]
AUTHORITY_JSON = [
    f'problems/2021-B4/reviews/{stem}-acceptance{suffix}.json'
    for stem in AUTHORITY_STEMS for suffix in ['', '-integrity']
]
PARENT_JSON = [
    'problems/2019-B4/reviews/coordinator-separation-scale-r1-review-1-manifest-v1.json',
    'problems/2019-B4/reviews/coordinator-separation-scale-r1-review-1-input-validation-v1.json',
]
DIRECT_READ_FILES = [
    'AGENTS.md', 'problems/2021-B4/statement.md',
    *[p for p, _, _ in KNOWN if '/proofs/' in p],
    *[f'problems/2021-B4/reviews/{s}-acceptance.md'
      for s in AUTHORITY_STEMS],
    'problems/2021-B4/notes/reasoning-return-r9-source-audit-v1.md',
    'problems/2021-B4/notes/reasoning-return-r9-failed-routes-v1.md',
]


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def safe_path(path: str) -> Path:
    # Explicit blindness guard for the queued, not-yet-started review.
    if ('problems/2022-B4/' in path and 'reasoning-return-r8' in path):
        raise AssertionError(f'Queued2022R8 input must not be opened: {path}')
    return Path(path) if Path(path).is_absolute() else ROOT / path


def raw_fingerprint(path: str) -> dict:
    data = safe_path(path).read_bytes()
    return {'path': path, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def dump_owned(suffix: str, doc: dict) -> None:
    path = ROOT / (PREFIX + suffix)
    if not str(path).startswith(str(ROOT / PREFIX)):
        raise AssertionError('Write escaped the owned prefix')
    path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + '\n')


def walk_records(value):
    if isinstance(value, dict):
        path = value.get('path')
        digest = value.get('sha256')
        if (isinstance(path, str) and isinstance(digest, str)
                and HEX64.fullmatch(digest)):
            length = value.get('bytes')
            yield {'path': path, 'sha256': digest,
                   **({'bytes': length} if isinstance(length, int) else {})}
        for child in value.values():
            yield from walk_records(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_records(child)


def validate_inputs() -> dict:
    cached = {}
    occurrences = []

    def actual(path):
        if path not in cached:
            cached[path] = raw_fingerprint(path)
        return cached[path]

    def check(record, origin):
        found = actual(record['path'])
        assert found['sha256'] == record['sha256'], (origin, record, found)
        if 'bytes' in record:
            assert found['bytes'] == record['bytes'], (origin, record, found)
        occurrences.append((origin, found))
        return found

    anchors = [check({'path': p, 'bytes': n, 'sha256': h},
                     'previously declared immutable anchor')
               for p, n, h in KNOWN]
    direct = [actual(p) for p in DIRECT_READ_FILES]

    metadata_paths = list(AUTHORITY_JSON) + list(PARENT_JSON)
    # The compact R8/R9 coordinator integrity records specify the exact
    # already-frozen input documents whose declared rows were checked.
    # Verify those rows anew; bind their inventories rather than copying.
    for stem in ['reasoning-return-r8', 'reasoning-return-r9']:
        path = f'problems/2021-B4/reviews/{stem}-acceptance-integrity.json'
        doc = json.loads(safe_path(path).read_text())
        for item in doc.get('inputs', []):
            metadata_paths.append(item['metadata']['path'])
    metadata_paths = list(dict.fromkeys(metadata_paths))
    metadata = []
    for path in metadata_paths:
        binding = actual(path)
        doc = json.loads(safe_path(path).read_text())
        rows = list(walk_records(doc))
        for row in rows:
            check(row, path)
        metadata.append({'metadata': binding,
                         'declared_fingerprint_occurrences_verified': len(rows)})
    # Direct bindings join the deduplicated summary but do not invent
    # historical declarations when none were made.
    unique = {p: {'path': p, 'bytes': d['bytes'], 'sha256': d['sha256']}
              for p, d in cached.items()}
    canonical = json.dumps([unique[p] for p in sorted(unique)],
                           sort_keys=True, separators=(',', ':')).encode()
    return {
        'checked_at_utc': now(), 'administrative_only': True,
        'all_verified': True, 'no_mathematical_code_or_certificate_rerun': True,
        'complete_new_2022R8_packet_and_peer_findings_not_opened': True,
        'previously_declared_anchors': anchors,
        'direct_mathematical_scope_and_protocol_bindings': direct,
        'immutable_parent_metadata': metadata,
        'declared_fingerprint_occurrences_verified': len(occurrences),
        'unique_paths_fingerprinted': len(unique),
        'canonical_deduplicated_summary_sha256': hashlib.sha256(canonical).hexdigest(),
        'canonical_digest_encoding': 'UTF8 JSON sorted unique path/bytes/sha256 records, sort_keys=True, separators comma/colon',
        'historical_rows_bound_in_parent_metadata_not_copied': True,
        'parent_rows_can_be_reproduced_by_this_exact_script': True,
        'unrelated_old_mathematics_not_reread_for_hash_preservation': True,
        'source_urls_fresh_browser_text_no_new_download_hash_claim': True,
    }


def sources(validation: dict) -> dict:
    return {
        'recorded_at_utc': now(),
        'status': 'candidate proof - unverified; constructor source record',
        'primary_public_sources': [
            {'title': 'Official SMMC2021 Paper B',
             'url': 'https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf',
             'actual_scope': 'page2 B4 full hypothesis and(b) target only; no preliminary proof',
             'local_statement': 'problems/2021-B4/statement.md',
             'fresh_local_PDF_sha256': None},
            {'title': 'Atkinson-Sharma1969, A partial characterization of poised Hermite-Birkhoff interpolation problems',
             'url': 'https://homepage.math.uiowa.edu/~atkinson/papers/HB_interp.pdf',
             'actual_scope': 'complete six pages230-235, all226 browser-extracted lines, definitions/Theorem2/full proof and distinct unused converse conjecture',
             'use': 'published sufficient criterion via accepted R9; no all-roots-real hypothesis',
             'fresh_local_PDF_sha256': None},
            {'title': 'Castryck-Laterveer-Ounaies, Constraints on counterexamples to the Casas-Alvero conjecture, and a verification in degree12',
             'url': 'https://arxiv.org/pdf/1208.5404',
             'actual_scope': 'Section3.4/Lemma17; Proposition19 complete statement/proof and following unramified remark, not whole23-page external proof or degree certificate',
             'use': 'normalization attribution and exact stronger-theorem boundary',
             'fresh_local_PDF_sha256': None},
        ],
        'accepted_bodies': [x for x in validation['direct_mathematical_scope_and_protocol_bindings']
                            if '/proofs/' in x['path']],
        'accepted_authority_and_historical_rows': 'Exact parents bound in input-validation-v1.json; no inventory duplication',
        'fresh_full_R6_or_all_R7_read_claim': False,
        'new_proof_supplied_in_main': ['unit and T4 bootstrap from actual late availability',
                                       'quartic Euler functional and complete six-pattern hand proof',
                                       'actual gcd uniqueness and coefficient gaps',
                                       'exact W/Wprime collision comparison and depth-one congruence'],
        'older_roles': ['constructor of accepted R6/R7/R8',
                        'old J15/PN/R5 whole reviewer; no independent self-recertification'],
        'root_role': 'generic research prompt only; no new R10 mathematical inference',
        'two_OTHER_fresh_initially_blind_whole_nonconstructor_audits_required': True,
        'no_new_2022R8_packet_or_peer_findings_opened': True,
        'no_mathematical_executable_CAS_scan_or_author_rerun': True,
        'no_charge_contact_bypass_or_full_third_party_paper_in_packet': True,
    }


def main() -> None:
    assert sys.argv[1:] in [['--prepare'], ['--freeze']], 'Use --prepare or --freeze'
    manifest_path = ROOT / (PREFIX + 'freeze-v1.json')
    assert not manifest_path.exists(), 'Frozen v1 must never be overwritten'
    validation = validate_inputs()
    dump_owned('input-validation-v1.json', validation)
    dump_owned('sources-v1.json', sources(validation))
    brief = {
        'at_utc': now(), 'administrative_only': True, 'all_old_inputs_match': True,
        'declared_fingerprint_occurrences_verified': validation['declared_fingerprint_occurrences_verified'],
        'unique_paths_fingerprinted': validation['unique_paths_fingerprinted'],
        'canonical_deduplicated_summary_sha256': validation['canonical_deduplicated_summary_sha256'],
        'new_main': raw_fingerprint(PREFIX + 'candidate-v1.md'),
        'whole_obligations': 52,
        'no_math_executable_or_queued_2022R8_read': True,
    }
    if sys.argv[1] == '--prepare':
        print(json.dumps(brief, indent=2))
        return
    dump_owned('freeze-output-v1.json', brief)
    suffixes = ['candidate-v1.md', 'obligations-v1.md', 'failed-routes-v1.md',
                'source-audit-v1.md', 'constructor-checks-v1.md', 'worklog-v1.md',
                'sources-v1.json', 'freeze-v1.py', 'input-validation-v1.json',
                'freeze-output-v1.json']
    manifest = {
        'frozen_at_utc': now(),
        'status': 'candidate proof - unverified; COMPLETE meaningful constructor checkpoint',
        'constructor': '/root/review_2021_reasoning_j15_r2',
        'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max'},
        'independently_verified_effective_settings': None,
        'claims': ['R10A actual m7/outer-r1 branch has an early inner-only odd order',
                   'R10B unique such order forces actual simple tail gcds, exact gaps, nu1/Delta14 and explicit19^12 congruence',
                   'R10C nu>=2 or delta0 forces at least two early inner-only odd orders'],
        'all_whole_obligations': 52,
        'actual_branch_first_break_and_ordinary_geometry_retained': True,
        'T4_and_a2_unit_are_proved_under_t_at_most_one_not_extra_assumptions': True,
        'root_broad_assignment_no_new_proof_inference': True,
        'two_OTHER_fresh_initially_blind_WHOLE_nonconstructor_audits_required': True,
        'no_full_m7_J15_degree20_annual_lift_or_novelty_claim': True,
        'no_mathematical_executable_CAS_scan_certificate_or_author_rerun': True,
        'no_new_2022R8_packet_or_peer_review_finding_opened': True,
        'no_old_shared_Git_cache_edit_spawn_charge_contact_bypass': True,
        'compact_old_inputs': {
            'declared_fingerprint_occurrences_verified': validation['declared_fingerprint_occurrences_verified'],
            'unique_paths_fingerprinted': validation['unique_paths_fingerprinted'],
            'canonical_deduplicated_summary_sha256': validation['canonical_deduplicated_summary_sha256'],
            'immutable_parent_metadata_not_expanded_in_new_inventory': True,
        },
        'authoritative_account_weekly': {
            'at_utc': '2026-10-17 19:29:14 UTC', 'total_used_percent': 59,
            'window_minutes': 10080, 'reset_unix': 1792745187,
            'ordinary_usage_allowed': True, 'total_ceiling_percent': 90,
            'integration_reserve': True,
        },
        'administrative_command': '.venv/bin/python problems/2021-B4/notes/reasoning-return-r10-freeze-v1.py --freeze',
        'artifacts': [raw_fingerprint(PREFIX + s) for s in suffixes],
    }
    dump_owned('freeze-v1.json', manifest)
    final = raw_fingerprint(PREFIX + 'freeze-v1.json')
    print(json.dumps({'freeze': final, **brief}, indent=2))


if __name__ == '__main__':
    main()
