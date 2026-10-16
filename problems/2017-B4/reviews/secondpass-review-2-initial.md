# Independent adversarial review R2: three 2017 B4 second-pass packets

**Initial report; independently completed before cross-review.**

Reviewer: `/root/review_2017_secondpass_r2`. Local review date: 2026-10-17, Australia/Brisbane; work and source checks occurred on 2026-10-16 UTC. I did not construct these candidates. I read no other review report, reviewer conclusion, shared issue file, status file, or research log. A directory listing used to avoid filename collisions showed other reviewers' filenames, but I did not open their contents. No cross-review was received before this initial report was frozen.

Requested settings supplied at launch: `gpt-6.1-sol`, `max`. The coordinator reported that the launch request was accepted. **Verified effective-setting readback: unavailable**; this report does not claim otherwise. Authoritative account telemetry returned 8% total weekly used during the review and 9% at 2026-10-16 15:42:26 UTC near the initial-report freeze; window length 10080 minutes, reset timestamp `1792745187` unchanged. No separately billed API was used.

I read the applicable root `AGENTS.md`. My tracked writes are confined to the `problems/2017-B4/reviews/secondpass-review-2*` namespace. Public source PDFs and rendered source pages are in ignored `.cache/`. I have not promoted any claim, modified a candidate or shared issue log, committed, or pushed.

## 1. Frozen inputs and scope

The actual SHA-256 values matched the coordinator's requested versions:

| Packet | SHA-256 |
|---|---|
| `notes/secondpass-macmahon-candidate-v1.md` | `83f254ec69a31b5bf57dddd241bd0e29277300b4f1ba78dbf3c2c02191913ffe` |
| `notes/secondpass-boundary-fiber-candidate-v1.md` | `984ecfd11306304dd68310b0b20148577a7e8d43da6761a9bd570f95024cacbc` |
| `notes/secondpass-periodic-grid-candidate-v1.md` | `6e2a25e0bd94d230892c8c8eb31d931c4a09190826f1f210a97fcb207e852bd7` |

Paths in this report are relative to `problems/2017-B4/` unless otherwise indicated.

I checked B4 in the [official 2017 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf), p. 2, and [official preliminary notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf), p. 12. The official domain is every integer n >= 2; C(n) counts tilings of the fixed regular unit-side 2n-gon by unit-side quadrilaterals. The target is both the liminf and limsup of log2 C(n)/n^2. The notes identify the intended convention through A006245, C(3)=2 and C(4)=8. Reflection, rotation, and arbitrary line-label quotients must not be introduced. The formal value C(1)=1 in recursions is consistent with the notes but extends the official domain only as a base convention.

All three packets correctly state that they are partial investigations. None determines either official rate or proves their equality. The attributed published 0.2721 lower bound is stronger than G2. I checked the cited 2024 primary theorem and conventions; I did not independently re-prove that published computer-assisted bound. No claim here is a current best bound or an established novelty claim.

## 2. Verdicts

These are one reviewer's mathematical findings, **not coordinator promotion**.

| Claim | Initial R2 verdict |
|---|---|
| M1: finite MacMahon inequality, sharp constant | Survives full reconstruction. Jensen, calculus, endpoints, conversion of constants, and asymptotic sharpness check out. |
| M2: arbitrary adaptive ternary hierarchy obstruction | Survives within its explicitly defined construction model, including the union over labelled trees and fixed bounded base blocks. No upper bound on all C(n) follows. |
| M3: conditional floor-robust recursion | Survives, provided the displayed injection holds for every sufficiently large integer n, with integer child sizes. |
| F1: full completion-fiber equality | Survives a full topological reconstruction, including empty slots, degree-one ports, disconnected patches, and an exterior graph with bridges. A more explicit regular-neighborhood paragraph is recommended below. |
| F2: constraint-component factorization | Survives conditional on F1 and the rank-three signotope theorem. A precise primary citation is supplied below. |
| F3: independent boundary-preserving gluing | Survives with the proper-arc boundary convention used to define w. Make that convention explicit in the hypotheses. |
| G1: fixed four-direction patch entropy limit | Survives. Nonnegative superadditivity proves the remainder-strip step without leaving any unresolved grid multicrossings. Correct the misleading wording identified below. |
| G2: weaker global lower certificate | **Request repair of frozen v1 before approval.** The omitted boundary strip retains fourfold crossings, while v1 instructs that all remaining crossings are unchanged. An explicit fixed resolution at every uncovered multicrossing is needed. The other geometry, count, injection, padding, and coefficient steps survive reconstruction. |

The main issue is a repairable construction omission, not an observed counterexample to the numerical inequality in G2. My independent finite count is Q(3,3)=4419734746. No L=4 value is used.

## 3. M1 reconstructed from the exact product

Put kappa = (3/4) ln 3 - ln 2 and c0=kappa/ln 2. The telescoped product is correct: telescoping the third index in MacMahon's product gives exactly

\[
M(a,b,c)=\prod_{i=1}^{a}\prod_{j=1}^{b}
\frac{i+j+c-1}{i+j-1}.
\]

The product and its three-bundle interpretation are attributed in [Felsner--Valtr, Section 4, equations (11)--(14)](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf), printed p. 11. The new inequality in the packet is not being inferred from an enumeration table.

### 3.1 Jensen's direction and the singular corner

For f(t)=ln(1+c/t), f''(t)=1/t^2-1/(t+c)^2>0. On the indicated unit cell the mean of x+y is i+j-1. Therefore f at that mean is **at most** the cell integral. The direction in the candidate is correct.

At the single corner x=y=0 the argument of f vanishes. This does not invalidate Jensen: the random variable is positive almost everywhere, its mean is positive, and E|f(x+y)| is finite. Near zero, f is bounded by a constant plus -ln(x+y), whose integral over a square is finite. Jensen may also be applied after restricting away from that corner and taking a limit. Because c>0 and x+y is not almost surely constant on any cell, this comparison is strictly unequal for each finite positive a,b,c. The claimed weak inequality remains valid.

### 3.2 Integral identity

Let N=a+b+c, and F(t)=t^2 ln(t)/2-3t^2/4, with F(0)=0. Direct integration gives

\[
I=F(N)+F(a)+F(b)+F(c)
-F(a+b)-F(a+c)-F(b+c).
\]

This formula is symmetric even though the original double integral is not visibly symmetric. The coefficients of ln N and of the quadratic polynomial cancel because N^2+a^2+b^2+c^2 equals the sum of the three pair-sum squares. Dividing by N^2 gives exactly the packet's A(p,q,r). There is no missing factor of two or missing endpoint term.

### 3.3 Global maximum, not just a stationary-point test

Set g(x)=x^2 ln x-(1-x)^2 ln(1-x) and h(x)=g(x)+2 kappa x^2. I independently differentiated:

\[
g'(x)=1+2x\ln x+2(1-x)\ln(1-x),\qquad
h''(x)=2\ln\frac{x}{1-x}+4\kappa.
\]

Thus h'' is strictly increasing, with its unique zero u=1/(1+exp(2 kappa)) in (1/3,1/2). h extends continuously to both endpoints. For H=sum h over the closed simplex:

1. On the boundary r=0, g(p)+g(1-p)=0, so H=2 kappa(p^2+(1-p)^2)<=2 kappa. Equality here is confined to vertices.
2. At an interior maximum, two coordinates larger than u are impossible: varying just those coordinates with fixed sum gives a positive second directional derivative. The same argument excludes one coordinate larger than u together with another equal to u.
3. If every coordinate is <=u, concavity on [0,u] gives H<=3h(1/3)=2 kappa, with equality only when all three are equal.
4. Otherwise there is one larger coordinate a and two smaller ones. Concavity permits averaging the two smaller coordinates. It remains to bound J(a)=h(a)+2h((1-a)/2), and it is harmless to bound it on the larger interval [1/3,1].

The displayed second derivative of J is also correct:

\[
J''(a)=\ln\frac{a^2}{1-a^2}+6\kappa.
\]

It increases strictly from a negative value at a=1/3 to positive infinity. J'(1/3)=0, and the one-sided limit J'(1)=4 kappa>0; the latter follows from h'(1)=1+4 kappa and h'(0)=1. Hence J' decreases below zero and then increases, with exactly one subsequent zero. J has no interior maximum on (1/3,1); its endpoint values are both 2 kappa. This justifies the global simplex maximum and the asserted unique interior equality point. The proof does not silently assume that a symmetric extremum must be balanced.

Consequently I<=kappa(N^2-a^2-b^2-c^2)=2 kappa(ab+bc+ca). From ln M<=I,

\[
M^2\le \exp(4\kappa S)=(27/16)^S,
\]

which is precisely M1. The logarithm-base conversion is correct.

For sharpness, one can make the cited balanced asymptotic precise by dividing ln M(k,k,k) by k^2. The sum becomes a midpoint Riemann sum of ln(1+1/(x+y)) on [0,1]^2. Away from x+y=0 convergence is ordinary uniform-continuity convergence. The small triangular corner is uniformly negligible: grouping terms by i+j-1 bounds its normalized contribution by a constant times delta^2(1+|ln delta|), after taking k large. The limit is I(1,1,1)=6 kappa. Since 2S=6k^2, ln M/(2S) tends to kappa, and the bit-valued ratio tends to c0. Finite strictness and asymptotic sharpness are compatible.

My independent exact integer/rational test checked all 364 triples 1<=a<=b<=c<=12, with strict inequality every time. This is supporting finite evidence; the preceding analytic reconstruction is the unrestricted argument.

## 4. M2 and M3 reconstructed

### 4.1 M2, including adaptive choices

At each internal node v, M1 gives

\[
\log_2 M(a_v,b_v,c_v)
\le c_0(n_v^2-a_v^2-b_v^2-c_v^2).
\]

For a tree with singleton leaves, every nonroot internal-node square cancels its occurrence as a child square. The remaining value is c0(n^2-n). This counts possibilities, so injectivity is unnecessary for the upper obstruction. If gluing identifies two parameter choices, it can only reduce the output count.

A full ternary tree has O(n) vertices and exponentially many ordered shapes for n leaves; n! bounds leaf labellings. If sizes or subsequent decisions depend on earlier local choices, every completed construction still has a labelled tree in this union. The upper bound on each product is uniform over that tree. Hence taking all such choices adds only O(n log n) to the logarithm. A full ternary singleton tree only exists at the appropriate odd leaf counts; this is a harmless restriction of the model, not an all-n lower construction. Allowing a fixed set of base blocks of bounded size changes the telescoping endpoint to the sum of squared leaf-block sizes and adds O(n) bits of block choices. The leading upper coefficient is still c0.

I found no hidden global C(n) estimate here. Arbitrary four-bundle patches and nonhierarchical interactions are outside the defined family, so the stronger published global lower bounds are consistent with M2.

### 4.2 M3, all-n induction and floors

Fix 0<gamma<A/(1-sum p_i^2). Since m_i(n)/n tends to p_i, the leading coefficient of

\[
(A-o(1))n^2+\gamma\sum_i m_i(n)^2-\gamma n^2
\]

is strictly positive. For all n above one fixed threshold, the quantity is nonnegative, every child size is a positive integer below n, and the assumed recurrence applies. Choose K to handle the finite set of smaller positive integers. The induction then yields

\[
b(n)\ge\gamma n^2-K\sum_i m_i(n)\ge\gamma n^2-Kn.
\]

The sign of the last inequality is correct because K>=0 and the sum of child sizes is <=n. Dividing by n^2 and allowing gamma to increase proves the stated liminf. A subsequence-only injection would not justify this induction; the candidate explicitly requires every sufficiently large n. Child positivity below the threshold is not an additional hidden hypothesis, because that threshold may be enlarged using p_i>0.

The lemma supplies neither the geometric injection nor limit existence, as the packet correctly states. With the three-bundle toll A(p,q,r)/ln 2, M1's continuum inequality gives the same c0 obstruction after division by 1-sum p_i^2.

## 5. F1: full reconstruction of the converse

### 5.1 Boundary data and complete signs

The objects must retain labelled boundary ports in their oriented cyclic order. A proper simple arc separates the disk; a second proper arc has odd intersection parity with it exactly when the endpoints alternate. With transverse intersections and at most one crossing per pair, this determines the crossing set X(w). This covers adjacent equal labels and crossing-free arcs as well as connected crossing graphs.

A generic placement of the 2m distinct endpoints on a strictly convex curve gives straight chords with the same alternation set. Parallelism of two extensions and concurrency of three extensions can be avoided by generic choices without changing their cyclic endpoint order. Thus the fixed exterior A0 exists. Its full-line completion has a fixed marked left order; translating original boundary labels to that order must be done once, as the candidate specifies.

The needed complete-sign theorem is stated precisely in [Felsner--Weil, *Sweeps, Arrangements and Signotopes*, Theorems 7 and 8](https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf), printed pp. 15 and 19. Rank-three triangle signs are characterized by the one-change condition on each ordered four-packet; the correspondence is with **simple marked** arrangements, not arbitrary projective/unmarked arrangements. A triple determines all three comparisons of the other two labels in the local sequences on its three strands. Reversing the packet order or complementing every sign changes conventions but not this theorem. Felsner--Valtr Section 1 supports the local-sequence/marked-arrangement/tiling dictionary, but does not by itself state this exact four-packet theorem. Add the precise Felsner--Weil citation to the author packet.

### 5.2 Forward map

Gluing any minimal patch to the fixed exterior produces exactly one crossing per global pair. For an alternating pair its crossing is inside, and for a nonalternating pair its exterior crossing is unchanged. There are no seam crossings because the ports are distinct and their collars can be matched. The resulting proper curves remain simple.

For a nonfree triple, choose an outside pair crossing. If all three pair crossings are outside, the triple is unchanged. If another crossing is inside, compare it to the chosen outside crossing on their common strand. The inside crossing lies in the designated disk slot, while the outside crossing is on its fixed prefix or suffix. Thus their order, and hence the entire triple sign, is fixed. The candidate's argument is valid even when exactly one rather than two of the triple's other crossings is inside.

Patch crossing orders are recovered from the inside subword of each global local sequence. Since boundary pairings and labels are retained, this is an injection. No rotational/reflection quotient enters.

### 5.3 Outside/inside comparisons and empty slots

Start from a complete marked sign pattern agreeing with sigma0 outside T(w), and choose a piecewise-linear wiring realization A. For every outside pair ij and every other crossing ik on strand i, the sign of ijk is frozen and fixes the relative local order. Therefore the outside crossings and their comparisons to all inside crossings are those in A0.

If strand i has at least one inside crossing, all its inside crossings consequently form one contiguous block between the same outside prefix and suffix as in A0. If it has no inside crossings, comparison data alone cannot locate an empty block, but the construction may **choose** the same gap in the matching outside local sequence as A0. Put two distinct cut points in that edge. This is a choice of location for a crossing-free segment, not a new constraint on sigma. It handles isolated vertices of X(w).

For every strand cut off exactly this one inside segment. The removed segment may have no crossings. All its pair crossings, if any, are designated inside simultaneously on both strands, so a removed piece never crosses a retained outside piece.

### 5.4 The embedded outside graph, including bridges and degree-one ports

Trim at a large outer circle, include that circle in the graph, and retain the two labelled port vertices on every cut strand. Every point of a retained strand piece has a path along that piece to the outer circle. Thus the resulting finite graph G is connected even when the patch crossing graph is disconnected or empty.

The graph isomorphism to the corresponding G0 from A0 retains:

- all outside crossings and all labelled port vertices;
- their order along each oriented strand, including the two cuts in an empty slot;
- the cyclic rotation at a crossing, fixed by the oriented labelled wiring convention;
- the order and rotations of the outer-circle vertices and the designated outer face.

These are stronger data than the abstract crossing graph. A connected finite graph with its oriented rotation system specifies its spherical embedding up to an orientation-preserving homeomorphism; choosing the outer face specifies the plane embedding. This does not require two-connectivity, so bridges and dangling port edges are permitted. One can prove it by replacing vertices with small disks, edges with ribbons in the prescribed cyclic order, and filling the complementary face disks. The outer circle fixes the planar outer face. The standard rotation-system facts are also explained in [Jeff Erickson's planar-graphs notes, “Rotation systems” and “Formalities and Trivialities”](https://jeffe.web.engr.illinois.edu/teaching/comptop/2023/notes/09-planar-graphs.html).

In G0, every port is incident to the face containing the original disk D. Following that face's boundary walk records the ports in order w. The walk may repeat a bridge or a cut vertex, but each degree-one port has one incident face corner. The graph isomorphism transfers the same face and the same cyclic list of port corners to G. This is how one establishes the designated-face assertion; it should not be assumed merely from equal crossing sets.

### 5.5 Turning the designated face into an actual disk

A face with dangling edges need not have a simple closed boundary. Therefore a bare appeal to a homeomorphism of its closed face is imprecise. The candidate's thickening can be made rigorous as follows.

Take a sufficiently thin regular neighborhood of the connected outside graph. Around each port, use a small collar and truncate only an initial crossing-free portion of the removed inside arc. The complement corresponding to the designated **bounded** face now has a Jordan boundary and is a closed disk. Its boundary ports, obtained from those collars, retain the face-corner order w.

Every removed arc lies in that same face: it cannot cross G, and its interior approaches that face at either endpoint. Each connected component of the removed crossing network has boundary ports, since it is built from proper cut-strand arcs. There is no component floating in a different face. The neighborhood can be chosen thin enough that all removed arcs, except their tiny endpoint collars, remain in this complementary disk. Piecewise-linearity and finiteness make the separation choice immediate. This works for mutually disconnected arcs, a disconnected crossing network, and every empty slot.

An orientation-preserving disk homeomorphism maps this disk and its ordered ports to D and its prescribed ports. The removed arcs become a minimal patch. Their local crossing orders are those in A's inside blocks. When this patch is glued back into A0's exterior, all complete local sequences are exactly those of A, so the full sign pattern is the chosen sigma. This proves surjectivity.

I found no topological counterexample after this reconstruction. The candidate already points to thickening; I recommend replacing its last two sentences with an explicit version of this argument. This is an exposition precision request, not a remaining mathematical obstruction in my review.

## 6. F2 and F3

### 6.1 Constraint factorization

Once F1 and the rank-three theorem are used, the only variable bits are the triples in T(w). A four-set constraint with more than one free variable makes all those variables adjacent by the defined component graph. Thus it uses variables from exactly one component, or none. All-zero-variable constraints hold because sigma0 is a complete arrangement. Counting valid assignments component by component therefore gives the product of the Z_j, with no omitted coupling.

The cases of an isolated free variable and no free variables are sound: the former is its own component, and the latter has the empty product 1. The crude bound 2^|T(w)| follows immediately. Triangle-free X(w) gives F=1. For the complete four-strand patch, the eight monotone four-bit words give 8, not 16. These are the correct marked counts.

### 6.2 Independent gluing

For each disk, endpoint alternation identifies exactly which global pair crossings it owns. In the original simple complete arrangement those pair sets are disjoint across disks and from the exterior. Replacement preserves each pair's crossing status. It cannot create a global self-intersection, because each affected strand is one proper arc in a disk and the disks are disjoint. It cannot create a second pair crossing, because a pair's inside status in each disk is fixed.

The input arrangements are recoverable: restrict a labelled global local sequence to the pair labels assigned to the disk. A changed local crossing order is visible there regardless of how other disjoint slots appear. The canonical left labelling in a marked arrangement rules out losing injectivity through a permutation of equivalent-looking disks or bundles. Thus the product injection, and then the fixed-zonogon dictionary, give F3.

Precision request: explicitly require each intersecting strand to meet a disk in a **proper** arc with two distinct transverse boundary ports, and exclude boundary segments/tangencies. The word w_j and the earlier F definition already require this interpretation, but “one connected arc” alone could be read to allow a tangency at an interior point. All rectangles and generic small disks used in G1/G2 can meet the stronger convention. The empty-disk case has factor 1 if F(empty)=1 is adopted; alternatively exclude it.

## 7. G1: exact geometry and entropy limit

The offsets are effective. On a boundary x=integer+1/10 or y=integer+1/5 there is no original integer or half-integer grid crossing; at a corner, x+y and y-x have noninteger fractional parts, so no diagonal passes through the corner. Vertical and horizontal lines also avoid corner tangency.

For an L by H rectangle, the vertical and horizontal counts are L and H. The rising constants run from -L+1 to H, and the falling constants from 1 to L+H. Hence there are exactly 3(L+H) strands. The LH integer points are fourfold, contributing 6LH pair crossings. The LH points with both coordinates half-integral are diagonal-only crossings, contributing LH more. These exhaust all pair intersections. Thus 7LH is correct; it is not substituted for the full word.

After an integer translation, the four line families and the fractional offsets have the same phase. A vertical seam x=L1+1/10 crosses no grid vertex; horizontal seams have the analogous property. Glue two minimal subrectangle patches using the fixed seam endpoint identifications. For each global pair, at most one of the subrectangles can demand its crossing, because these are the crossing statuses inherited from its unique original straight intersection. Thus the joined arcs stay minimal. A change in a local crossing order is recoverable by restricting to the known subrectangle crossing set. This proves both separate superadditivities. To invoke the literal disjoint-closed-disk version of F3, shrink the adjacent patches slightly into a crossing-free corridor; the boundary word is unchanged.

For any fixed positive a,b, repeated superadditivity and f>=0 give

\[
f(L,H)\ge \lfloor L/a\rfloor\lfloor H/b\rfloor f(a,b).
\]

When a remainder width or height is zero, simply omit that term. When it is positive, choose any one **minimal** fixed patch in that strip. This is enough for the lower bound. The phrase “leave its remaining strips in their original grid configuration” should be changed: that original grid can have multicrossings. The algebraic proof already supplies the correct replacement via f>=0, so G1 does not depend on an invalid remainder configuration.

Dividing by LH and taking min(L,H) to infinity proves the lower bound by every block ratio. The limsup is bounded by their supremum by definition. Finiteness needs a separate argument because an unrestricted two-dimensional superadditive function can have infinite supremum.

The forward completion injection F(w)<=C(m) is valid independently of F1's converse. For squares m=6L, so the published quadratic arrangement upper bound gives f(L,L)=O(L^2). For each fixed a,b, the block argument applied to arbitrarily large squares bounds f(a,b)/(ab) by that same finite square limsup. Taking the supremum proves S4 finite. This establishes the joint limit claimed in G1 for arbitrary aspect ratios with both dimensions tending to infinity.

This proof neither increases the number of grid directions nor establishes any superadditivity for the official C(n). No official entropy-limit assertion follows.

## 8. G2: what works and what must be repaired

### 8.1 Lattice counts and patch density

With m=2t+1, all four families are present at an integer point (x,y) of the axis square precisely when both |y-x| and |y+x| are <=t, equivalently |x|+|y|<=t. The number of such points is

\[
1+\sum_{s=1}^{t}4s=2t^2+2t+1.
\]

Of the (2t+1)^2 integer points of the square, the remaining 2t^2+2t have exactly one diagonal family: their smaller diagonal absolute coordinate is ||x|-|y||<=t and their larger one exceeds t. Thus each is triple. A triple involving both diagonals and a vertical or horizontal strand must lie inside the same central diamond, so no extra triple region was silently omitted outside the axis square. Other intersections outside it are simple.

The diamond area is 2t^2=m^2/2-O(m), and its boundary length is O(m). Use the translated tiling with rectangles

\[
[3i+1/10,3i+31/10]\times[3j+1/5,3j+16/5].
\]

Retain the rectangles whose closures lie in the diamond's interior. They have exactly the Q(3,3) boundary type, since all four finite bundles contain every line passing through such a rectangle. The discarded area is confined to a bounded-width strip around the diamond boundary, hence O(m); the patch count is m^2/18-O(m). A thin crossing-free corridor can separate neighboring closed rectangles without changing the word or the density. The triple-point disks outside the diamond are disjoint from these retained patches and from one another after shrinking.

### 8.2 Blocking issue R2-G2-1: unresolved fourfold points

Frozen v1 then says “Leave all remaining crossings unchanged.” There are still fourfold integer crossings in the omitted boundary strip. In particular, if retained rectangles have closures inside the central diamond, its boundary fourfold point (t,0) is outside every retained rectangle. It is not one of the t3 triple points. Leaving it unchanged retains a fourfold crossing. Tail completions do not alter that mixed-bundle crossing. The resulting object is not simple and cannot yet be counted by C(4m).

**Required repair by the author:** after the counted reroutings, resolve every uncovered multicrossing by one fixed simple local resolution, in pairwise disjoint small disks avoiding all selected patches. There are only O(m) uncovered fourfold points for this tiling, and selecting a fixed resolution costs no counted choices. Resolve any boundary-corridor multicrossings in the same way. State that only the remaining simple crossings are left unchanged. This gives simple partial arrangements with the prescribed parallel bundles, exactly the input required by the cited completion theorem. It leaves the displayed exponent and asymptotic coefficient unchanged.

This is a construction repair request. I have not edited the packet and do not approve G2's frozen v1 as a complete proof. A targeted re-review must check the author's actual revised placement/resolution text.

### 8.3 Tail completion: hypotheses checked

Subject to that repair, every modification is in a bounded central region, and the far tails remain straight parallel bundles. For a bundle choose one of its two ray directions and place a disk far along its central ray, with radius a fixed sufficiently large multiple of m. The bundle's width is O(m), while distance from that center to every other-family line grows linearly in the distance along the ray. Because the four directions are separated by positive angles, sufficiently distant disks meet all m lines of their own bundle, no line of another bundle, and none of the other tail disks.

These are precisely the geometric hypotheses in [Cortés Kühnast--Dallant--Felsner--Scheucher, Section 4, printed p. 12](https://arxiv.org/abs/2402.13107). Its input is a **simple partial** arrangement, which explains why the preceding unresolved crossings matter.

The packet's correction about connectivity is essential and valid: an m-line complete child cannot replace m parallel arcs while retaining the old pairwise endpoint pairing. Instead attach the child with reversal connectivity and assign the outgoing tails by that fixed reversal. This reconnection is the same for every child. One can choose a generic global direction to define left order; the resulting left labelling is then fixed across all choices, including any bundle whose selected physical tail points left in the original picture.

Every formerly parallel pair crosses once in its child; every cross-family pair retains its existing crossing. Restriction to within-bundle crossings recovers the children, and deletion of those crossings from the global local sequences recovers the partial arrangement. Thus the C(m)^4 factor is injective. This is a distinct completion operation, not an instance of F3 with the original parallel boundary word.

### 8.4 Padding and coefficient

For every sufficiently large n, the largest odd m<=n/4 leaves 0<=n-4m<=7 and satisfies m/n->1/4. Padding has an explicit wiring realization: after the old 4m-strand reversal, move each newly added largest strand through the preceding strands in a fixed order to complete the n-strand reversal. Each pair involving a new strand crosses once, and deletion of the new strands recovers the old local sequences. Thus this is an injection for every such n, not merely a subsequence estimate.

Write q=log2 Q(3,3). The counted partial exponent is (1/2+q/18)m^2-O(m). Substituting m=n/4+O(1) gives

\[
b(n)\ge\frac{1+q/9}{32}n^2-O(n)+4b(m).
\]

The child square ratio is 4(1/4)^2=1/4, so M3 divides the toll by 3/4. The coefficient is exactly (1+q/9)/24, numerically 0.19000607704480008 with the independently reproduced Q. The rounding, factors of four, and logarithm base all check out. This remains far below the attributed published 0.2721 bound. It is an escape from the narrowly defined M2 model, not a new frontier bound or an official limit computation.

## 9. Computation audit and preserved execution records

The original `secondpass-patchcount.py`, `secondpass-fourbundle.py`, and `secondpass-macmahon-bound.py` were read, as were their specified outputs and job metadata. I did not rerun them in place or overwrite their files. Their cut recurrence agrees with the attributed primary recipe in Section 5.1 of the 2024 paper.

The recurrence itself has a direct decomposition proof. Cut along one distinguished arc z. A strand crossing z has one port on each side and a position in the order along z. A noncrossing pair of such strands forces its order; the reverse choice would make that pair cross in both subdisks. For a crossing pair, either order assigns its crossing to exactly one subdisk. A strand not crossing z has both endpoints on its forced side. Thus admissible cut orders and the two minimal subpatches glue bijectively to minimal whole patches. Choosing z deterministically from the boundary word avoids counting an arrangement through several cuts. Each child has fewer strands, so the recursion terminates. Relabelling, cyclic shifts, and reflection give bijections between the corresponding counting problems; using them as cache keys does **not** quotient individual objects by those symmetries.

My independently written `reviews/secondpass-review-2-check.py` imports no author or first-pass module. It uses exact Fraction clipping with a perimeter coordinate, a separate cut-counter implementation, and actual reduced adjacent-swap wiring enumeration for complete patterns. Triple signs in those wirings are read from the middle strand's partner order. Exact generic straight completions use deterministic seeded sampling of integer parabola coordinates, rejecting parallelism or triple concurrency by exact arithmetic; no floating-point test certifies genericity.

Preserved command:

```text
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -u problems/2017-B4/reviews/secondpass-review-2-check.py
```

The driver created only its dedicated child, PID **30993**, with a 60-second explicit subprocess cap and a 100000-state cap. Incremental output was flushed after each completed phase. It finished successfully in 6.331 seconds, exit 0, without timeout or cap failure. Metadata is `secondpass-review-2-check-job.json`; stdout is `secondpass-review-2-check-output.txt`.

Results:

- Every rectangle L,H=1,...,5 had exactly 3(L+H) strands and 7LH alternating pairs under independent exact clipping.
- The square counts were 8, 10442, and **4419734746**, with 17436 total cached states after the third count. The exact boundary words and line equations are in stdout.
- For n=1,...,6, actual wiring class counts were 1, 1, 2, 8, 62, 908. Completion fibers equalled cut counts for all 1, 2, 5, 17, 79, 554 canonical boundary-word types, respectively. The canonical types reuse equal counts under cyclic shift, reflection, and relabelling. This checks one independent generic completion per type, not all possible exterior completions. No seven-strand result is newly claimed by this R2 run.
- Finite bundle lattice formulas were checked for t=1,...,30.
- All 364 sorted positive MacMahon triples with largest coordinate <=12 passed exact strict integer comparison.

The author's L=4 grid run is honestly incomplete: its preserved traceback reports the 50000 memo-state cap, and its job status is `failed`. Its completed L=1,2,3 checkpoints are distinct from that unfinished attempt. I made no L=4 attempt and use no alleged L=4 count. The author's n<=7 fiber comparison remains finite evidence; the unrestricted F1 verdict rests on the topology above.

Source-page rendering was also isolated: `secondpass-review-2-render.py` launches a child with a 20-second cap. Final render child PID **32828** completed in 0.351 seconds. Rendered Felsner--Valtr p. 11, the 2024 paper p. 12, and Felsner--Weil pp. 15 and 19 were visually inspected. An earlier successful render, PID 32383, wrote page images into my review namespace; those images were moved to ignored `.cache/` and the renderer was corrected to write there. The initial metadata/stdout were preserved separately. No source-page images remain to be committed with the report.

No mathematical test failed in my independent run. Failed source operations were preserved in the source manifest: `pdftotext` was absent from PATH; initial curl returned DNS error 6; the authorized public download succeeded after the required escalated retry. `pypdf` extracted unusable font-code strings from the Felsner--Weil PDF; raw extraction is cached for reproducibility, and the theorem statement/proof were instead checked on rendered pages. These are source-inspection failures, not evidence for or against the mathematical claims.

## 10. Issue list and handoff

| ID | Severity / status in this initial review | Requested action |
|---|---|---|
| R2-G2-1 | Substantive proof omission; **open** | Explicitly resolve every uncovered multicrossing before tail completion; leave only simple crossings unchanged. Re-review the revised geometry. |
| R2-G1-1 | Wording precision; argument reconstructed | Replace “original grid configuration” in remainder strips by one fixed minimal resolution, or simply cite repeated superadditivity and f>=0. |
| R2-F1-1 | Topological exposition; no remaining counterexample after reconstruction | Make the regular-neighborhood/Jordan-boundary step and empty-slot gap choice explicit; preserve all labelled port vertices. |
| R2-F2-1 | Source precision | Add Felsner--Weil Theorems 7--8 for the exact rank-three four-packet correspondence. |
| R2-F3-1 | Hypothesis precision | State proper transverse two-port arcs at disk boundaries; specify F(empty)=1 or exclude empty disks. |

The author must perform repairs. The coordinator may integrate the issue IDs into the shared log after this independent report is frozen. I require a targeted re-review of the actual G2 repair before withdrawing R2-G2-1. No result has been promoted by this reviewer, and a second independent initial audit remains a separate protocol obligation.

## 11. Primary-source fingerprints

All hashes below were computed from the local bytes actually inspected. Additional command/output fingerprints and the retrieval/render record are in `secondpass-review-2-sources.json`.

| Source | Local cache path from repository root | SHA-256 |
|---|---|---|
| Official Paper B | `.cache/official/2017-paper_b.pdf` | `69d7cf84128c2464d962136ed613808b6c7a7b07122cfba9c06b5adf775e2a68` |
| Official notes | `.cache/official/2017-solutions.pdf` | `c272a72239ef4c2ccd54df0702140179e0a9b85f5a9028c87d485841eb1a2c12` |
| Felsner--Valtr | `.cache/literature/2017/cited-7f7251133b0c4ebc.pdf` | `9f68329a62318b355cde668eabb9a05073ce755becfdd81dc5a6a15f9db68c26` |
| 2024 paper, arXiv v2 | `.cache/literature/2017/cited-b5bf6499a3fedd25.pdf` | `075dee678bceb7bddf599d1a402d37c56659bb84302765aa4c6a74b8539b0f17` |
| Felsner--Weil, author version | `.cache/literature/2017/secondpass-review-2-felsner-weil.pdf` | `a6995529d08034c0735b3f9b0b9a4f9dae01ac0a5f3864d88728c6d04f85c828` |
| Rote consistency source, not used for four-packet sufficiency | `.cache/literature/2017/cited-95c9ccd7e229423b.pdf` | `52c12c2b2d30ae72bcfe859f609520cbbc7f89a1c1dbf60e8002a33a74a28073` |

Full primary papers and source-page images remain ignored cache files. Their public availability was not treated as a redistribution licence, and no charge or access restriction bypass occurred.
