# General small-cofactor route: live hand derivation

2026-10-18 UTC. **Research lead - unverified**, root sole new constructor.
Not a frozen complete theorem packet or an accepted extension. This
records reasoning beyond the accepted special FS1–FS5 family. TWO OTHER
ENTIRE WHOLE audits would be required for any future proposed theorem.

The special F8 orbit structure makes all18 diagonal multiplicities u
equal and all24 off-diagonal multiplicities v equal. For a larger field
F_(2^s), S4/Frobenius need not act transitively on the corresponding
sets. In particular a generalization cannot simply reuse those two
variables or the special denominator6. The following algebra instead
retains sums and uses Cauchy. No field scan or CAS was used.

Suppose, as EXPLICIT UNPROVED-APPLICATION hypotheses, that ell>=7,
q>0 and a reduced homogeneous phi of degree ell*q-2 has precisely
the analogous ordinary singularities: P multiplicityq-2;
3(ell-1) diagonal points multiplicityq; and
o=(ell-1)(ell-3) off-diagonal points multiplicityq+1. Suppose three
exact prescribed line identities hold, phi has no absolute lines, and
phi=GH is a coprime actual factorization with H reduced of degree e>0.
These assumptions have NOT been proved for every proposed new ell/q
family here, and no general unique-large-component theorem is supplied.

Write m=mP(H), t=e-m, r_j its diagonal multiplicities, s_j the
off-diagonal multiplicities. The line identities give sum r_j=3t.
Put V=sum s_j and D=(ell-3)e+2m-V=(ell-1)e-2t-V. Exact projective
Bezout expands to

 qD=2e+e²-2m-m²-sum r_j²+V-sum s_j².             (A)

The accepted FS proof's classical REDUCED bound, applied componentwise
with no absolute lines, gives

 m(m-1)+sum r_j(r_j-1)+sum s_j(s_j-1)<=e²-2e.

Substitution into(A) yields qD>=4e-3m-3t=e>0. Hence D is a positive
INTEGER without any orbit-uniformity assertion. This general positivity
is a useful idea; it is conditional on the complete geometric inputs.

Cauchy gives sum r_j²>=3t²/(ell-1) and sum s_j²>=V²/o.
Set Aell=(ell-2)(ell+1), avoiding confusion with equation(A).
Eliminate V=(ell-1)e-2t-D. The resulting upper quadratic in t is

 qD <= (ell-1)e-D+2et-[(ell+2)/(ell-1)]t²
                    -[((ell-1)e-2t-D)²/o].        (B)

Its negative t² coefficient is Aell/o. Completing that square over
ALL real t, rather than asserting an actual feasible maximizer, gives

 qD <= (ell-1)e-D
       -[(ell-1)e²-2ell*eD+((ell+2)/(ell-1))D²]/Aell,

 D[q+1-(2ell/Aell)e]
       <=(ell-1)e-(ell-1)e²/Aell
                            -[(ell+2)/((ell-1)Aell)]D²
       <=(ell-1)Aell/4.                            (C)

The last step completes the e square at Aell/2. Therefore a geometric
small-cofactor bound e<=E would exclude this factorization if

 q+1-(2ell/Aell)E > (ell-1)Aell/4.                 (D)

This is a CONDITIONAL route, not an actual new exponent exclusion.
It needs a real degree bound E with sufficient coefficient and all
projective singularity/contact/no-line inputs checked. An F2 component
existence theorem alone gives neither that bound nor full invariance.

Consistency check by hand: ell7 has Aell40 and the same bracket
q+1-7e/20 as FS. Here D is SIX times the special FS integer. Discarding
its additional divisibility only gives D>=1, so(C) has upper60 rather
than10. With E=2q+8 this coarse version would need q>206, covering
q>=512 but losing the smallest q64 instance. The actual reviewed FS
orbits prove the stronger divisibility/normalization and cover q64.
This explains why general Cauchy bounds cannot simply replace the
orbit argument without tracking their integer loss.

Further rejected shortcut: S4 is transitive on the24 orderings of one
projective nonzero four-element set, but larger fields have MANY scalar
orbits of such sets. Their multiplicities cannot all be made one v.
Likewise coefficient Frobenius can split diagonal inverse-pair labels.
Any improvement must keep those orbit blocks or genuinely bypass them.

No mathematical executable, scan, numerical count, finite certificate,
published-author program or old computation was run. These are live
algebraic notes only; all displayed formulas and the new general
application require an eventual full constructor packet and TWO OTHER
whole audits before promotion. Priority remains unestablished.
