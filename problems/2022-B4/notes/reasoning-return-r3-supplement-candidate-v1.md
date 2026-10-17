# Postfreeze supplement: restricted conjugacy and arbitrary finite carry initialization

2026-10-17 UTC. **Candidate proof - unverified.** Same constructor and
requested settings as reasoning-return-r3-candidate-v1.md. No independently
verified effective-setting readback. Two fresh independent whole audits
must include this supplement before any of its claims are promoted.

The original candidate, log, sources and freeze are unchanged. This
supplement adds two deductions and makes one source-alphabet distinction
explicit. It does not repair a reviewer objection; no peer review of
the new 2022 packet has been read by its constructor.

## S1. The restricted family has eight parallel one-step ceiling orbits

Use the original candidate's A/B family and full-time quotient Q_n.
Its corrections h_n are in {-1,0,1}, with blocks (0,0) or (-1,1).
If this family had an ordinary positive integer lift, all quotient
values would be at least 81: the initial block criterion gives
Q_0=0 or81 mod100 and Q_0>0, and both intermediate positive steps
increase Q. In particular subtracting any c in {1,...,8} stays positive.

For each such fixed c set Z_n^(c)=Q_n-c. Exactly,

    10 Z_(n+1)^(c)=11 Z_n^(c)+(h_n+c).

Since 0<=h_n+c<=9, the correction is the unique canonical
ceiling correction for this integer state. Therefore

    Z_(n+1)^(c)=ceil(11 Z_n^(c)/10),  c=1,...,8.

These eight scalar orbits remain consecutive at every time.
For c=2,...,8 the correction is never zero. Because the
canonical correction is -Z mod10, these seven positive
scalar orbits would never be divisible by 10.

This restricted conjugacy is compatible with the full-controller
obstruction R3. It expressly shows why that theorem cannot be
applied to an arbitrary restricted input language.

A sufficient external statement for excluding this A/B family
would consequently be the following weak scalar residue property:
every positive ceil(11Z/10) orbit eventually has a term divisible
by 10. No proof of that property is supplied. The primary
Andrieu–Eliahou–Vivion paper still treats the stronger all-residue
termination/letter-occurrence assertions as conjectural; its
normality conjecture would imply the needed property. This is
another conditional obstruction, not an unconditional conclusion
about contest integers.

## S2. Uniform bounded carries fail even with input-aware initialization

The full-controller hypothesis remains essential. Work in the
accepted full ten-control strip system. A unit-quotient-offset
normalization means integers k_n with transformed digits

    delta_n=h_n+10k_(n+1)-11k_n in {0,...,9}.          (S2.1)

For given current k_n and h_n, the next carry is forced:

    k_(n+1)=ceil((11k_n-h_n)/10).

Thus the sole freedom for a fixed control word is k_0.
Even allowing a rule to inspect the entire ordinary initial
integer, its canonical prefix, or the future control word
before selecting k_0 does not change the continuation
once that integer carry has been selected.

**Claim S2.** For every proposed uniform integer bound K>=0,
there is one finite controller prefix from (d,r)=(1,0)
for which every initial k_0 in {-K,...,K} violates
|k_n|<=K somewhere in that prefix. This prefix has
arbitrarily large positive integer lifts in the official
domain. Therefore no uniformly bounded integer-offset
normalization to ceiling digits exists for the entire
positive-integer family, even with arbitrary initialization
in a finite set or a noncausal choice of that initialization.

This is stronger than R3's fixed-initial-carry conclusion.
It does not exclude scaling Q, unbounded offsets, a
nonuniform bound depending on Q_0, or a normalization
that outputs the larger base-p alphabet.

### Uniform escape from a suitable next state

The original candidate constructs a bounded REAL shadow
Qhat for every full controller word, independent of its
Z10 or ordinary integer lift. If the starting state has
t=2r+d, its shadow sum gives

    -t/120 <=Qhat_0<=(48-t)/120.

For states with 11<=t<=57 this interval guarantees,
for every integer initial carry m and every finite
uniform average of future controls,

    |m+9/2+Avg Qhat_0|>=1/40.

Indeed, for m>=-4 the expression is at least
1/2-57/120=3/120. For m<=-5 it is at most
-1/2+37/120=-23/120.

The finite averaging identity (R3.4) therefore implies
from ANY such state and ANY initial integer carry m

    max_(length-N controls) |k_N|
      >=(1/40)(11/10)^N-29/2.                       (S2.2)

No independence assumption about an integer orbit
enters this exact ten-branch average.

From any current controller state S=(d,r), its next
difference d' is fixed and lies in [-13,23]. The
ten controls let its next residue be the unique
representative r' in {12,...,17} congruent to r+c
mod6. Then

    11 <=2r'+d'<=57.

Thus any current state has an available one-step
transition to a state where (S2.2) applies.

Choose once an integer N=N(K) with
(11/10)^N/40-29/2>K. From any current state and carry,
there is an extension of length at most N+1
forcing |k|>K: first use the specified next residue;
if the carry has already escaped, stop, and otherwise
apply (S2.2). This is an existence argument with
fixed finite averages, not an executed search.

### One prefix eliminates all possible initial carries

Start with the 2K+1 possible initial integers m in [-K,K].
If any have violated the bound on the current prefix,
mark them eliminated permanently. For a remaining m,
its current carry and controller state are known
from the chosen prefix. Append one escape word as
above. At least that m is eliminated. Repeat for
any remaining m.

After at most 2K+1 extensions, all initial choices
are eliminated. The resulting SINGLE control prefix
has length at most

    (2K+1)(N(K)+1).

It is independent of how a proposed normalizer would
choose among the initial carries. That choice is
already covered by eliminating every possible m.
No assumption that a carry cannot return inside
[-K,K] is needed: one earlier violation is enough.

Finally lift this finite control prefix from initial
state (1,0), using the accepted finite lifting
bijection. Choose an arbitrarily large positive
integer Q_0, in its prescribed congruence class,
with Q_0>K. Then (a_0,b_0)=(60Q_0+1,60Q_0)
is an official admissible start. Every putative
initial carry in [-K,K] fails on its actual prefix.
If the carries had remained bounded, the shifted
integer scalar state would have been positive too.
This proves S2 for the actual positive-integer
family, rather than only for some irrational
infinite controller word.

The obstructing prefix may pass through equality.
S2 makes no assertion that every equality-avoiding
restricted controller has this property. In
particular S1 gives a valid bounded constant
offset on the A/B language.

## The published transducer has a different output alphabet

Akiyama–Frougny–Sakarovitch Proposition 13 normalizes
finite signed words to digits {0,...,p-1}; for
p=11 this is {0,...,10}. S2 requires the STRICTLY
smaller alphabet {0,...,9}, whose integer update
is the scalar ceiling/minimal branch. Digit 10
cannot be silently discarded when attempting to
use that published normalizer.

Its right reading direction and final-output boundary
also differ from the original R3 setup. S2 closes
the finite-initial-choice loophole for the smaller
ceiling alphabet; it still does not contradict
the published right transducer. An automaticity
or ordinary-integer coding theorem has not been
deduced from the controller.

## Source checks, computation, and audit boundary

S1 and S2 have complete hand proofs here and depend
on the frozen candidate's exact quotient equations,
finite lifting and real-shadow identities. No
enumeration, CAS, orbit search, source download
or separately billed API was used.

After the original freeze, the original AFS author
PDF was additionally read at Proposition 37,
Corollary 38 and nearby Section 5 limits. Its
at-most-two-expansions conclusion requires
p>=2q-1, failing for 11/10. AEV's introduction
and Section 3.3 distinguish the much weaker
zero-letter question from a proved theorem.
No unrestricted scalar residue-escape theorem
was located or applied. The broad web queries
for 11/10 were a bounded search, not a proof
of absence from the literature.

The original candidate's high-complexity irrational
family and uniform real growth statement are
unchanged. Universal equality, the stopped
121/100 instance, and high-complexity integer
avoiding paths remain unresolved in this work.
Only the coordinator can accept anything after
both independent whole audits, including this
supplement's additional arguments.
