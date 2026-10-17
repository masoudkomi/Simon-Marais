# Whole initially blind R2: exact reciprocal kernel RK1–RK3

2026-10-17 UTC. Reviewer: /root/review_2017_coarsening_r1.
Requested gpt-6.1-sol/max; effective-setting readback unavailable.
**Complete whole initial; coordinator reconciliation pending.**

Exact target: notes/coordinator-reciprocal-kernel-return-v1.md,
9541B, SHA2564c752f3ca4699ea0c184dbb79d79f9f192182cc91aeac7fd8a459b7b8bea49b8.
The ENTIRE candidate, all eight end obligations, embedded source/retrieval
scope and complete four-record manifest were read. The accepted MS body
and exact current UW candidate had been fully read before this audit.

My UW whole R2 initial was COMPLETELY FROZEN before opening this target.
No new RK peer report/finding or later coordinator disposition was read
before this entire RK initial freeze. I did not construct RK. Older FS
authorship and MS/OW/UW audit roles are disclosed; those do not count as
independent re-certification of any own background. Root is RK's author
and cannot be either independent reviewer.

No mathematical program, CAS, scan, sample, certificate replay or author
rerun was used. The four existing Hasse rendered spreads were visually
read; file hashing is administrative, not mathematical evidence.

## Verdict and exact scope

I find no substantive defect in RK1–RK3. All eight obligations pass
in their stated scopes: RK1 classifies the entire Q-linear kernel,
RK2 gives exact injectivity on a fixed-complement affine space, and
RK3 is conditional on an ACTUAL pair with its written hypotheses.
Universal UW existence is not silently promoted by this audit.

The cotangent independence input is published background, verified
in the original source with its unrestricted odd-prime scope. It
is not a new proof of that analytic theorem or an application of
ordinary Fourier faithfulness to a different map. No higher-series
rank or Diophantine exclusion is established by reciprocal separation.

## 1. Domain, maps and coefficient fields

Fix an ODD PRIME p, zeta=exp(2pi i/p), G=F_p^*, j=sigma_(-1),
N=sum_a sigma_a, and DIRECT sigma_a(zeta)=zeta^a. For rational
coefficients define

    L(sum n_a sigma_a)=sum n_a/(1-zeta^a),
    R_c(theta)=(1-zeta)L(sigma_c theta).

All denominators are nonzero because a is nonzero modp and zeta
has order p. The codomain is Q(zeta), while L is only asserted
Q-linear. The cotangent independence is over Q, not over the
cyclotomic field itself. This distinction is necessary.

The prefactor1-zeta is exactly the SAME nonzero number for every
index c in the R array. No group-ring product is confused with
evaluation by L. All later integral moments in RK3 are defined
on actual integral elements, not on arbitrary rational vectors
with denominators possibly divisible by p.

The official2025 B4(b) remains the all-integer geometric-sum
equation with degree n and n+1 terms. The present kernel result
has no x,y parameter and provides only auxiliary algebra.

## 2. Imported cotangent theorem, original source check

The imported statement is: for every odd prime p, the real
numbers cot(pi a/p),1<=a<=(p-1)/2, are Q-linearly independent.

I visually read ALL six printed pages275–280 of Hasse,
On a question of S. Chowla, Acta Arith.18(1971), including
the displayed theorem, character-matrix proof, the general
cotangent conclusion from the relative class-number formula,
the separate elementary cases and final addendum. The
general cotangent assertion is not confined to those cases;
no regular-prime or class-number divisibility condition occurs.
The classical analytic input is accepted as published, not
reproved by this audit.

As a cross-check, Hamahata2020 Theorem1.1 and full Theorem2.1
proof were read in the primary PDF. The relevant specialization
is ONE modulus q=p, derivative order0 (k=1), coefficient field
Q and T={1,...,(p-1)/2}. Phi_p is irreducible over Q, and T
together with -T is the full set of unit residues. This checks
its actual hypotheses without asserting independence over
Q(zeta) or importing its multiple-series conclusions.

## 3. Reconstruct the full kernel RK1

For u=zeta^a, elementary algebra gives

    1/(1-u^-1)=-u/(1-u),
    1/(1-u)+1/(1-u^-1)=1,
    1/(1-u)-1/(1-u^-1)=(1+u)/(1-u).

Writing u=e^(2it), t=pi a/p, the last ratio is i cot(t),
with the positive sign: its denominator is -2i e^(it)sin t
and numerator2e^(it)cos t. No convention change from direct
a to inverse a is made.

If eta is even under j, its coefficients satisfy n_(-a)=n_a.
Pairing a,-a gives

    L(eta)=sum_(a=1)^((p-1)/2)n_a=wt(eta)/2 in Q.

Thus every even zero-weight vector lies in the kernel.

If eta is odd, n_(-a)=-n_a, and pairing by differences gives

    L(eta)=i sum_(a=1)^((p-1)/2)n_a cot(pi a/p).

There is no extra factor2: both members of each pair are already
included in this difference. The coefficients n_a are rational,
so the imported theorem makes this zero only if every n_a=0.
L is therefore injective on the ENTIRE odd rational subspace,
without positivity, module or moment assumptions.

For arbitrary eta, its rational parity decomposition is

    eta_+=(eta+j eta)/2, eta_-=(eta-j eta)/2.

This decomposes a rational vector for ANALYSIS; it does not
construct integral module witnesses by dividing them.
L(eta_+) is rational/real, whereas L(eta_-) is purely imaginary.
If L(eta)=0, real and imaginary parts vanish separately.
Odd injectivity gives eta_-=0, and the even formula gives
wt(eta_+)=0. Hence eta is even and has weight0. Combining
both inclusions proves

    ker L={eta in Q[G]: j eta=eta, wt(eta)=0}.

Multiplication by1-zeta does not change the kernel, so this
is also the exact kernel of R_1. No global faithfulness
claim for L or R_1 is made.

## 4. Degenerate primes and the retained counterexample

At p=3 there is just one opposite pair. An even vector has
equal two coefficients, and weight0 forces both zero.
Thus the kernel formula correctly gives kernel0. The one
cotangent is nonzero, so odd injectivity has no exception.

For p>=5, the four indices1,-1,2,-2 are distinct. Therefore

    (sigma_1+sigma_(-1))-(sigma_2+sigma_(-2))

is a NONZERO rational/integral vector, even and of weight0.
Its two reciprocal pair sums are both1, so it lies in the
kernel. At p=3 the displayed expression collapses to zero;
the candidate correctly restricts the counterexample.

This shows that the accepted older warning about a nonzero
global reciprocal kernel survives. Restricted injectivity
below is an additional theorem, not a contradiction of it.

## 5. Fixed-complement injectivity and arbitrary indices RK2

Let C be fixed in Q and

    A_C={theta in Q[G]: theta+j theta=C N}.

For theta,eta in A_C their difference delta satisfies
delta+j delta=0 and hence is odd. If L(theta)=L(eta),
odd injectivity gives delta=0; the converse is immediate.
Thus L is injective on this affine space.

Every G translate remains in the SAME A_C, because G is
abelian, j commutes with every sigma_c, and sigma_c N=N.
For ANY c,d in G, cancellation of the COMMON prefactor
1-zeta therefore gives

    R_c(theta)=R_d(eta)
      iff L(sigma_c theta)=L(sigma_d eta)
      iff sigma_c theta=sigma_d eta.

This is equality of algebraic numbers, not a congruence
test or a claim about their residues.

Consequently two nonconjugate elements in one A_C have
disjoint reciprocal value SETS. An element's array has
p-1 distinct entries precisely when its group-ring
stabilizer is trivial. More generally equality of two
entries is exactly the corresponding stabilizer equality.

Rational coefficients are fixed under Galois automorphisms,
so

    sigma_h L(theta)=L(sigma_h theta).

It follows on A_C that the ACTUAL Galois stabilizer of
L(theta) equals the group-ring stabilizer of theta.
R_c(theta) has the same equality pattern as this L orbit,
by the common scaling. However,

    sigma_c R_1(theta)
      =(1-zeta^c)L(sigma_c theta),

with a different prefactor. The R array is therefore
not generally the Galois-conjugate list of R_1. No false
normalization identity is used.

## 6. Reconstruct exactly the conditional application RK3

Assume an ACTUAL pair theta_1,theta_2 of positive integral
I_f elements, not G-conjugate, with

    theta_i+j theta_i=2N, M_1(theta_i)!=0.

Augmentation gives2wt(theta_i)=2(p-1), hence original
weight p-1 in Z. Both belong to A_2. The accepted moment
law, directly rederived by index multiplication, gives

    M_1(sigma_h theta_i)=h^-1 M_1(theta_i).

An exact stabilizer equality forces h=1 since M_1 is
nonzero. Thus each element is free. RK2 now gives p-1
different values in EACH reciprocal array and disjoint
value sets ACROSS the two arrays.

Positivity, integrality and module membership are part
of the assumed actual pair; the rational parity
decomposition in RK1 is not used to produce or average
such elements. No saturation or division in I_f occurs.

The separately frozen UW candidate proposes exactly such
a pair for every p>=37. This audit treats that application
as CONDITIONAL on UW's separate acceptance, as the target
does. RK1/RK2 are independent of the UW moment construction.
The fact that this reviewer has now frozen a UW audit is
not a substitute for coordinator acceptance after both
UW audits.

## 7. Source provenance, read limits and preserved firewalls

Hasse's cached primary PDF is520142B,
SHA5536c10633a189e98ad59a2fee0a1dc1d9a760263b66bd5b6d35277a8e5758a3.
It has FOUR scanned two-page spreads. The first/final spreads
also contain adjacent articles' pages274 and281; those are
not Hasse pages or part of the theorem being imported.
The existing images /private/tmp/smmc-hasse-1.png through
-4.png were viewed at original detail, covering275–280.
No OCR text or empty pypdf extraction is claimed as a
source read. The PDF read-only skill was used; no PDF
authoring, new download or shared cache modification occurred.

Hamahata's primary web PDF was read through complete
§2.1, including the proof and its reference-based r=1
starting point. I do not claim to have independently
reproved that base reference or to need its stronger
number-field/multiple-series results. The Hasse
original supplies the exact sole imported theorem.

The complete MS accepted exposition and the entire
UW candidate were already read in the preceding full
audit, and their exact hashes are checked here.
MS global-kernel warnings remain true; the new theorem
uses the additional cotangent independence input.
No Fourier-injectivity transfer is asserted.

Set separation does not prove the source-specific
Jacobi normalization, integral cofactors, higher-jet
rank, augmented singular-system estimates, EVERY-
conjugate cancellation, nonzero delta or archimedean
bounds. It neither proves nor refutes the unrestricted
signed Nagell–Ljunggren theorem. No novelty or full
annual conclusion is claimed.

## 8. Complete initial disposition

All eight author obligations were independently
reconstructed, through22 ledger checks. No substantive
defect or required author repair was found. This is
a scoped pass recommendation, not promotion.

The entire main report, issue ledger, source record,
metadata and hash manifest were frozen before any
new RK peer finding was read. Older own bytes and
all four declared author input records remain
unchanged. No mathematical computation or author
rerun supplies any of the conclusions.

