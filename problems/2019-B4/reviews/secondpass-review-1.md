# 2019 B4(b), second pass: blind independent review R1

Completed 2026-10-17 Australia/Brisbane (2026-10-16 UTC).
Reviewer: `review_2019_renewal_r1`, distinct from the proof author.
Requested settings: `gpt-6.1-sol`, `max`; no independent effective-setting
readback was available. No other new reviewer report or conclusion, shared
issue log, or shared status log was read before this report was completed.

**Verdict:** I recommend accepting the mathematical partial results specified
below. I found no substantive unresolved objection after reconstructing the
whole chain, checking the boundary cases, and independently reproducing the
decisive finite certificates. This is one independent audit, not a promotion:
the coordinator must obtain the other blind audit and resolve any objections
from it. The exact growth constant remains undetermined, and B4(b) remains
open within this work.

## Frozen scope and source fidelity

The three principal audited notes have exactly the assigned SHA-256 values:

| File in `problems/2019-B4/notes/` | SHA-256 |
| --- | --- |
| `secondpass-canonical-renewal.md` | `886266000a34023b033099889a3bb23bc6b3e642194ded12ce53b3aaa1642763` |
| `secondpass-rigidity-obstructions.md` | `58112ed40ba7146c8b5885669602d44770bdd525540c4221eaf17b101eb1c109` |
| `secondpass-staircases-and-pumping.md` | `5e2539982e32d116076c2c17ad8e85d865792a14630db04634c7372ae345cd52` |

I also audited checkpoint 2, hash
`fbe7680f25cfcc216449e48755e87fa261d7c468721928075de0710f7b77d961`,
and its length-24 numerical enclosure. All 14 entries of the checkpoint-1
manifest and all 16 entries of the checkpoint-2 manifest independently matched
their hashes. These checks are recorded in `secondpass-review-1-evidence.json`.

The official cached Paper B, page 2, matches the normalized rule and the
liminf/limsup target in `statement.md`. Its SHA-256 is
`5d7dbea3566e5b34bd84fa517ba2c5bf0258459db3a980988008490169be46bb`;
the source is the [official 2019 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf).
The PDF skill was used read-only. No preliminary result was reconstructed or
proved in this review. The previously reviewed growth-existence and
convergent-enclosure proof in `proof.md` was used as an allowed lemma, and its
application was checked rather than relying on its acceptance narrative.

In particular, chronological left-tape output is the reverse of the physical
left context around the seed. Reversal is a bijection, so the new `c_(2k)` is
indeed the accepted `C_k`, with exponent `1/(2k)`, not a square-root or
seed-length variant of the accepted rate. The one-extra-move inequalities
`c_(2k) <= c_(2k+1) <= 2 c_(2k)` give the same per-move rate `lambda`.

## Whole reconstruction: canonical language and non-overlap

1. Equality of chronological tape contexts fixes each tape's output length
   and the total history length. A phase change complements both tapes, so
   equality and canonicality of a history are phase independent. Factor
   replacement therefore preserves the complete tape pair in any surrounding
   history, including an odd starting phase. Lexicographic order is preserved
   by a replacement with a smaller factor of the same length.

2. A canonical word has canonical factors. Every bad word has a shortest bad
   contiguous factor. These two facts establish the factorial avoidance
   description and the factor-free property of the minimal set, without a
   regular-language assumption.

3. For a minimal bad history `h` and any smaller equivalent `g`, a common first
   letter would leave a smaller equivalent proper suffix after cancellation.
   If their grid paths met at an internal time, the prefixes up to that vertex
   would be equal-context paths, and `g`'s initial `L` would make the proper
   prefix of `h` bad. Thus `L_g(t)-L_h(t)>0` at every internal time: it starts
   at 1, changes by at most 1 at a step, and cannot vanish internally.
   At the last step this also forces `h` to end `L` and `g` to end `R`.
   Comparing the first left-tape bits excludes `h` beginning `RL`;
   comparing the last right-tape bits excludes it ending `RL`.
   Hence every minimal bad factor begins `RR`, ends `LL`, and has length at
   least 4. No reverse-phase assumption is needed in the final comparison.

4. I specifically checked the planar splicing step. Write two properly
   overlapping minimal factors as `ab` and `bc`, with `a,b,c` nonempty.
   In the complete history `abc`, let `P` replace `ab` by its upper witness
   and let `Q` replace `bc` by its upper witness. They are paths for the same
   **fixed complete tape pair**. At time `|a|`, `P` has larger left coordinate
   than `Q`; at time `|ab|`, it has smaller left coordinate. Their difference
   has step increments in `{-1,0,1}`, so they meet at an intermediate integer
   time, strictly inside these endpoints. Concatenating the segment of `Q`
   from the original start vertex of `b` to that meeting vertex with the
   segment of `P` to the original end vertex of `b` is a legal directed path.
   Because the two endpoint vertices are fixed, it consumes exactly the two
   tape substrings of `b`, not merely the same total lengths. Its first move
   is `L`, while `b` starts `R`; this contradicts canonicality of a proper
   factor of `ab`.

   An overlap of length 1 cannot accommodate the strict sign reversal and is
   already impossible. A purported overlap containing an entire forbidden
   word is excluded by factor-freeness before this argument. Self-overlaps
   are covered. I found no witness-splicing defect.

5. For the renewal count, every failure after appending one letter to a
   canonical prefix has a unique final forbidden suffix. Conversely, a
   canonical prefix followed by a minimal bad factor cannot have an earlier
   bad occurrence: a crossing occurrence would overlap the final one, and
   containment is excluded by factor-freeness. Thus its length-`n-1` prefix is
   canonical. This gives the claimed bijection and
   `c_n = 2 c_(n-1) - sum_j f_j c_(n-j)`, including empty prefix and `n=1`.
   Formal multiplication gives `C(z)=1/(1-2z+F(z))`.

6. The proposed intrinsic rewriting system terminates on each finite
   equal-length lexicographic set. Every irreducible is canonical, and every
   reduction preserves context; uniqueness of the canonical representative
   therefore supplies the common normal form. Disjoint left-hand-side
   occurrences follow from factor-freeness and non-overlap. This does not
   assert a finite presentation or an explicit description of all rules.

## Boundary analysis and lower bound

I checked the two analytic boundary claims without assuming continuation
through the convergence circle or differentiability there.

* The accepted infimum formula implies `c_(2k) >= lambda^(2k)`, so the even
  terms alone force `C(R)=infinity`, where `R=1/lambda`. The odd-count sandwich
  supplies radius `R`. Every minimal bad factor has a canonical prefix, giving
  `f_n <= 2 c_(n-1)` and convergence of `F(x)` for `x<R`.
* On that interval the formal identity is an identity of convergent real
  series, so `F(x)=2x-1+1/C(x)`. Monotone convergence of the nonnegative
  coefficients and divergence of `C(x)` at the boundary imply the finite
  equality `F(R)=2R-1`. The denominator is positive below `R`.
* Inside the radius, `F'` exists and is nondecreasing. If `F'(x0)>2` for
  some `x0<R`, the denominator `D=1-2x+F(x)` is increasing on `[x0,R)` from
  an already positive value, contradicting its limit zero. Thus `F'(x)<=2`.
  Monotone convergence applied to its coefficient series gives
  `sum n f_n R^(n-1) <= 2`. Here the boundary notation denotes that convergent
  nonnegative series; no complex analytic derivative at `R` is assumed.
* For an exactly known prefix through `N`, termwise comparison in the tail
  gives `F(R)-P_N(R) <= R(2-P_N'(R))/(N+1)`. Rearrangement gives exactly the
  displayed `E_N(R)>=0`; the coefficient is `(N+1-n)/(N+1)`, with no off-by-one
  loss. All its degree-at-least-two coefficients are nonnegative, so its
  convexity on the positive axis is valid.

For `N=24`, I independently obtained `E_24(100000/176521)<0` and
`E_24(3/5)=-60351636099623798/1490116119384765625<0` using integer rational
arithmetic. The accepted lower count implies `R<3/5`, since
`395397(3/5)^24=111671791435977957/59604644775390625>1`.
Convexity excludes the entire closed interval between those two test points,
including its endpoints. Consequently `R<100000/176521` and
**`lambda>1.76521`** follow strictly. The older `N=20` argument is subsumed by
the same reconstructed proof and the complete coefficients through 20.

## Independent finite enumeration and upper certificate

The checker was written for this review and imports no author or reviewer
code. Its completeness argument is independent of a guessed suffix pattern:
at every length it fixes only the proved `RR` prefix and `LL` suffix, with
arbitrary final L-run length, and excludes every previously discovered
shorter minimal bad factor. An inductive completeness proof then applies:
every nonminimal bad candidate would contain one of those shorter factors.
Every remaining candidate is converted to literal tape words. A backward
grid dynamic program counts all legal paths exactly, after which greedy
selection among the feasible edges returns the lexicographically least one.
Each newly found bad word also has its proper prefix and suffix independently
checked canonical. Factoriality makes these two checks cover every proper
contiguous factor.

The independent result is:

| Length | 4 | 12 | 14 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `f_n` | 1 | 1 | 2 | 3 | 2 | 4 | 8 | 6 | 20 | 14 | 40 | 42 |

All omitted lengths through 24 have zero count. There are 143 words, all
distinct. Only **after** independent discovery did the checker load the
author's two raw-data files: their entire word set matched exactly. At length
24 it tested 74,645 complete candidates, with 500,540 visited nodes under
this implementation's counting convention. The author's two-node-smaller
count is not a word-set discrepancy.

A separate unrestricted enumeration of **every** history through length 16
partitions them by literal tape pairs and selects the first word of each
class. It uses neither the `RR`/`LL` restriction nor grid feasibility. It
independently matches the minimal words and the renewal context counts at
every one of these lengths. The exact reciprocal coefficient at length 24
also equals the previously reviewed `C_12=2985943`.

All pairs of the 143 words, including self-pairs, were checked for proper
factor containment and suffix-prefix overlaps. None occurs. The finite
avoiding-language reciprocal `1/D_24` is therefore justified directly for
this set even apart from the unrestricted theorem.

For its growth rate `rho`, cutting an avoiding word gives submultiplicative
counts `d_n`, and the elementary log-subadditivity argument yields
`d_n >= rho^n`. The radius `r=1/rho` is finite and positive (all-L words
exist, and counts are at most `2^n`). Thus its series diverges at `r`.
Inside the radius, `D_24(x)=1/sum d_n x^n>0`; continuity of the polynomial
then gives `D_24(r)=0`. This establishes the first-positive-root assertion
without presuming it from a numerical plot.

At `x=100000000/183516197`, independent exact arithmetic gives
`D_24(x)>0` and `D_24'(x)<0`, with the same rational numerators and denominators
as the author's certificate. Since `D_24''>=0`, its derivative is negative
throughout `[0,x]`, and the polynomial stays strictly positive there.
Therefore `r>x`, `rho<1.83516197`, and canonical-language inclusion gives
**`lambda<1.83516197`**. Numerical roots are not used in this deduction.

Both bounds are therefore supported by this audit:

```
1.76521 < lambda < 1.83516197.
```

These are partial asymptotic results. The finite computations support exact
finite coefficients and signs, not an extrapolated formula for all `f_n`.

## Rigid families, staircases, and finite-rule obstructions

I also reconstructed these arguments, rather than leaving them outside the
verdict.

**Two-parameter rigid family.** Every even-length history splits uniquely into
the four displayed two-move generators, so counting generator histories
does not omit unblocked histories. At the first pair boundary both heads
are zero, allowing only `A` or `D`. In the `A` branch, the next generator must
be `C`, the next `q-1` must be `A`, the next two must be `B`, the next `p-1`
must be `D`, and the final two are `C D`: every proposed alternative either
has no required head or leaves both heads one at a zero step. These checks
continue to hold at `p=1` and `q=1`, when the corresponding loops vanish.
Tape exchange supplies exactly the other branch. The blocked and unblocked
formulas and their total length `2p+2q+8` agree. The grid checker stress-tests
all `1<=p,q<=9`, finding exactly two histories.

The histories differ at both endpoints. Any alternative for a proper factor
would extend to a third history while preserving at least one endpoint,
so every proper factor has unique context. Thus every displayed `H(p,q)` is
minimal bad. Distinct run parameters give distinct words, justifying the
subseries `z^12/(1-z^2)^2`. This is a contribution, not an exhaustive formula.

**Finite presentations on the fixed generators.** For a finite list of sound
literal equations, choose a rigid `H` longer than every equation side. Each
side that could match is then a proper factor with unique context, so no
nontrivial rewrite can start from `H` in either direction. Its equivalent
partner is unreachable. Length preservation rules out an equation with a
different-length alternative; the same argument holds for the four blocked
generators, using length `p+q+4`. The empty list is immediate. This proves the
stated obstruction on these fixed alphabets and does not claim anything
about auxiliary generators, variable equation schemata, regular cross-sections,
or rationality of the counting series.

**Even run inflation.** Inserting the same two choices just after matched
occurrences on a tape inserts the same bit pair `1-a,a`; all later source
phases are retained. The first differing letters of the witness pair remain
ordered. Noncanonicity is preserved. Minimality need not be: the quoted
17-to-19-move inflation was independently checked, including its bad proper
prefix. Its two endpoint-canonicality results are recorded in the evidence.

**Staircase family.** I checked the starting indices `j^2+1` of the ascending
blocks, the central starting parity, and the descending parity alternation.
They give the stated tape contributions; merging adjacent contributions
produces runs `1,2,...,n,n,...,2,1` on both tapes. If both heads equal the
mandated bit, taking a side with remaining run length at least 2 fails on
the next move; taking its last isolated bit also fails unless it exposes
the opposite bit. Hence a successful simultaneous-head choice must precede
a doubled history letter. The formula has only the doubled runs listed in
the table. At their starts the other remaining run lengths are respectively
`1`, `j+1`, `n-1`, and `j-1`. In the central/descending cases a value 1 is
the final bit of that tape, so the other choice fails by exhaustion; value
0 means it is empty. Thus only the initial side can be chosen freely.

This covers `n=1`, `n=2`, `j=1`, and `j=2`, not just the long interior blocks.
It proves exactly two histories. Endpoint differences then prove proper-factor
uniqueness and minimality as before. Independently, the checker verified
contexts, every simultaneous-head decision, and exactly two paths through
`n=13`, total history length 364. The infinite family with runs at most 2
excludes any finite set of bases followed only by even run inflation: any
positive inflation produces a run of at least 3. This does not exclude a
recursive grammar.

**Strictness of each finite forbidden-factor upper rate.** Let `S` be a finite
subset of the minimal set; take `M>=1` at least its maximum length. The
bridge `(RL)^M` cannot contain a terminal `LL` and cannot start a forbidden
word with `RR`. An occurrence starting in the first word and ending in the
second would traverse a bridge longer than any forbidden word. The two
remaining boundary cases also fail: the bridge starts `R` and ends `L`,
so a crossing start or end cannot create the missing doubled pair. Thus any
two avoiding words can be joined by the bridge, proving irreducibility of
each sufficiently large finite block graph. All-L loops also exist.

Choose a staircase word of length `ell` exceeding every length in `S`.
It is `S`-allowed by minimality. In the graph with `(ell-1)`-letter states
and `ell`-letter edges it supplies an actual edge; forbidding it deletes
that edge. The old matrix `A` is finite and irreducible, and the new matrix
satisfies `0<=B<A` with at least one strict entry. I checked the supplied
Perron argument: a nonnegative Perron vector `x` of `B` and positive left
Perron vector `w` of `A` would, under equality of radii, force
`(A-B)x=0`, then `Ax=rho(A)x`, then `x>0` by irreducibility, contradicting
the strict entry. All theorem hypotheses are supplied; reducibility of `B`
causes no problem. Finite-block path counts have these spectral growth
rates. The canonical language avoids the additional staircase, proving the
strict inequality. Empty `S` is covered by taking `M=1`.

For a finite list of sound lex-decreasing replacements, each left-hand side
contains a minimal bad factor. Avoiding one such selected factor for each
rule implies avoiding every original left-hand side. The latter avoiding
language therefore has at least the selected set's strictly excessive rate.
The direction of this inclusion is correct. No claim about every possible
finite-state representation follows or is needed.

## Further finite assertions, limitations, and reproducibility

The separate bounded-run search through length 26 independently gives
`4:1, 12:1, 17:2, 20:1, 22:4, 24:1, 25:4`, all other such lengths zero,
with 14 words in total. It is a separate complete finite induction because
factors of bounded-run words remain bounded-run. The computed full set has
four length-19 minimal bad factors with three complete histories, confirming
the stated warning against extending rigidity to every minimal factor.
The quoted range-statistic, short greedy, and self-shuffle counterexamples
were independently checked by the grid path count. The fixed-window family
was reconstructed by the forced-head argument and stress-tested for
`0<=p,q<=6`, including the empty repeated powers. Its impossibility statement
is about choosing a successful first move using only those fixed windows;
it supplies no claim against backtracking or a scheduler with global data.

The run-compression and simultaneous-inflation generalizations remain
unproved. I did not independently reproduce all 1,791 states of the author's
parity-model experiment or its count of 592 simultaneous failures; these are
explicitly bounded exploratory observations, not inputs to any accepted
inference above. Likewise, the audit does not establish novelty, a complete
grammar for `F`, or a theorem about rationality/algebraicity/nonrationality.

Reproduction command from the repository root:

```
.venv/bin/python -u problems/2019-B4/reviews/secondpass-review-1-run.py
```

The runner uses `subprocess.Popen`, records its own child PID before waiting,
and enforces a 60-second hard timeout with targeted child cleanup. The final
child PID was 27303, exit status 0, elapsed time 7.2424 seconds; its complete
incremental stdout and evidence are retained. Python was 3.12.14, and the
mathematical checker uses only its standard library. No native CAS, install,
paid API, other owners' process, or worker Git operation was used. The earlier
smaller checker also completed; its metadata is retained in the run-history
file. Its initial stdout was superseded before being separately archived;
the final extended run reproduces every earlier mathematical check and adds
the explicitly recorded checks above.

Files owned by this review all start `reviews/secondpass-review-1`:
the report, independent checker and runner, final complete log, evidence,
job record, run history, and hash list. No proof, author computation, shared
issue/status file, existing review, or promotion record was edited.

**Remaining substantive objections from this audit: none.** The remaining
procedural requirements are the other independent blind audit and the
coordinator's decision; the remaining mathematical research target is the
exact determination of `lambda`.
