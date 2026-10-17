# Rank-mesh R1: targeted whole-repair reaudit of v1.1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; effective settings unknown. This is a targeted
reaudit after my complete initially blind whole v1 review and the other
whole initial review froze. I did not author this repair. Both complete
original reports, issue ledgers and source records have now been read;
no peer NEW targeted reaudit findings have been read before this freeze.

I recommend closing RMR1-01/RM2-01 and editorial N1 against the full
v1.1 replacement. The revised domain and proof resolve the actual
counterexamples. No new substantive issue was found in the repair or
its affected downstream uses. This does not overwrite my original
finding, promote the packet, or supply a second review by the same actor.
Coordinator reconciliation and the other targeted audit remain required.

## Exact version, read scope and independence

Read the complete full replacement, complete repair ledger, saved diff,
worklog and source JSON:

- main `rank-mesh-reasoning-r1-candidate-v1.1.md`, SHA-256
  `f6c1681ae288b37d2e845e31ca1ef4503d659c9669ec6801266f3564de771ee3`;
- repair `rank-mesh-reasoning-r1-repair-v1.1.md`, SHA-256
  `f9d637f76ee320d022dd481b836b04b584cf392bc5acf130106326701c94767d`;
- freeze-v1.1 manifest, SHA-256
  `0273dd67122b549dbf7b9cf6dab57f6671aab52ed793e942524c1bd69718bb14`.

The complete UR3 supplement was reread, not inferred only from its hash.
It is byte-identical at SHA-256
`40ad9b252b6c34f5dee5c8cd3eedea8e8feeabb0cec1497b224bf5c32ba58aab`.
The original v1, its false auxiliary consequence, both original reviews
and all earlier records are preserved. The administrative freeze checks
the eight repair artifacts, declared inputs and both original manifests.

The separately constructed uniform-strict packet is not a premise of
this reaudit or this rank-mesh proof. My roles as its constructor and as
this repair's reviewer are distinct. No proof or bound from that new
unverified construction is used here. No mathematical program, CAS,
enumerator, candidate/shared edit or Git command was used.

## The substantive v1 error and both retained counterexamples

The old sentence asserted O_D(rL+r^2) boundary-face loss from perimeter
O(L) alone for a rectifiable window. A connected perforated window can
have many tiny boundary components; perimeter does not pay one tube
initialization cost per component. The error was mathematical, not just
stylistic, and connectedness of the region alone would not repair it.

Both original examples are correctly preserved in the author ledger.
My example uses the forced D2 (1,0),(1,1) full grid, even L, r=2,
Theta(L^2) selected cells and one circular hole of radius L^-3 in each
retained odd/odd tile. Hole boundaries avoid selected curves, their total
length is O(1/L), and the original outer perimeter is
2L(1+sqrt(2)). Thus boundary-cell discarding loses Theta(L^2) residual
tiles despite perimeter O(L). This refutes the literal v1 bound.

The other initial reviewer strengthens it by keeping every lost retained
tile fully inside the window. For a selected cell

    2s-1/2<a1<2s+3/2, 2t-1/2<a2<2t+3/2,

the retained tile is [2s,2s+1] times [2t,2t+1]. A radius1/(10N)
physical hole centered at rank (2s+5/4,2t+1/2) lies in a skeleton tile,
strictly inside this selected cell and away from that whole retained tile
for large N. A quadratic number of these disjoint separated holes gives
total perimeter O(N) but loses Theta(N^2) fully retained tiles under
the boundary-face rule. This rules out silently repairing the theorem
by counting only fully contained retained tiles.

These are finite analytic families on actual full tilings, not samples
from a search. Their windows are connected but have many boundary
components. They are outside the repaired one-Jordan-boundary domain,
and the author does not recast either as a counterexample to H.

## Reconstructing the complete repaired tube and tile-loss argument

The revised RM1a explicitly requires W to be the bounded interior of
ONE rectifiable Jordan curve gamma, with length P. It discards every
selected face whose CLOSURE meets that curve. This includes contacts at
vertices and does not assume transversality.

By the unchanged RM1 bound, a selected face has diameter at most
r sum_i||v_i||. The same bound holds for its closure by continuity.
Every whole retained tile assigned to that face lies in its closure.
If p lies in the closure's intersection with gamma, every point of
each such tile is therefore within rho=C_D r of p, and hence belongs
to the rho-neighborhood of gamma. Skeleton tiles are already charged
separately; counting the remaining tiles is the required extra loss.

A rectifiable Jordan curve admits an arclength parametrization of
length P. Sample it at arclength gaps at most rho. There are at most
ceil(P/rho)+1 sample points, with harmless duplication of the endpoint.
Every curve point is within Euclidean distance rho of a sample, since
chord distance is at most intervening arclength. Every point of its
rho-tube is consequently within 2rho of some sample. Thus

    area(tube_rho(gamma))
       <=4pi rho^2(ceil(P/rho)+1)
       <=4pi rho P+8pi rho^2
       =O_D(rP+r^2).

This includes P<rho, where the r^2 term is necessary. No regularity
beyond rectifiability or uniform smoothness of the curve is presumed.
Its many folds, close approaches or thin interior necks cause overlaps
of covering disks and cannot increase this upper bound.

Every original tile has area det(v_i,v_j)=j-i>=1. Their interiors
are disjoint. Since the ENTIRE lost tile is in this tube, its tile
count is no greater than the tube's area. This proves the exact
additional whole-tile loss O_D(rP+r^2), without an independent
coordinate count or a hidden per-cell factor. At fixed r and P=O(L),
normalization by L^2 gives O(r/L+r^2/L^2), which tends to zero.

For M separately specified Jordan windows, the proof applies to each
curve and gives the union loss at most

    O_D(r sum_(j=1)^M P_j+M r^2).

The repair states this sum explicitly, without assuming M is uniformly
bounded or that the sum is automatically lower order. If the windows
or r vary, the actual expression has to be checked against the chosen
scale. Overlap can only reduce the union. No arbitrary perforated-window
or global window-assembly theorem is asserted by this finite-list bound.

## Every affected main-candidate use

The saved diff and full replacement agree on the repair's scope:

- RM1a's whole auxiliary paragraph has been replaced by the explicit
  Jordan hypothesis, the arclength-cover proof and the actual finite-list
  sum. The old perimeter-only implication survives only as a diagnosed
  historical error in the repair ledger and original frozen v1.
- RM2's instruction to discard faces touching the original outer boundary
  now explicitly uses the full genuine two-dimensional zonogon's one
  rectifiable Jordan polygon. Its perimeter is
  2 sum_i N_i||v_i||<=2cL sum_i||v_i||=O_D,c(L), so the repaired
  helper applies. Zero-content colors within a genuine two-dimensional
  instance are harmless; no one-direction segment is introduced as a
  Jordan disk by this repair.
- The final limitations explicitly retain the Jordan domain and charge
  r sum P_j+M r^2 over the actual chosen windows before any limit.
  They do not infer the missing macro-window, rare-count, orientation or
  global recovery interfaces from the corrected local helper.

I also checked the earlier fixed-domain encoding paragraph. Its domain
comes with an actual finite reference filling of K tiles. Such a filling
bounds both perimeter and number of boundary components by O_D(K), and
the origins are conditioned on first. This already pays the component
cost; it is not the false perimeter-only window assertion in disguise.
It remains unchanged and compatible with the repair.

N1 is corrected from six tile types to binom(D,2) in the general fixed-D
RM1a paragraph. For D4 this is six; for other fixed D the finite alphabet
and constants are still D-dependent. No new geometric or counting
claim is introduced by the editorial correction.

## Unchanged RM1/RM2/RM3 and full UR3 affected-scope check

The full replacement retains the biconnected whole-tile disk construction,
no-hole selected-arc escape, two-port residual chains and aggregate
perimeter 2n_F; it does not replace them by arbitrary curve cells.
Skeleton/rare-face coding, all INCIDENT forbidden-tile exclusions,
the special D4 one-merged-pair/two-singleton lifting restriction,
zero-row and separate two-group endpoint, active-curve exterior and
small-block/large-block aggregation have not been broadened.

In RM3 each resulting coarse block is itself a Jordan tile disk with
the actual small-zonogon fixed exterior. The error aggregation uses
its aggregate perimeter and isoperimetry, not the repaired arbitrary
window helper. There is still no unproved estimate for S hidden in the
code, and no multi-nonsingleton lifting theorem has appeared.

The unchanged UR3 class EXPLICITLY requires each B_j to be a Jordan
disk with perimeter <=C0 r_j and one fixed small-zonogon exterior for
all fillings. Therefore its boundary-triangle discard has the same
single-curve proof just checked: a triangle of side ell_j touching
the boundary lies in a C ell_j-tube of that one curve. Its area is
O_C0(ell_j r_j+ell_j^2)=O_C0(lambda r_j^2+ell_j^2) at the specified
scale. Varying thin necks or non-Jordan LIMIT boundaries do not change
the fact that every finite B_j has one rectifiable boundary. The
repaired hypothesis therefore already holds at every applied scale.

The triangle cores Q_j,t and the LC3 lattice regions are also expressly
Jordan and contained between a fixed triangle and its inset. Their
fixed-width missing strip and common reference exterior have the
separate direct construction in the supplement. The repair changes
none of the source's approximation metrics, quantitative extraction,
admissible affine slopes, fixed exterior, normalization or limit order.
Both initial whole reports had already reconstructed LC3 using the
complete relevant CKP primary statements/proofs and lozenge passage.
This topology repair creates no new missing-LC3 condition. I retain
my initial analytic findings rather than treating the corrected helper
as a new entropy theorem.

## Disposition and preservation

RMR1-01 and RM2-01 are resolved in the explicit v1.1 domain. N1 is
resolved. No further substantive repair is requested from this targeted
reaudit. I recommend coordinator acceptance of the repaired scoped
rank-mesh/UR3 package only after the other targeted audit and full
reconciliation. No H, PR, all-D extension, full 2017 limit or novelty
is established by this recommendation.

My original complete report and its issue ledger remain unchanged;
the original finding was valid and the old claim remains false.
The other original whole report and its distinct counterexample are
also preserved. The freeze rechecks all 26 earlier own frozen packets,
including unrelated 2020 and uniform-strict work. No new peer targeted
findings were read before this report froze. No mathematical program,
CAS, enumeration, source download, candidate/shared edit, Git or
spawning occurred. Account-wide weekly total:27%, reset1792745187,
with90%-total cutoff and integration reserve.
