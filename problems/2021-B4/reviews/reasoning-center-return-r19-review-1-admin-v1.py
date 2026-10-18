#!/usr/bin/env python3
"""R19 root review byte administration only; no mathematical computation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, sys
ROOT = Path(__file__).resolve().parents[3]
PRE = 'problems/2021-B4/reviews/reasoning-center-return-r19-review-1-'
AUTHOR = 'problems/2021-B4/notes/reasoning-center-return-r19-freeze-v1.json'
PIN = {'path': AUTHOR, 'bytes': 3893, 'sha256': 'dfe7b6b4f372b44a2806fc96ce41613bfc2fb7e8f5469fc2d10552aa83b835d3'}
STATIC = ('report-v1.md', 'ledger-v1.md', 'issues-v1.md', 'sources-v1.md', 'sources-v1.json', 'worklog-v1.md', 'admin-v1.py')
GENERATED = ('baseline-v1.json', 'input-validation-v1.json', 'metadata-v1.json')
def now(): return datetime.now(timezone.utc).isoformat()
def raw(p):
    assert p == 'AGENTS.md' or p.startswith('problems/2021-B4/')
    assert '..' not in Path(p).parts and not p.startswith('/')
    assert not p.startswith('problems/2021-B4/reviews/reasoning-center-return-r19-review-2-')
    return (ROOT/p).read_bytes()
def obj(p): return json.loads(raw(p))
def fp(p):
    b = raw(p)
    return dict(path=p, bytes=len(b), sha256=hashlib.sha256(b).hexdigest())
def check(x):
    y = {k:x[k] for k in ('path','bytes','sha256')}
    assert fp(x['path']) == y, x['path']
    return y
def inputs():
    rows = [check(PIN)]
    a = obj(AUTHOR)
    assert a['whole_obligations'] == 64 and a['ENTIRE_files'] == 13
    rows += [check(x) for x in a['payloads']]
    for n in ('reasoning-center-return-r18', 'reasoning-center-return-r17', 'reasoning-return-r8', 'reasoning-return-r5'):
        p = 'problems/2021-B4/reviews/'+n+'-acceptance.json'
        v = obj(p)
        assert v['status'].startswith('proved, independently reviewed')
        assert v['unresolved_substantive_issues'] == 0 and not v['repair_required']
        c, b = check(v['candidate']), check(v['accepted_copy'])
        assert raw(b['path']).endswith(raw(c['path']))
        rows += [fp(p), fp(p[:-5]+'.md'), b]
    for p in ('AGENTS.md', 'problems/2021-B4/statement.md', 'problems/2021-B4/notes/reasoning-center-return-r18-failures-v1.md', 'problems/2021-B4/notes/reasoning-center-return-r18-sources-v1.md', 'problems/2021-B4/notes/reasoning-center-return-r17-failures-v1.md', 'problems/2021-B4/notes/reasoning-return-r8-failed-routes-v1.md'):
        rows.append(fp(p))
    assert len(rows) == len({x['path'] for x in rows}) == 31
    return sorted(rows, key=lambda x:x['path'])
def labels():
    ids = re.findall(r'(?m)^(\d+)\. PASS — ', raw(PRE+'ledger-v1.md').decode())
    assert ids == [str(i) for i in range(1,65)]
    assert obj(PRE+'sources-v1.json')['no_corresponding_NEW_B_R19_finding_file_hash_metadata_access']
def put(s,v):
    assert s in GENERATED + ('manifest-v1.json',)
    with (ROOT/(PRE+s)).open('x') as f:
        json.dump(v,f,indent=2); f.write('\n')
def prepare():
    rows = inputs(); labels()
    put('baseline-v1.json', dict(at_utc=now(), protected_unique_paths=31, fingerprints=rows, all13_author_files_and_four_current_authorities_bound=True, unrelated_pending_review_ancestry_not_copied=True, historical_mutable_map_not_a_current_proof_premise=True))
    put('input-validation-v1.json', dict(at_utc=now(), result='PASS', protected31=True, author13=True, all4_current_authorities_and_exact_candidate_suffixes_checked=True, ALL64_ledger_labels=True, mathematical_computation=False))
    put('metadata-v1.json', dict(at_utc=now(), status='initial whole review; findings embargoed', reviewer='/root', constructor='/root/review_2021_reasoning_j15_r2', constructor_excluded=True, root_new_construction_inference=False, whole_obligations=64, ENTIRE_files_including_manifest=11, no_corresponding_NEW_B_R19_finding_file_hash_metadata_access=True, ALL_files_freeze_FULL_final_readback_SEPARATE_verify_before_peer=True, BOTH_explicit_before_findings_release=True, no_substantive_defect_or_required_repair=True, closed_scope_notes=6, requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True), independent_effective_readback=None, authorized_weekly_reset=1792874445, ceiling_TOTAL_percent=90, integration_reserve=True, automatic_later_window_authorized=False, mathematical_program_CAS_scan_author_source_or_old_replay=False))
    print(json.dumps(dict(prepare='PASS',protected31=True,ALL64=True,ENTIRE_files=11)))
def preserved():
    assert inputs() == obj(PRE+'baseline-v1.json')['fingerprints']; labels()
def freeze():
    preserved()
    put('manifest-v1.json', dict(frozen_at_utc=now(), status='ENTIRE initially blind WHOLE1 initial; findings embargoed', reviewer='/root', constructor_excluded=True, whole_obligations=64, ENTIRE_files_including_manifest=11, all_report_ALL64_issues_sources_logs_code_ALLmetadata=True, FULL_final_ALL11_model_readback_and_SEPARATE_verify_follow_freeze=True, no_corresponding_NEW_B_R19_finding_file_hash_metadata_access=True, BOTH_explicit_before_release=True, mathematical_computation=False, payloads=[fp(PRE+s) for s in STATIC+GENERATED]))
    print(json.dumps(dict(manifest=fp(PRE+'manifest-v1.json'),ENTIRE_files=11,ALL64=True)))
def verify():
    preserved(); v=obj(PRE+'manifest-v1.json')
    assert [x['path'] for x in v['payloads']] == [PRE+s for s in STATIC+GENERATED]
    for x in v['payloads']: check(x)
    print(json.dumps(dict(SEPARATE_postfreeze_verify='PASS',at_utc=now(),manifest=fp(PRE+'manifest-v1.json'),report=fp(PRE+'report-v1.md'),ENTIRE_files=11,whole_obligations=64,protected31=True,administrative_not_proof=True)))
if __name__ == '__main__': dict(prepare=prepare,freeze=freeze,verify=verify)[sys.argv[1]]()
