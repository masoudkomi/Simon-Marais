# Reversible insertion and the mass of confined tape components

2026-10-18 UTC. **Candidate proof - unverified.** Constructor C,
`/root/review_2017_coarsening_r1`; requested inherited `gpt-6.1-sol`
with `max` reasoning, effective-setting readback unavailable. TWO OTHER
initially blind ENTIRE WHOLE audits and coordinator reconciliation are
required. This is partial research on **2019 B4(b) only**. It does not
determine the growth constant, select a renewal regime, or solve the
annual problem. No novelty or external validation is claimed.

The positive assertion is an entropy estimate for the TOTAL mass in
long confined tape factors, allowing linearly many separate factors.
The negative assertion strengthens the accepted CN countermechanism:
one UNIVERSAL positive density of actual midpoint cuts coexists with
bounded fixed-range factors, for every prescribed fixed range. Thus
the positive estimate still does not cover the entire high-cut class.
The constructed counterfamilies remain exponentially rare; their rarity
is never substituted for a bound on all high-cut outputs.

## 1. Actual objects, operative inputs, and precise statements

At move times numbered from zero the source writes `0,1,0,1,...`.
A history in `L,R` assigns each bit to a chronological tape. Let
`R_n` be the set of DISTINCT resulting tape pairs `X=(u,v)` of total
length `n`, and `c_n=|R_n|`, including the empty pair at `n=0`.
The corresponding physical word with its seed marked is
`reverse(u)1v`. Histories, marked contexts, and unmarked physical
words are not identified.

The source phase is the bit to be written next. A phase-one context
is the bitwise complement of a phase-zero context. An even number
of moves preserves the phase. The complete accepted R7 body and its
current acceptance authority give the actual common root growth
`lambda` and the all-length bounds

```
1 < lambda < 2,
lambda^n <= c_n <= (n+1)lambda^n       for EVERY n>=0.       (1)
```

These weak consequences of accepted R7A suffice for all new counting.
Neither a cap nor a finite obstruction language is used. Accepted
CR4 defines the actual cut number, and accepted CN1 supplies its
explicit two-rate periods; their exact roles are stated in Section 6.
The full three accepted bodies and current authorities were read.
My older CR/CN reviewer roles are accepted-input context, not an
independent audit of this new construction. Root supplied the research
target, not a new mathematical inference in the argument below.

For a binary tape word `w`, let `H_w` give step `+1` to `0` and
step `-1` to `1`, starting at zero. A factor's range includes its
initial vertex and every subsequent vertex. For an integer `R>=1`,
write `L_R(X)` for the longest range-at-most-`R` factor on EITHER
tape. Empty factors are allowed but do not increase this maximum.

For an integer `T>=1`, define `P_(R,T)(w)` to be the maximum SUM
OF LENGTHS of pairwise letter-disjoint factors of `w`, each of length
at least `T` and range at most `R`. Put

```
P_(R,T)(X)=P_(R,T)(u)+P_(R,T)(v).                            (2)
```

This is a maximum packing on each tape separately, not a particular
history's set of excursions. Let `U_(R,T)(w)` be the number of letters
lying in at least one qualifying factor, and sum over both tapes to
define `U_(R,T)(X)`. Overlapping factors count their letters once in U.
All these statistics are intrinsic to the distinct output pair.

Fix throughout

```
K=R+2,               q=2^(4K+1),
b_R=log(2)/(2Rq),
B(T)=4*log(e(T+1))/T.                                       (3)
```

Here and below `log` is the natural logarithm. These constants are
deliberately weak and are not evaluated by a mathematical program.

**CT1: an all-fixed-range longest-factor estimate.** For all integers
`R>=1,n>=1,1<=ell<=n`, under uniform DISTINCT `X in R_n`,

```
Pr(L_R(X)>=ell) <= min(1,16(n+1)^5 exp(-b_R ell)).             (4)
```

Consequently `E L_R=O_R(log(n+1))`. This extends the RANGE covered
by accepted CR1--CR2; it is not a sharper replacement for their much
better range-three constants.

**CT2: total packing mass and covered mass.** For every integer
`R>=1` and real `0<epsilon<=1`, choose an integer `T>=8R` with

```
B(T) <= epsilon*log(2)/(16Rq).                               (5)
```

Such T exist, and every larger T also satisfies (5). For EVERY `n>=1`,

```
Pr(P_(R,T)(X)>=epsilon*n)
 <= min(1,8(n+1)(2n+1) exp(-epsilon*log(2)*n/(16Rq))).         (6)
```

In particular, for every fixed R,

```
lim_(T->infinity) limsup_(n->infinity) E[P_(R,T)(X)/n]=0,
lim_(T->infinity) limsup_(n->infinity) E[U_(R,T)(X)/n]=0.       (7)
```

There is also the displayed exponential bound (6), with epsilon
replaced by epsilon/3 and T chosen accordingly, for the event
`U_(R,T)>=epsilon*n`. This is a statement about ALL actual contexts
with the indicated packing or coverage, not just a selected family.

**CT3: a range-independent positive cut-density obstruction.** For
EVERY fixed real `r>=0` there are a fixed integer `t>=1` and actual
balanced-tape contexts `Y_m in R_(2n_m)` for EVERY `m>=1`, where

```
n_m=1680*t*m,
k_(n_m)(Y_m)/n_m > 1/84,
L_r(Y_m.left)<=12t-1,       L_r(Y_m.right)<=8t-1.              (8)
```

Here `k_n` requires an actual prefix AND actual suffix, equivalently
a complete history through the cut. The density `1/84` is independent
of r, unlike the lower density in accepted CN2. Periods and t still
depend on r and are fixed before m tends to infinity.

Thus for ANY chosen fixed r these outputs have `P_(r,T)=U_(r,T)=0`
for every `T>=12t`, while their cut density stays above `1/84`.
Neither a deterministic cover by arbitrarily long confined pieces
at that fixed range nor a longest-factor version can justify a bound
on all high-cut outputs. This includes the proposed maneuver of first
fixing a small positive cut density and only then choosing its range.

**CT4: an elementary separator obstruction and the remaining gap.**
The even actual marker `(0,1)` does NOT make the fixed-time composition
map uniformly finite-to-one: Section 7 gives a fibre of size at least
`N-2` with first factor degree `2N` and second factor degree `2N-2`.
This refutes that specific proposed constant-loss concatenation route,
not every possible separator or a probabilistic concatenation estimate.
The high-cut MASS estimate remains open after CT1--CT4.

For a real range r, height integrality reduces its factor statistic to
integer `floor(r)`. If `0<=r<1`, no nonempty factor qualifies, so CT1
and CT2 have the trivial zero-statistic interpretation. All nontrivial
counting assertions are stated for integer R>=1. Negative ranges and
preliminary part (a) are outside the task.

## 2. A phase-independent marker and confinement of the other tape

For a selected tape, consider the pair of marker words

```
U=0^K 1^K,                 V=1^K 0^K.                       (9)
```

With U on the left and V on the right, this is the actual output of
`(LR)^K(RL)^K` at phase zero and `(RL)^K(LR)^K` at phase one.
If the selected tape is the right tape, interchange L and R in
these schedules. Each marker uses exactly `4K` moves, returns both
individual heights to their old values, and ends at its starting
source phase. Therefore any number of insertions into an actual
history preserves every ORIGINAL bit and every later ORIGINAL phase.

For each actual output X, choose once and for all the lexicographically
least legal history of X, with `L<R`. The finite set of histories is
nonempty, so this defines a witness without any complexity assertion.
No assumption that arbitrary feasible prefixes extend is made.

Take a selected tape factor of range at most R. In the chosen history,
start just BEFORE its first letter and end just AFTER its last letter.
The other-tape letters consumed in this time interval form one
contiguous factor. At any time the SUM of the two full prefix heights
is 0 or 1: it is the height of the alternating source prefix. Thus,
while the selected coordinate lies in an interval of width R, the
other coordinate lies in an interval of width at most `R+1`.
This includes both endpoints and times when only the other tape moves.
In particular every original constant run in these two middle words
has length at most R and R+1 respectively. Neither middle word is
replaced by an arbitrary walk or an unconditioned height constraint.

Let a selected factor have length ell. Its constant runs all have
length at most R, so its number of runs is at least `ceil(ell/R)`.
Among consecutive run boundaries at least `floor((s-1)/2)` are valleys
`1|0`, where s is the number of runs. It follows that the number of
internal valleys is at least `ell/(2R)-1`, and in particular at least

```
max(0,floor(ell/(2R))-1).                                    (10)
```

At any such valley insert the marker (9) at the history time just
before the following selected 0. The selected marker begins with 0
after an original 1, and ends with 1 before an original 0. Its two
K-runs therefore do NOT merge with original selected letters.

### Exact decoding inside one marked witness block

Suppose the produced block's endpoints on BOTH tapes are supplied.
Read the two middle words in isolation from the outside prefixes
and suffixes; outside run mergers are consequently irrelevant.
Every selected middle run of length at least K is exactly one
inserted K-run. The old runs have length at most R<K, and the valley
rule prevents mergers. These runs occur as the pairs `0^K 1^K`.
Delete them. This recovers the selected middle word and each inserted
valley's position in that recovered word.

On the other tape the old middle runs have length at most R+1<K.
Every inserted word is `1^K 0^K`, in the same orientation. A constant
run in the produced other middle word contains at most ONE inserted
K-run: within one marker the two runs are opposite, and the terminal
0-run of a marker is opposite to the initial 1-run of the next marker,
even if there are no original letters between them. If intervening
original letters merge with a marker run, they cannot bypass that
opposite run to reach another inserted run. Consequently the runs
of length at least K are EXACTLY the runs containing one insertion.
Delete K equal letters from EACH such run. The remaining bit word
is unique, irrespective of which equal letters are considered deleted,
and is exactly the original other middle word.

Empty other middles, insertions at their endpoints, adjacent insertions,
and mergers with short old runs are all covered by this argument.
After the two middle words and unchanged outside pieces are restored,
the original distinct output X is recovered. Its deterministic witness
and selected factors can then be recomputed as finite choices. The
selected marker positions recover the chosen subset of valley sites.
Recovering every inserted history is unnecessary and is not claimed.

For several letter-disjoint selected factors in increasing tape order,
their chosen history intervals are disjoint and in the same order.
There may be gaps, and two successive intervals may share an endpoint.
Their other-tape intervals are also disjoint, allowing empty intervals
and repeated endpoints. Thus the same decoder applies block by block
when the ordered endpoint arrays are supplied. Original gaps are
unchanged. The decoding is an injection of OUTPUTS plus chosen sites,
not a count of the many legal histories of one output.

## 3. CT1: one long factor with only polynomial boundary information

For an X with `L_R(X)>=ell`, select deterministically a factor of
EXACT length ell and range at most R: first choose the left tape if
possible, otherwise the right, then the leftmost such factor. Put

```
M=max(0,floor(ell/(2R))-1),       J=floor(M/q),
N=n+4KJ.                                                        (11)
```

Select the first M valleys of this factor. Each J-subset produces an
actual output in R_N. Record the selected side and the UNCHANGED
prefix and suffix lengths on both tapes outside the witness block.
There are at most `2(n+1)^4` such records. Given the record and the
new output, the produced middle endpoints are determined by removing
these old outside lengths; Section 2 decodes X and the chosen subset.
If J=0 this is the identity insertion and remains injective. Hence

```
#{X in R_n:L_R>=ell} * binom(M,J) <= 2(n+1)^4 c_N.            (12)
```

For J>=1, factor by factor in the product formula for a binomial,

```
binom(M,J) >= (M/J)^J >= q^J.                                (13)
```

For example `(M-i)/(J-i)>=M/J` for `0<=i<J`; all denominators
are positive. For J=0 the final inequality is `1>=1` separately.
Using lambda<=2 and (3), the factor
`lambda^(4KJ)/binom(M,J)` is at most `2^(-J)`.

Since `M<=ell/(2R)<=n/(2R)` and `J<=M/q`,

```
N <= (1+2K/(Rq))n <= 2n,
J >= ell/(2Rq)-2.                                             (14)
```

Here `K/R<=3` and `q>=2^13`, so no small-R exception is hidden.
The lower bound uses `M>=ell/(2R)-2` and the floor in J.
Divide (12) by c_n and apply (1), (13)--(14). It is at most

```
2(n+1)^4(2n+1)*4*2^(-ell/(2Rq))
 <=16(n+1)^5 exp(-b_R ell),                                  (15)
```

which is (4). For ell>n the event is empty. In particular, if
`ell_0=ceil(log(16(n+1)^5)/b_R)` and `alpha=exp(-b_R)`, summing
the bounded tail gives

```
E L_R <= ell_0 + alpha/(1-alpha).                            (16)
```

This proves the claimed logarithmic expectation without assuming
consecutive-count asymptotics or choosing a renewal alternative.

## 4. CT2: linear collections of pieces with subexponential endpoint cost

Fix ONE tape and a real `0<eta<=1`. On the event that its packing
mass is at least eta*n, choose a maximum-mass packing, breaking ties
lexicographically by the ordered endpoint list. Let its lengths be
`ell_1,...,ell_m`, and W their sum. They are disjoint letter intervals,
`ell_j>=T`, and

```
W>=eta*n,              m<=W/T<=n/T.                           (17)
```

The number of valleys across these factors is at least

```
sum_j(ell_j/(2R)-2)
 >= W(1/(2R)-2/T) >= W/(4R) >= eta*n/(4R),                   (18)
```

provided `T>=8R`. The weaker subtraction by 2 is deliberate and
valid by (10). Choose the first

```
M=floor(eta*n/(4R))
```

valleys across the packing in order, and insert at a J-subset, with
`J=floor(M/q)` and `N=n+4KJ`. Each input has the SAME number of site
choices, and N is independent of the input and chosen subset. The
simple estimates now give

```
N <= (1+K*eta/(Rq))n <= 2n,
J >= eta*n/(4Rq)-2.                                           (19)
```

Record m and the `2m` produced block endpoints on EACH tape. They
form two NONDECREASING arrays in `{0,...,N}`. The selected blocks
are already ordered, so no m! matching or permutation record is used.
The other blocks may be empty. The number of possible arrays on one
tape is at most `binom(N+2m,2m)` by the count of weakly ordered
integer lists. Using Section 2 to decode block by block proves

```
A_n(eta) binom(M,J)
 <= c_N * sum_(0<=m<=floor(n/T)) binom(N+2m,2m)^2,             (20)
```

where A_n(eta) counts distinct outputs whose chosen tape has the
specified packing mass. Recording all boundaries by `(N+1)^(4m)`
would be too expensive; (20) is the essential ordered-boundary gain.
The endpoint arrays and the produced words first recover X; the
deterministic maximum packing of that X and its chosen witness then
fix every original block and every chosen valley. No independent
outside matching or arbitrary legal completion is assumed.

For m>=1, the elementary binomial estimate gives

```
binom(N+2m,2m) <= (e(N+2m)/(2m))^(2m)
 <= exp[(2n/T) log(e(T+1))].                                  (21)
```

For completeness, `x log(e(2n+x)/x)` increases for positive x:
its derivative is `log(1+2n/x)+x/(2n+x)>0`. Thus N<=2n and
`2m<=2n/T` justify the second inequality even when n/T is not an
integer. The m=0 term is 1. There are at most n+1 summands, so the
sum in (20) is at most `(n+1)exp(B(T)n)`.

Divide (20) by c_n and use (1), (13), and (19), obtaining

```
Pr(P_(R,T)(chosen tape)>=eta*n)
 <=4(n+1)(2n+1)
       * exp[(B(T)-eta*log(2)/(4Rq))*n].                      (22)
```

This also covers M=0 or J=0; the estimates may then exceed 1 and
make no false positive assertion. If there is no packing, A_n=0.

If the sum of the two tape packing masses is at least epsilon*n,
one tape has mass at least epsilon*n/2. Apply (22) with eta=epsilon/2
and take the union of these two events. Condition (5) leaves exponent
at most `-epsilon*log(2)/(16Rq)`, giving exactly (6).
The function B(T) tends to zero and is strictly decreasing for T>0,
as direct differentiation shows. Therefore every prescribed R and
epsilon admit a fixed T before n tends to infinity.

### Covered mass, with all overlapping factors accounted for

On one tape take the finite family of ALL qualifying factors. Greedily
choose a longest remaining factor, then discard every factor sharing
a letter with it, and repeat. The chosen factors are disjoint. If a
chosen interval has length d, every interval it discards has length
at most d and intersects it. The union of all those intervals is
contained in its enlargement by d-1 letters at each end, of length
at most `3d-2<=3d`. Summing these bounds over the chosen intervals
gives the pointwise inequality

```
U_(R,T)(w) <=3 P_(R,T)(w),
U_(R,T)(X) <=3 P_(R,T)(X).                                  (23)
```

The enlargement may be clipped by tape endpoints, which only improves
the bound. Thus covered mass at least epsilon*n implies packing
mass at least epsilon*n/3, proving the stated exponential coverage
bound from (6). Both statistics lie between 0 and n. For a fixed
epsilon, their normalized expectation is at most epsilon plus the
probability of exceeding epsilon*n. First choose the appropriate fixed
T, then let n tend to infinity, then let epsilon decrease to zero.
Monotonicity in T gives both limits (7). No interchange of an n-dependent
range or block threshold is used.

As an optional translation to the official objects, the proportion of
unmarked length-(n+1) outputs admitting SOME marked seed with either
bad property is at most `(floor(n/2)+1)` times its probability under
uniform R_n: the bad word count is at most the bad context count,
and accepted R7D gives `c_n<=(floor(n/2)+1)b_(n+1)`. Thus the same
fixed-parameter exponential rarities survive forgetting the mark.
This does not identify every 1 as an admissible seed, nor transfer
ratio convergence or select a renewal regime.

## 5. Why the proof is an actual counting argument, with its limitations

The marker construction is an entropy-increasing reversible map.
It uses actual full histories ONLY as deterministic witnesses for
where to insert; its inputs and decoded outputs are distinct tape
pairs. The exponential gain is the binomial choice of insertion sites,
while the loss is their fixed added length. The selected marker's
run orientation and the two ordered boundary arrays pay for every
possible other-tape merger and boundary matching. This is not an
application of a self-avoiding-walk pattern theorem.

The generic incoming/outgoing arrow count is the established
multivalued-map principle, for example Duminil-Copin--Ganguly--Hammond--
Manolescu, arXiv:1809.00760v2, Section 1.3, Lemma 1.5 and its complete
one-paragraph proof. That primary passage was read. Their walk model
and insertion theorems are NOT imported; no self-avoidance dictionary
or lattice-connective-constant identification is asserted. Here (12)
and (20) are proved directly by the displayed decoder.

The all-fixed-range constants are extremely weak. They are not uniform
in R, and T in (5) may be very large. In particular (7) has fixed R
BEFORE T and n; it gives no useful estimate when the height range is
allowed to grow with n. That missing uniformity cannot be suppressed
when discussing cut components. The next section demonstrates an
additional pointwise obstruction with one fixed positive cut density.

## 6. CT3: padding the actual CN periods without losing their phases

Use the COMPLETE accepted CN1 construction, not just its conclusion
about unspecified feasible words. For a fixed integer `h>=2`, it
supplies balanced words u,v of lengths

```
a=4(2^h-1),               b=3*2^h-4,                         (24)
```

with full ranges `2h` and `2h-1`, and explicit even phase-zero
histories for BOTH `(u,v)` and `(u,v^2)`. All elementary CN history
blocks have even length. In the slow history the separation between
the FIRST v and the SECOND v is between such elementary blocks,
so the source phase at this separation is zero. This extra operative
fact follows from the displayed `J_h J_h` schedule in the accepted
body; it is not inferred merely from the total output pair.

Let `s=01` and set

```
t=a/4=2^h-1,
p=3t-a/4=2t,
d=2t-b/4,
u'=s^p u s^p,                v'=s^d v s^d.                  (25)
```

The quantities are integers. Because `a>b>0`, `d>=t` and `p>=t`;
in fact d>t. Their lengths are exactly

```
|u'|=12t,                     |v'|=8t.                       (26)
```

There are ACTUAL phase-zero schedules for `(u',v')` and `(u',v'^2)`:
for the first, add left `s^p` by `(LL)^p`, right `s^d` by `(RR)^d`,
run the accepted fast history, then append these two left/right pads.
For the second, start with the same two pads, run the accepted slow
history but at its even middle-v boundary insert `(RR)^(2d)`, then
append the same two pads. The right word is exactly
`s^d v s^(2d) v s^d=v'^2`; the left word is exactly u'. Every inserted
loop is even, so phases are unchanged. The first/last left/right
pads are explicit consecutive history blocks that can later be removed.

Write F for the fast padded context and S for the slow padded context.
Their degrees are `20t` and `28t`. Form equal-degree actual contexts

```
A=F^7=(u'^7,v'^7),       B=S^5=(u'^5,v'^10),
|A|=|B|=140t.                                                 (27)
```

Their left-minus-right tape lengths are `28t` and `-20t` respectively.
Therefore, for every integer m>=1,

```
Y_m=A^(10m) B^(14m)=(u'^(140m),v'^(210m)),
|Y_m.left|=|Y_m.right|=n_m=1680tm.                             (28)
```

All these are ACTUAL even contexts with specified full histories.
The macrocontexts commute as output pairs, not as histories. To get
an initial midpoint cut, take as prefix `12m` macroblocks, with j
copies of B and `12m-j` of A. The suffix uses the remaining blocks.
This is possible exactly for the displayed constructed choices

```
2m<=j<=12m,
i_j=1008tm-24tj,           n_m-i_j=672tm+24tj.                 (29)
```

Indeed the prefix u' exponent is `84m-2j` and the prefix v' exponent
is `84m+3j`. Each prefix AND each suffix has at least one u' and v'
period: their exponents lie respectively in `[60m,80m]` and
`[90m,120m]`. These ranges also verify actual tape-bound endpoints.

### Turning each coarse cut into an actual interval of cuts

Use the explicit padded schedules for the chosen prefix and suffix.
Remove from the END of the prefix its last left `s^p` and last right
`s^d` loop blocks. The remaining context C is actual and has degree
`n_m-2(p+d)`, still even. Remove from the START of the suffix its
first left and right pad blocks, leaving an actual even context D.
Consequently, as an actual output factorization,

```
Y_m=C * (s^(2p),s^(2d)) * D.                                  (30)
```

This operation relies on the actual histories and explicit endpoint
pad blocks; it does not assert that height-zero removal is always legal.
For ANY integer e with `-t<=e<=t`, the central loop context in (30)
splits into two actual even contexts

```
(s^(p+e),s^(d-e)) * (s^(p-e),s^(d+e)).                        (31)
```

All four exponents are nonnegative because p,d>=t. Each factor can
be written using its left and right LL/RR loops at phase zero.
The first factor's degree is always `2(p+d)`, so C followed by it
still stops at EXACTLY time n_m. Thus (31) supplies the genuine cut

```
(i_j+2e, n_m-i_j-2e),             -t<=e<=t.                    (32)
```

Every counted vertex has a complete history, including the suffix.
For a fixed j the `2t+1` vertices are distinct. The centers for
successive j differ by `24t`, while each cluster lies within `2t`
of its center, so clusters do not intersect. There are `10m+1`
values of j. It follows that

```
k_(n_m)(Y_m) >= (10m+1)(2t+1) > n_m/84.                      (33)
```

To finish (8), choose h FIXED with `2h-1>r`. The pads s^p,s^d have
height range `[0,1]`, contained in the ranges of u and v. Hence u'
and v' retain the exact full ranges `2h` and `2h-1`. A balanced
periodic word of length l and full range exceeding r has no range-r
factor of length l: every l-letter cyclic factor visits the entire
set of period heights. Thus all its powers have longest such factor
at most l-1. Apply this with (26) to obtain the two bounds in (8).

For any finite list of ranges choose its maximum r. This proves the
same universal positive-density obstruction simultaneously for that
list. In particular, even at the fixed density epsilon0=1/84, no
choice of a SINGLE fixed range can make high cut number force pieces
of arbitrarily large length. It does not disprove a probabilistic
cover with an explicitly controlled exceptional set, nor an estimate
involving adaptive ranges or richer synchronized-component statistics.

### The new padded flat also has negligible mass; no high-cut cover follows

For fixed h, the output map `(i,j)->A^i B^j` is injective. Its two
word exponents are `(7i+5j,7i+10j)`: their difference recovers `5j`
and then i. Positive period lengths make these exponents determined
by tape lengths, without a primitive-word assumption. At degree
`140t*M` this flat consequently has exactly M+1 distinct outputs.
By (1) its probability is at most

```
(M+1)lambda^(-140t*M).                                        (34)
```

At total degree `2*(140t*M)`, its entire contribution to the midpoint
mean is at most

```
(140t*M+1)(2M+1)lambda^(-280t*M),                              (35)
```

using the elementary bound `k_n<=n+1`. These estimates concern this
ENTIRE particular flat only. Neither (34) nor (35) counts outputs
from all possible periods, nor covers the full high-cut event.

## 7. CT4: why the simplest fixed-separator argument does not close the gap

A tempting route to bounded normalized counts is a bounded-loss
injection from two arbitrary contexts with a fixed short separator.
Such an injection, if actually established with uniform constants,
could be much stronger than the existing polynomial bound. The
following shows that just inserting the rank-one actual marker
`B0=(0,1)` does NOT supply the needed bounded fibre assertion.

Put `s=01,t0=10`. For ALL integers r>=1 and s0>=0, the pair
`(s^r,t0^s0)` is an actual even context: a phase-zero history is

```
(LL)^(r-1) L R^(2s0) L.                                      (36)
```

The first LL loops contribute `s^(r-1)` to the left. The next L
writes 0; the R-block starts at phase one and writes `t0^s0`;
the final L writes 1. This also verifies the endpoint s0=0.

Fix N>=3 and `1<=a<=N-2`. Define actual contexts

```
X_a=(s^a,t0^(N-a)),                     degree 2N,
Z_a=(1 s^(N-a-1), 0 t0^(a-1)),          degree 2N-2.           (37)
```

The first is actual by (36). For the second, start with the actual
pair RL, giving `(1,0)`, then apply (36) with
`r=N-a-1>=1,s0=a-1>=0`. All histories are even. Therefore every
pair `(X_a,Z_a)` lies in the domain of the SAME fixed-time map

```
(X,Z) -> X * B0 * Z,
R_(2N) x R_(2N-2) -> R_(4N).                                (38)
```

But all these images equal `(s^N,t0^N)`. For the right word this is
`t0^(N-a) 1 0 t0^(a-1)=t0^N`, and the left word is
`s^a 0 1 s^(N-a-1)=s^N`. The N-2 input pairs are distinct because
their first tape lengths `2a` are distinct. This proves the stated
unbounded fibre. The family itself has range-one tapes and is rare
by CT1. It refutes only the unconditional uniform-fibre claim for
this explicit separator; it is not a counterexample to bounded
normalized counts or to all possible separator strategies.

## 8. Exact remaining high-cut inference and what has actually advanced

For uniform DISTINCT `X in R_(2n)`, accepted CR4/CN give

```
E k_n(X)=c_n^2/c_(2n),
E k_n=o(n) iff Pr(k_n>=epsilon*n)->0 for EVERY epsilon>0.      (39)
```

CT2 now gives an actual mass bound for a much broader event than
one long low-range factor: even many disjoint such factors cannot
occupy positive density when their minimum length is sufficiently
large at that FIXED range. It also controls the union of all such
factors and, with a polynomial loss, their unmarked outputs. This is
an actual counting theorem for a component-mass statistic, not a
finite example or a diagnostic abstract sequence.

To use it in (39), one still needs a proved cover or compression of
the high-cut outputs with its remaining exceptional mass controlled.
CT3 rules out a deterministic fixed-range cover that would work for
arbitrarily large T, even when the range can be chosen after fixing
the positive cut density. The explicit two-rate phases, interior pad
boundary, and cluster multiplicities explain the obstruction. CT3's
rare flat does not tell whether any other high-cut family has large
mass. CT4 separately blocks a simple uniform separator shortcut.

No proof is supplied that every high-cut output admits a short period
description, that all two-rate flats exhaust the event, that all period
descriptions together have small entropy, or that a height-range choice
can be made uniformly through the thresholds in (5). These are genuine
missing inferences. In particular the vanishing-mean condition in (39),
positive defect, exclusion of finite critical mean, exact lambda,
unmarked consecutive ratios, and
the annual answer all remain unresolved.

All new arguments are hand proofs; no mathematical scan, CAS, sample,
certificate replay, or routine program supplies any assertion. Source
read limits, actual failed routes, all proof obligations and compact
immutable-parent metadata are preserved in the accompanying packet.
