#!/usr/bin/env python3
"""R1 independent ordinary-Hasse reconstruction, frozen before raw certificates.

No constructor module is imported or executed. Integers in ascending U-degree.
For the unknown coefficient c_l, H_l(f)(w)=0 gives
c_l=-sum_{t=l+1}^{20} C(t,l)c_t w**(t-l), directly in ordinary coefficients.
"""
import argparse
import collections
import gzip
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
PREFIX = Path(__file__).with_name("three-witness-review-1")
COMPUTATIONS = ROOT / "problems/2021-B4/computations"
CHOOSE = [[math.comb(t, l) for l in range(t+1)] for t in range(21)]
FULL = (1 << 17) - 1

def trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly

def independently_enumerate_masks():
    # Ordinary coefficients are reconstructed modulo 19^2. A noncenter
    # rational witness belongs to 19 Z_(19), forcing c_l=0 modulo 19^2.
    masks = []
    hist = collections.Counter()
    passes = []
    for mask in range(1 << 17):
        ordinary = [0] * 21
        ordinary[20], ordinary[19] = 1, -20
        for l in range(18, 1, -1):
            if mask & (1 << (18-l)):
                ordinary[l] = -sum(CHOOSE[t][l] * ordinary[t]
                                   for t in range(l+1, 21)) % 361
            assert ordinary[l] % 19 == 0
        if sum(ordinary) % 361:
            continue
        units = [20-l for l in range(2,19) if ordinary[l] % 361]
        assert units
        J = max(units)
        hist[J] += 1
        passes.append(mask)
        if J in (17,18):
            continue
        if J == 16 and not mask & ((1 << 15) | (1 << 16)):
            continue
        if J == 15 and not mask & ((1 << 14) | (1 << 15) | (1 << 16)):
            continue
        masks.append((mask, J))
    assert len(set(m for m,_ in masks)) == len(masks)
    return masks, passes, dict(sorted(hist.items()))

def make_coefficient(ordinary, l, witness):
    if witness == 0:
        return [0]
    output = [0] * (21-l)
    for t in range(l+1,21):
        scalar = -CHOOSE[t][l]
        shift = t-l if witness == 2 else 0
        for e, value in enumerate(ordinary[t]):
            output[e+shift] += scalar * value
    return trim(output)

def construct_pair(ordinary):
    p = [0] * 19
    q = [0] * 21
    for l in range(2,21):
        for e,value in enumerate(ordinary[l]):
            p[e] += value
            q[e+l] += value
    return trim(p), trim(q)

def families(mask):
    ordinary = [[0] for _ in range(21)]
    ordinary[20], ordinary[19] = [1], [-20]
    def descend(l, umask):
        if l == 1:
            p,q = construct_pair(ordinary)
            yield umask,p,q
            return
        bit = 1 << (18-l)
        choices = (1,) if mask & bit else (0,2)
        for witness in choices:
            ordinary[l] = make_coefficient(ordinary,l,witness)
            assert all(value % CHOOSE[20][l] == 0 for value in ordinary[l])
            yield from descend(l-1, umask | bit if witness == 2 else umask)
    yield from descend(18,0)

def coprime_modulo(p, q, prime):
    a = trim([c % prime for c in p])
    b = trim([c % prime for c in q])
    if not a[-1] or not b[-1]:
        return False
    while len(b)>1 or b[0]:
        inverse = pow(b[-1],-1,prime)
        while len(a)>=len(b) and (len(a)>1 or a[0]):
            shift = len(a)-len(b)
            multiplier = a[-1]*inverse % prime
            # Remove the leading term exactly; update the remaining ones.
            a.pop()
            for e in range(len(b)-1):
                a[e+shift] = (a[e+shift]-multiplier*b[e]) % prime
            if not a:
                a=[0]
            trim(a)
        a,b = b,a
    return len(a)==1 and a[0]!=0

def independently_certify(p,q):
    if len(p)==1 and p[0]:
        return 0
    for prime in (101,103,107,109,127,131):
        if p[-1] % prime and q[-1] % prime and coprime_modulo(p,q,prime):
            return prime
    raise AssertionError(("No certificate",p,q))

def raw_certificate_groups():
    # This adapter is inactive during the pre-raw freeze/mask stage.
    hasher = hashlib.sha256()
    chunks=[]
    def rows():
        paths=sorted(COMPUTATIONS.glob("coordinator-three-witness-v2-certificates-*.jsonl.gz"))
        assert len(paths)==25
        for path in paths:
            n=0
            with gzip.open(path,"rb") as stream:
                for line in stream:
                    n+=1
                    hasher.update(line)
                    yield json.loads(line)
            chunks.append({"path":str(path.relative_to(ROOT)),"rows":n,
                           "sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
                           "bytes":path.stat().st_size})
    return itertools.groupby(rows(),lambda row:row[0]),hasher,chunks

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode",choices=("masks","benchmark","full"),default="masks")
    parser.add_argument("--limit",type=int,default=8192)
    args=parser.parse_args()
    start=time.monotonic()
    masks,passes,hist=independently_enumerate_masks()
    derived={"all_binary_choices":1<<17,"congruence_passes":len(passes),
             "J_histogram_before_exclusions":hist,"retained":len(masks),
             "retained_J_histogram":dict(collections.Counter(j for _,j in masks)),
             "refinement_count":sum(1 << (17-m.bit_count()) for m,_ in masks),
             "masks":[m for m,_ in masks]}
    Path(str(PREFIX)+"-independent-masks.json").write_text(json.dumps(derived,indent=2)+"\n")
    print(json.dumps({"event":"independently_derived_masks","pid":os.getpid(),
                     **{k:v for k,v in derived.items() if k!="masks"}}),flush=True)
    if args.mode=="masks":
        return
    counts=collections.Counter()
    total=0
    key_hasher=hashlib.sha256()
    polynomial_hasher=hashlib.sha256()
    if args.mode=="full":
        groups,stream_hasher,chunks=raw_certificate_groups()
    degree_hist=collections.Counter()
    sentinel=[]
    # Author's serialized polynomial adapter is set only after initial freeze.
    def serialized_pair(m,u,p,q):
        return json.dumps([m,u,p,q],separators=(",",":")).encode()+b"\n"
    for mask,J in masks:
        expected=1 << (17-mask.bit_count())
        raw={}
        if args.mode=="full":
            group_mask,group=next(groups)
            assert group_mask==mask,("Unexpected mask order",group_mask,mask)
            for row in group:
                umask=row[1]
                assert umask>=0 and not umask & mask and not umask & ~FULL
                assert umask not in raw,("Duplicate raw refinement",mask,umask)
                raw[umask]=row
            assert len(raw)==expected,("Wrong raw coverage",mask,len(raw),expected)
        seen=set()
        for umask,p,q in families(mask):
            assert not umask & mask and not umask & ~FULL and umask not in seen
            seen.add(umask)
            prime=independently_certify(p,q)
            counts[prime]+=1
            degree_hist[(len(p)-1,len(q)-1)]+=1
            key_hasher.update(f"{mask},{umask}\n".encode())
            polynomial_hasher.update(serialized_pair(mask,umask,p,q))
            if args.mode=="full":
                row=raw.pop(umask)
                recorded=row[2]
                if recorded==0:
                    assert len(row)==4 and len(p)==1 and p[0]==row[3]!=0
                    assert prime==0
                elif recorded==-1:
                    sentinel.append({"mask":mask,"U_mask":umask,"P":p,"Q":q,
                                     "prime":prime,"degrees":[len(p)-1,len(q)-1],
                                     "leading_residues":[p[-1]%prime,q[-1]%prime]})
                    assert (mask,umask)==(6436,24785) and prime==131
                else:
                    assert len(row)==7 and recorded==prime
                    assert row[3:]==[len(p)-1,len(q)-1,p[-1]%prime,q[-1]%prime]
            total+=1
            if total%8192==0:
                print(json.dumps({"event":"checkpoint","families":total,
                                  "seconds":round(time.monotonic()-start,3),
                                  "mask":mask}),flush=True)
            if args.mode=="benchmark" and total>=args.limit:
                break
        if args.mode=="benchmark" and total>=args.limit:
            break
        assert len(seen)==expected and not raw
    if args.mode=="full":
        assert next(groups,None) is None
        assert total==derived["refinement_count"]==1493024
        assert len(sentinel)==1
    result={"event":"complete","mode":args.mode,"pid":os.getpid(),
            "families":total,"elapsed_seconds":time.monotonic()-start,
            "certificate_histogram":dict(counts),"sentinel":sentinel,
            "degree_histogram":{str(key):value for key,value in sorted(degree_hist.items())},
            "key_stream_sha256":key_hasher.hexdigest(),
            "polynomial_stream_sha256":polynomial_hasher.hexdigest()}
    if args.mode=="full":
        result.update({"uncompressed_certificate_stream_sha256":stream_hasher.hexdigest(),
                       "chunks":chunks,"compressed_bytes":sum(c["bytes"] for c in chunks)})
    Path(str(PREFIX)+"-"+args.mode+"-result.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result),flush=True)

if __name__=="__main__":
    main()
