#!/usr/bin/env python3
"""Administrative preservation only; no mathematical computation or tests."""
from pathlib import Path
import argparse, datetime, hashlib, json, re
ROOT = Path(__file__).resolve().parents[3]
P = 'problems/2021-B4/reviews/reasoning-center-return-r17-review-1-'
A = 'problems/2021-B4/notes/reasoning-center-return-r17-'
PARENT = 'problems/2025-B4/reviews/reasoning-branch-return-r4-review-1-manifest-v1.json'
PAYLOAD = ['initial-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md','sources-v1.json','worklog-v1.md','freeze-v1.py','baseline-v1.json','input-validation-v1.json','metadata-v1.json']
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat()
def raw(p):
    assert not p.startswith('problems/2021-B4/reviews/reasoning-center-return-r17-review-2-')
    return (ROOT / p).read_bytes()
def obj(p): return json.loads(raw(p))
def fp(p):
    b = raw(p)
    return dict(path=p, bytes=len(b), sha256=hashlib.sha256(b).hexdigest())
def check(r):
    assert fp(r['path']) == {k:r[k] for k in ['path','bytes','sha256']}, r['path']
    return fp(r['path'])
def put(s,v):
    with (ROOT/(P+s)).open('x') as f:
        json.dump(v,f,indent=2); f.write('\n')
def digest(v): return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def baseline():
    af = fp(A+'freeze-v1.json'); a = obj(af['path'])
    assert af['sha256']=='5e9d1e9fe34d7e5041f645700d2315e6a5fce38279be9cd9423ade4c7df8ca5f'
    assert a['whole_obligations']==60 and len(a['artifacts'])==11
    rows=[af]+[check(r) for r in a['artifacts']]
    ab=obj(A+'baseline-v1.json')
    for r in ab['protected']: check(r)
    bindings=[]
    for b in ab['accepted_inputs']:
        auth=b['JSON_authority']['path']; v=obj(auth)
        assert v['status']=='proved, independently reviewed scoped partial result'
        assert not v['repair_required'] and not v['unresolved_substantive_issues']
        body=check(v['accepted_copy']); candidate=check(v['candidate'])
        assert raw(body['path']).endswith(raw(candidate['path']))
        rr=[fp(auth),check(b['MD_authority']),body,candidate]
        rows+=rr
        bindings.append(dict(id=b['id'],authority=rr[0],body=body,candidate=candidate,historical_occurrences_bound_not_replayed=v['record_occurrences_verified'],historical_paths_bound_not_replayed=v['unique_paths_verified']))
    par=fp(PARENT); pv=obj(PARENT)
    assert par['sha256']=='eaaca13b3a0858625c432c88bf86b65ee0e1f2266810b1e696136f8c56cd9bf2'
    assert pv['whole_obligations']==64 and len(pv['artifacts'])==10
    rows+=[par]+[check(r) for r in pv['artifacts']]+[fp('AGENTS.md'),fp('problems/2021-B4/statement.md')]
    unique={}
    for r in rows:
        assert r['path'] not in unique or unique[r['path']]==r
        unique[r['path']]=r
    ordered=[unique[k] for k in sorted(unique)]
    put('baseline-v1.json',dict(captured_at_utc=now(),administrative_only=True,prefix_confirmed_unused_before_first_write=True,constructor_all12_current=True,author_all43_guards_verified_at_capture=True,author_baseline_identity=fp(A+'baseline-v1.json'),author_historical_rows_not_recopied=True,accepted_bindings=bindings,immediate_own_parent=par,own_parent_all10_payloads_preserved=True,occurrences=len(rows),unique_paths=len(ordered),canonical_summary_sha256=digest(ordered),protected_rows=ordered,mutable_living_context_not_future_operative_immutability_guard=True,NO_NEW_corresponding_R2_material_access=True))
    print(json.dumps(dict(baseline=fp(P+'baseline-v1.json'),occurrences=len(rows),paths=len(ordered))))
def inputs():
    b=obj(P+'baseline-v1.json')
    for r in b['protected_rows']: check(r)
    assert digest(b['protected_rows'])==b['canonical_summary_sha256']
    return b
def freeze():
    b=inputs()
    assert re.findall(r'^(\d+)\. PASS',raw(P+'ledger-v1.md').decode(),re.M)==[str(i) for i in range(1,61)]
    stamp=now()
    put('sources-v1.json',dict(recorded_at_utc=stamp,exact_read_limits='source-checks-v1.md',primary_urls=['https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf','https://arxiv.org/pdf/1208.5404'],complete_seven_current_MD_JSON_authorities=True,fresh_operative_bodies='R5C; R8 setting/Euler/all claims/full R8A; R16 setting/full claims; R12B claim; R15C actual proof',whole_external_papers_erratum_or_old_certificates_freshly_audited=False,all12_constructor_files_read=True,no_invented_cache_hash_or_redistributed_paper=True))
    put('input-validation-v1.json',dict(verified_at_utc=stamp,administrative_only=True,all60_once_in_order=True,current_paths=b['unique_paths'],canonical_summary_sha256=b['canonical_summary_sha256'],all_protected_bytes_preserved=True,no_mathematical_program_scan_CAS_test_certificate_or_author_rerun=True))
    put('metadata-v1.json',dict(recorded_at_utc=stamp,reviewer='/root',constructor='/root/review_2017_coarsening_r1',OTHER_NEW_nonconstructor=True,root_generic_assignment_only=True,older_root_R8_and_review_roles_disclosed=True,whole_obligations=60,all60_pass=True,substantive_issues=0,required_repairs=0,closed_scope_notes=7,requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),independent_effective_readback=None,ENTIRE_initial_ALL60_issues_sources_log_code_ALLmetadata_frozen_together=True,NO_NEW_corresponding_R2_finding_content_hash_or_metadata_access=True,other_ENTIRE_R2_and_coordinator_reconciliation_required=True,promotion=False,annual_or_priority_claim=False))
    put('manifest-v1.json',dict(frozen_at_utc=stamp,status='ENTIRE initially blind OTHER WHOLE R17A-D review1',reviewer='/root',constructor='/root/review_2017_coarsening_r1',target=fp(A+'candidate-v1.md'),constructor_freeze=fp(A+'freeze-v1.json'),whole_obligations=60,all60_pass=True,substantive_issues=0,required_repairs=0,closed_scope_notes=7,ENTIRE_initial_ALL60_issues_sources_log_code_ALLmetadata_frozen_together=True,NO_NEW_corresponding_R2_finding_content_hash_or_metadata_access=True,immediate_own_parent=fp(PARENT),current_inputs={k:b[k] for k in ['occurrences','unique_paths','canonical_summary_sha256']},other_ENTIRE_R2_and_coordinator_reconciliation_required=True,promotion=False,artifacts=[fp(P+s) for s in PAYLOAD]))
    verify()
def verify():
    inputs(); v=obj(P+'manifest-v1.json'); assert len(v['artifacts'])==10
    for r in v['artifacts']: check(r)
    print(json.dumps(dict(postverified=True,whole_obligations=60,files_including_manifest=11,manifest=fp(P+'manifest-v1.json'),target=fp(A+'candidate-v1.md'))))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('operation',choices=['baseline','freeze','verify'])
    {'baseline':baseline,'freeze':freeze,'verify':verify}[p.parse_args().operation]()
