#!/usr/bin/env python3
"""Independent R2 exact checks. Does not import/read the author's program.

Represent all Cartier checks as ordinary polynomials over GF(2), after
clearing b**15. SymPy's Poly multiplication is independent of the author's
custom Laurent-monomial-set certificate. A separate supervisor bounds time.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import time

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).with_name("family-review-2-check.json")
started = time.monotonic()
results = {
    "purpose": "Independent exact symbolic evidence for blind reviewer R2",
    "method": "SymPy Poly over GF(2), clearing Laurent denominators; no constructor program imported or read",
    "python": sys.version,
    "sympy": sp.__version__,
    "platform": platform.platform(),
    "pid": os.getpid(),
    "checks": [],
}


def checkpoint(name, passed, **data):
    item = {"name": name, "passed": bool(passed), **data}
    results["checks"].append(item)
    OUT.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(item, sort_keys=True), flush=True)
    if not passed:
        raise AssertionError(name)


def poly(expr, *gens):
    return sp.Poly(expr, *gens, modulus=2)


manifest_path = ROOT / "problems/2024-B4/notes/fixed-factor-family-v1-manifest.json"
manifest = json.loads(manifest_path.read_text())
hashes = []
for artifact in manifest["artifacts"]:
    raw = (ROOT / artifact["path"]).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    hashes.append({"path": artifact["path"], "sha256": digest, "bytes": len(raw),
                   "matches": digest == artifact["sha256"] and len(raw) == artifact["bytes"]})
checkpoint("all frozen manifest artifact hashes", all(a["matches"] for a in hashes), artifacts=hashes,
           manifest_sha256=hashlib.sha256(manifest_path.read_bytes()).hexdigest())

x, y, z, t = sp.symbols("x y z t")
w = x + y + z
Q = x*x + y*y + z*z + x*y + y*z + z*x
R = (x+y)*(y+z)*(z+x)
D = x*y*z*w
E_product = poly((1+x*t)*(1+y*t)*(1+z*t)*(1+w*t), t, x, y, z)
E_formula = poly(1+Q*t*t+R*t**3+D*t**4, t, x, y, z)
checkpoint("formal list-with-multiplicity product", E_product == E_formula)
checkpoint("characteristic-two formal derivative", E_formula.diff(t) == poly(R*t*t, t, x, y, z))

q, u, d, s = sp.symbols("q u d s")
P = []
for j in range(6):
    value = poly({0: 1, 1: q, 2: d}.get(j, 0), q, u, d)
    for offset, coefficient in ((2, q*q), (3, u), (4, d*d)):
        if j >= offset:
            value += poly(coefficient, q, u, d) * P[j-offset]
    P.append(value)
expected = [1, q, q*q+d, q**3+u,
            q**4+q*q*d+q*u+d*d, q**5+q*d*d+u*d]
checkpoint("P_0 through P_5 by denominator recurrence", all(a == poly(e, q, u, d) for a, e in zip(P, expected)),
           coefficients=[str(a.as_expr()) for a in P])
A = q**5+q*d*d+u*d
checkpoint("direct official f_13 equals R times substituted A",
           poly(x**13+y**13+z**13+w**13, x, y, z)
           == poly(R*(Q**5+Q*D**2+R**2*D), x, y, z))

# Explicit polynomial checks for the Laurent quotient coordinate formulas.
b = sp.symbols("b")
checkpoint("eliminated A vanishes, after clearing b",
           poly(sp.expand(b*A.subs({d:q*q*b, u:q**3*(b+1/b)})), q, b).is_zero)
den_normalized = 1+q*q*(z/q)**2 + q**3*(b+1/b)*(z/q)**3 + (q*q*b)**2*(z/q)**4
num_normalized = 1+q*(z/q)+(q*q*b)*(z/q)**2
H_expr = b+b*z**2+(b*b+1)*z**3+b**3*z**4
checkpoint("normalized rational denominator, after clearing b",
           poly(sp.expand(b*den_normalized-H_expr), z, b).is_zero)
checkpoint("normalized numerator", sp.cancel(num_normalized-(1+z+b*z*z)) == 0)

# K=H/b. Multiply each Laurent identity by b**15 before checking it.
# The three independent numerator polynomials all have nonnegative b powers.
H = poly(H_expr, z, b)
H15 = H**15
checkpoint("K Frobenius identity after clearing b^16",
           (H**16 - poly(H_expr.subs({z:z**16, b:b**16}, simultaneous=True), z, b)).is_zero,
           H15_terms=len(H15.terms()), H15_z_degree=H15.degree(z), H15_b_degree=H15.degree(b))


def select_z_mod_16(P, residue):
    # Selecting coefficients in SymPy's full polynomial normal form. This
    # includes every term of P, rather than evaluations of b in finite fields.
    return sp.Poly.from_dict({((i-residue)//16, j): c
                             for (i, j), c in P.terms() if i % 16 == residue},
                            (z, b), modulus=2)


def coefficients_by_z(P):
    out = {}
    for (i, j), c in P.terms():
        assert int(c) % 2 == 1
        out.setdefault(str(i), []).append(j)
    return {i: sorted(es) for i, es in sorted(out.items(), key=lambda a: int(a[0]))}


L15 = sum(b**e for e in (8,10,12,14,16,18,20,22))
M15 = sum(b**e for e in (9,11,13,15,17,21,23))
J15 = sum(b**e for e in (3,9,11,13,15,17,19,21,23))
cases = [
    ("Cartier identity (9)", 5, 1+z+b*z*z,
     (L15+M15)*z+(L15+J15)*(z*z+b**16*z**3)),
    ("Cartier identity (10)", 6, z,
     L15*(z+z*z+b**16*z**3)),
    ("Cartier identity (11)", 6, z*z+b*z**3,
     M15*z+J15*(z*z+b**16*z**3)),
]
for name, r, numerator, rhs in cases:
    full = poly(numerator, z, b)*H15
    selected = select_z_mod_16(full, r)
    target = poly(rhs, z, b)
    rem = selected-target
    checkpoint(name, rem.is_zero, residue=r, clearing_factor="b^15",
               input_z_degree=full.degree(z), input_terms=len(full.terms()),
               selected_z_degree=selected.degree(z), selected_terms=len(selected.terms()),
               selected_coefficients_b_exponents=coefficients_by_z(selected),
               expected_coefficients_b_exponents=coefficients_by_z(target),
               remainder_terms=[] if rem.is_zero else rem.terms())

# An independent small recurrence sample in the localized divisor is only
# finite evidence; it is not the proof of arbitrary m.
# Use ordinary SymPy Laurent expressions as bounded dictionaries of Poly
# after clearing b^j, so T_j=b^j [z^j]F is always polynomial in b.
# K F=N gives T_j=b^2*T_(j-2)+(b^4+b^2)*T_(j-3)+b^6*T_(j-4)
# plus initial numerator terms 1,b*z,b^3*z^2.
T = []
for j in range(102):
    value = poly({0:1, 1:b, 2:b**3}.get(j,0), b)
    for delta, c in ((2,b*b), (3,b**4+b*b), (4,b**6)):
        if j >= delta:
            value += poly(c, b)*T[j-delta]
    T.append(value)
checkpoint("finite recurrence samples (evidence only)", T[5].is_zero and T[101].is_zero,
           samples=[{"m":0,"j":5,"n":13,"zero":T[5].is_zero},
                    {"m":1,"j":101,"n":205,"zero":T[101].is_zero}],
           nearby_nonzero_indices=[j for j in (4,6,100) if not T[j].is_zero])

results["completed"] = True
results["elapsed_seconds"] = time.monotonic()-started
OUT.write_text(json.dumps(results, indent=2)+"\n")
print(json.dumps({"completed":True,"elapsed_seconds":results["elapsed_seconds"]}), flush=True)
