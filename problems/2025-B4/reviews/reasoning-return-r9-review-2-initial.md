# R9A--R9F: complete initially blind WHOLE R2

18 October2026 UTC. Reviewer B, `/root/review_2022_complexity_r2`.
**Candidate proof - unverified.** This is the complete original-v1
initial audit, not coordinator acceptance or an audit of a later version.

I reconstructed all SIX claims, all48 obligations, all eleven constructor
files and the operative accepted/primary-source interfaces. The new
small-coordinate construction, both correctly costed norm branches,
overlap valuations and finite2 construction passed. **One auxiliary
boundary sentence is false as quantified**: the unit witnesses in the
rational counterexample are inside the box only when R>=1, whereas the
section allows every0<R<H. This does not invalidate the actual
R=sqrt(H) counterexample, but it requires an author correction in a
versioned record. I also retain a precise scope note on the model:
nonlinearity of the CHOSEN a_0^p is proved; absence of EVERY linear
generator of its ideal is not. The latter is not silently inferred here.

Exact target: `notes/reasoning-return-r9-candidate-v1.md`,22574bytes,
SHA256 `8fae8c0dd3e951fd4c847954f75186b8969f1dbdec9592b8cebcbda8394a9aa2`.
Exact constructor freeze:2790bytes,
SHA256 `93eed518f1584c8e4f1a7cbe4d6229c9532caae4269d18cf0393c1f0e934aa8f`.
C is sole NEW constructor. Root supplied only a broad assignment and
is the OTHER new whole auditor. I received a coordinator completion
identity without findings, but opened NO NEW root R9 report, ledger,
source record, manifest, metadata file or conclusion through this
ENTIRE initial freeze. No later constructor version was read.

## 1. Official scope, accepted premises and old roles

The actual official2025 PaperB page2(b) asks for all INTEGER x,y,n,q,
n,q>=2 in the geometric-sum equation. The present arithmetic sector
has n=p-1,q=p, p>=37 PRIME, |X|>=2. Both signs of X are retained;
G_p(X)>1 and p odd force Y>1. This is a very restricted diagonal
sector, not the whole annual problem. No preliminary(a), special
boundary classification, other term count or off-diagonal theorem is
reproduced as a solution.

The COMPLETE accepted R8 body28730bytes/SHA
`f00a2b2816f128df54060fd800cba83d726abf07303c1cc7c92688a61557ca15`
was read, including its acceptance header, actual transported real
phase equations, general Wronskian proof and BOTH evaluation branches.
I authored that OLD R8 and UW work; their accepted authorities came
from OTHER whole auditors. Reading them now is NOT independent
self-recertification or a claim that I constructed NEW R9. I also
reviewed OLD R6/R7. Their current scopes remain explicit.

The accepted R6 body28748bytes/SHA
`4e157819789da12d6f26e89929d88ec886d52947405d836fe3957ab8ee727d3a`
was freshly read in the exact opening/convention/phase and operative
Section5 scopes, with both acceptance JSONs read fully. Later unrelated
R6 height sections were not newly whole-audited. The new half-weight
extension is reconstructed below from its matched-prime Jacobi input.

Let m=(p-1)/2, q_p=ceil((p-4)/30). Accepted R8 supplies q_p free
nonconjugate ACTUAL positive original-weight I_f orbits, coefficients
0/1/2, complement2N and nonzero inverse first moment. Arbitrary
half-orbits give q_p m columns and2q_p m distinct canonical vectors
after adjoining their j-conjugates. R9A/B need q_p>=32; R9C--F do
not acquire that extra threshold. Direct sigma_a means zeta->zeta^a;
F uses a and M_r uses a^-r. These distinct index conventions are kept.

## 2. R9A: the actual real integral matrix

The accepted pulled-back real rows, for m representatives of a modulo
sign and k0,1, are trace expressions in ell_v tau_(a,v) J_(v,k).
Here tau is the ACTUAL root-of-unity phase, even in a; J_0=1 and
J_1=-sum_c n_(v,c)zeta^c. The pullback transports coefficients too.
One cannot hold ell fixed under Galois action and discard its transport,
or replace these rows by the stronger complex system. The new counting
argument is performed on exactly these actual real equations.

### 2.1 Integral basis and entry bounds

For h1..m let t_h=zeta^h+zeta^-h. Represent an integral real element
at powers0..p-1 with integer coefficients. Subtract its conjugate:
the resulting vector represents zero and therefore is a multiple of
the all-one vector, the only relation of degree<=p-1. Its coordinate0
is zero, forcing that multiple zero. Hence the representation is
symmetric. It is an integer combination of1 and the t_h, and
1=-sum_h t_h removes1 without dividing by2. Conversely a zero
integer combination of the t_h has constant coefficient0, so a
multiple of Phi_p must be zero. They are a Z-basis of O intersect
Kplus, not merely a rational basis with an unrecorded denominator.

Indices are reduced modulo p and sign, and t_0=2=-2sum_h t_h.
The product identity t_u t_h=t_(u+h)+t_(u-h) follows directly by
multiplying roots of unity. For a k0 entry, a trace is t_d; multiplying
by t_h gives coefficients bounded by2, including d0 and a t_0 term.

At k1 the trace entry is -sum_c n_c t_(c+d), or with d shifted by1
for the second real coordinate. Multiplication by t_h gives

    -sum_c n_c[t_(c+d+h)+t_(c+d-h)].

For each nonzero folded index r there are at most FOUR contributing
c occurrences, each coefficient0..2, so its negative contribution lies
in[-8,0]. A t_0 term can come only from c=-d-h or -d+h; its total
negative coefficient lies in[-4,0]. Replacing t_0 by-2sum t_r adds
one common number in[0,8] to every basis coefficient. The final
range is[-8,8]. Coincident indices are counted with multiplicity and
do not produce a fifth term; n_0=0 only removes terms. Thus the bound
is independent of the actual phase exponent, p and X. An archimedean
bound is not being substituted for an integral-coordinate bound.

Write ell_v=a_v+zeta b_v with a_v,b_v in Kplus and expand both in
this integral basis. There are U=2q_p m² integer unknowns. The at most
2m real-field equations each have m rational coordinates, giving at
most V=2m² integer equations. In particular U=q_p V for this upper
choice of V, even if the actual rank/number of nonzero rows is smaller.

### 2.2 Strict pigeonhole inequality and height

The images of2^U binary vectors have each coordinate in the inclusive
integer interval[-8U,8U], so there are at most(16U+1)^V images.
The sufficient strict inequality2^q_p>16U+1 gives a collision and a
nonzero difference with every coordinate in{-1,0,1}. A rank hypothesis
or solution-independent phase choice is not required.

From the ceiling definition p<=30q_p+4, hence m<=16q_p for q_p>=2,
and U<=512q_p³. At q_p32 one has
8192q_p³+1=2^28+1<2^32. The inequality
(1+1/q_p)^3<2 then preserves the strict estimate under q_p->q_p+1,
including the added1. Thus q_p>=32 suffices. Prime p>=937 is a
sufficient threshold; it is not represented as optimal.

Every conjugate of a_v or b_v has modulus<=2m. Therefore each ell_v
has every-conjugate modulus<=4m, and the q_p m-column sum is at most
A=4q_p m². Nonzero coordinates cannot all give ell_v0, because
1,zeta are linearly independent over the real field. All coefficients
are algebraic integers. The vector is actual-signature dependent and
may use ALL columns. It is not guaranteed to leave an evaluated
equality subspace. R9A passed within this exact scope.

## 3. R9B: nonzero and zero evaluation with dense support

The coefficient bound and two canceled actual orders fit the accepted
R8 analytic proof without change. At every real embedding,

    |sigma_a(delta)|<=4A |X|^(-1-1/p),
    delta=sum ell_v beta_v+j(sum ell_v beta_v) in O intersect Kplus.

If delta!=0, its real-field norm is a nonzero integer. Multiplication
over the m embeddings gives

    |X|<=(4A)^(p/(p+1))=(16q_p m²)^(p/(p+1))<16q_p m².

Every embedding is needed; a single small conjugate would not suffice.
This is explicitly CONDITIONAL on evaluated nonzero delta.

For the other branch, selected canonical vectors and their j-conjugates
are distinct modulo p, and monodromy/finite character averaging from
accepted R8 gives a nonzero formal constant combination H. It does not
give H(1/X)!=0. The number of active functions can be as large as
n_*=2q_p m: the previous sparse-cofactor bound2(R_2+1) is not assigned
to this dense pigeonhole vector. The GENERAL Wronskian argument has
numerator degree at most(p-2)nfun(nfun-1)/2 and first order at most
that degree+nfun-1. Its proof does not rely on sparse support, so a
nonzero coefficient h_t occurs with

    2<=t<=T_*=(p-2)n_*(n_*-1)/2+n_*-1.

The actual integral coefficient witness is rho=p^t t!h_t, with EVERY
conjugate bounded by H_t=2A p^t t!. This follows from every-order
binomial integrality and coefficient majorants, not division of a
factorial modulo p. Its norm gives
|h_t|>=(p^t t!)^-1 H_t^(-(m-1)). When delta0, the geometric analytic
tail at signed real1/X gives |h_t|<=4A/|X|. Combining these yields

    |X|<=2 H_t^m<=2[2A p^T_* T_*!]^m.

Negative X only changes alternating signs and |X|2 is inside the
convergent domain. The full factorial/support cost remains; this is
not a useful new unconditional improvement or Diophantine exclusion.
R9B passed BOTH branches, not just the favorable one.

## 4. Actual characteristic ideal and the new half-weight lift

Under the actual signed equation, accepted R6's e0 result supplies
p not dividing X-1. The conjugates of alpha=X-zeta have pairwise
coprime ideals: a common prime would divide a root difference and
therefore lie above p, already excluded. A prime dividing alpha has
residue zeta equal to the ordinary integer X. It has order p and
residue field F_ell, so ell1modp and splits completely. The norm
G_p(X)=Y^p forces all exponents to be multiples of p. Thus
(alpha)=A^p, Norm A=Y>1; A and all its conjugates are nonunit and
pairwise coprime. This uses actual A, not a formal residue controller.

For both parities and both signs of X, G_p(X) is odd. Consequently
Y is odd; in fact its rational prime factors are1modp, as used in the
Jacobi normalization. For a binary half psi, the classical matched
character can be chosen at EACH prime L of A, so the minus-normalized
Jacobi sum has ideal L^psi, all conjugate moduli sqrt(ell), and value
1modlambda². The operative primary formula in the2008 author text
was freshly inspected, including its inverse index and sign convention.

Multiplying to the actual valuations of A constructs b_psi in O
with ideal A^psi, all conjugate moduli sqrt(Y), hence
b_psi*j(b_psi)=Y, and b_psi1modlambda². Any two generators with the
SAME ideal AND these moduli have a quotient which is an integral unit
with all conjugates on the unit circle. Kronecker makes it +/-zeta^h,
and the common lambda² normalization makes it1. This is the valid
same-ideal use of Kronecker; it is not the invalid quotient in R9D.

Uniqueness proves G-equivariance and multiplicativity for generated
elements. In particular beta_N=b_psi*j(b_psi)=Y. Negative integer
Jacobi powers are allowed at an intermediate fraction-product stage;
positivity of the FINAL exponent ideal gives integrality, as in R6.
For positive theta in the generated group with complement2kN,F0,
k1 or3, beta_theta^p and alpha^theta have the same ideal and all
conjugate moduli Y^(kp). Their quotient is a root of unity. Writing
r=X-1, a local lambda-unit, one has

    alpha^theta = r^(k(p-1))[1+(lambda/r)F(theta)] =1 modlambda².

Fermat's congruence for signed r and F0 justify this formula; the
integer linear sum is a multiple of p before reduction. beta_theta^p
is also1modlambda², so the root of unity is1. This proves the required
pth-power identity for k1,3 without a generalized e1 theorem.

## 5. R9C: rational avoidance example and the boundary correction

W'' has14 independent rows: e1+H e2 and e3..e15. Adding e1 gives
rank15. Its two rational orthogonals are exactly

    S': w1+H w2=0, w3=...=w15=0,
    S:  w1=...=w15=0.

For ANY real0<R<H, an integer point in the S' box has |w1|<H,
so w2=0 and w1=0. Therefore equation(16), equality of the two SHORT
integer-point sets, is correct. In particular no such point escapes S.

The next sentence, however, says that both short sets contain e16
throughout that stated R range. This is false when R<1. The exact
certificate H2,d17,R1/2 makes the entire integer cube contain only
zero, whereas ||e16||=1. The same lower threshold is needed when
calling a unit witness a vector in a perturbed R-box. This is issue
R9R2-01. It is a localized auxiliary boundary correction, not a failure
of the intended R=sqrt(H)>1 construction; the latter is explicitly
present in the candidate and remains a valid counterexample.

For the asserted perturbations add e1+e_j to W'', j>=16. The new
kernel also has w1+w_j0. Every short point therefore has w1=w2=w_j0.
When R>=1, it contains e_k for some k>=16,k!=j; d>=17 ensures such
a k exists. Thus, at the chosen R=sqrt(H), all these homogeneous
systems have a nonzero unit vector, while S' has no short escape
from S. This is rational linear-algebra data, not a claimed actual
Jacobi signature or a counterexample to the Diophantine equation.
At R=H a vector(-H,1,0,...) escapes, explaining the strict upper
threshold. No claim about a particular published quantitative bound
at every d,H is needed for this generic obstruction.

The replacement signed-minor argument is valid. If A_0 has rank r
and b is outside its rational row space, select r+1 columns where the
augmented determinant is nonzero. Deleted-column r-minors of A_0
form a kernel vector by repeated-row determinant expansion, and b z
is that nonzero augmented determinant. The r! permutation estimate
gives ||z||_infinity<=r!B^r. Rank r0 uses the empty determinant1
at a nonzero coordinate of b. This supplies an avoidance estimate,
with its full cost, not a first-minimum estimate disguised as escape.

Fukshansky's actual Theorem1.2/sharpness discussion was read. It
separates avoiding lower-dimensional spaces from finding one small
nonzero vector and retains subspace-height costs. The new example and
minor proof do not depend on importing its quantitative theorem or an
unread Bombieri--Vaaler proof. Apart from R9R2-01, R9C's intended
counterexample and safe replacement passed.

## 6. R9D: overlap valuation and the failed integral-unit shortcut

Each binary half support has m elements. Two such supports are
disjoint exactly when their union is allG, equivalently psi1+psi2=N.
Thus a noncomplementary pair overlaps. A selected original-weight
element with M1nonzero cannot equal N, whose inverse first moment is0.

Choose an overlapping DIRECT index a and a prime Q of sigma_a A.
Let e=v_Q(sigma_a A)>0. Pairwise coprimality of the characteristic
conjugates yields

    v_Q(b1)=v_Q(b2)=e, v_Q(Y)=e.

The last equality follows from(Y)=product_sigma sigma A. If D is a
nonzero rational integer coprime to Y and b1b2-Y=D chi with chi
integral, the two left terms have valuations2e and e. Their difference
therefore has valuation EXACTLY e, not merely at least e. D is a unit
at Q, so v_Q(chi)=e and v_Q(chi/(b1b2))=-e.

Nevertheless each b_i separately divides chi: b_i divides Y because
Y/b_i=j b_i is integral; it also divides b1b2 and is coprime to D.
The invalid inference is multiplying those two noncoprime divisibilities.
The equality1-D chi/(b1b2)=Y/(b1b2) does have every conjugate
modulus1, but the right side has a pole at Q. It is not an integral
unit, so Kronecker does not apply. Requiring the two half ideals to
be coprime forces complementary supports, product Y and zero M1,
which discards the selected nontrivial original-weight element.

The actual current source v4 Lemma5 exposes this product step; the
version was checked directly. R9D proves a conditional valuation
obstruction under characteristic-ideal data, not existence of a
hypothetical solution and not falsity of a source's final nonexistence
theorem. Those quantifiers are essential. R9D passed in that scope.

## 7. R9E: actual weight6 finite2 equality and its original-weight limit

The specified psi has coefficients at sigma_(c^-1) for c=m+1..p-1,
the actual psi(1,1). With DIRECT indices its inverse first moment is
the SUM of c, not their inverses. Modp this is
-m(m+1)/2=1/8, since m(m+1)=-1/4. It is nonzero.

Theta=2 sigma2 psi+4 jpsi has canonical coefficients0,2,4,6,<p,
is positive in I and satisfies

    Theta+jTheta=6N,
    F(Theta)=2*2 F(psi)+4*(-F(psi))=0,
    M1(Theta)=2*(1/2)M1(psi)-4 M1(psi)=-3/8 !=0.

Its augmentation is3(p-1), source relative weight6 and source J-index3.
The source's exact J3 definition is met, with3<=m. Nonzero M1
excludes a p/norm-element reduction and forces a free G-orbit; it
does not turn weight6 into original weight.

For EVERY u in O, reducing coefficients modulo2 gives
sigma2 u=u²mod2O. No splitting of2 is assumed. The uniquely normalized
half lift therefore gives

    beta_Theta=(sigma2 b)^2(jb)^4
        =b^4(jb)^4=Y^4=1 mod2O.

Every G-conjugate satisfies the same congruence. If X is even choose
w=X; otherwise choose w=X-1. |X|>=2 makes w nonzero and even.
Removing its p-part preserves those properties since p is odd.
Each ideal(w',beta_Theta-sigma beta_Theta) is contained in(2) and
contains(w'). Their finite intersection is nonzero, contained in(2)
and proper. Thus(2) DIVIDES the equality ideal; the reverse inclusion
would be the wrong ideal-divisibility direction.

For signed homogeneous comparison, X>0 maps to(x,y,z)=(X,-1,Y).
Its characteristic number is zeta*j(alpha). X=-A maps to(A,1,Y),
with characteristic number -zeta*j(alpha). The characteristic ideals
are conjugate to A^p. In theta-action F0 and the even augmentation
also remove these root-of-unity/sign factors, and the common lambda²
normalization gives the conjugate beta. Thus the finite2 property
does survive the actual signed source interface. It is not justified
merely by identifying an ideal while ignoring arbitrary generators.
No e1 denominator theorem is imported.

To change complement6N to2N by an integer norm shift requires the
UNIQUE Theta-2N. The supports of psi and sigma2 psi differ: their
nonzero M1 values differ by1/2. Equal cardinalities give an index in
the former but not the latter; there jpsi0 and Theta0. At that index
Theta-2N has coefficient-2. Translation preserves the existence of
such an index. A mere norm shift/translate therefore does not produce
a positive original-weight R8 column. No statement about its actual
infinity phase follows from this finite2 congruence. R9E passed as a
necessary conditional construction, not an unconditional equation
counterexample or an original-weight bridge.

## 8. R9F: exact model data and the generator quantifier

Set c=2p²,a0=1+c zeta,A0=(a0). The norm is
Z=(c^p+1)/(c+1)>1, an odd positive integer. Here a0 is1modlambda²
because c has large p-valuation, and is1mod2O. If a prime divided
two distinct conjugates, it would divide c(zeta^a-zeta^b). A prime
over a divisor of c divides neither conjugate; the remaining root
difference has only lambda support, while a0 is a lambda-unit.
Hence the conjugate ideals are pairwise coprime without factoring Z.

At a prime of A0, zeta=-1/c lies in the rational prime field and has
order p. The rational prime is not p and not a divisor of c, so
ell1modp and residue degree1. Thus the matched-prime construction
applies to A0. Choose any actual accepted R8 two-half element theta
with F0,M1nonzero, and define b_i=a0^psi_i. These are integral,
normalized1modlambda², with ideal A0^psi_i and
b_i*j b_i=a0^N=Z. Every conjugate has modulus sqrt(Z). By the
same-ideal uniqueness argument they have exactly the normalized
Jacobi properties used here, not only their norms.

Original-weight beta_theta=b1b2 is1mod2O at all conjugates, so at
the MODEL choice w'2 its equality ideal is exactly(2). Also
chi=(b1b2-Z)/2 is integral. Since Z is odd, the overlap valuation
argument gives an unconditional pole of chi/(b1b2) in this model.
No actual X with w'2 or with the required linear characteristic
number has been supplied. This is ideal/normalization data, not a
new Nagell--Ljunggren or Strong Fermat solution.

The CHOSEN number a0^p is not linear in1,zeta. After reducing
zeta^p1, its coefficients at degrees p-2 and p-1 remain
p(p-1)c^(p-2)/2 and p c^(p-1). They differ because c2p² is not
(p-1)/2. If a0^p were in Q+Qzeta, its degree<=p-1 representative
minus a linear polynomial would be a multiple of Phi_p, forcing all
coefficients at2..p-1 equal. This proves the asserted chosen-number
nonlinearity.

The phrase that A0^p is generated by a0^p, "not by a linear" number
must be read with that CHOSEN-generator scope. The calculation does
NOT prove that the ideal admits NO other linear generator: a unit
can change a generator. A simple exact diagnostic in the SAME
cyclotomic field is zeta²(2+zeta), a nonlinear generator of the ideal
(2+zeta), which also has the linear generator2+zeta. Degree3<p-1
makes its nonlinearity immediate. This does not assert a linear
generator for the specific A0^p; it exposes the logical distinction.
The candidate itself ends by saying the additional linear hypothesis
was not checked. I retain that weaker scope as note R9R2-N3 and
do not certify an ideal-level linear-generator exclusion or silently
supply such a proof. The model data and chosen-number claim passed;
any stronger reading would require an author argument.

## 9. Current and obsolete source versions

The arXiv record was freshly checked:2108.08572v4 has Bartolome and
Mihailescu, revised22September2025, internal24September date and a
submitted/under-review comment. It is a different proof from sole-author
2021v1, *On a Popular Diophantine Norm Equation*. No external review
status is inferred from the text's acknowledgements.

The actual v4 definitions of positivity, relative weight,J_k,beta,
normalization and equality ideals, followed by the COMPLETE Lemma5
product argument and its downstream context, were read directly.
The current criticism is localized to multiplying separate
divisibilities without accounting for overlap. R9D/F supply the
valuation calculation. R9E supplies a conditional higher-weight
finite2 equality, not an actual solution refuting the final theorem.
No final v4 Diophantine result is imported or declared false.

For v1, the fresh read includes its identity/intro and the operative
Section4.3.4 small-vector/perturbation argument through its conclusion,
with bounded surrounding Section4.3 context. This is NOT a full25-page
proof audit. The generic R9C example challenges the proposed
homogeneous-existence-to-escape implication; it is not an actual
arithmetic matrix satisfying every other v1 premise. These criticisms
are not transferred between versions.

The2008 primary matched Jacobi formula, its sign/inverse conventions
and normalization uniqueness were checked in the author-uploaded
text. Its later height/class-number/appendix claims were not newly
proved or imported. Fukshansky's quantitative avoidance theorem is
context for the distinction, not a premise needed by the elementary
counterexample or cofactor proof. Precise read limits and null browser
response hashes are in the companion source record.

## 10. Complete result, failed routes, integrity and budget

The failed routes correctly retain the missing evaluated-nonzero
escape, phase restrictions, dense support cost and actual linear
characteristic-power interface. Distinct ideals are not additive
independence; formal monodromy is not nonzero specialization; unit
circle moduli without integrality do not imply a root of unity.
Neither the generic rational example nor the cyclotomic model is
advertised as an actual signed solution. No useful unconditional
height improvement, new exclusion, source final-theorem refutation,
annual solution or novelty follows.

The whole proof audit is complete despite the localized boundary
correction R9R2-01. R9A/B and the properly conditional/model-scoped
R9D--F passed; the intended R9C sqrt(H) example and cofactor replacement
also passed. The erroneous all0<R<H unit-witness sentence must be
corrected by the author, preserving v1, with affected review after
the versioned response. This report does not write the repair.

All mathematics was HAND reasoning. No mathematical code, CAS, mask
scan, field/rank search, source algorithm execution, old certificate,
author rerun or native mathematical child was used. Only metadata
scripts bind bytes/JSON/tags. No old/shared/Git/cache writes, spawning,
contact, charge, paid API, subscription or bypass occurred.

The compact baseline binds11 constructor files,28 selected current
authority/context records and9 immediately previous own frozen files:
48occurrences/48paths, canonical summary
`98214ae201f989e00eb6d39fee0e8e9dcb9c6d3eb6df4cd4c50a3ae4e8545d59`.
Constructor historical metadata is bound at exact parent fingerprints,
not recursively recopied. My own immutable NF parent binds466 older
own paths transitively; its nine files were reverified. The new review
prefix was unused before the first write. Original-v1 integrity and
all earlier own frozen bytes are preserved.

Requested inherited gpt-6.1-sol/max remains distinct from unavailable
independent effective readback. User authorization applies to the new
weekly window reset1792874445,90% TOTAL ceiling with integration
reserve and no automatic next-window spending. Direct primary/legacy
telemetry at00:44:05UTC2026-10-18 showed4% TOTAL,10080minutes,
ordinary allowed. Root owns shared monitoring/awake. The complete
report, ALL48 ledger rows, issues, source records and immutable
metadata freeze BEFORE opening any NEW peer R9 finding/file or later
constructor version. Root alone may reconcile and promote.
