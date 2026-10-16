# 2019 B4(b): non-overlapping canonical obstructions and renewal identity

**candidate proof - unverified**, version 1, 2026-10-16.

Author: `owner_2019_secondpass`; requested `gpt-6.1-sol`, `max`, with no
effective-setting readback. This is a proposed structural partial result
for the open part (b), separate from `proof.md` and its accepted audits.
Two independent adversarial audits are still required. No exact evaluation
of the growth constant is claimed.

## Definitions

A history is a word in `L,R`. Starting at phase 0, history position `i`,
numbered from zero, writes bit `i mod 2` to the chosen tape. Both tapes
retain chronological order. Let `pi(h)=(u,v)` be the resulting tape pair.
Starting instead at phase 1 complements both output tapes. Thus any
equality `pi(h)=pi(g)` of equal-length histories remains valid at either
phase and in any surrounding history. Context equality is preserved by
replacing a history factor by an equal-context factor.

Order histories lexicographically with `L<R`. A history is **canonical**
if it is the least history for its tape pair. Each pair has exactly one
canonical history since its histories form a nonempty finite set of a
fixed length. Let `c_n` count canonical histories of length `n`, equivalently
distinct marked chronological contexts after `n` moves. In particular
`c_0=1`, and `c_(2k)=C_k` in the accepted proof.

Let `F` be the set of noncanonical histories every proper contiguous
factor of which is canonical. These are the **minimal bad factors**.
Write `f_n=|F intersect {L,R}^n|` and the formal series

```
C(z)=sum(n>=0) c_n z^n,       F(z)=sum(n>=1) f_n z^n.
```

The reuse of `F` for the set and its series will always be distinguished
by an argument `(z)` for the series. No finite or regular description of
this full set is assumed.

## Lemma 1: canonical histories form a factorial avoidance language

A canonical history has only canonical factors: replacing a noncanonical
factor by a smaller equal-context history would decrease the whole history.
Conversely, every noncanonical history contains a shortest noncanonical
factor, which belongs to `F`. Therefore a history is canonical exactly
when it avoids every member of `F` as a contiguous factor.

This argument also shows that no member of `F` is a proper factor of
another member of `F`.

## Lemma 2: upper witnesses for minimal bad factors

Fix `h in F`, and take any smaller equal-context history `g`. They cannot
share their first letter: otherwise deleting that common initial move
would leave a smaller history for a proper suffix of `h`, at the opposite
bit phase, and complementing the two tapes would contradict membership
in `F`. Therefore `h` starts `R` and `g` starts `L`.

View histories for a fixed pair `(u,v)` as paths in the grid of consumed
prefix lengths. A vertex reached at time `t` is

```
(number of L's in the first t moves, number of R's in those moves).
```

Every legal history for that pair follows east/north edges through the
same grid. If `g` met `h` at an internal vertex at time `t`, their first
`t` moves would have exactly the same two tape prefixes. The `g` prefix
starts `L`, whereas the `h` prefix starts `R`; this would make the proper
prefix of `h` noncanonical. There is no such internal intersection.

Since the difference of their left-coordinate counts changes by at most
one in one time step, starts positive at time 1 and never vanishes until
the common endpoint, we have

```
L_g(t) > L_h(t)       for 0 < t < |h|.             (1)
```

Thus `g` is strictly above `h` on every internal time layer. The analogous
common-suffix cancellation also shows that `h` ends `L` and `g` ends `R`.
In fact `h` begins `RR` and ends `LL`: if its second move were `L`, the
first bit on its left tape would be the opposite of the first bit on
`g`'s left tape; the last two moves follow by the reversed argument.
Hence every member of `F` has length at least four.

## Theorem 3: no proper suffix-prefix overlaps

No nonempty proper suffix of a member of `F` is a prefix of another member
of `F`. Repetition of the same member is included in this assertion.

Suppose otherwise that `ab` and `bc` belong to `F`, with `a,b,c` all
nonempty. In the common history `abc`, replace its factor `ab` by an
upper witness from Lemma 2; call that path `P`. Independently replace
`bc` by one of its upper witnesses; call that path `Q`. Both are paths
for the same complete chronological output pair of `abc`, since both
factor replacements preserve contexts at the appropriate phases.

At time `|a|`, `Q` is on the original path while `P` is strictly above
it, by (1). At time `|ab|`, `P` is on the original path while `Q` is
strictly above it. The integer difference of their left coordinates
changes by at most one per time step. Therefore they meet at some time
strictly between `|a|` and `|ab|`.

Follow `Q` from the start of `b` to such a common vertex, then follow
`P` from that vertex to the end of `b`. This is a legal path between the
original endpoints of `b`, so it produces exactly the same two tape
substrings as `b`. Its first move is `L`, whereas `b`, being the start
of the minimal bad factor `bc`, starts `R`. It is therefore a smaller
history for `b`. Its starting bit phase may be 0 or 1; the phase-invariance
of context equality handles both. But `b` is a proper factor of `ab`,
contradicting the definition of `F`. This proves the assertion.

For an overlap of length one the required strict coordinate-order change
cannot occur in one time step; this is already a contradiction, so there
is no exceptional one-letter case.

## Corollary 4: an exact renewal equation

For every `n>=1`,

```
c_n = 2 c_(n-1) - sum(1<=j<=n) f_j c_(n-j).        (2)
```

Indeed append `L` or `R` to a canonical history of length `n-1`. If the
result is noncanonical, its forbidden factor must end at the new final
letter. That suffix is unique, since otherwise one forbidden suffix
would be a proper factor of another. Removing it gives a canonical prefix.

Conversely, concatenate any canonical prefix with any `f in F`. The
concatenation has no forbidden factor other than this final `f`: a second
one could neither lie in the prefix, lie properly in `f`, contain `f`,
nor cross the concatenation boundary, the last case being a proper
suffix-prefix overlap excluded by Theorem 3. In particular the prefix
of length `n-1` is canonical. This supplies the required bijection for
the subtracted term in (2).

As a formal power-series identity,

```
C(z) = 1 / (1 - 2z + F(z)).                       (3)
```

Replacing each `f in F` by its canonical representative gives a complete
terminating rewriting system for the concrete context equality. It
terminates because all rules preserve length and strictly decrease lexicographic
order on a finite set. Its irreducibles are precisely the canonical
histories by Lemma 1. Hence every history has the same canonical endpoint
under all terminating reductions. Theorem 3 additionally says all
left-hand sides have disjoint occurrences. The system is generally
infinite and is defined intrinsically; (3) is not an explicit enumeration
of `F`, and is not being presented as the final determination in (b).

## Corollary 5: a root equation and a tail constraint

Let `lambda` be the growth constant already obtained in the accepted
partial proof, and put `R=1/lambda`. Since `c_(2k)=C_k` and

```
c_(2k) <= c_(2k+1) <= 2 c_(2k),
```

the root growth of all `c_n` is also `lambda`; thus `C(z)` has radius `R`.
Moreover the accepted infimum formula gives `C_k >= lambda^(2k)`, so
`C(R)` diverges.

Each `f in F` has a canonical prefix of length `|f|-1`, so
`f_n<=2c_(n-1)`. Consequently the series `F(x)` converges for `0<=x<R`.
In that interval, (3) gives

```
F(x) = 2x - 1 + 1/C(x).
```

The nonnegative coefficients of `F` and monotone convergence as `x` tends
up to `R` therefore give

```
F(R)=2R-1,                                         (4)
1-2x+F(x)>0 for 0<=x<R.
```

So `R` is the first positive zero of the denominator in (3), with its
series interpreted up to its convergence boundary. This statement does
not require an analytic continuation or a claim that `F` is rational or
algebraic.

Also

```
sum(n>=1) n f_n R^(n-1) <= 2.                     (5)
```

For if `F'(x)>2` at some `x<R`, the monotonicity of `F'` would make
`1-2y+F(y)` increase strictly for all `y>=x` up to `R`. It could not
converge from its positive value at `x` to zero at `R`. Thus `F'(x)<=2`
for every `x<R`, and monotone convergence proves (5).

## Corollary 6: a new candidate numerical lower bound

Suppose `f_1,...,f_N` are known exactly and put

```
P_N(x)=sum(n<=N) f_n x^n.
```

From (5), the unknown tail at the root satisfies

```
F(R)-P_N(R)
 <= R/(N+1) * (2-P_N'(R)).                        (6)
```

This is just the termwise inequality `1<=n/(N+1)` for all tail indices
`n>=N+1`. Using (4), it follows that

```
E_N(R) >= 0,
E_N(x) = 1 - (2N/(N+1))x
         + sum(n<=N) ((N+1-n)/(N+1)) f_n x^n.      (7)
```

The exhaustive probe through twenty moves supplies

```
N=20,
P_20(x)=x^4+x^12+2x^14+3x^16+2x^17+4x^18+8x^19+6x^20.
```

Its exactness here is finite computational evidence; the unrestricted
deduction is (1)–(7). The probe's context counts agree with all overlapping
previously reviewed enumeration rows.

The accepted lower estimate `lambda>=395397^(1/24)` implies `R<3/5`,
since the exact rational number

```
395397*(3/5)^24 = 111671791435977957/59604644775390625 > 1.
```

Let `r0=100000/175279`. The exact rational computations in
`computations/secondpass-renewal.json` give

```
E_20(r0)<0,
E_20(3/5)=-24103772284678/667572021484375<0.
```

All coefficients of degree at least two in `E_20` are nonnegative, so it
is convex on the positive real axis. It is strictly negative throughout
`[r0,3/5]`, since a convex function is bounded above by its endpoint chord.
Equation (7) and `R<3/5` therefore force `R<r0`, proving the candidate
strict lower bound

```
lambda > 175279/100000 = 1.75279.                 (8)
```

The large numerator of `E_20(r0)` is saved verbatim in the certificate.
Only its exact negative sign is used. The separately displayed numerical
root estimate `0.5705129654647075` is not used by this proof.

Together with the independently constructed avoiding-language certificate,
the current **unreviewed candidate** enclosure would be

```
1.75279 < lambda < 1.83546967.
```

The missing exact determination is now concentrated in evaluating the
complete minimal-obstruction series `F(z)`, rather than mistaking any
finite avoiding automaton for the exact language.

## Computations and attribution

The mathematical derivation above was developed in this second pass.
Novelty has not been established. The construction of avoiding
representatives and the four-move relation are attributed to the official
2019 solution notes in the companion structural checkpoint; the new
non-overlap proof and tail estimate do not reprove preliminary part (a).
No external theorem about rational relations or context-free language
enumeration is assumed.

The finite overlap audit compares every pair of the 27 known minimal bad
factors and finds no proper suffix-prefix overlap. It also obtains the
reciprocal coefficients matching (3), as finite evidence. The family-only
fourteen-state automaton has characteristic polynomial

```
x^2 (x^3-x-1) (x^9-2x^8-x^7+3x^6-x^5-x^2+x-1),
```

computed exactly with SymPy. This is a polynomial for that upper-bound
automaton, and is not asserted to annihilate the true `lambda`.

Commands and PID/timeout records are in `computations/secondpass-*-job.json`.
The new symbolic and renewal runs both used explicit sixty-second child
timeouts and completed in under one second. No worker commit or push was
made, and all accepted files remain untouched.
