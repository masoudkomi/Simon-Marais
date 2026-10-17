"""External10-second timeout/PID/checkpoint/reap for one fixed sign child."""
from pathlib import Path
from datetime import datetime, timezone
import subprocess
import time
import sys
import json

root = Path(__file__).resolve().parents[3]
prefix = "problems/2019-B4/reviews/coordinator-cap-gap-r1-review-2-"
suffixes = ("sign-output-v1.json", "sign-stderr-v1.txt",
            "sign-start-v1.json", "sign-completion-v1.json")
assert all(not (root/(prefix+s)).exists() for s in suffixes)
command = [sys.executable, str(root/(prefix+"sign-v1.py"))]
started = datetime.now(timezone.utc).isoformat()
clock = time.monotonic()
with (root/(prefix+suffixes[0])).open("x") as out, (root/(prefix+suffixes[1])).open("x") as err:
    child = subprocess.Popen(command, cwd=root, stdout=out, stderr=err)
    checkpoint = {"command":command, "pid":child.pid, "started_at_utc":started,
        "external_timeout_seconds":10, "scope":"ONE independent homogeneous-integer fixed sign",
        "old_program_or_constructor_script_execution":False}
    with (root/(prefix+suffixes[2])).open("x") as stream:
        json.dump(checkpoint,stream,indent=2);stream.write("\n")
    timed_out = False
    try:
        code = child.wait(timeout=10)
    except subprocess.TimeoutExpired:
        timed_out = True
        child.kill()
        code = child.wait(timeout=5)
completed = {**checkpoint, "completed_at_utc":datetime.now(timezone.utc).isoformat(),
    "elapsed_seconds":time.monotonic()-clock, "exit_code":code,
    "timed_out":timed_out, "reaped":True}
with (root/(prefix+suffixes[3])).open("x") as stream:
    json.dump(completed,stream,indent=2);stream.write("\n")
print(json.dumps(completed))
if code or timed_out:
    raise SystemExit("Fixed sign child did not complete successfully")
