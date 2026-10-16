#!/usr/bin/env python3
"""External subprocess deadline and PID log for independent R2 jobs."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

base = Path(__file__).resolve().with_name("three-witness-review-2")
mode = sys.argv[1]
cap = int(sys.argv[2])
script = str(base) + "-independent.py"
cmd = [sys.executable, "-u", script, mode, *sys.argv[3:]]
output = str(base) + "-" + mode + "-output.txt"
stderr = str(base) + "-" + mode + "-stderr.txt"
jobpath = str(base) + "-" + mode + "-job.json"
start = time.monotonic()
job = {"command": cmd, "timeout_seconds": cap, "utc_start": datetime.datetime.now(datetime.timezone.utc).isoformat(),
       "requested_model":"gpt-6.1-sol", "requested_effort":"max", "effective_readback":"unavailable",
       "python": sys.version, "script_sha256": hashlib.sha256(Path(script).read_bytes()).hexdigest(),
       "stdout":output,"stderr":stderr}
with open(output,"w") as out, open(stderr,"w") as err:
    child = subprocess.Popen(cmd, stdout=out, stderr=err)
    job["pid"] = child.pid
    Path(jobpath).write_text(json.dumps(job,indent=2)+"\n")
    print(json.dumps({"event":"start","pid":child.pid,"mode":mode,"cap":cap}),flush=True)
    try:
        status = child.wait(timeout=cap)
        job["exit_code"] = status
        job["timed_out"] = False
    except subprocess.TimeoutExpired:
        child.terminate()
        try:
            child.wait(timeout=3)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait(timeout=3)
        job["exit_code"] = child.returncode
        job["timed_out"] = True
job["seconds"] = time.monotonic() - start
job["utc_finished"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
Path(jobpath).write_text(json.dumps(job,indent=2)+"\n")
print(json.dumps({"event":"finished",**job}),flush=True)
sys.exit(124 if job["timed_out"] else job["exit_code"])
