# R8: independent entire whole review 1

2026-10-18 UTC. Reviewer root; constructor C is excluded. Requested
inherited gpt-6.1-sol/max; independent effective-setting readback is
unavailable. The submission remains **candidate proof - unverified**
until the other entire audit and coordinator reconciliation. This report
is initially blind to every corresponding NEW B R8 finding, file, hash
and metadata record. Completion identities are administrative only.

I independently reconstructed all 48 obligations by hand and found no
substantive defect or required author repair in R8A--R8C's stated scope.
Seven closed boundary checks are recorded separately. All thirteen
author files were read completely, including both source records, all
48 obligations/checks, failures, worklog, code record, administration
source and every generated metadata file. An initially guessed source
filename did not exist; the actual source-audit-v1.md was then read in
full. A failed filename read is not credited as a source read.

## Exact domain and operative inputs

The official 2024 B4(b) asks for coefficientwise polynomial factors over
F2, equivalently integer lifts nonconstant modulo 2. It does not ask for
factorization of polynomial functions on a finite field. I read the
official setup and (b), extracted lines 57--75. No preliminary proof was
investigated. Set K=Fbar_2, W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X),
f=X^n+Y^n+Z^n+W^n, and phi=f/R. Here n=ell*q+1, ell>=3 odd,
q=2^i with i>=2, and NF4 forbids four DISTINCT ellth roots with sum zero.
The exception (ell,q)=(3,4), n=13, is explicitly retained.

I freshly read the COMPLETE T1--T4 accepted body and both current
structural authorities, and the COMPLETE general R6 body and both current
authorities. Only T1 and general R6B/C are operative: all absolute lines
are absent, f and phi are reduced, and EVERY nonlinear absolute component
has degree at least q. R6D's special family is not substituted for the
general statement. Root's older CG/R4/R5 construction and older reviews
are disclosed; their separately accepted results are not independently
self-recertified here. C's older R6/R7 construction is also disclosed.
R7, APN/component theorems, R4/R5 bounds and invariant cofactors are not
premises of this new proof.

## 1. All actual intersection points are covered

Since ell is odd, q is the maximal 2-power in n-1. The shifted bits of
ell do not overlap the final bit, so wt(n)=wt(ell)+1>=3. Thus T1 applies.
The coefficient of X^(n-1)Y in f is 1, so f is nonzero. Its full
homogeneous gradient has entries (X^ell+W^ell)^q and their Y/Z analogues.
At a simultaneous zero W cannot be zero; normalizing W=1 leaves only
ellth-root coordinates, a finite set. A repeated homogeneous irreducible
factor would divide all partials and produce an infinite projective
curve inside that set. This proves reducedness independently as well.

Any intersection of coprime positive-degree factors U,V of phi is
singular on phi. At an affine singular point (a:b:1), l=a+b+1,
f=R phi and the product rule give f=f_X=f_Y=0 even on R=0.
The derivatives imply a^ell=b^ell=l^ell=u. Substitution gives
f=(a+b+l)u^q+1=u^q+1, so u=1; the Frobenius q-power is injective.
In particular a,b,l are nonzero. Off the three diagonals, a,b,1,l
are all distinct: each possible equality gives a=b, a=1 or b=1.
Their sum is zero, contradicting NF4. Thus no off-diagonal affine
intersection was omitted.

At infinity Z=0 and R!=0, the full Z partial is
(X+Y)^(n-1)!=0. Differentiating f=R phi implies phi is smooth there.
The points with Z=0 and R=0 are exactly (1:0:0),(0:1:0),(1:1:0).
Using respectively a transverse Y or X partial, f and R have the same
derivative value 1; hence phi=1. Those vertices are not on the curve.
This handles the projective chart, rather than just the two affine
partials at infinity. Remaining intersections are P=(1:1:1) or one of
the three disjoint noncentral diagonal sets (b:1:1), b^ell=1,b!=1.

## 2. Both noncentral local cases

At (b:1:1), put X=b+x,Y=1+y,Z=1, c=b+1, E=b^-q and
B=1+b^(1-q). Exact Frobenius expansion gives

    f_q=B y^q,
    f_(q+1)=E x^q y+E x y^q+(1+E)y^(q+1),
    R=c^2 y+c y^2+x^2 y+x y^2.

The denominator identity follows by multiplying (c+x+y)y(c+x);
the two cxy terms cancel in characteristic 2. Both c and E are
nonzero, regardless of whether B vanishes.

If b is not in F_q, B!=0. Comparing degrees q and q+1 in f=R phi
gives

    phi_(q-1)=(B/c^2)y^(q-1),
    phi_q=(E/c^2)x^q+(E/c^2)x y^(q-1)
           +[(1+E)/c^2+B/c^3]y^q.

The B/c^3 term is the unit correction and is not discarded. The
nonzero x^q coefficient means the second form is not divisible by y.
If two polynomial factors vanished at this point, their positive
orders r,s sum to q-1 and their initial forms are scalar y^r,y^s.
Their next product form is divisible by y, even if one next form is
zero, contradicting the displayed phi_q. Thus such a point cannot
contribute to an intersection. No irreducibility or reducedness of
the complementary product at the point is needed for this obstruction.

If b is in F_q, B=0 and E=b^-1. The leading quotient is

    (b^-1/c^2)(x^q+x y^(q-1)+c y^q).

It has exact order q and q distinct tangent lines: at y=1 the
polynomial x^q+x+c has derivative 1; the leading x^q coefficient
also excludes an additional tangent y=0. Distinct factors partition
these tangents and therefore have coprime initial forms. The common
roots of T^ell-1 and T^(q-1)-1 form precisely mu_d,
d=gcd(ell,q-1). All roots are simple since both exponents are odd.
Removing b=1 leaves exactly 3(d-1) distinct ordinary diagonal points.
The three diagonal lines meet each other only at P, so none is counted
twice. The other diagonal points have the zero-intersection behavior
just proved.

## 3. Central cone and the actual factor-degree contradiction

At P, the numerator's first surviving term is x^q y+x y^q and
R=xy(x+y). Therefore phi has exact multiplicity q-2 and tangent cone

    (x^(q-1)+y^(q-1))/(x+y)
      = product_(alpha in F_q minus F2)(x+alpha y).

It is squarefree, including at q=4. If phi were reducible over K,
take an ACTUAL absolute irreducible component U of least degree e.
Reducedness ensures V=phi/U has no common component with U. With
N=ell*q-2, the complete general R6 bound and T1 give

    q<=e<=N/2,   N>=2q,
    e(N-e)-q(N-q)=(e-q)(N-e-q)>=0.

Thus Bezout's left side is at least (ell-1)q^2-2q. This is the
same actual U to which the component bound applies; V may be a
reducible product. No all-components-through-P statement is used.

At P the two multiplicities add to q-2, their tangent subsets are
disjoint, and the local intersection equals their product, at most
(q-2)^2/4. If one factor misses P, both the intersection and product
are zero. At each ordinary diagonal point the same argument gives
at most q^2/4. Every other projective intersection is excluded above.
Projective Bezout, with no common component, consequently gives

    e(N-e)<=((q-2)^2+3(d-1)q^2)/4.

The lower-minus-upper difference is exactly

    ((4ell-3d-2)q^2-4q-4)/4
       >=((ell-2)q^2-4q-4)/4.

For ell>=5,q>=4, its numerator is at least
3q^2-4q-4>=28. For ell=3,q>=8 it is at least q^2-4q-4>=28.
These follow monotonically from q(3q-4)-4 and q(q-4)-4;
no numerical optimization is required. The only remaining permitted
power-of-two pair is (3,4). Its lower bound is 24, upper 25 because
d=3, so no contradiction is claimed there. Every other stated pair
contradicts Bezout. This proves the whole-polynomial R8A in its exact
domain, not merely existence of one absolute component.

## 4. Arithmetic conditions and literal comparison

For 2^t=-1 modulo ell, Frobenius sends every root a to a^-1.
Four distinct roots with a+b=c+d=s have s!=0. Applying Frobenius
gives s/(ab)=s/(cd), so ab=cd. Both pairs are the root multiset of
the same monic quadratic T^2+sT+ab, contradicting four distinct roots.
For 2^t=3 modulo ell, Frobenius makes the sum of their cubes zero.
After d=a+b+c, that sum is (a+b)(a+c)(b+c), nonzero by distinctness.
These are complete sufficient-condition proofs, including composite
odd ell; neither is asserted necessary. They are classical conditions
stated immediately before the original thesis's Theorem 6.

At ell=11, 2^5=-1 modulo 11, and the order of 2 is exactly 10:
the proper divisors 1,2,5 all fail. At ell=23, 2^8=3 and 2^11=1;
since 11 is prime and 2!=1, the order is 11. Neither ell can produce
the exceptional pair. Thus EVERY i>=2 is included in both R8C
families. For i=10k or 11k respectively, gcd(i,ord_ell(2)) is not 1
and gcd(ell,2^i-1)=ell, so the older literal conditions fail. The
binary weights are 4 and 5. This is a comparison of stated hypotheses,
not a priority or exhaustive-literature claim.

## 5. Actual primary-source reading and limits

I freshly visually read ALL eleven existing thesis images 21--31,
printed pages 16--26, including the local expansions/lemmas, COMPLETE
Theorems 6/7 statements and supplied proofs, and the later returned
Theorem 8 context. Theorem 6 has q=4 and n>13. Theorem 7 additionally
requires gcd(ell,q-1)=1. The code formulation is literally equivalent
to NF4: four distinct exponents of a primitive ellth root are four
distinct elements of mu_ell. No unread JW coding theorem fills a gap.
The original joint journal PDF, JW1993 full proof and Ferard2017 body
remain unread; this proof makes no nonoverlap or new-method claim.

I freshly browser-read Fulton's Section 3.3 properties 1--7 and ENTIRE
Theorem 3 proof, extracted 2419--2624, plus the returned properties
8/9 through 2673, and Section 5.3's ENTIRE Bezout proof, 3829--3924.
The no-common-component and coprime-tangent hypotheses apply to these
actual products and in characteristic 2. Appendix A was freshly read
by the constructor, not by root in this audit. No whole 129-page or
foundational geometry audit is claimed. Source URLs/read scopes and
the existing local scan identity are recorded separately.

Absolute irreducibility forbids the official F2 polynomial factors,
including nonhomogeneous integer lifts. No APN/function-ring or
one-component shortcut is used. NF4-failing root sets, q=2, ell=1,
n=1/3, the exceptional absolute n=13 assertion, the full annual
classification and priority remain outside this result. All new math
was hand reasoning. Metadata administration preserves bytes/labels
only; no CAS, scan, mathematical test, source/author executable or
historical certificate was rerun. Entire frozen peer packets will be
read only after BOTH explicit entire completion confirmation.
