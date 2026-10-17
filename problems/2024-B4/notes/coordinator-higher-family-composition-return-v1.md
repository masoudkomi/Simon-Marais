# Higher Kasami-family indices: a necessary-condition lead and a failed converse

2026-10-17 UTC. **Research deductions — unverified.** Root constructor. This is not an addition to frozen KC or its audit scope. No claim is promoted without two further independent whole audits. The first reduction below is CONDITIONAL on KC, whose two audits are queued/active; the explicit failed converse uses only the separately accepted GK recurrence and CP1.

Fix q=2^k,k>=2, let d0=q²−q+1 and write

    L_r=(q^(2r+1)+1)/(q+1), r>=1.

Accepted GK gives g_(L_r)=P_r(g_d0), where P0=1,P1=T and the complete Frobenius recurrence is in the accepted proof. Since phi_d0 divides every phi_(L_r), transitivity would make

    phi_(L_r) | phi_n  ==> phi_d0 | phi_n.

IF the exact KC candidate is accepted, the latter forces n=L_s for some s>=1. The separately accepted CP1 degree condition then forces

    L_r−1 | L_s−1,
    q^(2r)−1 | q^(2s)−1,
    r | s.

The middle implication follows by cancelling the common rational factor q/(q+1) in the integer ratio; equivalently (L_s−1)/(L_r−1)=(q^(2s)−1)/(q^(2r)−1). For the last implication write s=ar+b,0<=b<r and reduce modulo q^(2r)−1. The remainder is q^(2b)−1, which is nonnegative and smaller than the modulus; it vanishes exactly at b0. No sufficiency is supplied by this necessary arithmetic condition.

In fact the tempting converse `r|s => whole phi_(L_r)|phi_(L_s)` is FALSE. There is a symbolic counterexample for EVERY q>=4 at r2,s4, requiring no polynomial scan or finite-field program.

At T0, A_q(0)=B_q(0)=1, so the accepted GK recurrence gives

    P_(j+2)(0)=P_(j+1)(0)+P_j(0),
    (P0(0),P1(0))=(1,0).

Hence the exact constant values repeat1,0,1,1,0,1,... with period3. At T1, A_q(1)=1 and B_q(1)=0, so P_j(1)=1 for EVERY j>=0. In particular

    P2(0)=P2(1)=1, but P4(0)=0 != 1=P4(1).

If whole phi_(L2) divided phi_(L4), CP1 would give g_(L4)=H(g_(L2)). Substitute GK to obtain P4(g_d0)=H(P2(g_d0)). Composition by the NONCONSTANT g_d0 is injective on F2[T] by leading degree. Therefore P4=H(P2), contradicted by these two equal-input values. Thus divisibility fails although2 divides4 and the degree ratio is an integer. This counterexample makes no assumption of KC.

More generally, whenever r is not1mod3, P_r(0)=P_r(1)=1. The same argument excludes every s=1mod3 as an outer target. The degree condition and this constant-value obstruction do not settle the other index pairs. They do not justify classifying all compositions, general factors or the annual reducibility problem. The next useful question is the actual decomposition structure of the explicit P_r, retaining wild-characteristic behavior rather than importing a characteristic-zero Ritt theorem.

No mathematical program, CAS, certificate rerun or scan was used. Every value above is a direct symbolic consequence of the accepted recurrence. No novelty claim, full annual answer or change to existing frozen bytes is made.
