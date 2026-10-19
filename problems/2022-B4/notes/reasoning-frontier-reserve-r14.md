# R14 reserve hand pass: an explicit positive-predecessor wedge

19 October 2026 UTC. **Exploratory / unverified throughout the NEW assertions
below.** C is the author; no independent review or acceptance is claimed.
Only open 2022 B4(b) is considered. This single short note is not a review
packet. Requested inherited gpt-6.1-sol/max; effective readback unavailable.

## Actual hypotheses and inherited boundary

Use the simultaneous physical map

    F(a,b)=(a+2 floor(b/20), b+3 floor(a/30)),
    O={(a,b) in Z²:a,b>0, ab>=600}, beta=11/10,
    Omega={x in O: F^n(x) is off the diagonal for every n>=0}.

The COMPLETE frozen PH13 constructor body was re-read for its exact
definitions; its subsequent scoped acceptance is coordinator-supplied.
Inherited PH13/CF facts, not NEW claims: the SUM growth Lambda is positive
and proper on O, Lambda(Fx)=beta Lambda(x), and IF Omega is nonempty it
has a least-growth member x*. EVERY official predecessor of x* is diagonal.
This last statement does not assert that any official predecessor exists.
The old parity-twin/source restrictions remain intact. C's PH13/CF
construction is disclosed, not independently re-certified here.

## Exploratory lemma 1: full integer preimages exist

This elementary full-lattice observation may overlap older Q inverse
results; it is not claimed as a new surjectivity method. Its purpose here
is to make the subsequent POSITIVE-domain interface explicit.

Fix an arbitrary integer target (A,B). Write A=2X+r, B=3Y+s with
r in {0,1}, s in {0,1,2}. A preimage has the form (2x+r,3y+s).
The PH13 normalization, valid also for negative integers by Euclidean
remainders, gives the exact equations

    x+floor((3y+s)/20)=X,  y+floor(x/15)=Y.

Eliminate y and define an integer function

    H(x)=x+floor((3Y-3 floor(x/15)+s)/20)-X.

When x increases by 1, floor(x/15) increases by 0 or 1. The remaining
floor therefore decreases by 0 or 1, since its numerator decreases
by 0 or 3. Hence H(x+1)-H(x) belongs to {0,1}. Also

    H(x)=(99/100)x+(3Y+s)/20-X+O(1),

with a bounded error, for positive and negative x alike. Thus H tends
to opposite infinities at the two ends of Z. The discrete intermediate
value argument gives some H(x)=0: take the first nonnegative value
after a negative one, and use the unit-step bound. Then
y=Y-floor(x/15) supplies a full integer preimage of (A,B).
No positivity or official-domain conclusion has yet been inserted.

## Exploratory lemma 2: the wedge forces EVERY preimage to be official

Suppose an actual integer preimage is (u,v). Let rho=u mod30 and
sigma=v mod20 be Euclidean remainders, including for negative inputs.
Thus 0<=rho<=29 and 0<=sigma<=19. The physical equations give

    10A=10u+v-sigma, 10B=u+10v-rho,
    99u=100A-10B+10sigma-rho,
    99v=100B-10A+10rho-sigma.

Consequently

    u >= [10(10A-B)-29]/99,
    v >= [10(10B-A)-19]/99.

Consider the explicit wedge

    W={ (A,B) in O: 10A-B>=241 and 10B-A>=241 }.

For a target in W these bounds give u>=2381/99>24 and
v>=2391/99>24. Since u,v are integers, BOTH are at least25,
and uv>=625>=600. Combined with lemma1, every target in W has
at least one official preimage, and every full integer preimage is
official. This retains the inclusive product600 boundary; the sufficient
wedge is deliberately conservative. No converse is asserted.

In particular min(A,B)>=30 and |A-B|<=29 imply membership in W:
10A-B=9A+(A-B)>=270-29=241, and likewise for the other inequality.
This is a uniform hand inequality, not a bounded-strip enumeration.

## Exploratory corollary: a minimizing avoider in W has ONE diagonal parent

Assume Omega nonempty and choose a globally least-growth x*.
IF x* belongs to W, lemmas1--2 supply an official parent. Inherited
PH13 then says every such parent is diagonal. There is at most one
diagonal parent, because the first coordinate of F(c,c), namely
c+2 floor(c/20), is strictly increasing in the integer c. Therefore
x* has a UNIQUE full integer preimage, necessarily (c,c) with c>=25.

Its gap must be one of {-1,1,2}. Indeed write c=60t+w,0<=w<60;
the launch gap is 2 floor(w/20)-3 floor(w/30), taking values
0,2,-1,1 on the four intervals separated by20,30,40. The zero case
cannot be an avoider. The additional PH13 shifted-target conditions on
this actual diagonal parent still apply, and are not reproved here.

Thus the genuinely no-official-parent branch of a minimizing avoider,
if it exists, must satisfy

    10A-B<=240 OR 10B-A<=240.

These are explicit unbounded boundary regions. Outside W a parent may
still exist; this is a necessary restriction, not an orphan criterion.

## Exact failed inference and next bottleneck

It is invalid to move x* forward until it enters a balanced region and
then apply minimality to that later state. Its growth is beta^n Lambda(x*),
strictly larger for n>0. An off-diagonal predecessor there merely recovers
an earlier avoiding state; it need not give growth BELOW Lambda(x*).
Eventual strip entry alone therefore cannot establish x* in W. Nor do
the two allowed diagonal-birth/twin conditions prove a return to zero.

The remaining useful target is either an actual avoidance-preserving
lower-growth transport from the complement of W, or control of the retained
diagonal births inside W. Neither is supplied. Full-lattice surjectivity
does not by itself settle positive-domain reachability, and the explicit
wedge repair does not erase the unbounded outside-wedge alternatives.
No infinite ordinary survivor, termination theorem or annual answer follows.

## Operations and checkpoint limits

The assigned path was narrowly checked absent before writing. No primary
source call, mathematical executable, computation/scan/CAS, old helper,
new agent, Git/shared/cache/old-byte change or review packet was used.
The proof attempts above are hand reasoning only. ONE NEW note is saved;
all assertions above their inherited interfaces remain exploratory/unverified.
Start direct telemetry:87%TOTAL at04:13:25UTC; interim87% at04:16:25UTC,
reset1792874445, ordinary usage allowed and both account views agree.
Only this window is authorized;90%TOTAL includes integration/review reserve.
Final full-note readback and end telemetry are reported to the coordinator.
