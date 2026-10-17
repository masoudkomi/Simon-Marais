# Collision-depth construction research log

2026-10-17 UTC. **Candidate proof - unverified.** Assigned continuation
of 2021 part(b), owning only reasoning-return-r3-*.
Earlier return and mirror candidates remain byte-for-byte frozen.

The target was a repeated2R root d different from exactly2r.
The earlier unique-least-weight reflection test excludes repetitions
only when its minimum is unique. Repetitions can force tied weights,
so simply claiming that a unit Taylor coefficient always controls the
even part would repeat the unresolved inference.

The successful new algebra subtracts a multiple of the even part
from its derivative. With E=T^(2m)A(T^2), the exact identity is

    2r^(2m+1)A'(r^2)
      =-delta U(2r)[1+delta(m/r-U'(2r)/(2U(2r)))].

The bracket is a19-adic unit. This yields a general finite repeated-root
displacement at least4nu without an extra ladder, and exact derivative
valuation formulas even in tied cases.

For the specific extra ladder through H14 at r, E has only three
even terms. The Euler identity gives a uniform error e0 of valuation
at least15nu+1. The TOP three actual rational witness equations then
supply the new finite-depth conclusion:

    nu=1, d!=2r, v_19(d-2r) in{15,16};
    H18 cannot use1.

This is not a full repeated-root or mask exclusion. The additional
five exact equations at r are essential. The remaining depths15,16
have not been excluded or shown to lift.

Construction path and precision checks:
- First obtained k>=4nu by factoring E=T6 A(T2), with A' divisible19.
  The previous naive bound from E' alone was only2nu; cancellation
  of its first Euler component is what strengthens it.
- For the longer ladder, k>=14nu and
  e0=h16+h18 r2+r4 has v(e0)>=15nu+1.
- H18 at1 makes a2=1 exactly. A unit a3 leaves no H16 witness.
  A nonunit a3 forces H17 at the actual r. H16 at0 or d then
  reduces, for nu1, to a quadratic with nonsquare discriminant10
  modulo19; for nu>=2 its constant has unique valuation1.
- With H18 noncenter and nu>=2, a3 unit again leaves no H16 witness.
  The nonunit case reduces to the single finite-field expression
  16-12lambda2+12kappa(lambda-1), with kappa0,2,4 and lambda0,1,2.
  Its zeros would require kappa14 or9, which are unavailable.
- At nu1, a3 unit is NOT automatically excluded for arbitrary k15.
  The proof excludes it only in the separate deep regime k>=17,
  where h16 is definitely nonzero of valuation4. Keeping that
  distinction avoids silently assuming h16 never vanishes.
- Deep-regime errors are a2 error>=3, h16 error>=6, a3 error>=4.
  Dividing the H16 equation by r3 leaves an error>=2.
  H18 fixes r modulo19^3 near one of two rationals. Each surviving
  exact comparison disagrees at valuation2, so its H16 residual
  has valuation1, contradicting that error bound.
- The exact-mirror case uses zero errors and is included separately
  in the same contradiction. No division by delta is made there.
- The six pairs(C,19A) and the two difference numerators were
  reconstructed by hand from the correct plus4a3 X in D4.
  No symbolic program or larger digit table generated this certificate.
- Indispensability uses only rational common-root supports, so it
  needs neither the earlier unreviewed global factor barrier nor a
  claim that all derivative gcds have been classified.

Other approaches considered and bounded:
- Literature searches for four rational or real recycled roots did
  not supply a verified exclusion of four rational witness values.
  Results assuming ALL roots real cannot be substituted.
- Marashdeh arXiv2608.14726 was read in the introduction through
  Theorems A--E, support definitions and scenario boundary, plus
  relevant Theorem5.9 and Remark5.10 passages. The one-nonzero-root
  descent determinant and two-element coefficient-support result
  do not settle our four-value case. Its claims are not proof inputs.
  The paper was not downloaded locally; no cache hash is invented.
- A possible Galois-group argument from local degree14 plus one
  root in a global degree15 factor was considered and not used.
  Even a large global Galois group would not itself contradict
  the rational witness conditions. No classification was imported.
- Prime5 still has the corrected bad-base-degree4 obstruction.
  The 2011 erratum was rechecked directly; no second-prime descent
  or contradiction is proposed here.
- Global rational heights are unrestricted. P-adic closeness alone
  does not make the two rational roots exactly mirrored. RC2
  explicitly retains two possible finite depths.

No mathematical computation, CAS, mask enumeration, digit tree,
J16 work or rerun of the old three-value certificate occurred.
Only hashing and administrative JSON creation are executable here.
No Git/shared edits, contacts, charges, access bypass, spawning,
or separately billed API.

Authoritative account-wide telemetry on this continuation is23%
total weekly used,10080-minute window,reset1792745187.
The ceiling remains90% total with integration reserve.

This packet requires two fresh independent nonconstructor whole
audits. Only root may promote any of RC1--RC3 after substantive
objections are repaired. Earlier frozen review and construction
packets are validated by metadata during this freeze.

