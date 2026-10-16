#!/usr/bin/env python3
"""Cache a public primary PDF with timeout, PID, timestamps and byte checkpoints."""
import hashlib
import json
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[3]
here = Path(__file__).resolve().parent
out = root / ".cache/literature/2025/initial-review-1-chen-mihailescu-2026-retry2.pdf"
assert not out.exists(), "Never overwrite an earlier retrieval"
command = ["curl", "-L", "--fail", "--silent", "--show-error", "--connect-timeout", "20", "--max-time", "180",
           "--write-out", "http_code=%{http_code} bytes=%{size_download} time=%{time_total} effective_url=%{url_effective}\\n",
           "https://camath.fudan.edu.cn/cambcn/ch/reader/create_pdf.aspx?file_no=47B208&flag=1", "-o", str(out)]
job = {"status": "starting", "started_utc": datetime.now(timezone.utc).isoformat(), "command": command,
       "output_path": str(out.relative_to(root)), "timeout_seconds": 185, "checkpoints": []}
started = time.monotonic()
with (here / "initial-review-1-cache.log").open("w") as log:
    child = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, cwd=root)
    job.update(status="running", child_pid=child.pid)
    while child.poll() is None:
        elapsed = time.monotonic()-started
        if elapsed > 185:
            child.terminate()
            try:
                child.wait(timeout=3)
            except subprocess.TimeoutExpired:
                child.kill()
                child.wait(timeout=3)
            job["status"] = "timeout"
            break
        item = {"elapsed_seconds": round(elapsed, 3), "bytes": out.stat().st_size if out.exists() else 0}
        job["checkpoints"].append(item)
        (here / "initial-review-1-cache-job.json").write_text(json.dumps(job, indent=2) + "\n")
        print(json.dumps(item), flush=True)
        try:
            child.wait(timeout=10)
        except subprocess.TimeoutExpired:
            pass
    job.update(return_code=child.returncode, status="complete" if child.returncode == 0 else job.get("status", "failed"),
               finished_utc=datetime.now(timezone.utc).isoformat(), elapsed_seconds=round(time.monotonic()-started, 3))
    if child.returncode and job["status"] == "running":
        job["status"] = "failed"
    if out.exists():
        job.update(bytes=out.stat().st_size, sha256=hashlib.sha256(out.read_bytes()).hexdigest())
(here / "initial-review-1-cache-job.json").write_text(json.dumps(job, indent=2) + "\n")
print(json.dumps(job, indent=2), flush=True)
raise SystemExit(0 if job["status"] == "complete" else 1)
