# 2021 return packets: independent whole audit 2

2026-10-17 UTC. Reviewer coordinator root, a nonconstructor of these
seven 2021 construction packets. This initial full report is frozen
before reading the peer return-review1 report or conclusions. Author
progress messages and candidates were available; peer findings were not.
All seven full mathematical texts were read and reconstructed. Accepted
D1-D5, normalization/Newton and T1 are scoped inputs, not re-enumerated.
No CAS, digit lifting, support enumeration or new computation was used.

## Verdict and exact scope

No substantive objection to G1,G2,C1,C2,W; exact-mirror M1; collision
RC1-RC3; parity PP1,PP2; sparse SD1; residual PB1; transfer TA1,TA2,
including the stated critical-value representation. These are partial
restrictions in explicit normalized branches. They exclude no full new
degree or J15 mask. The joint descent nonvanishing question remains an
unproved target, expressly not a theorem. No novelty established.
This review is not acceptance until both whole reports are reconciled.

## Setup, rationality and accepted inputs

The rational-witness normalization is monic degree20,
a0=1,a1=-1,a_j in Z_(19), f0=f'0=f1=0, center1 simple,
J15 and ord0=2. Accepted T1 needs at least four rational values covering
all derivative orders. Newton gives fourteen slots of valuation1/14,
so none is rational, and three further nonzero small slots. At least
two distinct small slots are rational. The accepted D1 one-remaining-slot
Galois argument puts all three in Q19, not necessarily Q. Its local
factor B=(X-1)g has degree15, g Eisenstein14; b0 has valuation1,
b1..b13 are divisible19, b14=-1mod19,b15=1. In sole-H3 D3 all small
valuations are the same integer nu, with a unique rational r at residueR
and two slots at2R. Actual H2,H4 use that same r. No rationality of a
local factor is silently inferred.

## G1: global factor and every derivative

Put pi14=19 and F(T)=pi^-19 f(piT). The X5 coefficient has valuation1,
the X19 coefficient is-20, and the lower-coefficient bounds put powers
2,3,4 strictly above the edge. Powers6..18 and20 have positive excess
weight. Thus F is integral and Fbar=-T19+lambda T5,lambda nonzero.
For a fractional root alpha, T=alpha/pi is a unit with Tbar14=lambda.
For k1..5, H_k(Fbar)(Tbar)=lambda*binom(5,k)*Tbar^(5-k) is nonzero,
since binom(19,k)=0mod19 and binom(5,k) is a unit. Scaling gives exact
valuation(19-k)/14. All five derivatives are nonzero at alpha.

The rational minimal polynomial Q of alpha has g as a local factor,
hence degreeM>=14. If M>=15, degrees of H_k for k>=6 are<=14 and
exclude divisibility. If M14, its local factor is exactly g; only H6
can still have sufficient degree after the first five exclusions. Its
monic form D14 has X13 coefficient-14, whereas g has that coefficient
divisible19. Thus it cannot equal Q. Over characteristic zero, one
common algebraic root of Q and a rational derivative forces Q to divide
that derivative. This excludes EVERY global conjugate, even a small
one globally conjugate to the fractional cluster. It proves G1 without
assuming g rational prematurely.

## G2 and W: complete root support

Remove the known rational factors X2(X-1)(X-u)(X-v) for distinct rational
small u,v, leaving monic Q15 over Q with local factors(X-w)g. If w is
rational, division makes g rational and Eisenstein. Otherwise any proper
rational factor is a union of the two local irreducible factors of
degrees1,14, so either it or its complement is rational linear. That
root cannot have fractional valuation and must be w, impossible. Thus
Q15 is irreducible. These give the claimed exhaustive dichotomy and,
using G1, every derivative common root is rational. Repeated rational
small slots are permitted in the first case; u,v are simple in the
second. Minimal four-value cover forces each of exactly four rational
values to be the sole rational common-root option at some order.

In sole-H3 D3 the low rational supports are H2:{r},H3:{1},H4:{r}.
H5's normalized constant a15 is a unit, excluding every small root,
including0. G1 excludes the fractional cluster, so H5 uses1. H1 can
use0 and H19 uses only1. If no rational2R root appeared at orders6..18,
{0,1,r} would cover all derivatives, contradicting T1. In the degree15
alternative the one rational2R value must be a sole witness somewhere.
If H6 uses0 or r, its indispensable order lies7..18. This reconstructs W
with actual rational roots and full supports, not just residue classes.

## C1: unique weighted even term and square test

At r set E(T)=(f(r+T)+f(r-T))/2, h_e=H_e(f)(r). Low even terms vanish,
so E=sum_even6..20 h_e T^e, h20=1 and other h_e are divisible19.
Write U=X2(X-r)B. At2r, U=4r3B has valuation3nu+1 and
eta=U'/U=2/r+B'/B has valuation-nu, because B'/B is integral.
For d_s=s-2r,d_t=t-2r, P=d_s d_t,S=d_s+d_t, exact reflection gives
P=2E(r)/U and S=P eta-2E'(r)/U. These do not divide by s-t.

If a unique weight m=v(h_e)+e*nu is least, the exponent e is a19-unit,
so E(r),E'(r) have valuations m,m-nu. Hence
v(P)=m-3nu-1, v(S)>=m-4nu-1. Every weight is at least1+6nu,
so2v(S)-v(P)>=m-5nu-1>0. Thus the discriminant S2-4P is nonzero,
with valuation v(h_e)-1+(e-3)nu and leading unit
-2(h_e/19^v(h_e))*R^(e-3)/(beta15*a15).
Since s,t lie in Q19, this valuation is even and its unit is a square.
For even e, this requires v(h_e)+nu odd. Ties remain outside the lemma.

If H6r0 and a12 unit, h8 has valuation1 and uniquely least weight,
forcing nu even and v(s-t)=5nu/2, with the recorded unit square.
The same argument applies to a later first unit even coefficient.
With every even derivative through18 zero, only h20 remains and
nu must instead be odd. Combining the first case with accepted D5's
nu<=v(q0)=1 excludes only its explicitly restricted realization.
The recorded tied family has centered odd factor T(T2-r2)^2 and residual
odd part T15, giving E=T16(T2-r2)^2; its three equal weights really
cancel. No all-weights-unique assertion is made.

## C2: exact sixth witness

With a13 unit and a rational noncenter H6 witness, D14's constant a14
is nonunit and its linear coefficient14a13 is a unit. On19Z19 its
difference quotient is that unit plus19Z19, so it is injective; simple
Hensel at0 gives one local zero. The stipulated rational witness, rather
than Hensel alone, supplies rationality. It is0,r or a2R slot.
For nonzero zeta, a14=-14a13*zeta+O(zeta2), so v(a14)=nu.

For zeta residueZ=0 or2R, beta14*14=7beta13 and beta13/beta15=5
give h6/19^(nu+1)=7beta13*a13*(R-Z), nonzero. That term's weight
7nu+1 is uniquely below all later even terms. Applying the direct C1
identity yields discriminant unit70(a13/a15)R3(Z-R). At Z0 this is
6sigma R4; at Z2R it is13sigma R4. The square residues modulo19 are
1,4,9,16,6,17,11,7,5:6 square,13 nonsquare. Thus the two square classes
and separation2nu are correct. The r case is restricted by C1 when a12
is a unit; it is not unconditionally excluded. The q0 valuation1
corollary is accordingly scoped. No rational lift is claimed.

## Reflection identity for RC, M and TA

When the two2R slots form a repeated root d, T1 makes d rational, or
only three rational roots could cover the derivatives. The exact rational
root set is{0,1,r,d}. Put delta=d-2r, finite valuationk>nu or delta0.
Now f=(X-d)^2U. Exact evaluation gives
E(r)=delta2 U/2, E'(r)=delta2 U'/2-delta U.
If E=T^(2m)A(T2), subtract2mE(r)/r to obtain
2r^(2m+1)A'(r2)=-delta U[1+delta(m/r-eta/2)].
The bracket is a unit. For delta nonzero,
k=(2m-2)nu-1+v(A'(r2)), v(A(r2))=2k+(3-2m)nu+1.
For delta0, A(r2)=A'(r2)=0. At m3..8, A' is divisible19, including
its leading term because A has degree at least2. Therefore k>=4nu
at m3, proving RC1, and k>=(2m-2)nu generally. At m9, A'=1,
k16nu-1 and delta0 is impossible. No division by delta in its zero case.

## Exact mirror M1 and the RC2 approximate extension

Under the five extra even equations H6..H14 at r,
E=T16(h16+h18T2+T4). The Euler identity yields
k=14nu-1+v(h18+2r2)>=14nu and
e0=h16+h18r2+r4 has valuation2k-13nu+1>=15nu+1.
For exact mirroring, h18=-2r2,h16=r4,e00. The top normalized derivatives
are D2=X2-2X+a2,D3=X3-3X2+3a2X+a3,
D4=X4-4X3+6a2X2+4a3X+a4. The PLUS sign4a3 is retained throughout.
Also h18=190D2r and a4=h16/4845-r4+4r3-6a2r2-4a3r.

For H18 at center, a21, h18 val1, h16 val2nu+1. If a3 unit,
H17 uses1 forcing a3=-1, while D4 injectivity on19Z19 excludes0,d
because its value at r has higher valuation than distances; D4r is
nonzero and D4(1)=a4-1 nonzero. If a3 nonunit, H17 must use
zeta in{0,r,d}; H16 must use xi0 or d. Their leading equations force
zeta=r. Then D4(0)/r2 and D4(2r)/r2 have exact main terms
304/51+(4/51-8)r+(3-2/51-1/4845)r2 and
304/51+(4/51-16)r+(11-2/51-1/4845)r2.
The e0 errors have valuation>=13nu; d replacement errors>=12nu.
For nu>=2 the constant has unique valuation1. For nu1, division19 gives
10+4R-12R2 or10-4R-12R2. Their scaled discriminant is10, a nonsquare.
Thus H18 cannot use center.

For nu>=2, H18's noncenter witness gives a2/r residue kappa0,2,4.
The h16 expression is nonzero and a4 nonunit. A unit a3 again gives
H17 center a3=2mod19 and D4 center5mod19, while small injectivity
excludes other roots. Hence a3 nonunit. Put zeta/r=lambda0,1,2 and
xi/r=mu0,2. Divide D4xi by r3: the residual for mu0 is
16-12lambda2+12kappa(lambda-1), and for mu2 its negative.
Lambda1 gives4; lambda0 needs kappa14; lambda2 needs kappa9.
None is allowed, proving nu1 under the longer ladder.

For depthk>=17 or delta0, h18=-2r2+epsilon with v(epsilon)>=4,
a2=2r-(96/95)r2+rho2,v(rho2)>=3,
h16=r4+rho16,v(rho16)>=6. Again a3,a4 are nonunit; H18 uses0 or d,
H17 zeta=lambda r, H16 xi=mu r, up to errors of valuation>=17.
Eliminating a4 gives C+rA=0mod19², where
C=4(1-mu3)+12(mu2-1)+12lambda(lambda-2)(mu-1),
A=mu4-1+1/4845-6(96/95)(mu2-1)
  +4lambda(3*96/95-lambda2)(mu-1).
I checked the error powers explicitly: rho2 contributes>=2 after
normalization, rho3>=2, rho16/4845>=2, and root replacement more.
The six(C,19A) pairs are (11,17),(4,7),(11,16) at mu0 and
(8,16),(15,7),(8,17) at mu2. Solving gives R15,13,10 and9,6,4.
H18 itself gives r95/48 or95/142 modulo19³, hence R10 or9.
Only two cases remain: (mu0,lambda2) gives C-8,A62068/4845,
root9690/15517; (mu2,lambda0) gives C8,A-15452/4845,
root9690/3863. Their differences from the H18 roots are
+1008995/(48*15517) and -1008995/(142*3863).
Since1008995=19²*2795 and2795=2mod19, both differences have valuation2.
With v(A)=-1, C+rA has valuation1, contradicting the required19².
This proves RC2's residual possibilities nu1 and k15 or16, while not
excluding either. In the exact mirror case the same algebra is exact
and the two real comparisons (<1 vs95/48>1, >2 vs95/142<1) already
exclude it, reproducing the independent M1 proof without using RC2.

Exactly four rational root values and T1 force each indispensable.
H1 supports{0,d}; H2,H4 use r; H3,H5,H19 use1. The long even ladder
already includes r. Thus0,d must be sole rational witnesses at different
orders7,9,11,13,15,16,17,18. At the order for0 its normalized constant
is exactly zero, giving the eight listed possible coefficients. This is
RC3, not an inference about full gcds over algebraic closure.

## PP1, PP2 and published descent recurrence

Under even a_j nonunit and H3 center, reduce P=D17mod19. Its X2
coefficient3a15 is nonzero and its linear/constant terms vanish, so0
has exact multiplicity2; P1=0 follows from the exact H3 equation before
reduction. Its derivatives are unit binomial multiples of D_j. Off
unit support use root0; on support, all rational f-roots other than1
reduce0 and cannot witness a unit normalized constant, so use1. Thus
P really has a degree17 Hasse-CA cover0,1 in F19.

For I the actual odd unit support containing1,15, recursively set integer
b_j0 off I and b_j=-sum_(k<j)binom(j,k)b_k on I, b0=1. Induction gives
b_j=a_jmod19. Retain b_j nonzero on I. F_I(Z)=sum b_j binom(Z,j) is
19-integral of degree15. Exact recursion gives F_I(m)=0 at every m in I,
especially F_I1=0. H3 center gives F_I17=0mod19. From f1/19=0 and
binom20j divisible19 for j2..18, replacing a_j by b_jmod19 changes
the unDIVIDED model F_I20 by multiples19². Thus F_I20=0mod19².
Taylor at1 is legitimate because all denominators divide15!, giving
F_I(-2)=F'_I(1)=0mod19. For odd j, binom(-2,j)=-(j+1) and
binom'(1,j)=-1/[j(j-1)], reproducing both coefficient equations.

The primary MacMahon recurrence of Diaz-Lopez et al Proposition2.1,
including its full two-block counting proof, was read. Induction gives
F_I=(-1)^|I| d(I;Z), with no reversal/complement. Marashdeh's one-root
connection is attributed and not imported as a multi-root exclusion.
For PP2, the Euler long-ladder estimates and noncenter H18 imply a2
nonunit and v(h16)>=min(3nu+1,4nu). The a4 identity then gives nonunit
a4; the five ladder equations force a6,a8,a10,a12,a14 nonunit, and D1
already gives a16,a18 nonunit. This reconstructs the extra parity
hypothesis directly, without using an unaccepted RC theorem.

## SD1 and PB1 reconstructed by hand

For I{1,15}, F_I(-2)=3-16*14=7mod19. For I{1,k,15},
F_J=1-Z+(k-1)binom(Z,k), F_J(-2)=4-k²,F'_J1=-(k+1)/k.
Eliminating F_J15 from the two endpoints yields
F_J(-2)+3F'_J1=0, hence k³-k+3=0mod19.
This is(k-15)(k²-4k+15); the quadratic discriminant13 is nonsquare.
Since k differs15, no size3 support works. This excludes all six
intermediate k symbolically, no enumeration.

PB1's explicit a1=-1,a3=2,a5=3,a7=6,a15=11 gives
P=X17+2X16+11X14+X12+9X10+14X2. I checked the binomial residues
17,15,13,11,3 and the displayed coefficients. P1=38=0mod19.
D1,D3,D5,D7,D15 at1 are respectively0,0,19,133,114 modulo19,
while D17 center is152. Other derivative indices use0. This checks
every required derivative without a program. Its divided-center
sums a3/6,a5/20,a7/42,a15/210 are13,3,11,11, total0mod19;
F'_I1=-1 and, with odd support size5, d(I;20)/19=1mod19. The first
endpoint is realizable, the second fails. There is no Q lift claim.

## TA1, TA2 and the critical-value representation

For m3..8 with previous even derivatives zero, the Euler identity above
gives v(A(r²))>=(2m-1)nu+1, or A(r²)0 in the exact delta0 case.
Every other nonconstant term has valuation>=2nu+1, including the monic
leading term since degA>=2. Hence v(h2m)>=2nu+1. If a_(19-2m) is a
unit, D_(20-2m) has unit linear difference quotient on19Z19. Its value
at r has valuation>=2nu, but distances to0,d have valuationnu. Neither
can be a zero. Any rational noncenter common witness must therefore
be the ACTUAL r, forcing the next even equation exactly.
If a_(18-2m) were unit, the next even term would be uniquely least in
E,E'. Its valuation difference would be nu, whereas reflection gives
k>nu (or E(r)0 at delta0), contradiction. This establishes TA1,
including endpoints m8 and the claimed next coefficient nonunit.

With all a3,a5,...,a13 units, assuming noncenter witnesses H6..H14
successively forces the long ladder. For H16, a3 unit forces witnessr
if any noncenter exists, else center1 covers it. All higher odd
orders have unit normalized constants and use only1, including H5
from a15 and H19. H2,H4 use r. Pick an H18 rational witness; if it is
0 or d, use it also for H1, and if it is1 or r use0 for H1. This gives
a three-value cover contrary to T1. Thus some H6..H14 has SOLE rational
center witness, TA2. It does not require no nonrational common root.

All odd Taylor coefficients at center1 beyond the linear term then
vanish. Thus f(1+T)=T[g(T)+c] for odd monic g degree19,c=f'1 a19-unit.
Double roots0,d imply g1=g(1-d)=c,g'1=g'(1-d)=0. The derivative sign
is consistent with odd g and even g'. No CA property of g follows.

## Sources, barriers and remaining obligations

The complete original2011 erratum was read; prime5 is bad for base
four and the old degree20 claim was retracted. Direct F5 checking of
G=X4-X2 gives derivative common roots0 and+/-1; G5=X20-X10. In the
normalized residue model a1=-1,a10=-1, others0, D1,D10 use1 and all
other D_j use0. This is a residue barrier, never a characteristic-zero
counterexample. CLO Proposition19 and its full Newton proof/extension
were read: they need all roots rational or an unramified field; those
hypotheses are unavailable. No such theorem is applied here.

No full repeated branch, tied-minimum classification, rational lift,
complete mask, new full degree or annual answer has been proved. The
whole audit preserves those limits. Frozen records are checked in the
manifest; only metadata hashing is executed.
