# Independent blind review 2: 2019 B4(b), third pass

Reviewer: `/root/review_2019_thirdpass_r2`. Date: 2026-10-16 UTC
(2026-10-17 Brisbane). Requested launch settings, as supplied in the
assignment: `gpt-6.1-sol`, `max`. No independent effective-setting readback
was available. This reviewer did not construct the candidate.

**Initial blind report.** I found no unresolved substantive objection to
the new partial results. I recommend that the coordinator consider them
for acceptance after the other independent audit and issue reconciliation.
I do not promote their status. They do not evaluate the exact constant
requested in B4(b), and are not a complete solution of that problem.

Frozen inputs:

- `notes/thirdpass-bounded-separation-v1.md`, SHA-256
  `3364e8c6cf23ba3ecb250f13a5873732c108b6904a68126f52f5d7234eb916d4`.
- `notes/thirdpass-v1-manifest.json`, SHA-256
  `ed672a1a68874ea44c2c4752dad7f1f7ef5e27e496ed4cf40d4f633cc2364b6b`.
  All 70 entries matched their recorded sizes and hashes.

I read no current peer-review file contents, conclusions, issue entries,
or third-pass acceptance/status material before freezing this report.
A filename-only inventory exposed peer filenames, with no review contents.
The earlier accepted mathematical texts and register were permitted inputs.
I wrote an independent FIFO and grid implementation before reading the
author's constructor sources or saved constructor tables. Pre-constructor
source/output hashes are in `thirdpass-review-2-preconstructor.json`.
The displayed small table in the candidate was necessarily visible, but
was not an input to my monitor construction.

## 1. Official domain and foundational inputs

I reopened the [official 2019 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2019-paper-b_1.pdf),
page 2, on the review date. Part (b) counts distinct ordinary binary
strings generated from seed `1`, with alternating additions whose first
bit is `0`. The candidate correctly states that the exact constant is
still unevaluated. I did not investigate preliminary part (a).

For a history of `n` moves, `pi(h)=(u,v)` denotes its two chronological
tapes. Its ordinary output is `reverse(u) 1 v`; reversing the left tape
is essential. Context equality includes both tape lengths and is stronger
than equality of ordinary outputs with different marked seed positions.
At source time `t`, zero-indexed, a legal grid edge consumes the next bit
of its chosen tape only if it equals `t mod 2`. The rectangle consists
of consumed tape-prefix lengths. Arbitrary monotone paths need not be legal.

Starting a factor at phase one complements both tapes relative to phase
zero. It preserves equality, inequality, and lexicographic ordering of
histories with `L<R`. Thus equal-context factor replacement is valid at
both phases, including odd factor lengths, and a smaller replacement
decreases the whole history. The canonical language `K` is factorial:
a smaller equal-context factor would contradict whole-history canonicity.
A shortest noncanonical factor is minimal, so `K=Avoid(F)` and `F` is
anti-factorial.

There is one canonical history per tape pair. The map from tape pairs to
ordinary strings is onto, with at most `n+1` preimages, one per seed
position. Therefore `b_(n+1)<=c_n<=(n+1)b_(n+1)`. Factoriality gives
`c_(m+n)<=c_m c_n`, and all counts are positive. Elementary subadditivity
yields `lim c_n^(1/n)=inf_n c_n^(1/n)`; the polynomial-factor comparison
identifies that limit with the ordinary-string constant `lambda`. This
independently confirms the earlier accepted context-growth input.

I also checked the accepted upper-witness and non-overlap inputs. If a
minimal bad factor `f` and a smaller equal-context history shared their
first move, cancellation would give a smaller history for a proper suffix,
with phase handled by complementation. Their first moves are therefore
`R` and `L`, respectively. An internal common grid vertex would make a
proper prefix of `f` noncanonical. The left-coordinate difference changes
by at most one per step, hence remains strictly positive internally and
returns to zero only at the endpoint. This requires no assumption that
the context has only two histories.

For a purported proper overlap `ab,bc` in `F`, embed their upper witnesses
in the grid for `abc`. At the start of `b` the first replacement is above
the second; at the end the order is reversed. A common internal vertex
permits following the second replacement and then the first, giving a
smaller equal-context history for the proper factor `b`. This contradicts
minimality. An overlap of length one cannot accommodate the strict order
change. Thus the accepted non-overlap result applies in the actual legal
tape grid and in contexts with multiple histories.

## 2. Envelopes and the exact obstruction interpretation

The pointwise minimum of two legal paths' left coordinates is legal.
Their integer coordinate difference cannot change sign without being
zero on a time layer, so switching the followed path occurs only at a
common vertex. Both paths have the same time and consumed tape prefixes
there. The envelope is a legal splice, as is the pointwise maximum.

Let `h` have an upper witness `P` whose gap is at most `D`, and let `f`
be a minimal noncanonical factor of `h`. Embed an upper witness `Q` for
`f` into the whole grid by following `h` elsewhere. Context replacement
makes that path legal for the same complete tapes, at either phase. The
lower envelope of `P,Q` equals `h` outside `f` and at its endpoints.
Internally both are strictly above `h`, so their minimum is strictly
above too; its gap is at most that of `P`. Its restriction proves
`f in F_D`. This covers factors touching either endpoint.

Consequently avoiding D-bubbles equals avoiding `F_D`, and every proper
factor of a member of `F_D` is in `K` and avoids `F_D`. Thus
`MF(K_D)=F_D`, with no artificial minimal obstructions. Increasing the
cap adds possible competitors and may reject more histories, giving

    K subset K_(D+1) subset K_D,
    F_D subset F_(D+1) subset F.

A positive gap is at most either total tape length, hence at most
`floor(n/2)` for a length-`n` witness. All full minimal factors through
length `2D+1` are captured; the claimed coefficient agreement follows.
Empty words and odd lengths produce no exception.

## 3. Independent synchronizer and minimal-factor reconstruction

My implementation uses generic FIFO emission and consumption rather than
a copied transition table. At positive gap `d`, the witness has `d`
unmatched left bits and the history has `d` unmatched right bits. Both
queues retain chronological order. Xor with the next mandated source bit
normalizes the current write symbol to zero.

- History `L` consumes a zero at the left queue head; history `R` emits
  zero at the right queue tail.
- Witness `R` consumes a zero at the right queue head; witness `L` emits
  zero at the left queue tail.
- Complement surviving bits for the next source time. Discard a gap above
  `D`; returning to empty queues completes a bubble.

These operations derive every proposed table entry, including the gap-one
return. A new segment starts on history `R`, witness `L`, with normalized
queues `(1,1)`. Head mismatches cannot lead to an equal-tape completion.

Inductively the subset contains exactly the partial strict-upper segments
whose gaps stayed in `1,...,D` and whose already testable bit constraints
hold. Pending left bits are obligations to future history moves, not a
claim of having read the future tape. At return, both queues are empty
and the segment's two tapes match exactly. Every bounded upper witness
follows one of the tracked branches. All active segments share the same
current source phase even if they began at different phases. There is
no parity restriction on the factor location or length.

Finite queues imply a finite subset monitor with an absorbing rejecting
sink. Exact refinement from acceptance status by target classes yields
a stable DFA congruence and the minimal right-language quotient. Every
independent raw transition was checked against its quotient target.

The minimal-factor product requires first rejection of the full word,
acceptance of its first-letter-deleted suffix, and no successful
continuation from the accepting terminal. These conditions enforce an
accepted proper prefix and suffix, which suffice for all proper factors
in a factorial language. The author's implementation imposes this rule;
it does not incorrectly accept extensions of an earlier bad prefix.

Independent state counts:

| Cap | Raw nonrejecting states | Quotient states |
|---:|---:|---:|
| 1 | 2 | 1 |
| 2 | 6 | 4 |
| 3 | 19 | 9 |
| 4 | 87 | 31 |
| 5 | 426 | 144 |
| 6 | 3678 | 2106 |
| 7 | 20377 | 11662 |

Cap one accepts all histories. The cap-seven maximum active subset size
is 57. A small benchmark ran before the larger capped construction.
No cap-eight search or increase of the old brute-force cap was attempted.

## 4. Rational renewal approximations and entropy

The adjacency convention is outgoing rows with letter multiplicity.
Thus the length-`n` accepted count is `e_start^T A^n 1`, and the transfer
series is `e_start^T (I-zA)^(-1) 1`. Two letters with a common target are
counted twice; no transpose is implicit.

The anti-factorial, non-overlapping properties pass from `F` to `F_D`.
Appending one letter to an accepted word either stays accepted or
completes a unique final forbidden factor. Conversely an accepted prefix
followed by `f in F_D` first becomes forbidden at the end: another
crossing occurrence would create a prohibited proper suffix-prefix
overlap. The resulting recurrence proves, as formal series,

    A_D(z)=1/(1-2z+F_D(z)).

This remains valid for infinite `F_D`, since every coefficient involves
finitely many words. The finite transfer and minimal-factor automata
give rational series. Every full factor eventually enters `F_D`, so
the factor series increase coefficientwise to `F(z)`. No regularity,
rationality, or algebraicity of the limit follows or is asserted.

Positive factorial counts give
`rho_D=lim_n a_(D,n)^(1/n)=inf_n a_(D,n)^(1/n)`. Inclusion gives decreasing
`rho_D>=lambda`. Fix `n`; once `D>=floor(n/2)`, coefficient agreement
gives `rho_D<=c_n^(1/n)`. The decreasing limit is at most every such
root, hence at most their infimum `lambda`, and is also at least
`lambda`. This proves entropy convergence without an unjustified
analytic-limit exchange. The stated weak lower enclosure follows with
the correct directions from the accepted marked-context block injection
at length `2D`.

## 5. Exact separation-three grammar

The independent nine rows equal every displayed and saved row. The
minimal-factor product has 23 states, of which 14 are coaccessible. A
manual reconstruction from this product complements the machine check.
In the independent product numbering, after `RR` one is at state 5,
and `L` reaches state 7. A further `L` terminates `RRLL`. Choosing `R`
instead forces `RLRL`, reaching junction 17 after `RRLRRLRL`. The complete
paths from that junction to its next visit or to the terminal are

    RRLRL       -> junction 17,
    LRLRL       -> junction 17,
    LRLRRLRL    -> junction 17,
    LRLL        -> terminal.

Every other branch is not coaccessible. This derives exactly

    RRLL | RRLRRLRL (RRLRL | LRLRL | LRLRRLRL)* LRLL.

An independent word-path NFA versus DFA traversal checked all 31 reachable
pairs, including rejecting continuations, with identical acceptance.

The loops are a prefix code: one starts `R`, and the two starting `L`
differ at position five. The terminal `LRLL` differs at position four
from every loop starting `L`. Thus parsing distinguishes the terminal
and uniquely chooses every loop. The two outer branches differ at
position four. This proves unambiguity. Fixed prefix/suffix lengths 8
and 4, and loop lengths 5,5,8, give

    F_3(z)=z^4+z^12/(1-2z^5-z^8).

An externally timed exact symbolic solve of the independent transfer
matrix with SymPy 1.14.0 reproduces the claimed `A_3(z)` and verifies
the renewal formula. Every run in the grammar has length at most two.
The two checked length-14 factors have minimum gap four, confirming the
proper inclusion in the full obstruction set. The four-move relation is
used as official attributed context; no preliminary proof is reproduced.

## 6. Complete exact separation-seven certificate

The independent construction produced 20377 raw states and 11662 quotient
states. All 23324 labelled quotient transitions equal the saved table;
all 40754 raw transitions respect the independent quotient map. Every
row of the 26397-state minimal-factor product and every saved coefficient
through length 80 agree too. This is a complete audit, not sampling.

Independently computing `v=A^200 1` reproduces all 11662 saved integer
entries. Their minimum is

    28992044787669162084686071274960499944391494615090998.

With `p=1834856083`, `q=1000000000`, every exact integer
`p*v_i-q*(Av)_i` is positive. The minimum of all 11662 slacks is

    2474277709610765473517281655170069565260566278840834.

The full slack list, encoded as compact JSON with integer entries, has
SHA-256 `7ecf94326086c2099204c22c98098aedbe4043942ef790a58909900a31d2ecde`.
This check uses no floating-point extremum selection.

Let `r=max_i(Av)_i/v_i<p/q`. Positivity and `1<=v/min(v)` imply

    e_start^T A^n 1 <= v_start/min(v) * r^n.

Hence `rho_7<=r<p/q`; inclusion `K subset K_7` proves

    lambda < 1834856083/1000000000 = 1.834856083.

Neither irreducibility nor primitivity nor a numerical Perron estimate
is needed. The archived floating-point exploratory displays are not
inputs to this proof, and the numerical eigenvalue is correctly labelled
evidence.

## 7. Adversarial checks, provenance, and disposition

The independent tape-grid oracle checks every factor of each tested word
using actual tape bits and source phase. It agrees on all 65535 histories
through length 15, separately for caps three and four. This includes
empty/unary words, both factor phases, early returns, and simultaneous
competitors. Cap two agrees on all 8191 histories through length 12.
These are finite evidence; the invariant and envelope proof establish
the unrestricted interpretation.

For all 143 earlier accepted minimal factors through length 24, a separate
grid-feasibility routine reconstructed the lexicographically least
equal-context history, checked noncanonicity and canonical proper prefix
and suffix, and independently computed minimum upper gap by a bottleneck
grid recurrence. Every saved width agrees. For every cap one through
seven, monitor rejection occurs exactly when the computed minimum is
within the cap. Widths eight and nine occur, confirming strictness at
seven. I did not re-enumerate length-24 histories or claim a new proof of
completeness of the earlier accepted factor list.

All saved D3--D7 quotient rows, counts, and positive vectors were compared
in full. All D3 and D7 minimal-factor rows, count lists, and available
renewal identities were compared too. All 70 frozen inputs passed their
hash/size audit. The new argument is elementary conditional on the
explicitly checked earlier inputs. Companion literature supplies method
attribution or future directions; no theorem is imported from an abstract.
Unrestricted bounded delay, full-language regularity, and an entropy-tail
estimate are not asserted. Novelty remains unestablished.

Only assigned `reviews/thirdpass-review-2*` files are retained. The
automatically generated bytecode cache for the independent import was
removed by its exact path. No author,
peer, shared issue, integration, Git, or status file was changed. There
was no commit, push, package installation, or global process kill.

Sources are `thirdpass-review-2-check.py`, `thirdpass-review-2-audit.py`,
and `thirdpass-review-2-run.py`. The wrapper records exact commands,
working directory, child PID, timeout, return status, and reaping; child
stdout records incremental checkpoints. Caps were 15 seconds for the
benchmark, 45 for D7, 35 for each full grid job, and 30 for the artifact
and symbolic audit. Every job completed normally; the longest took under
ten seconds. Python was project `.venv/bin/python` 3.12.14, with SymPy
1.14.0 used only for the small final symbolic solve. No Python-signal
timeout or native indefinite operation was used.

The independent core source was hashed before reading constructor
sources and never subsequently edited. Exact outputs, commands, logs,
dependencies, and this blind report/issue record are frozen in
`thirdpass-review-2-manifest.json`.

Unresolved substantive objections: **none found**. Requested mathematical
repairs: **none**. The exact growth value and full official determination
remain unresolved. Promotion requires the coordinator's reconciliation
of both independent reports and any resulting objections.
