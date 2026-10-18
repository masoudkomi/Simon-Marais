# A first-derivative parity row excludes actual frame II

2026-10-18 UTC. **Candidate proof - unverified.** Constructor A,
`/root/review_2021_reasoning_j15_r2`. Requested inherited
`gpt-6.1-sol/max`; independent effective-setting readback unavailable.
Root supplied a generic remaining-frame assignment and NO NEW proof
inference. TWO OTHER initially blind ENTIRE WHOLE audits and coordinator
reconciliation are required. This packet concerns official2021 B4(b)
only. It does not settle degree20 or the annual problem.

The proposed result excludes the ENTIRE actual frame II orbit from
accepted R18B, including its other double-origin representative. Its
proof is a rational four-witness obstruction, with no bound on any
valuation. An actual double root supplies a zero of the first derivative
AFTER division by20 over Q. Keeping this divided equation before
reduction modulo2 closes the dyadic outlier left by the earlier local
analysis. The contradiction is an exact coefficient/product valuation,
not an alleged incompatibility between ramification at2 and19.

The proof below is self-contained except for applying the separately
accepted R18B dictionary to the actual residual branch. It does NOT use
any R19 conclusion or any affected
review. In particular no original-coordinate Eisenstein statement,
unramified-field assumption, all-roots-rational claim, quotient-CA
assertion, sign inference or rational lifting theorem is used.

## 0. Exact proposed statements

Put `H_k(f)=f^(k)/k!` over Q. For a monic degree20 polynomial write

    f(X)=sum_(j=0)^20 binom(20,j)a_j X^(20-j),
    a0=1, a1=-1, a19=a20=0,
    D_j^f(X)=H_(20-j)(f)(X)/binom(20,j)
            =sum_(k=0)^j binom(j,k)a_k X^(j-k).        (0.1)

Every division here takes place over Q, BEFORE reduction at2. In
particular `D19^f=f'/20`, not the derivative of a reduced polynomial.

**R20A, rational four-witness obstruction.** There is no such f in
Q[X] satisfying all the following assumptions:

1. `0,1,r,s` are four DISTINCT rational values; each is a root of f,
   and0 ands have multiplicity at least2. Other roots are unrestricted.
2. For EVERY `1<=k<=19`, an ACTUAL common value of f and H_k(f) can
   be selected from `{0,1,r,s}`. The selected value can depend on k.
3. The following SIX equations hold over Q:

       H18(f)(r)=H4(f)(r)=H2(f)(r)=0,
       H16(f)(s)=0,
       H17(f)(1)=H3(f)(1)=0.                         (0.2)

No hypothesis about a rational factorization of the other fourteen
roots, irreducibility, 19-adic depth, real-rootedness or minimality of
the four-witness cover is imposed. A four-witness COVER is different
from the assertion that f has only four distinct complex roots.

**R20B, actual frame II exclusion.** In the COMPLETE accepted R18B
domain, the frame

    gcd(f,H13)=X, gcd(f,H16)=X-s, gcd(f,H18)=X-r       (II)

is impossible, as is its actual double-origin partner. All hypotheses
of that domain remain: normalized rational degree20, J15, the sole
H3 center, exact four rational root values, double0/s, simple r/1,
the actual degree14 carrier and rational witnesses at EVERY derivative
order, `(S),(W)`, actual m4 and the adjacent-center condition
`D11(1)=D12(1)=0`. R20B excludes this full frame, not merely a
bounded-depth or an integral-at2 specialization. The actual R18B
nu=1 conclusion is available but is not needed in the new dyadic proof.

## 1. Normalize the actual rational witness cover at2

Let v be the usual2-adic valuation on Q, with `v(2)=1` and
`v(0)=+infinity`; put `O=Z_(2)`, whose residue field is F2. Choose

    M=min{v(1),v(r),v(s)},
    u in{1,r,s} with v(u)=M,
    F(Z)=u^(-20)f(uZ), h=1/u, R=r/u, S=s/u,
    A_j=u^(-j)a_j.                                 (1.1)

Here u is an actual NONZERO rational root. Thus `F(1)=0`, whereas
the normalized mean is h, not necessarily1. All the transformed
witness values `0,h,R,S` belong to O. No statement about the
valuations of unselected roots is used to choose u.

By the chain rule over Q,

    D_j^F(Z)=u^(-j)D_j^f(uZ)
            =sum_(k=0)^j binom(j,k)A_k Z^(j-k).       (1.2)

The ACTUAL rational-witness assumption makes EVERY A_j integral in
O. Indeed `A0=1`. For each `1<=j<=18` select the actual transformed
witness `w_j in{0,h,R,S}` of H_(20-j). Then

    A_j=-sum_(k<j) binom(j,k)A_k w_j^(j-k) in O       (1.3)

by induction. Finally `A19=A20=0`. In particular all coefficients of
F and all D_j^F belong to O. This argument uses the original
common-root equations, not their residues or a gcd with nonrational
roots. It is the familiar divided-coefficient induction, included
in full here to handle rational witnesses whose original valuations
can be negative.

The actual root multiplicities give

    F(Z)=Z^2(Z-R)(Z-S)^2(Z-h)G(Z),                   (1.4)

with G monic of degree14 over Q. The displayed degree6 divisor is
monic in O[Z]. Long division by a monic polynomial works in O[Z];
its remainder is zero because (1.4) already holds over Q. Hence
`G in O[Z]`. This does not use Hensel factorization or a global
irreducibility assertion. Also `A1=-h` exactly.

## 2. All binary coefficient rows used in the proof

Write `b_j=bar(A_j)`, `rho=bar(R)`, `sigma=bar(S)`,
`eta=bar(h)` in F2. These are DYADIC residue symbols; rho is NOT
the accepted R18 notation for r/19 modulo19.

In F2[T], `1+T^(2^e)=(1+T)^(2^e)`. Multiplying the indicated
factors gives the COMPLETE odd binomial supports required below:

|degree j|identity for (1+T)^j|odd coefficient indices|
|---:|---|---|
|2|1+T^2|0,2|
|3|(1+T)(1+T^2)|0,1,2,3|
|4|1+T^4|0,4|
|16|1+T^16|0,16|
|17|(1+T)(1+T^16)|0,1,16,17|
|18|(1+T^2)(1+T^16)|0,2,16,18|
|19|(1+T)(1+T^2)(1+T^16)|0,1,2,3,16,17,18,19|
|20|(1+T^4)(1+T^16)|0,4,16,20|

These identities prove all parity supports by hand. No table
generator, finite mask scan or computed binomial certificate is used.
Since `A20=0`,

    bar(F)=Z^20+b4 Z^16+b16 Z^4.                    (2.1)

Evaluating at the actual normalized root1 yields

    b4+b16=1.                                      (2.2)

The six actual equations(0.2) become

    D2^F(R)=D16^F(R)=D18^F(R)=0,
    D4^F(S)=0, D3^F(h)=D17^F(h)=0.                 (2.3)

The first four reduced rows give, successively,

    b2=rho, b16=rho, b4=sigma, b18=rho.             (2.4)

For example the last row is
`rho + b2*rho + b16*rho + b18=0`; the three terms rho
sum to rho in F2. We have used only that every element of F2 is
idempotent. From(2.2),(2.4),

    rho+sigma=1.                                   (2.5)

Since `b1=eta`, evaluation of the degree3 and degree17 rows at h
then gives

    0=eta+eta+b2*eta+b3,
    0=eta+eta+b16*eta+b17,
    b3=b17=rho*eta.                                (2.6)

The two center equations in(2.6) are ACTUAL H17 and H3 equations.
They are not consequences of the statement that a residue vanishes.

## 3. The actual double root supplies the missing first-derivative row

Because s is an actual double root of f, S is an actual double root
of F. Consequently, over Q,

    D19^F(S)=F'(S)/20=0.                            (3.1)

The coefficient integrality in Section1 was proved WITHOUT dividing
an equation in F2 by20. It therefore makes reduction of the already
defined polynomial D19^F legitimate. Reducing F' itself would lose
this information, since its corresponding scalar20 is even.

If `sigma=1`, all positive powers of S reduce to1. The degree19
support in Section2, `A19=0`, and(2.4),(2.6) give

    0=bar(D19^F(S))
      =1+eta+rho+rho*eta+rho+rho*eta+rho
      =1+eta+rho.                                  (3.2)

In particular `rho=0,sigma=1` forces `eta=1`. This is the new
global common-root compatibility row closing the outlier scale.
It uses the original first derivative at the actual double root,
not a local quadratic's ramification or a merely formal local lift.

## 4. Case rho=1, sigma=0: the coefficient at the other double root

By(2.1),(2.4),

    bar(F)=Z^20+Z^4=Z^4(Z-1)^16.                    (4.1)

In(1.4), the factors Z^2 and `(Z-S)^2` already contribute Z^4
to the reduction. If eta were0, `(Z-h)` would contribute another
Z, contradicting the EXACT order4 at0 in(4.1). Thus `eta=1`.
The reduced degree6 factor in(1.4) is `Z^4(Z-1)^2`, so cancellation
in F2[Z] gives

    bar(G)=(Z-1)^14.                                (4.2)

Hence `R,h,G(0)` are units and S is a nonzero nonunit. The EXACT
coefficient of Z^2 in(1.4) is

    190 A18 = R*h*S^2*G(0).                         (4.3)

The signs of `(-R)(-S)^2(-h)` give the positive sign shown.
The left side has valuation EXACTLY1: `190=2*95` and `b18=1`.
The right side has valuation `2v(S)>=2`. This is impossible.
There is no numerical upper bound or ordinary-sign hypothesis here.

## 5. Case rho=0, sigma=1: a second derivative at the actual double root

Equation(3.2) forces eta1. Now

    bar(F)=Z^20+Z^16=Z^16(Z-1)^4,
    bar[Z^2(Z-R)(Z-S)^2(Z-h)]=Z^3(Z-1)^3,
    bar(G)=Z^13(Z-1).                               (5.1)

Thus S and `S-R` are units, while both `S-h` and G(S) lie in2O.
From the EXACT factorization(1.4), the Hasse second derivative at
the actual double root is

    H2(F)(S)=S^2*(S-R)*(S-h)*G(S).                   (5.2)

To justify(5.2) directly, write `F=(Z-S)^2 B`. In the coefficient
of T^2 of `F(S+T)=T^2 B(S+T)`, only B(S) remains. This works
even if S has multiplicity larger than2. The product in(5.2) lies
in4O, with zero factors allowed.

On the other hand the degree18 row, at the unit S and with
`b2=b16=b18=0`, is

    bar(D18^F(S))=1.                                (5.3)

Since `H2(F)=binom(20,18)D18^F=190 D18^F`, equation(5.3)
gives `v(H2(F)(S))=1`, contradicting(5.2). If the product in(5.2)
were zero, it would still contradict this exact nonzero valuation.

The cases(4),(5) exhaust(2.5). This proves the proposed R20A.

## 6. Application to the ACTUAL R18 frame II, in both root frames

We use the complete accepted R18B body and its current MD/JSON
authority, not an R19 theorem. Its exact domain has

    f=X^2(X-r)(X-s)^2(X-1)g in Q[X],
    a1=-1, a19=a20=0,
    {rational root VALUES of f}={0,1,r,s},
    H2(f)(r)=H4(f)(r)=0.                            (6.1)

The official rational-witness condition at EVERY derivative order,
together with the exact root-value set, gives the cover in R20A.
Its mean1 is an actual root; the coefficients are exactly those of
(0.1). The accepted five-center tuple has a3 a19-adic UNIT and
accepted R18 Section3 equation(8) supplies the ACTUAL equation
`D3^f(1)=0`, equivalently `H17(f)(1)=0`. Stipulated `(S)` supplies
`H3(f)(1)=0`. These are rational equations, not just field equations.

Frame II supplies `H16(f)(s)=0` and `H18(f)(r)=0` by its actual
full gcds. The first gcd `gcd(f,H13)=X` is part of the frame's
definition but is not needed in R20A. Thus every hypothesis of R20A
is supplied, and the entire actual frame II is excluded.

Accepted R18 Section7 pairs the two representatives by the actual
invertible rational transformation

    f_new(Y)=(1-s)^(-20)f(s+(1-s)Y),
    r_new=(r-s)/(1-s), s_new=-s/(1-s).               (6.2)

It fixes the actual mean1 and interchanges the two double origins.
Every derivative zero and the rational cover are transported by
the chain rule and nonzero rational scalar factors. It is enough
to choose the representative whose R18 full gcds have pattern(II)
and apply R20A to that ACTUAL polynomial. The new proof does not
require `1-s` to be a2-adic unit: Section1 renormalizes at2 again.
Consequently the entire double-origin orbit of frame II, not only
one preferred origin or one dyadic normalization, is excluded.

No rational-root conclusion is drawn from an irreducible local
factor or a Q19 zero. The actual global carrier in(6.1) remains
the accepted one, but its irreducibility and Eisenstein property
are unnecessary in the new obstruction. This proves R20B in its
exact proposed scope.

## 7. Published method, overlap and roles

The divided-coefficient induction and valuation normalization are
established methods; see [Castryck--Laterveer--Ounaies, Section3,
Proposition15](https://arxiv.org/pdf/1208.5404). They are reproved
here over the rational localization. The new proposed step is the
particular six actual rows together with the divided first derivative
and the two exact double-root identities, not the valuation method.

[Massri, Proposition7.7 and Remark7.8](https://arxiv.org/pdf/1806.09561)
already give the degree20 H4/H16 common-value prohibition. Here their
values r ands are distinct. That prohibition is not presented as new
or used to claim an exclusion of frame II. No priority or exhaustive
literature-overlap claim is made. The source record gives operative
passages actually read and distinguishes source discovery from proof.

The constructor authored older accepted R5/R8/R18 and other local
inputs, reviewed other packets, and authored the separate R19 packet.
These are disclosed roles, NOT independent self-recertifications.
R20 uses R18B as separately accepted input; its new four-witness
obstruction is subject to TWO OTHER whole audits. Neither root nor
another agent supplied a new R20 proof step. No new R19 affected
review or corresponding queued2019 AT review material was accessed.

## 8. Precise remaining gap and failed extension to frame III

The new statement does not exclude frame III. Its actual zero
witnesses give `a2=a4=0`; they do NOT give the frame-II row D2(r)=0.
At the level of the binary rows in this proof they instead allow

    rho=1, sigma=0, eta=1,
    b0=b1=b16=b17=1, all other b_j=0.                (8.1)

For this FORMAL parity sequence, the degree2 and4 rows vanish at0,
the degree3 and17 rows vanish at h1, the degree16 and18 rows vanish
at R1, and the degree19 row vanishes at S0. More generally, a row
with b_j0 has0 as a root; the remaining indices1,16,17 have1 as
a root. The original reduced polynomial is `Z^4(Z-1)^16` and is
consistent with the reduced degree6 root divisor. This is only a
binary consistency example: it is neither an actual rational CA
polynomial nor an unrestricted lift. It shows exactly why replacing
the missing D2(r) equation by D2(0) does not extend the contradiction.

Frame I's published overlap and the separately reported R19 acceptance
are not newly certified here. R19 was pending when this work began;
root reported its acceptance while the R20 packet was being completed.
No new R19 proof/review was read or made a premise. Actual frame III, other essential-center
branches including EC8/different EC9-H10, m3, other J15 domains and
the full degree20/annual question remain outside R20B. A genuinely
additional rational equation or a finer exact product obstruction
is needed to close those cases; reduction parity by itself does not.

All new mathematics is hand reasoning. No executable mathematical
program, CAS, scan, valuation cap, author/source-program replay,
separately billed API, access bypass or charge supplied the proof.
Administrative code binds bytes and parent records only. Full source,
failure, obligation/check and immutable provenance records accompany
this candidate. Internal review is not external validation.
