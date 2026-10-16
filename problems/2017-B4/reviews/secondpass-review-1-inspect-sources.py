#!/usr/bin/env python3
"""Render selected read-only source pages; images stay in private temporary storage."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
POPPLER = "/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm"
JOBS = [
    (".cache/literature/2017/cited-7f7251133b0c4ebc.pdf",11,"fv-p11"),
    (".cache/literature/2017/cited-b5bf6499a3fedd25.pdf",12,"ckdfs-p12"),
    (".cache/literature/2017/secondpass-review-1-felsner-weil.pdf",15,"fw-p15"),
    (".cache/literature/2017/secondpass-review-1-felsner-weil.pdf",19,"fw-p19"),
]
records = []
for source,page,label in JOBS:
    prefix = "/private/tmp/secondpass-review-1-"+label
    argv = [POPPLER,"-f",str(page),"-l",str(page),"-singlefile","-r","110","-png",str(ROOT/source),prefix]
    out = HERE/("secondpass-review-1-render-"+label+".log")
    job = {"source":source,"source_sha256":hashlib.sha256((ROOT/source).read_bytes()).hexdigest(),
           "page_one_based":page,"argv":argv,"timeout_seconds":20,
           "started_utc":datetime.now(timezone.utc).isoformat()}
    started = time.monotonic()
    with out.open("w") as log:
        child = subprocess.Popen(argv,stdout=log,stderr=subprocess.STDOUT)
        job.update(pid=child.pid,status="running")
        (HERE/"secondpass-review-1-render-jobs.json").write_text(json.dumps(records+[job],indent=2)+"\n")
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
        job.update(returncode=code,elapsed_seconds=time.monotonic()-started,
                   finished_utc=datetime.now(timezone.utc).isoformat())
    png = Path(prefix+".png")
    if png.exists():
        job.update(image=str(png),image_sha256=hashlib.sha256(png.read_bytes()).hexdigest())
    records.append(job)
    (HERE/"secondpass-review-1-render-jobs.json").write_text(json.dumps(records,indent=2)+"\n")
    print(json.dumps(job),flush=True)
