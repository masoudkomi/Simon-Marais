# Accepted reciprocal-kernel: exact coordinator scope

2026-10-17 UTC. **Proved, independently reviewed scoped partial result.**

RK1--RK3 are accepted in their EXACT rational-kernel, fixed-complement and actual-pair scopes. For EVERY odd prime p, L(sum n_a sigma_a)=sum n_a/(1-zeta^a) on Q[G] has kernel exactly the even rational vectors of augmentation0. The sole added theorem is the attributed Chowla--Hasse Q-linear independence of the half-set of cotangents for EVERY odd prime, not just the separately treated elementary cases. Even/odd pairing, rational real versus imaginary separation and both kernel inclusions are explicitly proved. The p3 endpoint and nonzero global kernel for p>=5 are retained.

On each affine space theta+j theta=C N with the SAME rational C, differences are odd, so L is injective. For ARBITRARY c,d, R_c(theta)=R_d(eta) iff sigma_c theta=sigma_d eta, because every translated vector has that SAME complement and the prefactor1-zeta is common and nonzero. Thus nonconjugate free vectors in one fixed-complement space give disjoint reciprocal arrays, each with p-1 entries. These arrays are common-scaled actual L-orbits, not generally the actual Galois conjugates of R1, whose prefactors vary. Equal augmentation alone does not replace the complement hypothesis.

RK3 retains its actual positive integral I_f pair hypothesis. UW1--UW4 have NOW separately received both whole audits and coordinator acceptance at proofs/reviewed-original-weight-universal-v1.1.md; combining that accepted pair existence with RK3 gives TWO disjoint free reciprocal arrays at ORIGINAL augmentation p-1 for every prime p>=37. This is a transparent composition of separately accepted statements, not a retroactive change of the frozen conditional RK body or a low-prime extension. Rational parity decomposition is used for analysis only and constructs no integral module witnesses.

Root is constructor and is EXCLUDED from independent auditor count. The OTHER fresh initially blind WHOLE audits by review_2021_reasoning_j15_r2 R1 and review_2017_coarsening_r1 R2 are complete, with32/22 inference checks covering all8 obligations. Root read the ENTIRE candidate, BOTH complete reports, ALL ledgers and BOTH source records, and reconciled the exact coefficient field, signs, full kernel, arbitrary array indices, complement, p3 endpoint and normalization. ALL six original Hasse pages275--280 were visually read by root and both reviewers across the four scanned spreads. The primary Hamahata single-modulus rational specialization is a cross-check, not a stronger-field import. Classical analytic/class-number theory is attributed, not newly proved. No substantive issue or author repair remains.

No higher-series rank, Jacobi integrality, EVERY-conjugate cancellation, nonzero delta, height bound or new Diophantine exclusion follows just from separation. The signed full annual Nagell--Ljunggren question and novelty/external validation remain unresolved. No mathematical program, CAS, scan or certificate replay supplies the argument; source-image inspection and hashes have their stated read/integrity roles. Full papers remain local and ignored; old bytes and both blind initials remain preserved.

The COMPLETE frozen mathematical submission follows as a byte-identical suffix. Its historical unverified label records submission status; this header and acceptance record state the current exact scope.

---

# Exact reciprocal kernel and separation on a fixed complement

2026-10-17 UTC. **Candidate proof - unverified.** Constructor: root.
This is an attributed application of the classical cotangent independence
theorem, with an explicit new-to-this-record restriction of the kernel.
No novelty, Diophantine exclusion or complete annual answer is claimed.
TWO OTHER initially blind whole audits are required before acceptance.
No mathematical program, CAS, scan or numerical experiment was used.

## 1. Definitions and the imported classical theorem

Let p be an ODD PRIME, zeta=exp(2*pi*i/p), K=Q(zeta), G=F_p^*,
sigma_a(zeta)=zeta^a, j=sigma_(-1), and N=sum_(a in G)sigma_a.
For theta=sum_a n_a sigma_a in Q[G] define

    wt(theta)=sum_a n_a,
    L(theta)=sum_a n_a/(1-zeta^a),
    R_c(theta)=(1-zeta)L(sigma_c theta), c in G.

The direct indices agree with the accepted MS/FS/OW/UW conventions.
No group-ring multiplication is confused with applying L. The factor
1-zeta in EVERY R_c is the SAME nonzero number, independent of c.

The sole external theorem imported is the Chowla-Hasse cotangent
independence theorem: the (p-1)/2 real numbers

    cot(pi*a/p), 1<=a<=(p-1)/2,

are linearly independent over Q. This is unconditional for every odd
prime p. No regular-prime, class-number divisibility or small-index
condition is added or assumed. The theorem is published background,
not a claimed new proof here. Its analytic nonvanishing/class-number
input is not reconstructed from first principles in this packet.

## 2. RK1: the entire Q-linear kernel

**Proposed RK1.**

    ker L = {eta in Q[G]: j eta=eta and wt(eta)=0}.

For every a, direct calculation gives

    1/(1-zeta^a)+1/(1-zeta^(-a))=1,
    1/(1-zeta^a)-1/(1-zeta^(-a))
        =(1+zeta^a)/(1-zeta^a)=i*cot(pi*a/p).

If eta is EVEN (j eta=eta), pair the terms indexed a,-a to obtain
L(eta)=wt(eta)/2 in Q. In particular every even zero-weight vector
is in the kernel. This proves one inclusion.

If eta is ODD (j eta=-eta), then its coefficients satisfy
n_(-a)=-n_a. Pairing instead by differences gives

    L(eta)=i sum_(a=1)^((p-1)/2) n_a cot(pi*a/p).

The imported theorem implies L(eta)=0 only if every rational n_a=0,
and then eta=0. Thus L is injective on the ENTIRE odd subspace.
This includes rational coefficients and needs no positivity, moment,
module membership or coefficient bound.

For arbitrary eta in Q[G], write

    eta_+=(eta+j eta)/2, eta_-=(eta-j eta)/2.

This is only a rational vector-space decomposition used to analyze the
kernel; it does not construct positive integral elements of I_f by
division. L(eta_+) is rational, and L(eta_-) is purely imaginary.
If L(eta)=0 then both parts must be zero. Injectivity on the odd part
gives eta_-=0, and the even formula gives wt(eta_+)=0. Therefore eta
is even of weight0, proving the converse inclusion and RK1.

The SAME kernel belongs to R_1, since its prefactor1-zeta is nonzero.
The map is still globally nonfaithful: for p>=5,

    eta=(sigma_1+sigma_(-1))-(sigma_2+sigma_(-2))

is a nonzero even zero-weight vector and L(eta)=R_1(eta)=0.
Thus RK1 preserves the old accepted counterexample instead of claiming
that ordinary Fourier faithfulness transfers to this map. For p3 the
kernel is zero; the displayed counterexample is explicitly restricted.

## 3. RK2: exact separation on each fixed-complement affine space

For a fixed C in Q put

    A_C={theta in Q[G]: theta+j theta=C*N}.

If theta,eta both belong to A_C, then delta=theta-eta is odd. RK1
therefore gives

    L(theta)=L(eta) iff theta=eta.                       (RK2a)

Every translate of an element in A_C is also in A_C: G is abelian,
sigma_c commutes with j and sigma_c N=N. Applying(RK2a) to translated
elements and cancelling the common NONZERO prefactor gives, for c,d in G,

    R_c(theta)=R_d(eta)
          iff sigma_c theta=sigma_d eta.               (RK2b)

These are ACTUAL equalities of algebraic numbers, not residue tests.
Consequently, within this one fixed-complement affine space, two
nonconjugate group-ring elements have DISJOINT reciprocal value SETS.
If an element has trivial G-stabilizer, its reciprocal array consists
of exactly p-1 distinct values. Conversely any stabilizer equality
produces the corresponding array equality, by direct reindexing.

The unnormalized map L is G-equivariant:

    sigma_h L(theta)=L(sigma_h theta).

Thus L(theta)'s actual Galois stabilizer agrees with theta's on A_C.
The array R_c(theta) is obtained from that orbit by a common scaling,
so it has the same equality pattern. It is NOT in general the list
of actual conjugates of R_1(theta): those have prefactors1-zeta^c.
No such erroneous Galois-normalization assertion is needed.

## 4. RK3: the precise conditional UW application

Suppose theta_1,theta_2 are positive integral elements of I_f, each
with complement theta_i+j theta_i=2N, nonzero first inverse moment
M_1(theta_i), and not G-conjugate. Their augmentation is then p-1.
The accepted moment action law gives

    M_1(sigma_h theta_i)=h^(-1)M_1(theta_i),

so each group-ring stabilizer is trivial. Applying RK2 with C=2 proves
that the two reciprocal arrays EACH have p-1 distinct values and their
two value SETS are disjoint, at the same ORIGINAL augmentation p-1.

This application requires an ACTUAL pair with these hypotheses. The
separate UW1-UW4 candidate proposes such a pair for every prime p>=37;
it is currently unverified pending two OTHER whole audits. If that
separate selection result is accepted, RK3 gives the corresponding
universal reciprocal-array corollary for p>=37. RK1/RK2 do not assume
UW or use any of its cubic/fifth computations. No unreviewed UW existence
statement is silently promoted as an accepted input to this packet.

The source's later application still needs its own complete Jacobi
integer normalization, coefficient integrality, higher-series jet
rank, augmented singular-system bounds, cancellation in EVERY conjugate,
nonzero-delta argument and compatible archimedean inequalities. A set
of distinct reciprocal values alone proves none of those statements.
The actual signed integer Nagell-Ljunggren equation remains unresolved.

## 5. Primary sources, actual reads and retrieval record

Original source: H. Hasse, *On a question of S. Chowla*, Acta Arith.18
(1971),275-280, DOI10.4064/aa-18-1-275-280.
[Publisher issue and public download](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/18).
Read ALL six printed pages275-280, including the theorem, the character-
matrix proof, the general cotangent conclusion from the class-number
formula, the two special elementary cases and the final addendum.
The general cotangent conclusion is not restricted to those two cases.
The displayed class-number formula is an attributed input, not newly
proved here. No tangent theorem is needed.

Cross-check: Y. Hamahata, *Okada's theorem and multiple Dirichlet series*,
Kyushu J. Math.74(2020),429-439, DOI10.2206/kyushujm.74.429,
[primary PDF](https://www.jstage.jst.go.jp/article/kyushujm/74/2/74_429/_pdf/-char/en).
Read introduction/Theorem1.1, Theorem2.1 and its displayed proof. Only
the rational single-modulus, zero-derivative specialization is relevant;
the stronger multiple-series statements and unseen reference proofs
are not imported.

Hasse cache is LOCALLY ONLY:
`.cache/literature/2025-reciprocal-return/hasse-chowla-1971.pdf`,
520142B, SHA2565536c10633a189e98ad59a2fee0a1dc1d9a760263b66bd5b6d35277a8e5758a3.
It is four SCANNED two-page spreads, also containing the adjacent
printed pages274/281. pypdf extraction yielded no text. pdftoppm rendered
all four spreads and root visually read the six Hasse pages; only their
scope is claimed. No OCR output is mistaken for readable source text.
The publisher's normal free link was used after the viewer cache missed;
no restriction, paywall or login was bypassed. A different repository
request returned403 and was not used as a source proof. Full downloaded
papers and page images are not uploaded to GitHub.

The complete accepted MS body and the complete current UW candidate
were read for conventions/limits. MS's global-kernel warning remains
correct. RK uses an ADDITIONAL published independence theorem on the
odd subspace, rather than attributing the restricted injectivity to MS
or Fourier faithfulness. All old bytes remain unchanged. No novelty
or general source-theorem repair is asserted.

## 6. Whole-audit obligations

1. Verify the exact prime/rational cotangent theorem and its actual
   unrestricted cotangent scope in the primary original source.
2. Reconstruct the reciprocal pair sum/difference, including the sign
   and direct-index conventions, and injectivity on the odd subspace.
3. Reconstruct the rational even/odd decomposition, real-imaginary
   separation and BOTH directions of the entire kernel classification.
4. Check p3 and p>=5 counterexample scopes, and that the global kernel
   survives while fixed-complement differences are odd.
5. Check invariance of A_C, equality(RK2b) for ARBITRARY c,d and the
   actual Galois-prefactor distinction.
6. Check the precise hypotheses of RK3 and its first-moment freeness;
   unverified UW existence must stay explicitly conditional.
7. Retain integral positivity/module/weight conventions without using
   rational averaging to construct new I_f witnesses.
8. No higher-jet rank, arithmetic cancellation, size bound, annual
   exclusion or novelty follows from separation alone. Root is the
   constructor and cannot count as either independent reviewer.
