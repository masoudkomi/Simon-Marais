# Fixed tape ends and the collision law of independent actual inputs

2026-10-18 UTC. **Candidate proof - unverified.** Sole NEW constructor B,
/root/review_2022_complexity_r2. Requested inherited gpt-6.1-sol/max;
independent effective-setting readback unavailable. TWO OTHER initially
blind ENTIRE WHOLE audits, followed by coordinator reconciliation, are
required. This concerns **2019 B4(b) only**. No selected renewal regime,
exact growth value, new numerical enclosure, ordinary-output ratio,
annual solution, external validation or novelty is claimed.

The new unconditional estimate concerns a specified END of a tape, rather
than an arbitrary factor location. Its length tail has a constant uniform
in the total input length. It controls a whole class of feasible alternative
cuts under the law of two independent uniform DISTINCT actual inputs.
The unaccounted-for contacts are explicitly retained. If the actual renewal
kernel is critical, those remaining contacts must diverge in probability
under this input law; finite critical mean would force a linear scale.
This is an actual necessary restriction, not a proof that the restriction
fails or that positive defect holds.

## 1. Domain, exact accepted premises and roles

The official objects start with 1 and receive the mandated alternating
bits at either physical end. Only the requested asymptotic enumeration
in (b) is investigated. Use the accepted chronological normalization:
a history in L,R sends source bits 0,1,0,1,... onto two ordered tapes.
Let R_n be the set of DISTINCT resulting pairs (u,v) of total length n,
c_n its size, and c_0=1. The physical word is reverse(u)1v with the
initial seed retained as a mark. Neither histories nor unmarked physical
words are counted by c_n.

The COMPLETE operative CT copy is reviewed-reasoning-cut-transfer-r4-v1.2.md.
Its coordinator header corrects t0=010 to t0=10. The presentation erratum,
old acceptance MD/JSON, unchanged submitted body and both audit records
remain historically preserved. There is no changed mathematical premise.
CT1/CT2 control confined factors at arbitrary locations and their packed
mass at each fixed range. CT3 disproves the required deterministic
fixed-range high-cut cover; CT4 disproves a uniform fibre bound for the
specific separator (0,1). None proves a mean-cut or renewal regime.

The COMPLETE accepted R7, CR, CN and G bodies and current MD/JSON
authorities were read. Operative inputs used below are:

* R7B: for every j>=1, c_j/c_(j-1)>lambda. In particular, for
  0<=p<=n,

      c_p/c_n <= lambda^(p-n).                         (1)

  Equality is allowed when p=n. This direction is essential; it does
  not follow from submultiplicativity alone.
* R7/CR: with R=1/lambda, F the ACTUAL complete minimal-obstruction
  series, delta=2-F'(R)>=0, and mu=R^2 F''(R)/2 interpreted as an
  extended nonnegative series, put s_n=c_n R^n and

      A_n=c_n^2/c_(2n)=s_n^2/s_(2n).

  If delta>0 then A_n tends to 1/(R delta). If delta=0 then A_n tends
  to infinity. In the finite critical case delta=0, mu<infinity,

      A_n ~ n/(2mu).                                 (2)

  These are conditional alternatives, not a determination of delta.
* CR4: composing DISTINCT inputs of degrees n,m, with both words of
  the second input complemented when n is odd, maps onto R_(n+m).
  A fibre consists exactly of its feasible antidiagonal cut vertices:
  BOTH prefix and suffix must be actual. Its size k_n(Z) satisfies

      1<=k_n(Z)<=min(n,m)+1,
      sum_(Z in R_(n+m)) k_n(Z)=c_n c_m.              (3)

* The current accepted enclosure is 1.765224<lambda<1.834843. Only
  lambda>7/4 is used in the new explicit constants. No numerical
  certificate, author program or historical freezer is replayed.

The finite path-vector bounds used inside CR are reconstructed in Section3
below. CN and G are read as relevant frontier/obstruction context; no new
pressure hypothesis is taken from them. The original canonical-renewal
text was also read through its acceptance register. Its F(R)=2R-1 has
the MINUS sign.

B constructed the accepted G and CR packets and reviewed R7 and CT.
Those old roles are NOT fresh independent recertification of their accepted
premises and do not audit this new construction. Root supplied a broad
target and no NEW mathematical inference. B is excluded from both required
reviews of this packet. No corresponding NEW active peer-review content
or metadata was used.

## 2. Definitions and complete proposed results

Give each 0 height increment +1 and each 1 increment -1. The range of a
word includes its initial vertex and all its prefix vertices, restarting
at height zero. Complementing a word negates the heights, and hence
preserves its range and whether it is constant.

Fix ONE of the four tape ends: initial/terminal on the left/right tape.
For an integer ell>=1, an end-piece event requires the tape to have at
least ell letters and uses its first/last EXACTLY ell letters. If it has
fewer letters, the event is false. Let E_r(ell) say that this piece has
range at most r, and E_const(ell) that it is constant.

Write

    alpha=20/21, beta=4/7, M=112448,
    C = {nonempty binary w : range(w)<=3 OR w is constant}.  (4)

**BT1: uniform end tails.** Under uniform DISTINCT X in R_n, for EVERY
n>=0, ell>=1 and EACH specified tape end,

    Pr(E_3(ell)) <= min(1,1400 alpha^ell),
    Pr(E_1(ell)) <= min(1,21 beta^ell),
    Pr(E_const(ell)) <= min(1,84 beta^ell).           (5)

The last assertion is not a fixed-range estimate: a constant word can
have arbitrarily large height range. For membership in C, the valid
upper bound is 1400 alpha^ell+84 beta^ell, optionally capped at 1.
The constants in (5) are independent of n and of the chosen end.

Now choose X in R_n and Y in R_m independently and uniformly. Let
Y' be Y with both words complemented when n is odd, and put

    Z=X*Y', i0=length(X.left), k=k_n(Z).

There is a distinguished feasible cut i0, supplied by these ACTUAL
inputs. For a different feasible cut j, set d=j-i0. If d>0, the two
transferred words are the last d letters of X.right and the first d
letters of Y'.left. If d<0, use the last -d letters of X.left and the
first -d letters of Y'.right. These words exist for every feasible j.
Let J count the alternative feasible j for which AT LEAST ONE of these
two transferred words belongs to C. Define

    U=k-1-J.                                         (6)

Thus U is a nonnegative integer. Every contact it counts transfers
two NONCONSTANT words, BOTH of range strictly greater than 3.
J and U depend on the distinguished input cut, not merely on Z.

**BT2: a uniformly integrable class of input collisions.** For every
n,m>=0 and integer D>=0, under this independent-input law P_x,

    E_x J <= M,
    Pr_x(J>2D) <= min(1,M alpha^D).                  (7)

In fact, if z>1 and z^2 alpha<1, then

    E_x z^J <= 1+M(z-1)(1+z)/(1-z^2 alpha).          (8)

If only range<=1 pieces are used in the definition of J, (7)--(8)
hold with (M,alpha)=(112,beta). For range<=3 alone the pair is
(112000,alpha). The union in (4) gives the displayed M=112448.

**BT3: exact input bias and a necessary critical collision law.** Put

    A_(n,m)=c_n c_m/c_(n+m).                         (9)

For all n,m>=0 the composed output has the k-size-biased uniform-output
law, and

    E_x(1/k)=1/A_(n,m),       E_x k>=A_(n,m).         (10)

Consequently, for integers L,D>=0,

    Pr_x(U<=L)
      <= min(1,(L+2D+1)/A_(n,m)+M alpha^D),          (11)
    E_x U >= A_(n,m)-1-M.                          (12)

For n=m and delta=0, U tends to infinity in probability. Still under
these hypotheses, for ANY integer sequence L_n>=0 with L_n=o(A_n),

    Pr_x(U<=L_n) ->0.                              (13)

In the finite critical alternative delta=0, mu<infinity, for every
epsilon>=0,

    limsup_(n->infinity) Pr_x(U<=floor(epsilon*n))
       <=min(1,2mu*epsilon).                       (14)

These assertions concern TWO independent uniform actual inputs, or their
size-biased composed output with its distinguished cut. They do NOT
replace the uniform law on R_(2n), evaluate mu or exclude criticality.

**BT4: a precise end-guard obstruction inherited from CT4.** For every
fixed integer w>=0 and every N>=2w+5, the separator map

    (X,Z) -> X*(0,1)*Z,
    R_(2N) x R_(2N-2) -> R_(4N)

has a fibre containing at least N-2w-3 input pairs such that:
all FOUR input tapes are alternating; and the first/last w letters of
each tape are independent of the chosen pair. Thus supplementing this
particular separator by these bounded end windows and a maximum-run-one
guard does not produce a size-independent fibre bound. This is a
CT4-derived negative corollary, not a new fixed-generator discovery.
Only the displayed subfamily's rarity is asserted in Section6.

## 3. BT1: a single-ended actual-witness injection

Choose the lexicographically least full legal history for each X in R_n,
with L<R. This is just a deterministic witness; no efficient algorithm
or independent history count is assumed.

First consider a TERMINAL piece of length ell on a specified tape.
Cut the witness immediately BEFORE the first selected letter of that
piece. The remainder runs to the end of the entire history. It contains
exactly ell selected-tape letters and some m>=0 other-tape letters.
The prefix has p=n-ell-m moves. For fixed m, record:

    the actual prefix context of degree p;
    the selected word of length ell;
    the other middle word of length m.

Concatenating the respective words recovers X. The prefix fixes the
location on each tape; m fixes p and the phase p mod2. Our deterministic
choice is therefore an injection into these data. There is NO extra
choice of a location or an unchanged suffix, and no sum over histories.
Only 0<=m<=n-ell can occur.

For an INITIAL piece, instead cut just AFTER its last selected letter.
Use the complete history up to that cut as the middle. The remaining
suffix has q=n-ell-m moves and starts at phase (ell+m) mod2.
Complement BOTH suffix words if necessary; the normalized suffix is one
of c_q actual contexts. Recording the two middle words and normalized
suffix again recovers X, including the known phase. Other-tape moves
before the first selected letter or after the last selected letter
are included in the chosen middle. They are not silently discarded.
This handles either tape and all four ends.

For any of these middle blocks, the relative source height at each time
is in {0,e}, where e is +1 or -1 according to its starting phase. The
two relative tape heights add to that value. If the selected word has
range<=3, it lies in one of the FOUR intervals [b,b+3] containing zero,
b=-3,-2,-1,0. The entire other word lies in an interval of width 4.
Every other-tape prefix is attained at a history time, including during
pauses on the selected tape, so this confines ALL its vertices.

Here are the required word counts, without numerical eigenvalues.
For adjacency T_s of the path on s levels, if a positive vector v obeys
T_s v=rho v and 1<=v_i<=K0, then

    T_s^j 1 <= T_s^j v =rho^j v <=K0 rho^j 1.       (15)

This is a direct entrywise inequality from nonnegative matrix entries.
For FOUR levels take v=(1,phi,phi,1), rho=phi,
phi=(1+sqrt5)/2. For FIVE levels take
v=(1,sqrt3,2,sqrt3,1), rho=sqrt3. Direct multiplication verifies both.
Thus the selected words have at most 4phi*phi^ell possibilities and,
for each selected interval and known phase, the other word has at most
2(sqrt3)^m possibilities. Their joint upper bound is

    8phi*phi^ell*(sqrt3)^m.                        (16)

Counting unattainable pairs only enlarges this bound. The witness
encoding and (1), with either c_p or c_q, now give

    Pr(E_3(ell))
      <=8phi*(phi/lambda)^ell
           sum_(m=0)^(n-ell)(sqrt3/lambda)^m
      <= [8phi/(1-sqrt3/lambda)](phi/lambda)^ell.    (17)

The elementary strict inequalities phi<5/3, sqrt3<26/15 and lambda>7/4
give sqrt3/lambda<104/105 and phi/lambda<20/21. The bracket in (17)
is less than 8*(5/3)*105=1400. This proves the first line of (5).
If ell>n the event is empty, so no negative upper sum is interpreted.

For range<=1, a nonempty word alternates, with at most TWO choices.
Its other middle word is confined to THREE levels. The vector
(1,sqrt2,1) gives eigenvalue sqrt2 and maximum coordinate sqrt2.
The same one-ended injection yields

    Pr(E_1(ell))
      <= [2sqrt2/(1-sqrt2/lambda)]lambda^(-ell).

Since sqrt2<3/2 and lambda>7/4, its bracket is less than 21,
and lambda^(-ell)<beta^ell. This proves the second line of (5).

For a constant selected word b^ell, EVERY complementary source bit
1-b in the middle must go to the other tape. Therefore two consecutive
letters b cannot appear in that other word: a complementary source
letter between them could not have been sent to the selected tape.
This holds at either starting phase and permits empty other middles.
Let a_m count binary length-m words avoiding bb. It has a_0=1,a_1=2
and a_m=a_(m-1)+a_(m-2). Induction using phi^2=phi+1 proves
a_m<=2phi^m. Summing over both possible b and applying the SAME
witness encoding gives

    Pr(E_const(ell))
      <=[4/(1-phi/lambda)]lambda^(-ell)
      <84 beta^ell.                                (18)

This is a bound for selected constant words, not a claim that arbitrary
binary middle words have Fibonacci growth.

All three proofs sum c_p/c_n or c_q/c_n using (1), rather than replacing
c_p by (p+1)lambda^p and losing an n-dependent factor. No translation
from arbitrary-location CT bounds or interchange of ranges is used.

## 4. BT2: sum the actual transferred contacts

For d>0 an alternative cut shifts exactly d letters from the END of
X.right to the second input, and d letters from the BEGINNING of
Y'.left into the first. If the tape bounds do not permit either piece,
there is no such cut. For d<0 the analogous statement uses X.left
and Y'.right. Prefix/suffix actualness is still required to count it.

For a fixed positive distance d there is at most one candidate cut in
each direction. Drop its feasibility condition solely for an UPPER
bound. BT1 and a union bound over the two transferred pieces and two
directions give

    Pr_x(some counted contact at distance d)
      <=5600 alpha^d+336 beta^d.                  (19)

The same bound applies to the EXPECTED number at that distance, by
summing the two indicator probabilities separately. There is no need
to assume the two end events independent. The independent input law
gives the required uniform marginal on each input, and complementation
of Y preserves the tested properties.

Sum (19) over d>=1. The geometric sums are alpha/(1-alpha)=20 and
beta/(1-beta)=4/3. Hence

    E_x J <=5600*20+336*(4/3)=112448=M.

Among distances 1,...,D there are at most 2D candidate vertices.
If J>2D, some counted contact has distance at least D+1. Summing
(19) over that tail proves

    Pr_x(J>2D)
      <=112000 alpha^D+448 beta^D <=M alpha^D,

because 0<beta<alpha<1. This includes D=0; capping at 1 is harmless.
With range<=3 alone omit the beta term. With range<=1 alone the
fixed-distance indicator sum is at most 84 beta^d, giving M=112.

For completeness, a nonnegative integer J and real z>1 satisfy the
finite identity

    E z^J=1+(z-1)sum_(j>=0) z^j Pr(J>j).

Use Pr(J>j)<=M alpha^floor(j/2), group even and odd j, and sum the
geometric series when z^2 alpha<1. This proves (8). Although J is
finite at each n,m, this last infinite upper bound is uniform in them.
It proves bounded exponential moments for this SPECIFIED collision class,
not for k or U.

## 5. BT3: the bias cannot be discarded

Under uniform independent inputs every element of R_n x R_m has
probability 1/(c_n c_m). Exactly k_n(Z) input pairs produce a fixed Z.
Consequently

    Pr_x(composed output=Z)=k_n(Z)/(c_n c_m)
      =[k_n(Z)/A_(n,m)]*(1/c_(n+m)).                (20)

This is precisely size bias by the positive finite variable k under
the UNIFORM output law; the terminology and general definition are
classical. Here the identity is proved directly on a finite set.
It is not valid to regard the composed output as uniform.
Conditional on Z, each of its k feasible cut vertices is the distinguished
one with probability 1/k, by the same bijection of cuts with input pairs.

Multiplying (20) by 1/k and summing proves (10)'s harmonic identity.
Also, with expectation E_o under uniform outputs,

    E_x k=E_o(k^2)/A_(n,m) >=(E_o k)^2/A_(n,m)
         =A_(n,m),

where the finite variance is nonnegative and E_o k=A_(n,m) by (3).
In particular 1<=A_(n,m)<=min(n,m)+1.

For any real t>=0,

    Pr_x(k<=t) <=t E_x(1/k)=t/A_(n,m).              (21)

Indeed, on k<=t its indicator is at most t/k; outside that event
the indicator is zero. This elementary bound does not assert an
unbiased or independent choice of a feasible cut from the output.

On {U<=L,J<=2D}, (6) gives k<=L+2D+1. Apply (21), then BT2 to
the excluded event J>2D. This proves (11). Taking expectations in
U=k-1-J and using (7),(10) proves (12).

For the midpoint set A_n=A_(n,n). If delta=0, the accepted CR5
alternative gives A_n->infinity. If L_n=o(A_n), choose, for example,
D_n=floor(sqrt(A_n)). Then D_n->infinity, D_n/A_n->0 and the
right side of (11) tends to zero. This proves (13), including every
fixed L_n=L. No n-scale conclusion follows for infinite critical mean.

If delta=0 and mu<infinity, use (2), L_n=floor(epsilon*n) and
D_n=floor(sqrt(n)) in (11). The first term tends to 2mu*epsilon
and the second tends to zero. The probability is at most 1, proving
(14), also at epsilon=0. In particular every deterministic L_n=o(n)
has Pr_x(U<=L_n)->0, but no positive uniform lower bound on U/n
almost surely or on EVERY input is claimed.

A bound on E_x U UNIFORM in n would, by (12), force bounded A_n
and hence delta>0. Such a bound is NOT proved. Nor is the converse:
bounded A_n under uniform outputs by itself does not bound higher
moments under its size-biased law. This distinction is essential to
the remaining argument, not an auxiliary hypothesis silently supplied.

## 6. BT4: all short end observations can still coincide

This section uses only the actual CT4 construction and spells out the
additional end-window restriction. Put s=01 and t0=10. For every
integer r>=1 and s0>=0 the phase-zero history

    (LL)^(r-1) L R^(2s0) L

produces (s^r,t0^s0); the endpoint s0=0 is allowed. Start instead with
the actual even history RL, producing (1,0), and then such a schedule
to get the second input below. For 1<=a<=N-2 set

    X_a=(s^a,t0^(N-a)),
    Z_a=(1 s^(N-a-1),0 t0^(a-1)).

They are actual of degrees 2N and 2N-2. Their two histories are even,
and the actual separator (0,1) has history LR. Direct word multiplication
gives, for EVERY a,

    X_a*(0,1)*Z_a=(s^N,t0^N).                       (22)

Restrict w+2<=a<=N-w-2, an interval with N-2w-3 integers. All four
tapes then have length at least 2w+3. They alternate and have respective
fixed first/last bits (0,1), (1,0), (1,1), (0,0). Thus their first and
last w letters are each independent of a, including the empty w=0
windows. The X_a are distinct because their first tape lengths 2a are
different. This proves the asserted fibre size EVEN WITH that supplied
end information and maximum run one.

The probability of belonging to this PARTICULAR subfamily under uniform
independent R_(2N) x R_(2N-2) inputs is at most

    (N-2w-3)lambda^(-(4N-2)),

by the accepted c_j>=lambda^j. It tends to zero for fixed w. This
bound is not a bound on the ENTIRE fibre of (22), all separator fibres,
all alternating inputs, or all high-cut outputs.

## 7. What the new result leaves unresolved

CT's arbitrary-location estimates and the new specified-end estimates
operate under different laws and quantifiers. Here the specified end
and one surviving actual prefix/suffix allow a geometric sum with no
polynomial total-length loss. The consequent J estimate covers ALL
feasible alternative cuts touching one tested boundary class, not just
one chosen periodic flat. It is valid uniformly in both input degrees,
at odd source phases, and when a tape or an entire input is empty.

Its complement U remains actual and uncontrolled. Criticality would
require almost all independent input pairs to have arbitrarily many
alternative cuts transferring two nonconstant words of range>3; finite
critical mean imposes the sharper small-quantile restriction (14).
Neither requirement has been disproved. No proof bounds these contacts
by fixed-range detectors, short periods, ordinary run lengths, a finite
signature, or a uniformly decodable short separator. BT4 explains why
some natural end-guard versions of the latter inference fail.

Range>=4 end words are not covered by the same path-vector geometric
sum: increasing the other word's allowed finite path can remove its
strict growth separation from the actual lambda. No all-range boundary
theorem, uniform adaptive range estimate or new pressure regularity is
claimed. The explicit constants are not optimized.

Uniform official unmarked outputs, uniform marked outputs, independent
input pairs, and their size-biased composed output remain distinct.
An exponential rarity assertion for histories or independent raw walks
would not prove the statements above. The actual F, delta, mu, the
unconfined contact law, exact lambda, original consecutive ratios and
the full annual answer remain open. Sources/read scopes, failed routes,
all56 whole obligations and immutable preservation references accompany
this hand proof. No mathematical program, scan, CAS, routine test,
certificate/source/author executable or old freezer was run.
