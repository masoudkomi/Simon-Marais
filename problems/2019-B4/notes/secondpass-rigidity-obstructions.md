# 2019 B4(b): rigid collisions and failed short scheduling rules

**candidate proof - unverified**, 2026-10-16, `owner_2019_secondpass`.
This note is separate from the accepted partial proof. Its unrestricted
claims require the two independent adversarial reviews before promotion.

## 1. An infinite family with exactly two histories

Use the chronological two-tape generators

```
A=(01,epsilon), B=(0,1), C=(1,0), D=(epsilon,01).
```

For `p,q>=1`, define the tape words

```
U_q=01(10)^q01,       V_p=01(10)^p01.
```

**Candidate rigidity lemma.** The pair `(U_q,V_p)` has exactly these two
generator histories:

```
K(p,q)=A C A^(q-1) B^2 D^(p-1) C D,
H(p,q)=D B D^(p-1) C^2 A^(q-1) B A.               (1)
```

Their unblocked histories are respectively

```
LLR L^(2q) RL R^(2p) LRR,
RRL R^(2p) LR L^(2q) RLL.
```

Proof: both tapes begin `01`, so the first source pair must be read wholly
from one tape; hence the first generator is `A` or `D`.

Suppose it is `A`. The remaining tapes are `(10)^q01` and
`01(10)^p01`. At the next pair boundary the next zero must come from the
right. Consuming its following one on the right would leave both heads
equal to one at a zero step, so the next generator must be `C`.

The tapes now have the form `0(10)^(q-1)01` and `1(10)^p01`.
While `q-1` is positive, consuming the next left zero and a right one
would again leave both heads one at a zero step. Thus the next `q-1`
generators are forced to be `A`, leaving `001` and `1(10)^p01`.

The next generator is forced to be `B`, because the left tape begins
`00` and the right tape begins one. The tapes become `01` and `(10)^p01`.
Taking `A` would exhaust the left tape and leave the right starting one
at a zero step. Thus a second `B` is forced. Now the tapes are `1` and
`0(10)^(p-1)01`.

For each of the next `p-1` right `01` pairs, matching its zero with the
last left one would exhaust the left tape and leave a right one at a
zero step. Therefore `D^(p-1)` is forced. The remaining tapes are `1`
and `001`, which force `C D`. This proves the first branch of (1),
including `p=1` or `q=1` where the displayed powers can be empty.

If the first generator is `D`, exchange the two tapes in the preceding
argument. This exchanges `A,D`, exchanges `B,C`, and exchanges `p,q`,
giving precisely the second branch of (1). Both displayed histories
exist and concatenate to the required tapes, so there are exactly two.

The Python check in `secondpass-family.json` independently counts paths
by an exact grid dynamic program for all `1<=p,q<=8`, obtaining exactly
two in all 64 cases. This is bounded evidence for, rather than a substitute
for, the unrestricted forced-choice argument.

## 2. Consequences for minimal factors and finite presentations

The unblocked histories `K,H` start with different letters and end with
different letters, and `K<H` lexicographically. Every proper contiguous
factor of either history has **unique** context: if such a factor had
another history for its context, replacing it would give a third history
for `(U_q,V_p)`. It could not give the other history in (1), since a proper
factor replacement preserves at least one of the first and last letters.
That contradicts the rigidity lemma.

It follows that each `H(p,q)` is a minimal bad factor in the sense of
`secondpass-canonical-renewal.md`. In particular the full minimal-obstruction
series has the exact contribution

```
sum(p,q>=1) z^(2p+2q+8) = z^12/(1-z^2)^2.         (2)
```

This is stronger than merely checking that all these strings are
noncanonical. Distinct parameters give distinct strings. The known short
factor `RRLL` is outside this family.

**Candidate finite-rule obstruction.** No finite set of sound context
replacement equations on the history alphabet presents the full context
equality relation. The same assertion holds for equations on `A,B,C,D`.

To prove it, let `M` be the maximum length of a side of an equation in a
proposed finite set. Choose `H(p,q)` longer than `M`. No nontrivial equation
can apply to it in either direction: every possible factor on which a
side could match is proper, and all such factors have unique contexts.
It is therefore isolated under those equations, even though it has the
equal-context partner `K(p,q)`. For blocked generators use `p+q+4>M`,
noting that a proper blocked factor is also a proper unblocked factor.
Sound equations cannot change length, because output tape length fixes
history length (twice the generator length in the blocked alphabet).

This proves failure of every finite presentation on these fixed
generators; it is not an assertion that finite-state cross-sections or
rational/algebraic growth series are impossible. An infinite presentation
can still have a regular language of normal forms. In particular one
must not infer nonrationality from this obstruction alone.

## 3. A forced-choice family with long common prefixes and suffixes

For `p,q>=0`, put

```
U=011(01)^p00(01)^q,
V=011(01)^(p+q+1).
```

These words have equal lengths, common prefix length at least `2p+3`,
and common suffix length at least `2q`. The pair is admitted: an explicit
generator history is

```
A C A^p B^2 A^q D^(p+q+1).                       (3)
```

Both tapes begin `01`, so the first generator must be `A` or `D`.
Nevertheless `D` is impossible. After it the left tape begins `011`
and the right tape is `1(01)^(p+q+1)`. The next zero is forced from the
left. If either of the next two left ones is consumed before the first
is followed by a left zero, both heads become one at the next zero step.
More explicitly, after that left zero, consuming the first left one
leaves the left head one and the right head one. Therefore the first
left one cannot be consumed; the right initial one is forced instead.
Thereafter each right zero must be followed by the right one, for taking
the first left one would again leave both heads one. The right tape is
eventually exhausted while the left still begins `11`, and the next
required bit is zero. Thus there is no history starting `D`.

The pair obtained by swapping `U,V` forces `D` instead. For any fixed
front-and-back input window size, choosing `p,q` sufficiently large makes
these two instances identical in those windows, including equal tape
lengths, while their first choices differ. Hence a scheduler using only
such fixed windows cannot be complete. It might still use other global
information or unbounded lookahead; no claim against those is made.

The small example `u=0100,v=01100111` also blocks the tempting rule
"if both tapes begin `01`, consume the left pair": the pair is accepted,
while `(u[2:],v)` is rejected. The exact witness and two-step-greedy
counterexample are in `computations/secondpass-structure.json`.

## 4. Other failed structural conjectures

An exhaustive exact grid test of 12012 balanced pairs of total length
twelve gives two pairs with the same tape lengths, endpoint imbalances,
minima, maxima, first bits and last bits but different feasibility:

```
(000,010111101)   accepted, witness RRRRLRLRLRRR;
(000,011001111)   rejected.
```

Thus even all of these range/boundary statistics together do not decide
the alternating-shuffle relation.

The proposed self-shuffle-root class
`epsilon`, `01`, or `01(01|10)*01` agrees through root length ten but is
false. At root length twelve the word

```
u=011000111001
```

can shuffle with a second copy of itself to an alternating word, with
history `LLRLLRLRLLRLRLRRLRLRRLRR`, despite not belonging to that class.
The successful comparison through smaller lengths is finite evidence
only and was not extrapolated. This counterexample shows that excursions
outside the first strip layer matter even on the diagonal `u=v`.

The 27 minimal bad factors through twenty moves have no suffix-prefix
overlaps. Most of their complete tape contexts have exactly two histories,
but four length-19 examples have three. For instance
`RRLRRLRLLLRRLRLLRLL` has three histories for its tape pair. Therefore the
stronger claim "every minimal bad factor is a two-history rigid collision"
is false; only the infinite family in Section 1 has been proved rigid here.
This distinction matters when trying to turn (2) into a complete formula
for the obstruction series.

All computations are bounded, with explicit child PIDs and sixty-second
timeouts recorded in the corresponding `secondpass-*-job.json` files.
None of these obstructions solves or reproduces preliminary part (a).
