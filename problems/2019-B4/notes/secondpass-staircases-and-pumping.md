# 2019 B4(b): staircase relations beyond every finite run model

**candidate proof - unverified**, 2026-10-16, `owner_2019_secondpass`.
This is a new checkpoint after the frozen checkpoint-1 notes; those files
and their evidence are unchanged. None of the new claims below has the
required independent audits. Exact growth remains undetermined.

## 1. Parity-preserving run inflation is sound, but not a complete model

Suppose `h,g` produce the same chronological contexts, `h` starts `R` and
`g` starts `L`. Insert two identical side choices immediately after an
occurrence of that side in `h`, and immediately after the matching tape-bit
occurrence in `g`. If the matched bit is `a`, the inserted bits are
`1-a,a` in both histories. All later source bits retain their phases.
The two enlarged histories still produce the same contexts and still
start `R,L`, respectively. Thus this insertion preserves noncanonicity
of `h`.

In particular increasing any existing history run by an even amount
preserves its noncanonicity, since the insertion can be made within that
run, just after its first letter. It does **not** necessarily preserve
being a minimal bad factor. The bounded `secondpass-pumping.py` probe
tests 152 single-run inflations of the five parity-compressed shapes
found through twenty moves. It finds nonminimal outcomes even when
`RRLL` has not been created. For example

```
RRLRRLRLLRLRLLRLL    is a minimal bad factor;
RRLRRLRLLRLLLRLLRLL  is not minimal.
```

The latter has a noncanonical proper prefix. Its exact smaller context
witness is saved in `secondpass-pumping.json`. Therefore a grammar that
merely inflates arbitrary interior runs while excluding `RRLL` is false.

The probe also shows that all five compressed shapes through length twenty
are insufficient even as sources for later even-run inflations: there is
a new minimal bad history of length 24 with every run at most two. The
next section gives an unrestricted family of such obstructions.

## 2. Staircase tape words

For `n>=1`, let `u_n` be the alternating-run word beginning with zero whose
run lengths are

```
1,2,...,n-1,n,n,n-1,...,2,1.                      (1)
```

It has `2n` runs, equal zero and one multiplicities, and length `n(n+1)`.
For example

```
u_1=01,
u_2=011001,
u_3=011000111001.
```

Define a history of length `2n(n+1)` by concatenating the following blocks,
with the products read in the indicated order:

```
h_n = RR
      [product(j=1,...,n-1) (LR)^j R]
      (LR)^(n-1) LL
      [product(j=n-1,...,1) (RL)^j L].            (2)
```

For `n=1`, the products are empty and this is `RRLL`. Every run of `h_n`
has length one or two. There are `n` double `R` runs followed by `n`
double `L` runs; all intervening letters alternate.

**Candidate staircase lemma.** The pair `(u_n,u_n)` has exactly two
histories: `h_n` and its side-exchange `bar(h_n)`.

### Context calculation

Start with mandated source bit zero. The initial `RR` supplies `01` to
the right tape. For an ascending block `P_j=(LR)^j R`, the first source
bit is `j+1 mod 2`, since its starting index is `j^2+1`. If this bit is
`a`, its left contribution is `a^j` and its right contribution is
`(1-a)^j a`.

For the central block `(LR)^(n-1)LL`, the first source bit is
`a=n+1 mod 2`; its contributions are `a^n (1-a)` on the left and
`(1-a)^(n-1)` on the right.

For a descending block `T_j=(RL)^j L`, the first source bit is `j mod 2`.
Calling it `a`, its contributions are `(1-a)^j a` on the left and
`a^j` on the right. Concatenating these expressions merges the final
single bit of each block into the next run. On each tape the run lengths
become exactly (1). Thus both histories in the lemma exist.

### Forced choices

If only one current tape head is the mandated bit, that side is forced.
If both heads are the mandated bit `a`, choosing a side can lead to a
completion only if consuming that `a` exposes the opposite bit on the
same tape: the other head is still `a` at the next step. In particular
a choice from a run with at least two remaining bits is impossible, and
so is a choice that exhausts its tape while the other still begins `a`.

Along the explicit history (2), both-head choices can occur only before
the first letter of a doubled run: if both heads equal `a`, the next
letter must come from the chosen tape again, by the preceding paragraph.
The remaining run lengths at these locations are obtained directly from
(1) and the contributions above:

| Location in (2) | Chosen side's remaining run | Other side's remaining run |
| --- | ---: | ---: |
| Initial `RR` | 1, with a following opposite bit | 1, with a following opposite bit |
| Final `RR` in `P_j`, `1<=j<=n-1` | 1, with a following opposite bit | `j+1` |
| Central `LL` | 1, with a following opposite bit | `n-1` |
| Final `LL` in `T_j`, `1<=j<=n-1` | 1, with a following opposite bit | `j-1` |

A zero in the last column means the other tape is empty. A one in that
column in the central/descending rows means the other tape consists of
its final one-bit run, so choosing it would exhaust it and fail. All
positive values at least two likewise forbid the other choice. These
facts cover the boundary values `n=1,2` and `j=1,2`.

Hence, once the first side is chosen, all subsequent moves on (2) are
forced for any successful history. If the first side is `R`, the only
successful history is `h_n`. Exchanging the tapes shows that if it is
`L`, the only successful history is `bar(h_n)`. This proves the lemma.

The initial exact grid checker tests `1<=n<=8` and counts exactly two histories
in every case, up to total history length 144. A separate formula/table
checker verifies (2), every row of the forced-choice table, and the exact
two-history count through `n=11`, within 17,689 grid states. This computation is
bounded evidence; the unrestricted claim rests on the block and forced
choice arguments above.

## 3. Consequences for canonical obstructions

As in the rigid two-parameter family, the two histories here differ at
both their first and last letters. Any alternative history for a proper
factor of either would give a third complete history while leaving at
least one endpoint letter unchanged. This is impossible. Thus all their
proper factors have unique contexts.

Consequently every `h_n` is a minimal bad factor, since it begins `R`
whereas its only alternative begins `L`. The full obstruction set has
infinitely many members with all runs at most two. In particular **no
finite collection of base histories, followed only by even run inflation,
can generate the full set**: even inflation of any run would create a
run longer than two, so only finitely many all-runs-at-most-two words
could come from finitely many bases. This observation does not exclude a
recursive grammar or a regular language with infinitely many such bases.

The general no-overlap theorem in `secondpass-canonical-renewal.md` gives
an independent way to organize all these obstructions. It does not by
itself enumerate them. Their sparse staircase subfamily cannot be used
to infer rationality or nonrationality of the entire series.

## 4. A finite-pattern upper bound is always strictly above the true rate

Here the no-overlap and minimal-factor results are used as candidate
lemmas. Let `S` be any finite subset of the full minimal bad factors.
Its avoiding language has a strictly larger growth rate than `lambda`.

First, if `M` is at least the maximum length in `S`, any two `S`-avoiding
words `a,b` can be joined by `(RL)^M` without creating a forbidden word.
Every forbidden word starts `RR` and ends `LL`. None can end inside the
alternating bridge, and any that ends in `b` but begins in `a` would be
longer than `M`; none can begin `RR` inside the bridge. This proves the
finite avoiding language is irreducible. It contains the all-`L` word at
every length and hence has a loop in its finite block graph.

Choose a staircase `h_n` longer than every member of `S`. Its proper
factors are canonical, so it avoids all of `S`. At block size equal to
`|h_n|`, forbidding it deletes at least one edge from the irreducible
nonnegative adjacency matrix for `S` avoidance. The growth rate strictly
decreases under this deletion. Here is the finite-matrix comparison
being used: if `A` is irreducible and `0<=B<=A`, `B!=A`, then
`rho(B)<rho(A)`. Otherwise take a nonzero nonnegative right Perron vector
`x` of `B` and a positive left Perron vector `w` of `A`. Equality of the
radii forces `w^T(A-B)x=0`, hence `(A-B)x=0`; then `Ax=rho(A)x` and
irreducibility makes `x` positive, contradicting `A!=B`. Existence of
these Perron vectors is the standard finite Perron–Frobenius theorem;
the matrices are finite, and the irreducibility condition was verified
by the explicit bridge.

The canonical language avoids `S union {h_n}`, so its growth `lambda`
is at most the newly decreased rate, strictly less than the old one.

More generally, every finite list of sound lex-decreasing context
replacements gives a strictly non-sharp factor-avoidance upper rate:
choose a minimal bad factor inside each left-hand side. Avoiding this
finite selection implies avoiding the original list, and its rate is
already strictly above `lambda` by the preceding paragraph.

This excludes identifying the true constant with the growth root of any
finite list of such forbidden histories. It does not rule out a different
regular cross-section, a finite transfer operator obtained by another
representation, or an algebraic value for `lambda`.

## 5. Bounded core probe and limits

`secondpass-core-probe.py` exhaustively investigates only histories whose
runs all have length at most two. The proven first/last-letter restriction
allows it to fix the prefix `RR` and suffix `LL`. It successively excludes
previously found shorter minimal bad factors in this same class. A factor
of a bounded-run word is again bounded-run, so a newly noncanonical word
that survives those exclusions is checked to have canonical proper
prefix and suffix by an independent exact grid dynamic program.

With a 20,000-node cap **at each length**, it completed every requested
length through 26. The largest layer visited 16,810 nodes and tested 1,544
complete candidate words. Total runtime was below a quarter second.
The new bounded-run minimal-factor counts are

```
4:1, 12:1, 17:2, 20:1, 22:4, 24:1, 25:4.
```

All other lengths through 26 have count zero in this restricted class.
The full obstruction set also has longer-run words, so these are not
the coefficients of its full series. No full language, recurrence or
growth value is inferred from this finite table.

The single-run inflation experiment and staircase check ran as separate
children with explicit sixty-second timeouts and recorded PIDs. New
files are `computations/secondpass-pumping*` and
`computations/secondpass-core-probe*`. No accepted or checkpoint-1 proof
file was edited.
