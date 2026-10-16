#!/usr/bin/env python3
"""Resolve only the explicit remaining exact pairs, without overwriting raw runs."""
from pathlib import Path
import datetime,hashlib,importlib.util,json,subprocess,sys,time

HERE=Path(__file__).resolve().parent
PREFIX='coordinator-three-witness-v2-resolve'
SOURCE=HERE/'coordinator-three-witness-v2-unresolved.jsonl'
HELPERS=HERE/'padic-rational-j17-compatibility.py'
PRIMES=(131,137,139,149,151,157,163,167,173,179)

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def child():
    spec=importlib.util.spec_from_file_location('frozen_helpers',HELPERS)
    module=importlib.util.module_from_spec(spec);sys.dont_write_bytecode=True;spec.loader.exec_module(module)
    records=[json.loads(line) for line in SOURCE.read_text().splitlines()]
    answers=[]
    for r in records:
        p,q=r['P'],r['Q'];answer={'center_mask':r['center_mask'],'u_mask':r['u_mask'],
          'raw_record_sha256':hashlib.sha256(json.dumps(r,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
          'degrees':[len(p)-1,len(q)-1]}
        trials=[]
        for ell in PRIMES:
            assert all(ell%d for d in range(2,int(ell**0.5)+1))
            if not p[-1]%ell or not q[-1]%ell:
                trials.append({'prime':ell,'status':'degree loss; not used'});continue
            deg=module.mod_gcd(p,q,ell);trials.append({'prime':ell,'gcd_degree':deg})
            if deg==0:
                answer.update(status='coprime_mod_prime',prime=ell,gcd_degree=0,leading_residues=[p[-1]%ell,q[-1]%ell]);break
        else:answer['status']='unresolved'
        answer['trials']=trials;answers.append(answer)
    result={'status':'targeted finite construction, independent audits pending','source_sha256':sha(SOURCE),
            'helpers_sha256':sha(HELPERS),'cases':answers,'resolved':sum(r['status']=='coprime_mod_prime' for r in answers),
            'unresolved':sum(r['status']!='coprime_mod_prime' for r in answers)}
    (HERE/(PREFIX+'-result.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)

def main():
    if '--child' in sys.argv:child();return
    out,err,job=[HERE/(PREFIX+s) for s in ('-output.txt','-stderr.txt','-job.json')]
    cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--child']
    rec={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'timeout_seconds':20,'status':'launching'}
    start=time.monotonic()
    with out.open('w') as f,err.open('w') as e:
        proc=subprocess.Popen(cmd,stdout=f,stderr=e);rec.update(pid=proc.pid,status='running');job.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
        try:proc.wait(timeout=20);rec['status']='completed' if proc.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:proc.kill();proc.wait();rec['status']='timeout; identified child reaped'
        rec.update(return_code=proc.returncode,elapsed_seconds=time.monotonic()-start)
    rec['sha256']={p.name:sha(p) for p in [Path(__file__),out,err,HERE/(PREFIX+'-result.json')] if p.is_file()}
    job.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)

if __name__=='__main__':main()
