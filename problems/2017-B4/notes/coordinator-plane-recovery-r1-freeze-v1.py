"""One-shot administrative PUS freeze: no mathematical code or author replay."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re
ROOT=Path(__file__).resolve().parents[3]
P='problems/2017-B4/notes/coordinator-plane-recovery-r1-'
def rec(path):
    b=(ROOT/path).read_bytes()
    return dict(path=path,bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def out(suffix,data):
    with(ROOT/(P+suffix)).open('x')as f:json.dump(data,f,indent=2,ensure_ascii=False);f.write('\n')
    return rec(P+suffix)
for suffix in ['input-validation-v1.json','freeze-v1.json']:
    assert not(ROOT/(P+suffix)).exists(), 'Never overwrite a frozen packet'
paths=[
'AGENTS.md','problems/2017-B4/statement.md',
'problems/2017-B4/proofs/reviewed-reasoning-value-return-r6-v1.1.md',
'problems/2017-B4/reviews/reasoning-value-return-r6-acceptance.md',
'problems/2017-B4/reviews/reasoning-value-return-r6-acceptance.json',
'problems/2017-B4/reviews/reasoning-value-return-r6-acceptance-integrity.json',
'problems/2017-B4/proofs/reviewed-allD-uniform-strict-v1.1.md',
'problems/2017-B4/reviews/allD-uniform-strict-acceptance.md',
'problems/2017-B4/reviews/allD-uniform-strict-acceptance.json',
]
rows=[rec(p)for p in paths]
expected={
'problems/2017-B4/proofs/reviewed-reasoning-value-return-r6-v1.1.md':(42807,'e0b25980d4073bb32634d1f1826bc383dcb00c2c1754f252f91410b6cf0a30d8'),
'problems/2017-B4/proofs/reviewed-allD-uniform-strict-v1.1.md':(39136,'a5ebfd81d59b26f301b1e105889451f4c86262da80e6e77e6913c045d71147d2'),
}
for p,(n,h) in expected.items(): assert rec(p)==dict(path=p,bytes=n,sha256=h)
for f in [paths[4],paths[8]]:
    a=json.loads((ROOT/f).read_text())
    assert a['unresolved_substantive_issues']==0 and not a['repair_required']
    for k in ['candidate','accepted_copy']:
        x=a[k];assert rec(x['path'])=={z:x[z]for z in ['path','bytes','sha256']};rows.append({z:x[z]for z in ['path','bytes','sha256']})
    assert (ROOT/a['accepted_copy']['path']).read_bytes().endswith((ROOT/a['candidate']['path']).read_bytes())
u={}
for x in rows:assert u.setdefault(x['path'],x)==x
digest=hashlib.sha256(json.dumps([u[k]for k in sorted(u)],sort_keys=True,separators=(',',':')).encode()).hexdigest()
tags=re.findall(r'^\|([0-9]{2})\|',(ROOT/(P+'obligations-v1.md')).read_text(),re.M)
assert tags==[f'{i:02d}'for i in range(1,37)]
out('input-validation-v1.json',dict(verified_at_utc=datetime.now(timezone.utc).isoformat(),administrative_only=True,records=rows,occurrences=len(rows),unique_paths=len(u),canonical_deduplicated_sha256=digest,both_accepted_candidate_copy_suffixes_exact=True,all36_obligations_in_order=True,historical_inventories_rewalked_or_copied=False,root_NEW_constructor_excluded=True,no_NEW_peer_PUS_files_findings_or_contribution=True,requested_model='gpt-6.1-sol',requested_reasoning='max',effective_setting_readback=None))
suffixes=['candidate-v1.md','obligations-v1.md','source-audit-v1.md','failed-routes-v1.md','worklog-v1.md','freeze-v1.py','input-validation-v1.json']
artifacts=[rec(P+s)for s in suffixes]
manifest=out('freeze-v1.json',dict(frozen_at_utc=datetime.now(timezone.utc).isoformat(),status='COMPLETE constructor PUS1–PUS3; candidate proof - unverified',constructor='/root',root_excluded_from_OTHER_audit_count=True,whole_obligations=36,claims=['PUS1 complete-boundary exterior independence','PUS2 lower interface preserving ORIGINAL plane reference outside EXACT dilated patch','PUS3 same-density rational/real compact-strict plane recovery'],TWO_OTHER_initially_blind_ENTIRE_WHOLE_audits_required=True,no_global_mass_upper_R_value_annual_or_novelty_claim=True,compact_input_summary=dict(occurrences=len(rows),unique_paths=len(u),canonical_deduplicated_sha256=digest),artifacts=artifacts))
for x in rows+artifacts:assert rec(x['path'])==x
print(json.dumps(dict(main=artifacts[0],manifest=manifest,all36=True,all_postverified=True,mathematical_computation=False),indent=2))
