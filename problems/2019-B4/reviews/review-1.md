# 2019 B4(b): independent adversarial review R1

**Initial report complete, 2026-10-16.** The reviewed object is the partial
candidate `proof.md`, version 1, SHA-256
`227cff77dc63aba6125494e6e39e3feb687fe4b8a3ff90d4392d72b4133e5a1e`.
That hash was checked before the audit, by the independent check script,
and again after the finite checks. Requested launch settings were
`gpt-6.1-sol` with `max` reasoning. A verified effective-setting readback
was not available; these are requested settings only.

I did not construct this candidate. I completed this report without
reading any other review report or any other reviewer's conclusions. I
read the candidate, statement, computation JSON files and computation
README, but did not read or run the author's computation scripts. The
new check script below was written independently from the mathematical
definitions. This report reconstructs the entire partial argument.

**Verdict:** I found no substantive mathematical gap in the stated partial
results. The context growth limit, converging enclosure argument, and
strict rational upper bound pass this audit. The finite context counts
used for the lower estimate were independently reproduced. One minor
attribution clarification, R1-E1 below, should be made by the proof author.
The exact value of the growth constant remains undetermined, so this is
not a full solution of the official request. This review does not promote
the candidate: that is the coordinator's responsibility after the second
independent audit and issue resolution.

## Official statement and scope

I compared `statement.md` to the cached original Paper B, page 2, including
visual inspection of a rendered page, and to the same
[official Paper B URL](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf)
accessed on 2026-10-16. The normalization is faithful: the seed is exactly
the one-letter string `1`; an odd current length permits a `0` at either
end; an even current length permits a `1` at either end; no additional
strings are admitted; and `b_n` counts distinct strings for positive
integer `n`. Part (b) asks for both root-growth lower and upper limits.
There is no official requirement that the histories or marked seeds be
counted as distinct words.

The [official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-solutions_1.pdf),
pages 10-12, assert the contextual exponential bounds with the golden
ratio and the real root greater than one of `x^3-x^2-x-1`, as attributed in
the candidate. I checked these asserted bounds and their identification
only; I did not audit, solve or reproduce the preliminary part (a).
The opening historical openness statement is an as-issued statement,
and the candidate makes no claim to have verified current global novelty.

Cached source SHA-256 values checked on 2026-10-16:

```text
5d7dbea3566e5b34bd84fa517ba2c5bf0258459db3a980988008490169be46bb  .cache/official/2019-paper_b.pdf
a865c3f68e9082e3cce457cb5f10a9df5f33feed16ae63c16a70f885fe59199e  .cache/official/2019-solutions.pdf
```

The temporary page image used for visual inspection was removed after
inspection. No third-party paper or page image was added to tracked review
evidence. No other annual problem, part (a) research, or 2026 problem was
investigated for this review.

## Reconstruction of Sections 1 and 2

1. **Contexts and fibres, Lemma 1.** At `2k` additions there is a finite,
   nonempty set of contexts, including the identity context for `k=0`.
   Every generated odd-length word has a generating history and therefore
   at least one marked context. Once an output word and a left length
   `p` in `0,...,2k` are fixed, both outside words are fixed by cutting at
   position `p`; a cut with central bit zero simply has no preimage.
   Thus every fibre has at most `2k+1` elements. This does not require
   that a word have a unique generating history or a unique seed position.

2. **Submultiplicativity.** For a history of `2(k+j)` moves, the first
   `2k` moves leave an odd-length core. The remaining moves therefore
   add the same bit sequence `0,1,...` as a new context from the seed.
   The final left string is `l_2 l_1`, and the final right string is
   `r_1 r_2`. Splitting any history gives a preimage under this composition
   map. Conversely, concatenate witnesses for two context pairs; even
   first-block length makes the second witness legal. Therefore the map
   from the Cartesian product is onto, which is the direction needed for
   `C_{k+j} <= C_k C_j`. Empty blocks at `k=0` or `j=0` work as identities.
   No injectivity is used here.

3. **Existence of the context rate, Theorem 2.** Since `1 <= C_k <= 2^(2k)`,
   the logarithms are finite and nonnegative. For fixed positive `r`, the
   division `k=qr+s`, `0<=s<r`, gives the displayed subadditive estimate.
   There are only finitely many residual logarithms `a_s`, so their
   quotient by `k` tends to zero. This proves the limsup bound for every
   `r`; the liminf is at least the same infimum by its definition. Thus
   `log C_k/k` has the finite asserted limit. This is a complete elementary
   proof of the subadditivity step and needs no external theorem.

4. **Removal of the mark and all lengths.** The fibre error in logarithms
   is at most `log(2k+1)`, which is negligible after division by `2k`.
   Changing that denominator to `2k+1` is legitimate since the word count
   is between one and `2^(2k)`. Exponentiation is continuous, giving the
   stated infimum formula for the odd-length root limit. At each positive
   length, appending the mandated next bit is an injective operation on
   distinct words. The resulting monotonicity sandwiches the even-length
   logarithmic quotients between the adjacent odd-length ones, with
   denominator ratios tending to one. This supplies convergence for every
   `n`, not just a subsequence. There is no missing `n=0` convention; the
   theorem only concerns positive lengths and a limit at infinity.

5. **Fixed-position injection, Lemma 3.** With `k>=1` fixed, all contexts
   in the selected class have left length `p` and right length `2k-p`.
   After `q` compositions the marked position is the known position `qp`.
   Reading the blocks to its left in reverse block order and the blocks
   to its right in forward order recovers each ordered context pair.
   Repeated bits, other occurrences of `1`, and collisions between
   different unrestricted histories cannot affect this decoding. When
   one block length is zero, all information on that side is empty and
   the other fixed-length side still recovers the contexts. In fact the
   boundary classes `p=0,2k` have one member each, as stated. The injection
   gives `b_{2kq+1} >= M_k^q`; taking `q` to infinity, using the already
   established full limit, yields `lambda >= M_k^(1/(2k))`.

6. **Converging enclosures.** Summing the `2k+1` position-class counts
   gives `C_k <= (2k+1)M_k`, and the context infimum gives the upper bound.
   Both endpoints are positive, trap the same finite positive `lambda`,
   and have ratio at most `(2k+1)^(1/(2k))`, tending to one. It follows that
   each endpoint converges to `lambda`. Neither endpoint sequence is
   asserted to be monotone, which is appropriate.

7. **Seed substitution inequality (4).** Choose one history for every
   length-`n` word before partitioning by its `n` possible marked positions.
   For the selected position `p`, replacing the single seed by a length-`m`
   word preserves the legality of every outside move exactly when `m` is
   odd, as assumed. The final output is parsed using the fixed `p` and
   known `m`, so the inserted word and the original outer word are both
   recovered. The proposed inequality follows even if `b_n/n` is not an
   integer. The cases `m=1` and `n=1` are also covered. I found no hidden
   assertion that the central seed must be uniquely recognizable.

These arguments are self-contained partial results for (b). Their
conclusions do not evaluate the common limit explicitly.

## Reconstruction of Section 3

For a block starting with bit zero, direct chronological construction
gives the following context pairs for the two sides of each replacement:

| histories | left context | right context |
| --- | --- | --- |
| `RRLL`, `LLRR` | `10` | `01` |
| `RRLRRLRLLRLL`, `LLRLLRLRRLRR` | `100110` | `011001` |

Changing the starting bit to one complements every added bit. It gives
`01`,`10` for the first pair, and `011001`,`100110` for the second pair.
The core string is never changed. The check script independently verifies
these identities at both parities using both context extraction and direct
updates around a deliberately marked core. Each right-hand history has
the same length as its left-hand counterpart and begins with `L` instead
of `R`, so substitution is lexicographically decreasing inside any fixed
prefix and suffix. Equal block lengths also leave the parity of all
subsequent moves unchanged.

Every output has a finite, nonempty set of histories of the required
length, so a lexicographically least history exists. Either forbidden
substring in it would produce a smaller history with the same output.
Consequently every word has an avoiding representative, which is the
surjectivity needed for `b_{t+1} <= d_t`. The argument includes `t=0` and
does not assume that avoiding histories themselves have distinct outputs.
Overlaps of rewrite rules cause no difficulty: the argument uses one
replacement in a least history, with no confluence assertion.

I rebuilt the suffix automaton from the proper-prefix set rather than
copying the supplied transitions. Upon a new letter, a newly completed
forbidden substring must end at that letter, since the prior prefix was
accepted. Its preceding proper prefix is a suffix represented by the
current state; rejection and longest-suffix update therefore preserve the
usual longest-suffix invariant. The prefix list contains twelve states,
and the independently constructed state order, transitions and adjacency
matrix match the certificate exactly. All states accepting means that
`d_t` is the empty-state component of `A^t 1`, with the row-to-destination
matrix orientation used in the proof.

The independently calculated slacks match all twelve displayed integers
and are strictly positive. Every weight is positive. In particular the
maximum exact row ratio is

```text
qprime = 154146715175 / 83884534067
q - qprime = 34347185987 / 8388453406700000 > 0
```

The maximum occurs at zero-based state index 9, `RRLRRLRLL`. Since the
matrix is nonnegative, `Av <= qprime v` and `1 <= v/min(v)` imply
`A^t 1 <= qprime^t v/min(v)` by induction. Thus the candidate's strict
upper bound follows from its already established limit. Irreducibility,
aperiodicity, diagonalizability, and a floating-point eigenvalue are not
needed. I did not independently recompute the unused numerical spectral
radius.

For the contextual comparison with the published root, exact evaluation
of its defining cubic at `q=183761/100000` gives

```text
q^3 - q^2 - q - 1 = -9159746959919 / 1000000000000000 < 0.
```

The cubic is strictly increasing above one, so this is indeed a smaller
upper estimate than that published contextual bound. This scalar check
does not reproduce the preliminary argument.

## Independent finite evidence

The check used Python 3.12.14 and the standard library, with no installs,
external CAS, or separately billed API. A subprocess with PID `11299`
ran with a 150-second outer timeout and a 120-second inner budget, and
returned exit code zero in about 1.87 seconds. Checkpoints were flushed
after each main stage and each 24-move position class. No run was left
incomplete, and no other process was stopped. The exact child command,
PID, limits, UTC start and completion record are in `review-1-run.json`.

The independently written check:

- exhausts all 131071 histories of lengths zero through sixteen, checking
  machine acceptance against direct forbidden-substring detection and the
  accepted state's longest-suffix invariant;
- compares every resulting avoidance count with exact matrix iteration;
- for lengths zero through fourteen, constructs every output word and
  verifies that its first history in lexicographic order avoids both
  forbidden strings, checking 7506 distinct least-history representatives
  in total and matching the reported unmarked counts through `b_15`;
- exhausts the 4096 histories of twelve moves to obtain 2030 distinct
  marked half-contexts, then composes all 4120900 ordered pairs of these
  half-contexts, one final left length at a time.

The last algorithm is a 12+12 meet-in-the-middle check, separate from the
author's reported full sequential enumeration and subset enumeration.
Both halves start with bit zero because twelve additions preserve the
initial parity. Every 24-move history splits into two of these half
contexts, and every composed pair has a legal concatenated history.
Deduplicating context pairs therefore gives the exact finite sets being
counted. The verified 24-move position counts are

```text
1, 24, 255, 1604, 6789, 21012, 50707, 100334, 168807,
247654, 322226, 375860, 395397, 375860, 322226, 247654,
168807, 100334, 50707, 21012, 6789, 1604, 255, 24, 1.
```

They sum to `2985943`; the unique maximum is `395397` at left length
twelve. Thus both finite constants used in Section 4 were independently
reproduced. The lower estimate is the exact number `395397^(1/24)`;
the decimal `1.710841292477...` agrees with an independent high-precision
evaluation. These computations are finite evidence. The unrestricted
asymptotic consequence rests on Lemma 3, reconstructed above, rather than
on extrapolating the finite data. I did not independently recount the
unmarked values `b_16` through `b_25`, which are not used in the partial
proof's conclusions.

Reproduction from the repository root:

```sh
.venv/bin/python -u problems/2019-B4/reviews/review-1-check.py
```

The monitored outer subprocess invocation and its parameters are preserved
in `review-1-run.json`; the script additionally refuses a proof hash change.
Evidence hashes at completion:

```text
76a026a7548d9fad134c81eb6e64369a80c2be27b0e16557f29c603cacf01302  review-1-check.py
bd43f6c72868cde09a1878451cb31f7701d78fe61bda6a896f286d1e43f64732  review-1-check-output.json
7ad7356c70f3006d1c468b7c0a61ab33800614361c6b2be97a03e14f231c29d4  review-1-check.log
```

## Objections and remaining limitations

**R1-E1 - minor attribution clarification; author action requested.**
Section 3 uses the published `RRLL -> LLRR` observation and its avoidance
representative method, found on page 11 of the official solution notes.
The opening paragraph attributes the published bounds, but Section 3
should explicitly identify this four-move relation and reused method as
published context. Suggested repair: add a sentence crediting the official
notes for that relation and avoidance idea, and distinguish the present
investigation's additional twelve-move relation and combined finite
certificate. Do not claim global novelty without a separate literature
check. This is an attribution/scope clarification, not a mathematical
counterexample or a gap in the bound. It can be checked without reopening
the unaffected mathematical arguments.

No substantive mathematical objections remain from this initial R1
audit. Counterexample and degenerate-case targets considered included
zero-size context blocks, left/right boundary classes, nonunique marks,
collisions between histories, both bit parities for a rule inside a
history, rewrite overlap, empty avoiding histories, all-length versus
odd-length limits, and the direction and strictness of the matrix bound.
The candidate handles these cases as described above.

The exact common limit is still not evaluated, the global novelty of the
partial results has not been established by this review, and this report
is only the first of the two required independent audits.

The authoritative account-wide telemetry consulted during this review
reported 3% used in a 10080-minute weekly window. This was below the 90%
total-weekly-use stopping threshold. No automatic extension into a new
window was requested or performed.
