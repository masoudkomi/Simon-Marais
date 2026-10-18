# A general ordinary-singularity threshold for whole irreducibility

2026-10-18 UTC. **Candidate proof - unverified.** Sole NEW constructor
`/root`. Requested inherited gpt-6.1-sol/max; independent effective
readback unavailable. TWO OTHER initially blind ENTIRE WHOLE audits
and coordinator reconciliation are required. Only official2024 B4(b)
is investigated. No full exponent classification or novelty is claimed.

The conditional general-cofactor algebra in the earlier live note can
be applied to ACTUAL curves, without first constructing a unique large
component. A second global inequality forces ANY smaller factor below
a useful degree threshold. The reduced-curve multiplicity bound then
contradicts its existence when q is large enough. No orbit-uniformity,
F2-definition of the chosen factor, or Frobenius/Gauss-map theorem is
needed. All derivations below are by hand, with no mathematical program.

## 0. Exact theorem proposed and relation to accepted work

Let s>=3 and k>=1 be integers and set

    Q=2^s, ell=Q-1, q=Q^k, n=ell*q+1,
    Aell=(ell-2)(ell+1),
    Lell=(ell-1)(ell-2)(ell+1)^2/4.

Thus ell>=7 is odd, q fixes F_Q, and n is odd of binary weight s+1.
Let K be the algebraic closure of F2. Put

    W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X),
    f=X^n+Y^n+Z^n+W^n, phi=f/R, N=deg(phi)=ell*q-2.

**CG1 (actual geometry).** phi is reduced and its COMPLETE projective
singularity set consists of P=(1:1:1) of ordinary multiplicityq-2,
3(ell-1) diagonal points of ordinary multiplicityq, and
(ell-1)(ell-3) off-diagonal points of ordinary multiplicityq+1.
Every factor U of degreee and multiplicitym at P satisfies the exact
diagonal sum identity sum r_j=3(e-m).

**CG2 (two inequalities for ANY proper factor).** If phi=UH with
0<e=deg(U)<=N/2, define m=mP(U), t=e-m, V=sum of its off-diagonal
multiplicities and the INTEGER

    D=(ell-3)e+2m-V=(ell-1)e-2t-V.

Then D>=1 and

    e^2-N*e+(Aell/4)(q+1)^2 >= 0,                 (I)
    D[q+1-(2ell/Aell)e] <= (ell-1)Aell/4.         (II)

The first follows from ordinary Bezout and two global square completions.
The second uses the classical multiplicity bound on each absolute
component, retaining the reduced correction for a product.

**CG3 (whole irreducibility at an explicit threshold).** If

    q>=max(2ell+7,Lell),                           (III)

then phi is ABSOLUTELY IRREDUCIBLE. In particular this holds for

    EVERY s>=3 and EVERY k>=4,
    n=(2^s-1)*2^(sk)+1.                           (IV)

Consequently those exponents do not admit the two positive-degree
coefficientwise F2 factors asked for in B4(b). This is a restricted
family exclusion, not the full annual classification. No statement
for every k1/k2/k3, or other odd parts, follows. The separately accepted
special FS theorem is stronger at s3: it covers k>=2 by extra F8
orbit information. That accepted theorem is preserved, not weakened.

Exact accepted T1 supplies absence of ABSOLUTE lines for every odd n
of binary weight at least3. Its operative proof was reread and its
authority bound. Accepted FP/FS give the specialQ8 prototype and the
reduced-curve warning; all general geometry and both inequalities are
reconstructed here. The previous live research/Frobenius notes are
constructive history, not accepted premises. No other agent contributed
a new inference in this packet. Prior reviewer preparation or accepted
input authorship is not new constructive contribution to CG1–CG3.

Classical singularity/Bezout methods, the irreducible multiplicity bound
and the qualitative APN literature are attributed. Hernando–McGuire
provides an F2-defined absolute COMPONENT in this divisor regime, not
the whole-polynomial assertion merely from that theorem. The unread
Férard2017 sequel remains a priority lead. Novelty is UNESTABLISHED.

## 1. Reducedness and the complete projective list

The numerator is nonzero: its X^(n-1)Y coefficient is1 because n is
odd. Its derivatives satisfy

    f_X=(X^ell+W^ell)^q, f_Y=(Y^ell+W^ell)^q.

All roots of Z^ell-1 are exactly F_Q*, simple because ell is odd.
The linear factors of the two derivative bases have coefficient
vectors (1+zeta,zeta,zeta) and (eta,1+eta,eta), respectively, with
zeta,eta in F_Q*. They cannot be proportional: the Z and X entries
would give simultaneously zeta=c*eta and1+zeta=c*eta. Thus f_X and
f_Y are coprime. A repeated irreducible factor of f would divide
both, so f and phi are reduced. Every factor of homogeneous phi is
homogeneous by additivity of least/greatest degrees in a polynomial
domain. The accepted T1 excludes every absolute line factor of phi.

A singular projective point of phi has f=f_X=f_Y=f_Z=0 because
f=R*phi. Choose any nonzero coordinate as Z and normalize it to1;
permutation symmetry permits this even if the original Z is zero.
Write alpha=X, beta=Y, lambda=alpha+beta+1. The derivative equations
give alpha^ell=beta^ell=lambda^ell=u. In this chart f=u^q+1,
since alpha+beta+lambda=1. Thus u^q=1 and u=1. Hence

    alpha,beta,lambda in F_Q*.

In particular all four coordinates X,Y,Z,W are nonzero. Conversely
the local calculations in Section2 prove that EVERY projective F_Q
point with these four coordinates nonzero is an ordinary singularity.
This supplies the complete list, with no affine-infinity omission.

There are Q²+Q+1 projective F_Q points. The four lines X0,Y0,Z0,W0
have Q+1 points each, six distinct pairwise intersections and no
triple intersection. Their union has4Q-2 points. The complement has

    Q²-3Q+3 = ell²-ell+1

points. Each of the three prescribed diagonals has Q+1 points, exactly
two on that four-line union, leaving Q-1=ell relevant points. These
three lines meet only at P, so their non-P points number3(ell-1).
The other (ell²-ell+1)-1-3(ell-1)=(ell-1)(ell-3) points are off all
three diagonals. All counts are exact incidence identities.

## 2. Ordinary cones at every listed point

At P set X=1+x,Y=1+y,Z1. Since ell is odd,
(1+t)^n=(1+t)(1+t^q)^ell has its first relevant terms
1,t,t^q,t^(q+1), with later degrees at least2q. The first surviving
four-term numerator is x^q*y+x*y^q. Dividing by xy(x+y) gives cone

    C_P=(x^(q-1)+y^(q-1))/(x+y)
       =product_(b in F_q minus F2)(x+b*y).

It is squarefree of degreeq-2 and none of the three prescribed
diagonals is tangent. Thus P is ordinary of the asserted multiplicity.

At a non-P diagonal point, permute to(b:1:1), where b in F_Q*
and b!=1. Put c=b+1,E=b^-1 and translate X=b+x,Y=1+y. Since
q fixes b and b^ell=1, the degree-q numerator vanishes. Its first
piece, of degreeq+1, is

    y[E*x^q+E*x*y^(q-1)+(1+E)*y^q].

The denominator starts c²*y. The quotient's cone is consequently

    (E/c²)[x^q+x*y^(q-1)+c*y^q].

It is nonzero and squarefree: at y1 the polynomial x^q+x+c has
derivative1, while y0 is not a cone factor. The point is ordinary
of multiplicityq and its prescribed diagonal is not tangent.

At an off-diagonal point(alpha,beta,1), the denominator is a unit.
Let lambda=alpha+beta+1; all three values are nonzero in F_Q and
fixed by q. The degree-q numerator vanishes, and its degreeq+1
piece is

    a*x^(q+1)+b*y^(q+1)+d*(x^q*y+x*y^q),
    a=alpha^-1+lambda^-1,
    b=beta^-1+lambda^-1, d=lambda^-1.

The two derivatives are a*x^q+d*y^q and d*x^q+b*y^q. Their
coefficient determinant is

    a*b+d²=1/(alpha*beta*lambda)!=0,

using (lambda+alpha)(lambda+beta)+alpha*beta=lambda. Hence no
nonzero projective point zeros both derivatives and the cone hasq+1
distinct lines over K. It is ordinary of multiplicityq+1. This also
proves the converse asserted in Section1. No transitivity of these
points under S4 or coefficient Frobenius is assumed.

## 3. Exact contacts and projective Bezout

Consider ANY phi=U*H with e=degU>0 and degH=N-e>0. Its factors
are coprime because phi is reduced. At a listed ordinary point the
two initial cones partition its distinct tangent lines. Their local
intersection multiplicity is exactly the product of their multiplicities.
Every intersection of U,H is singular on phi, so Section1 is a
COMPLETE Bezout list.

Write m=mP(U), r_j for its3(ell-1) diagonal multiplicities, and v_j
for its o=(ell-1)(ell-3) off-diagonal multiplicities. Put

    t=e-m, S=sum r_j, V=sum v_j, o=(ell-1)(ell-3).

These are ordinary nonnegative integers. Restriction to Y=Z gives
the exact nonzero degree-N identity

    phi(X,Y,Y)=(X^(ell*q)+Y^(ell*q))/(X+Y)^2.

Its zeros are P with contactq-2 and the other ell-1 roots in F_Q*
with contactq. At(1:0:0) it is nonzero. No such diagonal is tangent
at a zero by Section2; the contact of U at each is its multiplicity.
Bezout with this line therefore gives e=m+sum_on_line r_j. Adding
the three identities, whose only shared point is P, yields

    S=3t.                                        (1)

There is no premise m>0. Global Bezout is exactly

    e(N-e)=m(q-2-m)+sum r_j(q-r_j)
                             +sum v_j(q+1-v_j).  (2)

No real inequality has yet been used in(1)–(2).

## 4. First global square completion: the factor-degree constraint

Cauchy gives sum r_j²>=S²/[3(ell-1)]=3t²/(ell-1) and
sum v_j²>=V²/o. Here ell>=7 ensures both counts are positive.
The off-diagonal real quadratic has the global bound

    (q+1)V-V²/o <= o(q+1)²/4.

Substitute m=e-t in(2). Subtract its left side from this upper bound
to obtain

    0<=-(ell-1)qe+2(e+q+1)t
                     -[(ell+2)/(ell-1)]t²+o(q+1)²/4.

The global real maximum of the t-quadratic is
(ell-1)(e+q+1)²/(ell+2). Therefore

    0<=(ell-1)/(ell+2)
             *[e²-(ell*q-2)e+(Aell/4)(q+1)²].     (3)

Since the prefactor is positive, this is(I). Neither V nor t was
assigned a feasible/integer maximizing value; a global real upper
bound is valid for every actual factor. No degree grouping, unique
large component or equal-degree splitting is needed.

## 5. Reduced multiplicity bound and positivity of an integer

For an ABSOLUTE IRREDUCIBLE plane curve of degreed>=2, the classical
singularity bound is

    sum_P binom(mP,2) <= (d-1)(d-2)/2.            (4)

Its characteristic-two applicability is checked by the following
standard adjoint argument, also the operative Fulton proof. Some
directional derivative is nonzero, since a polynomial with all
partials zero over perfect K would be a square. Derivative Bezout
first gives delta=sum binom(mP,2)<=d(d-1)/2. Degree(d-1) forms
have dimension M=d(d+1)/2. Vanishing to ordermP-1 at each singular
point imposes at mostdelta linear conditions. Add M-delta-1>=0
distinct smooth points. A nonzero form of degreed-1 meeting all
conditions exists and has no common component with the irreducible
curve. Bezout gives d(d-1)>=2delta+(M-delta-1), which is(4).
This is classical geometry, not a new genus theorem or a p>2 argument.

For U REDUCED, write its distinct absolute factors U_i of degreesd_i.
There are c of them, eachd_i>=2 by accepted T1, so c<=e/2. Apply(4)
to each U_i, and sum pairwise Bezout for the cross multiplicities.
At every point mP(U)=sum_i mP(U_i), so

    sum_P binom(mP(U),2)
      <=sum_i (d_i-1)(d_i-2)/2+sum_(i<j)d_i*d_j
      =(e-1)(e-2)/2+c-1
      <=e(e-2)/2.                                (5)

Keeping c-1 is essential; the irreducible formula cannot be applied
directly to U. In particular for the listed singularities(5) gives

    m(m-1)+sum r_j(r_j-1)+sum v_j(v_j-1)<=e²-2e.  (6)

Define the integerD=(ell-3)e+2m-V=(ell-1)e-2t-V. Rearranging exact
equation(2) yields

    qD=2e+e²-2m-m²-sum r_j²+V-sum v_j².          (7)

Equation(6), with sum r_j=3t, makes its right side at least
4e-3m-3t=e>0. Consequently qD>=e>0, so D is a POSITIVE INTEGER:

    D>=1.                                       (8)

This uses no F2-definition of U and no extra orbit divisibility.

## 6. Second global square completion

Use the two Cauchy bounds again in(7) and eliminate
V=(ell-1)e-2t-D. The result is

    qD<=(ell-1)e-D+2et-[(ell+2)/(ell-1)]t²
                            -[((ell-1)e-2t-D)²/o].

The t² coefficient is -Aell/o. Completion of the square over ALL
real t gives

    qD<=(ell-1)e-D
       -[(ell-1)e²-2ell*eD+((ell+2)/(ell-1))D²]/Aell.

Equivalently,

    D[q+1-(2ell/Aell)e]
      <=(ell-1)e-(ell-1)e²/Aell
                           -[(ell+2)/((ell-1)Aell)]D²
      <=(ell-1)Aell/4.                            (9)

The last upper bound completes the e square at Aell/2 and drops a
nonpositive D² term. This proves(II) for every actual proper factor.
Its usefulness requires a positive bracket; Section7 supplies that
from(I), rather than assuming it or asserting all components pass P.

## 7. An actual small-factor bound and the contradiction

Suppose(III) and that phi is reducible over K. Choose any nonempty
proper set of its absolute factors with 0<e<=N/2; for example one
of smallest degree. Put e0=(ell-2)q/2. It satisfies e0<N/2 because
N/2-e0=q-1>0. Let P(e)=e²-N*e+(Aell/4)(q+1)². Direct substitution
gives

    P(e0)=(ell-2)/4
                    *[-q²+2(ell+3)q+(ell+1)].    (10)

For q>=2ell+7 the bracket is negative: at2ell+7 it is -ell-6,
and its derivative -2q+2(ell+3) is negative thereafter. P is
decreasing on e<=N/2. Hence P(e)<0 throughout[e0,N/2], contrary
to(I). It follows that every such chosen factor must satisfy

    e<e0=(ell-2)q/2.                              (11)

Thus the bracket in(II) has the STRICT lower bound

    q+1-(2ell/Aell)e > q/(ell+1)+1 >0.

By D>=1 its left side is strictly greater than q/(ell+1)+1.
But q>=Lell gives

    q/(ell+1)+1
       >=(ell-1)(ell-2)(ell+1)/4+1
       >(ell-1)Aell/4,

contradicting(II). Therefore phi has no such factor and is absolutely
irreducible. Equalities at the threshold cannot evade the strict +1.

Finally q=Q^k with Q>=8 and k>=4 satisfies q>=Q^4, whereas

    Lell=(Q-2)(Q-3)Q²/4 <Q^4/4,
    2ell+7=2Q+5<Q²<=q.

This proves the displayed infinite family(IV) as a candidate theorem,
not a finite pattern extrapolation. No source APN component theorem
has been promoted to whole absolute irreducibility in the deduction.

## 8. Boundaries, source limits and what remains open

The q=Q/k1 branch gives a Kasami-type degree and is OUTSIDE the
threshold theorem. Nothing proves every smaller k reducible or
irreducible. In particular the separately accepted s3/k2 result
uses stronger special orbit information, and its q8/n57 exclusion
is unchanged. For s>=4 the cases k2/k3 and many other exponents
remain unresolved here. Every factor and every local point in this
proof is over K; no assumption of a small F2 cofactor was hidden.

The earlier conditional note is now supplied with actual singularity/
contact inputs for this exact family, and its missing degree bound
is supplied by(3),(10)–(11). Its formulas are independently derived
again, not made true by calling the note accepted. The Frobenius
identity delta_q(f)=0 is a separate unverified lead. The recent
Gauss-map theorem has additional separability/strict exponent
hypotheses and is NOT a premise. No inference here requires a
characteristic-zero foliation bound or a characteristic-two duality
shortcut.

The classical curve inequality is attributed to Fulton, and the
singularity/Bezout APN method to its primary literature. The Férard2017
sequel has been identified but its operative proof is unread; neither
priority nor a claim that this theorem is absent there follows.
No mathematical executable, finite-field enumeration, factor table,
CAS, author rerun or certificate replay supplied this argument.
The complete obligations, failed routes, source limits and compact
preservation metadata accompany the eventual whole freeze. TWO OTHER
whole audits must reconstruct every step before any promotion.
