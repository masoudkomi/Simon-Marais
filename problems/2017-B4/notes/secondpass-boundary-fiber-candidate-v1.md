# Fixed-boundary patches as completion fibers: candidate v1

**candidate proof - unverified**

Written 2026-10-16. This is a proposed structural lemma and counting reduction, not a proof of either exact B4 rate. Novelty has not been established. Its converse uses an embedded-graph argument that especially needs adversarial scrutiny. The finite computations are evidence only.

## Objects, conventions and attributed ingredients

A boundary word w is a cyclic sequence in which each of m distinct labels occurs twice. On the boundary of an oriented closed disk D, mark 2m distinct points with those labels in that cyclic order. A minimal chord arrangement consists of m proper simple arcs joining like-labelled endpoints, with only transverse crossings, no three arcs meeting at one point, and each pair crossing at most once. F(w) counts such arrangements up to orientation-preserving homeomorphisms fixing the labelled boundary data. Equivalently for counting, one may use all local crossing orders along the labelled arcs; no rotational/reflection quotient of the objects is taken.

The crossing set X(w) consists exactly of pairs whose endpoints alternate around w. This follows from the elementary separation/parity property for two arcs in a disk plus the at-most-once hypothesis.

We use the established correspondence between C(m), simple marked pseudoline arrangements, commutation classes and complete triple-sign patterns. A complete sign pattern assigns a bit to each a<b<c, with the four bits on each increasing four-set changing at most once in their packet order. This correspondence is attributed mathematical context, not newly established here; see Felsner–Valtr, Section 1, [author PDF](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf), and the first-pass references. A bit can be read from the order of ab and bc in a left-to-right wiring diagram.

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

Take a complete pattern σ on the right side and a wiring realization A. On a strand i, compare any outside crossing ij (meaning ij not in X(w)) with any other crossing ik. The triple ijk is not in T(w), so its fixed sign forces the same relative order as in A0. Therefore:

1. The outside crossings along each strand have exactly the A0 order.
2. The crossings marked inside form the same single contiguous slot, between the same outside prefix and suffix.

Cut each strand at the two ends of that slot, using two nearby cut points on the appropriate edge if the slot is empty. Remove the pieces in the inside slots. Include a sufficiently large outer circle with the prescribed order of all unbounded strand ends. The remaining outside embedded graph is connected via that circle. Its labelled vertices, rotation at each crossing, local crossing orders and outer boundary agree with those of the fixed exterior of A0.

Use the standard classification of a connected plane graph embedding by its rotation system and designated outer face to identify the outside graphs by an orientation-preserving homeomorphism. The ports corresponding to D lie on the same designated complementary face with the same cyclic order w. Every removed inside arc stays in that face, since an inside piece cannot cross an outside piece: each crossing was assigned inside or outside simultaneously on both participating strands. A small thickening of the fixed outside graph, followed by a disk homeomorphism of its designated face, places the removed arcs into D with the required ports. Their local crossing orders define a patch counted by F(w).

This is intended to prove surjectivity. **Review point:** the argument about the designated face, dangling ports, and thickening must cover disconnected interior arrangements and empty inside slots. It should not be silently replaced by the weaker statement that the abstract crossing graph agrees.

## Candidate F2: a finite constraint factorization

Conditional on (F1) and the established complete sign-pattern correspondence, F(w) is an exact finite constraint count:

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

Suppose one fixed marked complete arrangement on n labelled strands contains disjoint closed disks P1,...,Pr. Their boundaries avoid crossings, and each disk meets any strand in either one connected arc or not at all. Let wj be the labelled boundary word in Pj. Replacing each local patch independently by a minimal realization with that same boundary word gives
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

Two fresh independent adversarial audits, including one full reconstruction, are required before any promotion of F1–F3. A reviewer of this packet must see neither the other initial review nor any author-created review verdict.
