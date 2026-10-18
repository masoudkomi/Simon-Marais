# Entire initially blind OTHER whole R2: Q1--Q8, v3

2026-10-18 UTC. Reviewer `/root/review_2017_coarsening_r1` (C).
Requested inherited gpt-6.1-sol/max; independently verified effective
settings are unavailable. This is an independent review, not coordinator
promotion. The submission remains **candidate proof - unverified** until
the coordinator reconciles both OTHER whole audits.

The entire target is
`notes/reasoning-complexity-return-r9-candidate-v3.md`, 44042 bytes,
SHA256 `77bf84340543589d96698a64df5e3850cdf22fe953ee45587ab0d79997184ff5`.
Its complete v2 and v1 proof appendices, all 100 obligations, all three
versions' source/failure/worklog records, v2 working draft, and frozen
metadata were included. I reconstructed the whole argument, rather than
treating the author's earlier claims or my old narrower review as proofs.
The administrative validation independently checks both literal main and
obligation suffix inclusions and all declared target artifacts. It does
not evaluate a mathematical formula or rerun an author program.

**Verdict:** no substantive defect identified in the exact Q1--Q8 partial
scope. No repair or advisory is requested. The ledger covers QO01--48,
QV201--232 and QW301--320 individually. In particular the orphan table is
an exact ordinary-integer classification; its two deletions are necessary
and correct. Q8 is an unbounded seed equivalence, not a termination result.

## Independence, scope and actual inputs

I did not construct Q1--Q8. I previously constructed old 2022 R4/R7/R8
material and reviewed other older packets, including the complete Q1--Q4
v1 submission. Those roles are disclosed; this does not count as an
independent recertification of my own older results. Their unresolved
ordinary/profinite and differently scaled fiber boundaries are respected,
but no theorem from those packets is needed here. The only operative old
mathematical context is the attributed eventual strip-entry statement.

No NEW A v3 review report, finding, ledger, source record, code or metadata
was opened or hashed before this entire initial freeze. The root's notice
that both OLD v1 audits were frozen permits release of that narrower
review, not access to a NEW v3 audit. Neither peer conclusions nor the
author's self-check outcomes supply an inference below. Root supplied the
generic review assignment and no new mathematical inference.

The official starts are positive ordinary integers, initial product at
least 600, simultaneous updates

    F(a,b) = (a + 2 floor(b/20), b + 3 floor(a/30)),

and a hit is equality at any nonnegative time, including zero. For the
inverse classification only, F is extended to Z^2 using Euclidean floors.
No negative or profinite point is silently used as an official start.
The established eventual entry into I = [-13,23] intersect Z is attributed
preliminary context only. Its proof is neither reproduced nor investigated.
Forward positivity and product preservation follow directly from the
nonnegative floor increments on positive inputs.

## Q1: every ordinary inverse fiber

Write uniquely a=30l+r, b=20k+s, with 0<=r<=29, 0<=s<=19. Then

    F(a,b) = k(2,20) + l(30,3) + (r,s).

For v=(2,20), w=(30,3), independently multiplying the four claimed
identities gives

    -3v+20w=(594,0),      2v-13w=(-386,1),
    13(594,0)+20(-386,1)=v,
     2(594,0)+ 3(-386,1)=w.

Thus L=Zv+Zw is exactly the kernel of Gamma(A,B)=A+386B mod594:
if Gamma=0, (A,B)=m(594,0)+B(-386,1). The A coefficient makes Gamma
onto, so there are exactly 594 classes. The determinant -594 also gives
uniqueness of k,l for each fixed digit pair.

If two digit pairs differ by hv+jw, inversion gives

    h=(30 ds-3 dr)/594,   j=(20 dr-2 ds)/594.

The digit bounds give |h|<=657/594<2 and |j|<=618/594<2. The four axial
nonzero choices violate |ds|<=19 or |dr|<=29, the two same-sign choices
give (|dr|,|ds|)=(32,23), and zero gives no distinct pair. The remaining
two choices give precisely +/- (28,-17). Therefore exactly the six
disjoint pairs (r,s),(r+28,s-17), r=0,1 and s=17,18,19, coincide.
Three in a class are impossible: all nonzero first-coordinate differences
would be +/-28, whereas three distinct first coordinates would require
a difference 56. Conversely (28,-17)=-v+w is in L.

The 600 digit pairs consequently meet 594 classes, all classes. For any
ordinary output the appropriate digit pair leaves an element of L, and
the actual integer k,l give a genuine preimage. This proves onto and the
one/two fiber assertion on all Z^2, including negative inputs. The six
double output Gamma classes are 28,29,206,207,414,415: the three values
386s mod594 are 28,414,206 and r adds zero or one.

The first digit rectangle R_L has r=0,1 and s=17,18,19. Its partner
has k'=k+1, l'=l-1, r'=r+28, s'=s-17, hence actual coordinates
(a-2,b+3). The reverse rectangle R_H has r=28,29 and s=0,1,2 and
partner (a+2,b-3). There are no other doubles. The two differences are
separated by 5 and their sums by 1. This is an exact fiber theorem,
not a statement about distinct asymptotic values or future mergers.

Solving the actual equations 10A=10a+b-s, 10B=a+10b-r gives

    99a=100A-10B-r+10s,
    99b=100B-10A-s+10r.

The claimed a interval has width 219/99=73/33<3, so at most three
integer candidates. Setting b=B-3 floor(a/30) and checking the first
forward equation recovers the entire fiber. This theoretical recovery
was not executed in this review.

## Q2--Q4: diagonal ancestry, positivity and the old seed reduction

A diagonal input has r=s mod10. That is incompatible with either double
rectangle, so its full ordinary fiber at F(t,t) is the singleton (t,t),
for every t in Z. Combined with onto this proves both inclusions of

    F(Z^2 minus Delta) = Z^2 minus F(Delta).

It does not make Delta or its complement forward invariant. In particular
being an off-diagonal START in F(Delta) does not decide its future.

Write t=60k+u, 0<=u<=59. The full image classification is

| u | F(t,t) | Difference |
|---|---|---|
| 0..19 | (66k+u,66k+u) | 0 |
| 20..29 | (66k+u+2,66k+u) | 2 |
| 30..39 | (66k+u+2,66k+u+3) | -1 |
| 40..59 | (66k+u+4,66k+u+3) | 1 |

The 10+10+20 off-diagonal rays are distinct: B residues within each
difference row differ, and the rows have different differences. A positive
output forces t>0, since for t<=0 both output coordinates are <=t; then
k>=0. The official product filter belongs on the output, not an asserted
bound on every possible diagonal parent. In particular
(66k+22,66k+20), k>=1, is a legal difference-2 start whose ONLY ordinary
parent is (60k+20,60k+20). It refutes universal off-diagonal inverse
descent, not universal future hitting.

For B>=36 and D=A-B in I, the inverse identities give independently

    a >= (90B+100D-29)/99 >=1911/99>19,
    b >= (90B-10D-19)/99 >=2991/99>30.

The worst D values are -13 and 23 respectively; they need not occur
together. Integrality yields a>=20, b>=31 and ab>=620 for EVERY ordinary
parent. Nonnegative floors then give a<=A, b<=B and A-a>=2. Existence
comes from Q1 and cannot be inferred from real matrix inversion alone.

Subtracting the inverse equations gives exactly

    10D=9d+r-s,
    ceil((10D-29)/9)<=d<=floor((10D+19)/9), d=a-b.

At -9<=D<=19 these bounds give -13<=d<=23: the extremal rounded values
are ceil(-119/9)=-13 and floor(209/9)=23. Outside F(Delta), all ordinary
parents are off-diagonal by Q2. A hypothetical surviving output therefore
pulls back to an actual official, inside-strip survivor with smaller sum;
time zero is checked, rather than forgotten. All these conditions matter.
For k>=1 the exact legal family

    X=(60k+30,60k+4), F(X)=(66k+30,66k+7)

has d=26 outside I, output D=23 inside I, and a UNIQUE parent because
the input residues (0,4) avoid both rectangles. Neither member's future
is asserted to avoid or hit the diagonal.

Q4 follows by ordinary well-ordering. If a survivor exists, eventual
entry supplies a survivor already in I. Choose one of least positive
sum. Unless B<=35, D is one of eight outer offsets, or the point is an
off-diagonal diagonal image, Q3 gives a smaller official inside survivor.
Thus universal hitting is equivalent to hitting the displayed Bset.
The finite patch has B<=35, A<=58 with all official filters. The eight
outer offsets and forty congruence rays remain unbounded. This proves
neither a finite decision procedure nor existence of a survivor.

## Q5--Q6: the rank and every useful merger orientation

The centers (c_0,...,c_4)=(0,-4,-3,-2,4) are congruent to their indices
mod5. Thus h(d)=|d-c_(d mod5)|/5 is a nonnegative integer for all
integers d. Phi(a,b)=a+b+2h(a-b) is a positive integer on official starts.
The optional bound h<=5 on I is correct: the residue-specific maximal
center distances are 20,25,25,25,15, all at most25. The centers' overall
spread is 8, not 4.

For |d-D|<=4, the reverse triangle inequality and center spread give
|h(d)-h(D)|<=12/5; since both heights are integers, it is <=2. At a
central Q3 output, d-D=(D-r+s)/9 lies in [-38/9,38/9], and integrality
gives |d-D|<=4. If B>=43, an inside parent cannot have a<=29: in that
case floor(a/30)=0 gives b=B and d<=29-43=-14, outside I. Therefore
a>=30 and b>=31 imply actual sum drop at least 3+2=5. Twice the height
increase is at most 4, giving Phi(parent)<=Phi(output)-1.

The raised cutoff is material. At (25,36)->(27,36), the respective
heights are 3 and 1, potentials 67 and 65; at (29,40)->(33,40) they
are 3 and 1 with potentials both 75. These legal central-output examples
block a silent strict-rank assertion at the old cutoff36. Phi is not
claimed monotone along every original forward step.

A critical point means one of the eight outer differences or a birth
with difference -1,1,2. An R_L input has D mod10 in {1,2,3,4}; R_H has
D mod10 in {6,7,8,9}. Intersecting with all eleven critical differences
leaves precisely the following actual partners and height changes:

| Input rectangle and D | Partner difference | h before to after | Sum change | Phi change |
|---|---|---|---|---|
| R_L, 1,2 | -4,-3 | 1 to0 | +1 | -1 |
| R_L, 21,22,23 | 16,17,18 | 5 to4 | +1 | -1 |
| R_H, -13,-12 | -8,-7 | 2 to1 | -1 | -3 |
| R_H, -11 | -6 | 3 to2 | -1 | -3 |
| R_H, -1 | 4 | 1 to0 | -1 | -3 |

There is no critical double of D20 or D-10. Every listed partner
difference stays in I and avoids zero. A>=30,B>=43 give partner lower
bounds (28,46) or (32,40), products 1288 or1280, so all are official.
They share the SAME next output. Hence an actual survivor transfers to
an off-diagonal official inside survivor with strictly smaller Phi,
even though one orientation raises the sum.

The family Y_j=(660j+239,660j+240), Z_j=(660j+241,660j+237), j>=0,
checks both directions of the distinction. Its sole predecessor at Y_j
is the diagonal (600j+219,600j+219), but F(Y_j)=F(Z_j)=
(726j+263,726j+261) and Phi(Z_j)=Phi(Y_j)-3. The exact floor quotients
at Y_j are 33j+12 and22j+7, and those at Z_j are33j+11 and22j+8.
No future assertion is needed. In contrast every D2 point in R_L
has B=60m+58 or60m+59 and A=B+2; the two exact updates are
(66m+64,66m+64) and(66m+65,66m+65). Positive official inputs force
m>=0, while the product filter remains in place. This is a genuine
one-step hitting subfamily, not a proof about every birth ray.

Define Sstar exactly as official off-diagonal strip starts with either
B<=42, or B>=43, critical, and outside BOTH rectangles. The latter says
F^-1(F(Y))={Y}, not F^-1(Y) singleton or absence of later mergers.
The finite patch has A<=65,B<=42. A least-Phi official strip survivor
must belong to Sstar: outside the critical set there is a smaller
central parent, and a critical double input has a smaller merger partner.
This proves both directions of Q6. Iterating selected legal survivor
moves terminates finitely, although the moves need not be one backward
trajectory. No inverse limit is invoked. Sstar remains unbounded;
for example (660j+682,660j+680) has a unique diagonal parent and no
next-output partner. The outer offsets20 and-10 also never double.

## Q7: full-strip available-parent rank and the exact orphan iff

For ALL D in I the numerator D-r+s lies in[-42,42]. Thus any ordinary
parent still satisfies |d-D|<=4. If it is inside I and B>=43, the same
a>=30 argument and sum/height calculation give a strict Phi decrease.
This proves a conditional statement about available inside parents,
not existence of one. If the output is not a birth, Q2 guarantees
off-diagonal parents. At a birth its unique diagonal parent cannot
transfer survival because it has hit at time zero.

For an orphan relative to I, all parents are outside I but Q1 supplies
at least one ordinary parent. The inverse bounds over full I give
-17<=d<=27, so outside values are K={-17,-16,-15,-14,24,25,26,27}.
The two parents of a double differ by5. No two elements in either length-4
component of K differ by5, and elements in different components differ
by at least38. Consequently every orphan has exactly ONE ordinary parent,
which is official by the earlier B>=36 positivity estimate. Central
outputs have no outside parent, leaving precisely the eight outer D.

For fixed proposed outside d and output D, set u=d-D, delta=10D-9d,
e=u mod2 in{0,1}. The full input equations, not just a congruence, are

    r=s+delta, 3l-2k=u,
    l=2z+e, k=3z+(3e-u)/2,
    B=66z+33e-10u+s,
    max(0,-delta)<=s<=min(19,29-delta).

To verify the converse, the interval gives valid r,s, l,k are integers,
and 30l-20k+r-s=10u+delta=d. The forward B equation above and
10D=9d+delta then give the prescribed full output (B+D,B). For a
specified B in the stated residue interval, z is an ordinary integer.
This is exact ordinary reconstruction, not a profinite existence claim.

Here is my independent hand reconstruction of ALL twenty interval
calculations. The column C is 33e-10u before reduction mod66; B=C+s.

| D | d | u | delta | e | s interval | C | B mod66 |
|---|---|---|---|---|---|---|---|
| 20 | 24 | 4 | -16 | 0 | 16..19 | -40 | 42..45 |
| 21 | 24 | 3 | -6 | 1 | 6..19 | 3 | 9..22 |
| 21 | 25 | 4 | -15 | 0 | 15..19 | -40 | 41..45 |
| 22 | 24 | 2 | 4 | 0 | 0..19 | -20 | 46..65 |
| 22 | 25 | 3 | -5 | 1 | 5..19 | 3 | 8..22 |
| 22 | 26 | 4 | -14 | 0 | 14..19 | -40 | 40..45 |
| 23 | 24 | 1 | 14 | 1 | 0..15 | 23 | 23..38 |
| 23 | 25 | 2 | 5 | 0 | 0..19 | -20 | 46..65 |
| 23 | 26 | 3 | -4 | 1 | 4..19 | 3 | 7..22 |
| 23 | 27 | 4 | -13 | 0 | 13..19 | -40 | 39..45 |
| -10 | -14 | -4 | 26 | 0 | 0..3 | 40 | 40..43 |
| -11 | -14 | -3 | 16 | 1 | 0..13 | 63 | 63..65,0..10 |
| -11 | -15 | -4 | 25 | 0 | 0..4 | 40 | 40..44 |
| -12 | -14 | -2 | 6 | 0 | 0..19 | 20 | 20..39 |
| -12 | -15 | -3 | 15 | 1 | 0..14 | 63 | 63..65,0..11 |
| -12 | -16 | -4 | 24 | 0 | 0..5 | 40 | 40..45 |
| -13 | -14 | -1 | -4 | 1 | 4..19 | 43 | 47..62 |
| -13 | -15 | -2 | 5 | 0 | 0..19 | 20 | 20..39 |
| -13 | -16 | -3 | 14 | 1 | 0..15 | 63 | 63..65,0..12 |
| -13 | -17 | -4 | 23 | 0 | 0..6 | 40 | 40..46 |

The triangular lists are forced by the inverse bounds: positive outside
options grow from {24} to{24,25,26,27} as D grows20 to23; negative ones
grow from{-14} to{-14,-15,-16,-17} as D decreases-10 to-13. No other
outside option exists. Negative parity e=1 for u=-1,-3 is essential.

Outside-parent existence alone is insufficient. For D21,22,23,-11,-12,-13
the full inverse d interval has endpoint difference4, so two parents
separated by5 are impossible. At D20 it is[19,24]. The d24 possibilities
are exactly (r,s)=(0,16),(1,17),(2,18),(3,19). Only(1,17) is in a
double rectangle, R_L; its partner has d19 inside I. This deletes B43
mod66, and only that residue. At D-10 the interval is[-14,-9]. The
d-14 possibilities are(26,0),(27,1),(28,2),(29,3). Only(28,2) is
in R_H, with partner d-9 inside I; it deletes B42 mod66. All remaining
entries have no inside partner. These checks prove BOTH directions
of the claimed orphan iff, not merely a necessary condition.

After those deletions the exact T_D are:

| D | T_D | Size |
|---|---|---|
| 20 | {42,44,45} | 3 |
| 21 | 9..22 union41..45 | 19 |
| 22 | 8..22 union40..65 | 41 |
| 23 | 7..65 | 59 |
| -10 | {40,41,43} | 3 |
| -11 | 0..10 union40..44 union63..65 | 19 |
| -12 | 0..11 union20..45 union63..65 | 41 |
| -13 | 0..12 union20..65 | 59 |

Their total is2(3+19+41+59)=244 modulo66 rays BEFORE the independent
modulo60 current-input rectangle exclusions and official filters. The
forty birth rays are disjoint by their differences -1,1,2. There is no
claim that the final seed set has284 rays after mixing the two periods.

## Q8: exact refined equivalence and genuine remaining gaps

Sdagger consists exactly of official off-diagonal strip starts with
either B<=42, or B>=43, outside R_L and R_H, and either a birth in
F(Delta) minus Delta or an orphan with the table's D and B mod66.
It is a subset of Sstar because every orphan has an outer difference.

If an official survivor exists, eventual entry gives a nonempty set
of official strip survivors. Minimize their positive integer Phi. A
minimum at B<=42 is retained. At B>=43 a non-birth with any inside
parent has a smaller official off-diagonal survivor by the full-I rank
lemma, so a minimum must be either a birth or an orphan. Those are
critical. If its current residues are in a double rectangle, the exact
Q5 partner is another smaller survivor. It therefore belongs to Sdagger.
This proves the contrapositive of the converse to the trivial inclusion
direction and hence both Q8 implications. Each selected inverse or
merger move keeps an ACTUAL official inside-strip survivor and decreases
Phi by at least1, so the alternative finite descent also terminates.
No source, compactness or changing-depth seed inference enters.

The restriction is strict on an unbounded legal family. For k>=1,
Y=(660k+23,660k) is critical D23, outside both input rectangles, and
in Sstar. But X=(600k+23,600k) is an actual inside parent, F(X)=Y,
with the same difference23 and Phi loss120k. Equivalently B mod66=0
is absent from T_23. Thus Y is not in Sdagger. Removal from a set of
possible MINIMUM survivors does not prove Y itself hits.

Both distinct source mechanisms remain. The birth family
(660j+682,660j+680), j>=0, has a unique diagonal incoming parent
but singleton next-output fiber. The orphan family

    X_j=(600j+30,600j+4),
    Y_j=(660j+30,660j+7), j>=1,

has unique incoming parent of difference26 outside I, D23, B mod66=7,
and current residues(0,7), so it too is a singleton-next-output seed.
All displayed starts are positive and above the product threshold.
Their future hitting or avoidance is NOT proved. No small patch was
checked. The only complete unbounded subfamily whose future hitting is
proved here is the explicit D2/R_L one-step subfamily established earlier.

## Source, failed-route and operation boundaries

The official question and preliminary statement were checked in the
actual primary PDF. The organizer's strip/invariance statement is
attribution only. The added source checks of integer toral maps and
generic nearest-lattice discretizations are comparisons, not premises.
Their actual settings were checked separately; the source companion
records exact read limits. No complete external dynamics proof or
exhaustive current-literature search is claimed.

The failed-route records preserve the real cutoff36/40 obstructions,
the ordinary birth and outside-strip inverse counterexamples, the
failure of sum alone to orient an R_L merger, and the unresolved future
of the residual seeds. Their elementary subsidiary examples agree with
the map:100S+d^2 need not lower positive critical R_L points; the
rounding-free S+c d^2 forward/inverse inequalities leave an intermediate
region; a mod2 and b mod3 are actual invariants. None is represented as
an impossibility theorem for every rank or every ordinary lift.

Q1 gives F^n(Z^2)=Z^2 for every finite n, so full-image density inside
each finite output box is exactly1, even with local collisions. This
is distinct from counting images of a fixed input box. The latter
normalization in Guiheneuf--Joly includes the determinant factor.
The submission retains this distinction and makes no density-to-emptiness
or generic-to-fixed-map inference.

I used hand algebra for every mathematical assertion and all twenty
interval rows. No mathematical program, state/orbit scan, CAS, inverse
recovery execution, finite-certificate replay or author rerun occurred.
The only code created/executed is administrative SHA/JSON/text-label
and literal-suffix integrity work under this assigned review prefix.
No old/shared/Git/cache bytes, other worker job, charge, contact or
access restriction was disturbed. There is no owned native math child
or unresolved computational job to report.

The exact new weekly window is explicitly user-authorized through90%
TOTAL with reserve, reset1792874445; direct telemetry at06:19UTC was10%
TOTAL, ordinary usage allowed. Root owns shared monitoring/keepawake.
No future reset is automatically authorized. The final metadata records
the handoff reading. No numerical annual answer, survivor construction,
no-tenfold theorem, automaticity or universal termination is accepted
by this reviewer. Coordinator reconciliation remains necessary.
