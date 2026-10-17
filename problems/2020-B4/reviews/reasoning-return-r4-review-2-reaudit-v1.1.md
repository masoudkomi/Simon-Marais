# Complete affected R2 reaudit of the 2020 R4 v1.1 repair

2026-10-17 UTC. **Independent affected reaudit; coordinator acceptance
pending.** Reviewer /root/review_2017_coarsening_r1 did not construct
R4A–R4E or the author repair. Requested gpt-6.1-sol/max, effective
readback unavailable. I authored the OLDER repaired R3 F1/F2 dependency,
which was separately accepted after two other audits. This report is
not counted as an independent re-audit of that old theorem.

**Verdict:** R4R2-01 is resolved in the complete versioned replacement.
The automatic final moment and the sufficiency of the interior list
are both proved correctly. No new substantive objection was found
in the affected proof, boundary, obligation and closing-scope changes.
The full E2 iff, R4A–R4D and exact numerical/source domains are retained.
This is a partial cyclic-difference-set result, not the official
unrestricted taut-integer classification.

## Target, actual reads and independence

The full target is notes/reasoning-return-r4-candidate-v1.1.md,
22700B, SHA256
c8fc32fba5fb12a7af4e25b398b65cd9d148273c3bc6f055ea21394a66e01ce2,
with author freeze SHA256
a76d1879815282839e87cf51b6a488279d213b11e1d5f00c8f216bbc44cc7b66.

Read the COMPLETE replacement main, all36 original plus8 repair
obligations, full repair ledger, full revised source audit, full
versioned worklog and ENTIRE five-file unified diff. A combined large
read was truncated; the complete main and complete diff were each
reread separately, so no mathematical section is inferred from a
truncated output. The official local(b) statement was reread. The
earlier full whole R2 report, its issue proof and source audit remain
preserved. No new targeted root/peer repair findings were read before
this report/ledger/source/integrity freeze.

This is the original issue-finding reviewer independently checking the
author's response. The automatic-row and shorter-list argument had
already been reconstructed in my original frozen R2, before the
constructor received it. Reconstructing the response is not independent
construction credit for this review. New author scans, CAS, math
programs, certificates and old constructor scripts were not executed.

## 1. Reconstruct the actual parameter and coefficient domain

Keep m>=3 odd, epsilon in{0,1},

    ell=m²+(2epsilon-1)m+1 prime,
    k=m+epsilon, L=m+2epsilon-1,
    ell-1=mL=k(k-1).

Thus ell is odd, m<ell, k<ell, and L is positive/even. H is the
unique multiplicative subgroup of F_ell^* of ORDER m, and D_epsilon
is the actual subset H or H union{0}. Its cyclotomic INDEX is L.
Every use of mu(z) below is an integer count of pairs from this
subset, not a formal unknown real vector.

For j>0 its power sum is S_j=m if m divides j and zero otherwise;
S_0=k is defined separately. For

    M_j=sum_(a,b in D_epsilon)(a-b)^j

the binomial expansion gives zero automatically when m does not
divide j. Ordered-pair reversal gives zero for odd j. Since m is
odd, the remaining indices are j=tm with even t, and

    M_(tm)=B_t=2mk+m² sum_(i=1)^(t-1)
                              (-1)^i binom(tm,im).

The target vector nu(0)=k, nu(z)=1 for z!=0 has constant moment
k+(ell-1)=k², zero positive moments below ell-1 and final moment
-1. This reconstructs E1–E4 and the original full E2 test. No field
congruence is yet being promoted to an unrestricted integer count.

## 2. The last row is automatic by two exact proofs

For ANY actual k-subset A of F_ell, diagonal pairs contribute zero
to the (ell-1)st difference moment, while every off-diagonal field
difference contributes one. Fermat therefore gives

    sum_(a,b in A)(a-b)^(ell-1)=k(k-1)=ell-1=-1 mod ell.

No earlier moment test or difference-set assumption is used. This
proves the new E2a exactly in its stated cardinality domain.

The proposed independent E2b calculation also holds. In F_ell,

    binom(ell-1,j)=(-1)^j, 0<=j<=ell-1.

At j=im, m odd, the factor (-1)^i in B_L cancels this sign.
All L-1 summands equal one. Consequently

    B_L=2mk+m²(L-1)
       =m[(m+1)L+1]=(m+1)ell-1=-1 mod ell.

The middle equality follows from L=m+2epsilon-1 and k=m+epsilon.
It is a literal integer identity before the final reduction. It
does not assume any interior B_t equation. The last target stays
-1; “redundant” never means replace it by zero.

## 3. Interior equations suffice by a reduced matrix

Impose B_t=0 for even2<=t<L. The preceding automatic moments plus
these equations give equality of actual and target moments at
every j=1,...,ell-2. The constant moments already agree. Also

    mu(0)=nu(0)=k

holds EXACTLY, because D_epsilon is an actual subset with k distinct
members. Let w(z)=mu(z)-nu(z) in F_ell. Thus w(0)=0. Removing that
known coordinate leaves

    sum_(z in F_ell^*) w(z) z^j=0, j=0,...,ell-2.

There are ell-1 unknown coordinates and ell-1 equations. Their
matrix is invertible: a polynomial of degree<=ell-2 vanishing at
all ell-1 nonzero residues is zero, proving independence of its
rows. Therefore w(z)=0 at every nonzero residue.

For fixed z!=0 and each second point b there is at most one first
point a=b+z. Hence 0<=mu(z)<=k<ell. Its congruence to1 then forces
the integer value1, not merely a value modulo ell. Together with
the actual zero count this gives an actual planar difference set.
Conversely any such set has the required interior moments. The
interior list is therefore an iff for the prescribed D_epsilon.

This proof neither assumes the full-field matrix's last row nor
requires an arbitrary formal moment vector to have its zero
coordinate known. That known coefficient is the exact reason the
smaller square matrix is available. Dropping a different list of
rows without a new recovery argument is not justified.

## 4. Boundaries and affected downstream claims

L=2 occurs only at (m,epsilon)=(3,0). There is no interior even t
in2<=t<L. All moments through ell-2 are then automatic, so the same
reduced matrix argument remains valid with an empty interior list.
This is an endpoint check of the symbolic criterion; no preliminary
prime-power construction is reproduced. The final B_2 remains-1.
The displayed E5 binomial condition requires L>2 and is correctly
left unasserted at this endpoint.

The full original E2 iff remains valid with the redundant last row
included. The E5 application and the Hall-based implication3|m
remain unchanged: in an actual E2 solution, the multiplier group
contains H of order m>=q in the stipulated prime modulus, and the
R4D saturation conclusion applies. The q4 exception is absent in
this standalone domain; no generic nonsaturated case is excluded.

All affected prose is corrected: the paragraph after E2, the
additional proofs, the final shortened-list warning and original
O28/O30/O32. The old “essential/insufficient” assertion does not
survive as current mathematical text. Its quotation in the repair
ledger and historical source/worklog suffixes is explicitly a
preserved error/history, not an uncorrected claim.

The exact R4A-through-R4D proof segment is unchanged. Its individual
versus common fixed-group distinction, q4 set/collision and multiplier
normalization hypotheses retain the original whole R2 dispositions.
The repair does not weaken q!=4 in Cohen-dependent branches, assert
that every multiplier group is saturated, or import a flag-transitive
classification. Its source record explicitly labels retained source
reads rather than fabricating a fresh external theorem check.

## 5. Disposition and remaining scope

All8 repair obligations pass, and the affected original O28/O30/O32
now pass in the replacement. The original full whole R2 already
reconstructed the other33 rows; their mathematical contents and
source boundaries are unchanged. The companion ledger records all44
rows and the original issue's resolved-in-replacement status.

Recommend coordinator acceptance of this repaired scoped partial
packet AFTER the other required affected audit and reconciliation.
Do not overwrite either original initial report or the original v1.
The nonsaturated multiplier branch and the unbounded interior system
remain open; no new taut classification, verification cutoff,
preliminary-part proof, numerical value or novelty is established.

