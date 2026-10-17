# FD2-01 targeted repair reaudit, reviewer 2

2026-10-17 UTC. This is a targeted independent reaudit of the author's complete
v1.1 structural and profile copies, their repair ledger, source metadata and
freeze. It does not alter or replace the frozen initial audit. The writer
identified FD2-01 and did not construct the repair. No later annulus result is a
dependency of this report.

## Conclusion

The substantive FD2-01 objection is repaired in the v1.1 statements. The
author now retains either direct ranked-label displacement or a fixed reference
gap bound \(G\), including the end gaps. The exact conversion
\(\lvert t-t_i(k)\rvert\leq Gr\) is correct, including \(r=0\), ranks near
the first/last occurrence, and values of \(r\) larger than a color count.
The resulting physical band, area and rounding terms are correct.

The author also removes the affected unsupported program implications:
neither a uniform modulus over all slopes, periodic replication from the word
“periodic” alone, nor boundary-preserving all-scale remainder padding is now
presented as proved. EAI, PR and (H) remain unproved. I recommend that the
coordinator resolve FD2-01 for these versioned copies after the other
independent targeted audit. I have not edited the original issue's frozen
status and do not promote the packet myself.

## Exact inputs and scope of comparison

- Structural v1.1:
  SHA-256 06c6b5eb0f793be00c4dfa1784eb8987cdd415eb1247d708cc827727cd9b5e87.
- Profile v1.1:
  SHA-256 212ad70f53b166bb23cb82ffae72dc38437d7a3f6cec54a7752b2d90a0f7791c.
- Author repair ledger:
  SHA-256 cca69e6dbe4bc199c446142721b1e3f004fba1520ca9396028523bb0bab6fbb3.
- Source metadata v1.1:
  SHA-256 d71027c2a84c41cb69365a4a38ac5ff66459be7a0be123719ad0ad28acdeddd1.
- Author freeze v1.1:
  SHA-256 ea3f730889db04083940bccc2fb545cd3984557c9854e43a11791d75186fb51b.

I read both complete v1.1 candidates and the complete repair note. Read-only
unified diffs against the frozen v1 copies confine the changes to the
provenance/repair headers, structural Section 5, profile Sections 3--4 and the
qualified next-target paragraph in profile Section 5. The labelled lattice
theorem, its proof, and the other structural proofs are unchanged.

This review rechecks all affected inferences; it does not pretend that a
targeted repair review is a new independent whole audit of the unrelated
lemmas. Their full initial reconstruction and exact source checks remain
frozen under fixedD-structural-review-2-initial.md and its companions.

## Reconstruct the finite-word gap conversion

Let \(w_0,w\) have equal color counts, length \(L\), and prefix counts
\(n^0_i(s),n_i(s)\), with
\[
|n_i(s)-n^0_i(s)|\leq r\quad(0\leq s\leq L),\qquad
r\in\mathbb Z_{\geq0}.
\]
For each active color, reference positions are
\[
0=t_i(0)<t_i(1)<\cdots<t_i(m_i)<t_i(m_i+1)=L+1
\]
and every consecutive difference is at most \(G\). Write \(t\) for the
position in \(w\) of occurrence \((i,k)\).

At prefix \(t\), \(n_i(t)=k\), so \(n_i^0(t)\geq k-r\). If \(k-r\geq1\),
this gives
\[
t\geq t_i(k-r).
\]
At prefix \(t-1\), \(n_i(t-1)=k-1\), so \(n_i^0(t-1)\leq k+r-1\).
If \(k+r\leq m_i\), the \((k+r)\)-th reference occurrence has not yet
appeared at \(t-1\), giving
\[
t\leq t_i(k+r).
\]
The use of \(t-1\) in the second inequality is essential and is correct in
the repaired text.

For the earlier-displacement bound there are two cases:

1. If \(k-r\geq1\), summing exactly \(r\) reference gaps gives
   \(t_i(k)-t\leq t_i(k)-t_i(k-r)\leq Gr\).
2. If \(k-r\leq0\), then \(k\leq r\); the initial sentinel gives
   \(t_i(k)\leq Gk\leq Gr\), while \(t\geq1\).
   Hence the same upper bound holds.

For the later-displacement bound:

1. If \(k+r\leq m_i\), summing \(r\) gaps gives
   \(t-t_i(k)\leq t_i(k+r)-t_i(k)\leq Gr\).
2. If \(k+r\geq m_i+1\), then \(m_i+1-k\leq r\), and the final
   sentinel gives
   \(L+1-t_i(k)\leq G(m_i+1-k)\leq Gr\).
   Since \(t\leq L\), the same upper bound holds.

Together these prove \(|t-t_i(k)|\leq Gr\) exactly. For \(r=0\) both
in-range inequalities apply to every occurrence and give \(t=t_i(k)\);
the words are identical. If \(r\) is large, a sentinel argument replaces
an out-of-range rank and never calls for a nonexistent occurrence. An empty
color has no labels to control. The finite-length trivial bound may be
stronger than \(Gr\), but this causes no failure.

The endpoint hypotheses are substantive. Merely bounding gaps between
successive existing occurrences would allow a color with one occurrence
and a long unregulated initial or terminal interval.

## Reapply the actual envelope theorem

Adjoin \(w_0\) to the finite family. The unchanged labelled theorem takes
reference displacement \(s=Gr\) and gives join and meet displacement at
most \(R=2(D-1)Gr\). Its proof remains applicable without assuming a
number of occurrences bounded in terms of \(D\): closure paths increase
the initial color at every step and have at most \(D-1\) edges.
The previous initial audit already reconstructed the closure, coclosure,
shuffle-interval and meet-duality arguments; no hypothesis of them has been
changed by this repair.

At a prefix position \(q\), any color-count discrepancy caused by
displacement at most \(R\) is at most \(R\). An occurrence newly before
\(q\) came from a reference position at most \(q+R\); one lost from that
prefix came from a position after \(q-R\). There are at most \(R\) slots
in either interval. Thus the vector lifts are within \(R\) in every
coordinate at the common integer abscissae.

All positive word edges have horizontal displacement one. Linear
interpolation at a common real abscissa preserves this prefix bound.
The physical vertical coordinate is
\(\sum_i(i-1)a_i\), so the vertical separation is at most a constant
depending only on \(D\) times \(R\). The weak-order comparable envelopes
have the same endpoints; the region between them is filled by
inversion-creating adjacent-swap parallelograms. Integrating a height band
of \(O_D(Gr)\) over a path of horizontal length \(O(L)\) gives area
\(O_D(GrL)\). Coincident pieces have zero area and do not require
extra tiles.

This remains an injective padding construction when the retained patch
and its boundary are fixed, because restriction recovers the patch.
If the boundary varies, recording one color word of length \(O(L)\)
uses \(O_D(L)\) bits; rank labels are forced by color order and do not
introduce a factorial matching factor.

For a real bound \(\varepsilon L\), taking
\(r=\lceil\varepsilon L\rceil\leq\varepsilon L+1\) yields precisely
\[
\operatorname{band}=O_{D,G}(\varepsilon L+1),\qquad
\operatorname{area}=O_{D,G}(\varepsilon L^2+L).
\]
The additional \(L\) area term is retained. With zero error one can
instead use \(r=0\) and obtain zero displacement; the displayed rounded
bound is only a valid upper estimate.

## Verify the retained all-M counterexample

For \(M\geq2\), all three colors occur \(M\) times, and \(L=3M\).
The reference and words are
\[
w_0=1^M2_1 3^M2_2\cdots2_M,\quad
w_A=2_1 1^M3^M2_2\cdots2_M,\quad
w_B=1^M3^M2_1 2_2\cdots2_M.
\]
Moving \(2_1\) across the first block changes prefix counts by
\((-1,1,0)\) where affected. Moving it across the third-color block
changes them by \((0,-1,1)\). Thus every prefix coordinate differs
from the reference by at most one.

The reference already inverts every pair \((2_b,3_c)\) for \(b\geq2\).
The union for the family also contains all \((1_a,2_1)\) and
\((2_1,3_c)\). Transitive closure forces every \((1_a,3_c)\).
These pairs, and no others, are exactly the inversions of
\[
w_\vee=3^M2_1 1^M2_2\cdots2_M.
\]
This is the exact join, not only a lower bound for it. At prefix \(M\)
the vector discrepancy is \((-M,0,M)\), with infinity norm \(M\)
and physical vertical discrepancy \(2M\).

Relative to \(w_0\), the new tile counts are \(M\) of type 12,
\(M\) of type 23, and \(M^2\) of type 13. Their areas are respectively
1, 1 and 2, giving exactly \(2M^2+2M\).
The rank \(2_1\) moves \(M\) positions in each input word.
Moreover the end gap of color 1 alone is \(2M+1\); no fixed \(G\)
can cover this family as \(M\) grows.

The repaired \(G\)-dependent estimates therefore allow this excursion and
area. They no longer make the false \(D\)-only prediction. The vector
height error \(M\) quoted by the author is consistent with this
calculation; the physical vertical error is \(2M\).

## Uniformity and the complete affected recovery discussion

For a fixed periodic reference containing every active color, the largest
cyclic gap is finite. Long restrictions inherit a common gap bound,
including the sentinel gaps. It belongs to that reference. In a family
with \(G\) bounded, summing gaps implies
\[
L+1\leq G(m_i+1)
\]
for every active color. A disappearing positive density as \(L\to\infty\)
therefore forces loss of a uniform \(G\). The author's withdrawal of
uniformity over arbitrary periods and missing-color limits is necessary
and correct.

I checked every affected paragraph in the complete profile note:

- Section 1 still proves the compact-profile upper maximum (P1) only.
  PR is a sufficient extra all-scale lower property, not established or
  claimed equivalent to (H).
- Section 2 still distinguishes free-window entropy from the exact full
  polygonal lift and supplies upper boundary fibers only. The primary
  free-window theorem and strong-irreducibility hypotheses are not
  changed or expanded by this repair.
- Section 3 now says explicitly that its \(D\)-only modulus is an
  unproved target, not a consequence of this side estimate. It requires
  control of backgrounds, degenerating strata, phase and offset repair,
  and recovery multiplicities.
- The formerly asserted periodic-family replication now requires exact
  commensurate windows and matching opposite collars. Calling a boundary
  periodic is expressly insufficient.
- Integer dilation and tile subdivision still preserve one normalized
  lift, but do not supply a reference at every integer scale. The
  remainder-padding step is now explicitly missing; applying the side
  theorem would require the appropriate label or gap hypotheses.
- The claimed extraction/insertion discussion remains a program whose
  band, exceptional-area, multiplicity and remainder losses must all be
  quantified together. The repair does not silently infer PR from EAI as
  currently informal.
- Section 4 now states the two qualified alternatives, retains the exact
  obstruction, and leaves closed corners, ranks, phases and zero-density
  flux as separate two-dimensional work.
- Section 5's next-target paragraph retains these requirements and does
  not import the separately frozen annulus candidate.

Accordingly the repair removes a false proved implication by narrowing
the consequence and accurately weakening the program status. It does
not prove the stronger original implication, EAI, PR, (H), a new numerical
frontier or the full 2017 problem.

## Integrity, sources and operations

All five v1.1 input hashes match the assignment/freeze. The complete original
v1 packet and its source/freeze bytes are verified unchanged, as are all
previous twenty files frozen by this reviewer and the author's listed
preserved review files. The separately frozen annulus candidate/worklog/
source/freeze hashes are checked administratively, without treating them as a
repair premise or reading peer annulus findings. The manifest records these
integrity checks.

No new source theorem is used in the gap proof: it is a finite-word argument.
The original primary theorem audit remains frozen in the initial source
record. Read-only diffs are administrative comparisons; their exit code 1
means the expected version differences were present. No mathematical
enumeration, CAS, broad tests, candidate edit, shared-state write, Git
operation, source download, charge or subagent spawn was performed.

Requested settings remain gpt-6.1-sol / max. Effective settings have no
independent verified readback. Latest authoritative weekly telemetry available
for this reaudit is 20% total used, reset 1792745187, with the 90% total-used
ceiling and integration reserve. The separate blind annulus audit starts only
after this targeted report, ledger and manifest freeze.
