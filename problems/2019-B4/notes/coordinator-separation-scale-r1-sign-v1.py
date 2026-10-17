"""Exact sign for a proved union of two already known infinite tails.

No histories, factors, automata or new original count rows are enumerated.
Only the fixed rational trial below is used in the candidate bound.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

P24={4:1,12:1,14:2,16:3,17:2,18:4,19:8,20:6,21:20,22:14,23:40,24:42}
F3_LONG_PREFIX={12:1,17:2,20:1,22:4}
RIGID_PREFIX={12:1,14:2,16:3,18:4,20:5,22:6,24:7}
def poly(c,x):return sum((v*x**k for k,v in c.items()),Q(0))
def prime(c,x):return sum((k*v*x**(k-1)for k,v in c.items()),Q(0))
alpha=Q(1765224,1000000)
x=1/alpha
a=1-2*x**5-x**8
ap=-10*x**4-8*x**7
b=1-x*x
bp=-2*x
assert a>0 and b>0 and x<Q(3,5)
old_g=poly(P24,x)+x**12/a-poly(F3_LONG_PREFIX,x)
old_gp=prime(P24,x)+12*x**11/a-x**12*ap/a**2-prime(F3_LONG_PREFIX,x)
tail=x**12/b**2-poly(RIGID_PREFIX,x)
tailp=12*x**11/b**2-2*x**12*bp/b**3-prime(RIGID_PREFIX,x)
old_e=1-Q(48,25)*x+old_g-x*old_gp/25
new_e=old_e+tail-x*tailp/25
assert tail>0 and tailp>0
assert new_e<0
def rat(q):return dict(numerator=str(q.numerator),denominator=str(q.denominator))
result=dict(status='exact fixed rational sign passed',lambda_trial=rat(alpha),
    r=rat(x),E_union_r=rat(new_e),E_previous_union_r=rat(old_e),
    new_tail_at_r=rat(tail),new_tail_prime_at_r=rat(tailp),
    F3_denominator=rat(a),rigid_denominator_base=rat(b),
    F3_denominator_positive=True,rigid_geometric_denominator_positive=True,
    r_less_than_three_fifths=True,all_missing_obstructions_length_at_least=25,
    P24=P24,F3_long_prefix_through24=F3_LONG_PREFIX,
    rigid_prefix_through24=RIGID_PREFIX,
    old_sign=(old_e>0)-(old_e<0),new_sign=-1,
    no_history_factor_automaton_original_count_or_prime_enumeration=True)
out=Path(__file__).with_name('coordinator-separation-scale-r1-sign-v1.json')
with out.open('x')as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(dict(status='passed',lambda_trial=str(alpha),old_sign=result['old_sign'],new_sign=-1,finite_rational_certificate_only=True)),flush=True)
