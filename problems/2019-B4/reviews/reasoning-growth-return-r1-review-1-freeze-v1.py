"""Administrative-only immutable ENTIRE whole review freeze, no math evaluation."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

ROOT=Path(__file__).resolve().parents[3]
P='problems/2019-B4/reviews/reasoning-growth-return-r1-review-1-'
T='problems/2019-B4/notes/reasoning-growth-return-r1-'
PARENT='problems/2024-B4/notes/coordinator-F8-pencil-r1-freeze-v1.json'

def read(p):
    assert not p.startswith('problems/2019-B4/reviews/reasoning-growth-return-r1-review-2-')
    assert not p.startswith('problems/2024-B4/reviews/coordinator-F8-pencil-r1-')
    return(ROOT/p).read_bytes()

def rec(p):
    b=read(p);return dict(path=p,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())

def j(p):return json.loads(read(p))
def new(s,x):
    with(ROOT/(P+s)).open('x')as f:json.dump(x,f,indent=2);f.write('\n')

for s in ['baseline-v1.json','metadata-v1.json','input-validation-v1.json','manifest-v1.json']:
    assert not(ROOT/(P+s)).exists(),'Do not replay or overwrite frozen review'
fm=T+'freeze-v1.json'; manifest=j(fm)
assert rec(T+'candidate-v1.md')['sha256']=='7e721249102d37af67d14283f27adb5c6156375baa97bcfb3837ea98578fe195'
assert rec(fm)['sha256']=='25d04505390ddad2020300d6459445741967ad9142be311540a5f14e2690b4b7'
bindings=[rec(fm)]
for row in manifest['artifacts']:
    assert rec(row['path'])==row
    bindings.append(row)
constructor_baseline=j(T+'baseline-v1.json')
assert len(constructor_baseline['inputs'])==20
for row in constructor_baseline['inputs']:
    assert rec(row['path'])==row
    bindings.append(row)
extras=[PARENT,
 'problems/2019-B4/reviews/secondpass-acceptance.json',
 'problems/2019-B4/reviews/reasoning-return-r7-acceptance.json',
 'problems/2019-B4/reviews/walk-Frechet-acceptance.json',
 'problems/2019-B4/reviews/coordinator-retained-core-gap-r1-acceptance.json']
for p in extras:bindings.append(rec(p))
for p in extras[1:]:
    assert isinstance(j(p),dict)
for prefix in ['reasoning-return-r7','walk-Frechet']:
    a=j('problems/2019-B4/reviews/'+prefix+'-acceptance.json')
    for key in ['candidate','accepted_copy']:
        assert rec(a[key]['path'])==a[key];bindings.append(a[key])
    assert read(a['accepted_copy']['path']).endswith(read(a['candidate']['path']))
ids=re.findall(r'^\| (G\d\d) \|',read(T+'obligations-v1.md').decode(),re.M)
rid=re.findall(r'^\|(G\d\d)\|',read(P+'ledger-v1.md').decode(),re.M)
assert ids==rid==[f'G{i:02d}'for i in range(1,61)]
unique={}
for row in bindings:
    assert unique.setdefault(row['path'],row)==row
canonical=[unique[p]for p in sorted(unique)]
digest=hashlib.sha256(json.dumps(canonical,sort_keys=True,separators=(',',':')).encode()).hexdigest()
now=datetime.now(timezone.utc).isoformat()
baseline=dict(recorded_utc=now,role='post-read immutable direct-input binding, not mathematical verification',
 exact_target=rec(T+'candidate-v1.md'),constructor_freeze=rec(fm),
 own_compact_parent=rec(PARENT),constructor_necessary_inputs_preserved=True,
 no_NEW_corresponding_peer_or_FP_peer_access=True,records=canonical,
 occurrence_count=len(bindings),unique_paths=len(unique),canonical_summary_sha256=digest,
 no_recursive_historical_inventory_copy_or_proof_replay=True)
new('baseline-v1.json',baseline)
metadata=dict(reviewer='/root',constructor='/root/review_2022_complexity_r2',constructor_excluded=True,
 scope='ENTIRE initially blind OTHER WHOLE G1–G5 and all60 obligations',
 old_DG_retained_core_constructor_and_other_review_roles_disclosed=True,
 own_old_inputs_not_freshly_independently_recertified=True,
 root_generic_assignment_and_typo_correction_not_NEW_inference=True,
 no_NEW_A2019_findings_file_source_code_or_metadata_read_or_hashed=True,
 complete_initial_before_peer_exposure=True,substantive_issues=0,required_repairs=0,
 closed_scope_notes=6,no_mathematical_executable_CAS_scan_author_rerun_or_certificate_replay=True,
 no_regime_numerical_annual_priority_or_fixed_length_claim=True,
 requested_settings=dict(model='gpt-6.1-sol',reasoning='max',inherited=True),
 independently_verified_effective_settings=None,
 last_direct_root_weekly_observation=dict(at_utc='2026-10-18 06:43:18 UTC',used_percent_TOTAL=12,
 reset_unix=1792874445,window_minutes=10080,ordinary_usage_allowed=True,
 user_authorized_current_window_to_TOTAL_percent=90,integration_reserve=True,
 automatic_later_window_spending=False),
 own_compact_parent=rec(PARENT),all60_reconstructed=True)
new('metadata-v1.json',metadata)
validation=dict(verified_utc=now,administrative_only=True,mathematics_checked_by_program=False,
 declared_occurrences_verified=len(bindings),unique_paths_verified=len(unique),
 canonical_summary_sha256=digest,all_current_constructor_payloads_preserved=True,
 complete_constructor20_necessary_current_inputs_preserved=True,
 R7_DG_accepted_copy_literal_suffixes_verified=True,all60_author_reviewer_labels_in_order=True,
 no_NEW_peer_access=True,no_historical_recursive_inventory_walk=True,errors=[])
new('input-validation-v1.json',validation)
suffixes=['initial-v1.md','ledger-v1.md','issues-v1.md','source-checks-v1.md','worklog-v1.md',
 'freeze-v1.py','baseline-v1.json','metadata-v1.json','input-validation-v1.json']
artifacts=[rec(P+s)for s in suffixes]
out=dict(frozen_utc=datetime.now(timezone.utc).isoformat(),
 status='COMPLETE initially blind OTHER ENTIRE WHOLE R1, not promotion',
 exact_target=rec(T+'candidate-v1.md'),constructor_freeze=rec(fm),
 reviewer='/root',all60_obligations=True,substantive_issues=0,required_repairs=0,closed_scope_notes=6,
 no_NEW_A2019_report_findings_source_code_metadata_read_or_hashed=True,
 no_mathematical_executable_or_author_rerun=True,
 own_compact_parent=rec(PARENT),current_occurrences_verified=len(bindings),
 current_unique_paths_verified=len(unique),artifacts=artifacts)
new('manifest-v1.json',out)
for row in canonical+artifacts:assert rec(row['path'])==row
for s in ['baseline-v1.json','metadata-v1.json','input-validation-v1.json','manifest-v1.json']:j(P+s)
print(json.dumps(dict(ENTIRE_whole_initial_frozen=True,manifest=rec(P+'manifest-v1.json'),
 report=rec(P+'initial-v1.md'),all60=True,substantive_issues=0,repairs=0,
 closed_scope_notes=6,record_occurrences=len(bindings),unique_paths=len(unique),
 mathematical_code=False),indent=2))
