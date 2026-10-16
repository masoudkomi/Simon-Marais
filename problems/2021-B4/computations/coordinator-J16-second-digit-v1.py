#!/usr/bin/env python3
"""Candidate next-digit necessary projection; no independent review credit.

The complete leading cover is an explicitly unreviewed construction input.
Scalar truncated recursions replace bivariate elimination. Benchmark is
deliberately incomplete; only a full traversal can supply mask exclusions.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import datetime,gzip,hashlib,json,math,subprocess,sys,time

HERE=Path(__file__).resolve().parent
SOURCE=HERE/'coordinator-J16-leading-branch-index-v1-result.json'
BINS=[[math.comb(j,k) for k in range(j+1)] for j in range(21)]
BETA=[0,0]+[math.comb(20,j)//19 for j in range(2,19)]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def emit(x):print(json.dumps(x,sort_keys=True),flush=True)

def consistent(rows,p=19):
    a=[[x%p,y%p,(-c)%p] for x,y,c in rows];rank=0
    for col in range(2):
        pivot=next((r for r in range(rank,3) if a[r][col]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        inv=pow(a[rank][col],-1,p);a[rank]=[v*inv%p for v in a[rank]]
        for r in range(3):
            if r!=rank:
                scale=a[r][col];a[r]=[(a[r][k]-scale*a[rank][k])%p for k in range(3)]
        rank+=1
    return not any(r[0]==r[1]==0 and r[2] for r in a),rank

def worker(limit,prefix):
    source=json.loads(SOURCE.read_text());branches=source['leading_branches']
    assert len(branches)==768 and source['expanded_label_residue_branches']==840396
    visited=0;passed=0;start=time.monotonic();counts={m:[0,0] for m in source['retained_masks']}
    examples={};ranks=Counter();digest=hashlib.sha256();coeff_digest=hashlib.sha256()
    raw=None;gz=None;chunk_rows=0;chunks=[];chunk_path=None
    def close():
        nonlocal raw,gz,chunk_rows
        if gz:
            gz.close();raw.close();chunks.append({'path':str(chunk_path.relative_to(HERE.parents[2])),
                'rows':chunk_rows,'bytes':chunk_path.stat().st_size,'sha256':sha(chunk_path)})
            raw=gz=None;chunk_rows=0
    def save(row):
        nonlocal raw,gz,chunk_rows,chunk_path
        if gz is None:
            chunk_path=HERE/(prefix+f'-certificates-{len(chunks)+1:03}.jsonl.gz')
            raw=chunk_path.open('wb');gz=gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0)
        line=(json.dumps(row,separators=(',',':'))+'\n').encode()
        digest.update(line);gz.write(line);chunk_rows+=1
        if chunk_rows==60000:close()
    stop=False
    for branch in branches:
        mask=branch['center_mask'];nu=branch['nu'];u=branch['U'];v=branch['V'];p=19
        fixed=dict(zip(branch['active_positions'],branch['active_labels']))
        inactive=branch['inactive_positions'];assert 3**len(inactive)==branch['full_label_expansions']
        left=[0]*19;right=[0]*19
        # Only active labels affect derivatives at (0,0) modulo19.
        a0=[1,-1]+[0]*17
        for j in range(2,19):
            if mask&(1<<(j-2)):
                a0[j]=-sum(BINS[j][k]*a0[k] for k in range(j))%p
                left[j]=-sum(BINS[j][k]*left[k] for k in range(j))%p
                right[j]=-sum(BINS[j][k]*right[k] for k in range(j))%p
            elif fixed.get(j)==1:left[j]=-j*a0[j-1]%p
            elif fixed.get(j)==2:right[j]=-j*a0[j-1]%p
        C4=BETA[16]*a0[16]%p
        matrix=[(sum(BETA[j]*left[j] for j in range(2,19))%p,sum(BETA[j]*right[j] for j in range(2,19))%p),
                (left[18],right[18]),((BETA[17]*left[17]+C4)%p,(BETA[17]*right[17]+C4)%p)]
        mod=p**(nu+2);power=p**nu;w1=power*u;w2=power*v
        for extra in product((0,1,2),repeat=len(inactive)):
            labels={**fixed,**dict(zip(inactive,extra))};a=[1,-1]+[0]*17;um=vm=0
            for j in range(2,19):
                if mask&(1<<(j-2)):
                    a[j]=-sum(BINS[j][k]*a[k] for k in range(j))%mod
                else:
                    label=labels[j];w=(0,w1,w2)[label]
                    if label==1:um|=1<<(j-2)
                    if label==2:vm|=1<<(j-2)
                    a[j]=(-j*a[j-1]*w-(BINS[j][j-2]*a[j-2]*w*w if nu==1 else 0))%mod
            P=(-1+sum(BETA[j]*a[j] for j in range(2,19)))%mod
            assert P%(p**(nu+1))==0 and a[18]%(p**(nu+1))==0 and a[17]%(p**nu)==0
            const1=P//(p**(nu+1))
            if nu==1:
                const2=(a[18]//(p*p)-C4*pow(BETA[18]%p,-1,p)*u*v)%p
                residual=(BETA[17]*(a[17]//p)+BETA[16]*a[16]*(u+v)
                          -p*BETA[15]*a[15]*(u*v-(u+v)**2))%(p*p)
            else:
                assert nu==2
                const2=a[18]//(p**3)
                residual=(BETA[17]*(a[17]//(p*p))+BETA[16]*a[16]*(u+v))%(p*p)
            assert residual%p==0
            constants=[const1%p,const2%p,(residual//p)%p]
            ok,rank=consistent([(x,y,c) for (x,y),c in zip(matrix,constants)])
            key=[mask,um,vm,nu,u,v]
            coeff_digest.update((json.dumps([key,a],separators=(',',':'))+'\n').encode())
            save(key+constants+[rank,int(ok)])
            visited+=1;counts[mask][0]+=1;ranks[str(rank)+' consistent='+str(ok)]+=1
            if ok:
                passed+=1;counts[mask][1]+=1
                examples.setdefault(mask,{'key':key,'affine_rows':[[x,y,c] for (x,y),c in zip(matrix,constants)]})
            if visited%8192==0:
                if gz:gz.flush();raw.flush()
                emit({'checkpoint':visited,'passing':passed,'elapsed_seconds':time.monotonic()-start})
            if limit and visited>=limit:stop=True;break
        if stop:break
    close()
    complete=visited==840396
    if not limit:assert complete
    result={'status':'complete finite construction; not independently reviewed' if complete else 'incomplete benchmark; no mask exclusion established',
            'expected_branches':840396,'visited':visited,'passing':passed,'limit':limit,
            'rank_histogram':dict(ranks),'per_mask_tested_passing':counts,'first_passing_examples':examples,
            'certificate_stream_sha256':digest.hexdigest(),'scalar_coefficient_stream_sha256':coeff_digest.hexdigest(),
            'chunks':chunks,'source_sha256':sha(SOURCE),'elapsed_seconds':time.monotonic()-start,
            'candidate_remaining_J16_masks':sorted(m for m,(tested,good) in counts.items() if good) if complete else None,
            'old_leading_exclusions':source['excluded_masks']}
    (HERE/(prefix+'-result.json')).write_text(json.dumps(result,indent=2)+'\n')
    emit({k:v for k,v in result.items() if k not in ['chunks','first_passing_examples','per_mask_tested_passing']})

def main():
    limit=8192 if '--benchmark' in sys.argv else 0
    prefix='coordinator-J16-second-digit-v1'+('-benchmark' if limit else '')
    if '--child' in sys.argv:worker(limit,prefix);return
    cap=30 if limit else 180
    out,err,job=[HERE/(prefix+s) for s in ['-output.txt','-stderr.txt','-job.json']]
    cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--child']+(['--benchmark'] if limit else [])
    rec={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'timeout_seconds':cap,
         'status':'launching','source_sha256':sha(SOURCE),'construction_only':True,'limit':limit}
    start=time.monotonic()
    with out.open('w') as f,err.open('w') as e:
        proc=subprocess.Popen(cmd,stdout=f,stderr=e);rec.update(pid=proc.pid,status='running');job.write_text(json.dumps(rec,indent=2)+'\n');emit(rec)
        try:proc.wait(timeout=cap);rec['status']='completed' if proc.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:proc.kill();proc.wait();rec['status']='timeout; identified child reaped; incomplete data'
        rec.update(return_code=proc.returncode,elapsed_seconds=time.monotonic()-start)
    rec['sha256']={p.name:sha(p) for p in [Path(__file__),out,err,HERE/(prefix+'-result.json')] if p.is_file()}
    job.write_text(json.dumps(rec,indent=2)+'\n');emit(rec)

if __name__=='__main__':main()
