# R5 constructor check, not an independent review

2026-10-17 UTC. Author `review_2017_coarsening_r1`.
**Candidate proof - unverified.** This is construction evidence only.
Two OTHER fresh initially blind whole audits remain required.

I reconstructed the selector recurrence twice: directly from D_j(w_j)=0,
and by adding the largest center index to F_I. The second route fixes
the sign F_I=(-1)^|I|d(I;Z). The selector I may contain nonunit center
coefficients, so it cannot be replaced by the unit support used in PP1.
All possible I are handled, not the64 odd-support cases from PN.

The term1-d=-p is the only reason q_I is F_I(d)/p; it leaves the crucial
extra exponent nu_w+1 in the descent divisibility. Every beta_j is an
ordinary integer, so neither actual rational coefficient denominators
nor the divided center equality conceal an inversion modulo p.
If the positive minimum were empty, the exact coefficients would already
equal the collapse and contradict positive d(I;d). This handles the zero
and two-value endpoints without assigning v(0) a finite value.

The triple patterns were checked explicitly: ++ permits123, +- permits
132/231, -+ permits213/312, -- permits321. Each block has distinct values.
Only disjoint blocks are counted independently. Six triples and one pair
give20!/(2*3^6), with all boundary comparisons ignored. Exact multiplication
checks1458*1668657070080000=2432902008176640000=20!, and repeated
multiplication gives19^12=2213314919066161. The strict inequality yields
nu_w+1<=11, hence nu_w<=10. No mathematical program supplied these values.

The generic carrier proof has its own lower-exponent checks. J>=d/2
ensures(p-2)/(J-1)<2, and2<=h<p makes every binom(h,k),1<=k<=h, a unit.
The fractional rescaling uses pi^(J-1)=p in an extension. Global minimal
polynomial divisibility is used only after the exact local evaluations.
The M=J-1 case is not omitted: the last equal-degree derivative has
unit trace coefficient-(J-1), whereas the local Eisenstein factor's
trace is divisible by p. Neither local factor rationality nor a large
Galois group is assumed.

R5D's proof uses exactly the accepted RC2 conclusion that H18 cannot
have center1 under the full repeated-root LADDER. It then obtains an
actual rational noncenter witness from the contest and applies the
accepted PN4. This is not a contradiction for the old low-order-only
barrier family, which was never a full witness example. Distinct2R
roots and a partial ladder remain outside the claim.

R5E uses TA1 at m3,4,5,6,7 with units a13,a11,a9,a7,a5. Each step's
earlier-even hypotheses are supplied by the previous step. The dropped
a3 was used only in the old TA2 final H16/three-cover argument; that
argument is not needed once the ladder is excluded by R5D. Sole rational
center becomes exact full gcd X-1 because every nonrational root lies
in the unrecycled rational Eisenstein carrier and1 is simple.

An unfrozen formatting defect joined two sentences as `proves(6)+without`;
it was corrected before this checkpoint. I also replaced the ambiguous
phrase "actually needed positive witness" by "selected actual positive
witness": no one low-valuation root is asserted individually essential.
The result constrains every cover collectively, not each root separately.

No CAS, code test, mathematical scan, finite-certificate rerun or empirical
absence argument was used. All30 obligations are exposed for independent
challenge, and all earlier frozen packets remain unchanged.
