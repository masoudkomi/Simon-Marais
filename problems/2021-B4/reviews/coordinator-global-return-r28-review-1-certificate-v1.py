"""ONE fresh independent, proof-critical finite certificate, not a search.

Different design from author's polynomial shift arithmetic: scalar exact
evaluation, Pascal addition, and Newton forward interpolation at 18 integer
points under the HAND-proved degree<=17 bound. No author code/import/read,
CAS, prime/depth/height loop, external package, network or old replay.
The complete stdout is preserved in this review's source JSON.
"""
from fractions import Fraction
import json
import os
import platform
import time

def run():
    started = time.monotonic()
    pascal = [[1]]
    for j in range(1,21):
        old = pascal[-1]
        pascal.append([1] + [old[i-1]+old[i] for i in range(1,j)] + [1])

    def scalar_Q(h):
        a = [0]*21
        a[0],a[1],a[3],a[6] = 1,-h,2*h**3,-35*h**6
        a[7] = -1+7*h-70*h**3+245*h**6
        a[8] = 7-48*h+448*h**3-980*h**6
        for j in range(11,19):
            center = 1 if j in (14,16,18) else h
            a[j] = -sum(pascal[j][i]*a[i]*center**(j-i) for i in range(j))
        return sum(pascal[20][i]*a[i] for i in range(21))

    samples = []
    for h in range(18):
        q = scalar_Q(h)
        assert q % 2 == 0
        samples.append(-q//2)
    layer = samples[:]
    forward = []
    while layer:
        forward.append(layer[0])
        layer = [right-left for left,right in zip(layer,layer[1:])]
    coeff = [Fraction(0) for _ in range(18)]
    basis = [Fraction(1)]
    for k,delta in enumerate(forward):
        for i,entry in enumerate(basis):
            coeff[i] += delta*entry
        if k < 17:
            nxt = [Fraction(0) for _ in range(len(basis)+1)]
            for i,entry in enumerate(basis):
                nxt[i] -= k*entry/Fraction(k+1)
                nxt[i+1] += entry/Fraction(k+1)
            basis = nxt
    assert all(c.denominator == 1 for c in coeff)
    integer_descending = [c.numerator for c in reversed(coeff)]
    field_values = [(-scalar_Q(x)*19) % 37 for x in range(37)]
    result = {
        "status":"independently reconstructed COMPLETE finite certificate; actual-domain and rational-reduction proof remain HAND obligations",
        "design":"scalar triangular equations plus Newton forward interpolation, degree<=17 proved by hand",
        "python":platform.python_version(),"dependencies":"Python standard library only",
        "child_pid":os.getpid(),"intrinsic_finite_bounds":{"interpolation_points":18,"all_field_elements":37,"highest_row":20},
        "integer_coefficients_descending":integer_descending,
        "coefficients_descending_mod37":[c % 37 for c in integer_descending],
        "values_at_0_through_36":field_values,
        "degree":17 if integer_descending[0] else "below17",
        "leading_coefficient_mod37":integer_descending[0] % 37,
        "all37_values_nonzero":all(field_values),
        "elapsed_seconds":time.monotonic()-started,
        "generic_prime_depth_height_search":False,"author_source_old_helper_executed":False
    }
    print(json.dumps(result,indent=2),flush=True)

if __name__ == "__main__":
    run()
