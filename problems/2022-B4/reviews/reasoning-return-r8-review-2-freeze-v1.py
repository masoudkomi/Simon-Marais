"""ADMINISTRATIVE initially blind R8R2 freeze: bytes/SHA/JSON only.

No mathematical computation, source certificate replay or author rerun.
Writes exclusively this assigned reviewer prefix. Refuses all NEW peer
R8 material and the queued sector3 packet before this whole freeze.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys


ROOT = Path('/Users/uqmkamga/Documents/ChatGPT/Website')
PREFIX = 'problems/2022-B4/reviews/reasoning-return-r8-review-2-'
AUTHOR = 'problems/2022-B4/notes/reasoning-return-r8-'
OWN_PARENT = 'problems/2021-B4/notes/reasoning-return-r10-'
HEX64 = re.compile('^[0-9a-f]{64}$')

KNOWN = [
    ('AGENTS.md', 4707,
     '28f743b6925d72b9d1a5bccff0239a897a7a46750ec623e99f43d5cea5e1baff'),
    (AUTHOR+'candidate-v1.md', 16851,
     '5e455e606a589f4a6e5d5086a57564099ccc23f17d3832cc1c355c0c33c532b9'),
    (AUTHOR+'freeze-v1.json', 3609,
     'd0c587428aa42027a22e2ea954f79a4c51596883658d0917038fafdd08152242'),
    ('problems/2022-B4/statement.md', 1195,
     '2011761509ac42d5ffa2ab9e86dd1db464618707443a68f43fb3e45f59ed36c0'),
    ('problems/2022-B4/proofs/reviewed-reasoning-return-r5-v1.1.md', 30324,
     '1a2544cb8ced3bba9cc6efed1870c242c652b3e6029f39881028d4637d7c6da6'),
    ('problems/2022-B4/proofs/reviewed-reasoning-return-r6-v1.1.md', 18580,
     '696cfaf139c3ce1cfccc17ca1643e378a4ad70bedd91374f24a82b4fe95daf8d'),
    ('problems/2022-B4/proofs/reviewed-reasoning-return-r7-v1.1.md', 23574,
     '739a88f2a5b4e3cdd13681094f420def99259c0d52b63aef3b394a407c29a342'),
    (OWN_PARENT+'freeze-v1.json', 3884,
     'ff20fd17e080ce3fb5d3c0f4f3f7c1f58624741b0fadc1be4a0fee26fc73f2bd'),
]
METADATA = [
    AUTHOR+'freeze-v1.json', AUTHOR+'sources-v1.json',
    AUTHOR+'input-validation-v1.json',
    *[f'problems/2022-B4/reviews/reasoning-return-r{n}-acceptance{s}.json'
      for n in [5,6,7] for s in ['', '-integrity']],
    OWN_PARENT+'freeze-v1.json', OWN_PARENT+'input-validation-v1.json',
]
DIRECT_SCOPES = [
    'AGENTS.md', 'problems/2022-B4/statement.md',
    *[f'problems/2022-B4/proofs/reviewed-reasoning-return-r{n}-v1.1.md'
      for n in [5,6,7]],
    *[f'problems/2022-B4/reviews/reasoning-return-r{n}-acceptance.md'
      for n in [5,6,7]],
]


def now():
    return datetime.now(timezone.utc).isoformat()


def safe(path):
    if path.startswith('problems/2022-B4/reviews/reasoning-return-r8-'):
        assert path.startswith(PREFIX), 'Blindness guard: no NEW peerR8 file'
    assert 'reasoning-sector3-return-r1-' not in path, 'Queued packet not yet opened'
    result = Path(path) if Path(path).is_absolute() else ROOT/path
    return result


def fingerprint(path):
    data = safe(path).read_bytes()
    return {'path':path, 'bytes':len(data),
            'sha256':hashlib.sha256(data).hexdigest()}


def write(suffix, data):
    path=ROOT/(PREFIX+suffix)
    assert str(path).startswith(str(ROOT/PREFIX))
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')


def declared(data):
    if isinstance(data,dict):
        p,h=data.get('path'),data.get('sha256')
        if isinstance(p,str) and isinstance(h,str) and HEX64.fullmatch(h):
            yield {'path':p,'sha256':h,
                   **({'bytes':data['bytes']} if isinstance(data.get('bytes'),int) else {})}
        for v in data.values():
            yield from declared(v)
    elif isinstance(data,list):
        for v in data:
            yield from declared(v)


def validate():
    cache={}
    occurrences=[]
    def actual(path):
        if path not in cache:
            cache[path]=fingerprint(path)
        return cache[path]
    def check(row,origin):
        found=actual(row['path'])
        assert found['sha256']==row['sha256'],(origin,row,found)
        assert 'bytes' not in row or found['bytes']==row['bytes'],(origin,row,found)
        occurrences.append((origin,found))
        return found
    anchors=[check({'path':p,'bytes':n,'sha256':h},'exact supplied immutable anchor')
             for p,n,h in KNOWN]
    parents=[]
    for path in METADATA:
        binding=actual(path)
        rows=list(declared(json.loads(safe(path).read_text())))
        for row in rows:
            check(row,path)
        parents.append({'metadata':binding,
                        'declared_fingerprint_occurrences_verified':len(rows)})
    direct=[actual(p) for p in DIRECT_SCOPES]
    # Match exact accepted-copy suffixes administratively, not by asserting
    # a new independent audit of their already accepted mathematics.
    for n in [5,6,7]:
        p=f'problems/2022-B4/reviews/reasoning-return-r{n}-acceptance.json'
        doc=json.loads(safe(p).read_text())
        assert safe(doc['accepted_copy']['path']).read_bytes().endswith(
            safe(doc['candidate']['path']).read_bytes())
    records=[cache[p] for p in sorted(cache)]
    encoded=json.dumps(records,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
    obs=safe(AUTHOR+'obligations-v1.md').read_text()
    assert re.findall(r'^\|R8-(\d\d)\|',obs,re.M)==[f'{n:02}' for n in range(1,33)]
    ledger=safe(PREFIX+'issues-v1.md').read_text()
    assert re.findall(r'^\|R8R2-(\d\d)\|',ledger,re.M)==[f'{n:02}' for n in range(1,43)]
    return {
        'verified_at_utc':now(), 'administrative_only':True, 'all_verified':True,
        'exact_target_accepted_input_and_own_predecessor_anchors':anchors,
        'complete_accepted_math_and_scope_bindings':direct,
        'compact_immutable_parent_metadata':parents,
        'declared_fingerprint_occurrences_verified':len(occurrences),
        'unique_paths_fingerprinted':len(cache),
        'canonical_deduplicated_summary_sha256':hashlib.sha256(encoded).hexdigest(),
        'canonical_encoding':'UTF8 JSON sorted path/bytes/sha256 records,ensure_ascii=false,sort_keys=true,separators comma/colon',
        'historical_inventories_bound_not_duplicated':True,
        'exact_rows_reproducible_from_immutable_parents':True,
        'all8_constructor_payloads_and_3_accepted_suffixes_match':True,
        'all_author_obligations':32,'whole_inference_checks':42,
        'no_NEW_peer_R8_file_or_finding_opened_before_ENTIRE_freeze':True,
        'no_queued_sector3_packet_opened':True,
        'no_mathematical_program_CAS_scan_author_rerun_or_certificate':True,
        'all_old_bytes_read_only_and_own2021R10_still_frozen':True,
    }


def sources(validation):
    return {
        'recorded_at_utc':now(),
        'status':'COMPLETE initially blind NONCONSTRUCTOR WHOLE R2; source checks not promotion',
        'primary_sources':[
            {'url':'https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf',
             'scope':'actual B4 hypothesis and(b), no preliminary proof'},
            {'url':'https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf',
             'scope':'modified-division/weights/alphabet and finite uniqueness pp6-7; Lemma29 INTEGER hypotheses and statement; complete Prop37/Cor38 and displayed proofs pp21-22,not all30pages'},
            {'url':'https://arxiv.org/html/2510.11723v2',
             'scope':'representation/minimal-word definitions; Section3.3 conjecture3.9,Prop3.10/proof,Remark3.11,Question3.12,Prop3.13/proof; no numerical/normality premise'},
            {'url':'https://www.researchgate.net/publication/220576840_Lower_bounds_for_Z-numbers',
             'scope':'original introduction properS and actual map1.1; COMPLETE Lemma3.1/Props3.1-3.2/proofs,not search algorithms'},
            {'url':'https://arxiv.org/pdf/math/0209247',
             'scope':'binary real-series definition and actual Theorems1.2/1.4 statements pp1-3; no complete ergodic proof imported'},
        ],
        'fresh_native_PDF_byte_hashes':None,
        'actual_access':'public browser open/find,about2seconds each,no native retrieval/cache write',
        'complete_accepted_input_bodies_and_scopes':validation['complete_accepted_math_and_scope_bindings'],
        'complete_constructor_packet_main_all32obligations_all8payloads_read':True,
        'prior_roles':'old R6 constructor,older complexity/R3/R4/F5/R7 whole reviewer; no NEW R8 construction contribution,no self-recertification',
        'new_scope_advisory':'N1: positive multiplier1<=c<=q only;c0 gives canonical zero,not a positive-value interface',
        'no_unproved_ordinary_predecessor_no_tenfold_normality_or_annual_import':True,
        'all_new_peer_R8_material_unread_until_COMPLETE_initial_freeze':True,
        'no_math_code_CAS_scans_author_rerun_paid_access_contact_bypass':True,
    }


def main():
    assert sys.argv[1:] in [['--prepare'],['--freeze']]
    final=ROOT/(PREFIX+'manifest-v1.json')
    assert not final.exists(),'Immutable whole initial already frozen'
    v=validate()
    write('input-validation-v1.json',v)
    write('sources-v1.json',sources(v))
    brief={'at_utc':now(),'all_inputs_match':True,'administrative_only':True,
           'whole_checks':42,'all_author_obligations':32,
           'substantive_open_issues':0,'scope_advisories':1,
           'required_author_mathematical_repair_for_exact_positive_scaling_scope':False,
           'declared_fingerprint_occurrences_verified':v['declared_fingerprint_occurrences_verified'],
           'unique_paths_fingerprinted':v['unique_paths_fingerprinted'],
           'new_whole_report':fingerprint(PREFIX+'initial-v1.md')}
    if sys.argv[1]=='--prepare':
        print(json.dumps(brief,indent=2));return
    write('freeze-output-v1.json',brief)
    suffixes=['initial-v1.md','issues-v1.md','source-checks-v1.md','worklog-v1.md',
              'freeze-v1.py','input-validation-v1.json','sources-v1.json','freeze-output-v1.json']
    manifest={
        'frozen_at_utc':now(),
        'status':'COMPLETE initially blind NONCONSTRUCTOR WHOLE R2 initial; recommendation only',
        'reviewer':'/root/review_2021_reasoning_j15_r2',
        'constructor':'/root/review_2017_coarsening_r1',
        'requested_settings':{'model':'gpt-6.1-sol','reasoning':'max'},
        'independently_verified_effective_settings':None,
        'whole_checks':42,'all_author_obligations':32,
        'recommendation':'No substantive defect in R8A-C or R8D for positive integer scaling1<=c<=q; retain N1 zero-scaling exclusion in accepted scope',
        'substantive_open_issues':0,'advisories':['N1 explicit positive multiplier,zero maps to canonical zero'],
        'required_author_mathematical_repair_for_exact_qualified_scope':False,
        'complete_initial_before_ANY_new_peer_R8_report_ledger_source_manifest_or_finding':True,
        'old_R6_authorship_and_other_reviews_disclosed_no_NEW_R8_construction_role':True,
        'no_ordinary_survivor_termination_no_tenfold_full_controller_annual_or_novelty_claim':True,
        'no_math_program_CAS_scan_author_rerun_or_certificate':True,
        'no_old_shared_cache_Git_edits_spawn_contact_charge_bypass':True,
        'compact_input_summary':{
            'declared_fingerprint_occurrences_verified':v['declared_fingerprint_occurrences_verified'],
            'unique_paths_fingerprinted':v['unique_paths_fingerprinted'],
            'canonical_deduplicated_summary_sha256':v['canonical_deduplicated_summary_sha256'],
            'historical_inventories_bound_not_duplicated':True},
        'authoritative_account_weekly':{
            'at_utc':'2026-10-17 19:36:52 UTC','total_used_percent':60,
            'window_minutes':10080,'reset_unix':1792745187,
            'ordinary_usage_allowed':True,'total_ceiling_percent':90,'integration_reserve':True},
        'administrative_command':'.venv/bin/python '+PREFIX+'freeze-v1.py --freeze',
        'artifacts':[fingerprint(PREFIX+s) for s in suffixes],
    }
    write('manifest-v1.json',manifest)
    print(json.dumps({'manifest':fingerprint(PREFIX+'manifest-v1.json'),**brief},indent=2))


if __name__=='__main__':
    main()
