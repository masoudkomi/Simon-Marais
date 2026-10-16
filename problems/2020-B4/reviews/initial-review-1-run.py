#!/usr/bin/env python3
"""Hard child timeout and incremental retained output for R1 exact checks."""
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import subprocess
import sys
import threading
import time

here=Path(__file__).resolve().parent
command=[sys.executable,'-u',str(here/'initial-review-1-check.py')]
timeout_seconds=90
started=time.monotonic()
job={'started_utc':datetime.now(timezone.utc).isoformat(),'supervisor_pid':os.getpid(),
     'command':command,'timeout_seconds':timeout_seconds,
     'stdout_path':str(here/'initial-review-1-check.stdout'),
     'scope':'2020 B4(b), independent finite checks, standard library only'}
proc=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,
                      text=True,bufsize=1,start_new_session=True)
job['child_pid']=proc.pid
job['status']='running'
path=here/'initial-review-1-job.json'
path.write_text(json.dumps(job,indent=2,sort_keys=True)+'\n')
print('CHILD_PID='+str(proc.pid)+' TIMEOUT_SECONDS='+str(timeout_seconds),flush=True)
def stream():
    with (here/'initial-review-1-check.stdout').open('w') as out:
        for line in proc.stdout:
            out.write(line)
            out.flush()
            print(line,end='',flush=True)
t=threading.Thread(target=stream,daemon=True)
t.start()
try:
    code=proc.wait(timeout=timeout_seconds)
    job['status']='completed' if code==0 else 'failed'
except subprocess.TimeoutExpired:
    job['status']='timeout'
    proc.terminate()
    try:
        code=proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        code=proc.wait(timeout=5)
t.join(timeout=5)
job['exit_code']=code
job['elapsed_seconds']=round(time.monotonic()-started,6)
job['completed_utc']=datetime.now(timezone.utc).isoformat()
path.write_text(json.dumps(job,indent=2,sort_keys=True)+'\n')
print(json.dumps(job,sort_keys=True),flush=True)
sys.exit(code if job['status']!='timeout' else 124)
