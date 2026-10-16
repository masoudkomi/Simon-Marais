#!/usr/bin/env python3
"""Independent J16 L1--L3 review, written before opening constructor code/data.

Own derivation: all 2^17 binary masks, exact zero-parameter normalized
coefficients, exact linear recurrences, and direct modular monic division.
No constructor or review-2 import.  The scalar recurrence uses every term,
with vanishing terms removed only by computing their modular coefficient.
"""
import argparse
import collections
import gzip
import hashlib
import itertools
import json
import math
from pathlib import Path
import sys
import time

P = 19
CH = [[math.comb(j, k) for k in range(j + 1)] for j in range(21)]
BETA = [0, 0] + [math.comb(20, j) // P for j in range(2, 19)]
BASE = Path(__file__).resolve().parents[1]


def encoded(x):
    return (json.dumps(x, separators=(",", ":")) + "\n").encode()


def valuation(x):
    assert x
    r = 0
    while x % P == 0:
        x //= P
        r += 1
    return r


def center(mask, j):
    return bool(mask & (1 << (j - 2)))


def mask_list():
    """Independent enumeration of the accepted necessary J16 binary masks."""
    out = []
    for mask in range(1 << 17):
        aa = [1, -1]
        for j in range(2, 19):
            aa.append(-sum(CH[j][k] * aa[k] for k in range(j)) % P
                      if center(mask, j) else 0)
        if aa[16] == 0 or aa[17] != 0 or aa[18] != 0:
            continue
        if not (center(mask, 17) or center(mask, 18)):
            continue
        if (-1 + sum(BETA[j] * aa[j] for j in range(2, 19))) % P:
            continue
        out.append(mask)
    return out


def constant_coefficients(mask):
    aa = [1, -1]
    for j in range(2, 19):
        aa.append(-sum(CH[j][k] * aa[k] for k in range(j))
                  if center(mask, j) else 0)
    return aa


def linear_rows(mask, umask, vmask, aa):
    ax, ay = [0, 0], [0, 0]
    for j in range(2, 19):
        if center(mask, j):
            ax.append(-sum(CH[j][k] * ax[k] for k in range(j)) % P)
            ay.append(-sum(CH[j][k] * ay[k] for k in range(j)) % P)
        else:
            bit = 1 << (j - 2)
            ax.append((-j * aa[j - 1]) % P if umask & bit else 0)
            ay.append((-j * aa[j - 1]) % P if vmask & bit else 0)
    return ax, ay, [
        [sum(BETA[j] * ax[j] for j in range(2, 19)) % P,
         sum(BETA[j] * ay[j] for j in range(2, 19)) % P],
        [ax[18], ay[18]],
        [(BETA[17] * ax[17] + BETA[16] * aa[16]) % P,
         (BETA[17] * ay[17] + BETA[16] * aa[16]) % P],
    ]


def assignments(positions):
    for labels in itertools.product(range(3), repeat=len(positions)):
        uu = vv = 0
        for j, label in zip(positions, labels):
            if label == 1:
                uu |= 1 << (j - 2)
            elif label == 2:
                vv |= 1 << (j - 2)
        yield uu, vv


def allowed_pair(mask, x, y):
    if x == y == 0:
        return False
    h2, h3 = center(mask, 18), center(mask, 17)
    if h2 and h3:
        return True
    if not x or not y:
        return False
    if h2:
        return (x + y) % P == 0 or (3*x-y) % P == 0 or (3*y-x) % P == 0
    assert h3
    return (3*x-2*y) % P == 0 or (3*y-2*x) % P == 0


def leading_cover():
    data = {}
    branches = []
    checks = 0
    bounds = collections.Counter()
    for mask in mask_list():
        aa = constant_coefficients(mask)
        q0 = -1 + sum(BETA[j] * aa[j] for j in range(2, 19))
        assert q0 != 0
        bound = valuation(q0)
        bounds[bound] += 1
        active = [j for j in range(2, 19)
                  if not center(mask, j) and aa[j-1] % P]
        inactive = [j for j in range(2, 19)
                    if not center(mask, j) and not aa[j-1] % P]
        data[mask] = dict(a0=aa, q0=q0, bound=bound,
                          active=active, inactive=inactive)
        for umask, vmask in assignments(active):
            ax, ay, rows = linear_rows(mask, umask, vmask, aa)
            for nu in range(1, bound + 1):
                checks += 1
                q = P**nu
                if aa[17] % q or aa[18] % q:
                    continue
                const = [q0 // q % P, aa[18] // q % P,
                         BETA[17] * (aa[17] // q) % P]
                for x in range(P):
                    for y in range(P):
                        if not allowed_pair(mask, x, y):
                            continue
                        if all((c + row[0]*x + row[1]*y) % P == 0
                               for c, row in zip(const, rows)):
                            branches.append((mask, umask, vmask, nu, x, y))
        print(json.dumps({"phase":"leading-mask", "mask":mask,
                          "branches_so_far":len(branches)}), flush=True)
    return data, branches, checks, dict(bounds)


def expanded_keys(data, branches):
    for mask, umask, vmask, nu, x, y in branches:
        for extra_u, extra_v in assignments(data[mask]["inactive"]):
            yield mask, umask | extra_u, vmask | extra_v, nu, x, y


_mult = {}


def scalar_coefficients(mask, umask, vmask, nu, x, y):
    """Full normalized Hasse recurrence modulo 19^(nu+2)."""
    modulus = P**(nu+2)
    q = P**nu
    aa = [1, -1]
    for j in range(2, 19):
        bit = 1 << (j-2)
        w = 1 if mask & bit else q*x if umask & bit else q*y if vmask & bit else 0
        if not w:
            aa.append(0)
            continue
        key = nu, w, j
        if key not in _mult:
            # All j lower coefficients are considered; omission below is
            # solely their actually computed coefficient being 0 modulo M.
            _mult[key] = [(k, (-CH[j][k] * pow(w, j-k, modulus)) % modulus)
                          for k in range(j)]
            _mult[key] = [(k, z) for k, z in _mult[key] if z]
        aa.append(sum(aa[k] * z for k, z in _mult[key]) % modulus)
    return aa


def direct_constants(mask, umask, vmask, nu, x, y):
    aa = scalar_coefficients(mask, umask, vmask, nu, x, y)
    q = P**nu
    scalar_mod = P**(nu+2)
    rem_mod = P**(nu+3)
    divided_p = (-1 + sum(BETA[j] * aa[j] for j in range(2,19))) % scalar_mod
    # F=f(Z)/Z^2 has coefficient c_(k+2) at exponent k.
    ff = [(math.comb(20, 18-k) * aa[18-k]) % rem_mod for k in range(17)]
    ff += [-20 % rem_mod, 1]
    s = q*(x+y)
    t = q*q*x*y
    for k in range(18, 1, -1):
        high = ff[k]
        ff[k-1] = (ff[k-1] + s*high) % rem_mod
        ff[k-2] = (ff[k-2] - t*high) % rem_mod
    denom = P**(nu+2)
    assert divided_p % (P*q) == 0, ("center-divisibility", mask, umask, vmask, nu, x, y)
    assert ff[0] % denom == 0, ("R0-divisibility", mask, umask, vmask, nu, x, y)
    assert ff[1] % denom == 0, ("R1-divisibility", mask, umask, vmask, nu, x, y)
    cc = [divided_p // (P*q) % P,
          (ff[0] // denom) * pow(BETA[18], -1, P) % P,
          ff[1] // denom % P]
    return aa, cc


def affine(rows, constants):
    """Independently Gaussian-eliminate the augmented 3-by-3 matrix."""
    mat = [[r[0] % P, r[1] % P, -c % P] for r, c in zip(rows, constants)]
    rank = 0
    for col in range(2):
        pivot = next((i for i in range(rank, 3) if mat[i][col]), None)
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inv = pow(mat[rank][col], -1, P)
        mat[rank] = [(z*inv) % P for z in mat[rank]]
        for i in range(3):
            if i != rank:
                f = mat[i][col]
                mat[i] = [(a-f*b) % P for a, b in zip(mat[i], mat[rank])]
        rank += 1
    return rank, not any(r[0] == r[1] == 0 and r[2] != 0 for r in mat)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--certificates", nargs="*")
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    started = time.monotonic()
    data, branches, checks, bounds = leading_cover()
    leading_masks = sorted(set(b[0] for b in branches))
    expected = set(expanded_keys(data, branches))
    assert len(expected) == sum(3**len(data[b[0]]["inactive"]) for b in branches)
    result = dict(status="incomplete", constructor_imports=False,
                  independent_mask_list=sorted(data), leading_checks=checks,
                  valuation_bounds=bounds, projected_branches=len(branches),
                  projected_branches_by_nu=dict(collections.Counter(b[3] for b in branches)),
                  expanded_keys=len(expected), leading_retained=leading_masks,
                  leading_excluded=sorted(set(data)-set(leading_masks)))
    print(json.dumps({"phase":"cover-ready", **result}), flush=True)
    totals = collections.Counter()
    passed = collections.Counter()
    rows_hash = hashlib.sha256()
    own_coeff_hash = hashlib.sha256()
    n = 0
    def source():
        if args.certificates:
            for path in args.certificates:
                with gzip.open(path, "rt") as fd:
                    for line in fd:
                        yield json.loads(line), line.encode()
        else:
            for key in expanded_keys(data, branches):
                yield list(key), None
    for saved, raw in source():
        key = tuple(saved[:6])
        assert key in expected, ("unexpected-or-duplicate", key)
        expected.remove(key)
        mask, umask, vmask, nu, x, y = key
        aa, constants = direct_constants(*key)
        _, _, jrows = linear_rows(mask, umask, vmask, data[mask]["a0"])
        rank, consistent = affine(jrows, constants)
        row = list(key) + constants + [rank, consistent]
        if raw is not None:
            assert saved == row, ("row-mismatch", saved, row)
            rows_hash.update(raw)
        else:
            rows_hash.update(encoded(row))
        # This is the reviewer's own explicit scalar stream encoding.
        own_coeff_hash.update(encoded([*key, aa]))
        totals[(nu, rank, consistent)] += 1
        if consistent:
            passed[mask] += 1
        n += 1
        if n % 8192 == 0:
            print(json.dumps({"phase":"scalar-checkpoint", "checked":n,
                              "seconds":round(time.monotonic()-started,3)}), flush=True)
        if args.limit and n >= args.limit:
            break
    result.update(status="complete" if not expected else "incomplete",
                  records_checked=n, missing_keys=len(expected),
                  row_stream_sha256=rows_hash.hexdigest(),
                  own_scalar_stream_sha256=own_coeff_hash.hexdigest(),
                  affine_counts=[{"nu":k[0],"rank":k[1],"consistent":k[2],"count":v}
                                 for k,v in sorted(totals.items())],
                  next_retained=sorted(passed),
                  next_extra_excluded=sorted(set(leading_masks)-set(passed)),
                  next_all_excluded=sorted(set(data)-set(passed)),
                  seconds=round(time.monotonic()-started,3),
                  python=sys.version)
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    print(json.dumps({"phase":"finished", **result}), flush=True)


if __name__ == "__main__":
    main()
