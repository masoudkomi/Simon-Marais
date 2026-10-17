"""Administrative constructor freeze only; no mathematical computation.

Verify declared immutable inputs, bind their metadata, and refuse overwrite.
No historical inventory is copied into a new exponentially growing inventory.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re

ROOT=Path(__file__).resolve().parents[3]
PREFIX='problems/2024-B4/notes/coordinator-component-saturation-r1-'

def rec(path):
    b=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def new(suffix,value):
    with (ROOT/(PREFIX+suffix)).open('x') as f:
        json.dump(value,f,indent=2);f.write('\n')

def rows(x):
    if isinstance(x,dict):
        if isinstance(x.get('path'),str) and re.fullmatch('[0-9a-f]{64}',str(x.get('sha256',''))):
            yield x
        for k,v in x.items():
            if '/' in k and isinstance(v,str) and re.fullmatch('[0-9a-f]{64}',v):
                yield dict(path=k,sha256=v)
            yield from rows(v)
    elif isinstance(x,list):
        for v in x:yield from rows(v)

generated=['sources-v1.json','input-validation-v1.json','freeze-output-v1.json','freeze-v1.json']
assert all(not (ROOT/(PREFIX+s)).exists() for s in generated)
ob=(ROOT/(PREFIX+'obligations-v1.md')).read_text()
ids=re.findall(r'^\|CS-(\d\d)\|',ob,re.M)
assert ids==[f'{i:02}' for i in range(1,31)]
metadata=[
 'problems/2024-B4/reviews/reasoning-components-r1-acceptance.json',
 'problems/2024-B4/reviews/reasoning-components-r1-acceptance-integrity.json',
 'problems/2024-B4/notes/reasoning-components-r1-input-validation-v1.json',
 'problems/2024-B4/notes/reasoning-components-r1-authority-hash-only-addendum-v1.json',
 'problems/2024-B4/reviews/Kasami-whole-criterion-acceptance.json',
 'problems/2024-B4/reviews/generalized-Kasami-acceptance.json',
]
cache={}; summaries=[]
for name in metadata:
    n=0
    for expected in rows(json.loads((ROOT/name).read_text())):
        path=expected['path']
        if path not in cache:cache[path]=rec(path)
        assert cache[path]['sha256']==expected['sha256'],(name,path)
        if 'bytes' in expected:assert cache[path]['bytes']==expected['bytes'],(name,path)
        n+=1
    summaries.append(dict(metadata=rec(name),declared_record_occurrences_verified=n))
now=datetime.now(timezone.utc).isoformat()
direct=[rec(p)for p in [
 'AGENTS.md','problems/2024-B4/statement.md',
 'problems/2024-B4/proofs/reviewed-Kasami-whole-criterion-v1.1.md',
 'problems/2024-B4/proofs/reviewed-generalized-Kasami-v1.1.md',
 'problems/2024-B4/proofs/reviewed-reasoning-components-r1-v1.1.md',
 'problems/2024-B4/notes/coordinator-ferard-retrieval-followup-v1.md',
 '.cache/literature/deep-literature-r2/2024-mcguire-thesis-1995-40.png',
]]
new('sources-v1.json',dict(recorded_at_utc=now,status='candidate proof - unverified',
 actual_primary_reads=[
  dict(name='Bensimhoun2004 Lueroth proof',url='https://upload.wikimedia.org/wikipedia/commons/3/3e/Another_elementary_proof_of_Luroth%27s_theorem-06.2004.pdf',read='COMPLETE theorem and BOTH pages of written proof',role='Classical foundational Lueroth theorem, arbitrary characteristic; polynomial/common-pair applications supplied in new main',native_binary_download_or_hash_claim=False),
  dict(name='Mesnager--Qu1907.01066v1',url='https://arxiv.org/pdf/1907.01066v1',read='Actual Section5.4 Definition44, following parameter paragraph and Proposition45/attribution',role='Classical trace-form attribution only, no permutation/exceptionality/monodromy import',full28page_audit=False,native_binary_download_or_hash_claim=False),
 ],direct_input_identities=direct,
 source_limits='Original JW1993 proof and exact Ferard2014 theorem unread; prior scanned CN232 article printed2019 has missing103/112, no later source claim imported',
 novelty_or_priority_established=False,third_party_paper_or_image_redistributed=False))
new('input-validation-v1.json',dict(checked_at_utc=now,administrative_only=True,
 all_verified=True,record_occurrences=sum(x['declared_record_occurrences_verified']for x in summaries),
 unique_paths=len(cache),immutable_metadata=summaries,direct_inputs=direct,
 compact_binding_instead_of_recopying_entire_historical_inventory=True,
 exact_records_remain_reproducible_in_immutable_referenced_inputs=True,
 whole_obligation_ids=ids,root_new_constructor_excluded_from_independent_review_count=True,
 mathematical_program_CAS_scan_or_source_certificate_rerun=False,
 new_year_or_full_annual_classification_or_novelty_claim=False))
artifacts=[rec(PREFIX+s) for s in ['candidate-v1.md','obligations-v1.md','source-audit-v1.md','failed-routes-v1.md','worklog-v1.md','freeze-v1.py','sources-v1.json','input-validation-v1.json']]
output=dict(frozen_at_utc=now,status='COMPLETE constructor checkpoint; candidate proof - unverified',main=artifacts[0],whole_obligations=30,record_occurrences=sum(x['declared_record_occurrences_verified']for x in summaries),unique_paths=len(cache),new_math_computation=False,two_OTHER_fresh_initially_blind_NONCONSTRUCTOR_WHOLE_audits_required=True)
new('freeze-output-v1.json',output)
artifacts.append(rec(PREFIX+'freeze-output-v1.json'))
new('freeze-v1.json',dict(frozen_at_utc=now,status='candidate proof - unverified',constructor='coordinator root',
 claims=['CS1 every-k common absolute component forces whole base Kasami divisor','CS2 exact common-component gcd and individual occurrence iff via accepted KC'],
 requested_settings=dict(model='gpt-6.1-sol',reasoning='max'),independently_verified_effective_settings=None,
 whole_obligations=30,two_OTHER_fresh_initially_blind_NONCONSTRUCTOR_WHOLE_audits_required=True,
 root_old_KC_GK_constructor_and_IC_review_roles_disclosed=True,
 new_external_classical_Lueroth_input_explicit=True,
 J_original_proof_monodromy_APN_transversality_Ferard_or_odd_k_exceptionality_import=False,
 exact_trace_identity_and_all_k_multiplicity_indecomposability_proved_in_main=True,
 common_pair_chart_transcendence_distinctness_field_and_globalization_obligations_explicit=True,
 q16_proper_block_exclusion_is_NEW_CANDIDATE_not_old_status_change=True,
 full_annual_classification_or_novelty_claim=False,
 mathematical_program_CAS_scan_or_author_rerun=False,
 latest_authoritative_account_weekly=dict(at_utc='2026-10-17 18:09:31UTC',total_used_percent=53,window_minutes=10080,reset_unix=1792745187,total_ceiling_percent=90,review_integration_reserve=True),
 administrative_command='.venv/bin/python '+PREFIX+'freeze-v1.py',artifacts=artifacts))
print(json.dumps(dict(output=output,manifest=rec(PREFIX+'freeze-v1.json')),indent=2))
