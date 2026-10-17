# 2022 B4(b): block arithmetic, rich irrational lifts, and a causal-carry obstruction

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
review_2022_complexity_r2, returning as a research owner after its
assigned reviews were frozen. Requested gpt-6.1-sol / max;
independently verified effective settings unavailable.

This packet requires two fresh independent nonconstructor audits.
It does not prove universal equality or construct an admissible
integer counterexample. No novelty is asserted. No mathematical
enumeration, CAS, or integer-start search is a premise.

## Inputs and scope

Only the open part (b) is considered. For positive integers
a_0,b_0 with a_0 b_0>=600, use the simultaneous map

    a'=a+2 floor(b/20),    b'=b+3 floor(a/30).

Use the exact accepted quotient/controller identities in
proofs/reviewed-partials-v1.md and the rational-lift arithmetic
in proofs/reviewed-arithmetic-complexity-v1.1.md. Write

    b=60Q+r,  0<=r<60,   d=a-b,
    c=3 floor((r+d)/30),
    d'=d+2 floor(r/20)-c,
    r'=(6e+r+c) mod60,   e in{0,...,9},
    h=(r+c-r')/6,
    10Q'=11Q+h,          h=-e mod10.

The full finite strip controller, when used below, has
-13<=d<=23 and all ten abstract controls at each state.
Its closure is accepted/attributed context; no preliminary
trapping argument is investigated or reproduced here.
Finite control words lift to congruence classes with arbitrarily
large positive integer representatives. An infinite word has
only a Z10 inverse-limit lift unless ordinary integrality is
separately established.

Rational in Z10 means a diagonal rational u/v in lowest terms
with gcd(v,10)=1. The fixed-denominator property vQ_n in Z
is an accepted input. Z10 is an inverse-limit ring, not a field.

The three main deductions are:

- R1: an exact restricted-family reduction to a stopped scalar
  ceiling map of base 121/100;
- R2: a run-length obstruction and explicit irrational avoiding
  lifts with maximal binary-loop factor complexity;
- R3: impossibility of one specified bounded causal integer-carry
  normalization of the full ten-control system.

The published divisibility-versus-real-growth mechanism used
in R2 is credited to Dubickas (2009), Theorem 3 and Section 4.
R1 identifies a particular instance of the approximate
multiplication termination question in Dubickas–Mossinghoff
(2009), Section 1. Neither source is imported as a theorem
resolving that instance.

## R0. Quantitative real growth for every official start

This auxiliary observation uses no strip input. Put s_n=a_n+b_n,
u_n=a_n mod30 and v_n=b_n mod20, using nonnegative residues.
With beta=11/10,

    s_(n+1)=beta s_n-(u_n+v_n)/10,   0<=u_n+v_n<=48.

Consequently

    C=s_0-sum_(j>=0) (u_j+v_j)/(11 beta^j)

converges in R, and

    s_n=C beta^n+theta_n,
    theta_n=sum_(j>=0) (u_(n+j)+v_(n+j))/(11 beta^j),
    0<=theta_n<=48.

The official product bound implies s_0>=49: positive integers
of sum at most 48 have product at most 24^2=576<600.
Thus C>=s_0-48>=1. In particular s_n>=beta^n.
At the inclusive product boundary, (24,25) has sum 49;
the inequality does not discard small initial quotients.

This is a real growing component of an actual orbit.
It does not identify the real value of a correction series
with its Z10 value. R3 will deliberately use a different,
bounded auxiliary real solution of the same affine equations.

## R1. The arbitrary two-loop family is an exact stopped-ceiling instance

At S=(d,r)=(1,0), the accepted loops are

    A: controls(0,0), residues(0,0,0), corrections(0,0);
    B: controls(1,9), residues(0,6,0), corrections(-1,1).

Their difference is always 1. Indeed c=0 at residues 0 and 6,
and the formula for d' then gives d'=1. Every infinite binary
word w_0 w_1 ... defines an abstract avoiding path by choosing
A for 0 and B for 1.

Let X_j=Q_(2j) be the quotient at block boundaries. Combining
the two exact quotient updates gives

    100 X_(j+1)=121 X_j-w_j.                         (R1.1)

For A the combined correction is zero. For B it is
11(-1)+10(1)=-1. The unique Z10 lift is

    X_0=sum_(j>=0) w_j 100^j/121^(j+1) in Z10.       (R1.2)

This series is not assigned its real value when discussing
ordinary integer lifts.

For an ordinary integer X_j, equation (R1.1) is integral
exactly in the following two classes:

    w_j=0: X_j=0 mod100;
    w_j=1: X_j=81 mod100.                            (R1.3)

For the second class use 121 X=1 mod100, and
21*81=1 mod100. These are also exactly the full two-control
conditions, including intermediate integrality:

- If X=0 mod100, the first quotient is 11X/10, is 0 mod10,
  and both controls are 0.
- If X=81 mod100, the first control is 1 and the first quotient
  is (11X-1)/10, which is 9 mod10. The second control is 9.

The converse follows from those same congruences. Merely
checking the final block equation has therefore not lost
a constraint from the middle of the original orbit.

For a positive integer lift X_0>=1, every block quotient
in this family is positive and increases, since
X_(j+1)>=1.21 X_j-0.01>X_j. Put

    Y_j=X_j-1.

On the two allowed classes,

    100 Y_(j+1)=121 Y_j+21-w_j.

Here 21-w_j is either 21 or 20, in {0,...,99}.
It is the unique least nonnegative correction making
the numerator divisible by 100. Therefore, exactly,

    Y_(j+1)=ceil(121 Y_j/100),
    Y_j mod100 in S={99,80}.                         (R1.4)

Any positive integer X in (R1.3) is at least 81, so the
corresponding Y is positive. Conversely, a positive orbit
of the ceiling map staying forever in S gives X=Y+1
and recovers the A/B controls by (R1.3), including every
intermediate quotient. Its contest initial pair is

    (a_0,b_0)=(60(Y_0+1)+1,60(Y_0+1)).

It is positive, has product>=600, and has d_n=1 at every
time. Thus the following two existence statements are
equivalent:

1. Some arbitrary A/B concatenation has a positive
   ordinary integer quotient lift.
2. Some positive integer Y has an orbit of
   T(Y)=ceil(121Y/100) staying in {80,99} mod100 forever.

Equivalently, all A/B integer lifts are excluded exactly
when the map that applies T on these two classes and
stops on all other classes terminates on every positive
integer.

This is an exact restricted-family reduction, not a
conjugacy for every contest controller path. Leaving S
means leaving this A/B family; it does not by itself
mean that the contest orbit has reached equality.
A nonterminating Y would supply an actual counterexample
to universal equality. Termination of this one scalar
instance would exclude this family only.

Dubickas–Mossinghoff formulate the general proper-subset
termination question, with 0<|S|<q. Their singleton
Proposition 3.2 does not cover this two-residue instance.
Andrieu–Eliahou–Vivion (2026), Question 3.12 and
Proposition 3.13, relate general termination to their
normality conjecture. It remains a conjectural input
there. The elementary implication needed here is just:
equidistribution modulo 100 for every positive
ceil(121Y/100) orbit would force escape from S.
No such equidistribution theorem is used.

## R2. A run-length obstruction that still sees rich words

Let w be any infinite binary loop word that is not
eventually zero. Suppose its lift X_0 in (R1.2) is
rational in Z10, with denominator v>0 coprime to 10.
Then vX_j is an ordinary integer for every j, by the
accepted fixed-denominator argument.

No X_j can be zero. If X_j=0, (R1.1) and
X_(j+1) in Z10 force w_j=0, since -1 is not divisible
by 100 in Z10. They then give X_(j+1)=0. Induction
would make the remaining word all zero, contrary
to the hypothesis.

Read the rational sequence also in R. Let gamma=121/100
and A=|X_0|+1/21. Iterating (R1.1), or using the
geometric bound for its error 1/100, gives

    |X_j| <=gamma^j(|X_0|+1/21)-1/21
          <=A gamma^j.                              (R2.1)

If a block of M consecutive zero loop symbols begins
at position j, (R1.1) has zero correction throughout it:

    100^M X_(j+M)=121^M X_j.

Multiplying by v and using coprimality shows
100^M divides vX_j. This is a nonzero integer, so

    100^M <=v|X_j| <=v A gamma^j.

Hence every such zero block satisfies

    M <= alpha j+log(vA)/log100,
    alpha=log(121/100)/log100
         =log(11/10)/log10 <1.                       (R2.2)

The constant depends on the rational lift; alpha does not.
One may replace a negative additive constant by zero
for a weaker bound. This is a bound on where long
constant factors may begin, not on the total number
of distinct factors.

For an actual positive integer A/B lift the sharper
bound follows directly from X_j<=gamma^j X_0:

    M <= alpha j+log(X_0)/log100.                    (R2.3)

The exceptional all-zero tail is necessary in the
rational formulation: its zero quotient is a bounded
lift. It never gives an official positive initial pair.

### An explicit word with maximal binary factor complexity

Let W_k be the finite concatenation, in lexicographic
order, of all binary words of length k. No enumeration
needs to be run: this is a symbolic definition of a
finite word of length k 2^k.

Starting from the empty prefix, at stage k append W_k.
Let N_k be the new total prefix length at that moment,
then append N_k zeros. Repeat forever. This defines
an infinite binary word w by nested prefixes.

For every k it contains W_k and therefore every binary
word of length k. Thus its factor complexity is exactly

    P_w(k)=2^k for every k>=1.

It is not eventually zero, since later W_k contain
ones. At position j=N_k it has a zero block of length
M=N_k, and N_k tends to infinity. If its Z10 lift
were rational, (R2.2) would require

    (1-alpha)N_k <=log(vA)/log100

for every k, an impossibility. Therefore its lift
is irrational in Z10. It is an abstract avoiding
controller path with all finite prefixes positively
integer-liftable, and with no rational infinite lift.

The corresponding correction word has at least 2^k
distinct factors of length 2k, because
0 ->(0,0) and 1 ->(-1,1) is an injective aligned
length-two code. Its factor complexity grows
exponentially, so it passes every finite linear
lower-slope test such as the accepted Dubickas-type
bound. The run obstruction excludes it for a
different positional reason. No universal upper
complexity bound for avoiding paths is inferred.

The divisibility-versus-growth idea is published
prior art. This is a separately proved, unreviewed
application to run placement and rich loop words,
without a novelty claim.

## R3. No uniformly bounded causal integer carry to ceiling digits

Here the input is the FULL ten-control strip system
from S_0=(1,0), including paths that may hit equality.
All ten controls are available after every finite prefix.
This section makes no assertion that an avoiding
subcontroller itself has ten branches everywhere.

A causal integer offset rule assigns k_n in Z to
each finite control prefix e_0,...,e_(n-1).
Its initial value k_0=m is fixed independently
of the future control word. Allow arbitrary memory.
It would normalize the quotient with unit coefficient
if the transformed corrections

    delta_n=h_n+10 k_(n+1)-11 k_n                   (R3.1)

always belonged to {0,...,9}. For ordinary integer
quotients this would make Z_n=Q_n+k_n satisfy
Z_(n+1)=ceil(11Z_n/10).

**Claim R3.** No such rule can keep |k_n| uniformly
bounded over all input prefixes. In particular no
fixed-initial-state finite causal transducer whose
states carry bounded integer offsets can achieve
(R3.1) for the full controller.

In fact any causal canonical-digit rule obeys

    max_(length-N controls) |k_N|
      >=(13/120)(11/10)^N-29/2.                    (R3.2)

The bound may be vacuous for small N. It is a
worst-input bound, not a statement that every
actual orbit has a growing carry.

### A separate bounded real shadow

For any infinite control word define

    Qhat_n=-sum_(j>=0) h_(n+j)/(11 beta^j) in R,
    beta=11/10.

This is explicitly a REAL definition. It is not an
identification with the Z10 series or with an actual
integer quotient. The signed alphabet gives
|Qhat_n|<=10 and
10Qhat_(n+1)=11Qhat_n+h_n.

Put

    bhat_n=60Qhat_n+r_n,
    ahat_n=bhat_n+d_n,
    shat_n=ahat_n+bhat_n.

The symbols
u_n=r_n+d_n-30 floor((r_n+d_n)/30) and
v_n=r_n-20 floor(r_n/20) are in [0,29] and
[0,19], respectively. They need not be the
ordinary real remainders of ahat,bhat.
The controller algebra nevertheless gives

    shat_(n+1)=beta shat_n-(u_n+v_n)/10.

The shadow sequence is bounded, so backward iteration
uniquely yields

    shat_n=sum_(j>=0) (u_(n+j)+v_(n+j))/(11 beta^j),
    0<=shat_n<=48.

Since d_0=1,r_0=0, shat_0=120Qhat_0+1 and therefore

    -1/120 <=Qhat_0<=47/120.                        (R3.3)

Actual official starts have R0's positive growing
component; the auxiliary shadow has that component
set to zero by its separate definition. No claim
that an admissible integer orbit is bounded has
been inserted into this argument.

### Exact finite averaging, with no independence premise about one orbit

Fix a length N. Average over the 10^N control prefixes,
each extended by zero controls solely to define Qhat.
The first N controller steps and offsets are causal,
so that extension does not change them.

For each fixed prefix of length n<N, k_n is already
fixed. Reducing (R3.1) modulo 10 gives

    delta_n=-e_n-k_n mod10.

If all delta_n are canonical digits, as e_n ranges
from 0 to 9 they are exactly 0,...,9 once each.
Their average is 9/2. This is exact finite counting,
not an independence assumption for an integer orbit.

Let Avg_N denote the above uniform finite average.
The sequence Zhat_n=Qhat_n+k_n satisfies the
transformed affine recurrence. Iterating it and
averaging gives exactly

    Avg_N k_N
      =beta^N [m+9/2+Avg_N Qhat_0]
         -9/2-Avg_N Qhat_N.                         (R3.4)

By (R3.3), Avg_N Qhat_0 is in
[-1/120,47/120]. For any integer m,

    |m+9/2+Avg_N Qhat_0| >=13/120.

For m<=-5 this expression is at most -13/120;
for m>=-4 it is at least 59/120.
Also |Avg_N Qhat_N|<=10. Applying the triangle
inequality to (R3.4) proves (R3.2), since some
individual |k_N| is at least |Avg_N k_N|.
Uniform boundedness is impossible.

### Exact boundary of the obstruction

This excludes a bounded online integer-offset
normalization with the SAME initial offset/state
for all futures from (1,0). If it were proposed
only for every positive integer Q_0 at that
controller state, but still with that fixed
causal initialization, finite positive lifting
of every control prefix would impose the same
impossible finite conditions.

It does not exclude initialization depending
on the canonical digits of Q_0, noncausal/future
boundary conditions, unbounded carries, rational
scalings of Q, a word-dependent initial state,
or a restricted input language.

Akiyama–Frougny–Sakarovitch Proposition 13 gives
a finite RIGHT transducer on finite signed
digit words, with a final-output condition.
That theorem is not contradicted: its reading
direction and terminal boundary are precisely
outside R3's fixed forward initialization.
There is no inference from finite controller
states to automaticity.

## Remaining mathematical gap and review obligations

R1 leaves a genuine two-residue integer termination
instance unresolved. R2 excludes additional explicit
irrational avoiding lifts even when the binary loop
word contains every finite binary factor. It does
not exclude all rich words or all rational lifts.
R3 blocks one tempting causal normalization bridge;
it does not replace it with a proof of equality.
The full nonperiodic, high-complexity ordinary-integer
avoiding-path question remains open in this work.

Independent reviewers should reconstruct the block
congruences and BOTH directions of R1, the official
positive/product domain, the nonzero rational
integer in the run proof, the recursive rich word,
the independence of real shadow and Z10 lift,
the exact sign and coefficients in (R3.4), and
the full-input/fixed-initial-carry scope.
The author must repair any substantive objection;
only the coordinator may promote a scoped result.
