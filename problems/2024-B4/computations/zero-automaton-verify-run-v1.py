#!/usr/bin/env python3
"""Bounded subprocess harness for the separate exact verifier."""

import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMMAND = [sys.executable, '-u', str(HERE / 'zero-automaton-verify-v1.py')]
OUT = HERE / 'zero-automaton-v1-verification-output.txt'
ERR = HERE / 'zero-automaton-v1-verification-stderr.txt'
JOB = HERE / 'zero-automaton-v1-verification-job.json'
record = {'command': COMMAND, 'external_timeout_seconds': 45,
          'status': 'not yet launched', 'dependencies': 'Python standard library only',
          'requested_model': 'gpt-6.1-sol', 'requested_reasoning': 'max',
          'verified_effective_settings': None}
start = time.monotonic()
with OUT.open('w') as out, ERR.open('w') as err:
    child = subprocess.Popen(COMMAND, stdout=out, stderr=err)
    record.update(pid=child.pid, status='running')
    JOB.write_text(json.dumps(record, indent=2) + '\n')
    print('Child PID', child.pid, 'timeout 45 seconds; parameters saved to', JOB, flush=True)
    try:
        child.wait(timeout=45)
        record['status'] = 'completed' if child.returncode == 0 else 'child failed'
    except subprocess.TimeoutExpired:
        record['status'] = 'external timeout; this child alone terminated'
        child.terminate()
        try:
            child.wait(timeout=2)
        except subprocess.TimeoutExpired:
            child.kill()
            child.wait()
    record['returncode'] = child.returncode
record['elapsed_seconds'] = time.monotonic() - start
paths = [OUT, ERR, HERE / 'zero-automaton-verify-v1.py']
verification = HERE / 'zero-automaton-v1-verification.json'
if verification.exists():
    paths.append(verification)
record['files_sha256'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
JOB.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2), flush=True)
