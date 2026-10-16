# Independent adversarial audit 1: 2017 concavity bound

Initial blind report, completed 2026-10-16 UTC (2026-10-17 AEST).
Reviewer task: `review_2017_concavity_r1`. The reviewer did not construct the
candidate and did not read the other concavity reviewer's files or conclusions
before this report and its issue log were frozen. No subagent was spawned.
Requested launch settings: `gpt-6.1-sol`, reasoning `max`; verified effective
setting readback: unavailable. These are distinct statements.

## Disposition and scope

**The proposed C1 upper bound survives this independent whole-argument audit.**
I found no substantive mathematical objection requiring a repair. This is a
review recommendation, not a promotion: only the coordinator may change the
candidate's status after both independent audits and issue resolution.

The claim audited is only

\[
\limsup_{n\to\infty}\frac{\log_2 C(n)}{n^2}
 <\frac{324757}{500000}=0.649514.
\]

It neither determines the two rates in the official problem nor establishes
that they coincide. The source cutpath and zone results are attributed inputs.
This audit establishes no novelty or priority claim. No other annual problem
or non-B4 problem was researched.

Frozen candidate:
`notes/deep-literature-r2-concavity-candidate-v1.md`, SHA-256
`07dc9766e56eca4ec3359289a537072d47e6f5ce6b48129538552f54899728fc`.
Construction freeze: `notes/deep-literature-r2-concavity-freeze-v1.json`,
SHA-256 `ec9c085810926b24f43c3249653f84b3a43ec72cbb7e148d38f2fd149b9b65b0`.
My independent run verified the sizes and hashes of all six listed construction
artifacts. I did not execute or modify the constructor's script or outputs.

## Primary-source applicability

I inspected the following original PDFs, rather than relying on abstracts or
the research notes' summaries. Their hashes and page ranges are also in this
review's source ledger.

1. [Official 2017 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-paper-2_1.pdf),
   PDF p. 2, B4 only: integer `n>=2`, regular `2n`-gon of side length one,
   unit-sided quadrilateral tiles, and the liminf and limsup of `log2 C(n)/n^2`.
   The problem expressly allows a nontrivial bound as progress.
2. [Official notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf),
   PDF p. 12: the intended sequence begins `1,1,2,8,62,...`, is identified
   with A006245, and its listed equivalent objects include pseudoline
   arrangements and commutation classes. The notes cite Felsner--Valtr for
   bounds on this very `C(n)`. I also visually inspected the full B4 page.
3. [Felsner--Valtr, Coding and Counting Arrangements of Pseudolines](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf),
   PDF pp. 1--4 and 7--10. Section 1 fixes a north-cell, induced orientations,
   and canonical labels from boundary order. Its tilings have fixed clockwise
   boundary vertices starting at the highest vertex; each rhombus uses the
   corresponding two boundary directions. Page 3 explicitly identifies these
   tilings with normalized dual drawings of marked simple arrangements.
   Pages 3--4 then give the deletion/insertion recurrence. I visually inspected
   pp. 2--3, including the explicit tiling dictionary and Figure 2.
4. [Dallant, arXiv:2502.20909v2](https://arxiv.org/pdf/2502.20909v2),
   version dated 2025-03-07, PDF pp. 1--7, particularly Section 2 and
   Lemmas 3--7. Page 1 uses simple Euclidean pseudolines and
   orientation-preserving homeomorphisms preserving the marked north-cell.
   This is the required convention. I visually inspected p. 5 to verify all
   constants, primes, and the exact integer constraints in Lemma 6.

Thus the candidate uses the intended fixed-polygon count, without quotienting
by rotations/reflections or replacing it by reduced words. This conclusion
uses the official intended equivalence and the published tiling dictionary;
it does not claim a new theorem about alternative meanings of a non-edge-to-edge
geometric tiling. The optional lower-order-factor observation in candidate
lines 191--193 is not needed as a substitute for the dictionary.

## Independent reconstruction: counting to the entropy domain

A directed north-to-south dual path crosses every pseudoline once, hence has
`n` transitions. Let `k,u,m` have the meanings in the candidate. Knuth's
middle-exit lemma says that a pseudoline is available as a middle exit at most
once along one path. Consequently `m<=n`; it also gives the injectivity of
the middle/left-right encoding. Taken middles and taken uniques are disjoint,
so `k+u<=n`, and plainly `k<=m`. The same facts hold after a half-turn.
A taken middle becomes a reverse unique; there can also be reverse uniques
at unbounded cells. The safe statements are the inequalities `k<=u'` and
`k'<=u`, exactly as used. Equality is not assumed.

Dallant's Lemma 3 states precisely

\[
 |\Gamma|\le {n-u\choose k}\left(\frac m{n-u}\right)^k
                      2^{n-k-u},
\]

and the primed bound. In particular it does **not** require `n-u<=m`.
I checked why removing that older restriction is legitimate, using the
Felsner--Valtr tree argument: fix the left-right bitstring, contract unique
steps, and consider depth `h=n-u` with `k` red (middle) steps. There is at most
one blue continuation at a node; the red outdegrees on each root-to-leaf path
sum to at most `m`. The extremal transversal argument allows `h` color classes
with zero sizes, so it also covers `m<h`. Balancing class sizes maximizes each
elementary symmetric polynomial: replacing sizes `s,t` by their average
increases the two-class product, while their sum and all other terms stay
fixed. The resulting bound is `binom(h,k)(m/h)^k`. The tree induction uses
the same balanced maximizing sizes for `k` and `k-1`, as in FV Lemma 5.
Multiplying by `2^(h-k)` gives the displayed bound. This checks the extended
domain without an assumption that the set of available middles is globally
fixed across different paths.

For the zone input, insert a curve following the cutpath, avoiding all old
vertices. It crosses each old pseudoline once and introduces no triple point,
so the simple `(n+1)`-pseudoline hypothesis of Dallant Theorem 4 applies.
Passing from its inserted-line zone back to the old visited cells removes
`2(n+1)` edge incidences on the inserted line and `2n` incidences caused by
splitting crossed old edges. This is the source's `5.5n-5` bound. Counting
lower edges independently gives

\[
 m+u+2(n-u)=2n+m-u.
\]

The terminal south-cell has no lower exits; the reverse count handles upper
edges. Thus the total is `4n+m+m'-u-u'`. Weakening the resulting zone
constraint to `m+m'-u-u'<=1.5n` is in the upper-bound direction. No claim that
these necessary constraints characterize actual paths is made.

All six tuple coordinates are integers in `[0,n]`, so `(n+1)^6` includes
every zero endpoint. This is safer than the source's literal `n^6` count.
For `N=n-u>0`, the binomial theorem at `p=k/N` gives the entropy upper bound
with the correct inequality direction. If `k=0` or `k=N`, take its elementary
endpoint value. If `N=0`, then `k=0` and the all-unique path, if it exists,
is deterministic; its class has size at most one. If `m=k=0`, interpret
the power with exponent zero as one. Empty classes cause no problem.

Normalizing by `n` gives exactly the candidate's `D`, with no missing
nonnegativity conditions. Each class is bounded in both directions, so its
exponent is bounded by `G=min(f,f')`. Summing classes gives

\[
 \gamma_n\le (n+1)^6\,2^{n\sup_D G}.
\]

## Independent reconstruction: concavity and reduction

Write `t=1-u=a+b`, `b=1-u-a`. Expanding binary entropy cancels the
`a log2(t)` terms and gives

\[
 f(\mu,a,u)=a\log_2(\mu/a)+b\log_2((a+b)/b)+b.
\]

The first nonlinear term is the concave perspective of `log2` in
`(mu,a)`; the second is the concave perspective of `log2(1+x)` in `(a,b)`.
Composition with the affine `b` and addition of `b` preserve joint concavity.
This step is joint concavity, not separate concavity.

The limiting extension is continuous on the compact domain used here.
For `a->0`, `0<=a log2(mu/a)<=a log2(1/a)->0` because `a<=mu<=1`.
For `b->0`, `0<=b log2(1+a/b)<=b log2(1+1/b)->0`.
These bounds include `(mu,a)=(0,0)` and `a=b=0`. For example, `a=0`
gives `f=1-u`; `u=1,a=0` gives zero; `b=0` gives
`f=a log2(mu/a)`. No divergent endpoint is ignored.

The linear domain `D` is invariant under exchanging the triples. Averaging
with that exchange preserves feasibility and gives

\[
 \min(f(T),f(T'))\le\tfrac12(f(T)+f(T'))\le f((T+T')/2).
\]

The cross constraints yield `a<=u` and the zone constraint gives
`mu-u<=3/4` in the symmetric triple. The complete symmetric domain is
therefore the one displayed in the candidate, including `a<=1-u` and
`a<=mu`. Finally `f_mu=a/(mu ln 2)>=0` in the interior, with the same
monotonicity at endpoints. Raising `mu` to `min(1,u+3/4)` is safe.

## Independent reconstruction: the two interval bounds

For `0<u<=1/4`, set `mu=u+3/4`. Differentiation while `mu,u` are fixed gives

\[
 f_a=\log_2\frac{\mu(1-u-a)}{a(1-u)}-1.
\]

Its derivative in `a` is negative. At `a=u`, nonnegativity reduces to
`3/4-(5/2)u>=0`, which holds with slack on this entire interval. Since
`a<=u`, the maximum is at `a=u`. The case `u=0` follows by continuity.
The resulting `Phi` is an affine restriction of the jointly concave `f`.
Direct differentiation, independent of the certificate, gives

\[
 \Phi'(u)=\frac{\ln\!\frac{(u+3/4)(1-2u)^2}{u(1-u)^2}
          +u/(u+3/4)+u/(1-u)}{\ln2}-2.
\]

At `u0=21/100`, the logarithm argument reduces to `107648/43687`,
and the rational terms are `7/32` and `21/79`. The value uses
`32/7` and `79/58`. All candidate formulas are correct.
The independently certified `0<Phi'(u0)<1/5000`, combined with the
concave tangent and `u-u0<=1/25`, yields a single strict uniform bound
below `324757/250000`. For `u<u0` the positive slope lowers the tangent;
there is no reversed inequality from a negative displacement.

For `u>=1/4`, set `mu=1` and take the joint tangent at `(a,u)=(1/4,1/4)`.
I independently obtain

\[
 F_0=1+\tfrac12\log_2(3/2),\quad
 f_a=\log_2(4/3)>0,\quad
 f_u=-\log_2(3/2)+\frac1{3\ln2}-1.
\]

The gradient sum is `log2(8/9)+1/(3 ln2)-1<0`, already implied by
`ln2>1/3`. Because `a<=u` and `f_a>0`, the tangent is at most
`F0+(f_a+f_u)(u-1/4)<=F0`. This is a global supporting plane on the
concave domain, and continuity covers `a=0`, `b=0`, and `u=1`.
The rational certificate gives `F0<1293/1000`.

## Independent exact rational certificate

I authored and ran `concavity-review-1-check.py` before reading the
constructor's Python script. It imports no constructor module and does not
execute it. Its primary log enclosure uses a different series:

\[
 t=1-1/r,\quad S_M(r)=\sum_{j=1}^M\frac{t^j}{j},\qquad
 0<\ln r-S_M(r)\le\frac{t^{M+1}}{(M+1)(1-t)},\quad M=96.
\]

This follows by integrating the geometric series for `1/(1-t)`, or from
the positive Mercator series; replace each remaining reciprocal denominator
by `1/(M+1)` to bound the positive tail. All arithmetic in the enclosures
and comparisons is `fractions.Fraction`. There is no floating-point premise.
For positive numerators, a lower bound divides by the upper `ln2` bound,
and an upper bound divides by its lower bound. The saved certificate
contains the full integer numerators and denominators.

Every required rational comparison passed. Decimal diagnostics, which are
only illustrations of the exact intervals, are:

| Quantity | Independently enclosed value |
|---|---:|
| `Phi(21/100)` | between 1.2990193231360811 and 1.2990193231366505 |
| `Phi'(21/100)` | about 0.00013632543865872108 |
| `F0` | about 1.292481250360578 |
| single uniform upper bound `A_hi` from the enclosures | about 1.2990247761541966 |
| `324757/250000-A_hi` | about 0.0000032238458033 (positive exactly) |

Here `A_hi=max(Phi_hi+Phi'_hi/25,F0_hi)` is an exact rational in the
certificate. It is strictly below the claimed objective constant, so the
slack is independent of the feasible tuple and of `n`.

I separately derived the candidate's atanh tail bound by expanding
`ln((1+z)/(1-z))`, with `0<z<1`, and majorizing its remaining positive
terms by a geometric series. My code also computes those `N=80` intervals
independently and checks they intersect the Mercator intervals. After the
independent run, I read the constructor script and checked its interval
division directions. A separate read-only exact comparison reconstructed
all five endpoints from the frozen JSON; every endpoint agreed. I never
reran the constructor's artifact-overwriting script.

The external supervisor imposed 30 seconds, recorded dedicated child PID
64642, and reaped it with exit code zero after about 0.133321 seconds.
There was no timeout or incomplete search. The mesh of `401*201` symmetric
points is labelled finite counterexample-search evidence only; none of the
unrestricted inequalities above rests on that mesh. Boundary examples are
saved as evidence alongside it.

Reproduction command from the repository root:

```sh
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -B -u problems/2017-B4/reviews/concavity-review-1-run.py
```

This command writes only this review's own job, stdout, stderr, and
certificate files. It does not alter the construction freeze.

## Independent reconstruction: the exponent and strictness

FV pp. 3--4 labels the inserted strand canonically from boundary order and
gives exactly `B_(n+1)<=gamma_n B_n`. It counts possible inserted paths in
one fixed old arrangement; it does not count arbitrary insertion histories
as distinct final tilings. Dallant Section 2 uses the same recurrence.

Using the exact fixed rational `A_hi` above, iteration for `j>=2` gives

\[
 \log_2 B_n\le \log_2 B_2+
 6\sum_{j=2}^{n-1}\log_2(j+1)+A_{hi}\sum_{j=2}^{n-1}j
 =\frac{A_{hi}}2 n^2+O(n\log n).
\]

Thus the limsup is at most `A_hi/2`, which is **strictly** below
`324757/500000`. This checks the factor `1/2` and avoids replacing a
pointwise strict inequality by an unjustified strict supremum. No existence
of a limit is assumed.

The literal source edge estimate `5.5n-5` has an irrelevant small-order
exception at `n=1`: one line has two visited halfplanes with total boundary
incidence two, while `5.5-5=0.5`. The official domain starts at `n=2`, and
the preceding iteration starts at `B2=1`; this exception is not used.
Alternatively `gamma1=1` directly supplies the candidate's written sum
starting at `j=1`. The weaker tuple zone constraint also holds directly for
`n=1`. I recorded this as a nonblocking scope clarification, not an objection
to C1.

## Adversarial checks and remaining limits

The issue log records the checked failure modes: zero middles and all-unique
paths; `a=0`, `b=0`, and `u=1`; `m<n-u`; asymmetric tuples; unbounded-cell
uniques; the sign of the small positive derivative; the high-`u` supporting
plane; exact tail and interval arithmetic; and the uniform strict slack and
recurrence factor. No counterexample to C1 or an inference used for it was
found. Source sufficiency, unrestricted optimization by numerical evidence,
and existence of the entropy limit were never assumed.

This audit imports the published middle-exit, zone, and tiling equivalence
results with their stated hypotheses; it is not a formalization or a new
proof of those external theorems. The author's lower-bound or novelty
investigations are outside this review. No full B4 solution is recommended.

Authoritative account-wide telemetry at the start reported 15% weekly used,
window 10080 minutes, reset Unix timestamp 1792745187. The stop threshold
was 90% total weekly used. Only reviewer-prefixed files were written in the
repository. No Git operation, shared-status edit, paid API, source-paper
redistribution, or unrelated process cleanup was performed.
