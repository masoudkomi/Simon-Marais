# Reviewed elementary integer-domain reductions

**Proved, independently reviewed (partial results)**, 2026-10-16 UTC.
This accepts C1-C4 of the complete [frozen P2025-v1 proof](../proof.md),
SHA-256 `c422139567ee3e2f4eafd852c9a3f5fac73cb6c8e0bfdf9e2c9c5311a9348b0d`.
Its original candidate labels record its earlier status. The mathematical
arguments remain unchanged; see [acceptance](../reviews/acceptance.md).

The accepted results are all boundary families and nonboundary signs;
the exact gcd and signed-domain LTE restrictions; the exclusion of
nontrivial even exponents in official degree two; and prime-exponent
reduction with the safe geometric-block factorization and gcd identity.
For the last identity G_k denotes 1+x+...+x^(k-1) for every positive k,
including G_1=1; this explicates the notation already used in its proof.

Both fresh, initially blind reviewers reconstructed every argument and
the LTE hypotheses, treated negative bases and zero factors, checked
the official degree n versus term count m=n+1, and independently tested
the stated identities. The finite scans are evidence, not a proof of
the unrestricted classification. No substantive mathematical repair was required.

The full predicted list beyond these reductions remains conjectural.
The known signed examples are (3,+/-11,4,2), (7,+/-20,3,2),
(18,7,2,3), and (-19,7,2,3), in official (x,y,n,q) order.
No completeness claim or novelty is established.

The source audit now has a [full-text supplement](../notes/reviewed-literature-supplement-v1.md).
In particular, Chen-Mihailescu's printed theorem retains a possible
small-prime negative-base exception omitted from its abstract. None of
these imported research theorems is needed for C1-C4, and this project
has not reconstructed their complete published proofs.
