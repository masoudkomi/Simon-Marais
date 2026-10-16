#!/usr/bin/env python3
"""Independent, finite identity checks. These are not CA counterexamples."""
import json
import os
import platform
import time
from fractions import Fraction

NAMES = ('x', 'y', 'z', 'X', 't', 'u', 'B0', 'B1', 'k1', 'k2')
ZERO_EXP = (0,) * len(NAMES)


class P:
    def __init__(self, terms=0):
        if isinstance(terms, P):
            self.terms = dict(terms.terms)
        elif isinstance(terms, dict):
            self.terms = {e: Fraction(c) for e, c in terms.items() if c}
        else:
            self.terms = {ZERO_EXP: Fraction(terms)} if terms else {}

    def __add__(self, other):
        other = P(other)
        result = dict(self.terms)
        for e, c in other.terms.items():
            result[e] = result.get(e, 0) + c
        return P(result)

    __radd__ = __add__

    def __neg__(self):
        return P({e: -c for e, c in self.terms.items()})

    def __sub__(self, other):
        return self + -P(other)

    def __rsub__(self, other):
        return P(other) + -self

    def __mul__(self, other):
        other = P(other)
        result = {}
        for a, c in self.terms.items():
            for b, d in other.terms.items():
                e = tuple(i + j for i, j in zip(a, b))
                result[e] = result.get(e, 0) + c * d
        return P(result)

    __rmul__ = __mul__

    def __pow__(self, power):
        result = P(1)
        for _ in range(power):
            result = result * self
        return result

    def subst(self, **values):
        result = P(0)
        for e, c in self.terms.items():
            term = P(c)
            for name, degree in zip(NAMES, e):
                term = term * (P(values.get(name, variables[name])) ** degree)
            result = result + term
        return result


variables = {}
for i, name in enumerate(NAMES):
    e = list(ZERO_EXP)
    e[i] = 1
    variables[name] = P({tuple(e): 1})
globals().update(variables)


def emit(kind, **fields):
    print(json.dumps({'kind': kind, 'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), **fields}, sort_keys=True), flush=True)


def zero(label, expression):
    assert not expression.terms, (label, expression.terms)
    emit('exact_identity', label=label, residual_terms=0)


emit('start', pid=os.getpid(), python=platform.python_version(), dependencies=['Python standard library: fractions, json'], variable_order=NAMES)
zero('coordinator_Qt_identity', (1-t*X)*(1+t*X)+X**2*t**2-1)
emit('checkpoint', stage='coordinator_model_complete')

f = [y**2, x*y, x**2, z]
g = [P(1), P(2), P(3), P(1)]
h, b, a = f[0]-z*g[0], f[1]-z*g[1], f[2]-z*g[2]
for i in range(4):
    for j in range(i+1, 4):
        delta = f[i]*g[j]-f[j]*g[i]
        zero(f'determinantal_internal_minor_{i+1}_{j+1}', delta-(g[j]*(f[i]-z*g[i])-g[i]*(f[j]-z*g[j])))
certificate = (z+h)*a+(-4*z-b)*b+3*z*h
zero('determinantal_z_squared_certificate', z**2-certificate)
zero('determinantal_polynomial_unit_certificate', (1-z*X)*(1+z*X)+X**2*certificate-1)
r1, r2 = x**2-3*y**2, x*y-2*y**2
zero('quotient_y_cubed_certificate', y*r1-(x+2*y)*r2-y**3)
zero('quotient_x_y_squared_certificate', y*r2+2*y**3-x*y**2)
zero('quotient_x_squared_y_certificate', y*r1+3*y**3-x**2*y)
zero('quotient_x_cubed_certificate', x*r1+3*x*y**2-x**3)
emit('finite_linear_algebra', label='degree_two_quotient', basis=['x^2','x*y','y^2'], relation_rows=[[1,0,-3],[0,1,-2]], rank=2, y_squared_in_relation_span=False, justification='first two coordinates force both coefficients to zero')
emit('monomial_generator_check', label='J_minimal_generators', generators=['z','x^2','x*y','y^2'], count=4, justification='no listed monomial divides another')
emit('checkpoint', stage='determinantal_model_complete')

generators = [(1,2),(0,3)]  # t*y^2, y^3 in Q[t,y]
contains = lambda e: any(all(i>=j for i,j in zip(e,g)) for g in generators)
assert not contains((0,2)) and contains((1,2))
emit('monomial_ideal_check', ideal=['t*y^2','y^3'], y_squared_nonzero=True, t_times_y_squared_zero=True, localized_ideal_when_t_unit=['y^2'], nonzero_localization_witness='evaluation y=0 maps onto Q[t,t^-1]')

closure = B1*(k2*B0-k1*B1)
zero('incidence_path_on_total_closure', closure.subst(B0=u,B1=1,k1=u,k2=1))
zero('special_total_fiber_equation', closure.subst(k1=0,k2=1)-B0*B1)
zero('infinity_point_in_special_total_fiber', closure.subst(B0=0,B1=1,k1=0,k2=1))
emit('closure_check', special_parameter=[0,1], finite_affine_fiber=['b=0'], closure_of_affine_fiber='B1=0', additional_total_closure_fiber_point=[0,1], path={'b':'1/u','B':[ 'u','1'],'K':['u','1']})
emit('complete', all_assertions_passed=True, scope='finite identities and finite-dimensional model calculations only')
