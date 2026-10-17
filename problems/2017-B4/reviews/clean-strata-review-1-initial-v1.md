# Blind whole reconstruction: FL1, CL1 and OB1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`, fresh
nonconstructor. I did not construct this packet and read no peer
clean-strata report, issues or findings before this report and its
companion records froze. Requested gpt-6.1-sol/max; independently
verified effective settings are unavailable. No search, enumeration,
CAS or mathematical program was run in this audit.

## Disposition

FL1, CL1 and the exact local obstruction OB1 survive the full analytic
reconstruction below. I found no substantive objection or required
author repair within their stated scopes. The flux identity has the
correct sign and cut-tile normalization; a rectifiable boundary gives
the claimed fixed-width tube count. The clean within-group assumption
fixes the entire fine sequence, so the interval isomorphism preserves
cover paths and their commutations and supplies the claimed tiling
bijection. The four-label example has exactly one fine tiling, two
coarse weak-lens tilings and one erased crossing; only the first coarse
tiling is attained.

These are separate partial results and an obstruction. A small number
of forbidden tiles is not the same condition as their complete absence.
No thin location band, arbitrary coarse insertion with rare crossings,
stratum repair, EAI, PR, H or official entropy rate is accepted here.
Only the coordinator may reconcile and promote the scoped claims after
both independent whole audits.

Input candidate SHA256:
`aa4c79b1fb3136ecd3e7c5ab845733697cca925ba8203b2988fba5c9a793bd95`.
Its entire text, freeze, search source and saved output/job provenance
were read. The search was not rerun; OB1 is checked independently of
its implementation. Accepted structural and DC1 background is used
only in the precise dictionary/source scopes described below.

## 1. FL1: exact boundary identity and its hypotheses

Orient the Jordan Lipschitz boundary counterclockwise and put
e_i=a_i-b_i, b=Jx+c. For Lipschitz coordinate functions the weak Green
identity reads

    integral_Omega det(grad f,grad g)=integral_boundary f dg.

It follows either from the distribution identity
det(grad f,grad g)=partial_1(f partial_2g)-partial_2(f partial_1g)
and the Lipschitz-domain trace formula, or by smooth approximation.
The lift is continuous and affine on the finitely many tiles meeting
this bounded window. Its derivative bound and the rectifiable boundary
give the needed traces and finite tangential variation. No smoothness
of a across tile edges, or polygonal shape of the window, is required.

Subtract the Green identities for a and b. Along the closed boundary,

    a_i da_j-b_i db_j=e_i da_j+b_i de_j,
    integral b_i de_j=-integral e_j db_i.

Thus the candidate's exact formula has the correct order and sign:

    integral_Omega [det(grad a_i,grad a_j)-det(J_i,J_j)]
      =integral_boundary [e_i da_j-e_j db_i].

Only whole-boundary closeness is used. The coordinate gradient bound
G_D bounds the variation of a_j along the boundary by G_D times its
perimeter; the fixed affine gradient bounds that of b_i by ||J_i||
times the same length. Since each |e_i|<=epsilon*L and perimeter<=C*L,
the absolute discrepancy is at most

    C*(G_D+||J||)*epsilon*L^2,

with harmless fixed choices of matrix norm. The offset c cancels from
the derivatives. The estimate needs no interior affine-closeness
assumption, no minor positivity for the comparison matrix and no
common-positive-direction hypothesis. J is fixed and bounded exactly
as the candidate states.

On a tile of type ij, i<j, the only nonzero ordered lift minor is
det(grad a_i,grad a_j)=1/(j-i). The physical tile area is j-i, so its
whole integral is one. Every other tile type contributes zero to this
pair minor. On a cut ij tile the contribution is the fraction of its
area inside Omega, lying in [0,1]. This verifies the normalization and
nonnegativity of the fractional count without replacing the integral
by an unjustified integer count.

## 2. FL1: a rectifiable tube controls all cut tiles

Let d_D bound every tile diameter. Every tile touching the boundary
is contained in its d_D-neighborhood. A curve of length ell<=C*L has
an arclength net with O(ell+1) points at any fixed positive spacing.
Fixed-radius disks about that net cover the fixed-width tube. Enlarging
the disks by a unit-cell diameter bounds the number of lattice cells
meeting the tube by O_D(C*L+1). This remains true with arbitrarily many
wiggles, close returns or small geometric features; no convexity or
lower curvature bound is used.

For fixed D, possible integer origins and tile types incident to a unit
cell form a fixed finite set. Hence O_D,C(L+1) actual tiles meet the
boundary. One can also use their disjoint interiors and minimum area
one inside a slightly enlarged tube. Either way the constants are
independent of the window's individual local features.

Tiles wholly inside contribute one, wholly outside zero, and the only
fractional ambiguity belongs to those boundary tiles. The number of
whole ij tiles, or of ij tiles intersecting the window including mere
boundary contact, therefore differs from the integral by
O_D,C(L+1). In particular, when det(J_i,J_j)=0, the nonnegative integral
and the discrepancy estimate give

    # intersecting ij tiles=O_D,C,J(epsilon*L^2+L+1).

For L bounded below by a fixed positive constant this is the written
O_D,C,J(epsilon*L^2+L) large-window form. The earlier O(L+1) expression
already records the small-scale convention. Fixed finitely many pairs
may be summed. Parallel-row groups and pairs involving a zero row have
zero determinant and are covered. No statement follows about where the
few tiles occur within the window.

For completeness, at finite scales discarding every fixed-side-l cell
containing a rare tile gives area O(l^2*(epsilon*L^2+L)); the candidate's
final O(epsilon*l^2*L^2) is its leading large-L order with fixed positive
epsilon and l. It must not be used uniformly after dropping the boundary
term in a simultaneous limit. The text's main claims already retain
that term and explicitly warn against exchanging the local/global
orders of limits. This is a parameter clarification, not an obstruction
to FL1 or a new recovery theorem.

## 3. CL1: clean boundary data fix every fine label sequence

For comparable endpoints p<=q, every crossing event adds a previously
absent inversion of two distinct fine colors. The number of ij tiles
is the number of such new ij ranked pairs, fixed by the boundaries.
It can also be verified directly from Green's identity: integrating
the ij lift minor over the whole tiled lens equals

    integral_p a_i da_j-integral_q a_i da_j
      =Inv_ij(q)-Inv_ij(p).

The last equality follows by counting i's before each j in either
word. The nonnegative tile contributions then show that absence of
all within-group tiles is equivalent to absence of all corresponding
new inversions. It is enough for one filling to have none; every
filling of these boundaries has the same zero counts.

p and q consequently agree on every pair of labels whose colors are
in one group, including the fixed ranks of an individual color. Their
entire restricted total orders r_g are identical, not just their group
totals. Any intermediate fine word w must preserve those same
comparisons, and hence has exactly the restricted sequence r_g.

Replace its kth group-g occurrence by coarse rank (g,k). Conversely
replace (g,k) by the kth fine ranked label of r_g. Since r_g itself
preserves each fine color's internal ranks, every expansion is a valid
fine shuffle. Groups are consecutive in fine color order. Therefore
for different groups g<h, every fine label of G_g is initially below
every label of G_h. Cross-group fine inversion pairs correspond
one-to-one, with the same orientation, to the coarse ranked pairs.
Their lower and upper inclusion tests are precisely the coarse
interval tests. Within a group the fine tests are fixed already.
This proves both directions and order preservation, yielding

    [p,q] isomorphic to [coarse(p),coarse(q)].

It also proves comparability of the two coarse endpoints. Nonconsecutive
groups could reverse some initial cross-group label orders and are
properly excluded. Zero-count fine colors have no labels. Empty coarse
contents can likewise be omitted; the interval correspondence itself
still makes sense with their empty sequences. A genuine clean Jordan
lens must have at least one nontrivial cross-group tile event.

## 4. CL1: cover paths, tilings, geometry and Jordan boundary

A cover swaps two adjacent labels at the same two word positions.
No within-group pair can be swapped in the clean interval. Thus a fine
cover corresponds to exactly one coarse cover at the same position,
with exactly the fine labels selected by the fixed r_g sequences.
The inverse expansion has the same property. A commutation of disjoint
adjacent swaps, whose position indices differ by more than one, is
therefore literally preserved in both directions. Maximal cover chains
and their commutation classes are in bijection; this is stronger than
a bijection of individual words alone.

The positive-shelling/marked-tiling dictionary converts those classes
to the genuine fine and coarse lens tilings. Its geometric hypotheses
can also be checked directly here. Every swap raises its positive path
and adds precisely one positive parallelogram. Each new interior lies
above the previous path, disjoint from earlier tiles. Same-color curves
do not cross, and the transverse functional det(v_i,x) strictly increases
along a color-i curve. Within a Jordan positive-path lens every such
curve joins its lower and upper boundary; at a different-color crossing
all local intersection signs are positive, so a pair crosses at most
once. Their boundary orders determine exactly the interval events and
the crossing orders determine the commutation class. No closed track
or unrecorded crossing can supply an extra filling.

For an additional direct geometric check of the inverse, label the
coarse group-g curves in their fixed rank order and assign the kth one
the kth fine label in r_g. Each coarse crossing joins different ordered
groups, so it becomes one positive fine ij parallelogram. Opposite
edges get the same fine labels because the other group changes none
of the ranks in r_g. At a vertex, coarse prefix counts determine the
sum of the corresponding fine prefixes. Thus faces and seams are
consistent and the boundary is exactly p,q. The positive dual-face map
has degree one on the prescribed fine Jordan boundary; its faces have
positive orientation. A regular interior point has exactly one face
preimage and an exterior point none. Adjacent sectors are locally open
at edges and vertices, so an identification there would force two
preimages of a nearby regular point. Hence it is a geometric tiling,
not a folded projection. This agrees with the commutation-class proof.

Choose coarse vectors w_g=(1,s_g) with strictly increasing s_g; rational
choices between the original group extremes are available because the
groups are consecutive. Every cross-group tile has positive area and
every coarse edge has unit x displacement. If the comparable coarse
paths share a physical vertex at the kth prefix, each increasing swap
that changes that prefix raises its y coordinate by s_h-s_g>0. Equality
of the endpoint y values forces no such prefix change, so the two
coarse prefix count vectors are equal. For each g this fixes the same
prefix of r_g and therefore the same full fine prefix counts. Their
physical fine vertices coincide. Fine Jordan boundaries exclude such
a common vertex except at the endpoints.

At a noninteger abscissa in (k,k+1), the difference of the coarse
boundary graphs is affine. Their nonnegative endpoint differences
cannot have an isolated interior zero; an identically zero interval
would already give common vertices. Thus there is no new nonvertex
contact. The coarse boundary is Jordan as asserted. Conversely a common
fine vertex on comparable fine paths gives equal fine prefix counts
by the same strict-swap argument, and hence equal coarse counts.
This confirms the claimed geometric correspondence independently of
any accidental kernel relation among physical vectors.

After expansion the fine words and fine vectors are exactly restored.
The bijection therefore preserves the entire original fine boundary,
not merely its side totals. For varying boundaries, each r_g is an
ordered list of fine colors with their ranks forced by order within
each color. O(L) letters suffice; no factorial assignment of fine
labels is required. A single within-group crossing destroys this fixed
sequence premise, so CL1 asserts no approximate version.

## 5. OB1: the four-label calculation is a complete hand proof

For p=1243 and q=4312, Inv(p) consists only of (3,4), and

    Inv(q)={(3,4),(2,4),(1,4),(2,3),(1,3)}.

In particular (1,2) is absent from q. At p, the adjacent 12 swap is
forbidden by that missing inversion and 43 is descending. The unique
allowed first cover swaps 24, producing 1423. The only choices there
are disjoint position swaps 14 and 23. They may occur in either order:

    1423 -> 4123 -> 4132,
    1423 -> 1432 -> 4132.

At 4123 the 12 swap is still forbidden, so 23 is forced. At 1432
only 14 is allowed. From 4132 only 13 can be added, giving q=4312.
These are all maximal chains, and the two middle covers commute.
Hence there is exactly one fine commutation class/tiling. The sole
within-B crossing, for B={2,3}, is 23.

The physical prefix y coordinates are

    p: 0,0,1,4,6,
    q: 0,3,5,5,6.

Their gaps at the three interior integer x positions are 3,4,1,
all positive; the linear edge gaps are positive in between. Thus this
fine lens is genuinely Jordan in the given integer projection. Its
tile areas also check: type24 area2, type14 area3, type23 area1,
type13 area2, total8, matching the graph area of these boundaries.

After merging 2,3 to B with A={1}, C={4}, the endpoints are ABCB and
CBAB. Their last B edge is a common zero-area tail. The first three
letters bound the usual ABC-to-CBA hexagon, with two maximal-chain
classes:

    ABCB -> ACBB -> CABB -> CBAB,
    ABCB -> BACB -> BCAB -> CBAB.

Their event orders are BC,AC,AB and AB,AC,BC respectively. No two
events in a three-strand reversal are disjoint, so these are two
different tilings. The first three-edge chains have a Jordan hexagon
under any strict ordering of the three coarse slopes. The common
tail makes the complete coarse object a legitimate weak lens rather
than a Jordan lens, exactly as the candidate states.

Project either fine chain and erase 23. Its surviving word sequence is

    ABCB -> ACBB -> CABB -> CBAB.

Thus only the first coarse tiling is attained. The second's intermediate
word BACB has no fine expansion in the interval: first B=2 gives
2143 and the forbidden inversion (1,2); first B=3 gives 3142 and
loses the mandatory common inversion (3,4). Equivalently the latter
ordering would require 4 before3 before1 before4. This is a direct
boundary compatibility obstruction, independent of the search.

The failure is local prescribed-boundary lifting after one erased
crossing. It does not refute CL1, whose zero-event hypothesis fails,
or global DC1 surjectivity. The DC1 section is available for a full
sorted/reversed outer frame because one may add a fixed internal
reversal prefix there; that prefix is forbidden by these local fine
endpoints. The distinction is essential and is maintained in the text.

## 6. Search provenance and exact scope

I read the search source and its saved metadata only. It uses unique
fine labels, four specified consecutive-group size patterns on five
labels, inversion differences at most eight, and stops on the first
projected-signature failure. It made 1837 interval checks before finding
an example with an additional common initial A edge. Removing that
zero-area prefix and shifting labels gives the exact four-label example
above. The stdout, empty stderr and job records agree that PID77136
finished normally and was reaped, under its recorded 10-second timeout,
in approximately0.137s. Its internal reported search time is shorter
than that external wall time, as expected.

No assertion relies on absence of other examples or on completeness
of an unbounded search. No rerun, extension of the search or native job
was performed here. OB1's complete finite example is certified by the
hand classification of its allowed covers, so a program bug would not
affect this proof. The other two claims are unrestricted analytic
arguments under their stated hypotheses and use no computation.

FL1 is a density bound, CL1 is an exact zero-crossing result, and OB1
separates them. Rare tiles may occur in every macroscopic mesh cell;
global epsilon*L boundary error is not local o(l) error at a fixed
microscopic l. The candidate correctly leaves routing, boundary changes,
extra coarse constraints, stratum approximation and full profile
recovery as unresolved work. No annulus, CUT or remainder-padding
claim is borrowed to close those gaps. No novelty is established.

## 7. Sources, independence and integrity

Accepted fixedD structural Sections 1--2 supply the integer marked
dictionary, finite local alphabet, explicit lift gradient formulas and
distributional minor identity. Their exact accepted exposition and
coordinator decision are fingerprinted. The accepted direction-coarsening
exposition and decision were read to check DC1's full-boundary section
against the local obstruction. Its asymptotic/conditional statements
are background, not a premise proving H here. The new flux, interval
and four-label calculations were reconstructed above. No new external
paper or source theorem was imported.

The complete candidate, its line-numbered second read, all saved search
artifacts and freeze were read without peer clean-strata findings.
The separate remainder-padding candidate was also read as an independent
next assignment; none of its claims is used here. The current candidate,
accepted background and all nine earlier own packets are validated by
the companion one-time metadata freeze. Only the assigned review prefix
is written. No candidate/shared edit, Git action, spawning, paid API,
contact, access bypass or PDF redistribution occurred. Fresh authoritative
weekly telemetry at this group transition returned 21% total used,
10080-minute window, reset1792745187, below the 90%-total ceiling with
integration reserve. The coordinator retains all promotion authority.
