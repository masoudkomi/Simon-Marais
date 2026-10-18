# Accepted reasoning-cofactor-return-r6: exact coordinator scope

2026-10-18 UTC. **Proved, independently reviewed scoped partial result.**

Accepted **R6A–R6D** in their exact domains. For every Q=2^s with s≥3 and every k≥2, the WHOLE polynomial φ_n over the algebraic closure of F2 is absolutely irreducible when n=(Q−1)Q^k+1. Thus these exponents do not admit the official coefficientwise factorization into two factors nonconstant modulo2. This is a scoped family result for2024 B4(b), not the full classification or a priority claim.

R6A is the local line-order lemma: an irreducible nonlinear factor at an actual smooth point, with complementary factor a unit there, has degree at least q if the whole polynomial's nonzero tangent restriction has no terms of degrees2,…,q−1. Only vanishing ORDER is transferred through the unit; missing individual Taylor coefficients are not assigned to the factor or quotient. The nonzero tangent and nonzero polynomial line restriction are explicit, over the working field.

R6B applies to every odd n≥3, n−1=ell*q with ell odd and q the maximal2-power. The numerator is nonzero, and its three partials have only finitely many common projective zeros: W cannot vanish, and normalization W=1 bounds the coordinates to ellth roots. A repeated factor would divide all partials and give an infinite common-zero curve, so the numerator and quotient are absolutely reduced. On ANY nonlinear absolute component choose an actual affine point outside that finite set. The complementary factor is a unit, Euler supplies a nonzero affine tangent, and exact Frobenius proves the numerator's tangent gap. Therefore EVERY nonlinear component has degree≥q. No central-point, prescribed finite-field rationality, odd component degree, separable Gauss map or characteristic-zero theorem is assumed.

R6C uses separately accepted T1 ONLY when odd binary weight≥3, eliminating all absolute lines. Every actual nonconstant divisor then has degree≥q and the number of components is at most ell−1. The n1/n3, q2 and binary-weight-two boundaries remain exactly as stated. A formal invariant polynomial is not assumed to divide the numerator.

For R6D, q=Q^k is indeed the maximal2-power and the binary weight is s+1≥4. Uniformly for Q≥8,k≥2, q≥Q²>2ell+7 and0<A=Q(Q−3)<Q²≤q. If the reduced φ_n were reducible, its least-degree absolute component would be the SAME actual proper factor with0<e≤N/2 to which separately accepted R4A gives e<A, while R6B/T1 give e≥q. This contradiction proves WHOLE absolute irreducibility. R4A's EVERY-actual-factor scope, reduced-product correction and signs proved BEFORE division are retained. R4B grouping/descent, the prime-s Frobenius filter and corrected R5 are not main premises.

C is the sole NEW constructor and EXCLUDED. OTHER root WHOLE1 and OTHER A WHOLE2 reconstructed ALL48 obligations each. Their ENTIRE report/ALLledgers/issues/source/log/code/ALLmetadata froze12:34:46.224754 and12:46:44.965881UTC; each received FULL final model readback and SEPARATE verification12:35:24.873297 and12:46:53.362390, respectively. BOTH entire checkpoints were explicitly confirmed before corresponding NEW peer findings/files/hashes/metadata were released. Root read ALL12 author files, BOTH complete eleven-file review packets, ALL96 dispositions/issues/source/log/code/ALLmeta and reconciled them. A clipped review2 baseline was recovered by a separate full read. Zero substantive defects or required repairs remain; six root and six A notes are closed exact-scope restrictions.

Old T1 authorship by A and root CG/R4/R5 construction are disclosed rather than counted as new independent recertification of those inputs. Root freshly read the complete operative R4 body and T1's complete operative statement/proof/current authorities; it does not newly claim a whole read of unrelated T2–T4. A freshly read complete T1–T4/R4/CG/correctedR5 bodies and authorities. Fresh primary Fulton Bézout and Arakelian–Speziali Proposition3.1 proof ranges are recorded; the latter's p>ambient dimension fails for a characteristic2 plane and is NOT applied. Férard2017's operative body remains unread/possible overlap unresolved, so novelty is not established. Constructor-only contextual sources are not falsely adopted as reviewers' whole reads.

The general k1 case, s<3, other odd parts and the annual classification remain unresolved by this packet. No mathematical executable,CAS,scan,test,source/author rerun or old-certificate replay supplied these hand proofs or audits. Administrative SHA/JSON checks are preservation only. Internal review is not external validation. The original mathematical candidate remains an exact suffix, and all prior bytes are preserved.

The COMPLETE frozen mathematical submission follows as a byte-identical suffix. Its historical unverified label records submission status; this header and acceptance record state the current exact scope.

---

# Tangent contact excludes the bounded actual cofactor

18 October 2026 UTC. **Candidate proof — unverified.** Constructor C,
`/root/review_2017_coarsening_r1`. TWO OTHER initially blind ENTIRE WHOLE
audits, each covering every obligation and all companions/metadata, and
coordinator reconciliation are required. No promotion, novelty or complete
annual classification is claimed. No mathematical program supplied a step.

Requested inherited settings: gpt-6.1-sol, max reasoning. Effective-setting
readback is unavailable. Only official 2024 B4(b) is investigated.

## 0. Question, proposed result and exact input boundary

Over K, the algebraic closure of F2, put

    W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X),
    f_n=X^n+Y^n+Z^n+W^n, phi_n=f_n/R.

The official question is coefficientwise reducibility of phi_n over F2 for
odd positive integers n. Two nonconstant integer polynomials modulo two
give two positive-degree factors of phi_n in the polynomial ring over F2.
An assertion that the WHOLE phi_n is absolutely irreducible therefore
excludes the requested factorization. Merely having an F2-defined absolute
component would not suffice.

The proposed main consequence is

    Q=2^s, s>=3, k>=2, n=(Q-1)Q^k+1
        ==> phi_n is absolutely irreducible.                 (R6D)

It covers the remaining k=2 parameters of this particular family using an
actual smaller-factor theorem already accepted in R4. It makes no assertion
about general k=1, s<3, other odd parts of n-1, or the full annual problem.
Previously accepted Q8, Q16, Q32 and k>=3 cases remain attributed old
results. Possible overlap with Férard2017 remains unresolved because that
operative body has not been obtained/read.

The NEW inference is a generic smooth-point tangent restriction. It uses
the numerator f_n, rather than assuming that a quotient/factor has the same
Taylor gap. The proof explicitly transfers the zero order through a unit
complementary factor.

There are exactly TWO operative accepted mathematical imports:

1. **T1**, `proofs/reviewed-structural-v1.1.md`, with current authority
   `reviews/structural-acceptance.md/json`: if odd n has binary weight at
   least three, phi_n has no absolute line factor. The complete operative
   T1 proof and its boundaries were freshly read. Its three prescribed
   numerator lines have multiplicity one.
2. **R4A**, `proofs/reviewed-cofactor-dominant-r4-v1.1.md`, with current
   authority `reviews/cofactor-dominant-r4-acceptance.md/json`: for
   Q=2^s,s>=3, ell=Q-1,q=Q^k,k>=1, N=ell*q-2,
   A=(ell-2)(ell+1), if q>=2ell+7, EVERY ACTUAL proper reduced factor U
   of phi_n over K with 0<e=deg(U)<=N/2 has e<A.

The complete accepted R4 body was freshly read. R4A itself depends on the
accepted CG1/CG2 inequalities and the reduced-product correction; this
packet does not replace that accepted proof by an irreducible genus formula
on a product. R4B's unique component, exact S4 descent and the additional
N>=3A-2 hypothesis are available context but are NOT needed below. No R4
symmetry congruence, R5 prime-s criterion, HM component theorem, modern
Frobenius-nonclassical theorem, invariant-ring assertion or formal cofactor
is a new mathematical premise.

C's older T1 whole-review and R4 whole-review roles are disclosed. Those
separately accepted inputs retain their two older OTHER audits; this new
construction does not recertify them independently. Root supplied the
generic target and requested checks, but supplied no NEW R6 inference.
C alone is the NEW constructor and is excluded from its independent reviews.

## 1. A local gap-to-degree lemma (R6A)

Here the coefficient field can be any field. Suppose F=h J are affine
polynomials in x,y, and P=(a,b) is a point such that

    h(P)=0, J(P)!=0, (h_x(P),h_y(P))!=(0,0).

Suppose h is irreducible of degree e>=2. Let v=(v1,v2) be any nonzero
vector with

    h_x(P)v1+h_y(P)v2=0,

and let L be the line parameterized by P+T v. Assume that for an integer
q>=2 the coefficients of T^j in F(P+T v) vanish for 2<=j<q.
Then

    e>=q.                                                   (1)

Proof. The constant coefficient vanishes since h(P)=0. The linear
coefficient is

    F_x(P)v1+F_y(P)v2
      =J(P)[h_x(P)v1+h_y(P)v2]=0,

by the product rule and h(P)=0. Thus T^q divides F(P+T v).

The restriction h(P+T v) is NOT the zero polynomial. Otherwise h vanishes
identically on the affine line L. An invertible affine change taking L to
the line y=0 shows that its defining linear polynomial divides h; this
contradicts irreducibility and e>=2. The restriction J(P+T v) is nonzero
and has nonzero constant coefficient J(P). Hence both restrictions are
nonzero, and the order at T=0 of their product is exactly the order of
h(P+T v). That order is therefore at least q. But a nonzero univariate
polynomial of degree at most e cannot have a zero of order exceeding e.
This proves (1).

The proof is a direct line restriction, valid in characteristic two. It
does not assume separability of a Gauss map, a generic tangent order theorem,
a characteristic-zero Hessian, or an irreducibility test on a finite-field
function. Its smooth-point and unit hypotheses are essential. It is a
classical tangent-contact argument, with no assertion of novelty.

## 2. Reducedness of the actual numerator (first part of R6B)

Let n>=3 be ANY odd integer. Write uniquely

    n=ell*q+1, q=2^i, i=v2(n-1)>=1, ell positive and odd.

The numerator f_n is nonzero: the coefficient of X^(n-1)Y is n=1 in
characteristic two. Its three homogeneous partial derivatives are

    (f_n)_X=(X^ell+W^ell)^q,
    (f_n)_Y=(Y^ell+W^ell)^q,
    (f_n)_Z=(Z^ell+W^ell)^q.                               (2)

Their common projective zero set is finite. Indeed, at a common zero W
cannot vanish, since W=0 would force X=Y=Z=0. Scale W to one. Then all
three X,Y,Z satisfy t^ell=1, so at most ell^3 triples are possible (with
the additional equation X+Y+Z=1). This is a statement over the algebraic
closure, not a finite-field sampling argument.

If an irreducible polynomial h occurred with multiplicity at least two
in f_n, the product rule would make h divide ALL three partial derivatives
in (2), including when that multiplicity is even. Its projective curve
would lie in their finite common zero set. A positive-dimensional plane
curve over an algebraically closed field is infinite, a contradiction.
Thus f_n is reduced over K.

For completeness, infinitude here can also be seen in affine coordinates.
An irreducible nonlinear homogeneous plane curve has an infinite affine
part in a chart it meets: after dehomogenizing, it has positive degree in
one variable; outside finitely many values where its leading coefficient
vanishes, that nonconstant univariate polynomial has a root in K. A line
too is infinite. Thus no curve can be contained in the finite set above.

In particular phi_n is nonzero and reduced whenever n>=3. The quotient
is homogeneous of degree n-3; the established polynomial divisibility by R
is used as the definition of phi_n, without reproducing preliminary (a).

## 3. Every nonlinear absolute component has degree at least q

Let h be ANY homogeneous absolute irreducible nonlinear factor of f_n,
with degree e>=2. This includes any nonlinear absolute factor of phi_n.
Write f_n=h J over K. Reducedness gives h not dividing J.

There is an affine point P of this component with Z=1 where the homogeneous
gradient of f_n is nonzero. The component is not the line Z=0 and has an
infinite affine part, whereas (2)'s common zero set is finite. Choose any
point outside that finite set. At this point

    J(P)!=0 and the homogeneous gradient of h is nonzero,    (3)

because grad(f_n)(P)=J(P) grad(h)(P).

The affine gradient in x,y is nonzero as well. Euler's homogeneous identity
for f_n, evaluated at P=(a:b:1), gives

    a(f_n)_X(P)+b(f_n)_Y(P)+(f_n)_Z(P)=n f_n(P)=0.

If the first two partials vanished, the third would vanish too, contrary
to the choice of P. Thus some nonzero affine vector v is tangent to f_n
at P; by (3) it is the same tangent as for h. Explicitly in characteristic
two one may take v=((f_n)_Y(P),(f_n)_X(P)).

We now check the Taylor-gap hypothesis of R6A on this ACTUAL line. For
ANY a,c in K the polynomial identity

    (a+cT)^n=(a+cT)(a^q+c^q T^q)^ell                       (4)

shows that no exponent 2,3,...,q-1 occurs. This follows from q being a
power of two. It remains true if a or c is zero. Apply (4) separately
to X=a+v1*T, Y=b+v2*T, the constant coordinate Z=1, and
W=a+b+1+(v1+v2)T. Addition preserves the missing coefficients. Thus
f_n on the tangent line has precisely the gap required by R6A. Its
constant and linear terms are zero at the chosen smooth tangent point.

Dehomogenizing h gives an irreducible affine polynomial whose degree is
at most e and whose line restriction is nonzero. The complementary
factor is a unit at P by (3). Applying R6A, or its identical univariate
order proof with the degree upper bound e, gives

    deg(h)>=q.                                              (R6B)

No equality n≡1 modulo a finite-field multiplicative order was used to
substitute a polynomial function for a polynomial. Every restriction is
an exact identity in K[T]. The point P avoids all other components
automatically by (3). The tangent line cannot be h itself because e>=2.
It cannot be a different component of f_n passing through P because the
other-factor value J(P) is nonzero. There is no missing infinity case:
a nonlinear projective component always meets the chosen affine chart.

One may also view this through the q-th-power gradient ratios in (2).
On the function field of h their ratios are q-th powers; Euler then
expresses y=x A^q+B^q in a suitable chart, giving tangent contact at least
q. This is an alternative explanation, NOT an imported Gauss-map theorem
or an additional premise. The direct proof (3)-(4) needs no function-field
separability hypothesis at all.

## 4. A general factor-degree consequence (R6C)

Assume in addition that n has binary weight at least three. Accepted T1
excludes EVERY absolute line of phi_n. Thus R6B applies to each of its
absolute irreducible factors, not just to those through a particular
singular point. If r is the number of those distinct components, then

    r*q <= deg(phi_n)=ell*q-2,
    r <= ell-1.                                             (5)

Reducedness was proved in Section2, so no uncounted multiplicity is hidden
here. Every actual nonconstant divisor U of phi_n over K, irreducible or
a product, has degree at least q, since it contains at least one such
component. Consequently

    0<deg(U)<q is impossible for an ACTUAL divisor U.         (6)

The same lower bound holds for a nonconstant F2 factor. It is not a
claim that every component is F2-defined, or that arbitrary formal
invariant polynomials with these degrees are actual divisors. No central
point incidence, fixed field or stabilizer hypothesis is imposed by (5).

At n=3, phi_3=1 has no positive-degree factors, so the selected-component
statement is vacuous. n=1 is excluded from R6B because f_1=0 and v2(0)
is undefined. For binary weight two, T1 is not available; Gold examples
have line components and must not be inserted in (5)-(6). R6B's bound on
NONLINEAR components still has its stated meaning in that domain. At
q=2 the lower bound is only two; no whole-sector irreducibility follows
from it alone. These are boundaries, not investigations of preliminary(a).

## 5. Excluding every bounded smaller factor (R6D)

Now fix Q=2^s,s>=3,k>=2, and put

    ell=Q-1, q=Q^k, n=ell*q+1,
    N=ell*q-2, A=(ell-2)(ell+1)=Q(Q-3).

The exponent n has exactly s+1 set bits: s consecutive ones from the
shifted Q-1, and the separate bit zero. Hence its binary weight is at
least four, and accepted T1 applies. The power q is exactly
2^v2(n-1), since ell is odd.

The relevant size comparisons are strict and hold for EVERY parameter:

    q>=Q^2>2Q+5=2ell+7,
    0<A=Q(Q-3)<Q^2<=q.                                    (7)

Suppose phi_n were reducible over K. Its degree N is positive. Choose an
absolute irreducible component h of least degree e. Since there are at
least two components, 0<e<=N/2. It is an ACTUAL proper factor, and is
reduced by Section2. Thus accepted R4A gives

    e<A.                                                   (8)

But T1 and R6B give e>=q, while (7)-(8) give e<q, a contradiction.
Therefore the WHOLE phi_n is absolutely irreducible, proving R6D.

This proof deliberately uses the universally quantified smaller-factor
conclusion R4A. It does not require the additional grouping step or the
unique-component descent of R4B. Equivalently, where one does use R4B,
its ACTUAL complementary cofactor H has degree below A<q and (6) forces
H to be a unit. These are two presentations of the same contradiction,
not a claim that any proposed invariant polynomial can be inserted as H.

For the alternative R4B presentation, its remaining size condition is
also satisfied:

    N-(3A-2)>=(Q-1)Q^2-3Q(Q-3)
              =Q(Q^2-4Q+9)>0.

That check is not needed to invoke R4A and is not an extra premise of
the main proof. Neither D-divisibility nor an assumed uniform Frobenius
orbit, common fixed point, cofactor coefficient field or prime value of
s has entered (7)-(8).

## 6. Official consequence and what remains open

For this family phi_n is a nonconstant absolutely irreducible polynomial
over F2. If the official coefficientwise identity supplied nonconstant
modulo-two g,h, reducing their coefficients would give phi_n=bar(g)bar(h)
with two positive-degree polynomials over F2, contradicting absolute
irreducibility. This conclusion allows nonhomogeneous g,h as in the
official wording; absolute irreducibility already forbids any such
polynomial factorization. It does not rely on finite-field evaluation.

The proposed theorem subsumes only within its stated family the older
accepted Q8, Q16, Q32 and k>=3 exclusions. It does not change their proofs,
repair historical R5 errors, or silently widen their accepted statements.
The additional parameter range includes the remaining k=2 values for
all s>=3, including composite s. It says nothing about arbitrary odd n,
other ell, s<3, or general k=1 (which includes the distinct Kasami case).
The annual reducibility classification remains open.

The source-led exploration first pursued tangent-orbit divisibility and
the classical degree2/3/4 invariant ring. Those routes did not produce
the final contradiction. Their exact limits are preserved in the separate
failed-routes and worklog files. No such auxiliary calculation is used
as an undeclared lemma here. The generic contact argument is classical
in nature; no claim of a novel geometric method or first publication is
made. Férard2017's full theorem remains an explicit access/read limit.

## 7. Audit and integrity boundary

The full obligations, constructor checks, failed routes, source/read
limits, worklog, no-math-code record and compact immutable-parent/input
metadata are part of this submission. The freezer performs byte/JSON
checks only; it does not test the theorem or rerun old computations.
No CAS, finite-field scan, factor table, optimizer, mathematical Python
test, source executable or author certificate is used. No old file,
shared dashboard, cache, Git history or other worker's record is edited.

Only root may promote after TWO OTHER complete initially blind WHOLE
audits and full reconciliation. The constructor is excluded, and accepted
old-input authorship/review roles must be disclosed separately by later
reviewers. This frozen candidate is not an announcement of a full answer,
external validation, established priority or absolute certainty.
