# Frame III: the full binary bridge fails, and the exact next row

18 October2026UTC. **Candidate proof - unverified. Complete research
checkpoint; NO actual frame-III exclusion has been obtained.** Constructor
A, /root/review_2021_reasoning_j15_r2. Requested inherited
gpt-6.1-sol/max; independent effective-setting readback unavailable.
Only official2021 B4(b) is considered. Every new assertion below needs
TWO OTHER initially blind whole audits before promotion. A is excluded.
Root's exploratory note was read and its low-row lead used; root should
also be excluded from review of a dependent submission. B/C would be the
two other reviewers. Root supplied no new inference in the present turn.

The intended bridge was to contradict the surviving actual frame by
combining its exact coefficient gaps with ALL of its extra centers at2.
That bridge fails already as a statement about residue data. Section3
gives one explicit binary divided-coefficient vector satisfying every
required witness row, including D6/D11/D12/D13/D15/D17 at the center,
D7/D14/D16/D18 at r, the double-s derivative row, and the degree20
factor-count identity. The older, shorter binary support did NOT check
all these extra center rows; the present certificate does.

This is a failure certificate for that specific inference. It is neither
an actual rational polynomial satisfying the CA conditions, nor a lift,
nor evidence that such a lift exists. No remaining annual branch is
excluded. A small exact refinement of the next actual row is retained:
H15 must have one of the full monic gcds X^2, X-r or X-s, with a5 either0
or of EXACT19-depth2. This clarifies multiplicity at0 but does not close
the four remaining rational-row equations.

No mathematical executable, CAS, enumeration, routine test, author/source
program or old certificate replay was used. The displayed20 binary rows
are a direct finite hand proof of one counterexample to a proposed
implication, not a scan over masks, valuations or polynomials.

## 0. Actual domain and independently accepted authority

Retain the ENTIRE accepted R18(S),(W), actual m4 and its adjacent-center
domain, followed by its oriented frame III. Write H_k=f^(k)/k! over Q,
and v=v19 with v(19)=1,v(0)=infinity. Thus

    f=X^20-20X^19+sum_(j=2)^18 binom(20,j)a_j X^(20-j),
    a0=1,a1=-1,a19=a20=0,a_j in Z_(19),
    f=X^2(X-r)(X-s)^2(X-1)g,
    rational root VALUES exactly {0,1,r,s},
    ord_0(f)=ord_s(f)=2, r/1 simple,
    v(r)=v(s)=1, s/r=2 mod19, r/19=9 mod19,
    J=max{j:v(a_j)=0}=15,
    H2(r)=H4(r)=H6(r)=0,H8(r)!=0,
    H3(1)=0,H2(1)!=0,H4(1)!=0,
    D11(1)=D12(1)=0,                                (A)

where

    D_j=H_(20-j)(f)/binom(20,j)
       =sum_(k=0)^j binom(j,k)a_k X^(j-k).          (B)

ALL derivatives1,...,19 have an ACTUAL RATIONAL common zero with f.
The common value may vary. This is stronger than a nonconstant rational
polynomial gcd. Other roots are not assumed rational or real. The actual
monic degree14 rational carrier g is irreducible and Eisenstein at19 in
the separately accepted dictionary; it is not a global factor inferred
merely from a local factor. It is not assumed irreducible over Q2.

The accepted full-gcd frame is

    gcd(f,H13)=X-r, gcd(f,H16)=X, gcd(f,H18)=X.       (C)

It implies a2=a4=0 EXACTLY. The R18 unit tuple supplies actual center
rows, rather than only residue zeros:

    D3(1)=D6(1)=D11(1)=D12(1)=D13(1)
          =D15(1)=D17(1)=0.                        (D)

In particular

    a3=2, a6=-35-6a5, v(a5)>=2.                   (E)

The original divided f-center equation, the degree14 carrier and all
other hypotheses remain operative; no quotient is presumed CA.
Accepted R20 excludes frame II and the accepted R19 excludes frame I.
Their exclusions are not new R21 proofs, and this paper addresses ONLY
the remaining frame III. The complete current R18/R20 bodies and their
MD/JSON authorities were read. Older authorship/review roles do not
independently recertify those accepted inputs.

The coordinator exploratory note correctly identifies the exact D5
fork and warns that D15 means degree15, not H15. It is unverified
context, not an accepted theorem. The D5 calculation is rederived here.
Any use of that lead is disclosed rather than presented as an independent
root review opportunity. Its earlier dyadic formulas are not premises.

## 1. Normalize using an ACTUAL minimum-valued rational witness

For this section v2(2)=1, v2(0)=infinity. Choose an actual nonzero
u in{1,r,s} of minimum dyadic valuation M, and put

    F(Z)=u^-20 f(uZ), h=1/u,R=r/u,S=s/u,
    A_j=u^-j a_j, G(Z)=u^-14 g(uZ).                (F)

All0,h,R,S are in Z2; one of the nonzero values is EXACTLY1 and
F(1)=0. For every degree j the actual witness equation is

    A_j=-sum_(k<j)binom(j,k)A_k w_j^(j-k),
    w_j in{0,h,R,S}.                              (G)

Starting with A0=1, (G) proves all A_j integral. It divides by no
binomial coefficient. A19=A20=0 already. Monic division in the exact
factorization proves G integral:

    F=Z^2(Z-R)(Z-S)^2(Z-h)G.                      (H)

This argument uses actual rational witnesses. It cannot be justified
by choosing an arbitrary local unit or a root of a residue polynomial.
Every normalization here is rational and all finite negative/tied
valuations are allowed.

Let b_j=A_j mod2. From a2=a4=0, a3=2, and (E),

    b2=b3=b4=0, b1=hbar, b6=hbar.                 (I)

Because20=16+4, the binary identity
(1+T)^20=(1+T^16)(1+T^4) gives

    Fbar=Z^20+b16 Z^4.

Using F(1)=0 gives b16=1. The ACTUAL H4(r)=0 is D16(R)=0;
its reduction is Rbar^16+b16=0, so Rbar=1. At D18(R)=0,
the only possible nonzero terms modulo2 are Z18+b16 Z2+b18;
thus b18=0. Consequently

    Fbar=Z^4(Z-1)^16, Rbar=1.                    (J)

If hbar=Sbar=0, (H) would contribute Z^5 at0: two from0,
two from S and one from h. That contradicts the exact multiplicity4
in (J). Thus at least one of h,S is a unit. In original coordinates
this gives the exact necessary alternative

    v2(r)=0<=v2(s), OR v2(r)=v2(s)<0.             (K)

In particular r cannot be the unique dyadic outlier and s cannot be
the unique dyadic outlier. This is a minimum/tie restriction, NOT an
ordinary-size/sign bound or a frame exclusion. No quantitative maximum
valuation is introduced. This small consequence alone is not advertised
as a new bridge to the annual problem.

The three normalized residue patterns allowed so far are
(hbar,Rbar,Sbar)=(1,1,0),(1,1,1),(0,1,1). The certificate below uses
the first. We do not silently discard the other two, or classify them.

## 2. A precise false inference

Consider the proposed implication:

    frame-III binary coefficient gaps + ALL nineteen divided-witness
    equations + its seven extra center rows + double-s row + actual
    rational-factor multiplicity counts => contradiction.            (P)

By the binary system in(P) we mean ONLY the reductions specified in
Sections1/3: actual distinct rational values may coalesce modulo2;
nonzero values of derivatives may reduce to0; the carrier is allowed
to split locally. Exact rational values/equations are not asserted to
be recovered from this system. If one adds a true further hypothesis
not implied by these reductions, the present counterexample need not
satisfy it. In particular we do NOT claim consistency of all dyadic
orders, all 19-adic equations simultaneously, or every unspecified
consequence of the characteristic-zero system.

The following explicit coefficient vector disproves(P) with this
precise meaning. It improves the earlier short-support diagnostic by
checking every required center, in particular D6(1)=0.

## 3. A complete hand certificate for the binary system

Set the normalized value residues

    hbar=Rbar=1, Sbar=0,

and set b_j=1 precisely at

    j in{0,1,6,7,12,13,14,15,16,17};             (L)

all other b_j,0<=j<=20, are0. Define, purely over F2,

    E_j(Z)=sum_(k=0)^j binom(j,k)b_k Z^(j-k).

This E_j is the reduced DIVIDED polynomial, not the jth derivative
of Fbar. Division in Q precedes reduction; reducing F first would
lose information when the relevant binomial scalar is even.

The FULL list below follows directly from
(1+T)^j=product_(binary digits e of j)(1+T^(2^e)).
The indicated label is the reduction of the assigned actual witness,
and not a newly constructed rational witness.

|degree j|E_j(Z) over F2|chosen witness label|value|
|---:|---|---|---:|
|1|Z+1|h=1|0|
|2|Z^2|0|0|
|3|Z^3+Z^2|h=1|0|
|4|Z^4|0|0|
|5|Z^5+Z^4|0|0|
|6|Z^6+1|h=1|0|
|7|Z^7+Z^6+Z+1|R=1|0|
|8|Z^8|0|0|
|9|Z^9+Z^8|0|0|
|10|Z^10|0|0|
|11|Z^11+Z^10|h=1|0|
|12|Z^12+1|h=1|0|
|13|Z^13+Z^12+Z+1|h=1|0|
|14|Z^14+Z^8+Z^2+1|R=1|0|
|15|Z^15+Z^14+Z^9+Z^8+Z^3+Z^2+Z+1|h=1|0|
|16|Z^16+1|R=1|0|
|17|Z^17+Z^16+Z+1|h=1|0|
|18|Z^18+Z^2|R=1|0|
|19|Z^19+Z^18+Z^3+Z^2|S=0|0|
|20|Z^20+Z^4|f-root residues0,1|0|

For examples of the actual derivation, binary14 permits k0,2,4,6,8,
10,12,14; intersecting with(L) leaves0,6,12,14. Binary11 permits
k0,1,2,3,8,9,10,11; only0,1 remain. At15 every binomial is odd,
and the first eight supported indices of(L) give exactly its eight
terms. These verify the potentially confusing center/r rows without
borrowing an ordinary-derivative reduction or an executable.

The root polynomial is E20=Z4(Z-1)^16. Reducing(H) gives

    Z^2(Z-1)Z^2(Z-1)*(Z-1)^14
        =Z^4(Z-1)^16.                            (M)

So the monic degree14 carrier reduction is (Z-1)^14. The double-s
row E19(Sbar)=0 is included; Fbar has derivative0, so its ordinary
derivative condition also holds. Fbar(0)=Fbar(1)=0, and its root
multiplicities4/16 allow the exact rational multiplicities to increase
on reduction. The certificate never replaces actual multiplicity2
by an assertion of exact reduced multiplicity2.

All seven center rows in(D) occur at h, and all four r rows with
degrees7,14,16,18 occur at R. The four as-yet-undetermined degrees
5,8,9,10 may all use the label0 in this formal model. The exact low
relations a3=2 and a6=-35-6a5 reduce to b3=0,b6=1, as required.
The original divided f-center identity f(1)/19=0 also reduces to0:
19 is odd, so its coefficient row is the same as E20(1)=0.

Even the exact accepted identity

    0=158289+22968a5-3168a7-1485a8
        -440a9-66a10+a12                         (N)

after a2=a4=0, reduces consistently to1+b8+b12=0, here1+0+1=0.
Identity(N) is not assumed to hold as a Q identity for a polynomial
constructed from the binary vector. This checks its modulo2
consequence and no stronger lift.

The first-break nonvanishing H8(r)!=0 is an exact rational condition.
Its normalized residue in this model is E12(R)=0. This is permitted:
a nonzero rational number may have positive dyadic valuation. There
is NO assertion that H8(r) itself vanishes. Similarly the exact FULL
gcds in(C) are not reconstructed from reduced gcds, which may enlarge.

This proves the narrowly stated failure of(P). It is important that
the vector(L) is not called an actual polynomial satisfying(A)--(E),
and not a formal solution of those equations to every 2-adic order.

## 4. The next exact rational row, including its full gcd

Return to the ACTUAL rational domain(A)--(E), with v=v19. Exact
substitution in(B) gives

    D5(X)=X^5-5X^4+20X^2+a5.

Accepted R18 has D5(1)=16+a5 a19-unit, so the actual H15 witness is
one of0,r,s. Define q(X)=X^3-5X^2+20. At r and s the factor q is
a19-unit, since r,s have positive valuation and20 is a unit. Hence
the complete actual fork is

    a5=0, or a5=-r^2 q(r), or a5=-s^2 q(s).       (O)

The branches are disjoint. Indeed D5(r)-D5(s)=(r-s)B where

    B=20(r+s)-5(r^3+r^2s+rs^2+s^3)
        +(r^4+r^3s+r^2s^2+rs^3+s^4).

Here v(r-s)=1 and v(r+s)=1 because s/r=2mod19. The first term
of B has valuation1, the following groups at least3 and4. Thus

    v(D5(r)-D5(s))=2,                             (Q)

so r and s cannot both be witnesses. Nor can0 coexist with either,
because then r^2 q(r) or s^2 q(s) would be nonzero. In each nonzero
branch v(a5)=2 EXACTLY, not merely >=2. This includes no extra depth
cap: v(r)=v(s)=1 was already the accepted exact frame domain.

For the FULL monic rational gcd, the carrier cannot divide degree5.
If a5=0, D5=X^2 q, q(0)=20, and neither r,s nor1 is a zero of q
in the actual frame. Thus gcd(f,H15)=X^2; its common value0 is
unique but its gcd is DOUBLE. If a5!=0 and its witness w is r or s,

    D5'(w)=5D4(w),
    D4(w)=w^4-4w^3+8w,
    v(D4(w))=1,

so that witness is simple in D5. Even if w=s is double in f, the
gcd has multiplicity1. The exact result is therefore

    gcd_monic(f,H15) in{X^2,X-r,X-s},             (R)

with exactly the branch choices(O). Nonzero rational scalar factors
from H15/binom(20,5) do not affect this gcd. We do not call all
three gcds linear or ignore the double-origin endpoint.

The exact polynomial identity for the row D7(r)=0 is

    a7=r[245-70r^3+7r^5-r^6+a5(42-21r)].         (S)

It is rederived by substituting a6=-35-6a5 into D7, not by reading
D15 as a degree5 polynomial. Formula(S) and(O) are not themselves
incompatible. No sign or ordinary height can be read from r/19=9.

## 5. What remains and what this checkpoint does not prove

The original actual system has not been replaced by the binary one.
After(A)--(E), the four rows still requiring actual noncenter values
are precisely

    D5(w5)=D8(w8)=D9(w9)=D10(w10)=0,
    each w_j in{0,r,s}.                           (T)

The center values at these degrees are19-units, so1 cannot witness
them; the choice need not be the same in different rows. Degree5 is
now the disjoint exact fork(O). ALL original root equations, including
f(s)=f'(s)=0 and f(r)=f(1)=0, still have to hold simultaneously.
The fixed rows at r and1 and the exact coefficient normalization
also remain. The binary certificate proves neither their solvability
nor their insolubility over Q or Q2.

One possible real next bridge is to derive an exact incompatibility
between(O), the other three equations(T), and the original double-s
equations, without imposing a convenience choice for w8,w9,w10.
A separate dyadic route would need an additional quantitative equation
or nonzero leading valuation beyond this residue model. For example,
in residue case hbar=Rbar=1,Sbar=0, (H),(J) give Gbar=(Z-1)^14
and the exact coefficient identity

    190 A18=R h S^2 G(0),
    v2(A18)=2v2(S)-1.                            (U)

Here S is nonzero/nonunit, R,h,G(0) units. The odd value on the
right is compatible with b18=0; the frame-II contradiction required
b18=1 and is unavailable. Thus(U) is not silently turned into a
contradiction. In the other residue cases G(0) need not be a unit.

The coefficient gap a4=0 does not imply H4(r)=H16(r)=0: H16's
actual witness is0. The published common-root prohibition for4/16
therefore does not remove frame III. All-real-root arguments, a
local-factor-to-rational-factor inference, a Q19-root-to-rational-root
inference, or an unproved quotient-CA property also do not close it.

The primary-source context and exact read limits are in the source
packet. In particular the known p5 bad-prime mechanism is retained;
the old2011 degree20 claim is not revived. No new theorem is imported
from a search-result abstract or uninspected universal-proof preprint.
The limited new formal obstruction and exact gcd refinement remain
unverified submissions. No actual frameIII, m3, other m4/EC/J15,
degree20 or annual conclusion is claimed.
