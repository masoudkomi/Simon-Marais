# 2023 B4(b) research log

Current stopping checkpoint, 19 October 2026: COMPLETE internally reviewed classification for fixed positive nonsquare N: all(k,k),k>0, and(k,2k)/(2k,k) for positive ODD k. External publication priority unconfirmed. Next if reauthorized: Retain full real-witness domain and attribution limits. Research is paused below the weekly ceiling; no new candidate awaits independent review. [Final all-nine report](../../progress/status-2026-10-19-final.md). Earlier dated entries below are historical; frozen proof and review bytes are unchanged.

## Research significance and connections

Opening overview updated 2026-10-18. For a fixed positive nonsquare \(N\),
the problem asks when two powers of one real number can have the same
irrational part \(-\sqrt N\). It is an elementary-looking question about
rational values whose structure lies in the quadratic field
\(\mathbb Q(\sqrt N)\). Conjugation changes the sign of \(\sqrt N\);
trace and norm convert that relation into rational arithmetic.

Repeated powers in a quadratic field satisfy second-order recurrences. This
connects the exponent-pair question with Lucas-type sequences and their
resultants: a common-root condition can force a strong divisibility relation
between exponent-dependent polynomials. The proof here develops the required
resultant identity directly. These connections suggest a way to replace
unbounded numerical searches by a uniform argument about exponents. The
[official notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2023solutions.pdf)
provide the original quadratic-field context and partial cases.

The project has a complete internally and independently reviewed
classification: \((k,k)\) for every positive \(k\), and \((k,2k)\),
\((2k,k)\) for positive odd \(k\). It holds for each fixed positive nonsquare
\(N\), including nonsquare integers that are not squarefree, and permits
negative real witnesses. Mathematical priority remains unestablished; no
publication or novelty claim follows from internal review. See the
[review register](reviews/README.md), [statement](statement.md), and
[literature audit](references.md).

## Coordinator acceptance update, 2026-10-16

The full classification argument has now received two fresh, initially blind independent adversarial audits, each reconstructing the whole proof. Both found no substantive mathematical objection; no repair was required. The coordinator promoted its status to **proved, independently reviewed**. See proof.md, proofs/reviewed-v1.md and reviews/acceptance.md. The owner-stage text below is retained as historical development; its pending-audit notices are superseded by this update. Novelty and prior-publication status remain unestablished.

## Historical owner checkpoint

2026-10-16 initial owner checkpoint. **Candidate proof - unverified**; no independently reviewed result or novelty claim.

Requested launch settings: `gpt-6.1-sol`, `max`. No independent effective-setting readback was available. The coordinator monitors account-wide weekly telemetry; the owner does not infer account usage from its own token count. No paid API, install, subagent, commit, push, or write outside this year directory was used.

## Statement and scope

The cached official Paper B, page 2, was checked against the current official download index. The statement fixes a nonsquare positive integer N and asks for positive integer exponents with an existential **real** witness, without a positivity assumption. N need not be squarefree. Only B4(b) was investigated. Established preliminary restrictions are cited from the official solution notes, without solving or reproducing (a).

The gcd reduction is one-way for arbitrary real witnesses: a witness for (a,b) gives a witness for (a/d,b/d) by raising it to d. In the off-diagonal case the published parity restriction makes d odd; only then can a negative reduced witness be lifted back through a real d-th root. An unrestricted assertion that all multiples preserve the witness is false.

## Approaches, useful observations and obstructions

1. **Quadratic conjugation and sign geometry.** For coprime opposite-parity exponents, Bézout puts the negative reduced witness in Q(sqrt(N)). Conjugation gives U>V>0 with U^e−V^e=U^o+V^o=2sqrt(N), where e is even and o odd. It follows that e>o. The rational trace D=U−V and negative norm parameter P=UV are positive. The integer recurrence F_(j+2)=D F_(j+1)+P F_j gives F_e=F_o and (D^2+4P)F_o^2=4N. For o>=3, equality forces 0<D<1. These are proposed lemmas inside the unverified candidate.

2. **p-adic/denominator exploration.** Treating D and P separately at primes dividing the denominator of D initially leaves a difficult cancellation case when v(P)=2v(D) and D^2+4P has high valuation. A direct blanket assertion that such cancellation is impossible was not established and is not used. This motivates eliminating P before taking denominator information.

3. **Lucas and primitive divisors.** The recurrence has rational positive parameters and characteristic roots U,-V. Applying an integral Lucas primitive-divisor theorem would require an additional normalization and a careful audit of integrality, coprimality, nondegeneracy and primitive-divisor hypotheses. No such application was established or used. The successful proposed Lucas ingredient is instead an elementary roots-of-unity product proving a unit resultant for coprime indices; its complete proposed proof is in candidate Section 3.

4. **Resultant elimination.** The candidate eliminates P from F_e−F_o and (D^2+4P)F_o^2−4N. Two unrestricted proposed polynomial identities yield the strong integer condition

       q^(2o) | (e/2) p^(e-o) - 2^(e-o-1) o q^(e-o),

   for reduced D=p/q. A size argument excludes e−o<2o. In the other branch the condition forces e>=2q^(2o)>=2^(2o+1). A separate real inequality gives e>2^(e−3o), incompatible with that bound. This is the proposed general exclusion; no bounded search is treated as proof.

5. **Exact computations and attempted falsification.** All 28 coprime even/odd pairs with 4<=e<=18 and 3<=o<e pass the resultant constant/weighted-degree checks. All 80 unit-resultant pairs through e=30 pass. Eight numeric instances were compared with direct Sylvester determinants up to an irrelevant overall sign. The coordinator's (4,3) trace/norm formula was independently checked algebraically. All 27,397 reduced rational traces in (0,1) with denominator <=300 were tested for the positive rational branches of (4,3) and (6,5); there were no integer-N hits. These computations are finite evidence only. Full source, parameters, dependency versions and stdout are in computations/.

6. **Preserved failed computation.** The initial (6,5) branch-search code had an incorrect hand-derived discriminant core and failed a recurrence assertion. The correct core is 4D^2−8D+5. The failed script, partial stdout, error and repair are preserved. This quadratic calculation does not occur in the general proposed proof. The corrected run completed.

7. **Earlier coordinator draft.** The (4d,3d) exclusion draft remains untouched. Its signs, trace/norm equations and denominator obstruction are consistent with the new candidate and checked formulas. This is constructor development, not one of its independent audits. The diary contains overlapping small-exponent exploration, so no novelty is claimed for the restricted exclusion.

## Candidate and remaining work

The full proposed classification is recorded in [candidate-resultant-v0.1.md](notes/candidate-resultant-v0.1.md): diagonal pairs and (d,2d)/(2d,d) for positive odd d. It matches the fixed-N quantifier and permits either-sign witnesses. Proof status is strictly **candidate proof - unverified**.

Two new adversarial reviewer agents, neither involved in construction, must complete blind initial reports. One must reconstruct the whole proof. The issue log identifies the main audit obligations. Any substantive issue requires an author repair and re-review. The coordinator alone can promote a result after both audits resolve all substantive objections.

The current primary-source search found no complete published classification, but establishes no absence theorem. The official index still links the original solution notes; a May 2024 AustMS Gazette report describes this as an open problem. The diary is an author-acknowledged incomplete attempt and supplies no accepted proof. Broader novelty verification remains open; see references.md for exact queries and dates.
