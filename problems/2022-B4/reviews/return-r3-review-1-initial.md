# 2022 B4(b) reasoning return: independent whole initial audit R1

2026-10-17 UTC. Reviewer: `review_2021_reasoning_j15_r2`.
Requested model/reasoning: gpt-6.1-sol / max. No independent effective-setting
readback is available. This is a review recommendation, not promotion.

## Identity, independence, and verdict

I reconstructed the whole original candidate and its whole supplement before
writing this report. I did not construct either packet, contribute its carry
argument, read another new return-r3 review or receive its findings. Accepted
older dependency expositions and acceptance statements were read; raw new peer
reviews were not. No mathematical program, orbit search, enumeration, CAS or
transducer implementation is a premise of this review.

The audited original is
`notes/reasoning-return-r3-candidate-v1.md`, SHA-256
`eb3d176680116595015069507f3904a0d048e44d3c2cde06965647010b82764e`.
The audited supplement is
`notes/reasoning-return-r3-supplement-candidate-v1.md`, SHA-256
`a0512f751dc5c648043025948a841fa4ecffb280785641c5e85f9fae5c99bca3`.
Their logs, source packet and both freeze manifests were inspected. The
accompanying input-validation record gives the byte checks.

**Recommendation:** R0, R1, R2, R3, S1 and S2 withstand this independent whole
audit in their stated, restricted scopes. I found no substantive mathematical
defect or required author repair. The issue ledger separates all the principal
inferences and records two nonblocking interpretation cautions. This review
does not accept universal equality, termination of the stopped scalar instance,
or the existence of an admissible infinite integer avoiding orbit.

## 1. Official domain and exact dependency interface

The official Paper B, page 2, supplies simultaneous updates on positive
integers, the inclusive condition a_0 b_0 >= 600, and equality at some
nonnegative time as the question in B4(b). The candidate matches that domain.
I did not investigate or reconstruct the preliminary trapping result.

The accepted quotient identities use b=60Q+r, 0<=r<60, d=a-b and

    c=3 floor((r+d)/30),
    d'=d+2 floor(r/20)-c,
    r'=(6e+r+c) mod60,
    h=(r+c-r')/6,
    10Q'=11Q+h,                 h=-e mod10.

The full controller is the accepted closed strip -13<=d<=23, with all ten
controls e=0,...,9. Its outgoing residues are exactly the ten representatives
of r+c modulo 6. In particular it remains a ten-control system even when an
individual path has already met equality. The new no-go results expressly
use this full system, not the equality-avoiding sublanguage.

The signed bound needed later follows without enumeration. In the strip,
-13<=r+d<=82, so c is one of -3,0,3,6. Thus
-62<=r+c-r'<=65; divisibility by 6 implies -10<=h<=10.

The accepted finite lifting bijection is the only passage from a finite
control prefix to ordinary integer starts: a length-L prefix gives one
congruence class Q_0 modulo 10^L and arbitrarily large positive representatives.
An infinite word does not acquire an ordinary integer representative by this
argument. Its inverse-limit lift belongs to the ring Z10. Multiplication by
10, or by 100, is injective in that ring although these numbers are not units:
10x=0 implies x=0 modulo 10^N for every N by considering the equation modulo
10^(N+1). The analogous argument works for all powers.

I also checked the fixed-denominator interface. If the lift starts at a
diagonal rational u/v with gcd(v,10)=1, iteration writes
10^n vQ_n=A_n with A_n an ordinary integer. Since Q_n is in Z10, A_n is
divisible by 10^n as an ordinary integer. Injectivity then shows vQ_n is an
ordinary integer. There is no division in a purported field Z10 here.

## 2. R0: real growth, including the product boundary

Let u=a mod30 and v=b mod20, with nonnegative residues. Then

    a'=a+(b-v)/10,       b'=b+(a-u)/10.

Adding gives exactly s'=beta s-(u+v)/10 with beta=11/10 and
0<=u+v<=48. Solving this recurrence over the reals gives

    C=s_0-sum_(j>=0) (u_j+v_j)/(11 beta^j),
    s_n=C beta^n+theta_n,
    theta_n=sum_(j>=0) (u_(n+j)+v_(n+j))/(11 beta^j).

The geometric sum of the coefficient 1/(11 beta^j) is 1. Consequently
0<=theta_n<=48 and C>=s_0-48. A positive integer pair with sum <=48
has product <=576, so the official hypothesis forces sum >=49 and C>=1.
In particular s_n>=beta^n. The example (24,25) is at product 600 and
sum 49; no strict-product or large-quotient hypothesis was inserted.

This calculation concerns actual coordinates and a real convergent series.
It does not assign a real value to the inverse-limit correction identity.
The shadow used in R3 is a different real solution with its growing
coefficient set to zero. The distinction is maintained throughout.

## 3. R1: both directions of the exact restricted scalar reduction

At d=1 and r=0 or 6, the displayed controller formulas give c=0 and d'=1.
At r=0, control 0 returns residue 0 with h=0; repeating gives A. Control
1 moves to residue 6 with h=-1; there control 9 returns to residue 0
with h=1, giving B. Thus both loops avoid equality at each intermediate
time, and arbitrary concatenations are abstract avoiding paths.

Write X_j=Q_(2j), and w_j=0 or 1 for A or B. The combined equation is

    100 X_(j+1)=121 X_j-w_j.

The sign of the B correction is -11+10=-1, which I checked directly.
Backward iteration in Z10 gives the unique lift

    X_0=sum_(j>=0) w_j 100^j/121^(j+1).

For integral X, A requires X=0 modulo 100. B requires 21X=1 modulo
100, whose solution is X=81 modulo 100 because 21*81=1701. These
block conditions are equivalent to the two individual control conditions:

* X=100t gives first quotient 110t, hence controls 0 then 0.
* X=81+100t gives first quotient 89+110t, hence controls 1 then 9.

Thus neither an intermediate integrality constraint nor a residue-state
condition disappears in the two-step equation. Conversely, the two controls
imply these very classes, so the test is exact.

For a positive integral infinite lift, X_0 is at least 81. The block map
has X_(j+1)>=1.21X_j-.01>X_j. The individual quotients increase too:
an A step has increment Q/10>0; the first B step has increment
(Q-1)/10>0 at Q>=81, and its second step has increment (Q+1)/10>0.

Set Y=X-1. On the allowed classes,

    100Y'=121Y+21-w.

The correction is 21 on Y=99 modulo 100 and 20 on Y=80 modulo 100.
Each is in [0,99] and has the required divisibility, hence is the unique
ceiling correction. Therefore Y'=ceil(121Y/100) on precisely these two
classes. A positive A/B ordinary integer lift produces a positive Y
orbit that stays in {80,99} modulo 100.

In the reverse direction, let a positive integer Y have such an infinite
ceiling orbit. The correction on its current residue determines w. Then
X=Y+1 obeys the exact block equation and the congruences above recover
the two intermediate quotient steps and residues. The initial contest pair
is (60X+1,60X), already with X>=81. It is positive, satisfies the official
product bound, and has difference 1 at every time. This proves both
directions of the existence equivalence, with no independent lifting
assumption omitted in the reverse direction.

The stopped-map termination formulation has the same quantifiers: a start
outside the two classes stops immediately; a start that never stops gives
exactly the positive ordinary lift just constructed. The context restricts
the phrase “all A/B integer lifts” to these positive lifts. The all-zero
word does have the zero quotient lift, which is outside the official domain.
Leaving the two classes is only leaving this family, not meeting equality.

The published scalar proper-subset termination question is relevant context,
not a theorem establishing this two-residue case. I checked the original
singleton result and the later conditional normality implication separately.

## 4. R2: nonzero divisibility and the rich irrational word

Assume w is not eventually zero and its Z10 lift is rational with fixed
denominator v. If X_j=0, the block equation and X_(j+1) in Z10 force
w_j=0, since 1 is not divisible by 100. Injectivity of multiplication by
100 then gives X_(j+1)=0. Iterating would make the entire remaining
word zero. Consequently vX_j is a nonzero ordinary integer for every j.

Read the rational recurrence also in the reals and put gamma=121/100.
The estimate |X_(j+1)|<=gamma|X_j|+1/100 solves to

    |X_j|<=gamma^j(|X_0|+1/21)-1/21<=A gamma^j,
    A=|X_0|+1/21.

For M zeros starting at j, one has
100^M X_(j+M)=121^M X_j. Clearing v and using coprimality forces
100^M to divide the nonzero integer vX_j. Hence

    100^M<=v|X_j|<=vA gamma^j,
    M<=alpha j+log(vA)/log100,
    alpha=log(gamma)/log100=log(11/10)/log10<1.

This is valid for negative or bounded rational real solutions as well as
positive ones; positivity was used only for the sharper ordinary-integer
estimate X_j<=gamma^j X_0. An eventually zero word is correctly excluded
from the nonzero-divisibility formulation. Such a tail can have quotient
zero and invalidates the nonzero integer step, but cannot be an official
positive A/B integer orbit by the growth already proved.

The word construction is exact and needs no executed list of binary words.
At stage k, the concatenation W_k contains each binary k-word as one of
its aligned components. Letting N_k be the prefix length after W_k,
then appending N_k zeros produces a zero factor starting at zero-based
position N_k with length N_k. Later stages contain ones, so the resulting
word is not eventually zero, and N_k tends to infinity. Rationality would
force (1-alpha)N_k<=constant for all k, a contradiction.

For every k, the word contains all 2^k possible k-factors, so its binary
factor complexity is exactly 2^k. Distinct aligned coded k-factors give
distinct correction factors of length 2k because the two blocks (0,0)
and (-1,1) are distinct and have equal length. Thus P_h(2k)>=2^k.
For odd lengths, factor complexity of an infinite one-sided word is
nondecreasing: each occurring factor has some right extension, and distinct
factors have distinct extended prefixes. It follows that
P_h(L)>=2^floor(L/2), and in particular its lower complexity slope is
infinite. This justifies the comparison with any fixed finite linear
asymptotic lower-slope test. It does not furnish a rational lift or an
ordinary integer orbit. Every finite prefix still has positive integer
lifts by the accepted finite bijection.

The divisibility-versus-real-growth method is properly attributed to
Dubickas. The run-position argument and word construction are proved
here in the actual signed-loop setting rather than obtained by importing
a scalar ceiling theorem without its hypotheses.

## 5. R3: shadow algebra and exact finite averaging

For an arbitrary full-controller infinite word, define the separate real
shadow

    Qhat_n=-sum_(j>=0) h_(n+j)/(11 beta^j).

Absolute convergence and -10<=h<=10 give |Qhat_n|<=10. Direct index
shifting gives 10Qhat_(n+1)=11Qhat_n+h_n. Define
bhat=60Qhat+r, ahat=bhat+d. These are real auxiliary quantities;
flooring their quotients is not being asserted.

In fact the controller algebra gives exactly

    bhat'=66Qhat+r+c,
    ahat'=66Qhat+r+d+2 floor(r/20).

Set u=r+d-30 floor((r+d)/30), v=r-20 floor(r/20). These are bounded
integer symbols even if ahat or bhat is negative. The last two displayed
equations imply

    shat'=beta shat-(u+v)/10,       shat=ahat+bhat.

The shadow is bounded because Qhat, d and r are bounded. Backward
iteration therefore uniquely gives
shat_n=sum_(j>=0)(u_(n+j)+v_(n+j))/(11 beta^j), in [0,48]. At initial
state (d,r)=(1,0), shat_0=120Qhat_0+1, so

    -1/120<=Qhat_0<=47/120.

No equality between the real and Z10 sums is used to obtain this interval.

Now let k_0=m be a fixed integer and k_n depend only on the first n
controls. If delta=h+10k'-11k belongs to {0,...,9}, then for a fixed
length-n prefix and its fixed k_n,

    delta_n=-e_n-k_n modulo 10.

The ten next controls consequently give the ten canonical digits once
each. In the uniform finite average over all 10^N prefixes, the mean
of delta_n is exactly 9/2 at every n<N. Extending each word by zero
controls merely defines its Qhat; it does not change its first N
controller states or carries. There is no distribution assertion about
one integer orbit and no independence premise between carries and shadows.

The recurrence for Zhat=Qhat+k is
Zhat'=beta Zhat+delta/10. Its finite solution gives, upon averaging,

    Avg k_N=beta^N[m+9/2+Avg Qhat_0]-9/2-Avg Qhat_N.

I verified the plus sign before 9/2 inside the brackets and the minus
sign outside. The average initial shadow belongs to the same interval.
For m<=-5 the bracket is <=-13/120; for m>=-4 it is >=59/120.
Its absolute value is thus >=13/120 for every integer m. Finally
|9/2+Avg Qhat_N|<=29/2, proving

    max_(length-N controls)|k_N|>=(13/120)beta^N-29/2.

Taking N large rules out a uniform bound over all prefixes for a fixed
initial carry. A finite causal offset transducer is a special case. If
the claim were proposed only for all positive integer starts with this
same causal rule and initial carry, finite lifting still realizes every
finite obstruction. This is a worst-input statement; it does not force
carry divergence on every actual orbit or on every avoiding language.

## 6. S1: the restricted constant offsets really do work

The positive A/B lift has every quotient >=81, including its intermediate
steps, as checked in Section 3. For c=1,...,8, the translated quotient
Z^(c)=Q-c is therefore positive and obeys

    10Z'^(c)=11Z^(c)+h+c.

Here h is in {-1,0,1}, so h+c is in [0,9]. Integrality makes it the
unique ceiling correction, and hence each Z^(c) is a positive orbit of
ceil(11Z/10). They remain consecutive since they are constant translates
of the same quotient at every time. For c=2,...,8 the correction is
never zero. Since its residue is -Z modulo 10, each of these seven
orbits would avoid multiples of 10 forever.

Thus the stated weak scalar residue-escape assertion would exclude the
A/B family, if independently proved. It is kept conditional. This valid
constant offset on a restricted language also checks that R3 and S2
cannot be applied after silently discarding the full-input hypothesis.

## 7. S2: arbitrary future-aware bounded initialization

The carry continuation is forced. Given integer k and h,
0<=h+10k'-11k<=9 is equivalent to

    k'=ceil((11k-h)/10).

This equivalence holds for negative values too. Once k_0 is fixed, no
memory, future knowledge, or later discretionary choice can alter the
sequence. Initial selection is the only freedom within this exact
unit-offset/canonical-digit model.

For any starting state let t=2r+d. The shadow calculation above yields
Qhat_0 in [-t/120,(48-t)/120]. If 11<=t<=57, then for any integer m,

    m>=-4:  m+9/2+Avg Qhat_0>=1/2-57/120=1/40,
    m<=-5:  m+9/2+Avg Qhat_0<=-1/2+37/120=-23/120.

The same exact averaging identity consequently proves

    max_(length-N controls)|k_N|>=beta^N/40-29/2,

uniformly for every such state and every initial integer carry.

From any current strip state the next difference d' is fixed. All ten
controls permit selecting the unique next residue in {12,...,17}
with the required class modulo 6. It follows that
11<=2r'+d'<=57, using the inclusive strip endpoints -13 and 23.
No accessibility enumeration is needed.

Fix K>=0 integral and choose N with beta^N/40-29/2>K. For any current
state and any carry that has not yet violated the bound, use that one
transition. It either violates the bound immediately or reaches a suitable
state where some length-N continuation has terminal |k|>K. Thus a word
of length at most N+1 eliminates any specified remaining initial carry.
The word can be chosen using that carry in an existence proof; it need
not be the same escape word for every carry.

To obtain one common prefix, begin with the finite set of 2K+1 possible
initial carries. Choose a surviving m, append an escape word for its
current carry and controller state, and mark all initial values that
have violated the bound anywhere so far. At least the chosen m is
removed. A previously removed value need not stay outside the interval;
one historical violation already prevents uniform boundedness. After
at most 2K+1 rounds there is a single prefix of length at most
(2K+1)(N+1) that defeats every m in [-K,K]. This checks the potentially
delicate interchange of “for each m an escape word” and “one word for
all m”: the finite concatenation argument supplies it explicitly.

Lift that one prefix to an arbitrarily large positive Q_0>K. It yields
an official start (60Q_0+1,60Q_0). Every bounded initializer, including
one that inspects this entire integer or its actual infinite future,
must select an m in [-K,K], already eliminated on this same actual
prefix. The continuation is forced, so future awareness cannot evade it.
The original positive-coordinate update also makes b_n nondecreasing;
therefore Q_n=floor(b_n/60)>=Q_0. A hypothetically bounded shifted
state Q_n+k_n would remain positive, as asserted in the supplement.

This proves the stated impossibility for a single uniform bound on the
entire positive-integer family. It does not exclude a bound depending on
the initial integer, unbounded offsets, a scaling of Q, a larger output
alphabet, or an avoiding restricted language. The obstructing finite
prefix may meet equality, which the candidate expressly permits.

## 8. Primary sources and remaining boundaries

I directly read the cited primary theorem/proof locations and record their
scope in the separate source checks. The scalar normality and residue-escape
assertions remain conjectural in the inspected source; no absence-from-the-
literature claim is needed. The published right transducer has its own final
acceptance condition and the larger output alphabet, so it is not contradicted
by either no-go theorem. The supplement correctly refuses the two-expansion
theorem at ratios 11/10 and 121/100.

The mathematical deductions proved here leave the intended gap intact:
nonperiodic, high-complexity ordinary integer avoiding lifts have not been
ruled out; the stopped 121/100 instance has not been resolved. There is
no promotion of a conditional bridge into a proof of universal equality.

## 9. Process and freeze

Only `reviews/return-r3-review-1-*` files were written for this task.
No candidate, shared file, source binary, accepted dependency or older
review was changed. No Git operation, spawning, external contact, paid
access or separately billed API was used. Primary sources were read via
their public pages/PDFs; existing ignored cached sources were only hashed.
Administrative Python was used solely for file sizes, hashing and manifest
validation, never as a mathematical premise.

Authoritative weekly telemetry during the audit: 23% total used of a
10080-minute window, reset 1792745187. The cutoff is 90% total, with
integration reserve. This report, issue ledger, source checks, input
validation and manifest are frozen before any substantive finding or
acceptance recommendation is transmitted to the coordinator. The other
fresh auditor's conclusions were not read before that freeze.
