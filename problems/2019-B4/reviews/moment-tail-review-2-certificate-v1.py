"""Independent fixed-trial integer certificate; no histories or search."""
from datetime import datetime, timezone
from pathlib import Path
from math import gcd
import hashlib
import json
import os

PREFIX = Path(__file__).with_name("moment-tail-review-2-")
ROOT = Path(__file__).resolve().parents[3]
P24 = {4: 1, 12: 1, 14: 2, 16: 3, 17: 2, 18: 4, 19: 8,
       20: 6, 21: 20, 22: 14, 23: 40, 24: 42}
Q = {12: 1, 17: 2, 20: 1, 22: 4}
N = 25


def multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def scaled_value(c, a, b):
    """Return b**degree times the exact value of integer polynomial c(a/b)."""
    d = len(c) - 1
    return sum(x * a**i * b**(d-i) for i, x in enumerate(c))


def reduced(n, d):
    assert d > 0
    g = gcd(abs(n), d)
    return {"numerator": str(n//g), "denominator": str(d//g)}


print(json.dumps({"checkpoint": "start", "pid": os.getpid(),
                  "purpose": "fixed rational sign certificate only"}), flush=True)

# B=1-2x5-x8; V=25-48x+sum(25-n)(P24_n-Q_n)x^n.
# Algebraically 25 E_G = V + x12(13-36x5-21x8)/B^2.
B = [1] + [0] * 8
B[5] = -2
B[8] = -1
V = [0] * 25
U = [0] * 25
V[0] = U[0] = 25
V[1] = U[1] = -48
for n, value in P24.items():
    U[n] = (25-n) * value
    V[n] = (25-n) * (value-Q.get(n, 0))
numerator = multiply(V, multiply(B, B))
for n, value in {12: 13, 17: -36, 20: -21}.items():
    numerator[n] += value
assert len(numerator) == 41 and numerator[-1] == 42
print(json.dumps({"checkpoint": "integer numerator reconstructed",
                  "degree": 40}), flush=True)

a, b = 100000000, 176522347
b_scaled = scaled_value(B, a, b)
g_n = scaled_value(numerator, a, b)
g_d = 25 * b**24 * b_scaled**2
p_n = scaled_value(U, a, b)
p_d = 25 * b**24
assert b_scaled > 0 and 5*a < 3*b
assert g_n < 0 and p_n > 0
value_g = reduced(g_n, g_d)
value_p = reduced(p_n, p_d)
next_n = scaled_value(numerator, a, b+1)
assert next_n > 0
print(json.dumps({"checkpoint": "exact signs independently established",
                  "E_G_sign": -1, "E_P24_sign": 1,
                  "next_fixed_trial_sign": 1}), flush=True)

# Compare only after establishing the independent signs.
author_path = ROOT / "problems/2019-B4/notes/coordinator-regular-tail-certificate-v1.json"
author_bytes = author_path.read_bytes()
author = json.loads(author_bytes)
assert author["E_G_r"] == value_g
assert author["E_P24_r"] == value_p
assert author["next_1e_minus8_trial_sign"] == 1
assert {int(k): v for k, v in author["P24_coefficients"].items()} == P24
assert {int(k): v for k, v in author["F3_long_prefix_through24"].items()} == Q

result = {
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "status": "complete fixed-trial exact integer certificate",
    "pid": os.getpid(), "N": N,
    "r": {"numerator": str(a), "denominator": str(b)},
    "alpha": {"numerator": str(b), "denominator": str(a)},
    "method": "cleared-denominator integer polynomial; no Fraction differentiation or bisection",
    "B_coefficients_low_to_high": B,
    "V_coefficients_low_to_high": V,
    "E_G_numerator_coefficients_low_to_high": numerator,
    "clearing_formula": "E_G(a/b)=scaled_value(numerator,a,b)/(25*b^24*scaled_value(B,a,b)^2)",
    "loop_denominator_scaled_numerator": str(b_scaled),
    "loop_denominator_positive": True,
    "r_less_than_three_fifths_integer_difference": str(3*b-5*a),
    "E_G_r": value_g, "E_P24_r": value_p,
    "next_fixed_alpha": {"numerator": str(b+1), "denominator": str(a)},
    "next_fixed_trial_cleared_numerator": str(next_n),
    "next_fixed_trial_sign": 1,
    "author_certificate_sha256": hashlib.sha256(author_bytes).hexdigest(),
    "author_rational_values_match": True,
    "new_history_factor_cap_or_automaton_enumeration": False,
    "trial_search_or_bisection": False,
    "CAS_or_external_dependency": False,
}
output = Path(str(PREFIX) + "certificate-v1.json")
with output.open("x", encoding="utf-8") as stream:
    json.dump(result, stream, indent=2)
    stream.write("\n")
print(json.dumps({"checkpoint": "completed", "output": str(output),
                  "author_values_match": True}), flush=True)
