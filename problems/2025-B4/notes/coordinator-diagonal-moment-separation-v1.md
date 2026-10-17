# A conditional separation lemma for the diagonal appendix

2026-10-17 UTC. **Candidate proof — unverified; research note.** This does not accept the second-case diagonal theorem, repair the entire appendix, or refute a published conclusion. It records one concrete possible way to discharge one previously listed interface.

Let p be an odd prime, zeta a primitive p-th root, K=Q(zeta), lambda=1−zeta and O=Z[zeta]. Take theta=sum_{a=1}^{p−1} n_a sigma_a in Z[Gal(K/Q)] and assume its inverse moment

    M=sum_a n_a a^(-1) in F_p

is NONZERO. Define, for c in F_p^*,

    eta_c=sum_a n_a (1−zeta)/(1−zeta^(ac)).

The ratio is evaluated at the nonzero residue ac modulo p. It lies in the localization O_(lambda): indeed

    (1−zeta^t)/(1−zeta)=1+zeta+...+zeta^(t−1)

reduces to t modulo lambda for the representative1<=t<p, and t is a nonzero element of O/(lambda)=F_p. Its reciprocal therefore belongs to the localization and reduces to t^(-1). Consequently

    eta_c = c^(-1) M mod lambda.

For distinct c,d these residues differ, because M!=0 and inversion is a bijection of F_p^*. Hence eta_c!=eta_d as elements of K. In particular any subset of these coordinates has pairwise distinct entries. No real ordering or size estimate is needed, and negative n_a cause no difficulty. Multiplying ALL coordinates by the same nonzero field element also preserves distinctness.

This argument proves the stated elementary candidate lemma under its explicit moment hypothesis. It does not prove that the theta selected in the ORIGINAL diagonal singular argument has that hypothesis.

## Exact source match and remaining application gap

Freshly reopened [Bartolome–Mihailescu, arXiv1412.5798v2](https://arxiv.org/pdf/1412.5798v2), internal version1.13,2021-11-02. Read the actual definitions in §2.4 and the relevant complete statements/proofs around Lemmas2.8/2.10, together with Appendix5.1–5.1.1. Lemma2.10 explicitly assumes a nonzero inverse moment, and its coefficient reduction has this same residue separation. The appendix footnote identifies its older eta with the current b1. The current main proof constructs a suitable moment in a different context. That construction is not silently substituted for the original2008 diagonal theta.

Thus, if the original selected theta and normalization are shown to satisfy these exact conditions, the appendix's distinct-coordinate hypothesis follows by the direct calculation above. This would remove that particular concern. It would not resolve the augmented-versus-original matrix notation, the cancellation for every conjugate, or the delta=0 argument previously recorded in `coordinator-diagonal-appendix-inspection-v1.md`.

The norm estimate still needs a complete application-specific reconstruction before any stronger diagonal range exclusion can be claimed. Earlier accepted first-case CF1 and elementary power-gap restrictions are independent of this appendix. No new computation, third-party PDF redistribution, author contact, charge, or access bypass occurred. Two independent whole audits would be required to promote this candidate lemma or any completed application.
