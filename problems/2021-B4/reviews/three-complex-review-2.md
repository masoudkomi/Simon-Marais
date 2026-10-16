# Independent full extension audit R2: three complex recycled values in degree 20

2026-10-16 UTC / 2026-10-17 Australia/Brisbane. Initial blind audit.
The reviewer did not construct the candidate. Requested settings remain
gpt-6.1-sol / max; verified effective-setting readback is unavailable.

**Recommendation: accept C20, using the explicitly accepted old finite
algebraic certificates.** The whole complex-to-algebraic and ramified local
argument has been reconstructed, and every new complementary polynomial
pair and certificate has been checked. No substantive objection remains
from this audit. This initial report is frozen before any new peer
extension audit is read. Promotion remains the coordinator's decision.

## Target, scope, and independence

The frozen target is `notes/coordinator-three-complex-witnesses-v1.md`,
SHA-256
`4696d98dfe053d74fc4114bc0986359288a8f542c7f87c29134746b7d73d2d65`.
The candidate manifest has SHA-256
`d9210626ef24fe18ccde57706399d6c30a5fedb81d71a972da5e562a1c582ec8`.
All **154** listed artifacts have the stated lengths and hashes; exact
observed values are in `three-complex-review-2-input-validation.json`.
The completion note, initial unresolved records, separate resolvers,
construction provenance, and old accepted certificate artifacts are
included in that integrity audit. Integrity alone is not mathematical
verification.

The proposed C20 concerns monic degree-20 polynomials over C whose
derivative common roots can all be supplied by at most three distinct
values. It does not assume all roots belong to that set. Its conclusion
is a power of one linear polynomial. It neither settles unrestricted
degree 20 nor classifies the degrees in 2021 B4(b). The preliminary part
(a) and other contest problems were not investigated.

I read AGENTS.md, this candidate, its completion and manifest, and the
explicitly accepted old finite dependency. I have not read
`reviews/three-complex-review-1*`, another new extension review or its
conclusions, shared status/issue logs, or the unrelated J=16 leading work.
No candidate or shared integration file was edited. Only reviewer files
with the `reviews/three-complex-review-2` prefix are created or changed.

The new normalized mask enumeration and exact polynomial implementation
were frozen before reading the constructor's new program or raw
certificate data. The preserved source is
`three-complex-review-2-construction-v1.py`, SHA-256
`d5e198884d3a4414883f79104a17b6d7c36c4332d47b26f5d656b5b6e0f198cd`.
Its timestamped freeze is `three-complex-review-2-construction-freeze.json`.
My new mask list was already independently derived at that point.
The completed full verifier has SHA-256
`8b1c62d1f1d0e68466bf0607bc932dca7ced53c3dc55e2794dbfd79ee8b93369`.

The symbolic ordinary-Hasse construction and modular Euclidean gcd are
adapted solely from my own frozen rational R2 implementation, source
SHA-256
`a9a0255a27c57cfd7ccac1528b8242233bdffb8e166545bd9c7d74b4d3be7b0e`.
Their exact shared source-body SHA-256 is
`1f54805cd28a4400bb661edc45fb2aa97f60e7105d3c0a0ca4ff135356fb68a6`;
I checked byte equality. The old ordinary-modulo-361 mask justification
was **not** carried over. No constructor program or helper is imported
or executed. After my construction freeze, raw metadata and serialization
were used only for comparison. Constructor reuse is explicitly recognized
as construction rather than independent-review credit.

## Primary attribution and dependencies

I rechecked Massri's [version-6 primary PDF](https://arxiv.org/pdf/1806.09561v6),
Theorem 7.10 and its proof on PDF pages 13–14, together with Remark 7.4.
The former states the already known three-recycled-root degree-20 claim;
the latter reports the 6,680-pattern filter. The present candidate
appropriately reproduces that restricted claim and claims no novelty.
Its computation does not assume Massri's separate 3^17-resultant run.
The cited v6 is the 2023 revision; the withdrawn v2, v3 and v5 are
different version objects, not a reason to describe v6 as withdrawn.

I rechecked [CLO's primary author PDF](https://arxiv.org/pdf/1208.5404),
§3.4 equations (9)-(10) and the normalization leading to Lemma 17.
The local argument reconstructed below supplies the specific finite-field
and ramification details used here. No all-roots-rational or unramified
variant of their later Proposition 19 is used.

The accepted old finite dependency consists of **explicit integer pairs**
for 772 masks and their 1,493,024 refinements, with no common algebraic
root. Its individual certificates are algebraic facts, even though those
particular masks were originally selected using rational-only conditions.
The coordinator explicitly accepted those facts after both prior audits.
This audit preserves them and checks their identity and exact inclusion
in the new complete catalog; it does not reuse the rational-only Newton
exclusions as complex theorems.

The old R2 freeze SHA-256 is
`68379652537bfa8f0b29e5d9304c5ab19d79a1c2bb63e295d288a76d13a6ec21`.
The full verifier checks that freeze and every artifact it binds, as well
as the old finite result and old sentinel. Primary source URLs, locations,
cached-paper hashes and verification times are recorded separately. Full
third-party papers remain only in ignored `.cache/`.

## Complete reconstruction: from arbitrary complex coefficients to algebraic ones

A one-value cover r forces f^(k)(r)=0 for all k=0,...,19. Taylor expansion
then gives f=(X-r)^20. For a nontrivial counterexample, choose a
first-derivative witness r from the cover and a different cover value b.
The monic affine transform

    g(X)=(b-r)^(-20)*f(r+(b-r)*X)

has 0 as a double root, 1 as a root, and a covering set represented by
{0,1,u}. If two distinct values suffice, let u=0. Each derivative equation
is preserved because the derivative is multiplied by a nonzero scalar.
The coefficients at this stage may still be arbitrary complex numbers.

Write g=sum binom(20,j)*a_j*X^(20-j), where a_0=1 and
a_19=a_20=0. For j=1,...,18 fix a label w_j in {0,1,U} for a selected
derivative witness. In characteristic zero,

    D_j(X)=(j!/20!)*g^(20-j)(X)
          =sum_(k=0)^j binom(j,k)*a_k*X^(j-k).

The coefficient of a_j in D_j(w_j) is 1. Thus the equations uniquely
determine a_1(U),...,a_18(U) over Z[U] without division. By induction,
their values at the original u are the original normalized coefficients.
The double-root condition at 0 already supplies the first derivative;
j=1 supplies the nineteenth derivative. The remaining root requirements
are P(U)=g_U(1)=0 and Q(U)=g_U(U)=0.

If either P or Q is nonzero as an integer polynomial, the actual common
complex value u is algebraic. Every coefficient then lies in Qbar, and
the same cover is algebraic. This includes the case where one polynomial
is identically zero and the other is not.

If **both P and Q vanish identically**, specialize U=2. All selected
derivative equations remain polynomial identities; both root equations
still hold. The leading coefficient remains 1, c_0=c_1 remain zero, and
1 remains a root. Hence the specialized polynomial is monic of degree 20,
has distinct roots 0 and 1, and cannot be a pure power. Its selected
witnesses lie in {0,1,2}. This supplies an algebraic counterexample even
when the original parameter or coefficients were transcendental.

There is no appeal to an embedding of all of C in a p-adic algebraic
closure. Only finitely many algebraic coefficients and roots now need
to be embedded. Include the cover and all splitting roots in a number
field L. An embedding L -> Qbar_19 exists by taking a root in Qbar_19
of a primitive element's minimal polynomial. The field K=Q_19(image(L))
is a finite extension of Q_19, generated by finitely many algebraic
elements. Polynomial identities, distinct roots, degree, and derivative
conditions survive this field embedding.

## Complete reconstruction: finite ramified local normalization

Translate the selected double root to 0 in K. Among the finitely many
nonzero splitting roots choose alpha of least valuation. Scale X by
alpha and divide by alpha^20 to keep the polynomial monic. All roots,
and in particular all selected witnesses, now have nonnegative valuation;
at least one nonzero root is a unit. K may be ramified, so v(K*) can be
(1/e)Z with e>1; no integral-valuation assertion is used.

Inductively, the normalized equations D_j(w_j)=0 at the integral chosen
witnesses give a_j in O_K for j=1,...,18: a_j is the negative sum of
products of earlier integral coefficients, integer binomial coefficients,
and nonnegative powers of an integral witness. a_19=a_20=0 as before.
This proves more than ordinary coefficient integrality and justifies
using the normalized D_j before reduction, even when their original
scalar normalization has a nonunit denominator.

For 2<=j<=18, binom(20,j) has 19-adic valuation exactly 1. Consequently

    bar(f)=X^20+bar(20*a_1)*X^19.

If a_1 were a nonunit, the reduction would be X^20, contrary to the
chosen unit root. Thus a_1 is a unit. The center c=-a_1 is itself a
common root for the nineteenth derivative, so f(c)=0. Scale by this
unit c. The new a_1 is -1; all a_j remain integral; all valuations of
roots relative to zero remain unchanged. Now

    bar(f)=X^19*(X-1).

At 1 the reduced ordinary derivative equals 1, so f'(1) is a unit and
the center is simple. For uniqueness of the unit root, divide exactly
by X-1 in O_K[X]. The quotient reduces to X^19, which cannot vanish
at any unit residue. Hence no other unit root exists, including a
second root congruent to 1. All other nonzero roots have strictly
positive valuation. In particular the chosen double root 0 differs
from the center. Relabeling the cover gives {0,1,u}, with u=0 allowed,
or with v(u)>0. This conclusion holds with fractional positive valuation.

## Correct residue-field filter and independent complete enumeration

For j=2,...,18 choose 1 whenever it is available as a common witness;
otherwise choose 0 or u. If w is a noncenter witness, the equation

    a_j=-sum_(k<j) binom(j,k)*a_k*w^(j-k)

puts a_j in the maximal ideal m_K. When w=0 it is exactly zero;
otherwise each summand has strictly positive valuation. It need **not**
belong to 19*O_K. For example, in a ramified extension an element pi
with pi^e=19 has 0<v(pi)<1 when e>1. Thus the old rational reasoning
that noncenter ordinary coefficients vanish modulo 19^2 would not be
a valid coverage proof here.

Reduce modulo m_K. A noncenter branch gives bar(a_j)=0; a center branch
gives the displayed normalized triangular equation with w=1. Beginning
at bar(a_0)=1 and bar(a_1)=-1, induction shows that all bar(a_j) lie in
the prime field F_19, even when the residue field of K is larger.

The exact identity f(1)=0 is

    -19+sum_(j=2)^18 binom(20,j)*a_j=0.

Divide it by 19 in characteristic zero. Since each quotient binom(20,j)/19
and each a_j are integral, reduction then gives

    -1+sum_(j=2)^18 (binom(20,j)/19)*bar(a_j)=0 in F_19.

There is no division by zero in the residue field and no assumption
that reduction modulo m_K equals reduction modulo 19 in O_K.

My new mask code works **directly with the normalized a_j in F_19**.
At each j it visits the branch a_j=0 and the branch
a_j=-sum_(k<j)binom(j,k)a_k. It performs exactly 131,072 leaf checks.
The final divided-root congruence retains **6,680 masks**, with no J
exclusion or small-cluster theorem applied. J is recorded only as the
largest j with nonzero residue, not as the largest center bit.

| J | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| masks | 1 | 1 | 3 | 5 | 26 | 32 | 101 | 131 | 315 | 461 | 887 | 1674 | 3043 |

Each mask M has 2^(17-popcount(M)) labeled assignments of 0 or U at
the noncenter positions. The independent total is **6,224,952**. All
6,680 sorted masks match the constructor's complete list entry for entry.
The earlier 772 masks are a verified subset. The complementary sorted
list has 5,908 masks and **4,731,928** assignments; together with the
accepted 1,493,024 old assignments they form an exact disjoint union.
All diagnostic J refinement counts were independently recalculated and
match; the complete lists and counts are retained in the review JSONs.

The canonical center mask of an actual normalized counterexample is
among these masks. For every noncenter order its chosen witness has
one of the labels 0 or u, so a refinement is present. Formal noncenter
choices are not required to make the center fail; this enlarges the
formal family and cannot omit an actual case. No lifting or sufficiency
claim is made for a residue survivor.

## Exact family reconstruction and meaning of the certificates

The normalized final family has c_20=1, c_19=-20 and c_0=c_1=0. My
integer construction solves ordinary Hasse equations, not the constructor's
helper recurrence. For l=18 down to 2 and w in {0,1,U}, it sets

    c_l(U)=-sum_(t>l) binom(t,l)*c_t(U)*w^(t-l).

This solves H_l(f)(w)=0 because the coefficient of c_l is 1. Dense
integer arrays in ascending U degree perform multiplication by U as
an exact shift. The identity

    binom(t,l)*binom(20,t)=binom(20,l)*binom(20-l,t-l)

connects this construction to the normalized a_j equations and shows
that the ordinary coefficients retain the required binomial factors.
It is an exact characteristic-zero algebraic construction, so the
same implementation works for complex or ramified specializations.
Its validity does not use the old rational residue filter.

At every leaf P=sum c_t and Q=sum c_t*U^t. An actual normalized
counterexample's coefficients equal these specialized coefficients
by triangular uniqueness, and its remaining root equations require
P(u)=Q(u)=0. The degree bounds deg c_t<=20-t, deg P<=18 and deg Q<=20
follow by induction. Repeated witness labels, unused U, U=0 and U=1
are included as excess rather than omitted specializations.

For a nonzero constant P, no characteristic-zero specialization can
vanish. Otherwise a certificate gives a prime ell with both **actual
integer degrees retained**, nonzero leading residues, and gcd 1 after
reduction. The finite-field Sylvester determinant is nonzero. It is the
reduction of the integer Sylvester determinant with those degrees, hence
the integer resultant is nonzero. This excludes a common root over
Qbar and indeed over any characteristic-zero extension field, by the
resultant identity or coprime Bezout identity over Q[U]. It therefore
excludes the local parameter as well.

Neither a witness nor its denominator is reduced modulo ell. There is
no rational-height bound, auxiliary-prime integrality requirement, or
unramifiedness condition hidden in that step. Computations establish
finite exact certificates; their unrestricted consequence uses the
coverage and resultant arguments just reconstructed.

## Complete new certificate audit

The full verifier traverses every new mask and every 0/U refinement
independently. For every row it checks the exact (mask,U_mask) key,
disjoint bits, bit range, absence of duplicates within the mask, and
each expected per-mask count. It checks the global count and no excess
raw row. All integer P,Q are independently regenerated; their complete
stream is hashed. Every constant row is checked exactly. Every other
row is checked for primality by trial division, exact integer degrees,
both nonzero leading residues, and the full modular Euclidean gcd.
All 79 compressed chunks are checked for bytes, hash, row count,
raw serialization and full uncompressed stream hash.

The completed independent run checked **all 4,731,928 new families**,
with exact unique coverage. It verified the following certificates:

| Independent complementary certificate | Families |
|---|---:|
| P is the stated nonzero constant | 5,908 |
| gcd 1 modulo 101, both degrees retained | 4,495,784 |
| modulo 103 | 218,175 |
| modulo 107 | 11,555 |
| modulo 109 | 477 |
| modulo 127 | 26 |
| separate initial sentinels modulo 131 | 3 |
| Total | 4,731,928 |

The three original sentinel rows remain explicit in the initial stream.
Every integer pair was regenerated, its raw-record hash compared, and its
entire modular gcd independently computed. The extra certificates are:

| (center_mask,U_mask) | integer degrees P,Q | leading residues at 131 | unnormalized gcd |
|---|---|---|---|
| (117075,9220) | (15,20) | (83,3) | 9 |
| (117075,1548) | (12,20) | (44,79) | 31 |
| (117075,9356) | (15,20) | (97,124) | 11 |

All primes were independently verified by trial division. The leading
residues are nonzero and both degrees are retained in every prime case.
There are exactly 78 chunks of 60,000 rows and a last chunk of 51,928
rows, **28,442,028 compressed bytes** altogether. No row was left
unresolved or omitted. Complete per-chunk hashes, byte lengths and row
counts, degree histogram, sentinels and exact totals are in
`three-complex-review-2-full-result.json`.

Both regenerated complementary global hashes match the constructor:

    integer polynomial stream:
    49da0560f41fdf3fce8a1ed7e63e877b5d51533de93142d74be7129d3db04da2

    uncompressed compact certificate stream:
    e4dee952d410bf709b8c90dd61002ee88c4179a5fe7a8ca0678fe3644a25ffb1

The old accepted polynomial stream has SHA-256
`aa5cd774ea5d10dcbb52a5bcee0d289d807ec7a364fd5921f29c9b412dda8cad`;
its certificate stream has SHA-256
`4befc080569dbe0d4d978efaef502e51f644163d15ef9bd22ae7112cf1840387`.
Its (6436,24785) initial miss is included through the accepted separate
modulo-131 certificate, not silently discarded. I additionally rebuilt that
old sentinel in the supplementary sentinel check and obtained retained
degrees (16,20), leading residues (8,102), and nonzero constant gcd 77
modulo 131. The supplementary file also independently records why each
original five-prime list did not certify its sentinel. It does not stand
in for the complete new audit.

The old full R2 finite-result file was rechecked unchanged at SHA-256
`fd0cc937f4ce00be1c02947d4bf5cbadb58af747a5c918a6879129d186cef891`.
The exact finite algebraic facts in that accepted packet, plus the fully
verified new complement, exclude all **6,224,952** normalized families.
Every would-be algebraic counterexample supplies one of these masks and
refinements, so is excluded. The specialization argument would turn any
complex counterexample into such an algebraic counterexample. This gives
the claimed C20 implication, within the stated old finite dependency.

The resolved audit questions and their evidence are recorded in
`three-complex-review-2-issues.json`. No author repair is requested and no
substantive objection remains. In particular no rational-only J exclusion,
unramifiedness hypothesis, height bound, or unrelated J=16 result is used.

## Resources, reproduction, and current limits

Run from the repository root:

    .venv/bin/python -u problems/2021-B4/reviews/three-complex-review-2-run.py full 900

This launches dedicated child PID 45858 under an explicit external
900-second timeout, with 16,384-family incremental checkpoints (288
full checkpoints). Its
command, source hash, PID, timestamps, stdout and stderr paths are in
`three-complex-review-2-full-job.json`. It started at
2026-10-16T16:33:01.035723+00:00 and finished at
2026-10-16T16:41:03.724732+00:00, **482.690 seconds** including wrapper
overhead. It exited 0, with empty stderr and no timeout. The wrapper reaped
the child; no termination or global process kill was needed. Complete
incremental stdout and the empty stderr are retained.

The independent 8,192-family benchmark finished in 1.062 seconds
including wrapper overhead, exit code 0, child PID 45474, with an
external 30-second deadline. Python is 3.12.14; the certificate code
uses only the standard library and integer arithmetic. No native CAS,
installation, separately billed API, charge, commit or push is used.
The precomparison source and all intermediate results are retained.
The optional direct sentinel reconstruction is

    .venv/bin/python -u problems/2021-B4/reviews/three-complex-review-2-sentinels.py

It uses only the reviewer's own exact integer implementation and finished
in 0.002 seconds of measured arithmetic. Its complete integer pairs,
trial-prime gcds, leading residues and hashes are retained in
`three-complex-review-2-sentinels-result.json`.

Authoritative account-wide weekly telemetry was checked at the start
and during the run: 11% total weekly used, reset timestamp 1792745187,
below the 90% total-used cutoff. No new weekly window was entered.

The report, issue log and timestamped artifact freeze were completed before
cross-review. Only the coordinator may promote C20 after both complete
independent audits. No novelty or unrestricted degree-20 solution follows.
