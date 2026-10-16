# Independent adversarial review R1: rational-witness partial lemma

Review completed 2026-10-16. This is an initial blind report on
`notes/rational-witness-p-plus-one-v1.md`, frozen SHA-256
`e9534a7759c68ed4388a3f1ff03857a14cf61c010b893527e1ddd83906fb72e6`.
The candidate remains **candidate proof - unverified** unless the coordinator
later completes the required independent-review process.

**R1 verdict:** I found no substantive mathematical objection to the stated
partial necessary condition or its degree-20 filter. I reconstructed the full
argument and independently reproduced every reported count and the full
19-entry residue histogram. Two nonblocking presentation corrections are
listed below. This is not a complete solution of 2021 B4(b), a novelty
assessment, or validation of any general Casas-Alvero proof claim.

## Independence and scope

I did not construct the candidate. Before completing this report, I read no
other review, source-audit objection, shared research note, or issue log. The
permitted `references.md` was consulted as a source locator; its descriptions
were not treated as evidence for a theorem. I read the author's computation
only after writing and successfully running my separate implementation.
No preliminary part (a) argument was investigated or reproduced. No other
year or contest problem was investigated. No author or shared files were
edited; no commit, push, or subagent was used.

Requested launch settings were `gpt-6.1-sol` / `max`, according to the
coordinator's assignment. There is no verified effective-setting readback in
this review. Authoritative account-wide weekly telemetry was 5% total used
at 2026-10-16 10:47:36 UTC, with a 10080-minute window; the 90% stopping
threshold was not approached. No separately billed API or installation was
used.

## Official hypothesis and published inputs

The [official 2021 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf),
page 2, specifies a degree-d polynomial with rational coefficients and, for
each integer k from 1 through d-1, a rational number r_k which is a zero of
both the polynomial and its kth ordinary derivative. The r_k may depend on
k. B4(b) asks which d >= 2 force the stated pure-power conclusion. In
particular, this hypothesis does not say that every zero is rational.

The cached primary PDFs, hashes, exact locations and commands are recorded
in `witness-review-1-manifest.json`. I checked the relevant complete pages,
including rendered mathematical formulas, rather than relying on snippets.

| Input | Exact primary-source check | Applicability |
|---|---|---|
| Castryck-Laterveer-Ounaies (CLO), [arXiv:1208.5404](https://arxiv.org/abs/1208.5404), Definition 1, Lemma 6 | A CA-polynomial over C excludes a pure power and has common roots with every nonconstant derivative; affine equivalence preserves these conditions. | A hypothetical nontrivial contest polynomial is such a CA-polynomial after making it monic. In characteristic zero, ordinary and Hasse derivatives differ by nonzero scalars. |
| CLO, Proposition 10, PDF/printed pp. 7-8 | A CA-polynomial cannot have a root of multiplicity at least d-2. I checked the two-case proof and its final common-root equations. | With the chosen multiple root moved to zero, 2 <= m <= d-3. This supplies the essential residual-degree bound D >= 2. |
| CLO, Section 3.4, equations (9)-(10), PDF/printed p. 13; Lemma 17, pp. 13-14 | The displayed degree-p+1 normalization has p-integral normalized coefficients, center at 1, and all other roots of positive valuation. The center is simple. The proof establishes that its scaling factor is a p-adic unit after initial minimum-root scaling. | The rationality of the final change of variable requires the reconstruction below; the intermediate minimum-root scaling need not be rational. |
| Draisma-de Jong, [EMS Newsletter 80 (2011)](https://www.ems-ph.org/journals/newsletter/pdf/2011-06-80.pdf), Proposition 6 and proof, **printed pp. 31-32**, PDF pp. 33-34 | Chosen roots covering every derivative cannot form a two-element set; a singleton forces a pure power. Full proof checked; no all-roots or real-roots hypothesis. Attribution there is to Draisma and Knopper. | Applies to rational derivative witnesses. CLO Section 1.2 and Proposition 7 confirm the covering-set meaning of type. |
| Massri, [arXiv:1806.09561v6](https://arxiv.org/abs/1806.09561v6), Remark 7.4, PDF p. 12 | It reports 6680 surviving binary cases out of 2^17 in degree 20. I also checked the preceding normalization/filter context on p. 11. | Used only as an attributed numerical cross-check. No later resultant computation or three-recycled-root theorem is assumed here. |

The newsletter's separate degree-family assertion is not an input. Likewise,
CLO Proposition 19, which assumes that all roots are rational, is not being
extended or used to fill a gap here.

## Full reconstruction

Let P in Q[x] be a hypothetical nontrivial contest polynomial of degree
d=p+1, p an odd prime, with leading coefficient A. Choose a rational common
root r of P and P', and let c be the unique root of P^(d-1). The contest
hypothesis gives P(c)=0, and c is rational. CLO Lemma 17 gives P'(c) != 0,
so c != r. Therefore

    F(x) = P(r + (c-r)x) / (A(c-r)^d)

is monic with rational coefficients, preserves rational common witnesses,
has a multiple root at 0, and has center 1. In particular its coefficient of
x^(d-1) is -d, and its constant and linear coefficients are zero.

For completeness, the rational final normalization really does inherit the
p-integrality from CLO. Translate r to zero, make the polynomial monic,
and temporarily divide its variable by a nonzero root t of minimum p-adic
valuation. Such a root exists because the polynomial is not a pure power.
The resulting monic polynomial h has all roots of nonnegative valuation
and at least one unit root. Write its normalized coefficients as b_j, so

    (j!/d!) h^(d-j)(x) = sum_(k=0)^j binom(j,k) b_k x^(j-k).

Its center is u=(c-r)/t=-b_1, hence b_1 is p-integral. For j=2,...,d-2,
plug a common root of h and h^(d-j) into this monic derivative. Induction
then makes every b_j p-integral. For 2 <= j <= p-1,
v_p(binom(p+1,j))=1: the numerator has exactly one factor p, and j! has
none. At a unit root of h, if b_1 were not a unit then the leading term
would be the unique term of minimum valuation. This is impossible in a
zero sum. Thus u is a unit. Dividing the variable further by u preserves
all coefficient-integrality conclusions and has combined scale
t*u=c-r, which is rational. This final polynomial is exactly F above.

Consequently

    F(x) = x^d - d*x^(d-1)
           + sum_(j=2)^(d-2) binom(d,j) a_j x^(d-j),
    a_j in Z_(p),          F mod p = x^(d-1)(x-1).

Division by x-1 in Z_(p)[x] gives a monic G with G mod p=x^(d-1).
Every nonzero root of G has positive valuation: at negative valuation
the leading term dominates, and at zero valuation it again dominates
because every lower coefficient has positive valuation. Also G(1) is a
unit, so 1 is simple. Thus every rational root of F other than 1 has
integer positive valuation, or is zero; it lies in p Z_(p). This argument
allows irrational and nonreal zeros, with possibly fractional positive
valuations, throughout.

Let m be the multiplicity of 0 and c_m its first nonzero coefficient.
CLO Proposition 10 gives m <= d-3, so

    F = x^m (x-1) Q,        D=deg(Q)=d-m-1 >= 2.

Monic division keeps Q in Z_(p)[x], Q mod p=x^D, and Q(0)=-c_m. The
displayed coefficient shape already gives v_p(c_m)>=1. If equality held,
Q would satisfy the usual p-Eisenstein conditions over Q_p and would be
irreducible of degree at least 2, hence have no Q_p or rational root.

There is also a direct check of the precise root consequence, avoiding
any reliance on an unstated version of Eisenstein. For a proposed root
z in Q_p, a negative or zero valuation makes z^D the unique lowest-valuation
term. If v_p(z)>=1, the constant term has valuation 1 and all other terms
have valuation at least 2 because D>=2. Each case is impossible. Therefore
the only rational zeros of F would be 0 and 1.

All contest witnesses would then be selected from {0,1}. The first
derivative must use 0 because 1 is simple, and the (d-1)st derivative
must use 1 because it is linear with that unique zero. The chosen set
therefore has **exactly** two elements, contradicting Draisma-Knopper's
result. This proves the claimed necessary condition v_p(c_m)>=2.

The published obstruction reconstructs as follows. Normalize the two
selected roots to 0 and 1 and make the polynomial monic. Integration
downwards from its constant highest derivative, with the selected
endpoint integration constants, gives each derivative one strict sign
in (0,1). The polynomial becomes strictly monotone, contradicting its
two endpoint zeros.

## Edge cases and attempted failure points

- p=3 gives d=4. Then m>=2 conflicts already with Proposition 10's
  m<=1. The conditional lemma is vacuous there; its stated odd-prime range
  is consistent. p=2 is outside the candidate's stated range.
- A linear residual factor would have a rational root even if Eisenstein.
  The proof uses D>=2 correctly; omitting the multiplicity bound would
  invalidate that step.
- Rationality of the witnesses is essential to restricting the selected
  roots to the rational zeros 0 and 1. The proof does not presume the other
  zeros rational, nor round their valuations up to 1.
- Zero has infinite valuation and causes no exception. The center's
  simplicity prevents its coincidence with the chosen multiple root.
- When a_18 is nonzero modulo 19, c_2=190*a_18 is nonzero with valuation
  exactly 1 and m=2, because the lower two coefficients vanish. When
  a_18 is zero modulo 19, m need not increase: c_2 may still be nonzero
  of valuation at least 2. The candidate makes no contrary inference.
- The counts are counts of binary selections. Different selections may
  yield the same coefficient residues. No uniqueness or lifting claim
  follows from the enumeration.

## Independent finite computation

For j=2,...,18 define the **monic normalized derivative**

    P_j(x) = (j!/20!) F^(20-j)(x)
           = sum_(k=0)^j binom(j,k) a_k x^(j-k).

Its coefficients are 19-integral. A non-center rational witness reduces to
0, so P_j evaluated there gives a_j=0 modulo 19. A selected center gives
P_j(1)=0, yielding exactly the stated residue recursion. Finally F(1)=0
and 1-20=-19 give the candidate's divided congruence. These are necessary
conditions for the exact official rational-witness hypothesis.

My separate standard-library implementation uses exact integer Appell
coefficients on a binary tree, without reducing the recursion modulo 19.
It checks the resulting exact integer F(1) modulo 19^2. Polynomial
dependence of the coefficients on the selected 0/1 residues makes this
equivalent to the required residue calculation. It completed before I
read the author's script, with an explicit 30-second subprocess timeout,
child PID 16342, exit code 0, and recorded elapsed time about 0.377 seconds.

| Quantity | Independently reproduced |
|---|---:|
| Binary selections visited | 131072 |
| Passing the divided F(1) congruence | 6680 |
| Passing, with a_18 nonzero modulo 19 | 3043 |
| Passing, with a_18 zero modulo 19 | 3637 |

The full a_18 histogram equals the author's saved histogram in all 19
residues. The independent output also records a canonical SHA-256 of the
sorted `(mask,a_18 residue)` survivor pairs and sample selections. The
script and output are `witness-review-1-filter.py` and
`witness-review-1-filter.jsonl`.

The recurrence and root obstruction establish only a necessary filter.
The run is finite computational evidence for its reported enumeration;
it is not proof of an unrestricted classification, existence of lifts,
or a degree-20 solution.

## Review issue log

| ID | Severity | Status | Finding / requested author action |
|---|---|---|---|
| R1W-01 | Minor citation correction | Open, nonblocking | The candidate says Proposition 6 is on printed pp. 32-33. In the frozen full newsletter the statement is on printed p. 31 and its proof on printed p. 32, corresponding to PDF pp. 33-34. Correct the locator. |
| R1W-02 | Minor notation clarification | Open, nonblocking | Define the normalized derivative explicitly as `(j!/d!) F^(d-j)`, or equivalently the Hasse derivative divided by `binom(d,j)`. Reduction of an unnormalized Hasse derivative alone would not imply a_j=0, because this binomial coefficient is divisible by p. The intended monic normalization is valid and gives the claimed recursion. |

No substantive objections remain in this initial R1 audit. I recommend the
partial mathematical statement for coordinator consideration after the
required second independent audit. Only the author should repair the two
presentation points, and only the coordinator may promote the status.
