# Direction coarsening by deleting equal-color crossings

2026-10-16 UTC. **Candidate proof — unverified.** Constructor: coordinator.
This is a mathematical reasoning pass, without a new enumeration or test
suite. Two fresh independent whole audits are required. The entropy
conclusion below is explicitly conditional on fixed-direction limits that
have not been established here. No full solution, priority or novelty is
claimed.

## 1. Proposed uniform comparison

Use the official marked wiring/tiling dictionary already checked in the
concavity audits. Let C(n) count commutation classes of reduced adjacent
transposition words for the longest permutation on n boundary-ordered
strands. Partition those initial labels into D consecutive nonempty color
blocks with sizes m1,...,mD, summing to n.

Let B(m1,...,mD) count commutation classes for reversing the order of those
blocks while preserving order inside each block. Equivalently, its wiring
diagrams have no same-color crossings and one crossing per pair of
different-color strands. These are the full fixed-direction zonogon
counts, not counts for one global periodic patch construction.

Put

    N=binom(n,2), S=sum_i binom(mi,2), K=N−S, E=n+2K.

The proposed finite inequality is

    B(m1,...,mD) <= C(n)
      <= B(m1,...,mD) * binom(n²−1,2S) * 2^(2S).           (DC1)

The decisive proposed point is that the fiber encoding uses ordered ports
on the projected strands and no S! matching factor. That claim must be
challenged carefully; if a hidden matching/order ambiguity remains, the
displayed entropy consequence has not been proved.

## 2. Projection is defined on commutation classes

Represent a reduced longest word as a left-to-right monotone wiring
diagram. Color a strand by its initial block. At each crossing of equal
colors, use the noncrossing smoothing that keeps vertical order. In word
language, erase the adjacent transposition when its two current colors
are equal. Such a transposition does not change the current color list.
Keep every transposition of different colors, with its same position index.

The resulting word takes the initial block order to the reversed block
order, with order preserved inside each block. It has exactly K letters:
each original pair of different-color labels crossed once. The required
block permutation has exactly K inversions, so the retained word is
reduced. This also proves that every two projected different-color strands
cross exactly once; it is not an assumption about their labels after
smoothing.

If two adjacent original generators commute, their position indices differ
by more than one and their supports are disjoint. Swapping them changes
neither crossing's color classification. After erasure, either nothing
changes, one retained generator is unchanged, or two disjoint retained
generators commute. Thus projection is independent of the chosen reduced
word within its commutation class. Denote it by P.

It is surjective. Given a reduced word for the block permutation, precede
it by a fixed reduced reversal within every initial color block. The
initial within-block reversals do not change colors. Following the given
block word then produces the full longest permutation, with length
S+K=N, hence a reduced word. Its projection is the supplied word.
Choosing this fixed section proves the lower inequality in (DC1).

## 3. Proposed port encoding of one fiber

Fix a projected class and one representative embedded diagram. Its n
directed strands are canonically identified by initial boundary order.
There are E=n+2K open strand segments between consecutive projected
vertices or endpoints: every retained crossing increases that count by2.
Use the embedding only to describe this invariant segment/order data;
no metric coordinates are counted.

Every erased crossing leaves two ports, one on each smoothed strand.
Along each of the E segments, record the ordered list of ports. The total
number of ports is2S. In addition give each port a binary label: whether
its partner is on the immediately preceding or immediately following
strand of the same color, in that color's fixed vertical order.

Why only these two possible partners? The original adjacent transposition
acted on two wires adjacent in the full vertical order. They were
therefore adjacent among wires of their common color. After all equal-
color crossings are smoothed, that color's strands never cross and their
rank order is fixed. Thus each removed vertex connects neighboring ranks.
The ranks and color of each projected strand are boundary data, so they
need no additional alphabet of size n or D at every port.

For a given pair of neighboring same-color ranks, list ports directed
toward one another on each strand in its left-to-right order. In every
actual original diagram their pairings are forced: the first port on
one strand pairs with the first on the other, and so on. Indeed all
removed contacts can be placed at their original sweep coordinates,
where the order along both monotone strands is the same. A contrary
pairing reverses the sweep order of two contacts of the same pair.

Therefore the proposed data reconstructs every removed degree-four
vertex. At each such vertex replace the noncrossing smoothing by the
crossing. The retained vertices/segment orders and these identified
ports specify the directed planar wiring graph, including local rotations.
Following labels from the fixed boundary then reconstructs the original
crossing order on every original strand. Such crossing orders determine
the marked arrangement/commutation class. Invalid port data (wrong counts,
impossible adjacency, an incompatible planar/sweep order) need not be
recognized for an upper bound; it suffices that actual fibers inject.

Two possible subtleties need particular independent scrutiny: whether
choosing a different representative of the same projected embedding could
change the port invariant without being absorbed by the encoded segment
orders; and whether identification of the paired ports leaves any planar
embedding or noncommuting order information unrecorded. The intended
argument uses the projected marked planar diagram, not merely its total
crossing counts or a reduced word selected by an arbitrary sweep.

The number of ways to distribute2S ordered ports among E fixed segments
is the weak-composition count binom(E+2S−1,2S). Once the counts on each
segment are given, its port order labels the positions canonically.
There are at most2^(2S) choices of neighbor bits. Since

    E+2S−1=n+2K+2S−1=n+2N−1=n²−1,

the proposed injection proves the upper inequality in (DC1). It never
counts arbitrary insertion histories as distinct final arrangements.

## 4. Balanced blocks give a uniform entropy error

For fixed D>=3, take mi in {floor(n/D),ceil(n/D)}. Then

    2S/n² -> 1/D  as n->infinity.

The binomial bound binom(M,k)<=2^(M*h2(k/M)), with the usual zero
endpoints, and (DC1) would imply

    0 <= [log2 C(n)−log2 B(m1,...,mD)]/n²
      <= h2(1/D)+1/D+o(1).                               (DC2)

This error tends to zero as D tends to infinity. It is uniform in the
projected arrangement and does not contain log n multiplied by1/D.
That distinction is the purpose of ordering ports locally and forcing
their pairing, rather than assigning a separate n-valued label to every
removed crossing.

## 5. Conditional transfer of fixed-direction limits

Suppose, in addition, that for every fixed D>=3 the full balanced count
satisfies

    ell_D = lim_(p->infinity) log2 B(p,...,p)/(Dp)².         (H)

This is a hypothesis requiring an actual theorem or proof for these
fixed-boundary counts. The earlier reviewed periodic-grid/fixed-boundary-
fiber result is not automatically (H).

The usual strand-addition injection gives monotonicity of B in each side:
an added strand can follow a prescribed extreme path, and deleting it
recovers the original class. Thus for balanced mi with p=floor(n/D),

    B(p,...,p) <= B(m1,...,mD) <= B(p+1,...,p+1).

Under(H), both normalized extreme logarithms tend to ell_D, so the middle
one does too. Let L_minus and L_plus be the official liminf/limsup.
Applying(DC2) for each fixed D gives

    ell_D <= L_minus <= L_plus <= ell_D+h2(1/D)+1/D.

Their difference is therefore at most h2(1/D)+1/D for every fixed D;
letting D tend to infinity proves L_minus=L_plus. In particular the
ell_D then converge to that common value. No numerical value is obtained.

This conditional argument has two separate obligations: the port
injection in(DC1), and a verified fixed-direction theorem(H). Neither
can be supplied by a numerical extrapolation, a claim that boundaries
are negligible, or a thermodynamic limit with different boundaries.

## 6. Literature check prompted by the proposed comparison

The existing sources distinguish full bundle counts from one fixed global
patch family. A new backward search located Widom, Destainville, Mosseri
and Bailly, *Random Tilings of High Symmetry: II*, J.Stat.Phys.120 (2005),
837ff, [author-hosted full paper](https://euler.phys.cmu.edu/widom/pubs/PDF/jsp120_2005_p837.pdf),
DOI10.1007/s10955-005-6998-x. Its introduction, §2–3 and the opening and
finite-side discussion of AppendixA were inspected. It asserts a large-
direction entropy limit, including unit sides, but expressly calls the
AppendixA presentation heuristic. Its variational input and exchange of
large-side/large-direction limits require an independent exact audit;
they are not adopted as(H) or as a solution of the official problem.
The paper is cached locally, not redistributed. Its old numerical data
or natural-log normalization is not used in(DC1)–(DC2).

No exact-priority search for this proposed colored port comparison is
complete. It may have an earlier Coxeter/heap or tiling formulation.
The next task is a conceptual adversarial proof audit, not a new large
enumeration. Every statement in this note remains unverified or explicitly
conditional until the project's independent-review gates are satisfied.
