"""Run the bounded exact residue probe with external timeout and PID records."""
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import sys
import time

prefix = Path(__file__).with_name("coordinator-odd-support-v1")
target = Path(__file__).with_name("coordinator-odd-support-counterexample-v1.py")
started = time.monotonic()
with Path(str(prefix)+"-stdout.txt").open("x") as stdout, \
        Path(str(prefix)+"-stderr.txt").open("x") as stderr:
    child = subprocess.Popen([sys.executable, str(target)], stdout=stdout, stderr=stderr)
    start = {"started_at_utc": datetime.now(timezone.utc).isoformat(),
             "child_pid": child.pid, "command": [sys.executable, str(target)],
             "external_timeout_seconds": 10, "scope": "64 odd-support counterexample probe"}
    with Path(str(prefix)+"-job-start.json").open("x") as stream:
        json.dump(start, stream, indent=2)
        stream.write("\n")
    timed_out = False
    try:
        code = child.wait(timeout=10)
    except subprocess.TimeoutExpired:
        timed_out = True
        child.kill()
        code = child.wait()
    result = {**start, "completed_at_utc": datetime.now(timezone.utc).isoformat(),
              "elapsed_seconds": time.monotonic()-started, "exit_code": code,
              "timed_out": timed_out, "reaped": True}
    with Path(str(prefix)+"-job.json").open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
print(json.dumps(result, indent=2))
raise SystemExit(code)
