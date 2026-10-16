# Fixed-boundary patches as completion fibers: candidate v1.1

**candidate proof - unverified**

Full revised version **v1.1**, 2026-10-17 (Australia/Brisbane). The revision author is `/root/owner_2017`, the original constructor of these second-pass packets. Both frozen independent initial reports were read for this author repair. All frozen v1 notes, manifests and review reports are preserved. The revised inferences require both targeted re-audits and coordinator acceptance before any promotion.

Original draft written 2026-10-16. This is a proposed structural lemma and counting reduction, not a proof of either exact B4 rate. Novelty has not been established. Its converse uses an embedded-graph argument that especially needs adversarial scrutiny. The finite computations are evidence only.

## Objects, conventions and attributed ingredients

For m≥1, a boundary word w is a cyclic sequence in which each of m distinct labels occurs twice. On the boundary of an oriented closed disk D, mark 2m distinct points with those labels in that cyclic order. A minimal chord arrangement consists of m proper simple arcs joining like-labelled endpoints. Each arc meets the boundary only at its two distinct ports, transversely; there are no boundary segments or tangencies. Interior intersections are transverse, no three arcs meet at one point, and each pair crosses at most once. F(w) counts such arrangements up to orientation-preserving homeomorphisms fixing the labelled boundary data. Equivalently for counting, one may use all local crossing orders along the labelled arcs; no rotational/reflection quotient of the objects is taken. Define **F(empty)=1** for the empty patch. The completion-fiber assertion below is stated for m≥1; the empty case is handled by this unit convention and introduces no official C(0) domain.

The crossing set X(w) consists exactly of pairs whose endpoints alternate around w. This follows from the elementary separation/parity property for two arcs in a disk plus the at-most-once hypothesis.

We use the established correspondence between C(m), simple marked pseudoline arrangements, commutation classes and complete triple-sign patterns. A complete pattern assigns a bit to each a<b<c; on each increasing four-set its packet has at most one sign change. The precise primary theorem is Felsner–Weil, *Sweeps, Arrangements and Signotopes*, **Theorem 7**, printed p. 15: the four-set monotonicity condition characterizes triangle-sign functions of simple marked arrangements. **Theorem 8**, on that page, gives the equivalent compatibility criterion for their local permutations; the proof of Theorem 7 is on printed p. 19. See the [author manuscript](https://page.math.tu-berlin.de/~felsner/Paper/sas-dam-rev.pdf). Identify its two signs consistently with our bit values. Packet reversal or complementing the sign convention preserves the one-change predicate. A triple fixes all comparisons between its pair crossings on common strands. Felsner–Valtr, Section 1, [author PDF](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf), supplies the marked-arrangement/local-sequence/tiling dictionary. These are attributed ingredients. The inspected Felsner–Weil PDF and page-image fingerprints are recorded in `author-repair-sources-v1.1.json`; full source files remain only in ignored cache. A bit may be read from the order of ab and bc in a left-to-right wiring diagram.

The independent cut recurrence in `secondpass-patchcount.py` implements the recipe of Cortés Kühnast et al., Section 5.1, [arXiv:2402.13107](https://arxiv.org/abs/2402.13107). It cuts on one arc, enumerates only crossing orders consistent with noncrossing pairs, and multiplies the two smaller patch counts. That recurrence is attributed; the completion-fiber formulation below and its tests are the focus of this pass.

## Candidate F1: complete-arrangement fiber formula

Place the endpoints generically on a strictly convex curve, join each pair by a straight chord, and extend each chord to its full straight line. Choose the positions so the lines have distinct slopes and no three are concurrent. Call this complete arrangement A0. The portion outside D is held fixed. Number its lines by their order at the left, and write σ0 for its complete triple-sign pattern.

Let T(w) consist of those triples of labels all three of whose pairs are in X(w). Thus every crossing of such a triple lies inside D in A0. The candidate formula is
\[
\boxed{F(w)=\#\{\sigma\in\mathcal C_m:
\sigma(t)=\sigma_0(t)\text{ for every }t\notin T(w)\}.}\tag{F1}
\]
Here \(\mathcal C_m\) is the set of complete marked arrangement sign patterns in the fixed left-boundary labelling. The formula depends on an actual fixed outside completion, not just a count of arcs or crossings.

### Forward map and why every nonfree triple stays fixed

Glue any patch realization to the fixed exterior A0\D. For pairs in X(w), the unique crossing remains inside and there is no outside crossing; for pairs outside X(w), there is no inside crossing and their unique outside crossing stays fixed. The output is a simple complete pseudoline arrangement.

Consider a triple t not in T(w). It has an outside crossing ij. If its other two crossings are outside too, its sign is visibly fixed. Otherwise at least one of ik or jk lies inside. On the common strand, an inside crossing remains between that strand's two boundary ports, whereas ij remains on its fixed outside prefix or suffix. Their relative order is fixed, which fixes the triple sign. Thus every nonfree sign agrees with σ0.

Different patch crossing orders yield different complete crossing orders: on each global strand, the local inside block is a fixed slot between unchanged exterior crossings. This gives an injection into the right side of (F1).

### Converse: the outside graph has to remain the same

Take a complete pattern σ on the right side and a piecewise-linear wiring realization A. On a strand i, compare any outside crossing ij (meaning ij not in X(w)) with any other crossing ik. The triple ijk is not in T(w), and its fixed sign determines their relative order on the common strand. That order agrees with A0. Consequently the outside crossings have exactly the A0 order, and if inside crossings occur, they form the same contiguous block between the same outside prefix and suffix.

An **empty** inside block needs a construction choice, not an extra sign constraint. In A0 record the gap between its exterior prefix and suffix. The same gap exists in A's identical exterior local sequence; choose two distinct nearby points in that edge and remove the crossing-free segment between them. If all crossings on a strand are inside, put its two cuts on its unbounded tails. In every case retain both cut endpoints as distinct labelled degree-one port vertices.

Remove one inside segment per strand. Add a sufficiently large outer circle, with its strand endpoints in the prescribed marked cyclic order. Every retained prefix and suffix reaches that circle along its own strand, so this finite outside graph is connected, even when the removed crossing network is disconnected or empty. Its isomorphism to the corresponding graph of A0 preserves exterior crossing labels, their order on every strand, both port labels per strand, rotations at crossings, and the labelled outer circle with its outer face. The crossing rotations are fixed by the oriented wiring convention; degree-one ports have no further rotational choice.

For completeness, the connected plane-embedding fact used here can be seen by replacing every vertex by a small oriented disk and every edge by a ribbon attached in its specified cyclic order. The rotation system specifies this regular neighborhood; filling its complementary disks specifies the spherical embedding, and designating the outer face specifies the plane embedding. This allows bridges and degree-one vertices. Agreement of the abstract crossing graph alone would not supply these data.

In A0's retained graph all ports are incident to the same bounded face U0, the one containing the former disk interior. Its facial boundary **walk** lists the labelled port corners in cyclic order w. The walk may repeat bridge edges or cut vertices; a degree-one port has one incident face corner. The preserved rotation system transfers this whole face and port-corner list to one bounded face U of A's retained graph.

Every removed inside arc has endpoint germs in U and cannot cross a retained edge: any pair crossing is classified inside or outside simultaneously on both participating strands. Its open arc is therefore contained in U. Every connected component of the removed crossing network has ports, because it is a union of these proper cut-strand arcs; there is no floating component in another face.

The unthickened facial walk need not itself be a Jordan curve. Choose a sufficiently thin **closed regular neighborhood** of the connected outside graph. Away from small port collars it is disjoint from all removed arcs; at each port trim only a short, crossing-free initial piece of the removed arc. Finiteness and piecewise-linearity allow all these collars and thicknesses to be chosen simultaneously. The closure of the complementary component corresponding to the bounded face U is now a closed disk with a Jordan boundary. It has one distinct transverse boundary port for each trimmed endpoint, in the same cyclic corner order w. All trimmed removed arcs and their crossings remain in that disk. This construction also works for an empty inside slot, for exterior bridges, and for several disconnected interior components.

An orientation-preserving disk homeomorphism sends this disk and its ordered labelled ports to D with the prescribed boundary positions. The trimmed arcs give a minimal patch with the required crossing orders. Gluing it to A0's fixed exterior reproduces every local sequence of A, hence the chosen complete sign pattern σ. This is the proposed surjectivity argument; together with the forward injection it gives (F1). Both reviewers must re-audit this explicit replacement of the v1 face/thickening paragraph.

## Candidate F2: a finite constraint factorization

Conditional on (F1) and Felsner–Weil Theorems 7–8 under the marked, fixed-order conventions just stated, F(w) is an exact finite constraint count:

- Variables are just the triple bits in T(w).
- Bits outside T(w) are fixed to σ0.
- Each four-set imposes its one-sign-change packet constraint.

Join two free variables whenever they occur in the same four-set constraint, and let K1,...,Ks be the connected components of this variable graph. Each constraint uses variables in at most one component. The all-fixed constraints are satisfied because σ0 is an arrangement. Hence
\[
F(w)=\prod_{j=1}^s Z_j,
\]
where Zj counts the assignments on Kj satisfying all constraints involving that component. This factorization is just a finite product decomposition, not an assertion that arbitrary free triples are independent.

In particular F(w)≤2^|T(w)|, and a triangle-free crossing set has F(w)=1. A four-strand complete patch has four free triple bits but only eight assignments, rather than sixteen: packet compatibility matters.

## Candidate F3: boundary-preserving patch gluing

Suppose one fixed simple marked complete arrangement on n labelled strands contains pairwise disjoint closed disks P1,...,Pr. A disk boundary contains no arrangement crossing. Each strand either misses the disk or meets it in exactly one **proper simple arc with two distinct transverse boundary ports**; exclude tangencies and boundary segments. Let wj be the full labelled paired boundary word in Pj. A disk meeting no strands has wj=empty and factor F(empty)=1. Replacing each local patch independently by a minimal realization with that same paired boundary word gives
\[
C(n)\ge\prod_{j=1}^r F(w_j).\tag{F3}
\]

The crossing pair assigned to a disk is fixed by boundary alternation and cannot occur in another disk or outside it. Thus replacements introduce neither missing nor repeated pair crossings. A change in a local crossing order is visible in the corresponding fixed slot of the global labelled strand order, so the product map is injective. The complete-arrangement/rhombus-tiling dictionary then returns a tiling in the official fixed-polygon count.

This is a deliberately narrow, auditable version of the standard local rerouting mechanism. It does not permit boundary pairings to change; it does not allow an arbitrary pair partition to be presumed geometrically realizable; and it does not prove a quadratic replication theorem or existence of the entropy limit.

## Finite evidence and an explicit failed simplification

The independent cut recurrence and the proposed fiber formula agree for every paired boundary word with m≤7. For m=7 this is 135135 words before caching; the 5283 dihedral/relabel canonical words are used only to reuse equal counts. It also matches MacMahon for six specified bundle sizes, including M(3,3,3)=980 and M(2,3,4)=490. Full output and dedicated-child metadata are preserved in the computation files.

Even the pair (number of strands, number of crossings) is insufficient boundary information. Both words below have four strands and three crossings:

```text
(0,1,0,2,1,3,2,3) -> F=1
(0,0,1,2,3,1,2,3) -> F=2
```

The first crossing graph is a path; the second contains one mutually crossing triple and an isolated strand. Thus substituting one patch for the other based only on those two scalar counts is invalid. No unrestricted statement is inferred solely from these examples.

Both initial v1 audits are frozen and were completed independently. The new citation, empty-slot construction, connected exterior/regular-neighborhood argument, and proper-port/empty-patch hypotheses in v1.1 require targeted re-audit by both reviewers. This author revision is not an independent review or a promotion; coordinator acceptance remains required.
