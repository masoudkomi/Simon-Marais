# Author repair for FD2-01

2026-10-17 UTC. **Candidate proof - unverified; targeted re-audit pending.**
Constructor `review_2017_coarsening_r1`. Requested gpt-6.1-sol/max;
effective settings have no verified readback. Only the coordinator may
resolve the review issue after both independent reviewers re-audit.

I accept reviewer2's substantive objection. The frozen profile v1
Section4 stated a padding consequence from nearby vector-height words
without retaining the ranked-label or bounded-gap hypothesis. That
statement is false as written; the omission was mathematical, not merely
a missing notation definition. Every v1 artifact and every review byte
has been preserved. The annulus construction was separately frozen
before this repair and is not a proof premise of the repaired packet.

## The exact obstruction retained

For any M>=2, length L=3M and equal color counts M, the reviewer gave

    w0=1^M 2_1 3^M 2_2...2_M,
    wA=2_1 1^M 3^M 2_2...2_M,
    wB=1^M 3^M 2_1...2_M.

All prefix coordinates differ by at most1 from w0. The union of
inversions contains every(1_a,2_1) and every(2_1,3_c), so closure
forces every(1_a,3_c). The already present inversions(2_b,3_c), b>=2,
remain. The resulting inversion set is exactly that of

    3^M 2_1 1^M 2_2...2_M.

Thus the prefix-M excursion is M and the physical added area is
2M²+2M: M new tiles each of types12 and23, and M² tiles of type13
whose area is2. The small-error words have a long positional motion
of label2_1, so they do not satisfy the small-displacement hypothesis.
There is no fixed gap G for these references as M grows. This hand
derivation verifies the exact all-M counterexample; no finite tests or
enumeration were used.

## Corrected statements and proof

The actual weak-order envelope lemma is unchanged: if every ranked
label moves at most r positions from a reference adjoined to the family,
the join and meet move every label at most2(D-1)r. It yields physical
band O_D(r) and padding area O_D(rL) for word length O(L).

The height-based consequence now has an explicit extra hypothesis.
Let reference color-i occurrence positions be t_i(k), with sentinels
t_i(0)=0 and t_i(m_i+1)=L+1. Require all consecutive gaps, including
the end gaps, to be at most a fixed integer G. For prefix-count error
at most an integer r, a family occurrence(i,k) at position t has

    t>=t_i(k-r) if k-r>=1,
    t<=t_i(k+r) if k+r<=m_i.

The lower bound follows from the reference prefix count at t being
at least k-r. The upper follows from the count at t-1 being at most
k+r-1. When the ranks pass an endpoint,1<=t<=L and the sentinel gap
bounds replace the corresponding inequality. This gives
|t-t_i(k)|<=G*r, including r=0. Apply the labelled theorem with G*r.

For a real error epsilon L take r=ceil(epsilon L). The corrected
consequence is band O_(D,G)(epsilon L+1) and area
O_(D,G)(epsilon L²+L). A fixed periodic all-color word gives such G;
G is not a D-only constant and cannot be held uniform across arbitrary
periods or missing-color limits. The end gaps prevent a vacuous
bounded-internal-gap condition for a rare color with few occurrences.

## Full replacement copies and affected program claims

The complete revised files are:

- `fixedD-reasoning-r1-structural-candidate-v1.1.md`: new author-repair
  header; Section5 now defines G, proves the exact position bound and
  states the correct parameter dependence and rounding term. The
  labelled theorem itself and all unrelated structural proofs are
  unchanged.
- `fixedD-reasoning-r1-profile-reduction-v1.1.md`: new repair header;
  Section4 now gives the labelled and fixed-G alternatives and retains
  the counterexample. Section3 explicitly says that neither a uniform
  EAI modulus, commensurate periodic replication, nor remainder padding
  follows from the side estimate alone. Its entire recovery discussion
  remains an unproved program. Section5's next-target paragraph carries
  the same qualifications.

Compactness, the upper-profile maximum, nonconvexity, the finite local
encoding, rational multigrids and rational density have no changed proof
in this repair. No new source theorem or later annulus result is being
quietly imported. The original EAI, PR, all boundary-stratum transfer
and(H) remain open. In particular a fixed positive-slope constant does
not provide uniform control as a color density tends to zero.

For comparison, the separately frozen annulus candidate avoids this
specific error by checking global rank-prefix ideals through closed
two-color winding, and its own rational words have a fixed G_J. That
is a new candidate needing its own whole audits, not a repair shortcut
or an accepted dependency of these v1.1 copies.

## Review provenance and operations

After the annulus checkpoint froze, I read both complete initial fixedD
reports and issue ledgers, plus reviewer2's source checks and manifest.
Both initial reviews had already frozen. Reviewer1 had qualified the
periodic constant in its reconstruction; reviewer2 supplied FD2-01's
explicit family and correctly required this scope repair. No review
file was edited and I have not marked their issue closed.

The copies were created with exclusive new-file writes from the verified
v1 bytes and exact replacement sections. Read-only `diff -u` checked
that the changes are confined to the stated headers and affected scope
paragraphs. Hashing and JSON writes are administrative. No mathematical
computation, CAS, enumeration, Git, shared-state edit, charge or source
download occurred. Fresh authoritative telemetry at00:32:37UTC was20%
total weekly used, same reset1792745187 and90%-total ceiling.
