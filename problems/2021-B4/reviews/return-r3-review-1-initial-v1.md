# Initial independent whole audit of the seven 2021 return packets

2026-10-17 UTC. Reviewer: /root/review_2022_complexity_r2, a nonconstructor
of every packet examined here. Requested model/reasoning: gpt-6.1-sol/max.
An independent effective-setting readback is unavailable. This report,
the per-claim ledger and source checks are frozen before reading any
other review or conclusion about these seven packets.

**Finding:** I found no substantive mathematical objection to the stated
scoped claims after reconstructing the whole combined argument. I request
no author repair. This is one review, not a promotion. The second
independent audit and the coordinator's decision remain necessary.
Nothing here establishes a full mask exclusion, the repeated-root branch,
degree 20, the annual classification, a rational lift, or novelty.

The seven targets, in problems/2021-B4/notes/, are:

| Suffix after reasoning-return-r3- | SHA-256 |
| --- | --- |
| candidate-v1.md | 0caf8d3f8df7144a7768230d566930da91ca107ab552935e9c2a73556f8aacc8 |
| mirror-candidate-v1.md | 20a72646d0e1bcfcf2ef3ca907d1363c6576a96df42dc2cb6909e11976e2945c |
| collision-candidate-v1.md | e7eab1257632a3d0e96c7e8eebcb9389197c7cd9041aca3dda6b5b463763c5ee |
| parity-candidate-v1.md | 6506e371c2a3eb8506f75c55ef3d80be9933ecbcd187be21fe5bd18932fe8789 |
| sparse-descent-candidate-v1.md | 5c454767cda1bbbe4e4e4041256b837e6b0086c5489ad68007f522b24eccc864 |
| parity-barrier-candidate-v1.md | 284e7ddc5a3d26111d2af4bd169b7fc6d2739a169a70ae3d38ff68d3ac03ada5 |
| transfer-candidate-v1.md | 0bcc9898ff010abf489f7b4c58d4a5011e91df99ab680bd0094d76054b3e3961 |

Each complete candidate, companion research/source record and manifest
was read. The supplemental metadata record checks the frozen artifacts
and their declared inputs. I did not rerun any old finite certificate,
search supports, enumerate masks, use a CAS, or run a mathematical
program. All mathematics below is hand reconstruction. Metadata hashing
is the only executable calculation performed for this audit.

## 1. Official domain and the accepted interface

The official 2021 Paper B, page 2, requires an actual rational common
root for each derivative order 1 through d-1. Its open part (b) asks for
the degrees d >= 2 having the stated pure-power conclusion. The witness
may depend on the derivative. This is stronger than a nonconstant
rational gcd, and weaker than requiring all roots of f to be rational.
I checked that domain directly against the official PDF and statement.md.
I neither investigated nor reproduced the preliminary part.

The new claims all concern a hypothetical nontrivial degree-20 polynomial
in the accepted normalization

    f = X^20 - 20X^19 + sum_(j=2)^18 binom(20,j)a_j X^(20-j),
    a_j in Z_(19), f(0)=f'(0)=f(1)=0,
    J=15, ord_0(f)=2.

The accepted normalization makes 1 simple and the only valuation-zero
root. The accepted Newton result gives fourteen slots of valuation 1/14,
three further nonzero slots of valuation greater than 1/14, and zero
twice. Accepted T1 says no three rational values cover all derivatives.
I read its full frozen coverage argument and acceptance scope: T1 is an
already reviewed finite-certificate dependency, not a new computation
performed or silently validated by this audit.

Here is the relevant local reconstruction, which also checks the exact
interface needed by every later packet. At least two distinct small
values must be rational by T1, since a rational number cannot have
valuation 1/14. Remove those two slots from the three small slots. The
remaining slot is fixed by the local Galois group and belongs to Q_19,
including when it repeats a value already removed. Thus all three local
small roots u,v,w have positive integer valuations. Over Q_19,

    f = X^2(X-u)(X-v)(X-w)B, B=(X-1)g,

where g is monic degree 14. Its nonleading coefficients have positive
valuation because its roots all have valuation 1/14; their membership
in Q_19 makes these valuations integral. Its constant coefficient has
valuation exactly 1. Hence g is Eisenstein. This proves local
irreducibility and does not assign rational coefficients to g.

Writing B=sum b_i X^i gives

    v(b0)=1, b1,...,b13 in 19Z_19, b14=-1 mod19, b15=1.

Expansion of the three small linear factors gives
c2=-b0 uvw, c3=b0(uv+uw+vw)-b1 uvw, and the corresponding
c4,c5,c6 identities in accepted D1. In particular c5 has valuation 1,
c5/19=b0/19 modulo 19, and, for the minimum small valuation nu,

    v(c2)>=1+3nu, v(c3)>=1+2nu, v(c4)>=1+nu.

For the sole-H3 subcase, accepted D2/D3 give equal small valuations nu.
The residue reconstruction uses

    F=T^2(T-U)(T-V)(T-W)=T^5-sT^4+tT^3-zT^2.

At a nonzero root R, H2(F)(R)=R(9R^2-5sR+2t) and
H4(F)(R)=5R-s. H2 at zero is nonzero. An H4 witness of residue
zero would force s=0 and a nonsquare discriminant 15R^2. With its
nonzero witness S, s=5S; an H2 witness in another slot would give
7A^2-17SA+8S^2=0, whose discriminant is 8S^2, also nonsquare.
Therefore both actual rational witnesses occupy the unique S slot;
the other two slots reduce to 2S. This gives the rational simple r,
R=r/19^nu nonzero, and two Q_19 roots s,t of scaled residue 2R.
The H3 initial values at 0,R,2R are respectively 8R^2,-2R^2,8R^2.
These are statements about actual slots, not only possible residues.

I also checked the accepted D5 interface: replacing selected noncenter
rational witnesses by zero changes the triangular normalized coefficients
by multiples of 19^nu. The divided center equation therefore makes
q0 divisible by 19^nu. The bound nu<=v(q0) requires q0 nonzero.
No new packet removes that qualification.

The dependencies were read as accepted, scoped project results.
No unreviewed return, mirror, collision or parity packet was used as an
accepted premise in checking a later one. Shared identities are
reconstructed below rather than justified by a cross-reference.

## 2. General packet G1 and G2: local roots and global carriers

For pi^14=19, a coefficient of pi^(-19)f(pi T) has its original
valuation plus (i-19)/14. At i=5 and i=19 this is zero. At
6<=i<=18 it is at least (i-5)/14>0; at i=20 it is 1/14.
The three low-coefficient bounds put i=2,3,4 strictly above zero,
and i=0,1 vanish. Thus the claimed integral reduction is exactly

    Fbar = -T^19 + lambda T^5, lambda=c5/19 mod19 != 0.

For a fractional-cluster root alpha, alpha/pi is a unit with reduction
T0 satisfying T0^14=lambda. For 1<=k<=5 the T^19 contribution
has zero k-th Hasse derivative modulo 19, and the other contribution
is lambda binom(5,k)T0^(5-k), nonzero. Hasse scaling therefore gives
the exact valuation (19-k)/14 for H_k(f)(alpha).

Let Q be the monic irreducible polynomial of alpha over Q. The local
minimal polynomial g divides Q in Q_19[X], so M=deg Q>=14.
If M>=15, the just-proved nonvanishing excludes orders <=5 and
the derivative degree excludes orders >=6. If M=14, then Q=g
locally. Only order 6 survives the degree test. Divisibility there
would identify Q with the monic D14, but its X^13 coefficient is
-14, a unit, while g's is divisible by 19. This excludes it.
If any global conjugate were a common root, Q would divide that
derivative, giving the same contradiction. G1 concerns the entire
global carrier, and its proof does not replace that carrier by g
when M>14.

For G2, choose two distinct rational small values and divide by
X^2(X-1)(X-u)(X-v). The rational degree-15 quotient has precisely
the two local irreducible factors (X-w) and g. If w is rational,
division makes g rational and Eisenstein. Repetition of a removed
small value causes no difficulty: one remaining copy is simply w.
If w is not rational, a proper rational factor of the quotient must
have local degree 1 or 14; its complementary factor then has degree
14 or 1. Either possibility supplies a rational linear factor with
root w, which is impossible. Thus the quotient is irreducible over Q.
In this case u,v are simple and the exact rational root set is
{0,1,u,v}. G1 now excludes that whole degree-15 carrier, including w.

In both alternatives every nonrational root of f belongs to the
unrecycled carrier. Consequently all derivative common roots are
rational, and the rational derivative gcds split into linear factors,
with whatever multiplicities they actually have. This conclusion
does not say f splits over Q. With exactly four rational values,
T1 makes each indispensable: if one were never a sole rational
common-root value, the other three would cover all orders.
In the all-small-rational alternative four or five values can occur;
no five-to-four cover reduction is asserted. I found no gap in G1/G2.

## 3. General packet C1, C2, W and the two retained barriers

At 2r the constant b0 uniquely dominates B. Every term of B' is
divisible by 19, including its degree-14 and degree-15 terms, whose
root-power valuations are at least 13nu and 14nu. Thus B(2r) has
valuation 1 and B'(2r)/B(2r) is integral. For
U=X^2(X-r)B,

    U(2r)=4r^3B(2r), v(U(2r))=3nu+1,
    U'(2r)/U(2r)=2/r+B'(2r)/B(2r), with valuation -nu.

Put h_e=H_e(f)(r). The exact even part is E=sum h_e T^e over even
6<=e<=20; h20=1 and every other coefficient here is divisible
by 19. The absence of degrees 0,2,4 uses f(r)=H2(r)=H4(r)=0.
The double zero at 0 gives f(2r)=2E(r), f'(2r)=2E'(r).

For the unique least weight m=alpha+e nu, the exponent e is a
19-unit, so E(r),E'(r) have valuations m,m-nu. Let
P=(s-2r)(t-2r), S=(s-2r)+(t-2r). Direct differentiation gives

    P=f(2r)/U(2r),
    S=P U'(2r)/U(2r)-f'(2r)/U(2r).

It follows that v(P)=m-3nu-1, v(S)>=m-4nu-1.
All possible weights are at least 1+6nu; in particular
2v(S)-v(P)>=m-5nu-1>0. Thus the product term strictly
dominates in (s-t)^2=S^2-4P. This proves

    v((s-t)^2)=alpha-1+(e-3)nu,
    leading unit=-2 eta R^(e-3)/(beta15 a15),
    eta=h_e/19^alpha mod19.

The valuation is even because s,t belong to Q_19, and the unit is
a nonzero square there. Equivalently alpha+nu is odd. This also
proves s!=t. If H6(r)=0 and a12 is a unit, h8 has valuation 1
and is uniquely least, so nu is even and v(s-t)=5nu/2.
Combining that with D5 is valid only in the stated q0!=0,
v(q0)=1 realization subcase. If every earlier even term vanishes,
e=20 has alpha=0, giving nu odd and v(s-t)=(17nu-1)/2.
No tied-weight case is covered by this test.

For C2, the stipulated noncenter rational H6 witness makes a14
nonunit. D14 has unit linear coefficient 14a13, and on 19Z_19
its difference at x,y is (x-y) times that unit plus 19Z_19.
It is injective, and simple-root Hensel lifting gives one zero
there. Its rationality comes from the actual rational common
witness, not Hensel lifting. Thus its value zeta is exactly 0,r,
or one of the two 2R slots. If zeta=0 then a14=0 exactly.
Otherwise the unit linear term gives v(a14)=nu and the residue
in equation (7); finite valuation greater than nu is impossible.

When Z=zeta/19^nu is 0 or 2R, the D14 difference gives

    h6/19^(nu+1)=7 beta13 a13(R-Z) mod19 != 0,

using 14 beta14=7 beta13. This term is uniquely least in E.
The leading square is 70 sigma R^3(Z-R), because beta13/beta15=5.
For Z=0 this is 6 sigma R^4; for Z=2R it is 13 sigma R^4.
The first scalar is a square modulo 19 and the second is a
nonsquare. Hence exactly the stated necessary square classes and
separation v(s-t)=2nu follow. For zeta=r the extra a12-unit
condition invokes the preceding even-nu test; the packet does not
invent an unconditional separation. In the v(q0)=1 application
nu=1, so the middle option is excluded and the two other necessary
alternatives follow. Neither alternative is asserted to exist.

For W, the low rational supports are {r},{1},{r},{1} at
orders 2,3,4,5. At order 5, c5 uniquely dominates at every
small root and is nonzero at 0. The center supplies the required
witness. G1 excludes nonrational roots when a complete common-root
statement is made. Order 1 may be covered by 0, and order 19
only by 1. If no rational 2R slot occurred at orders 6 through 18,
{0,1,r} would cover all orders, contradicting T1.
In the irreducible-degree-15 case there is just one rational
2R slot, which is indispensable at a higher order and is simple
as a root of f. Its gcd at that order is exactly its linear
factor because there is no other common-root value. If H6 uses
0 or r under C2, injectivity excludes a competing 2R witness at
that order; the required additional order lies in 7 through 18.

I checked both guards against extending these conclusions.
In the accepted low-order family B has centered odd part T^15,
so the even part is exactly T^16(T^2-r^2)^2. Its three weights
tie and both E(r),E'(r) vanish. The family satisfies only the
recorded low conditions, and is not a counterexample to C1 or W.
In characteristic 5, G=X^4-X^2 has H1,H3 sharing 0 and
H2=X^2-1 sharing +/-1. Frobenius gives G^5=X^20-X^10.
The normalized residue choice a1=-1,a10=-1, others zero,
has D1,D10 witnessed by 1 and other D_j by 0. This is a valid
first residue pattern, not a characteristic-zero lift.
It agrees with the original 2011 erratum's degree-20 warning.

## 4. Mirror packet M1: every actual top-witness alternative

The hypotheses here add the exact repeated root 2r and the five
even equations at r through order 14. They are essential.
Write E=T^16(h16+h18 T^2+T^4). Double zeros at 0,2r imply
E(r)=E'(r)=0. With r!=0 this yields

    h18=-2r^2, h16=r^4.

The exact top normalized derivatives have the displayed plus sign
4a3 X in D4. Since h18=190D2(r), h16=4845D4(r), setting
h=96/95 gives a2=2r-h r^2 and the stated formula for a4.
Both a2,a4 are nonunits, including nu=1 when the two a2 terms
can cancel. Rational division removes all the small factors;
the quotient g is Eisenstein. The rational root set is therefore
exactly {0,1,r,2r}, without requiring G1/G2 as a premise.

If a3 were a unit, H17 must use 1, giving a3=2 modulo 19.
D4 is an isometry on 19Z_19. Its value at r has valuation
4nu-1>nu and is nonzero, so neither 0 nor 2r is a zero.
D4(1) is 5 modulo 19. This leaves no H16 rational witness.
Hence a3 is nonunit. The centers of D2,D3,D4 are now nonzero
modulo 19, and r cannot witness D2 or D4 because h18,h16
are explicitly nonzero.

Thus the H18 witness is 0 or 2r, forcing respectively
r=95/48 or r=95/142. Each has nu=1 and scaled residue
R=10 or 9. Let the H17 witness be delta*r with
delta=0,1,2 and the H16 witness eta*r with eta=0,2.
Solving D3 gives

    a3=3delta(delta-2)r^2+delta(3h-delta^2)r^3.

Subtracting D4(r) from D4(eta*r), inserting this formula and
dividing by r^3 yields exactly C+rA=0 with the packet's C,A.
I independently expanded the constant and r coefficients.
The six pairs (C,19A) modulo 19 are

    eta=0: (11,17), (4,7), (11,16);
    eta=2: (8,16), (15,7), (8,17).

They demand R=15,13,10 and 9,6,4 respectively.
Only eta=0,delta=2,R=10 or eta=2,delta=0,R=9 survive.
In the first case C=-8 and A=31-18h+1/4845=62068/4845,
forcing r=9690/15517<1, contrary to 95/48>1.
In the second C=8 and A=15-18h+1/4845=-15452/4845,
forcing r=9690/3863>2, contrary to 95/142<1.
All root alternatives, including the tie producing the repeated
root, have therefore been handled. The exact mirror subfamily
exclusion M1 checks; it is not an arbitrary repeated-root exclusion.

## 5. Collision packet RC1: exact displacement rather than a leading term

Assume the two 2R slots coincide at d. T1 makes d rational;
otherwise only 0,1,r would be rational roots. The rational
root set is exactly {0,1,r,d}. Put delta=d-2r and k=v(delta)>nu
when nonzero. The value delta=0 must be kept as a separate case.

With f=(X-d)^2U and E=T^(2m)A(T^2), exact evaluation gives

    E(r)=delta^2 U(2r)/2,
    E'(r)=delta^2 U'(2r)/2-delta U(2r).

Subtracting 2m E(r)/r gives

    2r^(2m+1)A'(r^2)
      =-delta U(2r)[1+delta(m/r-eta/2)],
    eta=U'(2r)/U(2r).

The bracket is a unit because k>nu. For nonzero delta this proves
k=(2m-2)nu-1+v(A'(r^2)) and
v(A(r^2))=2k+(3-2m)nu+1. For delta=0 it proves A'=0,
and reflection also gives A=0 at r^2. Conversely A'=0
forces delta=0; no root difference was divided out.

At m=3 the nonleading coefficients of A' are divisible by 19,
and its leading term 7r^12 is too. Hence k>=4nu.
For 3<=m<=8 the same reasoning gives k>=(2m-2)nu.
For m=9, A'=1, giving k=16nu-1 and excluding delta=0.
These identities allow tied weights, zero intermediate h_e,
and arbitrary large finite k. RC1 checks in its full scope.

## 6. Collision packet RC2: center, valuation and depth exclusions

The extra ladder makes E=T^16(h16+h18 T^2+T^4). The preceding
identity gives, for finite k,

    k=14nu-1+v(h18+2r^2)>=14nu,
    e0=h16+h18r^2+r^4, v(e0)=2k-13nu+1>=15nu+1.

For delta=0, e0=0 and h18=-2r^2,h16=r^4. These exact-zero
versions justify the same later lower bounds.

First suppose H18 uses the center, so a2=1.
Then h18=190(r-1)^2 has valuation 1 and h16 has valuation
2nu+1, giving v(D4(r))=2nu and a4 nonunit. If a3 is a
unit, H17 uses 1 and forces a3=-1 exactly. D4's isometry
excludes 0,r,d, while D4(1)=a4-1 is nonzero. If a3 is
nonunit, H17 must use zeta in {0,r,d}, and H16 must use
xi in {0,d}. Writing lambda=zeta/r and mu=xi/r modulo 19,
division by r^2 gives 12(lambda-1)=0 for mu=0, or its
negative for mu=2. Thus zeta is the actual r and
a3=-r^3+3r^2-3r.

I recomputed D4(0)/r^2 and D4(2r)/r^2:

    Q0=304/51+(4/51-8)r+(3-2/51-1/4845)r^2+error,
    Q2=304/51+(4/51-16)r+(11-2/51-1/4845)r^2+error.

The e0 contribution has valuation at least 13nu. Moving d to
2r changes the integral D4 value by valuation at least k,
so its contribution after division has valuation at least
12nu. For nu>=2 the constant has valuation 1 and all other
terms at least 2. For nu=1 divide by 19: the equations are
10+4R-12R^2=0 or 10-4R-12R^2=0 modulo 19.
After division by 2 the discriminant is 124=10 modulo 19,
a nonsquare. Thus H18 cannot use 1, for any nu.

It follows that a2=2z-z^2 for z in {0,r,d}, and
kappa=a2/r modulo 19 is in {0,2,4}. Suppose nu>=2.
If z=r, h18=0 and h16=-r^4+e0 is nonzero. Otherwise
v(h18)=nu+1 and v(h16)=3nu+1<4nu.
In both cases v(D4(r))>=3nu and a4 is nonunit.
The a3-unit alternative again leaves no H16 witness:
D3's center gives a3=2 modulo 19, whereas D4's center
is 5 and its noncenter values are excluded by isometry.
For a3 nonunit, H17 uses zeta in {0,r,d} and
a3/r^2=3lambda(lambda-kappa) modulo 19.
H16 uses xi in {0,d}. After division by r^3 its equation is

    L=4(1-mu^3)+6kappa(mu^2-1)
        +12lambda(lambda-kappa)(mu-1)-6(kappa-2)=0.

Here -r^4/4845 is strictly higher because nu>=2;
the displacement errors have valuation at least 11nu.
For mu=0 this is 16-12lambda^2+12kappa(lambda-1),
and for mu=2 its negative. At lambda=1 it is 4.
At lambda=0 or 2 it would require kappa=14 or 9,
outside {0,2,4}. Thus nu=1.

Now the noncenter H18 equation gives v(h18)>=2; finite k
is at least 15. To exclude k>=17 and exact delta=0,
put epsilon=h18+2r^2. The Euler bounds give

    v(epsilon)>=4, v(e0)>=22,
    a2=2r-(96/95)r^2+rho2, v(rho2)>=3,
    h16=r^4+rho16, v(rho16)>=6.

For finite k the precise error valuations are k-13 and
2k-12 for epsilon,e0; for delta=0 both vanish.
This yields h16 nonzero of valuation 4 and v(D4(r))=3.
The a3-unit case is excluded as before. For a3 nonunit,
replace zeta,xi by lambda*r,mu*r with errors of valuation
at least 17. The a3 expansion is the mirror expression
plus an error of valuation at least 4.

After eliminating a4 and dividing by r^3, C+rA is divisible
by 19^2. This modulus is justified term by term:
rho2 contributes at least 3+2-3=2, the a3 error
4+1-3=2, and rho16/4845 at least 6-1-3=2.
Replacing d by 2r contributes much higher error.
Since h18 is nonzero of valuation 2, its witness is 0 or d.
The unit factors h*r and (4-h)*r give respectively

    r=95/48 mod19^3 or r=95/142 mod19^3.

The six C,A alternatives already independently expanded in section 4
leave only the same two pairs. In those pairs

    95/48-9690/15517=1008995/(48*15517),
    95/142-9690/3863=-1008995/(142*3863).

The denominators are 19-units, and
1008995=19^2*2795 with 2795=2 modulo 19.
Each difference has valuation exactly 2. Since v(A)=-1,
v(C+rA)=1, contradicting the required valuation at least 2.
This excludes finite k>=17 and delta=0. It leaves precisely the
stated necessary alternatives nu=1 and k=15 or 16.
Neither remaining depth is proved to exist or to be impossible.

## 7. Collision packet RC3: indispensability is a cover statement

All four rational values are indispensable by T1.
H1 has rational support {0,d}; H2,H3,H4 have {r},{1},{r};
H5 has {1} by its uniquely least c5 term, and H19 has {1}.
Under the ladder, r covers H6,H8,H10,H12,H14 whether or not
additional roots share those derivatives. Thus 0 and d can
only become sole rational witnesses at different orders in
{7,9,11,13,15,16,17,18}. For the order assigned solely to 0,
H_k(f)(0)=binom(20,20-k)a_(20-k)=0 exactly over Q.
The coefficient is nonzero, yielding one exact zero among
a2,a3,a4,a5,a7,a9,a11,a13. The argument is valid for rational
supports without any assertion that a complete gcd is linear.

## 8. Parity PP1 and PP2: one support, two lengths

Assume PP1's stated parity conditions and H3(1)=0.
P=D17 modulo 19 has degree 17, constant and linear terms zero,
and X^2 coefficient 3a15 nonzero. Its root 0 has multiplicity
exactly 2, and its root 1 follows from the exact equality
H3(1)=1140D17(1)=0 before reduction.
For 1<=j<=16,

    H_(17-j)(P)=binom(17,j)D_j mod19,

and all these scalars are units. If a_j is zero modulo 19,
0 witnesses it. If a_j is a unit, every actual rational
noncenter f-root reduces to zero and cannot witness D_j;
the actual witness must be 1. Thus P has the claimed
two-value Hasse-CA cover. It is not asserted to have only
two roots, nor is a characteristic-zero two-value theorem used.

Let I be the actual unit support among indices through 15.
It contains 1,15 and has only odd indices. The integer recursion
b_j=0 off I, b_j=-sum_(k<j)binom(j,k)b_k on I, b0=1
matches a_j modulo 19 by induction. In particular the
nonvanishing conditions b_j!=0 modulo 19 on I must be retained.
Define F_I(Z)=sum b_j binom(Z,j). Its coefficients are
19-integral, and its degree is 15. The recursion gives
F_I(m)=0 exactly for m in I, especially m=1.

The residual center equality gives F_I(17)=0 modulo 19.
The original divided center equality is
-1+sum beta_j a_j=0. Since beta_j are integral and a_j
with j>15 are nonunits, it gives F_I(20)/19=0 modulo 19,
or F_I(20)=0 modulo 19^2. Comparing coefficients only
modulo 19 is enough after dividing by the one factor 19.
It does not identify the original polynomial with the integer model.

Because 15! is a 19-unit, reduction at 17 is reduction at -2,
and Taylor expansion at the exact root 1 gives
F_I(20)=19F'_I(1) modulo 19^2. Thus the two endpoint
forms in PP1 are equivalent for this same I.
The direct coefficient check also agrees:
binom(17,j)=-(j+1) for odd j, and the derivative of
binom(Z,j) at 1 is -1/[j(j-1)] for odd j>=3.
These yield respectively sums 3 and -1 in equation (8).

The published descent recurrence is an identity of rational
polynomials, obtained first for infinitely many integer lengths.
Its sign gives F_I=(-1)^|I|d(I;Z), with I itself rather than
its complement. This also follows by adding the last index
to the displayed integer recursion; I checked the example {1,3}.
Consequently negative length -2 is a legitimate polynomial
evaluation, not a combinatorial count of permutations.

For PP2 I rederived the repeated-root Euler identity above,
rather than assuming RC2. It gives k>=14nu and e0 of
valuation at least 15nu+1, or the exact-zero counterpart.
A noncenter H18 witness z in {0,r,d} makes a2=2z-z^2
nonunit and h18 of valuation at least nu+1 when nonzero.
Then h16 has valuation at least min(3nu+1,4nu), and its
division by 4845 in the exact a4 identity still gives
a4 nonunit. The even ladder supplies a6,a8,a10,a12,a14
nonunit; accepted D1 supplies a16,a18 nonunit.
This proves precisely the parity condition required by PP1.
Neither proof assumes joint endpoint impossibility.

## 9. Sparse-descent SD1 and residue certificate PB1

I checked SD1 independently of PP1. For I={1,15},
F_I=1-Z+14binom(Z,15), and F_I(-2)=3-224=7 modulo 19.
For I={1,k,15}, J={1,k}, the recurrence gives

    F_J=1-Z+(k-1)binom(Z,k),
    F_J(-2)=4-k^2, F'_J(1)=-(k+1)/k.

The two endpoint conditions for I become
F_J(-2)+16F_J(15)=0 and
F'_J(1)+F_J(15)/(15*14)=0 modulo 19.
Since 16*15*14=-3 modulo 19, eliminating the last value
gives k^3-k+3=0. This factors as
(k-15)(k^2-4k+15) in F_19[k]. The quadratic discriminant
is 13, a nonsquare, so the only field root is 15, outside
the allowed intermediate indices. This excludes sizes 2
and 3, without requiring the nonvanishing coefficient
condition and without deciding any larger support. SD1 checks.

For PB1, the five stated nonzero normalized indices give

    P=X^17+2X^16+11X^14+X^12+9X^10+14X^2.

The binomial residues are 17,15,13,11,3 at indices
1,3,5,7,15. Multiplication by the proposed coefficients
gives exactly the displayed expansion. P(1)=38=0 modulo 19,
and its X^2 coefficient is nonzero. Off I the constant of
D_j vanishes. On I, the displayed center values are
0,0,19,133,114, all divisible by 19, and D17(1)=152.
Thus all sixteen required derivative orders have an actual
common root 0 or 1 in F_19. This checks the entire finite
certificate without a computer or support search.

In its integer model, b_j match the residues by the same
recursion, and |I|=5 makes F_I=-d(I;Z).
The four quantities a3/6,a5/20,a7/42,a15/210 are
13,3,11,11 modulo 19, summing to zero. Hence F'_I(1)=-1,
so d(I;20)/19=1 modulo 19. The quotient is integral because
F_I(1)=0 and 20=1 modulo 19.
This proves both the residual success and the second-endpoint
failure. It neither refutes PP1 nor supplies a lift to Q.

I also checked the exploratory exact factor identity in PB1's
source log: with Z=T^2 and C=r(r+delta), the centered
small factor is
T[(Z-C)^2+delta^2 Z]-2delta Z(Z-C).
Multiplying by V(Z)+TW(Z) and taking its even part gives
the stated relation with Z^7(h16+h18Z+Z^2).
No rational family, integrality, interpolation rank or
remaining-witness assertion is derived from that relation.

## 10. Transfer TA1 and TA2, including the critical-value limit

For 3<=m<=8, with the preceding even derivatives zero at r,
write E=T^(2m)A(T^2). The repeated-root Euler identity
again gives, for finite delta,

    k>=(2m-2)nu,
    v(A(r^2))>=(2m-1)nu+1.

For delta=0 the latter value is exactly zero. Every
nonconstant nonleading term of A(r^2) has valuation
at least 2nu+1. Its leading term has valuation
2(10-m)nu>=4nu>=2nu+1. Subtracting them proves
v(h_(2m))>=2nu+1, without choosing a least weight.
The endpoint m=8 is valid because A still has degree 2.

Set j=20-2m. Dividing by binom(20,2m) gives
v(D_j(r))>=2nu. If a_(j-1) is a unit, the linear
coefficient j a_(j-1) is a unit for 4<=j<=14,
so D_j is an isometry on 19Z_19. Both distances from
r to 0 and d have valuation nu. Neither value can
therefore be a zero of D_j. An actual rational
noncenter witness, if stipulated, must be the actual r.

If a_(j-2) were also a unit after this transfer,
h_(2m+2) would have valuation 1 and all earlier even
coefficients would be zero. Its weight is uniquely
least, including against the degree-20 term because
the difference is at least 2nu-1>0. It controls
both E(r) and E'(r). For delta=0 this contradicts
E(r)=0. For finite delta, direct reflection gives
valuations 2k+3nu+1 and k+3nu+1, differing by k>nu;
the unique even term would make them differ by nu.
This proves the asserted next even coefficient is
nonunit and completes TA1. Hensel lifting is not
substituted for the actual common-witness assumption.

For TA2 suppose all six a3,a5,...,a13 are units and
each of H6,H8,H10,H12,H14 has a rational noncenter
common witness. Successive TA1 applications force
all five equations at r, using a13,a11,a9,a7,a5.
The m=8 application with a3 then covers H16 by r
if any noncenter witness exists, and by 1 otherwise.
Each of H7,H9,H11,H13,H15,H17 has a unit normalized
constant, so only 1 among rational f-roots can
witness it. H3,H5,H19 can also use 1, and H2,H4 use r.
Choose an actual rational H18 witness. If it is 0
or d, use that same double root for H1; otherwise
use 0 for H1. This covers every order by at most
{1,r,x} with x=0 or d, contradicting T1.
The conclusion is exactly that one of the five
higher even orders has 1 as its sole rational
common-root value. It does not require H16 to
have a noncenter witness or exclude nonrational
common roots by assertion.

Under the same odd-unit hypotheses all odd
Taylor coefficients at 1 except the linear one
vanish. Thus f(1+T)=V(T^2)+cT=T[g(T)+c],
where V(0)=0, g is odd monic degree 19, and
c=f'(1) is a 19-unit. The latter follows also
by differentiating f modulo 19 at 1.
The double roots 0,d occur at T=-1,d-1,
both nonzero; oddness of g and evenness of g'
give g(1)=g(1-d)=c and g'(1)=g'(1-d)=0.
These are valid rational critical-value equations.
They do not supply common roots with every
derivative of g, so no prime-degree conclusion
may be applied to g. The packet states that limit.

## 11. Adversarial boundaries and decision

I specifically tested the logical places where a stronger false
statement could have entered: assigning Q coefficients to a
local factor; discarding a global conjugate outside the fractional
cluster; equating a residue slot with an actual rational root;
assuming a Hensel zero rational; treating two equal reduced roots
as an actual double root; using a unique-weight test at tied weights;
dividing by delta in its zero case; losing the one factor of 19
in the top-derivative errors; replacing the degree-20 divided
endpoint by only the residual degree-17 one; omitting coefficient
nonvanishing; treating coefficient support size as recycled-root
count; and importing a characteristic-zero or all-roots-rational
theorem in a weaker domain. None occurs in the stated claims.

The exact mirror exclusion is properly restricted by its extra ladder.
The collision-depth restriction leaves depths 15,16 and cases without
the ladder. PP1 leaves joint-endpoint supports unresolved; SD1 excludes
only sizes below 4. PB1 deliberately fails the second endpoint.
TA2 needs every stated odd unit and applies only to the repeated-slot
branch. The global factor result leaves all actual rational witness
equations unresolved. All these scope qualifications are mathematically
material and must accompany any accepted register.

No substantive issue remains in this initial audit, and no repair is
requested. Only the coordinator may promote a scoped result after
reading the second independent audit. Latest authoritative account
telemetry supplied by root was 24% weekly total during this audit,
reset 1792745187, with a 90% total ceiling and integration reserve.
No worker Git, shared-file edit, peer comparison, new mathematical
computation, external contact, charge or separately billed API occurred.
