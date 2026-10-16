#!/usr/bin/env python3
"""External timeout/reaping supervisor; only the recorded child is killed."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

here=Path(__file__).resolve().parent
prefix=here/'J16-digits-review-2'
script=Path(sys.argv[1]).resolve()
mode=sys.argv[2]
cap=float(sys.argv[3])
args=sys.argv[4:]
assert 0<cap<=300
command=[sys.executable,'-u',str(script)]+args
outpath=Path(str(prefix)+'-'+mode+'-stdout.txt')
errpath=Path(str(prefix)+'-'+mode+'-stderr.txt')
jobpath=Path(str(prefix)+'-'+mode+'-job.json')
start=time.monotonic()
job={'command':command,'cap_seconds':cap,'script_sha256':hashlib.sha256(script.read_bytes()).hexdigest(),
     'utc_started':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),'status':'starting'}
with outpath.open('wb') as out,errpath.open('wb') as err:
    child=subprocess.Popen(command,stdout=out,stderr=err)
    job.update({'pid':child.pid,'status':'running'})
    jobpath.write_text(json.dumps(job,indent=2)+'\n')
    print(json.dumps(job),flush=True)
    try:
        rc=child.wait(timeout=cap)
        job['timed_out']=False
    except subprocess.TimeoutExpired:
        child.kill()
        rc=child.wait()
        job['timed_out']=True
    job.update({'exit_code':rc,'elapsed_seconds':time.monotonic()-start,'status':'reaped',
                'utc_finished':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())})
job['stdout_sha256']=hashlib.sha256(outpath.read_bytes()).hexdigest()
job['stderr_sha256']=hashlib.sha256(errpath.read_bytes()).hexdigest()
jobpath.write_text(json.dumps(job,indent=2)+'\n')
print(json.dumps(job),flush=True)
sys.exit(0 if rc==0 and not job['timed_out'] else 1)
