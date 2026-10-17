# Coordinator signed power-gap return: construction record

2026-10-17 UTC. Status: candidate proof - unverified.

The literature return first examined the diagonal class-number
conditions of Mihailescu and the finite Vandiver/irregular-index
computations of Hart--Harvey--Ong. Those possible attributed
corollaries require a separate source and hypothesis audit and are
not premises of this packet.

The elementary construction instead isolates a gap between consecutive
q-th powers for G_s(t^q), including negative t and odd q. Exact
block gcds then force a common prime. The multiplicative order q
forces every common prime other than q to be at least 2q+1,
which excludes small cofactors. The remaining m=q^2 case is
eliminated by signed LTE. Iterating the last q-block once gives
the prime-power restriction without assuming an unrestricted
classification.

The proof was developed by hand. No Python test cases, trial scans,
finite-field tables or CAS computations were used. The known
m=q=3 examples were checked against the hypotheses by reasoning:
they lie outside the small-cofactor and a>=2 restrictions.

The original positive-base literature already covers a stronger
divisible-term-count statement in its own domain. We record that
overlap and make no novelty claim. This packet deliberately states
the signed cases and proves the required inequalities and gcd/order
steps, rather than importing a positive-base theorem for negative x.

All prior candidates, accepted proofs and unsuccessful approaches
remain unchanged. Two fresh nonconstructor whole reviews are pending.
