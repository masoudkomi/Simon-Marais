#!/usr/bin/env python3
"""R1 complex extension: new prime-field filter and full complementary audit.

Only the exact ordinary-Hasse integer-polynomial and finite-field routines
are reused from R1's own frozen old code. The old rational mask derivation
is neither called nor applied to a ramified extension. No author module runs.
"""
import argparse
import collections
import gzip
import hashlib
import importlib.util
import itertools
import json
import math
import os
from pathlib import Path
import sys
import time

ROOT=Path(__file__).resolve().parents[3]
PREFIX=Path(__file__).with_name("three-complex-review-1")
COMPS=ROOT/"problems/2021-B4/computations"
OLD_CORE=ROOT/"problems/2021-B4/reviews/three-witness-review-1-independent.py"
OLD_CORE_HASH="ed98ed514ac6dffa20e3c5779d7851437003326992f0619018f1837147386464"
assert hashlib.sha256(OLD_CORE.read_bytes()).hexdigest()==OLD_CORE_HASH
# Preserve all old files, including avoiding an old-prefix .pyc cache.
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location("r1_own_frozen_hasse_core",OLD_CORE)
core=importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
FULL=(1<<17)-1

def independently_derive_prime_field_masks():
    # All arithmetic here is in the prime field F_19, i.e. reduction modulo
    # the maximal ideal of O_K, not ordinary coefficients modulo 19^2.
    # Integral a_j reduce to 0 at a noncenter bit, even when 0<v(a_j)<1.
    masks=[]
    histogram=collections.Counter()
    bins=[[math.comb(j,k)%19 for k in range(j+1)] for j in range(19)]
    divided=[math.comb(20,j)//19%19 for j in range(2,19)]
    for mask in range(1<<17):
        a=[1,18]+[0]*17
        for j in range(2,19):
            if mask & (1<<(j-2)):
                a[j]=-sum(coef*value for coef,value in zip(bins[j],a))%19
        if (-1+sum(unit*value for unit,value in zip(divided,a[2:])))%19:
            continue
        unit_indices=[j for j in range(2,19) if a[j]]
        assert unit_indices
        histogram[max(unit_indices)]+=1
        masks.append(mask)
    assert len(masks)==len(set(masks))==6680
    # This accepted old set is subtracted solely because every explicit
    # pair in it already has a reviewed algebraic incompatibility certificate.
    old_path=ROOT/"problems/2021-B4/reviews/three-witness-review-1-independent-masks.json"
    old=json.loads(old_path.read_text())["masks"]
    assert len(old)==len(set(old))==772
    old_set=set(old)
    assert old_set<=set(masks)
    additional=[m for m in masks if m not in old_set]
    assert len(additional)==5908 and not set(additional)&old_set
    assert set(additional)|old_set==set(masks)
    counts={"all":sum(1<<(17-m.bit_count()) for m in masks),
            "accepted_old":sum(1<<(17-m.bit_count()) for m in old),
            "new_complement":sum(1<<(17-m.bit_count()) for m in additional)}
    assert counts=={"all":6224952,"accepted_old":1493024,"new_complement":4731928}
    return {"method":"normalized triangular equations in F_19, maximal-ideal reduction; no rational Newton/J filter",
            "all_binary_choices":1<<17,"all_masks":masks,"old_masks":old,"additional_masks":additional,
            "J_histogram_diagnostic_only":dict(sorted(histogram.items())),"refinement_counts":counts,
            "old_mask_source":str(old_path.relative_to(ROOT)),
            "old_mask_source_sha256":hashlib.sha256(old_path.read_bytes()).hexdigest(),
            "old_core_sha256":OLD_CORE_HASH}

def certificate_groups():
    digest=hashlib.sha256()
    chunks=[]
    def records():
        paths=sorted(COMPS.glob("coordinator-three-complex-witnesses-v1-certificates-*.jsonl.gz"))
        assert len(paths)==79
        for path in paths:
            rows=0
            with gzip.open(path,"rb") as stream:
                for line in stream:
                    digest.update(line)
                    rows+=1
                    yield json.loads(line)
            chunks.append({"path":str(path.relative_to(ROOT)),"rows":rows,
                           "bytes":path.stat().st_size,
                           "sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
    return itertools.groupby(records(),lambda r:r[0]),digest,chunks

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode",choices=("masks","benchmark","full"),default="masks")
    parser.add_argument("--limit",type=int,default=65536)
    args=parser.parse_args()
    start=time.monotonic()
    derived=independently_derive_prime_field_masks()
    Path(str(PREFIX)+"-independent-masks.json").write_text(json.dumps(derived,indent=2)+"\n")
    print(json.dumps({"event":"prime_field_masks_derived","pid":os.getpid(),
                      "binary_choices":derived["all_binary_choices"],
                      "all_masks":len(derived["all_masks"]),"old_masks":len(derived["old_masks"]),
                      "additional_masks":len(derived["additional_masks"]),
                      "refinement_counts":derived["refinement_counts"],
                      "J_histogram":derived["J_histogram_diagnostic_only"]}),flush=True)
    if args.mode=="masks":
        return
    if args.mode=="full":
        groups,raw_digest,chunks=certificate_groups()
    total=0
    counts=collections.Counter()
    degree_histogram=collections.Counter()
    key_digest=hashlib.sha256()
    polynomial_digest=hashlib.sha256()
    sentinels=[]
    for mask in derived["additional_masks"]:
        required=1<<(17-mask.bit_count())
        raw={}
        if args.mode=="full":
            raw_mask,group=next(groups)
            assert raw_mask==mask,("raw mask order",raw_mask,mask)
            for row in group:
                umask=row[1]
                assert umask>=0 and not umask&mask and not umask&~FULL
                assert umask not in raw,("duplicate raw family",mask,umask)
                raw[umask]=row
            assert len(raw)==required,("wrong raw coverage",mask,len(raw),required)
        seen=set()
        for umask,p,q in core.families(mask):
            assert umask not in seen and not umask&mask and not umask&~FULL
            seen.add(umask)
            prime=core.independently_certify(p,q)
            counts[prime]+=1
            degree_histogram[(len(p)-1,len(q)-1)]+=1
            key_digest.update(f"{mask},{umask}\n".encode())
            polynomial_digest.update((json.dumps([mask,umask,p,q],separators=(",",":"))+"\n").encode())
            if args.mode=="full":
                row=raw.pop(umask)
                if row[2]==0:
                    assert len(row)==4 and prime==0 and len(p)==1 and p[0]==row[3]!=0
                elif row[2]==-1:
                    assert len(row)==3 and prime==131
                    assert (mask,umask) in {(117075,9220),(117075,1548),(117075,9356)}
                    sentinels.append({"mask":mask,"U_mask":umask,"P":p,"Q":q,
                                      "prime":prime,"degrees":[len(p)-1,len(q)-1],
                                      "leading_residues":[p[-1]%prime,q[-1]%prime]})
                else:
                    assert len(row)==7 and row[2]==prime
                    assert row[3:]==[len(p)-1,len(q)-1,p[-1]%prime,q[-1]%prime]
            total+=1
            if total%8192==0:
                print(json.dumps({"event":"checkpoint","families":total,"mask":mask,
                                  "seconds":round(time.monotonic()-start,3)}),flush=True)
            if args.mode=="benchmark" and total>=args.limit:
                break
        if args.mode=="benchmark" and total>=args.limit:
            break
        assert len(seen)==required and not raw
    if args.mode=="full":
        assert next(groups,None) is None
        assert total==4731928 and len(sentinels)==3
        assert {(s["mask"],s["U_mask"]) for s in sentinels}=={(117075,9220),(117075,1548),(117075,9356)}
    result={"event":"complete","mode":args.mode,"pid":os.getpid(),"families":total,
            "elapsed_seconds":time.monotonic()-start,"certificate_histogram":dict(counts),
            "sentinels":sentinels,"degree_histogram":{str(k):v for k,v in sorted(degree_histogram.items())},
            "key_stream_sha256":key_digest.hexdigest(),"polynomial_stream_sha256":polynomial_digest.hexdigest(),
            "old_finite_dependency_families":1493024,"union_families":6224952,
            "reused_code_is_reviewers_own":str(OLD_CORE.relative_to(ROOT)),"old_core_sha256":OLD_CORE_HASH}
    if args.mode=="full":
        result.update({"uncompressed_certificate_stream_sha256":raw_digest.hexdigest(),
                       "chunks":chunks,"compressed_bytes":sum(c["bytes"] for c in chunks)})
    Path(str(PREFIX)+"-"+args.mode+"-result.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ("chunks","sentinels","degree_histogram")}),flush=True)

if __name__=="__main__":
    main()
