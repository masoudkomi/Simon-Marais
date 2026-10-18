# Confined tape pieces, exact composition fibres, and the critical-growth gap

2026-10-18 UTC. **Candidate proof - unverified.** Sole NEW constructor:
`/root/review_2022_complexity_r2` (B). Requested inherited
`gpt-6.1-sol/max`; independent effective-setting readback unavailable.
TWO OTHER fresh initially blind ENTIRE WHOLE audits, followed by coordinator
reconciliation, are required. This concerns **2019 B4(b) only**. No actual
renewal regime, exact lambda, improved enclosure, original-output ratio,
annual solution or novelty is claimed. No mathematical executable, scan,
CAS, source program or old certificate was run.

The unconditional new estimate counts DISTINCT actual chronological
contexts with a long tape piece confined to four height levels. Its
exponential loss gives logarithmic expected longest such pieces, including
an explicit near-zero tilted window. A second argument identifies exact
composition fibres with feasible antidiagonal cuts. The missing inference
is a bound on the NUMBER of those cuts from tape geometry. A bound on their
SPREAD is false, as the accepted staircase family shows below. Thus this
packet supplies an actual entropy separation, while leaving the critical
renewal regime open.

## 1. Official domain, exact inputs, and roles

The official process starts with1 and adds the mandated0 or1 at either
end according to length parity. Its DISTINCT length-n counts are b_n;
the requested quantities are their lower and upper exponential rates.
Only(b) is investigated. The accepted chronological normalization
distributes the source0101... onto two ordered tapes. An n-move context
X=(u,v) has |u|+|v|=n. Its physical left part is reversed only on returning
to the official string. Contexts retain the distinguished original1;
their counts c_n are neither histories nor unmarked b_(n+1).

Let R_n be the set of these DISTINCT contexts, c_n=|R_n|, c_0=1.
Each context has one lexicographically least L/R history, L<R. Source
phase1 is normalized to phase0 by complementing BOTH tape words.
Accepted operative inputs are:

* The second-pass canonical-renewal body under its acceptance register,
  including unique canonical histories and the ACTUAL minimal-bad set F.
* The complete accepted R7 body, which gives R=1/lambda,
  C(z)=sum c_n z^n=1/(1-2z+F(z)),
  F(R)=2R-1, F'(R)<=2, and delta=2-F'(R)>=0.
  With s_n=c_n/lambda^n, s_0=1, s_n increases strictly,
  1<s_n<n+1 for n>=1, and:
  delta>0 implies s_n->1/(R delta);
  delta=0 and mu=R^2 F''(R)/2<infinity implies s_n~n/mu;
  delta=0 and mu=infinity implies s_n->infinity, s_n/n->0.
  In the finite critical case mu>=1. Endpoint F'' is an extended
  nonnegative series, not an assumed analytic continuation.
* Accepted MR1: rho_n=c_n/c_(n-1) decreases nonstrictly, with
  rho1=rho2=rho3=2 and rho_(n+1)<rho_n for all n>=3.
  MR2's bounded-joining hypothesis is NOT an available theorem.
* Accepted G2: if M(a,b) counts actual contexts of bidegree(a,b), then
  M(a,b)<=lambda^(a+b) for EVERY a,b>=0. The actual tilted counts
  Z_n(t)=sum_a M(a,n-a)exp(t(2a-n)) have a rate
  P(t)=lim log Z_n(t)/n for every real t; P(t)>=P(0)=log lambda.
  Tape symmetry also gives Z_n(t)>=c_n for every n,t.
* The accepted current enclosure1.765224<lambda<1.834843. Only its
  easy consequence lambda>7/4 is used for the new rational constants.
  No old numerical certificate is replayed.

The compact baseline binds the exact complete accepted copies and their
authority records. B constructed the older G1--G5 packet and reviewed old
R7, MR, DG and other2019 inputs. Those roles do NOT independently
recertify their accepted premises or audit this NEW construction. Root
gave a broad research assignment, no NEW proof inference. Its separate
trace-recognition and short-joining notes are read as context only. No
NEW active peer-review material was opened. General finite-path walk
counting, phase normalization and elementary composition counting are
established methods; no priority claim is made.

## 2. Definitions and proposed results

For a binary word w, H_w(0)=0 and each0 adds1, each1 subtracts1.
Its range is max H_w-min H_w, including the initial height0. Heights
of a subword restart at0; translation does not change its range.
For X=(u,v) in R_n define L_r(X) as the largest length of a contiguous
subword of EITHER tape with height range<=r. At n=0 set L_r=0.
For n>=1 and 1<=ell<=n put

    A_(n,r)(ell)=#{X in R_n: L_r(X)>=ell}.

The event is equivalent to existence of a length-EXACTLY-ell tape
subword with range<=r. For ell>n its count is0. Only r=1,3 is used.
Write phi=(1+sqrt5)/2, alpha=20/21 and B_n=binom(n+3,3).

**CR1, exact confined-block estimate.** For every n>=1,1<=ell<=n,

 A_(n,3)(ell)
  <= [16phi/(1-sqrt3/lambda)] binom(n-ell+3,3)
                  phi^ell lambda^(n-ell)
  <= 2800 binom(n-ell+3,3) lambda^n alpha^ell.       (1)

This is a count of DISTINCT actual contexts. Neither independent random
walks nor histories are substituted for them.

**CR2, uniform-length consequences and an alternating endpoint.** Under
the uniform measure on R_n,

 Pr(L_3>=ell)<=min(1,2800 B_n alpha^ell),
 E L_3<=ceil(log(2800 B_n)/log(21/20))+20.           (2)

For r=1, which means alternating nonempty tape subwords,

 A_(n,1)(ell)<=42 binom(n-ell+3,3)lambda^(n-ell),
 E L_1<=ceil(log(42 B_n)/log lambda)+1/(lambda-1).   (3)

Both longest-piece expectations are O(log(n+1)). For every fixed
0<epsilon<=1, the contexts with L_3>=epsilon*n have upper root rate
at most lambda*alpha^epsilon<lambda. These assertions are about actual
uniform DISTINCT contexts, not uniform official outputs.

**CR3, actual tilted and random-length separation.** At fixed total n,
weight X by exp(t*(|u|-|v|))/Z_n(t). Then, for 0<epsilon<=1,

 Pr_(n,t)(L_3>=epsilon*n)
 <=min(1,2800 B_n exp[-n*(epsilon*log(21/20)-|t|)]).
                                                               (4)

For |t|<epsilon*log(21/20), deleting this bad class preserves the
EXACT actual pressure P(t). This is a window for a FIXED epsilon;
it does NOT establish differentiability or constancy of P at0.

Alternatively weight ALL finite actual contexts by z^N/C(z), where
z=R(1-eta),0<eta<1. At the empty context define L_3/N=0. Then

 Pr_z(L_3/N>=epsilon)
 <=2800*eta/(1-alpha^epsilon)^4 ->0.                (5)

This holds in EVERY accepted renewal regime, without selecting one.

**CR4, exact actual composition fibres.** For X=(u,v) in R_(n+m),
let k_n(X) count the indices i for which the tape prefixes of lengths
i,n-i form a phase0 context and the remaining suffixes form a phase-n
context. Both parts must be admitted; a height equality alone is not
enough. Equivalently these are the grid vertices on time layer n which
belong to SOME complete legal history of X. Then for EVERY n,m>=0,

    c_n*c_m=sum_(X in R_(n+m)) k_n(X),
    1<=k_n(X)<=min(n,m)+1.                         (6)

For balanced output bidegree(n,n), tape symmetry gives the exact identity

 sum_(X in R_(n,n)) k_n(X)=sum_(a=0)^n M(a,n-a)^2.  (7)

R_(n,n) here denotes the bidegree class, not total length n; this notation
is used only in(7) and the balanced consequence below. The fibres count
distinct input-context pairs, NOT numbers of full histories.

**CR5, the actual midpoint-cut mean and its limitation.** Under uniform
X in R_(2n), set a_n=E k_n(X). Then

    a_n=c_n^2/c_(2n)=s_n^2/s_(2n),
    a_0=a_1=1, a_(n+1)>a_n for all n>=1,
    sup a_n<infinity iff sup s_n<infinity.          (8)

Consequently the COMPLETE accepted scalar alternatives give:

* delta>0: a_n->1/(R delta);
* delta=0,mu<infinity: a_n~n/(2mu);
* delta=0,mu=infinity: a_n->infinity and a_n/n->0.

For uniform balanced bidegree(n,n), with mean denoted a_n^bal,

    a_n^bal>=s_n^2/(n+1),
    finite criticality implies liminf a_n^bal/n>=1/mu^2. (9)

Thus finite criticality would require a linear mean number of feasible
cuts, even while CR2 and CR3 forbid macroscopic bounded-range pieces
with positive limiting mass. There is presently no proved implication
from the former phenomenon to the latter. These exact fibre facts do
not by themselves determine the actual regime.

## 3. Proof of CR1: cut one canonical history, count actual pieces

Fix ell and an actual context in A_(n,3)(ell). Choose a deterministic
qualifying length-ell subword: first use the first tape if it has one,
and choose its leftmost such subword; otherwise do this on the second
tape. Use the UNIQUE canonical history of the whole context. In that
history cut immediately BEFORE the first selected tape letter and
immediately AFTER its last selected tape letter. The middle block
contains exactly ell letters of the selected tape and m>=0 letters of
the other tape. The prefix and suffix have p,q>=0 moves and

    p+m+q=n-ell.                                   (10)

The prefix is one of c_p actual contexts. The suffix starts at phase
p+ell+m, so complement BOTH its words if that phase is1. It is then one
of c_q actual phase0 contexts. The middle source starts at phase
sigma=p mod2. Given p,m,q, the selected side, the actual prefix, the
two middle words, and the normalized suffix, one recovers the original
pair by componentwise concatenation and undoing the specified suffix
complement. Hence this deterministic encoding is INJECTIVE. We need
not recover the selected history or prove that every counted triple
is attainable. Counting a larger set of triples is an upper bound.
There is no sum over the possible locations of a tape subword: its
location is already determined by the prefix. The sums over p,q are
kept explicitly below.

During the middle block, the selected tape's relative height lies in
an integer interval I=[b,b+3] containing0. Its true range may be less
than3; such a path is still contained in at least one of the four
intervals b=-3,-2,-1,0. Counting it in multiple intervals is harmless.
The middle source's relative height is0 at even times and e at odd
times, where e=(-1)^sigma. At EVERY history prefix,

    H_selected + H_other = source height in{0,e}.  (11)

Every prefix length of the other tape is reached at some history
time, so its entire walk lies in {0,e}-I, contained in a single integer
interval of width4, with FIVE levels. For e=1 that interval is
[-b-3,1-b]; for e=-1 it is[-b-4,-b]. Both contain0. No probabilistic
independence, arbitrary Fréchet theorem, or missing endpoint condition
is used in this elementary confinement argument.

Here are the required finite-path counts in full. Let T_s be adjacency
of the path on s integer levels, with no loops. If v is positive,
T_s v=rho*v and every coordinate of v is between1 and K, then entrywise

    T_s^j*1<=T_s^j*v=rho^j*v<=K*rho^j*1.          (12)

Thus from any FIXED starting level there are at most K*rho^j length-j
binary walks staying on that path. This includes j=0. It is only a
finite nonnegative-matrix identity, not an imported spectral theorem.

For FOUR levels, v=(1,phi,phi,1), rho=phi, K=phi;
the two interior equations are1+phi=phi^2. For FIVE levels,
v=(1,sqrt3,2,sqrt3,1), rho=sqrt3,K=2; the interior equations are
1+2=3 and2sqrt3=sqrt3*2. Consequently there are at most
4phi^(ell+1) selected-tape middle words, summing over the four I,
and at most2(sqrt3)^m other-tape middle words for each I and phase.
Summing over the two possible selected sides bounds the middle choices
by16phi*phi^ell*(sqrt3)^m. No floating-point eigenvalue is used.

The accepted s_j bound gives c_j<=(j+1)lambda^j for EVERY j>=0,
including j=0. Put N=n-ell>=0. For fixed m the sum over p+q=N-m is

 sum_(p+q=N-m)c_p*c_q
 <=lambda^(N-m)sum_(p+q=N-m)(p+1)(q+1)
 =lambda^(N-m)binom(N-m+3,3).                      (13)

The last identity follows, for example, by multiplying two geometric
derivatives sum_(j>=0)(j+1)x^j=(1-x)^(-2); it also follows by summing
the elementary quadratic in p. Combining the injective encoding,
(12), and(13), and enlarging the finite geometric sum,

 A_(n,3)(ell)
 <=16phi*phi^ell*lambda^N
       sum_(m=0)^N (sqrt3/lambda)^m binom(N-m+3,3)
 <=[16phi/(1-sqrt3/lambda)]phi^ell*lambda^N
                                  binom(N+3,3).  (14)

The denominator is positive because lambda>7/4>sqrt3. To obtain the
explicit rational version, use the EXACT elementary inequalities

    phi<5/3, sqrt3<26/15, lambda>7/4,
    sqrt3/lambda<104/105, phi/lambda<20/21.

The first two follow by squaring positive quantities: 5<49/9 and
3<676/225. Hence the prefactor in(14) is less than
16*(5/3)*105=2800. This proves all of(1). These rational comparisons
do not evaluate lambda or improve its accepted enclosure.

## 4. CR2: actual probabilities, logarithmic lengths, and range1

Because c_n>=lambda^n, division of(1) by c_n and replacement of
binom(n-ell+3,3) by B_n prove the probability bound in(2).
Let K=ceil(log(2800 B_n)/log(21/20)); then
2800 B_n alpha^K<=1. For a nonnegative integer-valued L,
E L=sum_(ell>=1)Pr(L>=ell), by summing its finite point masses.
Use1 for the first K terms and alpha^(ell-K) for the remaining terms.
The geometric tail is alpha/(1-alpha)=20. This proves(2), including
small n for which K>n, where the unused tail is an overestimate.

A nonempty binary word has range<=1 iff it alternates: after a step
reaches one endpoint of its two-level interval, the next step is forced
back. There are at most TWO such words of length ell. Each confines
the other tape in the same middle-block argument to THREE levels.
The path3 vector(1,sqrt2,1) has eigenvalue sqrt2, so(12) bounds the
other word count by sqrt2*(sqrt2)^m. Summing both selected sides now
gives middle factor4sqrt2*(sqrt2)^m, independently of ell. The same
convolution proves

 A_(n,1)(ell)
 <=[4sqrt2/(1-sqrt2/lambda)]binom(n-ell+3,3)lambda^(n-ell).

Since sqrt2<3/2 and lambda>7/4, sqrt2/lambda<6/7; the bracket is<42.
This proves(3)'s count. Divide by c_n>=lambda^n and sum the tail with
K=ceil(log(42 B_n)/log lambda). Its geometric remainder is
sum_(j>=1)lambda^(-j)=1/(lambda-1), proving the expectation claim.
Both n=0 expectations are0 by definition.

For fixed epsilon>0 take ell=ceil(epsilon*n). Every bad context is
counted in(1) and alpha^ell<=alpha^(epsilon*n). The polynomial B_n
has nth root tending to1, since log B_n=O(log(n+1)). Thus the bad
class has upper nth-root count at most lambda*alpha^epsilon<lambda.
There is no claim that its own limit exists.

## 5. CR3: weighted consequences without a regularity shortcut

For each total-n context, the tilt factor exp(t*(|u|-|v|)) is at most
exp(|t|n). Its bad weighted count is therefore at most

    2800 B_n lambda^n exp(|t|n)alpha^(epsilon*n).

The ACTUAL normalizer Z_n(t)>=c_n>=lambda^n. Dividing proves(4).
If |t|<epsilon*log(21/20), this probability tends to0 exponentially
up to a polynomial factor. The good weighted sum is then Z_n(t)
times1-o(1), so its logarithmic rate is the accepted P(t). This
proves the pressure-preservation claim. The allowable t window shrinks
with epsilon; no passage epsilon->0 uniformly in t was justified or
is asserted. Nor does an entropy gap for this one bad class describe
all possible macroscopic tape imbalances.

For the random-length measure put x=lambda*z=1-eta. Only n>=1 can
contribute to the event L_3/N>=epsilon because of the declared empty
convention. Its unnormalized mass is at most

 2800 sum_(n>=1)B_n*x^n*alpha^(epsilon*n)
 <=2800/(1-alpha^epsilon)^4.                       (15)

Here sum_(n>=0)binom(n+3,3)y^n=(1-y)^(-4) for0<=y<1; use x<=1.
Also C(z)=sum s_n*x^n>=sum x^n=1/eta. Division proves(5).
The bound may exceed1 away from the limit, in which case1 is a
valid additional bound. This is an ACTUAL uniform-in-regime estimate;
it does not use the finite-critical conditional angular law from G3.
Vanishing confined-piece fraction does NOT imply vanishing tape-length
imbalance, and the accepted critical angular alternatives are intact.

## 6. CR4: exact composition and balanced fibres

Fix n,m>=0. For X in R_n and Y in R_m, complement both words of Y
when n is odd, and concatenate corresponding tapes. Any legal history
of X followed by a legal history of this phase-adjusted Y witnesses
a context in R_(n+m). This defines a map from DISTINCT input pairs.
Conversely, split any legal full history at time n. Its tape prefixes
and suffixes give an input pair, so the map is surjective.

For a fixed output(u,v), an input determines i=|first input's first
tape|. Conversely, for each feasible i the prefixes u[0:i],v[0:n-i]
are fixed, and the suffixes are fixed. Undoing the known phase-n
complement uniquely recovers the second input. Feasibility of BOTH
parts is precisely the condition defining k_n. Concatenating witnesses
for those parts gives a full witness through that vertex. Conversely
a full witness through it proves both feasibility conditions. Thus the
fibre has exactly k_n elements, independent of how many histories each
input or output has. Summing finite fibres proves(6).

If a=|u| then feasible i must lie in

    max(0,a-m)<=i<=min(a,n).                       (16)

This integer interval has at most n+1 and at most m+1 elements. There
is at least one feasible cut by any full history. At n=0 or m=0 the
cut is unique, proving all empty cases explicitly. A height equality
H_u(i)+H_v(n-i)=0 or1 alone does not certify feasibility, since it
does not give legal prefix and suffix paths.

Restrict the output to |u|=|v|=n. If the first input has bidegree
(a,n-a), the second has bidegree(n-a,a). Complementation, if needed,
is a bijection onto the correct source phase. Thus the number of
input pairs with this a is M(a,n-a)M(n-a,a)=M(a,n-a)^2 by tape
symmetry. Summing the same exact fibres over balanced outputs proves(7).
It does not count compatible path pairs or assume a unique cut.

## 7. CR5: midpoint means, doubling, and the unselected alternatives

Use(6) with m=n and divide by c_(2n). This gives(8)'s exact mean.
The normalized version follows because lambda^(2n) cancels. At n=0,
k_0=1; at n=1, c_1=2,c_2=4, hence a_1=1. For n>=0,

    a_(n+1)/a_n=rho_(n+1)^2/[rho_(2n+1)rho_(2n+2)]. (17)

MR1 makes this at least1. For n>=1 it is strictly greater than1:
both denominator factors are at most rho_(n+1), and
rho_(2n+2)<rho_(2n+1)<=rho_(n+1), since2n+2>=4.
At n=0 the ratio is1 as stated.

If all s_n are bounded, a_n=s_n^2/s_(2n)<=s_n is bounded, because
s_(2n)>=s_n. Conversely suppose a_n<=M for all n; M>=1. Then

    s_(2n)>=s_n^2/M,
    s_(2^j n)>=M*(s_n/M)^(2^j) for every j>=0.     (18)

The second inequality follows by induction. The accepted bound
s_k<=k+1 gives, after taking logarithms in(18), dividing by2^j and
sending j to infinity at FIXED n>=1,

    log(s_n/M)<=0.

Thus s_n<=M for every n, proving the boundedness equivalence. There
is no interchange of an n-dependent M with this limit. If delta>0,
the accepted positive finite limit of s gives a_n->1/(R delta).
If finite criticality holds, substitution s_n~n/mu gives
a_n~n/(2mu). In the infinite-mean critical case s is unbounded;
the equivalence and monotonicity force a_n->infinity, whereas
a_n/n<=s_n/n->0. All three statements retain their exact hypotheses.

Finally, the balanced class is nonempty for every n: write the first
n source bits to one tape and the next n to the other. By(7) its mean
is sum_a M(a,n-a)^2/M(n,n). The elementary finite-sum inequality
(sum x_a)^2<=(n+1)sum x_a^2 and accepted capacity
M(n,n)<=lambda^(2n) imply(9). In the finite critical case, s_n~n/mu
then yields the displayed liminf after division by n. No uniform
fixed-bidegree asymptotic or equality of this bound is claimed.

## 8. The exact remaining geometric obstruction

These results do not select delta or mu. In particular they do NOT
prove that many feasible antidiagonal cuts imply a long confined
tape piece. Such an implication, even only strong enough to make
the actual mean cut count o(n), would exclude finite criticality
via(8), but is not supplied here. Positive defect versus infinite
critical mean would remain after that exclusion.

The accepted staircase pair(u_j,u_j) has exactly two full histories.
At time j(j+1), their first-tape positions differ by j when j is even
and j+1 when j is odd. To check this, before the central block of its
explicit history the elapsed time is j^2+1 and the excess R over L
is j+1; the next j-1 letters alternate starting L, subtracting1 just
when j-1 is odd. Side exchange gives the other position. Thus the
SPREAD of feasible cuts is unbounded although their NUMBER is2.

Moreover L_3(u_j,u_j)<=12 for all j. For j<=3 each tape has length
at most12. For j>=4 the only runs shorter than4 are the three runs
of lengths1,2,3 at each end. A range<=3 subword cannot contain a
complete run of length>=4. If it meets an end block, it contains at
most its six letters plus three letters from its adjacent long run,
hence has length<=9. Otherwise it meets at most two adjacent long
runs and has length<=6. These cases cover the two central equal long
runs and every truncated boundary. Thus a proposed bound of cut
SPREAD by a constant times the longest range3 piece is false. This
does NOT disprove a bound on cut NUMBER; none is currently proved.

Conversely, ((01)^m,(01)^m) has exactly m+1 feasible midpoint cuts
at time2m: the first-tape index must be even by bit counts; every
even index from0 to2m works by consuming alternating even pieces
successively in each part. These contexts have long range1 pieces
and very low multiplicity as distinct outputs. Many paths through
one such output cannot be counted as many outputs. In the even-block
subsystem, normalizing D^m A^m to A^m D^m via DA->AD requires m^2
swaps, despite just one initial boundary redex. Thus disjoint initial
redexes do not supply a one-pass collision bound.

The new entropy estimate rules out a macroscopic confined piece in
typical actual contexts, even under the critical conditional law.
It does not rule out many feasible cuts formed by more elaborate
unbounded-height matching. That is the concrete unresolved inference,
not a certificate size or a recognition running-time question.

The sources, actual read limits, unsuccessful routes, sixty whole
obligations and constructor reconstruction checks are separate frozen
companions. The metadata program verifies bytes and obligation labels
only; it contains no mathematical enumerator. No result is promoted
before TWO OTHER complete whole audits and coordinator acceptance.
