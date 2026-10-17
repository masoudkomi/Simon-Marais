# A 2026 irreducibility source and the diagonal-translation gap obstacle

2026-10-17 UTC. **Research note / unverified mathematical deduction.**
No new exponent exclusion, source-theorem refutation or annual solution
is asserted. No mathematical code, polynomial scan or CAS was used.

## Fresh primary source and exact read scope

Agrinsoni-Janwa-Delgado, *A new criterion for the absolute irreducibility
of multivariate polynomials over finite fields*,
[arXiv2602.01583v1](https://arxiv.org/html/2602.01583v1), submitted2February2026.
Read actual abstract/introduction and COMPLETE displayed sections2-4,
including Theorem8 and its proof, Lemmas9-10, Theorem12 and proof,
Corollaries14-15 and the final conclusions. References are leads, not
individually audited external proofs. The criterion requires a square-free
leading form, a gcd condition and a final degree gap outside the additive
semigroup of earlier gaps. Its abstract does not remove these hypotheses.

PDF cached LOCALLY ONLY at
`.cache/literature/2024-return-2026/agrinsoni-janwa-delgado-2602.01583v1.pdf`,
322639B, SHA25617b4056e0cdbc7c196bdbd01ab1bce84420f3a9a5a51fc1853d24bd8dff9980f,
14pages. pypdf inspected the actual first/last pages as a version check;
the mathematical source read above was the HTML text. No full source is
tracked. Related2025 Gold/Kasami publication metadata and a2026 Purdue
seminar were also found, but no unseen full theorem is imported from them.

## Proposed obstacle to ONE direct application

Work in characteristic2. Put

    f_m=x^m+y^m+z^m+(x+y+z)^m,
    D=(x+y)(y+z)(z+x), phi_m=f_m/D.

For positive m, each of the three distinct linear factors of D divides
f_m, by setting the corresponding variables equal. Thus phi_m is a
polynomial (possibly zero). For positive m, f_m is identically zero
exactly when m is a power of2: Frobenius gives one direction; otherwise
the binary product expansion has a mixed monomial, splitting the set
bits into two nonempty groups, which cannot cancel against the three
pure powers. This also shows phi_m!=0 when m has at least two set bits.

Let n be odd and NOT of Gold form2^k+1. Then n has at least THREE set
bits, since its low bit is1. For any nonzero constant a, diagonal
translation fixes D and gives the exact homogeneous-form decomposition

    phi_n(x+a,y+a,z+a)
      =sum_(j=1)^n binom(n,j) a^(n-j) phi_j(x,y,z).

Indeed the fourth input also translates by a in characteristic2; expand
each power, and the four degree-zero terms cancel. Each nonzero summand
phi_j is homogeneous of degree j-3, so different j cannot cancel.

The top degree is d=n-3. The j=n-1 coefficient is a, since n is odd.
Here n-1 is not a power of2, so phi_(n-1) is nonzero. Hence the FIRST
degree gap is exactly1.

There is also another nonzero LOWER form: choose j=1+2^r using the
lowest positive-position set bit r of n. Since n has another higher
set bit, j<n-1. The binary product expansion shows binom(n,j)=1 modulo2;
phi_j is nonzero and a^(n-j)!=0. Thus there are at least TWO lower forms.

Consequently the final positive gap automatically lies in the additive
semigroup of the earlier gaps, because that semigroup already contains1.
Theorem8's stated final-gap hypothesis therefore FAILS for this diagonal
translate at every such n, regardless of square-freeness or gcd tests.
This is an obstruction to this proposed direct use, not a contradiction
to the source theorem. Its Theorem12 cannot find a later gap outside that
semigroup either; the first-gap lower bound alone is trivial here.

No conclusion is drawn about other coordinate changes, dehomogenizations,
local forms, Gold exponents, the source's other applications or different
irreducibility criteria. A useful next route would need a different form
decomposition or genuinely new gcd/geometry information. The deduction
above remains unverified pending independent review and is not an accepted
restriction on the official exponent set.
