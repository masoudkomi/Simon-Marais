# Parity barrier source checks and continuation log

2026-10-17 UTC. Candidate proof - unverified.

PB1 was found by a targeted hand specialization motivated by the
Euler/secant divisibility appearing in the primary source, not by
enumerating odd supports. The support{1,3,5,7,15} has the four
nontrivial normalized residues2,3,6,11. Its residual D17 center
sum is152, divisible19, while the divided original center endpoint
is-1 modulo19. This is a useful exact counterexample to treating
the residual degree17 condition alone as a contradiction.

Primary published inputs, all already directly read in this task:
- Diaz-Lopez--Harris--Insko--Omar--Sagan,
  Descent polynomials, arXiv1710.11033v2,
  https://arxiv.org/pdf/1710.11033
  Proposition2.1 with full proof, Theorems2.2,2.3,4.1.
  Used only for the explicitly reconstructed sign/orientation of
  F_I=(-1)^|I|d(I;Z). Denominators divide15!, hence are19-units.
- Marashdeh, A descent-set obstruction for the Casas-Alvero
  conjecture, arXiv2608.14726v1,
  https://arxiv.org/pdf/2608.14726
  Introduction TheoremB and its multi-root boundary checked.
  The general one-nonzero-root/MacMahon correspondence is attributed.
  No unrestricted multi-root theorem is imported.
No new source download, invented viewer-byte hash or novelty claim.

The earlier frozen parity and sparse-descent results are NOT
accepted premises of the finite-field certificate. Every coefficient,
root and derivative cover is verified explicitly here. The reason
for recording d(I;20)/19 as well is to distinguish the residual
counterexample from a lift of the original normalized degree20
conditions.

A further constructive route was considered but not completed:
for a repeated root d=2r+delta, write centered Z=T2 and
C=r(r+delta). The small-root factor has odd part
T[(Z-C)2+delta2 Z] and even part-2delta Z(Z-C).
For a residual B(r+T)=V(Z)+T W(Z), the even Taylor condition is

    [(Z-C)2+delta2 Z]W(Z)-2delta(Z-C)V(Z)
      =Z7(h16+h18Z+Z2).

This exact factor identity suggests a linear interpolation
description in the residual coefficients. However:
- no full-rank or rational family assertion was established;
- integrality cannot be inferred merely by solving over Q19;
- choosing r to kill the first e0 coefficient is insufficient,
  because the logarithmic derivative must remain integral;
- satisfying the five still-unassigned odd derivative orders
  would remain a separate global problem.
No partial-family existence or counterexample is claimed.

Unsuccessful broader ideas remain bounded: all-real-root theorems,
a large unused-factor Galois group, and positivity of descent
counts over Z do not settle these finite-field or rational-lifting
conditions. The prime5 base-degree4 erratum remains in force.

No mathematical program, support enumeration, CAS, digit tree,
higher mask search or rerun of the old three-value/J16 certificates.
Only metadata hashing and exclusive JSON creation are executable.
All sixteen older own packets must match during freeze.

Only the assigned reasoning-return-r3-* prefix is written.
No Git/shared changes, spawning, contacts, charges, access bypass
or separately billed API. Requested gpt-6.1-sol/max; effective
readback unavailable. Latest weekly total23%,reset1792745187,
10080-minute window,ceiling90% total with integration reserve.
Two fresh independent nonconstructor audits are required.

