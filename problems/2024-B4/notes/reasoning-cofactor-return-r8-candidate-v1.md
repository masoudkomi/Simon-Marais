# A no-four-sum root set forces whole absolute irreducibility

18 October 2026 UTC. **Candidate proof - unverified.** Constructor C,
`/root/review_2017_coarsening_r1`. TWO OTHER initially blind ENTIRE WHOLE
audits and coordinator reconciliation are required. C is excluded. Root
supplied the research target only, no NEW mathematical inference. Requested
inherited gpt-6.1-sol/max; effective readback unavailable. No priority,
external validation or complete annual classification is claimed.

Only official2024 B4(b) is investigated. The conclusion concerns the WHOLE
polynomial over the algebraic closure, hence excludes a coefficientwise
factorization over F2. No preliminary construction is reproduced. The
root-set and intersection arguments below are hand proofs, not outputs of
a finite-field scan or factor table.

## 0. Exact statement and old-input boundary

Work over K=F2bar. For odd n put

    W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X),
    f_n=X^n+Y^n+Z^n+W^n, phi_n=f_n/R.

The established quotient is the exact coefficientwise polynomial in the
official question. For odd ell>=3 let mu_ell={a in K:a^ell=1}. The condition
used here is

    (NF4) no FOUR DISTINCT elements of mu_ell have sum zero.

It is a condition on the entire finite root set, not on the number of
points found by a scan. Classically it is the absence of weight-four
words in the maximal binary cyclic code of length ell. No coding theorem
is needed below; the finite-field version is used directly.

**R8A, proposed whole-polynomial criterion.** If ell>=3 is odd and satisfies
(NF4), q=2^i with i>=2, and (ell,q)!=(3,4), then the WHOLE

    phi_(ell*q+1)

is absolutely irreducible. No gcd(ell,q-1)=1 assumption is required.
The pair (3,4), n13, is expressly excluded from this absolute assertion.

**R8B, explicit arithmetic sufficient conditions.** Either congruence

    2^t=-1 mod ell, or 2^t=3 mod ell, for some integer t>=1,

implies (NF4). Consequently R8A applies at EVERY i>=2, except its stated
single pair, whenever one of these arithmetic conditions holds.

**R8C, concrete residual infinite families.** In particular, the WHOLE
quotient is absolutely irreducible for EVERY i>=2 at

    n=11*2^i+1, and n=23*2^i+1.

The subfamilies i=10k and i=11k, respectively, k>=1, fail the older
root-field coprimality criterion and fail the original no-four-sum theorem's
additional diagonal gcd condition. They are included by the present
proposed proof. This is a comparison of literal hypotheses, not a claim
that these exponents are absent from the published literature.

The only operative accepted mathematical inputs are:

* **T1** in `proofs/reviewed-structural-v1.1.md`, with its complete current
  structural-acceptance MD/JSON: odd binary weight>=3 excludes every
  absolute line of phi_n.
* **R6B**, and the general part of **R6C**, in
  `proofs/reviewed-reasoning-cofactor-return-r6-v1.1.md`, with its complete
  current acceptance MD/JSON: for odd n=ell*q+1, ell odd and q the maximal
  2-power, f_n and phi_n are reduced, and EVERY nonlinear absolute component
  has degree>=q. With T1 every positive-degree absolute divisor has
  degree>=q. The statement is not limited to R6D's special Mersenne family.

Both complete bodies and authorities were freshly read. C constructed OLD
R6/R7, and previously reviewed T1; those separate accepted inputs retain
their OTHER audits. This is not independent self-recertification. R7's
complete body/current authority was read as a comparison. R4 and corrected
R5 bodies were read as context, but their cofactor/threshold/Frobenius
inequalities are NOT premises. No classifying APN theorem, new genus
inequality, fixed-field orbit hypothesis or formal cofactor is imported.

The classical external geometric inputs are projective Bezout for curves
with no common component and the local equality between intersection
number and the product of multiplicities when tangent cones are coprime.
Fulton's complete operative proofs and characteristic-two scope were
freshly read; precise ranges are in the source record. Reducible
complementary products are allowed in these statements.

## 1. Published overlap: what is already classical

McGuire's original1995 thesis printed22–24 contains the relevant published
precursors. Theorem6 treats q4 under (NF4), with its stated n>13 range.
Theorem7 treats (NF4) together with gcd(ell,q-1)=1. The entire operative
statements and supplied proofs were visually read in the primary-author
scan, together with their local lemmas. The original joint journal PDF
was not read; its parallel coauthor thesis is the actual source read.

The proposed additional step is to use the separately accepted generic
component-degree lower bound q. It can dominate the contributions from
ALL remaining ordinary diagonal points even when gcd(ell,q-1)>1. The
classical no-four-sum method and both congruence conditions in R8B are
attributed, not presented as new general principles. Possible overlap
with later Férard or other work remains unresolved; no priority claim
follows from this reconstruction.

For the code terminology, fix a primitive ellth root zeta. A binary
polynomial of degree<ell and weight four has support at four distinct
exponents, so its value at zeta is the sum of four distinct elements
of mu_ell. Conversely any such four elements are four distinct powers
of zeta and specify this word. Thus the code/root formulations are
literally equivalent; no unread coding theorem is needed for that step.

## 2. All possible component intersections

Write n=ell*q+1. Since ell is odd, q is exactly the maximal 2-power
dividing n-1. Also wt(n)=wt(ell)+1>=3, so T1 applies. Reducedness is
available from R6B; its short justification is recalled here. The gradient
of f_n is

    (f_n)_X=(X^ell+W^ell)^q,
    (f_n)_Y=(Y^ell+W^ell)^q,
    (f_n)_Z=(Z^ell+W^ell)^q.

Their common projective zero set is finite: W cannot vanish there, and
after setting W=1 all X,Y,Z are ellth roots of unity. A repeated factor
would divide all three partials and give an infinite curve in this finite
set. Thus no repeated component is hidden in a factor partition.

Any intersection of two distinct absolute factors is singular on phi_n.
At an affine singular point (a:b:1), put l=a+b+1. Because f_n=R phi_n,
both f_n and its affine partials vanish at that point, including when R=0.
The two derivative equations give a^ell=b^ell=l^ell=u. Substitution into
f_n=0 gives u^q+1=0; thus a,b,l all belong to mu_ell. In particular they
are nonzero. This is a consequence at an ACTUAL singular point, not an
assumed decoration on a prospective factor.

If R(a,b,1)!=0, the four elements a,b,1,l are pairwise distinct. Equality
of any two is equivalent to one of a=b,a=1,b=1, the three diagonals.
Their sum is zero, contradicting (NF4). Therefore there is NO
off-diagonal singular point, and hence no component intersection there.

At infinity Z=0 away from R=0, `(f_n)_Z=(X+Y)^(n-1)` is nonzero, so
phi_n is smooth there. The only infinity points with R=0 are
(1:0:0),(0:1:0),(1:1:0). Differentiating f_n=R phi_n at these points
in a direction where the derivative of R is one gives phi_n=1. For
example use the Y derivative at (1:0:0), the X derivative at (1:1:0),
and symmetry. Thus infinity contributes no component intersections.

Every possible remaining intersection is P=(1:1:1) or one of the three
sets of noncentral diagonal points represented by (b:1:1), b in mu_ell
minus{1}. The three sets are disjoint: two diagonal lines meet only at P.

## 3. Noncentral diagonal local forms: both cases, not a gcd shortcut

Fix b in mu_ell minus{1}. Translate X=b+x,Y=1+y,Z=1 and set

    c=b+1, E=b^(-q), B=1+b^(1-q).

Expansion of `(a+x)^n=(a+x)(a^q+x^q)^ell` gives no positive numerator
terms below q, and gives exactly

    (f_n)_q=B*y^q,
    (f_n)_(q+1)=y*[E*x^q+E*x*y^(q-1)+(1+E)*y^q].

The translated denominator is

    R=c²*y+c*y²+x²*y+x*y².

Here c and E are always nonzero. We distinguish the actual Frobenius
condition on b; it need not hold uniformly on mu_ell.

If b not in F_q, then B!=0. Polynomial division gives

    (phi_n)_(q-1)=(B/c²)y^(q-1),
    (phi_n)_q=(E/c²)x^q+(E/c²)x*y^(q-1)
                          +[(1+E)/c²+B/c³]y^q.

In particular the next term is not divisible by the sole tangent y,
because its x^q coefficient E/c² is nonzero. No two factors vanishing
at this point can multiply to this local equation: if their orders r,s
are positive with r+s=q-1, their first forms are scalar multiples of
y^r,y^s, so their next product form is divisible by y, a contradiction.
Thus such a point contributes zero to any coprime factor intersection.

If b is in F_q, then B=0 and E=b^-1. The initial quotient term is now

    (phi_n)_q=(b^-1/c²)[x^q+x*y^(q-1)+c*y^q].

It has multiplicity q. Its tangent cone has q DISTINCT lines: after
putting y=1 the polynomial is x^q+x+c, whose derivative is 1, and the
coefficient of x^q is nonzero so there is no missing direction y=0.
Thus this is an ordinary point of total multiplicity q, and tangent
subsets of disjoint factors are coprime. This is the case which the
old gcd condition removed; it is explicitly retained here.

Put d=gcd(ell,q-1). Exactly d elements of mu_ell lie in F_q, because
the common roots of T^ell-1 and T^(q-1)-1 form mu_d. Both exponents
are odd so the roots are distinct. Hence there are exactly

    3(d-1)

noncentral diagonal points of this ordinary type. All other diagonal
points are of the preceding no-intersection type. No distribution or
equal multiplicity on different points is presumed.

## 4. Central cone and the global numerical contradiction

At P translate X=1+x,Y=1+y,Z=1. The numerator's degree q term
cancels and its degree q+1 term is x^q*y+x*y^q. Since R=xy(x+y),
the quotient has multiplicity q-2 with squarefree tangent cone

    (x^(q-1)+y^(q-1))/(x+y)
       =product_(alpha in F_q minus F2)(x+alpha*y).

The q-2 directions are distinct, since q-1 is odd. The same facts and
their characteristic-two boundaries are in accepted T1–T4/R6/R7.

Suppose phi_n is reducible over K. Choose an absolute irreducible
component U of least degree e and let V=phi_n/U. Reducedness makes
U,V coprime, both nonconstant. Put N=deg phi_n=ell*q-2. Since T1
excludes all lines and accepted R6B bounds every nonlinear component,

    q<=e<=N/2.

Consequently, using `(e-q)(N-e-q)>=0`,

    deg U*deg V=e(N-e)>=q(N-q)=(ell-1)q²-2q.       (L)

The interval is legitimate: N>=2q because ell>=3,q>=4. This uses an
ACTUAL least component and its ACTUAL complementary product. It does not
assume a small invariant cofactor, global component transitivity or that
all components pass through P.

At P, the local multiplicities of U,V add to q-2 and their tangent cones
are coprime. The local intersection is their product, at most (q-2)²/4.
If either misses P that product and the intersection are zero. At each
ordinary noncentral diagonal point their multiplicities add to q and
the same reasoning bounds its intersection by q²/4, including zero.
There is no intersection at any other point by Sections2–3. Projective
Bezout therefore gives

    e(N-e)<= [(q-2)²+3(d-1)q²]/4.                 (U)

The quadratic bounds maximize over all real multiplicity splits, so
they are valid upper bounds for actual integer splits. They do not require
the maxima to be simultaneously attained, nor a genus formula on V.

The difference between (L) and the right side of (U) is exactly

    [(4ell-3d-2)q²-4q-4]/4
       >=[(ell-2)q²-4q-4]/4,                     (D)

because d<=ell. For ell>=5,q>=4 the last numerator is at least
`3q²-4q-4>=28>0`. For ell=3 and q>=8 it is at least
`q²-4q-4>=28>0`. These inequalities follow directly from
q(3q-4)-4 and q(q-4)-4 respectively, without an optimizer or scan.

Thus (L) and (U) contradict each other throughout the proposed domain.
The only remaining allowed power-of-two pair is ell3,q4. There the
lower number is24 and the upper number is25 (d3), so this argument
does NOT exclude it. It must not be silently included. This proves
the proposed R8A, subject to the required independent reviews.

The ordinary F2 conclusion for n13 is a separately accepted Kasami/
three-bit fact; it is not needed to prove R8A and is not upgraded to
absolute irreducibility here. n1,n3,ell1 and q2 lie outside R8A.

## 5. Two complete arithmetic proofs of (NF4)

Suppose first Q=2^t is -1 modulo ell. Every a in mu_ell satisfies
a^Q=a^-1. If four distinct elements a,b,c,d had zero sum, put
s=a+b=c+d, which is nonzero. Raising the equal sums to the Qth
power gives

    s^Q=a^-1+b^-1=s/(ab)=s/(cd).

Therefore ab=cd. The unordered pairs {a,b} and {c,d} are both the
roots of the same monic quadratic T²+sT+ab, so they coincide. This
contradicts four distinct elements. Equivalently mu_ell is contained
in the norm-one circle of F_(Q²)/F_Q, but that language is not needed
to justify the calculation. This proves (NF4) in the first case.

If instead Q=2^t is 3 modulo ell, then a^Q=a³ for each a in mu_ell.
Four distinct elements summing to zero would also have sum of cubes
zero after applying Q-Frobenius. Substituting d=a+b+c, however, gives

    a³+b³+c³+(a+b+c)³=(a+b)(a+c)(b+c)!=0.

The exact characteristic-two polynomial expansion and distinctness
give the contradiction. This proves the second case and R8B. These
are classical sufficient conditions explicitly identified in the
original source before its Theorem6; they are fully rederived here
instead of importing an unread coding result.

For ell11, `2^5=32=-1 mod11`; R8B/R8A give every i>=2. Its order of
2 is exactly10: it divides10, 2^5=-1 and the proper divisors1,2,5
do not yield1. In particular i=10k fails the older coprimality and
gcd(11,2^i-1)=1 conditions. These exponents have binary weight four.

For ell23, `2^8=256=3 mod23` and `2^11=2048=1 mod23`.
Since11 is prime and 2!=1 mod23, the order is exactly11. Thus every
i>=2 is covered, including i=11k, where both older coprimality tests
fail. These exponents have binary weight five. These are exact hand
congruences supplying infinite families, not a table of factorizations.

## 6. Scope, attribution and exact remaining gap

Whole absolute irreducibility excludes the official two positive-degree
F2 factors even if their integer lifts are nonhomogeneous. The proof
is in K[X,Y,Z], never in a ring of polynomial functions on a finite
field. No conclusion follows merely from APN-ness or existence of one
F2-defined absolute component.

The no-four-sum condition and classical local/Bezout method are old.
The candidate extension combines them with the accepted universal
component-degree lower bound, retaining all ordinary diagonal points
instead of assuming they are absent. Original JMW/McGuire theorem and
proof scopes are precisely attributed. The journal version and original
JW1993 full proof were not read; they are not hidden premises. Férard2017's
operative body remains unread, so neither nonoverlap nor priority follows.

This criterion does not decide mu_ell with four distinct zero-sum roots,
nor provide a converse. In particular it does not address the general
remaining actual cofactor landscape or turn a formal invariant into a
divisor. Existing counterexamples outside (NF4) and other accepted
families are not contradicted. The unrestricted annual classification
and external validation remain open. Entire source/failure/worklog/
obligation/check/code/metadata records accompany this candidate; no
promotion occurs without TWO OTHER whole audits and full reconciliation.
