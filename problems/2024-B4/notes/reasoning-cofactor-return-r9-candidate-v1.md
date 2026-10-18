# Reciprocal and cubic jet tests beyond the no-four-sum condition

2026-10-18 UTC. **Candidate proof - unverified.** Sole NEW constructor B,
`/root/review_2022_complexity_r2`. Requested inherited gpt-6.1-sol/max;
independent effective-setting readback unavailable. Root supplied only the
broad research target and NO NEW mathematical inference. TWO OTHER initially
blind ENTIRE WHOLE audits and full coordinator reconciliation are required;
B cannot be counted. No priority, external validation or annual solution.

This is actual whole-polynomial geometry for official2024 B4(b). The new
test controls the NEXT local coefficient at every possible off-diagonal
component intersection, rather than requiring those singular points to be
absent. ALL ordinary diagonal intersections and their multiplicities remain
in the global budget. It yields explicit infinite higher-binary-weight
families even when the accepted NF4 and root-field gcd tests fail.

## 0. Exact domain, inputs and proposed conclusions

Work over K=F2bar. Put

    W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X),
    f_n=X^n+Y^n+Z^n+W^n, phi_n=f_n/R.

The established quotient is a homogeneous coefficientwise polynomial. The
official question concerns a product of TWO nonconstant polynomials over
F2, equivalently integer lifts nonconstant modulo2; one F2-defined absolute
component or a finite-field function identity does not settle that question.
This packet proves sufficient WHOLE ABSOLUTE irreducibility conditions.

Throughout the main criterion let

    ell>=3 odd, i>=2, q=2^i, n=ell*q+1,
    delta=q^2-q+1, d0=gcd(ell,q-1), N=deg(phi_n)=ell*q-2.

The power q is maximal in n-1 because ell is odd. The binary weight of
n is wt(ell)+1>=3. Define the following condition on the ENTIRE actual
root set mu_ell={a in K:a^ell=1}:

    (J) For every FOUR DISTINCT a,b,c,d in mu_ell with a+b+c+d=0,
        one has a^delta+b^delta+c^delta+d^delta !=0.

Unlike NF4, condition(J) permits zero-sum quadruples. It only forbids
simultaneous vanishing of their delta-power sum. The arithmetic tests and
actual infinite families below make the result more than a conditional
rephrasing of the original factorization question.

**R9A (whole jet criterion).** If(J) holds and (ell,q)!=(3,4), then the
WHOLE phi_(ell*q+1) is absolutely irreducible. No diagonal gcd1 or global
root-field coprimality hypothesis is imposed.

**R9B (two explicit sufficient congruences).** Either

    delta=-2^t mod ell, or delta=3*2^t mod ell,
    for some INTEGER t>=0,                              (C)

implies(J), and hence R9A in its stated domain. These use only reciprocal
and cubic identities on nonzero roots. The inverse function is NOT claimed
APN on every even-degree field, and no published APN theorem is imported.

**R9C (an actual NF4-failing binary-weight-five branch).** For EVERY k>=0,

    phi_(15*2^(4k+2)+1)

is absolutely irreducible. Here mu_15 fails NF4, gcd(4k+2,ord_15(2))=2,
and neither older neighbor congruence15|(q-2) or15|(2q-1) holds. These
are comparisons of exact hypotheses, not published nonoverlap assertions.

Combining this branch with separately accepted R6D and R7A also yields

    phi_(15*2^i+1) absolutely irreducible
    for EVERY i>=2 with i!=4.                            (F15)

The exception i=4 is n241=16^2-16+1; this packet makes no new assertion
there. The entire n classification and all remaining odd parts are open.

**R9D (another explicit unbounded odd-part family).** For EVERY i>=2 and
t>=1, put q=2^i and ell=q^2-q+1+2^t. Then phi_(ell*q+1) is absolutely
irreducible. For t=1 this is

    n=q^3-q^2+3q+1.

No factor table or finite-field scan supplies any statement above.

### Accepted interfaces and attribution

The only old mathematical imports needed by R9A/B/D are:

* **T1**, complete `proofs/reviewed-structural-v1.1.md` and current
  structural acceptance MD/JSON: odd binary weight>=3 excludes EVERY
  absolute line of phi_n.
* **GENERAL R6B/C**, complete
  `proofs/reviewed-reasoning-cofactor-return-r6-v1.1.md` and authority
  MD/JSON: phi_n is reduced, and EVERY nonlinear absolute component
  has degree>=q. The general statement is not restricted to the special
  Mersenne family in R6D. With T1 every positive-degree divisor has
  degree>=q.
* Classical projective Bezout for coprime plane curves and local equality
  I_P(U,V)=m_P(U)m_P(V) when their tangent cones are coprime. These apply
  also to reducible complementary products in characteristic2. The full
  operative proofs in Fulton Sections3.3/5.3 were freshly read.

Only the final combined(F15) additionally imports accepted R6D at Q16 and
R7A's root-field criterion. Their COMPLETE bodies/current MDJSON were freshly
read. The entire accepted R8 and T1–T4 bodies/current authorities and relevant
failures were also read. R7's general local algebra and R8's diagonal budget
motivate this adaptation; their identities are reconstructed explicitly
below, without silently applying their gcd or NF4 theorems outside scope.
No APN/component theorem, genus-on-product bound, R4 small-cofactor theorem,
formal invariant divisor or nonclassical Gauss theorem is imported.

The local/Bezout framework and inverse/cube algebra are classical. Original
McGuire/JMW context and exact prior-source limits are recorded separately.
I previously reviewed T1–T4/R8 and other accepted2024 inputs; that is not
a fresh independent self-certification. I did NOT construct OLD R6/R7/R8.
No published originality of this combination or these families is asserted.

## 1. A local product obstruction, with unit corrections

Let G be a nonzero polynomial near the origin with order r>=2, first
homogeneous term cL^r for c!=0 and a nonzero linear form L. If its next
homogeneous term G_(r+1) is not divisible by L, no product G=UV can have
U(0)=V(0)=0.

Indeed, positive orders u,v would add to r. Unique factorization of binary
forms gives U_u=aL^u,V_v=bL^v. Their degree r+1 product term is
U_u V_(v+1)+U_(u+1)V_v, necessarily divisible by L. This is a contradiction.
Missing next forms mean zero and cause no exception to this reasoning.

If a unit multiplies G, its next form changes by a scalar multiple of the
old initial L^r. Thus nondivisibility by L is preserved. This is a local
no-intersection statement, NOT a claim that G has no singular point or is
globally irreducible. We will apply it to the actual quotient, including
the next-form correction from its denominator.

## 2. The complete possible intersection locus

Reducedness is the accepted general R6B conclusion. Its hypothesis is met
for this odd n, independently of(J). Recall the actual reason: the three
partials of f_n are

    (f_n)_X=(X^ell+W^ell)^q,
    (f_n)_Y=(Y^ell+W^ell)^q,
    (f_n)_Z=(Z^ell+W^ell)^q.                            (1)

Their common projective zero set is finite: W cannot be0 there; after
normalizing W=1 each coordinate is an ellth root. A repeated component
would divide all partials and give an infinite curve in this finite set.
Thus selecting distinct components and their coprime complement is legal.

Any point where two distinct factors of phi_n vanish is singular on phi_n.
At an affine singular point (a:b:1), put c=a+b+1. Since f_n=R phi_n,
f_n and its affine partials also vanish there, INCLUDING R=0 points.
Injectivity of q-Frobenius in(1) gives a^ell=b^ell=c^ell=u.
Substitution into f_n=0 gives u^q+1=0 because a+b+c=1. Hence

    a,b,c belong to mu_ell.                              (2)

In particular they are nonzero. If R(a,b,1)!=0, then a,b,1,c are
pairwise distinct: any equality is equivalent to a=b,a=1 or b=1,
the three excluded diagonals.

There is no omitted intersection at infinity. At Z=0 with R!=0,
(f_n)_Z=(X+Y)^(n-1)!=0, so a point of phi_n there is smooth.
At R=0 the only infinity points are(1:0:0),(0:1:0),(1:1:0).
Differentiating f_n=R phi_n in a direction with R-derivative1 gives
phi_n=1 there: use Y at(1:0:0), X at(1:1:0), and symmetry.
Thus none is on the quotient curve.

Every possible remaining intersection is P=(1:1:1), one of the three
noncentral diagonal root sets, or an off-diagonal affine point as in(2).
Condition(J) will exclude only the LAST type as a component intersection;
such points may still be singular on a single component.

## 3. Off-diagonal jets and the power-sum identity

Fix an off-diagonal point as in(2). Translate X=a+x,Y=b+y,Z=1.
The identity

    (a+x)^(ell*q+1)=(a+x)(a^q+x^q)^ell

shows there are no positive translated terms of degrees2,...,q-1.
The linear term cancels at this singular point. Because ell is odd and
a^ell=b^ell=c^ell=1, the first two POSSIBLE nonzero numerator forms are

    F_q=(A x+B y)^q,
    A^q=a^(1-q)+c^(1-q), B^q=b^(1-q)+c^(1-q),
    F_(q+1)=a^(-q)x^(q+1)+b^(-q)y^(q+1)
                                      +c^(-q)(x+y)^(q+1).    (3)

Unique qth roots A,B exist in K; initially neither is assumed nonzero.
Define the actual scalar

    T=B(b+b^q)+A(a+a^q).

Two exact identities, valid also if one of A,B,A+B vanishes, are

    a^q b^q c^q F_(q+1)(B,A)=T,
    T^q=1+a^delta+b^delta+c^delta.                      (4)

For the first, expand(A+B)^(q+1), clear the displayed nonzero denominator
and substitute A^q,B^q from(3). The coefficient of B reduces to

    b c^q+c b^q+a b^q+b a^q
       =b(a+c)^q+(a+c)b^q=b+b^q,

using a+c=b+1. The coefficient of A similarly becomes a+a^q.
For the second, raise T to the qth power and substitute(3). It gives

    T^q=a+b+a^delta+b^delta
             +c^(1-q)[(a+b)^q+(a+b)^(q^2)].

Since a+b=c+1, the last contribution is c+c^delta, which proves(4).
No division by A,B or A+B has occurred, and no finite-field function
identity has replaced an equality in the local polynomial ring.

Condition(J) applied to the distinct nonzero roots a,b,1,c makes the
right side of(4) nonzero. Thus T!=0, which ALSO proves(A,B)!=(0,0).
This handles the simultaneous-zero case without a root-field gcd
assumption. Set L=A x+B y. The nonzero vector(B,A) spans L=0, so(4)
shows L does not divide F_(q+1).

The denominator is a unit here. Write its translated forms R=R0+R1+...
with R0!=0. Dividing f_n=R phi_n gives

    (phi_n)_q=F_q/R0,
    (phi_n)_(q+1)=F_(q+1)/R0+R1 F_q/R0^2.               (5)

The correction is divisible by L^q and cannot cancel the nonzero
restriction of F_(q+1) to L=0. Hence Section1 with r=q excludes two
factors vanishing at this point. This proves no off-diagonal component
intersection under(J), while allowing genuine singularities there.

## 4. ALL noncentral diagonal points

By symmetry a noncentral diagonal point is(b:1:1), where b in mu_ell
and b!=1. Put c0=b+1,E=b^(-q),B0=1+b^(1-q), and translate
X=b+x,Y=1+y,Z=1. Exact expansion as in Section3 gives

    F_q=B0 y^q,
    F_(q+1)=y[E x^q+E x y^(q-1)+(1+E)y^q],
    R=c0^2 y+c0 y^2+x^2 y+x y^2.                       (6)

Here c0 and E are nonzero. If b not in F_q, then B0!=0, and coefficient
comparison in f_n=R phi_n yields

    (phi_n)_(q-1)=(B0/c0^2)y^(q-1),
    (phi_n)_q=(E/c0^2)x^q+(E/c0^2)x y^(q-1)
                          +[(1+E)/c0^2+B0/c0^3]y^q.     (7)

In particular the next form is not divisible by y, because its x^q
coefficient is nonzero. Section1 with r=q-1>=3 excludes an intersection
of two factors there. It does not assert the point is smooth.

If b in F_q, then B0=0 and E=b^-1. The initial quotient form is now

    (b^-1/c0^2)[x^q+x y^(q-1)+c0 y^q].                 (8)

It has degree/multiplicity q and q DISTINCT tangent lines. Indeed at
y=1 the slope polynomial x^q+x+c0 has derivative1; no direction y=0
is missing because the coefficient of x^q is nonzero. This is an ordinary
point, and the tangent subsets belonging to disjoint factors are coprime.

The common roots of T^ell-1 and T^(q-1)-1 are precisely mu_d0,
d0=gcd(ell,q-1). Both exponents are odd, so these are distinct.
Exactly d0-1 noncentral points of this ordinary kind occur on each
diagonal. The three sets are disjoint, since two diagonals meet only
at P. Thus ALL3(d0-1) ordinary noncentral diagonal points are retained.
No equality of their multiplicity allocations to different components
is assumed.

## 5. The central cone and the global contradiction

At P translate X=1+x,Y=1+y,Z=1. The first nonzero numerator form is
x^q y+x y^q of degree q+1, and R=xy(x+y). Thus phi_n has multiplicity
q-2 and squarefree tangent cone

    (x^(q-1)+y^(q-1))/(x+y)
       =product_(alpha in F_q minus F2)(x+alpha*y).     (9)

The q-2 lines are distinct because q-1 is odd. Factors which miss P
have local order0, and are explicitly allowed.

Suppose the WHOLE phi_n were reducible over K. Select an actual absolute
irreducible component U of LEAST degree e and its actual complementary
product V. Reducedness gives gcd(U,V)=1. T1 excludes lines, and general
R6B/C gives

    q<=e<=N/2,   e(N-e)>=q(N-q)=(ell-1)q^2-2q.          (10)

For the second inequality use(e-q)(N-e-q)>=0. The interval is valid
because N=ell*q-2>=2q for ell>=3,q>=4. This is not a formal invariant
factor or a selected F2 component; V may be reducible and miss points.

At P the tangent cones of U,V partition(9), so the local intersection
is their multiplicity product and is at most(q-2)^2/4, including0 when
one misses P. At each of the3(d0-1) ordinary diagonal points, the same
coprime-cone equality gives at most q^2/4. Sections2–4 exclude ALL other
intersections. Classical projective Bezout therefore gives

    e(N-e)<= [(q-2)^2+3(d0-1)q^2]/4.                 (11)

The exact lower-minus-upper gap from(10)-(11) is

    [(4ell-3d0-2)q^2-4q-4]/4
        >=[(ell-2)q^2-4q-4]/4.                       (12)

For ell>=5,q>=4 the final numerator is at least3q^2-4q-4>=28>0.
For ell=3,q>=8 it is at least q^2-4q-4>=28>0. The only remaining
power-of-two pair is(3,4), where the lower24 and upper25 do NOT
contradict; this pair is expressly excluded. No optimizer or finite
case enumeration is used. Thus reducibility is impossible throughout
R9A's exact domain. This proves the proposed whole jet criterion.

The proof does not assume every component passes P, put a genus formula
on the product V, discard repeated factors without reducedness, or upgrade
one F2-defined component to a whole-polynomial theorem.

## 6. Reciprocal and cubic proofs of condition(J)

Let a,b,c,d be four DISTINCT nonzero elements with a+b+c+d=0.
First their reciprocal sum cannot vanish. Put s=a+b=c+d!=0. If

    a^-1+b^-1=c^-1+d^-1,

then s/(ab)=s/(cd) and ab=cd. Both unordered pairs would be the roots
of the same monic quadratic T^2+sT+ab. They would coincide, contrary
to four distinct elements. Hence their inverse sum is nonzero.

Their sum of cubes is also nonzero: substituting d=a+b+c gives

    a^3+b^3+c^3+(a+b+c)^3=(a+b)(a+c)(b+c)!=0.          (13)

If delta=-2^tmod ell, evaluating on mu_ell makes the delta-power sum
the 2^t-th power of their reciprocal sum. If delta=3*2^tmod ell,
it is the 2^t-th power of their cube sum. Frobenius is injective, so
both sums are nonzero. This proves R9B for t>=0, with no field-degree
coprimality condition. Negative exponents are used ONLY on nonzero roots,
not to define an original polynomial at zero. In particular no false
APN assertion for the inverse function on an even-degree field is needed.

## 7. The NF4-failing ell15 family and its full coverage except i4

Take ell15 and i=4k+2,k>=0. Since2^4=1mod15,

    q=4mod15, delta=4^2-4+1=13=-2mod15.

R9B's reciprocal test applies with t=1. The excluded pair(3,4) is
irrelevant because ell15. This proves the first R9C family uniformly.
Its binary weight is FIVE: shifting the four consecutive ones in15
by i>=2 leaves the separate least bit1 in n=15*2^i+1.

NF4 really FAILS here, without a computer test. mu_15=F_16^* and contains
F4^*. Choose beta in F16 minus F4 and let omega in F4 satisfy
omega^2+omega+1=0. The four elements

    beta, beta+1, beta+omega, beta+omega^2

are distinct, nonzero and have sum0. Thus R8's NF4 premise is unavailable.
They can be scaled by one of their inverses to give a quadruple containing1;
name the other three a,b,c, so c=a+b+1. Direct substitution gives f_n=0
and all three partials zero because each ellth power is1. Distinctness
gives R!=0, so this is an ACTUAL off-diagonal singular point of phi_n.
The new proof excludes component INTERSECTIONS there, not those singular
points themselves.

The order of2 modulo15 is exactly4, because2^4=1 and2,2^2 are not1.
Thus gcd(i,ord_15(2))=2 on this new branch, so R7A's stated criterion
is unavailable. Also q-2=2mod15 and2q-1=7mod15, so the accepted
neighbor-Frobenius congruences do not apply. R6D at ell15 has q=16^k,
which never has i=2mod4. These are literal old-input scope comparisons,
not assertions that these exponents have never been treated in literature.

To obtain(F15), divide the remaining i>=2 into their actual residues
modulo4. Odd i have gcd(i,4)=1 and follow from accepted R7A. Multiples
of4 with i>=8 have q=16^(i/4), i/4>=2, and follow from accepted R6D
with Q16. The 2mod4 case was just proved. Exactly i4 remains outside
these arguments. The identity n241=16^2-16+1 records its special form;
no new factorization or absolute conclusion at that index is imported.

## 8. A variable-odd-part family and known boundary checks

For i>=2,t>=1 set ell=delta+2^t. It is odd and at least15, and
delta=-2^tmod ell holds exactly. Thus R9B/R9A give R9D for every
such parameter pair. Taking t1 gives the displayed cubic-in-q expression.
No assertion that every root set in this additional family fails NF4 is
made or needed. It is a direct infinite family, not a table extrapolation.

The exceptional n13 corner is deliberately preserved: ell3,q4 satisfies
some reciprocal congruences, but the global inequality there is insufficient.
Nothing here upgrades the known ordinary F2 n13 status to absolute
irreducibility. Also n57=7*8+1 does not pass either arithmetic test:
delta1mod7 cannot be a negative power of2, since<2> has odd order3,
nor3times a power of2, since that would put5 in that order3 subgroup
but5^3=-1mod7. No known Kasami counterexample is silently included.

The accepted n205 factor example is not covered either. Here ell51,q4,
delta13. A reciprocal congruence would force2^t=-13mod51; modulo3
this requires t odd, while modulo17 it requires2^t=4 and thus
t=2mod8, since ord_17(2)=8. These are incompatible. A cubic
congruence is impossible already modulo3. These are analytic boundary
checks against actual known examples, not finite searches or new results
about their factorizations.

## 9. Official consequence, source limits and remaining gap

For the stated families, the WHOLE nonconstant homogeneous phi_n is
absolutely irreducible. Any official integer g,h both nonconstant modulo2
would reduce to a product phi_n=bar(g)bar(h) of two positive-degree
polynomials over F2, impossible already over K. Nonhomogeneous lifts
are allowed: irreducibility in the polynomial ring excludes them too.
All statements are coefficientwise, never modulo the function vanishing
ideal of a finite field. n1,n3,ell1,q2 and general remaining exponents are
outside the theorem, not silently classified.

The method adapts accepted local/Bezout arguments, not a new APN theorem
or a classification by absolute lines. Full current operative inputs and
failures were read with exact source limits. The classical no-four-sum
precedents and the original thesis/JMW attribution remain explicit.
The full original joint journal, JW1993 and Férard2017 operative proofs
are not newly claimed read; published overlap/priority is unestablished.
An old search-result remark about5mod8 was NOT imported as a theorem;
its full hypothesis/chronology was not reconstructed here. The accepted
n205 counterexample keeps an unrestricted5mod8 shortcut unavailable;
no new refutation of a fully audited external theorem is asserted.

When both arithmetic tests fail, nothing here proves(J) or its negation.
When(J) fails, the missing global intersection budget is not assigned a
convenient value. The surviving higher-weight/root configurations and the
full annual classification remain open. All proposed results remain
UNVERIFIED until TWO OTHER initially blind WHOLE audits and reconciliation.
No mathematical program, finite scan, CAS, sample table, optimizer, source/
author/old replay, cache change, Git, charge, contact or access bypass
supplies this proof. Entire companions/obligations/checks/source/log/code/
compact metadata, FULL final model readback and SEPARATE verification
are required before handoff. Old bytes remain unchanged.
