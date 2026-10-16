# A fixed-direction patch entropy and a bounded construction certificate — candidate v1.1

**candidate proof - unverified**

Full revised version **v1.1**, 2026-10-17 (Australia/Brisbane). The revision author is `/root/owner_2017`, the original constructor of these second-pass packets. Both frozen independent initial reports were read for this author repair. All frozen v1 notes, manifests and review reports are preserved. The revised inferences require both targeted re-audits and coordinator acceptance before any promotion.

Original draft written 2026-10-16. This packet concerns one four-direction periodic boundary family. It does not establish the exact liminf or limsup of the official C(n), or their equality. Its numerical lower certificate is weaker than the attributed published 0.2721 bound and is offered as an explicit test of the gluing framework, not a new best bound. Novelty is not established.

## Definition and exact boundary data

Use the infinite straight-line grid
\[
x=i,\quad y=j,\quad y-x=k,\quad y+x=\ell,
\qquad i,j,k,\ell\in\mathbb Z.
\]
For positive integers L,H let P(L,H) be the rectangle
\([1/10,L+1/10]\times[1/5,H+1/5]\). Let w(L,H) be the full cyclic labelled endpoint pairing induced by those lines on its boundary, and put
\[
Q(L,H)=F(w(L,H)),\qquad f(L,H)=\log_2 Q(L,H),
\]
where F counts minimal disk arrangements with that fixed boundary pairing. The full pairing matters; strand and crossing counts alone are insufficient.

The chosen rational offsets avoid every crossing of the original grid and every corner tangency. In the rectangle are exactly LH fourfold integer crossings and LH simple crossings at half-integer x,y where the two diagonals meet. Thus the required number of pair crossings is 7LH. There are L vertical strands, H horizontal strands, L+H rising strands and L+H falling strands, for a total 3(L+H). The script extracts the complete boundary word by exact rational clipping, rather than assuming a shape from these scalar counts.

## Candidate G1: a limit exists for this fixed-direction patch family

Vertical subdivision at the integer translate x=L1+1/10 gives
\[
Q(L_1+L_2,H)\ge Q(L_1,H)Q(L_2,H).\tag{1}
\]
The two subrectangles have the same grid phases after integer translation. Replace their interiors independently, retaining their entire common seam data. Each pair of global strands had its unique grid crossing in one of the two regions or outside both, so boundary-preserving replacements cannot introduce a double crossing. Different local crossing orders remain distinguishable in the full boundary-labelled arrangement. A small perturbation of the common seam into a crossing-free corridor, if desired, makes this an application of the disjoint-disk gluing lemma F3.

The same argument for horizontal subdivision gives
\[
Q(L,H_1+H_2)\ge Q(L,H_1)Q(L,H_2).\tag{2}
\]
Every boundary word has a minimal realization: generic straight chords give one, so Q≥1 and f≥0. Define S4=sup_{L,H≥1} f(L,H)/(LH), allowing infinity initially. For a fixed positive block (a,b), write L=qa+r and H=sb+u, with 0≤r<a and 0≤u<b. Repeatedly apply (1)–(2) and discard their nonnegative remainder terms to obtain
\[
f(L,H)\ge qs\,f(a,b).
\]
If r=0 or u=0, omit the corresponding remainder term rather than invoking f at zero. A positive-width remainder could equivalently be filled with one fixed minimal patch of its own full boundary word; no unresolved raw grid is retained. Dividing the displayed inequality by LH yields
\[
\liminf_{\min(L,H)\to\infty}\frac{f(L,H)}{LH}
\ge\frac{f(a,b)}{ab}.
\]
Taking the supremum over (a,b), together with the defining upper bound by S4, proves that the limit equals S4, provided it is finite.

For finiteness, any boundary word on m arcs can be completed outside its disk to a complete marked arrangement on m pseudolines: choose a generic straight chord model of that boundary word, extend it to full lines, fix its outside portion, and glue each local realization into that same outside portion. Different local crossing orders remain different global crossing orders. Hence F(w)≤C(m), independently of the stronger converse in candidate F1.

For squares m=6L, so Q(L,L)≤C(6L). The established published quadratic upper bound on C gives a finite square limsup. Since the block lower inequality above applies to squares too, S4 is finite. Thus
\[
\boxed{\lim_{\min(L,H)\to\infty}\frac{\log_2Q(L,H)}{LH}
=\sup_{L,H\ge1}\frac{\log_2Q(L,H)}{LH}<\infty.}\tag{G1}
\]

The appeal to a published quadratic upper bound supplies finiteness only; its particular constant is irrelevant. The growing number of directions in official B4 is absent here. Nothing in this two-dimensional Fekete argument licenses replacing Q by C.

## Exact computational evidence

The independently implemented boundary-cut recurrence produced:

| L=H | Strands | Q(L,L) | log2 Q / L² |
|---|---:|---:|---:|
| 1 | 6 | 8 | 3 |
| 2 | 12 | 10442 | 3.337527610836982 |
| 3 | 18 | 4419734746 | 3.560145849075202 |

The L=4 attempt stopped at its preset 50000-state cap. It has no reported count. Completed values and the incomplete trace, exact boundary words, line equations, PID, wall-clock cap and parameters are preserved in `secondpass-fourbundle-*`. G1 would turn any independently certified finite value into a lower bound for S4; the decimals themselves are numerical evidence.

## Candidate G2: a transparent, weaker-than-published B4 lower certificate

This subsection connects one such patch to the official growing-direction family. It is a reconstruction of the published four-bundle/recursive framework, using a small explicitly counted patch. It must not be described as improving the current global lower bound.

Take m=2t+1 lines in each of the four families, with constants in [-t,t]. All pairs from different families cross exactly once; same-family pairs are initially parallel. In the axis square [-t,t]², the central diamond |x|+|y|≤t is the region where all four families are present. It has area 2t²=m²/2−O(m). The complementary region in that square has only one diagonal family at each integer crossing, hence exactly three families. The integer counts are
\[
t_4=2t^2+2t+1,\qquad t_3=2t^2+2t.
\]

Use the translated 3 by 3 rectangles of the periodic tiling and retain only those whose closures lie inside the central diamond. Their number is K_m=m²/18−O(m): a discarded intersecting rectangle lies in a fixed-width band along a boundary of length O(m). Round and shrink retained supports within sufficiently thin crossing-free collars, retaining their entire paired boundary words and every grid crossing originally inside them. The rational offsets keep all grid vertices a fixed positive distance from the tiling edges, so this separates neighboring closed supports without releasing a multicrossing into an interior corridor. Choose any of the Q(3,3) minimal reroutings in each retained support.

At each of the t3 triple crossings outside the diamond, choose a tiny disk disjoint from all large supports and from the other such disks. It meets exactly its three incident strands in proper transverse two-port arcs and no nonincident line. Count both simple resolutions in each such disk.

### Fixed resolution of every uncovered multicrossing

Before the bundle-tail completion, let R_m be **all original multicrossings outside the retained large supports and the counted triple disks**, including any uncovered corridor point. In this tiling they are fourfold points in the omitted boundary band; there are O(m) of them. In particular (0,t) and (t,0) belong to this set when t≥1. They are not counted triple points and must be resolved.

Choose, once for each m and before varying any counted rerouting, a small closed disk E_v about every v in R_m. These disks can be simultaneously pairwise disjoint, disjoint from every previously selected support, and avoid all other original crossings and all lines not incident to v. Indeed there are finitely many distinct points and supports; no original grid vertex lies on a selected support boundary; and every nonincident straight line has positive distance from v. Take each radius smaller than the corresponding finite positive separation minima. Each of its four incident lines then cuts E_v in a proper transverse arc with two distinct ports. The choices made inside the other supports never alter the original geometry near E_v.

For each E_v fix **one** simple boundary-preserving four-strand resolution, for example one fixed adjacent-swap reversal wiring matched to its cyclic ports. The four incident lines' endpoints alternate pairwise, so this resolution makes every one of the six pairs cross exactly once and has no triple meeting. The same finite local construction would fix any other uncovered multicrossing if one arose under a support variant. No multiplicity is assigned to a fixed repair disk: it has one selected output, not an additional free parameter.

Only the remaining **simple** crossings are left unchanged. All selected patch realizations are simple; all counted triple disks and fixed repair disks are simple; and their boundary collars contain no crossings. Therefore the whole output is now a **simple partial arrangement**: each cross-family pair still crosses exactly once, and same-family pairs are still noncrossing. The original crossing-pair assignments were disjoint across these regions, so no replacement creates a missing or repeated pair crossing or a self-crossing of a global strand.

Every choice of the original counted patch and triple resolutions survives this fixed repair. Their local crossing orders remain recoverable in their designated slots of the global labelled strand orders, while all E_v choices are identical across outputs. Hence the number of simple partial arrangements is still at least
\[
2^{t_3}\,Q(3,3)^{K_m}
\ge 2^{m^2/2-O(m)}\,Q(3,3)^{m^2/18-O(m)}.
\]
The O(m) fixed disks add no counted choices and remove none. The omission error in K_m is the same boundary-band error already present in v1; no new exponent loss or coefficient change is introduced.

### Completion and padding

Now insert an arbitrary marked m-strand arrangement in a private tail disk for each formerly parallel bundle. The input is the **simple partial arrangement** just constructed, as required by Felsner–Valtr Section 4 and Cortés Kühnast et al. Section 4, [full arXiv version](https://arxiv.org/abs/2402.13107). All central modifications lie in bounded supports and leave the distant tails straight and parallel. Place one disk far along a distinct ray direction of each bundle. A radius O(m) covers its bundle's width; by choosing the center distance sufficiently large, angular separation keeps every other-family line and the other tail disks outside it. Thus the four disks are pairwise disjoint, meet all m strands of their own bundle in proper transverse arcs, and meet no strand of another bundle. They are beyond every finite cross-family crossing and all the fixed repair supports. These are the cited completion construction's hypotheses and give the injective factor C(m)^4.

This completion step uses a fixed reversal reconnection of each outgoing bundle tail. The old parallel boundary pairing is deliberately replaced by the complete m-strand pairing; every C(m) child has the same reversal connectivity. Thus it is a separate, specified bundle-completion operation rather than an application of F3 with an unchanged parallel pairing. Each formerly parallel pair then crosses once, and every cross-family crossing remains fixed. The reconnection is identical for every child choice, so boundary labellings are consistent across outputs. The child arrangement can be recovered from the crossings within its bundle; projecting the other crossing orders recovers the chosen partial grid arrangement. This is the intended product injection.

For arbitrary sufficiently large n, choose the largest odd m≤n/4 and append the at most seven unused strands by one fixed outside wiring pattern. Deleting those strands recovers the construction, so this padding is injective. We obtain
\[
\log_2 C(n)\ge
\frac{1+\log_2 Q(3,3)/9}{32}\,n^2-O(n)
+4\log_2 C(m),\qquad m/n\to1/4.
\]
The floor-robust recursion lemma M3 therefore gives the candidate lower bound
\[
\liminf\frac{\log_2 C(n)}{n^2}
\ge\frac{1+\log_2 Q(3,3)/9}{24}
=0.1900060770448\ldots.\tag{G2}
\]
The equality on the right uses the unchanged finite input Q(3,3)=4419734746. Both frozen initial reviews independently reproduced that input; the revised construction still requires both targeted re-audits and coordinator acceptance. The already published 0.2721 bound remains much stronger. This construction is useful as a small, reproducible geometry/count/recursion certificate and as a concrete escape from the ternary obstruction in M2, not as a frontier improvement.

## Review scope

Both independent initial reports on frozen v1 are complete. Each reviewer must re-audit the actual v1.1 changes before the coordinator can accept them: G1's nonnegative remainder argument; G2's finite separation and disjoint fixed resolution disks, recovery of simple partial input, survival of every counted choice, unchanged exponent, and the tail-completion hypotheses. The full marked-boundary count and all-n padding remain in force. Q(3,3), the original computation caps and outputs are unchanged; the unfinished L=4 run must never enter a bound. This author packet remains candidate proof - unverified and contains no promotion.
