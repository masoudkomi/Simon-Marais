#!/usr/bin/env python3
"""Complete complementary degree20 three-complex-witness families, construction only.

Certificate rows: [center_mask,U_mask,0,nonzero_constant] or
[center_mask,U_mask,prime,degree_P,degree_Q,lead_P_mod_prime,lead_Q_mod_prime].
All coefficients are regenerated exactly; aggregate polynomial SHA binds them.
Gzip chunks avoid large opaque single files and use deterministic headers.
"""
import collections,datetime,gzip,hashlib,importlib.util,json,math
from pathlib import Path
import subprocess,sys,time

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
PREFIX='coordinator-three-complex-witnesses-v1'
HELPERS=HERE/'padic-rational-j17-compatibility.py'
MASKS=HERE/'coordinator-three-complex-masks-v1-result.json'
PRIMES=(101,103,107,109,127)
CHUNK_SIZE=60000

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def emit(**x):print(json.dumps(x,sort_keys=True),flush=True)

def worker():
    spec=importlib.util.spec_from_file_location('frozen_author_helpers',HELPERS)
    module=importlib.util.module_from_spec(spec);sys.dont_write_bytecode=True
    spec.loader.exec_module(module)
    trim,add_scaled,mod_gcd=module.trim,module.add_scaled,module.mod_gcd
    masks=json.loads(MASKS.read_text())['additional_center_masks']
    assert len(masks)==5908 and len(set(masks))==5908
    expected=sum(2**(17-mask.bit_count()) for mask in masks)
    assert expected==4731928
    emit(event='parameters',patterns=len(masks),refinements=expected,
         mask_convention='bit j-2 is center1 for normalized derivative D_j',
         helpers_sha256=sha(HELPERS),masks_sha256=sha(MASKS),primes=PRIMES,
         certificate_rows='constant:[mask,U_mask,0,P]; modular:[mask,U_mask,prime,degP,degQ,leadP,leadQ]',
         chunk_size=CHUNK_SIZE,scope='5908additionalmasks;allnoncenterwitnesses0orU;noNewtonorrational-onlyfilter')
    a=[[0] for _ in range(19)];a[0],a[1]=[1],[-1]
    bins=[[math.comb(j,k) for k in range(j+1)] for j in range(21)]
    visited=0;success=collections.Counter();unresolved=0
    polynomial_digest=hashlib.sha256();certificate_digest=hashlib.sha256()
    chunks=[];rawfile=None;gz=None;chunk_rows=0;chunk_path=None
    start=time.monotonic()
    def close_chunk():
        nonlocal rawfile,gz,chunk_rows,chunk_path
        if gz is not None:
            gz.close();rawfile.close()
            chunks.append({'path':str(chunk_path.relative_to(HERE.parents[2])),
                           'rows':chunk_rows,'bytes':chunk_path.stat().st_size,
                           'sha256':sha(chunk_path)})
            rawfile=gz=None;chunk_rows=0
    def write_certificate(rec):
        nonlocal rawfile,gz,chunk_rows,chunk_path
        if gz is None:
            chunk_path=HERE/(PREFIX+f'-certificates-{len(chunks)+1:03}.jsonl.gz')
            rawfile=chunk_path.open('wb')
            gz=gzip.GzipFile(filename='',mode='wb',fileobj=rawfile,mtime=0)
        line=(json.dumps(rec,separators=(',',':'))+'\n').encode()
        certificate_digest.update(line);gz.write(line);chunk_rows+=1
        if chunk_rows==CHUNK_SIZE:close_chunk()
    with (HERE/(PREFIX+'-unresolved.jsonl')).open('w') as failures:
        def finish(mask,u_mask):
            nonlocal visited,unresolved
            p=[-19];q=[0]*21;q[20],q[19]=1,-20
            for j in range(2,19):
                add_scaled(p,a[j],bins[20][j]);add_scaled(q,a[j],bins[20][j],20-j)
            trim(p);trim(q);visited+=1
            polynomial_digest.update((json.dumps([mask,u_mask,p,q],separators=(',',':'))+'\n').encode())
            if len(p)==1 and p[0]!=0:
                write_certificate([mask,u_mask,0,p[0]]);success['constant_nonzero']+=1
            else:
                for ell in PRIMES:
                    if p[-1]%ell==0 or q[-1]%ell==0:continue
                    if mod_gcd(p,q,ell)==0:
                        write_certificate([mask,u_mask,ell,len(p)-1,len(q)-1,p[-1]%ell,q[-1]%ell])
                        success[str(ell)]+=1;break
                else:
                    failures.write(json.dumps({'center_mask':mask,'u_mask':u_mask,'P':p,'Q':q})+'\n')
                    write_certificate([mask,u_mask,-1]);unresolved+=1
            if visited%8192==0:
                failures.flush()
                if gz is not None:gz.flush();rawfile.flush()
                emit(event='checkpoint',visited=visited,unresolved=unresolved,completed_chunks=len(chunks),elapsed_seconds=time.monotonic()-start)
        def descend(j,mask,u_mask):
            if j==19:finish(mask,u_mask);return
            if mask & (1<<(j-2)):
                value=[0]
                for k in range(j):add_scaled(value,a[k],-bins[j][k])
                a[j]=trim(value);descend(j+1,mask,u_mask)
            else:
                a[j]=[0];descend(j+1,mask,u_mask)
                value=[0]
                for k in range(j):add_scaled(value,a[k],-bins[j][k],j-k)
                a[j]=trim(value);descend(j+1,mask,u_mask|(1<<(j-2)))
            a[j]=[0]
        for mask in masks:descend(2,mask,0)
    close_chunk()
    assert visited==expected and sum(c['rows'] for c in chunks)==expected
    result={'status':'complete finite construction; not independently reviewed',
            'patterns':len(masks),'refinements':visited,'resolved':sum(success.values()),
            'unresolved':unresolved,'resolution_histogram':dict(success),
            'polynomial_stream_sha256':polynomial_digest.hexdigest(),
            'uncompressed_certificate_stream_sha256':certificate_digest.hexdigest(),
            'chunks':chunks,'elapsed_seconds':time.monotonic()-start}
    (HERE/(PREFIX+'-result.json')).write_text(json.dumps(result,indent=2)+'\n')
    emit(event='complete',**{k:v for k,v in result.items() if k!='chunks'})

def main():
    if '--child' in sys.argv:worker();return
    out,err,job=[HERE/(PREFIX+s) for s in ('-output.txt','-stderr.txt','-job.json')]
    cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--child']
    rec={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,
         'timeout_seconds':900,'status':'launching','helpers_sha256':sha(HELPERS),
         'masks_sha256':sha(MASKS),'construction_only':True}
    start=time.monotonic()
    with out.open('w') as f,err.open('w') as e:
        proc=subprocess.Popen(cmd,stdout=f,stderr=e);rec.update(pid=proc.pid,status='running')
        job.write_text(json.dumps(rec,indent=2)+'\n');emit(**rec)
        try:proc.wait(timeout=900);rec['status']='completed' if proc.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:proc.kill();proc.wait();rec['status']='timeout; identified child reaped; partial chunks not a complete certificate'
        rec.update(return_code=proc.returncode,elapsed_seconds=time.monotonic()-start)
    rec['sha256']={p.name:sha(p) for p in [Path(__file__),out,err,HERE/(PREFIX+'-result.json'),HERE/(PREFIX+'-unresolved.jsonl')] if p.is_file()}
    job.write_text(json.dumps(rec,indent=2)+'\n');emit(**rec)

if __name__=='__main__':main()
