# Blind whole audit 1: rational-lift complexity obstruction

2026-10-16 UTC. Reviewer: `review_2017_coarsening_r1`, now independently
assigned to 2022 B4(b). I did not construct this candidate. Requested
launch model/reasoning: `gpt-6.1-sol`, `max`; effective-setting readback
is unavailable. This initial whole report, its issue ledger and source
record were completed before reading any peer arithmetic-complexity
review or its conclusions. Only the coordinator may promote a result.

Candidate SHA-256:
`e9c24e96982d1d2a74aa97cb5fd045a3319f37c69316fbada884eeec0a0412d3`.
Attribution supplement SHA-256:
`b2ddb5337b0e669bab594916ed0e590a358feb812b0d8c338948372422786aed`.
Both independently rehashed bytes match the supplied constructor manifest.

## Verdict and exact scope

I recommend accepting the packaged candidate and attribution supplement
as **partial results**, subject to the coordinator's second-review gate.
The rational-lift dichotomy, its application to admissible integer starts,
and the explicit mechanical avoiding family with nonrational Z_10 lifts
all reconstruct. I found no substantive mathematical objection requiring
author repair. The ring cancellation and factor-length details below
make the delicate steps explicit.

The original statement was checked against official Paper B, page 2,
including a visual rendering of that complete page. The actual domain is
positive integer a_0,b_0 with inclusive product threshold a_0 b_0>=600;
both updates use the old pair. Equality at time 0 counts. Only B4(b) was
investigated. The established eventual strip is accepted as attributed
context, without reproducing or researching preliminary part (a).

This does not prove that every official start reaches equality. It gives
a necessary complexity condition on all actual integer tails and excludes
one explicit low-complexity family from ordinary integer lifting. General
nonperiodic avoiding paths of high complexity remain possible in the
abstract controller. No novelty, real transcendence, or two-dimensional
density conclusion is accepted.

## 1. Accepted inputs and controller arithmetic

I read the normalized official statement, `reviewed-partials-v1.md`,
`reviewed-density-v3.md`, and the coordinator acceptance record. Their
hashes match the candidate manifest. The only mathematical input needed
from the accepted partials here is P1's exact quotient/controller and
finite lifting, together with the attributed eventual strip context.
Neither density theorem supplies a premise in the complexity proof.

Write b=60Q+r, 0<=r<60, d=a-b. Direct substitution into the simultaneous
map gives

    b'=66Q+r+c(d,r),
    d'=d+2 floor(r/20)-c(d,r),
    c(d,r)=3 floor((r+d)/30).

The difference is independent of the control e=Q mod 10. The new least
nonnegative residue is `r'=(6e+r+c) mod 60`. If
`r'=6e+r+c-60k`, then

    h=(r+c-r')/6=10k-e,
    10Q'=11Q+h,
    h=-e mod 10.

This verifies the sign and the denominator 6. For d in [-13,23] and
r in [0,59], `-13<=r+d<=82`, so c is one of -3,0,3,6. Hence
`-62<=r+c-r'<=65`. This integer is divisible by 6, giving -10<=h<=10.
Negative floor arguments and both strip endpoints are included. The
controller theorem is stated only for paths that stay in its finite
state set; the explicit loops below do so.

## 2. Inverse-limit lift and a denominator proof without field division

The ring Z_10 is the inverse limit of Z/(10^N), not a field. Integers
11 and v with gcd(v,10)=1 are units. Also multiplication by 10^n is
injective: if 10^n x=0, reduction modulo 10^(N+n) makes x zero modulo
10^N for every N.

For bounded h, the series

    Q_n=-sum_(j>=0) h_(n+j) 10^j/11^(j+1)

converges in this ring, since its tail from j=N vanishes modulo 10^N.
Shifting the series gives `10Q_(n+1)=11Q_n+h_n`; reducing modulo 10
then gives `Q_n=e_n mod 10`. Thus it realizes the supplied path.
If two lifts realize it, iteration makes their initial difference a
multiple of 10^N for every N, because 11 is a unit. Their difference
is zero. Its finite reductions therefore agree with accepted P1.

For a rational lift Q_0=u/v, take v>0, gcd(u,v)=1 and gcd(v,10)=1.
A convenient fully internal denominator proof is as follows. Iteration
gives

    10^n vQ_n = A_n,

where A_n is an ordinary integer. Reduction modulo 10^n implies
`10^n | A_n` as an ordinary integer. Write A_n=10^n z_n and use the
injectivity above to get `vQ_n=z_n in Z`. This proves the candidate's
fixed-denominator assertion without treating Z_10 as a field or
illegally inverting 2 or 5. In particular every Q_n is the same diagonal
rational z_n/v when subsequently read in the real numbers.

This also explains the intended meaning of nonrationality later: absence
of a diagonal rational u/v with denominator prime to 10. No claim about
separate algebraicity of the two components Z_2 and Z_5 is needed.

## 3. Rational dichotomy: bounded deterministic exception and real growth

Set beta=11/10. The real series

    C=Q_0+sum_(j>=0) h_j 10^j/11^(j+1)

has the candidate's positive sign. It is not set equal to zero merely
because the corresponding Z_10 series represents -Q_0. Real iteration
of the recurrence gives

    Q_n=C beta^n-T_n,
    T_n=sum_(j>=0) h_(n+j)10^j/11^(j+1),
    |T_n|<=10.

The last bound is the geometric sum `(10/11)/(1-10/11)=10`.

If C=0, the Q_n lie in the finite set `[-10,10] intersect (1/v)Z`.
There are finitely many (d,r) as well. The FULL state (Q,d,r) has one
successor: the rational residue Q mod 10 is well-defined because v is a
unit, and determines e; the controller determines d',r',h; the quotient
recurrence determines Q'. Therefore a repeated full state repeats all
future states. Finite-state repetition proves ultimate periodicity.
Repeating only Q would not be sufficient, but the proof correctly keeps
the controller state too.

If C!=0, then

    Q_(n+1)-Q_n=C(beta-1)beta^n-(T_(n+1)-T_n).

The final difference has absolute value at most 20. The first term
eventually dominates it with fixed sign. Thus Q_n is eventually strictly
monotone, also when C<0. Choose n_0 after this occurs. Independently,
`|Q_(n+1)|<=beta|Q_n|+1`, and summation gives exactly

    |Q_n|<=beta^n(|Q_0|+10)-10<=A beta^n,
    A=|Q_0|+10.

All constants here are attached to the one rational lift; no uniformity
over arbitrary paths is required.

## 4. Matching factors, nonzero divisibility, and the exact slope

Suppose two length-L h-factors start at n_0<=n<m and are equal. Then

    10^L Q_(n+L)=11^L Q_n+H,
    10^L Q_(m+L)=11^L Q_m+H,
    H=sum_(j=0)^(L-1) 11^(L-1-j)10^j h_(n+j).

There is no need for the blocks to be disjoint. Subtraction and
multiplication by v, using vQ_j in Z and gcd(10,11)=1, yield

    10^L | v(Q_m-Q_n).

Strict monotonicity beyond n_0 makes this integer NONZERO, so its
absolute value is at least 10^L. At the same time it is at most
`2vA beta^m`. Hence the correction factors at all starts from n_0
through M are pairwise different whenever `2vA beta^M<10^L`.

Let `kappa=log(10)/log(beta)` and

    M_L=ceil(kappa L-log(2vA)/log(beta))-1.

For every real t, ceil(t)-1<t, even when t is integral. The strict
growth inequality therefore holds at M_L. For all sufficiently large L,
M_L>=n_0, and there are

    M_L-n_0+1=kappa L-O(1)

distinct factors. Division by L gives the asserted liminf at least
kappa. No recurrence or uniform frequency of the word was assumed.
The proof needs all factors occurring in the one-sided word, which is
exactly the definition supplied in the candidate.

## 5. Official positive starts and the state-word inequality

For an actual orbit, its ordinary nonnegative integer quotients realize
the path and therefore equal its unique Z_10 lift. If they were bounded
in the strip, b=60Q+r and a=b+d would be bounded. Both are nondecreasing
positive integer sequences, hence eventually constant. Simultaneous
zero increments require b<=19 and a<=29, giving ab<=551. But positivity
made the product nondecreasing from an initial value at least 600.
This contradiction excludes the bounded case, including Q_0=0 and
starts at the inclusive threshold 600. No illicit initial assumption
Q_0>0 is used.

Thus every admissible actual tail in the attributed strip has correction
complexity liminf slope at least kappa. Equality is not an absorbing
state in the recurrence; the argument remains valid after an equality
has occurred, since the orbit is simply continued by its defining map.
Adding a finite initial prefix cannot remove factors of the tail.

The state word S=(d,r) satisfies the same lower slope. In detail a
length-(L+1) S-factor gives all h-values on its L successive transitions,
because `h=(r+c(d,r)-r')/6`. Hence

    P_S(L+1)>=P_h(L).

Reindexing K=L+1 and using `(K-1)/K->1` proves the candidate's state
bound. No equality of correction, control, and state complexities is
assumed.

## 6. Avoiding loops and mechanical-word audit

At (d,r)=(1,0), c=0 and D=1. Control 0 keeps r=0 and gives h=0.
Control 1 gives r'=6 and h=-1. At (1,6), c=0 and D=1, and control 9
returns r'=0 with h=1. These are precisely the two length-two loops

    A: e=(0,0), r=(0,0,0), h=(0,0),
    B: e=(1,9), r=(0,6,0), h=(-1,1).

Any concatenation stays at difference 1, so it avoids equality in the
abstract controller.

For irrational 0<alpha<1, the lower mechanical word
`w_j=floor((j+1)alpha)-floor(j alpha)` is binary. Its first N letters
sum to floor(N alpha), so its limiting average is irrational alpha.
An ultimately periodic binary sequence has rational limiting average;
therefore w is not ultimately periodic.

Its length-k factor depends on x={n alpha} through the k floor
differences. The only breakpoints are the k+1 distinct circle points
`-j alpha mod 1`, j=0,...,k. On their k+1 half-open arcs the vector of
differences is constant. The floor convention gives the right-side
value at a breakpoint, so no extra word is introduced at x=0. Thus
`P_w(k)<=k+1`, without needing an unproved Sturmian theorem.

Apply `0->(0,0)` and `1->(-1,1)`. If h had an eventual period p,
it would have even period 2p. Reading aligned length-two blocks would
give w an eventual period p, a contradiction. This avoids a possible
odd-period alignment mistake.

For L=2k, factors starting at even offsets require k input letters,
and those at odd offsets require k+1. Their respective counts are at
most k+1 and k+2, totaling L+3. For L=2k+1, both offsets require k+1
letters, each contributing at most k+2, again totaling L+3. Overlap
between the two collections can only improve the bound. Therefore
`limsup P_h(L)/L<=1`, whereas kappa>1. A rational lift would force
either ultimately periodic full states, hence periodic h, or the lower
slope kappa. Both are impossible. The lift is nonrational in Z_10.

Combining the pair `h_(2j)=-w_j`, `h_(2j+1)=w_j` in the lift series
gives the coefficient

    10^(2j)/11^(2j+1)-10^(2j+1)/11^(2j+2)
      =100^j/121^(j+1),

so the explicit series in the candidate has the correct positive sign.
In the real numbers its all-one geometric majorant sums to 1/21.
This bound does not identify the real limit with the inverse-limit
element or prove real irrationality/transcendence.

Accepted finite lifting P1 gives each prefix one quotient class modulo
10^N. For the displayed start d=1,r=0, an arbitrarily large positive
representative gives b_0=60Q_0, a_0=b_0+1 and product above 600. Thus
every finite prefix has ordinary admissible lifts, while the whole
infinite path has no ordinary integer lift. These quantifiers are
correctly distinguished.

## 7. Adversarial exception checks and published attribution

Two exact analytic checks are useful; neither is an enumeration premise.
First, the infinite repeated B loop really has a bounded rational lift:
`Q_0=sum 100^j/121^(j+1)=1/21` in Z_10, and its quotients alternate
1/21,-1/21. This is an actual instance of the first alternative, so
dropping that alternative would be false. It is not an official integer
counterexample.

Second, at the admissible start (a,b)=(599,600), Q=10,r=0,d=-1 gives
c=-3. The next b is 657, so Q'=10,r'=57,h=-10. The scalar rule
`ceil(11Q/10)` would give 11, not 10. This witnesses why a direct
application of a nonnegative-correction ceiling-map theorem is invalid.
The candidate and supplement explicitly avoid that application.

Dubickas's original Theorem 3, journal p.245, assumes coprime integers
p>q>1, a positive integer x_0, and `x_(n+1)=ceil(p x_n/q)`. Its
corrections lie in {0,...,q-1}; it proves lower slope log q/log(p/q).
Section 4, p.249, compares the divisibility supplied by repeated blocks
with real exponential growth. The candidate uses this same published
mechanism and constant at p=11,q=10, while separately establishing the
fixed rational denominator, signed growth case, and bounded deterministic
exception. The attribution supplement correctly calls it an adaptation
and makes no novelty claim. I checked the full theorem and Section 4
through the primary publisher PDF; no normality conjecture is used.
[Dubickas, primary paper, Theorem 3 and Section 4](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C40C0C07FEC20797475BB2899C436C9A/S0017089508004655a.pdf/on_integer_sequences_generated_by_linear_maps.pdf).

## 8. Remaining gap, operations and recommendation

The two loops allow arbitrary binary concatenations. Finite controller
size therefore gives no linear complexity upper bound for every avoiding
word. An ordinary integer avoiding orbit could still have complexity
meeting the new lower bound; the candidate does not exclude it. The
official universal equality question remains unresolved by this packet.

No mathematical computation, routine enumeration, CAS, numerical search,
or experiment was run. The report reconstructs the proof analytically.
Read-only commands checked source bytes and accepted-input hashes. The
bundled Poppler rendered the official cached paper for domain inspection;
Dubickas's complete relevant pages were read through the web PDF tool.
No new full paper was downloaded or redistributed, and no Git operation,
shared-status edit, candidate repair, or peer-review comparison occurred.

Recommendation: accept these partial claims with the attribution
supplement retained and eventually integrated into their exposition.
There is no open substantive mathematical issue in this initial audit.
The coordinator must still examine the other independent report and
resolve any contrary finding before promotion.
