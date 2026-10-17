"""Independent proof-critical rational sign check; no histories or automata."""
from fractions import Fraction
import json

p, q = 100000000, 176522347
N = 25
P24 = {4: 1, 12: 1, 14: 2, 16: 3, 17: 2, 18: 4,
       19: 8, 20: 6, 21: 20, 22: 14, 23: 40, 24: 42}
# Independent algebra: G=U+z^12/W after removing the known short prefix.
U = {4: 1, 14: 2, 16: 3, 18: 4, 19: 8, 20: 5,
     21: 20, 22: 10, 23: 40, 24: 42}
prefix = {12: 1, 17: 2, 20: 1, 22: 4}
assert {n: P24.get(n, 0)-prefix.get(n, 0)
        for n in P24 if P24.get(n, 0)-prefix.get(n, 0)} == U


def homogenized_moment(poly):
    return (25*q**24 - 48*p*q**23
            + sum((25-n)*c*p**n*q**(24-n) for n, c in poly.items()))


# W=1-2z^5-z^8. The identity used is
# 25 W^2 E_G = W^2[25-48z+sum(25-n)u_n z^n]
#                +13z^12-36z^17-21z^20.
w_num = q**8 - 2*p**5*q**3 - p**8
u_num = homogenized_moment(U)
sign_num = (u_num*w_num*w_num + 13*p**12*q**28
            - 36*p**17*q**23 - 21*p**20*q**20)
old_num = homogenized_moment(P24)
assert 5*p < 3*q
assert w_num > 0
assert sign_num < 0
assert old_num > 0
E_new = Fraction(sign_num, 25*q**24*w_num*w_num)
E_old = Fraction(old_num, 25*q**24)
W = Fraction(w_num, q**8)


def frac(x):
    return {"numerator": x.numerator, "denominator": x.denominator}


print(json.dumps({
    "method": "independent homogenized integer polynomial sign; fixed rational trial only",
    "r": frac(Fraction(p, q)),
    "claimed_lower_bound": frac(Fraction(q, p)),
    "N": N,
    "P24_coefficients": P24,
    "U_coefficients": U,
    "W_at_r": frac(W),
    "W_homogenized_numerator": w_num,
    "U_moment_homogenized_numerator": u_num,
    "new_sign_homogenized_numerator": sign_num,
    "old_sign_homogenized_numerator": old_num,
    "E_G_at_r": frac(E_new),
    "E_P24_at_r": frac(E_old),
    "tail_contribution_at_r": frac(E_new-E_old),
    "all_required_signs_pass": True,
    "history_factor_queue_or_automaton_enumeration": False,
    "bisection_or_float_used_for_mathematics": False,
}, indent=2))
