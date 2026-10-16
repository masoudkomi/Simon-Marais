# Independent blind audit 1: direction coarsening

2026-10-16 UTC. Reviewer: `review_2017_coarsening_r1`, not a constructor.
Requested launch setting: `gpt-6.1-sol`, reasoning `max`. No effective-setting
readback was available. This is the initial report, written before reading
any other coarsening review or its conclusions. Only the coordinator may
promote a result after the complete review process.

Reviewed candidate:
`../notes/coordinator-direction-coarsening-candidate-v1.md`, SHA-256
`6379079ab65bd0976058bcc323bf411beaa33c455a20eec5782885c3c72bab5a`.
The supplied freeze manifest agrees with the bytes independently hashed.
Scope is all of 2017 B4, under its already audited marked wiring/tiling
dictionary. No other annual problem or preliminary part was investigated.

## Verdict

I recommend accepting **DC1 as a finite comparison and DC2 as its
unconditional asymptotic consequence**, subject to the coordinator's second
independent review gate. The entire conditional transfer under (H) also
checks out. I found no counterexample or substantive obstruction to the
ordered-port injection. In particular, neither an `S!` matching factor nor
an additional noncommuting global-order factor is needed.

Two compressed steps in the candidate benefit from explicit lemmas:
invariance of the port code under original commutations, and recovery of a
commutation class from its labeled crossing orders. Both are reconstructed
below. They are not new unproved premises in this audit.

**(H) remains unestablished.** The inspected primary sources do not supply
an audited theorem for the full balanced fixed-boundary counts for every
fixed D. This is an outstanding condition for an unconditional existence
claim, rather than an objection to the explicitly conditional theorem.
Neither an exact numerical exponent nor a full solution of 2017 B4 follows.
No priority or novelty conclusion is offered.

## 1. Objects and projection

Let `w0` be the longest permutation on n ordered boundary labels. A reduced
adjacent-transposition word has `N=binom(n,2)` events, one for each unordered
pair of original labels. A commutation exchanges consecutive generators
`s_i,s_j` with `|i-j|>1`; braid moves are not quotiented out.

Color the initial labels in D consecutive nonempty blocks, of sizes m_i.
In every prefix of the original word, the current color list agrees with
the current color list obtained by erasing earlier equal-color events:
an erased event exchanges two equal entries and has no effect on this
list. Consequently each retained generator still acts on two different
colors at its same position index. There are exactly

    K = N - sum_i binom(m_i,2)

retained events. The output color blocks are reversed. Since the erased
word never exchanges labels of the same color, its within-color order is
the initial one. The resulting block permutation has K inversions; a word
of length K realizing it is reduced. In particular, each pair of projected
strands of different colors crosses once, and no same-color pair crosses.
This argument does not confuse original labels with labels after smoothing.

For one original commutation, the two events use disjoint pairs of total
positions. Reversing their order leaves both classifications unchanged.
After erasure the outputs are identical, differ only by omitting the same
event, or differ by the same allowed commutation. Thus P is a map on
commutation classes.

Fix reduced reversals inside the initial color blocks, in a fixed block
order. Prefixing any block-permutation word by these reversals yields the
full reversal and has length S+K=N. It is therefore reduced and projects
back to the chosen block word. A commutation in the latter remains a
commutation after prefixing, so this is a well-defined section on classes.
It proves both surjectivity and `B(m)<=C(n)`.

## 2. Canonical projected edges and port-code invariance

Name a projected strand by its color and its initial rank within that
color. At a retained vertex, name the vertex by its unique pair of
projected strand names. The sequence of these vertices along each strand
is invariant under commutations of a projected word. Thus an edge can be
named canonically by its projected strand and its two consecutive
retained vertices or endpoints. This identifies the same E edges in every
representative of a projected class. Here

    E = sum_strands (number of retained vertices on that strand + 1)
      = n + 2K.

An equal-color event in the original sweep joins neighboring ranks of that
color: its two positions are adjacent even in the total list. Smoothing
preserves those ranks, because projected strands of one color never cross.
The lower/upper neighbor bit therefore specifies its partner strand, when
one exists, without an alphabet that grows with n. Each such event supplies
one port on each of its two projected strands.

For completeness, inspect an original commutation before constructing the
code. Its two events use four distinct instantaneous total positions. The
four corresponding projected tracks are distinct. Erasing an equal-color
event does not change that list of tracks; retaining a different-color
event exchanges only its own two positions. Hence exchanging the two
events cannot change the order of two ports on a common projected strand,
cannot move a port across a retained vertex on its strand, and cannot
change a port's color-rank neighbor bit. If both events are retained, the
canonical projected edge identification above absorbs their commutation.
This proves invariance of the **whole code**, not merely of P.

The code can therefore be attached to an original commutation class
without choosing an arbitrary sweep as additional information. Metric
coordinates of a fixed representative are unnecessary.

## 3. Forced matching and reconstruction

For every neighboring same-color rank pair `(c,r),(c,r+1)`, concatenate
ports along each entire directed projected strand, using its known
retained-vertex order. On the upper rank retain ports with a lower-neighbor
bit; on the lower rank retain those with an upper-neighbor bit.

In any actual original diagram the kth ports in these two lists belong to
the same event. Indeed each event has one sweep coordinate on both
monotone tracks, so their event orders agree. A different permutation of
the pairing would put some two events in opposite orders on the two
tracks. This argument allows multiple contacts of a rank pair and does
not assume that projected ranks are original labels.

Given a code arising from a diagram, subdivide each canonical projected
edge by its ordered ports and identify paired ports as degree-four
vertices. Retained vertices keep their known projected through-strand
pairing. At a restored equal-color vertex, an original label entering on
one smoothed rank leaves on the other smoothed rank: restore the crossing
instead of the smoothing. These pairings determine all original directed
strands from their ordered boundary labels. Consequently the code
determines every event and the crossing-partner order along every original
strand. Invalid codes may fail these operations or create a directed
cycle; no recognition algorithm for them is required.

Here is a direct justification that no hidden global order remains.
Associate one event to each original unordered label pair. Order events
by the crossing orders on the original strands, and take the transitive
closure. Both original reduced words with this code are linear extensions
of that same event poset. Any two linear extensions of a finite poset are
connected by exchanges of consecutive incomparable elements. Incomparable
events cannot share an original label, since its strand totally orders all
its events. When consecutive events of a valid reduced word use disjoint
label pairs, their generator positions differ by more than one: adjacent
positions would share a current label. Their exchange is therefore an
allowed commutation. Moving between the two linear extensions by these
exchanges proves that the original words belong to the same commutation
class.

This also bypasses a possible ambiguity about embedding distant port
pairs in faces. We reconstruct the directed event graph and original
through-strand pairings; these already determine the commutation class.
For actual codes the required planar realization exists by construction.
We need not choose a new realization for every invalid abstract code.

Thus each fiber of P injects into the proposed port data.

## 4. Counting, boundary cases, and DC2

For E canonically ordered edges, first record nonnegative counts a_e with
sum `2S`. There are `binom(E+2S-1,2S)` such vectors. The positions of the
ports on each edge are then its first, second, etc.; they require no
independent labels. Choosing a bit at each of the `2S` positions gives at
most `2^(2S)` codes. Since

    E+2S-1 = n+2N-1 = n^2-1,

the upper half of DC1 follows. No arbitrary insertion histories or global
permutations of ports were counted as diagram data.

For the official n>=2 and every nonempty block partition, E>=n>0 and
`0<=2S<=n(n-1)<n^2-1`; stars and bars and the binomial are valid. When
S=0 the comparison is equality. When D=1 the projection has n edgeless
tracks and the same injection still works. The conditional theorem only
uses fixed D>=3 and eventually n>=D, so balanced blocks are nonempty.

For fixed D and balanced blocks,

    2S/n^2 = sum_i m_i^2/n^2 - 1/n -> 1/D.

Apply the elementary binomial entropy inequality with `M=n^2-1`, `k=2S`.
After division by n^2, the binomial term tends to `h2(1/D)` and the bit
term tends to `1/D`. Lower comparison gives nonnegativity. This proves
DC2 uniformly over the projected class. In particular, a factor
proportional to `(log n)/D` has not entered the estimate.

## 5. Reconstruction of the conditional transfer

The required monotonicity of B can be justified by duplicating an extreme
strand in the chosen color. Draw a parallel copy immediately on its fixed
within-color side. At each crossing with another color, replace that one
crossing by the forced two consecutive crossings with the copy and the
old strand. The new strand crosses every other-color strand once and no
same-color strand. This construction is invariant under commutations;
deleting the boundary-identified new strand recovers the original class.
Thus B is nondecreasing in each m_i.

Put `p=floor(n/D)` and assume (H) as stated, with the full B-count. Then

    B(p,...,p) <= B(m_1,...,m_D) <= B(p+1,...,p+1).

For the left logarithm divided by n^2, (H) is multiplied by `(Dp/n)^2`,
which tends to 1; the right uses `(D(p+1)/n)^2`, also tending to 1.
Therefore the middle normalized logarithm tends to ell_D. DC2 implies

    ell_D <= L_minus <= L_plus <= ell_D + epsilon_D,
    epsilon_D = h2(1/D)+1/D -> 0.

The normalized C-count has a finite upper bound from the already reviewed
zone estimate, so the subtraction of limsup and liminf is legitimate.
Taking arbitrarily large fixed D forces equality. Also
`0<=L-ell_D<=epsilon_D`, proving `ell_D->L`. There is no illicit exchange
of simultaneous p,D limits: n tends to infinity for each fixed D first.
An unbounded set of D for which (H) is verified would already suffice.

This is a correct conditional **existence** theorem. It determines no
numerical value and does not discharge the official problem in full.

## 6. Audit of the proposed literature route to (H)

Widom--Destainville--Mosseri--Bailly (2005), Appendix A, first takes large p
at fixed D, then large D, before discussing fixed p. Its exact input is a
local entropy variational principle. The fixed-p paragraph groups small
regions together, without a finite counting estimate uniform in their
sizes. This does not independently establish (H). Calling the appendix
heuristic is useful context, but is not itself the mathematical objection.
The scalar convergence in (H) is also weaker than the paper's homogeneous,
boundary-independent notion of a proper thermodynamic limit; its denial
of the latter for fixed D does **not** refute (H).
[Author paper, Appendix A, pp. 861--867](https://euler.phys.cmu.edu/widom/pubs/PDF/jsp120_2005_p837.pdf).

Following its reference 11, Destainville (1998), Section 2.2, Eq. (7),
replaces a product of local membrane counts by the global count after
asserting that interface corrections disappear. It does not give a
quantitative compatible-boundary lower estimate. Section 2.3 then assumes
a unique nonsingular maximizer and applies a Gaussian saddle-point
argument; the subsequent strict-concavity discussion treats the general
model condition as a hypothesis. Those steps require proof before they
can establish (H) for every fixed D. They are identifiable missing counting
and regularity obligations, rather than a blanket rejection of physical
reasoning.
[Original author preprint, Sections 2.2--2.3, pp. 6--10](https://arxiv.org/pdf/cond-mat/9804062).

Cohn--Kenyon--Propp (2001), Theorem 1.1 and its precise versions, give a
rigorous variational principle for domino/dimer tilings; their stated
extension includes three lozenge directions. No reduction of the general
D-direction zonogon count to that dimer model was supplied here. It is
therefore not a theorem proving (H) for arbitrary fixed D.
[Primary paper, abstract and Theorem 1.1](https://arxiv.org/pdf/math/0008220).

The bounded source search and inspected reference chain did not locate a
rigorous general (H). This is a report of search scope, not a claim that
no such theorem exists. The previous periodic-grid patch theorem counts a
specified boundary family and does not become (H) by nomenclature.

## 7. Evidence, operations, and remaining work

No enumeration, numerical experiment, CAS operation, or computational
mathematical certificate was used. The proof reconstruction is conceptual.
Read-only commands inspected the candidate, current protocol, official
normalized statement, and already accepted partial theorem. SHA-256
checks confirmed the supplied candidate and cached source.

The bundled Python `pypdf` extracted the cached 37-page paper to a temporary
text file. Bundled Poppler rendered PDF pp. 25--27, with `-cropbox` after
the first render exposed the PDF's large media box. The complete relevant
pages were visually inspected. Other relevant appendix text and the
original 1998 and 2001 primary PDFs were read through the web PDF tool;
the latter two were not downloaded into the repository. Source scope and
search queries are in `coarsening-review-1-sources.json`.

The coordinator's remaining tasks are the other independent audit,
resolution/integration of any contrary finding, and retention of (H) as
an explicit condition until a valid source or proof is audited. I suggest
including the canonical-edge and event-poset details above in the final
exposition. No source PDF, credentials, shared status file, Git commit, or
push was changed by this reviewer.
