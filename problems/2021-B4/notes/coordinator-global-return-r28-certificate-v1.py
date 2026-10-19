"""NEW complete finite polynomial certificate, NOT an unrestricted search.

Standard-library exact integer polynomial arithmetic. Read and reconstruct
the rational-witness reduction before using this finite certificate. This
program cannot establish any lifting, scope, gcd or annual conclusion.
"""
from math import comb
import json

def plus(*polys):
    out=[0]*max(map(len,polys))
    for poly in polys:
        for i,value in enumerate(poly):out[i]+=value
    while len(out)>1 and out[-1]==0:out.pop()
    return out

def times(poly,scalar,shift=0):return [0]*shift+[scalar*c for c in poly]

def certificate():
    a=[[0]for _ in range(21)]
    for j,poly in {0:[1],1:[0,-1],3:[0,0,0,2],6:[0,0,0,0,0,0,-35],
                   7:[-1,7,0,-70,0,0,245],8:[7,-48,0,448,0,0,-980]}.items():a[j]=poly
    # Actual b=0,A9=A10=0 specialization. Fixed A19=A20=0.
    for j in range(11,19):
        a[j]=plus(*(times(a[i],-comb(j,i),j-i if j in (11,12,13,15,17)else 0)for i in range(j)))
    q=plus(*(times(a[i],comb(20,i))for i in range(19)))
    assert len(q)==18 and all(c%2==0 for c in q)
    w=[-c//2 for c in q]
    expected=[27,11,26,34,13,3,11,26,14,18,28,5,13,12,16,27,28,11]
    assert [c%37 for c in reversed(w)]==expected
    values=[]
    for x in range(37):
        value=0
        for c in reversed(w):value=(value*x+c)%37
        values.append(value)
    expected_values=[11,27,28,19,10,20,10,6,30,1,10,19,13,29,15,8,31,34,5,21,9,8,34,1,22,32,3,10,9,8,6,27,35,27,33,10,8]
    assert values==expected_values and all(values)
    return dict(status='UNVERIFIED finite certificate; domain/reduction and independent audits still required',
                degree=17,prime=37,leading_coefficient_mod_prime=27,
                integer_coefficients_descending=list(reversed(w)),
                coefficients_descending_mod_prime=expected,
                values_at_0_through_36=values,all_37_values_nonzero=True,
                unrestricted_search=False,package_dependencies='Python standard library only')

if __name__=='__main__':print(json.dumps(certificate(),indent=2))
