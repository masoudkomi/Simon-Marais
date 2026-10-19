"""ONE NEW independently designed proof-critical fixed29 finite certificate.
Scalar b=0/1 evaluation and exact Lagrange interpolation, not author's
polynomial-array recurrence, synthetic division, or any old program.
The HAND proof supplies degree bounds and h^2(h-1) divisibility first.
Parent owns a 10-second external timeout and targeted child cleanup.
"""
from fractions import Fraction
from math import comb,gcd
import json
import os
import pathlib
import platform
import subprocess
import sys
import time

def finite_child():
    start=time.monotonic()
    def roots(h,b):
        a=[0]*21
        a[0],a[1],a[3],a[6]=1,-h,2*h**3,-35*h**6
        a[7]=-1+7*h-70*h**3+245*h**6
        a[8]=7-48*h+448*h**3-980*h**6+b
        for j in range(11,19):
            z=1 if j in (14,16,18) else h
            a[j]=-sum(comb(j,i)*a[i]*z**(j-i) for i in range(j))
        return (sum(comb(20,i)*a[i] for i in range(21)),
                sum(comb(20,i)*a[i]*h**(20-i) for i in range(21)))
    table={}
    for h in range(29):
        q0,r0=roots(h,0); qb,rb=roots(h,1)
        table[h]=(q0,qb-q0,r0,rb-r0)

    def interpolate(points,values):
        answer=[Fraction(0)]*len(points)
        for point,value in zip(points,values):
            basis=[Fraction(value)]
            for other in points:
                if other==point:continue
                nxt=[Fraction(0)]*(len(basis)+1)
                for i,c in enumerate(basis):
                    nxt[i]-=c*other/Fraction(point-other)
                    nxt[i+1]+=c/Fraction(point-other)
                basis=nxt
            for i,c in enumerate(basis):answer[i]+=c
        assert all(c.denominator==1 for c in answer)
        return [c.numerator for c in answer]

    rows={}
    for column,(name,bound) in enumerate((('Q0',17),('Q1',9),('R0',20),('R1',12))):
        points=list(range(bound+1))
        rows[name]=list(reversed(interpolate(points,[table[h][column] for h in points])))
    points=list(range(2,29)); values=[]
    for h in points:
        q0,q1,r0,r1=table[h]
        numerator=r0*q1-r1*q0; denominator=h*h*(h-1)
        assert numerator%denominator==0
        values.append(numerator//denominator)
    m=interpolate(points,values)
    content=0
    for c in m:content=gcd(content,abs(c))
    assert content==125970 and all(c%125970==0 for c in m)
    t=[c//125970 for c in m]
    coeff=list(reversed(t))
    residues=[c%29 for c in coeff]
    field_values=[sum(c*x**j for j,c in enumerate(t))%29 for x in range(29)]
    print(json.dumps(dict(status='COMPLETE independently reconstructed finite certificate ONLY; HAND actual-domain/elimination/degree/rational-root proof required',design='two scalar b values and exact Lagrange interpolation with proven bounds; no author expected lists imported',python=platform.python_version(),dependencies='Python standard library only',child_pid=os.getpid(),external_timeout_seconds=10,intrinsic_fixed_points_0_through_28=True,Q0=rows['Q0'],Q1=rows['Q1'],R0=rows['R0'],R1=rows['R1'],identity='N=125970*h^2*(h-1)*T(h)',degree_T=26,integer_T_descending=coeff,T_mod29_descending=residues,T_values_at_0_through_28=field_values,leading_mod29=residues[0],all29_nonzero=all(field_values),elapsed_seconds=time.monotonic()-start,generic_prime_depth_height_search=False,author_source_old_program_executed=False),indent=2),flush=True)

def bounded_parent():
    command=[sys.executable,str(pathlib.Path(__file__).resolve()),'--child']
    child=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
    print(json.dumps(dict(phase='owned child started',pid=child.pid,timeout_seconds=10,command=command)),flush=True)
    try:
        output,_=child.communicate(timeout=10)
    except subprocess.TimeoutExpired:
        child.terminate()
        try:output,_=child.communicate(timeout=2)
        except subprocess.TimeoutExpired:child.kill();output,_=child.communicate()
        print(output,end='')
        print(json.dumps(dict(status='INCOMPLETE timeout; targeted child reaped',pid=child.pid)),flush=True)
        raise SystemExit(2)
    print(output,end='')
    print(json.dumps(dict(phase='owned child finished',pid=child.pid,exit_code=child.returncode,reaped=True)),flush=True)
    raise SystemExit(child.returncode)

if __name__=='__main__':
    if sys.argv[1:] == ['--child']:finite_child()
    else:bounded_parent()
