# 2019 B4(b): independent adversarial second-pass review R2

Initial blind report completed 2026-10-17 (Australia/Brisbane; computations
dated 2026-10-16 UTC). Reviewer: `review_2019_renewal_r2`.
Requested settings, supplied in the delegation: `gpt-6.1-sol`, `max`.
There is no independently verified effective-setting readback.

## Finding and scope

I independently reconstructed the complete new enclosure argument and found
no unresolved substantive objection for the frozen versions listed below.
I also reconstructed the rigid collision, fixed-generator finite-presentation
obstruction, staircase, and strict finite-factor upper-approximation theorems.
The resulting partial claims are suitable for the coordinator's consideration
after the other independent audit. This report does not promote their status,
establish novelty, determine the exact growth constant, or solve all of B4(b).

In particular, the reviewed deductions support

```
C(z) = 1/(1-2z+F(z)),
F(R) = 2R-1,     sum(n f_n R^(n-1)) <= 2,
1.76521 < lambda < 1.83516197,
```

where `lambda` is the growth rate of the original distinct generated strings,
`R=1/lambda`, and `F` is the full intrinsically defined minimal-bad-factor
series. These identities do not give an explicit enumeration of all of `F`.

This initial report was completed without reading R1's reports, conclusions,
shared issue/status logs, or any other second-pass review. I read `AGENTS.md`,
the assigned checkpoint and hash lists, the three frozen candidate notes,
`statement.md`, and the accepted mathematical body of `proof.md`. I did not
read that proof's previous review files. I constructed my own programs before
opening the author's raw enumeration/certificate JSON. No author program was
imported, executed, or used as source code.

Frozen principal inputs, whose SHA-256 values I verified before reviewing:

| File under `problems/2019-B4/notes/` | SHA-256 |
| --- | --- |
| `secondpass-canonical-renewal.md` | `886266000a34023b033099889a3bb23bc6b3e642194ded12ce53b3aaa1642763` |
| `secondpass-rigidity-obstructions.md` | `58112ed40ba7146c8b5885669602d44770bdd525540c4221eaf17b101eb1c109` |
| `secondpass-staircases-and-pumping.md` | `5e2539982e32d116076c2c17ad8e85d865792a14630db04634c7372ae345cd52` |

The companion `secondpass-review-2-manifest.json` records all used local input
hashes, the final check-source hashes, and the outputs. Only this review's new
`secondpass-review-2*` files were written. No proof, shared issue log, other
owner's file, Git index, commit, or remote was changed.

## Official problem and the rate being bounded

I checked the B4 definition and part (b) against the
[official 2019 Paper B, page 2](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf)
using the primary PDF on 2026-10-17 Brisbane time. The target is the lower and
upper limiting nth-root rates of distinct admitted binary strings. The
normalization in `statement.md` matches the seed, alternating next-bit rule,
and distinct-string counting. I did not investigate or reproduce preliminary
part (a), or any other competition problem.

The accepted proof is used for the existence of the common rate `lambda`,
the infimum formula `lambda=inf C_k^(1/(2k))`, and the accepted lower anchor
`lambda >= 395397^(1/24)`. I checked that those results are used with their
actual hypotheses. A chronological left tape `u` corresponds to actual left
context `reverse(u)`, so chronological tape pairs and marked contexts are in
bijection. Thus `c_(2k)=C_k` exactly. Marking the seed introduces at most a
factor `2k+1` in the original distinct-string count, as established in the
accepted proof; no exponential factor is lost here.

Appending the mandated next bit to a fixed tape injects marked contexts into
the next layer; deleting the last move from an arbitrary history gives a
surjection from at most two next-side choices per previous context. Hence
`c_(2k) <= c_(2k+1) <= 2 c_(2k)`. The odd tape-pair layers have the same root
rate, so `C(z)=sum c_n z^n` has radius `R=1/lambda`. The new upper and lower
enclosures therefore concern the original requested rate, rather than a rate
for insertion histories or an unrelated marked model.

## Reconstruction of canonical factors and no-overlap

Context equality is preserved in any surrounding history: both histories in
an equality have the same length, and shifting their starting phase by one
complements both output tapes. The unchanged suffix consequently retains its
phase too. Equal-length lexicographic improvement of a factor improves the
whole history. Canonical histories therefore form a factorial language.
Every noncanonical word contains a shortest noncanonical contiguous factor;
the set `F` of these minimal factors is factor-free.

For `h in F`, take any smaller equal-context `g`. A common first letter
could be cancelled, giving a smaller proper suffix of `h` at the other phase;
a common last letter could likewise be cancelled to improve a proper prefix.
Thus `h,g` start `R,L` and end `L,R`, respectively. If the second letter of
`h` were `L`, its first left output bit would be 1 whereas `g`'s is 0.
If its penultimate letter were `R`, its last right bit would have the opposite
phase to `g`'s last right bit. Therefore every minimal bad factor begins `RR`
and ends `LL`, and has length at least four. This argument handles odd lengths
as well as even lengths.

Represent histories for a fixed tape pair as legal lattice paths through
consumed tape prefixes. A time layer determines the sum of the two coordinates.
If `g,h` met at an internal vertex, their prefixes would have the same two
outputs; the prefix of `g` starts `L`, improving the proper prefix of `h`
that starts `R`. This is impossible. Their left-coordinate difference starts
at 1 and changes by at most 1 per step, so it remains strictly positive at
every internal layer.

Now suppose `ab,bc in F` with `a,b,c` nonempty. The case where the overlap
would contain an entire member of `F` is already excluded by factor-freeness.
Replace `ab` and `bc` separately in `abc` by their smaller witnesses, obtaining
paths `P,Q` for exactly the same full tape pair. At time `|a|`, `P` has larger
left coordinate than `Q`; at time `|ab|`, it has smaller left coordinate.
The difference has increments in `{-1,0,1}`, so there is a common vertex at
an integer time strictly between these times. It is not merely a crossing
of geometric edges without a common legal state.

Following `Q` from the original start of `b` to that vertex and then `P` to
the original end of `b` is legal: the state is the same pair of consumed
prefixes, including the same time phase. It reads precisely the two tape
substrings read by `b`, starts `L`, and improves `b`, which starts `R`.
Since `b` is a proper factor of `ab`, this contradicts minimality. For an
overlap of length one there is no integer internal meeting layer, which
already contradicts the required sign change. This establishes the universal
cross-bifix-free assertion, including self-overlaps and all length parities;
the finite overlap tests are not its proof.

Appending one letter to a canonical prefix can become noncanonical only by
creating a forbidden suffix. The suffix is unique by factor-freeness.
Conversely a concatenation of a canonical prefix and `f in F` has no other
bad factor: an earlier one would lie in the prefix, properly contain/be
contained in `f`, or have a prohibited proper overlap with `f`. Thus its
prefix with the last letter deleted is canonical. This proves the subtraction
bijection and the exact recurrence

```
c_n = 2c_(n-1) - sum(j=1,...,n) f_j c_(n-j).
```

Each coefficient is a finite sum, so the reciprocal identity is legitimate
as a formal series even though `F` may be infinite and unclassified. The
intrinsic rewriting-system consequence also follows: a rule preserves length
and lowers lexicographic order in the finite set of histories of that length;
the only irreducibles are the unique canonical representatives. No finite
presentation or regularity assertion is needed for this conclusion.

## Reconstruction of the boundary limit, derivative, and lower enclosure

Root growth alone would not justify divergence at the radius. The additional
accepted infimum formula does: `c_(2k)=C_k >= lambda^(2k)`, so every even-index
term `c_(2k) R^(2k)` is at least 1. Thus `C(R)=infinity`, and nonnegative
coefficients imply `C(x)` tends to infinity as `x` increases to `R`.

Every minimal bad word is an extension of a canonical prefix, so
`f_n <= 2c_(n-1)`. Hence `F(x)` is finite for `0<=x<R`. Both series converge
absolutely there, so the formal identity evaluates to

```
F(x) = 2x-1+1/C(x),     D(x)=1-2x+F(x)=1/C(x)>0.
```

Taking the monotone limit of `F` gives `F(R)=2R-1` as an actual convergent
nonnegative series, not an analytic continuation. Its denominator has no
positive zero before `R` and has limit zero at `R`. If `F'(x)>2` at any
interior `x`, the nonnegative coefficients make `F'` nondecreasing, so `D`
would increase from the strictly positive `D(x)` up to the boundary. This
contradicts its zero limit. Interior differentiation is valid for a power
series within its radius. Taking the monotone boundary limit of the
nonnegative derivative series proves `sum n f_n R^(n-1) <= 2`. Equality is
not assumed, and no simple-pole assumption is used.

For exact coefficients through `N`, termwise comparison in the remaining
nonnegative tail gives

```
F(R)-P_N(R) <= R/(N+1) * (2-P_N'(R)).
```

Substitution of the root equation and rearrangement gives exactly the
stated `E_N(R)>=0`. I checked the direction of both inequalities and the
factor `2N/(N+1)`. Exactness through `N` matters: treating an incomplete
subset of short obstructions as if it were exhaustive would not justify
this tail argument. The independent enumeration below supplies exactness
through 24.

At `N=24`, my independent `Fraction` calculations reproduced the author's
complete reduced numerators and denominators for all four sign certificates.
In particular

```
E_24(100000/176521) < 0,
E_24(3/5) = -60351636099623798/1490116119384765625 < 0.
```

The accepted anchor implies `R<3/5`; independently I obtained

```
395397*(3/5)^24 - 1 = 52067146660587332/59604644775390625 > 0.
```

Since every coefficient of `E_24` above degree one is nonnegative, it is
convex on the positive axis. A convex function is bounded above by its
endpoint chord on this interval, so it is strictly negative throughout
`[100000/176521,3/5]`. Together with `E_24(R)>=0` and `R<3/5`, this forces
`R<100000/176521`, proving the strict lower bound `lambda>1.76521`.
None of the displayed floating-point root estimates enters this inference.

## Independent finite enumeration and upper enclosure

My checker uses a backward Boolean feasibility table on `(i,j)` tape-prefix
states, followed by greedily choosing `L` whenever that choice admits a
completion. Each transition checks the mandated bit `(i+j) mod 2`.
This computes the lexicographically least history for a given raw tape pair.
I also wrote a separate forward integer path-count recurrence.

To check this machinery without relying on any author certificate, I grouped
every raw history in lexicographic order by its pair of tapes for each length
0 through 14. For every history, the DP's canonical/noncanonical answer
agreed with its first occurrence in that grouping. The canonical counts were

```
1,2,4,8,15,28,52,96,177,326,600,1104,2030,3732,6858.
```

For the full minimal-factor computation I started from no known obstructions
and proceeded through every length 4 to 24. At each length I generated every
history with the proven prefix `RR` and suffix `LL`, pruning a branch only
when it already contained a previously found shorter minimal bad factor.
A surviving noncanonical word must be minimal by induction on length; I
additionally checked its longest proper prefix and suffix afresh with the DP.
Those two factors contain every proper contiguous factor. No `RLL` suffix,
run bound, or context statistic was imposed on this full enumeration.

The independently obtained nonzero counts were

| Length | 4 | 12 | 14 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Count | 1 | 1 | 2 | 3 | 2 | 4 | 8 | 6 | 20 | 14 | 40 | 42 |

The total is 143; all other positive lengths through 24 have zero count.
All ordered pairs of these words, including equal pairs, were separately
checked for proper suffix-prefix overlaps and proper factor containments;
there were none. Only after this independent result existed did I read the
author's raw `secondpass-probe20.json` and
`secondpass-full-obstruction24-v2.json`. Their union agrees with my complete
word set exactly, not just by coefficient counts. The reciprocal recurrence
also gives `c_24=2985943`, matching the accepted context count.

Let `d_n` count avoidance of this finite set. The same no-overlap bijection
gives its generating function `G(x)=1/D_24(x)` formally. Its counts are
positive and submultiplicative, since splitting an avoiding word produces
two avoiding words injectively. Thus their root rate `rho` exists as an
infimum, and `d_n>=rho^n`. The radius `r=1/rho` is finite and positive
(`1<=d_n<=2^n`), and `G` diverges at `r`. For `x<r`, `D_24(x)=1/G(x)>0`;
continuity of this polynomial and the divergence give `D_24(r)=0`.
This proves that `r` is its first positive zero; numerical root matching is
unnecessary.

My exact arithmetic reproduces

```
x0 = 100000000/183516197,
D_24(x0)>0,     D_24'(x0)<0.
```

Since `D_24''>=0` on the positive axis, its derivative is negative throughout
`[0,x0]`; hence its value is at least `D_24(x0)>0` there. Its first positive
zero satisfies `r>x0`, so `rho<1.83516197`. Canonical histories avoid the
finite set, giving `lambda<=rho<1.83516197`. The use of a strict upper bound
for `rho` makes the claimed strict bound for `lambda` valid even without
the stronger strictness theorem below.

## Rigid collisions and fixed-generator finite presentations

I reconstructed both branches of the `p,q>=1` rigidity lemma symbolically.
For the branch starting `A`, the right tape's initial `01` forces `C` next:
taking `D` instead would leave both heads at 1 at a zero step. While `q-1`
is positive, taking a cross-tape `B` instead of the required `A` leaves the
same fatal pair of heads. The residual `001` forces the first `B`; taking
`A` instead of the second `B` would exhaust the left tape while the right
still begins 1. The analogous obstruction forces the `p-1` copies of `D`,
and the final residuals `1,001` force `C D`. Tape exchange gives exactly the
other branch. Empty powers for `p=1` or `q=1` do not invalidate any step.
Direct concatenation verifies the two claimed tape outputs.

The two full histories differ at both endpoint letters. Any nontrivial
alternative for a proper contiguous factor could be spliced into its full
history while preserving at least one endpoint, producing a third history
distinct from both displayed ones. Therefore every proper factor has unique
context. This validates the minimal bad factors `H(p,q)` and their exact
subfamily contribution `z^12/(1-z^2)^2`; the two parameters are recoverable
from distinct interior even runs, so there is no double counting.

For any proposed finite set of sound equations on the fixed history
generators, choose such an `H` longer than every equation side. All matches
are then proper factors with unique context, so only trivial equations can
act, in either direction. This isolates `H` despite its other equal-context
history. A sound equation must preserve length because the total tape output
length determines it. The identical argument works on the four blocked
generators: their length is half the unblocked length, and a proper blocked
factor is a proper unblocked factor. This does not concern presentations
with extra auxiliary generators, or imply nonregular normal forms or
nonalgebraic growth.

As finite corroboration, my separate forward DP counted exactly two histories
for all 100 pairs `1<=p,q<=10`, verified both outputs and the lexicographic
minimum, and checked the proper-prefix/suffix canonicity.

I also reconstructed the fixed-window scheduling counterexample: after an
initial `D`, the left double-one run can never be consumed without leaving
both heads at 1 at a zero step. The right tape must eventually exhaust,
making completion impossible. The displayed `A`-initial witness is valid.
Taking sufficiently large `p,q` makes both swapped inputs identical in any
prescribed front/back windows, including equal tape lengths, while requiring
opposite first choices. I checked these statements by the independent DP
for `0<=p,q<=10` and checked the stated small greedy and range-statistic
counterexamples. These are supplementary to the enclosure.

## Staircases and strictness of every finite factor approximation

I derived the staircase context and forced-choice table by run consumption,
rather than inferring it from the finite two-history counts. The run list is
symmetric with an even number of runs; paired equal-length runs have opposite
bits, giving equal zero/one multiplicities and length `n(n+1)`.

For ascending `P_j`, its start time is `j^2+1`, so its contributions are
exactly those stated in the note. Before its final doubled `R`, the left
tape has consumed runs 1 through `j`, so its next run has length `j+1`.
The right tape has one bit remaining in that same-index run and a following
opposite bit. This proves the ascending row for every `j<=n-1`.

Before the central block, the left tape has consumed runs 1 through `n-1`;
the right has consumed runs 1 through `n` and the first bit of run `n+1`.
The alternating part of the central block leaves one bit of left run `n`
and exhausts right run `n+1`. Hence before the central `LL` the other run
has length `n-1`, or the tape is empty for `n=1`.

For the descending induction, at the start of `T_j` the right tape has an
entire run of length `j`, and the left has `j` bits remaining in the opposite
run. The `j` right moves exhaust that right run. Before the final doubled
`L`, one left bit remains while the right's next run has length `j-1`.
The extra `L` consumes the first bit of the next opposite run, leaving the
same induction state for `j-1`. If that other run has length one (`j=2`,
or the central `n=2` case), it is its tape's final run; choosing it exhausts
the tape and fails. If it has length zero there is no alternative side.
These calculations include `n=1,2` and `j=1,2` explicitly.

At any genuine two-head choice, the next move must come from the chosen tape
again. Thus such a choice occurs only at a doubled run, and the table leaves
only the initial choice unrestricted. The explicit history supplies a valid
completion on that choice. Tape exchange gives the other completion, proving
exactly two histories for every staircase. The distinct endpoints then prove
all proper factors unique exactly as for the rigid family. Hence every `h_n`
is a minimal bad factor, with unbounded length and runs at most two. Positive
even inflation makes a run longer than two, so finitely many bases under
only such inflations cannot generate all these words.

My finite checks verified tape equality, exactly two paths, the branch
conditions, and proper-prefix/suffix canonicity for `1<=n<=15` (up to 480
history letters and 58,081 grid states). These checks corroborate, rather
than replace, the preceding unrestricted argument. A separate exhaustive
bounded-run enumeration through 26 reproduced the fourteen factors with
counts `4:1,12:1,17:2,20:1,22:4,24:1,25:4`. All fourteen have exactly two
full histories by my DP. All 143 full factors through 24 parity-compress to
minimal factors; the note correctly leaves general compression unproved.
The stated inflation counterexample has a noncanonical proper prefix in my
independent checker, so arbitrary minimality-preserving run inflation is
indeed refuted. Matched-bit insertion of two same-side moves is sound because
the inserted bits agree and later phases are unchanged.

For finite `S subset F`, choose an integer `M>=1` at least every length in
`S` (this also treats `S` empty). I checked the bridge `(RL)^M` including
both boundaries. No forbidden word can finish in its interior, because it
ends `LL`; none can start in its interior or across its last boundary,
because it starts `RR` and the bridge ends `L`. Any forbidden word that
starts in `a` and ends in `b` crosses all `2M` bridge letters and is too
long. Thus every pair of allowed words can be connected.

At block length `m=|h_n|>max(lengths in S)`, take the finite graph with
allowed `(m-1)`-words as vertices and allowed `m`-words as edges. The bridge
makes this graph strongly connected, not just its maximum-growth component.
The all-`L` vertex has a loop. The word `h_n` avoids `S`, so it is an actual
edge. Adding it as a forbidden word deletes that edge from the same finite
irreducible adjacency matrix `A`, yielding `0<=B<=A`, `B!=A`. Counts of
long allowed words are sums of entries of powers of these matrices, so their
root rates are their spectral radii. No claim that the smaller matrix stays
irreducible is needed.

The stated finite Perron--Frobenius comparison is valid: if the radii were
equal, a nonnegative right Perron vector of `B` and a positive left Perron
vector of `A` imply `(A-B)x=0`. Then `Ax=rho(A)x`, and irreducibility makes
`x` positive, contradicting the nonzero nonnegative matrix `A-B`. Therefore
`lambda<=rho(B)<rho(A)`. A finite sound lex-decreasing rule list reduces to
this case by choosing one minimal bad factor inside each left-hand side:
avoidance of the chosen factors is contained in avoidance of that rule list,
so the latter's rate is also strictly above `lambda`. I found no missing
matrix hypothesis or reversed inclusion in this deduction.

## Adversarial issue log and limits

No substantive issue remains open in the reviewed chain. The following were
specific challenges resolved by the reconstruction, rather than assumptions
accepted from numerical agreement.

| ID | Challenge | Resolution |
| --- | --- | --- |
| R2-C1 | Crossing paths might not share a legal splice state. | Time-layer coordinate differences are integer and change by at most one; equality determines both consumed prefixes and the phase. |
| R2-C2 | The overlap could have length one or contain an entire obstruction. | The former cannot accommodate the sign change; the latter is excluded by factor-freeness. |
| R2-C3 | A power series need not diverge at its radius. | Here the accepted infimum formula bounds every even boundary term below by 1. |
| R2-C4 | The derivative or root equation might require continuation or a simple pole. | Interior absolute convergence and monotone boundary limits suffice; neither extra hypothesis is used. |
| R2-C5 | Partial obstruction data might invalidate the tail bound. | Full independent length induction reproduces all 143 words through 24, without the rejected `RLL` restriction. |
| R2-C6 | A positive denominator at one rational point might miss an earlier root. | The derivative sign plus convexity makes the denominator positive throughout the whole preceding interval. |
| R2-C7 | Marked/chronological contexts might bound a different exponential rate. | Tape reversal is a bijection, marking has only a linear multiplicity, and the accepted rate theorem applies. |
| R2-C8 | Rigidity might fail at an empty power or a staircase endpoint. | Forced residuals cover `p,q=1`, `n=1,2`, `j=1,2`; proper-factor replacements preserve an endpoint distinguishing the two histories. |
| R2-C9 | Removing an allowed edge might leave the spectral radius unchanged. | The bridge proves irreducibility of the entire finite block graph, which is the necessary strict-comparison hypothesis. |

I did not rerun the author's historical node-cap/timing claims, rejected v1
enumerator, the family-only fourteen-state characteristic polynomial, or
the complete 152-inflation/1791-state experimental model. None is used in
the reviewed new enclosure, rigidity, staircase, or strictness proofs.
The specific negative examples and the restricted-count/compression data
discussed above were checked independently. No theorem about rationality,
algebraicity, an unrestricted compression grammar, or global novelty has
been established or implicitly accepted by this report.

## Reproduction and operational record

The independent implementation is `secondpass-review-2-check.py`; its final
SHA-256 is `1f281f1463f6f51e9ee2a26d0dae7ff8129341c993ee86846846899946876aab`.
The runner is `secondpass-review-2-run.py`, SHA-256
`cba846cb30e359781cc7b189cebfe8b0479df78ba58d86227ec03083a8a3a435`.
It records the exact child command, PID, source hashes, timeout, timestamps,
status, and return code before/after each child. Each child has an explicit
60-second wall timeout; timeout cleanup addresses only that child PID.
All children completed normally, and there are no live review jobs.

The runtime was `/usr/local/bin/python3`, Python 3.15.0, with only the standard
library (`Fraction` for rational arithmetic); no package was installed and
no native CAS was used. The final enumeration child completed in 5.91 seconds
of runner wall time, visiting 425,893 prefixes and testing 74,645 full words
at length 24. Different node-count conventions explain why these prefix
counts differ from the author's; the candidate leaf counts and final word
sets agree. Incremental checkpoints every 100,000 prefixes are in its log.

From the repository root, the final checks were run in this dependency order
(independent commands within the first group may run concurrently):

```sh
python3 problems/2019-B4/reviews/secondpass-review-2-run.py factors-final enumerate --maximum 24 --timeout 60
python3 problems/2019-B4/reviews/secondpass-review-2-run.py brute-final brute --maximum 14 --timeout 60
python3 problems/2019-B4/reviews/secondpass-review-2-run.py families-final families --timeout 60
python3 problems/2019-B4/reviews/secondpass-review-2-run.py bounded-final enumerate --maximum 26 --bounded-runs --timeout 60
python3 problems/2019-B4/reviews/secondpass-review-2-run.py signs-final signs --enumeration problems/2019-B4/reviews/secondpass-review-2-factors-final.json --timeout 60
python3 problems/2019-B4/reviews/secondpass-review-2-run.py extras-final extras --enumeration problems/2019-B4/reviews/secondpass-review-2-factors-final.json --timeout 60
python3 problems/2019-B4/reviews/secondpass-review-2-run.py compare-final compare --enumeration problems/2019-B4/reviews/secondpass-review-2-factors-final.json --timeout 60
```

Each produces a correspondingly named `.json`, `.log`, and `-job.json`.
The earlier unsuffixed outputs and job records are retained as exploratory
checks from before check-source finalization; the `-final` jobs above are
the source-hashed reproducible review evidence. No run timed out or hit a
search cap. The mathematical proofs are the unrestricted arguments above;
finite computations supply exact finite coefficients and corroboration.

The coordinator supplied authoritative weekly usage of 7% total used at
delegation, below the 90% stop threshold; telemetry ownership remains with
the coordinator. No separately billed API, paid source, credential, or
authentication data was used. The official PDF was read through the primary
web source without downloading or committing a full third-party paper.
This completes the initial blind R2 report; any later cross-review discussion
must be recorded separately rather than altering this independence record.
