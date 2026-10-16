"""Exact necessary-condition check for f=x^d+A*x^a+B*x^b.

Derived independently in notes/two-support.md; related to the attributed
two-support reduction in arXiv:2608.14726. No assertion for unscanned d.
All arithmetic is exact. A and B are assumed nonzero, 1<=a<b<=d-2.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, gcd
import json
import sys

print(json.dumps({"python": sys.version, "dependencies": "Python standard library only",
                  "status": "finite exact computational evidence; unrestricted theorem not claimed"}))
for d in [20,24,28,30]:
    checked = 0
    compatible = []
    comparison_signs = {"R_power_less": 0, "R_power_greater": 0}
    for a,b in combinations(range(1,d-1),2):
        ca, cb, cba = comb(d,a), comb(d,b), comb(b,a)
        rr = Fraction((ca-1)*(cb-1), cb*(ca-cba))
        ss = Fraction((cb-1)*(cba-1), ca-cba)
        assert rr > 0 and ss > 0
        m,n = b-a,d-a
        common = gcd(m,n)
        left,right = rr**(n//common),ss**(m//common)
        checked += 1
        if left == right:
            compatible.append([a,b,str(rr),str(ss)])
        elif left < right:
            comparison_signs["R_power_less"] += 1
        else:
            comparison_signs["R_power_greater"] += 1
    print(json.dumps({"degree":d,"exponent_pairs_checked":checked,
                      "compatible_pairs":compatible,"comparison_signs":comparison_signs,
                      "search_complete":True}))
