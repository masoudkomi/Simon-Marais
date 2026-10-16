# Deep literature investigation: 2017 B4

Checked 2026-10-16 UTC. Research worker R2; requested GPT-6.1-sol/max,
effective-setting readback unavailable. This separate task began after the
blind 2021 J16 audit was frozen. Only the entire official 2017 B4 is in
scope. Existing proofs, reviews and central source files were not changed.
New mathematics below is **candidate proof - unverified**.

## Outcome and exact scope

The strongest bounds located in the inspected primary texts remain
`c_minus > 0.2721` and `c_plus < 0.6496`, where
`c_minus=liminf log2 C(n)/n²` and `c_plus=limsup log2 C(n)/n²`.
Neither equality of these quantities nor either exact value was located.
The 2025 upper-bound paper expressly calls existence of the limit open.
This is a dated search result, not an assertion that no later or unpublished
result exists.

The full 2025 entropy objective suggested a joint-concavity reduction.
A self-contained proposed improvement `c_plus < 0.649514` is frozen in
[the separate candidate](deep-literature-r2-concavity-candidate-v1.md), with
its exact logarithm certificate and
[freeze manifest](deep-literature-r2-concavity-freeze-v1.json). It requires
two fresh independent whole reviews. It is not a full B4 solution and has
not replaced the published frontier in any shared file. Its novelty is
unestablished.

## Source fidelity and the current frontier

The official [problem](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf)
asks for both asymptotic exponents of tilings of a fixed regular 2n-gon,
side length one, by unit-edge quadrilaterals. The
[official notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf),
p. 12, resolve the convention through C(3)=2, C(4)=8 and A006245.
The relevant arrangement count is simple, marked by a north unbounded
cell, with orientation distinguished. Reduced words, projective unmarked
arrangements and counts modulo reflection are different finite sequences.
The standard tiling dictionary is attributed context, not newly proved here.

1. Fernando Cortés Kühnast, Justin Dallant, Stefan Felsner and Manfred
   Scheucher, [arXiv:2402.13107v2](https://arxiv.org/pdf/2402.13107v2),
   2024-03-21, full 19-page author version, SoCG 2024,
   [DOI 10.4230/LIPIcs.SoCG.2024.43](https://doi.org/10.4230/LIPIcs.SoCG.2024.43).
   Theorem 1 and the constructions give `c_minus > .2721` for the same
   marked count. The paper merged two independent submissions. The earlier
   Dallant [arXiv:2402.13923v1](https://arxiv.org/pdf/2402.13923v1) gives
   .2604 and is superseded for the numerical frontier; its full text was
   cached but not independently audited in full during this pass.
2. Justin Dallant, [arXiv:2502.20909v2](https://arxiv.org/pdf/2502.20909v2),
   2025-03-07, full 12-page author version. Lemmas 3--7 give the .6496
   upper bound through cutpaths and the tight zone theorem. The current
   arXiv record still lists v2. Its version note matters: v1 accidentally
   retained the unnecessary hypothesis `n-u<=m` in Lemma 3; v2 removes it.
   Our proposed concavity reduction uses the actual v2 domain, with both
   `m<n-u` and `m>=n-u` cases retained. A historical paragraph on PDF p. 2
   repeats an older upper constant incorrectly; the main theorem and
   Section 2 are the relevant statements.

I checked the current [Scheucher](https://scheucher.dev/) and
[Dallant](https://justindallant.com/) publication pages and forward searches
through 2026. A newly located
[Rote talk, Oswinfest 2026](https://page.mi.fu-berlin.de/rote/Papers/slides/Oswinfest-2026-Enumeration%2Band%2BCounting%2Bof%2BPseudoline%2BArrangements.pdf)
reports the finite A006245 count for n=16 and a counting algorithm, not
existence or determination of the asymptotic limit. Its early asymptotic
slide still prints an older upper bound, so it is not a reliable replacement
for the 2025 frontier paper. The talk date alone does not date its reported
enumeration. The web tool exposed its full 167-page slide PDF; two normal
curl attempts timed out at 45 and 30 seconds, respectively, so no downloaded
original hash is claimed for this source.

## Lower-bound mechanisms and the project's fixed-direction work

The full SoCG paper's Section 5.1 encodes a patch by its paired cyclic
boundary word, chooses one segment z, and sums over legal crossing orders
on z. Noncrossing pairs force order relations; the admissible orders are
linear extensions of the resulting partial order. Every order determines
two smaller paired-boundary patches and contributes `F(P1)*F(P2)`.
Canonical relabelling supplies memoization. If a patch boundary cuts one
geometric line into disconnected segments, they must receive distinct
segment labels until the actual boundary matching is restored. Losing this
information changes the fiber count.

Section 5.2 gives a faster special three-family route. After shifting paths
to remove shared vertices, the model is a finite directed acyclic graph.
Its source/sink order ensures that any vertex-disjoint family has the
identity endpoint pairing. Only under this compatibility hypothesis does
the Lindström--Gessel--Viennot determinant count the desired unsigned
families. The paper uses a matrix of size 2l-1 for an l by l square patch;
at l=1000 its certified logarithm exceeds 1397192. This source computation
took about 18.5 hours; general patch calculations used up to 1 TB RAM.
I did not rerun those computations or launch a larger patch search.
The public [supplemental repository](https://github.com/fcorteskuehnast/counting-arrangements)
has MIT-licensed code, small configurations and an LGV Sage script. It was
inspected for discovery; its code was not executed in this pass.

Crucially, Section 6 explains a limitation even within the fixed-k model:
imposing one global periodic patch structure cannot recover all F_k,
even if arbitrarily large finite patches could be counted. It also keeps
fixed-k entropy questions separate from B_n. This corroborates the scope
restriction on the project's reviewed four-direction periodic-grid limit:
that theorem concerns one fixed boundary family, not the official
growing-direction count. A transfer to C(n) would need a uniform comparison
as the number of directions grows; fixed-D limits alone do not supply it.

A backward reference chain leads to Nicolas Destainville, Rémy Mosseri and
François Bailly,
[Fixed-boundary octagonal random tilings: a combinatorial approach](https://arxiv.org/pdf/cond-mat/0004145v2),
v2 dated 2000-08-25. Sections 2--3 describe fixed 4-to-2 octagons with side
parameters k1,k2,k3,p. Projecting away one direction leaves a 3-to-2 base
tiling; the remaining heights are constrained partitions on that base.
For fixed first three sides the exact count has an additive binomial form
`W(p)=sum_j a_j binom(p+K-j,K)`, `K=k1*k2+k1*k3+k2*k3`.
The coefficients record descents of maximal walks in the associated
configuration space. Their sum has a product expression, but the complete
descent distribution remains the information needed for W(p).
Fibers over different bases are not interchangeable independent boxes.
The empirical diagonal entropy near .36 uses natural logarithms per tile
and fixed-direction boundary conditions; it is not a rigorous .36 bound
for this competition's base-two growing-direction exponent. The paper also
distinguishes fixed from free/periodic boundaries, which affect entropy.

The 2026 Rote slides, pp. 18--41, offer another concrete algorithmic lead:
sweep a fixed k-line arrangement by a rope and record both the distribution
and permutation of l extra strands at each rope. Sparse partial-arrangement
transition tables are composed between successive ropes. The order state
is essential: the slides explicitly show a partial arrangement that is
valid for one input permutation and invalid for another. A small bounded
implementation could cross-check the reviewed paired-boundary fiber
method; the reported n=16 computation required very large resources and
is not an appropriate job to reproduce in this workspace.

## Upper-bound mechanisms and actionable mathematics

Dallant classifies each cutpath by six integers `(m,k,u,m',k',u')`.
The exact v2 constraints include `k<=m<=n`, `k+u<=n`, their primed
versions, `k<=u'`, `k'<=u`, and
`m+m'-u-u'<=1.5n`. The last inequality combines the two exit counts
through the zone theorem. The logarithmic objective is the minimum of
the two directional entropy bounds. The new frozen candidate rewrites
one directional bound as a sum of two concave perspectives, then averages
the directional triples. This leads to a one-variable concave tangent
bound near .21, rather than another large LP run. The exact certificate
uses rational logarithm intervals with 80 terms, a dedicated child with
30-second external timeout, PID 59036, exit 0 and reaped state. It adds no
independent verification by itself.

The more substantial published avenue is Section 4's weaker Conjecture 12:
every n-pseudoline arrangement has at least one line of zone complexity
at most `9n+O(1)`. One needs only a good deletion line at each stage;
specifying the deletion order costs O(n log n) bits. A proof of this
minimum-line statement would give the paper's .6074 bound, without first
proving its stronger average-zone Conjecture 11. The supported-cell zone
convention must be retained throughout.

Following that citation leads to Shira Zerbib,
[On the zone complexity of a vertex](https://arxiv.org/pdf/1604.07268v1),
[SIAM J. Discrete Math. 25 (2011), 719--730](https://doi.org/10.1137/100787246).
The full author PDF's theorem concerns straight lines in the real
projective plane in general position: some crossing becomes a face of size
at most five after its two incident lines are deleted. The discharging
proof and tight example concern a vertex, not a line. The author-posted
arXiv version is dated 2016 in the record (the cached PDF has a later
compilation dateline); the journal's primary record confirms publication
in 2011. Its line-zone convention counts faces after deleting the line,
with leading constant 5.5 rather than Dallant's supported-cell 9.5.
Transferring a vertex discharging argument to a good line for all
pseudoline arrangements is an actual missing theorem, not a consequence
of the five-face bound.

Priority next steps: review the frozen concavity candidate completely;
then seek a charge identity for one good deletion line under Dallant's
zone convention. For lower bounds, compare tiny paired-boundary DP counts
with source LGV or rope transitions before considering new geometries.
None of these steps establishes the requested exact exponents.

## Setter provenance and access limits

The contemporary Do--Guttmann--Henderson report in the Gazette, May 2018,
pp. 79--83, discusses this B4 but supplies no individual setter credit in
the inspected material. McNamara's contemporary committee-related blog
does not establish authorship of B4. The current 2026 committee roster,
topic overlap, chairmanship and authorship of commentary are not evidence
of a 2017 setter. The setter remains unknown in this packet. No one was
contacted.

All downloaded full papers and derived page images/text remain in ignored
`.cache/`; `.gitignore` explicitly ignores that directory and `*.pdf`.
Hashes, actual read scope, versions, queries and failed routes are in
[the search/source manifest](deep-literature-r2-search-sources-v1.json).
No Git actions, charges, access bypass or unrelated problem work occurred.
The latest authoritative weekly telemetry during this task was 15% total
used in the 10080-minute window, reset timestamp 1792745187, below the
90% cutoff.
