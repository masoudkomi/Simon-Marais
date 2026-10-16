#!/usr/bin/env python3
"""Fast full-result bookkeeping audit, following the complete mathematical audit."""
import collections
import gzip
import importlib.util
import json
from pathlib import Path
import sys
import time

HERE=Path(__file__).resolve().parent
COMP=HERE.parent/'computations'
PREFIX=HERE/'J16-digits-review-2'
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location('r2_math',HERE/'J16-digits-review-2-independent.py')
R=importlib.util.module_from_spec(spec);spec.loader.exec_module(R)
J=lambda p:json.loads(p.read_text())
own=J(Path(str(PREFIX)+'-full-result.json'))
old=J(COMP/'coordinator-J16-second-digit-v1-result.json')
v1=J(COMP/'owner-J16-Hensel-v1-result.json')
v2=J(COMP/'owner-J16-Hensel-v2-result.json')
start=time.monotonic()
rankhist=collections.Counter();counts=collections.defaultdict(lambda:[0,0]);first={}
with gzip.open(Path(str(PREFIX)+'-full-certificates.jsonl.gz'),'rt') as f:
    for line in f:
        k,key,c,rank,omit,digits=json.loads(line)
        if k!=1:
            break
        rankhist[str(rank)+' consistent='+str(bool(digits))]+=1
        counts[key[0]][0]+=1;counts[key[0]][1]+=bool(digits)
        if digits:
            first.setdefault(key[0],(key,c))
assert sum(v[0] for v in counts.values())==old['visited']==old['expected_branches']==840396
assert sum(v[1] for v in counts.values())==old['passing']==125346
assert dict(rankhist)==old['rank_histogram']
assert {str(m):v for m,v in counts.items()}==old['per_mask_tested_passing']
assert sorted(m for m,(n,g) in counts.items() if g)==old['candidate_remaining_J16_masks']
assert len(old['candidate_remaining_J16_masks'])==58
for sm,example in old['first_passing_examples'].items():
    key,c=first[int(sm)]
    assert example['key']==key
    M=R.linear(*key[:3])
    assert example['affine_rows']==[[x,y,z] for (x,y),z in zip(M,c)]
for k,level in enumerate(v1['levels'],1):
    st=own['layers'][k-1]
    assert level['input_precision']==k and level['input_expected_nodes']==st['parents']
    assert level['complete_input_traversal'] and level['stopped'] is None
    for sm,(visited,passing,generated) in level['per_mask_visited_passing_generated'].items():
        assert visited==st['parent_masks'].get(sm,0)
        assert generated==st['child_masks'].get(sm,0)
    tally={}
    for text,n in st['systems'].items():
        rank,good=text.strip('()').split(', ')
        tally['rank'+rank+'_consistent'+good]=n
    if st['T1_omitted']:
        tally['pruned_by_accepted_T1_missing_label']=st['T1_omitted']
    assert level['tally']==tally
assert v1['candidate_masks_at_last_complete_precision']==sorted(map(int,own['layers'][2]['child_masks']))
assert v1['last_complete_precision']==4 and v1['target_precision']==4
assert v1['node_cap_per_level']==1000000 and not v1['benchmark']
for i,level in enumerate(v2['levels']):
    st=own['layers'][i+3]
    assert level['input_nodes']==st['parents'] and level['output_nodes']==st['children']
    assert level['input_precision']==i+4 and level['output_precision']==i+5
    assert level['input_mask_counts']==st['parent_masks']
    assert {m:n for m,n in level['output_mask_counts'].items() if n}==st['child_masks']
    assert level['complete_input_traversal']
assert v2['last_complete_precision']==6 and v2['last_output_nodes']==0
assert v2['target_precision']==8 and v2['node_cap_per_level']==90
assert v2['candidate_masks_at_last_complete_precision']==[] and not v2['benchmark']

# Check the original ordinary Hasse equations at every one of the 104
# late exact states, using c_i and ordinary binomial coefficients directly.
hasse_count=0
for state in own['late_exact_states']:
    mask,um,vm,nu,X,Y=state['key'];u,v=19**nu*X,19**nu*Y
    a=state['a'];c=[0]*21
    for j in range(19):
        c[20-j]=R.C[20][j]*a[j]
    for j in range(2,19):
        bit=1<<(j-2)
        w=1 if mask&bit else u if um&bit else v if vm&bit else 0
        order=20-j
        val=sum(c[i]*R.C[i][order]*w**(i-order) for i in range(order,21))
        assert val==0
        hasse_count+=1
    assert c[0]==c[1]==0 and c[19]+20*c[20]==0
    hasse_count+=2

jobs={}
for name in ('coordinator-J16-coupled-leading-v1','coordinator-J16-leading-branch-index-v1',
             'coordinator-J16-second-digit-v1','owner-J16-Hensel-v1','owner-J16-Hensel-v1-postcheck',
             'owner-J16-Hensel-v2'):
    job=J(COMP/(name+'-job.json'))
    assert job['return_code']==0
    assert job['timeout_seconds']<=300
    assert job['elapsed_seconds']<job['timeout_seconds']
    jobs[name]={'pid':job['pid'],'cap':job['timeout_seconds'],'elapsed':job['elapsed_seconds'],'exit_code':0}
result={'complete':True,'ordinary_hasse_equations_checked':hasse_count,
        'root_consistent_parents':125346,'root_rank_histogram':dict(rankhist),
        'result_bookkeeping_matched':True,'candidate_jobs':jobs,'seconds':time.monotonic()-start}
Path(str(PREFIX)+'-metadata-result.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
