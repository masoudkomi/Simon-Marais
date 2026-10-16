# 2017 B4 research log

## Reviewed direction-coarsening result

DC1 and DC2 are now **proved, independently reviewed partial results**, as
is the conditional implication from full fixed-direction hypothesis (H) to
existence of the official limit. Both initially blind whole audits and
issue ledgers were read in full by the coordinator and their manifests
verified. The accepted exposition is proofs/reviewed-direction-coarsening-v1.1.md;
see reviews/coarsening-acceptance.md/json. H remains unproved, and exact
rates remain unknown. New research concerns the boundary extension needed
for H; no routine enumeration was added. Earlier checkpoint prose below
records its historical stage.

## Coordinator update after the deeper literature pass

The concavity candidate is now **proved, independently reviewed (partial result)**: the official limsup is below0.649514. Two fresh whole audits reconstructed the exact published cutpath domain, entropy endpoints, symmetrization, both supporting planes, uniform exact slack and marked-count insertion transfer. See proofs/reviewed-concavity-v1.1.md and reviews/concavity-acceptance.md/json. Initialize at B2; the harmless one-line zone wording is not used. The older pruned tree only needs at most one blue successor. No substantive repair remains. This improves the located0.6496 bound within the project; novelty and exact rates remain unresolved. The earlier owner checkpoint below is historical.

## Checkpoint, 2026-10-16

Status: **open in the latest directly inspected research statements; no new full solution or new substantive partial theorem proposed**. The entire official B4 is the authorized open target. Its two exact rates are not found by this pass. Current strongest located published bounds and their conventions are in references.md. This distinction matters: the 2017 notes' old constants are neither current best bounds nor a solution.

Launch settings requested by the coordinator: `gpt-6.1-sol`, `max`. No independent effective-setting readback was available. Only this year directory was edited, and no worker commit or push was made.

## Exact object and finite encoding

The official notes' identification with A006245 is the counting dictionary used throughout. A fixed polygon is intended; its orientations are distinguished. A marked wiring diagram has strand labels forced by the boundary order, so these labels do not introduce an extra factor of \(n!\). The crossing order on every strand records the arrangement. Commuting independent adjacent swaps changes the linear order in which disjoint crossing events are processed, but preserves these strand orders. Our script stores the full tuple of strand orders, rather than an insertion history or a geometrically normalized picture.

For a second finite representation, attach a binary sign to every triple \(a<b<c\): whether the crossing \(ab\) occurs before or after \(bc\). For every ordered four-set, the signs on its lexicographically ordered four triples have at most one sign change. The script exhaustively searches that local predicate with forward rejection of impossible partial assignments. Its agreement with the full reduced-word enumeration through 6 is a useful implementation check. A general equivalence of this predicate with the intended tilings belongs to the published higher-Bruhat/signotope dictionary; no new proof of that equivalence is asserted here.

## Approach 1: exact enumeration and the commutation quotient

Completed, bounded computational evidence:

| n | Reduced swap words | Distinct full strand-order tuples | One-change triple sign patterns |
|---|---:|---:|---:|
| 2 | 1 | 1 | 1 |
| 3 | 2 | 2 | 2 |
| 4 | 16 | 8 | 8 |
| 5 | 768 | 62 | 62 |
| 6 | 292864 | 908 | 908 |
| 7 | deliberately not run | deliberately not run | 24698 |

Through 6 the **entire sets** of triple signatures, not only their cardinalities, agree between the two algorithms. The exact word multiplicities within classes are preserved in the output. Already at \(n=4\), four classes have one word, two have two, and two have four. At \(n=6\), the multiplicity ranges from 1 to 7896. Therefore counting swap words and dividing by a supposed universal class size is invalid. We do not quotient by polygon symmetries.

The printed published table extends to 16 and gives \(\log_2 C(16)/16^2=0.374796117777\ldots\). Those larger values are transcribed literature data, not newly enumerated results. They do not establish a limiting constant or justify extrapolating a curve. Computation of all reduced words was stopped by design at 6, since the next level already has over a billion histories.

## Approach 2: fixed-direction statistical mechanics and bundle gluing

The solvable three-bundle subsystem is an instructive benchmark: MacMahon's product counts lozenge tilings of a hexagon whose three side lengths may exceed 1. This subsystem has repeated directions and is **not** the official regular \(2n\)-gon with all side lengths 1. Felsner–Valtr's published gluing injection is the bridge to the official family. `macmahon_check.py` independently evaluates the product using exact fractions for bundle sizes 1, 2, 3, 4, 8 and 16. The values begin 2, 20, 980, 232848. It also checks the arithmetic of their historical coefficient \(\tfrac34\log_2 3-1\).

Obstruction to getting the exact B4 rates this way: an explicit large family supplies only a lower bound. There is no argument that nearly all tilings have three bundles, or that the complement contributes a smaller exponential rate. A thermodynamic limit for a fixed number of directions cannot simply be reused when the number of directions itself tends to infinity and every boundary edge has length 1. The interface and boundary complexity must be controlled uniformly in that growing number.

The modern patch approach is a genuine refinement of this lower-bound mechanism. Its important extra datum is the full boundary pairing of a patch: the interior counts can be multiplied only when reroutings preserve that datum. Counting all local arrangements with the same number of strands ignores boundary pairing and can overcount incompatible assemblies. This is the promising constructive route for a later bounded experiment, but no new patch constant was obtained here.

## Approach 3: insertion counts, average versus maximum

Delete the strand whose boundary label is largest to obtain the canonical parent in the marked arrangement enumeration. Our triple-sign data records the number of extensions per parent, without summing over all possible deleted labels. The resulting exact computational evidence is:

| Parent strand count | Parents | Minimum children | Maximum children | Average children |
|---|---:|---:|---:|---:|
| 2 | 1 | 2 | 2 | 2 |
| 3 | 2 | 4 | 4 | 4 |
| 4 | 8 | 7 | 9 | 7.75 |
| 5 | 62 | 11 | 20 | 14.645161290323 |
| 6 | 908 | 16 | 45 | 27.200440528634 |

This separates two quantities often conflated: the actual ratio \(C(n+1)/C(n)\) is an average extension count, while a uniform maximum is only an upper bound for that ratio. Improving a worst-case bound does not identify the average. Conversely, uniformly choosing one child at each insertion step does not produce a uniform random final tiling: its probability is the product of reciprocal branch sizes. Uncorrected simulations would favor some tilings. Even a correctly weighted estimator can have extreme variance, as Rote's primary experiments explicitly warn.

A possible future approach is a potential function or a finite collection of boundary statistics controlling sums of children, rather than the worst individual parent. The small data can test proposed local statistics, but it cannot certify an unrestricted inequality. No claim of convergence of average extension entropy is made.

## Approach 4: supermultiplicativity and an entropy limit

Temptation: glue two independent arrangements and apply Fekete's lemma. Even granting a bound \(C(n+m)\ge C(n)C(m)\), Fekete normalizes \(\log C(n)\) by \(n\), not by \(n^2\); it does not determine B4. To make this work at quadratic scale, one would need a much stronger replication theorem, with sufficiently many independently choosable copies and a controlled loss.

One tempting but unsupported assertion is \(C(kn)\ge C(n)^{k^2-o(k^2)}\) uniformly enough in the block size. There is no construction for this in the present work. Arbitrary pairwise gadgets do not automatically fit into one planar wiring diagram: their triple crossing orders must be globally compatible. The published use of liminf and limsup, with limit existence still open, is a reason to scrutinize such a short argument especially carefully. This route is logged as an obstruction, not a candidate proof.

## Approach 5: entropy on triple signs and naive planar encodings

The triple-sign encoding has \(\binom n3\) bits. Treating them as independent gives a cubic-exponent bound and loses the known quadratic scale. Local four-set constraints substantially reduce the space, but simply applying a hereditary-substructure entropy bound in the triple coordinates retains a cubic normalization. An additional geometric compression or an inequality exploiting overlap at the right scale is required.

At the opposite extreme, enumerating all possible orders of the \(\binom n2\) crossings gives a factorial bound with an unwanted \(n^2\log n\) exponent. Taking a general planar-map encoding can recover the quadratic scale but does not by itself identify the leading constant. These observations explain why neither naive encoding is a solution. The successful published upper bounds use more geometry; their certificates have not been independently audited here.

## Next research checkpoint

1. Preserve the exact small enumerator as a regression oracle for any later patch or insertion work. Extend only with an explicit wall-time/memory budget; do not chase a new exact value of \(C(n)\) using reduced words.
2. If returning to the lower bound, specify a patch's boundary pairing exactly and independently validate its dynamic program before optimizing patch shapes. Compare against the known three-bundle product.
3. If returning to the upper bound, investigate correlations between extension count and simple parent statistics. First test whether a proposed potential predicts sums over children; do not infer an asymptotic bound from finite correlation.
4. Any proposed full or substantive partial argument must begin as **candidate proof - unverified**, then receive two fresh independent adversarial audits, one reconstructing it. No such promotion is requested at this checkpoint.
