#!/usr/bin/env python3
"""Run this review's exact check in its own bounded subprocess."""
import datetime
import json
import pathlib
import subprocess
import sys
import time

folder = pathlib.Path(__file__).resolve().parent
prefix = folder / 'ghosh-review-1'
command = [sys.executable, '-u', str(folder / 'ghosh-review-1-check.py')]
timeout_seconds = 30
started = time.monotonic()
with prefix.with_name(prefix.name+'-check.jsonl').open('w') as out, prefix.with_name(prefix.name+'-stderr.txt').open('w') as err:
    child = subprocess.Popen(command, stdout=out, stderr=err)
    job = {'command':command, 'child_pid':child.pid, 'timeout_seconds':timeout_seconds, 'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'parameters':'fixed exact models; no search'}
    prefix.with_name(prefix.name+'-job.json').write_text(json.dumps(job, indent=2)+'\n')
    print(json.dumps({'event':'spawned', **job}), flush=True)
    timed_out = False
    try:
        code = child.wait(timeout=timeout_seconds)
    except subprocess.TimeoutExpired:
        timed_out = True
        child.terminate()
        try:
            code = child.wait(timeout=3)
        except subprocess.TimeoutExpired:
            child.kill()
            code = child.wait(timeout=3)
    result = {'child_pid':child.pid, 'exit_code':code, 'timed_out':timed_out, 'elapsed_seconds':time.monotonic()-started, 'finished_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    prefix.with_name(prefix.name+'-result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'event':'finished', **result}), flush=True)
sys.exit(code if code else int(timed_out))
