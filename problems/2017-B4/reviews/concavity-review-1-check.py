#!/usr/bin/env python3
"""Independent exact audit; no constructor module or output is imported.

Natural logs use the positive Mercator series at t=1-1/r, rather than
the constructor's atanh series. Run through the adjacent external supervisor.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math
import sys

ROOT = Path(__file__).resolve().parents[3]
PREFIX = Path(__file__).with_name("concavity-review-1")


def encode(q):
    return {"numerator": str(q.numerator), "denominator": str(q.denominator)}


def log_interval(r, terms=96):
    # ln(r)=-ln(1-t)=sum_{j>=1} t^j/j, 0<t<1. For j>=M+1,
    # 1/j<=1/(M+1); the tail is bounded by a geometric series.
    assert r > 1
    t = 1 - 1 / r
    power = t
    total = Q(0)
    for j in range(1, terms + 1):
        total += power / j
        power *= t
    tail = power / ((terms + 1) * (1 - t))
    return total, total + tail


def audit_atanh_tail(r, terms=80):
    # Independently check the candidate's stated rational enclosure too.
    z = (r - 1) / (r + 1)
    total = sum((2 * z ** (2*j + 1) / (2*j + 1)
                 for j in range(terms)), Q(0))
    tail = 2 * z ** (2*terms + 1) / ((2*terms + 1) * (1 - z*z))
    return total, total + tail


ratios = [Q(2), Q(32, 7), Q(79, 58), Q(107648, 43687), Q(3, 2)]
logs = {}
result = {
    "kind": "independently authored finite rational audit, not an unrestricted computational proof",
    "method": "positive Mercator series t=1-1/r, M=96, exact Fraction arithmetic",
    "constructor_imported_or_executed": False,
    "logs": {},
}
for r in ratios:
    lo, hi = log_interval(r)
    alo, ahi = audit_atanh_tail(r)
    assert lo < ahi and alo < hi  # independent enclosures overlap
    logs[r] = lo, hi
    result["logs"][str(r)] = {
        "lower": encode(lo), "upper": encode(hi),
        "width": encode(hi-lo),
        "candidate_atanh_lower": encode(alo),
        "candidate_atanh_upper": encode(ahi),
        "enclosures_overlap": True,
        "decimal_diagnostic": [float(lo), float(hi)],
    }
    print("checkpoint: independently enclosed ln", r, flush=True)

L2, U2 = logs[Q(2)]
Lx, Ux = logs[Q(32, 7)]
Ly, Uy = logs[Q(79, 58)]
Lr, Ur = logs[Q(107648, 43687)]
Lq, Uq = logs[Q(3, 2)]
phi_lo = (Q(21,100)*Lx + Q(29,50)*Ly)/U2 + Q(29,50)
phi_hi = (Q(21,100)*Ux + Q(29,50)*Uy)/L2 + Q(29,50)
der_lo = (Lr + Q(7,32) + Q(21,79))/U2 - 2
der_hi = (Ur + Q(7,32) + Q(21,79))/L2 - 2
f0_lo, f0_hi = 1 + Lq/(2*U2), 1 + Uq/(2*L2)
A_hi = max(phi_hi + der_hi/Q(25), f0_hi)
claims = {
    "phi_lt_64951_over_50000": phi_hi < Q(64951,50000),
    "derivative_positive": der_lo > 0,
    "derivative_lt_1_over_5000": der_hi < Q(1,5000),
    "F0_lt_1293_over_1000": f0_hi < Q(1293,1000),
    "ln2_gt_2_over_3": L2 > Q(2,3),
    "uniform_A_hi_lt_324757_over_250000": A_hi < Q(324757,250000),
    "exponent_A_hi_over_2_lt_324757_over_500000": A_hi/2 < Q(324757,500000),
}
assert all(claims.values())
result["claims"] = claims
result["derived_intervals"] = {
    "Phi_21_over_100": {"lower": encode(phi_lo), "upper": encode(phi_hi)},
    "Phi_prime_21_over_100": {"lower": encode(der_lo), "upper": encode(der_hi)},
    "F0": {"lower": encode(f0_lo), "upper": encode(f0_hi)},
    "uniform_A_upper": encode(A_hi),
    "uniform_objective_slack": encode(Q(324757,250000)-A_hi),
    "limsup_upper": encode(A_hi/2),
    "limsup_slack": encode(Q(324757,500000)-A_hi/2),
}
result["decimal_diagnostics_only"] = {
    "phi": [float(phi_lo),float(phi_hi)],
    "derivative": [float(der_lo),float(der_hi)],
    "F0": [float(f0_lo),float(f0_hi)],
    "A_upper": float(A_hi),
    "objective_slack": float(Q(324757,250000)-A_hi),
    "limsup_upper": float(A_hi/2),
}

# Check the integer tuple domain and every endpoint convention at an explicit
# finite mesh as counterexample-search evidence. The analytic audit is separate.
def objective(mu,a,u):
    b = 1-u-a
    assert mu+1e-12 >= a >= 0 and b >= -1e-12
    b = max(0,b)
    return ((a*math.log2(mu/a) if a else 0)
            + (b*math.log2(1+a/b) if b else 0) + b)

maxval, maxarg = -1, None
for i in range(401):
    u=i/400
    mu=min(1,u+.75)
    for j in range(201):
        a=min(u,1-u)*j/200
        f=objective(mu,a,u)
        if f>maxval:
            maxval,maxarg=f,[mu,a,u]
result["finite_mesh_evidence_only"] = {
    "u_intervals":400,"a_intervals_per_u":200,
    "maximum":maxval,"argmax":maxarg,
    "boundary_values": {
        "mu_a_u_0_0_0":objective(0,0,0),
        "mu_a_u_1_0_1":objective(1,0,1),
        "mu_a_u_half_half_half":objective(.5,.5,.5),
        "mu_a_u_1_half_half":objective(1,.5,.5),
    },
}
freeze = ROOT / "problems/2017-B4/notes/deep-literature-r2-concavity-freeze-v1.json"
construction = json.loads(freeze.read_text())
result["construction_freeze"] = {
    "manifest_sha256":hashlib.sha256(freeze.read_bytes()).hexdigest(),
    "artifacts":[],
}
for record in construction["artifacts"]:
    p=ROOT / record["path"]
    digest=hashlib.sha256(p.read_bytes()).hexdigest()
    assert digest==record["sha256"] and p.stat().st_size==record["bytes"]
    result["construction_freeze"]["artifacts"].append({
        "path":record["path"],"sha256":digest,"bytes":p.stat().st_size,
        "matches":True,
    })
result["requested_model"]="gpt-6.1-sol"
result["requested_reasoning"]="max"
result["effective_setting_readback"]="unavailable"
output=PREFIX.with_name(PREFIX.name+"-certificate.json")
output.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result["claims"],sort_keys=True),flush=True)
print(json.dumps(result["decimal_diagnostics_only"],sort_keys=True),flush=True)
print("checkpoint: independent certificate and frozen-byte checks complete",flush=True)
