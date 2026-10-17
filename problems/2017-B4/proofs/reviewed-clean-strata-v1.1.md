# Reviewed clean-strata partial results

**Proved, independently reviewed partial results FL1, CL1, OB1**,
accepted exposition v1.1, 2026-10-17 UTC. BOTH fresh initially blind
nonconstructor whole auditors reconstructed every substantive inference.
The coordinator read both full reports, issue ledgers and source records,
verified the frozen hashes and found no unresolved substantive objection.
No mathematical repair was required. Only this acceptance header is new;
the frozen candidate body below is unchanged. Historical unverified labels
are superseded only within this scope.

FL1 is a boundary-flux and rare-tile COUNT estimate. CL1 is a boundary-preserving tiling bijection only when EVERY within-consecutive-group tile count is ZERO. OB1 is the exact four-label prescribed-boundary obstruction: one fine class, two coarse weak-lens classes and one erased internal crossing, with only one coarse class liftable.

Retain O(epsilon L²+L+1) at finite scales. Discarding fixed-side-l cells meeting rare tiles costs O(l²(epsilon L²+L+1)); its boundary term cannot be dropped in joint limits. The rare-tile estimate gives no thin location band. OB1 does not refute global DC1 surjectivity or clean CL1; it blocks arbitrary local reinsertion after even one forbidden event. The discovery search was not a proof premise; both audits reconstructed the exact example by hand.

No full2017 solution, H, PR, EAI or novelty is claimed. See
../reviews/clean-strata-acceptance.md and its exact JSON/integrity records.

---

# Rare tile flux, clean coarsening, and a local lifting obstruction

2026-10-17 UTC. **Candidate proofs - unverified.** Constructor: coordinator.
Two fresh independent nonconstructor whole audits are required. No H,
EAI, PR or full2017 solution is claimed. A short targeted counterexample
search was used to locate OB1, followed by the complete hand derivation
below; no finite absence result is used as proof.

## FL1: local affine closeness controls zero-minor tile density

Fix integer v_i=(1,i-1), D, and the canonical affine-on-tiles lift a of
an actual tiling. Its coordinate gradients are bounded by G_D. Let
Omega be a Jordan Lipschitz window of diameter O(L), perimeter <=C L.
Let b(x)=Jx+c, with fixed bounded J, and suppose on the whole boundary

    ||a-b||_infinity<=epsilon L.

For each i<j, Green's identity and integration by parts on the closed
boundary give exactly

    integral_Omega(det(grad a_i,grad a_j)-det(J_i,J_j))
      = integral_boundary ((a_i-b_i) da_j -(a_j-b_j) db_i).

Indeed integral a_i da_j-b_i db_j equals integral e_i da_j+b_i de_j,
and integral b_i de_j=-integral e_j db_i. Both a and b are Lipschitz;
the identity holds by the usual weak Green formula, or by piecewise
smooth approximation. The bound on boundary error and total variations
therefore gives absolute discrepancy at most

    C (G_D+||J||) epsilon L^2.

On a whole ij tile the integral of this ij minor is1, and it is zero
on all other types. For a window cut through tiles, the integral gives
the nonnegative sum of the ij tile area fractions. The number of tiles
meeting its boundary is O_D(C L+1): each lies in a bounded-width tube
about a rectifiable curve of length <=C L, and the finite integer-origin
tile alphabet gives a bounded number of possible tiles per unit cell.
Consequently the number of whole or intersecting ij tiles differs from
the integral by O_D,C(L+1).

If det(J_i,J_j)=0, the number of ij tiles intersecting Omega is thus
O_D,C,J(epsilon L^2+L). This applies to all within-group pairs for
parallel rows and all pairs involving a zero row. It is a tile-count
bound, not a theorem that these few tiles lie in a thin boundary band.
They may be distributed across the whole window.

## CL1: exact zero-loss coarsening when forbidden crossings are absent

Let p<=q be comparable ranked D-color words with fixed content and let
their physical boundaries form a Jordan lens in the integer projection.
Partition the colors into consecutive nonempty groups G_1,...,G_s.
Assume the lens has a tiling with NO ij tile when i,j belong to the same
group. Equivalently Inv(q) minus Inv(p) contains no such pair: the number
of those tile events is fixed by the boundary, independently of the
tiling. Zero-count colors can be omitted.

Let r_g be the ordered sequence of fine ranked labels in the restriction
of p to G_g. It is the same sequence in q. Delete fine color names in
each group and call its kth occurrence coarse label(g,k). Replace each
coarse label in any coarse word by the kth label of r_g.

**CL1.** This is an order isomorphism of intervals

    [p,q] <--> [coarse(p),coarse(q)].

It induces a bijection on tilings, with the original fine boundary kept
exactly after lifting. Thus ANY coarse replacement tiling of that exact
coarse lens lifts when the no-within-group-crossing condition holds.

For proof, every fine word in [p,q] has all within-group comparisons
fixed, because p and q agree on them. Hence it restricts to r_g and is
the unique expansion of its coarse word. For labels in different groups,
initial fine color order agrees with group order since groups are
consecutive. The lower and upper cross-group inversion conditions are
therefore exactly the coarse lower and upper conditions. This proves
both directions and the order isomorphism. The same comparison proves
coarse(p)<=coarse(q).

Each cover swap in either interval is between different groups, and
corresponds to the very same two fine ranked labels. Commutation of
disjoint swaps is preserved in both directions. The usual positive
word-shelling/marked-tiling dictionary therefore gives a bijection of
tilings, not merely a surjection of word paths. No internal event or
factorial assignment is hidden.

For a geometric coarse model choose any strictly ordered vectors
w_g=(1,s_g), for example rational s_g lying between the extreme original
slopes in G_g. All cross-group determinants are positive. The coarse
word interval gives a genuine positive parallelogram lens tiling. Its
boundary is Jordan as well: two comparable positive word paths with
unit horizontal steps can have the same physical vertex at a prefix
only when they have the same prefix count vector. Along an increasing
swap chain the y value at that prefix only rises, strictly whenever a
swap changes the prefix vector. Thus equality of y forces no prefix
change. Coarse prefix counts determine the fine counts through r_g,
so a common coarse vertex would give a common fine vertex. The latter
has only the two prescribed endpoints. The converse follows from the
same canonical fine heights.

The bijection needs the FULL boundary color sequences r_g, not just
the group totals. If boundaries vary, recording r_g has O_D(L) bits
for word length O(L). The assertion does not apply when even one
within-group crossing is present.

## OB1: a single deleted crossing can prevent arbitrary coarse insertion

There is an exact four-label counterexample to surjectivity of local
coarsening on tilings of an interval. Take fine colors1<2<3<4, each
once, with consecutive groups

    A={1}, B={2,3}, C={4},
    p=1 2 4 3,       q=4 3 1 2.

The only common inversion is(3,4). The new inversions are

    (2,4), (1,4), (2,3), (1,3).

All fine increasing paths MUST first cross(2,4). Then the crossings
(1,4) and(2,3) may occur in either order; they commute because their
labels are disjoint. Finally(1,3) crosses. This follows directly from
the successive words:

    1 2 4 3 -> 1 4 2 3,
    then 4 1 2 3 or 1 4 3 2,
    then 4 1 3 2 -> 4 3 1 2.

No alternative first or last cover is allowed by Inv(q). Thus the
fine lens has exactly ONE commutation class/tiling.

After merging2 and3 to B, the boundaries are

    A B C B -> C B A B.

The last coarse B edge is a common tail. The remaining ABC-to-CBA
hexagon has exactly TWO tilings, with event orders

    BC, AC, AB       and       AB, AC, BC.

The fine internal crossing(2,3) erases. Both fine swap chains project
to the first coarse tiling; the second has no fine lift preserving p,q.
A direct obstruction is its intermediate coarse word B A C B. Its
first fine B could be2, but that would put2 before1, an inversion
absent in q. If it were3, the retained inversion(3,4) would put4
before3 before1 before4, impossible. Therefore no word in [p,q]
projects to B A C B, which is a vertex path of the second coarse tiling.

Both fine and coarse geometric lenses exist by explicit positive
swap chains. The fine first and last prefixes are distinct until their
common endpoint in v_i=(1,i-1); the fine lens is Jordan. Coarsening
creates the common last B tail by collapsing the single23 tile.
The surviving hexagon is a legitimate coarse weak lens with two
fillings. Thus this is an actual prescribed-boundary lifting obstruction,
not just a failure of an arbitrary ABA projection with nonconsecutive
groups. It does not contradict global DC1 surjectivity, whose full
sorted/reversed boundary permits a fixed internal-reversal prefix.

### What the short computation did

The targeted script
coordinator-interval-lift-counterexample-search-v1.py compared projected
tile-event signatures against the complete coarse interval signature
sets, stopping at the first failure. Its test used unique fine labels,
consecutive groups and at most8 new inversions. A10-second external
timeout was set. Child PID77136 completed normally, was reaped, and
took about0.137s. It found the same example with an additional common
initial A edge and shifted labels; deleting that common prefix gives
the four-label hand proof above. The exact stdout, empty stderr, job
start and completion metadata are preserved. No larger search is needed
or claimed. The proof of OB1 is the unrestricted exact argument above,
not reliance on that program's implementation.

## Consequences and remaining gap

FL1 justifies a small entropy-loss *encoding* target for zero-minor
tiles. CL1 supplies exact insertion when those tiles are actually absent.
OB1 explains why the combination does not immediately solve strata:
deleting a small number of crossings does not guarantee every coarse
core can be put back with the old fine boundary. A valid replacement
must route rare crossings, change the boundary under a proved annulus,
or preserve sufficient extra coarse constraints.

Discarding every macroscopic cell containing a rare tile is also
invalid: low density does not prevent one rare tile in every large
cell. If cells have fixed microscopic side l, the bad-area estimate
is O(epsilon l^2 L^2), but global epsilon L affine error is not a local
o(l) error. These orders of limits cannot be interchanged silently.
No full stratum repair, profile recovery or H follows here.
