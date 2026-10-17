"""External timeout/PID harness for this reviewer's fixed certificate only."""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
from datetime import datetime, timezone


here = Path(__file__).resolve().parent
prefix = "divisor-review-2-"
command = [sys.executable, "-u", str(here / (prefix + "certificate-v1.py"))]
timeout_seconds = 5
started = time.monotonic()
stdout_path = here / (prefix + "stdout-v1.txt")
stderr_path = here / (prefix + "stderr-v1.txt")
with stdout_path.open("x") as stdout_file, stderr_path.open("x") as stderr_file:
    child = subprocess.Popen(command, stdout=stdout_file, stderr=stderr_file)
    start_record = {
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "child_pid": child.pid, "command": command,
        "timeout_seconds": timeout_seconds,
        "scope": "only the fixed 15-state, 48-column, 30-edge certificate",
    }
    with (here / (prefix + "job-v1.json")).open("x") as stream:
        json.dump(start_record, stream, indent=2)
        stream.write("\n")
    try:
        code = child.wait(timeout=timeout_seconds)
        status = "completed and reaped"
    except subprocess.TimeoutExpired:
        child.kill()
        code = child.wait(timeout=2)
        status = "timeout; identified child alone killed and reaped"
completion = {
    **start_record,
    "status": status, "returncode": code,
    "elapsed_seconds": time.monotonic() - started,
    "completed_at_utc": datetime.now(timezone.utc).isoformat(),
    "stdout": {"path": str(stdout_path), "sha256": hashlib.sha256(stdout_path.read_bytes()).hexdigest()},
    "stderr": {"path": str(stderr_path), "sha256": hashlib.sha256(stderr_path.read_bytes()).hexdigest()},
}
with (here / (prefix + "completion-v1.json")).open("x") as stream:
    json.dump(completion, stream, indent=2)
    stream.write("\n")
print(json.dumps(completion, indent=2))
print(stdout_path.read_text())
if code:
    print(stderr_path.read_text())
    raise SystemExit(code)
