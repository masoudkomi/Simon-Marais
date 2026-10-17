"""One fixed rational upper-bound certificate; no search or enumeration."""
from fractions import Fraction
import json

U = Fraction(1834856083, 1000000000)
endpoint = Fraction(1834847, 1000000)
z = 1 / U
tail = z**22 * (2-z**2) / (1-z**2)**2
bound = (2*U**2-1) / (2*U**18*(U**2-1)**2)

def pair(x):
    return {"numerator": str(x.numerator), "denominator": str(x.denominator)}

assert 1 < U < 2
assert 0 < z < 1
assert tail > 0
assert bound == U**2 * tail / 2
assert bound > 0
assert endpoint - (U-bound) > 0
print(json.dumps({
    "fixed_U": pair(U),
    "fixed_endpoint": pair(endpoint),
    "positive_tail": pair(tail),
    "positive_gap_floor": pair(bound),
    "new_exact_upper_bound": pair(U-bound),
    "strict_endpoint_slack": pair(endpoint-(U-bound)),
    "all_assertions_passed": True,
    "search_enumeration_matrix_or_old_certificate_replay": False,
}, indent=2))
