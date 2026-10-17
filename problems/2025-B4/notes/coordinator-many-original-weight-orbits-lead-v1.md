# A quantitative continuation of the two-moment selection argument

2026-10-17 UTC. **Research lead / candidate deduction - unverified.**
Root constructor of this quantitative continuation; the underlying
cubic/fifth relation and universal two-orbit packet are B's construction
with root's earlier cubic lead. Those packets still need independent
audits. This note is not an accepted theorem, a novelty claim or a
Diophantine exclusion. No mathematical program or scan was used.

Retain the EXACT definitions and hypotheses in the frozen UW candidate,
including prime p>=37, S of size at least p-4, m1 nonzero, and

    u=f*m1, v3=f^3*m3, v5=f^5*m5,
    7v5+800u²v3+4608u^5=0.

The function w3=m3/m1³ has fibers of size at most6 on S. The following
proposed counting argument is additional; it does not alter any frozen
UW statement or proof. It uses all actual INTEGER positive pair elements
and counts their conjugacy classes, rather than assuming all parameters
give distinct vectors.

## Complementary branch: f is nonzero everywhere on S

Then u:S->F_p^* is nonconstant, by the exact UW/FS polynomial argument.
Choose s whose u-fiber has smallest size, put a=u(s)!=0, and let

    T={t in S:u(t)!=a}.

Since u has at least two values, |T|>=ceil(|S|/2). For each t in T
use the actual positive, original-weight element theta_(s,t) in UW.
If a collection of these belongs to ONE Galois orbit, its two invariant
ratios have fixed values C3,C5. Therefore, for every such t with U=u(t),

    v3(t)=v3(s)+C3(U-a)^3,
    v5(t)=v5(s)+C5(U-a)^5.

Substitution in the displayed pointwise relation forces U to be a root of

    P(U)=7v5(s)+7C5(U-a)^5
          +800U²[v3(s)+C3(U-a)^3]+4608U^5.

This has degree at most5 and CANNOT be identically zero. If it were,
its U^4 and U^3 coefficients would give, respectively,

    7C5+480C3=0, 7C5+240C3=0.

Their suppressed factors -5a and10a² are units at p>=37. Subtraction
forces C3=0 since240 is a unit, then C5=0. The U^5 coefficient would
be4608!=0, contradiction. Hence each orbit uses at most FIVE U-values.

For a fixed such U, the first ratio fixes v3(t). Then
w3(t)=v3(t)/U³ is fixed, so there are at most SIX corresponding t.
Thus ONE orbit accounts for at most30 members of T. It follows that
these actual original-weight positive free elements represent at least

    ceil(|T|/30) >= ceil(|S|/60) >= ceil((p-4)/60)

different Galois orbits. Distinctness of the ratio tuple is only a
NECESSARY consequence of conjugacy; the count does not assume it is
a complete invariant or a bijection of pair parameters and elements.

## Zero direct-action branch

Suppose f(s)=0 at some s in S. Then b=psi_s is an ACTUAL positive
half-weight element of I_f with m1(s)!=0. For every h in G except-1 set

    theta_h=b+sigma_h b.

These have original weight p-1, complement2N, coefficients0/1/2 and
nonzero first inverse moment. If w3(s)!=0, their cubic invariant is

    w3(s)*(h³+1)/(h+1)³
       =w3(s)*(h²-h+1)/(h+1)².

Each value has at most TWO h-preimages: the numerator cannot be a
scalar multiple of the denominator, since comparison of leading and
linear coefficients would force -1=2, excluded at p>=37. This gives
at least ceil((p-2)/2) conjugacy classes among the p-2 parameters.

If w3(s)=0, the UW moment relation gives w5(s)=-4608/7!=0. The fifth
invariant is instead

    w5(s)*(h^5+1)/(h+1)^5
      =w5(s)*(h^4-h³+h²-h+1)/(h+1)^4.

Each value has at most FOUR h-preimages. An identically zero equation
would compare leading and cubic coefficients to force -1=4, excluded
at this threshold. This gives at least ceil((p-2)/4) free classes.
The positive scalar2b is included at h1; h-1 is excluded before any
moment division. The equivalence of h and h^-1 parameters is allowed,
so the argument does not falsely count every parameter as a new class.

This branch gives more than the proposed lower bound ceil((p-4)/60).
Combining both branches would therefore yield that bound universally.
It is weaker than UW's proposed TWO classes at some small primes; if
both proofs pass review, the combined bound would be
max(2,ceil((p-4)/60)), not a replacement weakening of UW.

## Application and limits

All these elements have the SAME complement2N. If the separate RK
fixed-complement reciprocal theorem passes its own review, any chosen
distinct free classes would give the same number of pairwise disjoint
reciprocal arrays, each of size p-1. This is only a conditional use of
another unverified packet, not an unqualified transfer of Fourier
faithfulness or an accepted higher-series rank theorem.

The original Mihailescu Lemma3 already uses a count of two-Fueter
selections. The proposed bound above is an alternative invariant-based
count, without assuming parameter uniqueness or an injective full
Stickelberger multiplier. Priority is unestablished. No original-weight
existence mechanism is presented as new merely from pairing.

Before promotion, TWO OTHER whole nonconstructor audits must reconstruct
the quintic nonidentity, at-most30 orbit-fiber count, minimum-fiber
choice and ceilings, both zero-action cases, integer positivity/freeness,
and all UW/RK dependency statuses. Until then this is only a preserved
research direction. No rank, Jacobi normalization, integral cofactor,
every-conjugate cancellation, nonzero-delta or size estimate has been
proved from the number of available arrays. The annual equation remains
unresolved.
