# R1 independent extension audit of proposed C20

2026-10-16 UTC / 2026-10-17 Brisbane. Reviewer:
`review_2021_three_witness_r1`, not a constructor. Requested model and
reasoning: `gpt-6.1-sol` / `max`; effective settings unavailable.

**Disposition: complete independent extension audit; no unresolved substantive
objection to C20, conditional on the explicit accepted old finite data.**
The entire new mathematical reduction and every complementary polynomial
pair/certificate were reconstructed. I recommend acceptance after the other
independent extension audit and the coordinator's promotion decision. This
report does not promote C20 or assert a full degree-20 or B4(b) solution.

## Frozen object and independence

Target: `notes/coordinator-three-complex-witnesses-v1.md`, SHA-256
`4696d98dfe053d74fc4114bc0986359288a8f542c7f87c29134746b7d73d2d65`.
Its completion note and all 154 artifacts are bound by manifest SHA-256
`d9210626ef24fe18ccde57706399d6c30a5fedb81d71a972da5e562a1c582ec8`.
Every artifact's bytes and hash matched at entry.

This is a separate extension audit. All old review files are preserved.
No new peer extension report or conclusion, unrelated J=16 leading work,
shared proof/status/issue/research-log file, or Git state was read or used.
The old 772-mask packet's explicit algebraic incompatibilities are an
accepted finite dependency; accepting its rational theorem alone would
not justify the extension. The dependency is spelled out below.

Before reading new certificate rows or inspecting new constructor
serialization, I wrote and ran a new prime-field enumeration. The new
independent source was frozen at SHA-256
`b486f1f2f5a2e364e65c83f33e6107eb0302dd9d1117d15cd589056f2df0defa`.
It calls only the exact polynomial-generation and finite-field routines
from **my own** old frozen ordinary-Hasse checker, SHA-256
`ed98ed514ac6dffa20e3c5779d7851437003326992f0619018f1837147386464`.
That source hash is asserted at runtime. Its old rational mask enumeration
is never called. Bytecode writing is disabled to preserve old files.
No constructor module is imported or executed. After the new source
freeze, constructor serialization/traversal lines and reuse provenance
were inspected for stream comparison; the checker needed no alteration.

The mathematical derivation of the normalized prime-field filter is new
to this extension audit. Reuse of my own already audited integer
polynomial/GCD core is explicit; it is not claimed to be a newly independent
second implementation of that core or an independent audit of my old report.

## 1. Entire complex-to-algebraic reduction

A one-value cover forces the Taylor coefficients of a monic degree-20
polynomial at that value to vanish through order 19, hence gives its
twentieth power. For a hypothetical nontrivial cover, choose a common
first-derivative root r **from the cover** and another distinct cover
value b. Translation by r, scaling by b-r, and monic rescaling preserve
all shared-root equations and nontriviality. They give a double root 0,
a root 1, and a cover contained in {0,1,u}. If the cover had only two
values, u=0 is permitted. No simplicity of a center has yet been assumed.

At this first stage a_1 is **not fixed**. Write the coefficient of
X^(20-j) as C(20,j)a_j, with a_0=1 and a_19=a_20=0. For derivative
orders 19 through 2, choose a label w_j in {0,1,U}, j=1,...,18, matching
the given cover. The identity

    H_(20-j)(f)(X) = C(20,j) sum_(k=0)^j C(j,k)a_k X^(j-k)

holds in characteristic zero by the binomial-product identity. The
unknown a_j has coefficient one in its normalized equation. Therefore
the triangular recurrence constructs all a_j(U) in Z[U] and specializes
to the normalized complex polynomial by induction. In particular this
stage includes the j=1 equation; it is not a premature application of
the later a_1=-1 family code.

The two additional root equations P(U)=f_U(1) and Q(U)=f_U(U) are integer
polynomials and vanish at the original complex u. If either is a nonzero
polynomial, that u is algebraic; every normalized coefficient then lies
in Q(u). A nonzero constant could not have the hypothesized root, so it
causes no exception. This does not assert that the original coefficients
before the arbitrary complex affine change were algebraic.

If P and Q are both identically zero, evaluate the polynomial identities
at U=2. The polynomial remains monic of degree 20, its constant and
linear coefficients remain zero, and it still has the distinct roots
0 and 1. It therefore cannot be a power of one linear polynomial. Every
selected derivative equation survives specialization, and 0,1,2 are all
roots when needed by its cover. The first derivative already has the
double root 0. This gives an algebraic nontrivial counterexample even
in this exceptional case. No specialization theorem, excluded-parameter
argument, or embedding of all C into Qbar_19 is being assumed.

## 2. Finite, possibly ramified, 19-adic normalization

The algebraic coefficients and cover generate a number field. Adjoining
the finitely many splitting roots still gives a finite extension of Q.
Embed that field in Qbar_19 and take its compositum with Q_19; this is
a finite extension K containing the coefficients, selected witnesses,
and all roots. All polynomial identities persist. K may be ramified;
v(19)=1 does not imply that its value group is Z.

Translate the selected double root to zero. A nontrivial polynomial
has a nonzero root, so choose one alpha with smallest valuation among
the nonzero roots. Replace f(X) by alpha^(-20)f(alpha X). Every root
and every selected witness is then integral, and some nonzero root is
a unit. Monicity, degree, zero multiplicity, and all derivative equations
are preserved by the explicit affine/scalar transformations.

The normalized derivative equations inductively show a_j in O_K:
each chosen witness is integral and a_j is a sum of products of earlier
integral a_k and its powers. This includes a_1. Merely dividing an
ordinary integral coefficient by C(20,j), which may be a nonunit, would
not have been a valid integrality argument; the triangular equations
provide the needed proof. The zero constant and linear coefficients
give a_20=a_19=0 exactly.

For 2<=j<=18, C(20,j) has 19-adic valuation one. Reduction at the maximal
ideal thus gives X^20+bar(a_1)X^19. If a_1 were a nonunit, a unit root
of f would reduce to a nonzero root of X^20, impossible. Hence a_1 is
a unit. D_1=X+a_1 has its selected common root c=-a_1, which is a unit
and belongs to the cover. Scaling by this c makes the center exactly
1 and a_1=-1 without changing which roots are units or integrality.

The reduction is now X^19(X-1). Its derivative at 1 is 1 in
characteristic 19, so f'(1) is a unit and the center is simple.
Alternatively, since K contains the splitting roots, reduce the product
of the integral linear factors: the sole nonzero residual root has
multiplicity one. Because the actual center 1 is one such root, it is
the unique root of valuation zero, counted with multiplicity one.
All other nonzero roots have strictly positive valuation, with no claim
that those positive valuations are integral. The double root 0 differs
from the center, and the cover remains {0,1,u}, where u=0 is allowed or
v(u)>0. The last-derivative condition is encoded by a_1=-1 and the
first-derivative condition by the double root 0.

This derives exactly the required normalization. It invokes no rational
root count, width-one Newton lemma, J=18/J=17 exclusion, degree-5
good-prime argument, or bound on root valuations beyond positivity.

## 3. Ramified residue filter and complete mask enumeration

For j=2,...,18 select the center whenever it is available. Otherwise
its cover witness is 0 or u and lies in the maximal ideal m_K. The
triangular equation then forces a_j into m_K, because every term has
a positive power of that witness and integral remaining factors. It
does **not** force a_j into 19 O_K. At a center bit its residue is the
negative sum of the previous residues with binomial coefficients.

For an explicit check of why the old rational modulo-361 justification
cannot be transferred, consider pi^2=19 and w=pi. The local equation
D_2(w)=0 is consistent with a_2=2pi-pi^2, of valuation 1/2. Its ordinary
coefficient C(20,2)a_2 has valuation 3/2, below 2. This is a check of
that local derivative equation, not a CA counterexample. It illustrates
the exact inference that must not be imported into this extension.

Reduction modulo m_K sends the noncenter residues to zero. Center
recursion starts from 1 and -1 and uses only binomial coefficients,
so every residue belongs to the prime field F_19 even if the residue
field of K is a nontrivial extension. The exact center-root equation is

    0 = -19 + sum_(j=2)^18 C(20,j)a_j.

Divide this characteristic-zero equality by 19 first. Every coefficient
C(20,j)/19 is an integer and every a_j is integral, so its reduction
is legitimate and gives the displayed necessary F_19 equation. There
is no division by the residue zero of 19 and no modulo-19^2 assertion.

My independent enumeration performs exactly these normalized equations
in F_19 for all 131,072 binary masks. It retains all 6,680 survivors.
The diagnostic largest-unit-index histogram is
6:1, 7:1, 8:3, 9:5, 10:26, 11:32, 12:101, 13:131, 14:315,
15:461, 16:887, 17:1674, 18:3043. J measures a nonzero coefficient
residue, not the largest center bit, and none of its classes is removed.
The retained ordered list matches the constructor's list exactly.

For a mask M all 2^(17-popcount(M)) 0/U refinements are included. Their
total is 6,224,952. The old accepted 772 masks are verified to be a subset
of these 6,680; their complement has 5,908 masks. The sets are disjoint,
have no duplicate mask, and their union is the complete list. Their
refinement counts are respectively 1,493,024 and 4,731,928, summing to
6,224,952. All three ordered lists match the constructor's index.

This uses the old set only to select **already certified explicit
polynomial pairs** for reuse. It does not apply the rational reasoning
that originally selected that set as a necessary filter for complex f.
Noncenter bits need not force failure at the center, so the family list
keeps harmless extra cases. Canonical center choice ensures every actual
normalized algebraic counterexample has one of these masks.

## 4. Integer families, exhaustive verification, and the accepted old data

After the 19-adic normalization, a_0=1,a_1=-1 are fixed. For every
chosen mask/refinement, solve its exact derivative equations in Z[U].
My frozen ordinary-Hasse core constructs the coefficient c_l directly,
descending l=18,...,2, by

    c_l = -sum_(t=l+1)^20 C(t,l)c_t w_l^(t-l),

starting from c_20=1,c_19=-20,c_0=c_1=0. This is the H_l(f)(w_l)
equation with coefficient one on the unknown c_l. The binomial identity
relates it exactly to the normalized-a recurrence, and every constructed
coefficient is checked coefficientwise divisible by C(20,l). I compute
P=sum c_l and Q=sum c_l U^l directly. Induction forces every actual
specialized coefficient to equal these values.

The first-derivative witness 0 is already imposed, and H_19(f)=20(X-1).
The remaining required root equations are precisely P(U)=Q(U)=0.
Repeated witnesses, unused U, and U=0 or 1 are all included, so coincident
labels do not create an omitted boundary case. Distinct formal refinement
indices need not give distinct polynomial pairs; coverage concerns all
indices, with each visited exactly once.

For each new mask the full checker independently generates every supported
U mask and checks uniqueness and the exact count. Raw rows must have the
same mask, disjoint center/U bits, unique U masks, and the complete group
count. Each generated key removes exactly one raw record, no record is
left over, and no extra group is allowed. Thus the verification checks
coverage per mask and per refinement, not merely a matching total.

The old finite dependency is the previously fully reviewed integer P,Q
incompatibility for every one of the 1,493,024 pairs. Those certificates
imply no common root in Qbar, not only no rational root. Since integer
polynomials with a common complex root would share a factor over Qbar,
the same nonzero resultants exclude complex roots as well. The old
rational mask selection does not weaken these individual algebraic facts.
All old compressed data and the separate old resolver remain hash-bound
in the new 154-artifact manifest. I additionally verified that my own
old review manifest and its 19 artifacts are unchanged. This is explicit
dependency reuse; I do not describe the old 25 chunks as freshly recomputed
in this extension run.

In particular the old sentinel (6436,24785) must still use its separate
prime-131 certificate. The complement's three sentinels do not replace it.
The accepted old polynomial stream has SHA-256
`aa5cd774ea5d10dcbb52a5bcee0d289d807ec7a364fd5921f29c9b412dda8cad`
and its raw certificate stream has SHA-256
`4befc080569dbe0d4d978efaef502e51f644163d15ef9bd22ae7112cf1840387`.

For each new nonzero constant P, incompatibility is immediate. Otherwise
the checker independently finds a prime with both actual integer degrees
retained and reduced gcd one. The integer Sylvester resultant then reduces
to a nonzero finite-field resultant, so the integer resultant is nonzero.
P and Q have no common algebraic root. No witness itself is reduced at
this auxiliary prime, so neither a rational denominator nor ramification
can invalidate the inference. This is an exact finite incompatibility
certificate for all parameter heights, not a numerical root search.

The complete new run independently regenerated and checked all 4,731,928
families, without a sample or missing group. Its resolution counts are:

| Certificate | New families |
|---|---:|
| Nonzero constant P | 5,908 |
| 101 | 4,495,784 |
| 103 | 218,175 |
| 107 | 11,555 |
| 109 | 477 |
| 127 | 26 |
| 131, resolving the three initial sentinels | 3 |

Every stored constant equals the independently computed nonzero P. For
every nonconstant record the two actual degrees, two leading residues,
degree retention, and coprimality were independently checked. The primes
were tested in order by my own frozen Euclidean routine; the six primes
were also verified by trial division. Thus the three sentinel cases fail
the original five-prime list in the sense required by that certificate
test and first pass at 131. Their preserved raw rows and both complete
integer polynomials match the unresolved-pair file exactly. The separate
resolver agrees with these independent results:

| (center mask,U mask) | degrees P,Q | leading residues modulo 131 |
|---|---|---|
| (117075,9220) | (15,20) | (83,3) |
| (117075,1548) | (12,20) | (44,79) |
| (117075,9356) | (15,20) | (97,124) |

All three gcds have degree zero. The initial sentinel rows are retained
in the raw stream rather than retroactively replaced. The distinct old
(6436,24785) resolver remains an explicit accepted dependency.

The complementary integer polynomial stream has SHA-256
`49da0560f41fdf3fce8a1ed7e63e877b5d51533de93142d74be7129d3db04da2`.
The uncompressed certificate stream has SHA-256
`e4dee952d410bf709b8c90dd61002ee88c4179a5fe7a8ca0678fe3644a25ffb1`.
Both match the frozen constructor values. Every one of the 79 gzip
chunks matches its recorded hash, byte count, and row count: 78 chunks
of 60,000 rows and a final 51,928 rows, totaling 28,442,028 compressed
bytes. The full result saves every degree-pair count, exact sentinel
polynomial, and chunk record. A separate postcheck also verified the
constructor's recorded source replacements and resolver-copy provenance
exactly; this code reuse is not independent-review evidence.

Combining the new checks with the explicitly accepted old finite facts
covers every one of the 6,224,952 refinements of all 6,680 masks. An
assumed normalized algebraic counterexample would supply a common
parameter root for one of these pairs. Each pair is incompatible, so
no such algebraic counterexample exists. The specialization argument
then excludes the hypothetical nontrivial complex counterexample.
This yields precisely C20: a cover of at most three complex recycled
values in degree 20 forces a linear power.

The computational outputs are finite exact evidence. Their uniform
mathematical implication uses the reconstruction, exhaustive coverage,
and nonzero-resultant argument, together with the accepted old pair
certificates; it is not an inference from bounded numerical searches.
No unresolved substantive objection was found in that chain.

## 5. Primary sources, attribution, and scope

I directly reread [CLO](https://arxiv.org/abs/1208.5404), Section 3.4,
PDF page 13, for the related valuation normalization. The new packet
supplies the finite-extension normalization above rather than silently
invoking rational-only consequences of the older packet. The normalized
Hasse identity was independently derived; no nonunit is divided after
reduction.

I directly reread [Massri v6](https://arxiv.org/abs/1806.09561v6), PDF
pages 13-14. Theorem 7.10 states the complex degree-20 three-recycled-root
claim. The present candidate appropriately reproduces that restricted
claim and does not assert novelty or validate Massri's original 3^17
computation. The cited v6 is a distinct source object from the earlier
withdrawn versions. No conclusion about every argument in that preprint
or the full Casas-Alvero conjecture is drawn here.

The cached primary PDF hashes are respectively
`d818747102d32060f43ae5f015f27065aadf38699b272a2367749db8b33fedbf`
and `8e5dec6d9d3ca1cb6becd7fa7e3d4c6ef18927cff9521c5f4eb9a1c1b567952f`.
Full third-party papers remain in the ignored cache; none is copied into
this review's tracked outputs. The only contest research scope addressed
is the restricted C20 result relevant to 2021 B4(b), not its preliminary
part or a degree classification.

## 6. Resource record and reproducibility

All new files use `reviews/three-complex-review-1*`. No old file, candidate,
other review, integration file, Git commit, push, or promoted status was
changed. No separately billed API or native CAS was used. Python 3.12.14
standard library suffices for the mathematical checker; pypdf reads sources.

Commands from the repository root:

    .venv/bin/python -u problems/2021-B4/reviews/three-complex-review-1-run.py --mode masks --timeout 20
    .venv/bin/python -u problems/2021-B4/reviews/three-complex-review-1-run.py --mode benchmark --limit 65536 --timeout 30
    .venv/bin/python -u problems/2021-B4/reviews/three-complex-review-1-run.py --mode full --timeout 900
    .venv/bin/python -u problems/2021-B4/reviews/three-complex-review-1-run.py --mode postcheck --timeout 30

Masks child PID 44699 exited zero and was reaped after 1.225 seconds.
Benchmark child PID 44769 checked 65,536 families, exited zero, and was
reaped after 6.461 seconds. Main child PID 44919 exited zero and was
reaped after 475.163 seconds under the explicit external 900-second
timeout. Its mathematical worker reported 475.110 seconds; the separate
supervisor elapsed time includes process setup/reaping. It saved
8,192-family checkpoints throughout. The postcheck child PID 46529
exited zero and was reaped after 0.165 seconds under 30 seconds. No
timeout, process termination, or global kill occurred. Reproduce in a
copied checkout if preserving the frozen R1 output metadata is required.

All 154 frozen candidate artifacts were rehashed after completion and
remain unchanged; all 19 old R1 artifacts and their manifest are also
unchanged. The independent extension source's pre-raw hash is identical
to its full-run hash. No failed finite family or incomplete run was
hidden. The three initial constructor misses and their independent
additional certificates remain explicit.

Authoritative weekly account telemetry read 11% total used at entry,
midrun, and after completion, with reset 1792745187 and a 10,080-minute
window. The 90% total-used cutoff and review/integration reserve were
respected; no new weekly window was used. The frozen review manifest
binds this report, issue log, source and input hashes, scripts, exact
outputs, results, and resource records. No peer new extension conclusion
was read before this report and its manifest were completed.
