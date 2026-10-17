# One clean consecutive-pair reduction in any fixed dimension

**Candidate proof - unverified**, coordinator, 2026-10-17 UTC.
Two fresh initially blind nonconstructor whole audits are required.
This extends only the ONE-merged-pair argument to arbitrary fixed D.
It does not assert the simultaneous several-nonsingleton-group theorem,
uniform D-direction entropy recovery, H, PR or the official limits.
No novelty is claimed and no mathematical computation was used.

## Explicit conditional background

Use the full marked zonogon/height/de Bruijn dictionary and the precise
RM1 rank-disk construction in the separately frozen main packet
rank-mesh-reasoning-r1-candidate-v1.md, SHA-256
e0f2e55e62aabe5547120f4fc72c506c3f680844a90aa98ece7147d404178d27.
Its RM1 is stated for general fixed D. Its two whole audits reconstruct
that disk/port result, but the whole packet still awaits author repair
of an auxiliary arbitrary-window assertion. The implication below is
EXPLICITLY CONDITIONAL on RM1's exact disk/port conclusions; it uses
no arbitrary-window tube estimate and silently accepts no dependency.

In particular a full tiling has contents N_i<=cL, standard vectors
v_i=(1,i-1), selected arcs at ranks divisible by r>=2, selected faces F,
and residual biconnected Jordan tile disks C. There are at most D(r-1)
unselected full arcs meeting one F. Every residual fine arc through
a C has one chain and exactly two boundary ports. The full skeleton
and complete fine boundary heights/ranks are retained.

Fix D>=3 and k in{1,...,D-1} and merge only colors k,k+1. All other D-2
groups are singletons, in their original order. Call a tile of type
(k,k+1) forbidden. Suppose the closure of the selected face F is
disjoint from EVERY forbidden whole tile, including incident tiles
outside a chosen residual disk C. Work with an interior selected
face so its closed stars are in the original full tiled disk.

## SP1. Actual coarse disk and exactly two ports

For each residual Jordan disk C in this F, coarsening embeds its
entire closed boundary and interior as a Jordan disk Cbar in a full
(D-1)-direction tiling. Every active coarse rank curve through Cbar
has exactly two boundary ports and corresponds there to ONE original
unselected fine chain, of one fixed fine color and rank. At most
D(r-1) coarse curves meet Cbar.

Proof. Let g(i) be the coarse group index and deform the fine vectors
to w_g=(1,g-1) by

    v_i(t)=(1,t(i-1)+(1-t)(g(i)-1)), 0<=t<=1.

For t>0 all ordered determinants are strictly positive. The map
x -> V_t a(x) on the actual full tiling is affine and positively
oriented on every tile. Its boundary goes once around its convex
zonogon. Boundary degree and local cyclic fan order show it is a
homeomorphism: every regular interior point has exactly one positive
preimage, and an edge/vertex multiplicity would persist at a nearby
regular point. The original boundary is injective in cyclic order.

Let F0 be its uniform limit at t=0. Every fiber is connected.
Indeed let e_t=sup|F_t-F0|. The inverse image under the homeomorphism
F_t of Z_t intersect closed_ball(y,2e_t) is compact and connected,
contains F0^(-1)(y), and every Hausdorff subsequential limit is
contained in that fiber by uniform convergence. Since the fiber is
contained in each such set, the limit is exactly the fiber. If
e_t=0 at some t>0, the assertion follows from the homeomorphism itself.

Every point of the closed C has a full forbidden-free neighborhood
by the closed-face hypothesis. Its incident positive tile faces
remain positive under F0. Two distinct outgoing fine rays could
coalesce only if an intervening fan sector were a within-pair tile;
that sector is excluded. Thus F0 is a local homeomorphism near each
point of C. Its fiber there has an isolated point. A connected
fiber with an isolated point is a singleton, so F0 is injective on
the whole C, including its vertices. Compactness makes it an embedding.

The positive limiting faces fill the coarse zonogon without overlap:
an open overlap would persist at t>0, and surjectivity follows by
compact preimage limits. A collapsed face cannot enter a positive
face interior, again by persistence. Integer vertices and unit
horizontal edge displacement exclude a partial-edge subdivision.
Hence these are a genuine full coarse tiling and the actual Jordan
disk Cbar, not an abstract map of a wiring picture.

For a singleton coarse curve, the fine identity is globally unchanged;
RM1 already gives its single chain and two ports on C.
For a merged-group coarse curve, fine identity can change only at
a deleted forbidden tile. None meets the closed F. During any visit
to F it therefore follows a single fine chain. It cannot leave F
through a selected barrier of that same merged group: meeting a
different fine color in that group would be a forbidden event,
and meeting its own fine color is impossible. Any departure crosses
a selected SINGLETON barrier.

Suppose it later returns to the same F. The original selected-face
sign of that very singleton barrier must be restored. That barrier
is the same entire coarse rank curve, since its group is singleton.
Restoring its sign requires a second crossing, impossible for the
full coarse de Bruijn arrangement. It follows that this merged
curve has at most one visit through F, with constant fine identity.
The retained portion belongs to one RM1 block and has its two ports.
This reasoning does not use that the number of singleton groups
is exactly two; any D-2 singleton groups work. It DOES use that
there is only one nonsingleton group.

Distinct active coarse curves give distinct unselected fine chains
in F. The RM1 bound consequently gives at most D(r-1) active curves.
This proves SP1. The restriction to closed incident cleanliness and
one merged pair is retained, not inferred from few total defects.

## SP2. Exact complete-boundary lifting, also after dilation

Every coarse filling of Cbar with its same complete boundary lifts
to a fine filling of C with its original boundary and ranks. This
is a count bijection, and remains a bijection after every positive
integer dilation M. In particular

    Z_fine(C)=Z_coarse(Cbar),
    Z_fine(MC)=Z_coarse(M Cbar).

Proof. Glue a proposed coarse filling to the unchanged full coarse
exterior. The complete boundary height fixes every active coarse
rank at its ports. SP1 gives precisely two such ports in the
reference, hence also in every replacement. A new internal coarse
track with no port would have to be closed, impossible in the full
arrangement. Thus each active level is one chain joining its two
prescribed ports. They carry the same original fine color and rank
in the reference, so label the whole replacement chain accordingly.

Each coarse face crosses two DIFFERENT groups. Its two assigned
fine colors are therefore distinct and in the original cyclic order,
so their fine vectors have positive determinant. Assigned edge
increments close around each face. Simple connectivity of the disk
makes their integral independent of path. Its boundary increments
are exactly the original fine boundary increments; fix its starting
height and physical point there. Positive face orientation and the
original Jordan boundary's degree one give an actual fine tiling.
Every original fine rank is recovered, not freely permuted.

Coarsening this fine filling returns the chosen coarse filling,
which proves injectivity. Conversely the fine boundary integral
of det(grad a_k,grad a_(k+1)) is0 in the clean reference. On
every possible fine tile its contribution is1 for the forbidden
pair and0 otherwise. Green's formula with the same complete
boundary therefore forces every fine filling to have no forbidden
tiles. Coarsening those fillings is the inverse of the labeled
chain construction. This proves surjectivity and whole-count equality.

For integer dilation, replace each fine reference tile by its
M-by-M uniform grid. Every boundary port is replaced by M ports
at consecutive multiplied ranks, carrying its same fine color.
Coarsening this dilated reference yields exactly the dilated coarse
reference. Each active reference coarse track still has two ports:
it is one of the prescribed parallel copies of its original track.
All boundary assignments are fixed before fillings vary. The same
recoloring/integration/degree proof applies, and the zero boundary
flux argument again excludes forbidden tiles in every fine filling.
This proves the second equality. No exact supermultiplicative
entropy inequality is inferred.

## SP3. The actual lower-dimensional exterior class

Delete every full coarse curve not meeting Cbar. Its height step
is constant on this connected disk, so deletion changes Cbar only
by a fixed translation and rank shift. The remaining full arrangement
has at most D(r-1) curves in total by SP1. It supplies one fixed
small full-zonogon exterior, to which every alternative Cbar filling
glues. Its boundary word length, diameter and perimeter are O_D(r).
Thus it is a GE_(D-1),C_D(r) disk in the dimension-induction program,
after a fixed marked direction deformation if needed. This is an
actual full-exterior property; perimeter/diameter alone would not
establish it for a ragged disk.

If UR_(D-1) were established for that exact class, SP2/SP3 would
transfer its dilation deficit to these fine clean disks. This is a
conditional application; UR_(D-1) is not assumed from a balanced
zonogon formula or from H_(D-1) alone. It is already the explicitly
reviewed target UR3 when D=4, subject to its independent acceptance.

## Scope and provenance

This is the same singleton-barrier mechanism as the earlier D4
construction, with the dimension dependence and exact active-curve
class supplied explicitly. No claim that arbitrary simultaneous
multiple merged groups work is made. The earlier erased-event
counterexample remains valid. The hypothesis is zero forbidden
events on the entire closed selected face and its incident tiles,
not just on the interior of C.

The background RM1 dependency, its pending window-scope repair,
the accepted full marked dictionary and the new all-D extension
must be distinguished in review. No extra window bound, rare-count
estimate, orientation chart, strict entropy transfer, global assembly
or general UR_D is a hidden premise or conclusion. Two fresh whole
nonconstructor audits must inspect every inference before promotion.
