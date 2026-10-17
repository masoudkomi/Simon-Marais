# FD2-01 targeted repair reaudit: issue ledger

2026-10-17 UTC. Applies only to the hashed v1.1 structural/profile/repair
packet. The original blind issue ledger is preserved byte for byte.

## FD2-01

- Original status: substantive false unqualified consequence in profile v1
  Section 4. Height closeness alone does not control weak-order envelopes.
- Author repair: retains direct ranked-label displacement, or adds a fixed
  finite-word reference gap \(G\) including both end gaps. Replaces the
  \(D\)-only band and area claims by the correct \(D,G\)-dependent bounds.
- Reaudit result: sufficient repair; recommend resolution for v1.1 by the
  coordinator after both targeted independent audits.
- Exact reconstruction: integer prefix error \(r\) implies
  \(|t-t_i(k)|\leq Gr\); the proof at \(t\) and \(t-1\) and both
  sentinel cases check. It covers \(r=0\), ranks at either end, empty
  colors and arbitrarily large \(r\).
- Consequences: join/meet ranked displacement at most \(2(D-1)Gr\);
  physical band \(O_D(Gr)\), area \(O_D(GrL)\); after rounding,
  \(O_{D,G}(\varepsilon L+1)\) and
  \(O_{D,G}(\varepsilon L^2+L)\).
- Counterexample: the retained all-\(M\) family has the stated exact join,
  vector error \(M\), physical vertical error \(2M\), and added area
  \(2M^2+2M\). Its \(2_1\) displacement is \(M\), and its reference
  gap is unbounded. No exception to the repaired statement occurs.
- Uniformity: the fixed reference, period, margin and rare-color
  dependence are retained. No arbitrary-reference or missing-color
  uniformity follows.
- Affected downstream scope: EAI, its \(D\)-only modulus, commensurate
  periodic replication, all-scale remainder padding, PR and (H) remain
  unproved. The revised complete text no longer presents these as supplied
  by the repaired side estimate.
- Authority: reviewer recommendation only. The original issue file is not
  edited, and this ledger does not promote any result.

## New substantive objections introduced by this repair

None found. No later annulus theorem was accepted or used. The separate
annulus candidate requires its own whole independent audits.
