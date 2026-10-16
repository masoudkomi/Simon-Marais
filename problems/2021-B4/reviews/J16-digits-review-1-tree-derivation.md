# Independent extension derivation before owner serialization

2026-10-16 UTC. R1. The parent extended the still-unfrozen review from
L1--L3 to the complete L1--L4 proposal. The two owner mathematical notes
were read; no owner program, certificate, result, or manifest had been
opened when this derivation and `J16-digits-review-1-tree-independent.py`
were first saved. No peer report or conclusion has been read.

The already independent uniform E proof applies at every precision.
For an input (X,Y) modulo 19^k satisfying E=0 modulo 19^k, k>=1,
the full digit fiber is M*(dX,dY)=-E(X,Y)/19^k over F19. Polynomial
Taylor expansion is valid over Z_(19); the omitted change terms have
valuation at least 2k>=k+1. The constant matrix M is unchanged at every
descendant. Enumerate all solutions by independent Cramer rank-two
solution, rank-one free coordinate, or both free coordinates at rank zero.
There is no division by X-Y and no test of equality of finite residues.

The independent evaluator uses all terms in the normalized scalar
recurrence modulo A=19^(nu+k+1). It builds F=f/Z^2 modulo 19*A,
including the two known top coefficients exactly. Full monic long
division computes R0,R1 modulo 19*A. The quotients Ptilde/q,
R0/(19q),R1/(19q) are then known modulo 19^(k+1). Multiplication by
the inverse of beta18=10 at that modulus gives E's second coordinate.
Only an actual exact division by a checked 19-power is performed; the
remaining denominator is a 19-adic unit. This derivation does not use
the owner's h_e/k_e formulas or degree truncation.

T1 removes a full family omitting u or v from its derivative labels:
H1 already uses 0 and H19 already uses 1, and all other derivatives
would then use just the remaining three rational roots. This pruning
does not follow from a residue being zero, coincident with another, or
unused as a value of a test polynomial. All full assignments are still
evaluated at the first level to cross-check the old complete L3 stream.

Starting with the independently derived 840396 full keys, compute every
input's entire digit fiber and union all unpruned children into the next
expected layer. A certificate key must be present exactly once in its
expected layer. Remove every processed key, require the layer to be
empty after all records, and require the independently constructed
children to equal the saved node layer. This proves finite traversal
coverage even if constructor order differs. All coefficient residues,
E residues, matrices, constants, ranks and solution sets are to be
checked, not merely the aggregate number of survivors.

An independent fixed cap is one million input or output states per
layer and fixed target precision 8, with a 300-second external child
timeout only after a bounded benchmark. No partial traversal may supply
an exclusion. If precision four leaves only rank-two states, the
constant-matrix fact proves a structural cap equal to that layer's size
at every later precision; a 90-state observed layer would therefore
justify (but not prove the outcome of) the bounded continuation.

For every final precision-four and later input, rebuild the exact
integer a_j by Horner evaluation of the full recurrence, form exact
integer F and exact integer quadratic remainders, and form Fraction
values of E. Their reduced denominators must be prime to 19. Compare
all scalar residues and affine constants to these exact fractions.
For a rank-two 3-by-2 matrix, the vector of signed two-row minors
lambda annihilates both columns. Its nonzero dot product with the
constant vector is a direct inconsistency certificate. A zero dot
product is also sufficient for consistency in rank two, since the
two-dimensional column space equals lambda's kernel.

If this complete tree is empty at any fixed precision, an actual
rational J16 pair is impossible: its exact roots satisfy E=0 and its
successive residues would yield a path through every finite layer.
No convergence, infinite lifting, root-height bound, algebraic closure
claim or nonsingularity assumption is needed. This excludes just J16
under accepted normalization/T1--T2, leaving other J classes unresolved.
