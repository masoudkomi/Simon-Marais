# Newton restrictions on rational recycled witnesses

2026-10-16. **Candidate proof - unverified.** No result in this note has yet
received two independent adversarial audits. No full degree or classification
of the contest question is claimed. Computations below are finite exact
evidence supporting the stated candidate reductions, not proof of an
unrestricted rational-witness classification. No novelty claim is made.

The earlier frozen `rational-witness-p-plus-one-v1.md` and all reviewer files
were left untouched. Version 1.1 of that note contains only the two requested
presentation repairs. The second blind review was not read by this author.

## Published inputs and conventions

Use only the open rational-witness B4(b) question. Write H_k=f^(k)/k!, let
v=v_p with v(p)=1, and use the standard extension to an algebraic closure
of Q_p when discussing nonrational roots. Multiplicities always count in
Newton-polygon root counts; they do not count when discussing the number
of distinct recycled witnesses.

The normalization and its source-by-source hypothesis check are in
`rational-witness-p-plus-one-v1.1.md`. The relevant published inputs are:

- Castryck-Laterveer-Ounaïes (CLO),
  [arXiv:1208.5404](https://arxiv.org/abs/1208.5404), Math. Comp. 83 (2014),
  3017-3037, §3.4 equations (9)-(10) and Lemma 17: for d=p+1 a nontrivial
  counterexample can be normalized with a rational double root at 0 and
  its rational center at 1, and in that normalization all other nonzero
  roots have positive p-adic valuation and 1 is simple. The affine change
  is rational under the contest hypothesis. We do not assume that every
  other root is rational.
- Draisma-Knopper's two-recycled-root obstruction, recorded in Draisma-de
  Jong, [EMS Newsletter 80](https://www.ems-ph.org/journals/newsletter/pdf/2011-06-80.pdf),
  Proposition 6, printed pp. 31-32 (PDF pages 33-34, one-based), and CLO
  Proposition 7. A nontrivial CA polynomial cannot realize all derivative
  conditions using only two distinct shared roots. This is stronger than
  a lower bound on the total number of complex roots.
- The classical Newton-polygon root-count theorem: a segment of slope -s
  and horizontal width L accounts for L roots of valuation s, counted
  with multiplicity in the algebraic closure. A primary author-posted
  statement is Poonen,
  [*Lectures on rational points on curves*](https://math.mit.edu/~poonen/papers/curves.pdf),
  §4.2.1, Theorem 4.2.3 (current PDF page 68 one-based; printed p. 62).
  Here the polynomial is over Q_p, the valuation is nonarchimedean, and
  we pass to its algebraic closure for this theorem. A root in Q_p has
  integral valuation, so a rational shared witness cannot belong to a
  cluster of nonintegral valuation.

No Massri three-recycled-root theorem is assumed. Its previously noted
computational claim does not enter any argument here.

In the normalization, put d=p+1, p>=5, and

    f(x)=x^d-d*x^(d-1)+sum_(j=2)^(d-2) binom(d,j)*a_j*x^(d-j),
    a_j in Z_(p),  f(0)=f'(0)=0,  f(1)=0,
    a_0=1, a_1=-1.

Define the degree-j normalized derivative explicitly by

    D_j(x)=(j!/d!)*f^(d-j)(x)
          =H_(d-j)(f)(x)/binom(d,j)
          =sum_(k=0)^j binom(j,k)*a_k*x^(j-k).

It has p-integral coefficients; all reductions of D_j use this expression
before reduction, never division by a nonunit in F_p. Write c_k for the
ordinary coefficient of x^k, let m>=2 be the multiplicity at 0, and define

    J=max{j in {2,...,d-2}: v(a_j)=0},    h=d-J.

J exists: the equality f(1)=0, divided by p, would reduce to -1=0 mod p
if every a_j were divisible by p. This uses v(binom(d,j))=1 for the indicated
range. Thus c_h has valuation 1, every c_k with 2<=k<h has valuation >=2
or is zero, and every middle coefficient has valuation >=1.

## 1. The long fractional-valuation edge

**Candidate proof - unverified.** If J>=d/2, then the Newton polygon has the
edge

    (h,1) -> (d-1,0),   width J-1,   root valuation 1/(J-1).

Indeed its supporting line is

    L(k)=(d-1-k)/(J-1).

For h<k<d-1, L(k)<1 while v(c_k)>=1. For 2<=k<h,

    L(k)<=L(2)=(d-3)/(J-1)<2,

where the last strict inequality follows from J>=d/2 and even d. The
coefficients c_0,c_1 vanish. At k=d, L(d)<0=v(c_d). Thus all other nonzero
coefficient points lie strictly above this line, establishing the edge.

Since d>=6 and J>=d/2, J-1>=2. These J-1 roots have nonintegral valuation
and cannot be rational witnesses. The remaining h+1 roots, counted with
multiplicity, include m copies of 0 and one copy of 1. Therefore

    number of distinct rational roots of f <= h-m+2.

At least three distinct rational recycled roots are required by the contest
hypothesis and the published two-recycled-root obstruction. Consequently

    m<=h-1=d-J-1.                                      (N1)

This counts distinct **rational** roots only after removing the known
nonintegral-valuation cluster. It does not bound the full complex root set
by three. In particular, for d=20 it excludes J=18 outright, since m>=2
whereas h-1=1. For J=17 it forces m=2.

The hypothesis J>=d/2 is essential to this particular supporting-line
argument. No assertion of the same edge is made for smaller J without an
additional valuation check.

## 2. A root on a width-one edge cannot be a low derivative witness

**Candidate proof - unverified.** Let P=sum b_j*x^j be over Q_p and let
u in Q_p be nonzero. Suppose P(u)=0 and the only terms of minimum valuation
among b_j*u^j are those with exponents i and i+1. If 0<=i<p, then

    H_k(P)(u)!=0 for every 1<=k<=i+1.                  (N2)

To prove this, divide all terms by the nonzero term b_(i+1)*u^(i+1).
The reduction of the i-th term is -1 because the sum is zero; every other
term except the (i+1)-th reduces to zero. Multiplying H_k(P)(u) by u^k
before dividing by the same term, its reduction is

    binom(i+1,k)-binom(i,k)=binom(i,k-1).

We take binom(i,i+1)=0. This last binomial is a p-unit for 1<=k<=i+1
because i<p, so H_k(P)(u) cannot vanish. Integer binomial coefficients on
all other terms do not lower valuations. This proves (N2).

A width-one Newton edge with only its endpoints on the supporting line
has exactly the required two minimum terms for its associated root. This
lemma uses the unique-minimum terms after the binomial difference, rather
than assuming that a simple root of P cannot be a root of a higher derivative.

## 3. The degree-20 J=17 reduction

**Candidate proof - unverified.** Assume d=20, p=19 and J=17. Then h=3,
and (N1) forces m=2. The width-16 edge from (3,1) to (19,0) accounts for
16 roots of valuation 1/16, unavailable as rational witnesses. Besides
0 (twice) and 1, precisely one root remains, counted with multiplicity.

There must be another rational recycled root, so that remaining root is a
rational number u, nonzero, distinct from 1 and of positive integral
19-adic valuation. In particular, it is the only available rational root
besides 0 and 1; all derivative conditions can be realized using {0,1,u}.

The left Newton edge is (2,v(c_2))->(3,1), of width one and slope
1-v(c_2). Since J=17, v(c_2)>=2. All terms to its right are strictly above
its extended supporting line, and terms to its left vanish. By (N2), u
cannot witness H_1,H_2 or H_3. The root 0 cannot witness H_2 or H_3 because
m=2 and c_3 is nonzero. Hence

    H_2(f)(1)=H_3(f)(1)=0.                            (N3)

H_3(1)=0 also follows from a_17 being a unit and the rational-witness
equations; the new information is the forced H_2(1)=0.

### Exact finite family compatibility evidence

Choose the center whenever it is available as a witness. For j=2,...,18
record a center flag for D_j; otherwise its witness is 0 or u. Modulo 19,
noncenter witnesses reduce to 0. The binary recurrence is

    a_j=-(1-j+sum_(k=2)^(j-1) binom(j,k)*a_k) mod19  [center],
    a_j=0 mod19                                     [noncenter].

The divided equation f(1)/19=0 requires

    -1+sum_(j=2)^18 (binom(20,j)/19)*a_j=0 mod19.

The complete 2^17 calculation gives 6680 necessary binary patterns, with
1674 having J=17. Condition (N3) removes the 1601 J=17 patterns without
the H_2 center flag, leaving 73. Noncenter flags need not enforce that the
center fails, so this calculation deliberately keeps a superset of the
canonical possibilities. Every counterexample nevertheless has one of the
retained canonical patterns.

For each of the 73 patterns, assign every noncenter witness to 0 or an
indeterminate U. There are exactly 29928 such refinements. Work in Z[U]
and set a_0=1,a_1=-1. Define the remaining a_j recursively by

    a_j(U)=-sum_(k=0)^(j-1) binom(j,k)*a_k(U)*w_j^(j-k),
    w_j in {0,1,U},

using the center flags and the selected refinement. This is the exact
equation D_j(w_j)=0. The monic polynomial f_U is then fixed, since its
constant and linear coefficients are zero. A putative counterexample with
parameter u must satisfy

    P(U):=f_U(1)=0,    Q(U):=f_U(U)=0                  (N4)

at U=u. These are univariate integer polynomials. No rational-height
bound is imposed, and no restriction on the other roots of f_U is imposed.

For each of the 29928 refinements, the saved exact certificate records one
of the following:

1. P is a nonzero constant; or
2. a prime ell for which both integer polynomial degrees are retained and
   the reductions of P and Q have gcd 1 in F_ell[U].

The second certificate implies Res(P,Q) is a nonzero integer: its reduction
is the nonzero resultant of the coprime reductions, with degrees retained.
Consequently P,Q are coprime over Q and have no common complex root. This
explains why a validated finite certificate would handle every rational
value of U, rather than just the values in a finite search box.

The complete run resolved all 29928 refinements, with no unresolved case:

| Certificate | Number of refinements |
|---|---:|
| P is a nonzero constant | 73 |
| coprime modulo 101 | 28583 |
| coprime modulo 103 | 1213 |
| coprime modulo 107 | 55 |
| coprime modulo 109 | 4 |

This supports the **candidate exclusion of J=17 in degree 20** after the
theoretical reduction. Neither the finite certificate computation alone
nor this unreviewed note is a promoted result. Its completeness and its
connection to all rational-witness counterexamples need two fresh audits.

No Massri theorem, resultants from another paper or all-roots-rational
assumption was used. The calculation is related to the already claimed
three-recycled-root family; no novelty is asserted.

## 4. A further degree-20 J=16 obstruction

**Candidate proof - unverified.** If d=20,p=19,J=16, then

    H_2(f)(1)=0 or H_3(f)(1)=0.                       (N5)

Here h=4, and (N1) gives m=2 or m=3. The width-15 edge from (4,1) to
(19,0) accounts for 15 unavailable roots of valuation 1/15.

If m=3, there is one remaining positive-valuation root. A third rational
witness forces that root to be rational, and the left width-one edge from
(3,v(c_3)) to (4,1) prevents it from witnessing H_3 by (N2). The root 0
also cannot witness H_3, so H_3(1)=0.

Suppose m=2 and H_2(1)!=0. Its witness must be one of the remaining two
positive-valuation roots. If their valuations differed, each would have a
width-one edge with lower exponent 2 or 3, so neither could witness H_2
by (N2). Therefore they have the same valuation s. Since one is rational,
s is a positive integer. In particular v(c_2)=1+2s>=3.

After substituting x=19^s*T and dividing by 19^(1+4s), reduction modulo
19 keeps the low initial form

    F(T)=T^2*(A+B*T+C*T^2),    A*C!=0.

All terms of degree >4 are strictly higher in valuation. The coefficient
of T^3 may initially be zero. The shared H_2 root gives a nonzero residue
alpha satisfying F(alpha)=H_2(F)(alpha)=0, and hence

    2B+5C*alpha=0.

Thus B is nonzero, alpha=-2B/(5C), and the other nonzero root of F is
beta=-3B/(5C). They are distinct and nonzero modulo 19. At these two roots,

    H_3(F)(alpha)=-3B/5,   H_3(F)(beta)=-7B/5,

both nonzero modulo 19. Therefore neither small root can witness H_3.
The root 0 cannot do so either, since B is nonzero and thus c_3 is nonzero.
The only remaining rational witness is 1, establishing H_3(1)=0 and (N5).

This argument needs the units 2,3,5,7 in the residue field. It is stated
only for p=19; no unsupported extension to the exceptional primes is made.

The finite binary-pattern calculation finds 887 patterns with J=16. Of
these, 799 omit both center flags for H_2,H_3; (N5) leaves 88 patterns.
The script also checks the 18 possible nonzero B/C residues directly,
confirming the displayed initial-form identities over F_19. It does not
solve the remaining two-root compatibility problem.

## 5. Checkpoint, exact artifacts and remaining obstruction

With the candidate J=18 and J=17 exclusions and the J=16 disjunction,
1164 of the original 6680 necessary binary patterns remain. Their largest
J is 16. This is not a rational-point existence claim and does not solve
degree 20, let alone the original degree classification. In particular a
finite center-pattern filter is not a proof of the full contest statement.

The important failed shortcut was that the long-edge root count alone
permits three rational witnesses when J=17. One must use the derivative
obstruction (N2) and the exact family compatibility calculation. For J=16,
one low derivative can use the small quadratic cluster; its initial root
ratio is 2:3. That configuration is permitted locally, and no contradiction
is claimed unless the next derivative is also required to use that cluster.

The remaining J=16 families can have two positive rational witnesses. A
general bivariate elimination was not launched: its cost and certificate
size need a separate bounded plan. No large CAS job or infinite p-adic
lifting process was left running. Lower J values may require several
Newton edges, and the present supporting-line proof does not automatically
apply below J=10.

All paths below are relative to `problems/2021-B4/`:

- `computations/padic-rational-newton-patterns.py` and `.jsonl`: complete
  binary count, J histogram, all 73 J=17 retained masks and 1601 discarded
  masks. Child PID 18148, timeout 30 seconds, exit 0.
- `computations/padic-rational-j17-compatibility.py` and
  `computations/padic-rational-j17-run.jsonl`: complete integer-polynomial
  generation and modular coprimality run. Child PID 18372, timeout 90
  seconds, exit 0, completed in 2.182 seconds. Checkpoints every 1024 cases.
- `computations/padic-rational-j17-certificates.jsonl`: all 29928 records,
  7267887 bytes. SHA-256
  `9676e4885d670a23ea1fb1b0a151ec1f9a8cece8532a1dd43277450b3a7a7fc3`.
  Each record gives center/refinement masks, degrees, polynomial hash and
  a constant or prime/gcd/leading-residue certificate. Integer coefficients
  regenerate deterministically from the masks; their full stream hash is
  `47a5b912863c67f22fed42daaf92b72949a06164966037ac97e4ad8afd22395b`.
- `computations/padic-rational-j17-spotcheck.py` and `.jsonl`: the author
  reconstructed 12 records through direct ordinary Hasse coefficients,
  rather than the a_j recurrence, and obtained exact gcd 1 over Q with
  SymPy. This includes every record requiring prime 109. Hashes matched.
  This is an author spot-check, not an independent review or an audit of
  all 29928 records.
- `computations/padic-rational-j16-obstruction.py` and `.jsonl`: full
  J=16 flag count, all retained/discarded masks and all 18 initial-form
  residue checks. Explicit 30-second child timeout, exit 0.

Exact commands from repository root:

```sh
.venv/bin/python problems/2021-B4/computations/padic-rational-newton-patterns.py > problems/2021-B4/computations/padic-rational-newton-patterns.jsonl
.venv/bin/python problems/2021-B4/computations/padic-rational-j17-compatibility.py > problems/2021-B4/computations/padic-rational-j17-run.jsonl
.venv/bin/python problems/2021-B4/computations/padic-rational-j17-spotcheck.py > problems/2021-B4/computations/padic-rational-j17-spotcheck.jsonl
.venv/bin/python problems/2021-B4/computations/padic-rational-j16-obstruction.py > problems/2021-B4/computations/padic-rational-j16-obstruction.jsonl
```

Python 3.12.14; integer-only main checks, SymPy 1.14.0 only for the author's
selected exact gcd spot-check. No dependencies installed, billed APIs used,
subagents spawned, shared integration files edited, commits or pushes made.
Only the targeted child would be killed if a timeout occurred. All children
finished and no timeout was hidden. Requested model/effort remain
gpt-6.1-sol/max, without verified effective-setting readback.

The next gate is two independent adversarial reviewers, one reconstructing
the entire normalization-to-family argument. They should challenge the
root-count multiplicities, width-one derivative lemma, canonical center
flags, exhaustive refinement list, polynomial normalization, modular
degree-retention requirement, and the J=16 initial-form argument. This
author is a constructor and cannot serve as either reviewer.
