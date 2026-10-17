"""One independent homogeneous-integer sign certificate; no search.

Only the fixed accepted U and the fixed new endpoint are used. This
derivation does not execute/import the constructor's Fraction program.
"""
from math import gcd
from pathlib import Path
import json

a = 1834856083
t = 1000000000
endpoint_numerator = 1834847
endpoint_denominator = 1000000
k = a - endpoint_numerator * (t // endpoint_denominator)
assert t % endpoint_denominator == 0 and k == 9083
assert 0 < t < a < 2*t
d = a*a-t*t

# b=(2U^2-1)/(2U^18(U^2-1)^2), U=a/t.
gap_numerator = (2*a*a-t*t)*t**20
gap_denominator = 2*a**18*d*d
# endpoint-(U-b)=b-k/t. All denominators below are positive.
N = t*gap_numerator-k*gap_denominator
D = t*gap_denominator
assert d > 0 and gap_numerator > 0 and gap_denominator > 0
assert N > 0 and D > 0


def pair(n, den):
    assert den > 0
    common = gcd(n, den)
    return {"numerator": str(n//common), "denominator": str(den//common)}


derived = {
    "fixed_U": pair(a,t),
    "fixed_endpoint": pair(endpoint_numerator,endpoint_denominator),
    "positive_tail": pair((2*a*a-t*t)*t**22, a**20*d*d),
    "positive_gap_floor": pair(gap_numerator,gap_denominator),
    "new_exact_upper_bound": pair(a*gap_denominator-t*gap_numerator,D),
    "strict_endpoint_slack": pair(N,D),
}
# Check the serialized fixed fractions only AFTER the independent sign.
constructor = Path(__file__).resolve().parents[1] / "notes/coordinator-cap-gap-r1-certificate-output-v1.json"
old = json.loads(constructor.read_text())
assert all(derived[name] == old[name] for name in derived)
print(json.dumps({
    "independent_homogeneous_integer_formula": "N=(2*a^2-t^2)*t^21-2*9083*a^18*(a^2-t^2)^2",
    "positive_raw_N": str(N), "positive_raw_D": str(D),
    "N_positive": N > 0, "all_denominators_positive": True,
    "exact_derived_fractions": derived,
    "all_six_serialized_constructor_fractions_match": True,
    "mathematical_scope": "ONE fixed exact sign, no parameter search or history/cap/matrix enumeration",
    "constructor_or_old_program_executed": False,
}, indent=2))
