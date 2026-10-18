# CT constructor hand reconstruction and boundary checks

2026-10-18 UTC. Candidate-unverified, not an independent review.
No mathematical program, enumeration, CAS or certificate replay ran.
The 64 obligations are supplied separately; the points below record
the actual adversarial hand checks, including possible decoder failures.

1. **Whole-context source invariant.** At absolute time s the total
   tape height is s mod2. During an arbitrary selected factor, its
   full prefix height stays in one translated R-band, so the other
   full prefix height stays in the opposite band enlarged by1. This
   is valid at BOTH source phases and includes the first and last
   other-tape vertices. Restarting both middle heights at zero changes
   only translations. Thus old middle runs have the asserted bounds.

2. **Marker schedule at both phases.** At phase0, LR writes selected0,
   other1 and RL writes selected1, other0. At phase1 the roles of LR
   and RL reverse; the prescribed reversed schedule therefore produces
   exactly the same U,V. Every block has even length4K. Multiple earlier
   insertions change neither the next original source bit nor either
   original coordinate height. Swapping physical tape names is valid.

3. **Selected marker isolation.** Markers are inserted at internal1|0
   valleys. Their initial0 is preceded by1 and final1 followed by0.
   All old selected runs have length<=R<K; all produced selected long
   runs have length EXACT K. Consecutive selected valleys are separated
   by original letters, so the inserted pairs cannot merge. The decoder
   recovers not merely X but the original site of each inserted pair.

4. **Other-tape mergers.** This was checked against the potentially
   worst cases: two insertions at the same other-tape position, inside
   one old run, across an empty other block, or at its boundary. Each
   inserted word is1^K0^K. Successive K-runs of the same bit always
   have an intervening opposite K-run. Thus one produced maximal run
   cannot contain two inserted K-runs. A long run cannot consist only
   of old bits because insertion never removes an original opposite
   letter, and old runs are<K. Deleting K from each long run restores
   the original word even when the insertion merged with old letters
   on both sides. No positional information inside identical letters
   is required. Boundary records separate the middle from outside runs.

5. **Several intervals.** Disjoint selected letter intervals give
   ordered disjoint witness-time intervals. If they are adjacent and
   no other move intervenes their endpoints can coincide. Their other
   coordinate intervals are still ordered and nonoverlapping, possibly
   empty. Two endpoint arrays label their pairings by their common
   chronological order. Decoding yields the original word pair and
   hence its deterministic maximum packing and witness. There is no
   unrecorded permutation or matching of exterior ports.

6. **Floors and constants.** For one factor, M>=ell/(2R)-2 and
   J=floor(M/q)>=ell/(2Rq)-2 because q>=2. Both J=0 and M=0
   give binomial1 separately. With q=2^(4K+1), each comparison length
   costs at most2^(4KJ) and the binomial supplies q^J, leaving2^-J.
   Since K/R<=3 and q>=8192, N<=2n in both uses. The four floor-loss
   factor times the two-side and boundary factors gives16(n+1)^5.

7. **Variable collection boundary entropy.** In the mass event the
   original selected length W>=eta*n and m<=W/T. The deliberately
   weaker valley count W/(2R)-2m leaves W/(4R) ifT>=8R. Nondecreasing
   2m endpoints in0..N have binomial(N+2m,2m) possibilities per tape.
   Squaring, then summing at mostn+1 choices ofm, gives B(T) rather
   than an erroneous O(n log n/T) rate. The increasing-function check
   in the main proves the bound at the real endpoint2n/T. No assumption
   that all pieces have equal length is used.

8. **Both tapes and covered mass.** The event for summed packing
   mass implies a one-side event at epsilon/2. This accounts for the
   factor2 and exponent loss in (6). Longest-first interval selection
   charges at most3d letters to each disjoint selected d-interval,
   proving U<=3P without a bound on overlap multiplicity. For the
   coverage event use epsilon/3 in (6); do not reuse its exponent with
   unchanged epsilon. Both normalized variables are<=1, so the stated
   expectation order is T first for fixed epsilon, then n, then epsilon.

9. **Accepted CN operative middle boundary.** The slow schedule is
   indexed by J_h J_h, each entry realized by an even elementary history
   (including beta0=RR). The separator between these two lists is
   exactly the right-tape v/v boundary and has source phase0. Thus the
   extra right pad2d can really be inserted there. A bare assertion
   that (u,v^2) is feasible would not alone establish this boundary.
   The entire accepted body, not merely its abstract claim, was read.

10. **New cut clusters.** From the displayed fast/slow padded schedules,
    their first and last pads are explicit even history blocks. Removing
    them from chosen prefix/suffix histories produces actual C,D at
    phase0. The intervening output is(s^(2p),s^(2d)). Splitting it as
    in (31) changes the first tape prefix by2e and the other by-2e,
    while its degree stays2(p+d). All four exponents are>=0. Adjacent
    base centers differ24t, versus cluster diameter4t; all clusters
    are disjoint. The product (10m+1)(2t+1)>20tm=n_m/84 is strict.
    Prefix/suffix exponents60m..80m and90m..120m also check m=1 and
    the endpoints j=2m,12m. They leave actual nonempty endpoint pads.

11. **Cyclic factors, fixed periods and their mass.** All periods are
    balanced. Their old height ranges contain[0,1], so adding01 pads
    does not alter their extrema. A period-length cyclic factor visits
    all height residues, hence no such range-r factor exists after h
    is fixed with2h-1>r. The new flat's exponent matrix(7,5;7,10)
    is injective: difference5j, then i. At each macrodegree only M+1
    outputs exist, not all reordered histories. Its probability and
    mean contribution bounds leave all other high-cut families uncounted.

12. **Short-separator hand counterexample.** Schedule(36) works even
    with s0=0; its two isolated L moves then form one LL loop. For
    N>=3 and1<=a<=N-2, prefix X_a uses r=a>=1, second parameterN-a,
    whereas Z_a is RL followed by r=N-a-1>=1 and s0=a-1>=0.
    They have degrees2N and2N-2; adding B0's two letters gives4N.
    Literal products on both tapes equal(s^N,t0^N). Different a give
    different first-factor lengths and therefore distinct inputs.
    This checks a genuine unbounded fibre, not only many histories.

13. **Exact remaining arithmetic/counting inference.** CT2 counts an
    entire positive-packing-mass event, so it improves on a rare-family
    or one-piece statement. It still supplies no cover of high-cut
    contexts. CT3 refutes a deterministic cover by arbitrarily long
    fixed-range pieces at one universal positive density. Its specific
    outputs remain exponentially rare, which alone proves no bound on
    high-cut mass. No delta/mu alternative, exactlambda, ratio transfer
    or annual claim is made. No old source body is silently treated
    as a new independent certificate.

Potential targets for the two OTHER reviewers: the other-tape long-run
decoder; endpoint-array identification of all multiple blocks; quantifier
order in CT2; the explicit CN slow boundary; removal of actual pad blocks
rather than mere height-zero words; and the fixed-time cluster count.
