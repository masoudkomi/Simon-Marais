# AU1–AU4: independent ENTIRE WHOLE2 initial audit

2026-10-18 UTC. Reviewer A, `/root/review_2021_reasoning_j15_r2`.
This is an independent review recommendation, not coordinator promotion.
The reviewed submission remains **candidate proof - unverified** pending
the other entire audit and coordinator reconciliation. All 64 obligations
are reconstructed in the companion ledger. I find no substantive defect
or required author repair in the exact AU1–AU4 statements. Eight closed
scope notes are retained in the issue log.

## Identity, independence and scope

The target is `notes/reasoning-occupation-return-r1-candidate-v1.md`,
22022 bytes, SHA256
`4df238467e493c58e7eb82d0ed1d6b52e173ad9499e666862cfbfca2e37caa6e`.
Its entire twelve-file author packet is bound by `freeze-v1.json`,
4361 bytes, SHA256
`e4b6369f4733f2e418ecc43e24329b011aa538799f1afaeb9dcc667abfe75ee9`.
I read all twelve files, including all 64 obligations, the constructor's
checks, failed routes, issues, sources, worklog, administration code and
all metadata. Constructor checks were not treated as an independent
certificate. The mathematical reconstruction below is by hand; neither
author code, old certificates, mathematical programs nor scans were run.

B constructed the new AU argument. I did not contribute a new AU proof
inference. My earlier construction of the accepted R7/CN inputs and
earlier whole reviews of LO/CR/G/BT/AT are disclosed. Their accepted
authority is imported at the exact scopes in the source audit, rather
than newly independently recertified by their former author or reviewer.

I have seen no corresponding NEW root AU mathematical conclusion,
preliminary public status, report, ledger or substantive commentary.
I have not opened, inventoried or hashed any corresponding root AU
review file. There is one explicit administrative exception: root's
completion message supplied the manifest name and SHA256. Receipt of
that identity is acknowledged, not denied; it supplied no mathematical
disposition and was not a peer-file access, baseline premise or proof
input. Root also disclosed an earlier public preliminary status message;
I did not see that status. The source/log/metadata preserve this event
and the distinction. Findings remain embargoed until explicit confirmation
that both ENTIRE initial packets are complete.

The official target is only 2019 B4(b): distinct physical strings produced
from seed 1 by the alternating source rule. Histories are witnesses,
chronological pairs are marked outputs, and forgetting the mark has a
polynomial fibre bound. These are three different counting objects.
There is no preliminary-part proof, numerical improvement, actual regime
selection, exact growth value or annual conclusion in this review.

## Actual contexts and the imported interfaces

Let `R_N` be the distinct chronological tape pairs after N moves and
`c_N=|R_N|`, with one empty pair at N=0. The source begins 0,1,0,1.
If X has degree n, the first source bit for a following context is flipped
exactly when n is odd. Thus actual composition is

    X odot Y = X * bar^(n mod 2)Y,

where the complement acts on BOTH tapes. Each displayed factorization
below supplies actual schedules, not just height equalities. The physical
word associated to `(u,v)` is `reverse(u)1v`.

The operative R7 import is the common actual rate lambda, the every-N
bounds `lambda^N <= c_N <= (N+1)lambda^N`, consecutive-ratio convergence,
and the marked/unmarked fibre bound. CN supplies balanced nonempty
periods and actual phase-zero fast/slow schedules, including the even
boundary between the two copies of the slow right word. Operative CT
v1.2 §6 supplies removable endpoint pads and its actual same-time
midpoint vertices. AT supplies `V <= 2(N+2)O`; V is the UNION of vertices
on full schedules. BT supplies the definition of its two-sided residual
U. No claimed converse from a height-matching vertex to a full schedule
is needed.

## AU1: a two-coordinate grid inside the viable union

Fix an arbitrary real r>=0, and first choose an integer h>=2 with
`2h-1>r`. Put `t=2^h-1`; then t>=3 and t is 3 modulo 4. CN's periods
have lengths `a=4t`, `b=3t-1` and full ranges 2h and 2h-1. For `s=01`,

    p=2t,  d=(5t+1)/4=2t-b/4,
    u'=s^p u s^p,  v'=s^d v s^d.

Both padding exponents are positive integers, in fact at least t.
The resulting lengths are exactly 12t and 8t. The fast schedule starts
and ends with `LL` repeated p times followed by `RR` repeated d times.
For the slow schedule, insert an additional `RR` block of exponent 2d
at CN's even middle-v boundary. Its right tape is
`s^d v s^(2d) v s^d=(v')^2`; its left tape is u'. Every inserted or
removed block has even degree, so the phase remains zero. This explains
why removing the specified endpoint pads retains actual schedules.
Removing arbitrary balanced substrings would not be justified.

The fast and slow padded contexts F and S have degrees 20t and 28t.
Consequently `A=F^7` and `B=S^5` have equal degree 140t and tape lengths
`(84t,56t)` and `(60t,80t)`. They commute as output pairs because both
tapes are powers of the same respective periods. Their histories need
not commute. For every m>=1,

    Y_m=A^(10m)B^(14m)=(u'^(140m),v'^(210m)),
    N=|Y_m|=3360tm,
    Z_m=A^(5m)B^(7m),  |Z_m|=1680tm,

and both Y and Z are actual balanced contexts of even degree.

Choose any coarse indices `0<=r0<=10m`, `0<=s0<=14m`, omitting exactly
the two corners where one coarse side is empty. The prefix
`A^r0 B^s0` and suffix `A^(10m-r0)B^(14m-s0)` are actual, contain a
macro, and multiply to the same output Y. Their cut coordinates are

    (i,j)=(84tr0+60ts0, 56tr0+80ts0).

Delete the specified final pads of the prefix and initial pads of the
suffix. The remaining contexts C,D are actual even contexts and give
`Y=C*(s^(2p),s^(2d))*D`. For ANY independent integers
`-p<=e<=p`, `-d<=f<=d`, the middle can instead be produced as

    (s^(p+e),s^(d+f)) * (s^(p-e),s^(d-f)).

Each factor is actual: generate its left loops by LL and right loops
by RR. Zero exponents are allowed. Concatenating C, these factors, D
gives a FULL schedule through `(i+2e,j+2f)`. Thus the tape rectangle and
endpoint restrictions hold by construction. These shifts are independent;
one must not impose the old CT same-time restriction `f=-e` here.

For possible equality of two such vertices, the coordinate sum gives
`140t(Delta r0+Delta s0)=2Delta e+2Delta f`, with right magnitude at most
`4(p+d)=13t+1<140t`. Hence the coarse sums agree. The left coordinate
then gives `24t Delta r0=2Delta e`, with right magnitude at most `8t`.
It follows that both coarse indices agree, after which both fine indices
agree. This proves disjointness of the clusters, not disjointness of
histories. The number of coarse vertices is
`140m^2+24m-1>140m^2`; the fine size is
`(4t+1)(5t+3)/2>10t^2`. Therefore

    V(Y_m)>1400t^2m^2=N^2/8064.

The arithmetic is exact: `3360^2=11289600=8064*1400`. The estimates hold
already at m=1. No rectangular filling theorem or inference from an
individual layer is used.

The s-pads range over [0,1], contained in each CN period's height set.
Since the periods and pads are balanced, the padded full ranges remain
2h and 2h-1. Every l-letter cyclic factor of a balanced l-period visits
the entire period's prefix-height set, translated by its starting height.
Its range is consequently the full period range. A factor of length at
least l contains such a factor. Hence no factor of range at most r has
length 12t in the left tape, or 8t in the right tape. Both CT packing
and covered-position masses vanish for T>=12t. The quantifiers are
`for each r choose h, then for all m`; there is no single universal
period valid for all r. The density 1/8064, however, is independent of r.

## AU2–AU3: actual injections and the entropy conclusions

Fix h=2, so L=10080. For a>=0 let
`m=max(1,ceil(sqrt(a/kappa)/L))`, `ell=Lm`. Then
`sqrt(a/kappa)<=ell<=L+sqrt(a/kappa)`, with the a=0 endpoint handled
by the maximum with 1. For every N>=ell, write n=N-ell and append the
fixed Y block to each X in `R_n`, complementing BOTH block tapes when
n is odd. The result is actual and its last ell/2 letters on each tape
are known. Deleting them recovers X, regardless of X's bidegree. This
includes n=0. Every full Y schedule can follow a full X schedule, so
the full viable UNION of Y translates into the resulting pair. Its
area exceeds `kappa ell^2>=a`.

The injection therefore gives `|H_N(a)|>=c_(N-ell)`. Dividing by the
accepted all-N upper bound for c_N gives precisely
`Pr_uniform_R_N(V>=a)>=lambda^(-ell)/(N+1)`. The law is uniform on
DISTINCT outputs. If `a_N=o(N^2)`, then ell=o(N), so the required
N>=ell holds eventually, along ALL integer N. Squeezing by c_N proves
the count-root limit lambda; squeezing the probability by 1 proves its
N-th-root limit 1. No threshold monotonicity or uniform ratio theorem
is involved. At fixed `0<eta<kappa`,
`ell/N<=sqrt(eta/kappa)+L/N<1` eventually, yielding exactly the displayed
positive lower bound for the log count divided by N. This is compatible
with an eta-dependent exponential loss at fixed eta.

For AU3 set `a_N=2(N+2)d_N` when `d_N=o(N)`. AT's inequality has the
required direction: V>=a_N implies O>=d_N. This a_N is subquadratic,
so squeezing the larger occupation class gives its rate lambda. There
is no conclusion about its probability staying positive, O/N, or E[O].

For physical strings, every actual length-(N+1) word has exactly
`floor(N/2)+1` ones. A legal marked seed must be one of those positions,
so the mark-forgetting fibre is at most that number, even though some
positions need not be viable. The physical class is explicitly the
image admitting SOME legal seed with the statistic. Dividing the marked
lower count by this polynomial and bounding above by the full physical
count gives the same rate, with the official exponent 1/(N+1). No
canonical seed choice or intrinsic unmarked statistic is asserted.

## AU4: both-sided unconfined contacts and recovery of outputs

Now h=3, t=7, L=23520. The padded periods have ranges 6 and 5. Set
`H=Lm/2=1680tm`, with each Z tape of length H/2. For every T>=H put
n=T-H. For arbitrary `P,Q in R_n`, define actual inputs

    X=P * bar^(n mod2)Z,  Y=Z*Q.

Both have degree T; H is even. Deleting the fixed suffix of X and
prefix of Y recovers P,Q, including n=0. Thus there are exactly c_n^2
constructed input pairs. Since T and n have the same parity, composition
is exactly `P*bar^(n mod2)(Z^2*Q)`. In the middle `Y_m=Z^2`, the
distinguished cut is `(H/2,H/2)` and has global time T after the prefix P.
Operative CT §6 supplies more than `H/84=20tm` actual viable vertices
at that SAME time. This is the sole same-time contact import in AU4;
the independent shifts of AU1 do not by themselves prove it.

For a positive left displacement z from that cut, the two transferred
words are a right-tape suffix before the cut and a left-tape prefix
after it. For a negative displacement they are the left-tape suffix
and right-tape prefix. In either case both are inside the two middle
periodic tapes, since the compared local vertices lie in `[0,H]^2`
and have sum H. Their lengths are |z|. If |z|>=12t, each contains a
complete cyclic period of its own tape; both are nonconstant and have
range greater than 3, even after complementation. They are therefore
U-contacts in BT's actual two-sided definition. A merely long constant
word would not suffice.

There are at most 24t-1 integer positions with |z|<12t, including the
distinguished cut. Discarding those from more than 20tm displayed
vertices gives, safely, `U>20tm-24t`. The claim remains valid if this
lower bound is negative at a small m. Additional undisplayed contacts
can only help. This proves the first probability bound by dividing the
injective image by c_T^2. The all-N bounds yield
`lambda^(-Lm)/(T+1)^2`. For FIXED m, H is fixed and consecutive-ratio
convergence gives `c_(T-H)/c_T -> lambda^(-H)`; the corresponding lower
bound tends to `lambda^(-Lm)`. No assertion uniform in growing m is made.

For u>=0 choose `m=ceil((u+24t)/(20t))`, which is positive even at u=0.
Then `20tm-24t>=u` and

    Lm <= 3360t*((u+24t)/(20t)+1)=168u+7392t.

For `u_T=o(T)`, H=o(T), hence T>=H eventually. The all-N lower bound
has (2T)-th-root limit 1; c_(T-H)^2 has (2T)-th-root limit lambda.
The full independent-input space supplies the matching upper bounds.
This proves both limits in AU4(8), without an assertion of divergence
in probability.

Finally fix an output of the constructed composition and the integer
`a0=|P.left|` in `[0,n]`. Its initial split `(a0,n-a0)` recovers P.
Remove the known H middle letters on EACH tape; the remainder determines
Q after undoing the known n-parity complement. Thus a0 determines the
whole preimage pair, so at most n+1 such pairs yield the output. The
number of DISTINCT outputs is at least
`c_n^2/(n+1)>=lambda^(2T-Lm)/(n+1)`. Every one has k_T>u, since its
constructed input decomposition has U>u. The matching c_(2T) upper rate
gives AU4(9). This recovery argument is essential: independent-input
pushforward and uniform-output measures are not interchangeable.

## Remaining inference and adversarial limits

These lower bounds remain compatible with events whose probabilities
go to zero, and with every accepted renewal-regime alternative. They
exclude a fixed exponential gap for any prescribed subquadratic-area
or sublinear-residual threshold sequence; they do not give an upper
bound on all high-area outputs, a positive limiting mass at fixed
quadratic density, or an actual criticality theorem.

For N>=1, `V/N^2 <= (N+2)^2/(4N^2) <= 9/4`. Markov proves that a
vanishing normalized mean implies vanishing tails at every fixed positive
quadratic density. Conversely splitting this bounded variable at eta
gives `E[V]/N^2<=eta+(9/4)Pr(V>=eta N^2)`; take the limit then let eta
decrease. Thus the stated equivalence is valid, while its actual premise
is OPEN. If proved, it would rule out finite-critical positive quadratic
mean, but would leave positive defect and infinite-critical mean to
distinguish. The original `F(R)=2R-1` sign is retained.

BT's critical residual divergence is conditional on actual criticality.
An exp(-o(T)) lower event probability does not prove that condition or
the divergence. G's angular law concerns a random-length ensemble and
the interval `[-v0,v0]`, with unknown 0<v0<1. An elementary binomial
bidegree bound only controls endpoint cones; it gives no contradiction
to that law. The particular original-output linear grammar is ambiguous;
this does not prove that every grammar for the language is ambiguous.
The fresh primary source read confirms the unambiguity/derivation-weight
distinction, not a missing unambiguous presentation or a new mass bound.

I explicitly tested the empty prefix, N=ell, T=H, h=2, m=1, r=0,
a=0, u=0, zero fine-loop exponents, both signs of z, odd free prefixes,
different input bidegrees, nonmonotone threshold sequences and variable-m
ratio misuse. The displayed actual schedules/injections and the all-N
bounds handle them. No counterexample to AU1–AU4 was found. Any later
claim selecting a regime, proving a uniform positive mass, or finding
the exact lambda would need a further argument and fresh review.

## Documentation and handoff

The companion source audit records which inputs were freshly read in
full, which operative portions were freshly read, and which historical
reads or metadata bindings supply preservation only. The documentary
script checks 115 protected fingerprint occurrences across 114 unique
paths, without importing a corresponding NEW root AU review record.
It does not execute mathematics. Requested inherited settings are
gpt-6.1-sol/max; independent effective-setting readback is unavailable.
The latest own authoritative meter was 57% total used in the explicitly
authorized reset1792874445 window; the 90% total ceiling and reserve
remain in force. No Git, shared/old-byte edit, charge, contact, bypass,
mathematical computation or new cache mutation occurred.
