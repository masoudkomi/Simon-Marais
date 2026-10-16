#!/usr/bin/env python3
"""Targeted R1 re-audit v1.1: exact provenance/diff checks and finite geometry.

No imports from author or original reviewer counters. Standard library only.
Driver preserves one dedicated child PID, argv, timeout and incremental output.
Finite geometry is evidence; the disjointness proof is in the review report.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import difflib
from fractions import Fraction as Q
import hashlib
from itertools import combinations
import json
from pathlib import Path
import platform
import subprocess
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def provenance():
    manifest_path=ROOT/"problems/2017-B4/notes/author-repair-manifest-v1.1.json"
    manifest=json.loads(manifest_path.read_text())
    expected={"macmahon":"a225f0042fc098d8a827093a3e680612848caf392db64cad24339d399769bcf0",
              "boundary-fiber":"e2891eafc6fa8449f6c70c817c2e21416a43f1893120929df02f2aa2dac86a8b",
              "periodic-grid":"1a6acb042e1e21bc0992cddbd7188c47e81249b5888faabaa4e73a45be0f5c6e"}
    for item in manifest["candidates"]:
        old=ROOT/item["old_path"]
        new=ROOT/item["revised_path"]
        diff=ROOT/item["exact_diff_path"]
        assert digest(old)==item["old_sha256"]
        assert digest(new)==item["revised_sha256"]==expected[item["claim_prefix"]]
        assert digest(diff)==item["exact_diff_sha256"]
        generated="".join(difflib.unified_diff(old.read_text().splitlines(keepends=True),
                         new.read_text().splitlines(keepends=True),fromfile=item["old_path"],
                         tofile=item["revised_path"],n=4))
        assert generated.encode()==diff.read_bytes(),item["claim_prefix"]
        print("EXACT DIFF COMPLETE",item["claim_prefix"],digest(new),digest(diff),flush=True)
    old=(ROOT/"problems/2017-B4/notes/secondpass-macmahon-candidate-v1.md").read_text()
    new=(ROOT/"problems/2017-B4/notes/author-repair-macmahon-candidate-v1.1.md").read_text()
    for start,end in (("## Candidate M1:","## Candidate M2:"),
                      ("## Candidate M3:","## Independent-review obligations")):
        aa=old[old.index(start):old.index(end)]
        bb=new[new.index(start):new.index(end)]
        assert aa==bb
        print("UNCHANGED MATH SECTION",start,hashlib.sha256(aa.encode()).hexdigest(),flush=True)
    for name,expected_hash in manifest["preserved_input_sha256"].items():
        assert digest(ROOT/name)==expected_hash,name
    print("PRESERVED INPUT HASHES COMPLETE",len(manifest["preserved_input_sha256"]),flush=True)
    source_path=ROOT/"problems/2017-B4/notes/author-repair-sources-v1.1.json"
    source=json.loads(source_path.read_text())
    assert digest(source_path)==manifest["source_record"]["sha256"]
    primary=source["newly_cited_primary_source"]
    assert digest(ROOT/primary["cache_path"])==primary["sha256"]
    assert digest(ROOT/".cache/literature/2017/secondpass-review-1-felsner-weil.pdf")==primary["sha256"]
    for image in primary["images_inspected"]:
        assert digest(ROOT/image["path"])==image["sha256"]
    for item in source["other_primary_hypotheses_retained"]:
        assert digest(ROOT/item["cache_path"])==item["sha256"]
    print("SOURCE FINGERPRINTS COMPLETE",primary["sha256"],flush=True)
    checkpoint=ROOT/"problems/2017-B4/notes/author-repair-checkpoint-v1.1.json"
    cp=json.loads(checkpoint.read_text())
    for item in cp["files"]:
        assert digest(ROOT/item["path"])==item["sha256"],item["path"]
    print("AUTHOR CHECKPOINT FILE HASHES COMPLETE",len(cp["files"]),flush=True)

def clipped_word(box):
    x0,x1,y0,y1=box
    events=[]
    for A,B in ((1,0),(0,1),(-1,1),(1,1)):
        low=min(A*x+B*y for x in (x0,x1) for y in (y0,y1))
        high=max(A*x+B*y for x in (x0,x1) for y in (y0,y1))
        for C in range(int(low)-2,int(high)+3):
            ports=set()
            if B:
                for x in (x0,x1):
                    y=(C-A*x)/B
                    if y0<y<y1:
                        ports.add((x,y))
            if A:
                for y in (y0,y1):
                    x=(C-B*y)/A
                    if x0<x<x1:
                        ports.add((x,y))
            if not ports:
                continue
            assert len(ports)==2
            for x,y in ports:
                assert not (x in (x0,x1) and y in (y0,y1))
                if y==y0: pos=(0,x)
                elif x==x1: pos=(1,y)
                elif y==y1: pos=(2,-x)
                else: pos=(3,-y)
                events.append((pos,(A,B,C)))
    assert len({p for p,line in events})==len(events)
    return tuple(line for p,line in sorted(events))

def geometry(t):
    lines=[(A,B,C) for A,B in ((1,0),(0,1),(-1,1),(1,1)) for C in range(-t,t+1)]
    points={}
    for i,j in combinations(range(len(lines)),2):
        A,B,C=lines[i]; D,E,F=lines[j]
        determinant=A*E-B*D
        if determinant:
            xy=Q(C*E-B*F,determinant),Q(A*F-C*D,determinant)
            points.setdefault(xy,set()).update((i,j))
    assert all(x.denominator<=2 and y.denominator<=2 for x,y in points)
    multi={xy:who for xy,who in points.items() if len(who)>2}
    assert all(x.denominator==y.denominator==1 for x,y in multi)
    triple={xy for xy,who in multi.items() if len(who)==3}
    quad={xy for xy,who in multi.items() if len(who)==4}
    assert len(triple)==2*t*t+2*t and len(quad)==2*t*t+2*t+1
    boxes=[]
    original=[]
    delta=Q(1,100)
    for i in range(-t//3-3,t//3+4):
        for j in range(-t//3-3,t//3+4):
            a,b=3*i+Q(1,10),3*j+Q(1,5)
            if all(abs(x)+abs(y)<=t for x in (a,a+3) for y in (b,b+3)):
                original.append((a,a+3,b,b+3))
                boxes.append((a+delta,a+3-delta,b+delta,b+3-delta))
    def in_box(xy,box):
        x,y=xy; a,b,c,d=box
        return a<x<b and c<y<d
    # Global multicrossing classification after the retained supports shrink.
    large={xy for xy in multi if any(in_box(xy,box) for box in boxes)}
    large_original={xy for xy in multi if any(in_box(xy,box) for box in original)}
    assert large==large_original and large<=quad
    assert len(large)==9*len(boxes)
    residual=set(multi)-large-triple
    assert residual<=quad
    assert (Q(0),Q(t)) in residual and (Q(t),Q(0)) in residual
    assert all(t-abs(x)-abs(y)<=6 for x,y in residual)
    radius=Q(1,1000)
    # Pairwise distinct repair/triple centers are integer lattice points, so
    # distance >=1 >2*radius. All original crossings lie in (Z/2)^2, so all
    # other vertices have distance >=1/2 >radius. A nonincident grid line is
    # >=1/sqrt(2) away from an integer center. Check remaining support distances.
    minimum=None
    for x,y in residual|triple:
        for a,b,c,d in boxes:
            dx=max(a-x,Q(0),x-b); dy=max(c-y,Q(0),y-d)
            d2=dx*dx+dy*dy
            assert d2>radius*radius
            minimum=d2 if minimum is None else min(minimum,d2)
    if original:
        assert clipped_word(original[0])==clipped_word(boxes[0])
    print("GEOMETRY COMPLETE",json.dumps({"t":t,"m":2*t+1,"K":len(boxes),"fourfold":len(quad),
        "triple":len(triple),"fixed_residual":len(residual),"repair_radius":str(radius),
        "support_shrink":str(delta),"minimum_squared_distance_to_large":str(minimum),
        "all_original_multicrossings_assigned":True,"boundary_examples_repaired":True}),flush=True)

def worker():
    print("R1 targeted re-audit",platform.python_version(),"stdlib only; exact finite evidence",flush=True)
    provenance()
    for t in list(range(1,13))+[20]:
        geometry(t)
    print("COMPLETE: no enumeration or side-4 retry",flush=True)

def main():
    p=argparse.ArgumentParser(); p.add_argument("--worker",action="store_true");p.add_argument("--timeout",type=float,default=25)
    a=p.parse_args()
    if a.worker:
        worker();return
    stdout=HERE/"secondpass-review-1-reaudit-check.log"
    jobpath=HERE/"secondpass-review-1-reaudit-job.json"
    argv=[sys.executable,str(Path(__file__).resolve()),"--worker"]
    start=monotonic()
    with stdout.open("w") as out:
        child=subprocess.Popen(argv,cwd=ROOT,stdout=out,stderr=subprocess.STDOUT)
        job={"started_utc":datetime.now(timezone.utc).isoformat(),"pid":child.pid,"argv":argv,
             "timeout_seconds":a.timeout,"script_sha256":digest(Path(__file__).resolve()),
             "stdout":str(stdout),"status":"running"}
        jobpath.write_text(json.dumps(job,indent=2)+"\n");print(json.dumps(job),flush=True)
        try:
            code=child.wait(timeout=a.timeout);job["status"]="complete" if code==0 else "failed_incomplete"
        except subprocess.TimeoutExpired:
            child.terminate()
            try: code=child.wait(timeout=2)
            except subprocess.TimeoutExpired:
                child.kill();code=child.wait(timeout=2)
            job["status"]="timeout_incomplete"
        job.update(returncode=code,elapsed_seconds=monotonic()-start,finished_utc=datetime.now(timezone.utc).isoformat())
        jobpath.write_text(json.dumps(job,indent=2)+"\n");print(json.dumps(job),flush=True)
    if code: raise SystemExit(1)

if __name__=="__main__":
    main()
