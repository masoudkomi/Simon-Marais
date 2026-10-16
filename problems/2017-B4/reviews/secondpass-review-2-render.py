#!/usr/bin/env python3
"""Read-only primary-PDF page rendering, isolated child and 20-second cap."""
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def render():
    import pypdfium2 as pdfium
    print("renderer pypdfium2; child_pid", os.getpid(), flush=True)
    targets = [
        (".cache/literature/2017/cited-7f7251133b0c4ebc.pdf", 11, "fv-p11"),
        (".cache/literature/2017/cited-b5bf6499a3fedd25.pdf", 12, "ckdfs-p12"),
        (".cache/literature/2017/secondpass-review-2-felsner-weil.pdf", 15, "fw-p15"),
        (".cache/literature/2017/secondpass-review-2-felsner-weil.pdf", 19, "fw-p19"),
    ]
    for source, page, tag in targets:
        pdf = pdfium.PdfDocument(ROOT/source)
        output = ROOT/f".cache/literature/2017/secondpass-review-2-source-{tag}.png"
        pdf[page-1].render(scale=1.7).to_pil().save(output)
        print("DONE", source, "page", page, "output", output.name, flush=True)
    print("COMPLETE", flush=True)


def main():
    if len(sys.argv) > 1:
        render()
        return
    output = HERE/"secondpass-review-2-render-output.txt"
    metadata = HERE/"secondpass-review-2-render-job.json"
    command = [sys.executable, str(Path(__file__).resolve()), "--worker"]
    started = time.monotonic()
    job = {"command": command, "timeout_seconds": 20,
           "started_utc": datetime.now(timezone.utc).isoformat(), "status": "running"}
    with output.open("w") as stream:
        child = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT)
        job["child_pid"] = child.pid
        metadata.write_text(json.dumps(job, indent=2)+"\n")
        try:
            code = child.wait(timeout=20)
            job["status"] = "complete" if code == 0 else "failed"
        except subprocess.TimeoutExpired:
            child.terminate()
            try:
                code = child.wait(timeout=2)
            except subprocess.TimeoutExpired:
                child.kill()
                code = child.wait(timeout=2)
            job["status"] = "timeout_incomplete"
    job.update(returncode=code, elapsed_seconds=time.monotonic()-started,
               finished_utc=datetime.now(timezone.utc).isoformat())
    metadata.write_text(json.dumps(job, indent=2)+"\n")
    print(json.dumps(job, sort_keys=True), flush=True)
    if code:
        raise SystemExit(code)


if __name__ == "__main__":
    main()
