# R1: separate blind audit of the Newton degeneration extension

Completed 2026-10-16 UTC (2026-10-17 Australia/Brisbane).
Reviewer `/root/review_2021_newton_r1`; requested settings remain
`gpt-6.1-sol` / `max`, without verified effective-setting readback.

**Scoped verdict:** I reconstructed the proposed degeneration and found
no unresolved substantive objection to its conditional statement (D1),
its degree-20 `J=15` consequence (D2), or its finite filter. The
characteristic-19 degree-5 input is the published CLO Theorem 4; its
definition and hypotheses match the polynomial obtained by reduction.
Independent enumeration gives 461 initial `J=15` masks, 392 removed and
69 retained, and 772 combined survivors after the separate earlier
`J=17` exclusion. All 461 saved `J=15` records were also compared after
converting the two mask encodings.

This is one fresh review of this separate candidate, not a promotion and
not an independent reproduction of CLO's published bad-prime computation.
It is not an endorsement of a solution of degree 20 or of the contest
degree classification.

## Frozen inputs and independence

The extension audited is
`notes/coordinator-newton-degeneration-v1.md`, SHA-256
`c38fbfa45e327c671c7737c03a4fdefb7407224445c4b8deb4761c4911a36a4f`.
Its manifest SHA-256 is
`66f3f164e57088236e526ad4d03da1cae6f916a3f63fb9ae5b8fe23596a1bb48`.
All six artifact hashes in that manifest matched, including the
coordinator script's bytes, which were hashed rather than read as code.

I did not construct this extension. I did not read another review,
reviewer's conclusions, shared issue file or shared status file. The
normalization and long-edge inputs had previously been reconstructed in
my own completed v1 audit; that initial audit remains unchanged at
SHA-256
`41ded8b1f1f7541e6b97978008cea7342668bf4452b37615e75d6d07c137d088`.
Its files were not edited. No author/coordinator module or earlier
checker was imported or executed for this extension check.

Only new `reviews/newton-review-1-extension*` files were written. The
candidate, its manifest, the old candidate and the old report were not
modified. No promotion, commit, push or subagent was made.

## Reconstructing the small cluster and scaling

The setup is a nontrivial rational-coefficient polynomial satisfying the
contest's rational shared-witness hypothesis, normalized as in the frozen
packet, with `p>=5`, `d=p+1`, `J>=d/2`, `h=d-J`, `m>=2`. In particular
`c_h` is nonzero of valuation 1, so `m<=h`; this also covers the
otherwise implicit upper bound on `m` needed in the case split.

The established edge from `(h,1)` to `(d-1,0)` has width `J-1` and slope
`-s_0`, where `s_0=1/(J-1)` is nonintegral because `J-1>=2`.
Newton roots are counted with multiplicity in an algebraic closure of
Q_p. The simple root 1 is the unique valuation-zero root. Consequently
the other `h` slots are `m` copies of 0 and `h-m` nonzero roots belonging
to edges on the left. Strict support of the long edge means `(h,1)` is
its left endpoint without a further collinear extension. Slopes increase
from left to right, so every nonzero left-cluster root has valuation
strictly greater than `s_0`.

If `h=m`, the only rational roots are 0 and 1, since a rational root
cannot have the nonintegral valuation `s_0`. The first and last derivative
conditions cannot then be covered without using these two values, in
conflict with the published two-recycled-root obstruction. Hence a
counterexample in the proposed setup would have `h>m`. For `h=2` this
is impossible because `m>=2`; thus the empty conclusion range in (D1)
correctly denotes an excluded case rather than an omitted derivative.

Let `nu` be the least nonzero valuation in the remaining cluster. The
edge immediately to the left of `(h,1)` has slope `-nu`, with some
left endpoint `(i,v(c_i))`, `m<=i<h`. Its line is

```
L_nu(t)=1+(h-t)nu.
```

All coefficient points lie on or above it. For `t>h`, its line lies
strictly below the long-edge line, since `nu>s_0`, and hence below
every nonzero coefficient point there. This independently verifies the
strictness needed for a degree drop, including the degrees `d-1,d`.
It is not enough merely to know nonnegative coefficient valuations.

Choose a finite splitting field `K/Q_p` and a root `alpha` of valuation
`nu`. Such an element is already in `K`; there is no assumption that
`nu` is an integer or that `alpha` is rational. Set
`beta=c_h alpha^h`. For each nonzero ordinary coefficient, the coefficient
of `T^t` in `g=beta^(-1)f(alpha T)` has valuation

```
v(c_t)-1+(t-h)nu >= 0.
```

Therefore `g` is in `O_K[T]`. Its degree-h coefficient is exactly 1,
all higher coefficients reduce to zero, and the degree-i coefficient
is a unit because that endpoint lies on the supporting line. Terms
below `m` are identically zero. The residue polynomial `G` consequently
has degree exactly `h`, is monic, has a root at 0, and has a nonzero
coefficient at some degree `i<h`.

This proves nontriviality even after extending the residue field: any
power of a linear polynomial with root 0 has the form scalar times
`T^h`; monicity would make it `T^h`. The surviving lower coefficient
precludes that. The possible increase of the multiplicity at 0 under
reduction does not turn `G` into a pure power. No assumption of
squarefreeness or distinct cluster roots was used.

## Witness equations survive the reduction

Negate the conclusion of (D1): every center equation for orders
`2,...,h-1` fails. The order-1 center equation already fails because
1 is simple. For each `k=1,...,h-1`, the contest supplies a rational
common root `w_k` of `f,H_k(f)`. It is not 1 and cannot be in the
long cluster, since rational p-adic valuations are integers. Thus
`w_k=0` or `v(w_k)>=nu`, and `z_k=w_k/alpha` lies in `O_K`.

Over the characteristic-zero field `K`, the exact Hasse identity is

```
H_k(g)(T)=(alpha^k/beta) H_k(f)(alpha T).
```

The scalar on the right need not itself be integral. This causes no
problem: the polynomial on the left is integral because `g` is integral
and its Hasse coefficients are multiplied only by integer binomial
coefficients. Exact evaluation gives `g(z_k)=H_k(g)(z_k)=0`.
Reduction commutes with both integral polynomial evaluation and Hasse
differentiation. Therefore

```
G(zbar_k)=H_k(G)(zbar_k)=0,   k=1,...,h-1.
```

Higher-degree terms which vanish in `G` cannot reappear in a Hasse
derivative after reduction: binomial coefficients cannot lower their
valuations. No factorial division is being performed in the residue
field. Repeated witnesses, witnesses with valuation strictly greater
than `nu`, and distinct witnesses which collapse to the same residue
are all allowed. The CA condition requires one common root per order,
without distinctness requirements, so these collisions lose none of
the required quantifiers.

The residue field of the finite extension `K/Q_p` is a finite extension
of F_p. Embed it in the algebraic closure of F_p. The same monic,
nontrivial degree-h polynomial and witnesses then satisfy every Hasse
derivative condition in CLO's definition. Absence of such a polynomial
over the algebraic closure gives the contradiction and establishes the
proposed conditional (D1). Orders `k>=h` are neither used nor needed.

## Published characteristic-p input

I directly read the full cached primary source, Castryck--Laterveer--
Ounaies, [Constraints on counterexamples to the Casas-Alvero conjecture,
and a verification in degree 12](https://arxiv.org/abs/1208.5404),
printed/PDF pages 4--5. Cached file
`.cache/literature/2021/cited-66c5af6a0f0239f5.pdf` still has SHA-256
`d818747102d32060f43ae5f015f27065aadf38699b272a2367749db8b33fedbf`.

Definition 1 is over an algebraically closed field, excludes powers of
linear polynomials, and uses Hasse derivatives for every order from 1
through one below the degree. The degree-h reduction meets precisely
these hypotheses. No all-roots-rational or F_p-rational-witness
assumption occurs in the published definition or is introduced here.

Paragraph 1.7 states that degree 2 has no bad prime, degree 3 has only
the bad prime 2, and degree 4 has bad primes exactly 3,5,7. Theorem 4's
complete degree-5 bad-prime list is

```
2, 3, 7, 11, 131, 193, 599, 3541, 8009.
```

Thus 19 is good for degrees 2,3,4,5 in the required sense. Theorem 4 is
a published computational theorem used as an attributed input. This
audit verifies its statement and its applicability; it does not claim
an independent reimplementation of the paper's Magma computation.

The same page's Table 1 explicitly lists 19 among the degree-6 bad
primes. The degree-7 clause of Theorem 4 states that the smallest
nonbad prime other than 7 is 127, so 19 is also bad in degree 7. The
extension correctly draws no absence conclusion at those degrees.
The degeneration theorem is conditional; it is not a way to assume
the good-prime hypothesis where that hypothesis is false or unverified.

The existing Newton multiplicity input is also consistent with
[Stoll's author-posted notes](https://www.mathe2.uni-bayreuth.de/stoll/teaching/pAdicAnalysis-WS2015/Skript-pAdicAnalysis-pub-print.pdf),
Theorem 3.6, already checked in my frozen report. That explicit
multiplicity reference is now present in the extension candidate.

## Adversarial and degenerate cases checked

- `h=m`: treated before choosing `nu`; an empty remaining cluster is
  never assigned a minimum valuation.
- `m>h`: impossible since `c_h!=0`. At `h=2`, these alternatives and
  `m>=2` completely exhaust the boundary case.
- Several left Newton edges: the **least** left-cluster valuation is
  the correct choice. Larger-valued roots may reduce to 0. For example,
  scaling the toy cluster `p x^2(x-p)(x-p^2)` by `alpha=p` gives
  `T^2(T-1)(T-p)`, reducing to `T^3(T-1)`. The multiplicity increase
  remains compatible with nontriviality. This toy polynomial is not
  asserted to satisfy the contest conditions.
- Fractional `nu`: an algebraic `alpha` is allowed. The toy cluster
  `p x^2(x^2-p)`, scaled by a square root of p, reduces to
  `T^2(T^2-1)`. No integer-valued exponent substitution is assumed.
- Collinear points, repeated roots and witness collisions: none
  invalidates the coefficient inequalities, the surviving endpoint
  coefficient or the CA common-root quantifiers.
- Reduction over a residue extension: the contradiction is over the
  algebraic closure of F_p, so restricting the reduction to F_p would
  be an unnecessary and unsupported assumption. The candidate does not
  make it.
- A surviving lower coefficient ensures `G!=T^h`; without it the
  pure-power degeneration would not contradict the good-prime input.
  The endpoint on the adjacent edge supplies exactly this safeguard.

I found no degenerate counterexample satisfying the stated assumptions.
These checks do not introduce a stronger theorem or extend the verified
good-prime range.

## Independent finite filter and complete record comparison

I derived the filter from normalized derivatives modulo 19, rather than
using the coordinator's ordinary-coefficient computation modulo 361.
Start with `a_0=1,a_1=-1`. For each `j=2,...,18`, a center flag forces
`a_j=-sum_(k<j) binomial(j,k)a_k mod19`; a noncenter flag forces
`a_j=0 mod19`. Require

```
-1+sum_(j=2)^18 (binomial(20,j)/19) a_j = 0 mod19.
```

The canonical-choice rule selects the center whenever it is available.
Although false flags do not enforce center nonvanishing, every actual
counterexample has a canonical mask in the enumerated superset. The
forced disjunction may therefore discard masks lacking all its center
flags. No lift, rational-point sufficiency or height bound is inferred.

The independent checker visits all 131072 masks and finds 6680 passing.
The relevant exact counts are:

| J | h | Initial | Kept by the verified degeneration input |
|---|---:|---:|---:|
| 18 | 2 | 3043 | 0 |
| 17 | 3 | 1674 | 73 |
| 16 | 4 | 887 | 88 |
| 15 | 5 | 461 | 69 |
| at most 14 | at least 6 | 615 | 615, no new filter applied |
| Total | | 6680 | 845 |

For `J=15`, (D1) requires one of orders `k=2,3,4` at 1, equivalently
one of `D_18,D_17,D_16`. Exactly 392 masks lack all three. The separate
earlier `J=17` exact-family exclusion then removes its 73 remaining
masks, giving `845-73=772`. Equivalently the prior 1164 survivors lose
392. The full sorted 772-mask list is saved; compact-JSON SHA-256 is
`64629e7b6d23fa787c62ea27b7a4cce2af1c7d2a2531542f4943eff19ad27c4d`.

After the independent run was complete, I compared the coordinator's
raw result with mine. The coordinator records bit `k-2` for `H_k`, while
my checker uses bit `j-2` for `D_j=H_(20-j)`. Reversing 17 bits converts
them. The comparison checks all 461 individual `J=15` masks bijectively,
their exact `low_center_orders` lists, and every retained/removed flag.
All matched. The initial and filtered histograms also matched. Only raw
author results were read; no coordinator generation code was read.

These computations are finite exact evidence for the necessary filter.
They do not assert that any of the 772 masks corresponds to a polynomial
over Q_p or Q, or that this filter solves degree 20.

## Reproduction, issues and limits

Independent bounded enumeration command, from the repository root:

```
.venv/bin/python -u problems/2021-B4/reviews/newton-review-1-extension-check.py > problems/2021-B4/reviews/newton-review-1-extension-check.jsonl 2> problems/2021-B4/reviews/newton-review-1-extension-check-stderr.txt
```

Supervisor PID 29079, child PID 29080, explicit timeout 30 seconds;
checkpoints every 16384 patterns; exit 0; elapsed 1.485 seconds total,
1.396 seconds in the child. Stderr was empty. Python 3.12.14, standard
library only, with no dependency installation. The child was reaped by
the supervisor; no job was left running and no kill was needed.

The separate raw-record comparison command was:

```
.venv/bin/python problems/2021-B4/reviews/newton-review-1-extension-compare.py > problems/2021-B4/reviews/newton-review-1-extension-raw-comparison.json
```

It exited 0. The complete initial, retained and removed sets, the 845
degeneration-only survivors and the 772 combined survivors are in
`newton-review-1-extension-result.json`. Every input artifact and the
frozen old report were hashed by the independent run. The new report's
manifest separately records reviewer artifacts and source hashes.

There are no open substantive issues in this extension audit. The old
normalization and full `J=17` exclusion remain separate inputs with
their own reports and coordinator promotion gate. Absence of CA
polynomials in characteristic 19 at degrees 6 or 7 is not endorsed:
the cited source says the opposite. No good-prime absence claim was
investigated for further degrees, and `J<d/2` remains outside this
supporting-line argument. No full contest solution, novelty judgment or
absolute-certainty claim is made.

Authoritative account-wide telemetry was 7% total weekly usage at the
start and 8% at the final computational transition, window 10080 minutes,
reset 1792745187. This remained below the 90% stop threshold. No paid
source or separately billed API was used. No new third-party paper was
downloaded or committed during this extension audit.
