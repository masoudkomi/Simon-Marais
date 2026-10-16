#!/usr/bin/env python3
"""Dedicated externally capped children; preserve PID, exact command and reaping."""
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

here = Path(__file__).resolve().parent
label, captext, *params = sys.argv[1:]
limit = float(captext)
assert 0 < limit <= 180
prefix = here / ('thirdpass-review-1-' + label)
source = here / 'thirdpass-review-1-check.py'
command = [sys.executable, '-u', str(source)] + params
record = {'command': command, 'external_timeout_seconds': limit,
          'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'started_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
t0 = time.monotonic()
with open(str(prefix)+'-stdout.log','w') as out, open(str(prefix)+'-stderr.log','w') as err:
    child = subprocess.Popen(command, stdout=out, stderr=err, cwd=here.parents[2], start_new_session=True)
    record['child_pid'] = child.pid
    Path(str(prefix)+'-job.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'child_pid':child.pid,'command':command,'timeout':limit}),flush=True)
    try:
        record['exit_code'] = child.wait(timeout=limit)
        record['timed_out'] = False
    except subprocess.TimeoutExpired:
        record['timed_out'] = True
        child.kill()
        record['exit_code'] = child.wait(timeout=10)
    record['reaped'] = True
record['seconds'] = time.monotonic()-t0
record['finished_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
Path(str(prefix)+'-job.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record),flush=True)
sys.exit(0 if record['exit_code']==0 else 1)
