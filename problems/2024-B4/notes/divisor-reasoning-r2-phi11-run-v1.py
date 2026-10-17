"""Bounded subprocess harness for the finite certificate, preserving its PID."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
PREFIX = "divisor-reasoning-r2-phi11-"
job_path = HERE / (PREFIX + "job-v1.json")
stdout_path = HERE / (PREFIX + "stdout-v1.txt")
stderr_path = HERE / (PREFIX + "stderr-v1.txt")
command = [sys.executable, "-u", str(HERE / (PREFIX + "check-v1.py"))]
timeout = 5.0
started = time.monotonic()
with stdout_path.open("x") as stdout, stderr_path.open("x") as stderr:
    child = subprocess.Popen(command, stdout=stdout, stderr=stderr)
    record = {
        "command": command,
        "child_pid": child.pid,
        "timeout_seconds": timeout,
        "started_at_utc": datetime.now(timezone.utc).isoformat(),
        "operation": "Check a fixed 15-state symbolic certificate; no index scan, search or CAS",
    }
    with job_path.open("x") as stream:
        json.dump(record, stream, indent=2)
        stream.write("\n")
    try:
        returncode = child.wait(timeout=timeout)
        record["status"] = "completed"
    except subprocess.TimeoutExpired:
        child.kill()
        returncode = child.wait(timeout=2)
        record["status"] = "timeout; only identified child killed"
    record["returncode"] = returncode
    record["elapsed_seconds"] = time.monotonic() - started
for name, path in (("stdout", stdout_path), ("stderr", stderr_path)):
    record[name] = {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
with job_path.open("w") as stream:
    json.dump(record, stream, indent=2)
    stream.write("\n")
print(json.dumps(record, indent=2))
print(stdout_path.read_text())
if returncode:
    print(stderr_path.read_text())
    raise SystemExit(returncode)
