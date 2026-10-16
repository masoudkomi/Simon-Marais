#!/usr/bin/env python3
"""Independent R2 arithmetic; written before reading constructor program/data.

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
PREFIX = ROOT / "problems/2021-B4/reviews/three-witness-review-2"
CHOOSE = [[math.comb(t, l) if t >= l else 0 for t in range(21)] for l in range(21)]
FULL = (1 << 17) - 1


def dump(path, obj):
    Path(path).write_text(json.dumps(obj, sort_keys=True, indent=2) + "\n")


def trim(poly):
    while len(poly) > 1 and not poly[-1]:
        poly.pop()
    return poly


def derive_masks():
    """Independent full 2^17 ordinary-Hasse recursion over Z/(19^2)."""
    c = [0] * 21
    c[20], c[19] = 1, -20
    passed = []
    kept = []
    histogram = collections.Counter()
    checks = 0

    def visit(l, mask):
        nonlocal checks
        if l == 1:
            checks += 1
            if sum(c) % 361:
                return
            js = [20 - t for t in range(2, 19) if c[t] % 361]
            assert js
            J = max(js)
            passed.append(mask)
            histogram[J] += 1
            if J >= 17:
                return
            if J == 16 and not (mask & ((1 << 16) | (1 << 15))):
                return
            if J == 15 and not (mask & ((1 << 16) | (1 << 15) | (1 << 14))):
                return
            kept.append((mask, J))
            return
        c[l] = 0
        visit(l - 1, mask)
        c[l] = -sum(CHOOSE[l][t] * c[t] for t in range(l + 1, 21)) % 361
        assert c[l] % 19 == 0
        visit(l - 1, mask | (1 << (18 - l)))
        c[l] = 0

    visit(18, 0)
    kept.sort()
    masks = [m for m, _ in kept]
    assert checks == 131072 and len(passed) == 6680
    assert len(masks) == 772 and len(set(masks)) == 772
    result = {"method": "ordinary Hasse coefficients modulo 361", "visited": checks,
              "passed_congruence": len(passed), "histogram": dict(sorted(histogram.items())),
              "masks": masks, "survivor_J_histogram": dict(sorted(collections.Counter(J for _, J in kept).items())),
              "family_count": sum(1 << (17 - m.bit_count()) for m in masks)}
    assert result["family_count"] == 1493024
    return result


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["derive", "benchmark", "full"])
    parser.add_argument("--limit", type=int, default=8192)
    args = parser.parse_args()
    started = time.monotonic()
    selftest()
    mask_result = derive_masks()
    dump(str(PREFIX) + "-independent-masks.json", mask_result)
    print(json.dumps({"event": "independent-mask-derivation", **{k:v for k,v in mask_result.items() if k != "masks"},
                      "seconds": time.monotonic() - started}), flush=True)
    if args.mode == "derive":
        return
    if args.mode == "benchmark":
        count = 0
        histogram = collections.Counter()
        for mask in mask_result["masks"]:
            for umask, (P, Q) in families(mask):
                count += 1
                if len(P) == 1:
                    assert P[0]
                    histogram[0] += 1
                else:
                    for p in [101,103,107,109,127,131]:
                        if P[-1] % p and Q[-1] % p and len(gcd_mod(P,Q,p)) == 1:
                            histogram[p] += 1
                            break
                    else:
                        raise AssertionError((mask,umask,"no prime"))
                if count >= args.limit:
                    print(json.dumps({"event":"benchmark", "count":count, "histogram":dict(histogram), "seconds":time.monotonic()-started}), flush=True)
                    return
    raise RuntimeError("Full raw-certificate comparison will be added only after freezing independent construction.")


if __name__ == "__main__":
    main()
