# Toward all exponents with the fixed factor phi_13

Coordinator construction/lead, 2026-10-16. **Candidate argument - unverified.** This is separate from the frozen infinite-family proof and its audits. No complete automaton or exclusion theorem has yet been produced. It is not a full B4(b) classification.

The primary [Derksen preprint, math/0510583](https://arxiv.org/abs/math/0510583) describes positive-characteristic recurrence zero sets using finite automata. Its full hypotheses and effective construction have not yet been audited here; it is a method lead, not a theorem imported into this argument.

For the normalized series F=P/K in the family proof, coefficients are Laurent polynomials in b over F2. Use **bivariate** Cartier operators C_(r,t), r,t in {0,1}, which retain z exponents congruent to r and b exponents congruent to t, subtract those parities and halve both exponents. Negative b exponents use the unique parity in {0,1}, so this also acts on Laurent polynomials.

Because K(z,b)^2=K(z²,b²),

    C_(r,t)(N/K)=C_(r,t)(N*K)/K.

If every numerator monomial z^i b^j satisfies 0<=i<=3, -1<=j<=2, the same bounds hold after this operation: N*K has z exponents 0..7 and b exponents -2..4. The starting numerator 1+z+bz² satisfies these bounds. Thus all transformed numerators belong to an explicitly finite 16-dimensional F2 vector space.

To decide whether a coefficient at z^(2a+r) vanishes identically in b, BOTH b-parity components must vanish at z^a. Their uniqueness follows from the even/odd Laurent decomposition. Consequently a possible exact deterministic automaton has a **linear subspace** of the numerator space as each state. Start at span(P). On input bit r (least significant first), replace a subspace W by the span of all C_(r,0)(N*K) and C_(r,1)(N*K) for a basis of W. A state is accepting exactly when all its basis numerators have zero coefficient at z^0. Linear dependence can be removed by exact binary Gaussian elimination.

The proposed invariant is that, after reading the low binary digits of j, the original coefficient vanishes iff all corresponding residual coefficient constraints vanish. At the end, their z^0 coefficients decide it. The finite-dimensional bound proves that a breadth-first search has finitely many possible subspaces, but does not give a practical small state count. A bounded incomplete search cannot supply a complete automaton. A completed transition-closed graph, independently reconstructed and checked, could give an exact zero-set description without extrapolating finite scans.

There is also a possible elementary bridge from **formal** A-divisibility to **actual** phi_13-divisibility in the reverse direction. Under lex order x>y>z, the leading monomials of Q,R²,D are x², x⁴y², x²yz. Their exponent vectors are independent over the integers, so distinct formal monomials in q,u,d have distinct leading monomials. This should prove the invariant substitution S=F2[q,u,d] into F2[x,y,z] is injective.

Each of x,y,z satisfies the squared quartic

    X^8+Q²X^4+R²X²+D²=0.

Hence the actual polynomial ring is integral over the image of S. If an actual polynomial quotient phi_(2j+3)/phi_13 exists, it also belongs to Frac(S), via the injective substitution. It is integral over S, and S is a UFD and integrally closed, so the quotient should lie in S. Combined with the already proposed forward substitution, this would identify actual phi_13-divisibility with the zero set of F. Every step requires fresh full audit before use.

Férard's abstract suggests that this fixed factor is especially relevant in the residue class 5 modulo 8, but the original theorem remains unread; do not infer any whole-polynomial irreducibility classification from that abstract. All other possible factors and odd residue classes remain a separate problem.
