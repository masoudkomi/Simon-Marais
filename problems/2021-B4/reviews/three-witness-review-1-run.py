#!/usr/bin/env python3
"""External timed supervisor for R1's separately identified standard-Python child."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import selectors
import subprocess
import sys
import time

p=argparse.ArgumentParser()
p.add_argument("--mode",required=True,choices=("masks","benchmark","full"))
p.add_argument("--timeout",required=True,type=float)
p.add_argument("--limit",type=int,default=8192)
a=p.parse_args()
prefix=Path(__file__).with_name("three-witness-review-1")
source=Path(str(prefix)+"-independent.py")
cmd=[sys.executable,"-u",str(source),"--mode",a.mode,"--limit",str(a.limit)]
job_path=Path(str(prefix)+"-"+a.mode+"-job.json")
job={"command":cmd,"cwd":os.getcwd(),"external_timeout_seconds":a.timeout,
     "started_at_utc":datetime.now(timezone.utc).isoformat(),
     "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
     "python":sys.version,"pid":None,"requested_model":"gpt-6.1-sol",
     "requested_reasoning_effort":"max","effective_settings_readback":None}
start=time.monotonic()
with open(str(prefix)+"-"+a.mode+"-stderr.txt","wb") as err, open(str(prefix)+"-"+a.mode+"-output.txt","w") as out:
    child=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=err,text=True,bufsize=1)
    job["pid"]=child.pid
    job_path.write_text(json.dumps(job,indent=2)+"\n")
    print(json.dumps({"event":"child_started","pid":child.pid,"timeout":a.timeout}),flush=True)
    selector=selectors.DefaultSelector()
    selector.register(child.stdout,selectors.EVENT_READ)
    timed_out=False
    while selector.get_map():
        if time.monotonic()-start>a.timeout and child.poll() is None:
            timed_out=True
            child.kill()
        for key,_ in selector.select(timeout=1):
            line=key.fileobj.readline()
            if not line:
                selector.unregister(key.fileobj)
            else:
                out.write(line)
                out.flush()
                print(line,end="",flush=True)
    code=child.wait()
job.update({"exit_code":code,"timed_out":timed_out,"elapsed_seconds":time.monotonic()-start,
            "child_reaped":True,"finished_at_utc":datetime.now(timezone.utc).isoformat()})
job_path.write_text(json.dumps(job,indent=2)+"\n")
print(json.dumps({"event":"child_reaped",**job}),flush=True)
sys.exit(124 if timed_out else code)
