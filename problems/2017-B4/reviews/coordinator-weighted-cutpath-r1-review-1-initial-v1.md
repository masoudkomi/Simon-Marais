# ENTIRE initially blind weighted-cutpath WHOLE review R1

2026-10-18 UTC. Reviewer C, `/root/review_2017_coarsening_r1`.

**Verdict: no substantive defect found in WC1–WC3 as stated. No author repair is required by this audit.** This is one independent whole review, not promotion. Root alone constructed the new weights, Cauchy comparison and hand constants and is excluded from both required reviews. This entire report, all forty ledger entries, issue/source/work records, code and metadata were completed before opening or hashing any corresponding new R2 review material. Findings are withheld until the coordinator confirms both entire initial freezes.

I authored older 2017 annulus/rank-mesh/profile and plane-interface work and reviewed other earlier submissions. Those roles are disclosed rather than represented as fresh independent reviews of my own inputs. The new WC proof uses the published cutpath interfaces and elementary graph/analytic arguments, not my old entropy-recovery constructions. I did not construct WC. Requested inherited setting is gpt-6.1-sol/max; effective readback is unavailable.

The immutable main under review is `notes/coordinator-weighted-cutpath-r1-candidate-v1.md`, 12695 bytes, SHA256 `f77d09e57a7462faaf6d48077c6815b9d33ffa722470596a947b9f46c4205928`. Its freeze is 2672 bytes, SHA256 `2ff11ebea88c684a2d86be972ae6f937ec5aec95040904eb27fc5c392ad7b4d4`. I read all ten constructor artifacts, including all forty obligations, the entire metadata program and its outputs. Administrative integrity checks do not count as mathematical validation.

## 1. Exact target, counting object and imported geometry

The official 2017 B4 concerns integer n≥2, tilings of the fixed regular 2n-gon of unit side length, and the lower and upper accumulation rates of n⁻² log₂C(n). There is no preliminary part. I read B4 in the original paper and the B4 comments in the official notes, which identify the intended sequence and distinguish the two hexagon tilings. No other contest problem is investigated.

The attributed dictionary is the fixed-orientation marked-arrangement dictionary, not an unmarked quotient. Dallant's introduction explicitly uses simple arrangements, one transverse intersection per pair, no triple point, a north unbounded cell and orientation/north-preserving equivalence. Felsner–Valtr's introductory representations fix the boundary-induced labels and identify the corresponding unrotated zonotopal tilings. Their Section 2 gives the canonical deletion/insertion inequality. The official notes cite this same counting context. Thus WC uses B_n=C(n), B₂=1, without multiplying by arbitrary label permutations or counting all sorting words before commutation. These are attributed source interfaces; I do not newly re-prove the complete foundational representation-equivalence theorem.

In an actual wiring dual, a downward edge crosses one pseudoline from its north side to its south side. The number of south-side signs increases by one. A north-to-south path therefore has exactly n edges, not an uncontrolled variable length. The graph and all such path sets are finite. Rotating the drawing by 180 degrees and reversing the path identifies exactly the same complete paths in the opposite direction. The rotation is orientation preserving and exchanges north and south; it introduces no new path choices.

For each forward complete path p, let u count unique exits taken and k count middle exits taken. A visited nonunique tail has exactly two extreme exits and d≥0 middle exits, with integer d. A two-exit cell has d=0 and is nonunique. Let m be the sum of **all available** middle exits over visited tails, including untaken alternatives. The terminal south cell contributes no forward exits. Reverse statistics on the same path use the corresponding opposite tails.

The operative published implications are

\[
k\le u',\quad k'\le u,\qquad m+m'-u-u'\le \tfrac32 n.
\]

I checked Dallant's original definitions and actual Section 2 statements, including the middle/unique correspondence and its zone comparison. The lower-boundary count is m+u+2(n−u)=2n+m−u; the opposite count is 2n+m'−u'. This is exactly the statistic combination used in WC. Dallant's Lemma 5 supplies a stronger finite boundary-edge estimate; the proof needs only its weakened displayed consequence for n≥2. It does not require the old six-variable domain to be sufficient for realization, nor Lemma 3's binomial refinement, nor its optimization certificate. The sharp earlier zone theorem is imported through the stated published pseudoline interface, not freshly independently proved here. See the source record for the literal reading boundary.

The n=1 finite-size issue from the older project proof is avoided: WC starts at n=2. For the two-line arrangement, the two cutpaths each take one nonunique two-exit step and one unique step; m=m'=k=k'=0, u=u'=1. This hand boundary check is consistent with the statistics and does not invoke an enumeration program.

## 2. The forward and reverse measures really live on the original path set

Assume L,M,V>1, L=MV, and

\[
2+d/V\le LM^d\quad(d=0,1,2,\ldots).
\tag{R1}
\]

At a unique tail assign its only edge weight 1. At a nonunique tail with d available middle exits, give each extreme weight (LM^d)⁻¹ and each middle weight (LM^dV)⁻¹. The outgoing sum is

\[
\frac{2+d/V}{LM^d}\le1.
\]

This assigns an edge weight before a path's eventual statistics are known. In particular, two prefixes merging at one original vertex see the same outgoing weights. Nothing is defined on a pruned decision tree or retrospectively conditioned on k,u,m.

Unfold the finite graph into the tree of directed prefixes from north. The product weight of a prefix bounds the sum of product weights of its immediate children. Iterating this elementary inequality, or adding zero-weight lost leaves, bounds the sum over complete north-to-south paths by one. Reconvergent prefixes remain distinct tree vertices, so reconvergence never merges distinct counted paths. A sink requires no outgoing probability normalization; discarding dead ends or mass loss can only decrease the complete-path sum. There is no issue of an infinite flow limit because every complete cutpath has length n and the graph is finite.

There are exactly n−u nonunique forward tails. Their d values sum to m. Precisely k chosen edges pay the extra V⁻¹. Hence

\[
W(p)=L^{-n+u}M^{-m}V^{-k},\qquad \sum_pW(p)\le1.
\tag{R2}
\]

Applying the same local rule in the rotated graph gives, on the **same indexed set** of complete p,

\[
W'(p)=L^{-n+u'}M^{-m'}V^{-k'},\qquad\sum_pW'(p)\le1.
\tag{R3}
\]

No independence of W and W' is claimed or needed. Finite Cauchy–Schwarz, applied to the vectors (√W(p)) and (√W'(p)), gives

\[
\sum_p\sqrt{W(p)W'(p)}\le
\sqrt{\left(\sum_pW(p)\right)\left(\sum_pW'(p)\right)}\le1.
\tag{R4}
\]

It would be invalid merely to multiply unrelated upper estimates for a path count; R4 is a valid comparison of two explicit measures on one finite set.

## 3. The geometric-mean lower bound has both inequality directions correct

Write U=u+u', T=k+k', A=m+m'. Then

\[
\sqrt{WW'}=L^{-n+U/2}M^{-A/2}V^{-T/2}.
\]

Since T≤U and V>1, replacing T by U makes V⁻ᵀ⁄² smaller, so

\[
\sqrt{WW'}\ge L^{-n+U/2}M^{-A/2}V^{-U/2}
=L^{-n}M^{-(A-U)/2}.
\]

The equality uses L/V=M. Since A−U≤3n/2 and M>1,

\[
\sqrt{WW'}\ge L^{-n}M^{-3n/4}=(LM^{3/4})^{-n}=K^{-n}.
\tag{R5}
\]

If A−U is negative the intermediate factor is larger, not smaller, so no extra nonnegativity assumption is hidden. The equality case T=U is harmless; no strict geometric-statistic inequality is required. Summing the lower bound R5 and using R4 gives γ_nK⁻ⁿ≤1 and thus γ_n≤Kⁿ. There is no missing number-of-statistic-classes factor: the sum is directly over every complete path. This proves WC1 once R1 is established for the chosen constants.

## 4. All local integer degrees, including 0,1 and arbitrarily large d

Take L=527/250, M=49/40 and V=2108/1225. Direct reduction gives L/M=V and all three exceed one. In particular V is positive and all cross multiplications below have positive denominators.

For d=0, L−2=27/250>0. For d=1,

\[
LM=25823/10000,\qquad 2+V^{-1}=5441/2108.
\]

Independently expanding the comparison gives

\[
25823\cdot2108=54{,}434{,}884,
\quad5441\cdot10000=54{,}410{,}000,
\]

whose difference is 24,884. For d=2,

\[
LM^2=1265327/400000,\qquad2+2V^{-1}=3333/1054,
\]

and

\[
1265327\cdot1054=1{,}333{,}654{,}658,
\quad3333\cdot400000=1{,}333{,}200{,}000,
\]

with difference 454,658. Thus R1 is strict at d=0,1,2.

For every integer d≥2 put g_d=(2+d/V)/M^d. Then

\[
g_{d+1}/g_d=\frac{2V+d+1}{M(2V+d)}
=M^{-1}\left(1+\frac1{2V+d}\right).
\]

The parenthesized expression decreases with d. At d=2 its value is 7891/6666, whereas

\[
49\cdot6666-40\cdot7891=326634-315640=10994>0.
\]

Therefore g_{d+1}<g_d for every d≥2. The already verified g₂<L proves R1 for every larger integer. There is no maximum-degree assumption and no scan. Restricting to integers is legitimate because d counts actual edges; the report makes no claim for all real d. WC1 follows for every n≥2 independently of how large a cell's degree grows with n.

## 5. The strict logarithmic comparison is a hand proof

For 0<t<1, the finite geometric identity integrated from 0 to t gives

\[
\log(1+t)=t-t^2/2+t^3/3-\int_0^t\frac{s^3}{1+s}\,ds,
\]

and analogously the degree-five truncation has remainder −∫₀ᵗs⁵/(1+s)ds. Both remainders are strictly negative. No asymptotic Taylor assertion or floating-point error estimate is being used.

At t=27/500, the cubic numerator over denominator 375,000,000 is

\[
20{,}250{,}000-546{,}750+19{,}683=19{,}722{,}933.
\]

The numerator for 527/10000 at the same denominator is 19,762,500. Their difference is 39,567>0, so log(527/500)<527/10000.

At t=9/40, the degree-five numerator over 512,000,000 is

\[
115{,}200{,}000-12{,}960{,}000+1{,}944{,}000-328{,}050+59{,}049
=103{,}914{,}999.
\]

The numerator corresponding to 203/1000 is 103,936,000; difference 21,001>0. Hence log(49/40)<203/1000.

Integrating the first three nonnegative terms of (1−s²)⁻¹ to 1/3 and retaining the positive remainder gives

\[
\log2>2/3+2/81+2/1215=842/1215>0.
\]

Thus

\[
\log(L/2)+(3/4)\log M
<527/10000+(3/4)(203/1000)=4099/20000.
\]

Finally, (37/125)(842/1215)=31154/151875 and

\[
31154\cdot20000-4099\cdot151875
=623080000-622535625=544375>0.
\]

Since L=2(527/500), division by the positive log 2 gives log₂K<1+37/125=162/125. This is WC2. All strict signs have fixed rational slack; they do not deteriorate with n. No mathematical executable was used for these calculations.

## 6. Transfer to the exact official rate and limits of the conclusion

The published canonical-label deletion/insertion interface is B_{j+1}≤γ_jB_j. With B₂=1 and WC1,

\[
\log_2B_n\le\sum_{j=2}^{n-1}j\log_2K
=\left(\frac{n(n-1)}2-1\right)\log_2K.
\]

The empty sum at n=2 equals zero. A finite later initialization would add a fixed constant, but none is needed once the same n≥2 zone convention is retained. Dividing by n² and using the attributed equality C(n)=B_n yields

\[
\limsup_n n^{-2}\log_2C(n)
\le\tfrac12\log_2K
=\tfrac12\log_2L+\tfrac38\log_2M
<81/125=0.648.
\]

The conclusion is strictly stronger than the recorded older 0.649514 upper bound. It is an upper bound only. The value, a matching lower bound, an effective all-scale upper envelope R and any full annual answer are not established by WC. Older accepted existence results are not premises here. No novelty or setter-identity claim is certified by a targeted search.

## 7. Adversarial checks and whole-review boundary

I specifically challenged: a variable path length; counting all sorting words or insertion histories; using degree-two cells as unique; conflating m with k; inconsistent terminal-tail conventions; losing reconvergent paths; weights depending on eventual statistics; applying Cauchy to different sets; assuming independence; reversing either exponent inequality; excluding negative A−U without reason; an unbounded-degree loophole; extending an integer certificate to reals; incorrect strict log remainders; missing half in the quadratic sum; and the source's finite starting-index qualification. The displayed reconstruction resolves these checks within the stated source interfaces.

The old concavity proof and its acceptance were read completely for exact source/finite-size context. Its computation was not rerun and its continuous relaxation maximum is not a premise of WC. The constructor's heuristic/free-boundary background is not needed and is not being certified. No source-author program, mathematical test suite, sampling, CAS, enumeration or source-download retry was used in this audit. Public primary PDFs were read through bounded web retrievals; their exact reading scopes and un-read foundations are recorded separately. Every substantive inference WC-O01 through WC-O40 has its own ledger row. Only the coordinator may promote after both entire audits and reconciliation.
