# Independent adversarial review R2: frozen Newton packet v1

Initial blind report, completed 2026-10-16 UTC (2026-10-17 Brisbane).
Requested model/effort: gpt-6.1-sol/max. No verified effective-setting
readback is available. Reviewer: `/root/review_2021_newton_r2`.

**Verdict:** the stated partial mathematical conclusions and complete
finite J=17 exclusion pass this audit. No unresolved substantive objection
was found. This is a reviewer recommendation, not coordinator promotion,
and it is not a solution or degree classification for 2021 B4(b).

## Scope, independence and frozen inputs

The target is `notes/padic-rational-newton-obstructions-v1.md`, SHA-256
`ce3ff564b48841ae3ae1bf66c3cf5303ed2833c2166590cb2460706f01b5c335`.
The checkpoint manifest has SHA-256
`2859c979347c52fe01e98c0e755c977e1b7c769cbf378861fc1c9b665dcf93ca`.
Every file hash and byte count listed in that manifest was checked and
matched. The normalization dependency read was
`notes/rational-witness-p-plus-one-v1.1.md`, not an earlier review of it.

I checked the official cached 2021 Paper B, page 2, against the target:
rational coefficients, a rational common root separately for each
derivative of order 1 through d-1, and the open classification for d>=2.
No preliminary part was solved, and no other annual problem was used.

Before this report was written I did not read any other review, review
conclusion, shared issue log, research log, status log, or acceptance file.
Directory inventories exposed filenames only. I did not construct the
candidate. After my independent full computation had finished, I read the
raw author certificates and the few author-source lines specifying their
JSON hash serialization. No author program was imported or executed. No
other review conclusions were used. A coordinator extension was assigned
while this review was in progress; its note has not been read and is
outside this frozen report.

## 1. Published inputs and rational normalization reconstructed

The relevant portions of the cached CLO paper were read directly:
definition of type in section 1.2, Lemma 6 and Proposition 7, equations
(7), (9), (10), the argument in section 3.4, and Lemma 17. The newsletter
Proposition 6 and its proof were read on PDF pages 33-34. That proposition
is about the selected recycled roots, so it supplies the required
obstruction to a covering set of size two. It is not merely a lower bound
on the full root set. A covering set of size one forces a pure power by
the last derivative and successive vanishing derivatives. Consequently
a nontrivial counterexample under the contest hypothesis needs at least
three distinct rational recycled roots. Irrational roots elsewhere do not
affect this deduction.

Here is an independent reconstruction of why the cited normalization
preserves the rational hypothesis. Make the polynomial monic and translate
a rational common root of f and f' to zero. Work in an algebraic closure
of Q_p. Choose a nonzero root of minimum valuation and temporarily divide
all roots by it; all roots then have nonnegative valuation and at least
one is a unit. This temporary scaling can be algebraic. Writing the
normalized derivatives in the displayed D_j form, their shared roots are
integral, and induction on j gives v(a_j)>=0. Evaluating f at a unit root,
using v(binom(p+1,j))=1 for 2<=j<=p-1, shows that a_1 is a unit. The center
-a_1 is therefore nonzero and has the minimum original root valuation.
Scaling instead by that center has the same integrality properties. The
original center is rational, since it is the unique root of the rational
linear polynomial f^(d-1). Hence the final affine transformation is
rational, and the final a_j belong to Z_(p).

The resulting reduction is x^(d-1)(x-1). Dividing by x-1 in Z_(p)[x]
gives a monic factor reducing to x^(d-1). A monic integral polynomial has
no root of negative valuation; a unit root of this factor would contradict
its reduction. Thus 1 is the unique valuation-zero root, is simple, and
all other nonzero roots have positive valuation. This verifies the exact
hypotheses used later without requiring all roots to be rational.

The identity

    H_(d-j)(f) / binom(d,j) = D_j
      = sum_(k=0)^j binom(j,k) a_k x^(j-k)

holds over Q. This displayed polynomial, rather than division after
reduction, establishes the p-integrality of D_j. Rational noncenter
witnesses reduce to zero because their positive valuations are integers.

Finally, f(1)/p=-1+sum (binom(d,j)/p)a_j proves that some a_j is a unit.
Thus J exists. With h=d-J, v(c_h)=1; coefficients of degrees 2 through
h-1 have valuation at least 2 or vanish; all other middle coefficients
have valuation at least 1. These statements use the rationality of a_j
to replace a positive valuation by a valuation at least 1.

## 2. Long edge and multiplicity count

For even d=p+1>=6 and J>=d/2, the line joining (h,1) to (d-1,0) is below
every other nonzero coefficient point. To its left the largest relevant
line height is (d-3)/(J-1)<2; to its right, up to d-2, it is below 1;
at degree d it is negative. The constant and linear coefficients vanish.
This proves the claimed width J-1 and valuation 1/(J-1). The condition
J>=d/2 and the strict inequality were checked at the boundary J=d/2,
including d=6. They are not extended to smaller J.

Poonen Theorem 4.2.3 was read on PDF page 68, printed page 62. Its
algebraically closed valued-field hypotheses hold in Q_p's algebraic
closure. The root count here must include multiplicities. For completeness
I reconstructed that convention rather than relying on the source's set
cardinality typography: after substituting x=lambda*T with v(lambda)=s,
normalize each linear factor by its coefficient of minimum valuation.
The nonzero reductions multiply, since the residue ring is a field. A
root of valuation greater than s contributes T, a root of valuation less
than s contributes a nonzero constant, and a root of valuation exactly s
contributes T minus a nonzero residue. Therefore the largest and smallest
exponents of minimum valuation differ by precisely the number of roots
of valuation s, with repeated linear factors counted repeatedly. This is
the Newton width assertion required by the packet. Zero roots are counted
separately through their multiplicity m.

Because J-1>=2, none of the long-edge roots is rational. The h+1 remaining
roots counted with multiplicity include m copies of zero and one simple
copy of 1. They give at most h-m+2 distinct rational roots. The covering
set obstruction just checked therefore implies m<=h-1. In degree 20 this
excludes J=18 and forces m=2 when J=17. Confusing distinct roots with
multiplicity, or assuming all the other roots rational, is unnecessary.

## 3. Width-one derivative lemma

Let the only two minimum-valuation terms at a nonzero root u be those of
degrees i and i+1. Divide by b_(i+1)u^(i+1). Their residues are -1 and 1.
After multiplying H_k(P)(u) by u^k and making the same division, the
residue is

    binom(i+1,k)-binom(i,k)=binom(i,k-1).

For 0<=i<p and 1<=k<=i+1, this binomial coefficient is a p-unit. All
other terms retain positive valuation, because multiplication by an
integer binomial coefficient cannot lower it. Hence the Hasse derivative
does not vanish. The endpoints i=0 and i=p-1, k=i+1, zero coefficients,
and terms of degree above p cause no exception. The explicit hypothesis
that only the endpoints lie on the supporting line supplies exactly the
two minimum terms. The argument does not use the false assertion that a
simple root cannot also annul a higher derivative.

## 4. J=17 theoretical and family reductions

For d=20, J=17, the width-16 cluster leaves four roots counted with
multiplicity. They include zero twice and 1 once. A third distinct
rational recycled root forces the last root u to be rational, distinct
from 0 and 1, and of positive integral valuation. The left edge is from
(2,v(c_2)) to (3,1), with v(c_2)>=2. Its extended supporting line is
strictly below all subsequent points. The width-one lemma with i=2
prevents u from witnessing H_1, H_2, or H_3. Since c_2 and c_3 are nonzero,
zero cannot witness H_2 or H_3 either. Thus H_2(1)=H_3(1)=0.

Choosing the center whenever available is legitimate even if another
witness is available simultaneously. The binary pattern computation keeps
a superset: a noncenter choice does not need to certify failure at 1.
Every actual counterexample nevertheless supplies a retained pattern.
Bits j-2, j=2,...,18, encode D_j, so the H_2 and H_3 flags are bits 16
and 15 respectively. Since a_17 is a unit, the H_3 flag must already be
present. The additional H_2 condition leaves 73 patterns.

Each noncenter witness must now be 0 or u. Exhaustively assigning these
two values covers all actual witnesses; derivatives of order 1 and 19
are already accounted for by the double zero and the center. To verify
the family construction by a distinct route, I worked with ordinary
coefficients c_k(U). Start with c_20=1 and c_19=-20, and descend
k=18,...,2 using

    c_k(U) = -sum_(t=k+1)^20 binom(t,k)c_t(U)w_k^(t-k),
    w_k in {0,1,U}.

This directly solves H_k(f)(w_k)=0. Coefficients c_0=c_1=0 are fixed.
The identity binom(t,k)binom(20,t)=binom(20,k)binom(20-k,t-k)
also verifies that every c_k is coefficientwise divisible by binom(20,k),
so this ordinary-coefficient construction agrees with the normalized
integer-polynomial family. The two remaining equations are P=f_U(1)=0
and Q=f_U(U)=0. Degenerate choices U=0 or U=1 are harmless: the
certificates exclude a larger set of values than the theoretical reduction
requires. No root-height bound or assumption about other roots enters.

## 5. Complete independent exact computation and certificate comparison

`newton-review-2-independent.py` first completed without reading author
programs or result files. Its binary enumeration uses ordinary Hasse
coefficients modulo 19^2, not the author's a_j recurrence. At a noncenter
branch it sets c_k=0; at a center branch it solves H_k(f)(1)=0 modulo
19^2. All middle c_k are divisible by 19. A leaf passes exactly when
f(1)=0 modulo 19^2; its J is recovered from the smallest degree whose
c_k is nonzero modulo 19^2. The tree visits all 131072 choices exactly
once.

The independent histogram is:

| J | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| patterns | 1 | 1 | 3 | 5 | 26 | 32 | 101 | 131 | 315 | 461 | 887 | 1674 | 3043 |

The 73 J=17 patterns have exactly 29928 refinements. Each was generated
over the integers by the ordinary-coefficient formula above. I used my
own Euclidean remainder implementation over the finite fields to check
coprimality, retaining both integer degrees. The certificate distribution
is 73 nonzero constants, 28583 at prime 101, 1213 at 103, 55 at 107,
and 4 at 109. No case was unresolved.

Only after that blind run completed, `newton-review-2-compare.py`
reconstructed every family again and compared all raw author records:

- all 29928 keys occur exactly once, with no missing or spurious family;
- every polynomial pair, degree, leading residue, constant, and prime
  agrees with the independent reconstruction;
- primality and both nonzero leading residues are checked for every
  modular certificate, and the recorded gcd is recomputed independently;
- all J=17 retained/discarded mask lists and all J=16 mask lists agree.

The complete author polynomial stream hash was independently reproduced:
`47a5b912863c67f22fed42daaf92b72949a06164966037ac97e4ad8afd22395b`.
The complete author certificate hash is
`9676e4885d670a23ea1fb1b0a151ec1f9a8cece8532a1dd43277450b3a7a7fc3`.
My separate polynomial serialization gives stream hash
`d26930f5a90034d2c5f5fabfa787af4cdbbfe6e5184d73b2d71e11230b13e01c`.

The inference from these finite certificates is valid: retained degrees
make the reduced resultant the reduction of the integer resultant.
Coprimality modulo the recorded prime therefore makes that resultant a
nonzero integer. Thus P,Q have no common complex root. Degree retention
is essential and was checked, including the possibility of leading
coefficients divisible by the testing prime. This excludes every member
of the complete finite family, and hence excludes J=17 under the
theoretical reduction. This is not empirical searching over rational U.

## 6. J=16 disjunction reconstructed

The long edge has width 15, so m<=3. If m=3, only one small positive-
valuation root remains. A third rational recycled root makes it rational,
and the left width-one edge with i=3 prevents it from witnessing H_3.
Since zero cannot witness H_3 either, H_3(1)=0.

If m=2 and H_2(1)!=0, the H_2 witness is one of the two small roots.
Different valuations would give two width-one edges, with lower exponents
2 and 3; every possible rational H_2 witness on either is prohibited by
the lemma. The valuations must therefore coincide at s. One root is
rational, so s is a positive integer, and v(c_2)=1+2s. The coefficient
of degree 3 lies on or above the line from (2,1+2s) to (4,1).

For x=19^s*T and division by 19^(1+4s), all coefficients are integral.
For degrees 5 through 18, valuation is at least 1+ks>1+4s; degree 19
has valuation 19s>1+4s, and degree 20 is also higher. Reduction therefore
has exactly the asserted form T^2(A+BT+CT^2), with A,C nonzero. Hasse
derivatives commute with this scaling after multiplication by the
appropriate nonzero scalar; integer binomial coefficients preserve the
positive valuation of discarded terms.

The rational H_2 witness has a nonzero residue alpha in F_19. Subtracting
the quadratic root equation from H_2(F)(alpha)=0 gives
2B+5C*alpha=0. Since alpha and C are nonzero, B is nonzero. The other
quadratic root is beta=-3B/(5C), whereas alpha=-2B/(5C). Both are nonzero
and distinct. Every small root reduces to one of these two values, even
if it is not rational. At these residues H_3(F) is respectively -3B/5
and -7B/5, both nonzero in characteristic 19. Thus no small root can
witness H_3, and B!=0 ensures that zero cannot either. H_3(1)=0 follows.
This proves the disjunction. The use of p=19 is essential to the unit
checks; no exceptional-prime generalization is being accepted.

As a stronger finite check than merely substituting 18 proposed ratios,
I divided by C and enumerated every A!=0, every B, and every nonzero
alpha over F_19: 18*19*18=6156 triples. Exactly 18 satisfy the root and
H_2 equations, and each has the asserted alpha,beta and nonvanishing
H_3 values. The binary filter leaves 88 of the original 887 J=16 masks,
discarding 799. Consequently 6680-3043-1674-799=1164 necessary patterns
remain, with largest J=16. These are necessary patterns only.

## 7. Counterexample and boundary-case audit

I specifically challenged repeated roots, unavailable irrational witnesses,
center/noncenter simultaneous choices, zero coefficients, absent J,
the edge threshold J=d/2, v(c_2)=2 in J=17, both possible J=16
multiplicities, coincident quadratic roots, B=0, reduction of Hasse
derivatives, prime-field versus algebraic-residue witnesses, and vanishing
leading coefficients in modular tests. The reconstruction above resolves
each within the stated hypotheses. No counterexample to a stated partial
claim was found. Lower J, higher-dimensional compatibility families,
exceptional primes for the quadratic identities, and all-degree
classification remain outside this result.

The Poonen statement uses root-set cardinality typography without an
explicit multiplicity qualifier in the displayed statement. This does
not leave a proof gap here: the multiplicity version actually needed was
reconstructed directly in section 2. An optional citation clarification
would improve attribution precision, but no mathematical repair is needed
for this point.

## Reproduction, resources and remaining limits

From the repository root, the exact commands are:

```sh
.venv/bin/python -u problems/2021-B4/reviews/newton-review-2-supervise.py newton-review-2-independent.py newton-review-2-independent-run 120
.venv/bin/python -u problems/2021-B4/reviews/newton-review-2-supervise.py newton-review-2-compare.py newton-review-2-compare-run 120
```

The dedicated children were PID 28394 (5.247 seconds) and PID 28596
(5.410 seconds), each with a 120-second explicit timeout, incremental
checkpoints, and exit code 0. Neither timed out. PID/job metadata and
complete output are saved in the adjacent R2 files. No process was
killed and no computation was left running. Python 3.12.14; main
verification uses only its standard library. Pypdf 6.10.0 was used for
source extraction. No dependencies were installed.

Primary source hashes, the official statement hash, requested settings,
telemetry and artifact hashes are in `newton-review-2-manifest.json`.
The authoritative account-wide weekly reading was 7% used, window 10080
minutes, reset Unix 1792745187, at both the opening and closing compute
checks. No new weekly window or separately billed API was used. Only
R2-owned `newton-review-2*` files were written. No candidate, shared log,
integration file, Git commit, push, or promotion was made.

This report accepts the packet's bounded partial conclusions and the
complete J=17 family certificate. It does not convert the 1164 surviving
necessary binary patterns into rational polynomials, and it does not
settle degree 20 or the contest's full open question.
