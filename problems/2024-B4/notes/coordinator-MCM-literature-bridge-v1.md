# A concrete MCM-polynomial bridge for the 2024 research

2026-10-17 UTC. **Research note; the new deductions below are candidate proof — unverified.** No new annual solution, novelty claim, or accepted external factor theorem is asserted. The separately accepted CP1–CP3 packet is complete without this note. Root developed this lead after freezing its initially blind CP audit, and supplied no step or repair to that construction.

## An exact candidate identification, without a new external theorem

Use the accepted notation x^n+(x+1)^n=g_n(U), U=x²+x. Put q=2^k, d=q²−q+1, and define the two DIFFERENT polynomials

    T_k(U)=sum_{i=0}^{k−1} U^(2^i),
    L_k(U)=sum_{i=0}^{k−1} U^(2^i−1)=T_k(U)/U.

The last quotient is a polynomial, since every term of T_k is divisible by U. In F2[x], set a=x, b=x+1, p=a^(q−1)+b^(q−1). Direct telescoping gives T_k(a²+a)=a^q+a. Also

    U p=ab(a^(q−1)+b^(q−1))=ba^q+ab^q=a^q+a,

using b=a+1 and b^q=a^q+1. Injectivity of F2[U] into F2[x] and cancellation in the polynomial domain give p=L_k(U). The already accepted CP four-term identity g_d(U)+1=U p^(q+1) therefore yields

    g_(q²−q+1)(U)+1 = U L_k(U)^(q+1) =: C_q(U).

This is precisely the defining Müller–Cohen–Matthews polynomial C_q. The expression T_k(U)^(q+1)/U^q denotes this polynomial; it does not discard U=0 or authorize division of evaluated functions. The identity also works at k=1, although the external MCM passages inspected below start at k>=2. No computation was used.

Consequently the two-variable whole difference quotient attached to this Kasami exponent is

    Q_d(U,V)=(C_q(U)+C_q(V))/(U+V).

Accepted CP1 supplies the exact homogeneous/Artin–Schreier pullback relation. It does NOT say that arbitrary factors after that pullback descend. This is the promising point of contact with published MCM difference factorizations.

## Actual primary passages inspected

- [Antonia Bluher, A New Identity of Dickson Polynomials, arXiv1610.05853v3](https://arxiv.org/html/1610.05853v3), introduction/notation and Lemma2.1 inspected; later sections only in excerpts. Its notation uses T for our L_k, and defines C=U L_k^(q+1). No splitting-field or exceptionality proof is imported here. The version page has differing version/internal dates; this note makes no inferred publication-date claim.
- [Michael Zieve, Bivariate factorizations via Galois theory, with application to exceptional polynomials](https://websites.umich.edu/~zieve/papers/biv.pdf), AppendixB, printed pp18–20: applicable text read; pp18–19 additionally rendered and visually inspected. It states the absolute factors of MCM differences, indexed by nonzero trace-zero elements. The coefficient field has an OVERLINE: these are absolute factors, not automatically F2 factors. The cached author PDF has227582bytes, SHA256 `c46313e0c187246b720d8424c3004c42902b2ff11747285da0f698b25dad0e47`, retained only in ignored `.cache/literature/2024/root-MCM/`. The printed stabilizer order on p19 is q+1; I do not silently change or import that group assertion. Earlier underlying monodromy proofs are not newly reconstructed.
- [Delgado–Janwa, arXiv1612.05997v1](https://arxiv.org/pdf/1612.05997v1), complete definitions and §3 equations(5)–(6), printed p7, inspected. They reproduce Janwa–Wilson's Kasami components P_alpha over F_q, with P_alpha(x,0)=(x+alpha)^(q+1), and group Frobenius conjugates into F2 factors. This is a published reproduction, not a new reading of the original Janwa–Wilson proof; no later transversality theorem is needed for the proposed orbit argument below.

## A useful proposed literature corollary and its unaccepted dependency

If the exact homogeneous Janwa–Wilson factor statement, normalization and Frobenius action are imported with verified hypotheses, then for k>=3 there are q−2 distinct absolute factors and each Frobenius orbit has length at most k. Since 2^k−2>k, there is more than one orbit, and products over separate orbits give nonconstant F2 factors of phi_d. The displayed specialization distinguishes the normalized factors; Frobenius sends the one labelled alpha to the one labelled alpha². Homogenization needs its full-degree/no-missing-line check. This would supply the known Kasami family itself, including d=57, in addition to the separately accepted CP family N=3641,... .

This paragraph is a CANDIDATE attributed corollary, not a promoted result: the original component theorem has not been independently reconstructed here. Merely counting extension-field factors without the Frobenius normalization would be insufficient. No factorization at k=2 follows from the orbit-count inequality, and this note makes no conclusion at that endpoint.

## Next mathematical questions

The first useful target is to prove an exact relationship between MCM difference factors and the Artin–Schreier pullbacks, retaining all coefficient fields and Frobenius orbits. A second is whether these fibers characterize any additional compositions g_n=H(g_d). The tempting extension N_m=(q^(2m+3)+1)/(q+1) is UNPROVED for arbitrary m and q: CP2 establishes only m=1 for every q; the older exact phi13 criterion establishes a different fixed-q progression. No generalization is inferred from those two slices.

No paid access, contact, bypass or redistribution occurred. The author-PDF retrieval returned only after a host delay much longer than the requested curl timeout; the completed curl session was explicitly reaped. That delay is operational history, not mathematical work. The algebra above and proposed orbit corollary need two independent whole audits before acceptance under the project protocol.
