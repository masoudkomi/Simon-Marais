# 2019 B4(b): bounded-separation transfer matrices

**candidate proof - unverified**, version 1, 2026-10-16 UTC.

Author: `owner_2019_structure3`. Requested launch settings are
`gpt-6.1-sol`, `max`; an independent effective-setting readback was not
available. No independent adversarial reviewer has yet audited this text.
The coordinator alone may change its status after the two required reviews.
This concerns only the open part (b). The exact constant remains unknown.

## 1. Inputs, scope and proposed conclusions

Use chronological tape contexts, canonical histories with `L<R`, their
factorial language `K`, the full minimal bad-factor set `F`, and its
series `F(z)` as in the accepted second-pass register
`proofs/reviewed-secondpass-v1.1.md`. The accepted growth constant of
canonical context counts and of the original distinct strings is the same
`lambda`. The full minimal factors have strictly upper equal-context
witnesses, are factor-free and have no proper suffix-prefix overlaps.
These accepted partial facts are inputs here; the preliminary part (a)
is not a research target or reproved.

Proposed additional partial results:

1. A finite automaton for every integer separation cap `D>=1`, containing
   `K` and excluding infinitely many bad histories in general.
2. Its minimal forbidden words are exactly those members of `F` admitting
   a witness whose maximal separation is at most `D`. Thus these are nested
   regular subsets of the actual obstruction set, not artificial rules.
3. Their transfer growth constants decrease to `lambda`.
4. At `D=3` the exact minimal-factor language is the unambiguous regular
   expression

       RRLL | RRLRRLRL (RRLRL | LRLRL | LRLRRLRL)* LRLL,

   with series `F_3(z)=z^4+z^12/(1-2z^5-z^8)`.
5. At `D=7`, a finite exact vector certificate gives the candidate strict
   improvement

       lambda < 1834856083/1000000000 = 1.834856083.

The finite automata and signs are independently reproducible computations;
the unrestricted interpretation depends on the proofs below. They have not
yet received the required two independent agent audits. Generic bounded
residual-buffer synchronization, minimal-forbidden-word automata, rational
transfer series and Perron-style vector bounds are established techniques;
see `thirdpass-literature.md`. Novelty of the particular application and
its structural conclusions is unestablished.

## 2. Paths and separation

For a fixed chronological tape pair `(u,v)`, a history is a monotone path
in the grid of consumed prefix lengths. Write `ell_h(t)` for the number
of left moves among the first `t` moves of `h`. If `h,g` have equal contexts,
their vertices at time `t` lie on the same time layer. Say that `g` is a
strictly upper witness for a length-`n` word `h` if

    ell_g(0)=ell_h(0), ell_g(n)=ell_h(n),
    ell_g(t)>ell_h(t) for 0<t<n.

The separation is `max_t(ell_g(t)-ell_h(t))`. Such a witness is
lexicographically smaller: its first move is `L` and that of `h` is `R`.
The accepted minimal-factor witness lemma ensures that every `f in F`
has a strictly upper witness, even when its complete context has more
than two histories. No two-history assumption is made.

For a pair of legal paths `P,Q` for the same tape pair, their pointwise
lower envelope in left-coordinate is legal. Indeed the coordinate
difference between the paths changes by at most one per time step, so
one can switch which path is followed only at a common vertex. The
envelope is therefore a splice of legal paths at common vertices. The
same argument applies to their upper envelope.

Define `F_D` to be the subset of `F` having a strictly upper witness with
separation at most `D`. Call any word with such a witness a **D-bubble**;
let `K_D` be the histories containing no D-bubble factor.

**Envelope lemma.** Every D-bubble contains a factor belonging to `F_D`.

Take a D-bubble `h` with a strictly upper witness `P`, and choose a
minimal noncanonical factor `f` of `h`. Let `Q` be a strictly upper witness
for `f`, embedded in the grid for `h` by following `h` outside the factor.
Both embedded paths are legal for the complete tape pair of `h`.
Their lower envelope equals `h` outside `f`; on every internal time layer
of `f` both paths are strictly above `h`, so their minimum is too. It is
at most `P`, so its separation above `h` is at most `D`. Its restriction
to `f` is the required bounded witness. This also covers factors meeting
an endpoint of `h`.

Consequently

    K_D = Avoid(F_D),       F_D = MF(K_D).             (1)

The forward inclusion follows from the lemma; the reverse follows by the
definition of `F_D`. Since `F_D` is a subset of the full anti-factorial
set `F`, every proper factor of its members avoids `F_D`, giving the
minimal-forbidden assertion. In particular `K_D` is factorial,
`K subset K_D`, `F_D subset F_(D+1)` and `K_(D+1) subset K_D`.

Every `f` of length `n` has separation at most
`min(number of L, number of R)<=floor(n/2)` for each upper witness.
Thus `F_D` agrees with `F` through length `2D+1`. Equivalently, if
`a_(D,n)=|K_D intersect {L,R}^n|` and `c_n=|K intersect {L,R}^n|`, then

    a_(D,n)=c_n for n<=2D+1.                         (2)

## 3. An explicit finite competitor automaton

Fix a D-bubble candidate and read its history `h` and a possible upper
witness `g` in synchrony by source time. At a time with separation `d>0`,
`g` has consumed `d` more left-tape bits than `h`, while `h` has consumed
`d` more right-tape bits than `g`. Let `u` be the left bits consumed by
`g` and still awaiting `h`; let `v` be the right bits consumed by `h` and
still awaiting `g`. Both queues have length `d`.

Before the next step, xor every stored bit with the mandated source bit
`a`. Thus the next source bit is normalized to zero; after this step the
source phase changes, so every remaining stored bit is complemented.
Use `bar(w)` for bitwise complement. The complete transition table is:

| Move of h | Move of g | Condition | New normalized queues |
|---|---|---|---|
| R | L | d<D | `(bar(u0),bar(v0))` |
| R | R | v starts 0 | `(bar(u),bar(tail(v)0))` |
| L | L | u starts 0 | `(bar(tail(u)0),bar(v))` |
| L | R | u and v start 0, d>1 | `(bar(tail(u)),bar(tail(v)))` |
| L | R | u=v=0, d=1 | successful return to separation zero |

There are no other possibilities: staying on a tape must match its first
pending bit, and decreasing the separation must match both first bits.
Raising the separation appends the present source bit to both queues.
A transition that would raise it above `D` is discarded.

A bubble can begin at any `R` in `h`, with the alternative move `L`.
Immediately after this step its normalized queues are `(1,1)`. Maintain
the subset `S` of all active positive-separation queue pairs, initially
empty. On each history letter take the union of all transitions in the
table, and additionally insert `(1,1)` on `R`. Reject as soon as any
active competitor returns to zero. After rejection the monitor stays
rejecting. The common phase normalization makes a bubble begun at an
arbitrary source time identical to one begun at phase zero; it does not
require a parity restriction on the factor's location or length.

Induction on the read length proves the invariant: before rejection,
`S` consists exactly of the normalized unmatched queues of all still
active strictly upper competitor segments begun since the start, with
all separations between one and `D`. Every successful return certifies
a D-bubble factor, and every such factor follows one of the tracked
nondeterministic branches. Therefore the subset monitor accepts
**exactly** `K_D`, by (1).

Only finitely many queue pairs exist with equal lengths between one and
`D`, and hence only finitely many subsets exist. The construction is a
finite DFA. `thirdpass-delay-automaton.py` builds its reachable part with
an explicit state cap, then performs exact deterministic partition
refinement with a rejecting sink. Stable blocks have identical rejection
status and target blocks on both letters, so the quotient accepts the
same language. An incomplete capped construction is explicitly marked
incomplete and supplies no exact language claim.

If `A_D` is the resulting nonnegative adjacency matrix, counting both
letters when they lead to the same state, every state retained is
accepting and

    A_D(z)=sum(n>=0) a_(D,n) z^n
          =e_start^T (I-z A_D)^(-1) 1.              (3)

Here the use of `A_D` for matrix and `A_D(z)` for series is distinguished
by the argument. Equation (3) is just finite-path enumeration, so the
series is rational. A product DFA that tracks the full word and the
word with its first letter removed recognizes `MF(K_D)`; it accepts only
when the former first rejects and the latter still accepts. This is
implemented by `thirdpass-minimal-delay.py` and is standard forbidden-word
technology, not a claimed new general algorithm.

## 4. Nested rational renewal approximations and convergence

The actual minimal factors have no suffix-prefix overlaps, and `F_D` is
a subset of them. The accepted renewal argument therefore applies without
alteration, including when the regular set `F_D` is infinite:

    A_D(z)=1/(1-2z+F_D(z)).                         (4)

All identities are formal power-series identities; each coefficient
involves only finitely many factors. Hence `F_D(z)` is rational too.
Every fixed member of `F` belongs to some `F_D`, so these rational series
increase coefficientwise to `F(z)`. This does not make the full series
rational or algebraic.

Because `K_D` is factorial, its positive counts are submultiplicative;
thus its root growth exists and

    rho_D = inf(n>=1) a_(D,n)^(1/n) >= lambda.

The sequence `rho_D` is decreasing. Fix any `n`. Once `D>=floor(n/2)`,
(2) gives `rho_D<=c_n^(1/n)`. Taking first the decreasing limit in `D`
and then the infimum over `n` proves

    rho_D decreases to lambda.                    (5)

This is a controlled transfer-matrix representation of the constant,
with a new approximation parameter. It is not an evaluated exact answer
to the official part (b). The accepted marked-context block injection
also gives the elementary enclosure

    rho_D/(2D+1)^(1/(2D)) <= lambda <= rho_D.

It follows from `rho_D<=c_(2D)^(1/(2D))` and the accepted lower bound
`lambda>=(c_(2D)/(2D+1))^(1/(2D))`. It is weak at the small caps used
here and does not improve the accepted numerical lower bound.

## 5. The complete separation-three language

The reachable subset monitor for `D=3` has 19 states. Its exact quotient
has the following nine accepting states, initial state zero; `-` denotes
rejection:

| State | L | R |
|---:|---:|---:|
|0|0|1|
|1|0|2|
|2|3|2|
|3|-|4|
|4|0|5|
|5|6|2|
|6|-|7|
|7|8|5|
|8|4|4|

The quotient is generated from the finite transition rules, not guessed
from a finite list of coefficients. The minimal-forbidden product
construction gives a 23-state DFA. Trimming branches that cannot reach
its terminal gives

    F_3 = {RRLL} union
          RRLRRLRL {RRLRL, LRLRL, LRLRRLRL}* LRLL. (6)

An exact DFA/NFA product-equivalence check is in
`thirdpass-regex3-check.py` and `thirdpass-regex3.json`; it visits 31
reachable product states and finds identical acceptance everywhere.
This finite language equality can alternatively be verified directly
from the displayed nine-state table and the proper-prefix/proper-suffix
criterion. It is not a coefficient-fitting argument.

The three loop words are prefix-free: the first begins `R`; the other
two have common first four letters `LRLR` but different fifth letters.
The terminal suffix begins `LRLL`, whereas any loop beginning `L` begins
`LRLR`. Thus every expression in the long branch has a unique loop
factorization, and the short branch differs at the fourth letter.
Therefore its ordinary generating function is

    F_3(z)=z^4 + z^12/(1-2z^5-z^8),               (7)
    A_3(z)=(z^8+2z^5-1)/
           (z^8-4z^6+2z^5-z^4+2z-1).

All words in (6) have runs of length at most two. This is an infinite
regular collection of true minimal factors, with arbitrary repeated
loops, rather than a finite length cutoff. It is a proper subset of the
whole obstruction set. For example the accepted length-14 obstruction
counts include two factors whose minimum separation is four. The
four-move relation `RRLL` is attributed to the official solution notes;
(6) extends the obstruction analysis for part (b), without solving the
preliminary part.

## 6. Exact separation-seven upper certificate

The complete `D=7` construction has 20,377 reachable nonrejecting subset
states, reduced to 11,662 nonrejecting quotient states. Its maximum
number of simultaneously active queue states is 57. The complete data
are in `computations/thirdpass-delay7-exact.json`, produced in 8.93
seconds under a 30-second external child timeout, with child PID and
reaping recorded in `thirdpass-delay7-exact-job.json`.

Let `A` be its adjacency matrix. The saved integer vector is
`v=A^200 1`, which is entrywise positive. Set

    p=1834856083, q=1000000000.

The independent grid/checker implementation verifies all 11,662 exact
integer inequalities

    p*v_i - q*(A v)_i > 0,

with minimum slack

    2474277709610765473517281655170069565260566278840834.

These signs are in `thirdpass-crosscheck15.json`. The matrix need not be
assumed irreducible. With the weighted sup norm defined by `v`,
`||A||_v=max_i (Av)_i/v_i < p/q`, so every accepted path count has root
limsup strictly below `p/q`. Since every canonical history is accepted,
its growth `lambda` satisfies

    lambda < p/q = 1.834856083.                   (8)

The numerical eigenvalue approximation `1.8348560829149` is evidence only;
it is not used by the strict rational certificate. Early exploratory
power-bound displays used floating point to choose minimum/maximum row
indices. Their source is preserved as
`thirdpass-delay-automaton-v1.py` and their displayed bounds are not used
by (8). The corrected current source compares exact `Fraction`s; the
final certificate checks every row regardless of any extremum selection.

## 7. Verification scope, failures and unresolved work

`thirdpass-delay-crosscheck.py` uses a separate tape-grid dynamic program,
without the queue transition implementation, on all 65,535 binary
histories through length 15 for caps three and four. It agrees with the
monitors in every case. Its minimax grid computation also finds the
minimum separation for each of the 143 independently reviewed minimal
factors through length 24, and agrees with monitor rejection for caps
three through seven. Some factors need caps eight or nine, confirming
that the separation-seven language is still a strict approximation.
These checks are finite evidence, not an independent agent review.

The initial symbolic job failed because system Python had no SymPy; a
second attempt with the bundled Python also lacked it. Both failures
and commands are saved. The existing project `.venv/bin/python` then
ran the small exact rational solve successfully with SymPy 1.14.0; no
package was installed. The system Python used by the standard-library jobs is 3.15.0; the
project virtual environment is Python 3.12.14. All other calculations use
Python's standard library. Every nontrivial computational job was a dedicated externally
timed subprocess with recorded PID, parameters, output and completion.
No existing owner/review file was changed; no worker commit or push was
made. Full downloaded papers are ignored cache material.

Needed next: two fresh blind adversarial audits, including a full
reconstruction of the queue invariant, envelope restriction, convergence,
finite grammar equivalence and all-row certificate. The exact growth
constant, the full minimal-factor series and a useful rigorous upper
bound on the entropy of high-separation obstructions remain open here.
Literature-based directions and setter-attribution limits are in
`thirdpass-literature.md`. Larger caps are not a substitute for those
structural questions.
