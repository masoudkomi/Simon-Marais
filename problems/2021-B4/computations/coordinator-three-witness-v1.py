#!/usr/bin/env python3
"""Exact selected three-witness families; exploratory until independently audited.

Reuses the frozen author's elementary polynomial helpers, explicitly recorded.
This is construction, not independent verification of the earlier packet.
"""
import argparse,collections,datetime,hashlib,importlib.util,json,math
from pathlib import Path
import subprocess,sys,time

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
HELPERS=HERE/'padic-rational-j17-compatibility.py'
MASKS=BASE/'reviews/newton-review-1-extension-result.json'
PRIMES=(101,103,107,109,127)

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def emit(**x):print(json.dumps(x,sort_keys=True),flush=True)

def worker(jvalue):
    prefix=f'coordinator-three-witness-J{jvalue}-v1'
    spec=importlib.util.spec_from_file_location('frozen_author_helpers',HELPERS)
    module=importlib.util.module_from_spec(spec);sys.dont_write_bytecode=True
    spec.loader.exec_module(module)
    trim,add_scaled,mod_gcd=module.trim,module.add_scaled,module.mod_gcd
    masks=json.loads(MASKS.read_text())['retained_masks'][str(jvalue)]
    expected=sum(2**(17-mask.bit_count()) for mask in masks)
    emit(event='parameters',last_unit_index=jvalue,patterns=len(masks),refinements=expected,
         mask_convention='bit j-2 is center1 for normalized derivative D_j',
         helpers_sha256=sha(HELPERS),masks_sha256=sha(MASKS),primes=PRIMES,
         scope='all selected necessary masks, all noncenter witnesses 0 or U')
    a=[[0] for _ in range(19)];a[0],a[1]=[1],[-1]
    bins=[[math.comb(j,k) for k in range(j+1)] for j in range(21)]
    visited=0;success=collections.Counter();unresolved=0;digest=hashlib.sha256()
    start=time.monotonic()
    with (HERE/(prefix+'-certificates.jsonl')).open('w') as cert:
        def finish(mask,u_mask):
            nonlocal visited,unresolved
            p=[-19];q=[0]*21;q[20],q[19]=1,-20
            for j in range(2,19):
                add_scaled(p,a[j],bins[20][j]);add_scaled(q,a[j],bins[20][j],20-j)
            trim(p);trim(q);visited+=1
            raw=json.dumps([mask,u_mask,p,q],separators=(',',':'))
            digest.update((raw+'\n').encode())
            rec={'center_mask':mask,'u_mask':u_mask,'degrees':[len(p)-1,len(q)-1],
                 'polynomials_sha256':hashlib.sha256(raw.encode()).hexdigest()}
            if len(p)==1 and p[0]!=0:
                rec.update(status='constant_nonzero',constant=p[0]);success['constant_nonzero']+=1
            else:
                for ell in PRIMES:
                    if p[-1]%ell==0 or q[-1]%ell==0:continue
                    if mod_gcd(p,q,ell)==0:
                        rec.update(status='coprime_mod_prime',prime=ell,gcd_degree=0,
                                   leading_residues=[p[-1]%ell,q[-1]%ell]);success[str(ell)]+=1;break
                else:
                    rec.update(status='unresolved',f1=p,fu=q);unresolved+=1
            cert.write(json.dumps(rec,sort_keys=True)+'\n')
            if visited%2048==0:
                cert.flush();emit(event='checkpoint',visited=visited,unresolved=unresolved,elapsed_seconds=time.monotonic()-start)
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
    assert visited==expected
    result={'status':'complete finite construction; no independent reviews yet',
            'last_unit_index':jvalue,'patterns':len(masks),'refinements':visited,
            'resolved':sum(success.values()),'unresolved':unresolved,
            'resolution_histogram':dict(success),'polynomial_stream_sha256':digest.hexdigest(),
            'certificates_sha256':sha(HERE/(prefix+'-certificates.jsonl')),
            'elapsed_seconds':time.monotonic()-start}
    (HERE/(prefix+'-result.json')).write_text(json.dumps(result,indent=2)+'\n');emit(event='complete',**result)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--J',type=int,choices=(15,16),required=True);parser.add_argument('--child',action='store_true');args=parser.parse_args()
    if args.child:worker(args.J);return
    prefix=f'coordinator-three-witness-J{args.J}-v1'
    out,err,job=[HERE/(prefix+s) for s in ('-output.txt','-stderr.txt','-job.json')]
    cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--J',str(args.J),'--child']
    rec={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'timeout_seconds':30,'status':'launching','helpers_sha256':sha(HELPERS),'masks_sha256':sha(MASKS),'construction_only':True}
    start=time.monotonic()
    with out.open('w') as f,err.open('w') as e:
        proc=subprocess.Popen(cmd,stdout=f,stderr=e);rec.update(pid=proc.pid,status='running');job.write_text(json.dumps(rec,indent=2)+'\n');emit(**rec)
        try:proc.wait(timeout=30);rec['status']='completed' if proc.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:proc.kill();proc.wait();rec['status']='timeout; identified child reaped'
        rec.update(return_code=proc.returncode,elapsed_seconds=time.monotonic()-start)
    rec['sha256']={p.name:sha(p) for p in [Path(__file__),out,err,HERE/(prefix+'-result.json'),HERE/(prefix+'-certificates.jsonl')] if p.is_file()}
    job.write_text(json.dumps(rec,indent=2)+'\n');emit(**rec)

if __name__=='__main__':main()
