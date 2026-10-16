#!/usr/bin/env python3
"""Exploratory extension and bubble-multiplicity check, not an independent audit."""
from pathlib import Path
import datetime,hashlib,json,subprocess,sys,time,os
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
PREFIX='coordinator-ambiguity-probe-v1'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def count_paths(u,v):
    dp=[[0]*(len(v)+1) for _ in range(len(u)+1)];dp[0][0]=1
    for i in range(len(u)+1):
        for j in range(len(v)+1):
            bit=str((i+j)%2)
            if i<len(u) and u[i]==bit:dp[i+1][j]+=dp[i][j]
            if j<len(v) and v[j]==bit:dp[i][j+1]+=dp[i][j]
    return dp[-1][-1]
def analyze():
    raw=json.loads((HERE/(PREFIX+'-extension.json')).read_text())
    rows=[]
    for item in raw['all_minimal_forbidden_in_complete_layers']:
        u,v=item['tapes'];rows.append({'word':item['larger'],'length':len(item['larger']),'histories':count_paths(u,v)})
    result={'status':'finite exploratory evidence only; author enumerator reused, not independent review','fully_completed_through':raw['completed_through'],'extension_rows':raw['rows'],'multiplicities':rows,'non_two_history_cases':[x for x in rows if x['histories']!=2],'compression_counterexamples':raw['compression_counterexamples']}
    (HERE/(PREFIX+'-multiplicities.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['fully_completed_through','extension_rows','non_two_history_cases','compression_counterexamples']}),flush=True)
def main():
    source=HERE/'secondpass-full-obstruction24-v2.json';old=json.loads(source.read_text())
    cache=ROOT/'.cache/research-seeds';cache.mkdir(parents=True,exist_ok=True)
    seed=cache/'2019-complete-through24.json'
    seed.write_text(json.dumps({'rows':[{'moves':old['completed_through']}],'minimal_forbidden':old['all_minimal_forbidden_in_complete_layers']})+'\n')
    out=HERE/(PREFIX+'-output.txt');err=HERE/(PREFIX+'-stderr.txt');job=HERE/(PREFIX+'-job.json')
    target=HERE/(PREFIX+'-extension.json')
    cmd=[sys.executable,'-u',str(HERE/'secondpass-full-obstruction-probe.py'),'--initial-probe',str(seed),'--max-n','28','--state-cap','2000000','--output',str(target)]
    record={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'timeout_seconds':35,'status':'launching','source_frozen_sha256':sha(source),'enumerator_sha256':sha(HERE/'secondpass-full-obstruction-probe.py'),'seed_sha256':sha(seed),'source_code_reused':'author targeted enumeration; no independent-review credit'}
    start=time.monotonic()
    with out.open('w') as f,err.open('w') as e:
        child=subprocess.Popen(cmd,stdout=f,stderr=e);record.update(pid=child.pid,status='running');job.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True)
        try:child.wait(timeout=35);record['status']='completed' if child.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:child.kill();child.wait();record['status']='external timeout; identified child reaped'
        record.update(return_code=child.returncode,elapsed_seconds=time.monotonic()-start)
    if child.returncode==0:analyze()
    record['sha256']={p.name:sha(p) for p in [Path(__file__),out,err,target,HERE/(PREFIX+'-multiplicities.json')] if p.is_file()}
    job.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True)
if __name__=='__main__':main()
