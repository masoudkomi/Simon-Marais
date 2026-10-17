# Finite affine extraction and effective one-sided dilation recovery

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
`/root/review_2021_reasoning_j15_r2`. Requested inherited
gpt-6.1-sol/max; independent effective-setting readback unavailable.
TWO OTHER fresh initially blind WHOLE nonconstructor audits and
coordinator reconciliation are required. This submission does not
promote itself, evaluate the official scalar, or claim novelty.

This is a proposed effectiveness bridge for ACTUAL fixed-D counts.
The new arguments replace the qualitative limiting-profile/Vitali step
by a finite affine extraction, and replace the strict receiving-density
limit by replication of one actual finite receiving block. The proposed
output is a computable one-sided finite-excess certificate, not a
two-sided convergence rate or a numerical evaluation of the entropy.
No mathematical program, enumeration, CAS, numerical optimization or
old certificate rerun was used. Algorithms below are mathematical
constructions proved terminating, not computations performed here.

## 0. Official domain, exact accepted inputs and four proposed claims

The official2017 B4 count C(n), n>=2, is the fixed regular2n-gon count,
with orientations distinguished, and its two rates are normalized by
n^2 and logarithm base2. Use the separately accepted marked dictionary:
these are full-reversal commutation classes, not reduced words, sweep
histories or rotation/reflection orbits. There is no preliminary(a).

For fixed integer D>=2 put v_i=(1,i-1), V=[v_1 ... v_D], and let
B_D(p)=B(p,...,p) be the FULL balanced fixed-boundary count. Write

    k_D=lim_(p->infinity) p^-2 log2 B_D(p), ell_D=k_D/D^2,
    L=lim_(n->infinity) n^-2 log2 C(n).

Existence at ALL integer p,n, ell_D<=L and ell_D->L are accepted G
premises, not conclusions independently recertified here.

For an integer C>=1 and real r>=1 use EXACTLY G's GE_(D,C)(r):
positive-area Jordan tile disks B with complete physical, colored,
ranked/lifted boundary, perimeter<=Cr, and ONE full standard zonogon
exterior with contents N_i<=Cr that works for EVERY filling of B.
Zero ambient contents are allowed. Integer dilation MB multiplies the
same boundary/ranks and subdivides each old edge into M consecutive
unit edges. Put Z_D(B) for its complete-boundary filling count. The
one chosen full exterior may be padded by G's fixed belts to a balanced
content p=max N_i<=Cr. The exterior is still the same for every filling.
This is not a diameter-only boundary class.

Read COMPLETE accepted G, DC, V, OP and HC bodies and their acceptance
MD scopes. The precise additional local interfaces used are FD's lift
and finite alphabet, FL1, RM1, OC1--OC3, LW1, CW0--CW4, SP1--SP3,
and all-D AD1--AD5/US_D1--US_D3. Their domains are retained below.
The accepted proofs give actual tile disks, ONE full reference, every
integer dilation, and q-independent strict constants before rational
periods. No generic Q decoration is asserted sufficient. HC's weighted
SUM is not replaced by one internal class, and its finite strictness
is not used as a mass estimate. The new argument instead retains the
mass of the entire actual B family through a finite profile cover.

I authored HC and the older all-D strict LOCAL packet, and whole-reviewed
G and several older local inputs. These are disclosed accepted-premise
roles, not independent self-recertification of my old work. The coordinator
gave the research target, not the Fourier estimate, finite receiving-block
argument, finite catalogue or new dilation proof. All new claims below
require OTHER whole auditors. Old bytes remain unchanged.

The proposed results are:

**EC1, finite affine extraction.** For compactly supported vector
F in W^(1,2)(R^2), let A_Q be its coordinatewise L2-best affine map
on a dyadic square Q of side l(Q), and define

    beta_F(Q)^2=l(Q)^-4 integral_Q |F-A_Q|_2^2.

Then

    sum_(all dyadic Q) |Q| beta_F(Q)^2
                   <=2^10 integral_(R^2) |DF|_F^2.             (1)

If each coordinate is G-Lipschitz on Q and 0<tau<=G, failure of
sup_Q||F-A_Q||_infinity<tau l(Q) implies

    beta_F(Q)^2>=tau^4/(2^12 G^2).                            (2)

Consequently a prescribed finite range of sufficiently many levels
contains one level with arbitrarily small total nonflat area, with
an explicit level bound. The particular form is classical Dorronsoro
methodology; see the primary
[Orponen text, introduction and planar argument](https://arxiv.org/pdf/1811.01702).
The proof and loose numerical constant needed here are given completely,
not imported from an unread theorem.

**EC2, finite local recovery data.** At fixed D, desired loss and fixed
outer collar, a finite algebraic/rational catalogue covers the compact
necessary slope set K_D. Its strict entries use an actual FINITE outer
receiving count as a replication block. Its boundary entries use ONE
adjacent merged pair and all other groups singleton. Given a finite-M
recovery modulus in dimension D-1, all local tolerances, frame periods,
physical scale thresholds, per-window remainder bounds and dilation
thresholds in this catalogue can be obtained by terminating operations
over rational/real algebraic numbers. No local entropy value or rate
of approach to that value is an oracle.

**EC3, effective finite-M GE recovery.** There are total algorithms
R(D,C,e), M_0(D,C,e), with positive integer outputs for integers D>=2,
C>=1 and positive rational e, such that for EVERY real r>=R, EVERY
B in GE_(D,C)(r), and EVERY integer M>=M_0,

    log2 Z_D(B)-M^-2 log2 Z_D(MB)<=e r^2.                    (3)

Thus the positive GE dilation deficit has a computable modulus at each
fixed D,C. No D-dependent scale is silently used in a growing-D limit.

**EC4, actual one-sided finite certificates.** There is a uniformly
computable rational epsilon(D,p)>=0 with epsilon(D,p)->0 at each fixed D,

    epsilon(D,p)>=max(0,p^-2 log2 B_D(p)-k_D).               (4)

Therefore V3's balanced EXTRA hypothesis E follows in this candidate,
and ell_D and L have uniformly enumerable certified lower bounds tending
to them. The upper-approximation hypothesis R of V3 is still unproved.
The new finite-M inequality, even with zero error, cannot by itself
provide it: the accepted abstract V4 sequence already satisfies that
stronger numerical inequality and can have a noncomputable limit.

## 1. A complete finite multiscale calculation

### 1.1 Fourier estimate, with a fixed normalization

Use Fourier transform exp(-2 pi i x dot xi). For t>0 let F_t have
multiplier exp(-t^2 |xi|^2). For x fixed use the affine function

    A_(x,t)(y)=F_t(x)+DF_t(x)(y-x).

For |h|_infinity<=t put s=t|xi| and a=2 pi xi dot h. Then |a|<9s.
The Fourier multiplier of F(x+h)-A_(x,t)(x+h) is

    exp(ia)-exp(-s^2)(1+ia).

For s<=1, Taylor's integral remainder bounds its modulus by
a^2/2+(1-exp(-s^2))(1+|a|)<=51s^2. For s>=1 its modulus is at
most1+exp(-s^2)(1+9s)<5: the latter product decreases on[1,infinity)
and starts at10/e<4. Hence its square is at most

    2601 min(s^4,1).                                         (5)

Plancherel applies to each coordinate. The best affine L2 error on a
side-t square Q is at most the average, over x in Q, of the errors
of A_(x,t). Sum over its dyadic level and then put y=x+h. Enlarging
the h domain to[-t,t]^2 gives

    sum_(Q at side t) |Q| beta_F(Q)^2
      <=10404 integral t^-2 min((t|xi|)^4,1)|Fhat(xi)|^2 dxi. (6)

The factor is4*2601; there is no extra t^2 after this cancellation.
For b>0 choose a dyadic t_* with1/2<t_* b<=1. The terms t<=t_*
sum to at most(4/3)b^2, and those t>t_* to less than(4/3)b^2.
Thus

    sum_(t dyadic) t^-2 min((tb)^4,1)<(8/3)b^2.

Since integral |xi|^2|Fhat|^2=(4 pi^2)^-1 integral|DF|_F^2,
(6) summed over all levels is bounded by27744/(4pi^2) times
that energy. This is less than2^10 since pi>3. Nonnegative sums
justify passage through the integrals. First doing the calculation
for smooth compactly supported functions and using W^(1,2)
approximation proves (1) as stated, including vector F by summation.
No differentiation of a merely uniform-limit profile is needed.

### 1.2 From L2 fit to whole-square affine control

For one scalar G-Lipschitz coordinate on Q, centered at z, the best
affine fit has constant term its mean and slope entries

    (12/l^4) integral_Q (x_j-z_j) F(x) dx.

Subtract F(z). The integral of |x_j-z_j| is l^3/4 and
|F(x)-F(z)|<=G l/sqrt(2). Each slope entry is at most3G/sqrt(2),
so its Euclidean row norm is at most3G. In particular F-A is
4G-Lipschitz (6G would also suffice).

If |F(x0)-A(x0)|>=tau l at some point of the closed Q, its absolute
value stays at least tau l/2 in the radius tau l/(12G) ball about
x0. Because tau<=G this radius is at most l/12. At least a quarter
of the radius-squared is inside Q. Thus its squared integral is
at least tau^4 l^4/(2304G^2). Summing coordinates is only larger;
2304<2^12 proves (2). The boundary of Q causes no exception.

If integral|DF|^2<=E, the sum of the areas of non-tau-flat squares
over ANY finite collection of levels is at most

    2^22 G^2 E/tau^4.                                     (7)

For N levels at least one has nonflat area at most this quantity/N.
The level range can start at any prescribed coarse level. No claim
that every fine level or the pointwise derivative is uniformly good
is made. Only ONE common level for the selected actual reference
profile is used below.

### 1.3 A flat fit lies near the actual nonconvex slope set

On a square in an actual full tiling, put h(x)=a(rx)/r. Its coordinate
Lipschitz bound may be taken as D, by the explicit finite tile-gradient
formula and convexity of the full zonogon. If A(x)=Jx+c is the best
fit, linearity of orthogonal projection and Vh=x give EXACTLY

    VJ=I, Vc=0, max_i ||J_i||_2<=3D.                       (8)

If ||h-A||_infinity<=tau l on the square boundary, the accepted exact
Green identity bounds the ij-minor discrepancy by

    tau l [4D l+4(3D)l]<=16D tau l^2.

Actual ij minors are nonnegative even on partial tiles. Therefore

    det(J_i,J_j)>=-16D tau for every i<j.                  (9)

Using24D instead of16D below leaves spare room. This is an approximate
membership statement; K_D has not been convexified by averaging.

For completeness an effective near-membership test needs no explicit
Lojasiewicz exponent. FD's exact identity bounds all entries of K_D by
D^2. Fix H=10D^2 and let

    S_nu={J:VJ=I, ||J_i||_2^2<=H^2,
                         det(J_i,J_j)>=-nu for all i<j}.

These are compact rational semialgebraic sets, decreasing to K_D as
nu decreases to0. Given any FINITE algebraic open cover U of K_D,
test nu=2^-m successively until S_nu subset U. Each test is a first-order
polynomial formula over real algebraic numbers, hence decidable by
real-closed-field quantifier elimination. The loop halts: otherwise
compactness gives J_m in S_(2^-m) outside U with a limit in K_D outside
U. This proves a terminating procedure, not a numerical CAS run.

The exact external algorithmic input is attributed to real-closed-field
quantifier elimination, for example
[Perrucci--Roy Theorem1](https://arxiv.org/pdf/1609.02879). Its rational
or real algebraic coefficients have decidable signs here; the source's
arithmetic/sign convention is not an oracle for arbitrary real constants.
It is used only for finite-dimensional polynomial formulas. It is not
applied to unknown entropies, sets of infinite tilings or halting facts.
Closed decision formulas can be given a dummy free variable, eliminated
down to that variable by the stated Theorem1, and evaluated at0. This
avoids relying on an unstated i=0 endpoint of that source's notation.
An algebraic coefficient can instead be represented by its polynomial
and rational isolating interval, with its unique root made an additional
quantified variable. Thus every decision call can be reduced to rational
coefficients; signs of arbitrary real inputs are never required.

## 2. Finite local recovery, with its parameter and effectiveness audit

This section supplies the local data for the new finite global proof.
It is stronger than citing G's qualitative compactness conclusion.
Every constant concerns fixed D and fixed positive tolerances.

### 2.1 Finite strict receiving-block comparison

Keep one allowed rational J', physical integer frame, denominator q
and common generic phase from the accepted all-D strict theorem. Use
its constants A0,K0,H_rec,B_end and put t=sqrt(epsilon). Enlarge the
geometric original-scale constant if needed. Its actual upper/lower
operations give

    log |F|<=log C_m+K0(tL^2+L+1),
    R_M(T)>=C_(k_M)/B_end,
    m=ceil((1+2A0t)L/q),
    k_M=floor((1-2A0t)ML/q).                              (10)

The lower operation can be required for EVERY M>=1 once L exceeds
a fixed constant times(q+1)/t. Indeed its necessary inequalities are
positive support margins, q k_M beyond the bounded main-lens end boxes,
and the rank-buffer inequality. Each follows from ML>=L and
q k_M>=(1-2A0t)ML-q after increasing that finite original threshold.
There is no entropy convergence threshold hidden in this enlargement.

Choose t so (2A0+1)t<=1 and (4A0+2)t<=1/2, and require q<=tL,
L>=1/t. The accepted exact block injection, now with block size m,
gives C_(k_M)>=C_m^(floor(k_M/m)^2). Set b=4A0+2. Directly,

    q m<=(1+(2A0+1)t)L,
    floor(k_M/m)>=M(1-(4A0+1)t)-2.

For M>=4/t its ratio to M is at least1-bt and its square at least
1-2bt. Also log C_m<=H_rec(qm)^2<=4H_rec L^2. Combining these FINITE
inequalities proves

    log |F|-M^-2 log R_M(T)
      <=[3K0+8b H_rec]tL^2+log B_end/M^2.                  (11)

In (11), L>=1/t paid L+1 by2tL^2. The last constant can instead
remain in a per-window O(L+1) remainder, uniformly in M>=1.
No receiving entropy e, supremum approximation, or rate of its limit
was used. In particular m is the actual upper receiving size belonging
to THIS original L, not an independently chosen good asymptotic size.
The source class and the one reference retain all complete boundaries,
phases and all-color rank/ideal tests of (10).

For a real strict center one first chooses t small for its loss/collar,
THEN the finite rational net and periods, and finally the original
scale threshold. The accepted q-free construction makes this legitimate.
A finite maximum of the M>=4/t thresholds works for the catalogue.

### 2.2 Why the strict geometric constants can be computed

Here is the finite selection/constant extraction, rather than an appeal
to the computability of a qualitative limit. On the rationally described
compact class K_(rho)={J in K_D:min det(J_i,J_j)>=rho}, enumerate finite
lists of integer frame pairs(u,v), det(u,v)>0, and positive dyadic kappa.
Test whether every J in K_(rho) has one listed frame with

    J_i u>=2kappa, J_i v>=2kappa for all i.                 (12)

This is a first-order polynomial test. The open common positive cone
and compactness in the accepted strict proof ensure eventual success.
Use the compact assigned subsets from(12) and retain margin kappa
for nearby rational approximants. All frame norms, support-line gaps,
two-row singular lower bounds and coefficient norms are now computable
algebraic numbers. Replace positive margins by smaller positive dyadic
numbers and upper bounds by larger integers.

For clarity, the O symbols in the accepted construction are not
treated as additional effectiveness axioms. One permissibly loose
arithmetic extraction is as follows. Choose a power-of-two integer T
at least2^20 times the maximum of100 and the following numbers:

    D, H+1, 1/rho, 1/kappa, all frame coordinate magnitudes,
    1/gamma,
    gamma=min det(u,v)/max(||u||,||v||).

Use Euclidean vector norms and Frobenius matrix upper bounds. The same
proof permits the following deliberately loose upper bounds:

|Quantity|Finite bound|Reason in the accepted construction|
|---|---|---|
|digital/rounding/lift and sample error constants|T^6|sum of D fixed vectors, I-JV, and nearest-coordinate rounding|
|positive-path physical band|T^12|coordinate endpoint increments, M_V and K_dir in its(25)--(26)|
|main-lens/end-box and extraction cut constants|T^24|frame slope gap>=T^-2, supporting-line gap>=gamma, and the preceding graph band|
|buffer and outer/inner frame expansion A0|T^40|larger than cut constant divided by gamma, with spare fixed tile margins|
|receiving density upper bound H_rec|T^12|presence bits for binom(D,2) types in an O(T^2 qm) box|
|strip code K0 and log2 B_end|T^64|four side strips/corner boxes with cut width, finite origins/types, O(L)-letter words and one endpoint|
|original physical scale coefficient|T^80|sample positivity, rank singular bound, support margins, q overshoot and bounded end-box thresholds|

Here sigma_min>=rho/(2sqrt(2)(H+1))>=T^-4; the common graph slope
gap is at least T^-2; and each unit frame length is at most2T.
For example a radius-T^24 end box has fewer than T^52 possible
origin/type presence bits, below T^64. A side strip of width
T^24 tL, plus its corner squares, has fewer than T^54(tL^2+L+1)
such bits; t<=1 absorbs t^2 terms. Words/endpoints use less than
T^8(L+1) additional bits. These inequalities verify the two coding
rows without counting possible fillings by unrecorded coordinates.

Taking t<=T^-100 meets the geometry caps; take it still smaller
for the specified loss and collar. The coefficient in(11) is below
T^120. A finite rational net in VJ=I is computable: choose free
rows3,...,D rationally and solve rows1,2 using det(v1,v2)=1; test
coverage and the strict chart margins by quantifier elimination.
Only after the tolerance is fixed choose a common denominator and
a rational generic phase outside its finitely many proper event
hyperplanes. These are finite searches with proved termination.
They determine q and the finite maximum scale T^80(q+1)/t.

The entries in this table are new conservative bounds to be audited,
not numerical claims that a program verified them. What matters is
that every input is a finite vector, a positive algebraic margin,
a finite type/origin count, or an explicit inequality. The receiving
entropy and its unknown convergence rate are absent from this list.

### 2.3 Boundary entries, including zero rows and all other colors

Assume inductively that(3) is available in dimension D-1 with its
computable outputs. Set C_-=4D^2. A good disk after SP has at most
D(r0-1) active coarse curves and at most2D(r0-1) boundary edges;
standard coarse edge lengths are below D. Thus it belongs to the
ACTUAL GE_(D-1,C_-)(r0), with one full exterior valid for every filling.
Absent coarse colors are allowed. Fine/coarse positive tile areas
are within factors D, so no area normalization is lost here.

For a boundary center J0 in K_D choose an OC cut and exactly ONE
adjacent zero-minor pair. If there is a zero row, pair it with one
neighbor, including another zero row if necessary. Otherwise OC
makes a positive parallel group consecutive, and one neighboring
pair in it is available. All other D-2 groups remain SINGLETON,
even if some of their rows vanish or are parallel. Rank two follows
from VJ0=I, so this is compatible with D=3 reducing to the grid base.

All relevant OC matrix/inverse/lift-error and homeomorphism bounds
are bounded by a computable polynomial in D,H: from weighted
Cauchy--Binet, 1/D<=det A<=D, while ||A|| is bounded by D^3(H+1).
For example B=2^10 D^8(H+1)^2 bounds these maps, inverses, the complete
affine-error maps and the needed standard-coordinate row norms. The
source unit shape A^-1[-1/2,1/2]^2 has bounded diameter,
perimeter and positive area between1/D and D. These bounds are
uniform over all boundary centers and the finite cuts.

Here is a safe explicit way of bounding the combinatorial constants.
Choose K=(100D(B+1))^100. Local coordinate ranges involve at most
2D*diameter+2 levels per color. Each selected full curve crosses
each other locally relevant full curve at most once; each crossing
letter costs at most D bits. A fixed-width boundary tube is covered
by at most ceil(P/width)+1 squares of twice that width. In one
selected face the residual curve number is at most D(r0-1), total
tile number at most its square/2, and boundary-edge sum at most twice
that number of curves. The fringe has width at most D^2 r0 plus
two tile diameters. Its possible origins, each of binom(D,2) types,
give the stated LW1 code. A rare tile marks at most four faces.
Every factor here is bounded by a product of fewer than twenty
factors100D(B+1); K dominates them and fixed norm conversions.
This also bounds the Green rare-count and the SP area/perimeter
conversions. This is finite counting of bounds, not a scan.

On a source window of span L with common affine error tau_source L,
the entire target square and star buffer fit by CW1 when the source
tolerance is small relative to the prescribed collar theta. CW0/CW0'
give ONE target offset. FL1 and the explicit finite tube bound give

    S_rare<=K(tau_source L^2+L+1).

LW1 at fixed rank spacing r0 gives a code bounded by

    K[L^2/r0+tau_source r0^2 L^2
                  +r0^2 L+r0L+r0^2+log(R_abs+2)].            (13)

Only actual global selected faces wholly inside the target square
are retained. Every good face is clean including incident tiles.
Its complete residual Jordan disks and their ranks are fixed.
SP1--SP3 identify their whole fine counts at EVERY integer M with
the coarse GE counts just described. This does not use a general
local lifting through a deleted forbidden crossing.

Fix a rational beta>0. Small blocks of fine area<beta r0^2 have
total area at most K sqrt(beta) r0^2 per face, by the aggregate
perimeter bound and isoperimetry (pi>3 is enough for a rational
constant). A tileable known disk with t reference tiles has its
whole log count at most a computable constant times t and hence
its area: use its reference perimeter<=4D t and the finite alphabet.
Small-block errors therefore cost at most K sqrt(beta) r0^2.
There are at most K/beta larger blocks per face. For those, if

    r0>=R(D-1,C_-,u), M>=M_0(D-1,C_-,u),

the induction error is at most u r0^2 for each one. Summing over
the O((L/r0+1)^2) actual local faces gives the finite-M loss

    K[sqrt(beta)+u/beta](L^2+r0 L+r0^2).                    (14)

For any desired rational local loss zeta>0 per outer SOURCE area,
replace zeta by min(zeta,1), put v=zeta/(100DK), choose beta<=v^2,
u<=v beta, then

    r0>=max(2,R(D-1,C_-,u),1/v),
    tau_source<=min(v/r0^2, theta/(100B^2)).

Decrease these rational caps if needed for the CW whole-tile margins.
Equations(13)--(14) now have total quadratic part below zeta times
the source area. All remaining terms have the EXPLICIT form

    K_entry [L+1+log(R_abs+2)],                            (15)

for a computable integer K_entry depending on the fixed choices.
The local M threshold is the induction M_0. Original scale thresholds
pay all tile/star margins and r0 fringe terms. Every choice is finite
arithmetic or a lower-dimensional call; there is no unknown eta(r0)
to evaluate. Using a smaller v absorbs any extra fixed factor K.

The code fixes one target anchor, not an independently unbounded
anchor for every disk. Once all codes are conditioned JOINTLY, one
actual full reference supplies all target pullbacks and all fine
exteriors. CW3/CW4 keep exact physical/ranked boundaries at every M.

### 2.4 A computable finite open catalogue of ALL slopes

Fix the desired collar and per-area loss. First perform the boundary
choices above, uniformly using D,H and the finite cuts. Their source
tolerances and unit-shape bounds are positive and computable. A small
algebraic ball about a boundary center is usable: an additional slope
error delta on a unit-size window adds at most a fixed delta L to
the source affine error, with the offset corrected at its center.

Let K_partial={J in K_D:some ordered minor=0}. Compute a finite
algebraic net of K_partial and assign each center one valid cut and
adjacent pair. This operation is effective: real algebraic points
are dense in every rational semialgebraic set, by real-closed-field
quantifier elimination applied inside rational open boxes. Enumerate
such points with exact polynomial/isolating-root descriptions and
test finite open-ball coverage. Compactness proves termination.
One may equivalently use an algebraic sampling algorithm.

Before this boundary net is selected, use the uniform boundary shape
bounds to fix the packing span described in2.5. Choose its ball radius
small enough to pay the affine error on those smaller windows. The
resulting boundary balls cover a fixed neighborhood of K_partial.
Find positive rational rho such that every J in K_D with a minor<=rho
is in a smaller union of those balls. Successive dyadic rho tests
are decidable polynomial formulas and eventually succeed by compactness.
If K_partial were empty, the eventually empty small-minor set gives
the same conclusion. No measure truncation depending on an unknown
profile is used.

The remaining compact strict K_(rho) uses2.2. After its physical frames
are fixed, fix their packing spans and the strict error caps BEFORE
choosing the finite rational center net and receiving phases. Thus
the net balls are small enough for each packed subwindow while still
covering K_(rho), by the q-safe order of choices. A finite algebraic
open catalogue therefore covers ALL K_D,
including zero ambient colors and every zero-minor stratum.

There is no computable value of a local entropy in this procedure.
The only infinite searches are successive finite polynomial decisions
or enumeration of finite rational/algebraic data, with their termination
proved by positive margins and compactness of finite-dimensional sets.

### 2.5 Packing a flat square without losing a fixed area fraction

For each catalogue unit parallelogram P, its translates tile the plane
by the lattice generated by its two sides. Choose a small rational
scale lambda>0, and retain only its scaled fundamental cells fully
inside the unit square. Cells meeting the square boundary are contained
in a strip of width O(diameter(P)lambda), whose area has that same
computable bound. Shrink each retained cell concentrically by1-kappa.
Their closures are disjoint; the lost area is at most2kappa. Choose
lambda,kappa so the total loss is less than any prescribed rational
packing fraction. These are finite geometric tests over algebraic
numbers and an explicit strip bound. No Vitali lemma is invoked.

Then use an inner homothetic copy of each outer window, factor1-theta,
for upper recovery; its additional lost fraction is at most2theta.
All required strict intermediate buffers and boundary target-core
preimages stay in the outer window, by the local collar choices.
Each template has finitely many windows, a computable minimum positive
span lambda_min and computable area/perimeter bounds. The slope-ball
radii are chosen using this packing span BEFORE their finite coverage
test, as ordered in2.4. A sufficiently small final flatness tolerance
then ensures that ONE affine estimate on the whole parent square
supplies the prescribed estimate on EVERY smaller window, with ONE
common offset per window.

These catalogue choices precede the near-K test; the final flatness
tolerance is chosen after that test and before the multiscale levels.
Rational receiving periods are chosen only
after the strict tolerances, and affect original thresholds only.

## 3. Finite global extraction with an explicit order of parameters

We prove(3) by induction in D. For D=2, V is invertible and every
full tiling is its fixed coordinate grid. A GE disk and every MB
therefore have count one, by gluing to the one full exterior. Take
R=M_0=1. This includes absent ambient colors whenever positive area
is possible. For D>=3 assume the total lower-dimensional algorithms
already constructed, not merely balanced entropy existence.

Fix integer C>=1 and rational0<e<=1; replacing larger e by1 suffices.
All normalization in this section is by r, NOT by a balance content
that could be too small compared with r. This removes any need to
extract a hypothetical positive-deficit subsequence.

### 3.1 Bounds independent of B and its filling

Choose the one GE full exterior, and G's fixed balanced belts, once.
Every filling extends injectively to content p<=Cr. Its normalized
lift h_T(x)=a_T(rx)/r takes values in[0,C]^D and is D-Lipschitz in
each coordinate on its convex full domain. That domain is in
[0,CD^2]^2. Extend each coordinate to the plane by its McShane
extension and clamp it to[0,C]. Multiply by

    chi(x)=max(0,1-dist_infinity(x,[0,CD^2]^2)).

Call the resulting vector F_T. It agrees with h_T on the full
domain, has compact support in[-1,CD^2+1]^2, and each coordinate is
(D+C)-Lipschitz. The following integer is an energy upper bound:

    E=D(D+C+1)^2(CD^2+2)^2.                               (16)

The extension is a device for the Fourier estimate and the finite
profile cover. No minor condition or V F_T=x is asserted outside
the actual full domain. Choose a dyadic integer S>=CD^2+2; all sets
of interest lie in the fixed square Qstar=[-S,S]^2. Put Astar=4S^2.

There is a computable integer c_D such that a known region E0 with
one finite list of boundary curves admits a tile-presence record
of length at most

    c_D[area(E0)+sum lengths+number of curves+1].             (17)

To make this literal, take tile diameter d=2D and one bit for every
one of binom(D,2) types at each possible integer origin. Cover a
width-(d+3) boundary tube by arclength samples at spacing one and
integer squares of side4(d+3). Fully interior unit cells cost their
area; the sampled squares cost at most a fixed integer multiple
of their total length plus one per curve. This constructs c_D from
D, with no separate coordinate code at each tile. All regions used
below have one B boundary plus a fixed finite list of window sides.

### 3.2 Make every loss small BEFORE the level range

Choose positive rationals delta,theta,zeta with

    10 c_D delta<e/8,  10 c_D theta Astar<e/8,
    zeta Astar<e/8.                                      (18)

The spare factors pay boundary squares, packing loss and inner collars.
Use2.3 with per-area loss zeta/10, and2.4--2.5 with packing fraction
at most delta/(10Astar). This fixes, in the noncircular order stated
there, the following finite data:

    boundary rank spacing and lower-dimensional error calls;
    boundary balls, then strict truncation rho;
    strict physical frames and all packing spans;
    strict tolerance, rational centers, periods and phases;
    a finite open catalogue U covering K_D;
    lambda_min>0, finitely many original L thresholds,
    local remainder constants, and one finite Mloc.

Use1.3 to find positive dyadic nu with S_nu subset U. Choose a
positive dyadic tau so small that tau<=D,24D tau<=nu, and the
whole-square affine error tau times its side is within one quarter
of every packed subwindow's prescribed source tolerance. The slope
balls were already chosen to pay another quarter. All these are
finite inequalities between the fixed catalogue data. A final
uniform profile-cover error will pay another quarter.

Select k0 so that for l0=2^-k0,

    64(C l0+l0^2)<=delta.                                (19)

Choose an integer

    N>2^22 D^2 E/(delta tau^4),
    l_min=2^(-(k0+N)).                                   (20)

These are explicit finite numbers. The level range contains N levels
k0,...,k0+N-1; using the slightly smaller l_min is harmless. All
subwindow spans are at least lambda_min l_min in normalized units.

### 3.3 A finite common profile fiber, then ONE good grid level

Put Gext=D+C+1. Choose a positive dyadic profile precision dprof
small enough that dprof<tau l_min/100 and its sup-norm error on
every smallest packed window is within that window's remaining
source allowance. It is fixed independently of r and B.

Divide each side of Qstar into ceil(16Gext S/dprof) equal intervals.
On that grid the spacing is at most dprof/(8Gext). Quantize
each coordinate value into intervals of length at most dprof/4.
The Lipschitz bound shows that two profiles with the same record
differ by less than dprof throughout Qstar. The number of records
has logarithm at most the computable integer

    Kprof=D(ceil(16Gext S/dprof)+3)^2
                       *ceil(log2(4C/dprof+2)).             (21)

One may replace the last ceiling by a larger integer found by exact
powers-of-two comparisons. No values of an infinite profile oracle
need to be computed to obtain this upper bound.

Partition the ACTUAL finite set of B fillings by this record and
choose a largest class A. All fillings are extended through the same
fixed exterior before recording. Then

    log Z_D(B)<=log|A|+Kprof.                              (22)

Choose one actual representative T0 in A, solely to select the
grid/windows. Apply EC1 to F_(T0) over the N levels in(20).
For squares contained in B/r the coordinate Lipschitz constant is D,
not Gext; hence(7) bounds their non-tau-flat area by delta at one
of these levels. Discard all squares not wholly inside B/r.
Any discarded square meeting B/r lies within a sqrt(2)l tube of
its ONE Jordan boundary. Sample that boundary at arclength l:
at most C/l+1 squares of side8l cover this tube. By(19), their
total area is at most delta. This works for ragged or nearly pinched
B without passing to a limiting Jordan curve or winding domain.

In every remaining flat square, use its exact best affine fit A_Q.
Equations(8)--(9) and the chosen nu put its matrix in U. Select one
catalogue entry whose ball contains it, correct the offset at the
square center, and put the corresponding finite packing template
inside that square. All members of A obey the required common
affine estimate on EVERY whole outer window: the T0 fit error,
the catalogue center error and the uniform profile-record error
were each paid above. V times every corrected offset is zero.

The inner windows cover B/r except for area at most

    2delta+delta/10+2theta Astar.                          (23)

There is a computable finite upper bound Wstar on their number,
uniform in B,r and the chosen level/profile: use the number of
side-l_min squares in Qstar times the largest template size.
Their unit shapes, original scale thresholds and perimeters all
come from finite lists. Their physical spans are at least
lambda_min l_min r. No window can become microscopic relative to
r after these choices, even though this lower fraction is very small.

The above is the entire replacement for both compact limiting-profile
selection and the fine Vitali step. It controls ONE common family
of actual fillings, with finite computable overhead and a common
finite set of windows. It does not assert every Lipschitz necessary
profile is realizable or replace nonconvex K_D by a convex hull.

### 3.4 Joint codes, actual lower insertions, and a finite inequality

Record all original tiles meeting B outside the INNER windows,
including the fixed tile-width margins. The area coefficient of its
record is at most c_D times(23) r^2. The remaining cost from(17)
is linear in r plus a constant: one original boundary of length<=Cr
and at most Wstar parallelogram boundaries, all with known length
bounds. Components are paid separately. The normalized area error
does not depend on a limit-domain boundary.

In each boundary window form its fixed target core and LW code,
including its single anchor. The global full content is p<=Cr,
so the position/height range R_abs is at most a computable constant
times C(r+1). Charge EACH window's logarithmic anchor separately.
Condition on ALL these boundary codes and the original outside record
JOINTLY inside A, and choose one largest joint class X. Only THEN
choose ONE actual full reference T in X. This is G's exact conditioning
order. T0 selected the windows; it need not be the final reference.
Every member of X, including T, still satisfies their same affine bounds.

Strict intermediate-window restrictions and the complete target good-disk
fillings determine every original inner-window tile. Together with the
outside record they determine the whole B filling. Apply(11) in strict
windows and the finite induction bound(14) in boundary windows. Sum all
upper recovery/code bounds. CW3/CW4 and SP's every-M equality produce
independent fine replacements inside disjoint reference patches of T,
with EXACT M-dilated boundaries, for EVERY M>=Mloc. Their product
injects into Z_D(MB). Different charts do not have to commute: only
their actual fine reference pullbacks are glued. Arbitrary inserted
interiors need not stay affine or preserve the upper profile/code class.

The resulting FINITE inequality is

    log Z_D(B)-M^-2 log Z_D(MB)
      <= c_D(2delta+delta/10+2theta Astar) r^2
                       +zeta Astar r^2 + A(r+1+log2(r+2)), (24)

for all M>=Mloc and all r above the original geometric thresholds.
Here A is a computable finite integer formed by Kprof, Wstar, the
catalogue remainder constants, the separately summed perimeters,
anchor ranges, code-length delimiters and fixed end-lobe constants.
No number of small blocks is multiplied by an uncontrolled r0^2
error: their area/perimeter split is exactly(14).

No limit or compactness in the count variable is used in(24). The
number of windows can be enormous, but is bounded BEFORE r and M
grow. Every lower product uses one reference and all its exact ranked
patches. The original B is held fixed during each dilation.

By(18) its quadratic coefficient is below e/2 after harmless further
decreases of delta,theta,zeta. Since log2(r+2)<=2r for r>=1, the
last term is at most4Ar. Choose the integer

    R>=max(1,8A/e,
       4 times all original physical L thresholds/(lambda_min l_min)),
    M_0=max(1,Mloc),                                        (25)

rounding upward and paying fixed tile margins in the thresholds.
Then(24) proves(3). All choices in(16)--(25) are terminating finite
arithmetic, real-algebraic decisions or calls to dimension D-1.
The base is exact UR2, so this constructs total algorithms by induction
for EVERY fixed finite D>=2. No uniform estimate as D grows is claimed.

## 4. Actual lower certificates, and exactly which gap is still open

For balanced side p, take C_D=D(D+1). Its perimeter is at most C_D p
because ||v_i||<=i, and its empty exterior makes it a genuine GE disk.
Let

    a_D(p)=p^-2 log2 B_D(p),
    Kbar_D=binom(D,2)(D+1)(D^2+1).

A tile-origin presence code in[0,Dp] x[0,D^2p] gives
0<=a_D(p)<=Kbar_D for every integer p>=1. Auxiliary p=1 has its
ordinary full zonogon meaning. D=2 has B_2(p)=1 exactly.

For an input p, compute R(D,C_D,2^-j) for1<=j<=p, and let j(p) be
the largest j for which that output is at most p. If none exists put
epsilon(D,p)=Kbar_D; otherwise put epsilon(D,p)=2^(-j(p)). These
are rational outputs of a total algorithm. At each fixed D every
fixed j eventually qualifies, so epsilon(D,p)->0. It can also be
taken nonincreasing since the available qualifying indices only grow.

For a qualifying j, (3) with the full balanced boundary gives, for
EVERY M above its computed dilation threshold,

    M^-2 log2 B_D(Mp)>=log2 B_D(p)-2^-j p^2.

Use the separately accepted all-integer G2 limit along these multiples.
The left side tends to p^2 k_D. This proves(4). If no j qualifies,
the elementary Kbar bound already proves it. In particular

    k_D>=a_D(p)-epsilon(D,p)                              (26)

is an ACTUAL one-sided finite-side certificate, not a conditional
restatement of E. Finite B_D(p) is computable in principle by the
accepted finite reduced-word/commutation-component procedure; it
is not computed by that expensive procedure in this research.

Using dyadic lower logarithm approximants d(D,p,s)<=a_D(p), increasing
to it with error below2^-s, define

    b(D,s)=D^-2 max(0,max_(1<=p<=s)[d(D,p,s)-epsilon(D,p)]).

Then b(D,s) is rational, computable, nondecreasing, bounded above
by ell_D, and tends to ell_D at each fixed D. The last assertion
uses the accepted full convergence a_D(p)->k_D and the proved
epsilon(D,p)->0, choosing one large p and then increasing s.
Thus max_(2<=D<=s)b(D,s) increases to L by accepted ell_D<=L and
ell_D->L. The direction limit is taken AFTER each fixed-D result;
the algorithm's finite maximum is a lower enumeration, not an exchange
of analytic limits or an invocation of a theorem at D=D(p).

For an all-integer finite tail, RP's actual balanced padding gives
B_D(q)>=B_D(Mp) when Mp<=q<(M+1)p. It follows that

    a_D(q)>=(Mp/q)^2[a_D(p)-epsilon(D,p)]

whenever M is above the computed threshold, with a trivial lower
bound0 if the bracket is negative. This is another directly
verifiable consequence, not an upper bound for k_D.

Nothing here produces u(D,s)>=ell_D converging from above. Inequality
(26) has the LOWER direction. Accepted V4 already shows that even
computable finite counts with exact all-size quadratic replication and
zero positive excess can have a noncomputable quadratic limit. Hence
there is no inference from EC1--EC4 to a two-sided numerical value,
a convergence rate for |a_D(p)-k_D|, or V3's independent upper
hypothesis R. Strict receiving templates alone are not silently
assumed to exhaust the fixed-boundary upper count.

## 5. Preserved failures and proposed scope

The Fourier/affine step is classical quantitative differentiation
methodology; the complete special estimate above is used because its
constants and finite quantifiers are visible. Real-closed-field
elimination is an attributed published decision theorem. The proposed
new inference is their integration with the exact marked local recovery
interfaces and the finite receiving-block inequality, retaining all
actual counts, phase/rank assignments and one-reference gluing.

Replacing the best-fit J by its average without a near-K test would
be invalid: K_D is nonconvex. Using only Dorronsoro L2 control without
the Lipschitz conversion would not give whole buffered affine control.
A separate fine level for every source filling would lose the common
reference. A mesh code based on global contents O(L) would incur the
wrong loss. Dropping phase/rank boxes, incident cleanliness, the tiny-block
split, or the separate window perimeter/anchor terms would break(24).
None is omitted. The failed approaches record also why a naive SFT,
free-boundary pressure, arbitrary-Q lifting or mass-free finite strictness
argument does not yield the requested upper approximation.

This complete proposed proof awaits TWO OTHER fresh initially blind
WHOLE audits. The local constant table, semialgebraic coverage, finite
M floor bounds, all zero/absent-color cases, joint conditioning and
source scopes are substantive audit obligations. No verified execution
of these theoretical algorithms, usable numerical error bound, practical
complexity estimate, two-sided computability or noncomputability of L,
complete annual answer, best bound, source absence or novelty is claimed.
