# Independent adversarial audit R1: rational Newton candidates

Initial blind report completed 2026-10-16 UTC (2026-10-17 Australia/Brisbane).
Reviewer: `/root/review_2021_newton_r1`. Requested launch settings were
`gpt-6.1-sol` / `max`; no effective-setting readback was supplied or inferred.

**Disposition:** I reconstructed the complete normalization-to-certificate
argument and found no unresolved substantive mathematical objection to the
partial claims (N1), (N2), the degree-20 `J=17` exclusion, (N5), and the
1164 necessary binary survivors. All 29928 exact family certificates passed
an independent reconstruction and finite-field gcd implementation. This is
one review, not a promotion. The original contest degree classification and
the remaining degree-20 cases remain unsettled by this packet.

There is one nonblocking citation-precision comment, R1-C1 below: Poonen's
displayed theorem does not explicitly write the multiplicity convention.
I verified the required version separately in Michael Stoll's author-posted
notes, Theorem 3.6, and reconstructed the product argument. This does not
invalidate any root count in the candidate.

## Frozen inputs and independence

- Candidate: `notes/padic-rational-newton-obstructions-v1.md`, SHA-256
  `ce3ff564b48841ae3ae1bf66c3cf5303ed2833c2166590cb2460706f01b5c335`.
- Input normalization: `notes/rational-witness-p-plus-one-v1.1.md`, SHA-256
  `ef87eebe1f49302f5e9af1ab0781b73bdb39de9763f7b75d60d5b6f746a9aa85`.
- Candidate checkpoint manifest SHA-256:
  `2859c979347c52fe01e98c0e755c977e1b7c769cbf378861fc1c9b665dcf93ca`.
  Every recorded byte count and file hash matched; the saved check is
  `newton-review-1-manifest-check.json`.
- No other reviewer report, reviewer conclusion, shared issue file, shared
  status file, or research integration file was read. The normalization
  note's reviews were not read. No author module was imported or executed.
- I derived the ordinary-coefficient construction before reading the raw
  certificates. After the independent code was written, a hash mismatch
  required reading only the author's serialization/digest lines returned
  by `rg -n 'sha256|dumps|digest|coeff_stream|encode'` in the compatibility
  script. Its recurrence and gcd routines were not read or used.
- The script, report, logs and local issue list have the assigned
  `reviews/newton-review-1*` prefix. No shared proof was repaired, no result
  was promoted, and no commit, push or subagent was made.

## Official hypotheses and rational normalization

I checked the [official 2021 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf),
page 2: the polynomial has rational coefficients, each derivative order
from 1 through `d-1` has a common root **in Q**, and the witness can vary
with the order. Only the part (b) scope was investigated. The candidate
assumes a nontrivial counterexample and proves partial necessary
conditions for `d=p+1`, `p>=5`; it makes no statement about every degree.
A pure power over C with coefficients in Q has its repeated root in Q,
as follows from the next-to-leading coefficient. Thus the nontriviality
assumption agrees with the contest conclusion.

The relevant published normalization is in Castryck--Laterveer--Ounaies
(CLO), [arXiv:1208.5404](https://arxiv.org/abs/1208.5404), section 3.4,
equations (9)--(10) and the argument preceding Lemma 17. I checked that
argument directly, including why the final affine map can be rational.
The following reconstruction avoids taking the rational normalization on
trust.

Translate a rational shared root with the first derivative to 0 and make
the polynomial monic. It has a double root at 0. Its center `c`, which is
the shared root for derivative order `d-1`, is rational and is a root of
the polynomial. In an algebraic closure of Q_p choose a nonzero root `t`
having smallest valuation, and first scale by `t`. This temporary scaling
need not be rational. All its roots have nonnegative valuation, at least
one nonzero root is a unit, and it has the binomial-coefficient form with
coefficients `a'_j`. The center `-a'_1` is one of these roots, so
`v(a'_1)>=0`. For successive normalized derivatives of degrees
`j=2,...,d-2`, substitute a chosen common root of nonnegative valuation.
The coefficient of `a'_j` is 1; induction gives `v(a'_j)>=0`.

For `2<=j<=p-1`, `v_p(binomial(p+1,j))=1`. For example, this follows from
`binomial(p+1,j)=p(p+1) binomial(p-1,j-2)/(j(j-1))`, whose other factors
are p-units in this range. At a unit root, the leading term is a unit and
all middle terms have positive valuation. Their sum can vanish only if
`a'_1` is a unit. In particular the center before scaling differs from
the double root 0. Rescale by that center rather than by `t`; the two
scalings differ by a p-unit, so integrality is preserved. This final
transformation is rational. It gives the candidate's monic polynomial
with `a_1=-1`, center 1 and `a_j in Z_(p)`.

Reduction is `f mod p=x^(d-1)(x-1)`. Monic division by `x-1` keeps the
quotient integral and reduces it to `x^(d-1)`. Hence every nonzero root
of that quotient has positive valuation, and 1 is simple. This argument
uses algebraic roots only to control valuations; it does not make them
rational. Rational shared witnesses other than 1 therefore have positive
**integer** valuation.

I also checked the derivative normalization algebraically:

```
D_j=(j!/d!) f^(d-j)=H_(d-j)(f)/binomial(d,j)
   =sum_(k=0)^j binomial(j,k) a_k x^(j-k).
```

The last expression is integral before reduction, so there is no division
by a nonunit in a residue field. Multiplication by a nonzero rational
scalar changes no derivative root.

The published witness-cover input is genuinely about recycled witnesses.
[Draisma--de Jong, EMS Newsletter 80](https://www.ems-ph.org/journals/newsletter/pdf/2011-06-80.pdf),
Proposition 6, printed pages 31--32, excludes a chosen covering set of
exactly two shared roots; a singleton would give a pure power. CLO's
type definition in section 1.2 and Proposition 7 agree with this reading.
Thus rational witnesses force at least three distinct rational roots of
`f`. This inference does not assume anything about the other roots.
No other theorem in the newsletter, and no Massri theorem, was used.

## Newton theorem, multiplicity and (N1)

I checked Poonen's [Lectures on rational points on curves](https://math.mit.edu/~poonen/papers/curves.pdf),
section 4.2.1, Theorem 4.2.3, PDF page 68 / printed page 62. Its hypotheses
are an algebraically closed field with a nonarchimedean valuation in a
subgroup of R. Here the field can be the algebraic closure of Q_p with
its extended valuation; the candidate need not apply the theorem over
Q_p itself. The slope sign in the candidate agrees with the coefficient
orientation used in the source. Zero roots are accounted for separately.

For explicit multiplicities I additionally checked Michael Stoll,
[p-adic Analysis in Arithmetic Geometry](https://www.mathe2.uni-bayreuth.de/stoll/teaching/pAdicAnalysis-WS2015/Skript-pAdicAnalysis-pub-print.pdf),
Theorem 3.6, printed/PDF page 16, with section 3's standing hypotheses.
The complete field Q_p with its nontrivial p-adic absolute value satisfies
them; roots are counted in its algebraic closure. The theorem expressly
counts roots with multiplicity. Its Lemma 3.5 gives the short check:
the first and last exponents attaining the weighted coefficient minimum
both add under products, so their difference adds. Factoring the
polynomial into linear factors then counts one for each factor having
the specified root valuation, including repeated factors. No root
separability assumption is needed. For example `(x-p)^2` contributes
width 2 although it has one distinct root.

Because `f(1)/p=-1+sum binomial(d,j)a_j/p=0`, some `a_j` is a p-unit.
Thus `J` exists. With `h=d-J`, the point `(h,1)` occurs; points with
`2<=k<h` are zero coefficients or have integer valuation at least 2;
all other middle points have valuation at least 1. The proposed line is

```
L(k)=(d-1-k)/(J-1).
```

For `J>=d/2`, evenness of `d` gives
`L(2)<2`; all points left of `h` are strictly above the line. Points
strictly between `h` and `d-1` have line height below 1. The leading
point is strictly above the line as well. Consequently the edge is
exactly from `(h,1)` to `(d-1,0)`, and its width `J-1` roots have
valuation `1/(J-1)`. Since `d>=6`, `J-1>=2`; that valuation is not an
integer. None of this cluster can be a rational witness, even if some
of its roots are repeated.

There are `h+1` remaining root slots counted with multiplicity. Of these,
`m` copies are at 0, so there are at most `h-m+2` distinct rational
roots. The covering-set input gives `3<=h-m+2`, precisely (N1). At
degree 20 this excludes `J=18` and forces `m=2` at `J=17`. The argument
does not use an unstated bound on the total number of distinct complex
roots. I checked the threshold `J=d/2`; the inequality is still strict.
For smaller `J` the coefficient bounds alone do not establish the same
edge, as the candidate correctly says.

## Width-one lemma (N2) and the J=17 theoretical reduction

At a nonzero root `u`, divide every term of `P(u)` by
`b_(i+1)u^(i+1)`. Exactly the terms of exponents `i,i+1` survive in the
residue field, with residues `-1,1`. After multiplying `H_k(P)(u)` by
`u^k` and dividing by the same term, the residue is

```
binomial(i+1,k)-binomial(i,k)=binomial(i,k-1).
```

For `0<=i<p` and `1<=k<=i+1` the latter is a p-unit. The binomial
factors on all other terms are integral and cannot make them enter the
minimum. This proves the claimed nonvanishing without an assumption
about higher derivatives of a simple root. It works also at `i=0` and
at `i=p-1`; the exponent and derivative ranges are valid there.

The hypothesis `i<p` matters. As an adversarial boundary check,
`P=x^p(x-1)-p(x-1)^2`, for any `p>=5`, has exactly its terms of
exponents `p,p+1` minimal at `u=1`, but `H_2(P)(1)=0`. This lies outside
the lemma. Thus the candidate has retained a necessary restriction.

For degree 20, `J=17` leaves, in addition to the 16 fractional-valuation
roots, exactly 0 twice, 1 once, and one additional root slot. The third
rational-witness requirement makes that slot a rational root `u`, distinct
from 0 and 1. It is simple and has positive integer valuation. Since
`m=2`, `c_2` is nonzero and has valuation at least 2, while `v(c_3)=1`.
The line joining these points is strictly below all other nonzero points:
at degree 4 and beyond its height is at most 0 and then decreases.
The small root is therefore on a width-one edge with lower exponent 2.
It cannot witness `H_1,H_2,H_3`. At 0, `H_2=c_2` and `H_3=c_3` are
nonzero. The remaining rational witness is 1, giving exactly (N3).
In particular, the new forced center flag is `D_18`, corresponding to
`H_2`; the `D_17` center flag also follows from `a_17` being a unit.

## Exhaustive pattern and family reconstruction

The binary choice must be canonical when it is used to exclude masks:
choose the center whenever it is a shared root. The enumeration need not
enforce that a noncenter flag forbids the center. It is a superset, and
every actual counterexample still supplies a canonical member of it.
Changing from another allowable choice to the canonical choice does not
change the actual coefficient residues or `J`.

I independently traversed all `2^17` choices using ordinary coefficients
`c_t` modulo `19^2=361`, rather than the author's normalized `a_j`
recurrence. Start with `c_20=1,c_19=-20,c_0=c_1=0`. At order
`r=18,17,...,2`, the center equation uniquely gives

```
c_r = -sum_(t=r+1)^20 binomial(t,r)c_t  (mod 361).
```

For a noncenter flag set `c_r=0 mod 361`. This is the correct necessary
condition because `c_r=binomial(20,r)a_(20-r)`, the binomial coefficient
has valuation 1, and a noncenter rational witness reduces to 0 in the
integral normalized derivative. Finally require `sum c_t=0 mod 361`.
The unit indices are exactly those with `c_(20-j)!=0 mod 361`.

The independent results are:

| J | Passing binary masks |
|---|---:|
| 6 | 1 |
| 7 | 1 |
| 8 | 3 |
| 9 | 5 |
| 10 | 26 |
| 11 | 32 |
| 12 | 101 |
| 13 | 131 |
| 14 | 315 |
| 15 | 461 |
| 16 | 887 |
| 17 | 1674 |
| 18 | 3043 |
| Total | 6680 |

The `H_2` center flag retains exactly 73 of the 1674 `J=17` masks and
discards 1601. All 73 also have the `H_3` center flag. For each retained
mask, I independently enumerated every subset of its noncenter positions
as the positions assigned to `U`; all other noncenter positions are
assigned to 0. The resulting set has exactly 29928 distinct
`(center_mask,u_mask)` pairs. Every raw certificate pair belonged to this
set, none was duplicated, and none of the expected pairs was missing.

For each pair I constructed exact integer polynomials without the
author's `a_j` recurrence. Set `c_20(U)=1,c_19(U)=-20,c_0=c_1=0` and solve
the ordinary Hasse equation at the selected `w_r in {0,1,U}`:

```
c_r(U)=-sum_(t=r+1)^20 binomial(t,r)c_t(U)w_r^(t-r).
```

Higher `c_t` are already determined, and lower coefficients do not enter
that derivative. This gives every selected exact derivative equation.
The identity
`binomial(t,r)binomial(20,t)=binomial(20,r)binomial(20-r,t-r)`
shows it is the same normalized family; additionally I checked exact
coefficientwise divisibility by `binomial(20,r)` for every `c_r` in all
29928 families. I then formed `P=sum c_t` and `Q=sum c_t U^t` directly.

The required equations `f(1)=f(u)=0` specialize to `P(u)=Q(u)=0`.
Conversely is not required: these are deliberately only necessary
compatibilities. The first derivative condition at 0 and the last at 1
are automatic in this normalization, so the enumeration covers all
remaining derivative orders. No assumption about the other polynomial
roots, a denominator bound, or a height cutoff on `u` enters this step.

## All modular certificates verified

For each raw record, the independently reconstructed `P,Q` had the
recorded integer degrees and the recorded polynomial SHA-256. The full
coefficient stream SHA-256 matched
`47a5b912863c67f22fed42daaf92b72949a06164966037ac97e4ad8afd22395b`.
The raw certificate file SHA-256 matched
`9676e4885d670a23ea1fb1b0a151ec1f9a8cece8532a1dd43277450b3a7a7fc3`.

I used SymPy 1.14.0's `sympy.polys.galoistools.gf_gcd` over `ZZ` to check
every reported finite-field gcd, independently of the author's code. The
four displayed moduli were independently checked to be prime. In every
modular record both reconstructed leading residues were nonzero, matched
the saved residues, and thus retained both degrees. Every gcd was the
monic constant 1. Every constant record had exactly the saved nonzero
constant `P`. Results:

| Exact finite certificate | Verified records |
|---|---:|
| Nonzero constant P | 73 |
| Coprime modulo 101 | 28583 |
| Coprime modulo 103 | 1213 |
| Coprime modulo 107 | 55 |
| Coprime modulo 109 | 4 |
| Total | 29928 |

In particular all four records using 109 were checked, not spot-checked.
`Q` had degree 20 in every record; nonconstant `P` degrees ranged from 2
to 16. The successful raw log contains the entire degree histogram.

The resultant inference is valid. For integer polynomials, degree
retention means the integer Sylvester determinant reduces to the
Sylvester determinant of the reductions with the same dimensions.
Coprime reductions over the prime field give a nonzero reduced
determinant. Thus the integer resultant is nonzero, so no common root
exists over an algebraic closure of Q. This proves the required
incompatibility for an arbitrary rational value of `U`, including one
whose denominator is divisible by the certificate prime. Directly
reducing the rational value was never assumed. Constants require no
resultant argument.

These are finite exact computational evidence for the exhaustive family
step. Together with the theoretical reductions they support the stated
candidate `J=17` exclusion. They do not establish the unrestricted contest
classification or compatibility of any surviving mask.

## Degree-20 J=16 reconstruction

Here the width-15 edge leaves 0 of multiplicity `m<=3`, the simple center
1 and `4-m` small nonzero roots. If `m=3`, only one small slot remains.
The rational-witness requirement makes it rational, on a width-one edge
with lower exponent 3. It cannot witness `H_3`, while
`H_3(0)=c_3!=0`, so `H_3(1)=0`.

For `m=2`, assume `H_2(1)!=0`. Its rational witness cannot be 0, and
cannot be in the fractional cluster. It is one of the two small root
slots. If their valuations differ, the left part of the Newton polygon
has two width-one edges with lower exponents 2 and 3. Any rational root
in either slot fails `H_2` by (N2), a contradiction. This statement only
uses (N2) for rational possible witnesses; it need not assert that all
algebraic small roots are rational.

Hence both small roots have the same valuation `s`; the rational witness
makes `s` a positive integer. The segment between degrees 2 and 4 gives
`v(c_2)=1+2s` and `v(c_3)>=1+s`. On substituting `x=19^s T` and
dividing by `19^(1+4s)`, all coefficients are integral. Terms of degree
greater than 4 have strictly positive valuation after this division:
for degrees 5--18 the lower bound is `(t-4)s>0`, and the degree-19 and
degree-20 terms have bounds `15s-1>0` and `16s-1>0`.
The reduction is therefore exactly

```
F(T)=T^2(A+BT+CT^2),  A*C!=0.
```

The rational `H_2` witness has nonzero residue `alpha in F_19` after
scaling. Hasse derivatives commute with this scaling up to the nonzero
factor `19^(1+(4-k)s)`, so its exact common-root equations reduce to
`F(alpha)=H_2(F)(alpha)=0`. Subtracting the quadratic factor equation
from `H_2(F)(alpha)=A+3B alpha+6C alpha^2=0` gives
`2B+5C alpha=0`. Therefore `B!=0`,
`alpha=-2B/(5C)`, and the other nonzero initial root is
`beta=-3B/(5C)`. They are distinct and nonzero modulo 19.

Every small root reduces, after scaling, to one of these two residues,
even if it is algebraic rather than rational. Since `H_3(F)=B+4CT`,
its values there are `-3B/5` and `-7B/5`, both nonzero modulo 19.
Thus neither small slot supplies an `H_3` witness. Also `B!=0` means
`c_3!=0`, so 0 supplies none. Only the center remains, giving
`H_3(1)=0` and proving the claimed disjunction (N5).

I independently checked all 18 nonzero residues `B/C`; their complete
table is in the raw log. The argument explicitly uses the nonvanishing
of 2,3,5,7 modulo 19 and makes no claim at the exceptional primes.
A useful stress case is `T^2(T+2)(T+3)`: the first small root can indeed
share `H_2`, while neither shares `H_3`. Thus the local quadratic
configuration by itself is not an illicit contradiction.

Exactly 88 of the 887 `J=16` masks contain an `H_2` or `H_3` center flag;
799 are removed. Together with removing `J=18,17`, the total remaining
is `6680-3043-1674-799=1164`, also obtained by direct enumeration. Their
maximum `J` is 16. Nothing in this audit asserts that any of them lifts
to Q_p or Q.

## Issue disposition and source precision

R1-C1 (nonblocking): the literal display in Poonen Theorem 4.2.3 is a
cardinality of a root set and does not expressly say to count repeated
roots with multiplicity. Taken literally without the usual convention,
it fails on `(T-p)^2`. The candidate states and uses the correct
multiplicity version throughout. Adding Stoll Theorem 3.6 as an explicit
reference, or a short product argument, would make the citation precise.
I verified that reference and argument above; no mathematical blocker
remains. Only the author/coordinator should edit the candidate.

The initial checker attempt stopped because I guessed a hash serialization
containing only `[P,Q]`; the saved format actually includes both masks.
The first polynomial constant, degrees, pattern counts and coverage had
already matched. After reading only the digest-format lines, I corrected
this interface assumption. The first attempt and its raw output are
retained, and the second run completed every check. This was a reviewer
implementation issue, not a candidate defect.

No other substantive objection remains in this review. I did not audit
the older Eisenstein candidate beyond its normalization input, the
author's unrelated scripts, any claimed full solution of degree 20, the
bivariate `J=16` problem, or other years. None is needed for, or endorsed
by, this report. No novelty judgment or absolute-certainty claim is made.

## Reproduction and bounded-job record

From the repository root, the successful independent command is:

```
.venv/bin/python -u problems/2021-B4/reviews/newton-review-1-check.py > problems/2021-B4/reviews/newton-review-1-check-rerun.jsonl
```

The script starts a separate child with an explicit 180-second timeout,
records its PID and command before work, and emits incremental checkpoints
every 512 family records. Successful supervisor PID 27008; child PID
27009; exit 0; total elapsed 9.694 seconds; family audit 8.877 seconds.
Python 3.12.14 and SymPy 1.14.0 were already installed. No dependencies
were installed. No timeout occurred and no process was killed or left
running. Targeted child cleanup is the only timeout action implemented.

The first attempt used the same command with output
`newton-review-1-check.jsonl`; its script snapshot is
`newton-review-1-check-attempt1.py`. Supervisor PID 26786, child PID
26787, exit 1 after 0.893 seconds at the hash-serialization assertion.
The raw output includes the first reconstructed `P,Q` and empty set of
guessed encodings. That failure is fully explained above.
Its stderr is saved in `newton-review-1-attempt1-stderr.txt`.
All review Python/JSON/JSONL files passed a syntax/readability check and
had no trailing whitespace. An optional final `ps` probe was unavailable
inside the sandbox (`operation not permitted`); the supervisor's completed
`wait` and exit record, rather than that probe, establish child completion.

Primary-source retrieval/hash details, including the new Stoll cache,
are in `newton-review-1-sources.json`. Cached papers remain ignored in
`.cache/`; no redistribution licence is claimed. The centrally cached
CLO, newsletter and Poonen PDFs were hashed against their recorded
versions. Stoll's author-posted PDF was newly fetched with `curl -L
--fail`, cached only, and its SHA-256 is
`4c0bb01c0d9aa251d704ec2d8c33b340317b79dd6fe58b0461eaf7fe4017ced3`.

Authoritative `get_usage_limits` telemetry reported 7% total weekly usage
at the beginning and at the final computational transition; weekly window
10080 minutes, reset timestamp 1792745187. This remained below the 90%
stop threshold. No separately billed API or paid source was used.
