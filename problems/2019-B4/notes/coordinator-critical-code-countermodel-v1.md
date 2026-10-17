# A critical non-overlap countermodel and the missing actual-language input

2026-10-17 UTC. **Candidate proof - unverified / research note.**
Root construction; not an accepted result and not a statement about
the actual canonical obstruction set. Two other whole audits are
required before promotion. No computation or external theorem was
used for the algebra below. No annual answer or novelty is claimed.

## The model and exact elementary calculation

Consider the DIFFERENT forbidden family

    Fstar={RR(LR)^kLL:k>=0}.

Each word has only its initial RR and terminal LL as double letters.
No proper suffix starts RR, whereas every family prefix of length>=2
starts RR. Length1 suffix L also differs from prefix R. Thus there
is no proper suffix-prefix overlap between any two members. No member
properly contains another: an occurrence would have to start at the
unique RR and end at the unique LL, hence be the entire word. This is
a genuine factor-free cross-bifix-free binary family, all words
starting RR, ending LL, with shortest member RRLL.

Let Kstar be its factorial avoidance language and a_n its counts.
Every a_n is positive (all-L and all-R are allowed). The same elementary
append-and-remove bijection as for accepted canonical renewal applies:
a new forbidden suffix is unique, and another crossing forbidden
factor would contradict non-overlap. Thus, as formal power series,

 Fstar(z)=z^4/(1-z^2),
 Astar(z)=1/[1-2z+Fstar(z)]
         =(1-z^2)/(1-z-z^2)^2.

Put Rstar=(sqrt(5)-1)/2 and lambda_star=1/Rstar=(1+sqrt(5))/2.
The factor1-z-z^2 has a simple zero at Rstar, its other zero has
modulus lambda_star>1, and the numerator1-Rstar^2 is positive.
Consequently the displayed rational function has a DOUBLE positive
pole at Rstar and no other pole of equal modulus. Partial fractions
therefore give a_n~K*n*lambda_star^n for a positive constant K:
K=(1-Rstar^2)/[Rstar^2*(1+2Rstar)^2]>0. This follows directly by
expanding the nonzero coefficient of(1-z/Rstar)^-2, with remaining
simple-pole and exponentially smaller terms.

In particular the growth root is lambda_star and a_n/lambda_star^n
is UNBOUNDED. The denominator Dstar has derivative0 at Rstar,
so Fstar'(Rstar)=2. Its second derivative is finite because Rstar<1
and Fstar's only poles are at+/-1. This is exactly the critical,
finite-second-moment regime in the accepted renewal analysis,
realized by a non-overlap binary avoidance language. Its ratios also
satisfy the signed-recurrence monotonicity conclusion proposed in MR1.
Thus non-overlap, the RR/LL endpoints, positivity, shortest length4,
ratio monotonicity and finite second moment do not FORCE positive
renewal defect or bounded joining. None is a proof for our actual K.

One can see joining failure without asymptotics. Any finite word
which has an RR occurrence followed later by an LL occurrence contains
some RR(LR)^kLL: choose adjacent double-letter occurrences where
the type changes RR to LL; with no intervening equal adjacent letters,
the middle is alternating LR. Therefore no bridge of ANY length joins
u=RR to v=LL in Kstar. Both endpoints individually are allowed.
Conversely every forbidden model word has that pattern, so this is
also a direct avoidance characterization. The choice of last RR before
the first later LL gives the same argument, including overlapping
RR runs and LL runs by selecting adjacent equal-letter pairs.

## Why this is not the actual canonical language

The model has a forbidden word RRLRLL of length6. The actual accepted
canonical obstruction coefficients have f6=0 and f12=1; its complete
first length12 obstruction is

    RRLRRLRLLRLL.

In fact this actual minimal bad factor CONTAINS the canonical word
RRLRLL as its positions4 through9 (one-based). Therefore a tempting
universal separator RRLRLL fails for the actual family too: take
u=RRL and v=RLL, which are canonical as all length3 words are;
then u*(RRLRLL)*v is the actual length12 obstruction. The empty
bridge for this particular pair may work; this only disproves this
ONE fixed separator, not bounded joining with a variable bridge.

The earlier finite C3 diagnostic remains finite evidence only; it
is neither needed nor rerun here. No larger joining scan is substituted
for a structural argument. The model demonstrates the exact generic
shortcut that is unavailable. A proof choosing the actual positive-
defect regime must use more than the non-overlap axioms listed above.
The separate MR2 theorem remains CONDITIONAL on a uniform bridge bound;
this note neither proves nor refutes that hypothesis for actual K.

## Sources and preservation

The append/remove reasoning is reconstructed here and attributed in
method to the accepted2019 canonical renewal body. The actual f6 and
length12 word are the already accepted exact finite-prefix data, not
a new enumeration. Root read that entire canonical-renewal construction
again in this return. Earlier MR/accepted bytes are unchanged. The
rational partial-fraction computation is hand algebra, not a new CAS
certificate. This whole note remains unverified until two other audits;
its model must never be relabelled an actual-language counterexample.
