#!/usr/bin/env python3
"""Exploratory leading-root coupling; candidate formulas, not reviewed proof.

Explicit constructor reuse of the earlier first-order projection's method.
Adds c3/c4 root-sum identity and equal-valuation low-derivative ratios.
"""
from pathlib import Path
from itertools import product
from math import comb
from collections import Counter
import datetime,hashlib,json,subprocess,sys,time

HERE=Path(__file__).resolve().parent
PREFIX='coordinator-J16-coupled-leading-v1'
SOURCE=HERE.parent/'reviews/newton-review-1-extension-result.json'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def valuation(n,p=19):
    assert n
    v=0
    while n%p==0:n//=p;v+=1
    return v

def child():
    p=19;b=[0,0]+[comb(20,j)//p for j in range(2,19)]
    masks=json.loads(SOURCE.read_text())['retained_masks']['16']
    rows=[];hist=Counter();total=0
    for mask in masks:
        a=[1,-1]+[0]*17;active=[]
        for j in range(2,19):
            if mask & (1<<(j-2)):a[j]=-sum(comb(j,k)*a[k] for k in range(j))
            elif a[j-1]%p:active.append(j)
        q0=-1+sum(b[j]*a[j] for j in range(2,19))
        assert q0 and q0%p==0 and a[17]%p==a[18]%p==0
        h3=bool(mask&(1<<15));h2=bool(mask&(1<<16));assert h2 or h3
        bound=valuation(q0);passing=Counter();examples={};tests=0
        for labels_tuple in product((0,1,2),repeat=len(active)):
            labels=dict(zip(active,labels_tuple));left=[0]*19;right=[0]*19
            for j in range(2,19):
                if mask&(1<<(j-2)):
                    left[j]=-sum(comb(j,k)*left[k] for k in range(j))%p
                    right[j]=-sum(comb(j,k)*right[k] for k in range(j))%p
                elif j in labels:
                    if labels[j]==1:left[j]=-j*a[j-1]%p
                    if labels[j]==2:right[j]=-j*a[j-1]%p
            for nu in range(1,bound+1):
                power=p**nu
                if a[17]%power or a[18]%power:continue
                # Necessary lift of P=f(1)/19 and a18 divisible by p^(2nu).
                # At nu>1 only its weaker consequence mod p^(nu+1) is used.
                eq1=[q0//power,sum(b[j]*left[j] for j in range(2,19)),sum(b[j]*right[j] for j in range(2,19))]
                eq2=[a[18]//power,left[18],right[18]]
                # c3/(p^(1+nu)) = -(c4/p)*(U+V) mod p.
                c4unit=b[16]*a[16]%p
                eq3=[b[17]*(a[17]//power),b[17]*left[17]+c4unit,b[17]*right[17]+c4unit]
                tests+=1
                for u in range(p):
                    for v in range(p):
                        if u==v==0:continue
                        if any((c+A*u+B*v)%p for c,A,B in [eq1,eq2,eq3]):continue
                        if not (h2 and h3):
                            # Unequal valuations force BOTH center equations;
                            # sole-center cases therefore have u,v nonzero.
                            if u==0 or v==0:continue
                            if h2:
                                # H3 noncenter: zero, u or v.
                                if all(z%p for z in [u+v,3*u-v,3*v-u]):continue
                            else:
                                # H2 noncenter: u or v (zero is not a root).
                                if (3*u-2*v)%p and (3*v-2*u)%p:continue
                        key=f'nu{nu}';passing[key]+=1
                        examples.setdefault(key,{'active_labels':list(labels_tuple),'residue_U_V':[u,v],
                                                 'equations':[eq1,eq2,eq3]})
        total+=tests
        row={'center_mask':mask,'H2_center':h2,'H3_center':h3,'minimum_valuation_upper_bound':bound,
             'active_positions':active,'projected_label_and_nu_tests':tests,
             'passing_leading_points':dict(passing),'first_examples':examples,
             'excluded_by_this_necessary_projection':not bool(passing)}
        rows.append(row);hist[str((h2,h3))+' excluded='+str(not bool(passing))]+=1
        print(json.dumps({'mask_complete':mask,'passing':dict(passing),'excluded':not bool(passing)}),flush=True)
    result={'status':'finite candidate coupled projection; no independent mathematical audits',
            'prime':19,'J':16,'masks':len(masks),'projected_label_and_nu_tests':total,
            'excluded_masks':[r['center_mask'] for r in rows if r['excluded_by_this_necessary_projection']],
            'retained_masks':[r['center_mask'] for r in rows if not r['excluded_by_this_necessary_projection']],
            'histogram':dict(hist),'rows':rows,'source_sha256':sha(SOURCE),
            'constructor_method_reused_from':'coordinator-J16-linear-projection-v1.py',
            'previous_source_sha256':sha(HERE/'coordinator-J16-linear-projection-v1.py')}
    (HERE/(PREFIX+'-result.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)

def main():
    if '--child' in sys.argv:child();return
    out,err,job=[HERE/(PREFIX+s) for s in ('-output.txt','-stderr.txt','-job.json')]
    cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--child']
    rec={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'timeout_seconds':30,'status':'launching'}
    start=time.monotonic()
    with out.open('w') as f,err.open('w') as e:
        proc=subprocess.Popen(cmd,stdout=f,stderr=e);rec.update(pid=proc.pid,status='running')
        job.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
        try:proc.wait(timeout=30);rec['status']='completed' if proc.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:proc.kill();proc.wait();rec['status']='timeout; identified child reaped'
        rec.update(return_code=proc.returncode,elapsed_seconds=time.monotonic()-start)
    rec['sha256']={p.name:sha(p) for p in [Path(__file__),out,err,HERE/(PREFIX+'-result.json')] if p.is_file()}
    job.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)

if __name__=='__main__':main()
