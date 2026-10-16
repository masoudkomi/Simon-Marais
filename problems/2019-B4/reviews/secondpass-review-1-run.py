"""Dedicated, hard-bounded child runner; never signals unrelated processes."""
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

prefix = Path("problems/2019-B4/reviews/secondpass-review-1")
cmd = [str(Path(".venv/bin/python").absolute()), "-u", str(prefix) + "-check.py"]
job = {"command": cmd, "timeout_seconds": 60, "started_utc": datetime.now(timezone.utc).isoformat(), "status": "starting"}
start = time.monotonic()
with open(str(prefix) + "-check.log", "w") as out:
    proc = subprocess.Popen(cmd, stdout=out, stderr=subprocess.STDOUT)
    job.update(pid=proc.pid, status="running")
    Path(str(prefix) + "-job.json").write_text(json.dumps(job, indent=2) + "\n")
    print("child pid", proc.pid, "timeout 60s", flush=True)
    try:
        proc.wait(timeout=60)
        job.update(status="completed" if proc.returncode == 0 else "failed", exit_code=proc.returncode)
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
        job.update(status="timeout; only this child was killed", exit_code=proc.returncode)
    job["elapsed_seconds"] = time.monotonic() - start
    Path(str(prefix) + "-job.json").write_text(json.dumps(job, indent=2) + "\n")
print(json.dumps(job), flush=True)
