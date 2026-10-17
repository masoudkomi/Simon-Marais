# HC1–HC3 whole R2 inference and issue ledger

2026-10-17 UTC. Initially blind NONCONSTRUCTOR review by
`/root/review_2022_complexity_r2`. Main SHA256
`e76949699e6f6bfbcf58a4f0c8a8f7e3affa903a92dc5ec61b92887e4fe07bff`.
All forty constructor obligations are covered individually below, followed
by twelve additional adversarial checks. **Zero substantive defects
identified; no author repair requested.** PASS means the written claim
survives this audit, not that a stronger bridge has been proved or that
coordinator acceptance has occurred. No new HC peer finding was read.

## Complete forty-obligation mapping

1. **HCR2-01 / R3-01 — PASS, official count.** The actual B4 target has
   all integers n>=2 and a fixed polygon. Official B4 notes resolve the
   orientation convention. The marked dictionary uses commutation
   classes; no word/history or symmetry quotient is substituted. C(1)
   remains auxiliary and n=0 is not introduced.
2. **HCR2-02 / R3-02 — PASS, partition domain.** Every m_i is positive,
   groups are consecutive initially, and B is full block reversal with
   within-color order retained. OP1's adjacency/crossed-set proof uses
   precisely that initial-block condition; arbitrary recoloring would
   not inherit it.
3. **HCR2-03 / R3-03 — PASS, exact accepted authority.** Complete DC,
   G, V, OP, U bodies and five MD/JSON acceptances were freshly read.
   G gives all-integer fixed-D k_D, L and monotonicity. U gives its exact
   scalar bound. V3 E/R remain extra hypotheses. Old own G authorship
   is disclosed rather than independently recertified.
4. **HCR2-04 / R3-04 — PASS, roles.** A is the new HC constructor;
   their old strict LOCAL authorship and G-review roles are explicit.
   I did not construct HC. I authored G, reviewed V/OP and local inputs;
   these older roles are explicit. Root's generic assignment supplied
   no new HC inference and is not accepted proof authority.
5. **HCR2-05 / R3-05 — PASS, IDs/acyclicity.** The lth s_r occurrence
   is well named. All generating relations are forward in a finite
   representative, hence no cycle; K=binom(m,2). At m=1 the event set
   is empty rather than a fictitious single coordinate.
6. **HCR2-06 / R3-06 — PASS, heap invariance.** A commuting swap has
   index distance>1 and changes neither occurrence numbering nor any
   noncommuting relative order. The transitive closure is therefore
   invariant on A, without choosing a canonical sweep.
7. **HCR2-07 / R3-07 — PASS, BOTH heap directions.** A's representatives
   extend P_A. Bring the desired first element of another extension
   left past incomparable elements and induct. Every such interchange
   is an allowed generator commutation. No braid relation identifies
   two distinct internal classes and no extension multiplicity is
   counted as C(m).
8. **HCR2-08 / R3-08 — PASS, actual ranks.** On rank r the ordered
   list contains indices r-1,r. Each generating pair shares a rank,
   including two events of equal index, and every pair on one list is
   a generating relation. Their closures coincide. Original-strand
   orders are not mistaken for smoothed-rank orders.
9. **HCR2-09 / R3-09 — PASS, exact OP1 usage.** Current neighboring
   ranks are adjacent at an erased event; every outside track begins
   and currently lies on one common side of both. Crossing at most
   once gives equality of crossed sets and hence of gap indices. The
   converse about arbitrary prefix matches is never assumed.
10. **HCR2-10 / R3-10 — PASS, whole isotonicity.** Actual external
    counts lie in 0,...,a and cannot decrease along any directed rank.
    The exact rank-list/heap identity then yields isotonicity on the
    entire poset, for contacts toward either neighboring rank and
    with repeated values allowed.
11. **HCR2-11 / R3-11 — PASS, full recovery.** The common index puts
    both ends in named gaps; A fixes the whole mixed-neighbor ID list
    in each gap. DC recovers matching and original labels. No within-gap
    shuffle or factorial remains unrecorded.
12. **HCR2-12 / R3-12 — PASS, class injection and SUM.** Q,A_i,f_i
    are class invariant and determine the full DC decoration. Summing
    Omega over each actual A_i once, then Q, gives the upper bound.
    Invalid abstract records only overcount. The lower B<=C is the
    actual accepted DC section, not arbitrary f-lifting.
13. **HCR2-13 / R3-13 — PASS, special Q.** Two parallel color families
    give the unique m-by-a grid. On every A rank, B tracks have the
    common order B_1,...,B_a. This special common order is not asserted
    for a general outside multicolor projection.
14. **HCR2-14 / R3-14 — PASS, special injection.** An actual B(1^m,a)
    class restricts to one A and one isotone f over that fixed Q. B–B
    crossings are forbidden and there is no missing B internal class.
15. **HCR2-15 / R3-15 — PASS, level sorting.** Weak isotonicity forbids
    a relation from a higher to a lower level. Concatenate arbitrary
    extensions of the equal-level induced subposets. This gives one
    extension of P_A, including unused levels and level ties.
16. **HCR2-16 / R3-16 — PASS, every adjacent step.** At stage j the A
    block is contiguous after B_1,...,B_j. Its local state is that of
    the chosen internal representative. Bubble B_(j+1) across all m A
    labels, stopping before earlier B's. A order and B order survive
    the completed bubble and the stage invariant propagates.
17. **HCR2-17 / R3-17 — PASS, actual reduced word.** The end list is
    B original order followed by A reverse order. There are exactly
    K A–A and ma A–B crossings, zero B–B crossings, and length K+ma
    equals this permutation's inversion number. It is an actual
    reduced class with the required full boundary.
18. **HCR2-18 / R3-18 — PASS, both prescribed ports.** Before each
    level-j A event every smoothed A rank has crossed the full B prefix
    of length j and no other B. Both endpoints therefore lie in gap j.
    Global position shifts during earlier bubbles do not shift this
    canonical external gap value.
19. **HCR2-19 / R3-19 — PASS, no history overcount.** Every chosen
    level extension realizes exactly (A,f). The already proved complete
    record injection makes all equal-record outputs one class and
    distinct records distinct. Thus both directions of H=B are proved.
20. **HCR2-20 / R3-20 — PASS, special boundaries/counterexample.**
    a=0 has one zero map per A; m=1 has one empty map for any a;
    a=1 is a full m+1-label reversal. The coarse word23212 on A,A,B,C
    has only equal-prefix gaps0,2, with both actual lifts, whereas
    H_2(2)=3. The candidate preserves this generic-Q obstruction.
21. **HCR2-21 / R3-21 — PASS, exact selected endpoints.** For even m,
    odd ranks end at m-1; for odd m, even ranks end at m-1. Each adjacent
    pair contains exactly one selected rank, including the boundary
    pairs. At m=1 the selected set is empty.
22. **HCR2-22 / R3-22 — PASS, chain partition.** Assign an event to
    its unique selected endpoint. The rank list is a chain of length
    x_(r-1)+x_r, and these event sets are disjoint and cover all K.
    Both incoming neighbor directions are included once, not twice.
23. **HCR2-23 / R3-23 — PASS, chain count.** Nondecreasing length-k
    lists in a+1 levels correspond to weak compositions and number
    binom(a+k,k). Restricting a full heap map to a partition of its
    events is injective. Dropped cross-chain comparisons give H<=T.
24. **HCR2-24 / R3-24 — PASS, lower H.** The constant zero map is
    valid for each actual A. This proves C(m)<=H_m(a) with no generic-Q
    section and with only one empty map when m=1.
25. **HCR2-25 / R3-25 — PASS, strict H<T.** Every generator occurs
    because missing s_r preserves the first-r position set. For even
    m>=4 use generators1,2 in selected chains1,3; for odd m>=5 use2,3
    in chains2,4. Their events are comparable. Constants a on the
    earlier chain and0 on the later chain violate heap order when a>0.
    Each actual summand is strict. For m<=3 one chain is the whole heap.
26. **HCR2-26 / R3-26 — PASS, strict T<V.** The ratio 1+a/(k+1)
    decreases, so F(u+v)<=F(u)F(v), strictly for positive a,u,v. The
    selected degrees partition x's into disjoint neighbor pairs and
    possibly one singleton. For m>=3 some positive pair exists in
    every A, giving the stated strict SUM comparison.
27. **HCR2-27 / R3-27 — PASS, hand identities.** m=2 has one event
    and H=T=V=a+1. The two m=3 classes121,212 each have a three-event
    heap chain, giving H=T=2 binom(a+3,3). a=0 gives all weights1;
    m=1 gives all counts1. These are not numerical certificates.
28. **HCR2-28 / R3-28 — PASS, balancing.** For u>=v+2 the stated
    ratio has positive denominators and differs from1 with numerator
    a(u-v-1)>=0. A balancing move strictly lowers the integer sum of
    squares, so it terminates while never lowering the product.
29. **HCR2-29 / R3-29 — PASS, exact integer means.** K/q is m-1
    for m even and m for m odd, so the terminal balanced tuple is
    constant. Sum the uniform product upper bound over actual A.
    Realizability of the maximizing degree tuple is unnecessary.
30. **HCR2-30 / R3-30 — PASS, sparse S and E.** One selected endpoint
    per event gives S recorded contacts. Every selected track has
    a_i+1 named gaps, giving E_*, without the old all-track E_+ or2S.
    Forgetting fixed row totals is an upper relaxation only.
31. **HCR2-31 / R3-31 — PASS, unselected order.** Fill selected ID
    lists in their gaps; each missing partner uses the same index.
    Full A_i fixes its unselected merged two-neighbor order. Bad
    monotonicity/prefix/realization arrays can be discarded without
    any extra multiplicity or false sufficiency assertion.
32. **HCR2-32 / R3-32 — PASS, sparse invariance.** The sparse counts
    are extracted from the invariant DC decoration and are independent
    of sweep choice. Recovery of that complete decoration proves an
    injection on the actual commutation quotient.
33. **HCR2-33 / R3-33 — PASS, composition domain.** S>0 forces a
    block m_i>=2, hence one selected track and E_*>=1. Then the top
    E_*+S-1 is at least S. For S=0 the single empty record is explicitly
    defined, avoiding a negative-top binomial.
34. **HCR2-34 / R3-34 — PASS, finite degeneracies.** D=1 has B(n)=1,
    a=0 and exact HC1; the weaker composition bound can be loose.
    All singleton blocks give B=C(n), S=E=0. m_i=1, auxiliary n=1
    and empty selected lists have one record, not zero choices.
35. **HCR2-35 / R3-35 — PASS, parity corrections.** Expand
    floor(m_i/2)=(m_i-delta_i)/2 before summing. This gives every term
    in (16), including +n and -sum delta_i. The correction is O_D(n)
    at fixed D, yielding all four limits in (17).
36. **HCR2-36 / R3-36 — PASS, both normalizations.** B_D(p)<=B(m_i)
    <=B_D(p+1) and Dp/n→1 give ell_D after n^-2 normalization. The
    official limit applied to each growing m_i gives L sum m_i^2/n^2
    →L/D. Neither step uses a uniform modulus in D.
37. **HCR2-37 / R3-37 — PASS, entropy binomial.** For sufficiently
    large n at fixed D>=2, M=E_*+S-1>=S>0. The binomial theorem at
    probability S/M gives the entropy bound; s=0,M use the usual
    endpoint convention. M/n^2→1/2 and S/M→1/D give g_D exactly.
38. **HCR2-38 / R3-38 — PASS, scalar signs.** Combine logarithms
    with the accepted limits to obtain L<=ell_D+L/D+g_D. Use ell_D<=L,
    rearrange only for D>1, and replace L/D by the larger U/D. No
    reversed inequality or circular existence argument appears.
39. **HCR2-39 / R3-39 — PASS, strict comparison and asymptotics.**
    Direct entropy expansion gives f=h(p)-h(p/2)+p. Its difference
    from g is strictly concave with zero endpoint values; the exact
    G''<0 proves positivity. The small-p expansion gives G(p)/p→1/2,
    preserving rather than halving the common logarithmic leading term.
40. **HCR2-40 / R3-40 — PASS, source/remaining gaps.** Actual finite
    heap and weak order-polynomial hypotheses hold; their classical
    attribution is explicit. Fixed-poset volume asymptotics, generic-Q
    sufficiency, quadratic weighted gain, effective E/R and a value
    formula are not supplied by these sources or inferred here. All
    earlier bytes are preserved; no mathematical code or peer finding
    supplied this initially blind reconstruction.

## Additional adversarial checks, not additional author hypotheses

41. **HCR2-41 — PASS, original labels under construction.** The B
    bubble crosses each current A label once, even though the current
    A order changes between stages. Deleting B recovers the exact
    chosen A representative; no adjacent local swap becomes invalid
    through an external strand lodged inside the block.
42. **HCR2-42 — PASS, stages a=0 and a=1.** The last stage j=a has
    no further B bubble; all its remaining internal events are still
    adjacent. For a=0 the construction reduces to A. For a=1 the last
    B singleton is the largest label and the final list is full reverse.
43. **HCR2-43 — PASS, same-index does not become sufficient.** In
    the actual two-versus-three example both endpoint indices could
    numerically be1, but their crossed sets differ. The sparse code
    treats that as an invalid record. The special grid's common B
    order is the additional fact used in its explicit inverse.
44. **HCR2-44 — PASS, every strictness witness is legal in the
    relaxation.** The constant assignments used to separate H from T
    are nondecreasing on all selected chains even if a chosen event
    is not first/last in its chain. They need not be actual maps or
    tilings; their sole role is witnessing a missing cross-chain order.
45. **HCR2-45 — PASS, exact summed strictness.** Each actual A
    contributes a strict finite integer inequality in the asserted
    ranges; summing a finite nonempty set preserves strictness. This
    does not give a uniform relative gap or a quadratic log gap as
    m,a grow. The candidate states exactly that limitation.
46. **HCR2-46 — PASS, degenerate balancing parameter.** u>=v+2
    forces u>=2, so a+u and v+1 are positive even at a=0. The step
    is then equality in the product, but the sum-of-squares decrease
    still makes the finite procedure terminate.
47. **HCR2-47 — PASS, generic outside interaction.** Outside colors
    may cross each other and have different orders along neighboring
    tracks. Only a_i's common cardinality, OP1 necessity and the
    existing complete DC decoration are used for the generic upper
    code; no staged grid construction is transplanted to that setting.
48. **HCR2-48 — PASS, no entropy division at M=0.** Finite S=0 is
    handled by J=1 separately. In the fixed-D limit S grows like
    n^2/(2D), so M>=S>0. Possible small-n composition endpoints do
    not enter the displayed s/M formula without qualification.
49. **HCR2-49 — PASS, D=2 scalar endpoint.** The accepted full grid
    has ell_2=0, g_2=1/2 and the rearranged bound is L<=1. It is a
    valid coarse upper bound, not an asserted sharp evaluation. D=1
    remains a finite coding case and is excluded from division by D-1.
50. **HCR2-50 — PASS, literature index shift and closures.** The
    source order polynomial counts weakly isotone maps to a finite
    chain. Levels0,...,a require a+1, not a. The poset is finite and
    acyclic by direct construction; no general directed-cycle claim
    or fully-commutative-element theorem is imported.
51. **HCR2-51 — PASS, prior U and effectiveness limits.** The exact
    accepted rational U is used only after existence of L. Its older
    numerical certificate and the external cutpath proof are not
    rerun. Neither this numeric upper bound nor G's qualitative
    recovery discharges E/R or computes any fixed-D entropy.
52. **HCR2-52 — PASS, preservation and initial blindness.** Only
    the unused assigned R2 prefix is written. The constructor freezer
    is text input, not executed. Administrative SHA/JSON verification
    is not mathematical evidence. The new HC R1 prefix is excluded
    from every read/hash collection until this complete initial freeze.

No proposed correction or new mathematical result is included. If a
later peer comparison reveals a substantive issue, it must receive a
versioned author repair and both affected reaudits; this initial ledger
must remain byte-identical. Pending coordinator reconciliation, HC1–HC3
retain candidate status. Primary read limits and role disclosures are in
the separate source-check report; all hashes are in the immutable freeze.
