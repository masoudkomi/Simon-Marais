#!/usr/bin/env python3
"""Candidate proof - unverified. Exact log inequalities for the Dallant lead.
No CAS or optimization solver; stdlib Fraction only. Default launches a
recorded child with 30s external timeout and incremental checkpoints.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import os

HERE=Path(__file__).resolve().parent
PREFIX='deep-literature-r2-concavity'

def encoded(x):
    return [x.numerator,x.denominator]

def log_interval(r,N=80):
    assert r>1
    z=(r-1)/(r+1)
    total=F(0);power=z
    for k in range(N):
        total+=2*power/F(2*k+1)
        power*=z*z
    error=2*power/(F(2*N+1)*(1-z*z))
    return total,total+error

def worker():
    start=time.monotonic()
    ratios={'ln2':F(2),'ln32over7':F(32,7),'ln79over58':F(79,58),
            'lnA':F(107648,43687),'ln3over2':F(3,2)}
    logs={}
    for name,r in ratios.items():
        low,high=log_interval(r)
        logs[name]=(low,high)
        print(json.dumps({'checkpoint':name,'terms':80,'lower_float':float(low),'upper_float':float(high)}),flush=True)
    l2,h2=logs['ln2'];l1,h1=logs['ln32over7'];ls,hs=logs['ln79over58'];la,ha=logs['lnA']
    a,b=F(21,100),F(29,50)
    phi_low=(a*l1+b*ls)/h2+b
    phi_high=(a*h1+b*hs)/l2+b
    c=F(7,32)+F(21,79)
    derivative_low=(la+c)/h2-2
    derivative_high=(ha+c)/l2-2
    quarter_high=1+logs['ln3over2'][1]/(2*l2)
    assert phi_high<F(64951,50000)
    assert derivative_low>0 and derivative_high<F(1,5000)
    assert quarter_high<F(1293,1000)
    assert F(64951,50000)+F(1,25)*F(1,5000)==F(324757,250000)
    result={'status':'candidate finite exact certificate; no independent audits',
      'pid':os.getpid(),'python':sys.version,'terms_per_log':80,
      'log_formula':'ln(r)=2 sum_(k>=0) z^(2k+1)/(2k+1), z=(r-1)/(r+1)',
      'tail_upper_bound':'2*z^(2N+1)/((2N+1)*(1-z^2))',
      'log_intervals':{name:{'argument':encoded(ratios[name]),'lower':encoded(lo),'upper':encoded(hi)} for name,(lo,hi) in logs.items()},
      'phi_at_21over100':{'lower':encoded(phi_low),'upper':encoded(phi_high),'upper_target':encoded(F(64951,50000))},
      'derivative_at_21over100':{'lower':encoded(derivative_low),'upper':encoded(derivative_high),'upper_target':encoded(F(1,5000))},
      'phi_at_quarter_upper':encoded(quarter_high),
      'objective_bound':encoded(F(324757,250000)),
      'candidate_limsup_bound':encoded(F(324757,500000)),
      'seconds':time.monotonic()-start}
    (HERE/(PREFIX+'-certificate.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'complete':True,'seconds':result['seconds'],
                     'phi_interval':[float(phi_low),float(phi_high)],
                     'derivative_interval':[float(derivative_low),float(derivative_high)],
                     'objective_bound':float(F(324757,250000)),
                     'candidate_limsup_bound':float(F(324757,500000))}),flush=True)

def main():
    if '--child' in sys.argv:
        worker();return
    command=[sys.executable,'-u',str(Path(__file__).resolve()),'--child']
    out,err,job=[HERE/(PREFIX+s) for s in ('-stdout.txt','-stderr.txt','-job.json')]
    start=time.monotonic()
    rec={'command':command,'cap_seconds':30,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'utc_started':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'status':'starting'}
    with out.open('wb') as f,err.open('wb') as e:
        child=subprocess.Popen(command,stdout=f,stderr=e)
        rec.update(pid=child.pid,status='running');job.write_text(json.dumps(rec,indent=2)+'\n')
        print(json.dumps(rec),flush=True)
        try:
            rc=child.wait(timeout=30);rec['timed_out']=False
        except subprocess.TimeoutExpired:
            child.kill();rc=child.wait();rec['timed_out']=True
        rec.update(exit_code=rc,status='reaped',elapsed_seconds=time.monotonic()-start)
    rec['output_hashes']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (out,err,HERE/(PREFIX+'-certificate.json')) if p.exists()}
    job.write_text(json.dumps(rec,indent=2)+'\n');print(json.dumps(rec),flush=True)
    sys.exit(0 if rc==0 and not rec['timed_out'] else 1)

if __name__=='__main__':
    main()
