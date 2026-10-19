# ET12 independent WHOLE initial review 1

2026-10-19 UTC. Reviewer C, `/root/review_2017_coarsening_r1`. **Independent initial review; coordinator reconciliation pending.** This document is sealed until the coordinator explicitly confirms BOTH ENTIRE initially blind review checkpoints. Nothing here promotes the candidate.

Target: B's `reasoning-exception-return-r12-candidate-v1.md`, 25536 bytes, SHA256 `de6c6478d45115aa559d00070c7ed469ab9b146d07398219b99b1a0553057c87`, with its complete five-file frozen packet. B is the sole NEW constructor. I supplied no NEW ET12 inference. I previously constructed accepted R10 and reviewed accepted GR11. Those roles are disclosed: this audit independently reconstructs NEW ET12, and does not count as a new independent certification of my own older R10. The accepted inputs remain separately attributed and conditional exactly as their current authorities state.

Requested inherited settings are `gpt-6.1-sol` / `max`; an independent effective backend readback is unavailable. No configuration or API change was made. No corresponding NEW ET12 peer report, finding, file inventory, hash or metadata was accessed or received. No mathematical executable, numerical test, scan, CAS, old certificate, source/author/helper/freezer replay, Git operation or shared/old/cache mutation supplied evidence.

## 1. Disposition and exact scope

**PASS all 36 obligations in the stated ET1--ET3 scopes. No substantive defect or required repair found.** Ten scope/adversarial notes below are closed. This is a mathematical initial-review disposition, not a full annual solution or an external source-theorem certification.

The local trace ladder is proved for every prime (p\geq5), finite exact (s=v_p(d)\geq2), both reciprocal signs, and (1\leq r\leq p-2). Its actual application assumes the restricted ordinary signed prime-diagonal equation at (p\geq37) and equality of the ACTUAL characteristic ideal classes. The accepted GR11 input then leaves exact depth two near (-1). ET12 neither excludes that sector nor infers that the local family lifts globally. Its individual height bound is weaker than R10. The comparison with the inspected author source identifies only a limit of a stated LOCAL divisibility inference, not a counterexample to an actual-solution/Vandiver theorem.

The official open problem has ordinary integer quadruples satisfying (1+X+\cdots+X^n=Y^q), (n,q\geq2). Here the restricted term count and exponent are (p), and the official degree is (p-1). There is no claimed reduction of all official solutions to that sector. I read the complete local official statement and primary setup/open(b); preliminary text returned incidentally was not investigated or reproduced.

## 2. Entire independent reconstruction

### 2.1 Fields, units, valuations, and the branch

Put (e=p-1), (L=\mathbb Q_p(\zeta_p)), (\mathcal O_L=\mathbb Z_p[\zeta_p]), (P=(\zeta_p-1)). Eisenstein's criterion for (\Phi_p(1+T)) gives degree (e), total ramification, and (v_P(p)=e). The usual integral basis is (1,\zeta,\ldots,\zeta^{p-2}). This distinguishes integer-valued (v_P) from (v_p(p)=1).

The element (1+\zeta) is a GLOBAL cyclotomic unit: its norm is (\Phi_p(-1)=1). Thus (\mu=(1+\zeta)^{-1}) and every (\nu_r=(\zeta^2-\zeta)(1+\zeta)^{r-1}) are integral at ALL finite primes of (K=\mathbb Q(\zeta)); also (\nu_r\in P\mathcal O_L). This is stronger than local-at-(p) integrality and is needed later.

For η in {1,-1} let

    F_eta(T)=(1-mu*T)^(eta/p)*(1-zeta*mu*T)^(-eta/p)
            =sum_(n>=0) A_n*T^n.

Use the formal binomial branches with constant term one. Define

    P_n(Z)=sum_(a=0)^n binom(eta/p,a)*binom(-eta/p,n-a)*Z^(n-a).

Then (A_n=(-1)^nP_n(\zeta)/(1+\zeta)^n). For EVERY (n), (p^n n!A_n\in\mathcal O_K): multiply each binomial by its own (p^a a!) or (p^{n-a}(n-a)!); the resulting products have integral factors η-pj or -η-pj, and the remaining coefficient is an ordinary binomial integer. No factorial is inverted globally in this argument.

Write (d=p^st), (t\in\mathbb Z_p^\times), (s\geq2). The (n)-th evaluated term has

    v_P(A_n*d^n) >= e*((s-1)*n-v_p(n!)).

Legendre's formula gives (v_p(n!)\leq(n-1)/e) for (n\geq1), so these valuations tend to infinity. The (n=1) term equals η(ζ-1)d/[p(1+ζ)] and has valuation ((s-1)e+1). For (n\geq2) the terms have valuation at least (2e): (n=2) follows directly, and for (n\geq3) the displayed estimate is already larger than (2e). Consequently (F_\eta(d)\in U_2). The formal (p)-th-power identity evaluates there by convergence.

The only (p)-th root of unity in (U_2=1+P^2\mathcal O_L) is one, since every nontrivial (\zeta^a-1) has (P)-valuation one. Hence this evaluated series is the SAME unique normalized root (\gamma_d^\eta), not an arbitrary phase. This also independently proves the existence needed for the purely local ET1 statement.

### 2.2 Trace identities and the first surviving coefficient

The cyclotomic trace satisfies (\operatorname{Tr}(1)=p-1), (\operatorname{Tr}(\zeta^a)=-1) for (1\leq a\leq p-1). Therefore, for a polynomial (Q) of degree at most (p-1),

    Tr(Q(zeta))=p*Q(0)-Q(1).

The degree restriction is essential and is obeyed below. On the integral basis, (\operatorname{Tr}((\zeta-1)\cdot1)=-p), whereas (\operatorname{Tr}((\zeta-1)\zeta^a)=0) for (1\leq a\leq p-2). Thus

    Tr(P O_L)=p Z_p.

Pairing (c) with (-c) in (1/(1+\zeta^c)) gives (\operatorname{Tr}(\mu)=e/2), an equality in (\mathbb Q_p).

Let (B_n=\operatorname{Tr}(\nu_r A_n)). For (0\leq n<r), cancel the denominator (1+\zeta); the remaining polynomial is

    (-1)^n*(Z^2-Z)*(1+Z)^(r-1-n)*P_n(Z).

It has degree (r+1\leq p-1), constant term zero and value zero at one, so its trace is exactly zero, including (n=0).

At (n=r), divide

    (Z^2-Z)*P_r(Z)=(1+Z)*Q(Z)+2*P_r(-1).

Then (\deg Q\leq r+1\leq p-1), (Q(0)=-2P_r(-1)), (Q(1)=-P_r(-1)). Applying the polynomial trace formula and (\operatorname{Tr}(\mu)=e/2) gives

    B_r=(-1)^(r+1)*p*P_r(-1).

Modulo (p), clearing the complete denominator yields

    p^r*r!*P_r(-1) = (2*eta)^r mod p.

Indeed each summand reduces to η^a(-η)^(r-a)(-1)^(r-a) times the corresponding ordinary binomial coefficient. Their sum is η^r*2^r. Since (r<p), (r!) is a (p)-unit. Hence (v_p(B_r)=1-r). This NONINTEGRAL coefficient for (r\geq2) is the essential denominator that cannot be discarded.

### 2.3 The entire infinite tail

For all (n), multiply (A_n) by (p^n n!). Its integrality and (\nu_r\in P\mathcal O_L) imply

    v_p(B_n)>=1-n-v_p(n!).

Thus every (n>r) contributes a term of valuation at least

    (s-1)*n+1-v_p(n!).

This is STRICTLY larger than (k_r=(s-1)r+1). If (n<p), (v_p(n!)=0<n-r). If (n\geq p), (r\leq p-2) and

    n-r >= n-p+2 > (n-1)/(p-1) >= v_p(n!).

The strict middle inequality is equivalent to ((p-2)(n-p+1)+1>0). No cutoff at (n=p), bounded-degree approximation, or unproved tail estimate has been used. These bounds tend to infinity. Trace is a continuous finite-dimensional linear map, so the convergent series may be traced term by term. The one least-valuation term therefore cannot be cancelled by the tail.

Combining its coefficient, the factor (d^r), and the vanished earlier terms proves

    v_p(H_(r,eta)(d))=(s-1)*r+1,
    H_(r,eta)(d)/p^((s-1)*r+1)
       =(-1)^(r+1)*(2*eta*t)^r/r! mod p.

At (r=p-2), (r) is odd, Wilson gives ((p-2)!=1\pmod p), and Fermat reduces the leading residue to η/(2t), which is nonzero. This proves ET1 over its whole domain, not just a lower valuation bound.

### 2.4 Actual ordinary integer traces

For an ACTUAL solution (\Phi_p(X)=Y^p), (p\geq37), |X|>=2, condition(C) is equality of the classes of the unique actual integral (A) and (jA), where (A^p=(X-\zeta)), (N(A)=Y). It is not inferred from the local root. The separately accepted R10 supplies the global ratio root

    gamma^p=(X-zeta)/(zeta*X-1),
    gamma*jgamma=1, (gamma)=A/jA,

with its unique completion in (U_2), when the center is (-1). Substituting (d=X+1) gives exactly ((1-\mu d)/(1-\zeta\mu d)), with no missing sign or root-of-unity factor. The ET1 branch and this global root coincide by the same (U_2) uniqueness. Accepted GR11, with its explicitly published signed height import, leaves (v_p(X+1)=2) under(C); ET2's formula itself remains valid at every finite depth (s\geq2) in its printed conditional domain.

The product over ALL Galois conjugates of (A) is the rational ideal ((Y)). Both (A) and (jA) therefore divide ((Y)). It follows that

    (Y*gamma)=(Y)*A/(jA),
    (Y/gamma)=(Y)*(jA)/A

are integral ideals. Both numbers belong to the ring of integers O_K; no representative is declared principal, and local integrality alone is not substituted for this ALL-prime argument. Multiplication by the globally integral ν_r then gives ordinary integer traces Δ_(r,η).

Because (X=-1\pmod p), the equation gives (Y^p=\Phi_p(X)=1\pmod p). Thus (Y=1\pmod p), with (Y>1) and (p\nmid Y). There is one prime above (p), with local degree (p-1=[K:\mathbb Q]), so the rational trace in (K) agrees with its trace in (L). Multiplication by (Y) preserves both the exact valuation and the displayed residue. In particular the actual last trace has valuation (p-1) at depth two.

At every complex embedding (\sigma), |σ(γ)|=1 follows from γjγ=1 and the commutativity of the Galois group. Also |σ(ν_r)|<2^r for an odd (p), including (r=1). Consequently

    0 < |Delta_(r,eta)| < (p-1)*2^r*Y.

Its exact integer divisibility gives (Y>p^{(s-1)r+1}/[(p-1)2^r]). The right side grows with (r), with ratio (p^{s-1}/2>1). At (r=p-2), dividing this strongest individual trace lower bound by the accepted R10 lower bound (p^{1+(s-1)(p-1)}/2^{p-1}) gives exactly (2/[(p-1)p^{s-1}]<1). This is no new useful height or Diophantine exclusion.

For the reciprocal check, (j\nu_r=-\zeta^{-r-2}\nu_r). At (r=p-2), (j\nu_r=-\nu_r), so the two ACTUAL reciprocal traces are exact negatives. Their leading residues change by the same sign. They are not independent constraints.

### 2.5 The local counterfamily and its limits

Take (d=p^2), (X=p^2-1), for any prime (p\geq5). The preceding series produces the required local root. Its last trace has exact valuation (p-1<2(p-2)), with leading residue η/2. This is a symbolic entire-prime-family counterexample ONLY to deriving the stronger local divisibility from that expansion and normalization alone. It supplies no (Y), no actual Diophantine solution, no global root and no class equality. It cannot refute a theorem imposing additional actual-solution and Vandiver assumptions. For an actual solution under(C), ET2 would impose its exact trace on that SAME root; an external stronger divisibility would require an additional valid arithmetic argument or another auxiliary.

Finite depth is essential: at (d=0) the trace is zero, outside ET1. Depth one, (p=3), and (r=p-1) are not claimed. The upper range on (r) protects both the trace polynomial degree and the strict factorial-tail inequality. Negative ordinary (X) changes neither the (p)-adic unit argument nor the positive ordinary integer (Y) or all-embedding bound.

## 3. All 36 separate obligation outcomes

Every PASS is an independent hand disposition in the displayed scope; no program evaluated any formula below.

| ID | Outcome and reason |
|---|---|
| ET12-O01 | PASS. Official(b) has ordinary signed quadruples; the actual diagonal here has term count/exponent p and degree p-1, without an annual reduction. |
| ET12-O02 | PASS. Local prime p>=5 is distinct from actual p>=37. Neither p3 nor a stronger annual domain is inserted. |
| ET12-O03 | PASS. C is equality of ACTUAL ideal classes for the unique integral A; no principality or arbitrary local-to-global inference. |
| ET12-O04 | PASS. Exact finite depth s>=2 and unit t are explicit; d0/depth1 excluded, both X signs retained. |
| ET12-O05 | PASS. FULL current R10/GR11 bodies and EACH current MDJSON read; missing GR11 middle from an earlier clipped read was separately recovered in full. Older C R10 authorship/GR11 review disclosed. |
| ET12-O06 | PASS. Eisenstein degree p-1, integral basis, unique p-completion and v_P(p)=p-1 agree with all uses. |
| ET12-O07 | PASS. Norm(1+zeta)=1 proves GLOBAL inverse integrality; nu_r lies in P. No fractional ideal scope loss. |
| ET12-O08 | PASS. Direct d=X+1 substitution gives the exact quotient, and eta=-1 is its reciprocal without a phase change. |
| ET12-O09 | PASS. Coefficient convolution has (-1)^n and exponent n-a; the eta sign is correct. |
| ET12-O10 | PASS. The product/ordinary-binomial argument proves p^n n! A_n integral for EVERY n at EVERY prime. |
| ET12-O11 | PASS. Legendre's bound proves convergence through n=p and every later factorial jump; no truncated tail. |
| ET12-O12 | PASS. First/deeper term bounds put the series in U2; mu_p intersects U2 trivially, identifying the SAME normalized branch. |
| ET12-O13 | PASS. Tr Q(zeta)=pQ0-Q1 is used only at degree<=p-1. The numerator division at n=r lowers its possible degree p first. |
| ET12-O14 | PASS. Integral-basis traces prove Tr(P O_L)=p Z_p, including equality via zeta-1 itself. |
| ET12-O15 | PASS. Reciprocal pairing gives Tr mu=e/2, legitimate at odd p. |
| ET12-O16 | PASS. All n<r, including n0, leave degree r+1<=p-1 with zero constant and value at1. |
| ET12-O17 | PASS. Remainder is 2P_r(-1); Q0=-2P_r(-1), Q1=-P_r(-1), and Q degree<=p-1. |
| ET12-O18 | PASS. Combining polynomial trace and Tr mu gives (-1)^(r+1)pP_r(-1), with exact sign and single p factor. |
| ET12-O19 | PASS. The mod-p numerator sum is (2eta)^r, nonzero for r<p; coefficient valuation is 1-r. |
| ET12-O20 | PASS. n-r>v_p(n!) holds for all n>r by the two explicit ranges, including n>=p. |
| ET12-O21 | PASS. Trace continuity and increasing lower bounds justify termwise trace; no later term can cancel the unique minimum. |
| ET12-O22 | PASS. Exact equality and nonzero leading residue follow for EVERY r/eta, rather than a lower bound alone. |
| ET12-O23 | PASS. r=p-2 odd, Wilson and Fermat give eta/(2t), including eta=-1. |
| ET12-O24 | PASS. R10 supplies the GLOBAL root under C; quotient identity plus local U2 uniqueness identifies it, with no converse local lift. |
| ET12-O25 | PASS. Product of actual conjugate ideals=(Y) makes both Ygamma and Y/gamma integral at ALL primes without A principal. |
| ET12-O26 | PASS. Y>1, Y1modp and p-free, combined with the unique p-completion, give ordinary integer Delta and unchanged residue. |
| ET12-O27 | PASS. Complex norm-one and strict |nu|<2^r make exact divisibility yield the strict height inequality. |
| ET12-O28 | PASS. The r-step ratio is p^(s-1)/2>1; strongest member/R10 is exactly 2/[(p-1)p^(s-1)]<1. |
| ET12-O29 | PASS. jnu_r=-zeta^(-r-2)nu_r; r=p-2 reciprocal traces are negatives, not independent mismatched valuations. |
| ET12-O30 | PASS. GR11's accepted actual conditional conclusion leaves s2 and hence last valuation p-1; its published height premise remains attributed. |
| ET12-O31 | PASS. Entire local family d=p² has no asserted Y, solution, C or global lift. It refutes only the specified LOCAL implication. |
| ET12-O32 | PASS with stated source limit. Fresh COMPLETE operative Section5 text includes extra actual/Vandiver hypotheses and changing gamma/delta notation; no theorem refutation, final-publisher identity or erratum claim. |
| ET12-O33 | PASS with literal limits. Source text ranges and failed access are separated from unread pixels/foundations; my reads are recorded independently below and in sourcesJSON. |
| ET12-O34 | PASS. Center0 transfer, leading unit root, joint combinations and nontrivial minus classes are genuine remaining gaps, not hidden conclusions. |
| ET12-O35 | PASS. No stronger useful height, exclusion, all-prime-range claim, full annual solution or publication priority is inferred. |
| ET12-O36 | PASS. New helper is documentary-only; author/source/old executables not run. Two OTHER whole audits and coordinator reconciliation remain required. |

## 4. Issue ledger: no open substantive issues

| ID | Type | Challenge and resolution |
|---|---|---|
| ET12R1-N01 | Closed scope | Local existence at an ordinary X does not give an actual solution or C. ET1/ET3 say this explicitly; ET2 supplies the global root only through accepted R10. |
| ET12R1-N02 | Closed boundary | d0 would have zero trace and depth1 is not covered. p3/r=p-1 are unclaimed; no endpoint counterexample to a printed assertion. |
| ET12R1-N03 | Closed denominator | Cleared coefficient is p^n n! A_n; treating A_n integral would be wrong. The proof retains the full denominator and the exact 1-r trace valuation. |
| ET12R1-N04 | Closed tail | Factorial jumps cannot match the first surviving term, by the strict ALL-n inequality, not just n<p checking. |
| ET12R1-N05 | Closed degree/phase | Degree p numerator is divided first; Q degree<=p-1. The unique U2 branch rules out a hidden root-of-unity phase. |
| ET12R1-N06 | Closed global integrality | Local root/integrality alone would not make an ordinary trace. Both Ygamma orientations are cleared globally using actual ideals dividing (Y). |
| ET12R1-N07 | Closed dependency/role | C authored older R10. Current R10/GR11 scopes were fully read with EACH authority; this is no fresh independent self-recertification of R10. |
| ET12R1-N08 | Closed strength | Individual heights are strictly weaker than R10; reciprocal top traces are negatives, and no joint independence or height gain is claimed. |
| ET12R1-N09 | Closed source limit | The author-copy Section5 text was read completely. Bars/pixels/final publisher and external foundations are not certified. A local counterfamily cannot refute its extra-hypothesis theorem. |
| ET12R1-N10 | Closed frontier | No C-exclusion, minus-class impossibility, ordinary infinite family of solutions, annual result or novelty follows. Candidate keeps those gaps visible. |

## 5. Failed adversarial routes and remaining arithmetic gap

I tested conceptually whether high factorial indices could create an equal-depth term; the strict inequality in 2.3 excludes it. I challenged the rational/global denominator transition: the explicit actual-ideal argument in 2.4 closes it, whereas a purely local argument would fail. I checked reciprocal sign and the last residue independently; both agree, so they cannot manufacture two incompatible constraints. I also checked whether the local counterfamily accidentally asserts an ordinary solution; it expressly supplies none.

At the source level, a discrepancy in a locally motivated divisibility does not imply that Theorem4 is false: extra global and Vandiver assumptions could force an empty sector or a different arithmetic conclusion. This review neither imports that source theorem nor resolves its full operative proof. At the research frontier, the new ladder has no controlled nonzero small linear combination, no leading cyclotomic-unit p-th-root construction at infinity, and no argument against an actual depth-two C solution or nontrivial minus class. Those are unresolved, not defects in the printed ET1--ET3 results.

## 6. Literal source checks and scope

Fresh official source read: [2025 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf), setup59--61/open(b)67--71. Only(b) was investigated.

For [Mihailescu's author-posted chapter](https://www.researchgate.net/profile/Preda-Mihailescu/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren/links/546326840cf2c0c6aec1e13c/Class-Number-Conditions-for-the-Diagonal-Case-of-the-Equation-of-Nagell-and-Ljunggren.pdf), I freshly read the standing equation, signed Theorem3 and Theorem4 statements (PDF58--174), COMPLETE Lemma5 proof/lifts (770--850), surrounding actual setup (851--998), and COMPLETE Section5 (2401--2752), recovering all overlapping gaps. The source imposes actual-solution and Vandiver assumptions. Its last selector and larger divisibility motivate the comparison; ET12 rederives its quantities and covers both reciprocal orientations. I do not certify the source theorem, its external reflection foundations, typography pixels, corrections or final publisher version. The inspected copy dates itself Version2.0, September17,2007, distinct from the 2008 chapter citation. These statements are source-scope context; the trace algebra above is independently reconstructed.

[Bartolome--Mihailescu](https://arxiv.org/pdf/1412.5798): opening0--125 and COMPLETE Theorem2.2 statement230--248 were freshly read. Its signed upper bound agrees with the already attributed GR11 premise. The accessible PDF has an external2015v2 banner and internal2021 date. I did not freshly read its complete proof or Appendix for this audit and import no new assertion from them. The [Chen--Mihailescu2026 DOI](https://doi.org/10.1007/s11401-026-0018-7) returned Internal Error in this audit; its abstract/domain comparison is the constructor's recorded read, not a new external theorem premise or a fresh operative-proof read by me.

FULL current R10 and GR11 accepted bodies and EACH current authority MDJSON were read. A clipped earlier GR11 combined output was not counted complete: its missing entire middle was separately recovered. The GR11 sourceJSON was fully read as a source-boundary record, not a substitute for literal primary reads. The author ENTIRE five-file packet, including its documentary code and all metadata, was read; no constructor self-check was executed or adopted as mathematical evidence.

No binary source was downloaded or hashed, no cache was written, no CUA/native browser was used, and no third-party full paper is redistributed. My fresh text reads do not inherit the constructor's failed screenshots or its prior complete-section reads. Public text extraction may lose conjugation bars; explicit fixed ET12 formulas and both eta choices avoid depending on a visual interpretation. No paid access, subscription, contact or bypass occurred.

## 7. Worklog, preservation and administrative boundary

I confirmed the assigned review prefix unused before writing. Sequence: ENTIREauthor read; exact local trace reconstruction and adversarial endpoints; FULL accepted inputs/EACHauthorities; fresh original text reads and recovery of clipped GR11 material; all36 independent dispositions and closed issue ledger; own documentary script/baseline; FULL final ALL4 payload MODEL readbacks; manifest creation/readback; SEPARATE read-only documentary verification. Completion timestamps/hashes are in the manifest and separate tool result, not evidence for mathematics.

Necessary declared guards appear ONCE in the baseline. The immediate OWN CM16 author manifest is bound compactly by path/bytes/SHA with its existing guard summary; its historical inventory is not expanded or rerun. The released JC15 B parent manifest occurs only as an exact necessary author-declared metadata guard, not as new mathematics. Mutable research maps are not immutable guards. Old R25/IT12/JC15 releases and unrelated CL14 acceptance supply no ET12 premise. No unrelated root exploration was read.

Fresh account-wide telemetry was79% TOTAL on2026-10-19 at02:07:53UTC, reset1792874445, ordinary usage allowed, legacy and limit-id values agreeing. The authorized ceiling is90% TOTAL in that same window with review/integration reserve; no automatic later-window spending. Root owns awake/shared-budget coordination. There was no stalled operation, pending approval or running child in this audit. All old bytes are preserved. This five-file review is an initial audit only; findings remain sealed until explicit BOTH confirmation.
