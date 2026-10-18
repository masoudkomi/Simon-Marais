# Cubic rather than quartic cofactor threshold — research seed

18 October2026UTC. **Candidate proof - unverified.** Root sole NEW
constructor. This seed is recorded AFTER root's entire2019CR whole R1
freeze09:12:42UTC; no other agent supplied a NEW inference here. It is
not a frozen submission or accepted theorem. Both OTHER whole audits
will be required for the eventual complete packet. Do not count root.

Use only the NOW ACCEPTED exact CG1/CG2 constraints. Let

    Q=2^s,s>=3, ell=Q-1, q=Q^k,k>=1,
    A=(ell-2)(ell+1), p=ell-1, a=(ell+2)/(ell-1).

For a hypothetical smallest proper absolute factor,0<e<=N/2, CG2 gives
P(e)>=0, integerD>=1 and

    D B <= T - a D^2/A,
    B=q+1-(2ell/A)e,
    T=p(e-e^2/A).

The accepted elementary P(e0) argument, at e0=(ell-2)q/2, needs only
q>=2ell+7 and proves e<e0. Hence B>q/(ell+1)+1>0.
Now the crucial additional consequence is **T>0**, since the displayed
left side is positive and aD²/A>0. Thus e<A. Divide by D BEFORE using
D>=1. Because T>0,

    B <= T/D - aD/A <= T-a/A.

Adding(2ell/A)e and maximizing its ONE real quadratic over all e gives

    q+1 <= [p+2ell/A]e - p e^2/A - a/A
         <= pA/4 + ell + (ell^2-ell-2)/(pA)
          = pA/4 + ell + 1/p.

The complete maximum is at e=A/2+ell/p; no feasible integer maximizer
is asserted or needed. All inequalities are over ordinary reals/integers,
not characteristic2. The sign T>0 is indispensable: replacing T/D by T
without first proving it would be wrong when e>A.

Proposed stronger sufficient threshold:

    q>=2ell+7 AND
    q> (ell-1)(ell-2)(ell+1)/4 + ell-1 + 1/(ell-1).

Under it the hypothetical factor is impossible, proving WHOLE absolute
irreducibility, hence excluding the official positive-degree F2 product.
In particular this would cover EVERY s>=3,k>=3: for Q>=8 the second
right side is

    (Q-2)(Q-3)Q/4 + Q-2 + 1/(Q-2)
       < Q^3/4+Q < Q^3 <= q,

and q>=Q³>2Q+5. This extends the accepted general all-k>=4 conclusion.
It gives no blanket k2 result: at Q8,q64 the proposed second threshold
is66+1/6, although the separate accepted FS theorem covers that special
case. General k2, the full annual classification and priority remain open.

No new local geometry, unproved orbit uniformity, large-component grouping,
F2 descent, Frobenius theorem, field enumeration, CAS, mathematical program
or certificate is used. The old accepted proof/source scopes remain exact;
Férard2017's operative body remains unread. Possible prior overlap must
still be investigated. This seed must be expanded into a complete exact
candidate/obligation/source/failure/log/metadata packet before review.
