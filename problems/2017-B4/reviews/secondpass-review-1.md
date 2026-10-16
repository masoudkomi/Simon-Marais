# Independent adversarial initial review R1: 2017 B4 second-pass candidates

Initial report completed 2026-10-17 Australia/Brisbane (2026-10-16 UTC). This is a reviewer report, **not a promotion**. All three frozen packets retain their author status **candidate proof - unverified** until the coordinator completes the required independent-review process.

I did not construct these packets. I reconstructed all eight claims below without reading another review, another reviewer's conclusions, or the shared issue/status logs. I read AGENTS.md, the three packets, their manifest/checkpoint, the official 2017 statement and references, the specified author computation sources/outputs, and primary mathematical sources. I changed no candidate or author computation. Requested launch settings were `gpt-6.1-sol` / `max`; launch acceptance is parent-supplied evidence. Effective model/reasoning readback is unavailable. Account-wide weekly telemetry was independently read at 7%, then 8%, used in the same 10080-minute window, reset Unix time 1792745187. No paid API was used.

## Frozen versions and verdicts

| Packet | SHA-256 |
|---|---|
| `notes/secondpass-macmahon-candidate-v1.md` | `83f254ec69a31b5bf57dddd241bd0e29277300b4f1ba78dbf3c2c02191913ffe` |
| `notes/secondpass-boundary-fiber-candidate-v1.md` | `984ecfd11306304dd68310b0b20148577a7e8d43da6761a9bd570f95024cacbc` |
| `notes/secondpass-periodic-grid-candidate-v1.md` | `6e2a25e0bd94d230892c8c8eb31d931c4a09190826f1f210a97fcb207e852bd7` |

| Claim | Initial R1 verdict |
|---|---|
| M1 finite MacMahon inequality and asymptotic sharpness | Argument checks out on reconstruction; no substantive objection found. |
| M2 unequal/adaptive ternary hierarchy obstruction | Checks out within the precisely restricted construction model. |
| M3 conditional all-n unequal recursion | Checks out; the all-n injection hypothesis is essential. |
| F1 fixed-boundary completion fiber | The embedded-graph converse checks out, including dangling ports and empty slots; detailed reconstruction below. Add the direct signotope theorem citation identified below. |
| F2 constraint-component factorization | Checks out conditional on F1 and the established complete signotope correspondence; no independence of arbitrary free bits is inferred. |
| F3 injective boundary-preserving gluing | Checks out under its stated one-arc-per-strand and disjoint-disk hypotheses. |
| G1 fixed-direction entropy limit | Checks out. The proof can use superadditivity and nonnegativity directly, avoiding the imprecise reference to unresolved grid strips. |
| G2 four-bundle lower certificate | **Needs author repair before acceptance as a complete construction proof.** Boundary fourfold crossings are left unresolved by the literal instructions. The finite count, geometry, tails, padding and coefficient otherwise check out. |

The substantive open objection is **R1-G2-01** below. It concerns completion to simple arrangements, not a counterexample to the numerical inequality after an appropriate repair. Nothing here supplies either official exact rate, their equality, or an improved published bound.

## Domain, convention and attribution audit

The official [2017 Paper B, p. 2, B4](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf) asks for the liminf and limsup of `log2 C(n)/n^2` for every integer n >= 2, for unit-side quadrilateral tilings of a regular 2n-gon. The [official preliminary notes, p. 12](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf) identify the intended fixed-polygon count with the standard marked-arrangement sequence. Orientations are distinguished: C(3)=2 and C(4)=8. No quotient by polygon rotations/reflections, reduced-word multiplicity, or arbitrary strand labellings may be introduced. The packets respect this convention. Their formal one-strand value in M3 is explicitly an auxiliary empty-network convention, not a claim about an official regular two-gon.

The main sources checked were:

1. Felsner and Valtr, [*Coding and Counting Arrangements of Pseudolines*](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf), Sections 1 and 4, especially PDF pp. 1-3 and 11-12, equations (11)-(14). The source's objects are simple marked Euclidean arrangements. Section 4's partial arrangements have three specified noncrossing parts and all inter-part pairs crossing; this is the required MacMahon object, not an arbitrary patch with the same numbers of strands and crossings. I inspected the rendered p. 11 product/completion figure as well as text.
2. Cortés Kühnast, Dallant, Felsner and Scheucher, [*An Improved Lower Bound on the Number of Pseudoline Arrangements*, full arXiv v2](https://arxiv.org/pdf/2402.13107), Sections 1, 2, 4 and 5.1 and Appendix A. The full version in the cache is v2, 21 March 2024, 19 pages. Section 1 fixes the marked north-cell and orientation-preserving convention. Section 4 requires private, nonoverlapping bundle disks meeting no other bundle; Section 5.1 uses complete boundary endpoint pairing and legal cut orders. It does not replace that pairing with scalar crossing data. The rendered p. 12 bundle-completion figure agrees with the packet's explicit reversal interpretation.
3. Felsner and Weil, [*Sweeps, Arrangements and Signotopes*](https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf), author manuscript, Theorems 7 and 8, Definition 1, and the proof of Theorem 7, PDF pp. 14-15 and 18-19. This directly supplies the iff characterization by monotonicity on every four-set and the reconstruction of a simple marked arrangement. Reversing packet order or complementing every sign does not change the one-sign-change condition. I inspected rendered pp. 15 and 19 because local `pypdf` text extraction is unreadable for this old embedded font.
4. For the plane-embedding step, I checked the precise connectedness and outer-face conventions against Jeff Erickson's [*Planar Graphs*, sections on rotation systems and planar maps](https://jeffe.web.engr.illinois.edu/teaching/comptop/2023/notes/09-planar-graphs.html). The reconstruction below also explains the regular-neighborhood argument directly; a disconnected abstract crossing graph alone would not suffice.

**R1-F1-01 (citation precision, not a mathematical counterexample):** Felsner-Valtr Section 1 supports the arrangement/tiling/local-sequence dictionary but is not a direct citation for the sufficiency of the four-set signotope axioms. The boundary packet's opening attribution should cite Felsner-Weil Theorem 7 (and optionally Theorem 8) explicitly. The required theorem has now been checked in an original author manuscript; its hypotheses match the fixed left order and simple marked arrangements used here. This source correction should be made by the author/coordinator before promoting F1/F2.

The 2024 paper gives a published lower bound stronger than 0.2721. Consequently both 0.1887218755... and 0.1900060770... are weaker constructions. I made no new best-bound or current-frontier claim. G1 concerns a fixed four-direction family; its entropy limit is not the official growing-direction limit.

## M1: complete reconstruction of the sharp finite inequality

Write `kappa = (3/4) ln 3 - ln 2`. It is positive because 27 > 16, and `kappa < (1/2) ln 2` because 3 < 4. For positive integer a,b,c, telescoping MacMahon's three-dimensional product over its third coordinate gives the double product M in the packet. The source and product normalization agree; for example M(1,1,1)=2, M(2,2,2)=20, and M(3,3,3)=980.

1. For fixed c>0, `f(t)=ln((t+c)/t)` has `f''(t)=1/t^2-1/(t+c)^2>0`. On each unit cell the mean of x+y is i+j-1. Convex Jensen therefore bounds the logarithmic summand **above by the cell integral**, exactly as claimed. The logarithmic singularity is integrable: near zero the diagonal slices have length O(t), and the relevant integral is bounded by a constant times `integral_0^epsilon t |ln t| dt`. The value at the single corner has measure zero. Jensen is strict for every positive cell because x+y is not almost surely constant. Hence the eventual product inequality is actually strict for finite positive a,b,c; the packet only claims <=, which is valid.
2. A double antiderivative of ln t is `F(t)=t^2 ln(t)/2-3t^2/4`. Applying inclusion-exclusion to the two rectangle integrals gives

   `I = F(a+b+c)-F(a+c)-F(b+c)+F(c)-F(a+b)+F(a)+F(b)-F(0)`.

   The `ln N` terms and quadratic terms cancel after scaling by N=a+b+c. This yields exactly the symmetric A(p,q,r) in the packet, with `p+q+r=1`. In particular, the expression is symmetric even though the original double integral singles out c.
3. For `h(x)=x^2 ln x-(1-x)^2 ln(1-x)+2 kappa x^2`, differentiation gives the displayed h'' and its strictly increasing single zero `u=(1+exp(2 kappa))^-1`, with `1/3<u<1/2`. Concavity extends continuously to 0; no derivative at 0 is required. The maximum of `H=sum h` exists on the closed simplex. On an edge it is `2 kappa[p^2+(1-p)^2] <= 2 kappa`. An interior maximum cannot have two coordinates above u, since transferring mass between them gives a positive second derivative. If all are <=u, strict concavity and Jensen give the balanced maximum. If exactly one is >u, averaging the other two increases or preserves H and reduces the problem to J(a).
4. I independently obtain `J''(a)=ln(a^2/(1-a^2))+6 kappa`. It is strictly increasing on (0,1), is negative at 1/3, and tends to positive infinity at 1. Also `J'(1/3)=0` and `J'(1-)=4 kappa>0`; the latter uses the finite one-sided values h'(0+)=1 and h'(1-)=1+4 kappa. Thus J' decreases from zero, then increases through one further zero. J has no interior maximum on [1/3,1]. Its two endpoint values both equal 2 kappa. The only interior simplex equality case is p=q=r=1/3.
5. Combining these steps gives `ln M <= 2 kappa (ab+bc+ca)`. Doubling the logarithm and exponentiating gives exactly `M^2 16^S <= 27^S`, without a missing factor of two or a bit/natural-log conversion error.

The sharpness statement is appropriate. Independently of the source's displayed asymptotic, the normalized balanced logarithmic sums are midpoint Riemann sums for the integrable function `ln((x+y+1)/(x+y))` on the unit square. Away from the corner convergence is ordinary uniform Riemann convergence; the corner contribution is bounded by sums of `k ln(s/k)/s^2` and tends uniformly to zero as its scaled size tends to zero. The limit is `I(1,1,1)=6 kappa`. Since `2S=6s^2`, `log2 M(s,s,s)/(2S)` tends to `kappa/ln 2=c0`. No sharpness statement about all C(n) follows.

I found no substantive defect in M1. The independent finite integer checks below are supporting evidence, not the proof of this unrestricted statement.

## M2: tree/adaptivity and counting scope

At every internal node, M1 gives `log2 M <= c0[n_v^2-a_v^2-b_v^2-c_v^2]`. In the sum over internal nodes every internal child square cancels its own positive square. Singleton leaves leave exactly `n^2-n`. This is an upper bound on the number of parameter assignments even if gluing is noninjective, and therefore on represented outputs.

An adaptive choice of later widths is still encoded by its eventual ordered tree, labelled leaves, and local choices. Taking a union over all those encodings is legitimate. Full ordered ternary trees with n leaves have O(n) vertices and exponentially many shapes; n! labelled-leaf orders add `O(n log n)` bits. This remains lower order than n^2. A finite set of bounded-size leaf blocks contributes only O(n) further bits. Telescoping with such blocks subtracts their squared sizes, whose sum is at least n, so it does not weaken the leading obstruction.

Minor convention: a full ternary tree with singleton leaves has odd n. For even n that particular family is empty unless the stipulated base blocks or another explicit convention are used. The upper bound is still true and no all-n lower construction is asserted by M2. Clarifying this would improve the model's definition, but it is not a counterexample.

This argument does not bound C(n), an arbitrary family of patch interactions, a hierarchy whose base size grows with n, or a method with extra choices not included in the tree model. The packet makes those scope restrictions correctly.

## M3: conditional all-n induction

For a fixed `0<gamma<A/(1-sum p_i^2)`, the normalized induction slack tends to

`A + gamma sum p_i^2 - gamma > 0`.

Thus one common threshold N makes the claimed inequality and `1<=m_i(n)<n` valid for every n>=N. Choose K to cover all 1<=r<N in `b(r)>=gamma r^2-Kr`. Strong induction then gives

`b(n)>=(A-o(1))n^2+gamma sum m_i(n)^2-K sum m_i(n) >= gamma n^2-Kn`.

The final inequality uses K>=0 and `sum m_i<=n` in the correct direction. The denominator is positive because k>=2 and all p_i lie strictly between 0 and 1. Taking the liminf and then gamma upwards proves the displayed conclusion. Taking gamma strictly below the critical coefficient is essential; the proof does not incorrectly claim an O(n) error at the exact critical coefficient. Floors, unused strands and any subsequence of admissible geometric sizes cannot be dismissed without the asserted injection for every sufficiently large n. The packet keeps that hypothesis explicit, so I found no substantive objection.

## F1: reconstruction of the full completion-fiber converse

The topology here is stronger than agreement of abstract crossing graphs. The following reconstruction is why I accept the proposed converse.

**Basic patch data.** Alternation of endpoints determines whether a pair has odd intersection parity in a disk. With at most one transverse crossing, this determines the pair's crossing status exactly. A generic convex chord model exists: parallelism and triple concurrence are finitely many avoidable algebraic degeneracies. Extending its chords gives a complete straight-line arrangement A0. Fixing its entire exterior supplies both crossing data and the marked end order. It is not enough merely to specify X(w).

**Forward map.** Gluing any minimal patch into that fixed exterior gives proper simple global curves and exactly one crossing per pair. There are no triple intersections after smoothing the boundary joins. If a triple has an exterior crossing ij, its comparison with a second crossing on i or j is determined either wholly by the fixed exterior or by the fixed prefix/inside-block/suffix position. One comparison fixes the triangle bit. Thus every nonfree bit is fixed. Local crossing-order differences survive as differences in an identified block of a global strand. They cannot become equal complete sign patterns, because complete triangle bits determine all comparisons of crossings sharing a strand.

The equivalence between local crossing orders and boundary-labelled patch homeomorphism classes also handles disconnected crossing graphs: add the boundary circle and its marked ports. This augmented graph is connected, crossing rotations are determined by oriented pair intersections and the boundary order, and its rotation system determines its embedding. A cache using relabelled/rotated/reflected boundary words therefore reuses equal counts, without quotienting the individual arrangements being counted.

**Relative orders forced by nonfree triples.** Orient the complete realization from left to right with the prescribed marked left order. For a<b<c there are precisely two possible crossing chains: `ab<ac<bc` or its reverse. Therefore one triple bit determines the relative order of any two of these crossings on their common strand. If ij is exterior, the triple ijk is nonfree for every third label k. Consequently every exterior crossing has exactly the A0 comparisons with every other crossing on either participating strand. This proves both the exterior orders and the contiguity of the interior block: no exterior crossing can be inserted between two interior crossings if none was between them in A0.

If a strand has no interior crossings, the A0 slot is an edge between a specified exterior prefix and suffix; cut two nearby points in that edge. If all crossings on a strand are interior, use its two unbounded tails for the cuts. Thus empty or maximal slots cause no exception.

**Connected exterior graph and port face.** Remove the interior segment on every strand, keeping its two cut endpoints as distinct labelled degree-one vertices. Add a sufficiently large outer circle with labelled endpoints in the fixed marked cyclic order. Every retained prefix and every retained suffix reaches this circle along its own strand. The whole retained graph is connected, even when the removed patch has several components or some removed arcs have no crossings.

Its graph isomorphism with the retained graph of A0 preserves: exterior crossing labels; their order on each strand; the two cut-end labels per strand; the cyclic order of endpoints on the large circle; and the rotation at every vertex. At an ij crossing (i<j), the four incident rays have the same directed X rotation in every wiring realization; degree-one vertices have no extra rotational choice. The outside of the large circle is the same designated unbounded face. Hence the connected rotation-system classification applies with the required oriented outer-face information.

In the retained graph of A0, every cut port is incident to the same bounded face U0 containing the former disk interior. The port sequence in its facial walk is precisely w (with the fixed orientation). Rotation systems determine facial walks, including repetitions caused by bridges. Thus the corresponding ports in the new retained graph are all incident to one face U in the same order. This is the missing conclusion that would be unjustified if one kept only the abstract crossing graph.

**Thickening, then a disk.** No removed interior segment can cross a retained edge: a crossing is classified inside or outside simultaneously on both incident strands. Its open segment is connected and its endpoint germs lie in U, so it stays in U. Take a sufficiently thin regular neighborhood of the connected retained graph, disjoint from the removed segments except for short pieces at their port tips. Its complementary component corresponding to U is a closed disk, with one boundary port per trimmed removed endpoint and cyclic word w. This regular-neighborhood step is needed because the unthickened facial boundary can repeat bridge edges and need not be a Jordan curve. An orientation-preserving disk homeomorphism sends it to D and the labelled ports to their prescribed boundary positions. The trimmed removed segments now form a minimal patch of the required type. All local crossing orders survive.

This proves surjectivity; the forward injection proves the equality. It covers: m=1,2; X empty; X complete; noncrossing isolated strands; an empty interior slot between exterior vertices; several disconnected interior components; exterior bridges; and the case of no exterior crossings on some or every strand. For an empty word the natural empty-patch count is 1. No counterexample was found. Making the facial-walk/regular-neighborhood explanation explicit in a later author version would improve auditability, but the candidate already invokes the needed thickening and connected exterior graph.

## F2 and F3

For F2, a four-set constraint contains at most one connected component of the variable-incidence graph by its definition: any two free variables in a common constraint are joined. Fixed bits do not create a coupling between separate components; each fixed bit is a constant, not a variable. All-fixed constraints are satisfied by sigma0. The solution space is exactly the product of the component solution spaces, so its cardinality factors. The empty product case gives 1. The bound `2^|T|`, the triangle-free conclusion, and the eight rather than sixteen assignments on a complete four-strand patch follow. None assumes independent free triples.

For F3, disjoint disks with one connected arc per participating strand are important. Boundary alternation fixes every crossing pair assigned to a disk. Because the initial complete arrangement is simple, that pair cannot also be assigned elsewhere. Replacement preserves a strand's connectivity and creates no missing/repeated pair crossing, tangency or triple crossing. The full marked end order stays fixed. Restricting a global strand's crossing list to the pairs assigned to a chosen disk recovers its local crossing list. Hence distinct tuples of local patch classes cannot give the same marked global class. The empty/no-crossing disks contribute a factor 1. The fixed-polygon tiling correspondence uses the marked convention already checked above. I found no substantive objection to this stated narrow lemma.

## G1: geometry, seams and the finite fixed-direction entropy

The rectangle offsets work exactly. Its corners have noninteger x and y, and y-x and y+x have fractional parts 1/10 and 3/10. No corner tangency occurs. Grid vertices have integer or half-integer coordinates, so none lies on a boundary with x fractional part 1/10 or y fractional part 1/5. The vertical/horizontal strand counts are L,H. Rising constants run from 1-L to H inclusive and falling constants from 1 to L+H inclusive; both counts are L+H. There are LH integer fourfold points and LH half-integer diagonal twofold points. Thus there are `6LH+LH=7LH` pair crossings. Full boundary words, not these scalars, were used for counting.

An integer seam preserves every family phase. A global line crosses a vertical or horizontal seam at most once, and each distinct pair's unique original crossing lies in at most one subrectangle. Boundary-preserving replacements glue to simple arcs with no double crossings. Local crossing orders can be recovered by the assigned crossing-pair sets and their fixed strand slots. This proves both product inequalities. Abutting closed rectangles can be trimmed within crossing-free collars to obtain disjoint support disks; no F3 hypothesis is being discarded.

**R1-G1-01 (wording):** At line 35, leaving remainder strips in the “original grid configuration” literally leaves multicrossings. It suffices to choose one fixed minimal realization of each remainder strip. More cleanly, iterating the two established inequalities gives the block lower bound directly from f>=0, with no assertion that the raw multiple grid is a simple realization. This does not leave a gap in the abstract superadditivity proof.

For any fixed a,b, division by LH and `floor(L/a) floor(H/b)/(LH) -> 1/(ab)` as min(L,H)->infinity gives the claimed block-density lower bound. The limsup is bounded by the defining supremum S4. F(w)<=C(m) uses only the forward completion injection, not F1's converse. For squares m=6L and a published `log2 C(m)=O(m^2)` bound gives a finite square-density limsup. Applying the block lower bound to squares shows that every rectangular block density is at most that same finite constant. This last step correctly handles arbitrarily thin rectangles; the weaker direct bound `O((L+H)^2)/(LH)` alone would not. Consequently S4 is finite and the joint limit exists as stated. It says nothing about existence of the C(n) limit.

## G2: geometry and coefficient, with one necessary construction repair

The stated integer counts are correct. Fourfold points are precisely `|x|+|y|<=t` with integer coordinates, whose count is `2t^2+2t+1=(m^2+1)/2`. In the remaining integer points of [-t,t]^2 exactly one of y-x,y+x is in [-t,t], because the larger absolute value is |x|+|y| and the smaller is ||x|-|y||. There are `2t^2+2t=(m^2-1)/2` such triple points. All diagonal/diagonal intersections lie in the diamond, since their L1 norm is the maximum absolute value of the two line constants. No additional multicrossings occur outside the described regions; the other cross-family intersections are simple.

A tiling of the plane by the translated 3-by-3 rectangles has area 9 per cell. Retain cells wholly inside the diamond. Any lost cell touching the diamond is in a band of bounded width about its boundary, of area O(t), so the number retained is `2t^2/9-O(t)=m^2/18-O(m)`. Shrinking supports by a small fixed crossing-free collar preserves their boundary pairing and makes them disjoint. Selected patch pairs and the triple-point disks have disjoint crossing assignments. Their choice count is therefore the displayed product.

**R1-G2-01 (substantive, author repair required):** At line 73 the instruction “Leave all remaining crossings unchanged” leaves fourfold crossings not covered by retained patches. For every t>=1 the point (0,t) lies on the diamond boundary and is incident to x=0, y=t, y-x=t and y+x=t, all in the finite grid. No patch wholly in the diamond interior contains this boundary point, and it is not one of the triple points outside the diamond. It therefore remains a fourfold crossing. The later private tail insertions act far away and cannot resolve it. Thus the literal construction has not yet produced the simple complete arrangements counted by C(4m).

The required repair is local and appears not to change the exponent: explicitly resolve every remaining multiple crossing by one fixed simple boundary-preserving choice in a disjoint small disk. In particular this includes the omitted fourfold boundary points. Such choices exist (four-strand complete local patches have eight realizations, any one of which may be fixed), and add no multiplicity to be counted. The author must state the repair and check it in the construction; a reviewer should not silently supply it while approving the frozen version. This report does not alter the candidate.

Subject to that repair, the remainder of G2 checks out:

- **Private tails.** One may use far north, east, northeast and northwest tails for the vertical, horizontal, rising and falling bundles respectively. For a center distance much larger than t, a disk of radius O(t) meets all strands of exactly that bundle and no other family; the four disks are disjoint and beyond all finite inter-family crossings. This verifies the primary source's hypotheses. The packet correctly states that inserting a complete child reverses the outgoing bundle connectivity. It is not a boundary-preserving replacement of the old parallel matching. The reconnection is the same for every child, so marked labels are consistent, same-family crossing orders recover each child, and inter-family orders recover the root choices. There is no missing n! factor.
- **All-n padding.** The largest odd m<=n/4 leaves `0<=n-4m<=7`. Realize the constructed marked arrangement as a wiring diagram and append the extra strands by a fixed reversal wiring to its right. Every new/old and new/new pair can then cross once, with no changes among old pairs. Deleting the extra labels recovers the original arrangement. This is an all-n injection for all sufficiently large n, not just for n divisible by eight or four.
- **Recursion coefficient.** Put q=log2 Q(3,3). The local logarithmic toll is `(1/2+q/18)m^2-O(m)`. Since m=n/4+O(1), the coefficient of n^2 is `(1+q/9)/32`. Four child proportions 1/4 give denominator `1-4/16=3/4` in M3, so the final coefficient is exactly `(1+q/9)/24`. The independent integer computation reproduces Q(3,3)=4419734746, giving the numerical value 0.19000607704480008... . It is slightly above c0, consistent with going outside the ternary model, and far below the attributed published bound 0.2721.

The side-4 failed run supplies no number and was not used. No larger-cap rerun is needed for this certificate.

## Independent computation artifacts, exact scope and failures

All reviewer computation sources are in `reviews/secondpass-review-1-*`. None imports an author enumerator or patch counter. The first script was written independently from the primary cut recipe and the stated four-set axioms. For a noncrossing pair of neighbors of a cut strand, it derives the mandatory order by testing the two induced four-port half words, rather than copying the author's predecessor formula. The signotope generator is an independent direct packet-compatibility backtrack. Geometry uses exact rational clipping against all four rectangle sides and separately enumerates line-pair intersections.

Every run used Python 3.12.14 and only the standard library for mathematics. Each driver launched one dedicated child, recorded its PID/argv/script hash/timeout/status, saved incremental stdout, and could terminate only that child. No CAS or global process kill was used. Source-page rendering additionally used bundled Poppler under separate 20-second child timeouts. The exact full argv and start/finish times are in the task job JSON files.

Commands from the repository root used the Python executable

`/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`.

| Task argument to `problems/2017-B4/reviews/secondpass-review-1-check.py` | Child PID | Wall cap | Result |
|---|---:|---:|---|
| `--task algebra --timeout 55` | 29351 | 55 s | Complete, 0.350 s. Exact un-telescoped MacMahon products for all 560 sorted triples with 1<=a<=b<=c<=14 satisfy the strict integer inequality. A denominator-300 simplex grid was numerical evidence only. |
| Initial `--task fibers --timeout 55` | 29350 | 55 s | Failed in 0.079 s at n=4 due to a reviewer-side nongeneric chord model; retained in `*-v1-failed.py`, `*-fibers-v1-failed.log`, and its job JSON. |
| Corrected `--task fibers --timeout 55` | 29468 | 55 s | Complete, 35.112 s. Through n=7, 135135 paired words were generated and 5283 dihedral/relabel canonical representatives were compared exactly; all patch counts equal their computed completion-fiber counts. Signotope totals were 1,1,2,8,62,908,24698. All six listed MacMahon patch tests agreed, including 980 and 490. |
| `--task grid --timeout 55` | 29349 | 55 s | Complete, 4.606 s. Q(1,1)=8, Q(2,2)=10442, Q(3,3)=4419734746. Reproduced all three full boundary words and 7L^2 pair-crossing counts. Also Q(1,2)=Q(2,1)=73, Q(1,3)=Q(3,1)=674, Q(2,3)=Q(3,2)=1613974. |
| `--task finite-grid --timeout 55` | 29352 | 55 s | Complete, 0.135 s. Exact intersections for 0<=t<=12 reproduce every stated t3/t4 value; translated-patch counts at t=3,5,10,20,40,80 support the omission calculation. These finite checks do not prove the O(m) assertion. |

The first source version had SHA-256 `64e59a225cd01a3218778ecf445f579f0d8cd9c0f2598ca2e211bd2769e0d8ac` and is preserved as `secondpass-review-1-check-v1-failed.py`. It used parabola abscissae B^i. Three endpoint pairs with equal index sums have equal products, and their secant lines can concur for every B; trying more bases cannot repair that structural defect. The corrected version uses `B^((i+1)^3)+i`, explicitly checks every triple for concurrence and slopes for distinctness, and aborts rather than accepting a degenerate completion. Every canonical case through seven strands passed at B=2. Its script hash is `273cf84d27a1df14f8777a7b9f7b8366f68bc7f66d374e87bb74f59663d58d82`. This reviewer failure does not affect the author's separately checked generic model.

Canonical representatives reuse equal counts through explicit disk symmetries/relabel transport; individual arrangements are not divided by those symmetries. The exact scope is representative comparisons plus generation of all paired words, not 135135 independently recomputed geometric completions. The author implementation uses the same count-cache distinction. The two four-strand examples in the candidate were reproduced exactly with three crossing pairs and counts 1 and 2.

The author-side integer-cap-24 check and side-4 failure were inspected, but were not rerun or overwritten. The independent M1 grid stops at 14; the unrestricted M1 verdict comes from the analytic proof, not an extrapolation of either integer grid. The independent Q(3,3) reproduction is the finite computation necessary for the stated certificate.

## Source/cache and evidence manifest

The frozen packet hashes and all reviewer artifact hashes are recorded in `secondpass-review-1-manifest.json`; it excludes its own hash to avoid self-reference. Cached papers remain ignored and are not included in the review deliverables for redistribution.

| Local source | SHA-256 |
|---|---|
| `.cache/official/2017-paper_b.pdf` | `69d7cf84128c2464d962136ed613808b6c7a7b07122cfba9c06b5adf775e2a68` |
| `.cache/official/2017-solutions.pdf` | `c272a72239ef4c2ccd54df0702140179e0a9b85f5a9028c87d485841eb1a2c12` |
| `.cache/literature/2017/cited-7f7251133b0c4ebc.pdf` | `9f68329a62318b355cde668eabb9a05073ce755becfdd81dc5a6a15f9db68c26` |
| `.cache/literature/2017/cited-b5bf6499a3fedd25.pdf` | `075dee678bceb7bddf599d1a402d37c56659bb84302765aa4c6a74b8539b0f17` |
| `.cache/literature/2017/secondpass-review-1-felsner-weil.pdf` | `a6995529d08034c0735b3f9b0b9a4f9dae01ac0a5f3864d88728c6d04f85c828` |

The last paper was retrieved from the author URL above with `curl -L --fail --silent --show-error --max-time 25 ... -o .cache/literature/2017/secondpass-review-1-felsner-weil.pdf`. The initial sandbox attempt failed with exit 6, `Could not resolve host: page.math.tu-berlin.de`; the prescribed escalated retry succeeded with exit 0. Its 395712 bytes and 26 pages were checked. No access restriction was bypassed and no charge was incurred. The cache path was verified by `git check-ignore`. Local `pypdf` extraction of its p. 15 returned font-glyph names rather than readable prose; this failure motivated the preserved bounded render script and page-image inspection. Temporary source page images are under `/private/tmp/secondpass-review-1-*.png` and are not added as tracked third-party pages.

Reviewer changes are limited to this review namespace plus that ignored, review-specific paper cache. No commit, push, candidate repair or shared issue-log modification was performed. The proof author should repair R1-G2-01 and the identified source/wording points, then obtain re-review of the affected text. Only the coordinator may decide promotion after the other independent audit and resolution of substantive objections.
