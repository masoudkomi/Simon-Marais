#!/usr/bin/env python3
"""Exploratory p-adic necessary projection, conditional on unreviewed T2.

No two-variable polynomial elimination and no independent-review credit.
"""
from pathlib import Path
from itertools import product
from math import comb
from collections import Counter
import datetime,hashlib,json,subprocess,sys,time

HERE=Path(__file__).resolve().parent
PREFIX='coordinator-J16-linear-projection-v1'
SOURCE=HERE.parent/'reviews/newton-review-1-extension-result.json'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def valuation(n,p=19):
    assert n
    v=0
    while n%p==0:n//=p;v+=1
    return v

def child():
    p=19;b=[comb(20,j)//p for j in range(2,19)]
    masks=json.loads(SOURCE.read_text())['retained_masks']['16']
    rows=[];hist=Counter();valuation_hist=Counter();total=0
    for mask in masks:
        a=[1,-1]+[0]*17;active=[]
        for j in range(2,19):
            if mask & (1<<(j-2)):a[j]=-sum(comb(j,k)*a[k] for k in range(j))
            elif a[j-1]%p:active.append(j)
        assert max(j for j in range(2,19) if a[j]%p)==16
        q0=-1+sum(b[j-2]*a[j] for j in range(2,19))
        assert q0 and q0%p==0 and a[18]%p==0
        max_min_val=valuation(q0);valuation_hist[max_min_val]+=1;hist[len(active)]+=1
        passing=0;example=None;tests=[]
        for choices in product((0,1,2),repeat=len(active)):
            labels=dict(zip(active,choices));left=[0]*19;right=[0]*19
            for j in range(2,19):
                if mask & (1<<(j-2)):
                    left[j]=-sum(comb(j,k)*left[k] for k in range(j))%p
                    right[j]=-sum(comb(j,k)*right[k] for k in range(j))%p
                elif j in labels:
                    if labels[j]==1:left[j]=-j*a[j-1]%p
                    if labels[j]==2:right[j]=-j*a[j-1]%p
            eq1=[(q0//p)%p,sum(b[j-2]*left[j] for j in range(2,19))%p,sum(b[j-2]*right[j] for j in range(2,19))%p]
            eq2=[(a[18]//p)%p,left[18],right[18]]
            points=[]
            for u in range(p):
                for v in range(p):
                    if max_min_val==1 and u==v==0:continue
                    if (eq1[0]+eq1[1]*u+eq1[2]*v)%p==0 and (eq2[0]+eq2[1]*u+eq2[2]*v)%p==0:points.append([u,v])
            total+=1
            rec={'active_labels':list(choices),'equations_constant_U1_V1':[eq1,eq2],'residue_solutions':len(points)}
            tests.append(rec)
            if points:
                passing+=1
                if example is None:example={**rec,'first_residue_solution':points[0]}
        rows.append({'center_mask':mask,'active_positions':active,'constant_divided_f1':q0,
                     'minimum_witness_valuation_upper_bound':max_min_val,
                     'projected_assignments':len(tests),'assignments_with_some_residue_point':passing,
                     'excluded_by_projection':passing==0,'first_projection_example':example,'tests':tests})
        print(json.dumps({'mask_complete':mask,'projected_assignments':len(tests),'passing':passing}),flush=True)
    result={'status':'finite exploratory necessary projection; T2 dependency and projection proof unverified',
            'degree':20,'prime':19,'J':16,'masks':len(masks),'source_sha256':sha(SOURCE),
            'full_0UV_assignments':sum(3**(17-m.bit_count()) for m in masks),
            'both_UV_used_mod_swap_assignments':sum((3**(17-m.bit_count())-2*2**(17-m.bit_count())+1)//2 for m in masks),
            'active_transition_histogram':dict(sorted(hist.items())),
            'constant_valuation_histogram':dict(sorted(valuation_hist.items())),
            'projected_assignments':total,'excluded_masks':[r['center_mask'] for r in rows if r['excluded_by_projection']],
            'rows':rows}
    (HERE/(PREFIX+'-result.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)

def main():
    if '--child' in sys.argv:child();return
    out,err,job=[HERE/(PREFIX+s) for s in ('-output.txt','-stderr.txt','-job.json')]
    cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--child']
    rec={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'timeout_seconds':30,'status':'launching'}
    start=time.monotonic()
    with out.open('w') as f,err.open('w') as e:
        proc=subprocess.Popen(cmd,stdout=f,stderr=e);rec.update(pid=proc.pid,status='running');job.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
        try:proc.wait(timeout=30);rec['status']='completed' if proc.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:proc.kill();proc.wait();rec['status']='timeout; identified child reaped'
        rec.update(return_code=proc.returncode,elapsed_seconds=time.monotonic()-start)
    rec['sha256']={p.name:sha(p) for p in [Path(__file__),out,err,HERE/(PREFIX+'-result.json')] if p.is_file()}
    job.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)

if __name__=='__main__':main()
