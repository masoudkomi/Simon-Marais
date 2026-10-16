#!/usr/bin/env python3
"""Run reviewer finite arithmetic in a supervised child with a hard timeout."""
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

here = Path(__file__).resolve().parent
script = here / "initial-review-1-check.py"
command = [sys.executable, "-u", str(script)]
timeout_seconds = 60
started = time.monotonic()
job_path = here / "initial-review-1-job.json"
job = {"status": "launching", "command": command, "cwd": os.getcwd(), "timeout_seconds": timeout_seconds,
       "started_utc": datetime.now(timezone.utc).isoformat(), "supervisor_pid": os.getpid(),
       "python": platform.python_version(), "child_script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
       "parameters": "Stored verbatim in initial-review-1-evidence.json parameters", "cleanup_policy": "target this child PID only"}
with (here / "initial-review-1-child.log").open("w") as log:
    child = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT)
    job.update(child_pid=child.pid, status="running")
    job_path.write_text(json.dumps(job, indent=2) + "\n")
    print(json.dumps({"child_pid": child.pid, "timeout_seconds": timeout_seconds}), flush=True)
    try:
        code = child.wait(timeout=timeout_seconds)
        job.update(status="complete" if code == 0 else "failed", return_code=code)
    except subprocess.TimeoutExpired:
        child.terminate()
        try:
            child.wait(timeout=3)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait(timeout=3)
        job.update(status="timeout", return_code=child.returncode, terminated_child_pid=child.pid)
job.update(finished_utc=datetime.now(timezone.utc).isoformat(), elapsed_seconds=round(time.monotonic()-started, 6))
job_path.write_text(json.dumps(job, indent=2) + "\n")
print(json.dumps(job, indent=2), flush=True)
sys.exit(0 if job["status"] == "complete" else 1)
