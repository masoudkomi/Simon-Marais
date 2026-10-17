# Annulus A1--A5 v1.1 targeted reaudit, reviewer 2

2026-10-17 UTC. This separate targeted report reviews the author's full
replacement, complete repair ledger and affected uses after both original
whole audits were frozen. It does not edit or supersede their historical
bytes. The independent 2024 divisor initial audit was also frozen before
this repair was opened.

## Conclusion and correction to my original audit

The explicit v1.1 repair is sufficient for AR1-01, and it incorporates
ANN2-N1 and ANN2-N2 correctly. I recommend coordinator resolution for
the hashed v1.1 copy after both targeted independent reaudits. I found
no new substantive issue in the changed argument or its affected uses.
No promotion is performed by this reviewer.

My initial whole report did not flag the literal standalone A2
rank-domain omission. Its “no substantive defect” conclusion was too
broad for that wording. I had reconstructed A2 with the inherited
rank-range interpretation used by A1, without identifying that A2
did not explicitly require it. Reviewer 1's absent-color example is
a real counterexample to the literal unqualified standalone statement.
I acknowledge that omission here; the original report and ledger remain
byte for byte unchanged.

Inputs:

- Complete candidate v1.1, 26275 bytes, SHA-256
  c6da61f229ffa72dd830cd40132969717a395e3744b6d775cbe83a32bdd3747c.
- Complete repair ledger, 7152 bytes, SHA-256
  a0805df0cdc05f30ab8256fe9cf64ba466f932abc3cd97b45d68f1d98cae51b0.
- Constructor freeze v1.1, SHA-256
  43ec9d1ce2e2f160658ed356cdf70a3429aa672bf28bf9af5832a9a813ccb4f9.

The full worklog, source metadata and textual diff were read as well.
Both complete original whole reports and both complete issue ledgers
were read after their initial freezes. The later peer targeted report
was not needed or read for this conclusion.

## 1. Reconstruct the exact missing-color counterexample

The outer frame has \(N=(10,10,10,10)\), ascending blocks below and
descending blocks above. It is the convex Jordan zonogon \(Z_{10}\).
The common-comparison poset has only the four independent same-color
rank chains; all cross-color comparisons differ at the two extremes.

For the inner single type-13 tile take lower/upper words \(13,31\)
and assigned start/end
\[
a=(7,-2,7,4),\qquad b=(8,-2,8,4).
\]
The kernel vector \(k=(1,-2,1,0)\) satisfies \(Vk=0\), and
\(a=(4,4,4,4)+3k\). Directly,
\[
Va=(16,24),\quad V(a+e_1)=(17,24),\quad
V(a+e_3)=(17,26),\quad Vb=(18,26).
\]
Every point of this tile also has a coefficient representative
\((4,4,4,4)+\alpha e_1+\beta e_3\), \(0\leq\alpha,\beta\leq1\),
strictly inside the cube \([0,10]^4\). Since \(V\) has rank two,
it maps a small open neighborhood of each such representative to a
physical open neighborhood in \(Z_{10}\). The compact tile therefore
lies strictly inside that outer zonogon, with positive separation.

The four literal sets \(I(h)\) have color counts
\[
(7,0,7,4),\ (8,0,7,4),\ (7,0,8,4),\ (8,0,8,4).
\]
They are all ideals of the four chains. The two active inner
colors use genuine available rank 8. The absent color-2 interval
has no labels, so saying that its inner ranks are identified with
the outer ranks imposes no lower bound on the assigned constant
\(-2\).

A full outer tiling, normalized at zero, has each color coordinate
between zero and ten: its de Bruijn tracks run between the ten
boundary ranks, and a closed track is excluded by strict transverse
monotonicity. Thus the negative color-2 assignment cannot extend.
The claimed v1 entry construction exposes the failure precisely:
the restriction of \(p_0\) to literal \(I(a)\) reaches
\((7,0,7,4)\), physically \((18,26)\), instead of the assigned
start \((16,24)\).

This is a failure of the omitted coordinate domain. It does not
contradict A1 with its explicit domain, the range-corrected
shelling argument, or A3's winding test. The author retains and
attributes the exact example correctly.

## 2. Explicit rank box fixes A1/A2 for every color

The replacement now declares \(I(h)\) only on
\([0,N]\cap\mathbb Z^4\) and states the A2 condition
\[
0\leq a_i\leq b_i\leq N_i\quad\hbox{for every }i.       \tag{R}
\]
This condition includes every absent inner color. If \(m_i=0\),
then \(a_i=b_i\) must still be in the available interval.
If \(N_i=0\), this forces both to be zero.

Every boundary prefix of a positive path from \(a\) to \(b\)
is coordinatewise between them, so (R) puts all boundary heights
in A1's domain. The cardinality of the color-\(i\) portion of
\(I(a)\) is now exactly \(a_i\), not a truncated value.
Similarly \(I(b)\) has the actual counts \(b_i\). Hence the
restricted word \(A\) ends at height \(a\), physically \(Va\),
and the complementary word \(B\) begins after the actual
height \(b\).

Ideality of the middle boundary prefixes, together with \(p_0\)'s
restricted order before and after them, gives the same two full
linear extensions \(ApB,AqB\). A1 puts them in the outer interval,
and their middle comparison remains \(p\leq q\). The two fixed
positive swap shellings therefore surround exactly the assigned
core, rather than a differently placed core having the truncated
coordinates.

All entry abscissae are at or before the inner initial abscissa;
all exit abscissae are at or after its final abscissa. Their exact
heights agree on the two sides of each seam. Pointwise path order
partitions the outer vertical sections into lower band, core and
upper band. Tile interiors are disjoint, no corner cap is missing,
and primitive integral edges exclude T-junctions. These were valid
geometric inferences once the actual seam endpoints are secured.

Fixing the boundary fixes the padding before the core filling
varies; restriction recovers every core. For varying boundary
codes, the word lengths and relative integer offsets retain the
\(O(L)\) bounds, so the polynomial offset choices and
\(4^{O(L)}\) word choices still give \(2^{O(L)}\) fibers.
No label factorial is introduced by adding the missing hypothesis.

## 3. Translated frames preserve a fixed assignment

For an outer starting height \(z_0\), the repair explicitly uses
\[
z_{0,i}\leq a_i\leq b_i\leq z_{0,i}+N_i,\qquad
I(h-z_0).
\]
Subtract \(z_0\) from heights and \(Vz_0\) from physical points.
Positive edge increments, content, Jordan containment, seam
geometry and the poset are unchanged. Global labels are exactly
\(z_{0,i}+1,\ldots,z_{0,i}+N_i\).

This is one fixed translation of the common frame. It does not
permit changing the already assigned inner offset, independently
adjusting corners or permuting color ranks. The boundary-code
count is in relative coordinates, so an arbitrarily translated
but fixed outer base adds no uncounted entropy factor.

## 4. A3 derives the range before invoking A1

The revised A3 statement deliberately does not assume (R) or
ideality. It retains the actual Jordan lenses, words and
assigned lifts, then assumes containment, the common affine
estimates and the numerical vertex buffer.

For each pair \(i<j\), the old valid homotopy estimate gives
winding one about \(h_{ij}(x)\). The point avoids the projected
outer loop throughout. The actual two-color loop bounds its
ordered weak lens, which is contained in
\([0,N_i]\times[0,N_j]\). Thus winding one first gives both
coordinate inequalities, regardless of whether either color
occurs on the inner boundary.

All six tests put every boundary height in the full rank box.
In particular they put \(a,b\) there, and their nonnegative
content gives \(a_i\leq b_i\). This proves (R).
Only then does the proof invoke the A1 equivalence to derive
ideality. There is no circular assumption of the missing A2
hypothesis.

For a translated frame, the exact new offset is
\[
c'=c-(I-JV)z_0.
\]
It belongs to \(\ker V\), since \(V(I-JV)=0\). Direct expansion
gives
\[
(h-z_0)-J(x-Vz_0)-c'=h-Jx-c.
\]
Both affine errors and all physical distances are unchanged.
The winding proof yields the relative range and ideals required
by translated A2.

The vertex-buffer constant and six-pair singular-value estimates
are unchanged. No uniformity as a minor tends to zero is added.
The absent-color example fails the range conclusion and hence
cannot satisfy all A3 hypotheses; it is not an A3 counterexample.

## 5. ANN2-N1: strict containment from unit-horizontal graphs

The author now supplies the requested geometric step explicitly.
Every boundary edge spans an interval \([k,k+1]\) with integral
\(k\); the two outer boundary paths are also affine on exactly
that interval. Containment and positive vertex distance place both
endpoints of an inner edge strictly between the outer graphs.
Both differences are affine and positive at their endpoints, so
they stay positive throughout the edge.

This covers all inner boundary edges and rules out a nonvertex
contact. Their closed inner lens is strictly contained in the
outer Jordan domain. Compactness gives a positive minimum
separation. The proof correctly does not claim that every
point has numerical distance at least the original vertex
bound \(t\); only the tested vertices need that quantitative
bound for winding. This clarification is valid specifically
in the integral unit-horizontal model.

## 6. ANN2-N2 and downstream scope

The revised transfer summary now lists the required fixed data:
a rational strict slope, one common affine offset, one phase,
a compatible receiving integer frame, actual Jordan two-path
inner lenses with comparable words and their assigned lifts,
physical containment, affine errors and the quantitative buffer.
It says explicitly that direct A2 instead requires (R) and
the ideal tests as hypotheses.

The statement retains the \(O(L)\) word and relative-offset
bounds for the fiber estimate. It expressly does not construct
a thin canonical frame for every shape, bound arbitrary relative
area overhead, allow independent corner offsets, or extend a
constant uniformly to a zero minor.

The read-only diff confirms that the A4 digital comparison,
flatness, phase and bounded end-lobe arguments, and the A5
block-gluing/liminf proof are unchanged. Their original whole
reconstructions remain applicable. The summary change makes
their actual conditional interface more precise; it does not
create an additional unrestricted entropy theorem.

No DG or CUT theorem is used as a repair premise. Arbitrary-window
extraction, non-strict strata, global original-zonogon profile
recovery and (H) remain unproved in this packet. The external
Levi source remains an attributed lead only.

## Procedure, immutable records and status

I read the full v1.1 replacement and ledger, complete unified diff,
both whole original reports and both issue ledgers. No peer targeted
reaudit conclusion was used. The author inputs, original annulus v1,
both original audit records and all thirty-nine earlier files frozen
by this reviewer are verified unchanged by their recorded hashes.

Only annulus-review-2-reaudit- files are written. There was no
mathematical enumeration, routine test, CAS, numerical certificate,
candidate/shared edit, Git action, source download, charge or spawn.
The counterexample and rebase were checked by exact hand algebra
and geometry.

Requested gpt-6.1-sol / max; independent effective readback
unavailable. Latest authoritative weekly use is 21% total,
reset 1792745187, below the 90% total-used ceiling with reserve.
The full report, issue dispositions, source/procedure record
and hash manifest are frozen separately from all prior reports.
Coordinator resolution and promotion remain pending.
