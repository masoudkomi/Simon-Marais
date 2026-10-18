# Accepted coordinator-F8-pencil-r1: exact coordinator scope

2026-10-18 UTC. **Proved, independently reviewed scoped partial result.**

Accepted FP0–FP2 ONLY for q=8^k,k>=2 (q>=64), n=7q+1,
phi=(X^n+Y^n+Z^n+(X+Y+Z)^n)/[(X+Y)(Y+Z)(Z+X)], over the
algebraic closure of F2. The official2024(b) target remains actual
coefficientwise factorization overF2, not polynomial-function equality
or splitting solely after a field extension. q8/n57 is excluded.

FP0: for ANY factorU, degreee, multiplicitym atP111, andt of the
six special F8 tangent directions, T=sum of24 off-diagonal singular
multiplicities obeys T<=6(e-m)-qt. For F2-definedU, t is0,3or6.
Constants/full factors and factors missingP are retained. The exact
six-line contact2q−2 and nonzero restrictions justify every contact
sum; tangencies at off-diagonal points give LOWER estimates only.

FP1: no absolute factor has degree in the ENTIRE band
[2q+9,5q−11], including both endpoints. The complete43-point PROJECTIVE
singularity list and ordinary cones give the exact Bezout sum. The
three diagonal contacts give S=3(e-m). Real Cauchy and GLOBAL maxima
inT andz yield the negative endpoint comparison, without assuming
an actual integral/feasible maximizer or using FP0 on a decreasing
quadratic branch. Arbitrary unequal complementary degrees are covered.

FP2: there is exactly one absolute irreducible component of degree
at least5q−10, and the sum of all others is at most2q+8. Greedy
proper grouping proves existence; degree uniqueness and normalized
COEFFICIENTWISE Frobenius give an F2-defined large component and
F2-defined cofactor. No equal-degree or transitive-factor-orbit
assumption, ordinary F2 irreducibility or whole irreducibility is used.

The smaller F2 cofactor may still be NONCONSTANT. Neither ordinary
reducibility nor irreducibility, whole absolute irreducibility, the
q8 endpoint or the annual classification follows. Published qualitative
absolute-F2-component existence in this family is already covered by
Hernando–McGuire Theorem16 (proper7 dividesq−1), and is attributed.
Their Theorem15's irreducibility hypothesis is not dropped. Quantitative
priority is unestablished. The unused2026 highest-form criterion is
not imported; its default-chart hypothesis was not supplied.

Root is sole NEW constructor and EXCLUDED from the two independent
audits. OTHER A R1 and C R2 each completed fresh initially blind
ENTIRE WHOLE36/36 audits. Both COMPLETE reports, ALL36+36 ledger
rows, source/log/code and ALL metadata froze before ANY NEW
corresponding peer finding/file/hash. Root has now read and reconciled
the ENTIRE constructor and BOTH complete audit packets, including
all local/projective/line/quadratic/grouping/Frobenius inferences,
source hypotheses, all five A closed notes and C's closed challenges.
Zero substantive issues or author repairs remain. A's ledger is
the combined issues-v1.md file, not a separately named ledger;
an initial missing-name lookup supplied no absent content. A later
combined constructor display clipped the freezer opening, which
was reissued completely before acceptance. No unread output is
counted as a full read. Older authorship/review roles are disclosed
and do not independently self-recertify accepted inputs.

All new mathematics is hand derivation. No mathematical program,
finite-field enumeration, CAS, factor table, author rerun or old
certificate replay supplied a step. Administrative direct fingerprint/
JSON/suffix/label checks do not prove mathematics. Exact primary
read limits remain preserved; no full external-proof audit, external
validation, new annual solution or novelty is claimed.

The COMPLETE frozen mathematical submission follows as a byte-identical suffix. Its historical unverified label records submission status; this header and acceptance record state the current exact scope.

---

# Diagonal contacts, six F8 lines and a dominant four-bit component

2026-10-18 UTC. **Candidate proof - unverified.** Sole NEW constructor
`/root`. Requested inherited gpt-6.1-sol/max; verified effective readback
unavailable. TWO OTHER initially blind ENTIRE WHOLE audits are required.
No annual classification, ordinary irreducibility or novelty is claimed.
Only the official coefficientwise2024 B4(b) factorization is investigated.

For q=8^k, k>=2, set n=7q+1 and work over the algebraic closure K of F2.
Write W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X),

    phi=(X^n+Y^n+Z^n+W^n)/R, N=deg(phi)=7q-2.

These exponents have four binary ones. They belong to the 3|a branch
of n=7*2^a+1 that the accepted neighbor-Frobenius criterion leaves open.
The proposed quantitative results are:

**FP0.** For ANY factor U, put e=deg U, m=m_P(U), and let t count the
six F8 pencil directions at P that belong to U's tangent cone. The sum
T of its24 off-diagonal singular multiplicities satisfies

    T <= 6(e-m)-q*t.

This bound is additional geometric information. The following degree
gap already follows from exact diagonal contacts and ordinary Bezout;
it does not need the extra pencil bound.

**FP1.** No homogeneous factor of phi over K has degree in the interval

    2q+9 <= e <= 5q-11.                              (1)

**FP2.** There is exactly one absolute irreducible component G of degree
at least5q-10. Normalize one nonzero coefficient of G to1. Then G is
defined over F2. All its other components together have total degree
at most2q+8. The remaining cofactor may be constant or nonconstant;
that distinction, hence the official reducibility question, is UNRESOLVED.

The existence of some absolute F2 component in this family is already
published context: Hernando–McGuire Theorem16 applies because7 is a
proper divisor of q-1. We do not claim that qualitative conclusion as
new. The present complete argument proposes the displayed quantitative
degree gap together with the six-line constraint. Priority is unestablished.
The q8/n57 endpoint is explicitly excluded from FP1–FP2; no claim about
its factorization is imported or reconstructed in this proof.

## 1. Squarefreeness and the entire projective singularity set

This section reconstructs the relevant local algebra, rather than
applying the accepted neighbor theorem outside its hypotheses. Formal
differentiation of the numerator f gives

    f_X=(X^7+W^7)^q, f_Y=(Y^7+W^7)^q.

The linear factors of the first seventh-power difference have coefficient
vectors(1+zeta,zeta,zeta), and those of the second have
(eta,1+eta,eta), where zeta,eta range over F8*. They cannot be
proportional: their Z and X entries would give both zeta=c*eta and
1+zeta=c*eta. Thus f_X and f_Y are coprime. Any repeated irreducible
factor of f would divide both derivatives, so f and its quotient phi
are squarefree. The numerator is nonzero, for example its X^(n-1)Y
coefficient is1. All factors of the homogeneous phi are homogeneous:
least and greatest degree add, so a product with degree spread zero
has factors with degree spread zero.

If a projective point is singular on phi, the identity f=R*phi implies
f=f_X=f_Y=0 in any affine chart, including where R vanishes. Normalize
a nonzero coordinate to Z1, using permutation symmetry. With
alpha=X,beta=Y,lambda=alpha+beta+1, the derivative equations imply

    alpha^7=beta^7=lambda^7=u.

The value of f is u^q+1, because alpha+beta+lambda=1. Hence u=1.
Thus alpha,beta,lambda all belong to F8*. This also shows no coordinate
can be zero: if any coordinate were zero, permuting one of the nonzero
ones into Z would contradict the displayed nonzero roots. In particular
there are no additional singularities hidden at infinity of this chart.

Conversely every projective F8 point with X,Y,Z,W nonzero is singular
on phi, with the explicit multiplicities proved below. There are
73 points in P²(F8): (8³-1)/(8-1)=73. The four lines X0,Y0,Z0,W0
have nine points each, six distinct pairwise intersections, and no
triple intersection. Their union has36-6=30 points. The remaining43
are exactly the singularities. They consist of

    P=(1:1:1); 18 nontrivial prescribed-diagonal points;
    24 points off all three prescribed diagonals.     (2)

Indeed each of the three lines X=Y,Y=Z,Z=X has nine F8 points, of
which two have X*Y*Z*W=0. Its other seven consist of P and six more
points. The three lines have only P in common. This gives1+18 points,
leaving24. The complete projective list is important to Bezout below.

## 2. Every singularity is ordinary, with exact multiplicity

At P set X=1+x,Y=1+y,Z1. The denominator is xy(x+y), and
(1+t)^n=(1+t)(1+t^q)^7. The first surviving numerator term is
x^q*y+x*y^q. The quotient's initial cone is

    C_P=(x^(q-1)+y^(q-1))/(x+y)
       = product_(b in F_q minus F2)(x+b*y).          (3)

It has q-2 distinct lines; none is x0,y0,x+y0. Thus P is ordinary of
multiplicity q-2 and no prescribed diagonal is tangent there.

At a nontrivial diagonal point, by symmetry take(b:1:1), b in F8*,
b!=1. Let c=b+1, E=b^-1, and translate X=b+x,Y=1+y. Since q fixes F8,
the degree-q numerator piece vanishes; its degree-(q+1) piece is

    y*[E*x^q+E*x*y^(q-1)+(1+E)*y^q].

The denominator starts c²*y. Therefore phi has multiplicity q and cone

    (E/c²)*[x^q+x*y^(q-1)+c*y^q].                   (4)

This cone is squarefree: after y1 the polynomial x^q+x+c has
derivative1, and y0 is not a cone factor. Thus all q tangent lines
are distinct, and the prescribed diagonal y0 is not tangent.

At an off-diagonal point(alpha,beta), lambda=alpha+beta+1, the
denominator R is a unit. Since all three nonzero coordinates are fixed
by q-Frobenius, the degree-q numerator piece again vanishes. The
degree-(q+1) piece is

    H=(alpha^-1+lambda^-1)*x^(q+1)
       +(beta^-1+lambda^-1)*y^(q+1)
       +lambda^-1*(x^q*y+x*y^q).                    (5)

Its partial derivatives are a*x^q+d*y^q and d*x^q+b*y^q, with
a=alpha^-1+lambda^-1,b=beta^-1+lambda^-1,d=lambda^-1. Their coefficient
determinant is

    a*b+d²=1/(alpha*beta*lambda) !=0.

Indeed (lambda+alpha)(lambda+beta)+alpha*beta=lambda. There is no
nonzero projective common root of the two derivatives, so H has q+1
distinct linear factors and is nonzero. Every such point is ordinary
of multiplicity q+1. This proves the converse and all of(2).

In ANY factorization phi=U*V, squarefreeness gives coprime U,V. At each
of the43 ordinary points their initial cones partition the distinct
lines of phi, hence are disjoint. Classical local intersection therefore
equals the product of their multiplicities, even if one is zero.
Any projective intersection of U,V is singular on phi, so there are no
other terms in their projective Bezout sum.

## 3. Exact contacts on the prescribed diagonals

Set e=deg U, m=m_P(U). Write u_i for its multiplicities at the18
nontrivial diagonal points, and v_j for those at the24 off-diagonal
points. Each u_i lies in[0,q], each v_j in[0,q+1], and m in[0,q-2].
Let S=sum_i u_i and T=sum_j v_j; these are ordinary integers.

On Y=Z, exact division or the derivative of f transverse to that line
gives the homogeneous restriction

    phi(X,Y,Y)=(X^(7q)+Y^(7q))/(X+Y)².              (6)

It is nonzero, of degree N. At infinity(1:0:0) it is nonzero. Its zeros
are P of contact q-2 and the six nontrivial seventh roots of contact q.
Since that diagonal is not tangent at ANY of those points, the contact
of U there is exactly its multiplicity, as checked in(3)–(4). Every
zero of U on this line is a zero of phi and is on this list. Hence

    e=m+sum_(six points on that line) u_i.

Symmetry gives the same identity on the other two diagonals. They
share only P, so adding gives

    S=3(e-m).                                      (7)

No assertion that U passes P is made; m0 is included throughout.

## 4. Six F8 pencil lines give an additional multiplicity constraint

There are nine F8 lines through P; remove the three prescribed diagonals,
leaving six lines. Each of the24 off-diagonal singularities belongs to
exactly one of those six lines, since the line joining it to P is
defined over F8 and is not a prescribed diagonal. Thus those six lines
partition the off-diagonal list. No distribution count per line is
needed by the bound.

We must prove none of the six lines is a component of phi. In the Z1
chart a line has local parameter x=t,y=b*t with b in F8 minus F2:
the omitted slopes0,1,infinity are exactly the prescribed diagonals.
In f along the line, a term of degree h has coefficient
1+b^h+(1+b)^h. The nonconstant supported degrees of(1+t)^n are jq
and jq+1, j=0,...,7. Since b^q=b, the degree-q, q+1 and2q terms
all vanish, while the degree-(2q+1) coefficient is

    1+b³+(1+b)³=b*(1+b) !=0.

There are no intervening supported degrees. Dividing by
R=b*(1+b)*t³ proves that phi restricted to that line has exact initial
degree2q-2 and coefficient1. In particular the restriction is not zero.
No line is a component of phi or U.

Bezout of U with each such line is therefore e. If its direction does
not belong to U's cone at P, its contact there is exactly m. If it
does belong to U's cone, it does not belong to V's, whose contact is
then q-2-m. Additivity and the exact total contact2q-2 above give U's
contact m+q. This also covers m0 and U or V missing P. Thus its contact
is m+q*epsilon_L, with epsilon_L either0 or1.

At every off-diagonal singularity the line contact is at least the
corresponding v_j, including when it is tangent there. All other
intersection contributions are nonnegative. Summing the six line bounds
and writing t=sum epsilon_L proves FP0:

    T <= 6(e-m)-q*t <= 6(e-m).                     (8)

At off-diagonal points this uses LOWER contact bounds, not equality
for a tangent line. At P it uses the proved exact total contact and
the disjoint ordinary cone. If U is defined over F2, t is0,3 or6:
the six directions F8 minus F2 form two squaring orbits of length3,
and its cone subset is invariant. No such restriction is imposed on
an arbitrary factor over K.

## 5. The quantitative Bezout inequality and its uniform optimization

Let z=e-m>=0. From the ordinary points and classical projective Bezout,

    e(N-e)=m(q-2-m)+sum_i u_i(q-u_i)
                         +sum_j v_j(q+1-v_j).

Cauchy on the18 and24 entries, with (7), gives the real inequality

    e(N-e) <= m(q-2-m)+3q*z-z²/2
                            +(q+1)*T-T²/24.        (9)

Here all degrees/multiplicities are ordinary integer numbers; these
real-valued inequalities are not identities in characteristic2.
The quadratic f(T)=(q+1)T-T²/24 has GLOBAL maximum6(q+1)², attained
at T=12(q+1). This bound works for all actual T; the stronger FP0
constraint is not needed in FP1. No substitution of an upper bound
for T on the decreasing side of this quadratic is made.

Assume for contradiction

    2q+9 <= e <= N/2=(7q-2)/2.                     (10)

Use the GLOBAL bound f(T)<=6(q+1)² and substitute m=e-z. The difference
of the resulting upper bound in(9) and e(N-e) becomes

    -3z²/2+(2e+2q+2)z-6qe+6(q+1)²
    <= (2/3)*[e²-(7q-2)e+10(q+1)²].              (11)

This is completion of the square over ALL real z, so no unproved
integral maximizing choice or endpoint feasibility is used. The
numerator is convex in e and its two endpoint values on(10) are

    -3q+109,
    -9q²/4+27q+9.

Both are strictly negative at every q>=64. A convex function is bounded
above on this interval by the maximum of its two endpoint values.
Consequently the final upper bound in(11) is strictly negative,
contradicting(9). Thus no factor with degree(10) exists.

For any factor degree between the endpoints in(1), choose U or its
complement so that e<=N/2. The smaller degree remains at least2q+9,
because N-(5q-11)=2q+9. The preceding contradiction proves FP1.

## 6. Greedy grouping and Frobenius descent of the dominant component

Factor phi into its distinct absolute irreducible components. If every
degree were at most2q+8, add components until their sum e first exceeds
2q+8. Its new value is an integer satisfying

    2q+9 <= e <= 4q+16 <= 5q-11,

where the last inequality uses q>=64 (q>=27 would suffice there).
The sum is smaller than N, so this is a proper factor forbidden by
FP1. Therefore some absolute component has degree at least2q+9.
FP1 forces its degree to be at least5q-10, unless it is the entire
polynomial, which already satisfies that same bound. Two components
of degree5q-10 cannot fit in N, since 2(5q-10)>7q-2 for q>=64.
The dominant absolute component is unique, and all other degrees sum
to at most N-(5q-10)=2q+8.

Normalize G by setting the coefficient of its leading monomial in a
fixed monomial ordering to1. Coefficientwise squaring permutes the
normalized absolute factors of phi and preserves their degrees.
Uniqueness of the dominant one fixes G under squaring, so every
coefficient satisfies a²=a. Hence all coefficients lie in F2.
The remaining cofactor is in F2 too, by division or uniqueness of its
product of other normalized factors. This proves FP2 without assuming
ordinary F2 irreducibility, an equal-degree splitting, or a transitive
Frobenius orbit of all components.

## 7. Exact unresolved inference

The argument permits a single dominant F2 component multiplied by a
smaller nonconstant F2 cofactor of degree at most2q+8. It does not show
that the latter is a unit. It therefore does not decide whether n=7q+1
qualifies in the official part(b), and is not whole absolute
irreducibility. Only FP0's six-line constraint, the degree gap and
dominant-component statement are proposed for review. At q8 the endpoint inequalities are not
negative; that endpoint is excluded rather than forced through them.

The classical singularity/Bezout method is attributed, and the already
published qualitative absolute-component result is not reinvented as
new progress. No mathematical code, CAS, finite-field scan, factor table,
author rerun, experiment or numerical extrapolation supplied this proof.
All expansions, incidence counts and optimization identities are hand
derivations. Full source/read limits, failed routes, ALL obligations and
compact byte metadata accompany the candidate. Root is excluded from
the TWO OTHER whole-auditor count. Only reconciliation after both entire
initials may promote any exact scoped partial.
