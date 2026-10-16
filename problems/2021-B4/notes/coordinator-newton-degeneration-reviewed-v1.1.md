# Reviewed small-cluster degeneration

**Proved, independently reviewed (partial result)**, 2026-10-16 UTC.
This is an acceptance register for the unchanged mathematical argument in
[the frozen v1 note](coordinator-newton-degeneration-v1.md). Its candidate
label records the original version; subsequent acceptance is documented in
[degeneration-acceptance.md](../reviews/degeneration-acceptance.md).

In the specified degree d=p+1 rational-witness normalization, p>=5,
J>=d/2 and h=d-J, suppose no nontrivial Hasse Casas-Alvero polynomial of
degree h exists over Fbar_p. Then at least one of H2,...,H_(h-1) vanishes
at the center1. For h=2 the empty disjunction excludes the case.

The proof rescales the small-root cluster along the adjacent Newton edge.
It gives an integral polynomial whose reduction has degree exactly h
and is not a pure power. If no stated center equation held, every required
low derivative would retain a common witness after reduction, contradicting
the characteristic-p hypothesis. The proof permits fractional slopes,
repeated roots, residue extensions and coincident reduced witnesses.

CLO's published good-prime results verify the premise at p=19 for h<=5.
In degree20, the extra J=15 condition H2(1)=0 or H3(1)=0 or H4(1)=0
removes392 of461 necessary masks, leaving69. Combined with the separately
accepted older J=17 exclusion and J=16 condition,772 necessary masks
remain. None is asserted to lift to a rational polynomial.

Two independent reviewers, neither a constructor of this argument,
reconstructed the complete theorem, directly checked the primary source's
Hasse definition and good-prime list, and independently enumerated and
compared every one of the461 records. Both found no unresolved substantive
objection. No proof repair was required. Their initial extension audits
were blind to one another and separate from their frozen old reports.

The premise is false at h=6 and h=7 for p=19 in the cited source. No
application there, lower-J classification, solution of degree20, or
novelty is claimed. The coordinator's separate finite-field examples are
exploratory evidence and were not a dependency of either review.
