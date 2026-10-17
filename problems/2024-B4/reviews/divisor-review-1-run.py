"""Externally time-limit and reap only this review's finite checker."""
from pathlib import Path
import datetime
import json
import platform
import subprocess
import sys
import time

base = Path(__file__).with_name("divisor-review-1")
checker = Path(str(base) + "-check.py")
timeout_seconds = 10
command = [sys.executable, str(checker)]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
clock_start = time.monotonic()
with Path(str(base) + "-stdout.txt").open("x") as stdout, \
        Path(str(base) + "-stderr.txt").open("x") as stderr:
    child = subprocess.Popen(command, stdout=stdout, stderr=stderr)
    start_record = {"started_at_utc": started, "child_pid": child.pid,
                    "timeout_seconds": timeout_seconds, "command": command,
                    "python": platform.python_version()}
    with Path(str(base) + "-job-start.json").open("x") as stream:
        json.dump(start_record, stream, indent=2)
        stream.write("\n")
    print(json.dumps(start_record), flush=True)
    timed_out = False
    try:
        code = child.wait(timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        timed_out = True
        child.kill()
        code = child.wait()
    elapsed = time.monotonic() - clock_start
done = {**start_record, "completed_at_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "returncode": code, "timed_out": timed_out,
        "elapsed_seconds": elapsed, "child_reaped": child.poll() is not None,
        "targeted_cleanup_only": True}
with Path(str(base) + "-job.json").open("x") as stream:
    json.dump(done, stream, indent=2)
    stream.write("\n")
print(json.dumps(done), flush=True)
if timed_out or code:
    raise SystemExit(1)
