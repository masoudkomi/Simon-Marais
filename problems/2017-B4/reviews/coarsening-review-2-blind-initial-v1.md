# Direction coarsening: independent blind whole audit 2

Date: 2026-10-16 UTC. Reviewer: `/root/review_2017_coarsening_r2`.
Requested settings in the assignment: `gpt-6.1-sol`, `max` reasoning.
Effective-setting readback: unavailable to this reviewer; the request is not
represented as a verified effective setting.

## Scope, independence and verdict

I did not construct this candidate and did not read the other coarsening
reviewer's report, issues, messages or conclusions before freezing this
initial report and its separate issue log. I read the repository protocol,
the official-statement normalization, the existing accepted concavity
exposition for the established marked-count convention, and the candidate
below. I reconstructed the whole coarsening argument rather than testing a
selection of finite examples. No enumeration, CAS or mathematical search
program was run.

Reviewed artifact:
`notes/coordinator-direction-coarsening-candidate-v1.md`, SHA-256
`6379079ab65bd0976058bcc323bf411beaa33c455a20eec5782885c3c72bab5a`.
Its coordinator freeze file was also read. The candidate's status remains
**candidate proof - unverified** until the coordinator applies the project's
two-reviewer acceptance process.

**Mathematical verdict:** I find the finite inequality (DC1) and its balanced
error (DC2) valid. The critical missing-`S!` concern can be resolved
conceptually: the pair of adjacent color ranks identifies the port lists,
and common sweep order forces their matching. I give a reconstruction
below that recovers the original event orders without making any
unrecorded choice of planar rotation or global sweep order. I found no
counterexample or substantive objection to DC1. Making that reconstruction
and the canonical segment identifiers explicit is a useful exposition
improvement, not an extra hypothesis.

The deduction from **(H)** to existence of the official normalized limit is
also valid, with (H) interpreted as a finite real limit for the **full**
fixed-boundary balanced count for every fixed D. I have not proved (H), and
the source checks below do not establish it. This is a conditional partial
result. It neither computes the official rates nor solves 2017 B4. I make
no originality or priority claim.

## 1. Conventions and projection

The official domain is n >= 2, with tilings in a fixed, oriented polygon;
the established dictionary uses reduced adjacent-transposition words for
the longest permutation, modulo commuting adjacent disjoint swaps.
Individual reduced words, insertion histories, and rotation/reflection
quotients are different counts. The candidate uses the correct convention.

Fix D nonempty consecutive initial color blocks of sizes m_i, with sum n.
Let N = binom(n,2), S = sum_i binom(m_i,2), and K = N-S. In a reduced
longest word every pair of original labels crosses once, so precisely S
crossings involve equal colors. Colors follow original labels. Erasing an
equal-color adjacent swap does not change the current color list. Thus,
inductively, each retained swap has exactly its original position index
and still involves different colors.

The retained word has K letters and ends with the blocks reversed, with
the canonical projected labels in each color still in initial order.
That target permutation has K inversions. Its K-letter word is therefore
reduced. This also proves that its different-color projected strands cross
exactly once and its same-color projected strands never cross. One must
not identify the projected labels with the original labels after all
smoothings; the candidate correctly avoids doing so.

For a local commutation s_i s_j = s_j s_i, |i-j| > 1, the two adjacent
position intervals are disjoint. Neither swap changes the colors at the
other interval. After erasure the two local outputs are identical, or
differ by the same allowed commutation. This proves P is well defined on
commutation classes.

For surjectivity, fix a word reversing each initial block internally, of
total length S. Follow it by any word for the projected block permutation.
The result ends at the full longest permutation and has N letters, hence
is reduced. Its first S letters erase and its remaining word survives.
The same fixed prefix respects commutations in the latter word, so this
is also a section on classes. Consequently B(m_1,...,m_D) <= C(n).

## 2. Canonical segment identifiers and invariant port data

Here is a coordinate-free specification of the candidate's segment data.
Number projected strands by initial boundary position. On each projected
strand, list its retained vertices in directed order, including the
identities of their other projected strands. This list is invariant under
commutation. Label the strand's gaps by their position in that list,
including its two endpoint gaps. Across all strands there are

    E = sum_v (number of retained vertices on v + 1) = n+2K

labelled gaps. The canonical identity of a gap is its projected strand
number and its gap index; no coordinate, sweep representative, extra
alphabet, or metric length is needed.

Place a port at each of the two smoothed arcs of every erased crossing.
Record their directed order in each gap. Each port also records whether
its partner has color rank one smaller or one larger. Color rank means
rank among the wires of that same color at a sweep position. After
smoothing, those ranks are constant along projected strands.

Original full-order adjacency implies same-color-rank adjacency. The
converse is not assumed: some arbitrary encodings may place a proposed
contact where other colors obstruct it. Such data are invalid, and need
not be accepted by a decoder for an upper bound. Every actual original
diagram produces the claimed neighbor bits.

The port decoration itself is invariant under original commutations.
It is not enough to have proved this for P alone. For the same local
commutation of disjoint position intervals, do the smoothing and retain
ports inside the two disjoint local rectangles. If both events survive,
the retained vertices commute and neither changes any port order. If an
event erases, its ports stay on arcs disjoint from the other rectangle;
they cannot move through a retained vertex or another port on their
projected strand. If both erase, their two sets of affected projected
strands are disjoint in this local interval. The same decorated directed
graph results. Applying this to every commutation proves invariance of
the canonical gap counts and ordered bits. An arbitrary fixed embedding
of the projected class is only a way to draw these data.

## 3. Forced matching and injective recovery

Fix a color and neighboring projected ranks r,r+1. On rank r take the
subsequence of all ports pointing toward r+1. On rank r+1 take the
subsequence pointing toward r. These are subsequences of complete
directed strand orders; retained vertices separate their canonical gaps.
In an actual original word, each removed crossing of these two ranks has
a sweep time, and its two ports have that same time before an arbitrarily
small smoothing. Distinct such contacts occur in the same chronological
order on both monotone tracks. Hence their two subsequences have equal
length, and the k-th item on one pairs with the k-th item on the other.
Any non-order-preserving alternative would reverse the sweep order of
two contacts on one of the tracks. This argument applies even when the
same neighboring projected ranks meet many times. It does not identify
those ranks with original labels.

In particular, the encoding determines an actual pair of ports for every
erased vertex. No arbitrary matching remains and there is no S! factor.
To make the next step fully explicit, recover the original crossing
sequences as follows.

1. Subdivide each canonically identified projected gap at its ordered
   ports. The incoming/outgoing arcs at each retained crossing are known
   from its two directed projected strands.
2. At each matched port pair create one erased vertex. Its two incoming
   rank arcs continue onto the opposite outgoing rank arcs. This is the
   unique crossing routing that undoes the noncrossing smoothing. At a
   retained vertex continue along the known projected crossing paths.
3. Start the original labels in fixed left boundary order and follow
   these deterministic paths. Every actual input encoding gives n
   directed paths and assigns two original labels to each vertex. Read
   the vertices in order along every original-labelled path.

Invalid abstract encodings might have directed cycles, impossible
contacts, or improper label multiplicities. None affects injectivity on
actual inputs. For two actual originals having the same encoded data,
the above path routing is the same, so all original crossing-event
orders are the same.

For completeness, these orders determine the reduced-word commutation
class directly. Form the event partial order generated by the orders
on individual original strands. Each original word is a linear extension
of it. Any two linear extensions are connected by swaps of adjacent
incomparable events. Such events cannot share a strand, since events on
one strand are ordered. In an actual wiring sweep, swapping two consecutive
events on disjoint label pairs swaps disjoint adjacent-position intervals,
so their generator indices differ by more than one. This is precisely
an allowed commutation. All the resulting intermediate words are valid
because these are commutations of valid reduced words.

This reconstruction answers the possible hidden-planarity objection
without requiring a theorem that an unspecified abstract graph has a
unique embedding. The label paths and the original-strand event orders
already suffice for the counted equivalence relation. Global ordering of
events on disjoint original strands carries no further information in a
commutation class.

## 4. Counting, endpoints and DC2

There are 2S ports. Their gap counts form a weak composition of 2S into
the E canonically labelled gaps. Once those counts are fixed, port
positions in a gap are numbered by their order. Therefore the number
of such data is at most

    binom(E+2S-1,2S) 2^(2S) = binom(n^2-1,2S) 2^(2S).

The alphabet has size two per port because the strand identity supplies
its color and rank. Invalid bits at extreme ranks simply overcount. The
matching does not cost another factor. Multiplying this uniform fiber
bound by B proves DC1.

The finite statement holds for positive integers m_i and 1 <= D <= n.
For D=n, S=0 and P is the identity, giving equality. For D=1, K=0 and
B=1; the same encoding is meaningful. D=2 presents no exceptional
case. If one extends the notation to n=1, D=1, the factor is
binom(0,0)=1 and the inequality is again equality. The official domain
starts at n=2. Empty color blocks were excluded and are not silently
used; for a fixed D the asymptotic balanced construction only needs
n >= D. Ports can always be placed strictly between retained events
and endpoints by choosing a word sweep with distinct event times.

For balanced m_i and fixed D, write n=Dp+r, 0 <= r < D. Then

    sum_i m_i^2 = n^2/D + r-r^2/D,
    2S/n^2 = 1/D - 1/n + (r-r^2/D)/n^2 -> 1/D.

For M=n^2-1 and k=2S, 0 <= k <= M. The binomial entropy inequality,
including k=0 and k=M, gives the exact upper error

    (M/n^2) h_2(k/M) + k/n^2.

Continuity of h_2 gives h_2(1/D)+1/D+o(1). The lower error is zero
by the section. Thus DC2 follows. Each limit here first fixes D;
there is no unjustified uniform interchange of n and D. The resulting
constant tends to zero as D grows. No term (log n)/D is introduced.

## 5. Audit of the conditional limit transfer

The needed monotonicity of B in each side has an injective construction.
Add a parallel strand in a sufficiently thin strip next to a specified
extreme strand of that color. At every crossing of that existing strand
with another color, the added strand also crosses it, with a fixed local
order; it does not cross its own color. This creates the enlarged block
permutation. Deleting the specified new boundary-ranked strand recovers
the starting diagram, so distinct original classes remain distinct. A
deterministic representative may be chosen for each class if desired;
the deletion left inverse suffices for the counting injection.

Consequently, with p=floor(n/D), the candidate's coordinatewise squeeze
between B(p,...,p) and B(p+1,...,p+1) is valid. Under the precise (H),
both extreme logarithms divided by n^2 tend to ell_D, because
Dp/n and D(p+1)/n tend to one. Thus the balanced logarithm also tends
to ell_D. DC2 now yields, for every fixed D >= 3,

    ell_D <= L_minus <= L_plus <= ell_D+delta_D,
    delta_D = h_2(1/D)+1/D -> 0.

The known finite exponential upper bounds for the official count also
ensure finiteness; equivalently (H) can explicitly assert a finite real
limit. Taking the difference and then letting D grow gives
L_plus=L_minus=L, and ell_D <= L <= ell_D+delta_D gives ell_D -> L.
This deduction does not require exchanging large-side and large-direction
limits or replacing fixed boundaries by free/periodic ones.

Hypothesis (H) is a genuine outstanding obligation. A result for a single
periodic grid patch family, or for a fiber with extra prescribed boundary
data, is insufficient. Even conditional equality does not specify a
numerical value for the two official rates.

## 6. Bounded source audit for (H)

The cached Widom--Destainville--Mosseri--Bailly paper was hash-checked:
SHA-256 `ecb3e7ba3ffa04c6ce66395dac2098810eb27da49debf9f55f2bd74d1e86b877`.
I inspected Appendix A's opening on printed p.861 (PDF p.25), selected
subsequent pages, and its bibliography on pp.872-873. The exact caveat is:
“Our presentation is heuristic but can be made rigorous.” Its Appendix A
relies on a variational principle and addresses the high-direction
comparison; this is not a supplied exact proof of (H) for every fixed D.
The phrase about lacking a proper thermodynamic limit at finite D concerns
boundary effects and is not, by itself, a proof that the scalar limit in
(H) fails to exist. [Author-hosted paper](https://euler.phys.cmu.edu/widom/pubs/PDF/jsp120_2005_p837.pdf).

The bibliography points to Cohn--Larsen--Propp (boxed plane partitions),
Cohn--Kenyon--Propp (domino tilings), and Destainville's 1998 boundary
paper. Destainville's [original arXiv record](https://arxiv.org/abs/cond-mat/9804062)
describes lozenges in two dimensions and rhombohedra in three dimensions,
with a functional-integral/saddle-point method; that abstract is not an
all-D theorem for the present full balanced count. I did not turn this
abstract-level check into a claim about every theorem in its full paper.

A further primary-source lead, Krieger--Menz--Tassy,
[Deducing a variational principle with minimal a priori assumptions](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v27i4p1/pdf/),
Theorems 15-17 and the introductory model definition, concerns scalar
graph homomorphisms from subsets of Z^m to Z. It cannot be applied here
solely because the tilings admit a higher-dimensional height description.
An exact correspondence, profile-count theorem and extension hypotheses
would still need verification. No such application was established in
this audit.

The bounded searches and these source checks did not locate a verified
original theorem (H). This is a statement about this audit's search scope,
not a proof that no such theorem exists. There was no purchase, charge,
access bypass, contact with authors, PDF upload or redistribution.

## 7. Operational record

Only files with this review's assigned `coarsening-review-2` prefix were
authored in the repository. Candidate and other reviewers' artifacts were
unchanged. No Git mutation or shared status edit was performed.

Read-only tools: `cat`, `rg --files`, `shasum -a 256`; bundled Python
with `pypdf` for selected source-page extraction; public web search and
primary-source opens. The bundled Python was
`/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`.
No mathematical computation or long native CAS job was needed, so no
subprocess/PID cleanup applies.

For source visual QA, web PDF screenshot failed with cache miss. The
bundled `pdftoppm` command rendered PDF p.25 into the temporary file
`/private/tmp/coarsening-review-2-source-p25.png`, but its oversized white
canvas made the text too small; the text extraction and the web source
both directly confirmed the exact caveat. This render is not a
mathematical certificate or an artifact to commit.

The coordinator supplied account-wide weekly usage of 16% at 21:37 UTC,
reset timestamp 1792745187 and a 90%-total cutoff. This short review did
not start a new window or use separately billed APIs. The initial report
and issue log are frozen together in the accompanying SHA-256 manifest
before any other coarsening review can be read or compared.
