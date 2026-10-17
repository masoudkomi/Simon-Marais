# R9 constructor adversarial checks

2026-10-17 UTC. **Candidate proof - unverified.** These are hand
construction checks, not either required OTHER whole review.

1. **Real nodes versus real roots.** Applied the interpolation theorem
   to values0,1,r,s only. It constrains evaluations of a real polynomial
   and makes no assertion about locations of its other roots. Its
   hypotheses are satisfied by Q coefficients without an all-root
   rationality assertion.
2. **Twenty-four rather than twenty-three.** Every order2..19 supplies
   one selected entry, all four order0 roots are included, and BOTH
   actual order1 roots are entered. A selected-scenario matrix with
   only one order1 root would lose one unit of the run bound. The
   second actual double root is essential to the stated four-run proof.
3. **Deletion at an endpoint.** An odd block of length2a+1 loses its
   last entry and has length2a, or disappears if a0. Since deleting
   never joins blocks, no new odd interior block is created. An initial
   block beginning0 is untouched even if its length is odd.
4. **Exact dimension and empty final columns.** After K<=3 deletions,
   n=24-K is21,22,23 or24. The allowed polynomial degree is n-1,
   at least20. Entries stop at19 but Pólya holds through n-1 because
   total entries already equal n. An unexamined empty final column
   does not invalidate the theorem or add a false derivative condition.
5. **Multiple available witnesses.** Extra derivative zeros are omitted
   from a selected incidence matrix; f still solves its homogeneous
   system. Applying R9A to every selection is what allows the endpoint-
   whenever-possible proof of R9B. No canonical selector is presumed.
6. **Support and gcd.** A rational-witness assumption alone would not
   exclude additional algebraic gcd roots. The exact accepted GLOBAL
   carrier input does that here. At0,s gcd multiplicities can be1 or2,
   so R9B uses divisibility by X²(X-s)² and does not call each gcd
   linear or each forced-interior order essential at a single node.
7. **Ordinary geometry.** The six possible interior pairs are left
   separate. Congruence s/r2 is never converted to r between0,s or to
   any other real inequality. Both rational order diagnostics in the
   failed-routes file were checked algebraically without a program.
8. **Parity at low orders.** r is simple, has H2/H4, and cannot share
   H3/H5. Its2 and4 blocks are isolated. Center1 cannot shareH2/H4,
   so its3 block is isolated. Its5 and19 can join other orders and
   are not automatically odd singleton contributions.
9. **Sign in the exact identity.** Since2r-s=-delta,
   f'(2r)=-2delta U(2r)+delta²U'(2r). Dividing by2 and subtracting
   eE(r)/r gives the negative delta bracket in(5). The left exponent
   is e+1. This yields Delta=(e-2)nu-1+v(W'), not the estimate for W.
10. **Nonzero logarithmic denominators.** g's constant uniquely wins
    at2r, the factor2r-1 is a unit, and r is nonzero. Therefore B,U
    at2r are nonzero even if the actual double root s equals2r.
    delta0 itself is handled before any division by delta.
11. **Cubic reflection.** Expanding the two reflected forms gives
    z³-12z+16 and z³-3z-2. Their inflections are0; the unreflected
    forms have coefficient-6z² and inflection2. At z1 all four second
    derivatives are plus/minus6b, never zero modulo19.
12. **Strict and tied depths.** sigma<nu implies first W' term has
    valuation nu+sigma+1<=2nu, below every later term>=2nu+1.
    At sigma=nu this argument deliberately stops. T4 allows tied
    cancellation and W'=0 in the exact delta0 case.
13. **Smallest Taylor endpoint.** At m7, l3, nu1 the last W' term
    has valuation4, while the required comparison threshold is3.
    At every other permitted l or larger nu it remains at least that
    threshold. A leading coefficient l does not vanish modulo19.
14. **Cubic depth and weighted depth.** Cubic Delta lies in the
    half-open interval[(e-1)nu,e nu); weighted finite Delta is>=e nu.
    No assertion of disjointness of all original R8 alternatives is
    required: the contraposition first assumes EC fails. EC can be
    compatible with other necessary conditions.
15. **Origin exchange.** The accepted exact formula multiplies delta
    by the unit(1-s)^-1, so a depth obstruction cannot change sign or
    become a contradiction under the other double-origin frame.
16. **Nonclosure.** A hand formal m4 incidence word has exactly four
    odd interior blocks. It defeats a putative inference from the new
    run lower bound alone to full branch exclusion. It is not called
    an actual polynomial, local lift or counterexample.
17. **Old depth10.** A cubic-only upper depth follows from the newly
    proved exact formula PLUS nu<=10, if one wants it. There is no
    global maximum collision/height bound from the old MINIMUM
    selected depth; T4 and essential-center cases stay unrestricted
    by such an upper bound.

No mathematical executable, symbolic package, numerical routine,
mask enumeration, native CAS job or old-certificate rerun was used.
The freeze script checks only labels, file records and byte hashes.
The remaining unproved branch contradiction is kept explicit.
