"""One prescribed proof-critical integer sign; no author input or Fraction.

The homogeneous degree46/40 formulas were derived by hand in the companion
certificate. No search, language enumeration, symbolic algebra or imports
from the constructor are performed. Output is captured by a timed parent.
"""
import json
from math import gcd

p = 125000
s = 220653
a = s**8 - 2*p**5*s**3 - p**8
b = s**2 - p**2
c = 13*s**8 - 36*p**5*s**3 - 21*p**8
d = 13*s**2 - 17*p**2
ah = (25*s**24 - 48*p*s**23 + 21*p**4*s**20 - 13*p**12*s**12
      + 48*p**19*s**5 + 80*p**21*s**3 + 12*p**22*s**2
      + 80*p**23*s + 35*p**24)
ao = (25*s**24 - 48*p*s**23 + 21*p**4*s**20 + 22*p**14*s**10
      + 27*p**16*s**8 + 28*p**18*s**6 + 48*p**19*s**5
      + 25*p**20*s**4 + 80*p**21*s**3 + 30*p**22*s**2
      + 80*p**23*s + 42*p**24)
inew = a*a*b**3*ah + p**12*c*b**3*s**20 + p**12*d*a*a*s**16
inewden = 25*s**24*a*a*b**3
iold = a*a*ao + p**12*c*s**20
ioldden = 25*s**24*a*a
assert p > 0 and s > 0 and 5*p < 3*s
assert a > 0 and b > 0 and inewden > 0 and ioldden > 0
assert inew < 0 < iold

def reduced(n, den):
    common = gcd(abs(n), den)
    return dict(numerator=str(n//common), denominator=str(den//common))

print(json.dumps(dict(
    status='independent fixed-trial homogeneous-integer sign certificate passed',
    trial=dict(p=p, s=s, alpha_numerator=s, alpha_denominator=p),
    homogeneous_integers={key:str(value) for key,value in [
        ('a_h',a),('b_h',b),('C_h',c),('D_h',d),('A_h',ah),('A_old_h',ao),
        ('I_new',inew),('I_new_denominator',inewden),
        ('I_old',iold),('I_old_denominator',ioldden)]},
    E_union=reduced(inew,inewden), E_previous_union=reduced(iold,ioldden),
    signs=dict(new=-1,old=1),
    no_constructor_input_or_Fraction_or_symbolic_differentiation=True,
    single_prescribed_trial_no_search_or_language_enumeration=True
),indent=2),flush=True)
