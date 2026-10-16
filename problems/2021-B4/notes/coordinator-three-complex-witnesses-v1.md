# Degree 20 and at most three complex recycled values

2026-10-16 UTC. **Candidate proof - unverified.** Constructor: coordinator.
This is a proposed reproduction of a published restricted claim, not a
solution of the full Casas-Alvero conjecture or of 2021 B4(b). It needs
two independent complete extension audits. No novelty is claimed.

Proposed C20: a monic degree-20 polynomial in C[X] which shares a root
with each derivative of orders 1,...,19, and which admits a set of at
most three roots supplying all these witnesses, is a power of a linear
polynomial. Other roots are unrestricted. The witness set, rather than
the total set of roots, is being counted.

Massri [arXiv:1806.09561v6](https://arxiv.org/abs/1806.09561v6),
Theorem 7.10, already states this stronger-than-rational claim. The present
argument proposes a different exactly checkable exhaustion after the
6,680 center-mask filter noted in that paper. It does not validate every
argument in that preprint or use its 3^17 resultant computation. Earlier
withdrawn versions and the active cited v6 are distinct source objects.
The valuation normalization is related to Castryck-Laterveer-Ounaies,
[arXiv:1208.5404](https://arxiv.org/abs/1208.5404), Section 3.4;
the specific proof and ramification points used here are given below.

## 1. A complex counterexample with this cover gives an algebraic one

Suppose a non-pure-power counterexample with a cover of size at most
three exists. A one-value cover forces all Taylor coefficients below
degree 20 at that value to vanish, hence a pure power. Otherwise choose
a first-derivative witness r from the cover and a different cover value
b. Translate and scale by r,b so that the monic polynomial has a double
root 0, a root 1, and a cover {0,1,u}. If only two distinct values are
needed, take u=0; no distinctness of all three is required in the formal
families. The coefficients at this point may be complex.

Write f=sum_j binom(20,j)*a_j*X^(20-j), a_0=1, and a_19=a_20=0.
For j=1,...,18 choose one cover value w_j in {0,1,u} witnessing the
derivative of order 20-j. Its normalized equation is

    D_j(w_j)=sum_(k=0)^j binom(j,k)*a_k*w_j^(j-k)=0.

Fix those choices as the symbols 0,1,U. Starting at a_0=1, the recursion

    a_j(U)=-sum_(k<j) binom(j,k)*a_k(U)*w_j^(j-k)

determines every a_j in Z[U]. It specializes to the original coefficients
by induction. The remaining root equations are integer polynomials
P(U)=f_U(1)=0 and Q(U)=f_U(U)=0. If either is nonzero, their actual common
complex root u is algebraic, so f has algebraic coefficients and the
same algebraic cover. If both are the zero polynomial, specialize U=2;
the resulting monic algebraic polynomial still has distinct roots 0,1,
the double root 0, and all selected derivative equations. It is nontrivial
and has a cover of size at most three. Thus in either case an algebraic
counterexample exists. This step avoids presupposing an embedding C into
a p-adic algebraic closure or that arbitrary complex coefficients are algebraic.

## 2. Normalize in a finite extension of Q_19

Embed the algebraic coefficients, cover and splitting roots in Qbar_19,
and work in a finite extension K containing them. Its valuation v extends
v(19)=1 and may have fractional values. Translate the selected double
root to 0. Scale by a nonzero root of smallest valuation, so every root
is integral and some nonzero root is a unit. Divide by the leading
coefficient to keep the polynomial monic. All selected common witnesses
are roots, hence integral as well.

The triangular normalized derivative equations above imply inductively
that every a_j is integral: at stage j its chosen integral witness makes
a_j a sum of products of previously integral coefficients and powers of
that witness. This includes j=1; the constant and linear coefficients
are zero because 0 is a double root. For 2<=j<=18 the binomial coefficient
binom(20,j) is divisible by 19 exactly once. Thus reduction is

    f_bar(X)=X^20 + (20*a_1)_bar*X^19.

The integral unit root forces a_1 to be a unit; otherwise f_bar has no
nonzero root. The center c=-a_1 is itself a chosen common root, since
D_1=X+a_1. Scale by this unit c to set the center to 1 and a_1=-1;
integrality and the unit/nonunit partition of roots are preserved.
Then

    f_bar(X)=X^19*(X-1).

The reduced root 1 is simple, and f'(1) is a unit, so the center is
simple. It is the only root of valuation zero, with multiplicity one.
Every other nonzero root has positive valuation. Therefore the chosen
double root differs from the center, and the cover can be written
{0,1,u} where u=0 is allowed, or v(u)>0. The first-derivative condition
at 0 and last-derivative condition at 1 are encoded by a_19=a_20=0 and
a_1=-1.

No rational-only root count, integral-valuation bound, J=18/J=17
exclusion, or small-cluster good-prime disjunction is used for C20.

## 3. Residue-field reduction gives precisely the finite necessary filter

For each j=2,...,18 choose the center whenever it is an available common
root. Otherwise choose 0 or u. A noncenter equation implies a_j lies
in the maximal ideal, since every term contains a positive power of
the noncenter witness. It need NOT lie in 19*O_K: ramification matters.
Reducing in the residue field gives a_j_bar=0 at such a position.
A center equation gives

    a_j_bar=-sum_(k<j) binom(j,k)*a_k_bar.

Although the residue field may extend F_19, induction from a_0=1 and
a_1=-1 shows that all a_j_bar belong to its prime field F_19.
The exact center-root equation, divided by 19, is integral and gives

    -1 + sum_(j=2)^18 (binom(20,j)/19)*a_j_bar = 0 in F_19.

The division is made in the exact characteristic-zero identity first;
we do not divide zero by zero in the residue field. No assertion about
ordinary coefficients modulo 19^2 in O_K is needed or generally valid
for noncenter branches. This is the crucial distinction from the earlier
rational-only audit's ordinary-modulo-361 derivation.

All 2^17 binary choices are exhaustively enumerated by
`computations/coordinator-three-complex-masks-v1.py`, using this normalized
prime-field recursion. Bit j-2 specifies a center choice. The final
condition has exactly 6,680 survivors. J, the largest unit-coefficient
index (not the largest center bit), has histogram

    6:1, 7:1, 8:3, 9:5, 10:26, 11:32, 12:101, 13:131,
    14:315, 15:461, 16:887, 17:1674, 18:3043.

J is used only for this diagnostic; none of its classes is removed.
Each survivor M has 2^(17-popcount(M)) choices of 0 or U at its noncenter
positions. Including all of them gives 6,224,952 exact families. The
canonical mask of an actual counterexample is among them. No converse
lifting claim is made about a surviving mask.

## 4. Exact integer families and compatibility certificates

Now fix a mask and a refinement. Set a_0=1,a_1=-1 and solve the same
triangular equations over Z[U], for j=2,...,18. The selected witness is
1 at a center bit and 0 or U otherwise. Set a_19=a_20=0, and form

    P(U)=f_U(1), Q(U)=f_U(U).

Every normalized algebraic counterexample has exactly those specialized
coefficients by induction and hence supplies a common root of P,Q.
Cases U=0,1, repeated selected witnesses and unused U are included;
this is harmless excess rather than an omitted degeneracy.

The earlier reviewed rational packet checked 772 of these masks,
1,493,024 families. Its conclusion for each explicit pair is algebraic:
P,Q have no common root over Qbar. The rational-only mask selection in
that packet does not restrict the algebraic meaning of its individual
nonzero-resultant certificates. The new normalized enumeration explicitly
verifies these 772 masks are a subset of the 6,680. The complementary
5,908 masks have 4,731,928 refinements and are a separate construction.
Both sets and their disjoint union have exact counts and sorted lists.

For a nonzero constant P there is no common root. Otherwise a certificate
specifies a prime where both actual integer degrees are retained and
the reduced polynomials have gcd 1. The integer Sylvester determinant
then has nonzero reduction, so its resultant is nonzero and no common
root over Qbar exists. The alleged witness is not reduced modulo that
auxiliary prime, so there is no denominator or ramification exception.

The complementary constructor reuses the frozen earlier construction's
polynomial helpers and traversal, with every change recorded in its
construction-provenance JSON. This is explicit code reuse, not independent
review. It has a dedicated subprocess with a 900-second timeout,
8,192-family checkpoints and deterministic 60,000-row gzip chunks.
Partial files do not establish a completed exhaustion. The completed run,
three separate miss resolutions, hashes and resource records are in the
[completion note](coordinator-three-complex-witnesses-v1-completion.md)
and frozen manifest. These remain constructor evidence pending audits.

If all these pairs have the stated incompatibility certificates, the
counterexample's parameter is excluded in every family, proving C20.
That implication and every new certificate still require two independent
audits. The previously accepted rational T1-T3 packet remains a separate
unchanged result; no complex conclusion has yet been promoted.
