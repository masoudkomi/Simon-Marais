"""One-time externally timed runner for the independent finite certificate."""
from pathlib import Path
from datetime import datetime, timezone
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/moment-tail-review-1-"
command = [sys.executable, PREFIX + "certificate-v1.py"]
start = datetime.now(timezone.utc).isoformat()
t0 = time.monotonic()
out = (ROOT / (PREFIX + "certificate-output-v1.json")).open("x")
err = (ROOT / (PREFIX + "certificate-stderr-v1.txt")).open("x")
child = subprocess.Popen(command, cwd=ROOT, stdout=out, stderr=err)
with (ROOT / (PREFIX + "job-start-v1.json")).open("x") as stream:
    json.dump({"started_at_utc": start, "pid": child.pid,
               "command": command, "external_timeout_seconds": 10}, stream, indent=2)
    stream.write("\n")
timed_out = False
try:
    status = child.wait(timeout=10)
except subprocess.TimeoutExpired:
    timed_out = True
    child.kill()
    status = child.wait()
finally:
    out.close()
    err.close()
result = {"started_at_utc": start,
          "completed_at_utc": datetime.now(timezone.utc).isoformat(),
          "pid": child.pid, "command": command,
          "external_timeout_seconds": 10, "timed_out": timed_out,
          "exit_code": status, "elapsed_seconds": time.monotonic()-t0,
          "child_reaped": True,
          "mathematical_scope": "one rational sign certificate; no history enumeration"}
with (ROOT / (PREFIX + "job-v1.json")).open("x") as stream:
    json.dump(result, stream, indent=2)
    stream.write("\n")
print(json.dumps(result, indent=2))
assert not timed_out and status == 0
