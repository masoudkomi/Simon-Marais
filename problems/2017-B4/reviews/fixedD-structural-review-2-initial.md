# Independent whole review 2: fixed-D structural packet

2026-10-17 UTC. Blind initial audit of both frozen notes. The packet remains **candidate proof - unverified** pending coordinator reconciliation. I did not construct it, have not read a peer fixed-D structural report, issues, or conclusions, and make no acceptance decision.

Requested settings: gpt-6.1-sol / max. Independent effective-setting readback is unavailable. Earlier 2021, 2022, and 2024 review bytes remain preserved and their peer findings unread.

Reviewed structural candidate SHA-256: c776e81d0fd44c0e8042ddc00a0d949966cdc106ba9b7e67486dc4d14a1b7d87.

Reviewed profile-reduction note SHA-256: 973e8d7da034082b4416100d51650798ec3eb90e75cfd44106b5810dd9ec7e8d.

Both match the supplied freeze. Exact source and output fingerprints are recorded separately.

## Initial disposition

**One substantive scope correction is required before accepting the whole packet unchanged.** The profile note, Section 4, claims a uniform \(O_D(\epsilon L)\) weak-order padding band from nearby vector-height words and fixed color counts. Prefix-height closeness alone does not imply that claim. Section 2 below gives an exact family with prefix-height error one and a join excursion of order L, even with all three color counts equal.

The structural note's actual envelope theorem assumes bounded displacement of each ranked label; that theorem survives reconstruction. Its separate bounded-gap conversion also survives, but its constant depends on the reference gap bound, not just D. The profile note must explicitly retain one of those hypotheses and the appropriate constant dependence. This does not refute (H) or the expressly unproved EAI program.

The remaining structural lemmas and the compact-profile identity survive my whole reconstruction within their stated scopes. In particular I found no independent obstruction to the rational multigrid construction after checking its degenerate-row cases and completing the local degree argument at edges and vertices. Only the coordinator may accept unaffected statements or request and reconcile an author repair.

## 1. Official target and marked auxiliary counts

The [official 2017 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf), p.2, asks for both normalized liminf and limsup of the fixed-polygon tiling count for integers \(n\ge2\). The [official notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf), p.12, identify A006245 and give \(C(3)=2,C(4)=8\), consistent with the established marked/oriented convention. No rotation/reflection quotient, reduced-word count before commutation, or insertion-history count is substituted.

The fixed-D count \(B_D(p)\) is an auxiliary full-boundary count with p strands in each of D ordered direction classes. It is not asserted equal to the original \(C(Dp)\). Hypothesis (H) is the existence of its normalized limit, not its value. The packet does not claim to prove (H), either requested 2017 constant, or a new frontier bound.

## 2. Substantive issue: prefix-height closeness does not bound the join

The affected passage is profile-reduction Section 4, lines 163--169. As written it moves from nearby vector-height boundary words with fixed color counts to a uniform \(O_D(\epsilon L)\) envelope band and \(O_D(\epsilon L^2)\) padding area. The structural lemma proves this from ranked-label displacement; the following example separates those two notions.

Fix \(D=3\) and any \(M\ge2\). All words below contain exactly M copies of each color, have length \(L=3M\), and preserve the ranks within every color. The single displayed 2 in the first two blocks means the first ranked occurrence \(2_1\); the last block contains \(2_2,\ldots,2_M\).

\[
\begin{aligned}
w_0&=1^M\,2_1\,3^M\,2_2\cdots2_M,\\
w_A&=2_1\,1^M\,3^M\,2_2\cdots2_M,\\
w_B&=1^M\,3^M\,2_1\,2_2\cdots2_M.
\end{aligned}
\tag{CE}
\]

At every prefix position the three color-count coordinates of \(w_A\) differ from those of \(w_0\) by either zero or \((-1,1,0)\). For \(w_B\) the difference is either zero or \((0,-1,1)\). Thus their vector prefix heights are uniformly within one in the maximum norm. In the physical integer model the y-coordinate error is also at most one, since its coefficients are \(0,1,2\). Both paths lie just above the reference path.

The union of their inversion sets contains every inversion \(1_a>2_1\) from \(w_A\), and every \(2_1>3_c\) from \(w_B\), where the inequality here denotes reversed order of initially ordered labels. Transitive closure therefore forces every \(1_a>3_c\). The already present inversions \(2_b>3_c\), \(b\ge2\), are retained. No same-color inversion occurs, and there is no forced inversion between a 1 and \(2_b\), \(b\ge2\). The exact join is

\[
w_A\vee w_B\vee w_0
=3^M\,2_1\,1^M\,2_2\cdots2_M.
\tag{J}
\]

At prefix M its color-count vector is \((0,0,M)\), whereas the reference has \((M,0,0)\). Hence the join height excursion is M and its physical y-excursion is \(2M\). Setting \(\epsilon=1/L\) makes the original word discrepancy \(\epsilon L=1\), while the join discrepancy diverges.

The area discrepancy is also exact. Relative to \(w_0\), each of \(w_A,w_B\) adds M unit-area tiles of type 12 or 23. The join adds all \(M^2\) type-13 inversions, of tile area 2, and M additional inversions of each of types 12 and 23. Its band area above \(w_0\) is

\[
2M^2+2M.
\]

Thus the claimed \(O_D(\epsilon L^2)=O_D(L)\) area estimate fails under prefix-height closeness alone. This is not an artifact of coupling epsilon to L: for any fixed positive epsilon the examples satisfy \(1\le\epsilon L\) at arbitrarily large L, yet the normalized join excursion stays \(1/3\). No uniform D-only constant times epsilon can control it as epsilon tends to zero. No enumeration or numerical experiment is involved.

There is no contradiction to the structural envelope lemma: label \(2_1\) moves M positions in both examples, so its hypothesis has \(r\ge M\), not \(r=1\). Nor is this a counterexample to an interpolation theorem restricted to a uniformly bounded-gap flat reference; the reference here has long gaps. It identifies the hypothesis that the profile note omitted.

Required author repair: state the proved padding consequence with a ranked-label displacement assumption, or add a fixed periodic reference with gap bound G and state the resulting dependence on G. A constant depending only on D is not justified by the given height-to-label conversion as slopes approach a zero-density stratum. General near-flat/corner/stratum recovery remains in the unproved program.

## 3. Integer dictionary and finite-range encoding

For \(v_i=(1,i-1)\), every pair \(i<j\) has determinant \(j-i>0\). The initial sorted boundary path is lower than its reversed path. Swapping adjacent increasing colors replaces a two-edge lower path by the upper boundary of precisely one positive-area parallelogram. Because every edge advances x by one, each swap raises a graph pointwise. The successive added interiors are disjoint, and a full reduced block reversal fills the zonogon.

Independent swaps change only shell order. Conversely, a tiling's de Bruijn arcs cross each tile through the midpoints of opposite edges. The functional \(\ell_i=\det(v_i,\cdot)\) strictly increases along an oriented color-i arc; its two boundary color-i sides are respectively its minimum and maximum level on the zonogon. Therefore no arc closes or returns to the same side. Each color has p proper disjoint arcs.

For colors \(i<j\), the local oriented tangents at every crossing can be \(+v_j,-v_i\), with positive determinant. The endpoints alternate around the disk. An oriented proper arc separates the disk, so the algebraic intersection with the other arc is \(+1\) or \(-1\); with all local signs equal the pair crosses exactly once. This excludes multiple crossings, rather than presuming a simple arrangement.

The resulting marked bundle arrangement determines the crossing order along every ranked strand. Sweeping it gives reduced block-reversal words; two shell orders differ by commuting independent crossings. Vertex heights are counts of crossed color arcs and recover the positions by V, so the arrangement recovers the same geometric tiling. These arguments agree with the attributed zonogon/wiring dictionary and preserve the fixed boundary ranks.

The use of integer origins adds no hidden vertices on primitive edges: an edge has x-displacement one and contains no other integer point. The local model still explicitly imposes nonoverlap and face-to-face incidence; it is not a packing model with extra T-junctions.

For fixed D a tile incident to a unit lattice cell has one of finitely many types and integer origins within a bounded distance. Recording all such incidents has a finite alphabet. Matching the records within a neighborhood wider than a tile diameter, and checking exact cover inside each cell, reconstructs the tiling. Boundary cells have their prescribed cut/outside data. This supplies a genuine finite-range encoding and an upper bound \(B_D(p)\le2^{O_D(p^2)}\). It does not show that any desired boundary can be filled.

## 4. Vector lifts, compact profile space, and minor closure

Lifting a \(v_i\) edge to \(e_i\) is consistent around each tile. Since the tiled disk is simply connected, it defines a continuous piecewise affine lift a with \(Va(x)=x\). The p disjoint color-i arcs put vertex coordinate \(a_i\) between 0 and p. The boundary lift after normalization is independent of the tiling and p.

In a type-ij tile, inverting the matrix with columns \(v_i,v_j\) gives exactly

\[
J_i=\frac{(j-1,-1)}{j-i},\qquad
J_j=\frac{(-(i-1),1)}{j-i},
\]

with all other rows zero. Its sole nonzero ordered minor is \(\Delta_{ij}=1/(j-i)>0\). Gradients have a D-dependent bound. On the fixed convex domain \(Z_1\), the normalized lifts are uniformly Lipschitz and bounded, with common boundary trace. Their uniform closure \(X_D\) is compact.

The determinant identity

\[
\det(\nabla f,\nabla g)=\partial_1(f\partial_2g)-\partial_2(f\partial_1g)
\]

is valid in distributions for Lipschitz functions. Uniform convergence of f, together with weak-star convergence of uniformly bounded derivatives of g, passes its right side to the limit. Positivity therefore passes to each ordered minor; the resulting determinant is a bounded function and is nonnegative almost everywhere. The limit also satisfies \(V\nabla h=I\). No sufficiency assertion for arbitrary K-valued gradient fields is inferred.

For \(J\in K_D\), Cauchy--Binet gives

\[
1=\sum_{i<j}(j-i)\Delta_{ij}.
\]

Every nonnegative minor is bounded. With \(\sum J_k=(1,0)\) and \(\sum(k-1)J_k=(0,1)\), taking determinants against \(J_i\) yields

\[
J_i=\left(\sum_k(k-1)\Delta_{ik},-\sum_k\Delta_{ik}\right).
\]

The antisymmetric convention gives the correct signs, so entries are bounded. The defining constraints are closed, proving compactness of K.

Every ranked pair of different colors crosses once, giving exactly \(p^2\) tiles of each type ij. Multiplying its minor \(1/(j-i)\) by its tile area \(j-i\) gives one per tile, so the integrated minor is \(p^2\), or 1 after normalization. The same identity passes to uniform limits, either by the common boundary formula or a cutoff approaching the boundary with a uniformly bounded error. These are macroscopic constraints, not a free-boundary approximation.

## 5. The two nonconvexity certificates

The six swaps in each displayed reversal word are increasing-color swaps and the two listed word-state sequences are correct. In the first tiling the type-12 tile has prefix 4, hence origin \(v_4\). In the second the type-34 tile has prefix 2, hence origin \(v_2\). In the integer model both centers are \((2,7/2)\), so their interiors overlap on an open set.

The averaged rows there are

\[
(1/2,-1/2),\ (0,1/2),\ (3/2,-1/2),\ (-1,1/2).
\]

The row-1/row-4 minor is \(1/4-1/2=-1/4\). The average violates a necessary condition for \(X_4\) on positive area, although both original profiles have the same prescribed boundary lift. Dilation followed by the forced fine ij grids preserves each original normalized lift, so this is also an obstruction in the closure of fine tilings.

For the regular unit octagon the stated coefficients solve the two tile-interior equations exactly:

\[
\sqrt2-\tfrac34,\quad \tfrac{5\sqrt2}{4}-1,\quad
\tfrac74-\sqrt2,\quad1-\tfrac{\sqrt2}{2}.
\]

All lie strictly between zero and one. Thus the designated point lies in both interiors. The general determinant formula follows from the first dual row of \([v_1,v_2]^{-1}\) and the second dual row of \([v_3,v_4]^{-1}\):

\[
-\frac{\det(v_2,v_3)}{4\det(v_1,v_2)\det(v_3,v_4)}<0.
\]

For these regular directions one may choose a projection positive on all four vectors to realize the same swap shelling. This does not require their original x-components to be positive. Finite tile types still give the derivative bound needed for the closure obstruction. Hence the unit-length example is valid as well. No conclusion against a nonconvex variational principle or (H) follows.

## 6. The labelled weak-order envelope lemma

I reconstruct the actual theorem independently of the incorrect height-only corollary in Section 2.

Initial labels are ordered by color then rank. An inversion set is closed and coclosed on triples of initially increasing labels. For the union U of the family inversion sets, let S be its transitive closure. It is closed. To check coclosure for \((a,c)\in S\), use an increasing U-path from a to c and an intermediate label b. If b is on the path the conclusion follows. Otherwise one U-edge straddles b; coclosure in its original word supplies the prefix edge to b or suffix edge from b, giving \((a,b)\in S\) or \((b,c)\in S\).

A closed/coclosed set specifies a transitive tournament: the two possible directed triangles would violate the two respective conditions. It is therefore a total label order. U-edges strictly increase color, so S has no same-color inversion and every path has at most \(D-1\) edges. S is an inversion set of a valid shuffle and is the least such set containing U. This proves existence and the formula for the join in the shuffle interval.

For a U-edge not already inverted in the reference word, reversal in one family word whose labels each move at most r implies that its reference position gap is at most \(2r\). Edges already inverted in the reference have negative position increments along the path. Thus a newly created inversion in S spans reference distance at most \(R=2(D-1)r\). Old inversions are retained because the reference belongs to the family. Comparisons across reference distances greater than R do not change; a label can gain at most R old successors before it, or lose at most R old predecessors, hence moves at most R.

Reverse the whole word and reverse the ranks inside each color. This antitone involution preserves label-displacement bounds and maps the shuffle interval to itself, so it gives the meet and its same bound. Zero or absent color classes give no exception, and r=0 leaves the reference word.

This theorem is uniform in color multiplicities because the chain length is bounded by D, not by the total number of labels. The counterexample in Section 2 does not meet its small-r hypothesis.

## 7. Correct geometric padding and its precise scope

For bounded label displacement R, each color prefix count differs by at most R. Physical x is the prefix length and physical y is the corresponding weighted sum of color counts, so the paths remain in a band \(O_D(R)\). A weak-order chain between comparable words shells the region between their monotone paths by positive tiles. Padding to a common meet and join therefore costs \(O_D(rL)\) under the labelled hypothesis. For fixed inner boundary the old patch is recovered by restriction. For varying inner words, retaining the boundary words costs at most \(O_D(L)\) bits, since ranks are forced rather than separately permuted.

The structural note's periodic-reference conversion is valid when every active color has a gap bound G. If prefix counts differ by at most r, the kth occurrence lies between the reference \((k-r)\)th and \((k+r)\)th occurrences, with the usual endpoint truncation. A bound \(O_G(r+1)\) on positional displacement follows. Therefore the resulting physical padding constant depends on both D and G. It is not uniform as a color density tends to zero or the reference period develops arbitrarily long gaps.

No statement here closes four sides of an annulus or matches corner offsets. Those are explicitly outside the structural lemma. Adding the missing label/gap hypothesis in the profile note is necessary before its claimed already-proved padding consequence can be accepted.

## 8. Periodic multigrids, including zero and parallel rows

Let rational \(J\in K_D\). Omit zero rows and choose phases avoiding coincident parallel lines and triple intersections. The excluded phase conditions are a countable set of proper affine conditions, so such phases exist. Rank two supplies two nonparallel active row families; their strip widths bound every grid cell, even when other rows vanish or are parallel or antiparallel.

Index a grid cell by the integers k determined by the intervals between \(J_i x-\theta_i\) and consecutive integers. A zero row has a fixed integer coordinate. Crossing a single family changes only its corresponding coordinate by one. At a nonparallel ij crossing, the four cell indices differ by \(e_i,e_j\), so their physical images \(Vk\) form a type-ij parallelogram.

For \(i<j\), an actual crossing has \(\Delta_{ij}>0\), because zero determinant means parallel rows and no crossing. The domain crossing orientation and \(\det(v_i,v_j)>0\) therefore make the map orientation preserving on that dual face. No degenerate face is introduced for a zero minor.

Here is the edge/vertex detail behind the candidate's compressed degree argument. The embedded grid dual is topologically a locally finite plane cellulation. Choose an orientation-preserving parametrization of each quadrilateral face onto its image parallelogram, consistently on edges. Grid-cell representatives are uniformly close to their k-image because \(k-Jx\) is bounded and \(VJ=I\); bounded cell diameters extend this to a uniformly bounded displacement of the whole dual map from the identity. It is therefore proper and homotopic to the identity through proper maps, of degree one.

For a point away from the image edge graph, every preimage is in a face and has positive degree, so there is exactly one. At an edge interior the two incident orientation-preserving face images lie on opposite sides of their shared nonzero edge. At a vertex the oriented image sectors turn through positive angles; their total winding is a positive integer. Thus the map is open locally there as well. A self-identification of edges or vertices would give overlapping open neighborhoods and hence a nearby regular value with at least two face preimages, contradicting degree one. The map is consequently an embedding and its parallelograms tile the plane face to face.

For rational J, a full-rank integer period lattice with \(JP\subset\mathbb Z^D\) exists by clearing denominators. It preserves the phased grid; physical translation is \(VJP=P\). Heights at vertices are \(k=Jx+O_J(1)\), and affine interpolation preserves that estimate. Hence the construction provides the stated periodic flat background, including rational degenerate strata. This is a local plane background, not a fixed-zonogon recovery theorem.

## 9. Rational slope density

For \(M_\eta(i,j)=\eta^{(i-j)^2}\), \(0<\eta<1\), an ordered 2-by-2 minor has diagonal exponent A and off-diagonal exponent B with

\[
B-A=2(j-i)(\ell-k)>0\quad(i<j,\ k<\ell).
\]

Thus \(\eta^A-\eta^B>0\), and \(M_\eta\to I\) as \(\eta\to0\). Cauchy--Binet makes every ordered minor of \(M_\eta J\) strictly positive, because every minor of J is nonnegative and at least one is positive by \(\det(VJ)=1\).

For small \(\eta\), \(A_\eta=VM_\eta J\) is close to I with positive determinant. Right multiplication by \(A_\eta^{-1}\) restores \(VJ_\eta=I\) and preserves the signs of all minors. Rational points are dense in the rational affine space \(VJ=I\), so a further rational approximation preserves strict positivity. This proves density of rational points in K, but neither density within every fixed zero-minor stratum nor a non-affine boundary-preserving approximation theorem.

## 10. Compact-profile identity and the recovery gap

The finite alphabet already gives finite \(L_+\), and the swap construction gives \(B_D(p)\ge1\). For every profile h, neighborhood counts are bounded by \(B_D(p)\), so \(s_+(h)\le L_+\).

If \(h'\) lies sufficiently close to h, \(B_{\epsilon/2}(h')\subset B_\epsilon(h)\). Taking the neighborhood limsup count and then the infimum over epsilon gives upper semicontinuity, including the extended value \(-\infty\).

If every \(s_+(h)<L_+\), choose for each h a radius whose count limsup is below some \(c_h<L_+\). A finite subcover of compact \(X_D\) bounds the total count by a finite sum. Its normalized logarithmic limsup is at most the maximum of those finitely many \(c_h\), strictly below \(L_+\), a contradiction. Thus

\[
L_+=\max_{h\in X_D}s_+(h)
\]

is correct and does not require convexity.

Property PR at one maximizer would imply \(L_-\ge s_+(h^*)=L_+\), so it is sufficient for (H). Neither the identity nor upper semicontinuity establishes PR. Conversely a two-profile abstract model whose optimal configurations alternate profiles at successive scales can have convergent global entropy with no one maximizing profile recovered at every scale; no equivalence is claimed.

The packet's one-profile oscillation example also checks. The derivative of \(x^2(1+\tfrac14\sin\log x)\) is \(x[2+\tfrac14(2\sin\log x+\cos\log x)]>0\), and its integer increments are \(O(p)\). Integer scales approach both extremal sine phases, so the normalized logarithm oscillates between limiting values \(3/4\) and \(5/4\). This is expressly an abstract count example, not a tiling construction.

The fixed-mesh skeleton has \(O_D(p/\delta)\) cells at fixed \(\delta\), hence subquadratic recording cost. Once a sufficiently wide tile collar is fixed, interior choices form independent exact-boundary fibers. Their finite-alphabet counts are bounded by area. These are valid upper/pigeonhole estimates and do not replace their boundaries by other words.

The BBQ source theorem counts restrictions of infinite-shift configurations; it does not impose one lifted polygon frame. Strong irreducibility in its other theorem supplies a filling length not established here. The source distinction is correct.

EAI is an unproved program, not a fully proved equivalence with PR. Uniform scale thresholds, fixed boundary/phase selection, corner rank matching, exact flux, zero-row and parallel-row strata, loss estimates, and transfer back to every sufficiently large p remain obligations. Dilation/subdivision preserves a single profile, but supplies no exponential lower count without the missing insertion/recovery operations. Rational plane slopes do not by themselves regularize a full non-affine boundary profile.

The zero-density-color collar warning is sound: an inner constant lift offset in an absent color can be balanced in the active coordinates to preserve \(Va=x\), yet connecting it to an outer frame with no such ports would force closed color curves. Mere uniform height proximity does not solve that flux obstruction. The counterexample in Section 2 is a separate warning about dropping the ranked-label/gap condition even before attempting an annulus.

## Required disposition

Retain the successful structural arguments and compact-profile lemma as candidates eligible for reconciliation. Repair the unqualified height-based \(O_D(\epsilon L)\) statement in profile Section 4, and re-review that affected consequence. Leave EAI, PR, (H), and the exact 2017 limits unproved. No computation or enumeration substitutes for any of those missing inferences.
