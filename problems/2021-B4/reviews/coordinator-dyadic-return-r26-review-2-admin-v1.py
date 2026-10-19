"""NEW R26 review2 documentary bytes/JSON/labels only; no mathematics.
prepare creates a compact baseline; freeze binds four final payloads;
verify is a SEPARATE read-only invocation. Never replay author/old code.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2021-B4/reviews/coordinator-dyadic-return-r26-review-2-'
PAYLOADS = [P + x for x in ['initial-v1.md', 'sources-v1.json', 'admin-v1.py', 'baseline-v1.json']]
FREEZE = P + 'manifest-v1.json'
BASELINE = P + 'baseline-v1.json'
AUTHOR = 'problems/2021-B4/notes/coordinator-dyadic-return-r26-'
AF = AUTHOR + 'freeze-v1.json'
PARENT = 'problems/2020-B4/notes/reasoning-global-return-r20-freeze-v1.json'
EXPECTED = {
    AF: (1605, '53490bd1b739294fce389af4b76ccc96339bfcc6471c619bedc3c5df33e6270a'),
    AUTHOR + 'candidate-v1.md': (20650, '892743f6ecea716e9e704e80112338c375c5b83dd515f44bdc0f71f648c80f92'),
    PARENT: (1776, 'ba2ea31635915d211efac6fc28024e6fefebe0f07e59df7eca31c6a52c831664'),
    'problems/2021-B4/proofs/reviewed-reasoning-deep-return-r24-v1.1.md':
        (27431, 'a52fcb31da9b494659d29b1ea0b587baba3a096264688ac6989e3d98ed578946'),
    'problems/2021-B4/proofs/reviewed-coordinator-dyadic-depth-return-r25-v1.1.md':
        (19422, '311568bc5ded810dfa823efedd968e9c0f05eb0ff129856499babb6785064c2e'),
}


def now():
    return datetime.now(timezone.utc).isoformat()


def fp(rel):
    data = (ROOT / rel).read_bytes()
    return dict(path=rel, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())


def read(rel):
    return json.loads((ROOT / rel).read_text())


def check(row):
    assert fp(row['path']) == row, row['path']


def create(rel, obj):
    assert rel.startswith(P)
    with (ROOT / rel).open('x') as stream:
        json.dump(obj, stream, indent=2)
        stream.write('\n')


def labels():
    text = (ROOT / PAYLOADS[0]).read_text()
    for i in range(1, 33):
        assert text.count('|R26-' + str(i).zfill(2) + '|') == 1
    assert read(PAYLOADS[1])['whole_obligations'] == 32


def prepare():
    author = read(AF)
    paths = ['AGENTS.md', 'problems/2021-B4/statement.md', AF]
    for row in author['payloads']:
        check(row)
        paths.append(row['path'])
    paths.append(AUTHOR + 'exploration-unverified.md')
    for stem in ['reasoning-deep-return-r24', 'coordinator-dyadic-depth-return-r25']:
        js = 'problems/2021-B4/reviews/' + stem + '-acceptance.json'
        authority = read(js)
        assert authority['status'] == 'proved, independently reviewed scoped partial result'
        check(authority['accepted_copy'])
        paths += [authority['accepted_copy']['path'], js[:-4] + 'md', js]
    paths.append(PARENT)
    assert len(paths) == len(set(paths))
    records = [fp(p) for p in paths]
    for row in records:
        if row['path'] in EXPECTED:
            assert (row['bytes'], row['sha256']) == EXPECTED[row['path']], row['path']
    labels()
    create(BASELINE, dict(created_utc=now(), necessary_immutable_records=records,
                         record_occurrences=len(records), unique_paths=len(paths),
                         ONE_exact_own_parent=fp(PARENT), parent_payload_inventory_not_expanded=True,
                         author_baseline_bound_as_payload_not_recursive_guard_copy=True,
                         living_maps_guarded=False, new_corresponding_peer_access=False,
                         forbidden_R27_access=False, mathematical_code=False))
    print(json.dumps(dict(prepared=fp(BASELINE), necessary_paths=len(paths), utc=now()), indent=2))


def guards():
    baseline = read(BASELINE)
    for row in baseline['necessary_immutable_records']:
        check(row)
    return baseline


def freeze():
    b = guards()
    labels()
    create(FREEZE, dict(frozen_utc=now(), status='sealed initially blind OTHER whole2 initial',
                       whole_obligations=32, entire_files=5, reviewer='B', constructor='/root; excluded',
                       payloads=[fp(p) for p in PAYLOADS],
                       ONE_exact_own_parent=b['ONE_exact_own_parent'],
                       necessary_record_occurrences=b['record_occurrences'],
                       necessary_unique_paths=b['unique_paths'],
                       FULL_final_ALL4_payload_MODEL_readbacks_completed=True,
                       FULL_manifest_MODEL_readback_THEN_SEPARATE_readonly_verify_required=True,
                       corresponding_new_peer_access=False, forbidden_R27_access=False,
                       release_requires_explicit_root_BOTH=True,
                       requested_model='gpt-6.1-sol', requested_reasoning='max', effective_readback=None,
                       authorized_reset=1792874445, total_weekly_ceiling=90, reserve=True,
                       mathematical_truth_checked_by_code=False))
    print(json.dumps(dict(manifest=fp(FREEZE), utc=now()), indent=2))


def verify():
    f = read(FREEZE)
    assert [x['path'] for x in f['payloads']] == PAYLOADS
    for row in f['payloads']:
        check(row)
    b = guards()
    labels()
    assert f['entire_files'] == len(PAYLOADS) + 1 == 5
    print(json.dumps(dict(SEPARATE_readonly_verify_utc=now(), result='PASS', entire_files=5,
                         literal_obligation_labels=32, necessary_paths=b['unique_paths'],
                         manifest=fp(FREEZE), payloads=[fp(p) for p in PAYLOADS],
                         writes=0, mathematics_certified=False), indent=2))


if __name__ == '__main__':
    assert len(sys.argv) == 2 and sys.argv[1] in ['prepare', 'freeze', 'verify']
    {'prepare': prepare, 'freeze': freeze, 'verify': verify}[sys.argv[1]]()
