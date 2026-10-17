"""Externally cap the one identified target child, checkpoint PID and reap it."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

B = Path(__file__).resolve().parent
P = "reasoning-return-r3-kasami-target-"
command = [sys.executable, "-u", str(B / (P + "check-v1.py"))]
timeout = 10
started = time.monotonic()
out_path = B / (P + "stdout-v1.txt")
err_path = B / (P + "stderr-v1.txt")
with out_path.open("x") as out, err_path.open("x") as err:
    child = subprocess.Popen(command, stdout=out, stderr=err)
    job = {"started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "child_pid": child.pid, "command": command, "timeout_seconds": timeout,
           "scope": "q8,d57,n3641 composition conjecture only", "parent_pid": os.getpid()}
    with (B / (P + "job-v1.json")).open("x") as f:
        json.dump(job, f, indent=2)
        f.write("\n")
    print(json.dumps(job), flush=True)
    timed_out = False
    try:
        return_code = child.wait(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        child.kill()
        return_code = child.wait()
result = {"completed_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
          "child_pid": child.pid, "return_code": return_code,
          "timed_out": timed_out, "child_reaped": True,
          "elapsed_seconds": time.monotonic()-started,
          "stdout_sha256": hashlib.sha256(out_path.read_bytes()).hexdigest(),
          "stderr_sha256": hashlib.sha256(err_path.read_bytes()).hexdigest()}
with (B / (P + "completion-v1.json")).open("x") as f:
    json.dump(result, f, indent=2)
    f.write("\n")
print(json.dumps(result), flush=True)
print(out_path.read_text(), end="")
print(err_path.read_text(), end="", file=sys.stderr)
assert return_code == 0 and not timed_out
