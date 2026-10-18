# A bounded cofactor for every k>=2 — unfinished research seed

18 October2026UTC. **Candidate proof - unverified; UNDER CONSTRUCTION.**
Root sole NEW constructor. This is separate from the frozen cubicR3
submission and must not alter its bytes or be silently accepted with it.
The R3 intermediate e<A is still UNVERIFIED; the derivation below must
be independently reviewed in a complete future packet. No annual result
or novelty is claimed.

KeepQ=2^s,s>=3,ell=Q-1,q=Q^k,k>=1,N=ellq-2,
A=(ell-2)(ell+1). AcceptedCG1/CG2 plus the elementary sign argument
written inR3 propose the following statement whenq>=2ell+7:

    EVERY proper factor with0<e<=N/2 has e<A.

This is stronger than a statement only about the least component:
the P(e0)/positiveB argument applies to ANY such proper factor,
including a reduced UNION of absolute components. The c-1 correction
in the accepted premise is essential for this reuse. No old failed
greedy-grouping argument can be promoted without this NEW sharp bound.

IfN>=4A and the whole reduced polynomial is reducible, there is a
UNIQUE absolute irreducible component of degree>N/2. Otherwise every
component has degree<=N/2 and thus<A. Accumulate distinct components
until their union first has degree>=A. Such a union exists since total
degreeN>=4A; its degree is<2A<=N/2. It is a proper factor contradicting
the displayed bound. Thus a large component exists; uniqueness follows
because two degrees>N/2 cannot sum withinN. Its complementary product
has degreee<N/2, hence **e<A**. Its dominant degree is therefore>N-A.

For EVERYQ>=8,k>=2, q>=Q²>=2Q+5=2ell+7 and

    N-4A >= (Q-1)Q²-2 -4Q(Q-3)
           =Q³-5Q²+12Q-2>0.

For example the final polynomial isQ²(Q-5)+12Q-2>0 forQ>=8.
Thus this would give a dominant component and a cofactor of degree<A
for ALL general k>=2, even where the cubic threshold does not force
the cofactor to be constant.

Since phi has coefficientsF2 and the dominant component is UNIQUE,
Frobenius must preserve it. After normalizing a nonzero coefficient,
its equation descends toF2; its complementary product does too.
Likewise every projective linear symmetry ofphi preserves that unique
component and the small cofactor as divisor sets. This gives S4
invariance of the divisor, without assuming uniform multiplicity on
ALL F_Q singular points. Polynomial semi-invariant normalization and
any particular invariant-ring claim require separate verification.

Potential further information, NOT proved here: every component meets
some prescribed diagonal by S=3(e-m), unless m=e, whose other geometry
must be checked. At a non-P diagonal the tangent roots satisfyx^q+x+c,
so lie inF_(q²); atP tangents lie inF_q. An ordinary branch may bound
the component's definition field. This requires a full argument and
does not by itself give point-orbit uniformity, a growing lower bound
forD, or a k2 irreducibility theorem.

Remaining obstacle: small cofactor degree<A is of orderQ², comparable
to q at k2. S4/Frobenius is not transitive on the many off-diagonal
F_Q points for generalQ. A constant orbit-size congruence would not
automatically give the orderQ lower bound onD suggested by the cubic
inequality. No such lower bound or general k2 exclusion is asserted.

All deductions above are hand reasoning, no CAS/field/factor scan.
Preserve this seed, complete the exact accepted-premise and group-action
checks, then obtain TWO OTHER initially blind whole audits if proposing
a formal result. The current R3 review queue and hourly09:27:30UTC
report take precedence over integrating an unfinished research seed.
