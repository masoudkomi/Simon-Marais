#!/usr/bin/env python3
"""Run R2's independent CAS checks with an explicit child timeout."""
import json
from pathlib import Path
import subprocess
import time

folder = Path(__file__).resolve().parent
root = folder.parents[2]
command = [str(root / ".venv/bin/python"), "-u", str(folder / "family-review-2-check.py")]
record = {"command": command, "cwd": str(root), "timeout_seconds": 30,
          "native_cleanup": "terminate only the recorded child PID on timeout"}
record_path = folder / "family-review-2-run.json"
start = time.monotonic()
with (folder / "family-review-2-stdout.txt").open("w") as stdout, (folder / "family-review-2-stderr.txt").open("w") as stderr:
    child = subprocess.Popen(command, cwd=root, stdout=stdout, stderr=stderr)
    record.update(pid=child.pid, status="running")
    record_path.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record), flush=True)
    try:
        code = child.wait(timeout=record["timeout_seconds"])
        record.update(status="completed", timed_out=False, returncode=code)
    except subprocess.TimeoutExpired:
        child.kill()
        code = child.wait(timeout=5)
        record.update(status="timed_out", timed_out=True, returncode=code)
    record["elapsed_seconds"] = time.monotonic()-start
    record_path.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record), flush=True)
raise SystemExit(0 if not record["timed_out"] and code == 0 else 1)
