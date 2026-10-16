#!/usr/bin/env python3
"""External wall-clock cap with child PID and flushed output checkpoints."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ap = argparse.ArgumentParser()
ap.add_argument("--timeout", type=float, required=True)
ap.add_argument("--prefix", required=True)
ap.add_argument("command", nargs=argparse.REMAINDER)
args = ap.parse_args()
prefix = Path(args.prefix)
started = time.monotonic()
job = {"command":args.command, "timeout_seconds":args.timeout,
       "status":"running", "runner_pid":__import__("os").getpid()}
for name in args.command:
    path = Path(name)
    if path.is_file() and path.suffix == ".py":
        job.setdefault("source_sha256", {})[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
with open(str(prefix)+"-stdout.txt", "w") as out, open(str(prefix)+"-stderr.txt", "w") as err:
    child = subprocess.Popen(args.command, stdout=out, stderr=err)
    job["child_pid"] = child.pid
    Path(str(prefix)+"-job.json").write_text(json.dumps(job, indent=2)+"\n")
    print(json.dumps(job), flush=True)
    try:
        code = child.wait(timeout=args.timeout)
        job.update(status="finished", exit_code=code, timed_out=False, reaped=True)
    except subprocess.TimeoutExpired:
        child.terminate()
        try:
            child.wait(timeout=5)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait()
        job.update(status="timed_out", exit_code=child.returncode, timed_out=True, reaped=True)
job["seconds"] = round(time.monotonic()-started, 3)
for kind in ("stdout", "stderr"):
    p = Path(str(prefix)+"-"+kind+".txt")
    job[kind+"_sha256"] = hashlib.sha256(p.read_bytes()).hexdigest()
Path(str(prefix)+"-job.json").write_text(json.dumps(job, indent=2)+"\n")
print(json.dumps(job), flush=True)
sys.exit(0 if job.get("exit_code") == 0 else 1)
