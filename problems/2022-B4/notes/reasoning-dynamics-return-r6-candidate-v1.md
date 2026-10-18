# Power-sparse growth coincidences for actual ordinary trajectories

18 October 2026 UTC. **Candidate proof - unverified.** Constructor A,
`/root/review_2021_reasoning_j15_r2`. Requested inherited
gpt-6.1-sol/max; independently verified effective-setting readback
unavailable. Root supplied a generic target, not a new inference.
TWO OTHER initially blind ENTIRE WHOLE audits and coordinator
reconciliation are required. Only official2022 B4(b) is investigated.

The new assertion is about the ACTUAL real growth values of ordinary
integer trajectories. It does not assume the conditional tenfold orbit
or replace an infinite ordinary lift by finite congruence shadows.
Except for an explicit permanent parity twin, equal-growth coincidences
of an ordered pair under common diagonal translation have a power-saving
count. Consequently, on EVERY fixed-difference line, almost every pair
of adjacent starts has different growth, and the number of distinct
growth values below X is asymptotic to X/2. Nevertheless there are
certified positive growth gaps tending to zero, even between adjacent
starts on the single line a−b=6. This supplies a real growth-fibre mass
statement and a precise obstruction to a uniform numerical separation
test; it does not settle universal diagonal hitting.

## 0. Actual domain, old inputs and four proposed results

Let

    F(a,b)=(a+2 floor(b/20), b+3 floor(a/30)), beta=11/10.

An official start is a pair of positive ORDINARY integers with ab≥600.
Both updates use the old pair. Time0 counts for the diagonal question.
The established trapping statement is attributed context only; no
preliminary proof is investigated or needed below.

The COMPLETE current accepted CF1–CF6 body and MD/JSON authority were
read. Only its unconditional sum-growth identity, cooperation and exact
even-a parity twins are operative. CF6 remains explicitly conditional
and is NOT a premise. For x=(a,b), write x_n=F^n(x), S_n=a_n+b_n and

    Lambda(x)=lim beta^(−n) S_n,
    S_n=beta^n Lambda(x)+E_n, 0≤E_n≤48.          (0.1)

The error formula comes from ordinary remainders r_n∈[0,29], s_n∈[0,19]:
S_(n+1)=beta S_n−(r_n+s_n)/10 and
E_n=(1/11) sum_(j≥0)(r_(n+j)+s_(n+j)) beta^(−j).
For official starts Lambda≥1. All these are REAL limits. The finite
shift identities below can be evaluated on auxiliary Z², but no
10-adic point is claimed to be a positive ordinary start.

For coordinatewise ordered x≤y, put

    (u_n,v_n)=F^n(y)−F^n(x), W_n=u_n+v_n.

Cooperation makes u_n,v_n nonnegative nondecreasing integers. In
particular

    Lambda(y)=Lambda(x) iff W_n≤48 for every n;    (0.2)
    W_m≥49 implies Lambda(y)−Lambda(x)≥beta^(−m).
                                                        (0.3)

Indeed equal growth gives W_n=E_n(y)−E_n(x)≤48. Conversely a bounded
W_n vanishes after division by beta^n. For(0.3), subtract(0.1) at m;
the error difference is at most48. Thus crossing49 is an actual
all-future certificate of unequal growth, not just a finite discrepancy.

The older accepted fixed-offset density theorem's common-shift/lifting
method and finite block deletion are attributed. Its COMPLETE v3 proof
and MD/JSON authority were read, including the repaired all-prefix
uniformity. The NEW step here is a uniform COUPLED escape for ordered
separations, followed by actual growth counting. No new rational-base
theorem or novelty of the older lifting/counting method is claimed.

Fix universal constants

    M=32, B=10^32, eta=log(B−1)/log(B), 0<eta<1.   (0.4)

They are deliberately nonoptimal. No table or scan determines them.

**D6A — uniform coupled escape and the exact permanent exception.**
Let x be an official start and y=x+(u,v), where u,v≥0 and u+v>0.
If (u,v)=(1,0) and the first coordinate of x is even, then for EVERY
integer t≥0 the two starts x+60t(1,1), y+60t(1,1) have equal growth
and are permanent gap(1,0) twins. In every other case, after ANY prefix
class t=r mod10^N, at least one of its B refinements modulo10^(N+M)
has separation W_(N+M)≥49 for EVERY ordinary parameter in that class.
The same M works after every surviving prefix, at every ordinary size.

**D6B — power-sparse actual equal-growth parameters.**
For any nonexceptional ordered pair in D6A and any integer H≥1,

    #{0≤t<H: Lambda(x+60t(1,1))
                   =Lambda(y+60t(1,1))} ≤ B H^eta.   (0.5)

More precisely at most(B−1)^k residue classes modulo B^k can have
W_(Mk)≤48. The equal-growth set has natural density0. Thus the
permanent parity twin is the ONLY nonzero ordered gap with equal
growth for ALL sufficiently large common diagonal translates.
No assertion that the nonexceptional exceptional set is empty follows.

**D6C — actual growth spectrum on every fixed-difference line.**
Fix any integer d. Among official starts x_b=(b+d,b), b≥b_*(d), the
sequence L_b=Lambda(x_b) is nondecreasing. Its adjacent equalities
satisfy

    #{b_*(d)≤b≤H: L_(b+1)=L_b}=O_d((H+1)^eta).     (0.6)

Hence the first H−b_*+1 legal starts have
H−b_*+1−O_d((H+1)^eta) DISTINCT real growth values. If N_d(X) counts
distinct such values at most X, then

    N_d(X)=X/2+O_d((X+1)^eta) as X→infinity.        (0.7)

This is an actual counting statement, not an algorithm deciding exact
membership, a uniform real spacing, a two-dimensional density theorem,
or a hitting/avoiding classification.

**D6D — arbitrarily small CERTIFIED positive ordinary growth gaps.**
For every integer N≥0 there is an ordinary t_N with1≤t_N≤B such that
the two official starts

    x_N=(60*10^N*t_N+22,60*10^N*t_N+16),
    y_N=x_N+(1,1)                                 (0.8)

have initial difference a−b=6 and

    beta^(−N−M) ≤ Lambda(y_N)−Lambda(x_N)
                                    ≤50 beta^(−N).  (0.9)

Thus these are genuinely DISTINCT growth values tending arbitrarily
close, not finite shadows whose growth equality remains undecided.
Both starts have coordinate size at most60B10^N+23. No useful lower
spacing bound for all starts of a given size, and no hitting conclusion,
is asserted. A finite choice construction, without computing t_N or
enumerating trajectories, proves the claim below.

## 1. Finite phase control of TWO actual orbits

The exact identity, already present in the accepted older work, is

    F(z+60h(1,1))=F(z)+66h(1,1) for z∈Z²,h∈Z.   (1.1)

If the initial common parameter t changes by10^m h, then at every
0≤j≤m the two trajectories change by the SAME vector

    60*11^j*10^(m−j)h(1,1).                     (1.2)

This follows by induction while the shift is divisible by60. Their
separations and ordinary remainders through time m are unchanged.
One further application of(1.1) at time m gives the time-(m+1)
common shift

    6*11^(m+1)h(1,1).                            (1.3)

In particular, after fixing parameter digits through modulus10^(j−1),
the next digit h=0,…,9 changes the two time-j states by(1.3) with
m=j−1. Since 11^j=1 mod10, their residues modulo60 are shifted by
6h in BOTH coordinates. The separation at time j is unchanged.
These are exactly the ten points of one common diagonal residue class
modulo6. Later parameter digits, divisible by10^j, do not alter this
choice or any previous remainder/separation data.

This applies after ANY prefix t=r mod10^N, starting with its first free
phase at time N+1. It gives one integer parameter class for each finite
sequence of successive choices, by induction on the newly selected
decimal digit. It neither controls the already fixed time-N phase nor
changes the current separation. This one-step delay is retained below.
Every resulting finite class has infinitely many nonnegative ordinary
parameters, so official base starts give actual official trajectories.
There is no inference from an infinite choice sequence to an ordinary
integer lift.

Write a,b for the current LOWER state. At one freely chosen phase,
its residues run through (a+6h,b+6h) modulo60. Four consequences will
be used separately, never as simultaneous independent controls:

1. floor(b/20) mod3 can take each value0,1,2: every20-wide slab of
   residues0,…,59 meets every class modulo6. Consequently the NEXT
   a-coordinate mod6 can be chosen as any of the three residues with
   its invariant parity, since a_next=a+2floor(b/20).
2. floor(a/30) mod2 can take either value: each half0,…,29 and30,…,59
   contains five of the ten available residues. Hence the NEXT
   b-coordinate can be chosen even or odd.
3. If a has residue4 mod6, its residue modulo30 can be set to28.
   If it has residue5 mod6, that residue can be set to29. These are
   members of the five available mod30 values; no residue lifting
   outside the common diagonal class is presumed.
4. Modulo20, the ten values b+6h run through ALL residues of b's
   fixed parity, since gcd(3,10)=1. For a gap v≥2, choose18 if b is
   even and19 if b is odd; then floor((b+v)/20)>floor(b/20).
   For v=1 this is possible exactly when b is odd, using19.

Each is a finite modular observation. The two coordinate phases are
coupled, and the proof does not ask for arbitrary independent residues.

## 2. Uniform escape: all ordered gaps and parity boundaries

At any current phase put y−x=(u,v), u,v≥0. Subtracting the map gives

    u_next=u+2A, A=floor((b+v)/20)−floor(b/20)≥0,
    v_next=v+3C, C=floor((a+u)/30)−floor(a/30)≥0.  (2.1)

The lower a-coordinate keeps its parity. Therefore a nonexceptional
ordered pair can NEVER become the excluded gap(1,0) over an even lower
a: if initial v>0 it remains positive; if initial u≥2 it remains at
least2; and the remaining gap(1,0) over odd a stays over odd a.
The case u=v=0 was excluded from the statement.

If W≥49 we are finished and monotonicity preserves that certificate.
Suppose W≤48 and the pair is nonexceptional. The following strategy
uses only successive free phases of Section1.

### A. Starting with v=0

Then u≥1. If the lower a is odd, choose one phase so its NEXT residue
mod6 is5. At the following phase set its residue mod30 to29. Since
u≥1, the upper a then crosses the next30 boundary and C≥1. Thus after
at most TWO phase decisions v≥3. If lower a is even, nonexceptionality
gives u≥2; first set its NEXT residue mod6 to4 and then its mod30
residue to28. Again C≥1 and v≥3. Any earlier increase only helps.
It would be false to assume a two-unit a-gap can cross a30 boundary
in EVERY current mod6 class; this two-phase adjustment is necessary.

### B. Starting with v=1 or2

For v=2 one free phase makes A≥1 by consequence4, so u increases by
at least2. The same is true at v=1 when lower b is odd. When v=1 and
lower b is even, first choose a phase making the NEXT b odd, by
consequence2; if v has already increased we are further ahead, while
otherwise consequence4 at the next phase gives A≥1. Thus within at
most TWO decisions u≥2 while v≥1.

If v is not already at least3, use the two-phase a-adjustment from A,
valid now because u≥2 even when lower a is even. It makes C≥1 and
v≥4. Hence within at most FOUR phase decisions this case has v≥3.
No independence of the a- and b-phase choices is required.

### C. Once v≥3

Every new phase can make A≥1 by consequence4, using an available
residue18 or19. Each such update increases u by at least2, while v
never decreases. The current W is at least3, so at most23 further
decisions give W≥3+2*23=49. This also covers u=0 at entry to this case.

All cases are therefore finished after at most4+23=27 decisions.
If the prefix was fixed through time N, its first free phase is at
N+1 and the last controlled update is no later than N+28. Our M=32
allows the remaining digits to be fixed arbitrarily. The certificate
W_(N+M)≥49 depends only on the refined class modulo10^(N+M), by
Section1. It holds for EVERY ordinary parameter in that class, not
only a selected representative. This proves the escape part of D6A
with the SAME constant after EVERY prefix, including large reached
states and arbitrary initial ordered gaps.

For the excluded pair (1,0) over even a, floor((a+1)/30)=floor(a/30)
at every step, and the b inputs coincide. Thus (2.1) leaves the gap
(1,0) forever; the lower a stays even. The same is true after every
common60t shift. This is precisely the accepted CF5 parity twin,
not a counterexample silently dropped from a generic strictness claim.

## 3. Actual growth coincidences and the power-saving count

Fix a nonexceptional ordered official pair. For each k≥0 let R_k be
the set of residues t modulo B^k for which W_(Mk)≤48. That condition
is well-defined on each residue by(1.2). Since W is nondecreasing,
R_(k+1) projects into R_k. If R_k is empty there is nothing to count.
Otherwise D6A applies to EVERY such prefix with N=Mk, and removes at
least one of its B children. Hence

    |R_0|≤1, |R_(k+1)|≤(B−1)|R_k|,
    |R_k|≤(B−1)^k.                              (3.1)

No independence/randomness is assumed. Equal growth implies membership
in every R_k by(0.2). Conversely, membership at all block endpoints
keeps W bounded by48 at all times, so does imply equal growth. This
is an exact ordinary infinite-intersection description, without an
assertion that its surviving ordinary parameters are empty.

For an integer H≥1 choose k=floor(log_B H), so B^k≤H<B^(k+1).
Each residue class modulo B^k contributes at most ceil(H/B^k)≤B
integers to0≤t<H. Thus

    #equal parameters ≤ B(B−1)^k ≤ B H^eta.       (3.2)

This is a power bound, not just an exchange of an infinite density
limit. Division by H proves natural density0 because eta<1. The
exceptional parity twin has every parameter equal by Section2, while
every other nonzero ordered pair has density-zero equal parameters.
This also proves the last assertion of D6B about equality for all
sufficiently large translates. Empty sets, small H and early escape
are included; the deliberately large constant may make small-H bounds
trivial but never invalid.

## 4. Distinct growth values on EVERY fixed-difference line

For a fixed integer d, legal starts x_b=(b+d,b) form the consecutive
integer ray b≥b_*(d), for some finite b_*. Positivity and the product
threshold are retained; they are monotone on the positive ray.
The sequence L_b is nondecreasing by cooperation and the real limit.
Adjacent starts differ by(1,1), so the excluded parity-twin gap can
NEVER occur in this comparison, at any residue or reached state.

For each of the60 residues of b modulo60 choose its first legal
representative b_r. Apply D6B to x_(b_r) and x_(b_r+1), under their
common60t translation. Summing the60 power bounds gives(0.6), with
finite starting discrepancies absorbed in O_d. The constant is uniform
in H; no difference radius growing with H or time is substituted.

For a nondecreasing real sequence, each distinct value occupies one
consecutive run. Therefore the number of distinct values in a finite
prefix is exactly its length minus its number of adjacent equalities.
This proves the first distinct-growth count; nonadjacent collisions
cannot be counted again as separate values or occur across unequal
intermediate values.

Finally(0.1) at time0 gives

    2b+d−48≤L_b≤2b+d.                            (4.1)

The set of legal indices with L_b≤X is a finite prefix whose size is
X/2+O_d(1): all b≤(X−d)/2 qualify and none with b>(X−d+48)/2 do,
apart from the fixed lower endpoint. Counting its distinct runs and
using(0.6) gives(0.7). All quantities counted are actual ordinary
trajectories and actual real growth values. This does not produce
their decimal expansions or an exact equality decision procedure.

## 5. Strictly positive gaps tending to zero, with ordinary witnesses

Apply the algebraic finite escape lemma to the ordered base pair
z=(22,16), z+(1,1), allowing the common shift60w. Although z itself
is not an official start, the finite phase lemma is valid on Z² and
supplies one residue w=r modB for which the time-M separation is at
least49. Every sufficiently positive representative is official.

For any N≥0, 11^N is a unit modulo B. Choose the unique positive
t_N∈{1,…,B} with

    11^N t_N=r modB.                             (5.1)

The starts in(0.8) are official: t_N≥1 gives lower coordinates at
least82 and76, with product>600. For0≤j≤N, direct induction gives

    F^j(x_N)=(60*11^j*10^(N−j)*t_N+22,
              60*11^j*10^(N−j)*t_N+16),
    F^j(y_N)=F^j(x_N)+(1,1).                     (5.2)

For j<N the common coefficient is divisible by10, and the remainders
22/23 modulo30 and16/17 modulo20 give equal floor quotients, so(1.1)
proves the induction. At time N the common coefficient w=11^N t_N
has the escape residue r modulo B. Therefore W_(N+M)≥49, proving
the lower bound in(0.9) via(0.3).

At time N the sum separation is exactly2. Subtracting(0.1) there
gives beta^N[Lambda(y_N)−Lambda(x_N)]≤2+48=50, proving the upper
bound. This also confirms the clock normalization: a time shift by N
multiplies the real growth by beta^N. Both starts are on a−b=6, and
their maximal coordinate is at most60B10^N+23. The upper bound tends
to0 while the lower bound stays strictly positive for every N.

The residue r can be chosen by the finite hand strategy, without a
trajectory table or an unbounded search. Its explicit decimal digits
or numerical evaluation of Lambda are not needed by this existence
proof. Unlike a finite-word lift alone, the threshold49 certifies
the infinite real growth values are different. This is the substantive
global conclusion obtained from the finite steering.

## 6. Attribution, failures and exact remaining problem

The common-shift identity and repeated-block residue counting are old
accepted methods, not newly discovered theorems. The coupled control
of ordered gaps, its exact parity exception, power-sparse actual growth
collisions, spectrum mass and certified small positive gaps are the
new proposed inferences. The original Dubickas–Mossinghoff work is
relevant for approximate-multiplication and prohibited-residue methods;
no generic residue-normality or singleton theorem is substituted for
this map-specific two-orbit proof. Exact primary read limits are in
the source packet. No external full-paper audit or priority claim.

The power-saving exponent is extremely close to1, deliberately not a
practical numerical algorithm. Even a density-zero exceptional set
can contain positive ordinary parameters. Equal growth is not merger,
does not fix the permanent displacement, and does not decide whether
either trajectory hits the diagonal. The unordered-pair case is not
silently included. CF6's tenfold existence remains unproved and unused.
No actual infinite avoider, universal hitting proof, automatic infinite
ordinary lift or effective last-event bound is claimed.

All new mathematical work is by hand. No CAS, scan, table, mathematical
program, routine test, author/source replay or finite certificate was
run. A complete obligation/check/failure/source/log/code/ALLmetadata
packet must freeze, be fully read back and separately verified before
any review handoff. Only two OTHER whole audits and coordinator
reconciliation can promote the exact claims. All older bytes remain
unchanged.
