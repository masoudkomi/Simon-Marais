# The abstract modified-branch matrix is realized at every odd prime-power size

2026-10-17 UTC. **Research lead / candidate deduction - unverified.**
Root constructor. This is SEPARATE from B's frozen R5 submission and
from root's complete initially blind R5 R1 audit. It does not repair
or refute R5, whose matrix assertion is expressly NECESSARY ONLY.
No peer R5 finding is used. Two other whole audits are needed before
this separate deduction could be promoted. No scan or mathematical
program was used, and priority is unestablished.

R5D associates an actual modified saturated example of odd order q
with a symmetric INTEGER q-by-q matrix T satisfying

    T1=0, T²=qI-J, entries>=-1,
    diagonal multiset {one0,(q-1)/2 ones,(q-1)/2 minusones}.

These abstract conditions alone cannot exclude every odd q>3:
the following standard quadratic-character construction supplies them
for EVERY odd prime power q. The construction has no prime p=q²+q+1
or cyclotomic subgroup in that DIFFERENT field as an input.

Let F=F_q, chi:F->{0,+1,-1} its quadratic character with chi(0)=0.
Index rows/columns by the q elements of F and put

    T_(x,y)=chi(x+y).

All entries are ordinary rational integers. The matrix is symmetric.
For each fixed x, translation y->x+y permutes F, so its row sum is
sum chi=0. Its diagonal is chi(2x). Since multiplication by2 permutes
F, it has one0 and equal numbers of+1 and-1, as required.

For completeness the exact square identity has a short hand proof.
When x=y,

    (T²)_(x,x)=sum_z chi(x+z)²=q-1.

For x!=y, let d=y-x and set w=(z+x)/d. The summand is
chi(d² w(w+1))=chi(w(w+1)). To evaluate its sum, count pairs (w,v)
with v²=w(w+1). The change U=2w+1, V=2v is invertible and turns
the equation into (U-V)(U+V)=1. Each a in F* gives exactly one
solution by U-V=a,U+V=a^-1, and all solutions arise this way.
Thus there are q-1 pairs. Counting v first gives instead
q+sum_w chi(w(w+1)). Consequently that character sum is-1.
Every off-diagonal entry of T² is therefore-1, proving T²=qI-J.

The q-dimensional all-ones vector has eigenvalue0. Real symmetry,
the square identity on its orthogonal complement and trace0 give
eigenvalues+sqrt(q),-sqrt(q), each with multiplicity(q-1)/2. These
irrational eigenvalues when q is nonsquare are compatible with the
ordinary integer entries.

Even the abstract nonnegative principal-block/Gram data can be
realized: put S=J+T and

    C=[0  1^t; 1  S].

Then S is symmetric nonnegative integer, S1=q1 and
S²=qI+(q-1)J. It follows directly that C²=q(I+J-E00), Ce0=1-e0,
and C(1-e0)=q1. Its diagonal and spectrum are precisely the formal
data in R5D. This does NOT identify C with the cyclic-indexed
P(A+I) of an actual prime-field cyclotomic matrix.

What is missing is the embedding into the multiplicative-coset
indices of F_p, p=q²+q+1, with every incidence/cyclotomic relation
and actual H-difference count. The abstract character matrix is NOT
an actual planar difference set in that prime field, and supplies
no new taut order. The possible original branch q=3^(3^s) is not
excluded or constructed by this matrix realization. No claim about
all odd integer q, primality of any p, or a matrix converse is made.

The construction is the plus-index version of the classical
Paley/Jacobsthal quadratic-character correlation method. A search
verified the original bibliographic record
[R.E.A.C. Paley, On Orthogonal Matrices,1933](https://doi.org/10.1002/sapm1933121311),
J. Math. Phys.12,311--320. The publisher record was read; the full
original paper was NOT accessed or imported. The proof above is
self-contained. Search hits for later notes/theses were discovery,
not theorem premises, and no new source proof is claimed from them.
No charge, subscription, download or restriction bypass was needed.

This is a precise limitation of an appealing possible proof route.
R5's correct necessary-only scope already allows such realizations.
Before any promotion, independent whole auditors must check the
quadratic-character sum by the conic bijection, ordinary-integer
entries/diagonal, the exact square and block identities, and the
separation of abstract matrices from ACTUAL cyclotomic data. The
full2020 annual problem remains unresolved.
