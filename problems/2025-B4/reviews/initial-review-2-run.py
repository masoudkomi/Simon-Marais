#!/usr/bin/env python3
"""Dedicated child process with explicit wall timeout and persisted incremental logs."""
import json
from pathlib import Path
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
script = BASE / "initial-review-2-checks.py"
job = BASE / "initial-review-2-job.json"
log = BASE / "initial-review-2-run.log"
timeout_seconds = 45
started = time.time()
with log.open("w") as stream:
    child = subprocess.Popen([sys.executable, "-u", str(script)], stdout=stream,
                             stderr=subprocess.STDOUT)
    metadata = {"command": [sys.executable, "-u", str(script)], "pid": child.pid,
                "timeout_seconds": timeout_seconds, "started_unix": started,
                "output_log": str(log), "cleanup_scope": "this child PID only"}
    job.write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps(metadata), flush=True)
    try:
        exit_code = child.wait(timeout=timeout_seconds)
        metadata["timed_out"] = False
    except subprocess.TimeoutExpired:
        metadata["timed_out"] = True
        child.terminate()
        try:
            child.wait(timeout=3)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait()
        exit_code = child.returncode
    metadata["exit_code"] = exit_code
    metadata["elapsed_seconds"] = time.time() - started
    job.write_text(json.dumps(metadata, indent=2) + "\n")
print(log.read_text(), end="", flush=True)
raise SystemExit(exit_code or 0)
