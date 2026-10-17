# Targeted re-audit of FD2-01 author repair v1.1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`, a nonconstructor.
Requested gpt-6.1-sol/max; independent effective-setting readback remains
unavailable. This is a separate targeted repair audit, after the two
fixedD initial whole reports and my independent annulus report froze.
I read reviewer2's complete original fixedD report, issue ledger and
source checks as expressly authorized. I did not read reviewer2's
targeted v1.1 re-audit or any peer annulus finding before this freeze.

## Disposition and correction of my initial assessment

I recommend resolving FD2-01 for the v1.1 copies: the mathematical
hypothesis omitted from v1 is now explicit, its constant depends on the
reference gap bound G, and the rounding and endpoint cases are correct.
The unchanged labelled envelope theorem is not contradicted by the
retained all-M example. All affected recovery passages now state their
additional open obligations instead of claiming them from height
closeness. No new substantive objection arose in this targeted audit.
Only the coordinator may resolve the issue or promote a result after
both targeted audits. EAI_D, PR, H and the full 2017 problem remain open.

My initial whole report failed to flag the unqualified claim in profile
v1 Section 4. Although its reconstruction discussed periodic constants,
the no-objection disposition did not confront the statement actually
written. Reviewer2's exact family establishes a substantive mathematical
omission, which I independently reconstruct below. This separate report
corrects that part of my assessment; every byte of the initial report,
issue record and manifest remains preserved.

The reviewed v1.1 structural candidate has SHA256
`06c6b5eb0f793be00c4dfa1784eb8987cdd415eb1247d708cc827727cd9b5e87`;
the profile note has SHA256
`212ad70f53b166bb23cb82ffae72dc38437d7a3f6cec54a7752b2d90a0f7791c`;
the author repair has SHA256
`cca69e6dbe4bc199c446142721b1e3f004fba1520ca9396028523bb0bab6fbb3`.
The sources, constructor freeze and preserved v1/initial-review records
are verified in the companion metadata. Read-only full diffs show that
the two replacement copies change only their headers, the finite-word
gap argument and the identified program qualifications.

## 1. Exact finite-word conversion, including end ranks

Write N for word length here, to distinguish it from the geometric
window scale L. The reference and all family words have the same color
content m_i. In the reference, color-i ranks have positions

    0=t_i(0)<t_i(1)<...<t_i(m_i)<t_i(m_i+1)=N+1,

and every consecutive gap is at most G for each active color. G is a
fixed positive integer belonging to this reference family. The prefix
count discrepancy in every coordinate and every position is at most an
integer r>=0. Let the occurrence (i,k) in one family word be at position
t, so its counts at t and t-1 are k and k-1.

At position t the reference count is at least k-r. If k-r>=1, this gives
t>=t_i(k-r). At position t-1 the reference count is at most k+r-1.
If k+r<=m_i, it follows that t<=t_i(k+r): otherwise the reference prefix
at t-1 would already contain rank k+r. These inequalities use the two
different prefix positions, so there is no missing one-position error.

For an interior lower rank, summing r consecutive reference gaps gives

    t_i(k)-t <= t_i(k)-t_i(k-r) <= G*r.

If k-r<=0, then k<=r and the initial sentinel gives instead

    t_i(k)-t <= t_i(k)-1 <= k*G-1 <= r*G-1.

For an interior upper rank, likewise

    t-t_i(k) <= t_i(k+r)-t_i(k) <= G*r.

If k+r>m_i, then m_i+1-k<=r and the terminal sentinel gives

    t-t_i(k) <= N-t_i(k)
               <= (m_i+1-k)*G-1 <= r*G-1.

Thus in every case

    |t-t_i(k)| <= G*r.                                  (B)

When r=0 neither endpoint case can arise for an actual rank
1<=k<=m_i. The two interior inequalities say t=t_i(k), so the family
word equals the reference. When r exceeds some or all rank counts, the
endpoint estimates above remain valid. A color with m_i=0 has no ranked
labels, contributes identically zero prefix counts and requires no
position bound; the empty word is trivial. No lower bound on color
density was silently used in (B).

The end gaps are essential to the stated uniformity. Bounding just gaps
between existing occurrences would say nothing about the displacement
of a unique occurrence near one end. The finite-word sentinels repair
that issue. For a fixed periodic word containing each active color,
both internal and end gaps in sufficiently long restrictions are bounded
by its period. That bound is not a D-only constant, and changing periods
or letting a positive density disappear can make it diverge.

For a real prefix error epsilon*L, take r=ceil(epsilon*L). This is a valid
integer upper bound, including epsilon=0. Since r<=epsilon*L+1, (B)
gives the advertised estimate with its additive constant. No uniform
O_D(epsilon*L) consequence is recovered by silently dropping G or the
rounding term.

## 2. Reconstructing the labelled theorem used after (B)

The finite family contains its reference, with ranks fixed within each
color. Its join is the increasing-label transitive closure S of the
union U of its inversion sets. Closure is immediate. For coclosure,
take a U-path a=x0<...<xk=c and an intermediate label b. If b is on the
path, take its prefix or suffix. Otherwise one U-edge straddles b; the
original inversion set supplying that edge is coclosed, supplying an
edge to or from b, and the corresponding path prefix/suffix gives
(a,b) or (b,c) in S. Closure and coclosure rule out the only two directed
triangles in the associated tournament, so S is an inversion set.
Every U-edge strictly increases color, and hence a U-path has at most
D-1 edges and cannot create a same-color inversion. This proves the
join exists within the same shuffle interval.

Suppose each ranked label moves at most s from its reference position.
A U-edge new relative to the reference spans a positive reference
position difference at most 2s. An old reference inversion has negative
position difference along the path. Thus any comparison newly reversed
in the join spans reference distance at most R=2(D-1)s. Old inversions
remain because the reference belongs to the family. A label gains at
most R old successors before it and loses at most R old predecessors,
so the absolute change of its position is at most R. Reversing the word
and ranks within each color is an antitone involution preserving all
these displacement estimates; it gives the meet bound. No density or
gap assumption is part of this labelled theorem.

Applying it with s=G*r from (B) proves the v1.1 exact bound

    join/meet ranked displacement <= 2(D-1)*G*r.

This is consistent with r=0, absent colors, and arbitrary finite color
multiplicities. The fixed-D chain bound alone does not turn bare prefix
error into small s; that was precisely the false inference in v1.

## 3. Geometric band, area and recovery scope

At a common integer x-prefix, moving ranked labels by at most R changes
each color count by at most R. With v_i=(1,i-1), physical x remains that
prefix length and the y-error is bounded by
R*sum_i(i-1), hence O_D(R). Linear interpolation on each unit-x edge
keeps the same bound between integer prefixes. For word length N=O(L),
the region between comparable bounding paths therefore has area
O_D(R*L).

An increasing-inversion chain fills this region with positive ij
parallelograms: each swap raises the path pointwise and adds a tile above
the already filled region. Weak contacts or empty lobes contribute no
area and do not invalidate the shelling. Applying the common meet and
join to a family of comparable patch boundaries therefore gives band
O_D(G*r) and padding area O_D(G*r*L). The fixed inner patch is recovered
by restriction to its original boundary. If that boundary varies, two
color words of length O(L) use O_D(L) bits; ranks within a color introduce
no independent matching permutation.

For r=ceil(epsilon*L), these bounds are exactly

    band O_(D,G)(epsilon*L+1),
    area O_(D,G)(epsilon*L^2+L).

They control a qualified one-dimensional side padding. They do not
identify all corner offsets, close a four-sided annulus, choose a common
periodic phase or establish flux compatibility across a missing-color
stratum. The repair states each of these limits explicitly.

## 4. The retained all-M obstruction is exact

For D=3 and M>=2, use the reference and two family words

    w0=1^M 2_1 3^M 2_2...2_M,
    wA=2_1 1^M 3^M 2_2...2_M,
    wB=1^M 3^M 2_1...2_M.

wA's prefix difference from w0 is either zero or (-1,1,0); wB's is
either zero or (0,-1,1). Their maximum coordinate discrepancy is one,
and their physical y-error is at most one. They are above w0 in weak
order. wA supplies all (1_a,2_1) inversions and wB all (2_1,3_c)
inversions. Transitive closure forces all (1_a,3_c), while the existing
(2_b,3_c), b>=2, persist. These are precisely the inversions of

    3^M 2_1 1^M 2_2...2_M.

There are no new inversions involving 1_a and 2_b, b>=2. The prefix-M
reference height is (M,0,0), and the join height is (0,0,M), giving
coordinate error M and physical error 2M. Relative to w0 the newly
added pairs are M type12, M type23, and M^2 type13, whose physical areas
are 1,1,2. Added area is exactly 2M^2+2M.

The first rank 2 moves M positions, so the small labelled-displacement
hypothesis fails. The reference also has unbounded end/internal gaps
as M grows, so it fails every fixed-G hypothesis. Taking N=L=3M and
epsilon=1/L disproves the v1 D-only band and area consequences. At a
fixed epsilon>0 the examples eventually satisfy 1<=epsilon*L, while
their normalized join excursion stays 1/3, excluding a D-only estimate
uniform as epsilon decreases. This is an exact all-M proof, not finite
computational evidence. The author retains and correctly attributes it.

## 5. All changed program passages remain qualified

The v1.1 profile header and Section 4 state both valid alternatives:
direct ranked-label displacement, or prefix discrepancy together with
a fixed end-inclusive gap bound G. Section 3 expressly says that a
uniform EAI_D modulus does not follow from this estimate and requires
separate treatment of degenerating strata. Extraction is still an
unproved map with controlled fibers, and insertion is still an unproved
closed annulus with a recoverable core.

The old claim of ordinary periodic replication is now conditional on
commensurate windows and opposite collars matched by period
translations. Integer dilation/subdivision of a fixed tiling preserves
its profile, but the remainder at general scales still needs an explicit
boundary-preserving padding construction. If the side theorem is used
there, it requires the very labelled/gap hypotheses established above.
The author no longer infers it from height proximity. The combined
quantified control of exceptional area, bands, extraction multiplicity
and all-scale errors is expressly a program, not a theorem EAI_D=>PR
already proved from a fully formalized target.

The upper-profile maximum identity, finite local encoding, rational
multigrids, rational density and same-frame nonconvexity obstruction
have no changed mathematical proofs. Their original whole audits are
not replaced by this targeted report. The new annulus candidate is
mentioned only for comparison and explicitly excluded as a repair
dependency; no annulus result is used in this audit. The revised final
target paragraph likewise retains closed boundary, rank, phase,
stratum and full-frame recovery obligations. Nothing now asserts H,
PR, a uniform stratum transfer or an exact 2017 exponent from this
side estimate.

## 6. Scope and operational record

The complete repair note, sources, both full replacement copies and
full read-only v1/v1.1 diffs were read. Reviewer2's complete original
report, issue ledger and source checks were read only after both initial
fixedD audits froze. Its targeted repair report was not read. My whole
annulus report froze before any of these repair reads, and its issue
and reasoning remain separate.

This targeted correction is elementary and self-contained; no new
published theorem or external source premise is needed. No enumeration,
CAS, search, mathematical subprocess or new PDF download was used.
Python is reserved for one-time metadata fingerprints and exclusive
new JSON records under this assigned re-audit prefix. Candidate files,
all earlier reports, shared status and Git are unchanged. Fresh
authoritative telemetry at this task transition returned 20% total of
the 10080-minute weekly window, reset1792745187, below the 90%-total
ceiling with integration reserve.
