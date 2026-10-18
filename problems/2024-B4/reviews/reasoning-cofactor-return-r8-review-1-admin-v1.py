"""Exclusive new review metadata administration; no mathematical program."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import sys

ROOT=Path(__file__).resolve().parents[3]
P='problems/2024-B4/reviews/reasoning-cofactor-return-r8-review-1-'
A='problems/2024-B4/notes/reasoning-cofactor-return-r8-'
THESIS='.cache/literature/deep-literature-r2/2024-mcguire-thesis-1995'
STATIC=['report-v1.md','ledger-v1.md','issues-v1.md','sources-v1.md','worklog-v1.md','admin-v1.py']
GENERATED=['sources-v1.json','baseline-v1.json','input-validation-v1.json','metadata-v1.json']
PARENT='problems/2019-B4/reviews/reasoning-cut-transfer-r6-review-1-manifest-v1.json'

def now():
    return datetime.now(timezone.utc).isoformat()

def permitted(path):
    assert not Path(path).is_absolute() and '..' not in Path(path).parts
    assert not path.startswith('problems/2024-B4/reviews/reasoning-cofactor-return-r8-review-2-')
    return ROOT/path

def fp(path):
    data=permitted(path).read_bytes()
    return dict(path=path,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())

def obj(path):
    return json.loads(permitted(path).read_text())

def match(row):
    assert fp(row['path'])=={k:row[k] for k in ['path','bytes','sha256']},row['path']

def put(suffix,value):
    with permitted(P+suffix).open('x') as stream:
        json.dump(value,stream,ensure_ascii=False,indent=2)
        stream.write('\n')

def snapshot():
    author=obj(A+'freeze-v1.json')
    assert fp(A+'candidate-v1.md')==dict(path=A+'candidate-v1.md',bytes=15501,sha256='044343181cc87099291f327728fc07cbd1d4e97c59558fcb88b3237f6511eaea')
    assert fp(A+'freeze-v1.json')==dict(path=A+'freeze-v1.json',bytes=3554,sha256='05075573ae2f40c214473d309de4c9490dbe0c404e60c8f1ddde5b9e2d79dbe3')
    assert len(author['artifacts'])==12
    records=[fp(A+'freeze-v1.json')]
    for row in author['artifacts']:
        match(row)
        records.append(fp(row['path']))
    paths=['AGENTS.md','problems/2024-B4/statement.md',PARENT,
        'problems/2024-B4/proofs/reviewed-structural-v1.1.md',
        'problems/2024-B4/reviews/structural-acceptance.md',
        'problems/2024-B4/reviews/structural-acceptance.json',
        'problems/2024-B4/proofs/reviewed-reasoning-cofactor-return-r6-v1.1.md',
        'problems/2024-B4/reviews/reasoning-cofactor-return-r6-acceptance.md',
        'problems/2024-B4/reviews/reasoning-cofactor-return-r6-acceptance.json',
        THESIS+'.pdf']+[THESIS+f'-{p}.png' for p in range(21,32)]
    records.extend(fp(path) for path in paths)
    for stem,key in [('structural','accepted_proof'),('reasoning-cofactor-return-r6','accepted_copy')]:
        authority=obj('problems/2024-B4/reviews/'+stem+'-acceptance.json')
        match(authority[key])
    assert fp(THESIS+'.pdf')['sha256']=='d8e8e62d873c5ec69e2fd40473a9aee257bb8d4994cb5ffc1a42cb70f8bcbd24'
    labels=re.findall(r'(?m)^\| R8-(\d{2}) \|',permitted(P+'ledger-v1.md').read_text())
    assert labels==[f'{i:02d}' for i in range(1,49)]
    author_labels=re.findall(r'(?m)^\| R8-(\d{2}) \|',permitted(A+'obligations-v1.md').read_text())
    assert labels==author_labels
    unique={row['path']:row for row in records}
    ordered=[unique[path] for path in sorted(unique)]
    return dict(fingerprints=ordered,record_occurrences=len(records),unique_paths=len(ordered),
        all13_author_files_bound=True,all48_separate_labels=True,
        immutable_immediate_own_parent_only_no_recursive_expansion=fp(PARENT),
        existing_thesis_binary_and_ALL11_visual_pages_bound=True,
        mathematical_assertions_evaluated=False)

def prepare():
    state=snapshot()
    for suffix in STATIC:
        fp(P+suffix)
    put('sources-v1.json',dict(date_utc='2026-10-18',reviewer='/root',
        all13_author_files_FULL_model_read=True,all48_hand_reconstructed=True,
        fresh_COMPLETE_bodies_and_current_authorities=['T1--T4;only T1 operative','general R6;R6B/C operative'],
        older_own_roles='CG/R4/R5 constructor and older reviews; separately accepted inputs not freshly independently recertified',
        no_NEW_corresponding_peer_material_access=True,
        primary_sources=[
            dict(url='https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf',read_scope='B4 setup/(b),57--75;no preliminary proof',binary_sha256=None),
            dict(url='https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf',record='https://thesis.caltech.edu/4053/',doi='10.7907/1CZ2-6S05',read_scope='ALL existing11 PNG21--31/printed16--26 visually read;complete operative Theorems6/7 supplied proofs and local lemmas',existing_local_binary=fp(THESIS+'.pdf'),existing_images=[fp(THESIS+f'-{p}.png') for p in range(21,32)]),
            dict(url='https://math.stanford.edu/~conrad/145Page/handouts/algcurves.pdf',read_scope='ENTIRE3.3 properties1--7/Theorem3/proof2419--2624;returned8/9to2673;ENTIRE5.3 Bezout statement/proof3829--3924',clipped_first_return_recovered=True,not_freshly_read='AppendixA/all129pages',binary_sha256=None)],
        unread_NOT_imported=['joint journal1995 PDF','JW1993 full proof','Ferard2017 operative body'],
        no_NEW_download_cache_mutation_charge_contact_bypass=True,no_mathematical_program_CAS_scan_or_old_replay=True))
    put('baseline-v1.json',dict(at_utc=now(),**state))
    put('input-validation-v1.json',dict(at_utc=now(),result='PASS',all13_author_files_bound=True,all48_separate_labels=True,record_occurrences=state['record_occurrences'],unique_paths=state['unique_paths'],administration_only=True))
    put('metadata-v1.json',dict(at_utc=now(),status='initial entire OTHER WHOLE1;findings embargoed',reviewer='/root',constructor_C_excluded=True,whole_obligations=48,ENTIRE_files=11,
        no_NEW_corresponding_peer_finding_file_hash_metadata_access=True,FULL_final_ALL11_model_readback_then_SEPARATE_verify_required=True,
        requested_inherited=dict(model='gpt-6.1-sol',reasoning='max'),independent_effective_readback=None,
        weekly_reset_only=1792874445,TOTAL_ceiling=90,integration_reserve=True,no_mathematical_program_or_old_replay=True))
    print(json.dumps(dict(prepare='PASS',author_files=13,whole_obligations=48,record_occurrences=state['record_occurrences'],unique_paths=state['unique_paths'])))

def validate():
    old=obj(P+'baseline-v1.json')
    state=snapshot()
    assert all(old[key]==value for key,value in state.items())
    return state

def freeze():
    state=validate()
    put('manifest-v1.json',dict(frozen_at_utc=now(),status='ENTIRE initially blind WHOLE1;finding embargoed',whole_obligations=48,ENTIRE_files_including_manifest=11,
        all_report_ALL48_issues_sources_worklog_code_ALLmetadata=True,FULL_final_ALL_payload_model_readback_completed=True,
        FULL_manifest_model_readback_then_SEPARATE_verify_required=True,no_NEW_corresponding_peer_finding_file_hash_metadata_access=True,
        explicit_BOTH_required_before_peer_access_or_release=True,record_occurrences=state['record_occurrences'],unique_paths=state['unique_paths'],payloads=[fp(P+suffix) for suffix in STATIC+GENERATED]))
    print(json.dumps(dict(freeze=fp(P+'manifest-v1.json'))))

def verify():
    state=validate()
    manifest=obj(P+'manifest-v1.json')
    assert len(manifest['payloads'])==10 and manifest['whole_obligations']==48
    for row in manifest['payloads']:
        match(row)
    print(json.dumps(dict(SEPARATE_readonly_verify='PASS',at_utc=now(),ENTIRE_files=11,whole_obligations=48,record_occurrences=state['record_occurrences'],unique_paths=state['unique_paths'],manifest=fp(P+'manifest-v1.json'),report=fp(P+'report-v1.md')),indent=2))

if __name__=='__main__':
    mode=sys.argv[1] if len(sys.argv)==2 else ''
    assert mode in ['prepare','freeze','verify']
    dict(prepare=prepare,freeze=freeze,verify=verify)[mode]()
