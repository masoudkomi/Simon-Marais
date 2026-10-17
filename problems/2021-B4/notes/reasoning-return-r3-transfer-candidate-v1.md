# A transfer from repeated roots to higher even witnesses

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
review_2021_reasoning_j15_r2. Requested gpt-6.1-sol/max; effective
readback unavailable. Two fresh independent nonconstructor whole
audits are required. No mask, whole repeated branch, degree20
solution, annual classification or novelty is claimed. No
mathematical program, enumeration or CAS was used.

## Setup and proposed results

Use accepted normalized J15 multiplicity-two sole-H3 D3:

    f=X20-20X19+sum_(j=2)^18 binom(20,j)a_j X^(20-j),
    a_j in Z_(19), f(0)=f'(0)=f(1)=0,
    H3(1)=0, H2(1)!=0, H4(1)!=0.

There is a rational simple r, v(r)=nu>=1, sharing H2,H4.
Suppose the two other small slots coincide at a double root d,
with d/r=2 mod19. Accepted T1 forces d rational, and the exact
rational root set is{0,1,r,d}. Write delta=d-2r. If delta!=0,
put k=v(delta)>nu. The exact case delta=0 is allowed below.

**Proposed TA1 (transfer).** Let3<=m<=8 and assume the even
derivatives H2,H4,...,H_(2m-2) all vanish at r.
Then v(H_(2m)(r))>=2nu+1. If, in addition,

    a_(19-2m) is a unit, and H_(2m)
    has an actual rational noncenter common root,

that root must be the actual r. Thus H_(2m)(r)=0.
In this event a_(18-2m) must be nonunit.

The witness hypothesis means existence of a noncenter common
root, even if the center is also a common root. It is weaker
than assuming the center equation is nonzero. The exact
rational root, not merely a residue or a Q19 root, is forced.

**Proposed TA2 (higher essential center).** If every one of

    a3,a5,a7,a9,a11,a13

is a19-adic unit, then at least one of

    H6,H8,H10,H12,H14

has1 as its SOLE RATIONAL common-root value with f.
In particular at least one of those center equations vanishes.
This conclusion holds for arbitrary positive integer nu and
both delta=0 and delta!=0. It requires no extra ladder as an
initial hypothesis.

Equivalently, if all five displayed even derivatives possess
rational noncenter common roots, at least one of those six
odd normalized coefficients is nonunit. These remain necessary
conditions for a specified repeated-root branch, not full
canonical-mask exclusions or a proof about distinct2R roots.

Only accepted D1/D3 and T1 are theorem inputs. Earlier return,
collision and parity packets are not treated as accepted lemmas.

## 1. A uniform even-Taylor valuation

Accepted D1 writes

    f=(X-d)^2 U, U=X2(X-r)B,
    U(2r)=4r3 B(2r), v(U(2r))=3nu+1,
    eta=U'(2r)/U(2r)=2/r+an integral element.

Here B has constant valuation1, coefficients1..13 divisible19,
degree14 coefficient-1 mod19 and leading degree15 coefficient1.
These facts give v(B(2r))=1 and B'(2r)/B(2r) integral.

Let E(T)=[f(r+T)+f(r-T)]/2. The even zero hypotheses give

    E(T)=T^(2m)A(T2),
    A(Z)=h_(2m)+h_(2m+2)Z+...+Z^(10-m),
    h_e=H_e(f)(r).

Every h_e for even e<=18 is divisible19, while h20=1.
Exact double-root evaluation gives

    E(r)=delta2 U(2r)/2,
    E'(r)=delta2 U'(2r)/2-delta U(2r).

Subtract2m E(r)/r:

    2r^(2m+1)A'(r2)
      =-delta U(2r)[1+delta(m/r-eta/2)].             (1)

For finite delta the bracket is a unit. Since m<=8, the monic
A has degree at least2. Its derivative at r2 is divisible19:
every nonleading differentiated coefficient has that factor,
and its leading term has valuation at least2nu.
Consequently, for delta!=0,

    k=(2m-2)nu-1+v(A'(r2))>=(2m-2)nu,
    v(A(r2))=2k+(3-2m)nu+1>=(2m-1)nu+1.            (2)

If delta=0, the first reflection equality instead gives
A(r2)=0 exactly; this is enough for the same next estimate.

Every nonconstant NONLEADING term of A(r2) has valuation at
least2nu+1. The leading term has valuation
2(10-m)nu>=4nu>=2nu+1. Thus, subtracting these terms from A(r2),

    v(h_(2m))>=2nu+1.                              (3)

This proof neither divides by delta in its exact-zero case
nor assumes a unique least even Taylor weight. It handles
the tied minima retained by repeated roots.

## 2. Injectivity forces the exact noncenter witness

Put j=20-2m, so4<=j<=14. Then

    H_(2m)=binom(20,2m)D_j, v(binom(20,2m))=1,
    v(D_j(r))>=2nu.

If a_(j-1)=a_(19-2m) is a unit, the linear coefficient
j a_(j-1) of the integral D_j is a unit. For x,y in19Z19,

    D_j(x)-D_j(y)=(x-y)(j a_(j-1)+19Z19).

In particular its difference has valuation exactly v(x-y).
The other possible rational noncenter f-roots0,d both have
distance of valuation nu from r. Since D_j(r) has valuation
at least2nu>nu, neither D_j(0) nor D_j(d) can be zero.
Thus any stipulated rational noncenter common witness is r
itself, and its derivative value is exactly zero.

Suppose now a_(j-2)=a_(18-2m) were a unit.
The next even Taylor coefficient h_(2m+2) would have valuation1:
D_(j-2)(r) reduces to its unit constant a_(j-2).
All previous even coefficients vanish by the hypotheses and
the just-proved transfer. Hence at T=r the single term
h_(2m+2)r^(2m+2) uniquely minimizes the even Taylor weights.
All later subleading terms have an extra positive r-power;
the monic degree20 term is higher because
(20-(2m+2))nu>=2nu>1. The same unique term controls E'(r),
since its exponent2m+2 is a19-unit.

If delta=0, the resulting E(r)!=0 contradicts its reflection
equality E(r)=0. If delta!=0, direct reflection gives

    v(E(r))=2k+3nu+1,
    v(E'(r))=k+3nu+1,

because the linear-in-delta term in E' uniquely dominates
its delta2 eta term. Thus their valuation difference is k>nu.
The unique even Taylor term would instead make this difference
exactly nu. This contradiction proves a_(j-2) nonunit and
completes proposed TA1.

## 3. A three-value rational cover gives TA2

Assume all six odd coefficients a3,a5,...,a13 are units.
Suppose, to get a contradiction, that every one of
H6,H8,H10,H12,H14 has a rational noncenter common root.

Starting with accepted H2(r)=H4(r)=0, apply TA1 successively
at m3,4,5,6,7. Its unit coefficients are respectively
a13,a11,a9,a7,a5. This forces

    H6(r)=H8(r)=H10(r)=H12(r)=H14(r)=0.

For H16, use m8 and the remaining unit a3.
If H16 has any rational noncenter common root, TA1 forces
that root to be r. If it has no such root, the contest
hypothesis supplies1. Thus H16 can in either case be covered
by{r,1}. No assumption about availability of its center was
made.

The unit coefficients a13,a11,a9,a7,a5,a3 make the normalized
constants for H7,H9,H11,H13,H15,H17 units.
At any rational noncenter f-root the corresponding normalized
derivative has that nonzero residue, so each of these odd
orders can use only1. H3 uses1 by hypothesis; H5 can use
only1 because J15 makes its small-root constant a15 a unit.
H19 uses only1. The low even orders H2,H4 use r.

It remains only H1 and H18. H1 is shared by both double roots
0,d. Let w be any actual rational H18 common witness.
It belongs to{0,1,r,d}. If w is0 or d, choose that same
value for H1. If w is1 or r, choose0 for H1.
Every derivative is therefore covered by

    {1,r,x}, with x equal to0 or d.

This contradicts accepted T1's minimum of four distinct
rational witness values. The contradiction proves that some
even order in{6,8,10,12,14} has no rational noncenter common
root at all. Its required rational common root is then1,
which is its sole rational common-root value. This is TA2.

No claim about nonrational derivative common roots or full
gcds is needed. Both0 and d are rational by the separate
T1/valuation argument in the setup.

## Scope, sources and unresolved work

Under TA2's unit hypotheses there is also an exact alternative
representation, requiring no even-witness assumption. All odd
Hasse derivatives at1 of orders3,5,...,19 vanish, by the same
unit-constant argument and the stipulated H3 center. Hence

    f(1+T)=V(T2)+cT=T[g(T)+c],
    c=f'(1), V(0)=0, g(T)=V(T2)/T.

Here V is monic degree10, g is an odd monic polynomial of
degree19 over Q, and c is a19-unit (f mod19 is X19(X-1)).
The double roots0,d give the exact rational equations

    g(1)=g(1-d)=c, g'(1)=g'(1-d)=0.

This is only a critical-value reduction. It does NOT make g
a degree19 Casas-Alvero polynomial, so the known prime-degree
theorem cannot be applied to it without additional hypotheses.
No critical-value incompatibility or classification is claimed.

The rational normalization, local residual estimates, sole-H3
root roles and T1 are the accepted project results with their
published attribution. Their exact source fingerprints are
retained in the companion record. The Euler identity, valuation
estimate, transfer and cover argument are reconstructed here.

The original2011 erratum still prevents the prime5 shortcut.
CLO's all-roots-rational theorem is not applied. No new external
theorem, download, novelty claim, larger mask search or finite
digit test is used.

TA1 can derive parts of the ladder from explicit unit and
actual witness hypotheses. TA2 requires all six specified
odd coefficients to be units; it does not prove they always
are. Missing odd units, a first higher center, distinct2R
roots and the full rational-lifting system remain unresolved.

