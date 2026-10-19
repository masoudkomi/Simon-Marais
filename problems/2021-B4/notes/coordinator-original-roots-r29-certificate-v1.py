"""NEW necessary exact finite certificate, fixed degree20 and prime29 only.
Standard library integer polynomials; no CAS/factorization/search/old replay.
The actual-domain and rational-denominator inference is a separate hand proof.
"""
from math import comb,gcd
from functools import reduce
import json

def add(a,b):
 out=[0]*max(len(a),len(b))
 for i,c in enumerate(a):out[i]+=c
 for i,c in enumerate(b):out[i]+=c
 while len(out)>1 and out[-1]==0:out.pop()
 return out
def scale(a,k):return [k*c for c in a]
def shift(a,k):return [0]*k+a
def mul(a,b):
 out=[0]*(len(a)+len(b)-1)
 for i,c in enumerate(a):
  for j,d in enumerate(b):out[i+j]+=c*d
 while len(out)>1 and not out[-1]:out.pop()
 return out
def total(rows):
 out=[0]
 for row in rows:out=add(out,row)
 return out
def run():
 a=[[0] for _ in range(21)];d=[[0] for _ in range(21)]
 a[0]=[1];a[1]=[0,-1];a[3]=[0,0,0,2];a[6]=[0]*6+[-35]
 a[7]=[-1,7,0,-70,0,0,245];a[8]=[7,-48,0,448,0,0,-980];d[8]=[1]
 for j in range(11,19):
  k=lambda i:j-i if j in (11,12,13,15,17) else 0
  a[j]=total(scale(shift(a[i],k(i)),-comb(j,i)) for i in range(j))
  d[j]=total(scale(shift(d[i],k(i)),-comb(j,i)) for i in range(j))
 q0=total(scale(a[i],comb(20,i)) for i in range(19));q1=total(scale(d[i],comb(20,i)) for i in range(19))
 r0=total(scale(shift(a[i],20-i),comb(20,i)) for i in range(19));r1=total(scale(shift(d[i],20-i),comb(20,i)) for i in range(19))
 n=add(mul(r0,q1),scale(mul(r1,q0),-1));assert len(n)==30
 assert n[0]==n[1]==0
 n=n[2:];quot=[0]*(len(n)-1);quot[-1]=n[-1]
 for i in range(len(n)-2,0,-1):quot[i-1]=n[i]+quot[i]
 assert n[0]==-quot[0] and mul([-1,1],quot)==n
 content=reduce(gcd,(abs(x) for x in quot));assert content==125970
 t=[c//content for c in quot];assert len(t)==27 and all(content*c==q for c,q in zip(t,quot))
 coeff=[c%29 for c in reversed(t)];values=[]
 for x in range(29):
  value=0
  for c in coeff:value=(value*x+c)%29
  values.append(value)
 assert coeff[0]==24 and all(values)
 print(json.dumps({'finite_certificate_only':True,'N_identity':'125970*h^2*(h-1)*T(h)','degree_T':26,'T_integer_coefficients_descending':list(reversed(t)),'T_coefficients_descending_mod29':coeff,'T_values_at_0_through_28':values,'leading_unit':24,'all29_nonzero':True,'Q0_integer_coefficients_descending':list(reversed(q0)),'Q1_integer_coefficients_descending':list(reversed(q1)),'R0_integer_coefficients_descending':list(reversed(r0)),'R1_integer_coefficients_descending':list(reversed(r1))},indent=2))
if __name__=='__main__':run()
