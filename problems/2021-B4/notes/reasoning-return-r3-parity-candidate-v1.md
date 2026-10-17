# An odd-support projection to two descent-polynomial congruences

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
review_2021_reasoning_j15_r2. Requested gpt-6.1-sol/max; independent
effective readback unavailable. Two fresh independent nonconstructor
whole audits are required. This is a necessary structural criterion and
a recorded unresolved obstruction, not a branch or degree20 exclusion.
No enumeration, CAS, mathematical program or support table was run.
No novelty is claimed.

## Precise scope

Use the accepted normalized J15 multiplicity-two setting

    f=X20-20X19+sum_(j=2)^18 binom(20,j)a_j X^(20-j),
    a_j in Z_(19), f(0)=f'(0)=f(1)=0,
    ord_0 f=2, J=max{j:v_19(a_j)=0}=15,

with an actual rational common root for every nonconstant derivative.
Accepted D1/Newton implies every rational root except1 reduces to0
modulo19. The other roots are not assumed rational. Write

    D_j=sum_(k=0)^j binom(j,k)a_k X^(j-k),
    a0=1,a1=-1;  H_(20-j)=binom(20,j)D_j.

For proposed PP1 assume additionally

    H3(f)(1)=0,
    a_j=0 mod19 for every even j in{2,4,...,18}.     (P)

No sole-low-center or repeated-root hypothesis is needed for PP1.

**Proposed PP1.** There is a subset

    I subset{1,3,5,7,9,11,13,15},  1,15 in I,

with the exact nonvanishing coefficient condition in section3, whose
published MacMahon descent polynomial d(I;Z) satisfies

    19 divides d(I;17),
    19^2 divides d(I;20).                           (1)

Equivalently, because this polynomial is19-integral and degree15,

    d(I;-2)=0 and d'(I;1)=0 mod19.                 (2)

The derivative is the ordinary derivative of a polynomial in the
length variable Z. It is not a Casas-Alvero derivative of f.

The reduction D17 over F19 is itself a nontrivial degree17
Hasse-CA polynomial, with a cover using only0 and1 and zero of
multiplicity exactly2 at0. This is a positive-characteristic
necessary consequence, not a counterexample in characteristic zero.

**Proposed PP2.** The repeated2R-root setting with the exact even
ladder H6(r)=H8(r)=...=H14(r)=0 and a noncenter rational H18 witness
implies(P). Hence PP1 applies to that explicitly restricted setting.
Section5 reconstructs the needed Euler bound directly; no earlier
unreviewed return or collision theorem is used as an accepted input.

What is NOT proved: that no I satisfies(1), that a satisfying I lifts,
or that the finite support projection classifies a full mask.
The endpoint obstruction in(1) remains an explicit research target.

## 1. A residual degree17 CA polynomial

Reduce the normalized coefficients modulo19 and put

    P(X)=D17(X) mod19.

Its leading coefficient is1. Since J=15, a16=a17=0 mod19.
Thus P(0)=0 and P has no linear term. Its X2 coefficient is
binom(17,15)a15=3a15 mod19, a unit, so its zero at0 has exact
multiplicity2. The extra center hypothesis H3(f)(1)=0 gives
P(1)=0 because H3=1140D17 and the equality holds over Q before
reduction. Division by1140 does not lose that exact zero.

For1<=j<=16,

    H_(17-j)(P)=binom(17,j) D_j mod19,

with the binomial coefficient a unit. If a_j=0 mod19 then
D_j(0)=0. If a_j!=0 mod19, any actual rational f-witness of
D_j must be1: at every other rational f-root the reduction of
D_j is its nonzero constant a_j. Therefore D_j(1)=0 mod19.
Both0 and1 are roots of P, so these choices verify every required
Hasse-CA condition for P. This includes j=1, where D1=X-1.

No other rational f-root is introduced, and no local-only root is
used as an actual rational witness. The reduction P can have
other F19 or extension roots; we assert the existence of the
two-value cover, not that its complete root set is{0,1}.

## 2. The exact integer coefficient model for a support

Let I be the set of j in{1,...,15} for which a_j is a unit.
By(P), I consists of odd indices, and it contains1 and15.
Set b0=1. Define ordinary INTEGERS b1,...,b15 by

    if j notin I, b_j=0;
    if j in I, b_j=-sum_(k<j) binom(j,k)b_k.          (3)

In particular b1=-1. These are integer recursions, not numerical
approximations. Induction shows

    a_j=b_j mod19 for0<=j<=15.

At a nonzero residue a_j the exact actual rational witness is1
as above, so D_j(1)=0 forces precisely(3) modulo19.
At a zero residue both sides are zero by construction.
For j>=16 all a_j vanish modulo19 by J15, including the even
indices already in(P).

For the actual support to equal I, rather than merely be contained
in I, one must retain

    b_j!=0 mod19 for every j in I.                  (4)

It is not legitimate to discard this nonvanishing requirement.

Define a rational polynomial in a NEW variable Z by

    F_I(Z)=sum_(j=0)^15 b_j binom(Z,j).             (5)

All its denominators divide15!, so all coefficients are19-integral.
Its degree is15 because b15!=0 mod19. For every m in I the
recursion makes F_I(m)=0 EXACTLY over Q: terms with j>m vanish
at the nonnegative integer m. In particular F_I(1)=0 exactly.

## 3. The two endpoint divisibilities

The exact center equality for H3 gives D17(1)=0. Reducing it and
using b_j congruent a_j yields

    F_I(17)=0 mod19.                               (6)

The original center root f(1)=0, divided by19 in the normalized
formula, gives

    -1+sum_(j=2)^18 [binom(20,j)/19]a_j=0.

All terms beyond15 have a_j=0 mod19. Since F_I(20) equals
1-20+sum_(j=2)^15 binom(20,j)b_j, an actual integer multiple19,
the same congruence gives

    F_I(20)=0 mod19^2.                             (7)

This step does not claim f equals the integer coefficient model,
or that the latter has an exact root at1. It compares only the
divided center equality modulo19.

Because F_I is19-integral,17=-2 mod19 gives (6) equivalent to
F_I(-2)=0 mod19. Taylor expansion at the exact root1 gives

    F_I(1+19)=19 F'_I(1)+19^2 C, C in Z_(19).

Thus(7) is equivalent to F'_I(1)=0 mod19.
The denominator condition degree15<19 is what makes this
Taylor argument valid without a hidden factorial denominator19.

For a direct coefficient check,

    binom(17,j)=-(j+1) mod19 for odd j,
    [d/dZ binom(Z,j)]_(Z=1)=-1/[j(j-1)]
        for odd j>=3.

Therefore the same two equations can be written

    sum_(j in I, j>=3) (j+1)b_j=3 mod19,
    sum_(j in I, j>=3) b_j/[j(j-1)]=-1 mod19.        (8)

These are exact finite-field equations on the single recursively
defined support vector, not an inferred infinite criterion from
sample evaluations.

## 4. Attribution and identification with descent polynomials

For a finite set I of positive indices, d(I;n) counts permutations
of n letters whose descent set is exactly I, for n>max I.
Its extension to a polynomial in n is classical MacMahon theory.

The precise recurrence used here is published as Proposition2.1
in Diaz-Lopez--Harris--Insko--Omar--Sagan, Descent polynomials,
arXiv1710.11033v2:

    d(I;Z)=binom(Z,m)d(I-minus{m};m)
                -d(I-minus{m};Z),  m=max I.        (9)

A brief verification also fixes orientation: select the m entries
in an initial block with descent set I-minus{m}; the remaining
entries form an increasing final block. The concatenation either
has the extra descent at m or does not, giving(9).

Adding the last selected m in(3),(5) gives

    F_I(Z)=F_(I-minus{m})(Z)
                -F_(I-minus{m})(m)binom(Z,m).

Induction from F_empty=1 and(9) proves exactly

    F_I(Z)=(-1)^|I| d(I;Z).                         (10)

For example I={1,3} gives F_I=1-Z+2binom(Z,3), which is
d({1,3};Z). Thus no complement or reversal of I has silently
been substituted. Equations(6),(7) prove(1), and Taylor gives(2).

Marashdeh's arXiv2608.14726 TheoremB already connects the
one-nonzero-recycled-root triangular recursion with MacMahon
descent counts. We attribute that general connection and make
no novelty claim for(10). The present application records the
SAME support at degrees17 and20, with the second endpoint
divided by19. The source does not establish nonexistence of
such a support for us; the multi-root rational lifting problem
is not replaced by its one-root characteristic-p statement.

## 5. Why the repeated-root ladder supplies all even nonunits

This section gives the exact scoped application PP2. Assume
accepted sole-H3 D3, the two2R slots equal a double root d,
the five extra even equations through H14 at r, and an actual
rational noncenter H18 common witness. T1 makes d rational:
otherwise only0,1,r are rational f-roots. Put delta=d-2r,
k=v(delta)>nu if delta!=0.

Use accepted D1 to write

    f=(X-d)^2 U, U=X^2(X-r)B,
    U(2r)=4r^3 B(2r), v(U(2r))=3nu+1,
    eta=U'(2r)/U(2r), v(eta)=-nu.

The same coefficient estimates as in D1 give B'(2r)/B(2r)
integral, so eta=2/r+an integral element.

The even Taylor part is

    E(T)=T16(h16+h18T2+T4).

Double roots at0,d give
E(r)=delta2 U(2r)/2 and
E'(r)=delta2 U'(2r)/2-delta U(2r).
Subtract16E(r)/r to obtain the exact identity

    2r17(h18+2r2)
      =-delta U(2r)[1+delta(8/r-eta/2)].

If delta!=0 the bracket is a unit, so k>=14nu since h18
is divisible19. Moreover

    e0:=h16+h18r2+r4,
    v(e0)=2k-13nu+1>=15nu+1.

If delta=0, the same identities give e0=0 and
h18=-2r2, so the needed bounds remain valid.

A noncenter H18 witness z is0,r or d. Its equation is
a2=2z-z2, so D2(r)=(r-z)(r+z-2). Hence a2 is nonunit and v(h18)>=nu+1
when h18 is nonzero. Consequently

    h16=-h18r2-r4+e0,
    v(h16)>=min(3nu+1,4nu).

The exact identity
a4=h16/4845-r4+4r3-6a2r2-4a3r makes a4 nonunit.
For even j6,8,10,12,14, the ladder is D_j(r)=0,
which reduces to a_j=0 mod19. Accepted D1 also makes
a16,a18 nonunit. Together with a2,a4 this proves(P).
No conclusion of the earlier unreviewed collision packet is
assumed as an accepted theorem.

## Unresolved structural obstruction and limits

It would be useful to prove joint nonvanishing: for every odd
I subset{1,3,...,15} containing1,15 and satisfying(4),
at least one of d(I;-2),d'(I;1) is nonzero modulo19.
THIS IS NOT PROVED OR ASSERTED TRUE HERE.

No support enumeration or computation was used to decide it.
Even its truth would exclude only(P), and then the stated
repeated-ladder application. A support satisfying the congruences
would still be only a necessary residue pattern, with no rational
lift, exact common roots or complete mask established.

Attempts to use real root bounds for descent polynomials do not
settle these finite-field conditions. Likewise all-real-root
versions of Casas-Alvero do not apply to our unused roots.
The old2011 prime5 erratum remains in force; no second-prime
argument is asserted. This packet does not redo the J16 or
three-value certificates and does not enlarge any mask search.


