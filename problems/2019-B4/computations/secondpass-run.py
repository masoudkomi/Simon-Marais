#!/usr/bin/env python3
"""Run one recorded child with an explicit timeout and targeted cleanup."""
import argparse
import datetime
import json
import os
import signal
import subprocess
import sys
import time

p = argparse.ArgumentParser()
p.add_argument("--timeout", type=float, default=60)
p.add_argument("--record", required=True)
p.add_argument("--log", required=True)
p.add_argument("command", nargs=argparse.REMAINDER)
a = p.parse_args()
command = a.command[1:] if a.command[:1] == ["--"] else a.command
record = {"command": command, "timeout_seconds": a.timeout,
          "cwd": os.getcwd(), "started_utc": datetime.datetime.now(datetime.UTC).isoformat(),
          "runner_pid": os.getpid(), "status": "running"}
with open(a.log, "w") as log:
    child = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT,
                             start_new_session=True)
    record["child_pid"] = child.pid
    with open(a.record, "w") as f:
        json.dump(record, f, indent=2)
    print(json.dumps(record), flush=True)
    started = time.monotonic()
    try:
        code = child.wait(timeout=a.timeout)
        record.update(status="complete", returncode=code)
    except subprocess.TimeoutExpired:
        os.killpg(child.pid, signal.SIGTERM)
        try:
            child.wait(timeout=2)
        except subprocess.TimeoutExpired:
            os.killpg(child.pid, signal.SIGKILL)
            child.wait()
        record.update(status="timeout", returncode=child.returncode)
    record["elapsed_seconds"] = time.monotonic() - started
    record["finished_utc"] = datetime.datetime.now(datetime.UTC).isoformat()
with open(a.record, "w") as f:
    json.dump(record, f, indent=2)
    f.write("\n")
print(json.dumps(record), flush=True)
sys.exit(0 if record["status"] == "complete" and record["returncode"] == 0 else 1)
