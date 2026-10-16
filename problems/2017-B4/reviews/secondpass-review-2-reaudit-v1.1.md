# R2 targeted independent re-audit of the 2017 B4 v1.1 repairs

**Targeted re-audit completed before seeing the other re-audit. No coordinator promotion.**

Reviewer: `/root/review_2017_secondpass_r2`. Local date: 2026-10-17 Australia/Brisbane; UTC work date: 2026-10-16. This continues my frozen independent initial report, SHA-256 `1780d421be9d46158f02428ab4a46e0504f3fd3733e31c6e37a398c35cd32012`, without modifying it. I did not construct or repair these candidates. Both initial reports were already frozen before the author repair; initial conclusions were then available. I have **not read the other reviewer's v1.1 re-audit or conclusions** before freezing this report. The author's repair map identifies original issue IDs; that is not treated as evidence of reviewer acceptance.

Requested launch settings remain `gpt-6.1-sol` / `max`; no effective-setting readback is available. Authoritative account-wide telemetry at 2026-10-16 16:01:52 UTC returned **10% total weekly used**, reset timestamp `1792745187`, window length 10080 minutes. The 90% total-used cutoff and reserve remain in force. No paid API was used.

My new tracked writes are only `reviews/secondpass-review-2-reaudit*`. I did not edit the candidates, shared issues/status, sources, old reviews, or original computations, and did not commit, push, or promote any result.

## 1. Exact re-audit scope and input verification

I read the **full revised packets**, their exact diffs, `author-repair-changelog-v1.1.md`, `author-repair-manifest-v1.1.json`, `author-repair-sources-v1.1.json`, and `author-repair-checkpoint-v1.1.json`. The requested packet fingerprints matched:

| Revised packet | SHA-256 |
|---|---|
| `author-repair-macmahon-candidate-v1.1.md` | `a225f0042fc098d8a827093a3e680612848caf392db64cad24339d399769bcf0` |
| `author-repair-boundary-fiber-candidate-v1.1.md` | `e2891eafc6fa8449f6c70c817c2e21416a43f1893120929df02f2aa2dac86a8b` |
| `author-repair-periodic-grid-candidate-v1.1.md` | `1a6acb042e1e21bc0992cddbd7188c47e81249b5888faabaa4e73a45be0f5c6e` |

Paths are relative to `problems/2017-B4/` unless stated otherwise. A separate R2 program independently regenerated all three unified diffs with four context lines and obtained byte-for-byte equality. It checked all 17 preserved-input hashes in the author's manifest, all source PDF/image fingerprints, and all files listed in the author's checkpoint. It checksummed the other **initial** report only; no other re-audit was opened.

The M1 and M3 mathematical sections are byte-identical to v1. Their full analytic and inductive reconstruction in my initial review therefore carries forward; there is no new enumeration or new hypothesis concealed in those sections. Q(3,3) is the same exact finite input independently reproduced in my initial run. The new mathematical review focuses on the actual revised geometry/topology, not on the author's claim that a repair should work.

## 2. Verdict and issue disposition

**The actual v1.1 repairs resolve my substantive objection and the precision requests. I find no unresolved mathematical objection in the re-audited scope.** This is R2's recommendation for these exact bytes; only the coordinator can combine the independent audits and promote a result.

| Claim / previous point | R2 v1.1 disposition |
|---|---|
| M1 and M3 | Initial mathematical verdict retained; mathematical sections unchanged. |
| M2 full ternary scope | Accepted clarification: full ternary singleton trees exist only for odd n; the even-n family is empty; this remains an upper-counting model. |
| R2-F1-1: empty slots, facial walks, Jordan disk | Resolved by the revised explicit construction, checked below. |
| R2-F2-1: precise signotope theorem | Resolved by Felsner--Weil Theorems 7--8 with the correct simple marked/fixed-order convention. |
| R2-F3-1: proper ports / empty factor | Resolved: two distinct transverse boundary ports, no tangencies/boundary segments, F(empty)=1, and F1 restricted to m>=1. |
| R2-G1-1: unresolved raw remainder grid | Resolved: nonnegative superadditivity, with zero remainders omitted, replaces that instruction. |
| **R2-G2-1: uncovered fourfold crossings** | **Resolved for this v1.1:** all uncovered multicrossings receive one fixed simple resolution before completion. Simultaneous separation, pair preservation, recoverability, and the unchanged exponent check out. |

The exact official liminf and limsup remain undetermined here. G1 concerns four fixed directions only. G2 remains a reproducible lower certificate near 0.190006, weaker than the attributed published 0.2721 result; no new best-bound or novelty claim is accepted.

## 3. Critical G2 repair: independent mathematical audit

### 3.1 Large supports can be made genuinely disjoint

The selected cells are translates by (3i,3j) of [1/10,31/10] x [1/5,16/5]. Their closures lie inside the central diamond. Original grid vertices have either both coordinates integral or both half-integral. The vertical/horizontal tiling edges have fractional coordinates 1/10 and 1/5; neither type of grid vertex is on them. The original corner coordinates also avoid every grid line. Thus a sufficiently small inward collar and corner rounding preserve the full labelled pairing and every original crossing in a retained cell. They separate adjacent closed supports.

This is a choice of convex or slightly rounded convex support, so every participating original line still cuts it in one proper arc. The collar can be chosen to avoid not just vertices but corner tangencies and all port collisions. The grid has only finitely many periodic edge/corner event types, so a fixed sufficiently small collar works; the author's weaker finite-m choice also suffices. No inside grid vertex is released into an interior corridor. Therefore every retained support still has exactly the Q(3,3) boundary type and nine original fourfold points.

Cells intersecting the diamond but not retained lie in a constant-width boundary band. The area loss and number of discarded cells are O(m), while the diamond area is m^2/2-O(m). Hence K_m=m^2/18-O(m) remains valid after making supports disjoint. The shrinking does not alter this count.

All raw triple points outside the diamond receive the counted three-strand disks. Those disks can be chosen after the large supports, avoiding their closed supports and every nonincident line. They do not interfere with retained cells. There are still exactly t3=(m^2-1)/2 of them.

### 3.2 R_m covers the missing vertices, including both examples

The revised definition takes **every** original multicrossing outside the large supports and counted triple disks. It explicitly includes corridor points, so no unlisted residual case is assumed away. In the stated support choice, these are the uncovered fourfold points in the boundary band. The points (0,t) and (t,0), for t>=1, are fourfold original vertices on the central diamond's boundary, lie in no retained interior support, and are not triple points; v1.1 now explicitly resolves them.

An independent way to check the asserted size is

\[
|R_m|=t_4-9K_m
=\frac{m^2+1}{2}-9K_m=O(m).
\]

All original triples are already covered, and each retained support retains its nine fourfold vertices. This also confirms that the corridor modification has not silently increased the leading error.

### 3.3 Simultaneous separation is sufficient for arbitrary m

After the large supports and counted triple disks are fixed, each v in R_m is outside their closed supports and is on none of their boundaries. There are finitely many such vertices, supports, original crossing points, and original lines for a fixed m. Distances from v to a previously selected support, to any distinct original crossing, and to a nonincident original line are all strictly positive.

To make the author's existence argument explicit, choose a radius less than one quarter of the minimum separation between distinct residual centers, and less than one half of the relevant distances to fixed supports, other original crossings, and nonincident lines. Empty minima impose no restriction. One can instead take one sufficiently small common radius for the finite set. This proves simultaneous pairwise disjointness, not just that each disk can be chosen in isolation.

All incident lines pass through the center of E_v and have distinct directions. They therefore cut its circle transversely in eight distinct ports, while no nonincident line meets the disk. The counted reroutings in other supports cannot later violate any of these separations because they stay within those supports and their boundary ports. Supports, E_v, and fixed resolutions are selected before any counted parameter is varied, as the revision requires.

No radius bound uniform in m is needed for the proof or the exponent. The finite exact checks below exhibit a uniform small radius for the checked cases only; the finite-separation argument above is the unrestricted justification.

### 3.4 Fixed resolutions restore the simple partial input

The four centered original lines are pairwise crossing, so their paired boundary endpoints alternate for each of the six pairs. One fixed complete four-strand wiring can consequently be matched to that cyclic port data. It has six distinct transverse pair crossings and no triple point. Retaining crossing-free endpoint collars ensures a proper attachment to the original straight pieces. This is a fixed resolution with exactly one selected output, not a factor of eight.

Partition each original cross-family pair by the region containing its unique original crossing. If it belongs to a counted large support, a counted triple disk, or an E_v, its alternating endpoints force exactly one crossing in that region and none elsewhere. If the original crossing lies outside all those supports, the revised text leaves it unchanged only after confirming it is simple. A same-family pair has no original crossing, and its endpoints in each affected support are nonalternating, so no replacement introduces one.

Hence every cross-family pair still crosses exactly once, every same-family pair remains noncrossing, and all multiple crossings have been resolved. Local arcs are simple and each support is disjoint, so no global strand acquires a self-crossing. This now produces the **simple partial arrangement** needed for the published tail completion. The direct pair argument is valid even though the raw starting grid is nonsimple; it does not improperly apply F3's simple-complete hypothesis to that raw grid.

### 3.5 Recovery of choices and the exponent

Fix all repair disks and their wirings. Each counted large-patch/triple choice is still placed in its own unchanged support with its original labelled boundary pairing. Restricting the final labelled local sequences to that region's assigned pair labels recovers its crossing orders. All E_v local orders are the same for every output, and cannot conceal a changed order in a different fixed slot. Thus every original counted parameter tuple survives and remains distinguishable.

The partial count is still

\[
2^{t_3}Q(3,3)^{K_m},\qquad
\log_2\text{count}\ge
\left(\frac12+\frac{\log_2Q(3,3)}{18}\right)m^2-O(m).
\]

The O(m) fixed resolutions contribute zero bits and delete no counted choices. There is no extra boundary loss and no additional amplification factor from them.

The tails remain straight outside a bounded central region. Four sufficiently distant, pairwise separated disks of radius O(m), one in a different bundle ray direction, meet all lines of their own bundle and no other-family line or support. Finite positive angular separation makes these choices possible simultaneously. This checks the hypotheses of [Cortés Kühnast et al., Section 4](https://arxiv.org/abs/2402.13107), with the simple partial input now restored.

The fixed reversal reconnection at each child remains essential: it changes the old parallel pairing by the same predetermined reversal for every child. The child arrangements are recovered from within-bundle crossing orders; deleting those crossings recovers the mixed-bundle partial orders and the counted choices. No variable boundary relabelling or reflection quotient is inserted. The factor C(m)^4 and the all-n padding argument from the initial review still apply.

For the largest odd m<=n/4, m=n/4+O(1) and 0<=n-4m<=7. M3 therefore gives the unchanged coefficient

\[
\frac{1+\log_2Q(3,3)/9}{32}\cdot\frac{1}{1-4/16}
=\frac{1+\log_2Q(3,3)/9}{24}
=0.1900060770448\ldots.
\]

**R2-G2-1 is withdrawn against the specified v1.1 bytes.** The frozen v1 still has the omission recorded in my initial report; that historical report must remain intact.

## 4. Other actual revised arguments

### G1 remainder strips

The revised proof first establishes Q>=1 using a generic minimal chord realization. For L=qa+r and H=sb+u, repeated separate superadditivity gives f(L,H)>=qs f(a,b) after dropping nonnegative remainder terms. The revision omits zero-width terms explicitly, so it invokes neither f(0,H) nor f(L,0). A positive remainder may be filled by one fixed minimal realization; no unresolved raw grid is used. The original square upper-bound argument still proves the supremum finite. This resolves R2-G1-1 and preserves only the fixed-direction joint limit claim.

### F1 connected exterior, facial walk, and actual disk

I checked each new step against the former obstruction cases. On a nonempty inside block, comparisons with outside crossings locate the same block as in A0. On an empty block, v1.1 correctly **chooses** A0's exterior gap instead of asserting that comparison data locates an empty segment. Both port vertices are retained as distinct degree-one vertices. If all crossings are inside, cuts can be put on the unbounded tails, with the outer circle taken still farther away.

Every retained strand piece reaches the outer circle, so adding the circle makes the exterior graph connected even for an empty or disconnected inside crossing graph. The graph isomorphism includes crossing labels, ordered exterior sequences, port identities, oriented rotations and the marked outer circle/outer face. These are the data needed for the connected plane-embedding classification. No two-connectivity hypothesis is required, so exterior bridges cause no missing case.

The revised argument transfers a **facial walk** and its port corners, rather than assuming a Jordan face boundary. At a degree-one port there is one incident face corner, even though its bridge edge is traversed twice by the facial walk. In A0 all such corners border the bounded face containing the former disk, so the transferred face has the full port list w in the correct orientation.

The removed arcs cannot cross the retained graph. Their endpoint germs are in that one face, so their open arcs remain there. Every connected component contains ports. A sufficiently thin closed regular neighborhood, with disjoint small port collars, is disjoint from the removed arcs away from those collars. Piecewise-linearity and finiteness make this simultaneous choice valid even for a very short empty slot: choose its two collars disjoint and retain a nonempty middle piece. The selected bounded complementary component now has one Jordan boundary and is a disk; all trimmed arcs and crossings lie in it. This handles the bridge and disconnected-network cases.

Mapping this disk and the ordered distinct ports to D preserves the inside local orders. Gluing to A0's fixed exterior reproduces all complete local sequences. Thus the revised proof still establishes F1's surjectivity, with the needed topology now explicit. R2-F1-1 is resolved.

### F2 exact theorem citation

The replacement now cites [Felsner--Weil, *Sweeps, Arrangements and Signotopes*](https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf), Theorems 7 and 8 on printed p. 15 and Theorem 7's proof on p. 19. These are exactly the primary statement/proof inspected in my initial review. The cached PDF SHA-256 is `a6995529d08034c0735b3f9b0b9a4f9dae01ac0a5f3864d88728c6d04f85c828`; its previously inspected page images also match the repair's recorded hashes.

The theorem applies to simple **marked** arrangements with a fixed line order, and characterizes their triangle signs by the monotonic four-packet condition. Consistently identifying the two signs with the bit convention is sufficient; packet reversal/global complementation preserve the predicate. The unchanged component-factorization argument then has its exact cited premise. R2-F2-1 is resolved.

### F3 ports and empty factors

The full revised definition and F3 statement now require precisely one proper simple arc per participating strand, two distinct transverse ports, and no tangencies or boundary segments. Pairwise disjoint closed disks are explicit, as is the initial arrangement's simplicity. F(empty)=1 handles empty supports; F1 itself is stated only for m>=1, so there is no artificial C(0) assertion. These are the hypotheses my initial reconstruction needed. R2-F3-1 is resolved.

### M2 parity and retained scope

The new paragraph defines a full ternary tree and identifies the odd singleton-leaf restriction. Its telescoping count, labelled-tree union and bounded-base-block extension retain the same scope. This is not an all-n lower construction or an upper bound on all C(n). No M1/M3 inference changed.

## 5. Independent checks and execution record

I did not run the author's repair builder or verification program in place. `reviews/secondpass-review-2-reaudit-check.py` is an independently written standard-library checker. Exact command from the repository root:

```text
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -u problems/2017-B4/reviews/secondpass-review-2-reaudit-check.py
```

It launched dedicated child PID **38181**, with a **20-second subprocess wall cap** and incremental flushed checkpoints. It completed in **1.336 seconds**, return code 0, on Python **3.12.14**. Parameters, command, PID, times and status are preserved in `secondpass-review-2-reaudit-check-job.json`; full stdout is in `secondpass-review-2-reaudit-check-output.txt`. No failed attempt, timeout, cap increase, or cleanup of another owner's process occurred.

Besides fingerprints/diffs, it constructs all pair intersections of the finite four-family straight grid for t=1,...,12 using exact Fraction arithmetic. It selects the stated periodic cells, shrinks each side inward by 1/100, and verifies preservation of **every** original vertex in every retained cell, including nine fourfold points per cell. It verifies all triple/fourfold formulas, that neither boundary example is covered, and that R_m is exactly the uncovered fourfold set.

For those finite instances, one radius 1/1000 suffices for the triple/fixed disks: the script checks distances to all nonincident lines and all shrunken retained supports, and verifies the checkerboard half-integer vertex lattice needed for separation from other original vertices. The smallest observed squared distance to a retained support was 121/10000 when retained supports existed. For t=1,...,5 there are no retained cells; the corresponding support-distance minimum is correctly reported as absent rather than zero. For t=12 the run had K_m=18, 312 triple points and 151 uncovered fourfold points.

These small exact checks are **finite evidence**, not a proof of the separation or O(m) statements for arbitrary m. The unrestricted arguments are in Section 3 above. The unchanged count Q(3,3)=4419734746 is carried forward from my independent initial enumeration; there was no need to rerun that enumeration. No L=4 count or higher-cap computation was attempted or inferred.

## 6. Sources, freeze, and remaining scope limits

The source fingerprints newly relied on by the repairs were checked against the actual cached bytes:

| Source | SHA-256 |
|---|---|
| Felsner--Weil author PDF | `a6995529d08034c0735b3f9b0b9a4f9dae01ac0a5f3864d88728c6d04f85c828` |
| Felsner--Weil printed p. 15 image | `3b98b63e492bb0a856fb8c30b92dad2147638482ce904c66bdd1a1c08bdaee49` |
| Felsner--Weil printed p. 19 image | `670df316662c4c3dcde28814552d23452526ef98309a6ad450d929899cf8480e` |
| Felsner--Valtr author PDF | `9f68329a62318b355cde668eabb9a05073ce755becfdd81dc5a6a15f9db68c26` |
| Cortés Kühnast et al. arXiv v2 PDF | `075dee678bceb7bddf599d1a402d37c56659bb84302765aa4c6a74b8539b0f17` |

The latter two sources' roles remain the attributed MacMahon/tiling dictionary and the simple-partial/private-tail completion hypotheses checked in my initial reconstruction. Full PDFs and source-page images remain ignored cache files. No new download, charge, or redistribution was needed.

The accompanying `secondpass-review-2-reaudit-freeze.json` seals this report, the independent checker, its job/stdout and the actual author input fingerprints. It is written before any cross-review of the v1.1 results.

**Remaining unresolved objections from R2 in this targeted scope: none.** This does not determine the official B4 rates, establish novelty, independently re-prove the stronger published bound, promote unfinished computations, or replace the other reviewer's independent re-audit. The coordinator remains responsible for integrating both audits, deciding promotion, and committing/pushing the checkpoint.
