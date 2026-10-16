#!/usr/bin/env python3
"""External process timeout with PID, log checkpoints and targeted reaping."""
import datetime
import json
import pathlib
import subprocess
import sys
import time

base = pathlib.Path(sys.argv[1])
limit = float(sys.argv[2])
command = sys.argv[3:]
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
clock = time.monotonic()
record = {'started_utc': started, 'command': command, 'cwd': str(pathlib.Path.cwd()),
          'timeout_seconds': limit, 'requested_model': 'gpt-6.1-sol',
          'requested_reasoning_effort': 'max', 'effective_settings_readback': None}
with base.with_name(base.name+'-stdout.log').open('w') as out, base.with_name(base.name+'-stderr.log').open('w') as err:
    child = subprocess.Popen(command, stdout=out, stderr=err)
    record.update(pid=child.pid, status='running')
    base.with_name(base.name+'-job.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps({'event': 'spawn', 'pid': child.pid, 'timeout': limit, 'command': command}), flush=True)
    try:
        code = child.wait(timeout=limit)
        record['status'] = 'completed'
    except subprocess.TimeoutExpired:
        child.terminate()
        try:
            child.wait(timeout=3)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait()
        record['status'] = 'timeout; targeted child terminated and reaped'
        code = child.returncode
    record.update(returncode=code, elapsed_seconds=time.monotonic()-clock,
                  finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(), reaped=True)
    base.with_name(base.name+'-job.json').write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record), flush=True)
sys.exit(code if record['status'] == 'completed' else 124)
