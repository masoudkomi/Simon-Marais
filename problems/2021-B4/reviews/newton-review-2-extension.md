# Independent adversarial review R2: Newton degeneration extension v1

Completed 2026-10-16 UTC (2026-10-17 Brisbane). Requested settings:
gpt-6.1-sol/max; no verified effective-setting readback. Reviewer:
`/root/review_2021_newton_r2`.

**Verdict:** the conditional degeneration theorem, its characteristic-19
applications through degree h=5, and the stated complete necessary-pattern
filter pass this audit. No unresolved substantive objection was found.
Coordinator promotion remains a separate action after both independent
reviews. No full polynomial degree or contest classification is proved.

## Independence and exact target

The target is `notes/coordinator-newton-degeneration-v1.md`, SHA-256
`c38fbfa45e327c671c7737c03a4fdefb7407224445c4b8deb4761c4911a36a4f`.
Its manifest has SHA-256
`66f3f164e57088236e526ad4d03da1cae6f916a3f63fb9ae5b8fe23596a1bb48`.
All six listed artifact hashes matched.

Before reading this target, I completed and froze the old-packet blind
report `newton-review-2.md`, SHA-256
`18f04c057a43b715bfa326c050cf61ab574052289706eedc680ff4cea674a818`,
and its manifest, SHA-256
`2186cc6b5fb77cf8677486d19000eed8e8ea11189985020bf635f7d9333d8ab2`,
at 2026-10-16T15:16:51.194844+00:00. Those files were not changed by this
extension audit. I did not construct either candidate and have not read
another review, its conclusions, or shared issue/research/status logs.
The extension's reference to an R1 source manifest was not followed; my
old report independently reconstructed the Newton count with multiplicity.

This review uses the verified old normalization and root-count chain as
an explicit dependency. It also reconstructs the new scaling argument
and all witness quantifiers below. The coordinator's finite program was
not read, imported or executed. A separate F_19 computation finished and
saved its results before I read the coordinator's finite-result JSON.

## 1. Supporting line and the exact cluster being reduced

Under the normalized rational-witness hypothesis, J exists, h=d-J>=2,
v(c_h)=1, and the old supporting-line proof applies for J>=d/2. The
long edge from (h,1) to (d-1,0) has width J-1 and root valuation
s_0=1/(J-1). With p>=5 and even d=p+1>=6, J-1>=2. This valuation is
nonintegral, excluding all these roots as rational witnesses, regardless
of whether some of the other roots are irrational or nonreal.

The unique root of valuation zero is the simple center 1. The h remaining
root slots comprise m copies of zero and h-m other roots. Nonzero roots
in these slots have valuation strictly greater than s_0: their Newton
edges lie strictly to the left of the long edge, with strictly smaller
slopes. No collinear extension is possible because every other nonzero
coefficient point lies strictly above the long edge's supporting line.
Multiplicity is retained in these statements.

If m=h, only 0 and 1 can be rational recycled roots. The precise
two-recycled-root obstruction excludes this case. If m<h, the finite
nonempty set of the other h-m root valuations has a minimum nu>s_0.
This is the valuation corresponding to the rightmost of the left-hand
edges, immediately incident to (h,1). Its other endpoint has some
integer abscissa i with m<=i<h. Every coefficient point lies on or above

    L(t)=1+(h-t)*nu.

Points with t>h are strictly above it: the previous long-edge line is
already strictly higher there because nu>s_0. More generally convexity
also places all points on the required side of this supporting line.
These inequalities are global, not restricted to the two endpoints.

Selecting the **smallest** small-root valuation is essential: it makes
all small rational witnesses integral after division by the selected
root. Using the largest valuation instead would not justify that step.
The candidate uses the correct extremum.

## 2. Finite extension, scaling and nontrivial reduction

A rational polynomial has finitely many roots algebraic over Q_p, so
their splitting field is a finite extension K/Q_p. Choose an actual
root alpha of valuation nu in that field. No assumption that nu is an
integer, or that alpha is rational, is required. Its valuation is in
K's value group, and beta=c_h*alpha^h is a nonzero element of K.

For each ordinary coefficient, the valuation after the proposed scaling
is

    v(c_t*alpha^t/beta)
      = v(c_t)-1+(t-h)*nu >= 0.

This follows exactly from the supporting-line inequality. Vanishing
coefficients cause no exception. Hence g=beta^(-1)f(alpha*T) belongs
to O_K[T]. At degree h its coefficient is exactly 1. Every degree above
h has positive valuation and vanishes in the residue field. The term
of degree i is a unit and survives. Degrees below m vanish identically.
Consequently G has degree exactly h, is monic, is divisible by T^m,
and has a nonzero coefficient below degree h.

This proves nontriviality even if some small roots coincide or further
coefficients vanish: a pure h-th power with root zero over a field
would be a scalar multiple of T^h. Here the leading coefficient is 1
and the lower coefficient is nonzero. There is also a separate useful
check: alpha was chosen as an actual root, so g(1)=0 and therefore
G(1)=0, while G(0)=0. Thus G has the distinct roots 0 and 1 in its
residue field. The reduction cannot collapse to a pure power.

Equivalently, factor f in K. After x=alpha*T, the long-cluster factors
and the center factor reduce to nonzero constants once their scalar
parts are removed. The remaining factors contribute degree h: zero
roots give T, and the other roots have integral ratios to alpha. At
least one ratio is exactly 1. This factorization independently checks
both the cluster size and the nature of the limiting polynomial.

## 3. Every required Hasse witness survives

Suppose no equation H_k(f)(1)=0 holds for 2<=k<=h-1. Because the center
is simple, its H_1 equation also fails. For each individual order
1<=k<=h-1, the contest hypothesis supplies a rational common root w_k
of f and H_k(f). These orders are among the original 1,...,d-1, so no
new witness-existence assumption is being introduced.

Each w_k is different from 1 by the supposition. Its valuation cannot
be s_0, because a nonzero rational number has integral p-adic valuation.
It is therefore zero or one of the h-m small roots, with valuation at
least nu. Thus z_k=w_k/alpha is integral, including z_k=0. Different
orders may choose different roots, and their reductions may coincide;
neither distinction is needed for the Casas-Alvero condition.

The coefficientwise Hasse identity over K is

    H_k(g)(T)=(alpha^k/beta) H_k(f)(alpha*T).

It follows by applying H_k to each monomial, not by dividing an ordinary
derivative in the residue field. The polynomial on the left is integral,
as is g. Substitution of integral z_k gives the exact equalities
g(z_k)=H_k(g)(z_k)=0. Coefficient reduction commutes with Hasse
differentiation and evaluation, since the binomial coefficients are
integers and z_k is integral. Hence

    G(zbar_k)=H_k(G)(zbar_k)=0

for every k=1,...,h-1. A nonunit scalar alpha^k/beta does not invalidate
this argument: the identity is exact in K and the resulting polynomial
is integral because it is H_k(g). There is no division by a factorial
after reduction, no lost derivative order, and no assumption that the
witnesses lie in F_p.

The residue field k of a finite p-adic extension is a finite extension
of F_p and embeds into its algebraic closure. Therefore G is a
nontrivial degree-h CA polynomial over Fbar_p in precisely the Hasse
sense required by the conditional premise. This is the contradiction.
For h=2, m>=2 already gives m=h, and the preceding two-witness case
excludes it; the asserted empty disjunction therefore has its stated
meaning. No undefined minimum valuation is taken in that boundary case.

This reconstructs the entire conditional theorem. Within the
degeneration step, rationality of the selected witnesses is used to
exclude the fractional long cluster; rationality of the original
coefficients and the established normalization remain part of the
underlying hypotheses.

## 4. Characteristic-19 hypotheses checked against the primary source

I read CLO PDF/printed pages 4-5 directly. Source SHA-256:
`d818747102d32060f43ae5f015f27065aadf38699b272a2367749db8b33fedbf`.
The author-posted source is [arXiv:1208.5404](https://arxiv.org/abs/1208.5404).

Definition 1 is over an algebraically closed field, uses every Hasse
derivative of order 1 through degree minus one, and excludes powers of
linear polynomials. The reduced G just constructed satisfies exactly
that definition. The source's bad-prime terminology means existence of
such a nontrivial polynomial in that characteristic. There is no
all-roots-rational restriction to be imported from the separate
characteristic-zero discussion.

The source states that degree 2 has no bad prime, degree 3 has only 2,
and degree 4 has exactly 3,5,7. Theorem 4 lists the degree-5 bad primes
as 2,3,7,11,131,193,599,3541,8009. Thus 19 is good for every h=2,3,4,5.
These are published inputs. I checked their domains and exact lists;
I did not rerun CLO's large computations or claim a new proof of them.

The same page lists 19 in the degree-6 table. The degree-7 theorem says
that, apart from 7, the smallest nonbad prime is 127, which makes 19
bad there also. Consequently this source does not justify applying the
conditional theorem at h=6 or h=7. A more constrained limiting family
could in principle require separate work, but no such conclusion is
being accepted here.

For d=20, h=5 is J=15. The theorem therefore forces a center witness
for at least one of H_2,H_3,H_4. At h=3 and h=4 it reproduces the
earlier low-order center restrictions. It does not by itself provide
the separate exact exclusion of J=17.

## 5. Independent complete finite filter

`newton-review-2-extension-check.py` uses incremental Pascal evaluations
over F_19. Before a_j is set, its stored values[t] are the partial
evaluations D_t(1). A noncenter branch takes a_j=0. A center branch
takes a_j=-values[j] and updates every later value by
binom(t,j)*a_j. It also maintains the divided f(1) residue
-1+sum (binom(20,j)/19)a_j. This is independent of the coordinator's
ordinary-coefficient modulo-19^2 implementation, and uses no coordinator
code or result file.

The full binary tree visits 2^17=131072 choices, with 6680 passing
patterns and the same entire J histogram as the old blind audit. At
J=15 the center orders 2,3,4 correspond to derivative-degree bits
16,15,14 in this review's convention. The complete result is:

| J | h | initial patterns | discarded by low-center disjunction | retained |
|---|---:|---:|---:|---:|
| 18 | 2 | 3043 | 3043 | 0 |
| 17 | 3 | 1674 | 1601 | 73 |
| 16 | 4 | 887 | 799 | 88 |
| 15 | 5 | 461 | 392 | 69 |

The 772 combined survivors consist of 615 with J<15, 69 with J=15,
and 88 with J=16. This uses the previously audited complete J=17
exclusion; retaining those 73 would instead give 845. The 392 newly
discarded masks are exactly the difference between the old set of
1164 and the new set of 772.

After saving this independent result, I read the coordinator's result
JSON and compared every one of its 461 J=15 records. Its masks label
bit k-2 by Hasse derivative order k, whereas this review labels bit
j-2 by derivative degree j=20-k. These conventions require a reversal
of the 17 bits. After that explicit conversion, all masks, every
listed low center order, every retention boolean, both histograms, and
the counts match. There are no duplicate or missing masks. Exact
comparison data are in `newton-review-2-extension-comparison-result.json`.

The center flags may be selected canonically whenever the center is
available, even if another witness is available too. Noncenter branches
impose only necessary residue equations and may therefore overlap with
other patterns. Every actual counterexample has an available canonical
pattern surviving the valid disjunction. Neither enumeration nor
retention establishes a rational or p-adic lift of any pattern.

## 6. Adversarial findings, execution and limits

No substantive defect was found after checking the strict supporting
line, minimum versus maximum small valuation, m=h, repeated roots,
vanishing coefficients, fractional nu, finite splitting-field existence,
nontriviality after reduction, coalescing witnesses, nonprime residue
fields, nonunit scaling factors, Hasse derivative integrality, the exact
characteristic-p theorem domain, and both mask conventions.

The exact bounded commands from the repository root are:

```sh
.venv/bin/python -u problems/2021-B4/reviews/newton-review-2-supervise.py newton-review-2-extension-check.py newton-review-2-extension-independent-run 30
.venv/bin/python -u problems/2021-B4/reviews/newton-review-2-supervise.py newton-review-2-extension-compare.py newton-review-2-extension-compare-run 30
```

The dedicated children were PID 29574, 0.241 seconds, and PID 29861,
0.074 seconds, each under an explicit 30-second external timeout, with
job metadata and complete output saved. Both exited 0 without timeout.
No child remains running and none was killed. Python 3.12.14; main
checks use only the standard library; PDF extraction used pypdf 6.10.0.
No dependency, paid API, or additional worker was used.

Requested settings, exact input/output hashes, primary sources and
account-wide weekly telemetry are recorded in the separate extension
manifest. Only extension-owned `newton-review-2-extension*` files were
written; the old report, old manifest, proof candidates, shared logs,
integration files and Git history were untouched.

The conditional theorem is accepted with its characteristic-p premise.
The stated h<=5 applications and 772 necessary-pattern count are
accepted with the published inputs and audited old J=17 exclusion.
Unrestricted lower J, bad-prime degrees 6 and 7, rational existence of
survivors, degree 20 itself, and the full contest question remain open
within this packet.
