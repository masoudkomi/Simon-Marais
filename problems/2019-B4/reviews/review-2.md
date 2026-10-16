# Independent adversarial review R2: 2019 B4(b)

Initial report completed 2026-10-16, 10:21 UTC. This reviewer did not construct
the proof. No other review report, review evidence, coordinator status, or
review queue was read, and no other reviewer's conclusions were received
before completing this report.

**Verdict:** no substantive mathematical defect found in the partial results
of proof version 1. The unrestricted arguments for existence of the growth
rate, the context enclosures, the seed substitution inequality, and the strict
upper bound pass this audit. The two quoted finite context counts were also
reproduced independently. This is one reviewer's conclusion, not a promotion
to `proved, independently reviewed`. The exact growth constant remains
undetermined in this submission, so it does not supply a full solution of the
official determination problem.

## Version, scope, and primary sources

- Audited `problems/2019-B4/proof.md`, version 1, SHA-256
  `227cff77dc63aba6125494e6e39e3feb687fe4b8a3ff90d4392d72b4133e5a1e`.
  The hash was checked before and after the finite audit.
- The normalized `statement.md` agrees with the definitions and part (b) on
  page 2 of the [official 2019 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf): seed `1`; one added bit per step; add `0` from odd length and `1` from even length; either end is allowed; no additional strings; positive integer lengths; count distinct strings; determine both the lower and upper limits of the nth roots.
- Cached primary paper SHA-256:
  `5d7dbea3566e5b34bd84fa517ba2c5bf0258459db3a980988008490169be46bb`.
  Its B4 area was checked both by text extraction and by rendering page 2.
- The attribution of the contextual estimates involving phi and the real
  root greater than 1 of `x^3-x^2-x-1` is consistent with pages 10-12 of the
  [official solution notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-solutions_1.pdf), cached SHA-256
  `a865c3f68e9082e3cce457cb5f10a9df5f33feed16ae63c16a70f885fe59199e`.
  These estimates were used only as attributed context. The preliminary
  part (a) was not rederived in this review.
- No assertion about present literature completeness or novelty is certified
  by this report. The audited arguments are self-contained apart from the
  expressly attributed contextual estimates, which they do not require.
- Requested launch settings: `gpt-6.1-sol`, `max`. A verified effective-model
  or reasoning-setting readback was unavailable; these are requested settings
  only. The account-wide weekly telemetry read at the start of the audit
  reported 3% used in a 10080-minute window, below the 90% stop threshold.

## Independent reconstruction of the unrestricted arguments

### 1. Context counting and composition

At move number i starting with i=0, the added bit is `i mod 2`, independently
of the left/right choice. A history of 2k moves therefore gives a pair of
words `(l,r)`, with l the reverse of the bits selected for left insertion and
r the bits selected for right insertion. The resulting unmarked word is
`l1r`. Distinct histories can yield the same pair; pairs, rather than
histories, are what C_k counts.

Every word in B_(2k+1) has such a pair. For a fixed output word and left
length p, the only possible pair is obtained by cutting immediately before
and after its pth-position seed. There are 2k+1 possible positions, and some
are not legal seed positions. Thus the claimed surjection and fibre bound
are valid, including k=0. They do not assume that different seed positions
remain distinguishable after the mark is forgotten.

After the first 2k moves the current length is still odd. The next 2j moves
use exactly the same alternating bit sequence as a fresh 2j-move history.
For contexts a=(l1,r1) and b=(l2,r2), doing a first and b second produces
`(l2l1,r1r2)`. Representatives of any two context classes can be composed,
because the legal added bit depends only on parity. Conversely, splitting
any full history at 2k gives these two contexts. Hence this map is onto the
whole context set at k+j, proving C_(k+j) <= C_k C_j. Possible collisions in
the composition map do not invalidate the upper bound. The cases k=0 or
j=0 give the identity context.

### 2. Growth-rate existence, including even lengths

All C_k are finite and at least 1, and C_k <= 2^(2k). Consequently
a_k=log(C_k) is nonnegative, finite, subadditive, and at most 2k log 2.
For fixed r>=1, writing k=qr+s gives
`a_k <= q a_r + a_s`, with s in the fixed finite set 0,...,r-1.
Dividing by k proves that the upper limit is at most a_r/r. The lower
limit is at least the infimum over r. Thus a_k/k converges to that infimum.
There is no omitted finiteness or lower-bound hypothesis in this use of
subadditivity.

The logarithms of C_k and b_(2k+1) differ by at most log(2k+1). Division
by 2k removes that difference. Replacing denominator 2k by 2k+1 changes the
quotient by at most `log(2)/(2k+1)`, using the history bound. Exponentiation
therefore gives convergence of the odd roots and the displayed infimum
formula for lambda. In particular 1 <= lambda <= 2.

For each n, right-appending its mandated bit gives an injection from B_n
to B_(n+1): the final added bit can be deleted to recover its input. Thus
`log b_(2k+1) <= log b_(2k+2) <= log b_(2k+3)`. Divide by 2k+2; the two
outer expressions tend to log lambda because their denominator ratios tend
to 1. This proves convergence along even lengths and hence along all
positive lengths. No parity subsequence is left untreated.

### 3. Fixed-position lower bounds and converging enclosures

Fix k>=1 and a maximizing left length p. When q contexts from this class
are composed, the final word is
`l_q ... l_1 1 r_1 ... r_q`, with each l_i of length p and each r_i of
length 2k-p. Its seed lies after exactly qp bits. Cutting at this known
position and splitting into these known block lengths reconstructs every
pair in its original chronological order. Repeated occurrences of `1` in
the output do not affect this recovery because the cutting position is
known. Thus the map from ordered q-tuples of contexts to unmarked output
words is injective.

At p=0 or p=2k one side has only empty blocks; the nonempty side still
decodes in fixed block lengths. Moreover each endpoint class contains only
one context, as all moves are forced to the same side. These boundary
cases therefore cause no ambiguity. It follows that
`b_(2kq+1) >= M_k^q`. Taking roots and letting q tend to infinity using
the already proved all-length limit gives `M_k^(1/(2k)) <= lambda`.

The upper endpoint follows from the infimum formula. There are 2k+1
position classes, so `C_k <= (2k+1) M_k`. The endpoint ratio is at most
`(2k+1)^(1/(2k))`, which tends to 1. Since the positive number lambda lies
between them, both endpoint sequences converge to lambda. Monotonicity of
the endpoint sequences is not needed or asserted.

### 4. The separate seed substitution inequality

Choose one generating history for each word of B_n and group these words
by the position p of their seed. Some class has at least b_n/n members.
For odd m, first generate any x in B_m and then follow the chosen history
of a class member y, treating x as the replacement seed. Every subsequent
parity agrees with the original history because m-1 is even. The output
is `y[:p] + x + y[p+1:]` and belongs to B_(m+n-1).

From the output, p and m recover x as its length-m central block; replacing
that block by `1` recovers y. This proves injectivity of the pair map and
the claimed inequality. The argument covers m=1, n=1, and both extreme
seed positions. For even m the parity justification would fail, but that
case is correctly excluded by the statement.

### 5. Rewrites at arbitrary positions and both starting parities

Independent direct calculation gives the following contexts:

| Histories sharing a context | First bit 0 | First bit 1 |
| --- | --- | --- |
| `RRLL`, `LLRR` | (`10`,`01`) | (`01`,`10`) |
| `RRLRRLRLLRLL`, `LLRLLRLRRLRR` | (`100110`,`011001`) | (`011001`,`100110`) |

The first-bit-1 contexts are the bitwise complements of the first-bit-0
contexts. Equality of the two context components means equality around
any current central word, not merely around seed `1`. Both replacements
have equal length and preserve the added-bit sequence and the parity at
the end of the block. Their first new letter is L in place of R, so they
strictly lower the full history in lexicographic order, regardless of the
prefix and suffix surrounding the rewritten block.

For a fixed output word the history set is finite and nonempty, so it has
a lexicographic minimum. If either forbidden block appeared in that
minimum, its replacement would be a legal history of the same length for
the same output and would be smaller. Thus every output word has an
avoiding representative. This yields `b_(t+1) <= d_t`; it does not assume
that all avoiding histories give different words, nor that the two rewrite
rules form a complete system of collision relations.

### 6. Automaton and exact upper certificate

Independently collecting all proper prefixes of the two forbidden words
gives exactly the 12 listed states, with no proper prefix already containing
a forbidden word. If the current processed history avoids both words,
any newly created forbidden occurrence ends at its new last letter.
Keeping the longest suffix which is a proper prefix of a forbidden word
retains precisely the information needed to detect that event. This
justifies the suffix transition construction by induction at every length,
including the empty history. Every non-rejecting state is accepting.

The separately constructed transitions and row-oriented adjacency matrix
agree entry for entry with the submitted certificate. With A so oriented,
`(A^t 1)_epsilon` counts allowed length-t continuations from the empty state.
The integer vector is positive and all twelve displayed integer slacks
were reproduced exactly; their minimum is 174288855158. They imply
`Av <= q' v` for

`q' = max_i (Av)_i/v_i = 154146715175/83884534067 < 183761/100000`.

The maximum occurs at zero-based state index 9, `RRLRRLRLL`. The decimal
`1.8376059054209015` is only a rendering of this exact rational maximum,
not a claimed exact value for lambda or for the spectral radius.

Nonnegativity of A preserves coordinate inequalities, so
`A^t 1 <= (q')^t v/min(v)`. Combining this with the avoiding-representative
argument and taking nth roots proves
`lambda <= q' < 1.83761`. No irreducibility, diagonalization, floating
eigenvalue estimate, or Perron-Frobenius hypothesis is required. The strict
comparison with the attributed larger root psi is also consistent:
`q^3-q^2-q-1 = -9159746959919/1000000000000000` for q=183761/100000,
and this cubic is strictly increasing above 1. This is only a comparison
with the published context estimate, not a reproof of the preliminary part.

## Independent finite audit and counterexample search

The review checker was written before inspecting any author computation
program. It imports and executes none of `enumerate.py`,
`upper_certificate.py`, or `explore.py`. It reads the submitted certificate
JSON only to compare an independently built automaton and recomputed
integer arithmetic against the submitted data.

Completed finite checks:

- All histories of lengths 0 through 16: independently counted words,
  contexts and avoiding histories; checked every lexicographic minimum
  avoids both forbidden blocks; checked fibre bounds. At 16 moves the
  independent counts were 23144 contexts, 11279 words, and 23171 avoiding
  histories. No counterexample was found in this finite range.
- Exact equality of the composed context sets for every k,j>=0 with
  k+j<=4, including identity contexts.
- All left positions for k=1,2,3 and q=1,2,3: 45 parameter cases of the
  fixed-position injection, including both empty-side cases. Each generated
  tuple was decoded back to the original tuple.
- Seed substitution with m in {1,3,5,7} and n=1,...,8: 32 parameter cases,
  verifying membership, injectivity and recovery from outputs.
- Direct enumeration of all 4096 histories of 12 moves, encoded from
  their source-position subsets, gave 2030 distinct half-contexts.
  Composing two such halves examines 4120900 context pairs. Since each
  half has even length, the source bit sequence restarts at 0 in the second
  half. Conversely every 24-move history splits into two such halves.
  The final left and right strings were packed injectively into a 24-bit
  integer for each externally known left length. Each position was handled
  separately to bound memory, then discarded after counting and hashing.
  This independently reproduced the entire submitted position-count row:

  `1, 24, 255, 1604, 6789, 21012, 50707, 100334, 168807, 247654, 322226, 375860, 395397, 375860, 322226, 247654, 168807, 100334, 50707, 21012, 6789, 1604, 255, 24, 1`.

  Its sum is C_12=2985943, its maximum is M_12=395397, and the unique
  maximizing left length is 12. Sorted three-byte context hashes for all
  25 positions are saved in the evidence JSON. The associated decimal
  lower endpoint is approximately 1.710841292477; that decimal evaluation
  is evidence only. The exact integer count together with the unrestricted
  injection is the justification for the corresponding asymptotic bound.

The finite tests supplement the mathematical reconstructions above; they
do not establish any unrestricted inference by extrapolation.

## Reproduction and job record

Files owned by this reviewer:

- `reviews/review-2.md`: this report.
- `reviews/review-2-check.py`: independent standard-library checker.
- `reviews/review-2-evidence.json`: complete successful results, exact
  integer certificate checks, finite search ranges and context hashes.
- `reviews/review-2-run.log`: incremental child output.
- `reviews/review-2-job.json`: exact command, PID, timeout, parameters,
  elapsed time and exit code.

From the repository root, the exact checked child command was:

```sh
/Users/uqmkamga/Documents/ChatGPT/Website/.venv/bin/python -u problems/2019-B4/reviews/review-2-check.py
```

It ran as child PID 12199 under a parent subprocess supervisor with an
explicit 180-second timeout and targeted `child.kill()` on timeout. The
job completed normally with exit code 0, in approximately 1.4 seconds,
and no timeout or incomplete search occurred. No other process was
terminated. Every context position produced an incremental output
checkpoint. Python version: 3.12.14; checker dependencies: standard library
only. Primary PDF inspection used the existing pypdf 6.10.0 and bundled
`pdftoppm`; no packages were installed and no separately billed API was
used. The PDF rendering was transient and the complete third-party papers
remain in ignored `.cache/official/`.

## Findings and required next actions

There are no unresolved substantive R2 issues and no proof repair is
requested by this review. No counterexample or unsupported theorem
application was identified within the audited arguments.

The coordinator must still reconcile this report with the second,
independently completed audit before any status promotion. Any proof
changes affecting these arguments require review against their new hash.
The distinction between these partial results and a full determination of
lambda must remain explicit. In particular the numerical spectral estimate
and the finite context counts do not identify the exact growth constant.

No other owner's files, proof text, shared issue log, or repository-level
files were changed. This reviewer did not commit or push.
