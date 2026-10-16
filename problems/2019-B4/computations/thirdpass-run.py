#!/usr/bin/env python3
"""External timeout supervisor, one explicitly specified child."""
import argparse,datetime,hashlib,json,os,subprocess,time
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--timeout',type=float,required=True)
p.add_argument('--prefix',required=True)
p.add_argument('command',nargs=argparse.REMAINDER)
a=p.parse_args()
assert a.command and 0<a.timeout<=120
prefix=Path(a.prefix)
record={'command':a.command,'timeout_seconds':a.timeout,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'supervisor_pid':os.getpid(),'status':'starting'}
job=Path(str(prefix)+'-job.json')
def save():job.write_text(json.dumps(record,indent=2)+'\n')
save()
start=time.monotonic()
with open(str(prefix)+'.log','w') as log,open(str(prefix)+'-stderr.txt','w') as error:
 child=subprocess.Popen(a.command,stdout=log,stderr=error)
 record.update(child_pid=child.pid,status='running');save()
 try:
  rc=child.wait(timeout=a.timeout)
  record.update(status='completed',returncode=rc)
 except subprocess.TimeoutExpired:
  child.kill();rc=child.wait();record.update(status='external_timeout_killed_and_reaped',returncode=rc)
record['elapsed_seconds']=time.monotonic()-start
record['completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
record['source_sha256']={s:hashlib.sha256(Path(s).read_bytes()).hexdigest() for s in a.command if Path(s).is_file()}
save()
print(json.dumps(record,indent=2))
