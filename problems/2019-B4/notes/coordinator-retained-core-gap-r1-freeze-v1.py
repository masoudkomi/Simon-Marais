"""Administrative create-new freeze; no mathematical evaluation or replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
PREFIX = 'problems/2019-B4/notes/coordinator-retained-core-gap-r1-'


def fp(path):
    data = (ROOT / path).read_bytes()
    return {'path': path, 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def rows(value):
    if isinstance(value, dict):
        if (isinstance(value.get('path'), str)
                and isinstance(value.get('bytes'), int)
                and isinstance(value.get('sha256'), str)):
            yield value
        for child in value.values():
            yield from rows(child)
    elif isinstance(value, list):
        for child in value:
            yield from rows(child)


def write(suffix, value):
    with (ROOT / (PREFIX + suffix)).open('x') as stream:
        json.dump(value, stream, indent=2)
        stream.write('\n')


if __name__ == '__main__':
    assert not (ROOT / (PREFIX + 'freeze-v1.json')).exists()
    authority = 'problems/2019-B4/reviews/coordinator-cap-gap-r1-acceptance.json'
    authority_bytes = (ROOT / authority).read_bytes()
    parent = json.loads(authority_bytes)
    assert parent['status'] == 'proved, independently reviewed scoped partial result'
    checked = {}
    occurrences = 0
    for expected in rows(parent):
        actual = fp(expected['path'])
        assert actual == {key: expected[key] for key in actual}, expected['path']
        checked[actual['path']] = actual
        occurrences += 1
    direct = [
        'AGENTS.md', 'problems/2019-B4/statement.md', authority,
        'problems/2019-B4/reviews/coordinator-cap-gap-r1-acceptance.md',
        'problems/2019-B4/reviews/coordinator-cap-gap-r1-acceptance-integrity.json',
        'problems/2019-B4/proofs/reviewed-thirdpass-v1.1.md',
        'problems/2019-B4/proofs/reviewed-moment-tail-v1.1.md',
        'problems/2019-B4/reviews/coordinator-cap-gap-r1-review-1-initial-v1.md',
    ]
    for path in direct:
        checked[path] = fp(path)
        occurrences += 1
    ordered = [checked[path] for path in sorted(checked)]
    for item in ordered:
        assert fp(item['path']) == item
    stamp = datetime.now(timezone.utc).isoformat()
    write('inputs-v1.json', {
        'recorded_at_utc': stamp,
        'administrative_only': True,
        'immutable_parent_acceptance': fp(authority),
        'current_record_occurrences_verified': occurrences,
        'current_unique_paths_verified': len(ordered),
        'records': ordered,
        'older_parent_inventory_bound_not_recopied': True,
        'historical_recheck_or_math_replay_claim': False,
        'root_constructor_requires_two_OTHER_whole_audits': True,
    })
    main = (ROOT / (PREFIX + 'candidate-v1.md')).read_text()
    obligations = (ROOT / (PREFIX + 'obligations-v1.md')).read_text()
    for n in range(1, 17):
        assert obligations.count('|RC-%02d|' % n) == 1
    assert 'Candidate proof - unverified' in main
    suffixes = ['candidate-v1.md', 'obligations-v1.md',
                'source-audit-v1.md', 'freeze-v1.py', 'inputs-v1.json']
    write('freeze-v1.json', {
        'frozen_at_utc': stamp,
        'status': 'candidate proof - unverified; complete mathematical checkpoint',
        'constructor': '/root',
        'requested_settings': {'model': 'gpt-6.1-sol', 'reasoning': 'max'},
        'independently_verified_effective_settings': None,
        'whole_author_obligations': 16,
        'two_OTHER_initially_blind_WHOLE_nonconstructor_audits_required': True,
        'proposed_new_upper': '1.834843',
        'root_constructor_excluded_from_independent_count': True,
        'mathematical_code_scan_CAS_sign_child_or_old_replay': False,
        'exact_rate_annual_or_novelty_claim': False,
        'immutable_accepted_parent': fp(authority),
        'current_record_occurrences_verified': occurrences,
        'current_unique_paths_verified': len(ordered),
        'artifacts': [fp(PREFIX + suffix) for suffix in suffixes],
    })
    print(json.dumps({'freeze': fp(PREFIX + 'freeze-v1.json'),
                      'main': fp(PREFIX + 'candidate-v1.md'),
                      'occurrences': occurrences, 'paths': len(ordered)}, indent=2))
