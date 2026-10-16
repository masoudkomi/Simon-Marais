#!/usr/bin/env python3
"""Bounded dedicated-child audit runner; kills only its identified child."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "criterion-review-2-check.py"
RUN = HERE / "criterion-review-2-run.json"
STDOUT = HERE / "criterion-review-2-stdout.txt"
STDERR = HERE / "criterion-review-2-stderr.txt"
TIMEOUT_SECONDS = 45
COMMAND = [sys.executable, "-u", str(SCRIPT)]
start = time.monotonic()

with STDOUT.open("w") as out, STDERR.open("w") as err:
    child = subprocess.Popen(COMMAND, stdout=out, stderr=err, cwd=HERE.parents[2])
    data = {"command": COMMAND, "child_pid": child.pid, "timeout_seconds": TIMEOUT_SECONDS,
            "started_utc": datetime.now(timezone.utc).isoformat(), "status": "running",
            "script_sha256": hashlib.sha256(SCRIPT.read_bytes()).hexdigest(),
            "stdout": str(STDOUT), "stderr": str(STDERR),
            "parameters": {"internal_limit_seconds": 35, "orbit_state_cap": 256, "recurrence_max_j": 65535}}
    RUN.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(f"child_pid={child.pid}; explicit timeout={TIMEOUT_SECONDS}s", flush=True)
    try:
        code = child.wait(timeout=TIMEOUT_SECONDS)
        data.update(status="completed" if code == 0 else "failed", returncode=code)
    except subprocess.TimeoutExpired:
        child.kill()
        data.update(status="timeout; identified child killed", returncode=child.wait())
    data["elapsed_seconds"] = time.monotonic() - start
    data["completed_utc"] = datetime.now(timezone.utc).isoformat()

data["stdout_sha256"] = hashlib.sha256(STDOUT.read_bytes()).hexdigest()
data["stderr_sha256"] = hashlib.sha256(STDERR.read_bytes()).hexdigest()
RUN.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
print(json.dumps(data, sort_keys=True), flush=True)
raise SystemExit(0 if data["status"] == "completed" else 1)
