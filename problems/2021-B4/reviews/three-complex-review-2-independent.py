#!/usr/bin/env python3
"""Independent complex-extension R2 arithmetic, adapted only from my frozen rational R2.

Uses ordinary coefficients c_t of f, and solves H_l(f)(w)=0 for c_l.
No constructor/reviewer module is imported. Ascending dense U coefficients.
"""
import argparse
import collections
import gzip
import hashlib
import json
import math
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
PREFIX = ROOT / "problems/2021-B4/reviews/three-complex-review-2"
CHOOSE = [[math.comb(t, l) if t >= l else 0 for t in range(21)] for l in range(21)]
FULL = (1 << 17) - 1


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n")


def trim(poly):
    while len(poly) > 1 and not poly[-1]:
        poly.pop()
    return poly


def derive_masks():
    """Normalized Hasse equations over the prime field, valid with ramification.

    This does not interpret noncenter c_l as zero modulo 361 in O_K.
    Only a_j modulo the maximal ideal is set to zero on a noncenter branch.
    """
    a = [0] * 19
    a[0],a[1] = 1,18
    b = [0,0] + [math.comb(20,j)//19 for j in range(2,19)]
    assert all(math.comb(20,j)%19 == 0 and b[j]%19 for j in range(2,19))
    visited = 0
    masks = []
    histogram = collections.Counter()

    def visit(j,mask):
        nonlocal visited
        if j == 19:
            visited += 1
            if (sum(b[k]*a[k] for k in range(2,19))-1)%19 == 0:
                masks.append(mask)
                J = max(k for k in range(2,19) if a[k])
                histogram[J] += 1
            return
        a[j] = 0
        visit(j+1,mask)
        a[j] = -sum(math.comb(j,k)*a[k] for k in range(j))%19
        visit(j+1,mask|(1<<(j-2)))
        a[j] = 0

    visit(2,0)
    masks.sort()
    assert visited == 131072 and len(masks) == len(set(masks)) == 6680
    oldpath = ROOT / "problems/2021-B4/reviews/three-witness-review-2-independent-masks.json"
    oldbytes = oldpath.read_bytes()
    assert hashlib.sha256(oldbytes).hexdigest() == "c72bfadb19594d425ba967a697eaf4813d04a03730fdf8e7f01948c5f6b2b2ed"
    oldmasks = json.loads(oldbytes)["masks"]
    assert len(oldmasks) == len(set(oldmasks)) == 772 and set(oldmasks) <= set(masks)
    oldset = set(oldmasks)
    newmasks = [m for m in masks if m not in oldset]
    count = lambda ms:sum(1 << (17-m.bit_count()) for m in ms)
    assert len(newmasks) == 5908 and count(masks) == 6224952
    assert count(oldmasks) == 1493024 and count(newmasks) == 4731928
    return {"method":"normalized Hasse equations in F19, no rational-only filter", "visited":visited,
            "mask_count":len(masks),"masks":masks,"histogram":dict(sorted(histogram.items())),
            "old_accepted_masks":oldmasks,"old_count":len(oldmasks),"old_families":count(oldmasks),
            "new_masks":newmasks,"new_count":len(newmasks),"new_families":count(newmasks),
            "union_families":count(masks),"old_mask_source_sha256":hashlib.sha256(oldbytes).hexdigest()}


def solve_coefficient(c, l, w):
    """H_l = c_l + sum_{t>l} binom(t,l)c_t*w^(t-l)."""
    if w == 0:
        return [0]
    out = [0] * (21 - l)
    for t in range(l + 1, 21):
        weight = CHOOSE[l][t]
        offset = t - l if w == 2 else 0
        for e, value in enumerate(c[t]):
            out[e + offset] -= weight * value
    return trim(out)


def form_pair(c):
    P = [0] * 21
    Q = [0] * 21
    for t in range(2, 21):
        for e, val in enumerate(c[t]):
            P[e] += val
            Q[e + t] += val
    return trim(P), trim(Q)


def families(mask):
    c = [[0] for _ in range(21)]
    c[20], c[19] = [1], [-20]

    def visit(l, umask):
        if l == 1:
            yield umask, form_pair(c)
            return
        bit = 1 << (18 - l)
        if mask & bit:
            c[l] = solve_coefficient(c, l, 1)
            yield from visit(l - 1, umask)
        else:
            c[l] = [0]
            yield from visit(l - 1, umask)
            c[l] = solve_coefficient(c, l, 2)
            yield from visit(l - 1, umask | bit)
        c[l] = [0]

    yield from visit(18, 0)


def prime(p):
    return p >= 2 and all(p % d for d in range(2, math.isqrt(p) + 1))


def gcd_mod(a, b, p):
    a = trim([n % p for n in a])
    b = trim([n % p for n in b])
    while b != [0]:
        inv = pow(b[-1], -1, p)
        while a != [0] and len(a) >= len(b):
            factor = a[-1] * inv % p
            offset = len(a) - len(b)
            for i in range(len(b)):
                a[i + offset] = (a[i + offset] - factor * b[i]) % p
            trim(a)
        a, b = b, a
    return trim(a)


def selftest():
    # Direct literal Hasse equation checks at many values, independent of the
    # polynomial-construction formula's U shifts. These test all 17 equations.
    for mask in [0, 3, 15, FULL, 6436]:
        for index, (umask, (P, Q)) in enumerate(families(mask)):
            if index >= 4:
                break
            for u in [-3, 0, 1, 2, 7]:
                scalar = [0] * 21
                scalar[20], scalar[19] = 1, -20
                for l in range(18, 1, -1):
                    bit = 1 << (18 - l)
                    w = 1 if mask & bit else u if umask & bit else 0
                    scalar[l] = -sum(CHOOSE[l][t] * scalar[t] * w ** (t - l)
                                     for t in range(l + 1, 21))
                assert sum(P[e] * u ** e for e in range(len(P))) == sum(scalar)
                assert sum(Q[e] * u ** e for e in range(len(Q))) == sum(scalar[t] * u ** t for t in range(21))
    for p in [101, 103, 107, 109, 127, 131]:
        assert prime(p)
        assert len(gcd_mod([1, 0, 1], [1, 1], p)) == 1
        assert len(gcd_mod([-1, 0, 1], [-1, 1], p)) == 2


def full_audit(mask_result):
    """Every new family; normalized mask coverage and accepted old finite facts."""
    start = time.monotonic()
    problem = ROOT / "problems/2021-B4"
    masks = mask_result["new_masks"]
    constructed_masks = json.loads((problem/"computations/coordinator-three-complex-masks-v1-result.json").read_text())
    assert constructed_masks["center_masks"] == mask_result["masks"]
    assert constructed_masks["additional_center_masks"] == masks
    assert constructed_masks["previously_certified_center_masks"] == mask_result["old_accepted_masks"]
    assert constructed_masks["binary_leaves"] == 131072
    assert constructed_masks["all_refinements"] == 6224952
    assert constructed_masks["additional_refinements"] == 4731928
    assert constructed_masks["previously_certified_refinements"] == 1493024
    assert constructed_masks["J_histogram"] == {str(k):v for k,v in mask_result["histogram"].items()}
    oldfreeze = problem/"reviews/three-witness-review-2-freeze.json"
    assert hashlib.sha256(oldfreeze.read_bytes()).hexdigest() == "68379652537bfa8f0b29e5d9304c5ab19d79a1c2bb63e295d288a76d13a6ec21"
    for item in json.loads(oldfreeze.read_text())["artifacts"]:
        raw = (ROOT/item["path"]).read_bytes()
        assert len(raw) == item["bytes"] and hashlib.sha256(raw).hexdigest() == item["sha256"]
    oldresult_path = problem/"reviews/three-witness-review-2-full-result.json"
    oldresult = json.loads(oldresult_path.read_text())
    assert oldresult["families_verified"] == 1493024 and oldresult["all_certificates_verified"]
    assert oldresult["sentinels_resolved_independently"][0]["center_mask"] == 6436
    assert oldresult["sentinels_resolved_independently"][0]["u_mask"] == 24785
    assert oldresult["polynomial_stream_sha256"] == "aa5cd774ea5d10dcbb52a5bcee0d289d807ec7a364fd5921f29c9b412dda8cad"
    result = json.loads((problem/"computations/coordinator-three-complex-witnesses-v1-result.json").read_text())
    chunks = result["chunks"]
    assert len(chunks) == 79
    assert [Path(c["path"]).name for c in chunks] == [f"coordinator-three-complex-witnesses-v1-certificates-{i:03}.jsonl.gz" for i in range(1,80)]
    prime_list = [101,103,107,109,127,131]
    assert all(prime(p) for p in prime_list)
    stream_digest = hashlib.sha256()
    polynomial_digest = hashlib.sha256()
    chunk_checks = []
    compressed_bytes = 0

    def rows():
        nonlocal compressed_bytes
        for item in chunks:
            path = ROOT/item["path"]
            raw = path.read_bytes()
            h = hashlib.sha256(raw).hexdigest()
            assert len(raw) == item["bytes"] and h == item["sha256"]
            compressed_bytes += len(raw)
            n = 0
            with gzip.open(path,"rb") as handle:
                for line in handle:
                    stream_digest.update(line)
                    row = json.loads(line)
                    assert isinstance(row,list) and all(type(v) is int for v in row)
                    assert (json.dumps(row,separators=(",",":"))+"\n").encode() == line
                    n += 1
                    yield row
            assert n == item["rows"]
            chunk_checks.append({"path":item["path"],"rows":n,"sha256":h,"bytes":len(raw)})

    raw_rows = iter(rows())
    unresolved_lines = (problem/"computations/coordinator-three-complex-witnesses-v1-unresolved.jsonl").read_text().splitlines()
    assert len(unresolved_lines) == 3
    unresolved = {}
    for line in unresolved_lines:
        r = json.loads(line)
        key = (r["center_mask"],r["u_mask"])
        assert key not in unresolved
        unresolved[key] = r
    expected_sentinels = {(117075,9220),(117075,1548),(117075,9356)}
    assert set(unresolved) == expected_sentinels
    resolver = json.loads((problem/"computations/coordinator-three-complex-witnesses-v1-resolve-result.json").read_text())
    assert resolver["resolved"] == 3 and resolver["unresolved"] == 0 and len(resolver["cases"]) == 3
    resolver_map = {(r["center_mask"],r["u_mask"]):r for r in resolver["cases"]}
    assert set(resolver_map) == expected_sentinels
    count = 0
    histogram = collections.Counter()
    degree_histogram = collections.Counter()
    sentinels = []
    for mask in masks:
        seen_u = set()
        for umask,(P,Q) in families(mask):
            row = next(raw_rows)
            assert row[:2] == [mask,umask]
            assert not (mask&umask) and (mask|umask) <= FULL and umask not in seen_u
            seen_u.add(umask)
            polynomial_digest.update((json.dumps([mask,umask,P,Q],separators=(",",":"))+"\n").encode())
            count += 1
            degree_histogram[(len(P)-1,len(Q)-1)] += 1
            if row[2] == 0:
                assert len(row) == 4 and len(P) == 1 and P[0] and row[3] == P[0]
                histogram["constant_nonzero"] += 1
            else:
                if row[2] == -1:
                    key = (mask,umask)
                    assert row == [mask,umask,-1] and key in expected_sentinels
                    r = unresolved[key]
                    assert r == {"center_mask":mask,"u_mask":umask,"P":P,"Q":Q}
                    rc = resolver_map[key]
                    record_hash = hashlib.sha256(json.dumps(r,sort_keys=True,separators=(",",":")).encode()).hexdigest()
                    assert record_hash == rc["raw_record_sha256"]
                    assert rc["status"] == "coprime_mod_prime" and rc["gcd_degree"] == 0
                    p = rc["prime"]
                    assert p == 131 and rc["degrees"] == [len(P)-1,len(Q)-1]
                    leads = rc["leading_residues"]
                    sentinels.append({"center_mask":mask,"u_mask":umask,"prime":p,"degrees":[len(P)-1,len(Q)-1],"leading_residues":leads,"raw_record_sha256":record_hash})
                else:
                    assert len(row) == 7 and row[2] in prime_list[:-1]
                    p = row[2]
                    assert row[3:5] == [len(P)-1,len(Q)-1]
                    leads = row[5:7]
                assert p in prime_list and leads == [P[-1]%p,Q[-1]%p]
                assert P[-1]%p and Q[-1]%p
                assert len(gcd_mod(P,Q,p)) == 1
                histogram[str(p)] += 1
            if count%16384 == 0:
                print(json.dumps({"event":"checkpoint","visited":count,"mask":mask,"seconds":time.monotonic()-start}),flush=True)
        assert len(seen_u) == 1 << (17-mask.bit_count())
    assert next(raw_rows,None) is None
    assert count == 4731928 and len(sentinels) == 3
    assert {(r["center_mask"],r["u_mask"]) for r in sentinels} == expected_sentinels
    assert compressed_bytes == 28442028
    assert polynomial_digest.hexdigest() == result["polynomial_stream_sha256"]
    assert stream_digest.hexdigest() == result["uncompressed_certificate_stream_sha256"]
    initial_histogram = dict(histogram)
    del initial_histogram["131"]
    assert initial_histogram == result["resolution_histogram"]
    assert sum(initial_histogram.values()) == result["resolved"] == 4731925
    final = {"independent_method":"normalized F19 masks; ordinary Hasse triangular exact integer families; independent modular Euclidean gcd",
             "binary_masks_visited":131072,"all_masks":6680,"old_accepted_masks":772,"new_masks":5908,
             "all_mask_lists_match":True,"complete_unique_refinement_coverage":True,
             "new_families_verified":count,"old_families_accepted_as_finite_algebraic_dependency":1493024,
             "union_families":6224952,"old_R2_freeze_sha256":hashlib.sha256(oldfreeze.read_bytes()).hexdigest(),
             "old_R2_full_result_sha256":hashlib.sha256(oldresult_path.read_bytes()).hexdigest(),
             "all_new_certificates_verified":True,"primes_trial_division_verified":prime_list,
             "histogram":dict(histogram),"polynomial_stream_sha256":polynomial_digest.hexdigest(),
             "uncompressed_certificate_stream_sha256":stream_digest.hexdigest(),"compressed_bytes":compressed_bytes,
             "chunks":chunk_checks,"sentinels_resolved_independently":sentinels,
             "degree_histogram":[{"degreeP":a,"degreeQ":b,"count":n} for (a,b),n in sorted(degree_histogram.items())],
             "seconds":time.monotonic()-start}
    dump(str(PREFIX)+"-full-result.json",final)
    print(json.dumps({"event":"complete",**{k:v for k,v in final.items() if k not in ["chunks","degree_histogram"]}}),flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode",choices=["derive","benchmark","full"])
    parser.add_argument("--limit",type=int,default=8192)
    args = parser.parse_args()
    start = time.monotonic()
    selftest()
    mask_result = derive_masks()
    dump(str(PREFIX)+"-independent-masks.json",mask_result)
    print(json.dumps({"event":"independent-mask-derivation",**{k:v for k,v in mask_result.items() if k not in ["masks","new_masks","old_accepted_masks"]},"seconds":time.monotonic()-start}),flush=True)
    if args.mode == "derive":
        return
    if args.mode == "benchmark":
        count = 0
        histogram = collections.Counter()
        for mask in mask_result["new_masks"]:
            for umask,(P,Q) in families(mask):
                count += 1
                if len(P) == 1:
                    assert P[0]
                    histogram[0] += 1
                else:
                    for p in [101,103,107,109,127,131]:
                        if P[-1]%p and Q[-1]%p and len(gcd_mod(P,Q,p)) == 1:
                            histogram[p] += 1
                            break
                    else:
                        raise AssertionError((mask,umask,"no prime"))
                if count >= args.limit:
                    print(json.dumps({"event":"benchmark","families":count,"histogram":dict(histogram),"seconds":time.monotonic()-start}),flush=True)
                    return
    if args.mode == "full":
        full_audit(mask_result)


if __name__ == "__main__":
    main()


