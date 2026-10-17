"""Exact regular-tail certificate for2019; no histories or new factors enumerated."""
from fractions import Fraction as Q
from pathlib import Path
import json
COEFF={4:1,12:1,14:2,16:3,17:2,18:4,19:8,20:6,21:20,22:14,23:40,24:42}
LONG_PREFIX={12:1,17:2,20:1,22:4}
def poly(c,x):return sum((v*x**n for n,v in c.items()),Q(0))
def prime(c,x):return sum((n*v*x**(n-1) for n,v in c.items()),Q(0))
def e(x):
 a=1-2*x**5-x**8;ap=-10*x**4-8*x**7
 assert a>0
 g=poly(COEFF,x)+x**12/a-poly(LONG_PREFIX,x)
 gp=prime(COEFF,x)+12*x**11/a-x**12*ap/a**2-prime(LONG_PREFIX,x)
 return 1-Q(48,25)*x+g-x*gp/25
lo=176521000;hi=176600000
# Alpha/10^8 is a trial lower bound. This just selects a rational sign certificate.
assert e(Q(10**8,lo))<0 and e(Q(10**8,hi))>0
while hi-lo>1:
 mid=(lo+hi)//2
 if e(Q(10**8,mid))<0:lo=mid
 else:hi=mid
alpha=Q(lo,10**8);r=1/alpha;value=e(r)
assert value<0 and r<Q(3,5)
plain=1-Q(48,25)*r+poly(COEFF,r)-r*prime(COEFF,r)/25
def rat(v):return {'numerator':str(v.numerator),'denominator':str(v.denominator)}
result={'status':'exact negative certificate passed','lambda_trial':rat(alpha),'lambda_trial_decimal':str(float(alpha)),'r':rat(r),'E_G_r':rat(value),'E_P24_r':rat(plain),'r_less_than_three_fifths':True,'loop_denominator_positive':True,'missing_factor_min_length':25,'P24_coefficients':COEFF,'F3_long_prefix_through24':LONG_PREFIX,'next_1e_minus8_trial_sign':1 if e(Q(10**8,hi))>0 else 0,'no_new_history_factor_or_automaton_enumeration':True}
out=Path(__file__).with_name('coordinator-regular-tail-certificate-v1.json')
with out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps({'status':'passed','lambda_trial':str(alpha),'decimal':float(alpha),'E_G_sign':-1,'E_P24_sign':(plain>0)-(plain<0),'finite_rational_sign_certificate_only':True}),flush=True)
