"""Administrative-only R5 file integrity; no mathematical evaluation.
Run once with --freeze, then read all output JSON before --verify.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[3]
P='problems/2024-B4/notes/cofactor-Frobenius-r5-'
PARENT='problems/2024-B4/notes/cofactor-dominant-r4-freeze-v1.json'
CONTENT=['candidate-v1.md','obligations-v1.md','sources-v1.md',
         'failures-worklog-v1.md','freeze-v1.py']
META=['baseline-v1.json','metadata-v1.json','input-validation-v1.json']

def stamp(): return datetime.now(timezone.utc).isoformat()
def raw(path): return (ROOT/path).read_bytes()
def obj(path): return json.loads(raw(path))
def rec(path):
    data=raw(path)
    return dict(path=path,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
def check(row):
    assert rec(row['path'])=={k:row[k] for k in ['path','bytes','sha256']},row['path']
def put(suffix,value):
    with (ROOT/(P+suffix)).open('x',encoding='utf-8') as out:
        json.dump(value,out,indent=2,ensure_ascii=False);out.write('\n')
def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def accepted(stem,sha):
    auth='problems/2024-B4/reviews/'+stem+'-acceptance.json'
    value=obj(auth)
    assert value['status']=='proved, independently reviewed scoped partial result'
    assert value['unresolved_substantive_issues']==0 and not value['repair_required']
    check(value['accepted_copy']);check(value['candidate'])
    assert value['accepted_copy']['sha256']==sha
    assert raw(value['accepted_copy']['path']).endswith(raw(value['candidate']['path']))
    return dict(authority=rec(auth),accepted_body=value['accepted_copy'],candidate=value['candidate'],
        historical_occurrences_bound_not_replayed=value['record_occurrences_verified'],
        historical_paths_bound_not_replayed=value['unique_paths_verified'])

def bindings():
    return [accepted('cofactor-global-r2','fd110d1615e730d754063b157cc1906b418702f510b2640bfd1b5c63e898548d'),
            accepted('cofactor-dominant-r4','14c47b6db082bee1d60bcf297c289fe949fdec9384cc8a159b199c56ba265838')]

def freeze():
    existing={str(x.relative_to(ROOT)) for x in (ROOT/'problems/2024-B4/notes').glob('cofactor-Frobenius-r5-*')}
    assert existing=={P+s for s in CONTENT},existing
    labels=re.findall(r'^\| (CF-\d{2}) \|',raw(P+'obligations-v1.md').decode(),re.M)
    assert labels==['CF-'+str(i).zfill(2) for i in range(1,33)]
    parent=obj(PARENT)
    assert (rec(PARENT)['bytes'],rec(PARENT)['sha256'])==(3054,'1d0c4e90c0b75a2417539401d4350e13dd29c9d3030fc06074f4cff18358371b')
    inputs=['AGENTS.md','problems/2024-B4/statement.md',PARENT,
        'problems/2024-B4/notes/cofactor-global-r2-source-audit-v1.md']
    for stem in ['cofactor-global-r2','cofactor-dominant-r4']:
        inputs += ['problems/2024-B4/reviews/'+stem+s for s in
                   ['-acceptance.md','-acceptance.json','-acceptance-integrity.json']]
        value=obj('problems/2024-B4/reviews/'+stem+'-acceptance.json')
        inputs += [value['accepted_copy']['path'],value['candidate']['path']]
    declared=[rec(path) for path in inputs]+parent['artifacts']
    unique={}
    for row in declared:
        check(row)
        assert row['path'] not in unique or unique[row['path']]==row
        unique[row['path']]=row
    guards=[unique[k] for k in sorted(unique)]
    bound=bindings()
    summary=dict(occurrences=len(declared),unique_paths=len(guards),sha256=canonical(guards))
    put('baseline-v1.json',dict(captured_at_utc=stamp(),administrative_only=True,
        prefix_confirmed_unused_before_first_write=True,protected=guards,current_input_summary=summary,
        accepted_operative_bindings=bound,operative_claims=['CG1','CG2','R4A','R4B','R4C'],
        immediate_own_parent=rec(PARENT),parent_ten_payloads_unchanged=True,
        ancestor_inventories_bound_by_immutable_authority_not_recopied_or_replayed=True,
        no_NEW_R5_peer_exists_or_was_accessed=True))
    put('metadata-v1.json',dict(created_at_utc=stamp(),administrative_only=True,
        constructor='/root',constructor_excluded_from_independent_count=True,
        status='candidate proof - unverified',proposed_claims=['R5A','R5B','R5C','R5D'],
        whole_obligations=32,all32_constructor_checks_by_hand=True,
        requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),
        independently_verified_effective_settings=None,
        TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required=True,
        ENTIRE_report_ALL_ledger_sources_logs_code_ALLmetadata_before_peer_access=True,
        no_NEW_R5_peer_construction_contribution_or_material_access=True,
        no_mathematical_program_CAS_scan_optimizer_certificate_or_author_source_rerun=True,
        no_old_frozen_bytes_changed=True,no_paper_download_redistribution_charge_contact_or_bypass=True,
        prime_s_ge5_and_k_ge2_only=True,no_general_k2_annual_or_novelty_claim=True,
        latest_direct_weekly_telemetry=dict(observed_at_utc='2026-10-18 10:05:59 UTC',
            total_used_percent=24,window_minutes=10080,reset_unix=1792874445,
            ordinary_usage_allowed=True,legacy_by_limit_agree=True,
            ceiling_TOTAL_percent=90,integration_reserve=True,
            human_authorized_current_window_ONLY=True,automatic_later_window_spending=False)))
    for row in guards:check(row)
    put('input-validation-v1.json',dict(checked_at_utc=stamp(),administrative_only=True,
        all_current_guard_bytes_exact=True,current_input_summary=summary,
        both_accepted_body_suffixes_exact=True,all32_obligation_labels_once_in_order=True,
        no_mathematical_validation_by_script=True,errors=[]))
    put('freeze-v1.json',dict(frozen_at_utc=stamp(),status='ENTIRE author R5A-D candidate unverified',
        constructor='/root',constructor_excluded=True,whole_obligations=32,
        TWO_OTHER_ENTIRE_initially_blind_whole_audits_required=True,
        all_content_and_metadata_frozen_before_any_NEW_R5_peer_material_exists=True,
        current_input_summary=summary,accepted_operative_bindings=bound,
        immediate_own_parent=rec(PARENT),files_including_freeze=9,
        artifacts=[rec(P+s) for s in CONTENT+META]))
    verify()

def verify():
    value=obj(P+'freeze-v1.json');base=obj(P+'baseline-v1.json')
    assert len(value['artifacts'])==8
    for row in value['artifacts']+base['protected']:check(row)
    assert canonical(base['protected'])==base['current_input_summary']['sha256']
    assert bindings()==value['accepted_operative_bindings']
    print(json.dumps(dict(postverified=True,administrative_only=True,whole_obligations=32,
        main=rec(P+'candidate-v1.md'),freeze=rec(P+'freeze-v1.json'),
        current_input_summary=base['current_input_summary'],files_including_freeze=9),indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--freeze',action='store_true');group.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    freeze() if args.freeze else verify()
