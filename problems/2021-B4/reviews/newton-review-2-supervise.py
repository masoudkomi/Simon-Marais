#!/usr/bin/env python3
"""Bounded targeted child supervisor for R2 computations only."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

base = Path(__file__).resolve().parent
child_path = (base / sys.argv[1]).resolve()
assert child_path.parent == base and child_path.name.startswith("newton-review-2-")
label = sys.argv[2]
assert label.startswith("newton-review-2-") and "/" not in label
limit = int(sys.argv[3])
assert 1 <= limit <= 180
output = base / (label + ".jsonl")
job = base / (label + "-job.json")
start = time.monotonic()
with output.open("w") as log:
    child = subprocess.Popen([sys.executable, "-u", str(child_path), *sys.argv[4:]], stdout=log, stderr=subprocess.STDOUT)
    metadata = dict(pid=child.pid, command=[sys.executable, "-u", str(child_path), *sys.argv[4:]], timeout_seconds=limit, output=str(output), script_sha256=hashlib.sha256(child_path.read_bytes()).hexdigest(), started_at_unix=time.time())
    job.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(json.dumps(dict(event="spawned", **metadata)), flush=True)
    offset = 0
    timed_out = False
    while child.poll() is None:
        remaining = limit - (time.monotonic() - start)
        if remaining <= 0:
            timed_out = True
            child.kill()
            child.wait()
            break
        try:
            child.wait(timeout=min(5, remaining))
        except subprocess.TimeoutExpired:
            pass
        text = output.read_text()
        print(text[offset:], end="", flush=True)
        offset = len(text)
    text = output.read_text()
    print(text[offset:], end="", flush=True)
    metadata.update(exit_code=child.returncode, timed_out=timed_out, elapsed_seconds=time.monotonic() - start, output_sha256=hashlib.sha256(output.read_bytes()).hexdigest())
    job.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    print(json.dumps(dict(event="finished", **metadata)), flush=True)
    sys.exit(124 if timed_out else child.returncode)
