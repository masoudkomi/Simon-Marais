# Initial blind whole-argument audit: J15, double zero

2026-10-16 UTC. Reviewer `review_2021_reasoning_j15_r1`. Requested setting:
`gpt-6.1-sol`, reasoning `max`; verified effective-setting readback is
unavailable. This is an independent adversarial review of the complete
mathematical argument, not a construction contribution. No other J15 review
conclusion was consulted before this report, its issue log, and its source
audit were frozen. No construction file was edited. The coordinator alone
may promote a result after both required reviews.

**Recommendation:** accept precisely D1–D5 and the asserted properties of
the low-order family, conditional on the explicitly accepted inputs. I find
no unresolved substantive objection in the frozen version. This does not
exclude the complete J15 case, any complete center mask, or degree 20.

## Frozen object, scope, and review method

The audited candidate is
`notes/reasoning-J15-double-root-candidate-v1.md`, SHA-256
`e3da7a889e5937722546dab2596fdb2140597066584487ce15fb8c4e4fd8bbff`.
Its manifest and intuition transcript were read and their stated hashes
checked. The candidate still bore **candidate proof - unverified** during
this audit. The analytic proof does not depend on the 324-pair intuition
enumeration, and I did not rerun that enumeration or any mask/CAS search.

I reconstructed every new inference in sections 1–6, with particular
attention to tied valuations, repeated slots, Hasse differentiation under
rescaling, the field of a factorization, and the corrected sign. The
following are accepted prior inputs rather than fresh re-audits of their
finite certificates:

- `rational-witness-p-plus-one-reviewed-v1.2.md`: rational affine
  normalization, integral normalized coefficients, simple center 1, and
  strictly positive valuations for all other nonzero roots.
- `padic-rational-newton-reviewed-v1.1.md` and its frozen body: the
  fourteen-slot edge and the width-one derivative lemma with lower
  exponent less than 19.
- `coordinator-three-rational-witnesses-reviewed-v1.1.md`, T1 and T3:
  at least four distinct rational recycled values, and zero multiplicity
  2 or 3 when J15. Only multiplicity 2 is investigated here.

The official cached paper, page 2, explicitly requires a rational common
root separately for every derivative order. It does not require the full
root set to be rational. The target remains B4(b); no argument for the
preliminary part was developed. Primary-source locators, hashes, and the
bounded source audit are in `reasoning-J15-review-1-sources.json`.

All valuations below are 19-adic, with v(19)=1. Put O=Z_19. A zero
coefficient has infinite valuation. Root-slot counts include multiplicity;
the covering count uses distinct rational values.

## 1. Independent reconstruction of D1 and the coefficient estimates

The accepted Newton edge is from (5,1) to (19,0), with every other
coefficient point strictly above its extended supporting line. It gives
exactly fourteen roots of valuation 1/14. The normalized simple center
accounts for the one root of valuation zero. With the zero root counted
twice, exactly three nonzero slots remain, all of valuation greater than
1/14. None of the fourteen fractional-valuation slots is rational, since
the valuation of a nonzero rational is an integer. T1 therefore forces at
least two distinct rational values among those three remaining slots.

Choose two such values u,v and remove one copy of each. The absolute
Galois group of Q_19 preserves the root multiset and valuations, fixes u
and v, and therefore preserves the one-slot remainder in this small
cluster. That remainder w is fixed. In characteristic zero an algebraic
element fixed by the absolute Galois group lies in Q_19. If the slot is
another copy of u or v, it is already fixed. Thus all three slots are in
Q_19 and have positive integral valuations. This establishes local
splitting only; the argument supplies no global rationality for w.

After removing X^2, X-1 and the three small factors, the monic quotient g
has precisely the fourteen valuation-1/14 roots. Each nonleading
coefficient of g is an elementary symmetric sum of products having
strictly positive valuation. The coefficient lies in Q_19; its valuation
is therefore at least 1 (or it is zero). Its constant coefficient is one
product of all fourteen roots and has valuation exactly 1. Hence g is
Eisenstein over O. No quotient over Q is needed or claimed.

For B=(X-1)g=sum b_i X^i this gives

    v(b_0)=1;  b_1,...,b_13 in 19 O;
    b_14=-1 mod19;  b_15=1.

Writing s_1=u+v+w, s_2=uv+uw+vw, s_3=uvw, direct multiplication of

    X^2(X^3-s_1 X^2+s_2 X-s_3) B(X)

gives exactly

    c_2=-b_0 s_3,
    c_3=b_0 s_2-b_1 s_3,
    c_4=-b_0 s_1+b_1 s_2-b_2 s_3,
    c_5=b_0-b_1 s_1+b_2 s_2-b_3 s_3,
    c_6=b_1-b_2 s_1+b_3 s_2-b_4 s_3.

For nu=min v(u_i)>=1, all terms after b_0 in c_5 have valuation at
least 1+nu, so v(c_5)=1. The other identities give

    v(c_2)>=1+3nu, v(c_3)>=1+2nu, v(c_4)>=1+nu.

For every j=2,...,18, binom(20,j) has valuation exactly 1: its numerator
contains the sole factor 19 and j! has none. Dividing gives the stated
bounds on a_18,a_17,a_16. Moreover c_5/b_0=1 mod19 and
c_6/b_0=b_1/b_0 mod19. Since a_15 is a unit,

    b_1/b_0=c_6/c_5=beta_14 a_14/(beta_15 a_15) mod19.

All fractions here are integral; this is an equality of residues, not an
equality of valuations when a numerator residue vanishes. The minus sign
in c_2 and plus sign of the leading c_6 term are the ones for three small
factors and a double zero.

## 2. Rescaling audit and exhaustive valuation partitions for D2

The reduction of the whole polynomial at the first scale can be justified
directly, without an implicit division by a nonunit in the residue field.
For alpha=19^n, n>=1,

    B(alpha T)/b_0 in O[T],  B(alpha T)/b_0 = 1 mod19.

Indeed the coefficients through degree 13 beyond the constant have
valuation at least in, while the degree-14 and degree-15 coefficients
have valuation at least 14n-1 and 15n-1. At an inner scale, an already
removed outer factor contributes

    (alpha T-u)/(-u)=1-(alpha/u)T =1 mod19

because v(alpha)>v(u). The scalar used to divide f(alpha T) can lie in
Q_19; the resulting polynomial is integral. For any such scalar lambda,

    H_k(lambda^(-1) f(alpha T))(t)
      =lambda^(-1) alpha^k H_k(f)(alpha t).

Hasse derivatives use integral binomial coefficients and commute with
reduction. Consequently a nonzero reduced value at a reduced root rules
out an exact common root. A zero reduced value is used only as a
necessary condition. Rational roots outside {0,1,u,v,w} cannot exist.

There are exactly three unequal valuation partitions up to permutation:
one smallest and two equal deeper values; three strictly increasing
values; or two equal smallest values and one deeper value. The argument
handles each, including coincident residues.

**One smallest, two equal deeper.** At the first scale the reduction is
F=T^4(T-U). Its H_4 is 5T-U, whose values at 0,U are -U,4U, both
nonzero. This excludes every noncenter root as an H_4 witness. The unique
outer root lies on a width-one edge with exponents 4,5, so it is excluded
as an H_2 or H_3 witness as well. The lemma applies because 4<19.

At the inner scale the reduction is G=T^2(T-V)(T-W). Its H_2 values
at 0,V,W are respectively VW, V(3V-2W), W(3W-2V). A noncenter H_2
witness therefore needs W/V in {3/2,2/3}={11,7}. Its H_3 values at
these points are -(V+W),3V-W,3W-V, giving the necessary set
{-1,3,1/3}={18,3,13}. These sets are disjoint in F_19. Hence at least
one of H_2,H_3 also uses the center. The calculation does not divide by
V-W and covers V=W.

**Three strictly increasing valuations.** The preceding H_4 exclusion
still applies. At the intermediate scale the reduction is T^3(T-V),
and H_3 takes the nonzero values -V and 3V at 0,V. The outer root is
already excluded from H_3, so H_3 uses the center. For H_2 the three
nonzero roots lie on width-one edges with endpoint exponents (4,5),
(3,4), and (2,3). Their lower exponents are all less than 19, so all
three are excluded by the width-one lemma. Zero is excluded because
c_2 is nonzero. Thus H_2 uses the center too. All three center equations
are forced.

**Two equal smallest valuations, one deeper.** At the outer scale the
reduction is F=T^3(T-U)(T-V). The deepest root is on the width-one
edge (2,3) and cannot witness H_2 or H_3. Zero cannot witness H_2.
It cannot witness H_3 either: in c_3, the term b_0 uv has valuation
1+2nu, whereas every other contribution has strictly greater valuation.
At U,V the reduced H_2 values are U^2(4U-3V),V^2(4V-3U), and the
H_3 values are 3U(2U-V),3V(2V-U). H_4 takes 4U-V,4V-U there and
-(U+V) at zero or the deeper root. Thus the three respective necessary
ratio sets are

    H_2: {4/3,3/4}={14,15},
    H_3: {2,1/2}={2,10},
    H_4: {-1,4,1/4}={18,4,5}.

They are pairwise disjoint. At most one of the derivatives can have a
noncenter witness, forcing at least two center equations. This remains
valid when U=V; in that case the displayed nonzero evaluations simply
give further exclusions. These cases prove all of D2.

## 3. Reconstruction of the sole-H3 residue collision, D3

If H_2(1),H_4(1) are nonzero but H_3(1)=0, D2 forces equal small
valuations nu>=1. Divide by 19^nu. The integral scaled reduction is

    F=T^2(T-U)(T-V)(T-W)=T^5-sT^4+tT^3-zT^2,
    z=UVW nonzero.

All three nonzero residues lie in F_19 by D1. At a cubic root R,
the cubic equation eliminates z and gives

    H_2(F)(R)=R(9R^2-5sR+2t),
    H_3(F)(R)=10R^2-4sR+t,
    H_4(F)(R)=5R-s.

H_2(F)(0)=-z excludes zero. If the noncenter H_4 witness reduces to
zero, then s=0. For a nonzero H_2 witness R, t=-9R^2/2. The other
two residues have sum -R and product -7R^2/2, so their discriminant is
15R^2. Since 15 is a nonsquare modulo 19 and R is nonzero, this
contradicts splitting over F_19, also when the other two slots coincide.

Otherwise let S be the nonzero H_4 witness residue. Then s=5S; the
other two slots A,B have A+B=4S. If H_2 uses one of those slots,
substitution into its equation gives

    7A^2-17SA+8S^2=0.

Its discriminant is 65S^2=8S^2, again nonsquare. This calculation
does not cancel A-S or A-B and therefore covers every repeated-slot
possibility. H_2 must use S. Its equation yields t=8S^2, whence
AB=4S^2 and A+B=4S. Thus A=B=2S. The nonzero square residues of
F_19 are {1,4,9,16,6,17,11,7,5}; neither 8 nor 15 occurs.

There is exactly one slot of residue S. The exact rational H_2 and
H_4 witnesses must both be the value r occupying that slot. Thus they
are the same actual rational root, not just roots with equal residue.
The other two actual roots may differ or coincide; D1 places them in
Q_19 and does not place them in Q. For completeness, H_3(F) takes
8S^2,-2S^2,8S^2 at 0,S,2S. No noncenter actual H_3 witness is being
silently used. This proves D3.

## 4. Exact discriminant and its valuation, D4

Write the other two roots as a,b and set A=a/r, B=b/r. They reduce to
2. In this paragraph B_res denotes the degree-15 residual polynomial
from D1, not the root ratio. Since v(B_res(r))=1, put

    C(T)=B_res(rT)/B_res(r),
    x=c_1=r H_1(B_res)(r)/B_res(r),
    y=c_2=r^2 H_2(B_res)(r)/B_res(r),
    z=c_3=r^3 H_3(B_res)(r)/B_res(r).

For k=1,2,3, H_k(B_res)(r) lies in 19 O. Terms with original
exponent at most 13 have a coefficient divisible by 19; the degree-14
and degree-15 terms contain respectively at least 14-k and 15-k powers
of r. These are at least 11 and 12. Integer binomial coefficients do
not lower their valuations. Hence

    x in 19^nu O, y in 19^(2nu) O, z in 19^(3nu) O.

Set P=T^2(T-A)(T-B)=T^4-sT^3+tT^2 and L=P(1). The factorization

    f(rT)=r^5 B_res(r)(T-1)P(T)C(T)

converts the exact H_2 and H_4 equations at r into H_1(PC)(1)=0 and
H_3(PC)(1)=0. Product differentiation introduces no factorial errors
with Hasse derivatives. Explicitly,

    P'(1)=2-s+2L, H_2(P)(1)=5-2s+L, H_3(P)(1)=4-s.

The first equation gives s=2+(2+x)L. Substituting it in the second
gives

    D L=2+x,  D=2+4x+2x^2+xy-z.

D=2 mod19 is a unit. Therefore

    s=2+(2+x)^2/D,
    t=1+(2+x)(3+x)/D,
    (A-B)^2=(2+x)[x^3-2x^2-4x(1+y)+4z]/D^2.       (R1)

I reconstructed the last identity by writing its numerator as
(2+x)[(2+x)^3-4D]. This verifies its exact signs independently, with
no cancellation of A-B. It includes a=b. Since x=O(19^nu),
y=O(19^(2nu)), z=O(19^(3nu)), (R1) gives

    (A-B)^2=-2x mod 19^(2nu).

Furthermore H_1(B_res)(r)/B_res(r)=b_1/b_0 mod19: all higher-degree
derivative terms vanish after dividing by b_0 and reducing, and
B_res(r)/b_0=1 mod19. The section-1 residue identity therefore shows
that when a_14 is a unit, v(x)=nu. In (R1), -4x is the unique term of
valuation nu in the bracket. Its prefactor and denominator are units,
so v((A-B)^2)=nu and this square is nonzero. A nonzero square in
Q_19 has even valuation, proving nu even.

Let R=r/19^nu mod19. Dividing by 19^nu and reducing gives

    (A-B)^2/19^nu
      =-2R beta_14 a_14/(beta_15 a_15) mod19.

For even nu, the left side is the square of a 19-adic unit, and the
right side is nonzero. The sign is consequently **-2**, as printed in
the frozen candidate. If a_14 is nonunit, x may have greater valuation
or vanish, and terms in (R1) can compete; no parity conclusion follows
from this argument. This limitation is respected by D4.

## 5. Canonical masks and the center constant, D5

Use the normalized degree-j derivative

    D_j=H_(20-j)(f)/binom(20,j)
       =sum_(k=0)^j binom(j,k)a_k X^(j-k).

The displayed integral polynomial is formed over Q before any reduction;
one never divides by the zero residue of binom(20,j). Every exact
rational witness w_j obeys

    a_j=-sum_(k<j) binom(j,k)a_k w_j^(j-k).

Choose center 1 whenever available. In D3, every selected noncenter
witness is 0 or a rational small root of valuation nu, hence belongs
to 19^nu O. A possible non-Q third small root is never selected. Replace
these noncenter choices by 0 and keep all center choices at 1, defining
a_j^0 recursively. These constants are integers: there are only integer
binomial coefficients and the initial values 1,-1.

Induction proves a_j=a_j^0 mod 19^nu. At a noncenter step every term
contains a positive power of w_j, so both the actual coefficient residue
and the replaced coefficient are zero. At a center step it is an integral
linear combination of earlier coefficients, preserving the induction.
The exact center root equation is

    f(1)/19=-1+sum_(j=2)^18 beta_j a_j=0.

Thus q_0=-1+sum beta_j a_j^0 is divisible by 19^nu. If q_0 is
nonzero, nu<=v(q_0). Also a_14 and a_14^0 have the same residue.
For a canonical mask with only H_3 among H_2,H_3,H_4 at the center,
v(q_0)=1 and unit a_14^0, an actual double-zero realization would
have nu=1 by this bound and nu even by D4, a contradiction. If q_0=0
there is no finite bound. A separate multiplicity-three argument is
needed before a complete mask can be removed. D5 makes this distinction.

## 6. Independent audit of the explicit rational low-order family

Take any nonzero r in 19 Z_(19), so d=1-r is a unit. All displayed
expressions are rational and d is nonzero. In particular

    S=X^2(X-r)(X-2r)^2,
    P=S[(X-r)^14(X-L)+19d^13(X-r)^2],
    Q=S[1-(X-r)^2/d^2],  L=20-19r.

Modulo 19, Q=X^5-X^7 and H_3(Q)(1)=10-35=-25, a unit. The
high-degree piece has the coefficientwise expansion

    S(X)(X-r)^14(X-L)
      =X^20-20X^19+380rX^18+r^2 times an integral polynomial.

The first-order term can be seen from
X^2(X-r)^15(X-2r)^2=X^19-19rX^18+O(r^2); multiplication by
X-20+19r cancels the X^19 term of first order in r. Since 19 divides
380 and r belongs to 19 Z_(19), the high-degree expression differs
coefficientwise from its r=0 value by 19^2 times an integral polynomial.
After dividing the added low-degree piece by 19 its reduction is X^7.
Therefore, for k=2,3,4, H_k(P)(1)/19 has the same residue as the
r=0 expression P_0=X^20-20X^19+19X^7. In particular the numerator
defining K=-H_3(P)(1)/(19H_3(Q)(1)) is divisible by 19, and

    H_3(P_0)(1)/19=-925,
    H_3(Q_0)(1)=-25,
    K=-37=1 mod19.

Hence K lies in Z_(19) and is a unit. In

    B_r=(X-r)^14(X-L)+19[K+(d^13-K/d^2)(X-r)^2],

the constant term is 19K modulo 19^2, so has valuation 1.
Direct substitution gives B_r(1)=-19d^15+19d^15=0. Its reduction
is X^14(X-1); consequently g_r=B_r/(X-1) is monic integral, reduces
to X^14, and has constant coefficient of valuation 1. It is Eisenstein
over Z_(19), hence over O. The center 1 is simple, since g_r has no
unit root and S(1) is a unit.

The coefficient of X^19 in f_r=S B_r is
-(5r+14r+L)=-20. Reduction gives X^19(X-1), so all middle ordinary
coefficients are divisible by 19 and all normalized a_j are integral.
The three small factors and the section-1 identities give c_2 nonzero,
v(c_5)=1, v(c_2)>=1+3v(r), v(c_3)>=1+2v(r), and
v(c_4)>=1+v(r). Thus the zero multiplicity is exactly 2 and J=15.

At X=r the first and third Hasse derivatives of B_r vanish, since its
expansion in Y=X-r contains only degrees 0,2,14,15. The other factor
X^2(X-2r)^2 equals (Y^2-r^2)^2 and is even in Y. The coefficients
of Y^2 and Y^4 in f_r(r+Y) therefore vanish, proving the exact
H_2(f_r)(r)=H_4(f_r)(r)=0 equations. The definition of K gives
H_3(f_r)(1)=0 exactly.

The center nonvanishing values can be checked by four small binomial
identities, without expanding the family symbolically:

    H_2(P_0)(1)/19=-149,  H_2(Q_0)(1)=-11,
    H_4(P_0)(1)/19=-3790, H_4(Q_0)(1)=-30.

With K=-37 modulo 19 these yield 258=11 and -2680=-1 modulo 19
for H_2(f_r)(1)/19 and H_4(f_r)(1)/19. Both derivatives therefore
fail at the center. The other two small roots are exactly 2r,2r.
Also B_r'(r)=0 implies b_1/b_0=0 mod19, so the section-1 identity
forces a_14 nonunit, as claimed. In (R1) one has x=z=0 and A=B=2,
giving zero discriminant consistently. Every denominator used above is
a 19-adic unit. The family does not verify the other derivative
conditions and supplies no Casas–Alvero counterexample.

## Adversarial outcome and limits

The issue log records the field, rescaling, cluster ties, coincident
slots, sign, denominator, and family checks separately. Each was resolved
by the reconstruction above; no substantive repair is requested. There
was no large computation, enumeration, native CAS operation, or pending
child process in this review. Source extraction and SHA checks were
short read-only commands. The proof itself is analytic.

No conclusion is drawn for sole-H_2 or sole-H_4 center patterns, the
nonunit-a_14 branch beyond its exact necessary square condition,
two/three low center equations, the separate triple-zero candidate, or
J<=14. Earlier J16 exclusions and the number of remaining masks were
not used as proof inputs. The result is a partial conditional restriction
under the rational-witness contest hypothesis. Its attribution and
absence of a novelty claim are appropriate.

The parent supplied authoritative weekly telemetry at 2026-10-16
21:35 UTC: 16% total used, weekly reset 1792745187, cutoff 90% total.
This review did not reinterpret it as a percentage of the remaining
allowance or use separately billed APIs. No Git operation, shared status
edit, source edit, or peer J15 review read was performed.
