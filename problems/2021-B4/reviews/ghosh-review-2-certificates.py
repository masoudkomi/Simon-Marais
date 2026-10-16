"""Finite exact checks for independent Ghosh source audit R2.

Run through the separately recorded subprocess command, with a 30-second timeout.
No computation here establishes or refutes an unrestricted CA statement.
"""
import json, os, platform, sys
import sympy as s

def emit(event, **kw):
    print(json.dumps(dict(event=event, **kw), sort_keys=True), flush=True)

emit('dependencies', pid=os.getpid(), python=platform.python_version(), sympy=s.__version__)
x,y,z,t,X,u,v,w = s.symbols('x y z t X u v w')
a,b,h=x*x-3*z,x*y-2*z,y*y-z
certificate=(z+h)*a+(-4*z-b)*b+3*z*h
emit('nilpotent_certificates',
     simple_residual=str(s.expand((1-t*X)*(1+t*X)+X*X*t*t-1)),
     z_squared_residual=str(s.expand(certificate-z*z)),
     inverse_residual=str(s.expand((1-z*X)*(1+z*X)+X*X*certificate-1)))
G=s.groebner([x*x-3*y*y,x*y-2*y*y],x,y,domain=s.QQ)
emit('artinian_two_variable_quotient', groebner=[str(f) for f in G.polys],
     y_squared_remainder=str(G.reduce(y*y)[1]),
     y_cubed_remainder=str(G.reduce(y*y*y)[1]))
columns=[(y*y,1),(x*y,2),(x*x,3),(z,1)]
minors=[s.expand(columns[i][0]*columns[j][1]-columns[j][0]*columns[i][1])
        for i in range(4) for j in range(i+1,4)]
GI=s.groebner([a,b,h],x,y,z,domain=s.QQ)
emit('all_minor_remainders', values=[str(GI.reduce(f)[1]) for f in minors])
emit('zero_divisor_models', first_annihilator=str(t*y),
     second_annihilator=str(t*y*y),
     translated_identity_residual=str(s.expand(u*u*(u*(v+t))-v*u**3-t*u**3)))
K1,K2,B0,B1,epsilon=s.symbols('K1 K2 B0 B1 epsilon')
incidence=B1*(K2*B0-K1*B1)
emit('incidence_model', homogenized=str(incidence),
     special_fiber=str(incidence.subs({K1:0,K2:1})),
     escaping_curve_residual=str(s.expand(incidence.subs({B0:epsilon,B1:1,K1:epsilon,K2:1}))))

# An exploratory test of Proposition 3.3 in its actual derivative family.
# It is retained whether or not it yields a counterexample.
xs=s.symbols('x1:5')
marks=[1,2,2,1]
def elementary(seq,k):
    from itertools import combinations
    return s.expand(sum(s.prod(q) for q in combinations(seq,k)))
Fs=[]
for i,j in enumerate(marks,1):
    marked=xs[j-1]
    shifted=[xx-marked if k!=j-1 else -marked for k,xx in enumerate(xs)]
    Fs.append(elementary(shifted,5-i))
point=dict(zip(xs,[0,1,4,6]))
emit('char11_actual_family', n=4,p=11,marks=marks,point=list(point.values()),
     characteristic_exclusion_product=int(s.prod(s.binomial(4,i-1) for i in range(1,5))),
     values=[int(f.subs(point))%11 for f in Fs],
     generators=[str(f) for f in Fs])
for i in range(4):
    GG=s.groebner(Fs[i+1:],*xs,modulus=11) if i<3 else None
    rem=GG.reduce(Fs[i])[1] if GG else Fs[i]
    emit('char11_global_redundancy', row=i+1, remainder=str(rem), is_redundant=(rem==0))
Jac=s.Matrix([[s.diff(f,xx).subs(point)%11 for xx in xs] for f in Fs])
from itertools import combinations
nonzero3=[]
for rr in combinations(range(4),3):
    for cc in combinations(range(4),3):
        det=int(Jac.extract(rr,cc).det())%11
        if det: nonzero3.append({'rows':[j+1 for j in rr],'cols':[j+1 for j in cc],'det':det})
emit('char11_jacobian',matrix=[list(map(int,row)) for row in Jac.tolist()],first_nonzero_3_minor=nonzero3[:1])
emit('complete')
