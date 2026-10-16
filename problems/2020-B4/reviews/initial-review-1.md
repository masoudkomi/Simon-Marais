# 2020 B4(b): independent initial review R1

Completed 2026-10-16 UTC (2026-10-17 Australia/Brisbane). This report reviews the frozen **candidate proof - unverified** at `proofs/partial-v1.md`, SHA-256 `f53945e49bd626847e52a61f7e39e96defd2ae44900f9d235c2c14e720f41525`. It does not promote that candidate or claim a complete solution of B4(b).

**Verdict:** I found no substantive mathematical objection to P1-P6 or to the separately attributed square-descent application, within the stated partial scope. I reconstructed the complete argument, audited the implemented necessary conditions, and performed independent exact checks. There is one citation-version correction and one optional wording improvement below. Acceptance, any repairs, a second independent review, and promotion remain the coordinator's responsibility.

## Independence, scope, and settings

I did not construct the candidate. I did not read another review, its conclusions, the shared issue log, research/status integration logs, or another reviewer's messages. Inputs were AGENTS.md, the frozen candidate, statement.md, references.md, the computational scripts and saved data, official sources, and the cited primary literature. The input and output hashes are in `initial-review-1-manifest.json`; source URLs, locators, and access limitations are in `initial-review-1-sources.json`.

Only B4(b) is audited. I did not solve or reconstruct the preliminary prime-order construction. An initial whole-page extraction of the official solutions and of Alexeev-Mixon included adjacent preliminary/construction text in tool output; that material was not used in this review or reproduced here. Subsequent extracts were restricted to the relevant setup/discussion. Positive finite checks use the boundary q=1 and the already recorded composite prime powers q=4,8,9. At q=2 I check the general nondegeneracy count, without constructing a preliminary example.

Requested settings supplied at launch: `gpt-6.1-sol`, reasoning `max`. No verified effective model/effort readback was available; this is not a claim that the requested settings were independently confirmed. Authoritative account-wide telemetry was 8% weekly used initially and 9% at the final source/computation transition, window 10080 minutes, reset Unix time 1792745187. Both observations were in the same window and below the 90% cutoff. No separately billed API, purchase, or subscription was used.

## Official statement fidelity

I compared statement.md with the official Paper B page 2, using text extraction and the existing visually inspected B4 crop. The official target is all integers n>=2, with n selected vertices of a regular polygon on n^2-n+1 vertices, and all unordered Euclidean pairwise distances distinct. P1 uses exactly that domain, number of vertices, and distance condition. The coordinate labeling is a relabeling, not an extra hypothesis.

The order convention q=n-1 and cardinality k=n=q+1 is correct. In particular n=2, q=1 is taut and is outside the positive-exponent prime-power convention. The official discussion's informal converse must have this exception. P2 correctly restricts nondegenerate projective planes to q>=2. Neither the source discussion nor the candidate supplies an unrestricted solution of the cyclic Prime Power Conjecture.

## Complete reconstruction of P1-P6

### P1: distances and ordered differences

The number v=n(n-1)+1 is odd. For r=1,...,(v-1)/2, the angle pi*r/v lies strictly between 0 and pi/2, so the chord length 2R*sin(pi*r/v) is strictly increasing for R>0. Thus equality of two chord lengths is exactly equality of their residue differences up to sign. The zero difference never comes from two distinct selected vertices. Reversal cannot preserve a nonzero difference because 2 is a unit modulo v.

If the unordered distances are distinct, ordered differences from distinct unordered pairs cannot agree; the two orientations of one pair also cannot agree. There are k(k-1)=v-1 such differences, exactly the number of nonzero group elements, so injectivity gives one occurrence of each. In the other direction, equal unordered distances yield equal directed differences after choosing the appropriate orientation, contradicting uniqueness. The triangle boundary {0,1} modulo 3 satisfies the condition. This proves both directions with no assumption of prime-power order.

### P2: precise plane equivalence

For t!=0, a point of D intersect (D+t) is uniquely an a in D with a-b=t for b in D. Consequently the intersection size is one. Since k>=3 for q>=2, two translates cannot be equal. Two distinct points x,y are on the translate determined by the unique representation x-y=a-b, namely t=x-a=y-b. Each point has exactly k incident translates because t=x-d for the k distinct d in D.

There is a point P outside a chosen line L because v-k=q^2>0. For A,B distinct on L, the lines L,AP,BP are distinct and intersect pairwise at A,B,P respectively, with no triple intersection. Their union therefore has 3k-3=3q points. The complement has (q-1)^2>0 points. At the smallest permitted q=2 the complement still has one point. Any chosen Q in the complement makes A,B,P,Q have no collinear triple. This establishes the nondegenerate axioms; q=1 is deliberately not covered. Translating residues preserves incidence and acts regularly on points and lines.

Conversely, the group must act by collineations, as the final paragraph of P2 specifies. The stabilizer H of a line acts freely on that line's q+1 points, so |H| divides q+1. It also divides |G|=q^2+q+1. Their gcd is one because v=q(q+1)+1. Thus every line stabilizer is trivial. A line orbit has v elements, all the lines, so the action is regular on lines as well. After identifying points with G, every line is a unique translate of the chosen D. The unique line through x,y gives existence of a representation of x-y, and uniqueness of both the line and its translating element gives uniqueness of the ordered pair in D.

The proof establishes the cyclic regular-collineation case. It does not assign such an action to an arbitrary plane. Being cyclic, being Desarguesian, and having prime-power order are kept distinct. There is no use of an unproved structural conjecture here.

### P3: two normalizations and multipliers

The directed difference 1 has a representation a-b=1. Subtracting b makes 0 and 1 elements of the set; its elements may then be sorted. This loses no existence case, but it can retain multiple representatives of an equivalence class. It need not be the same translate as the next normalization.

For S=sum(D), gcd(k,v)=1 gives the unique c=-S/k modulo v for which the translated sum is zero. If t is already known to be a numerical multiplier of this normalized D, then tD=D+h has sums 0=0+kh. Thus h=0. The same fixed set works for every multiplier, with no choice depending on t. Translating an original set preserves the numerical-multiplier property because t(D+c)=D+c+h+(t-1)c.

The First Multiplier Theorem is an import, not derived from the sum argument. Its planar cyclic case applies: the ambient group is abelian, lambda=1, each prime p dividing q has p>1, and gcd(p,v)=1. A subgroup generated by these multipliers therefore fixes the single normalized set. There is no converse inference from invariance to the difference-set property.

### P4: occupancy, diagonal terms, and the spectral identity

For any divisor d of v, the zero residue class for ordered differences contains k diagonal pairs and h-1 nonzero differences, where h=v/d. Its total is k+h-1=q+h, giving the squared-occupancy equation. Every nonzero residue class modulo d has exactly h elements of Z/vZ, all nonzero, giving the cross-correlation equation. This also covers d=1 and d=v. The indices i-r and i+r give the same counting statement after reversing differences, so the stated sign convention is sound.

In the group ring, the constant coefficient of A(X)A(X^-1) is k=q+1 and each other coefficient is one. This gives exactly q+sum X^r. Every nontrivial v-th root satisfies sum zeta^r=0, even if it is not primitive, and A(zeta^-1) is the complex conjugate of A(zeta). Hence the norm identity follows. Passing occupancies or these spectral consequences is not asserted to construct a difference set.

### P5: quotient norm and every prime case

If q=1 modulo 3, then 3 divides v and the d=3 equations apply. The nonzero correlation is ab+bc+ca=h, and the zero correlation is a^2+b^2+c^2=q+h. Their difference is q. Substituting x=a-c,y=b-c gives q=x^2-xy+y^2 without a sign or factor-of-two error.

For p=2, the only zero of this form modulo p is (0,0). For an odd prime p=2 modulo 3, if y=0 then x=0; otherwise t=x/y satisfies t^2-t+1=0. It follows that t^3=-1. The element -t has cube one and is not one, since t=-1 would imply p=3. This contradicts Lagrange's theorem in the group of order p-1. Thus p divides both x and y. Repeatedly dividing x and y by p removes p^2 from the norm at each step; since q>0, the process terminates and forces an even p-adic valuation.

For q=10 modulo 12, q=1 modulo 3 but v_2(q)=1, a contradiction. The shift to n=11 modulo 12 is exact. The comparison with Bruck-Ryser is also correct: 10=1^2+3^2 passes that necessary sum-of-two-squares condition. No claim about sufficiency is made. This is a standard reconstructed restriction with no novelty claim.

### P6: all orbit strata and bounded subset sums

For each d dividing v, x with gcd(x,v)=v/d corresponds bijectively to a unit u modulo d by x=(v/d)u. The stratum size is phi(d), including phi(1)=1 for x=0. For t,t' in M, equality tx=t'x modulo v is equivalent to (t-t')u=0 modulo d, and cancellation of u gives t=t' modulo d. The orbit size is therefore the order of the image of M in the units modulo d, identical throughout the stratum. Partitioning it gives phi(d)/|M mod d| orbits.

As a union of entire multiplier orbits, a normalized D must have size k expressible using each orbit at most once. Grouping equal lengths gives the bounded subset-sum condition. The singleton {0} is counted once; it is not a zero-length orbit. Binary splitting of a count into 1,2,4,... and a final remainder represents every multiplicity from zero to that count. Truncating reachability above the positive target cannot remove a sum that later decreases, because all weights are positive. None of these tests considers the required difference multiplicities, so passing does not give existence.

## Imported theorems and the square-descent application

The following are checks of published statements and their application hypotheses, not independent reproofs of all the literature. Gordon's 1994 original was downloaded and pages 2-3 were visually inspected because its extracted mathematical symbols were imperfect. Original Jungnickel-Vedder, Wilbrink, and Xiang-Chen full proofs were not obtained; their source coverage is stated precisely below.

| Import and checked locator | Application audit |
|---|---|
| Gordon 1994, Theorems 2-4 | Planar abelian divisor multipliers, a common invariant translate, and the bound cardinality(M)<=q+1 with q=4 exceptional are stated. P3 also proves its needed common-translate case directly. |
| Gordon 1994, Theorem 5(2); Peluse, Theorem 2.1 | The quadratic-nonresidue obstruction is restricted to nonsquare q; the script honors this. |
| Gordon 1994, Theorems 6-8 | Square descent, the even-order restriction, and the 3-divisibility restriction match the uses here. |
| Bruck-Ryser original, Theorem 1 | q>=2 and q=1 or 2 modulo 4 are the relevant plane hypotheses; odd valuations of primes 3 modulo 4 are the obstruction. |
| Jungnickel-Vedder publisher abstract | Abelian hypothesis and even q>4 imply 8 divides q. It agrees with Gordon's restatement. |
| Wilbrink publisher abstract | Abelian regular collineation group, v_p(q)=1, p=2 or 3 imply q=p. The p=3 use is exactly the required consequence. |
| Gordon small-lambda arXiv v1, Lemma 2 and Theorems 3-4 | For the orbit inequality, the code ensures G=Z_p x Z_h, p prime, gcd(p,h)=1, s=ord_h(m), m a multiplier; lambda=1. The cyclic multiplier bound's (21,5,1) exception is avoided before application. |

For square descent, P1 first gives a cyclic, hence abelian, planar difference set of order 2304=48^2. The imported descent statement in Gordon 1994 yields an order-48 planar difference set in a subgroup. A subgroup of a cyclic group is cyclic and hence abelian. In fact the required subgroup order is 48^2+48+1=2353 and 5310721=2353*2257, consistent with the ambient order. Wilbrink applies to 48 since v_3(48)=1 and 48!=3. This contradiction is valid. The original Jungnickel-Vedder full theorem proof remains unaudited here, as references.md already discloses; the exact descent statement was checked in Gordon's original article. It is an attributed application, not a new theorem or a new prime-power proof.

### Conservative orbit inequality, including zeros

Here is my independent reconstruction of the necessity used by residual_orders.py. Since p divides v exactly once, CRT gives Z/vZ=Z_p x Z_h with gcd(p,h)=1 and exponent(Z_h)=h. The multiplier m^s fixes the second coordinate. For o>1 its orbits are h singletons at first coordinate zero and length-o orbits at nonzero first coordinate. A fixed set chooses a>=0 non-singleton orbits and b>=0 singletons, with b<=h and k=ao+b.

The ordered differences of selected singleton points occupy only (0,z), z!=0, giving b(b-1)<=h-1. Ordered differences within each selected length-o orbit occupy only (x,0), x!=0, giving a*o*(o-1)<=p-1. Other differences were omitted, so this remains a necessary, weaker count. This proves that the code's nonnegative formulation is conservative even though the paper says positive. Skipping o<=1 loses exclusions and cannot create them.

The issue is real: for q=8, p=73, h=1, m=2, s=1 and o=9, the only permitted counts are (a,b)=(1,0). The independently verified, zero-sum translate of the recorded order-8 set is {1,2,4,8,16,32,37,55,64} modulo 73; it is fixed by 2 and has no singleton. A literal strictly-positive test would reject this existing set. The implementation does not make that mistake.

## Computational audit and exact evidence

`initial-review-1-check.py` and its separate supervisor use the Python 3.12.14 standard library. The final run had child PID 33388, a 90-second hard subprocess timeout, incremental flushed checkpoints, exit code 0, and elapsed time 5.759215 seconds. The preceding version ran successfully under PID 33148 in 4.432773 seconds; the final version added the explicit zero-singleton witness check. No CAS operation, process-wide kill, timeout, or incomplete mathematical search occurred. The deliberately forced node-limit test was correctly recorded as incomplete. The exact command, parameters, PID, dependencies, and outputs are retained in the accompanying run, job, evidence, and stdout files.

Independent checks included:

- All 20349 five-element subsets modulo 21: distance-separation distinctness versus full signed difference multiplicities. There were 42 difference sets and zero mismatches. For all 42, the unique zero-sum translate was checked against all numerical multipliers, totaling 252 multiplier checks. Their full multiplier group has size 6, confirming the importance of the q=4 exception.
- The saved witnesses of orders 1,4,8,9 were verified by independent signed counts. Incidence and four-point nondegeneracy were checked for the composite prime-power examples; the q=2 complement size was checked directly from the general proof. Across 180 quotient cases, including d=1 and d=v, all occupancy and group-ring coefficient equations agreed.
- The local norm divisibility claim was checked on 31840 pairs modulo the 13 primes p<100 with p=2 modulo 3, including 2. A further 6560 positive integer norms from -40<=x,y<=40 had the required even valuations. Every saved quotient occupancy vector was independently regenerated. These finite checks supplement, rather than replace, the argument above.
- The bounded subset-sum algorithm agreed with a direct set-based enumeration in 39984 comparisons, including zero multiplicities and target zero. Actual generator-action orbits were enumerated for q=1,4,6,8,9,10,12,323,1944,2304,2435. At the three residual orders alone, this covered all 15023463 residues and agreed with the divisor-stratum formula and recorded histograms.
- The entire 2<=q<=5000 filter tally was independently reproduced with separate factorization, subgroup generation, and subset-sum code. All first examples, counts, and residual values matched. The negative n=7 search was independently completed with directed-difference rejection, agreeing with 4386 calls and no witness. An artificial one-node cap returned `incomplete_limit_reached`, not nonexistence.
- The residual orbit-inequality data were independently recomputed by enumerating b first and deriving a, rather than copying the code's enumeration of a. All data agreed, including h=1 and empty diagnostics when all available actions have o=1.

Every exclusion filter was checked for its domain: Bruck-Ryser's congruence, even q exceptions 2 and 4, Wilbrink's exception 3 and valuation condition, Mann's nonsquare condition and prime moduli, and the multiplier bound's exception. Stopping subgroup generation after q+2 distinct elements proves a sufficient lower bound for exclusion, even if that returned collection is not yet a subgroup; it is not passed to an orbit computation. Complete groups are used whenever actual orbits are needed. Residual orders mean undecided by that filter pass.

The necessary conditions are visibly insufficient. At q=28, (a,b,c)=(13,9,7) passes the quotient equations, but the published even-order condition excludes a cyclic planar set. At q=2304 the orbit lengths can sum to k=2305 as 1+1080+540+360+216+60+36+12, but square descent still excludes the order. For q=1944 and q=2435 the exact histograms fail the subset-sum condition. There is no false inference of existence from either kind of pass.

## Literature status and parameter range

Alexeev-Mixon v2 (revised 2026-01-16), section 4, distinguishes arbitrary planes, cyclic planes, and the stronger Desarguesian conjecture. It continues to treat the cyclic classification as conjectural. Its Sidon-extension result does not solve B4(b). Its two-billion lower bound is an older sufficient range and does not contradict a later larger verification. [Alexeev-Mixon v2](https://arxiv.org/abs/2510.19804v2).

The small-lambda paper's abstract reports the twenty-billion verification; section 3 and Table 2 in the cached original preprint were checked. The table describes its limit using k, so the conservative range 2<=q<2*10^10 translates exactly to 3<=n<=2*10^10, plus the separately handled n=2 boundary. I did not rerun that published computation or audit its full implementation. The publisher confirms the online date 2020-11-21 and 2022 issue. [Gordon publisher record](https://link.springer.com/article/10.1007/s10801-020-00992-x), [full preprint](https://arxiv.org/pdf/2007.07292).

Peluse's Theorem 1.2 is asymptotic; it does not eliminate every possible exceptional order. The qualifications in references.md about search coverage, inaccessible originals, and finite evidence are appropriate. This audit does not establish that no later paper exists. Prime-power existence is used only as attributed context; Singer's original proof was not audited or reproduced.

## Reviewer issue entries and disposition

| ID | Severity | Finding and requested disposition |
|---|---|---|
| R1-2020-C1 | Minor citation correction; not mathematical | `references.md` and the computational documentation label the orbit inequality as Gordon 2020/2022 Theorem 3 and the cyclic bound as Theorem 4. These numbers are correct for the cached arXiv **v1**, but the publisher-version text indexed from the author's former PDF URL has the inequality as Theorem 2 and the cyclic bound as Theorem 3 (its Theorem 4 is the contracted-multiplier extension). Identify the preprint version explicitly or give both numbering systems. The actual statements and applications audited here agree. The direct author PDF download returned HTTP 404; no claim of a newly retrieved published PDF is made. |
| R1-2020-C2 | Optional exposition | In the first sentence of P2's converse, insert "by collineations" after "cyclic regular action on points". The closing paragraph already supplies this condition, so I interpret it as part of the stated hypothesis; making it immediate avoids the literally weaker and insufficient notion of an arbitrary permutation action on the point set. |

There are no open substantive mathematical objections from this reviewer. The absence of an objection is limited to the frozen partial package and the specified source coverage. In particular, it does not turn the conjectural classification into a full solution or replace the second independent audit.
