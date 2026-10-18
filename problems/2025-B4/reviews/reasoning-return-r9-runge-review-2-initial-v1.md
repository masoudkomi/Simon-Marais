# Runge-cover RG1–RG3: initially blind whole review R2

2026-10-18 UTC. Reviewer A, `/root/review_2021_reasoning_j15_r2`.
**Complete initial whole audit; no substantive defect or required repair found.**
This is a review recommendation for the exact scoped RG1–RG3 candidate, not
promotion. Two OTHER whole audits and the coordinator's full reconciliation
remain the protocol for acceptance. The annual problem is not solved here.

Target: `problems/2025-B4/notes/reasoning-return-r9-runge-candidate-v1.md`,
16773 bytes, SHA256
`8bcd69dfa97441b23fd456268e655312aea55a0f7a64a5237f0117f6a192b90a`.
Constructor freeze: 2364 bytes, SHA256
`cb5073bbce53c07b12e5b253af51f278ebd6475c0600d700bef6a9064a7ec32b`.
All eight payloads, the constructor freeze, and all 34 obligations were read.
No new root Runge R1 report, ledger, source record, manifest or findings was
opened or hashed before this complete initial freeze. The root's completion
identity alone was received. There was no mathematical program, scan, CAS,
certificate replay, author rerun, new source download, cache mutation or Git
operation. The administrative freeze only reads declared files and hashes
bytes. Requested inherited settings are gpt-6.1-sol/max; independent effective
setting readback is unavailable.

I previously reviewed 2025 FS/OW/UW/RK work. I did not construct this Runge
packet or its accepted R6/R8 inputs, and supplied no new Runge inference.
Constructor C's older R6 authorship is disclosed in the target. In this audit
I read both accepted bodies and their acceptance records in full for their
operative interfaces. Their independent acceptance is imported, not newly
self-certified. The older unverified R9 packet is an immutable parent only;
none of its claims or peer reviews is a mathematical premise. My own 2021
R12 constructor packet is likewise a preservation parent, not a premise.

## 1. Exact result and arithmetic interface

The official 2025 B4(b) asks about the degree-n geometric sum with integer
variables and n,q at least 2. This packet treats only

    Phi_p(X) = Y^p, p >= 37 prime, |X| >= 2,
    Phi_p(T) = 1 + T + ... + T^(p-1).

Thus the official degree is p−1 and the official exponent is p. The sign of
X is unrestricted. The accepted R6 interface gives Y>1 and the exact
normalized Jacobi lift. The packet does not reproduce preliminary part (a).

For K=Q(zeta_p), O=Z[zeta_p], it fixes theta once for each p, before any
solution, with canonical coefficients n_a in {0,1,2}, total weight p−1,
theta+j theta=2N, F(theta)=0 and M_1(theta) nonzero. One accepted R8A
representative suffices; its existence for every p>=37 does not depend on
a hypothetical solution. The accepted R6/R8 interfaces give an ACTUAL
beta in O with

    beta^p = product_a (X-zeta^a)^(n_a).

This is an equality with twist 1. The matched-prime Jacobi construction,
original weight and lambda^2 normalization are essential imported data.
The accepted argument first forms the appropriate fractional products,
then obtains a positive integral final ideal. It removes the remaining
unit using its archimedean absolute values and the normalization. It does
not merely assert a root over an extension or for an arbitrary half-weight
vector. I checked the relevant endpoints of the complete R6 body as well
as the complete R8 body. A phase-free cover chosen without this arithmetic
input would not justify the proof below.

The proposed output is a finite, solution-independent procedure for a
p-dependent bound B(p) on |X|. Its coefficients are not evaluated. It is not
a bound on p, a proof of nonexistence, an improvement on published heights,
or a proof that a previously selected single delta is nonzero.

## 2. RG1: function field and actual point

Let P_theta(T)=product_a(T-zeta^a)^(n_a) and consider

    W^p=Phi_p(T), U^p=P_theta(T).

The vectors 1 and n are independent over F_p. In a dependence with a
nonzero coefficient of n, the n_a would all be the same residue. Their
sum is p−1, so that residue is 1. Because 0<=n_a<=2<p, all n_a would
actually equal 1. Then theta=N and M_1(theta)=sum_a a^(-1)=0 in F_p,
contradicting the hypothesis. A dependence with coefficient of n zero is
trivial. Valuations at T=zeta^a now exclude every nontrivial p-th-power
relation between the two radicands, even over the algebraic closure of K.

For completeness the successive Kummer degree test can be made without
an uninspected general subextension theorem. Adjoin W first. Its cyclic
group acts by W->zeta W. If P_theta became a p-th power v^p in K(T)(W),
the ratio sigma(v)/v would be a p-th root of unity. The eigenspaces in the
basis 1,W,...,W^(p-1) are K(T)W^k. Thus v=c(T)W^k and
P_theta=c(T)^p Phi_p^k, contradicting the valuation independence. A
prime-degree Kummer extension has degree either 1 or p in characteristic
zero with mu_p present. The same reasoning over the algebraic closure
gives geometric integrality. Consequently the field has degree p^2,
Galois group F_p^2 and constant field K.

At (T,W,U)=(X,Y,beta) both W and U are nonzero and X avoids every zeta^a.
The two equation derivatives in W and U give rank 2. This is a smooth
K-point on the affine model. Normalization is an isomorphism there, so
it lifts uniquely to a finite point P of the smooth projective curve C
with P in C(K) and T(P)=X in O. No residue extension or chosen geometric
point is being substituted for P.

## 3. RG1: infinity, conjugation and genus

Both radicands have degree p−1 and leading coefficient 1. At infinity
their ratio is a unit with constant 1, with a formal p-th root over K.
The leading residue of U/W is therefore zeta^c, c in F_p. For each c the
remaining W equation has ramification p because gcd(p,p−1)=1. This gives
exactly p points Q_c over infinity, each with residue field K.

The candidate's displayed parameter is exact:

    T=s^(-p),
    W=s^(-(p-1)) q(s^p),
    U=zeta^c s^(-(p-1)) q_theta(s^p),
    q(t)=(1+t+...+t^(p-1))^(1/p),
    q_theta(t)=product_a(1-zeta^a t)^(n_a/p).

All roots here are the formal roots with constant 1. Also W/T=s q(s^p)
has initial term s, so the completion really is K((s)). Replacing s by
zeta^k s absorbs the possible leading root in W; it does not create p
additional points for a fixed c. Thus ord_Q T=−p and ord_Q U=ord_Q W=−(p−1).

An embedding sigma_a of K maps this curve to its conjugate curve, with
Q_c mapped to the branch labelled ac. I checked this convention explicitly.
There is no assumed automorphism of the original curve with fixed
coefficients. This distinction is needed in the all-embedding count.

At each finite root zeta^a the radicand valuation vector is (1,n_a);
at infinity it is (p−1,p−1). Every vector is nonzero modulo p, and inertia
has order p. No other geometric branch values occur. There are p branch
values, each contributing p(p−1) to tame Riemann–Hurwitz for degree p^2:

    2g−2 = −2p^2 + p(p^2−p),
    g = 1 + p^2(p−3)/2.

As a check, the intermediate curve W^p=Phi_p has genus
(p−1)(p−2)/2. It already has the same ramification p over every branch
value, so the degree-p map from C to it is geometrically unramified and
gives the same genus. Tameness here is geometric in characteristic zero;
no good-reduction assertion at the arithmetic prime over p is needed.

## 4. RG2: simultaneous nonvanishing and global integrality

With d=2g+p−1 put D_c=dQ_c−sum_(b!=c)Q_b. Since all Q_b are K-rational,
deg D_c=2g. Smooth projectivity and geometric integrality give the ordinary
curve Riemann–Roch hypotheses. Both D_c and D_c−P have degree above
2g−2, since an actual K-point P has degree 1. Hence

    l(D_c)=g+1, l(D_c−P)=g.

At any finite P the coefficient of D_c is zero, and L(D_c−P) is precisely
the subspace vanishing there. Any FULL K-basis of L(D_c) therefore has a
member nonzero at P. These functions have their only possible pole at
Q_c and vanish to order at least 1 at every other Q_b. This is the
basepoint statement actually needed; it asserts nothing about an
arbitrarily preselected single function.

The finite morphism T identifies C minus its infinite fibre with the
normalization of A^1 in the function field. A function regular there is
integral over K[T]. Alternatively its product over the p^2 function-field
Galois conjugates supplies a monic equation with coefficients in K(T)
having no finite poles, hence in K[T].

A positive ordinary integer h can clear all finitely many algebraic
coefficient denominators in that equation: express them in the integral
basis 1,zeta,...,zeta^(p−2) and clear their rational denominators. If the
equation for f has coefficients c_j(T), the equation for hf has
coefficients h^j c_j(T), all in O[T]. Evaluating at X in O makes hf(P)
integral over O. Since its value lies in K and O is integrally closed,
it lies in O itself. This includes finite primes above p; no enlarged S
is concealed. Rescaling by a nonzero h preserves every zero/pole and
the full-family nonvanishing property. The function-field monic norm
equation in this step is distinct from the number-field norm used last.

## 5. Exact finite construction, including the cancellation issue

For 0<=i,j<p the candidate defines

    B_ij=U^i W^j / product_a(T-zeta^a)^floor((i n_a+j)/p).

This is indeed a K[T]-basis of the finite normalization ring. The p^2
Kummer characters split the field into K(T)U^iW^j. Their projections
preserve integrality over K[T], because 1/p^2 is a unit of that ring;
this does not assert integrality over O[T]. At T=zeta^a all primes over
that value have ord(T-zeta^a)=p and ord(U^iW^j)=i n_a+j. The displayed
floor is the largest allowed pole order of a rational coefficient.
At any other finite place U and W are units. Consequently an integral
element on each eigenline is exactly a polynomial multiple of B_ij.
Distinct characters give linear independence. Possible arithmetic residue
extensions at a branch do not change these valuations. Affine normality
of the original equations is not assumed.

At Q_c the pole number is

    k_ij=(i+j)(p−1)−p sum_a floor((i n_a+j)/p)
        =sum_a ((i n_a+j) mod p) >= 0,

with k_ij=−(i+j) modulo p and leading coefficient zeta^(ci). The equality
uses sum n_a=p−1 and there being p−1 indices a. This also checks the
ordering of U^i and W^j in the character.

Suppose a polynomial-basis expression has a largest pole number H>d.
Every term with number H has the same i+j modulo p. For a fixed i this
determines the unique j in [0,p−1]; H then determines its polynomial
power h. Across the p points its leading coefficients are a linear
combination of zeta^(ci), i in F_p. The full Fourier matrix is invertible
in characteristic zero. Cancellation at every Q_c would force all
coefficients at H to vanish, contradicting the choice of H. Therefore
every function regular at finite points with all infinite poles bounded
by d lies in the finite span of T^h B_ij with ph+k_ij<=d.

Every member of L(D_c) has that property. In the finite span, imposing
the vanishing of the Laurent coefficients −d,...,0 at each Q_b, b!=c,
is exactly the condition of a zero of order at least 1 there. At Q_c
the existing bound is d. No extra or missing conditions occur. These
are finitely many exact K-linear equations. The formal series above
compute every coefficient required for them. Finite linear algebra,
the monic Galois equations, and rational-integer denominator clearing
thus construct the full scaled bases without a solution as input.

Writing all resulting coefficients in the rational cyclotomic basis
gives the candidate's positive rational

    M=2 max_(c,l) sum_(i,j,h,r) |a_(c,l,i,j,h,r)| 2^(p(h+i+j)).

There is a nonzero basis member, so M>0. The procedure is finite and
exact. It could be very expensive, and no coefficient list, numerical
M or computational efficiency is claimed or tested in this packet.

## 6. RG3: one common unused branch and all conjugates

The series q and q_theta are analytic for |t|<1: all their defining
factors have zeros only on the unit circle. For any complex fibre with
|T|>1, choose s^p=1/T. Multiplying s by zeta^k runs through the p values
of W in the displayed formula. Once W is matched, the p values of U
are distinguished by exactly one branch label. Thus the formula covers
the actual fibre, including negative real X; it is not merely a formal
asymptotic assertion.

For each of the p−1 embeddings sigma_a, the actual point P^sigma_a has
a branch label b_a on the conjugate curve. The pole point sigma_a(Q_c)
has label ac. Exactly one c is forbidden by b_a=ac at that embedding.
At most p−1 labels are forbidden among the p choices. Hence there is
ONE c whose auxiliary family vanishes at the approached branch at
EVERY embedding. Counting a conjugate pair twice only weakens the count.
Choosing a separate c for each embedding would not be enough; that
incorrect alternative is not the argument in the target.

On |s|=1/2, |T|=2^p. For either root product the nonnegative exponents
sum to (p−1)/p<1 and each factor has modulus at most 1+2^(−p)<2.
It follows that |W|,|U|<=2^p. Every denominator |T-zeta^a|>=2^p−1>=1.
For any embedding the absolute value of a coefficient sum a_r zeta^r
is at most sum |a_r|. Therefore every conjugate scaled family member
has modulus at most M/2 on that circle.

At a branch other than its pole, that function vanishes at s=0.
The quotient by s is analytic on |s|<1. The basis expression has no
finite pole in the punctured disc: its possible denominator zeros
occur only at |s|=1. Maximum modulus on the radius-1/2 disc gives

    |sigma_a(F_(c,l)(P))| <= M |X|^(−1/p)

for every a and l when |X|>2^p. The coefficient bound was uniform in
c,l, embedding and branch.

Now choose ONE l whose value at the actual P is nonzero, using the full
family property for the common c. The same algebraic integer is used
at all embeddings, and every conjugate of a nonzero algebraic number
is nonzero. If |X|>max(2^p,(M+1)^p), all of its p−1 conjugate absolute
values are less than M/(M+1)<1. Their product is the absolute value
of a nonzero ordinary integer norm, giving the contradiction. Points
below that threshold already satisfy the asserted bound. Individual
auxiliary zero evaluations cause no missing case.

## 7. Source scope and adversarial checks

The covering form of Runge's method is published background. I freshly
read Levin's Theorems 1.2–1.3 and the complete operative section 2,
including its data/effectivity caveat and proof of Theorem 2.1. Its
effectivity requirements motivate, rather than replace, the finite
construction audited above. No explicit superelliptic Theorem 4.3 or
field-enlarging covering theorem is applied. The source checks record
the exact read limits and additional classical primary statements.

The following possible failures were checked against the entire proof:

- A dependent theta, geometrically split cover, or constant-field
  extension is excluded by valuations, not by a finite example.
- An unremoved zeta twist could change infinity rationality; the exact
  accepted normalized lift excludes it in the stated domain.
- Normalization is used at a verified smooth actual K-point. A geometric
  point over an unspecified extension would invalidate the place count.
- The infinity branch count is p, not p^2; parameter changes have already
  absorbed the W root.
- Riemann–Roch is used at degree-one actual points. There is no claim of
  the same dimension difference for arbitrary closed points of larger degree.
- Character projection denominators are harmless over K[T] only. The
  separate rescaling argument is what supplies arithmetic integrality.
- Infinite-order cancellation cannot hide an unbounded polynomial
  degree because all p Fourier evaluations are used.
- Negative X is treated by complex local parameters and absolute values;
  no simultaneous choice of positive real p-th roots is presumed.
- One common c, followed by one nonzero family member, precedes the
  number-field norm. Mixing local functions would not prove the claim.
- No assertion about the old single-delta zero branch is needed or obtained.

The separate 34-row ledger records every constructor obligation as
reconstructed, with zero open substantive issues and zero requested
author repairs. This supports scoped acceptance of RG1–RG3 after the
other independent whole audit and coordinator reconciliation. It does
not enlarge the conclusion beyond the finite coefficient procedure.
