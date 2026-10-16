# Independent adversarial audit R2: degree-20 three-rational-witness packet

Initial blind audit, 2026-10-16 UTC / 2026-10-17 Australia/Brisbane.
Reviewer did not construct the candidate. Requested settings: gpt-6.1-sol,
max reasoning. Effective-setting readback was unavailable and is not claimed.

**Recommendation: accept the scoped claims T1, T2 and T3, relative to the
specified separately reviewed input packets.** This audit reconstructs the
whole new argument and verifies every one of its 1,493,024 finite families.
No substantive objection remains from this audit. Only the coordinator may
promote a result after the independent-review gate. Degree 20 and the full
2021 B4(b) classification remain unsolved by this packet.

## Frozen target, independence, and scope

The target is `notes/coordinator-three-rational-witnesses-v1.md`, SHA-256
`be91345a8511338d55f30b140ee2555698c21d0e341efe29fe2536bca4fffbda`.
Its manifest SHA-256 is
`b01f42be62a8019fc6af3d6042434254e8f88fe6060dba6e454babf9eaa0cd78`.
All 50 manifest artifacts have the stated byte lengths and SHA-256 hashes;
the complete list of observed hashes is in
`three-witness-review-2-input-validation.json`.

I read AGENTS.md, the target, its manifest, and the three explicitly
designated mathematical inputs. I did not read another review report,
another reviewer's program or conclusions, shared issue/status files, or a
research log. The permitted raw dependency
`newton-review-1-extension-result.json` was used solely for its mask list,
after my own exhaustive mask derivation. Its other conclusions were not
used. Its frozen SHA-256 was checked by the manifest validation.

My ordinary-coefficient construction, mask enumeration, and finite-field
gcd program were written before reading constructor code or raw
certificates. That version is preserved as
`three-witness-review-2-construction-v1.py`, SHA-256
`72c7f6dbdf9486f628f19a1e855a945f3bfd040244160786f90bddf2b546863d`.
The timestamped precomparison freeze and independent-mask hash are in
`three-witness-review-2-construction-freeze.json`. Subsequently I inspected
only the constructor's stream/row serialization interface and result data
needed to compare exact streams. The comparison additions do not change
my independently written coefficient construction or Euclidean gcd.
No author module was imported or executed. The final full verifier is
`three-witness-review-2-independent.py`, SHA-256
`a9a0255a27c57cfd7ccac1528b8242233bdffb8e166545bd9c7d74b4d3be7b0e`.

The official [2021 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf),
page 2, confirms rational coefficients and a potentially different
**rational** common root for each derivative. The open target is part (b).
This audit neither solves nor reproduces the preliminary part (a).
T1 is a necessary witness-count restriction in degree 20, not a degree
classification. T2 and T3 are conditional structural consequences in the
same normalization. Other roots are allowed to be irrational or nonreal.

## Primary sources and accepted inputs

I checked CLO's [primary author PDF](https://arxiv.org/pdf/1208.5404),
§3.4, equations (9)-(10), Lemma 17, Proposition 10, and the characteristic-p
definitions and degree-5 bad-prime list. Their normalization applies to
the present characteristic-zero polynomial, and 19 is good for degrees
2 through 5. Their type definition and Proposition 7 concern a covering
set of recycled roots. The detailed local input hypotheses were also
checked against the designated input notes.

I checked Draisma–de Jong's [primary newsletter article](https://www.ems-ph.org/journals/newsletter/pdf/2011-06-80.pdf),
Proposition 6 on printed pages 31–32. It excludes two chosen recycled
values, not merely a polynomial with two total roots. It credits Draisma
and Knopper. The adjacent one-value observation is the appropriate
pure-power case. The later degree-family assertion in that article is
not used.

I read Massri's [version-6 primary PDF](https://arxiv.org/pdf/1806.09561v6),
Theorem 7.10 and its proof on PDF pages 13–14. The theorem claims exclusion
of three recycled roots for complex degree-20 CA polynomials, a stronger
claim than the present rational restriction. The candidate correctly
attributes that prior claim, does not claim novelty, and does not depend
on it. I have not audited Massri's separate exhaustive computation.

`three-witness-review-2-sources.json` records verification time, exact
hashes of all three local mathematical input notes, source URLs, source
locations, and hashes of the cached primary papers. No full paper was
copied into the tracked review artifacts. A web screenshot request for
Massri's final pages failed with a cache miss; the primary PDF text and
local cached PDF supplied the source check instead.

The separately reviewed inputs are used for the rational normalization,
the long-edge root count, exclusions of J=18 and J=17, and the J=16 and
J=15 center disjunctions. This audit checks their application and the
new complete certificate; it does not purport to replace the previous
independent audits of their 29,928-family and degeneration certificates.

## Whole-argument reconstruction: normalization and coverage

Assume a nontrivial degree-20 polynomial has a covering set of at most
three rational recycled roots. A covering set of one value gives a power;
the precise two-value obstruction excludes a two-value cover. We may
therefore work with three distinct covering values.

The unique root c of the nineteenth derivative belongs to the cover.
Choose a first-derivative witness r from the same cover. The input
normalization makes c simple, so r and c differ. The transformation
x -> r+(c-r)x, followed by division by the new leading coefficient,
is rational, preserves all common-root equations, and sends r to 0 and
c to 1. Hence the selected cover becomes {0,1,u}, where u is rational,
nonzero and different from 1. The input's valuation normalization applies
after this rational change: its temporary scaling to minimum valuation
zero can be followed by scaling the unit center to 1. The net scaling is
exactly by the rational center difference. It does not require all roots
to be rational.

Write f=sum c_t x^t. The forced ordinary coefficients are

    c_20=1, c_19=-20, c_1=c_0=0,
    c_(20-j)=binom(20,j)*a_j,  2<=j<=18.

Each a_j is 19-integral; every noncenter rational root has positive
**integral** 19-adic valuation. The center is simple. The first derivative
equation at 0 and the nineteenth derivative equation at 1 are already
encoded by these coefficients; f(1)=0 must still be imposed.

For each normalized derivative of degree j, choose the center whenever
it is available. This remains a choice inside the three-value cover.
Otherwise choose either 0 or u from that cover. Reducing a noncenter
witness equation gives a_j=0 modulo 19; reducing a center equation gives
the specified triangular residue equation. Since
v_19(binom(20,j))=1, the divided equation f(1)/19=0 supplies precisely the
final necessary congruence. These are implications from an actual
counterexample; no finite residue pattern is asserted to lift.

The canonical choice is important when applying a center disjunction:
if a theorem forces H_k(f)(1)=0, the j=20-k center bit must be set.
The converse requirement that a noncenter bit make the center fail is
not imposed on formal families. This only enlarges the enumerated family
and cannot remove an actual counterexample.

For the retained masks, each noncenter position has two labeled choices,
0 or U. At every stage the new coefficient is uniquely determined over
Z[U] by the selected Hasse equation. Thus an actual specialization is
forced by induction, without division and without a height bound on u.
The constant and linear coefficients remain zero throughout. Its
remaining necessary root equations are P(U)=f_U(1)=0 and Q(U)=f_U(U)=0.
No condition on the rationality of other roots is inserted. Cases where
U happens to be unused, or U=0 or 1, may be included as harmless excess.

## Independent exhaustive mask derivation

I used **ordinary Hasse coefficients modulo 19^2**, rather than the
author's a_j recurrence. Starting with c_20=1 and c_19=-20, at l=18 down
to 2 the noncenter branch sets c_l=0 modulo 361; the center branch sets

    c_l=-sum_(t=l+1)^20 binom(t,l)*c_t modulo 361.

The new c_l is always divisible by 19. A noncenter witness has a_j
divisible by 19, so c_l=0 modulo 361 is exactly the required necessary
ordinary-coefficient condition. On a center branch, the displayed
ordinary Hasse equation is exact modulo 361. The binomial identity

    binom(t,l)*binom(20,t)=binom(20,l)*binom(20-l,t-l)

connects these coefficients to the normalized derivatives. The leaf
check sum c_t=0 modulo 361 is f(1)/19=0 modulo 19. The greatest j with
c_(20-j) nonzero modulo 361 recovers J. This directly visits all 131,072
binary choices exactly once.

There are 6,680 congruence passes, with J counts

| J | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| count | 1 | 1 | 3 | 5 | 26 | 32 | 101 | 131 | 315 | 461 | 887 | 1674 | 3043 |

For J=18 the root-count input contradicts multiplicity m>=2. J=17 is
excluded by the accepted exact compatibility input. At J=16 the
disjunction concerns H_2 and H_3, exactly bits j=18 and j=17, retaining
88 of 887 masks. At J=15 it concerns H_2,H_3,H_4, exactly bits j=18,17,16,
retaining 69 of 461. The degeneration hypothesis applies there because
h=5, J>=10, and 19 is good for Hasse CA polynomials of degree 5 over the
algebraic closure of the residue field. No claim at h=6 or 7 is used.

The independently obtained survivors comprise 615 masks with J<=14,
69 with J=15 and 88 with J=16, for 772 in total. My complete sorted list
has no duplicates and matches the designated dependency list entry for
entry. Every mask has exactly 2^(17-popcount(mask)) refinements. Their
sum is **1,493,024**. The raw independent result is preserved as
`three-witness-review-2-independent-masks.json`.

## Every integer family and every finite certificate

My construction keeps ordinary coefficients c_t(U). For the next exponent
l and selected witness w in {0,1,U}, I solve

    H_l(f)(w)=c_l+sum_(t>l) binom(t,l)c_t*w^(t-l)=0

directly for c_l. This is triangular because binom(l,l)=1. Dense
integer arrays store powers of U in ascending order. A choice w=U shifts
an existing coefficient array by t-l; a choice w=1 does not shift it;
a choice w=0 makes c_l=0. The displayed binomial identity also proves
that c_l is a binomial coefficient times an integer polynomial, in
agreement with the normalized shape. No author recurrence or polynomial
helper is used.

At each leaf I construct P=sum c_t and Q=sum c_t U^t. The degree bounds
deg c_t<=20-t, deg P<=18 and deg Q<=20 follow by induction from this
construction. The computed integer degrees are checked against each
saved row; in fact every Q has degree 20. Polynomial trimming is exact.

The independent traversal is sorted by center mask and recursively takes
0 before U at each noncenter position. For **every leaf** it checks the
next raw row's exact (mask,U_mask) key, disjoint bits, correct range, and
absence of a duplicate U_mask within the mask. Each mask's complete
expected refinement count is checked, as are the global count and the
absence of an extra raw row. This is a uniqueness and coverage check,
not merely agreement of total counts.

For a constant certificate it checks that P is exactly the stated
nonzero integer. For each other row it verifies primality by trial
division, the two integer degrees, both nonzero leading residues, and
the **entire** Euclidean gcd computation in the indicated finite field.
It checks all 25 compressed-file hashes and byte lengths, exact raw row
serialization and uncompressed stream hash, all chunk row counts, and
the regenerated full integer polynomial stream hash.

| Independent certificate result | Families |
|---|---:|
| P nonzero constant | 772 |
| gcd 1 modulo 101 with both degrees retained | 1,416,728 |
| modulo 103 | 71,108 |
| modulo 107 | 4,109 |
| modulo 109 | 297 |
| modulo 127 | 9 |
| separate sentinel certificate modulo 131 | 1 |
| Total | 1,493,024 |

There is exactly one initial sentinel, key (6436,24785). Its integer P,Q
are independently regenerated and match the saved unresolved record.
Modulo 131 they have degrees (16,20), leading residues (8,102), and
constant gcd (the unnormalized Euclidean gcd is 77). The resolver's raw
record hash `68235145f9694471df510c6806dfaf4af3b7e4c519e1ef2396d655752d22dc3f`
also matches. A supplementary reconstruction records why each original
prime failed: P loses degree at 101; the gcd degrees at 103,107,109,127
are respectively 1,2,1,1. Thus the initial unresolved case is preserved
honestly and fully resolved by the additional certificate.

The following exact global hashes match the target:

    integer polynomial stream:
    aa5cd774ea5d10dcbb52a5bcee0d289d807ec7a364fd5921f29c9b412dda8cad

    uncompressed compact certificate stream:
    4befc080569dbe0d4d978efaef502e51f644163d15ef9bd22ae7112cf1840387

There are 24 chunks of 60,000 rows and a final chunk of 53,024 rows,
9,431,158 compressed bytes altogether. Complete per-chunk observations,
degree histogram, and sentinel details are in
`three-witness-review-2-full-result.json`. The independent verifier
actually checked all cases; the selected scalar self-checks in its source
are additional implementation checks and are not the claimed audit.

## Why these certificates exclude arbitrary rational witnesses

A constant nonzero P cannot vanish at any characteristic-zero value.
For a prime certificate, the reduced polynomials retain the actual
integer degrees and are coprime. Their finite-field Sylvester determinant
is therefore nonzero. Reduction commutes with the determinant of the
integer Sylvester matrix of those same degrees, so the integer resultant
is nonzero. Consequently the original P,Q have no common root over an
algebraic closure of Q, and in particular no rational specialization u.

This argument does not specialize u modulo the certificate prime. Thus
a denominator divisible by that prime creates no exception. It needs no
finite rational-height bound, no integrality of u at the auxiliary prime,
and no assumption about the other roots of f. This is the unrestricted
parameter step; the finite certificate is used only after exact symbolic
coverage has reduced the proposed cover to those finite families.

The three-witness assumption therefore leads to a contradiction in every
permitted mask/refinement. Together with the precise one- and two-witness
inputs, this establishes the proposed scoped T1 subject to the project's
independent-review promotion decision.

## Reconstruction of T2 and T3, including the quotient argument

For J>=10 the accepted long-edge statement gives J-1 root slots of
valuation 1/(J-1), a noninteger, so none is rational. Of the other h+1
slots, m are 0 and one is the simple center 1. There are at most h-m
other distinct rational roots, giving at most h-m+2 rational roots in
total. T1 forces at least four because all available rational roots
together always form a covering set. Hence m<=h-2.

For J=16, h=4 and m>=2 force m=2. Exactly two remaining small slots
must supply two distinct rational values u,v, otherwise four rational
roots are impossible. Both are nonzero, different from 1, and have
positive integral 19-adic valuation. All four rational roots are needed
for a cover by T1. The remaining 15 slots are exactly the long cluster,
each with valuation 1/15.

For J=15, h=5 gives m=2 or 3 and excludes m=4. If m=3, again there
are precisely two small nonzero slots and both must be distinct rational
roots u,v. The remaining 14 slots are the long cluster, each of valuation
1/14. If m=2 there is an extra small slot, and the candidate appropriately
makes no corresponding exact residual-quotient assertion.

In the J=16 case, monic division by x^2(x-1)(x-u)(x-v) stays in
Z_(19)[x]: synthetic division by a 19-integral rational root preserves
19-integral coefficients. It is an exact rational quotient of degree 15.
In the J=15,m=3 case the same statement holds for
x^3(x-1)(x-u)(x-v), with quotient degree 14. In either case let N be the
quotient degree; **all** its roots have valuation 1/N.

The coefficient of x^(N-r) is a signed sum of products of r roots.
Every summand has valuation r/N>0, so the coefficient has at least that
valuation, or is zero. Rationality makes every finite valuation integral,
hence each nonleading coefficient is divisible by 19 in Z_(19). The
constant coefficient is a single product of all N nonzero roots, so its
valuation is exactly N/N=1, with no cancellation. The monic quotient is
Eisenstein over the 19-adic valuation ring and is irreducible over Q_19,
therefore over Q. This does not infer a rational factor from an arbitrary
Newton edge: the quotient is rational because all removed roots were
explicitly rational, and its exact degree accounts for the whole cluster.

These arguments justify all assertions of T2 and the stated scope of T3.

## Adversarial cases and issue disposition

I specifically tested the points that could invalidate the coverage or
the unrestricted conclusion: choosing the first-derivative witness from
the original cover; a center root coinciding with it; canonical center
flags when multiple witnesses exist; duplicate or omitted refinements;
zero or constant polynomial cases; auxiliary-prime denominators; loss of
degree on reduction; the initial sentinel; rational-root multiplicities;
the two small roots coinciding; and an unjustified rational Newton factor.
They are resolved by the arguments and full checks above.

`three-witness-review-2-issues.json` records these audit questions and
their disposition. There is no requested author repair and no remaining
substantive objection from this initial blind audit. This conclusion is
limited to T1–T3 and the designated input dependencies. It does not
certify Massri's computation or exclude four or more rational witnesses.

## Reproduction, resource use, and process cleanup

From the repository root, the full independent run is

    .venv/bin/python -u problems/2021-B4/reviews/three-witness-review-2-run.py full 420

The wrapper launched dedicated child PID 35352 at
2026-10-16T15:49:36.871102+00:00. Its explicit external timeout was 420
seconds, with checkpoints every 16,384 families (91 full-run checkpoints).
It finished at 15:51:48.934174+00:00 with exit code 0, 132.063 seconds
including wrapper overhead, empty stderr, no timeout, and no termination
needed. The child was reaped. No global process kill was used. The exact
command, source hash, PID, timestamps and output paths are preserved in
`three-witness-review-2-full-job.json`; complete incremental stdout and
stderr are retained separately.

An 8,192-family independent benchmark also finished with exit code 0
under a 30-second external timeout, PID 35231. Its source and output
are retained. The supplementary sentinel command is

    .venv/bin/python -u problems/2021-B4/reviews/three-witness-review-2-sentinel.py

It uses only the reviewer's own implementation, standard-library integer
arithmetic, and finished in under a millisecond of measured arithmetic.
No native CAS routine or new dependency was used. Python is 3.12.14;
pypdf 6.10.0 was used only to inspect cached primary source pages. No
installation, charge, separately billed API, commit, or push occurred.

Authoritative account-wide telemetry was checked at the start and during
the sustained audit: 9% total weekly used, reset timestamp 1792745187.
This is below the 90% cutoff and was not interpreted as 9% of a remaining
allowance. No new weekly window was entered. All retained reviewer artifacts
have the `problems/2021-B4/reviews/three-witness-review-2` prefix; no
candidate, other review, or coordinator-owned integration file was edited.

This report and its artifacts are frozen before cross-review. The
timestamped final freeze manifest records their hashes and blindness
declaration. Project promotion remains the coordinator's decision.
