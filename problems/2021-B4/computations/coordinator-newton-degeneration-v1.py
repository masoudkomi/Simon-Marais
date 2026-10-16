#!/usr/bin/env python3
"""Finite necessary mask filter for an unverified degeneration candidate."""
from pathlib import Path
from math import comb
from collections import Counter
import datetime, hashlib, json, os, subprocess, sys, time

HERE = Path(__file__).resolve().parent
PREFIX = 'coordinator-newton-degeneration-v1'

def child():
    p, d, modulus = 19, 20, 361
    counts, retained = Counter(), Counter()
    masks = []
    c = [0] * (d+1)
    c[d], c[d-1] = 1, -d
    def visit(r, mask):
        if r == 1:
            if sum(c) % modulus:
                return
            units = [d-t for t in range(2,d-1) if c[t] % modulus]
            assert units
            j = max(units)
            counts[j] += 1
            h = d-j
            keep = h not in (2,3,4,5) or any(mask & (1 << (k-2)) for k in range(2,h))
            retained[j] += bool(keep)
            if j == 15:
                masks.append({'mask_hasse_orders_2_to_18':mask,
                              'low_center_orders':[k for k in (2,3,4) if mask & (1 << (k-2))],
                              'retained':keep})
            return
        c[r] = 0
        visit(r-1,mask)
        c[r] = -sum(comb(t,r)*c[t] for t in range(r+1,d+1)) % modulus
        visit(r-1, mask | (1 << (r-2)))
    visit(d-2,0)
    assert sum(counts.values()) == 6680
    assert counts[15] == 461
    result = {'status':'finite exact necessary filter; degeneration proof remains unverified',
              'p':p,'degree':d,'modulus':modulus,'binary_flags':2**17,
              'before':dict(sorted(counts.items())),
              'after_low_center_disjunction':dict(sorted(retained.items())),
              'J15_removed':counts[15]-retained[15], 'J15_retained':retained[15],
              'masks_J15':masks}
    target=HERE/(PREFIX+'-result.json')
    target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='masks_J15'}),flush=True)

def main():
    if '--child' in sys.argv:
        child();return
    out,err,job=[HERE/(PREFIX+s) for s in ('-output.txt','-stderr.txt','-job.json')]
    cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--child']
    record={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'command':cmd,'timeout_seconds':20,'status':'launching'}
    start=time.monotonic()
    with out.open('w') as f,err.open('w') as e:
        proc=subprocess.Popen(cmd,stdout=f,stderr=e)
        record.update(pid=proc.pid,status='running')
        job.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True)
        try:
            proc.wait(timeout=20)
            record['status']='completed' if proc.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:
            proc.kill();proc.wait();record['status']='timeout; identified child reaped'
        record.update(return_code=proc.returncode,elapsed_seconds=time.monotonic()-start)
    record['sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in (Path(__file__),out,err,HERE/(PREFIX+'-result.json')) if p.is_file()}
    job.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True)

if __name__=='__main__':main()
