# 2019 B4(b): structural second pass, checkpoint 1

Date: 2026-10-16. Author: `owner_2019_secondpass`. Requested launch settings:
`gpt-6.1-sol`, `max`; effective-setting readback unavailable. This note covers
only the open part (b). All proposed mathematical results below are
**candidate proof - unverified**. They have not received the two required
independent audits, and do not alter the accepted partial proof.

The exact value of the growth constant remains unknown. The main structural
routes examined here are an alignment characterization, a narrow-strip walk
characterization, and the collision/canonical-form problem for the concrete
two-tape monoid. A new infinite relation family yields a candidate improved
upper bound. No numerical fit, bounded completion or spectral estimate is
being called an evaluation of the exact constant.

## 1. Checked recoding and an exact alignment characterization

Reverse the final left context and call the resulting chronological tapes
`u,v`. Each pair of source bits is `01`. Assigning both to the left, one to
each side in either order, or both to the right gives exactly

```
A=(01,epsilon), B=(0,1), C=(1,0), D=(epsilon,01).
```

Componentwise concatenation correctly preserves chronological order on both
tapes. The correspondence `LL,LR,RL,RR -> A,B,C,D` is bijective on histories,
and its image on outputs is precisely the even-move marked-context monoid.
Thus each context of total tape length `2k` is a degree-`k` monoid element.
This is a recoding, not an assumption that the four generators freely generate.

**Candidate alignment lemma.** A pair `u,v` belongs to this monoid if and only
if each tape can be tiled by monomers and adjacent dimers `01`, such that the
monomer words on the two tapes are bitwise complements.

Proof: read a generator product. An `A` or `D` supplies one dimer on its tape;
`B` or `C` supplies a pair of opposite monomers, in the same order on the two
tapes. Conversely, start with such tilings. Read the next opposite monomer
pair as `B` or `C`; insert all dimers preceding it as `A` or `D`. Finish with
any remaining dimers. Every such generator product gives the prescribed
tapes. Empty tapes and empty monomer words are included.

The dimers here must be disjoint substrings of the original tapes. Sequential
deletion of newly created `01` pairs is a strictly weaker test: it would admit
`u=0011,v=epsilon`, whereas every legal product with empty second tape uses
only `A` and has first tape `(01)^k`. This blocks an attempted shortcut through
the usual cancellation rule `01 -> epsilon` or the bicyclic monoid.

The relations `AD=DA`, `BCB=ABD`, `CBC=DCA`, and
`ACBBCD=DBCCBA` were checked directly. The first three are not a complete
presentation. In the unblocked history alphabet, orienting `RRLL -> LLRR`
terminates and has no self-overlap, hence is confluent by the elementary
disjoint-replacement argument. The two `RRLL`-avoiding sides of the 12-move
relation therefore cannot follow from that relation alone. This also rules
out hoping that a completion of only those three small equations recovers
the whole concrete kernel.

## 2. An exact narrow-strip walk characterization

For a binary word `w`, let `h_w(i)` be the number of zeros minus the number
of ones in its prefix of length `i`. A shuffle path from `(0,0)` to
`(|u|,|v|)` moves one unit east or north according to which tape supplies
the next source bit. Its consumed prefix has imbalance

```
h_u(i)+h_v(j).
```

**Candidate walk lemma.** The pair admits an alternating shuffle beginning
with `0` if and only if there is such a monotone path all of whose vertices
satisfy `h_u(i)+h_v(j) in {0,1}`. For an even total length its endpoint
imbalance must be zero.

Proof: an alternating prefix has precisely these imbalances. Conversely,
every step changes the displayed sum by `+1` or `-1`; starting at zero and
remaining in `{0,1}` forces the changes `+1,-1,+1,-1,...`, which are exactly
the mandated bits. This includes length zero.

Equivalently put `x_i=h_u(i)` and `y_j=-h_v(j)+1/2`. Then the allowed cells
are those with `|x_i-y_j| <= 1/2`. This is a one-dimensional discrete
Fréchet free-space diagram at its smallest possible threshold. If the
usual discrete definition permits simultaneous diagonal advances, they
can be split: both unit steps must point in the same direction for both
endpoints to be allowed, and one of the two possible intermediate
differences belongs to `{0,1}`. No general Fréchet theorem
is used to infer an enumeration or growth formula.

The formulation suggests using extrema or excursion signatures, but a
total-balance-only test is inadequate: `u=v=0011` has the correct total balance
yet cannot even supply the second mandated bit. A characterization of
entire ordered excursions, rather than just their extrema, is still needed.

## 3. Infinite collision family and candidate upper bound

For integers `p,q >= 1`, define

```
H(p,q) = RRL R^(2p) LR L^(2q) RLL,
K(p,q) = LLR L^(2q) RL R^(2p) LRR.
```

The spaces only separate blocks. Both have length `2p+2q+8`. Direct block
concatenation of the source bits beginning with zero gives, for both,

```
u = 011 (01)^(q-1) 001,
v = 011 (01)^(p-1) 001.
```

For clarity, on `H` the blocks contribute to the left tape
`0`, then `1`, then `(10)^q`, then `01`, and to the right tape
`01`, then `(10)^p`, then `0`, then `1`. These simplify to the displayed
words. On `K` the left/right roles and `p,q` are exchanged, giving the
same ordered pair. A starting bit of one complements both tapes, so the
equality holds in either block phase. Also `K < H` lexicographically for
`L < R`.

Consequently a lexicographically least history for any context or unmarked
word avoids every `H(p,q)`, as well as the published four-move left-hand
side `RRLL`. The four-move replacement and avoiding-representative method
are from the official 2019 solution notes, p. 11. The infinite family is
derived in this second pass; global novelty is not established.

The infinite forbidden language has the regular expression

```
RRLRR (RR)* LRLL (LL)* RLL.
```

The NFA in `computations/secondpass-family.py` recognizes this language or
`RRLL`, restarts state 0 after every input letter, and rejects when a full
forbidden substring appears. Determinization has fourteen reachable
non-reject states. All are accepting. For its adjacency matrix `T`, the
JSON certificate supplies a positive integer vector `v` and verifies
exactly

```
183585027 v_i - 100000000 (T v)_i > 0  for every i.
```

The least slack is `802812110828110`. Defining
`r=max_i (Tv)_i/v_i` gives `r < 183585027/100000000`. Induction from
`1 <= v/min(v)` bounds the number of avoiding histories by a fixed constant
times `r^t`. Since every generated word has an avoiding representative,
the accepted existence theorem for the growth limit would imply

```
lambda < 1.83585027.                     [candidate; unreviewed]
```

The separately reported numerical spectral interval, approximately
`1.835850250400994`, selects the certificate and is not its proof.

Adding all twenty-move bounded minimal obstructions to this NFA produces
163 DFA states and a second exact integer certificate for

```
lambda < 1.83546967.                     [candidate; unreviewed]
```

This latter result depends on the finite context-equality witnesses in
`secondpass-probe20.json`, checked at both phases before use. It is a bound,
not a complete rewriting theorem. The infinite family by itself is
demonstrably incomplete: the 17-move histories

```
RRLRRLRLLRLRLLRLL and LLRLLRLRLLRLRRLRR
```

have the same tapes `(011000110,01100110)` and both avoid all the family
left-hand sides and `RRLL`. Thus even accepting the family bound does not
evaluate the exact growth constant.

## 4. Bounded canonical-form probe and operational record

`secondpass-probe.py` visits histories in lexicographic order, retains the
first representative of each exact tape pair, and marks the others as
nonminimal. A nonminimal word is a minimal forbidden factor precisely when
deleting either its first or last letter leaves a minimal word. Indeed any
shorter nonminimal factor is contained in one of those two proper factors;
replacing that factor in a history preserves context at either bit phase.

The initial run capped history states at 20,000, used at most 16,384 at one
length, and completed in under 0.1 seconds. After inspecting that output,
the explicit second bound was raised to `2^20=1048576` histories at one
length, with the same sixty-second timeout; that run completed in 4.87
seconds. It found **27** minimal forbidden factors through twenty moves.
Their new counts by length are

```
4:1, 12:1, 14:2, 16:3, 17:2, 18:4, 19:8, 20:6.
```

The odd-length obstructions at 17 and 19 rule out a proposed description
that uses only even-length history obstructions. No extrapolation of the
finite list, recurrence or regularity is made.

All commands used `.venv/bin/python`. Every computational child ran through
`secondpass-run.py`, which records its exact command, timeout, PID, UTC
timestamps and completion in a job JSON, directs incremental checkpoints
to a log, and on timeout terminates only that child's process group. All
three jobs completed; no interrupted or unrecorded long run is claimed.

```
.venv/bin/python problems/2019-B4/computations/secondpass-run.py --timeout 60 --record problems/2019-B4/computations/secondpass-probe-job.json --log problems/2019-B4/computations/secondpass-probe.log -- .venv/bin/python -u problems/2019-B4/computations/secondpass-probe.py --max-moves 14 --state-cap 20000 --output problems/2019-B4/computations/secondpass-probe.json
.venv/bin/python problems/2019-B4/computations/secondpass-run.py --timeout 60 --record problems/2019-B4/computations/secondpass-probe20-job.json --log problems/2019-B4/computations/secondpass-probe20.log -- .venv/bin/python -u problems/2019-B4/computations/secondpass-probe.py --max-moves 20 --state-cap 1048576 --output problems/2019-B4/computations/secondpass-probe20.json
.venv/bin/python problems/2019-B4/computations/secondpass-run.py --timeout 60 --record problems/2019-B4/computations/secondpass-family-job.json --log problems/2019-B4/computations/secondpass-family.log -- .venv/bin/python -u problems/2019-B4/computations/secondpass-family.py --probe problems/2019-B4/computations/secondpass-probe20.json --state-cap 20000 --output problems/2019-B4/computations/secondpass-family.json
```

## 5. Literature applicability checks and next structural questions

The primary-source institutional record for Massimiliano Goldwurm and Klaus
Wich, [*Unambiguous Turn Position and Rational Trace Languages*](https://air.unimi.it/handle/2434/4919),
technical report, March 2005, was checked on 2026-10-16. Its abstract gives
examples over direct products of free monoids with unbounded inherent
ambiguity. The indexed author-manuscript introduction was visible; direct
PDF opening returned 403. This is a concrete reason that rationality of our
two-tape relation cannot alone justify a regular unambiguous cross-section.
No theorem about this particular monoid follows from that paper, and no
full paper was cached or redistributed.

Tullio Ceccherini-Silberstein, *Growth and ergodicity of context-free
languages II: the linear case*, Trans. AMS 359 (2007), 605–618,
[DOI 10.1090/S0002-9947-06-03958-4](https://doi.org/10.1090/S0002-9947-06-03958-4),
was located through the author's institutional record and an indexed
manuscript abstract. Its stated growth-sensitivity theorem assumes
unambiguity. Direct AMS PDF opening failed. Our elementary linear grammar
has highly ambiguous derivations, so this theorem does not produce a
growth equation here. No assumption that the whole language is inherently
ambiguous is made.

The following one-variable linear grammar is exact for the odd-length
unmarked language, by grouping two legal insertions:

```
S -> 1 | 10S | 1S0 | 0S1 | S01.
```

Its productions are outer context operations, so their order is the reverse
of chronological construction. Distinct derivations can yield the same
word. Applying an unambiguous-CFG algebraic generating-function theorem
to this displayed grammar would count histories instead of words. This
blocks a second attempted shortcut; it is not a proof against the
existence of some different unambiguous grammar.

Next: derive the full alternating-shuffle obstruction structure from the
narrow-strip diagram, or an unambiguous/controlled-ambiguity representative
language. A finite collection of additional collisions, a fitted
recurrence, or a numerical eigenvalue is insufficient for the exact target.
