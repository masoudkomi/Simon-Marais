#!/usr/bin/env python3
"""Constructor integrity check and immutable handoff, not mathematical review."""
from pathlib import Path
import datetime,gzip,hashlib,json,subprocess,sys,time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE=HERE.parent
PREFIX='coordinator-three-complex-freeze-v1'
MANIFEST=BASE/'notes/coordinator-three-complex-witnesses-v1-manifest.json'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def emit(x):print(json.dumps(x,sort_keys=True),flush=True)

def child():
    result=json.loads((HERE/'coordinator-three-complex-witnesses-v1-result.json').read_text())
    digest=hashlib.sha256();total=0;checked=[]
    for c in result['chunks']:
        p=ROOT/c['path']
        assert p.stat().st_size==c['bytes'] and sha(p)==c['sha256']
        count=0
        with gzip.open(p,'rb') as f:
            while block:=f.read(1024*1024):
                digest.update(block);count+=block.count(b'\n')
        assert count==c['rows']
        total+=count;checked.append(c)
        emit({'chunk_verified':p.name,'rows':count,'total':total})
    assert total==4731928 and digest.hexdigest()==result['uncompressed_certificate_stream_sha256']
    resolver=json.loads((HERE/'coordinator-three-complex-witnesses-v1-resolve-result.json').read_text())
    assert resolver['resolved']==3 and resolver['unresolved']==0
    assert {(r['center_mask'],r['u_mask']) for r in resolver['cases']}=={(117075,9220),(117075,1548),(117075,9356)}
    out={'status':'constructor gzip/hash/row integrity only; no independent mathematical audit',
         'chunks':len(checked),'compressed_bytes':sum(c['bytes'] for c in checked),
         'rows':total,'uncompressed_certificate_stream_sha256':digest.hexdigest(),
         'all_resolver_cases_recorded':True}
    (HERE/(PREFIX+'-result.json')).write_text(json.dumps(out,indent=2)+'\n');emit(out)

def main():
    if '--child' in sys.argv:child();return
    assert not MANIFEST.exists(),'Frozen manifest exists; do not overwrite it.'
    out,err,job=[HERE/(PREFIX+s) for s in ('-output.txt','-stderr.txt','-job.json')]
    cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--child']
    rec={'started_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'command':cmd,'timeout_seconds':30,'status':'launching'}
    start=time.monotonic()
    with out.open('w') as f,err.open('w') as e:
        proc=subprocess.Popen(cmd,stdout=f,stderr=e);rec.update(pid=proc.pid,status='running')
        job.write_text(json.dumps(rec,indent=2)+'\n');emit(rec)
        try:proc.wait(timeout=30);rec['status']='completed' if proc.returncode==0 else 'failed'
        except subprocess.TimeoutExpired:
            proc.kill();proc.wait();rec['status']='timeout; identified child reaped'
        rec.update(return_code=proc.returncode,elapsed_seconds=time.monotonic()-start)
    job.write_text(json.dumps(rec,indent=2)+'\n');emit(rec)
    assert rec['status']=='completed'
    old_manifest=BASE/'notes/coordinator-three-rational-witnesses-v1-manifest.json'
    old=json.loads(old_manifest.read_text())
    files={ROOT/r['path'] for r in old['artifacts']}
    for r in old['artifacts']:
        assert sha(ROOT/r['path'])==r['sha256']
    files.add(old_manifest)
    files.update(HERE.glob('coordinator-three-complex-*'))
    files.update(BASE.glob('notes/coordinator-three-complex-witnesses-v1*'))
    files.update([BASE/'reviews/three-witness-acceptance.json',
                  BASE/'reviews/three-witness-acceptance.md',
                  BASE/'notes/coordinator-three-rational-witnesses-reviewed-v1.1.md'])
    files={p for p in files if p.is_file() and p!=MANIFEST}
    artifacts=[{'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':sha(p)} for p in sorted(files)]
    record={'frozen_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'status':'candidate proof - unverified','constructor':'coordinator',
            'complex_claim':'C20 only; no full degree or contest classification',
            'old_masks':772,'additional_masks':5908,'all_masks':6680,
            'old_families':1493024,'additional_families':4731928,'all_families':6224952,
            'new_initial_misses_preserved':3,'new_separate_misses_resolved':3,
            'independent_complex_extension_reviews':0,
            'old_finite_algebraic_certificate_is_explicit_reviewed_dependency':True,
            'integrity_not_independent_math_review':True,'artifacts':artifacts}
    MANIFEST.write_text(json.dumps(record,indent=2)+'\n')
    emit({'manifest':str(MANIFEST.relative_to(ROOT)),'artifacts':len(artifacts),
          'manifest_sha256':sha(MANIFEST),
          'candidate_sha256':sha(BASE/'notes/coordinator-three-complex-witnesses-v1.md')})

if __name__=='__main__':main()
