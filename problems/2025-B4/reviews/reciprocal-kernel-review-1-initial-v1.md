# RK1–RK3: initially blind independent nonconstructor whole R1

2026-10-17 UTC. Reviewer `/root/review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; independently verified effective settings unknown.
Target9541B, SHA256
`4c752f3ca4699ea0c184dbb79d79f9f192182cc91aeac7fd8a459b7b8bea49b8`.

I reconstructed the WHOLE packet and all eight obligations, including
visual inspection of the actual primary Hasse theorem and all six
printed pages. No substantive defect or required author repair was
found. I recommend exact RK1/RK2 and the conditional RK3 application
after the other complete independent audit and coordinator reconciliation.
I do not promote the candidate or prove a new Diophantine conclusion.

I previously whole-reviewed PG/CF1, FS and OW, and completed a separate
initially blind UW whole R1 immediately before this audit. None of
those roles constructed NEW RK or supplied the cotangent-kernel route.
The UW report and all older bytes were frozen before RK was first read.
Root is the RK constructor and cannot count as an independent reviewer.
No new RK peer report, conclusion or later root inspection was read
before this complete initial freeze. No new UW existence is imported
as accepted merely because my own first audit recommended it.

## Source premise and exact field

For each odd prime p the real cotangents cot(pi*a/p),
1<=a<=(p-1)/2, are Q-linearly independent. Hasse's original p275
states the general cotangent conclusion using the class-number formula;
the later special cases concern elementary proofs. No regular-prime
hypothesis appears. The source record gives exact visual read limits.
The classical analytic input is attributed, not reproved here.

The modern primary cross-check's r=1,k=1,q=p,K=Q specialization
has the same rational coefficients and representative set. Its stronger
number-field and multiple-series statements are not needed. The unseen
reference proof of its r=1 base case is not claimed reconstructed.

Rationality matters. The proof below concerns Q[G], not arbitrary
K=Q(zeta) coefficients or reduction modulo p. The factor i need not
belong to K: a purely imaginary expression i times a real cotangent
sum can still be an element of K. No field-membership assertion about
each unscaled real cotangent is required by the kernel argument.

## RK1: both inclusions in the full kernel

Write z=zeta^a, with z!=1 because a is a nonzero residue. Then
1/(1-z^-1)=-z/(1-z). Hence the pair sum is1 and the pair
difference is(1+z)/(1-z). With z=exp(2ix), x=pi*a/p, dividing
the numerator and denominator by exp(ix) gives i*cot(x), with the
POSITIVE sign. All denominators are nonzero.

For even eta, opposite coefficients both equal n_a. Pairing gives
L(eta)=sum_(a=1)^((p-1)/2)n_a=wt(eta)/2. Thus every even
zero-weight rational vector is in ker L. This implication is exact
and uses no integral positivity, module membership or moments.

For odd eta, opposite coefficients are -n_a. Pairing by differences
instead gives

    L(eta)=i sum_(a=1)^((p-1)/2)n_a cot(pi*a/p).

The coefficients n_a are rational. The imported independence theorem
therefore makes L injective on the ENTIRE odd subspace, not just on
a sparse or positive subset. This is the additional source premise
absent from the older globally nonfaithful reciprocal-map discussion.

For an arbitrary rational vector eta, division by2 produces its even
and odd parts eta_+,eta_-. It is legitimate in Q[G] for this linear
analysis, but is not an integral-module witness construction. The even
image is rational and hence real. The odd image is purely imaginary.
Their sum can vanish only if both vanish. Odd injectivity gives
eta_-=0; the even formula gives wt(eta_+)=0. Thus eta is even with
weight0, proving the converse and the ENTIRE stated kernel.
Multiplication by the fixed nonzero1-zeta gives precisely the same
kernel for R_1. There is no use of Fourier faithfulness in this proof.

The boundary checks agree. At p=3 an even vector has two equal
coefficients and weight twice either, so the even weight-zero kernel
is zero. At p>=5 the four indices1,-1,2,-2 are distinct. Their
displayed pair difference is nonzero, even and of weight0 and is
therefore killed by L and R_1. This preserves the old global kernel
warning. The resulting kernel has one dimension fewer than the even
subspace; no unaccounted odd kernel remains.

## RK2: the exact fixed-complement restriction

Suppose theta+jtheta=eta+jeta=C*N in Q[G], with the SAME rational C.
Then delta=theta-eta satisfies jdelta=-delta. Consequently equality
of L(theta),L(eta) implies delta=0 by the just-proved odd injectivity;
the converse is immediate. This proves injectivity on that entire
affine space, without a coefficient or moment restriction.

The SAME complement condition is substantive. Equal augmentation
alone would not suffice: the nonzero even zero-weight counterexample
can be added without changing augmentation or L. The proof does not
make that stronger assertion. Positivity alone also cannot replace
the fixed-complement equation.

Because G is abelian, multiplication by sigma_c commutes with j;
sigma_c N=N. Thus every translate of theta or eta still belongs to
A_C. For ARBITRARY c,d, equality of R_c(theta),R_d(eta) cancels the
one common nonzero prefactor1-zeta, leaving equality of L on those
two translated vectors. Injectivity on A_C then yields exactly
sigma_c theta=sigma_d eta, with the reverse implication immediate.

If theta,eta are nonconjugate, such an equality cannot hold for any
c,d, so their reciprocal value SETS are disjoint. For a single theta,
two array entries coincide precisely when the corresponding translates
coincide. Trivial group-ring stabilizer therefore gives p-1 distinct
array values, and a nontrivial stabilizer gives an actual collision.

The additional assertion concerning L's true Galois orbit also checks:
rational coefficients are fixed, and sigma_h sends each denominator
1-zeta^a to1-zeta^(ha), so sigma_h L(theta)=L(sigma_h theta).
Its Galois stabilizer agrees with theta's by the same A_C injectivity.
However sigma_h R_1(theta)=(1-zeta^h)L(sigma_h theta), whereas
R_h(theta)=(1-zeta)L(sigma_h theta). The varying prefactor prevents
identifying the latter array with the former actual conjugate list.
The candidate keeps this distinction and only uses the common-scaled
L-orbit's equality pattern. No false Galois normalization is needed.

## RK3: actual pair hypothesis, not a new existence theorem

Assume two ACTUAL positive integral I_f elements with complement2N,
nonzero M_1 and nonconjugacy. Their augmentation is p-1: augmentation
of theta+jtheta=2N gives2wt(theta)=2(p-1). The accepted direct
reindexing law M_1(sigma_h theta)=h^-1 M_1(theta) makes each exact
stabilizer trivial. This calculation is for integer vectors with a
defined nonzero F_p moment; it does not extend that functional to
arbitrary rational vectors with a p-divisible denominator.

Now RK2 applies with C=2 to EVERY pair of translated vectors.
It gives two disjoint reciprocal arrays, each of p-1 distinct values,
at the unchanged ORIGINAL augmentation p-1. Positivity and I_f
membership are retained hypotheses; rational averaging was used only
for the RK1 kernel calculation and creates no new witness.

The separate UW candidate supplies a proposed universal pair for
p>=37, but this packet explicitly conditions that corollary on UW
acceptance. My earlier UW whole R1 is context, not a second audit
or a promotion. RK1/RK2 do not require UW's cubic/fifth calculations.
There is no circular premise or silently assumed universal selection.

Even disjoint complete reciprocal lists do not by themselves supply
arbitrary higher-binomial-series rank, Jacobi normalization/integrality,
augmented singular-system estimates, cancellation in every conjugate,
nonzero delta or the required archimedean bounds. These are separate
source-application obligations, retained by the candidate. No signed
integer Nagell–Ljunggren exclusion, full annual answer or novelty is
asserted. The earlier global-kernel counterexample and narrow accepted
MS scopes remain correct and unchanged.

The separate ledger contains thirty-two inference checks covering all
eight end obligations. The conclusion follows from the exact published
rational theorem and the full new kernel/restriction argument, not
from isolated local checks, numerical examples or a higher-weight
substitute. No mathematical program, CAS, scan, certificate replay or
author rerun was used. The original source scan was read visually;
administrative hashes are integrity only. Only this review prefix was
written, and the candidate and all older own packets are preserved.
