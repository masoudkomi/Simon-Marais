# Fresh initially blind WHOLE R4 audit R1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; independently verified effective settings
unavailable. This is a nonconstructor whole review recommendation,
not coordinator promotion.

**Recommendation:** no substantive defect found in E1, E2 and V1–V4
in their stated partial scopes. I independently reconstructed the whole
argument, including the expansion language/radix normalization, both
prime valuations, every finite shadow continuation and the inverse-limit
counterexample. No required author repair was identified. The no-ninefold
bridge, positive ordinary infinite A/B lifting and the full contest
question remain unresolved. A second fresh whole audit and coordinator
reconciliation remain required before promotion.

Main:23750 bytes, SHA256
`cf3df09a2b38097bcbbe5c80c332a9bf1787f07a2114bf67b6108651240e2b2a`.
Constructor freeze:3530 bytes, SHA256
`f579d150c8b52450e5c20630fd36621ba8d36c3a6168c23235d352068c413f66`.
I read the complete candidate, worklog, source MD/JSON, failed routes
and all28 obligations. All four exact accepted input bodies and their
three acceptance scope MDs were read completely. The final40-row
per-inference ledger and source/integrity records accompany this report.

## Independence and official boundary

I previously performed the independent whole R1 audit of the accepted
2022 R0–R3 and S1–S2 packet. That old review is not a new theorem premise
or a construction contribution to this R4 packet. I did not construct
E1/E2/V1–V4 or supply the power100 strategy. Root supplied that lead
and the R4 author constructed the new proof; neither is counted as an
independent R4 auditor. No new R4 peer report, findings or later root
inspection was read before this COMPLETE initial freeze. No substantive
finding was sent before it.

The [official2022 paper,p.2 B4(b)](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf)
uses positive ordinary integers, inclusive initial product600, simultaneous
updates from the old pair and an equality time n>=0. The new deductions
concern only a restricted avoiding family or an abstract integer
recurrence. They do not prove preliminary part(a), universal equality or
an official positive counterexample.

I checked the accepted quotient/finite lifting, repaired density,
arithmetic-complexity/attribution and whole R0–R3/S1–S2 expositions.
Their roles are kept separate. Density one never becomes pointwise
termination. Low-complexity exclusions never become restrictions on all
loop words. The old full-controller carry obstructions allow all ten
controls and do not apply to the restricted A/B alphabet by fiat. The
preliminary strip is established attributed context only.

## 1. Exact A/B interface, stopped maps and both controls

At state(d,r)=(1,0), loop A has two zero corrections, while B has
corrections(-1,1), intermediate residue6 and return residue0. Both
intermediate differences remain1. Combining the two quotient equations
gives

    100 X_next=121 X-w,  w in{0,1}.

For A, X divisible by100 makes the first quotient11X/10 divisible
by10, so both controls are0. For B, X=81 mod100 makes the first
control1; (11X-1)/10=9 mod10, giving the required second control9.
Conversely those controls impose the same classes. Thus final block
integrality has lost no intermediate condition.

The stopped X map is floor(121X/100) ONLY on classes0 and81. With
Y=X-1 the exact ceiling correction is21-w, respectively21 or20,
so it is ceil(121Y/100) on classes99 and80. This is a stopped
two-class correspondence, not a formula for the full contest quotient.
Any positive allowed X is at least81; both block and intermediate
quotients increase and stay positive. An infinite such orbit supplies
the official pair(60X+1,60X), safely above the product threshold, with
difference1 at every original time. Exiting this stopped map merely
exits the restricted mechanism; it need not hit contest equality.

## 2. E1: ordinary integrality, every language prefix and one common radix

Fix coprime p>q>=2 and beta=p/q. The finite value convention is
(1/q)sum a_i beta^i with full alphabet0,...,p-1. It differs from
ordinary greedy beta notation.

For a positive integer N, division qN=pN'+a gives
0<=a<p and0<=N'<N, so the modified division terminates. Reading
its digits in reverse order represents N. Every prefix represents an
earlier nonnegative integer. To recover the last digit of any length-m
integer-valued word, multiply the value by q^m and reduce modulo p:

    q^m N=a_0 q^(m-1) mod p,
    hence a_0=qN mod p.

The digit range and coprimality fix a_0 uniquely. The prefix is then
the integer(qN-a_0)/p. Induction gives uniqueness up to leading zeros,
including the empty representation of0. Consequently an integer step
qZ_next=pZ+d with d in the full alphabet appends a legitimate digit
to the canonical representation of Z. This is a proof of EVERY finite
prefix condition, not just convergence of a digit series.

For the ordinary integer recurrence qQ_next=pQ+h with bounded h,
direct telescoping gives

    beta^(-n)Q_n
      =Q_0+sum_(j<n) h_j/(p beta^j).

The limit C exists absolutely. The remaining geometric tail bounds
Q_n-C beta^n uniformly; C>0 therefore implies eventual growth to
positive infinity. C>0 is a real hypothesis and is not inferred from
an inverse-limit controller lift.

For each integer c satisfying

    L+(p-q)c>=0,  U+(p-q)c<=p-1,

the positive eventual translates Z_n=Q_(N+n)-c obey

    qZ_next=pZ+h_(N+n)+(p-q)c.

The sign of the correction and the factor p-q are correct. This finite
set of shifts permits one N for which all these Z_n are positive for
all n>=0. Start each tail with the canonical finite representation of
Q_N-c. Appending every correction is a valid integer step, hence an
admissible word under the actual prefix-language definition.

There are two equivalent direct checks of the common real value.
With the radix after its seed, the c-tail contributes exactly c more
than the h-tail, because

    sum_(n>=0) (p-q)c/(p beta^n)=c.

It cancels the seed's -c. All values are beta^N C.
Alternatively pad all seeds on the left to one common length m.
After n appended digits each finite word has value Q_(N+n)-c.
With the radix before the padded word its value is

    beta^(-m-n)(Q_(N+n)-c) -> beta^(N-m)C.

This independently verifies one COMMON normalization and value for
all shifts, even when canonical seed lengths differ. Leading zeros
preserve the prefix condition. At every common appended position the
two c-tails differ by the nonzero constant(p-q)(c-c'); they cannot
be copies differing only in leading zeros. Thus the asserted expansion
multiplicity is genuine. An empty shift interval makes E1 vacuous;
no unproved digit-admissibility or positivity extension is used.

## 3. E2: nine full-alphabet expansions, eight minimal tails and eight maximal tails

An assumed positive A/B lift has every Q_n>=81. Taking c=1,...,9
is legal already at time0. In the real growth series, a B block at
index j contributes

    -1/(11 beta^(2j))+1/(11 beta^(2j+1))
        =-100^j/121^(j+1).

Thus C=X_0-R with0<=R<=1/21, and C>0. The same formal digit
series evaluated in Z10 is NOT assigned this real value. The narrow
correction range[-1,1] gives exactly the E1 interval1<=c<=9 and
digits h+c in0,...,10. The seed values X_0-c are all positive.
The E1 common padding produces nine distinct root-admissible expansions
of one positive real number, rather than nine separately rescaled numbers.

The minimum/maximum indexing can be checked directly without relying on
an ambiguous branch convention. At an integer node z, a full-alphabet
digit satisfies d=-11z mod10. If10 does not divide z there is exactly
one digit, in1,...,9. If10 divides z the two possibilities are0 and10.
The minimum transition is ceil(11z/10); the maximum is
floor((11z+10)/10). Consequently:

- c=1,...,8 give minimal/ceiling tails, since0<=h+c<=9.
- c=2,...,9 give maximal tails, since1<=h+c<=10.
- c=2,...,8 give seven unary tails: their digits are always1,...,9,
  so every node of these tails has just one full-alphabet successor.

These are assertions about the tails from their positive integer seed
nodes. They do not assert that each finite seed path is itself unary.
The direct adjacent-node identity

    floor((11z+10)/10)+1=ceil(11(z+1)/10)

agrees with the c-indexing. An all-A positive tail would require every
100^m to divide one fixed positive X. Hence B occurs infinitely often;
both h=-1 and h=1 occur infinitely often. In particular c=1 is not
also maximal, c=9 is not also minimal, and the overlap among the nine
constructed tails is exactly the seven stated unary ones. The digit10
on the ninth tail must stay; it is generally a maximal, not a ninth
ceiling, path. The construction proves AT LEAST nine expansions in
total, not exactly nine.

The [original AFS manuscript](https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf),
Proposition37, permits at most11 here by taking integer k=10>9.
Corollary38's at-most-two hypothesis p>=2q-1 fails at11/10.
[AEVv2,Conjecture3.9 and Section3.3](https://arxiv.org/html/2510.11723v2)
retain the stronger multiplicity claim as conjectural. Thus no available
statement inspected here contradicts nine. The proposed no-ninefold
consequence remains expressly conditional and excludes A/B only.

For the FULL signed correction bounds[-10,10], the E1 inequalities
would require c>=10 and c<=0 simultaneously. The interval is empty;
none of this supplies the omitted full-controller bridge.

## 4. V1: both prime valuations and the exact accelerated return

Before the next B from an infinite positive orbit there are k>=0
A steps. Its unit B-state is121^k x/100^k, so the two valuations
of x are BOTH exactly2k. Equality of the valuations and evenness
are necessary at EVERY block time, with k=0 giving two zero valuations.
A unit condition alone or divisibility by a large power of100 alone
would not give this conclusion.

For the exact finite stopping test, set a=nu_2(x),b=nu_5(x) and
s=floor(min(a,b)/2). Before s, both valuations are at least2,
so A is forced and legal. If a,b are unequal or their common value
is odd, at state s at least one valuation is0 or1 and they are not
both zero. This state is neither a multiple of100 nor a unit81,
and no previous state has stopped. Thus s is the FIRST stopping index.
If a=b=2k, after exactly k A steps the state is a unit U; it stops
there unless U=81 mod100. The valuation criterion has not silently
replaced that necessary residue check.

At a B-state U, the next quotient is(121U-1)/100. To reach the next
B after k A steps requires exactly

    nu_2(121U-1)=nu_5(121U-1)=2(k+1),
    U_next=121^k(121U-1)/100^(k+1)=81 mod100.

The exponent is k+1 because it includes the B denominator. Conversely
these exact equalities for positive unit states give an integer after
B with valuations2k, then exactly k integral A steps and a unit81
ready for the next B. Concatenation reconstructs every ordinary
intermediate state and both original controls. Positivity follows from
the B-unit minimum81 and increasing steps. The congruence in the first
valuation equality also forces U=81 mod100. This is a true accelerated
equivalence, not a termination theorem or a descent; each positive step
increases x.

## 5. V2: signed fixed points and exact first/second-B shadow criteria

The equation ceil(121Y/100)=Y is equivalent to
-100/21<Y<=0, giving exactly-4,-3,-2,-1,0. Only-1 belongs to
the allowed classes80,99. It is a genuine signed fixed point, but
X=Y+1=0 and the contest pair(1,0) are inadmissible. No statement
about other negative nonfixed orbits is needed.

For positive K, X_0=100^K gives exactly

    X_j=121^j100^(K-j),  0<=j<=K,

through K legal A steps. At state K,121^K=1+20K mod100, so
B is available iff K=4 mod5. Otherwise state K is the first stop.
In the surviving case r=K+1 is divisible by5 and the post-B state
Z=(121^r-1)/100 has

    a=nu_2(Z)=1+nu_2(r),
    b=nu_5(Z)=-1+nu_5(r).

I reconstructed both all-exponent valuation identities. For an odd
multiplier, a geometric sum preserves the initial2-adic valuation of
121-1. Every further squaring adds one, since the current base is
1 mod8 and its sum with1 has valuation1. This proves3+nu_2(r).
For5, remove the exponent factor coprime to5 by its geometric sum.
Raising a base1 mod5 to the fifth power adds exactly one: its first
binomial term has the unique smallest valuation. This proves1+nu_5(r).
Division by100 subtracts2 at EACH prime. No uninspected LTE theorem
or one-prime estimate is being imported.

If a!=b or the common value is odd, V1 gives the first stop at
K+1+floor(min(a,b)/2). Otherwise a=b=2ell, necessarily ell>=1,
which is equivalent to

    r=R_ell u,  gcd(u,10)=1,
    R_ell=2^(2ell-1)5^(2ell+1)=(5/2)100^ell.

There are exactly ell A steps after the first B. The next unit is
U_2=121^ell(121^r-1)/100^(ell+1), at time K+1+ell.

For the stated second-B congruence put M=100^(ell+1). In the
binomial expansion of(1+120)^r, the first divided term is3u.
The second is180u(r-1), congruent to20u modulo100 because250
divides r. For EVERY term j>=3 the expression

    3u*120^(j-1)(r-1)...(r-j+1)/j!

has2-adic valuation at least3(j-1)-nu_2(j!)>=2(j-1)>=4.
Its5-adic valuation is at least(j-1)-nu_5(j!)>=2. The latter
follows from nu_5(j!)<j/4, including j=3,4; integer-valued
valuations make the strict real bound sufficient. The original divided
binomial term has denominator only at2 and5, so these bounds establish
integrality and divisibility by100 after division, not just a formal
congruence of nonintegers. The finite zero terms cause no exception.

It follows that(121^r-1)/M=23u mod100. Since121^ell=21^ell
=1+20ell mod100 and23^(-1)=87 mod100, the condition U_2=81
is exactly u=47+60ell mod100. A balanced unit with another residue
stops; matching valuations alone are insufficient.

For every even positive K satisfying the first-B condition, r is odd,
so a=1 and the first post-B state already stops. Thus the two stated
even-K escape times are exact. The symbolic witnesses also match the
formula: K249 has ell1,u1 and U_2=83 mod100, stopping at251;
K1749 has ell1,u7 and U_2=81 mod100, permitting its second B.
These are hand congruences, not orbit scans or infinite-survival evidence.

## 6. V3: exact two-prime isometry, residue bijections and finite shadow universality

For ell>=1 set R=R_ell,M=100^(ell+1),Lambda=121^R and
Phi_ell(u)=121^ell(Lambda^u-1)/M for ordinary integers u>=0.
The preceding identities give

    nu_2(Lambda-1)=nu_5(Lambda-1)=2ell+2.

Thus these are ordinary nonnegative integers, including Phi(0)=0.
For u!=v, factor Lambda^u-Lambda^v by Lambda^min(u,v), a unit
at both primes. For d=abs(u-v)>0 the same geometric/squaring/fifth-power
arguments give

    nu_p(Lambda^d-1)=2ell+2+nu_p(d),  p=2,5.

Here Lambda=1 mod16 supplies the required2-adic squaring condition.
Multiplication by121^ell is a unit; division by M subtracts exactly
2ell+2 at EACH prime. Therefore

    nu_2(Phi(u)-Phi(v))=nu_2(u-v),
    nu_5(Phi(u)-Phi(v))=nu_5(u-v).

The sign of the difference is immaterial. This is stronger than simply
preserving a largest common power of100.

For every N>=1, congruence modulo100^N is equivalent to both
valuations being at least2N. The forward equality makes Phi well-defined
on residue classes; the reverse makes it injective there. Since the
finite domain and codomain have the same cardinality, it is bijective.
Reduction between successive moduli commutes with evaluation on ordinary
representatives, so the bijections and their unique inverses are compatible.
The moduli100^N are cofinal among10^n, giving a bijection of Z10.
This is a map of the inverse-limit space; it does not make division by
100 a field operation, assert a ring automorphism or assert ordinary
integer surjectivity. Setting v=0 in the two valuation identities also
proves the exact unit-preservation property.

For every ordinary positive unit u, K=R_ell u-1 is positive. The
already verified finite shadow formula, including the exact valuations,
gives A^K B A^ell and next unit Phi_ell(u). It does not merely
give a congruence shadow at that time.

I also reconstructed the finite-loop residue statement independently:
for a prescribed word w_0,...,w_(N-1), the one initial class is

    x_w=sum_(j<N) w_j100^j/121^(j+1) mod100^N.

The denominators121 are units for this FINITE congruence. Reducing
to each prefix depth proves all intermediate integer quotients; the
class criteria in section1 then prove both controls in every block.
For a word beginning B this class is81 mod100. Its Phi preimage
class is a unit and has arbitrarily large ordinary positive representatives
u. Every such representative gives the actual shadow exponent K above
and realizes the complete finite concatenation A^K B A^ell w.
In particular words with arbitrarily many B's occur after the first B.
This proves more than a long initial A delay, without a numerical search.

For an infinite prescribed word, the unique pulled-back inverse classes
give one element of Z10. They need not contain one ordinary positive
integer. In addition K varies with representative and depth in the
finite construction. Thus no ordinary positive infinite exponent or
nonterminating orbit follows. The quantifiers are finite throughout V3.

## 7. V4 and the complete remaining domain gap

For ell1, R250,M10000. Phi_1(0)=0 and for every u>=1 monotonicity
gives

    Phi_1(u)>=121(121^250-1)/10000>81.

The final inequality already holds with exponent2, since
121(121^2-1)=1771440>810000. Thus the ordinary positive target81
has NO ordinary nonnegative integer preimage. Nevertheless every finite
modulus has one unique preimage class, a unit class, with arbitrarily
large positive representatives. Compatibility gives one inverse-limit
preimage u_*. If u_* were a nonnegative ordinary integer, the fixed
ordinary integer Phi_1(u_*)-81 would be divisible by all100^N and
would be zero, contradicting the displayed inequality. This proves
exactly the asserted domain obstruction. It does not rely on an
unstated p-adic exponential theorem.

The target81 itself makes one B update to98 and then stops. It is
not an infinite avoiding example. The signed fixed point has X0=0,
also outside the official positive domain. These boundary cases prevent
either counterexample from being misreported as a contest counterexample.

For source scope, the original
[Dubickas–Mossinghoff body,Section1 and Propositions3.1–3.2](https://www.researchgate.net/publication/220576840_Lower_bounds_for_Z-numbers)
uses a nonempty PROPER residue set; its proved singleton case does
not cover{80,99} modulo100. The inspected AEV implications require
unproved normality/residue assertions. No such result resolves the
stopped map here. There is no claim that this bounded source check
proves absence of all stronger literature results or establishes novelty.

I challenged the digit10 endpoint, language admissibility, unequal seed
lengths, real/Z10 sign distinction, ordinary positivity, both intermediate
controls, both primes and odd/even endpoints, factorial denominators,
stopping-state indexing, arbitrary finite words, cofinal compatibility
and ordinary versus inverse-limit surjectivity. No substantive gap or
counterexample to the stated deductions was found.

All new claims remain partial and candidate-unverified until coordinator
promotion. No scan, CAS, mathematical program, author rerun, new native
paper download, contact, charge, spawning, shared edit or Git action was
used. The only non-administrative Python operation read named pages of
the existing AFS cache. All37 older own packets and the separate GK
telemetry addendum are preserved. The new freeze checks bytes and
serializes only this assigned review prefix.
