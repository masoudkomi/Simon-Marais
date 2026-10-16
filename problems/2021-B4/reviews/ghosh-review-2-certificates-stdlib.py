"""Exact finite independent R2 checks; standard library only; use 30s child timeout."""
from fractions import Fraction
from itertools import combinations
import json, os, platform
N=5
ZERO=(0,)*N
class P:
    def __init__(self,v=0):
        self.d=dict(v.d) if isinstance(v,P) else ({e:c for e,c in v.items() if c} if isinstance(v,dict) else ({ZERO:v} if v else {}))
    def __add__(self,o):
        o=P(o); d=dict(self.d)
        for e,c in o.d.items(): d[e]=d.get(e,0)+c
        return P(d)
    __radd__=__add__
    def __neg__(self): return P({e:-c for e,c in self.d.items()})
    def __sub__(self,o): return self+-P(o)
    def __rsub__(self,o): return P(o)+-self
    def __mul__(self,o):
        o=P(o); d={}
        for a,c in self.d.items():
            for b,e in o.d.items():
                k=tuple(x+y for x,y in zip(a,b)); d[k]=d.get(k,0)+c*e
        return P(d)
    __rmul__=__mul__
    def __pow__(self,n):
        a=P(1)
        for _ in range(n): a=a*self
        return a
    def deriv(self,i):
        d={}
        for e,c in self.d.items():
            if e[i]:
                k=list(e); k[i]-=1; d[tuple(k)]=c*e[i]
        return P(d)
    def at(self,v): return sum(c*prod(x**p for x,p in zip(v,e)) for e,c in self.d.items())
    def text(self): return [[list(e),c] for e,c in sorted(self.d.items())]
def prod(seq):
    r=1
    for x in seq: r=r*x
    return r
def variable(i):
    e=[0]*N; e[i]=1
    return P({tuple(e):1})
def emit(event,**kw): print(json.dumps(dict(event=event,**kw),sort_keys=True),flush=True)
def mons(n,d):
    if n==1: yield (d,)
    else:
        for k in range(d+1):
            for rest in mons(n-1,d-k): yield (k,)+rest
def rank(matrix,p=None):
    A=[[Fraction(c) if p is None else int(c)%p for c in row] for row in matrix]
    if not A: return 0
    r=0
    for j in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][j]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=1/A[r][j] if p is None else pow(A[r][j],-1,p)
        A[r]=[c*inv if p is None else c*inv%p for c in A[r]]
        for i in range(len(A)):
            if i!=r:
                c=A[i][j]
                A[i]=[a-c*b if p is None else (a-c*b)%p for a,b in zip(A[i],A[r])]
        r+=1
        if r==len(A): break
    return r
def poly_rank(polys,p=None):
    es=sorted(set().union(*(q.d.keys() for q in polys))) if polys else []
    return rank([[q.d.get(e,0) for e in es] for q in polys],p)
emit('dependencies',pid=os.getpid(),python=platform.python_version(),libraries='standard library only')
x,y,z,t,X=[variable(i) for i in range(N)]
a,b,h=x*x-3*z,x*y-2*z,y*y-z
cert=(z+h)*a+(-4*z-b)*b+3*z*h
emit('nilpotent_certificates',simple_residual=((1-t*X)*(1+t*X)+X*X*t*t-1).text(),
     z_squared_residual=(cert-z*z).text(),inverse_residual=((1-z*X)*(1+z*X)+X*X*cert-1).text())
q1,q2=x*x-3*y*y,x*y-2*y*y
qs=[q1,q2]; cs=[v*q for v in (x,y) for q in qs]
emit('artinian_quotient',degree2_rank=poly_rank(qs),degree2_rank_with_y_squared=poly_rank(qs+[y*y]),
     degree3_rank=poly_rank(cs),degree3_monomial_count=4,
     y_cubed_certificate_residual=(x*q2-y*q1+2*y*q2+y**3).text())
cols=[(y*y,1),(x*y,2),(x*x,3),(z,1)]; d4=[h,b,a,P(0)]
res=[]
for i,j in combinations(range(4),2):
    minor=cols[i][0]*cols[j][1]-cols[j][0]*cols[i][1]
    res.append((minor-(cols[j][1]*d4[i]-cols[i][1]*d4[j])).text())
emit('all_minor_identities',residuals=res)
emit('translated_torsion_identity',residual=(x*x*(x*(y+t))-y*x**3-t*x**3).text())
emit('incidence_model',formula='B1*(K2*B0-K1*B1)',special_fiber_K_0_1='B1*B0',
     escaping_curve='B=[epsilon:1], K=[epsilon:1]',escaping_curve_residual='1*(1*epsilon-epsilon*1)=0')
xs=[variable(i) for i in range(4)]; marks=[1,2,2,1]
def elementary(seq,k): return sum((prod(q) for q in combinations(seq,k)),P(0))
Fs=[]
for i,j in enumerate(marks,1):
    shifted=[xx-xs[j-1] if k!=j-1 else -xs[j-1] for k,xx in enumerate(xs)]
    Fs.append(elementary(shifted,5-i))
pt=[0,1,4,6,0]
emit('char11_actual_family',n=4,p=11,marks=marks,point=pt[:4],exclusion_product=96,
     values=[f.at(pt)%11 for f in Fs],generators_exponent_coefficient=[f.text() for f in Fs])
minimal=0
for i in range(4):
    span=[]
    for j in range(i+1,4):
        for e in mons(4,j-i): span.append(P({e+(0,):1})*Fs[j])
    r0=poly_rank(span,11); r1=poly_rank(span+[Fs[i]],11); minimal+=r1-r0
    emit('char11_global_redundancy',row=i+1,degree=4-i,rank_lower_span=r0,rank_with_target=r1,is_redundant=(r1==r0))
Jac=[[f.deriv(i).at(pt)%11 for i in range(4)] for f in Fs]
emit('char11_jacobian',matrix=Jac,rank=rank(Jac,11),global_minimal_generators=minimal)
emit('complete')
