#!/usr/bin/env python3
"""Create exclusive author metadata; all mathematics is hand-derived in Markdown."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
import re

ROOT=Path.cwd().resolve()
P='problems/2017-B4/notes/coordinator-weighted-cutpath-r1-'
NOW=datetime.now(timezone.utc).isoformat()
assert ROOT.name=='Website'

def rec(path):
    assert not path.startswith('problems/2017-B4/reviews/coordinator-weighted-cutpath-r1-')
    assert not path.startswith('problems/2024-B4/reviews/cofactor-global-r2-')
    assert not path.startswith('problems/2022-B4/reviews/reasoning-seed-return-r1-review-2-')
    raw=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(raw),sha256=sha256(raw).hexdigest())

def check(row):
    actual=rec(row['path'])
    assert actual=={k:row[k]for k in('path','bytes','sha256')},row['path']
    return actual

def read(path):
    rec(path)
    return json.loads((ROOT/path).read_text())

def out(suffix,obj):
    with(ROOT/(P+suffix)).open('x')as f:
        json.dump(obj,f,indent=2)
        f.write('\n')

protected=[]
roles=[]
for path,role in [
    ('AGENTS.md','current protocol'),
    ('problems/2017-B4/statement.md','official normalized statement'),
    ('problems/2017-B4/reviews/concavity-acceptance.json','old accepted scope/context authority'),
    ('problems/2017-B4/proofs/reviewed-concavity-v1.1.md','old complete proof freshly read as context'),
    ('problems/2017-B4/notes/coordinator-mass-upper-r1-worklog-v1.md','earlier unresolved upper-mass quantifier audit')
]:
    protected.append(rec(path));roles.append(dict(path=path,role=role))
a=read('problems/2017-B4/reviews/concavity-acceptance.json')
assert a['unresolved_substantive_objections']==0
assert a['substantive_author_repair_required'] is False
check(a['accepted_proof'])

parent=check(dict(path='problems/2022-B4/reviews/reasoning-seed-return-r1-review-1-manifest-v1.json',
    bytes=3076,sha256='fb74fbfc26e944a8a0a35812b8aa294d3f41c1e9d28a75b16e56a63315a27b78'))
protected.append(parent)
pm=read(parent['path'])
for row in pm['artifacts']:
    check(row)
    if row['path'].endswith(('metadata-v1.json','input-validation-v1.json')):
        protected.append(rec(row['path']))

labels=re.findall(r'^\|WC-O(\d{2})\|',(ROOT/(P+'obligations-v1.md')).read_text(),re.M)
assert labels==[f'{i:02}'for i in range(1,41)]
assert 'candidate proof - unverified' in(ROOT/(P+'candidate-v1.md')).read_text().lower()
assert 'Cauchy--Schwarz' in(ROOT/(P+'candidate-v1.md')).read_text()
assert '544375' in(ROOT/(P+'candidate-v1.md')).read_text()
# These are document/identity checks ONLY. No rational, log or graph calculation.
sources=[
    dict(author='Justin Dallant',version='arXiv2502.20909v2',
         url='https://arxiv.org/pdf/2502.20909v2',
         imported='actual cutpath graph/rotation correspondence/weakened zone inequality; insertion interface',
         read_limit='definitions, complete operative Section2 through Lemma7, insertion and final upper transfer; no LP/certificate rerun'),
    dict(authors='Stefan Felsner and Pavel Valtr',
         url='https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf',
         imported='marked fixed-polygon dictionary and canonical deletion/insertion',
         read_limit='Section1 convention/dictionary and insertion passage; no fresh full equivalence foundation proof'),
    dict(author='Simon Marais Mathematics Competition',
         url='https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf',
         read_limit='page2 B4 official domain only'),
    dict(author='Simon Marais Mathematics Competition',
         url='https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf',
         read_limit='page12 B4 intended count/dictionary only'),
    dict(authors='Widom/Destainville/Mosseri/Bailly',
         url='https://euler.phys.cmu.edu/widom/pubs/PDF/jsp120_2005_p837.pdf',
         imported=False,read_limit='introduction/relevant Section3 and AppendixA opening/A1 portions/B, not full37 pages; heuristic/variational context only'),
    dict(author='Rom Pinchasi',url='https://www2.math.technion.ac.il/~room/ps_files/zonespl.pdf',
         imported='only through attributed Dallant statement',
         read_limit='original manuscript body unread: public web retrieval failed')
]
out('sources-v1.json',dict(recorded_at_utc=NOW,status='candidate proof - unverified',
    primary_records=sources,full_read_limits_companion=P+'source-audit-v1.md',
    no_NEW_cached_PDF_download_or_hash=True,no_novelty_or_setter_claim=True,
    mathematics_is_new_root_hand_path_argument_not_old_certificate=True))
out('baseline-v1.json',dict(captured_at_utc=NOW,administrative_integrity_only=True,
    protected_direct_records=protected,roles=roles,compact_own_parent=parent,
    own_parent_all_artifacts_checked=len(pm['artifacts']),
    historical_inventories_bound_not_copied_or_recursively_replayed=True,
    no_NEW_peer_weighted_CG_or_seed_R2_material_opened=True))
out('metadata-v1.json',dict(recorded_at_utc=NOW,status='candidate proof - unverified',
    constructor='/root',sole_new_constructor=True,root_excluded_from_both_reviews=True,
    whole_obligations=40,all40_hand_dispositions_present=True,
    conclusions=['WC1 direct K^n cutpath bound','WC2 strict log2K<162/125','WC3 official limsup<81/125'],
    no_math_program_CAS_scan_sample_optimization_certificate_or_source_rerun=True,
    no_fullannual_exactvalue_upper_R_effective_modulus_or_priority_claim=True,
    requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),
    independently_verified_effective_settings=None,
    telemetry=dict(observed_at_utc='2026-10-18T08:47:57+00:00',weekly_used_percent_TOTAL=19,
        reset_unix=1792874445,window_minutes=10080,ordinary_usage_allowed=True,
        authorized_ceiling_percent_TOTAL=90,integration_reserve=True,no_automatic_later_reset=True),
    no_NEW_corresponding_peer_files_findings_hashes_or_metadata_opened=True,
    TWO_OTHER_ENTIRE_initially_blind_WHOLE_audits_required=True,promotion=False))
out('input-validation-v1.json',dict(validated_at_utc=NOW,
    administrative_only_not_mathematics=True,protected_records_checked=len(protected),
    exact40_obligation_labels=True,old_concavity_authority_and_copy_exact=True,
    own_parent_manifest_and_all_artifacts_exact=True,
    no_mathematical_certificate_executed=True,errors=[]))
suffixes=['candidate-v1.md','obligations-v1.md','failures-worklog-v1.md',
          'source-audit-v1.md','freeze-v1.py','sources-v1.json',
          'baseline-v1.json','metadata-v1.json','input-validation-v1.json']
artifacts=[rec(P+s)for s in suffixes]
out('freeze-v1.json',dict(frozen_at_utc=NOW,status='candidate proof - unverified',
    constructor='/root',sole_new_constructor=True,constructor_excluded=True,
    scope='2017 B4 only; WC1-WC3 actual marked cutpaths and official limsup<0.648',
    whole_obligations=40,ENTIRE_main_all40_hand_checks_failures_sources_log_code_ALL_metadata_frozen=True,
    TWO_OTHER_ENTIRE_initially_blind_WHOLE_audits_and_reconciliation_required=True,
    no_math_program_or_mathematical_certificate_run=True,
    compact_own_parent=parent,artifacts=artifacts,author_promotion=False))
for row in read(P+'freeze-v1.json')['artifacts']:
    check(row)
print(json.dumps(dict(main=rec(P+'candidate-v1.md'),freeze=rec(P+'freeze-v1.json'),
    whole_obligations=40,new_packet_paths=10,mathematics_computed=False),indent=2))
