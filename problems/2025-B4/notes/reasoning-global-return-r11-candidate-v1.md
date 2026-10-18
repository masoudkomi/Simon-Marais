# 2025 B4(b): actual characteristic-class asymmetry outside one depth

**Candidate proof - unverified.** Sole new constructor: worker A,
`/root/review_2021_reasoning_j15_r2`. Two OTHER initially blind WHOLE
audits and coordinator reconciliation are required. Requested inherited
settings are `gpt-6.1-sol` / `max`; an independent effective readback is
unavailable. No mathematical program, scan, CAS, test, prime table,
optimizer, or old/source/author script replay was used.

The new bridge combines the accepted ACTUAL diagonal cofactor-ideal norm
bound with published signed height bounds. It eliminates the whole
conjugation-invariant-class sector at center 0, and the whole such sector
at center -1 of depth at least 3. It does **not** eliminate a solution
having a nontrivial minus class, or the remaining invariant-class sector
at exact depth 2 near -1. This is not an annual solution or a novelty
claim. The norm bound is accepted prior work; the heights are attributed
published input, not new unrestricted height theorems.

## 1. Domain and exact imports

Consider ordinary integers in the restricted signed prime-diagonal
domain

    p >= 37 prime, |X| >= 2, Phi_p(X) = Y^p.                (D)

The official degree is p-1 and the number of terms is p. Both ordinary
signs of X are included. No reduction of the full official B4(b) domain
to (D) is asserted. Put U=|X|, e=p-1, K=Q(zeta_p), O=Z[zeta_p],
j=complex conjugation, Kplus=K^j, and lambda=1-zeta. Normalize
v_lambda(lambda)=1, so v_lambda(p)=e.

For (D), Y is positive and greater than 1. The residue X=1 mod p is
impossible: expansion at 1 gives v_p(Phi_p(X))=1, whereas the valuation
of Y^p is a multiple of p. The characteristic factors X-zeta^c are
pairwise coprime away from the unique prime above p; that prime does not
divide them here. Unique ideal factorization therefore gives a unique
nonzero integral ideal A with

    A^p = (X-zeta),  N_K(A)=Y.                              (1)

The class condition below concerns this ACTUAL A:

    (C)  [A]=[jA] in Cl(K).                                (2)

It is never inferred from local solvability or imposed by choosing an
abstract representative.

**Accepted input NI.** R10A/R10D in the complete current accepted body
`proofs/reviewed-reasoning-compatible-return-r10-v1.1.md`, with its
current acceptance MD and JSON, imply the following for an actual (D)
satisfying (C). There is a unique a in {0,-1} and a finite s>=2 with

    X-a = epsilon*c*p^s, epsilon in {1,-1}, c>0, p not | c.

The canonical nonzero integral cofactor ideal J satisfies

    N_K(J) < 2^e*Y / p^[1+(s-1)e].                         (3)

Consequently

    Y > p^[1+(s-1)e] / 2^e.                               (4)

The construction removes exactly the ramified prime powers, retains the
whole actual centered cofactor, and does not identify J with DR8's
ordinary unitary partition. Only (4) is used in the new comparison.

**Published height input HB.** Mihailescu, *Class Number Conditions for
the Diagonal Case of the Equation of Nagell and Ljunggren*, Developments
in Mathematics 16 (2008), 245-273, Theorem 3, states signed bounds for
integer solutions of Phi_p(X)=p^eta*Y^p, eta in {0,1}, p>=17. In our
eta=0 domain the operative parts are

    X=0 mod p:   U < (4p)^(e/2);                           (HB0)
    X=-1 mod p:  U < 4*(p-2)^p.                            (HB-)

The author-posted version read is Version 2.0, September 17, 2007, linked
to the 2008 chapter. Bartolome--Mihailescu arXiv:1412.5798, Theorem 2.2,
repeats these bounds. Its accessible PDF has an internal November 2,
2021 version line despite the older arXiv identifier; those dates are
not conflated. Appendix 5.1 supplies a later discussion of the singular
system in the upper-bound proof. HB- is an **external published theorem
import**. Reading its complete operative original section and the
appendix is not represented as a fresh independent proof of all its
cyclotomic and matrix foundations. Section 5's lower-trace argument and
Theorem 4 are not imported.

Section 3 below supplies an independent, explicit selection and
coefficient argument for HB0 in the needed s>=2 sector, using only a
precisely stated classical annihilation consequence of the same source.
Thus the center-0 conclusion need not rely on the source's unqualified
nonvanishing-power sentence modulo the ramified ideal (p).

The accepted DR8 body and its current MD/JSON were fully read for the
actual adjacent cofactor/order context and its failure boundaries. None
of its support counts, cofactor lower bounds, or Jacobi interpretations
is an additional premise of the proof below.

## 2. Proposed actual global conclusions

**GR1.** No actual solution (D) satisfying (C) has X=0 mod p.

**GR2.** No actual solution (D) satisfying (C) has X=-1 mod p and
v_p(X+1)>=3. Therefore any actual solution satisfying (C) must obey

    X=-1 mod p^2,  X != -1 mod p^3.                        (5)

This conclusion includes both ordinary signs of X. It imports HB- as
specified above. The local exclusion of depth 1 and of the other
residue classes is prior R10A, not a new local criterion.

**GR3.** Define the actual class difference

    D_A = [A]*[jA]^-1.

For every actual (D) outside the single sector (5), D_A is nontrivial
of exact order p, j(D_A)=D_A^-1, and

    D_A in ker( N:Cl(K) -> Cl(Kplus) ).                    (6)

In particular

    v_p(h_K) > v_p(h_Kplus).                               (7)

Equivalently, the relative norm kernel has a nontrivial p part. A
class-number consequence or a regular-prime exclusion already present
in the literature is not claimed new. The ideal-specific placement (6)
uses the actual characteristic class and the new comparison, rather
than a selected abstract order-p ideal.

**GR0, an auxiliary positive selection.** For p>=7, there exists a real
positive lift Theta with reduction in the span of the regular even
idempotents epsilon_2,epsilon_4, weight ph with 0<h<e/2, and

    rho=-sum_c n_c*zeta^c,  v_lambda(rho)=2,
    rho^h != 0 mod pO.                                    (8)

This is proved for all such p by averaging, without a search. It is the
selection used in the complete center-0 argument next. It does not
assert that every nonzero element of O/pO has nonzero h-th power.

## 3. A source-safe center-0 height argument

### 3.1 The precise classical annihilation import

Let sigma_c(zeta)=zeta^c and use the source convention

    epsilon_i = e^-1 sum_c c^-i*sigma_c in F_p[G].

The consequence needed from Mihailescu Section 2.5, Lemma 5, and
Section 4.3, Lemma 13 is the following:

    If an actual (D) has p^2 | X and a positive integral group-ring
    lift Theta reduces to span(epsilon_2,epsilon_4), then
    (1-zeta*X)^Theta is a p-th power in O.                  (AI)

Here B_2=1/6 and B_4=-1/30 are p units for p>=7. These two even
components are outside the irregular/reflected support in that source,
so they annihilate both the order-p characteristic class and the
relevant primary-unit quotient. Also 1-zeta*X is locally a p-th power:
it is in U_(2e), and U_(e+2)=U_2^p by the complete local power map,
with 2e>=e+2. Thus the unit remaining after principalization is primary
and killed by the same components, which gives (AI). The p-th root is
integral because its p-th power is integral and O is integrally closed.
For a non-idempotent combination of these two components one can apply
their support projection Pi first: Pi*Theta=Theta modulo p, and Pi
annihilates the primary-unit quotient. Thus no idempotence of
epsilon_2+u*epsilon_4 for arbitrary u is being presumed.

This imports the classical regular-component annihilation/reflection
consequence, not Vandiver's conjecture. No fresh full Washington or
class-field-theory proof is claimed. In the web rendering Lemma 13's
short alpha-prime definition omits X; the surrounding definition (24)
and its proof use alpha-prime=1-zeta*X. We have stated the actual
quantity explicitly and have not applied an assertion about 1-zeta
whose norm is p.

### 3.2 Positive lifts and exact ramified valuation

For u in F_p and c in F_p^times, let n_c(u) be the integer in
{0,...,p-1} representing

    c^-2 + u*c^-4 mod p,

and put Theta_u=sum_c n_c(u)*sigma_c and S(u)=sum_c n_c(u).
The functions are even in c, so jTheta_u=Theta_u. Moreover

    Theta_u mod p = e*(epsilon_2+u*epsilon_4),
    S(u)=0 mod p.                                         (9)

The second fact is the finite-field power-sum identity. The vector is
nonzero for every u: otherwise c^2+u would vanish for every nonzero c,
which is impossible for p>=7. Hence S(u)>0 and h(u)=S(u)/p is a
positive integer. Its parity is even, because S(u) is a sum of equal
pairs and p is odd; parity is not needed for the averaging inequality.

For each fixed c, as u ranges over F_p the residue n_c(u) ranges once
over {0,...,p-1}. Consequently

    sum_u S(u)=e*p*e/2,
    (1/p)*sum_u h(u)=e^2/(2p)<e/2.                        (10)

Choose a u with 0<h=h(u)<e/2. This proves the required weight bound
without selecting a numerical parameter or checking a table.

Write n_c=n_c(u), Theta=Theta_u, rho=-sum_c n_c*zeta^c. In the expansion
zeta^c=(1-lambda)^c, the constant and linear coefficients of rho are
divisible by p: sum_c n_c=0 mod p and sum_c n_c*c=0 mod p. The
quadratic coefficient is

    -(1/2)*sum_c n_c*c*(c-1) = 1/2 mod p.                 (11)

Indeed the c^-2 term contributes sum_c 1=e=-1 mod p to the c^2
moment, and every other moment involved has a nontrivial power modulo
e and sums to zero for p>=7. Since e>=6, the first two coefficients
have lambda valuations at least e and e+1, the quadratic coefficient
is a p unit, and all later terms have valuation at least 3. Thus

    v_lambda(rho)=2,  2h<e,

which proves all of GR0 and the last assertion in (8).

### 3.3 Coefficients and the needed nonzero power

Define the convergent-at-zero series

    F(T)=product_c (1-zeta^c*T)^(n_c/p)=sum_i a_i*T^i,
    b_i=p^i*i!*a_i.

The branch is defined by the binomial series. Put
S_j=sum_c n_c*zeta^(cj). Logarithmic differentiation gives

    b_0=1,
    b_i=-sum_(j=1)^i S_j*p^(j-1)*[(i-1)!/(i-j)!]*b_(i-j).

It follows by induction that b_i belongs to O and

    b_i = rho^i mod pO.                                   (12)

For i<p, i! is p free, so p^i*a_i is integral. For the chosen h,
(12) and 2h<e give the exact equality

    v_lambda(b_h)=2h,
    v_lambda(p^(h-1)*a_h)=2h-e<0.                         (13)

This verifies the particular nonvanishing required by the argument.
An arbitrary nonzero rho modulo p would not justify (13), since O/pO
has nilpotents.

### 3.4 All-embedding remainder, both ordinary signs

Assume the actual (D) has p^2|X. By (AI), choose an integral nu with
nu^p=(1-zeta*X)^Theta. Its p-th root in K is unique up to mu_p; because
Theta is real and p is odd, its unique real root also belongs to K and
is integral. Evenness gives sum_c c*n_c=0 mod p and ph even. Factoring
each 1-zeta^c*X at infinity, and pairing c with -c, shows that this
real root is

    nu = X^h*F(1/X).                                      (14)

This identity follows by equal p-th powers and realness; it does not
choose a real root separately at incompatible embeddings. Galois
conjugation of Theta preserves its weight, positivity and realness.

For any conjugate series, absolute coefficients are majorized by those
of (1-T)^(-h). One may prove this factor by factor using
|binom(a,i)| <= (a)(a+1)...(a+i-1)/i! for a>=0. The Taylor tail at
|T|=1/U is therefore at most

    binom(2h,h+1)*U^(-h-1)*(1-1/U)^(-2h-1).               (15)

Suppose U >= (4p)^h. Then U>4h+2, since h<e/2 and p>=7. Bernoulli's
inequality gives (1-1/U)^(2h+1)>1/2. Also
binom(2h,h+1)<4^h/2. All conjugates of the algebraic integer

    R=p^h*nu-sum_(i=0)^h p^h*a_i*X^(h-i)

have absolute value strictly less than (4p)^h/U<=1. The integer R
must vanish. After division by p, every term in the resulting identity
is integral except possibly p^(h-1)*a_h: for i<h the factor
p^(h-1-i)*b_i/i! is integral. Hence that last term is integral too,
contradicting (13). We have proved

    U < (4p)^h < (4p)^(e/2)                               (16)

in the needed center-0, s>=2 sector, with both ordinary signs included.

Two literal source-proof shortcuts have been avoided: the false
general inference that a nonzero ramified residue has nonzero powers,
and the unqualified estimate (1-1/U)^(-2h-1)<2 for every U>2. The latter
estimate is used here only under the contradiction hypothesis
U>4h+2. These are not asserted counterexamples to the published height
theorem; (9)--(16) supply the needed instance explicitly.

## 4. The two actual norm-height contradictions

First note Y<U for every (D). If X=U>=2, then
(U^p-1)/(U-1)<U^p. If X=-U, then
(U^p+1)/(U+1)<U^p. Taking the positive p-th root gives the claim.
This uses ordinary absolute value, not a p-adic size comparison.

Suppose (C) holds and the center in NI is 0. Since s>=2, (4) gives

    Y > p^p/2^e.

But (16), or the published HB0, gives Y<U<(4p)^(e/2). Their ratio is

    [p^p/2^e]/[(4p)^(e/2)]
      = p*(sqrt(p)/4)^e >1                               (17)

for p>=37. This is a contradiction. If the original actual residue
X=0 mod p had depth 1, NI already contradicts (C); therefore the whole
actual X=0 mod p sector satisfies GR1.

Now suppose (C) holds, the center is -1, and s>=3. Equation (4) yields

    Y > p^(2p-1)/2^e.

Published HB- gives Y<U<4*(p-2)^p<4*p^p. The ratio of the displayed
lower bound to 4*p^p is

    p^(p-1)/2^(p+1) = (p/2)^e/4 >1                        (18)

for p>=37. Again this is a contradiction. NI leaves only center -1
and s=2, which is precisely (5). This proves GR2 with its explicitly
attributed external height input. Negative X causes no change in
(17), (18), NI, or the signed statement HB-.

There is no contradiction from the same comparison at s=2 near -1:
the lower bound p^p/2^e is below 4*(p-2)^p for p>=37. Indeed
(1-2/p)^p>1/16 for p>4: the real function
t*log(1-2/t) is increasing for t>2, since its derivative is
log(1-z)+z/(1-z)>0 for z=2/t in (0,1). Its value at t=4 gives 1/16.
Thus the ratio 4*(p-2)^p/[p^p/2^e] exceeds 2^e/4>1.
No failure of one bound to contradict another is promoted to an
existence statement.

## 5. The actual relative-kernel class

For every (D), (1) gives [A]^p=1. Therefore D_A^p=1 and
j(D_A)=D_A^-1. If the actual solution is outside (5), GR1/GR2 and NI
show that (C) is impossible, so D_A is nontrivial and has exact order
p. This is a class of the ACTUAL solution, not a class engineered in a
fixed field independently of X.

The ideal norm from K to Kplus is unchanged by j. Consequently
N(D_A)=1 in Cl(Kplus), proving (6). Let B=Cl(Kplus), C_K=Cl(K),
and let i:B->C_K be extension of ideals. Norm followed by extension
is not being confused with the other composite: the needed identity is

    N(i(b))=b^2 for b in B.                                (19)

It holds also at ramified primes, by the usual norm of an extended
ideal in a degree-2 field extension. Thus the cokernel of
N:C_K->B has exponent dividing 2. At the odd prime p it has no p
part, and

    v_p(|ker N|)=v_p(h_K)-v_p(h_Kplus).                    (20)

The order-p class in (6) makes the left side positive, proving (7).
This does not assume injectivity of i, Vandiver, or a class-number
table. A sufficient hypothesis excluding these actual sectors is that
ker N has no element of order p; it is not asserted for arbitrary p.
The familiar relative-class-number interpretation is only an
attributed terminology, not a new class-number theorem.

## 6. What remains and failed genuine approaches

* The entire unbounded-cofactor sector at exact depth 2 near -1 with
  (C) remains open. The two true inequalities leave a genuine interval.
  A lower trace calculation or a stronger global phase restriction
  would have to supply a new bound; it is not present here.
* Nontrivial minus p classes are not forbidden. GR3 forces one from an
  actual solution in the other sectors, without proving that such a
  class is impossible in the field. Regular-prime consequences are
  already covered by published class-number methods; no newly solved
  prime range is claimed.
* More local depth cannot force (C). Accepted R10 gives actual local
  roots in all its residual classes, so a local approximation or an
  arbitrary formal Jacobi element cannot replace the global condition.
* The canonical J/H in NI were not identified with DR8's ordinary
  cofactor partition. Their primewise phase is not the ordinary
  multiplicative order of X or the disjoint support of its components.
* Pairwise disjoint ideal representatives, conjugation norm 1, or a
  small ideal norm do not by themselves give principality. Even a
  forced unit cofactor ideal would first give a class conclusion, not
  automatically a Diophantine contradiction.
* Products of DR8's support lower bounds do not give an upper support
  bound at unbounded c. No input/history/ideal data were treated as
  ordinary distinct solutions.
* Source Theorem 4 and its Section 5 lower-trace proof were read for
  the possible stronger bridge, but are not imported or extended from
  the published Vandiver hypothesis to (C). Coefficient orders in a
  normalized local root must be checked independently before such a
  strengthening. No assertion that the published theorem is false is
  made here.
* The center--1 part uses published HB-. We read its complete operative
  original upper-bound section and the later Appendix 5.1. The latter
  explicitly details a first-case matrix argument and refers to a
  similar second-case adaptation; this packet does not claim a new
  complete matrix proof of HB-. GR1 has the separate proof above.
* Distinct-prime exclusion results cannot be substituted at q=p. The
  2026 Chen--Mihailescu distinct-prime theorem is not imported. The
  coordinator's formal higher-trace warning is unverified context and
  is not a premise or an actual Jacobi counterexample.
* The actual inequalities use no valuation cutoff, bounded prime
  search, residue lifting inference, abstract ideal countermodel, or
  assumed high contact from norm 1. Publication overlap of the new
  ideal-specific corollary and positive selection remains open.

## 7. Complete proof obligations and constructor dispositions

Every row is a candidate constructor check, not an independent review.

| ID | Obligation and exact disposition |
|---|---|
| O01 | Official B4(b) only; (D) is a restricted signed sector, term count p and degree p-1. Matched. |
| O02 | p>=37 is explicit throughout; no p=3,5,7,17 endpoint import is needed. |
| O03 | Phi_p(X)>1 for both ordinary signs; hence Y>1, not a negative p-th root. Checked in domain and Section 4. |
| O04 | X=1 mod p has valuation 1 and cannot be an actual p-th power. Ordinary and p-adic domains distinguished. |
| O05 | Actual characteristic conjugates are coprime, A integral/unique and N(A)=Y. No formal representative substitution. |
| O06 | (C) is actual equality of classes, not ideals or units. No local implication assumed. |
| O07 | NI is taken from complete currently accepted R10 with BOTH authorities; canonical integrality and strict norm bound retained. |
| O08 | Actual center a in {0,-1}, finite s>=2, c>0 p-free and epsilon sign are exactly NI, with no c upper bound. |
| O09 | HB statement matches signed integers, p>=17 and source eta=0; both signs and center choice checked. |
| O10 | HB- is an external published import; operative proof reading and lack of full external recertification stated literally. |
| O11 | AI is precisely the regular epsilon2/epsilon4 primary annihilation consequence; no Vandiver assumption. |
| O12 | B2 and B4 are p units for p>=7; idempotent convention uses c^-i after reindexing. |
| O13 | 1-zeta*X is the correct primary number at center 0, and local U_(2e) membership implies it is a p-th power locally. |
| O14 | Canonical n_c(u) are nonnegative, even in c and nonzero as a vector for all u. |
| O15 | S(u) is a positive multiple of p, by both power sums; h exists without numerical selection. |
| O16 | Averaging is over all u algebraically and gives average e^2/(2p)<e/2, not a finite experiment. |
| O17 | Constant and linear lambda coefficients are divisible by p; quadratic coefficient exactly 1/2 mod p. |
| O18 | All higher lambda terms have valuation >=3; v_lambda(rho)=2 and 2h<e are exact, not just lower bounds. |
| O19 | Coefficient recurrence proves b_i integral and b_i=rho^i mod pO, including the ramified nilpotent issue. |
| O20 | i! is p-free for i<=h<p; v_lambda(b_h)=2h<e gives the nonintegral last coefficient. |
| O21 | The global real p-th root in O is selected coherently, and (14) follows from equal p-th powers and realness for both X signs. |
| O22 | Coefficient majorization and (15) apply at every embedding with the same h. |
| O23 | The denominator estimate <2 is used only at U>4h+2, implied by U>=(4p)^h, not for all U>2. |
| O24 | R is integral, every conjugate has absolute value <1 including equality at U=(4p)^h, hence R=0. |
| O25 | Division by p leaves all i<h terms integral and contradicts exactly v_lambda(p^(h-1)a_h)<0. |
| O26 | GR1 ratio (17) is >1 for all p>=37 and depth 1 is discharged separately by NI. |
| O27 | GR2 uses s>=3 and (18)>1 for all p>=37; it does not use a bounded-depth enumeration. |
| O28 | Exact depth 2 near -1 remains unexcluded; the monotonic real-function calculation explicitly verifies the numerical gap. |
| O29 | D_A is the actual class difference, killed by p, nontrivial outside (5), inverted by j, and has exact order p. |
| O30 | Relative norm kills D_A; N composed with extension is square on Cl(Kplus), so its cokernel has no odd-p part. No extension injectivity presumed. |
| O31 | Class-number consequence (20) has correct kernel/cokernel direction, ordinary finite class groups and no regularity assumption/table. |
| O32 | No annual solution, prime range, stronger height, automatic class triviality, local-to-global converse, or priority claim; DR8/root warnings are not hidden premises. |

## 8. Literal source, role and worklog record

Fresh operative reads in this construction: official 2025 setup and B4(b)
in the original Paper B; complete local statement; complete accepted R10
and DR8 bodies and EACH of their current acceptance MD/JSON; current
2025 research-map frontier as a mutable dated observation. Old roles:
A constructed DR8 and reviewed R10 WHOLE1; these are accepted-input
roles, not fresh independent self-certification. Root supplied only the
generic research target, no new proof inference or positive-selection
step. No NEW R23 peer files, actual inventories, hashes, findings, or
metadata were accessed during this construction.

Primary source reads were bounded web text/PDF text, not CUA or a native
browser. In the Mihailescu author-posted text: complete introduction and
Theorem 3 hypotheses; complete Section 2.5/Lemma 5/lifts and the relevant
Section 2.6 primary-number setup; COMPLETE operative Section 4, including
Lemmas 10--14 and its general, center-0, first-case and second-case
arguments; and COMPLETE Section 5 for a failed stronger bridge. In
arXiv:1412.5798: opening/version/Remark 1.4; complete Theorem 2.2
statement; COMPLETE Appendix 5.1 lemma, proof and application. Other
parts of that paper, Washington's book and the complete reflection
proof were not freshly read. Source JSON records precise line/page
windows and the import boundary; no inherited source reading is claimed.

The chapter's publication DOI is
https://doi.org/10.1007/978-3-211-74280-8_15 ; author-posted full text:
https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren .
Later source: https://arxiv.org/pdf/1412.5798 . No third-party binary was
downloaded in this rotation; binary hashes and final-publisher byte
identity are unavailable. No full third-party text is redistributed.

Work sequence: narrow unused-prefix check; complete operative-input and
official/source reading; hand norm-height comparison; source selection
and coefficient repair; class-norm-kernel argument; adversarial signed,
depth, ramification and inequality checks; complete draft and 32
obligations; metadata-only freeze/full readback/separate verification.
The one guessed source filename
`coordinator-diagonal-firstcase-sources-v1.md` did not exist; the exact
RD source file was then read. No mathematical result depended on that
failed path. All network calls completed promptly; no stalled job,
native subprocess, approval, purchase, contact or bypass occurred.

The last direct account-wide observations before drafting were 71%
TOTAL at 2026-10-18 23:29:50 and 23:31:27 UTC, reset 1792874445,
10080-minute window, ordinary usage allowed. The authorized ceiling is
90% TOTAL with integration/review reserve and no automatic later-window
spending. Final telemetry is recorded in the freeze metadata.

Documentary preparation verified 66 necessary fingerprint occurrences
on 63 paths. Before freezing, the NEW unfrozen baseline was compacted
to exact current authority and immediate-parent bindings, counts and a
deduplicated digest, with explicit reconstruction code. No growing
historical path list was recopied; no external old byte was modified.
The 23:40:10 UTC direct recheck remained 71% TOTAL in the same window.
The first final-draft readback caught and corrected a local-filtration
index (U_2^p=U_(e+2), not U_(e+1)) and changed the strict elementary
comparison's auxiliary endpoint from p>=4 to p>4. Both corrections
precede the immutable freeze; neither changes the target p>=37 domain.

No substantive constructor objection is suppressed. The remaining
depth-two/global-class questions and external HB- proof-import boundary
are explicit. This packet must receive two OTHER complete initially
blind adversarial audits before coordinator promotion.
