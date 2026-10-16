# A fixed-direction patch entropy and a bounded construction certificate

**candidate proof - unverified**

Written 2026-10-16. This packet concerns one four-direction periodic boundary family. It does not establish the exact liminf or limsup of the official C(n), or their equality. Its numerical lower certificate is weaker than the attributed published 0.2721 bound and is offered as an explicit test of the gluing framework, not a new best bound. Novelty is not established.

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
Also f≥0. Define S4=sup_{L,H≥1} f(L,H)/(LH), allowing infinity initially. For a fixed block (a,b), tile a large rectangle with floor(L/a)floor(H/b) copies and leave its remaining strips in their original grid configuration. Repeated use of (1)–(2) yields
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

Tile the interior of the central diamond by integer translates of the 3 by 3 square patch, omitting only O(m) patches near its boundary. The number is m²/18−O(m). Choose any of its Q(3,3) reroutings independently in each patch. At each of the t3 triple crossings outside the diamond, a disjoint tiny disk permits its two resolutions. Leave all remaining crossings unchanged. Boundary preservation and disjoint crossing-pair assignments give at least
\[
2^{m^2/2-O(m)}\,Q(3,3)^{m^2/18-O(m)}
\]
partial arrangements.

Finally, in a private tail disk for each formerly parallel bundle, insert an arbitrary marked m-strand arrangement. The standard bundle completion construction of Felsner–Valtr Section 4 and Cortés Kühnast et al. Section 4 gives an injective factor C(m)^4. Its hypotheses here are explicit: each disk meets just one bundle, all m strands of that bundle, and no other bundle. Place these disks far beyond the finite cross-family crossing region, in four separate directions.

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
The equality on the right uses the finite computational count Q(3,3)=4419734746 and must await its independent audit. The already published 0.2721 bound remains much stronger. This construction is useful as a small, reproducible geometry/count/recursion certificate and as a concrete escape from the ternary obstruction in M2, not as a frontier improvement.

## Review scope

Two independent adversarial reviewers, one reconstructing the entire argument, must audit any proposed promotion. In G1 check the exact seam phase, product injection and distinction from C. In G2 check the grid's triple/fourfold counts, the density and omission error of 3 by 3 patches, private bundle-tail disks, padding to all n, the recurrence coefficient, and the exact finite DP count. The unfinished L=4 run must never enter a bound.
