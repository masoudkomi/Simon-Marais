#!/usr/bin/env python3
"""Exclusive administrative R2 byte/JSON freeze; no mathematical computation."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re

ROOT = Path.cwd().resolve()
P = 'problems/2020-B4/reviews/reasoning-arithmetic-return-r10-review-2-'
C = 'problems/2020-B4/notes/reasoning-arithmetic-return-r10-'
NOW = datetime.now(timezone.utc).isoformat()
assert ROOT.name == 'Website' and (ROOT / 'AGENTS.md').is_file()


def rec(path):
    raw = (ROOT / path).read_bytes()
    return dict(path=path, bytes=len(raw), sha256=sha256(raw).hexdigest())


def read(path):
    return json.loads((ROOT / path).read_text())


def out(suffix, value):
    with (ROOT / (P + suffix)).open('x', encoding='utf-8') as handle:
        json.dump(value, handle, indent=2, ensure_ascii=False)
        handle.write('\n')


rows, unique = [], {}


def bind(expected, label):
    expected = {key: expected[key] for key in ('path', 'bytes', 'sha256')}
    assert rec(expected['path']) == expected, expected['path']
    assert expected['path'] not in unique or unique[expected['path']] == expected
    unique[expected['path']] = expected
    rows.append(dict(label=label, **expected))


target = dict(path=C + 'candidate-v1.md', bytes=20380,
              sha256='774da07295679d39d7aa3b22485f986e2a2dfc9445d25d4a56a0a4c0d7bce233')
freeze = dict(path=C + 'freeze-v1.json', bytes=3016,
              sha256='68dd827ca8c9f4156317022115f0981d818335508067299167cfd2d85541de43')
bind(freeze, 'exact ENTIRE constructor freeze')
constructor = read(freeze['path'])
assert constructor['full_obligations'] == 52
for item in constructor['artifacts']:
    bind(item, 'complete constructor artifact')
bind(target, 'exact main independently reconstructed')
baseline = read(C + 'baseline-v1.json')
for item in baseline['records']:
    bind(item, 'constructor selected input identity; not historical recursion')
ordered_constructor = sorted(baseline['records'], key=lambda x: x['path'])
constructor_hash = sha256(json.dumps(ordered_constructor, sort_keys=True,
                                    separators=(',', ':')).encode()).hexdigest()
assert constructor_hash == baseline['canonical_deduplicated_sha256']
assert len(ordered_constructor) == baseline['deduplicated_paths_verified'] == 13

parent_path = 'problems/2021-B4/reviews/reasoning-return-r13-review-2-manifest-v1.json'
parent = rec(parent_path)
bind(parent, 'compact immediately preceding own ENTIRE whole review')
for item in read(parent_path)['artifacts']:
    if item['path'].endswith(('metadata-v1.json', 'input-validation-v1.json')):
        bind(item, 'necessary compact own parent metadata')

for number in (7, 8):
    authority_path = f'problems/2020-B4/reviews/reasoning-return-r{number}-acceptance.json'
    authority = read(authority_path)
    assert authority['unresolved_substantive_issues'] == 0
    bind(authority['accepted_copy'], 'specific accepted old input')

ids = re.findall(r'^\|(\d{2})\|', (ROOT / (P + 'ledger-v1.md')).read_text(), re.M)
assert ids == [f'{n:02d}' for n in range(1, 53)]
assert 'Scoped PASS' in (ROOT / (P + 'initial-v1.md')).read_text()
ordered = [unique[path] for path in sorted(unique)]
summary = dict(occurrences=len(rows), unique_paths=len(ordered),
               sha256=sha256(json.dumps(ordered, sort_keys=True,
                                        separators=(',', ':')).encode()).hexdigest())
out('baseline-v1.json', dict(captured_at_utc=NOW, summary=summary, records=ordered,
                            occurrence_labels=[dict(label=x['label'], path=x['path']) for x in rows],
                            old_history_recursively_rehashed=False))
out('metadata-v1.json', dict(
    status='ENTIRE OTHER initially blind WHOLE R2 complete; scoped PASS pending reconciliation',
    reviewer='/root', constructor='/root/review_2017_coarsening_r1',
    obligations=52, substantive_issues=0, required_repairs=0, closed_scope_notes=5,
    NEW_peer_R10_findings_files_metadata_read_or_hashed=False,
    incidental_peer_filename_only_disclosed=True, root_new_R10_inference=False,
    requested_model='gpt-6.1-sol', requested_reasoning='max',
    independently_verified_effective_setting_readback=None,
    mathematical_program_CAS_scan_author_rerun=False,
    root_Schmidt_visual_read_pages=[8, 9], root_claims_whole16page_read=False,
    classical_CFT_foundations_imported_not_whole296page_reconstruction=True,
    exact_source_limits=P + 'source-audit-v1.md', promotion=False))
out('input-validation-v1.json', dict(
    validated_at_utc=NOW, summary=summary, all_selected_fingerprints_match=True,
    constructor13path_summary_reconstructed=True, all52_ledger_rows_present=True,
    administrative_integrity_only_not_mathematical_testing=True))

for path, item in unique.items():
    assert rec(path) == item, path
suffixes = ['initial-v1.md', 'ledger-v1.md', 'issues-v1.md', 'source-audit-v1.md',
            'worklog-v1.md', 'freeze-v1.py', 'baseline-v1.json',
            'metadata-v1.json', 'input-validation-v1.json']
out('manifest-v1.json', dict(
    frozen_at_utc=NOW,
    status='ENTIRE OTHER initially blind WHOLE R2 complete; scoped PASS pending reconciliation',
    reviewer='/root', constructor='/root/review_2017_coarsening_r1', target=target,
    constructor_freeze=freeze, all_obligations_reconstructed=52,
    substantive_issues=0, required_repairs=0, closed_scope_notes=5,
    ENTIRE_before_ANY_NEW_peer_findings_files_or_metadata=True,
    input_summary=summary, compact_own_parent=parent,
    artifacts=[rec(P + suffix) for suffix in suffixes]))
for path, item in unique.items():
    assert rec(path) == item, path
print(json.dumps(dict(manifest=rec(P + 'manifest-v1.json'), initial=rec(P + 'initial-v1.md'),
                      summary=summary, obligations=52, promotion=False), indent=2))
