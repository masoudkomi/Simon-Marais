# A composite-conductor unit issue in Schmidt's Proposition 3.1(a)

18 October2026UTC. **Exploratory source objection — unverified.** Root
constructed this argument and is excluded from its independent review.
This is not a new taut order, a mixed-order exclusion, a verdict on the
paper's main theorems or an accepted mathematical result. The sealed
SQ16 review was completed before this separate research/download; its
frozen source record remains unchanged.

## Source and literal reading

Bernhard Schmidt, [Cyclotomic Integers of Prescribed Absolute Value and
the Class Group](https://personal.ntu.edu.sg/bernhard/Publications/pub/class.pdf).
The original author's PDF has encoded text extraction. A local download
and Poppler rendering made the pages readable. Fresh visual reading
covers complete printed pages1--10, including the COMPLETE statement and
supplied proof of Proposition3.1 across pages8--9. This is not a full
16-page/reference-chain audit. The PDF remains ignored/local; its exact
retrieval identity is in the source JSON. No licence for Git redistribution
has been established or assumed.

Proposition3.1(a), as printed for arbitrary positive integers m,n and a
principal ideal A=(y) of O_m with A*bar(A)=(n), asserts equivalence between
a SAME-ideal integral solution x*bar(x)=n and n/(y*bar(y)) being a square
of a real unit. Its proof treats every cyclotomic unit as a product of a
real unit and a root of unity. The following proposed counterexample
tests that step at a composite conductor. It does not specialize the
standing prime-conductor field of SQ14--SQ16 to a composite one.

## Hand counterexample proposed for the printed scope

Let zeta be a primitive fifteenth root of unity, K=Q(zeta), E its maximal
real subfield, and u=1-zeta. The identity

    Phi_15(X)=(X^15-1)(X-1)/[(X^5-1)(X^3-1)]

gives Phi_15(1)=1 by cancelling the simple factors at1. Therefore
the algebraic integer u has absolute field norm1 and is a UNIT of O_K.
Set eta=u*bar(u), a positive real unit.

Eta is NOT a square in E. Suppose v in E had v²=eta. Then w=u/v
would lie in K and satisfy

    w²=u²/(u*bar(u))=u/bar(u)=-zeta,

since bar(u)=1-zeta^-1=-zeta^-1*u. The root -zeta has order30:
if zeta=exp(2*pi*i*a/15), gcd(a,15)=1, its exponent in mu_30 is
2a+15, coprime to30. An element whose square has order30 must have
order60. Thus w is a primitive sixtieth root. That would put the
degree16 field Q(zeta_60) inside the degree8 field Q(zeta_15), which
is impossible. This proves the proposed nonsquare assertion without
assuming an unproved cyclotomic unit decomposition or a numerical test.

Now choose n=4, y=2u and A=(y)=(2). Then A*bar(A)=(4), and x=2
is an actual INTEGRAL element with (x)=A and x*bar(x)=4. Nevertheless

    n/(y*bar(y))=eta^-1

is not a square in E, hence is not a square of a real unit. This
contradicts the printed equivalence if the displayed scope is taken
literally. The example uses n>1 and is not merely its unit-norm boundary.

## Scope of the objection and the square-ideal repair

This does not contradict the independent SAME-SQUARE-IDEAL construction
used in the project's corrected integral SQ14/SQ15 arguments. Indeed,
in any such balanced principal ideal A=(y), let epsilon=y*bar(y)/n,
which is a real unit because both ideals equal(n). Then

    z=y²/epsilon

is integral, has (z)=A² and z*bar(z)=n². No square root of epsilon
is needed. Thus Proposition3.1(b)'s square-ideal conclusion has this
direct proof even if the stated proof of part(a) needs qualification.
Nothing here corrects the SAME ideal A without its actual unit condition.

The proposed obstruction is specifically the composite-conductor
unit step; it supplies no counterexample in the project's actual
prime-conductor fixed field, no loss of the retained Gamma obstruction,
and no refutation of all later class-group theorems in the paper.
A repair might need a unit-index hypothesis or the precise norm-unit
image, rather than the universal real-unit-square assertion. That
repair and its hypotheses have not been independently audited here.

Two OTHER adversarial reviews are required before calling this objection
proved, independently reviewed. No mathematical program/CAS/scan/routine
test or old executable replay was used. Curl/Poppler only retrieved and
rendered the source; SHA checks identify bytes, not mathematical truth.
No charge, contact, access bypass or full-paper Git upload occurred.
