# PM8 adversarial constructor checks

2026-10-18 UTC. **Candidate proof - unverified.** C's own checks do
not replace either required OTHER whole audit. No mathematical program.

## Actual geometry instead of formal degree compatibility

The critical diagram is a genuine four-cell face, dual to a SINGLE
simple crossing. At an outdegree4 cell the middle positions2 and3 are
adjacent, so this crossing exists on its actual lower boundary. The
four sign patterns on those two wires distinguish all four cells even
if some are unbounded. The bottom cell's incoming edges share that
crossing and are adjacent in the LINEAR upper chain. They cannot be
two separated extreme edges around an unspecified cyclic boundary.

The unbounded-parent issue is handled before any minimum-degree claim:
the two middle successors are proved BOUNDED from the preceding and
following lower wires, not merely assigned indegree1. A bounded
indegree1 cell has at least two lower edges. This rules out both
forward uniques and nonterminal dead ends at those successors. Without
boundedness, an unbounded digon would defeat that particular step.

If the bottom had indegree>=3, at least one of its two adjacent incoming
edges would be incoming-middle. Rotating the middle-successor lemma
then forces its tail to be forward-unique. Both candidate tails have
already been proved nonunique. Thus indegree2 is exact. The reverse
penalty is not lost at south: south has reverse outgoing degree2 in
this case and is a reverse TAIL, while its forward degree0 is ignored.

The wire sign rank ensures there is no incomplete two-step trial.
At outdegree4 there are four distinct uncrossed exit colors, so at
least four steps remain. Ordinary rows elsewhere sum1 after WO
normalization, and every nonsouth cell has an exit. Both one-step
successes and two-step diamond continuations therefore have their
claimed full probability mass.

## Weighted events and trial boundaries

At an intermediate bad cell with huge degree, the proof sums all next
edges rather than selecting one with a falsely uniform lower bound.
Only GOOD intermediate degrees3/4 require an individual edge bound;
their minimum probability is at least mu. The uniform kappa=mu² is
deliberately weaker than a possible extreme-edge estimate and suffices.

Trials are selected by the CURRENT outdegree only. A trial ending at
level j+2 may be followed immediately by another starting there, but
the first target set is{j+1,j+2}, the second{j+3,j+4}. Their success
charges cannot reuse a target. The shared endpoint's bad flag may
help only the first trial's success, not the next. Outdegree4 at a
skipped intermediate tail is counted once and is the sole possible
extra d2 occurrence per trial, giving t>=c_F/2.

The block tree is finite and uniquely unfolds each actual path. Its
row sum is the conditional expectation of2^-Y divided by a, at most1.
No eventual c,b event changes those row weights. Restricting the final
nonnegative sum to the event is valid after the moment is established.
The orientation-reversed event uses its own adapted process; no joint
adaptation or independence between P and Q is asserted.

The quantity P(E) by itself does not bound #E. The lower bound
sqrt(P(p)Q(p))>=K^-n for EVERY same complete path and Q(E)<=1 are
what turn it into an absolute count by Cauchy. No uniform-sampling
comparison, path-count denominator or assumption gamma_n≈K^n enters.

## Hand arithmetic and exact constants

The new raw objective can be smaller than K only because d2 is
infeasible. This is preserved explicitly rather than concealed:

    L0 M0=(19/9)(171/140)=361/140,
    L0 M0²=(361/140)(171/140)=61731/19600,
    2+2/V0=221/70,
    (221/70)/(61731/19600)=61880/61731.

For the next row,

    61731*171=10556001,
    19600*140=2744000,
    (2+3/V0)=523/140,
    523*19600=10250800,
    10556001-10250800=305201.

The ratio for all d>=2 decreases and starts at

    (523/442)/(171/140)=73220/75582,
    75582-73220=2362>0.

Hence dividing d2 ONLY by chi makes every row substochastic. The
pathwise product payment is chi^(-c_F) and chi^(-c_R), giving the
half exponent only AFTER Cauchy. Its sign in (20) is negative.

For the objective comparison,

    19³=6859, 19⁴=130321, 2*9*6859=123462,
    9⁴=6561, 130321-123462-6561=298>0.

Differentiating ln L+(3/4)[ln2+ln L-ln(L²-1)] gives

    7/(4L)-3L/[2(L²-1)]=(L²-7)/[4L(L²-1)].

This derivative is strictly negative all the way to19/9 because
361<567. No wrongly continued feasible envelope or root approximation.

delta is chosen once from two positive logs, so delta>0. Since
delta ln chi<=ln(K/K0), J0<=sqrt(KK0)<K. The escape moment loses
one factor2 in the trial count and another square root in Cauchy:

    c_F>=delta*n/2 => t>=delta*n/4,
    P(E)<=a^(delta*n/8) => #E<=K^n a^(delta*n/16).

These are the exponents in the main, without an illicit improvement.
The high-b tail uses b>=eta*n and rho^(eta*n/2), correctly shrinking
because rho<1. All constants remain fixed before the arrangement.

## Remaining scope and review priority

This candidate claims neither positive bad density on every path nor
that the few-d2 family is empty. It gives a different absolute count
for that family. Factor3 in the exact low-cost premise is absorbed
using one fixed base J_L'<K and one uniform later-size threshold.
The broader count4J^n holds without that threshold and transfers by
canonical insertion, whose total prefactor contributes only O(N).

The constructor has not found a remaining proof gap, but that statement
is not promotion. The source foundations remain in their accepted
attributed scopes, no literature priority is established, and two
OTHER whole audits must test all64 obligations and the complete packet.
