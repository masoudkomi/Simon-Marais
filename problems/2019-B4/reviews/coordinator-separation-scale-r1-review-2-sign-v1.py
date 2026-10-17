"""Independent SS3 certificate: one fixed integer-polynomial evaluation.

This is not the constructor's Fraction/derivative program. No history,
word, automaton, root search or trial scan is performed. The polynomials
below come from the hand-derived Euler-operator identities in the review.
"""

from datetime import datetime, timezone
import json
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PREFIX = "problems/2019-B4/reviews/coordinator-separation-scale-r1-review-2-"
M, N = 125000, 220653


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for degree, coefficient in polynomial.items():
            result[degree] = result.get(degree, 0) + coefficient
    return {d: c for d, c in result.items() if c}


def multiply(a, b):
    result = {}
    for i, ai in a.items():
        for j, bj in b.items():
            result[i+j] = result.get(i+j, 0) + ai*bj
    return {d: c for d, c in result.items() if c}


def homogenized_value(polynomial):
    degree = max(polynomial)
    # Pure integer sum is the homogeneous evaluation N^degree P(M/N).
    return degree, sum(coefficient * M**power * N**(degree-power)
        for power, coefficient in polynomial.items())


def reduced(a, b):
    assert b > 0
    factor = gcd(abs(a), b)
    return {"numerator": str(a//factor), "denominator": str(b//factor)}


a = {0: 1, 5: -2, 8: -1}
b = {0: 1, 2: -1}
a_squared = multiply(a, a)
b_cubed = multiply(multiply(b, b), b)
common = multiply(a_squared, b_cubed)
q_euler = {0: 25, 1: -48, 4: 21, 12: -13, 19: 48,
           21: 80, 22: 12, 23: 80, 24: 35}
q_old_euler = {0: 25, 1: -48, 4: 21, 14: 22, 16: 27,
              18: 28, 19: 48, 20: 25, 21: 80, 22: 30,
              23: 80, 24: 42}
f3_euler_numerator = {12: 13, 17: -36, 20: -21}
rigid_euler_numerator = {12: 13, 14: -17}

# 25 E_union = q_euler + f3_euler_numerator/a^2
#                        + rigid_euler_numerator/b^3.
union_polynomial = add(multiply(q_euler, common),
    multiply(f3_euler_numerator, b_cubed),
    multiply(rigid_euler_numerator, a_squared))
old_polynomial = add(multiply(q_old_euler, a_squared),
                     f3_euler_numerator)
union_degree, union_integer = homogenized_value(union_polynomial)
old_degree, old_integer = homogenized_value(old_polynomial)
assert union_degree == 46 and old_degree == 40
a_integer = N**8 - 2*M**5*N**3 - M**8
b_integer = N**2 - M**2
assert M > 0 and N > 0 and 5*M < 3*N
assert a_integer > 0 and b_integer > 0
assert union_integer < 0 and old_integer > 0

union_value = reduced(union_integer,
    25*N**(union_degree-22)*a_integer**2*b_integer**3)
old_value = reduced(old_integer,
    25*N**(old_degree-16)*a_integer**2)

# Corroboration occurs only AFTER the independently derived integer signs.
# Do not execute or import the constructor's mathematical script.
reference = json.loads((ROOT /
    "problems/2019-B4/notes/coordinator-separation-scale-r1-sign-v1.json").read_text())
assert union_value == reference["E_union_r"]
assert old_value == reference["E_previous_union_r"]

result = {
    "checked_at_utc": datetime.now(timezone.utc).isoformat(),
    "status": "independent one-trial integer-polynomial signs certified",
    "method": "hand Euler simplification, sparse integer multiplication, homogeneous evaluation; no Fraction/derivative evaluator",
    "r": {"numerator": M, "denominator": N},
    "lambda_trial": {"numerator": N, "denominator": M},
    "union_integer_polynomial": {str(d): union_polynomial[d]
        for d in sorted(union_polynomial)},
    "old_integer_polynomial": {str(d): old_polynomial[d]
        for d in sorted(old_polynomial)},
    "union_degree": union_degree, "old_degree": old_degree,
    "union_homogeneous_integer": str(union_integer),
    "old_homogeneous_integer": str(old_integer),
    "a_integer": str(a_integer), "b_integer": str(b_integer),
    "a_denominator_power": 8, "b_denominator_power": 2,
    "E_union_r": union_value, "E_previous_union_r": old_value,
    "r_positive_and_less_than_three_fifths": True,
    "both_tail_denominators_positive": True,
    "new_sign": -1, "old_sign": 1,
    "matches_constructor_values_only_after_independent_sign_evaluation": True,
    "constructor_script_executed_or_imported": False,
    "history_factor_automaton_scan_CAS_root_search_or_trial_search": False,
}
with (ROOT / (PREFIX + "sign-v1.json")).open("x") as stream:
    json.dump(result, stream, indent=2)
    stream.write("\n")
print(json.dumps({"status": "passed", "fixed_r": f"{M}/{N}",
    "union_sign": -1, "old_sign": 1,
    "degrees": [union_degree, old_degree],
    "constructor_script_rerun": False}), flush=True)
