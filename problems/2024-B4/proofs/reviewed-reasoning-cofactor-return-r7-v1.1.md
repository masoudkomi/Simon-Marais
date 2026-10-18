# Accepted reasoning-cofactor-return-r7: exact coordinator scope

2026-10-18 UTC. **Proved, independently reviewed scoped partial result.**

Accept R7A–R7D, a sufficient whole-polynomial ABSOLUTE irreducibility criterion for the exact official2024(b) quotient over F2. Put n=ell*2^i+1, with odd ell>=3, i>=2, m=ord_ell(2), gcd(i,m)=1. Then the ENTIRE quotient phi_n is absolutely irreducible. Thus no pair of integer polynomials with both coefficientwise reductions nonconstant can give the requested factorization for these exponents. This does not classify all n or assert a converse when the gcd condition fails.

The accepted T1 excludes all absolute lines because wt(n)=wt(ell)+1>=3. The proof freshly reconstructs reducedness from the finite homogeneous gradient locus, rather than assuming a singularity theorem supplies it. Derivative equations at any putative factor intersection put affine a,b,l=a+b+1 among the ellth roots in E=F_(2^m). Infinity off R is smooth by the nonzero homogeneous Z derivative; at the three remaining infinity vertices phi=1.

R7B proves any two distinct absolute components can meet ONLY at P=(1:1:1). At each noncentral diagonal point the actual quotient has order q-1, sole tangent y, and next homogeneous coefficient x^q equal to b^(-q)/(b+1)^2, which is nonzero. At off-diagonal points the first form is L^q=(Ax+By)^q, with (A,B) not both zero. Clearing the next-form evaluation in direction(B,A) gives T=B(b+b^q)+A(a+a^q), and T^q=1+a^d+b^d+l^d for d=q^2-q+1. If it vanished, four DISTINCT E-elements a,b,1,l would solve one same nonzero-shift differential equation for the auxiliary Kasami power. The published APN theorem under gcd(i,m)=1 excludes this. The denominator-unit correction is retained and is divisible by L^q, so it cannot cancel the tangent restriction. Neither A nor B nor A+B is divided by. A local initial/next-form product argument excludes simultaneous vanishing at all these points.

At P the quotient cone is the squarefree product of q-2 distinct directions indexed by F_q minus F2. For a reduced reducible partition phi=UV, the central tangent subsets are disjoint, giving I_P(U,V)=ord_P(U)*ord_P(V), including zero if either factor misses P. No other intersection exists. Bezout therefore equates deg(U)*deg(V) to that product. Every positive-degree homogeneous divisor H has ord_P(H)<deg(H): equality would leave a binary homogeneous form after moving P to(0:0:1), hence absolute lines, excluded by T1. This strict inequality contradicts Bezout. No assumption that every component passes through P, genus formula, characteristic-zero Hessian or separable Gauss map is made.

R7D includes ell=2^s-1, s>=2, gcd(i,s)=1, i>=2; in particular i=2 and odd s>=3 give n=2^(s+2)-3 of binary weight s+1. The ell=3,i=2,n=13 case FAILS the gcd condition and is not covered; ell=1,i=1,n=1,n=3 are outside the criterion. The separately accepted R6 family is (Q-1)*Q^k+1, not a plus-sign variant; it is not a premise of this new gcd criterion. Other old R4/R5/three-bit/GK comparisons remain context with their original scopes.

Constructor C is EXCLUDED. Root OTHER WHOLE1 ENTIRE11/ALL64 froze13:56:26.404044UTC, FULL final all11 model readback and SEPARATE verify13:56:39.411753PASS. A OTHER WHOLE2 ENTIRE11/ALL64 froze13:59:26.846209, FULL final all11 model readback and SEPARATE verify14:00:11.097845PASS. BOTH were explicitly confirmed before any corresponding NEW peer findings/files/hashes/metadata access or release. Root FULL-read/reconciled ENTIRE13 author, BOTH22 review files, ALL128 dispositions, all issues/sources/logs/code/metadata. Zero substantive defects or required repairs remain; six root and nine A notes are closed within the submitted argument.

Both reviewers freshly checked official B4 setup/(b), the operative complete odd and FIRST complete even proofs of Carlet–Kim–Mesnager arXiv2002.00050v1, and Fulton's COMPLETE operative local-intersection and projective Bezout proofs. The original proofs behind CKM Lemmas4/5 were not freshly audited; these are precisely attributed published inputs. The later unfinished alternative even argument is unused. The first even proof covers field degree divisible by6. Root read the complete T1–T4 body/current authority; A also freshly read complete R6. Root's R6 body reading is historical with current authority checked and reducedness independently reconstructed here. A additionally read Fulton AppendixA; root makes no fresh whole-AppendixA claim. These literal source limits are preserved in each review.

Old root CG/R4/R5/R6 and A T1/C7/C11/CP/GK/S3/NF/R4/R5/R6 roles remain disclosed; no new independent self-recertification of old constructions is claimed. Férard2017's operative body remains unread, so no priority or nonoverlap claim is made. All new mathematics and both audits are hand reasoning. Administrative hashes are not mathematical evidence. No mathematical executable, CAS, scan, routine test or old certificate replay supplied a step. Full annual classification and external validation remain open or unclaimed.

The COMPLETE frozen mathematical submission follows as a byte-identical suffix. Its historical unverified label records submission status; this header and acceptance record state the current exact scope.

---

# A finite-field obstruction to intersections of the actual components

18 October 2026 UTC. **Candidate proof — unverified.** Constructor C,
`/root/review_2017_coarsening_r1`. TWO OTHER initially blind ENTIRE WHOLE
audits and coordinator reconciliation are required. This is a scoped
family assertion for official 2024 B4(b), not a complete classification,
priority claim, or claim of external validation. No mathematical program,
finite scan, CAS, or factor table supplies a step.

Requested inherited settings: gpt-6.1-sol, max reasoning. Effective-setting
readback is unavailable. Root supplied a generic target, no new proof
inference. C constructed the OLD accepted R6 and is not its independent
recertifier; that input keeps its separate older OTHER audits. The same
distinction applies to C's older sector3 construction and review roles.

## 0. Result, scope and exact imports

Work over K=the algebraic closure of F2. Put

    W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X),
    f_n=X^n+Y^n+Z^n+W^n, phi_n=f_n/R.

The quotient is the established polynomial in the official question;
its existence is not re-proved as preliminary work here. The question in
part (b) is a coefficientwise polynomial factorization over F2, with both
factors of positive degree. Whole absolute irreducibility excludes that
factorization. Having one absolute component over F2 would not suffice.

**R7A, proposed root-field criterion.** Let ell>=3 be odd, let i>=2, and
write

    q=2^i, n=ell*q+1, m=ord_ell(2).

If gcd(i,m)=1, the WHOLE phi_n is absolutely irreducible over K.

The auxiliary statements proved in the course of R7A are **R7B**: no two
distinct absolute components can meet away from P=(1:1:1), and **R7C**:
the squarefree tangent cone at P then contradicts a proper factorization.
**R7D** is the resulting explicit family: for every s>=2 and i>=2 with
gcd(i,s)=1, phi_((2^s-1)2^i+1) is absolutely irreducible. In particular,
for every odd s>=3, phi_(2^(s+2)-3) is absolutely irreducible. The latter
has binary weight s+1>=4. These are consequences, not computational data.

The operative accepted input is **T1**, from
`proofs/reviewed-structural-v1.1.md`, current
`reviews/structural-acceptance.md/json`: odd n of binary weight at least
three gives no absolute line factor of phi_n. Here wt(n)=wt(ell)+1>=3,
so its hypothesis holds. The full T1 proof/current authority was read.
Reducedness is the already accepted R6B statement; its short proof is
also reproduced in Section2 to make the component split explicit. No
new independent review of either old proof is claimed.

The external finite-field input is the classical **Kasami APN theorem**:
on E=F_(2^m), z -> z^(2^(2i)-2^i+1) is APN when gcd(i,m)=1. Thus, for
every c!=0 and every t in E, z^d+(z+c)^d=t has at most two solutions.
Attribution and literal operative read limits are in the source companion:
Carlet–Kim–Mesnager, [A direct proof of APN-ness of the Kasami functions](https://arxiv.org/pdf/2002.00050),
Sections1–4, including the complete odd-dimensional proof and the separate
complete first even-dimensional proof. Its external Lemmas4/5 remain
published inputs; their original underlying proofs are not claimed freshly
read. The later unfinished alternative even discussion is unused. This
is an application of a published theorem, not a new APN theorem.

The classical intersection inputs are projective Bezout for two curves
without a common component, and equality of local intersection number
with the product of multiplicities when their tangent cones are coprime.
The complete operative proofs in Fulton, *Algebraic Curves*, Sections3.3
and5.3, were read in the [author's teaching copy](https://math.stanford.edu/~conrad/145Page/handouts/algcurves.pdf).
They apply to reducible curves, over an algebraically closed field, in
characteristic two. No characteristic-zero Hessian or generic-separable
tangent assertion is imported.

## 1. The small local product obstruction

Let G in K[x,y] have order t>=2 at the origin, with initial homogeneous
term c*L^t for a nonzero linear form L and nonzero scalar c. Suppose
its term G_(t+1) is not divisible by L. Then it is impossible to write
G=UV with U(0)=V(0)=0.

Indeed, if r=ord(U)>=1 and s=ord(V)>=1, then r+s=t. Unique factorization
of binary forms gives U_r=a*L^r and V_s=b*L^s. The degree t+1 term of
their product is U_r V_(s+1)+U_(r+1) V_s, which is divisible by L.
This is a contradiction. A missing next term is treated as zero and
would be divisible by L, so nondivisibility is the exact needed condition.

The statement is local; it does not assert that G itself is irreducible.
It says that at this point at most one factor in a product can vanish.
Multiplying G by a local unit preserves the condition, because its next
term changes by a scalar multiple of the initial L^t term.

## 2. Reducedness and the complete possible intersection locus

The numerator f_n is nonzero: the coefficient of X^(n-1)Y is one.
Its homogeneous partial derivatives are

    (f_n)_X=(X^ell+W^ell)^q,
    (f_n)_Y=(Y^ell+W^ell)^q,
    (f_n)_Z=(Z^ell+W^ell)^q.                         (1)

Their common projective zero set is finite. W cannot be zero at a common
zero, since then X=Y=Z=0. Normalize W=1; all three coordinates must be
ell-th roots of unity. A repeated irreducible factor of f_n would divide
every partial in (1) and define an infinite curve in this finite set.
That is impossible. Thus f_n, and hence phi_n, are reduced over K. This
is the accepted R6B reducedness proof, restated with its actual hypotheses.

If two factors of phi_n vanish at the same point, the product rule makes
that point singular on phi_n. Consider a singular affine point (a:b:1),
and put l=a+b+1. From f_n=R*phi_n, f_n and its affine partials vanish
there, even if R vanishes. The two derivative equations and injectivity
of the q-th power give a^ell=b^ell=l^ell=u. Substitution in f_n=0 gives

    0=(a+b+l)u^q+1=u^q+1.

Therefore

    a^ell=b^ell=l^ell=1.                              (2)

In particular all three coordinates are nonzero. Let E=F_(2^m), with
m=ord_ell(2). The congruence 2^m=1 mod ell puts every ell-th root in E,
so a,b,l are all in E. Also m>=2: order one would require ell to divide1.
Under gcd(i,m)=1,

    E intersect F_q = F2.                              (3)

This standard finite-field intersection follows from the fixed fields
of the powers of Frobenius, or from gcd(2^m-1,2^i-1)=1 on nonzero
elements. No sampled field is being substituted for the algebraic closure.

At infinity Z=0, away from R=0, the homogeneous derivative

    (f_n)_Z=(X+Y)^(n-1)

is nonzero. Such points of phi_n are smooth. The three remaining
infinity points on R=0 are (1:0:0),(0:1:0),(1:1:0); phi_n is one at
each. One can check this by differentiating f_n=R phi_n in a direction
in which the derivative of R is one: the derivative of f_n is also one.
This is the same exact evaluation in T1's accepted companion calculation.
It is not a claim based only on the X,Y partials at infinity.

Consequently an intersection is either P=(1:1:1), a noncentral point on
one of the three diagonal lines R=0, or an affine point with R!=0
satisfying (2). The following two sections exclude the latter two types.

## 3. Noncentral diagonal points have a unit complementary factor

By coordinate symmetry it is enough to consider (b:1:1), b^ell=1,
b!=1. Condition(3) gives b not in F_q. Set

    c=b+1, E0=b^(-q), B0=1+b^(1-q).

Both c and B0 are nonzero. Translate X=b+x,Y=1+y,Z=1, and write F_j
for the homogeneous degree j term of f_n in x,y. The exact identity
(a+x)^n=(a+x)(a^q+x^q)^ell shows that all positive terms below q
vanish at a singular point. The first two terms here are

    F_q=B0*y^q,
    F_(q+1)=y*[ E0*x^q+E0*x*y^(q-1)+(1+E0)*y^q ].       (4)

The denominator is exactly

    R=c^2*y+c*y^2+x^2*y+x*y^2.                         (5)

Since f_n=R phi_n, its quotient has multiplicity q-1 and first two
homogeneous terms

    (phi_n)_(q-1)=(B0/c^2)*y^(q-1),
    (phi_n)_q=(E0/c^2)*x^q+(E0/c^2)*x*y^(q-1)
                          +[(1+E0)/c^2+B0/c^3]*y^q.    (6)

To verify the second line, subtract the degree q+1 product of c*y^2
and the first quotient term from (4), then divide by c^2*y. Subtraction
is addition in characteristic two. In particular the nonzero coefficient
E0/c^2 at x^q cannot be cancelled. The sole tangent y does not divide
the next term. Since q>=4, q-1>=3, Section1 applies and prevents two
factors from vanishing at this point. All three diagonals are covered
by symmetry. This uses the plane multiplicity q-1; it does not mistake
the contact with a prescribed line for that multiplicity.

## 4. Off-diagonal jets and the exact Kasami identity

Let (a:b:1) satisfy(2) and R(a,b,1)!=0. Then a,b,1,l are pairwise
distinct: equality of any pair reduces to a=b, a=1, or b=1, precisely
the three excluded diagonals. Define A,B as the unique q-th roots in K
of

    A^q=a^(1-q)+l^(1-q),
    B^q=b^(1-q)+l^(1-q).                               (7)

The initial numerator terms after translation X=a+x,Y=b+y,Z=1 are

    F_q=(A*x+B*y)^q,
    F_(q+1)=a^(-q)*x^(q+1)+b^(-q)*y^(q+1)
                                      +l^(-q)*(x+y)^(q+1). (8)

There are no positive terms below q, for the same exact Frobenius
expansion as before. The degree q term is nonzero. Indeed, if A=B=0,
then a/l and b/l are in F_q; hence 1/l=(a+b+l)/l is in F_q, putting
a,b,l in F_q. By(3) they are all one, contrary to this off-diagonal
point. Individual A or B need not be divided by in what follows.

Put L=A*x+B*y and take its nonzero tangent direction (B,A). The following
two hand identities are the key step, with d=q^2-q+1:

    F_(q+1)(B,A) = T/(a^q*b^q*l^q),
    T=B*(b+b^q)+A*(a+a^q),
    T^q=1+a^d+b^d+l^d.                                (9)

For the first identity, expand (A+B)^(q+1). After using(7) and clearing
the denominator a^q*b^q*l^q, the coefficient multiplying B becomes

    b*l^q+l*b^q+a*b^q+b*a^q
       =b*(a+l)^q+(a+l)*b^q
       =b*(b+1)^q+(b+1)*b^q=b+b^q.

The coefficient multiplying A is a+a^q by the same calculation with
a,b interchanged. This proves the first line of(9), including any
zero-coefficient case, without division by A,B or A+B.

For the second identity, raise T to the q-th power and use(7):

    T^q=a+b+a^d+b^d
          +l^(1-q)*[(a+b)^q+(a+b)^(q^2)].

Since a+b=l+1, the final bracket becomes l^q+l^(q^2), and its product
with l^(1-q) is l+l^d. As a+b+l=1, the desired expression follows.
All equalities in(7)-(9) hold in K; no finite-field function identity has
yet replaced a polynomial factorization statement.

## 5. Applying the published APN theorem at actual singular points

All a,b,1,l lie in E. The published Kasami theorem applies to z^d on E
by gcd(i,m)=1. If its parameter is stipulated in the range1,...,m-1,
replace i by its positive residue there. It is nonzero since m>=2 and
gcd(i,m)=1; Frobenius reduction shows the same positive-exponent
function on E, including its value zero at z=0.

Suppose T=0. By(9),

    a^d+b^d=1+l^d.

Take c0=a+b=1+l. It is nonzero. Each of the four DISTINCT elements
a,b,1,l solves

    z^d+(z+c0)^d=a^d+b^d.                              (10)

This contradicts the APN bound of two solutions. Hence T!=0. Equation(9)
shows that L does not divide F_(q+1).

Because R is a unit here, write R=R0+R1+... with R0!=0. The quotient's
terms of degrees q and q+1 are

    (phi_n)_q=F_q/R0,
    (phi_n)_(q+1)=F_(q+1)/R0+R1*F_q/R0^2.              (11)

The correction is divisible by L^q, so it cannot cancel the nonzero
restriction of the first term to L=0. Thus the initial term is a
nonzero scalar times L^q and L does not divide the next term. Section1
excludes the simultaneous vanishing of two factors. This proves R7B:
any intersection of distinct absolute components is confined to P.

The APN theorem is used only to certify the nonzero value in(9) at
this actual finite-field singular point. Whole irreducibility in the
polynomial ring over K follows from the subsequent geometric argument;
it is not inferred from APN-ness of the original exponent n on a field.

## 6. The central cone, coprime factors and projective Bezout

At P translate X=1+x,Y=1+y,Z=1. The degree q term of f_n cancels;
its degree q+1 term is x^q*y+x*y^q. The denominator is x*y*(x+y).
Consequently phi_n has multiplicity q-2 and initial cone

    C(x,y)=(x^(q-1)+y^(q-1))/(x+y)
           =product_(alpha in F_q minus F2)(x+alpha*y). (12)

The q-2 lines are distinct: q-1 is odd, so the roots of the numerator
are simple and division removes exactly alpha=1. There is no missing
factor x or y in(12). In particular this is a squarefree tangent cone.

Suppose phi_n were reducible over K. Since it is reduced, split its
absolute components into two nonempty sets, obtaining homogeneous
positive-degree U,V with phi_n=U*V and gcd(U,V)=1. Set a0=deg U,
b0=deg V, r=m_P(U), s=m_P(V), allowing r or s to be zero if the
factor avoids P. The tangent cones at P partition(12), so if both
vanish their tangent cones are coprime. The classical local intersection
formula therefore gives

    I(P,U,V)=r*s.                                      (13)

If either is a unit at P, both sides are zero instead. R7B shows there
are no other intersections, including at infinity. Projective Bezout
now gives the exact equality

    a0*b0=r*s.                                        (14)

For every nonconstant homogeneous divisor H of phi_n,

    m_P(H)<deg H.                                     (15)

To see this, change projective coordinates taking P to(0:0:1). Equality
would make H a binary homogeneous form independent of Z: every monomial
has X,Y-degree equal to deg H. Over K it is a product of linear forms,
and hence would supply an absolute line of phi_n. Accepted T1 forbids
that. The non-strict inequality is the elementary local-degree bound;
the strict improvement in(15) does not assume irreducibility of H.

Apply(15) to U and V. Since a0,b0 are positive, a0*b0>r*s, contradicting
(14), also when r*s=0. This proves R7C and the proposed R7A. No inference
that all components pass P was used; factors missing P were expressly
included. No genus formula for a reducible curve is applied.

## 7. Consequences, endpoints, overlap and remaining gap

For s>=2 let ell=2^s-1. Its multiplicative order m is exactly s: 2^s=1
mod ell, while for 0<t<s the positive integer 2^t-1 is smaller than ell.
R7A therefore gives R7D under gcd(i,s)=1. Taking i=2 and s odd>=3 gives

    n=(2^s-1)*4+1=2^(s+2)-3.

For example ell7,m3 gives every i>=2 not divisible by3; the hand
illustrations n29 and n113 are not a factor table. No special finite
case is needed for either example. When s2 the result overlaps the
accepted binary-weight-three family; s>=3 has weight at least four.

In the new domain n>=13, deg phi_n=ell*q-2>0, and q is the MAXIMAL
power of two dividing n-1 because ell is odd. The gcd hypothesis excludes
the ell3,i2,n13 corner; no incorrect absolute irreducibility assertion
at13 is made. i1 is outside this packet and belongs to the separately
attributed published whole3mod4 sector. ell1 is outside this packet
and has binary weight two. n1 is a zero numerator endpoint, and n3
gives a unit quotient; neither is silently included in this theorem.

The suggested n=(Q+1)Q+1 boundary has binary weight three and is already
covered by accepted three-bit r2. It was rejected as a new target before
the present proof was developed. Accepted R6's ell=2^s-1,i=s*k,k>=2
and the present gcd(i,s)=1 condition cover different parameter ranges;
neither is re-labelled as a new proof of the other. No R4 degree bound,
R5 prime-field/Frobenius filter or F2-descended cofactor is needed here.

For the stated family, any official g,h with both reductions nonconstant
would yield phi_n=bar(g)*bar(h) over F2, hence over K, contradicting whole
absolute irreducibility. Nonhomogeneous g,h are allowed: irreducibility
in the polynomial ring already excludes such a product. Nothing relies
on reducing polynomial functions modulo z^(2^m)-z.

No converse is claimed when gcd(i,m)>1. In that range the finite-field
intersection argument and the APN bound fail in the proof; that does
not assert actual reducibility. The general odd-n classification,
smaller exceptional sectors and possible published overlap remain open.
The Férard2017 operative body remains unread. This adaptation uses a
classical published APN theorem and classical intersection geometry,
with no new-method or priority assertion.

## 8. Whole-audit and preservation boundary

The full obligations/constructor checks, issue and failed-route record,
source scopes, worklog, no-mathematical-code record, compact input/parent
fingerprints and ALL metadata form one submission. The older working
notebook remains historical, with its incomplete read-status statements
dated there; this complete main and source record supersede those live
read limits without altering the notebook.

The new administrative script performs byte/JSON/obligation checks only;
it does not run mathematics or old authors' programs. Every old input,
peer record, shared map, cache and Git byte is preserved. Root alone may
promote after TWO OTHER ENTIRE initially blind WHOLE audits, full source
hypothesis checks, all substantive repairs and affected reaudits. C as
constructor is excluded. This candidate is not an annual solution.
