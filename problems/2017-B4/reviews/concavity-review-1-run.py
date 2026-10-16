#!/usr/bin/env python3
"""External 30-second supervisor with a recorded dedicated PID and reaping."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

here=Path(__file__).resolve().parent
prefix=here / "concavity-review-1"
script=here / "concavity-review-1-check.py"
job=here / "concavity-review-1-job.json"
stdout=here / "concavity-review-1-stdout.log"
stderr=here / "concavity-review-1-stderr.log"
cmd=[sys.executable,"-B","-u",str(script)]
record={"command":cmd,"timeout_seconds":30,"cwd":str(here.parents[2]),
        "check_script_sha256":hashlib.sha256(script.read_bytes()).hexdigest(),
        "started_utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "parameters":{"log_terms":96,"u_intervals":400,"a_intervals":200}}
env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1")
t0=time.monotonic()
with stdout.open("w") as out,stderr.open("w") as err:
    child=subprocess.Popen(cmd,cwd=here.parents[2],env=env,stdout=out,stderr=err)
    record["child_pid"]=child.pid
    job.write_text(json.dumps(record,indent=2)+"\n")
    try:
        record["exit_code"]=child.wait(timeout=30)
        record["timed_out"]=False
    except subprocess.TimeoutExpired:
        child.terminate()
        try:
            child.wait(timeout=2)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait()
        record["exit_code"]=child.returncode
        record["timed_out"]=True
    record["reaped"]=True
record["elapsed_seconds"]=time.monotonic()-t0
record["finished_utc"]=datetime.datetime.now(datetime.timezone.utc).isoformat()
job.write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record,indent=2),flush=True)
print(stdout.read_text(),end="",flush=True)
print(stderr.read_text(),end="",file=sys.stderr,flush=True)
sys.exit(record["exit_code"] or (124 if record["timed_out"] else 0))
