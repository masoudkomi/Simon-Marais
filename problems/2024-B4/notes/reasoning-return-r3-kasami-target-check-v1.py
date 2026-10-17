"""One targeted composition conjecture check, not a factor or exponent scan.

Question: for q=8, d=q^2-q+1=57 and n=(q^5+1)/(q+1)=3641,
is g_n in F2[g_d]? A saved exact whole-divisor/composition proof is
separate from this finite certificate. Bit i denotes coefficient of U^i.
"""
from pathlib import Path
import hashlib
import json
import time

PREFIX = Path(__file__).with_name("reasoning-return-r3-")
started = time.monotonic()


def mul(a, b):
    out = 0
    while b:
        bit = b & -b
        out ^= a << (bit.bit_length() - 1)
        b ^= bit
    return out


def square(a):
    out = 0
    while a:
        bit = a & -a
        out ^= 1 << (2 * (bit.bit_length() - 1))
        a ^= bit
    return out


def power(a, n):
    out = 1
    while n:
        if n & 1:
            out = mul(out, a)
        a = square(a)
        n >>= 1
    return out


def compose(a, b):
    out = 0
    while a:
        bit = a & -a
        out ^= power(b, bit.bit_length() - 1)
        a ^= bit
    return out


def dickson_pair(n):
    # G_0=0,G_1=1, G_(2m)=G_m^2,
    # G_(2m+1)=G_m*G_(m+1)+U^m.
    if n == 0:
        return 0, 1
    m = n // 2
    p, q = dickson_pair(m)
    odd = mul(p, q) ^ (1 << m)
    return (square(p), odd) if n % 2 == 0 else (odd, square(q))


def support(a):
    return [i for i in range(a.bit_length()) if (a >> i) & 1]


def sha(a):
    payload = str(a).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


q = 8
d = q*q-q+1
n = (q**5+1)//(q+1)
assert (d, n) == (57, 3641)
print(json.dumps({"stage": "start", "q": q, "d": d, "n": n}), flush=True)
polys = {}
independent = []
for exponent in (d, n):
    polynomial = dickson_pair(exponent)[0]
    # Independent direct identity after U=X^2+X, using Frobenius product.
    direct = power(3, exponent) ^ (1 << exponent)
    substituted = compose(polynomial, 6)
    assert substituted == direct
    assert polynomial.bit_length()-1 == (exponent-1)//2
    polys[exponent] = polynomial
    independent.append({"exponent": exponent, "g_support": support(polynomial),
                        "g_decimal_sha256": sha(polynomial),
                        "direct_X_support": support(direct),
                        "full_substitution_identity_checked": True})
    print(json.dumps({"stage": "constructed_and_directly_checked", "n": exponent,
                      "degree": polynomial.bit_length()-1}), flush=True)

inner = polys[d]
remaining = polys[n]
degree_inner = inner.bit_length()-1
outer = 0
steps = []
failure = None
while remaining.bit_length() > 1:
    leading = remaining.bit_length()-1
    if leading % degree_inner:
        failure = {"remaining_leading_degree": leading,
                   "inner_degree": degree_inner,
                   "reason": "nonzero polynomial in monic inner must have leading degree divisible by inner degree"}
        break
    degree_outer = leading // degree_inner
    outer ^= 1 << degree_outer
    remaining ^= power(inner, degree_outer)
    steps.append({"removed_outer_degree": degree_outer,
                  "remaining_degree": remaining.bit_length()-1})
if failure is None:
    outer ^= remaining
    remaining = 0
assert polys[n] == compose(outer, inner) ^ remaining
result = {
    "status": "exact finite targeted certificate; no unrestricted extrapolation",
    "question": "generalized Kasami whole-divisor/composition lead, q8 first new case only",
    "parameters": {"q": q, "d": d, "n": n},
    "is_composition": failure is None,
    "outer_support": support(outer),
    "remainder_support": support(remaining),
    "failure": failure,
    "leading_extraction_steps": steps,
    "full_gn_equals_outer_of_gd_plus_remainder": True,
    "independent_direct_X_substitution_checks": independent,
    "elapsed_seconds": time.monotonic()-started,
    "no_multivariate_factorization_or_scan": True,
}
out = Path(str(PREFIX) + "kasami-target-certificate-v1.json")
with out.open("x") as f:
    json.dump(result, f, indent=2)
    f.write("\n")
print(json.dumps({"stage": "complete", "is_composition": result["is_composition"],
                  "outer_support": result["outer_support"], "failure": failure,
                  "certificate": str(out), "elapsed_seconds": result["elapsed_seconds"]}), flush=True)
