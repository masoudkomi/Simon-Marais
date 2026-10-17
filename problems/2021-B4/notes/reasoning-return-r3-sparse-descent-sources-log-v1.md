# Sparse-descent source checks and research log

2026-10-17 UTC. Status candidate proof - unverified.

This follows the frozen parity packet, whose proposed PP1 would
turn a restricted 2021 polynomial into a common odd support for
two descent endpoints. PP1 is not an accepted premise of SD1:
SD1 explicitly assumes just the two arithmetic endpoint equations.

I first considered whether all odd supports had a common
nonvanishing property modulo19. No such theorem was established.
A general prime-bound conjecture based on examples was rejected:
positive descent counts need not be units modulo19, and no
general finite-field positivity principle is available.

For support{1,k,15}, eliminating the last recursion coefficient
instead gives a cubic in the remaining index. It factors as
(k-15)(k2-4k+15), with nonsquare discriminant13 for the quadratic.
This simultaneously excludes every intermediate k without
enumerating support values. The two-index case is a single
explicit necessary boundary check. Supports of size>=4 remain.

Primary source:
- Alexander Diaz-Lopez, Pamela E. Harris, Erik Insko, Mohamed Omar,
  Bruce E. Sagan, Descent polynomials, arXiv1710.11033v2.
  https://arxiv.org/pdf/1710.11033
  Read Proposition2.1 and its full proof, Theorems2.2,2.3,4.1,
  and nearby root-bound passages on2026-10-17 UTC.
  The recurrence used by SD1 is exactly the published polynomial
  identity, with max I=15. No root-bound theorem is applied.
  Journal: Discrete Mathematics342(6),2019,1674-1686,
  doi10.1016/j.disc.2019.01.034.
- General Casas-Alvero/MacMahon attribution is recorded in
  reasoning-return-r3-parity-sources-v1.json, including Marashdeh
  arXiv2608.14726 TheoremB and its explicit multi-root boundary.
  That preprint is not a theorem dependency of this arithmetic lemma.

No full new source was downloaded locally; no viewer-byte hash is
invented. Only URL, version, read scope and verification date are
claimed. No new search after the frozen parity packet was needed.

No mathematical program, support enumeration, CAS, Hensel table,
larger mask search or old finite-certificate rerun. Exact hand
algebra and the F19 square list supply the proof certificate.
Only metadata hashing and exclusive JSON creation are executable.

All fifteen older own packets must match during freeze.
Only reasoning-return-r3-* is written. No shared/Git changes,
contacts, charges, access bypass, spawning or separately billed API.
Requested gpt-6.1-sol/max; effective readback unavailable.
Latest authoritative weekly total23%,reset1792745187,
window10080 minutes,ceiling90% total with integration reserve.
Two fresh nonconstructor audits are required; only root promotes.

