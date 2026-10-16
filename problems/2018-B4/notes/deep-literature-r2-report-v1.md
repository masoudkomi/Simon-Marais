# Deep literature investigation: the general 2018 enumeration

Checked 2026-10-16 UTC. Research worker R2; requested GPT-6.1-sol/max,
effective-setting readback unavailable. Only the general open portion is
in scope. The already known m=5 preliminary case was not researched or
reproduced. This packet adds historical and source analysis; it does not
claim a new enumeration theorem or change the accepted reproduction.

## Outcome

The exact literal count requested in 2018 had an explicit published
binomial-sum formula before the competition. A full author original gives
the arbitrary-weight result; an earlier primary exposition gives the exact
equal-weight specialization and attributes it to Howe (1988). The
contemporary competition report confirms the same two-row Kostka target.
I located no documented explanation for calling that formulation open.
The discrepancy is unresolved as history; it does not invalidate the
formula or authorize replacing the question by a stronger one.

## Exact match of domains and formulas

The [official statement](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-paper-b_1.pdf)
counts two-row arrays with mn columns, weakly increasing rows, strictly
increasing columns, and each of the m symbols occurring 2n times, for
positive integers m,n. This is precisely
`K((mn,mn),(2n,...,2n))`, with m content entries. The statement requests
the cardinality; it adds no product-form, sign-free, coefficient-positivity
or computational-complexity requirement.

Milena Hering and Benjamin J. Howard,
*The ring of evenly weighted points on the projective line*,
[Math. Z. 277 (2014), 691--708](https://doi.org/10.1007/s00209-013-1272-4),
has a full [author PDF](https://webhomes.maths.ed.ac.uk/~mhering/HH.pdf)
dated 2014-01-19, matching [arXiv:1211.3941v2](https://arxiv.org/abs/1211.3941).
The preprint title omits “projective”; that is a title/version difference,
not a different result. Proposition 3.2, PDF pp. 6--7, assumes a
positive integral weight vector w of length N with even total |w| and
counts shape `(|w|/2,|w|/2)` with content w. Its formula is

    sum_(J subset [N], |w_J|<|w|/2)
       (-1)^|J| binom(|w|/2-|w_J|+N-|J|-2, N-2).

Theorem 1.1(1) gives the corresponding Hilbert function in degree d by
replacing the difference of weights by `d*(|w|/2-|w_J|)`; the value is
zero when d|w| is odd. Both theorems are stated to work in all
characteristics and over the integers. Thus no characteristic-zero
representation-theory hypothesis is being silently imposed on the
combinatorial count.

Set `N=m,w=(2n,...,2n)` in Proposition 3.2, or equivalently
`w=(2,...,2),d=n` in Theorem 1.1. The shape, content and evenness condition
match exactly. Group subsets by cardinality j to obtain, for m>=2,

    sum_(0<=j<m/2) (-1)^j binom(m,j)
        * binom(n*(m-2*j)+m-j-2,m-2).

Here binomial coefficients with top below the nonnegative bottom mean
zero. The degenerate m=1 case is zero by strictness in each column and
is handled outside this notation. The m=2 case is one and agrees with
the sum. No investigation of the preliminary m=5 case is needed for this
match.

The source proof is also constructive enough to identify exactly what
has been reproduced: encode a tableau by the top-row multiplicities,
subtract bounded compositions of total one less from those of total
|w|/2 using the first/last minimum bijection in Proposition 3.2, and apply
inclusion-exclusion (Lemma 3.1). This is the published antecedent of the
repository's reflection/coefficient argument, not a novel method here.

Giorgio Ottaviani,
[Five Lectures on Projective Invariants](https://seminariomatematico.polito.it/rendiconti/71-1/119.pdf),
Rend. Semin. Mat. Univ. Politec. Torino 71 (2013), 119--194,
Theorem 40, printed p. 186/PDF p. 68, already states the equal-weight
binomial sum. In that notation use `d=m,k=2n`. When d is odd the theorem
requires k even; this is satisfied for every n here. Its degree is then
k/2 with respect to weight vector `(2,...,2)`, exactly the Hilbert-function
specialization above. For even d it uses `(1,...,1)`. Confusing that
grading convention could cause a factor-of-two error, but the displayed
formula with k=2n agrees with Hering--Howard.

Ottaviani attributes the formula to Roger Howe,
*The classical groups and invariants of binary forms*, Proc. Sympos. Pure
Math. 48 (1988), 133--166, Section 5.4.2.3. Hering--Howard also identify
their arbitrary-weight formula as an extension of this equal-weight
formula. Howe's original chapter was not obtained: normal AMS volume/DOI
requests failed or returned 403. Therefore 1988 is a corroborated
attribution through two inspected primary authors, not a claim that I
read the 1988 original. No inaccessible theorem is needed to establish
the pre-2018 availability, since the 2013 and 2014 texts suffice.

## What the contemporary competition record actually says

Anthony Henderson, [The 2018 Simon Marais Mathematics Competition](https://austms.org.au/wp-content/uploads/2025/02/Mar19-461.pdf),
Gazette of the Australian Mathematical Society 46(1), March 2019,
printed pp. 33--34, explicitly identifies B4's target at printed p. 34
as the Kostka number above. The full 84-page issue was cached; its B4
paragraph was extracted directly with pypdf. Web-search OCR renders the
shape incorrectly, so the original page's formula controls. The report
does not impose an additional quality condition on the requested formula
or identify an individual setter. Its authorship does not establish that
Henderson proposed B4.

The [official solution comments](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2018-solutions_1.pdf)
relate the enumeration to torus quotients of Grassmannians and A060854.
They do not change the rows, content, strictness or requirement to find a
formula. A060854 concerns related standard rectangular tableaux and is
not a substitute for this content-restricted count.

Exact-title, author and formula searches found no official correction or
contemporary explanation connecting the open label to the earlier
binomial formula. That negative search result is not proof of an
editorial mistake. Possibilities such as an unstated desire for a product
or positive coefficients remain speculation and are not adopted here.

## Deeper structure and useful consequences for our writeup

Hering--Howard Sections 2, 4 and 5 identify the count with the degree-n
part of the invariant ring for m ordered points on the projective line
with all weights two. The associated polytope Q_w is explicitly given by
top-row multiplicities, their total, coordinate bounds and the strict
column prefix inequalities (Definition 4.2). Proposition 4.5 supplies a
SAGBI degeneration to its polytopal semigroup algebra. Theorem 1.2 gives
a squarefree quadratic Gröbner basis and Koszul property for even
weights. These are geometric explanations for why fixed-m stretching
has a polynomial Hilbert count. They are not necessary extra assumptions
for the enumeration, nor newly solved contest conditions.

Remark 3.6 distinguishes its alternating counting formula from a stronger
desire for positive polynomial coefficients and points to the 2004
King--Tollu--Toumazet conjecture. This is a historical remark in that
paper, not a verified current-status assertion about that separate
conjecture and not evidence that positivity was intended by B4. Remark
3.7 observes generic Kostka computation is #P-complete; generic varying
shape/content hardness does not contradict a special equal-content
formula that collapses exponentially many subsets into O(m) terms.

The useful next mathematical action for this problem is faithful
integration of the already reviewed literal formula with the original
pre-competition attribution and grading dictionary. Additional work on
arbitrary content, positivity or invariant presentations would require a
new expressly authorized question. No such question is substituted here.

## Provenance, records and limits

The setter of 2018 B4 remains unverified. Neither the 2026 committee roster
nor committee membership, research topic, report authorship or chairmanship
has been used as individual credit. No one was contacted. The provenance
discrepancy is recorded for the coordinator's central mapping, not edited
there by this worker.

The [search/source manifest](deep-literature-r2-search-sources-v1.json)
records dated queries, versions, cache paths, SHA-256 values and failed
routes. Full third-party PDFs remain in ignored `.cache/`; no full paper
was added to the owned notes. Existing 2018 accepted proof/reviews were
read as context and not altered. No Git actions, paid access or access
bypass occurred. Latest authoritative weekly telemetry in this task:
15% of the 10080-minute account window, reset 1792745187; 90% total cutoff.
