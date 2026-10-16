#!/usr/bin/env python3
"""Run only R2's child with explicit deadline; keep PID/job/checkpoints."""

from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
script = HERE/"initial-review-2-check.py"
timeout_seconds = 90
job_path = HERE/"initial-review-2-job.json"
stdout_path = HERE/"initial-review-2-check.stdout"
job = {
    "started_utc": datetime.now(timezone.utc).isoformat(),
    "command": [sys.executable, "-u", str(script)],
    "cwd": str(ROOT),
    "timeout_seconds": timeout_seconds,
    "child_script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
    "parameters": "Fully specified in child script; deterministic seed 20201016",
    "dependencies": "Python standard library only; no native CAS",
}
started = time.monotonic()
with stdout_path.open("w") as stream:
    child = subprocess.Popen(job["command"], cwd=ROOT, stdout=stream,
                             stderr=subprocess.STDOUT)
    job["child_pid"] = child.pid
    job_path.write_text(json.dumps(job, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"child_pid": child.pid, "timeout_seconds": timeout_seconds,
                      "checkpoints": str(stdout_path)}), flush=True)
    try:
        child.wait(timeout=timeout_seconds)
        job["timed_out"] = False
    except subprocess.TimeoutExpired:
        # Target only this exact child; never kill all interpreter processes.
        child.kill()
        child.wait()
        job["timed_out"] = True
    job["returncode"] = child.returncode
job["finished_utc"] = datetime.now(timezone.utc).isoformat()
job["elapsed_seconds"] = time.monotonic()-started
job_path.write_text(json.dumps(job, indent=2, sort_keys=True)+"\n")
print(stdout_path.read_text(), end="")
print(json.dumps({"returncode": child.returncode, "timed_out": job["timed_out"]}), flush=True)
sys.exit(1 if job["timed_out"] or child.returncode else 0)
