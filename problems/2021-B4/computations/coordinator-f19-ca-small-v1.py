#!/usr/bin/env python3
"""Exploratory exact F19-rational-witness CA search, not independent review."""
from pathlib import Path
from itertools import product
from math import comb
from collections import Counter
import datetime,hashlib,json,subprocess,sys,time

HERE=Path(__file__).resolve().parent
PREFIX='coordinator-f19-ca-small-v1'

def child():
    p=19
    results=[]
    for d in (6,7):
        powers=[[pow(x,t,p) for t in range(d+1)] for x in range(p)]
        binoms=[[comb(t,k)%p for t in range(d+1)] for k in range(d)]
        for center in (0,1):
            tested=0;examples=[];count=0;digest=hashlib.sha256()
            for row in product(range(p),repeat=d-3-center):
                c=[0]*(d+1);c[d]=1;c[d-1]=(-d*center)%p
                if center:
                    c[3:d-1]=row
                    c[2]=-sum(c[3:])%p
                else:
                    c[2:d-1]=row
                tested+=1
                if all(v==0 for v in c[2:d]):
                    continue
                roots=[x for x in range(p) if sum(c[t]*powers[x][t] for t in range(2,d+1))%p==0]
                witnesses={1:0,d-1:center}
                valid=True
                for k in range(2,d-1):
                    ws=[x for x in roots if sum(binoms[k][t]*c[t]*powers[x][t-k] for t in range(k,d+1))%p==0]
                    if not ws:valid=False;break
                    witnesses[k]=ws[0]
                if valid:
                    count+=1
                    rec={'coefficients_ascending':c,'rational_roots':roots,'witness_by_order':witnesses}
                    digest.update((json.dumps(rec,sort_keys=True,separators=(',',':'))+'\n').encode())
                    if len(examples)<20:examples.append(rec)
                if tested%20000==0:
                    print(json.dumps({'degree':d,'center':center,'tested':tested,'found':count}),flush=True)
            result={'degree':d,'center':center,'p':p,'tested_normalized_polynomials':tested,'nontrivial_F19_rational_witness_CA_count':count,'complete_solution_stream_sha256':digest.hexdigest(),'first_twenty_examples':examples}
            results.append(result)
            print(json.dumps(result),flush=True)
    (HERE/(PREFIX+'-result.json')).write_text(json.dumps({'status':'finite exploratory evidence only; no unrestricted proof or review credit','results':results},indent=2)+'\n')

def main():
    if '--child' in sys.argv:child();return
    out,err,job=[HERE/(PREFIX+s) for s in ('-output.txt','-stderr.txt','-job.json')]
    cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--child']
    rec={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'timeout_seconds':35,'status':'launching'}
    start=time.monotonic()
    with out.open('w') as f,err.open('w') as e:
        proc=subprocess.Popen(cmd,stdout=f,stderr=e);rec.update(pid=proc.pid,status='running');job.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
        try:proc.wait(timeout=35);rec['status']='completed' if proc.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:proc.kill();proc.wait();rec['status']='timeout; identified child reaped'
        rec.update(return_code=proc.returncode,elapsed_seconds=time.monotonic()-start)
    rec['sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),out,err,HERE/(PREFIX+'-result.json')] if p.is_file()}
    job.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)

if __name__=='__main__':main()
