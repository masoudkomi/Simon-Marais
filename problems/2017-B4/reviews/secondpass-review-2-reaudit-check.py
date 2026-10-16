#!/usr/bin/env python3
"""R2 v1.1 targeted finite checks; no author modules or other re-audit read.

The driver preserves a dedicated child PID, 20-second wall cap, parameters and
incremental stdout. These hash/diff and finite exact-geometry checks supplement
the mathematical re-audit; they are not proof of an asymptotic assertion.
"""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction as R
from itertools import combinations
from pathlib import Path
import difflib
import hashlib
import json
import platform
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NOTES = ROOT/"problems/2017-B4/notes"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rectangle_contains(rect, point):
    x0,x1,y0,y1 = rect
    x,y = point
    return x0 < x < x1 and y0 < y < y1


def distance_squared_to_rectangle(point, rect):
    x,y = point
    x0,x1,y0,y1 = rect
    dx = max(x0-x, R(0), x-x1)
    dy = max(y0-y, R(0), y-y1)
    return dx*dx+dy*dy


def geometry(t):
    lines = [(a,b,c) for a,b in ((1,0),(0,1),(-1,1),(1,1))
             for c in range(-t,t+1)]
    vertices = defaultdict(set)
    for i,j in combinations(range(len(lines)), 2):
        a,b,c = lines[i]
        d,e,f = lines[j]
        det = a*e-b*d
        if det:
            point = (R(c*e-b*f,det), R(a*f-c*d,det))
            vertices[point].update((i,j))
    triples = {v for v,incident in vertices.items() if len(incident)==3}
    fours = {v for v,incident in vertices.items() if len(incident)==4}
    assert all(2 <= len(incident) <= 4 for incident in vertices.values())
    assert len(triples)==2*t*t+2*t and len(fours)==2*t*t+2*t+1
    # All original vertices lie on the checkerboard half-integer lattice.
    # Distinct such points have squared separation at least 1/2.
    for x,y in vertices:
        assert (2*x).denominator==(2*y).denominator==1
        assert int(2*x-2*y)%2==0

    original = []
    shrunken = []
    epsilon = R(1,100)
    rho = R(1,1000)
    for i in range(-t-2,t+3):
        for j in range(-t-2,t+3):
            x0,y0 = 3*i+R(1,10), 3*j+R(1,5)
            x1,y1 = x0+3,y0+3
            if max(abs(x)+abs(y) for x,y in ((x0,y0),(x0,y1),(x1,y0),(x1,y1))) < t:
                original.append((x0,x1,y0,y1))
                shrunken.append((x0+epsilon,x1-epsilon,y0+epsilon,y1-epsilon))
    covered = set()
    for old,new in zip(original,shrunken):
        old_vertices = {v for v in vertices if rectangle_contains(old,v)}
        new_vertices = {v for v in vertices if rectangle_contains(new,v)}
        assert old_vertices==new_vertices
        assert sum(v in fours for v in old_vertices)==9
        covered.update(old_vertices)
    assert not triples.intersection(covered)
    residual = fours-covered
    assert (R(0),R(t)) in residual and (R(t),R(0)) in residual
    assert len(residual)==len(fours)-9*len(shrunken)

    # One uniform small radius already separates all counted triple disks and
    # fixed repair disks in these finite instances. It is not needed by the
    # author's more general finite-separation existence proof.
    minimum_support_distance_squared = None
    for v in triples|residual:
        x,y = v
        assert x.denominator==y.denominator==1
        for i,(a,b,c) in enumerate(lines):
            if i not in vertices[v]:
                square_distance = (a*x+b*y-c)**2/R(a*a+b*b)
                assert square_distance > rho*rho
        for rect in shrunken:
            square_distance = distance_squared_to_rectangle(v,rect)
            assert square_distance > rho*rho
            if minimum_support_distance_squared is None or square_distance < minimum_support_distance_squared:
                minimum_support_distance_squared = square_distance
    assert 4*rho*rho < R(1,2)
    print("geometry t",t,"m",2*t+1,"K",len(shrunken),"triple",len(triples),
          "uncovered_fourfold",len(residual),"radius",str(rho),
          "min_support_dist_squared",str(minimum_support_distance_squared),flush=True)


def worker():
    print("R2 targeted v1.1 re-audit; Python",platform.python_version(),flush=True)
    manifest = json.loads((NOTES/"author-repair-manifest-v1.1.json").read_text())
    for item in manifest["candidates"]:
        old,new = ROOT/item["old_path"], ROOT/item["revised_path"]
        diff = ROOT/item["exact_diff_path"]
        assert sha(old)==item["old_sha256"]
        assert sha(new)==item["revised_sha256"]
        assert sha(diff)==item["exact_diff_sha256"]
        expected = "".join(difflib.unified_diff(old.read_text().splitlines(keepends=True),
                         new.read_text().splitlines(keepends=True),
                         fromfile=item["old_path"],tofile=item["revised_path"],n=4))
        assert expected==diff.read_text()
        print("candidate/diff verified",item["claim_prefix"],sha(new),flush=True)
    for path, expected in manifest["preserved_input_sha256"].items():
        assert sha(ROOT/path)==expected
    print("all",len(manifest["preserved_input_sha256"]),"preserved input hashes verified; checksum only for other initial report",flush=True)
    old = (NOTES/"secondpass-macmahon-candidate-v1.md").read_text()
    new = (NOTES/"author-repair-macmahon-candidate-v1.1.md").read_text()
    for begin,end in (("## Candidate M1:","## Candidate M2:"),
                      ("## Candidate M3:","## Independent-review obligations")):
        assert old[old.index(begin):old.index(end)]==new[new.index(begin):new.index(end)]
    print("M1 and M3 mathematical sections byte-identical",flush=True)
    source = ROOT/manifest["source_record"]["path"]
    assert sha(source)==manifest["source_record"]["sha256"]
    sources = json.loads(source.read_text())
    for item in [sources["newly_cited_primary_source"],*sources["other_primary_hypotheses_retained"]]:
        assert sha(ROOT/item["cache_path"])==item["sha256"]
    for item in sources["newly_cited_primary_source"]["images_inspected"]:
        assert sha(ROOT/item["path"])==item["sha256"]
    checkpoint = json.loads((NOTES/"author-repair-checkpoint-v1.1.json").read_text())
    for item in checkpoint["files"]:
        assert sha(ROOT/item["path"])==item["sha256"]
    print("source PDF/image and checkpoint fingerprints verified",flush=True)
    for t in range(1,13):
        geometry(t)
    print("COMPLETE: finite separation evidence; no Q enumeration rerun or L4 attempt",flush=True)


def main():
    if len(sys.argv)>1:
        worker()
        return
    command = [sys.executable,str(Path(__file__).resolve()),"--worker"]
    output = HERE/"secondpass-review-2-reaudit-check-output.txt"
    jobfile = HERE/"secondpass-review-2-reaudit-check-job.json"
    started=time.monotonic()
    job={"command":command,"timeout_seconds":20,"max_t":12,
         "large_support_inward_offset":"1/100","local_disk_radius":"1/1000",
         "started_utc":datetime.now(timezone.utc).isoformat(),"status":"running"}
    with output.open("w") as log:
        child=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT)
        job["child_pid"]=child.pid
        jobfile.write_text(json.dumps(job,indent=2)+"\n")
        print("child_pid",child.pid,"job",jobfile,"stdout",output,flush=True)
        try:
            code=child.wait(timeout=20)
            job["status"]="complete" if code==0 else "failed"
        except subprocess.TimeoutExpired:
            child.terminate()
            try:
                code=child.wait(timeout=2)
            except subprocess.TimeoutExpired:
                child.kill()
                code=child.wait(timeout=2)
            job["status"]="timeout_incomplete"
    job.update(returncode=code,elapsed_seconds=time.monotonic()-started,
               finished_utc=datetime.now(timezone.utc).isoformat())
    jobfile.write_text(json.dumps(job,indent=2)+"\n")
    print(json.dumps(job,sort_keys=True),flush=True)
    if code:
        raise SystemExit(code)


if __name__=="__main__":
    main()
