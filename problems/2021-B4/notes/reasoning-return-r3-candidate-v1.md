# J15 double zero: global derivative factors and an even-part collision test

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
review_2021_reasoning_j15_r2, now in a new construction task after
freezing all assigned 2017 audits. Requested gpt-6.1-sol/max; independent
effective-setting readback is unavailable. Two fresh independent
nonconstructor adversarial whole audits are required. No complete mask,
degree20, annual classification or novelty is claimed. No enumeration,
Hensel table, CAS or mathematical program is a premise.

## Inputs and notation

Use the accepted rational-witness normalization, Newton result, T1 and
J15 double-zero D1--D5:

    f=X^20-20X^19+sum_(j=2)^18 binom(20,j)a_j X^(20-j),
    a_j in Z_(19), f(0)=f'(0)=f(1)=0,
    J=max{j:v_19(a_j)=0}=15, ord_0 f=2.

The center1 is simple. At least four distinct rational values are needed
to cover all derivatives. Fourteen root slots have valuation1/14. The
three further nonzero small slots lie in Q19, have positive integer
valuations, and include at least two distinct rational values. Only
over Q19, D1 gives

    f=X^2(X-u)(X-v)(X-w)B, B=(X-1)g,
    deg g=14, g monic Eisenstein over Z19.

Write f=sum c_i X^i, B=sum b_i X^i and
beta_j=binom(20,j)/19 for2<=j<=18. Then v(b0)=v(c5)=1,
b_i in19Z19 for1<=i<=13, b14=-1 mod19, b15=1, and

    c5/19=beta15*a15, beta13/beta15=5.

For nu_min the minimum small-root valuation, D1 gives
v(c2)>=1+3nu_min, v(c3)>=1+2nu_min, v(c4)>=1+nu_min.
The monic degree-j normalized derivative is

    D_j=H_(20-j)(f)/binom(20,j)
       =sum_(l=0)^j binom(j,l)a_l X^(j-l), a0=1,a1=-1.

The cited accepted project inputs attribute the normalization to
Castryck--Laterveer--Ounaies and separately verify the rational cover.
No factorization of g over Q is an input.

## G1. No fractional-cluster root is globally recycled

**Proposed G1.** The whole rational irreducible factor containing the
fourteen-slot fractional cluster is coprime to every H_k(f),1<=k<=19.

Choose pi with pi^14=19 in an algebraic extension of Q19. Then
F(T)=pi^(-19)f(pi T) is integral and reduces to

    Fbar(T)=-T^19+lambda T^5,
    lambda=c5/19 mod19 nonzero.                       (1)

Only exponents5 and19 have zero coefficient weight. Exponents6,...,18
have positive weights at least(i-5)/14, exponent20 has weight1/14,
and the lower-coefficient bounds put exponents2,3,4 strictly above
the supporting line. Constant and linear terms vanish. This checks
the precise reduction, not just its root count.

For a fractional root alpha, T0=alpha/pi is a unit and its reduction
satisfies T0bar^14=lambda. For1<=k<=5, Hasse scaling gives

    H_k(f)(alpha)=pi^(19-k) H_k(F)(T0),
    H_k(Fbar)(T0bar)=lambda binom(5,k) T0bar^(5-k)!=0.

Here binom(19,k)=0 mod19 and binom(5,k)!=0. Thus exactly

    v(H_k(f)(alpha))=(19-k)/14,1<=k<=5.                (2)

Let Q be alpha's monic irreducible polynomial over Q. It divides f,
and g divides Q over Q19, since g is alpha's local minimal polynomial.
Put M=deg Q>=14. If M>=15, (2) excludes a common root for k<=5,
while k>=6 gives deg H_k<=14<M. If M=14, then Q=g over Q19.
Only k=6 remains after (2) and the degree bounds. Divisibility there
would force Q=D14, but D14 has X^13 coefficient -14, a19-adic unit,
whereas g's X^13 coefficient is divisible by19. This is impossible.
Therefore Q divides no derivative. Every global conjugate of alpha
is unrecycled. This argument never assigns rational coefficients
to the local g when M>14.

## G2. Exact global factor dichotomy and complete recycled set

Choose two distinct rational small roots u,v. Over Q define

    Q15=f/[X^2(X-1)(X-u)(X-v)].

It is monic degree15, with local factorization Q15=(X-w)g. If w
is rational, then division gives g in Q[X], Eisenstein at19; all
three small slots are rational, allowing repetition. If w is not
rational, Q15 is irreducible over Q: a proper rational factor must
be a union of the two local irreducible factors of degrees1 and14.
It therefore has degree1 or14, in either case giving a rational
linear factor. Its root cannot have fractional valuation and would
have to be w, a contradiction.

In the second alternative the rational root set is exactly{0,1,u,v},
with u,v simple. G1 excludes Q15 itself, so w is unrecycled too.
In the first alternative g contains all nonrational roots and G1
excludes it. Thus in BOTH alternatives all common roots with all
nonconstant derivatives are rational. Every derivative gcd splits
into rational linear factors, with its possible ordinary multiplicities.
The whole f need not split over Q.

In the degree15 alternative T1 forces all four rational values to
be necessary. Each is the sole common-root value of some derivative:
if not, removing that value would leave a three-value cover. In
the all-small-rational alternative the rational root set has four
or five values, and the minimal cover may have four or five.
No fourth-value or complete-mask exclusion is claimed.

## C1. A reflection criterion beyond unit a14

Now impose accepted D3's sole-H3 hypotheses:

    H3(f)(1)=0, H2(f)(1)!=0, H4(f)(1)!=0.

All small valuations equal an integer nu>=1. There is a rational
simple root r with R=r/19^nu mod19 nonzero, and two roots s,t in
Q19 with s/19^nu=t/19^nu=2R mod19. The same actual r shares H2
and H4. s,t may coincide; one may be non-Q. Write

    f=(X-s)(X-t)U, U=X^2(X-r)B,
    h_k=H_k(f)(r),
    E(T)=[f(r+T)+f(r-T)]/2
        =sum_(e even,6<=e<=20) h_e T^e.               (3)

Here h0=h2=h4=0, h20=1, and h_e in19Z19 for even e<=18, since
the normalized derivatives are integral and binom(20,e) has valuation1.

**Proposed C1.** Suppose the nonzero weights v(h_e)+e nu have a UNIQUE
minimum, at e. Put alpha=v(h_e), an integer. Then s!=t and

    v((s-t)^2)=alpha-1+(e-3)nu                         (4)

is even. If eta=h_e/19^alpha mod19, its nonzero leading unit is

    (s-t)^2/19^(alpha-1+(e-3)nu)
       =-2 eta R^(e-3)/(beta15 a15) mod19,             (5)

so the displayed residue must be a square. In particular alpha+nu
must be odd. Tied minima are not covered.

Proof. Put m=alpha+e nu. The even indices6,...,20 are all units
modulo19, so the same unique term controls E(r) and E'(r), giving
valuations m,m-nu. Exact reflection and the double zero at0 give

    f(2r)=2E(r), f'(2r)=2E'(r).

D1 shows v(B(2r))=1 and B'(2r)/B(2r) integral. Indeed b0 is the
unique least-valuation term of B(2r); differentiation still leaves
every numerator term divisible by19. Consequently

    U(2r)=4r^3 B(2r), v(U(2r))=3nu+1,
    U'(2r)/U(2r)=2/r+B'(2r)/B(2r), valuation -nu.

Let d_s=s-2r,d_t=t-2r,P=d_s d_t,S=d_s+d_t. Direct differentiation
gives, without dividing by any root difference,

    P=f(2r)/U(2r),
    S=P U'(2r)/U(2r)-f'(2r)/U(2r).

Thus v(P)=m-3nu-1, v(S)>=m-4nu-1. Every possible weight is at least
1+6nu, including the top weight20nu. Hence m>1+5nu, and

    2v(S)-v(P)>=m-5nu-1>0.

In (s-t)^2=S^2-4P the product term uniquely dominates, proving(4)
and nonvanishing. Its leading term is -2E(r)/(r^3 B(2r)).
Using the unique term of E and B(2r)/19=beta15 a15 mod19 gives(5).
No assertion that s,t are rational over Q is used.

### Conditional nonunit-a14 parity obstruction

If H6(f)(r)=0 and a12 is a unit, e=8 has valuation1 and is the
unique least weight: the earlier even terms vanish, and later
weights, including h20, are larger. Therefore

    nu is even, v(s-t)=5nu/2,
    -2 beta12 a12 R^5/(beta15 a15) is a nonzero square. (6)

Here a14 is automatically nonunit, because D14(r)=0 and r=0 mod19.
This reaches a branch outside accepted unit-a14 D4. More generally,
if H6(r),H8(r),...,H_(e-2)(r) vanish and a_(20-e) is a unit for
even e<=18, the unique-e criterion forces nu even.

Combining(6) with accepted D5 excludes the RESTRICTED realization
subcase q0!=0,v(q0)=1,a12^0 nonzero mod19 AND H6(f)(r)=0:
D5 forces nu<=1, contradicting positive even nu. This does not
exclude a full center mask, since H6 need not share r.

If every even derivative through18 vanishes at r, then E(T)=T^20.
C1 instead forces nu odd, v(s-t)=(17nu-1)/2, and the unit square
-2R^17/(beta15 a15). These are necessary conditions, not a lift.

## C2. A sixth-derivative witness trichotomy

Assume D3 and a13 a unit. Suppose H6 has a rational noncenter
common root; the contest forces one if H6(f)(1)!=0. Then a14 is
nonunit. On19Z19 the integral D14 has linear term14a13 X and

    D14(x)-D14(y)=(x-y)(14a13+19Z19).

It is injective there, and the simple-root Hensel argument at0
gives exactly one zero zeta in19Z19. The actual common witness is
therefore uniquely zeta. Its rationality follows from the stipulated
rational common witness, not from Hensel's lemma. It is0,r,or a2R-slot root.
If zeta=0 then a14=0 exactly; otherwise
a14=-14a13 zeta+O(zeta^2) gives v(a14)=nu and

    a14/19^nu=-14a13(zeta/19^nu) mod19.               (7)

A finite v(a14)>nu is incompatible with these hypotheses.

Put sigma=a13/a15 mod19. The necessary alternatives are:

| H6 noncenter common root | Necessary residue condition | Separation |
| --- | --- | --- |
| zeta=0 | sigma is a square | s!=t, v(s-t)=2nu |
| zeta=r | if a12 is a unit, nu is even | use C1; no other unconditional split claim |
| zeta/19^nu=2R | sigma is a nonsquare | s!=t, v(s-t)=2nu |

For the first and third rows let Z=zeta/19^nu mod19, so Z=0 or2R.
The integral D14 difference, 14 beta14=7 beta13, gives

    h6/19^(nu+1)=7 beta13 a13(R-Z) mod19 !=0.

Thus alpha=nu+1 at e=6, with weight7nu+1 uniquely below all later
even weights. C1 gives v((s-t)^2)=4nu and leading unit

    (s-t)^2/19^(4nu)=70 sigma R^3(Z-R) mod19.

For Z=0 this is6 sigma R^4; for Z=2R it is13 sigma R^4.
The nonzero squares modulo19 are{1,4,9,16,6,17,11,7,5}:
6 is square and13 is not. This proves both square-class restrictions,
the exact separation and exclusion of the repeated-root case in
these two rows. No root table is used.

If v(q0)=1,a12,a13 are units and H6(f)(1)!=0, then D5 gives nu=1
and the middle row is impossible. A square sigma forces zeta=0,
a14=0; a nonsquare sigma forces a rational2R witness, v(a14)=1
and v(s-t)=2. This remains a restricted necessary realization
condition, not proof that any row is impossible or lifts.

## W. Where the fourth rational witness must occur

G1--G2 concern COMPLETE common-root sets. Under D3 the low-order
supports are exactly

    H2:{r}, H3:{1}, H4:{r}, H5:{1}.

For H3 the accepted initial values at0,R,2R are nonzero; H2,H4
have only the unique R slot. H5 is nonzero at all small roots by
the degree-five initial form and at0 since c5!=0, so it must use1.
G1 excludes all remaining roots. H1 can always use0; a repeated
2R root adds no necessity at this order. H19 uses only1.

Some rational2R-slot root must therefore share H_k for6<=k<=18,
or{0,1,r} would cover every derivative contrary to T1. In the
irreducible-degree15 alternative exactly one2R slot is rational,
and G2 makes it the sole common-root value for some such higher
derivative. It is simple, so that gcd is its exact rational linear
factor. If H6 uses0 or r in C2, the necessary additional order
lies in7,...,18. With three distinct rational small roots either
2R slot can supply it. No unproved four-value exclusion is used.

## The tied-weight barrier is real

C1 does not assert that one weight is always least. In the accepted
low-order family with r,2r,2r, the centered odd factor is
T(T^2-r^2)^2, and the residual factor has odd part T^15.
Consequently its even part is exactly

    E(T)=T^16(T^2-r^2)^2
        =T^20-2r^2 T^18+r^4 T^16.

All three weighted terms have weight20nu and cancel at r together
with their derivative, permitting the double2r root. This explains
why the reflection test does not contradict that barrier family.
It satisfies only the recorded low conditions, not the full contest
hypothesis. General tied weights, other low-center patterns, multiple
centers, lower J and the complete nonunit branch remain unresolved.

## Prime5 and primary-source boundary

The primary August2011 Draisma--de Jong erratum retracts the degree20
consequence because5 is bad for base degree4. Indeed in F5,

    G=X^2(X^2-1), G^5=X^20-X^10

is a nontrivial Hasse-CA residue pattern. G shares H1,H3 at0
and H2=X^2-1 at +/-1. All these roots lie in F5; rational reduced
witnesses do not remove the bad point.

Even the binomial-normalized first residue system allows it:
take a0=1,a1=-1,a10=-1 and all other a_j=0 in F5.
Then fbar=X^20-X^10; D1 and D10 use1, and every other D_j,
2<=j<=19,j!=10, uses0 because D_j(0)=a_j. D10(1)=1-1=0.
This exact finite-field formula is not a characteristic0 example
or a claimed lift. It shows why a first-level prime5 test alone
does not close the problem. No two-prime exclusion is proposed.

CLO Proposition19 explicitly needs all roots rational (or its stated
unramified-number-field extension); it is not a rational recycled-
witness result. Its full proof and the original erratum were
rechecked. Our arguments use the separately accepted D1 and
rational witness inputs and make no all-roots-rational inference.
The eight accepted single-low-center patterns remain necessary
patterns, never complete mask exclusions. No novelty is established.

