# Neighbor-Frobenius NF1–NF3: entire initially blind whole R1

18 October 2026 UTC. Independent reviewer A,
`/root/review_2021_reasoning_j15_r2`. This is the COMPLETE initial whole
audit, not a promotion. The submitted result remains **candidate proof -
unverified** until the coordinator reconciles TWO OTHER whole audits.
Requested inherited gpt-6.1-sol/max; an independent effective-setting
readback is unavailable.

Target: `problems/2024-B4/notes/coordinator-neighbor-Frobenius-r1-candidate-v1.md`,
13799 bytes, SHA256
`775501d763a46b8411a6509c7da06d3a7fc3dacb3b27141881b80de2ea37f9d4`.
Constructor freeze: 2492 bytes, SHA256
`f97a4dc9eb21dea3e4e4e94d42ba7f3bdf09ddf3555e2defcab19c4ec5812671`.
I read the complete seven-record constructor packet, including all 36
obligations, source record, failed approaches, administrative script
SOURCE ONLY and input metadata. I reconstructed the entire proof by
hand. No mathematical program, CAS, finite-field scan, author-script
rerun, factor table or old certificate supplies this review.

No NEW B NF report, finding, ledger, source record or metadata has been
opened or hashed before this entire initial freeze. Root is the sole
NEW constructor and is excluded from the independent-review count.

## Outcome and exact role boundary

I find **no substantive defect, required repair or unresolved issue** in
NF1–NF3 within their stated hypotheses. I recommend acceptance of these
scoped partial claims after the second OTHER whole audit and coordinator
reconciliation. This report does not itself accept the result.

I previously constructed accepted T1–T4 and the old C7/C11 arguments and
reviewed CP/GK, later jet/Hermitian and S3 packets. These are disclosed
older roles, not independent recertification of my own work. I did not
construct or supply an inference for the NEW neighbor-Frobenius argument.
In particular its new two-branch algebra and global degree-sum
contradiction were not supplied by me. Its final proof does not need T1,
S3 or the accepted three-bit theorem as mathematical premises. I checked
their exact accepted scopes as context and did not replace a new
inference by those old results. My immediately preceding frozen 2017 R6
review is bound only for preservation; its mathematics is unrelated.

The theorem is a sufficient exclusion criterion for the actual ordinary
F2 factorization problem. It is not a classification of all exponents,
all binary-weight-four exponents, or the annual open problem. There is
no literature-priority determination. McGuire's original Theorem 8
already includes a displayed special family and n=29.

## 1. Official polynomial domain and arithmetic hypotheses

The actual official (b) asks for a coefficientwise integer congruence
`f_n = R g h (mod 2)` with neither g nor h constant modulo 2, where n is
an odd positive integer. Reducing coefficients gives a polynomial
identity in F2[X,Y,Z]. The allowed g,h are nonzero and have positive
degrees; zero is itself constant modulo 2. Conversely F2 factors have
integer lifts by selecting coefficients 0 or 1. Cancelling the nonzero
polynomial R in this domain makes the target exactly two positive-degree
F2 factors of the established quotient phi_n. Thus absolute
irreducibility of the WHOLE quotient is sufficient to exclude n. A
single absolutely irreducible component would be insufficient.

Here q=2^a, a>=2, ell>=3 is odd, and n=q ell+1. In particular n>=13 is
odd and N=deg(phi_n)=q ell-2>0. No n=1 or n=3 convention enters the
argument; ell=1 and a=1 are outside the submitted theorem. The first
arithmetic branch ell|(q-2) is equivalent to ell|(2^(a-1)-1) because
2 is invertible modulo odd ell. The second branch ell|(2q-1) is already
ell|(2^(a+1)-1). All proper and composite odd divisors are included.

In the first branch a common divisor of ell and q-1 would divide the
consecutive integers q-2 and q-1. In the second it would divide
(2q-1)-2(q-1)=1. Hence gcd(ell,q-1)=1 in either branch. The only common
ell-th root and Fq-unit is therefore 1. The first branch has no ell>=3
when q=4, which causes no missing endpoint; the second includes ell=7.

The numerator is nonzero because its mixed coefficient X^(n-1)Y is
n modulo 2, hence 1. The normalized quotient is the established one;
no preliminary family is researched or reconstructed in this audit.

## 2. The local lemma and the global repeated-component issue

Suppose a local nonzero series H has first homogeneous piece c L^m,
and its next piece is not divisible by L. If H=AB with orders s,t>0,
then s+t=m. Unique factorization of the initial forms in K[x,y]
forces A_s and B_t to be scalar multiples of L^s and L^t. The piece of
degree m+1 is A_s B_(t+1)+A_(s+1)B_t. Both summands are divisible by L.
This is a contradiction. The conclusion about a unit cofactor is
preserved by multiplication by units and invertible coordinate changes.
This is an actual factorization argument; total multiplicity alone is
not being used to prove it.

Global squarefreeness is checked separately. With W=X+Y+Z,

    f_X=(X^ell+W^ell)^q,  f_Y=(Y^ell+W^ell)^q.

Since ell is odd, the forms before taking q-th powers split into
distinct linear factors X+zeta W and Y+eta W for ell-th roots of unity.
Their coefficient triples are (1+zeta,zeta,zeta) and
(eta,1+eta,eta). Proportionality with scalar c would give, from Z and X,
zeta=c eta and 1+zeta=c eta simultaneously. This is impossible, including
zeta=1 or eta=1. Thus the two partial derivatives are coprime in
K[X,Y,Z], also after their q-th powers. If an irreducible h appeared at
least twice in f, it would divide both partial derivatives. This remains
true when differentiation of the repeated power is zero in
characteristic 2. Consequently f, and its divisor phi, are squarefree.

A homogeneous product over a graded polynomial domain has homogeneous
factors: least and greatest occurring degrees add, so zero spread in
the product forces zero spread in each factor. Therefore any absolute
reducibility gives coprime positive-degree homogeneous U,V with phi=UV.
The proof is not restricted to an equal-degree split, a particular
coefficient field, or components passing a chosen point.

## 3. Every projective shared point is covered

Work first in Z=1. A singular point (alpha,beta) of phi gives
f=f_X=f_Y=0 in f=R phi, even when R=0. Let lambda=alpha+beta+1. By
injectivity of q-th powers, the derivative equalities give

    alpha^ell=beta^ell=lambda^ell=u.

Since n=q ell+1, the numerator at this point is
(alpha+beta+lambda)u^q+1=u^q+1. Hence u=1. All three quantities
alpha,beta,lambda are nonzero ell-th roots. In particular none of the
later inversions is made at a retained zero coordinate or zero lambda.

The list is P=(1,1), the nontrivial three diagonals, and the points with
alpha!=1, beta!=1, alpha!=beta. A diagonal point different from P is a
permutation of (b:1:1), b^ell=1, b!=1; an X=Y representative is normalized
using b^-1, which is defined and still an ell-th root.

This covers the whole projective plane, rather than assuming away
infinity. If a projective singularity had any zero coordinate, permute
a nonzero coordinate into Z and scale it to 1. The polynomial and R are
symmetric, so the same calculation would force the remaining two
coordinates to be nonzero, a contradiction. In particular no point of
the original Z=0 line is singular. Every common zero of U,V is singular
on UV, including all homogeneous partials, so all common projective
zeros lie on the above list. The proof requires only this necessary
list and does not need to count or assume absence of off-diagonal
points.

## 4. P and every nontrivial diagonal

At P use X=1+x,Y=1+y,Z=1. The exact denominator is xy(x+y). For
n=q ell+1 with ell odd,

    (1+t)^n=1+t+t^q+t^(q+1)+terms of degree at least 2q.

Constants, degree one and degree q cancel in the four-term numerator;
the first nonzero piece is x^q y+x y^q. Division by xy(x+y) gives order
q-2 and initial cone

    C=(x^(q-1)+y^(q-1))/(x+y)
      = product_(b in Fq minus F2)(x+b y).

The q-2 directions are distinct: x^(q-1)+y^(q-1) has the q-1 distinct
nonzero Fq slopes and dividing by x+y removes only slope 1. No x or y
factor was lost. Hence initial cones of U,V at P partition distinct
lines and are coprime. The local intersection number is m m', with
m=ord_P U and m'=ord_P V. It is zero when either factor is a unit;
there is no assumption that both factors or all components pass P.

At (b:1:1), write c=b+1, E=b^-q, B=1+b^(1-q). The quantities c,E are
nonzero. If B=0 then b is a nontrivial element of Fq with b^ell=1,
contrary to the gcd condition. In coordinates X=b+x,Y=1+y,Z=1,

    R=c^2 y+c y^2+x^2 y+x y^2,
    f_q=B y^q,
    f_(q+1)=y[E x^q+E x y^(q-1)+(1+E)y^q].

The lower positive terms vanish by the same binary expansion and the
root equations; terms involving the next ell bit start at 2q>q+1.
Thus phi has order q-1, with first piece (B/c^2)y^(q-1). Comparing the
degree q+1 terms in R phi gives

    phi_q=(E/c^2)x^q+(E/c^2)x y^(q-1)
           +[(1+E)/c^2+B/c^3]y^q.

The B/c^3 term really occurs: it comes from c y^2 times the preceding
quotient piece. The coefficient of x^q is nonzero, so phi_q is not
divisible by y. The local lemma applies with m=q-1. No two factors can
both vanish here. Symmetry covers all three nontrivial diagonals; no
line-contact or multiplicity-only shortcut replaces this calculation.

## 5. Off-diagonal expansion and the first Frobenius branch

At an off-diagonal point the denominator is a local unit. The first
two positive homogeneous pieces of f are

    H_q=A x^q+B y^q,
    A=alpha^(1-q)+lambda^(1-q),
    B=beta^(1-q)+lambda^(1-q),
    H_(q+1)=(alpha^-q+lambda^-q)x^(q+1)
       +(beta^-q+lambda^-q)y^(q+1)
       +lambda^-q(x^q y+x y^q).

Indeed the coefficients of degree q and q+1 in (c+t)^(q ell+1) are
c^(1-q) and c^-q when c^ell=1. Below q the only possible positive
degree is one, whose contributions cancel. The next possible ell-bit
terms start at 2q>q+1. I checked both pure and both mixed terms of the
degree q+1 expression. Applying the lemma to f=(R U)V is legitimate:
R is a unit and hence R U and U have the same local vanishing status.

Assume ell|(q-2). All singular coordinates have q-th powers equal to
their squares. Let F=F2(alpha,beta,lambda), a finite field. Both
endomorphisms agree on its generators, so they agree on all of F,
including sums, inverses and the tangent slope constructed next.

Put u=alpha+1, v=beta+1. Off-diagonality and lambda!=0 give
alpha,beta,lambda,u,v,alpha+beta all nonzero. Directly,

    A=v/(alpha lambda), B=u/(beta lambda).

In particular both A and B are nonzero. The unique q-th root t of A/B
lies in F because its Frobenius is a field automorphism, and is also
the unique root in K. Thus t^q=t^2 and

    t^2=D=beta v/(alpha u)!=0.

The sole tangent is L=y+t x. Because its y coefficient is 1, its
projective direction is covered by x=1; no direction at x=0 is omitted.
On that line, with h=H_(q+1)(1,t),

    lambda^2 h
      =v^2/alpha^2+(u^2/beta^2)t^3+t+t^2
      =v^2/alpha^2+D+t[uv/(alpha beta)+1]
      =lambda[v/(alpha^2 u)+t/(alpha beta)].

For the last step I used uv+alpha beta=lambda. For the constant term,
v^2/alpha^2+D=v(uv+alpha beta)/(alpha^2 u); for the t coefficient the
same identity applies. Thus the entire next piece is being evaluated,
not a selected monomial. If h=0, nonzero denominators force
t=beta v/(alpha u)=D=t^2. Hence t is 0 or 1. The first is excluded by
D!=0; the second gives beta(beta+1)=alpha(alpha+1), so
(alpha+beta)^2+(alpha+beta)=0. Distinctness rules out alpha+beta=0;
alpha+beta=1 would make lambda=0. Both are impossible. Thus h!=0 and
the next piece misses L. The local lemma excludes every shared factor
zero in this branch, without a finite-field enumeration.

## 6. Second Frobenius branch: the full squared evaluation

Assume ell|(2q-1). Then alpha^(2q)=alpha and similarly for beta,lambda.
Again set u=alpha+1, v=beta+1, all the same nonzero denominators. We have
A^2=alpha+lambda=v and B^2=beta+lambda=u. Also (v^q)^2=v and
(u^q)^2=u; square injectivity gives A=v^q and B=u^q. Therefore

    H_q=(v x+u y)^q,  L=v x+u y,  t=v/u.

There is no missing scalar or assumed q^2=id. The rational expression
t obeys t^(2q)=t, because the 2q power is a Frobenius and fixes all its
generators. For h=H_(q+1)(1,t), square the ENTIRE expression above.
Using alpha^-2q=alpha^-1, beta^-2q=beta^-1,
lambda^-2q=lambda^-1 and t^(2q+2)=t^3 gives

    lambda h^2=v/alpha+(u/beta)t^3+t^2+t
      =(v/u^2)[u^2/alpha+v^2/beta+v+u]
      =v(alpha+beta)/(u^2 alpha beta).

Here u^2/alpha=alpha+alpha^-1 and v^2/beta=beta+beta^-1;
u+v=alpha+beta cancels the noninverse terms. All factors on the right
are nonzero. Equivalently h^2 is the last ratio with one additional
lambda in its denominator, matching author obligation NF-26. Thus
h!=0, so the unique tangent does not divide the next homogeneous
piece. The local lemma eliminates all shared off-diagonal zeros in the
second branch as well. The calculation remains valid for every allowed
proper or composite ell and arbitrary a>=2; it does not depend on a
particular finite field table or on the existence of a specified number
of points.

## 7. Global intersection contradiction, with every factor position allowed

By the previous sections, any coprime positive-degree homogeneous
factorization phi=UV can have common projective zeros only at P. The
complete projective argument excluded infinity, not just the displayed
affine list. Classical Bezout over the algebraically closed K applies
because U,V have no common component. Their disjoint tangent cones
at P give

    e d=m m',  e=deg U>0, d=deg V>0.

For a nonzero homogeneous polynomial of degree e, its translated
dehomogenization has order at most e at a point; it is not the zero
polynomial. Thus 0<=m<=e and 0<=m'<=d. If either multiplicity is zero,
the product equality is impossible. Otherwise (m/e)(m'/d)=1 forces
m=e and m'=d. Orders of products add in the local polynomial domain.
Hence

    q ell-2=e+d=m+m'=ord_P phi=q-2,

contrary to ell>=3. This covers arbitrary uneven degrees, factors
missing P, factors not defined over F2 and all possible groupings of
the globally distinct absolute components. Neither an old no-line
theorem nor an assumption that every component passes P is needed.
NF1 and the intermediate NF2 follow as stated.

## 8. Corollary, genuine failure branch and attribution

The order of 2 modulo 7 is 3. If a=1 modulo 3 then q=2 modulo 7 and
7|(q-2); if a=2 modulo 3 then q=4 modulo 7 and 7|(2q-1). For
a=0 modulo 3 neither test holds. Therefore the criterion excludes
n=7*2^a+1 exactly for the claimed a>=2 with 3 not dividing a. Its binary
expansion has the four distinct bits 0,a,a+1,a+2.

For 3|a, q-th powers fix F8, and at off-diagonal F8 singular points
A=B=0 in the degree-q piece. The necessary nonzero sole tangent is
absent. Nothing proved above decides this branch or n=57. This is a
failure of the premise, not an actual factorization or an integer-sign
contradiction. Exponents outside the neighbor tests and the complete
ordinary reducibility classification remain unresolved.

I freshly inspected McGuire's complete original Theorem 8 statement
and proof on printed pp.24–26 via the existing three page images.
Its displayed ell=2^(a+1)-1 family, including n=29, is contained in
the second branch; the local method and special example are attributed.
The present broader statement is not certified novel. The only general
theorem imports used here are projective Bezout and the coprime-tangent
local intersection formula, whose operative statements I checked in
Hernando–McGuire Section3.2/Corollary8. Their separate absolute-component
theorem does not imply whole irreducibility; their Theorem15 retains
its ordinary-irreducibility hypothesis. Neither was used as a premise.
The detailed source record states all current read limits.

## 9. Completeness, preservation and recommendation

All 36 author obligations have individual dispositions in the companion
ledger. There are zero substantive objections and zero open issues.
No constructor repair is proposed or performed. The preservation record
binds the exact seven target files, every direct input fingerprint, and
the immutable immediate own-parent metadata without copying unrelated
historical inventories. All old/shared/cache files remain untouched.

Recommend only the exact NF1–NF3 exclusions for coordinator reconciliation
after the second OTHER initially blind whole audit. No full annual
solution, additional positive factor family, n=57 exclusion, general
four-bit classification, numerical value or novelty follows.
