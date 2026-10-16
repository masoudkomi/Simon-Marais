#!/usr/bin/env python3
"""Construct all binary degree-20 center masks; no rational-only filters.

Construction, not independent review.  Reduction uses the residue field of
a possibly ramified extension of Q_19.  Noncenter a_j reduce to zero there;
we do NOT assert they are divisible by 19 in its valuation ring.
"""
from collections import Counter
from pathlib import Path
import hashlib,json,math,time

HERE=Path(__file__).resolve().parent
OLD=HERE.parent/'reviews/newton-review-1-extension-result.json'
OUT=HERE/'coordinator-three-complex-masks-v1-result.json'

def main():
    start=time.monotonic()
    bins=[[math.comb(j,k) for k in range(j+1)] for j in range(21)]
    a=[1,-1]+[0]*17
    masks=[];hist=Counter();refinements=Counter();leaves=0
    def visit(j,mask):
        nonlocal leaves
        if j==19:
            leaves+=1
            if (-1+sum((bins[20][k]//19)*a[k] for k in range(2,19)))%19:
                return
            unit_indices=[k for k in range(2,19) if a[k]%19]
            assert unit_indices
            top=max(unit_indices)
            masks.append(mask);hist[top]+=1
            refinements[top]+=2**(17-mask.bit_count())
            return
        a[j]=0;visit(j+1,mask)
        a[j]=-sum(bins[j][k]*a[k] for k in range(j))%19
        visit(j+1,mask|(1<<(j-2)))
        a[j]=0
    visit(2,0)
    masks.sort()
    old=sorted(json.loads(OLD.read_text())['combined_with_prior_j17_exclusion_masks'])
    assert leaves==131072 and len(masks)==len(set(masks))==6680
    assert len(old)==len(set(old))==772 and set(old)<=set(masks)
    additional=sorted(set(masks)-set(old))
    total=sum(2**(17-m.bit_count()) for m in masks)
    old_count=sum(2**(17-m.bit_count()) for m in old)
    additional_count=sum(2**(17-m.bit_count()) for m in additional)
    assert (total,old_count,len(additional),additional_count)==(6224952,1493024,5908,4731928)
    result={'status':'complete finite mask construction; unverified complex coverage',
        'binary_leaves':leaves,'center_masks':masks,'center_mask_count':len(masks),
        'J_histogram':dict(sorted(hist.items())),
        'J_refinement_histogram':dict(sorted(refinements.items())),
        'all_refinements':total,'previously_certified_center_masks':old,
        'previously_certified_refinements':old_count,
        'additional_center_masks':additional,'additional_refinements':additional_count,
        'previous_mask_source':str(OLD.relative_to(HERE.parents[2])),
        'previous_mask_source_sha256':hashlib.sha256(OLD.read_bytes()).hexdigest(),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'elapsed_seconds':time.monotonic()-start}
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if not isinstance(v,list)},sort_keys=True),flush=True)

if __name__=='__main__':main()
