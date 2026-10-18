# R7: OTHER initially blind ENTIRE WHOLE review 2

18 October 2026 UTC. Reviewer A, `/root/review_2021_reasoning_j15_r2`.
This is a complete nonconstructor audit of the frozen R7A–R7D submission,
not an extension-only check. The constructor is C. Root gave the generic
assignment, not a new proof inference. Requested inherited settings are
gpt-6.1-sol / max; independent effective-setting readback is unavailable.

**Disposition:** all 64 obligations pass. I found no substantive defect and
require no author repair. I recommend only the exact R7A–R7D scope below,
subject to root's reconciliation of TWO OTHER whole audits. This review is
not an acceptance, annual classification, novelty claim or external validation.
Nine closed scope/source notes are recorded separately.

This mathematical disposition is frozen before release. Through the entire
initial freeze, final readback and separate verification I have not accessed
ANY corresponding NEW root R7 review finding, file, source, code, hash,
metadata, user commentary or thread material. No new peer conclusion was
received. Identity-only handoff precedes explicit BOTH confirmation.

## Input and role boundary

The target is `notes/reasoning-cofactor-return-r7-candidate-v1.md`, 17331
bytes, SHA256
`f8afed9064dcc6445c3e6bb05102ecb1c1420c3da0ad6bdf9ef7db4f28c4b05e`.
The author freeze is 3129 bytes, SHA256
`18d2a87ffb4f0f7ca2140659a0883f697974620ba507453fdfda01b8cff49cd1`.
I read all 13 author files, including all 64 obligations, notebook, failed
routes, source MD/JSON, administrative code and every metadata file. I did
not execute the author code, old computations, source programs or certificates.

I freshly read the complete accepted T1–T4 body and authority MD/JSON, and
the complete accepted R6A–R6D body and authority MD/JSON. T1 is the operative
line exclusion. R6 reducedness is also reconstructed explicitly in the new
submission and here. I separately read the current R4, corrected R5 and
three-bit-r2 authority MD/JSON as context. Their complete bodies were read
in my earlier assigned audits; I do not claim a fresh whole reading of
those context-only bodies in this R7 audit. They supply no new R7 premise.

My old construction roles include accepted T1–T4 and C7/C11. My previous
CP WHOLE2/GK and S3/NF/R4/R5/R6 review roles are separately disclosed.
I did not construct or supply the NEW R7 root-field criterion,
jets, auxiliary four-solution obstruction or final assembly. Reading an
accepted input that I previously constructed does not newly independently
recertify it. Its prior two OTHER audits remain the authority.

## Exact result and official question

Let K be the algebraic closure of F2, W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X), and
use the already established polynomial quotient phi_n=f_n/R. For every
odd ell>=3 and i>=2, put q=2^i, n=ell*q+1 and m=ord_ell(2). The asserted
criterion is

    gcd(i,m)=1  ==>  the WHOLE phi_n is absolutely irreducible.

R7B confines intersections of distinct absolute components to P=(1:1:1).
R7C supplies the contradiction there. R7D specializes ell=2^s-1 with
s>=2 and gcd(i,s)=1. Taking i=2 and odd s>=3 gives n=2^(s+2)-3 and
binary weight s+1. These quantifiers do not assume ell prime.

The local official normalization and fresh official Paper B, page 2,
B4 setup and (b), agree: the target is coefficientwise reduction of
integer polynomials, both nonconstant modulo two. Absolute irreducibility
of the whole nonconstant quotient excludes any such product. A theorem
about one F2-defined component alone would not do so. I do not solve,
derive or reproduce preliminary (a).

## 1. Basic algebra, reducedness and possible intersections

The odd ell is invertible modulo 2, so its multiplicative order m exists;
ell divides 2^m-1, putting every ellth root of unity in E=F_(2^m).
Order one would force ell|1, hence m>=2. The common fixed field of the
i-th and m-th Frobenius powers is F_(2^gcd(i,m))=F2. This is valid for
composite ell. Also q is exactly the maximal two-power in n-1, and
wt(n)=wt(ell)+1>=3. T1 therefore excludes every absolute line.

The monomial X^(n-1)Y occurs in f_n with coefficient one, so f_n is
nonzero. Its three partials are (X^ell+W^ell)^q and their Y,Z analogues.
Their common projective zero set is finite: W=0 would force every
coordinate zero; after W=1 each coordinate is an ellth root. If an
irreducible factor repeated in f_n, the product rule would put its whole
curve inside that finite gradient locus, including an even multiplicity
in characteristic two. A positive-degree projective curve over the
infinite algebraically closed field has infinitely many points. Hence
f_n and phi_n are reduced. This is the old R6B inference with all its
hypotheses matched, rather than a new unqualified squarefreeness assumption.

If two actual factors of phi_n vanish at Q, all partials of phi_n vanish
at Q. Product differentiation of f_n=R*phi_n implies f_n and its affine
partials vanish too, whether or not R(Q)=0. In the chart Z=1 write
Q=(a:b:1), l=a+b+1. Injectivity of q-th powers gives
a^ell=b^ell=l^ell=u. Evaluating the actual numerator gives
0=(a+b+l)u^q+1=u^q+1. Thus u=1, and a,b,l are nonzero elements of E.
The use of f_n=0 is necessary; the derivative equations alone do not
give u=1.

There is no omitted meeting at infinity. At Z=0, R!=0 implies X+Y!=0,
so (f_n)_Z=(X+Y)^(n-1)!=0. On phi_n=0 this makes the quotient smooth.
The three points where also R=0 are (1:0:0), (0:1:0), (1:1:0). At
the first use the Y derivative; at the last use the X derivative;
the derivative of f_n and of R both equal one. Coordinate symmetry
handles the remaining point. Thus phi_n=1 there, so none is on the curve.
This checks a homogeneous derivative, rather than presuming that the
affine X,Y test covers infinity.

Every possible intersection is now P, a noncentral diagonal root point,
or an affine off-diagonal point with a^ell=b^ell=l^ell=1. This describes
potential factor intersections, not an assumption that all singularities
are nodes or that all components pass P.

## 2. The local product test and the three diagonals

For a polynomial G with initial form c*L^t, c!=0 and t>=2, a product
G=UV with both factors vanishing has initial forms a*L^r, b*L^s for
r,s>=1, r+s=t. Its term of degree t+1 is
a*L^r V_(s+1)+b*L^s U_(r+1), divisible by L. Therefore a next term
not divisible by L rules out simultaneous vanishing. If a next term
is missing it is zero and gives no such exclusion. A local unit only
adds a multiple of L^t to the next term; it preserves the test. This
does not assert global irreducibility of a germ merely because it has
one tangent.

On the representative diagonal point (b:1:1), b^ell=1 and b!=1,
the finite-field intersection makes b not in F_q. Put c=b+1,
E0=b^-q and B0=1+b^(1-q). All necessary denominators and B0 are
nonzero. After X=b+x, Y=1+y, Z=1, independent expansion of
(a+x)^n=(a+x)(a^q+x^q)^ell gives

    F_q=B0*y^q,
    F_(q+1)=E0*x^q*y+E0*x*y^q+(1+E0)*y^(q+1).

The positive-degree terms below q vanish by the singular-point equations.
The exact denominator is

    R=c^2*y+c*y^2+x^2*y+x*y^2.

Dividing by its simple y factor gives the quotient's order q-1 and
initial form (B0/c^2)y^(q-1). At the next degree its x^q coefficient
is E0/c^2, which is nonzero. More explicitly the whole next form is

    (E0/c^2)x^q+(E0/c^2)x*y^(q-1)
       +((1+E0)/c^2+B0/c^3)y^q.

In the product calculation only the degree-two term c*y^2 can affect
this degree; the degree-three terms do not. The local product test
applies since q>=4. It excludes two global factors vanishing here.
All three diagonals follow by the actual coordinate-permutation symmetry.
I checked plane multiplicity q-1 separately from line-contact order.

## 3. Off-diagonal identity, auxiliary field theorem and unit correction

At an off-diagonal potential meeting, a,b,1,l are four DISTINCT nonzero
elements of E: any equality reduces to a=b, a=1 or b=1 and hence R=0.
Let A,B be the unique q-th roots in K defined by

    A^q=a^(1-q)+l^(1-q),  B^q=b^(1-q)+l^(1-q).

The local numerator has initial forms

    F_q=(A*x+B*y)^q,
    F_(q+1)=a^-q*x^(q+1)+b^-q*y^(q+1)+l^-q*(x+y)^(q+1).

If A=B=0, the ratios a/l,b/l lie in F_q. Their sum with 1 is 1/l,
so a,b,l also lie in F_q. Their membership in E then forces a=b=l=1,
contradicting the off-diagonal hypothesis. Thus L=A*x+B*y is nonzero,
and (B,A) is a nonzero direction on L=0. No division by A, B or A+B
is legitimate or needed; individual zero values are harmless.

Here is my independent expansion of the key scalar. Clear the nonzero
denominator D=a^q*b^q*l^q in F_(q+1)(B,A), expand (A+B)^(q+1), and
replace A^q,B^q by their definitions. The coefficient of B is

    b*l^q+l*b^q+a*b^q+b*a^q
      = b*(a+l)^q+(a+l)*b^q = b+b^q,

because a+l=b+1. The coefficient of A is a+a^q. Thus

    D*F_(q+1)(B,A)=T=B*(b+b^q)+A*(a+a^q).

Raising to the q-th power, the terms contributed by b^(1-q) and
a^(1-q) are b+b^(q^2-q+1) and a+a^(q^2-q+1). The remaining terms
combine to l^(1-q)*[(a+b)^q+(a+b)^(q^2)]. Since a+b=l+1, this is
l+l^(q^2-q+1). Therefore, for d=q^2-q+1,

    T^q=1+a^d+b^d+l^d.

This derivation does not put q^2=1 on E. Frobenius is applied to field
elements at an actual singular point, while the jets above are exact
polynomial expansions over K.

The published Kasami APN theorem applies on E because gcd(i,m)=1.
Its conclusion used here is only that, for c0!=0, z^d+(z+c0)^d=t
has at most two E-solutions. If needed, reduce i to its positive residue
modulo m; it is nonzero, and the positive monomial function agrees also
at zero. If T=0, c0=a+b=1+l is nonzero and a,b,1,l are four distinct
solutions of the SAME equation with t=a^d+b^d, contradiction.
Consequently F_(q+1)(B,A)!=0, so L does not divide F_(q+1).

I freshly read the operative primary proof in Carlet–Kim–Mesnager,
including the complete odd-dimensional argument, Lemma4 and the FIRST
complete even-dimensional argument with Lemma5. The even proof has no
restriction excluding field degrees divisible by six: its coprimality
makes the exponent parameter odd. The later unfinished alternative
discussion is not used. The underlying original proofs cited for
Lemmas4/5 were not freshly audited; this remains an attributed published
theorem import, not a self-contained new proof of APN-ness.

Finally at R0!=0, the quotient's degree q+1 term is
F_(q+1)/R0+R1*F_q/R0^2. The correction vanishes on L=0 because it is
divisible by L^q. The local product test therefore excludes an off-diagonal
meeting of two factors. It is not permissible to transfer every Taylor
coefficient through an arbitrary unit without this calculation. Together
with the diagonal and infinity checks this proves exactly R7B.

## 4. Central cone and whole-polynomial conclusion

At P the degree q part of f_n vanishes and its degree q+1 part is
x^q*y+x*y^q. Dividing the exact local denominator x*y*(x+y) gives

    C=(x^(q-1)+y^(q-1))/(x+y)
      = product_(alpha in F_q minus F2)(x+alpha*y).

There are q-2 distinct factors, none x or y. In particular the root
alpha=1 is removed once; alpha=0 was never a root. The odd exponent
q-1 makes all roots simple. Hence the central order is exactly q-2.

If the reduced homogeneous phi_n were reducible over K, partition its
actual absolute components into two nonempty sets U,V. They have positive
degrees a0,b0 and no common component. Let r=m_P(U), s=m_P(V), allowing
zero. Their initial forms partition C. If both vanish, the tangent cones
are coprime; the local intersection formula gives I(P,U,V)=r*s. If one
is a unit, I=0=r*s instead. R7B and the separate infinity check say there
is no other contribution. Projective Bézout gives a0*b0=r*s.

For every positive-degree homogeneous divisor H of phi_n, however,
m_P(H)<deg(H). Indeed equality after moving P to (0:0:1) would leave
only monomials whose X,Y-degree equals deg(H), making H a homogeneous
binary form independent of Z. It splits into linear forms over K and
would give an absolute line factor of phi_n, prohibited by T1. This
argument covers reducible H and factors with zero order at P. Applying
it to U,V gives a0*b0>r*s, including r*s=0. This contradicts Bézout and
proves R7A/R7C. There is no premise that all components pass P, no
irreducible genus formula on a product and no ordinary-point assumption
at any noncentral singularity.

The exact imported intersection hypotheses were freshly checked in
Fulton's entire operative Sections3.3 theorem proof and5.3 Bézout proof:
proper local intersection and coprime tangent cones for equality, and
projective curves without a common component for the global formula.
The algebraic proofs apply to reducible U,V over K in characteristic2.
Appendix A's separate nonzero-characteristic warnings do not restrict
these results. I do not claim an audit of the whole book.

## 5. Consequences and adversarial endpoints

For ell=2^s-1 the order is exactly s: no positive t<s can have ell
dividing the smaller positive integer 2^t-1. Thus R7D follows for
EVERY s>=2, not only prime s. With i=2, odd s>=3 gives
(2^s-1)*4+1=2^(s+2)-3 and wt=s+1. The symbolic proof suffices;
examples n29,n113 are arithmetic illustrations, not finite evidence.

I challenged the following possible extensions and retained the stated
boundaries. At ell3,i2,n13 the gcd is two, so the criterion says nothing;
the old ordinary-F2 irreducibility result there is not falsely upgraded
to absolute irreducibility. For ell3 and odd i>=3 the criterion is in
its domain and overlaps old three-bit results. At i1 the present proof
is not claimed; q2 would give a zero-degree central cone and needs its
separate published sector. At ell1 the line exclusion is unavailable.
n1 is a zero numerator and n3 a unit quotient, both outside the theorem.
Composite ell, even m, m divisible by six, i larger than m, A=0 or B=0,
and factors avoiding P introduce no omitted division or quantifier.

The old R6 family has i=s*k and s>=3, so gcd(i,s)=s>1; it does not
follow from this criterion. R4/R5 bounds and an F2-descended small
cofactor are not used. Failure of the gcd condition is a failure of
this proof, not a reducibility theorem. The unread Férard2017 operative
body prevents a nonoverlap or priority claim. Neither a finite-field
function calculation nor APN-ness of the TARGET exponent n is substituted
for whole-polynomial irreducibility.

## 6. Completion and preservation

The independent per-inference ledger covers all64 labels in order. All
adversarial notes are closed scope/source reminders, not unresolved
objections. No mathematical executable, CAS, scan, test or author/source
rerun was used. The only new executable records byte/JSON/label integrity.
No frozen author, old proof, shared dashboard, cache or Git file was
edited. Compact provenance binds the exact author packet, operative
accepted bodies/current authorities and immutable immediate own parent
without copying a growing historical inventory.

Own direct authoritative usage at13:52:58UTC was40%TOTAL,10080minutes,
reset1792874445, ordinaryUsageAllowed=true, legacy/by-limit readings
agreeing. This is the explicitly authorized existing window only, with
a90%TOTAL ceiling and integration reserve. Final completion identity is
recorded by the manifest; FULL final model readback and a later SEPARATE
read-only verification must both precede handoff. Findings remain
embargoed until root explicitly confirms BOTH entire independent freezes.
