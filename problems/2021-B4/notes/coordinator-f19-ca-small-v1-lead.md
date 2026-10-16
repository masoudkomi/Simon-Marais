# Finite F19 check: a proposed extension is obstructed

2026-10-16 UTC. **Exploratory finite evidence, unverified.** This is
separate from the frozen degeneration candidate and is not a premise of
that argument. No independent-review credit is claimed.

One possible strengthening would replace absence of CA polynomials over
Fbar19 by absence of degree6 or7 CA polynomials with F19-rational witnesses.
A complete small finite search instead finds examples already over F19.
Thus that particular route cannot remove the published bad-prime obstacle.

For example G(T)=T^6+T^3 has roots0,8,12,18 over F19. Derivative orders
1,2,4,5 can use0, and order3 can use8: H3(G)=20T^3+1 reduces to T^3+1.
It is nontrivial and has a repeated root0. This explicit finite example
alone blocks a blanket claim of no F19-rational-witness CA degree6.
It is not a characteristic-zero counterexample or a lift to the contest.

The standard-library search enumerates monic polynomials with double0,
center normalized to0 or1, c_(d-1)=-d*center, and requires G(1)=0 when
the center is1. Translation and nonzero scaling over F19 cover polynomials
having a rational repeated root and rational center, but the program is
only a finite exploratory check. Counts before identifying affine-equivalent
or differently marked copies:

| Degree | Center | Polynomials examined | Nontrivial rational-witness CA found |
|---|---|---:|---:|
|6|0|6859|42|
|6|1|361|2|
|7|0|130321|18|
|7|1|6859|8|

All root/witness tests use exact modular arithmetic. The first20 examples
per row and hashes of complete solution streams are saved. Supervisor
childPID28994 completed in2.260seconds under an explicit35second timeout;
no process remains. Source, output, job metadata and failure-free stderr
are in computations/coordinator-f19-ca-small-v1*. No paper or theorem
claim has been accepted on the strength of these finite checks.
