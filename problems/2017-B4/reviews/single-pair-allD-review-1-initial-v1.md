# Independent whole initial audit of SP1–SP3

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`; requested
`gpt-6.1-sol` / `max`, verified effective settings unavailable.

The complete initial reconstruction below was completed without reading
another SP review or receiving its findings. I did not construct or
contribute to this all-D candidate. I previously reviewed the separate
rank-mesh packet and constructed a D4 strict-recovery candidate, but that
construction is not a premise here. No mathematical program, enumeration,
CAS, Git operation, shared-file change or subagent was used. The only
program accompanying this report fingerprints the frozen records.

**Recommendation:** no substantive defect found in SP1–SP3 with their
stated hypotheses and exact conditional RM1 dependency. This is a
recommendation to the coordinator, not promotion. In particular it proves
neither a several-merged-groups theorem nor UR_D, H, PR or the official
limit. The whole-count equalities and the small actual exterior are the
substantive conclusions audited here.

## Exact scope and dependency boundary

The candidate is `coordinator-single-pair-allD-candidate-v1.md`, SHA-256
`c0d51d61f110cf5a190344403d346940b06b95a6d1880c6c725d241c92c397b4`.
Its six-record constructor manifest has SHA-256
`2714227e14b516d260a1c9d1c8cdef5ae7b9071ea8b9b9c7140b65b6ead520db`.
I read the complete candidate and manifest, the accepted full marked
dictionary and its acceptance scope, the exact RM1 construction, the
definition of GE in the dimension program, and the UR3 class/target.
The earlier whole rank-mesh audit and targeted repair audit already read
the complete RM1 and UR3 bodies. Their prior files remain unchanged.

The fine directions are the fixed ordered integer vectors
v_i=(1,i−1). There is exactly one merged pair k,k+1, with
1<=k<=D−1 and D>=3. All other groups are singleton. C is one residual
biconnected Jordan tile disk inside an interior selected face F. The
closure of F, including all incident outside tiles, avoids every
forbidden (k,k+1) tile. This is stronger than the absence of forbidden
tiles merely in the interior of C. The full selected skeleton and
complete original heights/ranks are retained.

The exact RM1 conclusions are an explicit conditional premise: at most
n_F<=D(r−1) unselected full fine arcs meet F; each nonempty residual
chain has two ports and lies in one biconnected block; C really is a
Jordan disk. The historical auxiliary arbitrary-window assertion in the
frozen main v1 is not used. Its later repair does not need to be silently
imported to make this conditional implication meaningful. SP's claimed
conclusions can be checked under precisely these premises.

## SP1: actual coarsening and the no-return assertion

For t>0 the interpolated directions retain their strict order. On each
fine tile the affine height map F_t has positive determinant. Its
boundary maps once and injectively around the corresponding convex
zonogon. A regular interior image point consequently has degree one
and exactly one positive tile-interior preimage. An edge or vertex
identification would persist on adjacent open sectors; the cyclic fan
order supplies the same local orientation. Hence F_t is a homeomorphism
of the entire disks, not just an abstract wiring equivalence.

I checked the connected-fiber argument because a uniform limit of
homeomorphisms must not be assumed injective. For y in the limiting
zonogon let e_t be the uniform error. The preimage of
Z_t intersect closed B(y,2e_t) is compact and connected, since this
intersection is convex. It contains every point of F_0^{-1}(y).
Any Hausdorff limiting point x satisfies |F_0(x)−y|<=3e_t and therefore
belongs to that fiber. Conversely the whole fiber belongs to every
such compact set, so every Hausdorff subsequential limit is exactly the
fiber. Compactness and connectedness pass to that limit. If e_t=0 for
a positive t, F_0 itself is that homeomorphism. This proves connected
fibers, including fibers that contain collapsed forbidden faces.

Every point of closed C has a full forbidden-free neighborhood in the
original full tiled disk. The interior-face and incident-tile hypotheses
are used here, especially at a boundary vertex. Every incident face
there stays positive. Two distinct outgoing rays can coincide after
merging only if the intermediate angular sector is a forbidden pair
tile. There is no such sector. Positive and negative rays cannot
coincide because their horizontal coordinates have opposite signs.
The resulting local cyclic fan still fills one full neighborhood with
degree one. Thus F_0 is a local homeomorphism at every point of C.
A fiber meeting C has an isolated point; a connected fiber with an
isolated point is a singleton. This also rules out a remote collapsed
piece identifying with a vertex of C. Compactness gives an embedding
of the entire closed disk and its Jordan boundary.

The limiting positive faces have disjoint interiors, since an open
overlap would persist before the limit. Every point of the limiting
zonogon has a limiting preimage, so these faces and the collapsed faces
cover it. A collapsed face cannot enter a positive face's interior:
a sufficiently small neighborhood in that positive face would persist
under F_t and would overlap a nearby point of the other tile. The
surviving edge vectors all have horizontal displacement one and integer
vertices. An integer vertex cannot sit strictly inside one such edge.
There is consequently no partial-edge subdivision or T junction. This
is a genuine full coarse marked tiling. Any zero-content nominal
direction is harmless; a nonempty clean tile disk itself supplies two
different active coarse groups. If the only two active fine colors
were exactly the merged pair, no nonempty clean C would exist.

The singleton coarse tracks have unchanged fine identity. For the
merged group, fine identity can change only at a deleted forbidden
crossing. During a visit to F there is no such crossing. A departure
cannot cross a selected barrier from the same group: an equal fine
color cannot cross, and the other member of the pair would give a
forbidden tile meeting closed F. Hence it crosses a selected singleton
barrier. That barrier is the same full coarse rank curve: the singleton
height coordinate and its half-integer level have not been merged.
Returning to F must restore its separating sign, which requires a
second crossing of that same full coarse track. Distinct full coarse
tracks meet at most once. A merged track therefore visits F at most
once, with one fixed fine color and rank.

This proof uses no upper bound of two on the number of singleton
groups. Any of D−2 singleton groups can supply the barrier. It does
use that there is only one nonsingleton group, so a barrier from an
unrelated merged group cannot be substituted. The exterior route and
an escape through the original outer boundary are also excluded by
the interior-F hypothesis. A curve meets a boundary edge at its
midpoint, not at a tile vertex; boundary tangency is not an extra visit.

During this single visit the unselected fine arc has its RM1 consecutive
chain. Consecutive tile cycles share opposite edges and hence lie in
one biconnected block. Thus an active coarse curve through Cbar has
one chain and exactly two ports. Distinct coarse curves correspond to
distinct such fine chains. The active count is at most n_F<=D(r−1).
This handles block pinches without treating their union as one disk.

## SP2: every filling, exact inverse and integer dilation

Glue any complete-boundary coarse replacement to the fixed actual full
coarse exterior. Its complete coarse height fixes the two boundary
ports at every active rank. An extra internal component of a rank
level would be a closed full de Bruijn track, which is impossible.
Every active level is therefore a single chain between its prescribed
pair of ports. Those two ports have the same original fine color and
rank by SP1; assign that identity to the entire replacement chain.
The ranks of tracks are fixed by boundary labels and their
noncrossing order, not freely permuted in a new filling.

Every replacement tile crosses two different coarse groups. The two
assigned fine colors are distinct and occur in the original strict
order. Its opposite edges belong to the same two tracks. Assigning
the fine elementary height increments therefore gives a closed cocycle
around every tile. Simple connectivity of Cbar makes its integral
path independent. Along its boundary the fine increments are exactly
the original boundary increments. Fixing one original height and point
recovers the full original fine boundary, including its ranks.
Each lifted face is a positive fine parallelogram. Boundary degree one,
together with the preserved cyclic fan order, makes the result an
actual fine tiling of C rather than an overlapping map. Coarsening it
returns the chosen coarse replacement.

The converse is essential for equality of whole counts. For the
original fine lift the Green boundary integral of the (k,k+1) minor
is zero, because the clean reference contains no such tile. For any
other fine filling of the same complete boundary the integral is the
same. On one (k,k+1) tile the minor is the inverse physical determinant
and its area is that determinant, so its integral is exactly one.
Every other tile contributes zero. The integral is thus precisely the
nonnegative number of forbidden tiles, which must vanish. Coarsening
every fine replacement is legitimate. Applying the fixed boundary-label
construction recovers the same fine replacement, giving the inverse.
Both maps preserve whole complete-boundary counts; this is stronger
than merely exhibiting one lift or an injection.

For integer M>=1, the uniform M-by-M reference grid on each enlarged
tile matches across shared edges and gives an actual reference filling
of MC. The coarsened lift is exactly M times the original coarsened
reference. Each original boundary edge is repeated M times. Each
original active half-integer rank interval produces exactly M parallel
sublevels with its same two port locations and fine color; their
consecutive fine ranks are fixed at both ports. No other rank interval
can acquire a port, since the boundary coordinate extrema were already
integer. The original disk need not be reconstructed as a new
rank-mesh block at scale M: the proof uses these fixed dilated port
data. The recoloring/cocycle/degree argument applies with those data,
and the zero Green integral still excludes forbidden tiles from every
fine filling. Consequently both displayed count equalities hold for
every positive integer M. No finite supermultiplicativity or entropy
continuity has been inferred.

## SP3: deletion gives the actual GE class

A full coarse track disjoint from closed Cbar has its height step
constant on that connected disk. Deleting that track translates the
disk by one fixed vector and shifts its ranks by constants. It removes
no tile of Cbar. Repeating for every inactive track leaves an actual
full marked arrangement containing Cbar, with at most D(r−1) tracks
in total. This is the usual marked deletion operation, applied to a
globally given arrangement; no arbitrary wiring window is declared
extendable. Its full zonogon has at most twice this many boundary
edges. Fixed directions give O_D(r) perimeter and diameter.

Every alternative Cbar filling already glues to the same original full
coarse exterior. The deletion of inactive tracks is outside the disk,
and cannot create a new internal inactive rank component: that would
be a closed full track. Hence the reduced exterior is the same for
all alternatives. Cbar has complete boundary and perimeter at most
2D(r−1) edge lengths by its active two-port description. It therefore
belongs to the stated GE_(D−1),C_D(r) class. A fixed marked direction
deformation retains this actual disk/exterior property if standard
lower-dimensional directions are requested. Perimeter or diameter
alone would not have been enough, and that inference is not made.

The final application is expressly conditional on UR_(D−1) for this
exact arbitrary complete-boundary GE class. Balanced full-zonogon
entropy does not supply it. The D=3 endpoint is compatible with the
two-direction unique-grid situation; the D=4 endpoint is the separately
stated UR3 target, whose independent acceptance is not assumed here.
No all-D recovery is a conclusion of SP1–SP3.

## Adversarial checks and disposition

I specifically tried: an outside coarse shortcut returning through a
different fine identity; a rank reconnection in a replacement; a
remote collapsed fiber identifying a clean vertex; a chain passing
between different pinched blocks; extra closed or tangent rank curves;
failure of the M-copy port matching; deletion of an inactive track
altering the disk; endpoint merged pairs; absent nominal colors; and
the D=3 lower-dimensional endpoint. The written strong hypotheses
exclude the shortcut and collapse cases, exact two-port levels exclude
the reconnections, and the remaining arguments above cover the other
cases. Replacing closed incident cleanliness by interior cleanliness,
or allowing another nonsingleton group, would remove steps of this
proof; neither weakening is asserted.

All 25 claim-level checks in the separate issue ledger pass in the
stated scope. There is no requested author repair. The result remains
candidate-unverified pending the other independent whole audit and the
coordinator's full dependency/integrity reconciliation. This report
does not promote the conditional RM1 premise or any UR theorem.
