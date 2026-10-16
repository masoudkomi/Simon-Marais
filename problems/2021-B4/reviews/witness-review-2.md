# Independent adversarial review R2: rational-witness degree-p+1 restriction

Completed initial blind report: 2026-10-16, 11:01:44 UTC.

**R2 verdict: no blocking mathematical gap found in the frozen partial lemma
or its stated finite filter.** Two editorial clarifications are listed below.
This is one reviewer's assessment, not a promotion. The author's status remains
**candidate proof - unverified** until the coordinator applies the protocol.
The result supplies a necessary condition, not a new complete degree or the
answer to 2021 B4(b).

## Independence and scope

I did not construct the candidate, communicate with another reviewer, or open
another review, a source-audit note, or a shared research/issue log before
completing this report. The permitted `references.md` locator was opened in
full; that file also contains embedded literature-status prose. None of its
separate linked audit notes was opened. I used the candidate, its associated
script and output, the official statement, and the primary PDFs listed below.
In particular, I did not inspect R1's report or conclusions.

The coordinator reports the launch request as `gpt-6.1-sol` / `max`.
No verified effective-model or reasoning-setting readback is available to this
reviewer; requested and effective settings are not being equated.

Only files beginning `problems/2021-B4/reviews/witness-review-2` were created.
No author file, shared log, central manifest, Git index, commit, or remote was
changed. No subagent or separately billed API was used. Authoritative account
telemetry returned **5% total weekly used**, with a 10080-minute window, during
the audit. This is total usage, not a percentage of the remaining allowance.
The final checkpoint returned **6% total weekly used** in the same window.

## Frozen inputs and primary sources

SHA-256 hashes were checked from the actual local files:

| Input | SHA-256 |
|---|---|
| `notes/rational-witness-p-plus-one-v1.md` | `e9534a7759c68ed4388a3f1ff03857a14cf61c010b893527e1ddd83906fb72e6` |
| `computations/rational_witness_p_plus_one.py` | `bd3bb2cda41e769aa7ccf42c5489a64be5200c08144e59575a40ebd56f40de31` |
| `computations/rational-witness-p-plus-one.jsonl` | `ff68846a021c2216fa56d29b77a53a54335b0011b955d52389835214d26b71aa` |
| `statement.md` | `5cd9750a2458191370590120fb4ae7d547740784eb1de38ee9e2e7890a2fabed` |
| `.cache/official/2021-paper_b.pdf` | `2d507d593500f762e90b041d03a451e884ea33c8769f9a2132427e14d8f926d1` |
| CLO, `.cache/literature/2021/cited-66c5af6a0f0239f5.pdf` | `d818747102d32060f43ae5f015f27065aadf38699b272a2367749db8b33fedbf` |
| Draisma-de Jong newsletter PDF | `9babd9ea728de626f8921a4086f6170039537c7305ac5b500f6ba0edda942ad0` |
| Massri v6 PDF | `8e5dec6d9d3ca1cb6becd7fa7e3d4c6ef18927cff9521c5f4eb9a1c1b567952f` |

The first four relative paths in this table are relative to
`problems/2021-B4/`; cache paths are relative to the repository root.

Primary locators, checked 2026-10-16:

- [Official Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf),
  page 2, B4. Its exact hypothesis has rational coefficients and a rational
  common root for each derivative order 1 through d-1; the witness may depend
  on the order. The open part asks which integer degrees d>=2 force a scalar
  times a rational linear form to the d-th power. I did not prove or
  reproduce preliminary part (a).
- [Castryck-Laterveer-Ounaies, arXiv:1208.5404](https://arxiv.org/abs/1208.5404),
  cached 23-page PDF: definition and scope on page 4; affine invariance on
  page 6; multiplicity restriction on pages 7-8; valuation setup on pages
  10-11; degree-p+1 normalization and equations (7), (9), (10) on pages
  12-14. Its Proposition 19 has the stronger all-roots-rational hypothesis
  and is not used here.
- [Draisma-de Jong, EMS Newsletter 80](https://www.ems-ph.org/journals/newsletter/pdf/2011-06-80.pdf):
  Proposition 6 is on **printed page 31**, with its proof on **printed page
  32** (PDF pages 33-34). It concerns the complete selected witness set,
  rather than the full root set, and credits Draisma and Knopper.
- [Massri, arXiv:1806.09561v6](https://arxiv.org/abs/1806.09561v6),
  Remark 7.4 on PDF page 12 reports the count 6680. This supplies a numerical
  cross-check only. Its later resultant claim is not an input to this review.

Relevant complete pages were read by `pypdf` text extraction. The source
statements and formulas, rather than a secondary summary, were checked.

## Reconstruction of every substantive step

Let P in Q[x] have degree d=p+1 for an odd prime p, satisfy the exact contest
witness hypothesis, and fail to be a scalar times a d-th power of a linear
polynomial. Thus the complex nontrivial Casas-Alvero inputs apply; the
contest's rational witnesses imply their weaker complex witness hypothesis.
No assertion that all roots are rational enters this implication.
A complex pure power with rational coefficients has its unique root equal
to minus the x^(d-1) coefficient divided by d times the leading coefficient,
so that root is rational and the contest's stated rational conclusion holds.
Thus there is no extra class of complex pure powers omitted by this step.

### 1. Rational affine normalization and valuation integrality

Take a rational shared root r of P and P', and the rational shared root c of
P and P^(d-1). The latter is the uniquely determined center of mass. The
published simplicity result makes c different from r. If A is the leading
coefficient of P, the final normalization is explicitly

    F(x) = P(r+(c-r)x) / (A(c-r)^d).

It is monic and rational, sends r to 0 and c to 1, and preserves every common
root equation and rationality of the witnesses. The chain rule supplies the
nonzero derivative scaling factor. The center condition gives coefficient
-d at x^(d-1), and the double root at 0 removes the linear and constant terms.

The following reconstruction verifies that a potentially algebraic
intermediate scaling in the published normalization causes no rationality
gap. Work in a splitting field over Q_p, with an extension of v_p. After
translation by r, divide roots temporarily by a nonzero root u of minimal
valuation, and make the polynomial monic. Now all roots have valuation >=0
and some root has valuation 0. Write its coefficients as binom(d,j)b_j,
with its linear and constant terms zero. Its center -b_1 is a root, hence
v_p(b_1)>=0. For

    B_j(x) = (j!/d!) F^(d-j)(x)
           = sum_(k=0)^j binom(j,k) a_k x^(j-k),

and the analogous expression before the final scaling, the common-root
equations inductively give v_p(b_j)>=0: the equation isolates b_j, and all
earlier coefficients and the selected root are integral. For 2<=j<=p-1,
v_p(binom(p+1,j))=1, since the falling numerator has exactly one factor p
and j! has none. At a unit root, the original polynomial equation therefore
forces b_1 to be a unit. Thus the translated center c-r has the same
valuation as u. Dividing by c-r, instead of u, still makes all roots and all
a_j integral, and it gives a_1=-1. The net affine change is exactly the
rational one displayed above. Consequently a_j in Q with v_p(a_j)>=0,
which is precisely a_j in Z_(p).

It follows that

    F mod p = x^(d-1)(x-1).

Monic division by x-1 gives an integral quotient with reduction x^(d-1).
Every nonzero root of that quotient has strictly positive valuation: a
negative valuation makes the leading term uniquely smallest, and valuation
0 makes the leading term a unit with every other term divisible by p.
Also the quotient's value at 1 is a unit, so F'(1) is nonzero and 1 is
simple. This independently checks the exact valuation assertion used by the
candidate, without assuming integral valuations for algebraic roots.
Rational roots other than 1 have integer valuation and hence belong to
p Z_(p); zero belongs there as well.

### 2. Multiplicity, residual degree and monic division

The multiplicity m of 0 is at least 2. CLO Proposition 10 applies to
nontrivial complex Casas-Alvero polynomials and excludes every multiplicity
>=d-2, so m<=d-3. Its proof covers the two alternatives for whether the
center coincides with this multiple root; its resulting pure-power case is
excluded by our starting assumption. There is no added real-root or
all-roots-rational hypothesis.

Since 1 is simple,

    F=x^m(x-1)q,       deg(q)=D=d-m-1>=2.

The monic factors x and x-1 can be divided out over Z_(p). Cancelling their
reductions in the integral domain F_p[x] yields q mod p=x^D. Comparing
constant coefficients after division by x^m gives q(0)=-c_m, where c_m is
the first nonzero coefficient of F. In particular c_m is nonzero and has
valuation at least 1. All these reductions are legitimate over Z_(p).

### 3. Eisenstein obstruction and exact witness-set contradiction

If v_p(c_m)=1, q is monic, all its lower coefficients are divisible by p,
and its constant coefficient is divisible by p but not p^2. With D>=2 these
are the Eisenstein conditions over Q_p. For a direct check independent of
the irreducibility theorem, a putative t in Q_p with q(t)=0 is impossible:

- If v_p(t)<0, the leading term has strictly smaller valuation than every
  lower term.
- If v_p(t)=0, the leading term is a unit and every lower term is divisible
  by p.
- If v_p(t)>=1, the constant term has valuation 1, whereas each nonconstant
  lower term has valuation >=2 and t^D has valuation >=D>=2.

There is a unique term of least valuation in each case, preventing the sum
from vanishing. The case t=0 is excluded by q(0) nonzero. Thus q has no Q_p
root and no rational root. The rational roots of F are exactly 0 and 1.

For every derivative, a rational contest witness must then lie in {0,1}.
The witness for the first derivative is necessarily 0, since 1 is simple;
the highest derivative's witness is 1. Therefore the selected witness set
has cardinality exactly two, not merely at most two. Proposition 6 prohibits
that exact situation even if q has additional irrational or nonreal roots.
Its proof also independently reconstructs: normalize the two witnesses to
0 and 1, begin with the constant positive top derivative of a monic
polynomial, and successively integrate with the prescribed zero at one
endpoint. Each derivative has a fixed strict sign on (0,1); the final
polynomial is strictly monotone and cannot vanish at both endpoints. This
uses one endpoint witness for every derivative and imposes no restriction
on other roots.

The contradiction proves the partial assertion v_p(c_m)>=2. The candidate
has not substituted a theorem about the number of all roots for this
witness-set theorem.

### 4. Endpoints and attempted failure cases

For p=3, d=4, m>=2 and m<=d-3=1 already conflict, so the conditional lemma
is vacuous. There is no attempt to form a negative-degree residual factor.
For larger odd primes, any hypothetical example has D>=2 as required.
p=2 is outside the candidate's stated odd-prime scope. No claim for all
integer d>=2 is inferred from this restriction.

The degree bound is essential: a degree-one Eisenstein polynomial x+p has
the rational root -p. The source's exclusion of m=d-2 rules out precisely
that residual-degree-one escape. Likewise a pure power or a shared multiple
center cannot be inserted into the argument: both are already excluded by
the nontrivial hypothesis and the degree-p+1 normalization. A rational
witness with a denominator divisible by p cannot bypass the filter, since
the normalized roots have nonnegative valuations. No counterexample or
degenerate case invalidating the claimed implication was found.

## Independent reconstruction of the degree-20 finite filter

The derivative notation should be made explicit. For j=2,...,18 use the
monic normalized derivative B_j=(j!/20!)F^(20-j), so

    B_j(x)=sum_(k=0)^j binom(j,k)a_k x^(j-k),
    a_0=1, a_1=-1.

Every B_j has p-integral coefficients. A selected witness reducing to 0
gives a_j=0 mod 19. A selected center 1 gives

    a_j = -(1-j+sum_(k=2)^(j-1) binom(j,k)a_k) mod 19.

The polynomial equation F(1)=0, divided by 19, gives exactly

    -1+sum_(j=2)^18 (binom(20,j)/19)a_j = 0 mod 19.

These are necessary implications only. A derivative without an actual
center witness may still vanish at 1 modulo 19, so the residue condition
must not be treated as sufficient to identify its actual witness set.
Different binary selections may also produce the same residue vector; the
reported count is of binary selections, not distinct polynomials.

The new script `witness-review-2-filter.py` does not import or execute the
author's script. It instead starts from B_1=x-1 and constructs each
polynomial using B_j'=j B_(j-1), integrating coefficient vectors over F_19.
All divisors 1,...,18 are invertible. It chooses the integration constant
to make B_j(0)=0 or B_j(1)=0, then tests the displayed final congruence.
It visits every integer mask 0,...,131071, with bit j-2 selecting the center
for B_j. This traversal order differs from the author's recursive order.

Exact run from the repository root:

```text
.venv/bin/python problems/2021-B4/reviews/witness-review-2-filter.py > problems/2021-B4/reviews/witness-review-2-filter.jsonl
```

Python 3.12.14, standard library only. The script launched a dedicated child
PID **17567**, with an explicit **30-second timeout** and flushed progress
every 16384 masks. The child completed with exit code **0** in
**1.210941833 seconds** and was reaped by `child.wait()`. The shell session
also completed with exit code 0. A redundant `ps -p 17567` inspection was
denied by the sandbox (`zsh:1: operation not permitted: ps`); the successful
bounded child wait already establishes completion, so no cleanup or global
process kill was needed.

The independent histogram of a_18 residues among accepted masks is:

| Residue | Count | Residue | Count | Residue | Count |
|---:|---:|---:|---:|---:|---:|
| 0 | 3637 | 7 | 146 | 14 | 163 |
| 1 | 182 | 8 | 187 | 15 | 199 |
| 2 | 160 | 9 | 134 | 16 | 176 |
| 3 | 171 | 10 | 164 | 17 | 162 |
| 4 | 142 | 11 | 175 | 18 | 136 |
| 5 | 190 | 12 | 198 | | |
| 6 | 179 | 13 | 179 | | |

All **19 entries** match the frozen author's output. The counts are
**6680** accepted selections, **3043** with nonzero a_18, and **3637** with
zero a_18. For nonzero a_18, c_2=190a_18 has valuation 1 and m=2, so the
partial lemma excludes those selections under the rational-witness
hypothesis. The 3637 other selections have merely survived necessary
congruences. This is finite computational evidence, with no lifting,
existence, sufficiency, or general degree-20 conclusion.

Supplementary reproducibility hashes:

- Independent script SHA-256:
  `c5f8cf23bef153d1eb8f839a5b719b865184bb88fd324ced329cf2051d32d307`.
- Independent JSONL SHA-256:
  `2cba75925e88d47d6071c865f824bfd5d2f0f04f6b8090e6a86beedd967a6c8d`.
- SHA-256 of accepted ASCII records `mask:a18\n`, in increasing mask order:
  `a50958cec7910ce28e51381be52a075e1732844323eb675c7793d77f3f3d38bd`.

The author's and reviewer's complete histogram dictionaries were compared
by exact Python equality, and their totals and the two split counts were
asserted. No author's code was executed to obtain the independent result.

## R2 issue record and limits

| ID | Severity | Observation | Required treatment |
|---|---|---|---|
| W2-E1 | Editorial | The candidate places newsletter Proposition 6 on printed pp. 32-33. Its statement is on p. 31 and proof on p. 32, PDF pp. 33-34. | Correct the locator when the author edits the note. The theorem being used is correct. |
| W2-E2 | Editorial clarity | `H_(20-j)` is not explicitly defined. The standard Hasse derivative is binom(20,j) B_j; that scalar has valuation 1, so directly reducing the standard Hasse derivative would lose the a_j condition. | Define the monic B_j=(j!/20!)F^(20-j) before the filter, or explicitly say the Hasse derivative is divided by binom(20,j). The candidate's phrase "normalized Hasse derivative" and its recursion are mathematically consistent with this intended normalization. |

No substantive repair is requested by R2. The algebraic intermediate scaling,
the precise selected-witness theorem, the residual degree, the non-integral
algebraic root valuations, and the small prime endpoint have all been
audited above. The optional notation/locator edits do not change the proof.
If an author changes the mathematical scope or inference, the affected
argument requires re-review rather than relying on this frozen assessment.

This review does not audit Massri's resultant certificate, resolve the
general Casas-Alvero conjecture, classify rational-witness degrees, or claim
novelty. Published ingredients remain attributed. Only the coordinator can
reconcile both independent reviews and decide any status promotion.
