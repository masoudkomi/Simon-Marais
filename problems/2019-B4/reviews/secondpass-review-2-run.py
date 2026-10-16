#!/usr/bin/env python3
"""Bounded dedicated R2 child runner; no global process cleanup."""
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

p = argparse.ArgumentParser()
p.add_argument("name")
p.add_argument("mode")
p.add_argument("--maximum", type=int, default=24)
p.add_argument("--enumeration")
p.add_argument("--bounded-runs", action="store_true")
p.add_argument("--timeout", type=int, default=60)
a = p.parse_args()
root = Path(__file__).resolve().parent
base = root / ("secondpass-review-2-" + a.name)
cmd = [sys.executable, "-u", str(root / "secondpass-review-2-check.py"), a.mode,
       str(base.with_suffix(".json")), "--maximum", str(a.maximum)]
if a.enumeration:
    cmd += ["--enumeration", a.enumeration]
if a.bounded_runs:
    cmd += ["--bounded-runs"]
metadata = {"started_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "command": cmd, "timeout_seconds": a.timeout, "runner_pid": os.getpid(),
            "cwd": str(Path.cwd()),
            "check_script_sha256": hashlib.sha256((root / "secondpass-review-2-check.py").read_bytes()).hexdigest(),
            "runner_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
log = base.with_suffix(".log")
job = base.with_name(base.name + "-job.json")
started = time.monotonic()
with log.open("w") as stream:
    child = subprocess.Popen(cmd, stdout=stream, stderr=subprocess.STDOUT)
    metadata["child_pid"] = child.pid
    job.write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps({"started_pid": child.pid, "job": str(job), "log": str(log)}), flush=True)
    try:
        metadata["return_code"] = child.wait(timeout=a.timeout)
        metadata["status"] = "complete" if child.returncode == 0 else "failed"
    except subprocess.TimeoutExpired:
        child.kill()
        child.wait()
        metadata["return_code"] = child.returncode
        metadata["status"] = "timeout; dedicated child killed"
metadata["elapsed_seconds"] = time.monotonic() - started
metadata["ended_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
job.write_text(json.dumps(metadata, indent=2) + "\n")
print(json.dumps(metadata), flush=True)
sys.exit(0 if metadata["status"] == "complete" else 1)
