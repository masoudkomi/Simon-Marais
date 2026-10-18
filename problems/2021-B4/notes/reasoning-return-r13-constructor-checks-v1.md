# R13 hand constructor checks, not independent review

18 October 2026 UTC. Candidate proof - unverified. These are a second
arithmetic presentation of the NEW proof, supplied by its constructor.
They are not two independent audits, tests, code output or a lift.

## 1. All affine residual values

For R=11+v−C+B in the main, the following is R at v=0,1,2 after
substitution of u,t and the forced B,C. Every entry comes directly
from the three displayed affine equations; none is zero.

| u / t | 0 | 1 | 2 |
|---|---|---|---|
| 0 | (11,12,13) | (17,6,14) | (16,12,8) |
| 1 | (7,1,14) | (6,2,17) | (3,1,18) |
| 2 | (17,9,1) | (9,17,6) | (4,9,14) |

Equivalently each coefficient F is nonzero and Fv+G=0 has the
single root listed in the main. Their integer checks before reduction
are

    1*8+11=19, 8*5+17=57, 15*4+16=76,
    13*17+7=228, 15*11+6=171, 17*11+3=190,
    11*14+17=171, 8*6+9=57, 5*3+4=19.

Thus the complete proof-critical certificate is hand reproducible in
either direction. It does not enumerate coefficient masks or valuations.

## 2. Euler functional from direct coefficients

With A=a6 a unit, define the integral residues

    c=a10/(A r^4), b=a9/(A r^3),
    d=a8/(A r^2), e=a7/(A r).

The reduced quartic before any reflection is

    q(z)=c+10b z+7d z^2+6e z^3+z^4.

Also D8(r)/(A r^2)=d+8e+9 modulo19. The surviving W terms therefore
give

    0=q(1)+5(d+8e+9)+3
     =c+10b+12d+8e+11.

If q(0)=0, c=0. In the monic coefficient form of the main,
B=10b, C=7d, −4v=6e. Thus12d=−C and8e=v modulo19, giving
R=11+v−C+B exactly. This independently checks the Hasse conversion
and the final3 from beta6/beta10. If the root was2, the pure field
reflection is performed first; the functional is unchanged.

## 3. Depth and exact-zero boundaries

The T4 terms for degrees ell=0,1,2,3 in D10(rz) have valuations at
least4nu in every case. At ell4 the coefficient has valuation4nu
and unit factor210A; at ell>=5 the valuation exceeds4nu. A zero
coefficient has infinite valuation, which only strengthens this.
For i=1,2,3 in the derivative scaling, the analogous denominators
have depths3nu,2nu,nu; all remaining coefficients meet them.

The W denominator has depth4nu+1. The left side is zero for delta0
or has depth at least9nu+1. The later h16/h18 terms have depths at
least6nu+1 and8nu+1; r^10 has depth10nu. The corresponding excesses
are at least5nu,2nu,4nu and6nu−1, all positive for every integer nu>=1.

No finite displacement bound or selected-depth bound10 is used. a5
is allowed to be unit. a7,a8,a9,a10 may vanish exactly. A=a6 is
divided only AFTER accepted R12A has forced it to be a unit.

## 4. Whole-fork and carrier boundaries

An essential H12 center with NONUNIT a8 is ruled out using Q6; a
unit H12 center is not declared impossible. In the latter unit-a8
case R8 already cannot choose T4 or its NONUNIT EC12 alternative.
Under T4, if an order has no noncenter witness, its constant cannot
vanish, because 0 is an actual root of f. Hence the supplied center
meets the exact nonzero qualification, and the depth bounds give EC.

The global full-gcd claim uses the actual rational irreducible g of
degree14 and derivative degrees10/9. It does not infer rationality
from local Eisenstein irreducibility, promote a Q19 zero, use the
equal-degree H6 trace boundary without checking it, or declare the
degree-six quotient CA. Simple1 fixes gcd multiplicity one.
