# Targeted annulus repair re-audit: AR1-01 and ANN2-N1/N2

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`, nonconstructor.
Requested gpt-6.1-sol/max; no independently verified effective-setting
readback. This targeted report follows my frozen blind whole A1--A5
audit and the separately frozen fixedD and CUT audits. Both complete
original annulus reports and issue ledgers were read only after both
initial freezes, as authorized. No peer targeted annulus re-audit was
read before this report froze. No DG or CUT inference is a premise here.

## Disposition

I recommend resolving AR1-01 for the full v1.1 candidate. It now explicitly
requires the available rank interval for every color, including an
absent inner color. The entry/exit seam proof uses that interval to reach
the actual assigned lift rather than a truncated prefix. A3 derives the
new condition from winding, before invoking A1, so the repair is not
circular. The translated-frame identities preserve every hypothesis.
ANN2-N1's strict-nesting explanation is correct in the fixed integral
unit-horizontal geometry. ANN2-N2's summary now keeps the complete
conditional transfer and code-range hypotheses. No new substantive
objection arose in this targeted reconstruction.

This is a recommendation for coordinator reconciliation after both
targeted audits, not reviewer promotion. The original v1 omission and
both initial reports remain preserved. A1--A5 remain partial results
in their stated model and receiving family; no H, full 2017 solution,
arbitrary-shape thin frame or stratum-uniform recovery is accepted here.

The full v1.1 candidate has SHA256
`c6da61f229ffa72dd830cd40132969717a395e3744b6d775cbe83a32bdd3747c`;
the repair ledger has SHA256
`a0805df0cdc05f30ab8256fe9cf64ba466f932abc3cd97b45d68f1d98cae51b0`;
the author freeze has SHA256
`43ec9d1ce2e2f160658ed356cdf70a3429aa672bf28bf9af5832a9a813ccb4f9`.
The complete replacement, repair ledger, textual diff, worklog and
sources were read. Their bytes and the exact diff are checked in the
companion metadata, along with all earlier own frozen packets.

## 1. The explicit all-color rank domain repairs the seam

For an outer frame based at zero with content N, A1 defines I(h) only
for integer h in [0,N]. A2 now explicitly assumes

    0<=a_i<=b_i<=N_i for every i.                       (R)

The inner content m=b-a is nonnegative and its boundary paths are
positive. Every integer vertex height on either boundary therefore
satisfies a<=h<=b. It is genuinely in I's domain. This proves the
domain for all tested prefixes, including the initial and final ones;
it is not an inference from the literal set formula's ideality.

If m_i=0, the i coordinate is constant a_i=b_i throughout the inner
boundary. It still must be in [0,N_i]. The interval of inner i ranks
can be empty without losing this bound. If N_i=0, (R) forces a_i=b_i=0
and hence m_i=0. If a coordinate equals an available endpoint, its
prefix is truly empty or full; no off-by-one convention is needed.
Each active inner rank is exactly the global label a_i+1,...,b_i.

In particular I(a) has exactly a_i members of color i and I(b)
exactly b_i. Let A be the restriction of p0 to I(a), B the restriction
to the complement of I(b). A reaches lift a and physical point Va;
after the prescribed inner path reaches b, B reaches the outer final
height N. The actual coordinate counts are no longer replaced by
max(a_i,0) or any other truncation.

Every prefix along A is an ideal: I(a) is an ideal, and predecessors
inside I(a) appear earlier in p0's restricted order. Every prefix
through p or q is an ideal by the boundary hypothesis. In B, any
remaining predecessor outside I(b) occurs earlier in p0's order and
any predecessor inside I(b) is already selected. Both ApB and AqB
are therefore linear extensions of the one outer poset, giving

    p0<=ApB<=AqB<=q0.

The middle comparison uses the same exact global ranks for p and q.
The original adjacent increasing-swap construction supplies positive
planar tile shellings of the first and last comparisons. Their interiors
are disjoint because their paths are pointwise ordered. Their middle
region is precisely the assigned physical inner lens. Appending the
actual inner filling gives the complete outer filling.

A has all x coordinates at or before Va_x, and B at or after Vb_x,
since each edge advances x by one. They are actual rank-matched entry
and exit seams outside the inner interior. They leave no unmatched
corner cap. Coincident seams or weak bands are handled by the same
positive shelling; neither auxiliary band is required to be Jordan.
The original A2 closed-annulus construction is thus valid under (R).

## 2. Translated frames retain the assigned inner offset

For an outer starting lift z0, the relative coordinates are

    x'=x-Vz0,  h'=h-z0.

The explicit condition becomes

    z0_i<=a_i<=b_i<=z0_i+N_i,

and the ideal test is I(h-z0). The relative entry word has a_i-z0_i
occurrences of color i; starting from z0 it ends at a exactly. Global
rank labels are z0_i+1,...,z0_i+N_i, and the core uses the consecutive
subinterval a_i+1,...,b_i. This is a fixed normalization of one outer
frame. It does not choose a new kernel offset for the inner patch or
independent offsets at different corners.

For the affine lift Jx+c, define

    c'=c-(I-JV)z0.

Since VJ=I and Vc=0, Vc'=0. Direct substitution gives

    h'-Jx'-c'=h-Jx-c.

The same identity holds for the outer boundary lift. Both error bounds
are unchanged, and physical translation preserves distance and nesting.
The ordered minors and sigma(J) are unchanged. Applying the zero-based
argument therefore proves exactly the relative range and ideal tests;
there is no silent change in the specified phase or rank assignment.

## 3. Fixed-core injection and varying-boundary fibers

For one inner boundary, its offset, words, seams and two padding chains
are chosen before its filling varies. Restriction to that fixed physical
core recovers every input tiling. The construction is injective and
requires no matching permutation or crossing-order factor.

For a varying family in one fixed receiving frame, record the relative
starting vector and two words. Four relative integer coordinates of
magnitude at most cL have at most (2cL+1)^4 possibilities. Two words
of length at most cL contribute at most 4^(2cL), with a polynomial
length-convention factor. The ending vector follows from the first
word's content. The recorded offset and word vectors place the entire
core physically and assign its ranks exactly. Given that code and an
outer output, restriction recovers its inner filling. Thus a fiber has
size at most 2^O_c(L), with the stated relative-coordinate and word
bounds retained. Arbitrarily unbounded offset ranges are not silently
included in this estimate.

The repaired summary calls this a transfer only after a receiving
frame satisfying the actual geometry and rank or winding hypotheses
has been supplied. Injection and this upper-fiber estimate do not bound
the area overhead of finding such a frame for every arbitrary shape.

## 4. A3 derives range before ideality, without circularity

The revised A3 starts with the outer Jordan frame and an actual inner
two-path Jordan lens with comparable words and assigned integer lifts.
It explicitly does not assume (R), ideality or strict nesting. Instead
it assumes physical containment, a positive boundary-vertex distance t,
one common affine offset c in ker V and the displayed errors E0,E1.
All ordered row minors of J are positive; each M_ij is therefore an
orientation-preserving invertible map with least singular value at
least sigma(J)>0.

For an inner boundary vertex x, the point y=M_ij*x+c_ij is inside the
affine image of the outer Jordan domain and is at distance at least
sigma(J)*t from its boundary. Its assigned pair height h_ij differs
from y by at most sqrt(2)E1. The strict inequality

    sigma(J)*t>sqrt(2)(E0+E1)

therefore keeps h_ij inside that affine image and more than sqrt(2)E0
from its boundary. The actual outer projected height loop is pointwise
within sqrt(2)E0 of the affine loop. The straight boundary homotopy
avoids h_ij, preserving winding one. This uses only vertex tests for
the inner boundary and the stated all-boundary estimate for the outer
lift; no interior-gradient interpolation is asserted.

The actual projected loop is the lower two-color E/N path followed
by the upper in reverse. Their weak-order comparison makes all open
lobes positively oriented; common pieces cancel. A point off the loop
with winding one belongs to an open lobe of the projected weak lens.
That lens is contained in [0,N_i] times [0,N_j]. Thus winding first
proves the coordinate bounds for h, without ever forming an off-domain
I(h). All six pairs cover every color. At the initial and final
vertices this gives (R), including the constant height of an absent
inner color. Only then is A1 used to prove ideality at every boundary
vertex from the six projected lens memberships. The repaired A2 can
now be invoked. These are all its rank hypotheses, derived in the
correct logical order.

Weak or collapsed projected boundaries cause no loophole. Their
winding cannot be one off the loop unless they have a genuine open
lobe containing the test point. If an outer color were absent, the
corresponding projection would be a segment; in that case these strict
A3 hypotheses cannot all hold, rather than proving a spurious rank.
The direct A2 theorem still treats empty colors at closed rank endpoints.

The factor sqrt(2) correctly converts a coordinate infinity error into
two-coordinate Euclidean error. The least singular value bounds
physical distance from below. Constants still depend on sigma(J)^-1
and are not uniform as a minor tends to zero. Rationality is used by
A4's receiving construction, not by this winding proof. The relative
frame identity in Section 2 applies without modifying any estimate.

## 5. ANN2-N1: strict nesting follows in the stated edge geometry

Containment and t>0 put every inner boundary vertex strictly inside
the outer Jordan domain. All relevant vertices have integral x
coordinate because their lifts are integral and the first row of V
is all ones. Every edge has horizontal displacement one. On an
interval [k,k+1] containing an inner edge, that edge and each outer
boundary path are affine graphs. Their vertical gaps at k and k+1
are strictly positive. The gap to either outer graph is affine, so
it is positive on the entire interval.

Hence no inner edge can touch an outer edge in its interior. At an
integer abscissa a contact would be a forbidden vertex contact.
The inner boundary is disjoint from the outer boundary; the assumed
containment and the two-path geometry give strict nesting of the whole
closed inner lens. Compactness gives a positive separation. This fills
the premise needed in A2.

The author correctly does not claim that the minimum separation over
all inner edge points is at least the stated vertex bound t. The
winding argument only uses the bound at the vertices it tests. Nor is
the affine-gap argument asserted for arbitrary edges with longer
horizontal spans or nonintegral unsynchronized breakpoints. The
clarification resolves ANN2-N1 in this exact model without a stronger
new quantitative claim.

## 6. Retained counterexample remains a genuine diagnostic

The author retains my exact single type13 tile in the full Z_10 frame:

    p=13, q=31,
    a=(7,-2,7,4), b=(8,-2,8,4).

V(1,-2,1,0)=0, so its points have alternative coefficient
representatives (4,4,4,4)+alpha e1+beta e3, alpha,beta in [0,1],
strictly inside the coefficient cube. The physical vertices are
(16,24),(17,24),(17,26),(18,26), and the physical tile is strictly
inside Z_10. The outer common poset consists of four independent rank
chains, so the literal I formulas at all four assigned vertex heights
are ideals after erasing the negative second coordinate. The active
inner ranks are legitimate rank 8 of colors 1 and 3, while the color-2
interval is empty.

The proposed old entry word has coordinate counts (7,0,7,4) and ends
physically at (18,26), not at (16,24). It fails to retain the assigned
core. A full outer lift cannot take the value -2 in color 2 relative
to its prescribed base. The v1.1 condition (R) expressly excludes this
example, while still allowing valid absent-color examples with
0<=a_2=b_2<=10. A3 excludes the assignment independently because
winding one in its pair projections would force that same range.
No new premise is added merely to the conclusion of A3.

The older growing kernel-offset example is also preserved. It remains
an assigned-lift obstruction to a bounded collar with error growing
like M, and violates the required order-M buffer. It refutes neither
the corrected A2 nor the A3 sufficient test. Both examples are exact
analytic diagnostics, not computations supporting an infinite claim.

## 7. ANN2-N2 and unchanged downstream claims

The complete transfer summary now fixes a strict rational J, one common
affine offset c, one phase and a compatible receiving integer frame.
It requires actual comparable two-path Jordan inner lenses with assigned
integer lifts, physical containment, and A3's common-affine estimates
and quantitative buffer. If A2 is applied directly, the summary instead
explicitly requires its rank box and ideal tests. It retains O(L) word
lengths and O(L) relative integer offsets for the varying-code bound.

It does not construct a thin canonical frame around an arbitrary
shaped lens, bound the relative area overhead, allow independently
chosen corner offsets, reset phases freely or provide uniform constants
at zero minors. ANN2-N2 is therefore resolved in the proposed v1.1
scope. The final interface section leaves arbitrary cut windows,
non-strict slopes, fixed-zonogon profile recovery and all-scale global
remainders open. Neither DG nor CUT is used as a repair dependency.

A4's rational digital words, same-phase comparisons, bounded main-lobe
trimming and offset alignment are mathematically unchanged. A5's exact
block-gluing inequality and receiving-family limit are unchanged. The
repairs neither alter those counts nor promote their C_L entropy to
the full balanced B_D count. My original whole reconstruction of those
parts and the other original whole report remain the appropriate
whole-audit records; this targeted report checks every changed use.

## 8. Source, independence and operations

Both complete original whole reports and ledgers, plus reviewer2's
original source checks, were read after their freezes. The first
report's rank-domain objection and the second report's two geometric/
scope suggestions are now reconciled by explicit author text. I did
not read any peer targeted repair conclusion. My whole CUT report was
frozen before this task started and supplies no premise to this repair.

The full replacement, ledger, worklog, source record and complete saved
diff were read. The companion metadata re-generates that textual diff
and verifies its exact bytes, the seven author artifacts, the frozen v1,
both initial annulus audit packets and all eight earlier own packets.
No earlier candidate or report is altered. The elementary rank,
shelling, affine and winding checks use no new external theorem. The
Levi paper remains a historical lead for a separate interface, not an
A1--A5 dependency. No new PDF retrieval or redistribution occurred.

No enumeration, CAS, numerical test, mathematical subprocess, shared
status edit, Git operation, spawning, paid API, contact or access bypass
was used. Only this assigned targeted prefix is written. One-time
hashing, exact textual diff comparison and JSON freezing are
administrative. Fresh authoritative telemetry at this task transition
reported 21% total weekly used, 10080-minute window, reset1792745187,
under the 90%-total ceiling with integration reserve. Only the
coordinator may resolve/promote the scoped claims after both audits.
