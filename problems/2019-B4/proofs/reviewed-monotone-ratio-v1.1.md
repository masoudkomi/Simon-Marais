# Accepted monotone-ratio: exact coordinator scope

2026-10-17 UTC. **Proved, independently reviewed scoped partial result.**

MR1 is accepted for the ACTUAL full canonical count sequence c_n: rho1=rho2=rho3=2, rho4=15/8, and rho_(n+1)<rho_n for EVERY n>=3. Thus c is log-concave, strictly at n>=3, and the consecutive canonical ratios are decreasing strict upper endpoints converging to the accepted lambda. No original unmarked b-ratio theorem, numerical improvement or monotonic individual lower-root claim follows.

MR2 is accepted ONLY AS A CONDITIONAL IMPLICATION. If ONE uniform finite C joins EVERY pair u,v in actual K by SOME bridge of length<=C, then c_n/lambda^n<=sum_(k=0)^C lambda^k for all n, delta>0 and delta>=1/[R*sum_(k=0)^C lambda^k]. J_C/C3 remains UNPROVED; the finite joining diagnostic and separate short-joining note are not premises and are not accepted by this promotion. All actual endpoint regimes remain unselected.

Root constructed the new argument and is excluded from both independent audits. Two OTHER fresh initially blind WHOLE reports, with32 and28 inference checks covering ALL12 obligations, reconstructed the whole general signed-recurrence identity, j=n sign/indices, strict induction including n5, variable-length disjoint-union injection and empty cases, fixed-C limit order and exact R7 defect consequence. Root read the COMPLETE candidate, BOTH complete reports, ALL ledgers and source/authority records. No substantive issue or repair remains. The older R7 author's review is of the NEW MR proof; older R7 is an accepted premise, not independently recertified by its own author.

No external theorem, mathematical computation, finite cap or code-metadata shortcut supplies a missing step. Exact lambda remains in1.76522347<lambda<1.834856083; its value and actual normalized regime, annual answer and priority remain unknown. This is a scoped partial result with internal review, not external validation.

The COMPLETE frozen mathematical submission follows as a byte-identical suffix. Its historical unverified label records submission status; this header and acceptance record state the current exact scope.

---

# Monotone canonical ratios and the exact bounded-joining bridge

2026-10-17 UTC. **Candidate proof - unverified.** Root constructor.
TWO OTHER fresh initially blind WHOLE audits are required. No new
numerical enclosure, exact lambda, ordinary-output ratio theorem,
positive-defect theorem without an extra hypothesis, annual answer
or novelty is claimed. No mathematical program supplied this proof.

## Exact premises and proposed results

Use the COMPLETE accepted canonical language K, its counts c_n>0,
c0=1, and its actual nonnegative obstruction coefficients f_j:

    c_n=2c_(n-1)-sum_(j=2)^n f_j*c_(n-j), n>=1,
    f1=f2=f3=0, f4=1,
    lambda=lim c_n^(1/n), 1.76522347<lambda<1.834856083.

The empty sum at n1 is zero. These follow from the exact accepted
canonical renewal and its separately accepted exact-prefix certificate.
No capped/regular language or derivation count is substituted for K.
The just-accepted R7 gives c_n/c_(n-1)>lambda, convergence of those
ratios, and boundedness of c_n/lambda^n iff delta=2-F'(1/lambda)>0.
Its complete three-regime and original-output qualifications are retained.

**MR1.** The ratios rho_n=c_n/c_(n-1), n>=1, are NONINCREASING,
with

    rho1=rho2=rho3=2, rho4=15/8,
    rho_(n+1)<rho_n for EVERY n>=3.                    (MR1)

Equivalently c_n is log-concave, strictly so at every n>=3.
Thus rho_N itself is the minimum of the first N ratios, and these
upper endpoints decrease strictly to lambda from N>=3 onward.
The previously accepted algebraic lower endpoints remain as in R7;
no monotonicity of the individual lower endpoints is asserted.

**MR2, CONDITIONAL.** Suppose there is a FIXED integer C>=0 such that
for EVERY u,v in K some w of length<=C satisfies uwv in K. Then

    c_n/lambda^n <= sum_(k=0)^C lambda^k for every n,
    delta>0,
    delta >=1/[R*sum_(k=0)^C lambda^k], R=1/lambda.    (MR2)

No such bounded-joining hypothesis is proved here. In particular C3
remains a research question. The separate finite diagnostic plays NO
role in MR1 or the conditional implication MR2.

## 1. An elementary signed-recurrence induction

We prove a general statement directly. Let a0=1, a_n>0, alpha>0,
and b_j>=0 for j>=2 satisfy

    a_n=alpha*a_(n-1)-sum_(j=2)^n b_j*a_(n-j).

Then r_n=a_n/a_(n-1) is nonincreasing. At n1, r1=alpha;
at n2, r2=alpha-b2/a1<=r1. Suppose monotonicity has been proved
through r_(n-1), for n>=3. For2<=j<=n-1, all indices are valid and

    [a_(n-j)/a_(n-1)]/[a_(n-j-1)/a_(n-2)]
                 =r_(n-j)/r_(n-1)>=1.              (1)

Every denominator is positive. Divide the recurrences at n and n-1
by their preceding terms. Comparing the common j-terms using(1),
and retaining the extra NONNEGATIVE j=n term in the subtracted sum,
gives r_n<=r_(n-1). More explicitly,

    r_(n-1)-r_n
      =sum_(j=2)^(n-1) b_j*[a_(n-j-1)/a_(n-2)]
                         *[r_(n-j)/r_(n-1)-1]
            +b_n*a0/a_(n-1) >=0.                  (2)

This proves the general induction for every n. It requires positivity
of the ENTIRE a sequence; arbitrary signed recurrences which later
give zero or negative terms are not covered. There is no assertion
that every positive sequence or every avoidance language has this form.

Apply it to the accepted c recurrence with alpha2,b_j=f_j.
The initial zero coefficients give c1=2,c2=4,c3=8; f4=1 gives c4=15.
Hence the displayed initial ratio values in MR1 are exact.

To prove strictness, rho4<rho3 is already established. For n>=5,
the j4 term is present in(2). By the strict induction hypothesis,

    rho_(n-4)>=rho_(n-2)>rho_(n-1),

where at n5 the first comparison uses rho1>=rho3. Its coefficient
f4*c_(n-5)/c_(n-2) is strictly positive. Thus that one summand
in(2) is positive and every other summand is nonnegative. We get
rho_n<rho_(n-1), completing strict induction. Log-concavity follows
by multiplying rho_(n+1)<=rho_n by the positive denominators;
its strict indices are n>=3, while n1,n2 are equalities.

R7 already proves rho_n>lambda and rho_n->lambda. Combining these
accepted facts with the new induction gives the decreasing STRICT
upper endpoints in MR1. It does not prove an actual new numerical
bound without using exact count data, and no data are newly computed.
In particular the earlier R7 diagnostic about arbitrary monotone
submultiplicative sequences remains valid: the extra signed recurrence
with nonnegative f_j is the essential added structure here.

## 2. Bounded joining would choose the defective regime

Assume precisely the additional hypothesis of MR2. Fix n,m and select
one allowed bridge for EACH pair u in K of length n, v in K of length m.
If its selected length is k, the resulting word of length n+m+k
determines u and v by cutting at their known lengths. Thus the
assignment is injective into the DISJOINT UNION over k=0,...,C, and

    c_n*c_m<=sum_(k=0)^C c_(n+m+k).                    (3)

The bridges may vary with both words, their lengths may differ, and
no unique realization or one common bridge is assumed. Only a uniform
finite bound C is required. The n0/m0 endpoints cause no exception.

Divide(3) by c_m. For fixed n,k, the accepted R7 ratio limit gives

    c_(m+n+k)/c_m=product_(i=1)^(n+k) rho_(m+i)
                           ->lambda^(n+k).

If n+k0 the empty product is1. There are finitely many k and C is
fixed before the limit, so(3) yields
c_n<=lambda^n*sum_(k=0)^C lambda^k for every n. By R7's exact
boundedness equivalence delta>0. Its limit is1/(Rdelta), hence taking
n to infinity in the uniform bound gives the final inequality in MR2.
No ratio monotonicity is actually needed for this implication; it uses
the already accepted R7 limit and boundedness equivalence. There is
no circular use of positive defect to obtain that limit.

The bounded-joining condition remains UNPROVED. The separate hand J2
obstruction and one length8 diagnostic are UNVERIFIED research context,
not premises. No finite absence of counterexamples or generic code
theorem is substituted for(3)'s uniform combinatorial hypothesis.
All three actual endpoint regimes therefore remain unresolved here.

## Sources, roles, work log and exact limits

Mathematical inputs are solely accepted canonical renewal and R7,
with exact f4 from the previously reviewed finite prefix. Their full
bodies/acceptance scopes were read in root's immediately preceding
WHOLE2019 review and reconciliation. Root authored the older moment
packet and reviewed other old2019 work, but supplied none of NEW R7's
positive-kernel proof. Those roles do not certify this NEW construction:
root is MR constructor and cannot count as either independent auditor.

The elementary signed-recurrence comparison is written in full, without
claiming a new general sequence-theory mechanism or importing a theorem
from search snippets. A bounded primary literature search for reciprocal
power-series log-concavity/Kaluza-related methods located general renewal
context but no theorem was used. Cross-bifix-free-code repository metadata
concerns restricted/fixed languages and supplies no joining theorem for
the current full K. The exact adjacent-count limit was already accepted
in R7 and is not relabelled new. Priority remains unestablished.

Root first examined a possible short joining route. A hand example
blocked C2. ONE bounded counterexample diagnostic (separately saved)
found no C3 failure at length8; no larger scan followed. Returning to
the ACTUAL recurrence instead revealed(1)--(2), so the unconditional
monotonicity proof uses no diagnostic data at all. The generic-Fekete
shortcut, unconditional joining claim, individual lower-root monotonicity,
positive-defect conclusion without joining, transfer of ratios to b_n,
exact lambda, analytic continuation and full annual answer are all
explicitly unavailable. All older frozen mathematical bytes remain
unchanged; new metadata checks are integrity only.

## Twelve complete WHOLE-audit obligations

1. Exact canonical c/F recurrence, c0, all positive terms, f1..f4 and
   accepted full-language scope; no cap or derivation substitute.
2. Generic induction domains, n1/n2, j=n extra term and positivity of
   every denominator; no negative-index ratio in(1) or(2).
3. Exact cancellation identity(1) and sign of every term in(2).
4. Complete application to c, exact initial values and rho4=15/8.
5. Strict induction via j4 for EVERY n>=5, including n5 indices.
6. Log-concavity equivalence/strict n>=3 and the R7 limit/strict upper
   combination, without new numerical or lower-root monotonicity claims.
7. MR2 is CONDITIONAL on one uniform C, while bridges depend on u,v.
8. Injectivity into the disjoint union in(3), including variable length
   and empty-word cases; no matching/factor or collision omitted.
9. Fixed n,k finite ratio products, limit order with FIXED C and no
   circular assumption of bounded normalized counts.
10. Exact R7 boundedness/finite-limit consequence and inequality for
    delta, without promoting the unproved joining hypothesis.
11. All source/old-role limits and exclusion of diagnostic data from
    the unconditional theorem; no imported generic-code theorem.
12. Whole candidate status and two-OTHER-audit requirement, actual
    lambda/regime/original-output/annual/priority gaps preserved.
