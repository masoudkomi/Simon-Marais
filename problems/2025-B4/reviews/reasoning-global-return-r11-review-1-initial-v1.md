# R11: independent whole initial audit 1

18 October 2026 UTC. Reviewer C, `/root/review_2017_coarsening_r1`.
This is a COMPLETE initially blind WHOLE audit of GR0--GR3 and ALL32
constructor obligations. The mathematical disposition is sealed until the
coordinator explicitly confirms BOTH entire initials. No corresponding NEW
review-2 finding, file, actual inventory, hash or metadata was accessed.

**Disposition: PASS in the exact stated partial scopes.** All32 obligations
pass; zero substantive defects, zero required repairs. Nine closed scope or
exposition notes appear below. This is an independent audit recommendation,
not coordinator promotion, an annual solution or a publication-priority claim.

The audited immutable main is
`notes/reasoning-global-return-r11-candidate-v1.md`, 25923 bytes,
SHA256 `aa1e1242621a9bd99b42bb306827e41e8ee6309b963ce2c63c8e503cd325bbe3`.
Its ENTIRE5 freeze is 2639 bytes, SHA256
`1e6953c80d9d17efbb2b94c5ae6af3a0b9880119d46c1e0fde7dc4c28a266771`.
The main, source JSON, full administration code, baseline and freeze were all
read. The author code was inspected, not executed. Mathematical reconstruction
was by hand; no mathematical program, CAS, scan, table, test, optimizer or
old/source/author executable replay supplied a premise.

## Independence, domain and exact prior authority

A is the sole NEW R11 constructor. C authored OLD accepted R10 and other older
inputs, and independently reviewed OLD DR8. Those roles are disclosed: this
audit does not count as independent recertification of C's OLD R10 theorem.
C supplied no NEW R11 proof inference before this audit. The complete current
R10 accepted body and EACH current acceptance MD/JSON were freshly read, as
were the complete DR8 body and EACH current MD/JSON. R10 supplies NI in its
separately reviewed scope. DR8 supplies context and failure boundaries only;
no DR8 support count is used to prove GR0--GR3.

Official B4(b) asks about integer bases and perfect powers with degree and
exponent at least two. R11 assumes the narrower actual signed sector

    p>=37 prime, |X|>=2, Phi_p(X)=Y^p,
    K=Q(zeta_p), O=Z[zeta_p], e=p-1,
    j=complex conjugation, lambda=1-zeta_p.

The official degree is e; the number of terms and perfect-power exponent are
p. There is no reduction of every annual solution to this sector. Neither
preliminary (a) nor a different annual problem was investigated.

The new claim is conditional on the ACTUAL characteristic class condition

    A^p=(X-zeta), N(A)=Y, and [A]=[jA].                    (C)

It is not a condition on an arbitrary representative, a local root or a
formal Jacobi element. The accepted NI says that (C) forces one unique center
a in {0,-1}, finite s>=2, X-a=epsilon*c*p^s with c>0 p-free, and a canonical
nonzero INTEGRAL cofactor ideal J with

    1 <= N(J) < 2^e*Y/p^[1+(s-1)e].

Thus Y>p^[1+(s-1)e]/2^e. The strict inequality, integrality, unbounded c,
both ordinary signs and the global class hypothesis are indispensable.

## Whole reconstruction

### 1. Actual characteristic ideal and elementary signed bounds

For X=U>=2, Phi_p(X)=(U^p-1)/(U-1)>1. For X=-U<=-2 it is
(U^p+1)/(U+1)>1. Since p is odd, Y is necessarily positive and >1.
Both displayed expressions are strictly below U^p, so 1<Y<U at both signs.

If X=1 mod p, expansion at 1 makes v_p(Phi_p(X)) exactly one. The
valuation of Y^p is divisible by p, so that residue cannot occur. For
different nonzero c,d, any common prime ideal of X-zeta^c and X-zeta^d
lies above p; the residue exclusion makes that prime absent. Their product
is Y^p. Unique ideal factorization now makes every exponent in each factor
a multiple of p, giving the unique nonzero integral A. Absolute ideal norms
give N(A)^p=Y^p and N(A)=Y. This proof uses actual ideals of an actual
integer solution; no local realization or squarefreeness is inserted.

### 2. Published height boundary, and the precise annihilation import

The signed bound near -1 is an external theorem import. The original
author-posted chapter states Theorem3 for integer solutions of
Phi_p(X)=p^eta*Y^p, eta in {0,1}, p>=17, and includes
|X|<4(p-2)^p at residue -1. Theorem2.2 of the later paper states the same
bound. Our eta=0, p>=37, both-sign domain matches. [Mihailescu chapter](https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren),
[Bartolome--Mihailescu](https://arxiv.org/pdf/1412.5798).

The complete operative original upper-bound section was read, including its
regular/singular and second-case discussion. The later Appendix5.1 explicitly
details a first-case application and calls the second-case adaptation similar.
This audit verifies the literal published statement and its operative scope;
it does not claim a new proof of all classical reflection, cyclotomic-unit or
singular-matrix foundations. Theorem4, the Vandiver-based lower-trace argument,
unrelated distinct-prime results and the appendix's later section are not
imported. This is a declared theorem dependency, not an unstated assumption
that a local series automatically satisfies every global conjugate equation.

For the separate center-0 proof, the relevant source Lemma5 annihilates the
order-p class and primary-unit obstructions in the regular/reflected
components. Its index convention becomes epsilon_i=e^-1 sum c^-i sigma_c
after inversion of the summation parameter. B2=1/6 and B4=-1/30 are p-units
for p>=7; hence epsilon2 and epsilon4 lie in the required annihilator. This
uses the cited classical reflection theorem, not Vandiver. The full Lemma5
proof/lifts and the center-0 primary setup were read in the author version.

Here is an explicit check for a non-idempotent combination, to remove any
possible implicit extension of the source's idempotent calculation. Put
alpha=1-zeta*X and let Pi lift epsilon2+epsilon4. Its characteristic ideal
has order dividing p. Principalizing its Pi image gives alpha^Pi=epsilon*beta^p.
If p^2 divides X, alpha is in U_(2e), hence in U_2^p=U_(e+2), so epsilon
is a locally p-th-power unit. Pi kills that primary-unit quotient. Applying
Pi again makes alpha^(Pi^2) a global p-th power; Pi^2-Pi is divisible by p
in Z[G], so alpha^Pi is one too. If Pi*Theta=Theta mod p, the same argument
makes alpha^Theta a global p-th power. A root initially in K is integral
when Theta has nonnegative coefficients, since its p-th power is integral
and O is integrally closed. This also covers the principal characteristic
class, not only classes of exact order p. The actual primary element is
1-zeta*X; the short source Lemma13 rendering that drops X is read using
its preceding definition(24), not as a statement about 1-zeta.

### 3. Positive selection and ramified nonvanishing

For each u in F_p and c!=0 let n_c be the canonical nonnegative residue of
c^-2+u*c^-4. Its c and -c coefficients are equal. The coefficient vector
cannot vanish: otherwise the polynomial c^2+u would vanish on all p-1>=6
nonzero residues. Both relevant power sums vanish, so S=sum n_c is a
positive multiple ph of p. Pairing also makes S even and h even.

As u runs through F_p each fixed n_c takes all p residue representatives
once. Therefore average_u h=(p-1)^2/(2p)<(p-1)/2. A choice exists with
0<h<e/2, without a search or a numerical parameter. The reduction of Theta
is e(epsilon2+u*epsilon4), so the previous annihilation argument applies.

Set rho=-sum n_c*zeta^c. In the finite expansion zeta^c=(1-lambda)^c,
the constant and linear coefficients are divisible by p, while the
quadratic coefficient is

    -sum n_c*c*(c-1)/2 = 1/2 mod p.

Indeed sum n_c*c^2=-1 and sum n_c*c=0 in F_p: all remaining exponents
are nontrivial modulo e, also at the auxiliary endpoint p=7. Higher
terms have lambda valuation at least three. Since v_lambda(p)=e>=6,
v_lambda(rho)=2 exactly. Consequently v_lambda(rho^h)=2h<e. This is a
genuine nonzero power modulo pO, not the false general implication for
an arbitrary nonzero element of the nonreduced quotient O/pO.

### 4. Coefficients, global denominators and coherent real branches

For F(T)=product_c(1-zeta^c T)^(n_c/p)=sum a_i T^i, put
b_i=p^i i! a_i and S_j=sum n_c zeta^(cj). Logarithmic differentiation
gives b_0=1 and

    b_i=-sum_(j=1)^i S_j p^(j-1) (i-1)!/(i-j)! b_(i-j).

Every factorial ratio is an integer, so b_i is integral. Modulo p only
j=1 remains; b_i=rho*b_(i-1) and b_i=rho^i mod pO.

For completeness, the global denominator step needs more than the phrase
“i! is p-free.” At i<p, for any integer n>=0,

    p^i binom(n/p,i)=product_(k=0)^(i-1)(n-kp)/i!

is an integer. At every rational prime ell!=p, the numerator arithmetic
progression contains at least floor(i/ell^r) multiples of ell^r for every
r, because p is an ell-unit. These counts dominate v_ell(i!). There is no
p in i!. Thus the quotient is integral at every prime. Multiplication of
the individual binomial series gives p^i a_i in O for i<p. This is also
the elementary content of source Lemmas10--11; the recurrence alone would
only prove b_i integrality. This missing one-sentence justification is a
closed exposition note, not a false coefficient claim or a required repair.

At our chosen h<p, b_h-rho^h has lambda valuation at least e, whereas
rho^h has valuation 2h<e. Hence v_lambda(b_h)=2h and

    v_lambda(p^(h-1) a_h)=2h-e<0.

The annihilation input gives a root in K. Since Theta is j-invariant,
alpha^Theta is real; a p-th root in K can be adjusted by a root of unity
to its unique real root. Indeed j(nu)/nu is in mu_p and multiplication
by zeta^k solves the adjustment because 2 is invertible modulo p. This
real root is integral. Pairing c,-c gives sum c*n_c=0 mod p and S=ph
even. Factoring the product at infinity then proves exactly

    nu=X^h F(1/X).

Both sides have the same p-th power and are real. The factor F has real
coefficients, and the only real p-th root of unity is one. This is one
global root and its genuine conjugates, not independently chosen phases.
It works for negative X as well; h is even and |1/X|<1.

### 5. All-conjugate integral remainder and height contradiction

For a>=0, the absolute binomial coefficients are bounded by the rising
coefficients of (1-T)^(-a). Multiplying gives the same majorant (1-T)^(-h)
at every embedding. Taylor's real remainder bound therefore yields

    |F(1/X)-sum_(i<=h) a_i X^-i|
      <= binom(2h,h+1) U^(-h-1) (1-1/U)^(-2h-1).

Assume U>=(4p)^h. Here h is positive, p>=7 and 2h<e, so U>4h+2.
Bernoulli gives (1-1/U)^(2h+1)>1/2. Also
binom(2h,h+1)<4^h/2, since in the sum of the row 2h the two symmetric
terms at h-1 and h+1 already use twice this coefficient and the central
coefficient is positive. Thus each conjugate of the INTEGRAL remainder

    R=p^h nu-sum_(i=0)^h p^h a_i X^(h-i)

has modulus <(4p)^h/U<=1. The strict inequality persists at equality
U=(4p)^h. A nonzero algebraic integer has nonzero integer absolute norm,
so R=0. “Integer R” here means algebraic integer; no claim that R is
rational is needed. Dividing by p, all i<h terms remain integral by the
global denominator argument and h-1-i>=0. The last term would then be
integral, contradicting its negative lambda valuation. Therefore

    U<(4p)^h<(4p)^(e/2).

The proof uses the denominator estimate only under U>4h+2 and proves the
specific ramified nonvanishing it needs. It does not rely on either of
the two overbroad source shortcuts identified by the constructor.

### 6. Actual norm-height comparison and the exact survivor

Under (C), NI already excludes depth one and every residue other than
the two centers. At center zero, s>=2 gives Y>p^p/2^e. But Y<U and
the preceding height give U<(4p)^(e/2). The lower/upper ratio is

    p*(sqrt(p)/4)^e>1, since p>=37>16.

This proves GR1 at both signs and at every unbounded cofactor c.

At center -1 with s>=3, NI gives Y>p^(2p-1)/2^e. The imported signed
height yields U<4(p-2)^p<4p^p. The lower/upper ratio is
(p/2)^e/4>1 for p>=37. Thus GR2 leaves exactly
X=-1 mod p^2 but X!=-1 mod p^3 for an actual solution satisfying (C).

The same arithmetic does not exclude depth two. For real t>2,
t*log(1-2/t) is increasing, since with z=2/t its derivative is
log(1-z)+z/(1-z)>0; the latter function is zero at z=0 and has positive
derivative z/(1-z)^2. At t=4 the exponential is 1/16. Hence for p>4,
(1-2/p)^p>1/16, making the HB- upper bound strictly above p^p/2^e.
This is only compatibility of true bounds, not a construction of a
solution. The unbounded depth-two invariant-class sector stays open.

### 7. Actual class difference and the relative kernel

A^p principal makes D_A=[A]/[jA] killed by p, and j(D_A)=D_A^-1.
Outside the exact surviving sector, NI and GR1/GR2 rule out D_A=1.
Thus its order is exactly p. Norm to Kplus is invariant under j,
so N(D_A)=1. This places a class of the actual solution in the relative
norm kernel, rather than assuming that an abstract p-class is realizable.

Let i extend ideals from Kplus to K. For every ideal class b,
N(i(b))=b^2, including ramified primes, because [K:Kplus]=2.
The cokernel of N therefore has exponent dividing two. The p-part of
that cokernel is zero, so for finite class groups

    v_p(|ker N|)=v_p(h_K)-v_p(h_Kplus).

The order-p class makes this positive. No injectivity of extension,
Vandiver, regularity table, fractional-small-norm conclusion or ideal
principality is inferred. This proves GR3 in precisely its stated scope.

## ALL32 separate obligation dispositions

Each disposition concerns the NEW whole argument, with OLD NI accepted as
a separately reviewed input. PASS does not broaden the official domain.

| ID | Disposition | Independent check |
|---|---|---|
| O01 | PASS | Official degree e, term count/exponent p; signed restricted sector only; no preliminary proof or annual reduction. |
| O02 | PASS | Main conclusions assume p>=37; auxiliary selection needs only p>=7; no smaller-prime import is needed. |
| O03 | PASS | Both geometric expressions are positive >1, so odd p forces Y>1; neither sign produces a negative Y. |
| O04 | PASS | At X=1 mod p the cyclotomic value has p-valuation one, incompatible with Y^p. |
| O05 | PASS | Pairwise characteristic factors are coprime, each ideal exponent is divisible by p, and A is unique/integral/nonzero with norm Y. |
| O06 | PASS | (C) is equality of actual ideal classes; no replacement by an equality of ideals, a unit or a local root. |
| O07 | PASS | COMPLETE current R10 body/MDJSON read; strict integral-J NI retained; old C authorship disclosed. |
| O08 | PASS | Unique center, finite s>=2, epsilon sign and unrestricted positive p-free c are precisely NI's domain. |
| O09 | PASS | Literal published signed theorem allows eta=0, p>=17 and residue -1; actual p>=37 is inside it. |
| O10 | PASS | HB- is an attributed external theorem; operative proof/appendix read; no fresh matrix-foundation recertification claimed. |
| O11 | PASS | Regular/reflected component import verified at source Lemma5; Pi argument above handles a non-idempotent Theta; no Vandiver. |
| O12 | PASS | Idempotent inversion convention and B2/B4 denominators checked; p>=7 avoids every denominator prime. |
| O13 | PASS | Correct actual element is 1-zeta X, in U_(2e); U_2^p=U_(e+2) gives local p-th-power primaryness. |
| O14 | PASS | Canonical coefficients are nonnegative/even; a degree-two polynomial cannot vanish on all p-1 nonzero residues. |
| O15 | PASS | Nonzero vector implies positive S; power sums give p|S, pairing evenness gives even h. |
| O16 | PASS | Exact averaging in F_p gives e^2/(2p)<e/2; no finite experiment or selected prime is involved. |
| O17 | PASS | Constant/linear moments vanish; quadratic moment is -1, giving coefficient +1/2 mod p. |
| O18 | PASS | e>=6 separates the first two p-divisible terms from lambda^2; higher terms start at degree three. |
| O19 | PASS | Logarithmic derivative recurrence has integer factorial ratios; reduction leaves j=1 and b_i=rho^i. |
| O20 | PASS | h<p, h! a p-unit and 2h<e give exact v_lambda(b_h)=2h and negative last-coefficient valuation. |
| O21 | PASS | Adjusting a global root by mu_p gives the unique real root; paired product proves coherent equality at both X signs. |
| O22 | PASS | Positive rising-binomial majorant and Taylor remainder hold uniformly for all actual conjugates with the same h. |
| O23 | PASS | U>=(4p)^h implies U>4h+2; Bernoulli is used only in this range, with strict factor <2. |
| O24 | PASS | Global coefficient denominators cleared as proved above; R integral and every conjugate <1, even at threshold equality. |
| O25 | PASS | p^i a_i is globally integral for i<p by the arithmetic-progression denominator lemma; all earlier terms survive division by p. |
| O26 | PASS | Ratio p(sqrt(p)/4)^e>1 at all p>=37; NI, not a new argument, excludes depth one. |
| O27 | PASS | s>=3 gives the displayed lower bound and (p/2)^e/4>1; signed HB- applies without a sign switch. |
| O28 | PASS | The derivative and p>4 endpoint prove a genuine gap at s=2; compatibility of bounds is not asserted existence. |
| O29 | PASS | Actual D_A is p-torsion, nontrivial outside the one survivor, hence order p and inverted by j. |
| O30 | PASS | Norm is j-invariant; N composed with extension is square on the lower class group, not the reversed composite. |
| O31 | PASS | Cokernel is 2-torsion; odd-p valuation formula has the correct direction and forces a positive relative kernel p-part. |
| O32 | PASS | Annual/full-class exclusion, useful new unrestricted height, numerical prime range, local converse and novelty remain unclaimed. |

## Issue ledger: nine closed notes, no required repair

| ID | Status | Challenge and resolution |
|---|---|---|
| R11R1-N1 | CLOSED, scope | Restricted p-diagonal plus actual (C) is never substituted for all official solutions; arbitrary nontrivial minus classes survive. |
| R11R1-N2 | CLOSED, role | C's OLD R10 authorship is disclosed and accepted NI is not independently self-certified here; DR8 is context only. |
| R11R1-N3 | CLOSED, algebra | A generic linear combination of regular idempotents is not itself idempotent. The explicit Pi^2-Pi and Pi*Theta-Theta argument closes the passage. |
| R11R1-N4 | CLOSED, exposition | “i! p-free” alone only proves local-at-p integrality from b_i. The elementary arithmetic-progression denominator proof above establishes the actual global assertion; source Lemmas10--11 also supply it. |
| R11R1-N5 | CLOSED, phases | A real p-th-power target need not make an arbitrary root real. The root-of-unity adjustment and paired product prove one coherent global real root. |
| R11R1-N6 | CLOSED, norm | A single small embedding would not kill R; covariance/unchanged weight gives every embedding small, and R is an algebraic integer. |
| R11R1-N7 | CLOSED, source | HB- remains an external signed theorem import, not a reconstructed whole singular-matrix proof or a new Vandiver-free lower-trace theorem. Literal publication/version limits are recorded. |
| R11R1-N8 | CLOSED, class group | Extension injectivity is unnecessary. Norm-after-extension square gives 2-torsion cokernel and the exact odd-p kernel formula. |
| R11R1-N9 | CLOSED, residual | s=2 near -1 and actual nontrivial minus classes are not excluded or constructed; no annual or priority conclusion follows. |

The suggested one-sentence denominator clarification in N4 is optional
exposition. The assertion itself is true with the supplied elementary proof;
no substantive unproved new hypothesis or changed theorem is required.

## Literal source and operation record

The separate source JSON records the COMPLETE primary windows read. In the
Mihailescu author text these include Theorem3/standing signed equation,
Section2.5/Lemma5/lifts, relevant Section2.6 primary definition, and the
COMPLETE operative Section4 through its closing second-case paragraph.
The Appendix5.1 lemma/proof/application in arXiv1412.5798 was read completely,
along with its version line/Remark1.4 and the exact Theorem2.2 statement.
Washington's book, the full reflection foundations and the whole later
19-page paper were not freshly audited. Only the opening of Section5 was
incidentally returned here; its lower-trace theorem is not imported.

An initial combined local/web response clipped the aggregate middle. The
DR8 tail and BOTH complete acceptance records were separately recovered;
all operative source gaps were filled by bounded individual openings.
No clipped middle is represented as read. No new binary was downloaded,
no source text was redistributed, no raw PDF hash is available, and there
was no stalled call, approval, native job, purchase, contact or bypass.

The author administration/baseline declares an external R13 parent. Its
literal identity was seen as part of the required ENTIRE5 author metadata;
its external payloads/inventory were NOT opened, followed or hashed. It is
not an operative premise. This review binds the immutable ENTIRE5 itself,
the exact current operative authorities and its own immediate FL15 parent.
It does not run the author helper or expand that unrelated parent history.
All current required guard checks are documentary only. Historical mutable
maps in author metadata remain dated observations, not live byte guards.

Work sequence: narrow unused-prefix check; complete author5 reads; fresh
operative body/authority reads; full hand proof and all32 endpoint checks;
primary bounded text/PDF reading with clipped passages recovered; signed
and global-integrality adversarial checks; complete report/ledger/issues;
documentary-only compact integrity build; FULL final ALL-payload model
readback; freeze; FULL manifest model readback; SEPARATE read-only verify.
No corresponding NEW review2 material was accessed before that entire
checkpoint or before explicit BOTH release. The immediate own parent is
the frozen FL15 constructor; it is bound without recopying historical lists.

Requested inherited gpt-6.1-sol/max is distinct from an unavailable
independent effective-setting readback. Direct telemetry at23:51:09UTC was
72% TOTAL, ordinary usage allowed, reset1792874445, window10080minutes.
The authorized ceiling remains90% TOTAL with reserve; no later-window
spending is authorized. Root owns shared integration/Git and keep-awake.
Only this new exclusive review prefix was written.
