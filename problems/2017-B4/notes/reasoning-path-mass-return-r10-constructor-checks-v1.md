# R10 separate constructor hand dispositions — ALL60

2026-10-18 UTC. Candidate proof - unverified. These are constructor checks,
not independent audits. No mathematical program or finite enumeration was run.
Every row corresponds to exactly one obligation in the separate checklist.

O01 — CHECKED. Official B4 lines48–57 and the complete local statement prescribe exactly n>=2 and n^-2 log2 C(n) for the fixed regular unit-sided polygon. Natural logs in the new claims are explicitly converted by ln2.
O02 — CHECKED. The full accepted DC finite dictionary and PM9 current body identify C with reversal commutation classes. Only |i-j|>1 exchanges are permitted; braids alter the class. No new geometric representation theorem is assumed.
O03 — CHECKED. The disjoint class partition of the finite set of words gives W=sum m. The official object is a class; the word count is never relabelled C.
O04 — CHECKED. Initial inversion number0, final N, each adjacent swap changes it by +/-1. Exactly N swaps force every increment+1 and hence minimality.
O05 — CHECKED. Current PM9C supplies C(n)<=H^(N-1), SAME fixed H>1. At n=2 exponent0 agrees with one class; no factor4 or factorial is introduced.
O06 — CHECKED. Only R10E's L comparison uses accepted all-D G2/G3. Its operative definition and final all-integer/D-order passage were read afresh. B's older authorship is not counted as a new audit.
O07 — CHECKED. Empty w_0,w_1 are internal recursion bases. p_2=(1) and all claims about official classes start at2.
O08 — CHECKED. Successive swaps at positions1,2,...,n-1 carry label1 across every higher label; other labels retain their increasing relative order.
O09 — CHECKED. The return swaps n-2,...,1 carry the current rightmost middle label n to the front. The resulting list is n,2,...,n-1,1, including n=2,3.
O10 — CHECKED. Adding1 to indices1,...,n-3 confines the recursion to positions2,...,n-1. Relabelling that increasing interval invokes the induction legitimately.
O11 — CHECKED. Expanding 2n-3+(n²-5n+6)/2 gives (n²-n)/2; auxiliary base lengths0 agree also at2 and3.
O12 — CHECKED. The word both has length N and reaches reversal, so it belongs to the actual reduced-word dictionary; formal syntax alone was not the realization argument.
O13 — CHECKED. Ascending/descending runs turn from n-1 to n-2; every step differs by1. The last outer index1 meets recursive first index2 when nonempty. Shift preserves the induction property.
O14 — CHECKED. A path in the graph of allowed commutations would need an initial adjacent commuting pair. None exists; braid moves are deliberately outside that graph.
O15 — CHECKED. w_2=(1),w_3=(1,2,1). Nothing about the number or complete classification of other singleton classes is inferred.
O16 — CHECKED. Phase t contains positions j in[1,n-1] with j congruent to t modulo2; adjacent such indices differ2. Even phases at n=2 may be empty.
O17 — CHECKED. After a right move from parity t to parity t+1, that position is the left endpoint of the next active edge; after a left move it is the right endpoint. This is a deterministic matching action on every label.
O18 — CHECKED. At an endpoint the edge that would continue outward is absent; after exactly one phase the inward endpoint edge is active. Initial i=n odd is precisely the zero-travel/wait case.
O19 — CHECKED. Odd i uses (n-i)+1+(i-1)=n phases and finishes n-(i-1). Final inward distance i-1 is at most n-1, so no second reflection is needed.
O20 — CHECKED. Even i uses (i-1)+1+(n-i)=n and finishes1+(n-i). The same distance bound excludes a second reflection. There are no labels outside these parity cases.
O21 — CHECKED. n=2a has a layers of each parity and sizes a,a-1. n=2a+1 has2a+1 layers of size a. Both totals are N; reversal implies reducedness by O04.
O22 — CHECKED. All letters within a layer commute pairwise; any layer permutation is obtained by adjacent exchanges of such letters. Applying this separately in every layer stays in one class.
O23 — CHECKED. The known vector of layer lengths slices the full word into fixed segments. Distinct permutation choices differ in one segment, even if a generator appears in another segment.
O24 — CHECKED. Each segment's letters are distinct, so its factorial counts choices without overcount. Products yield both displayed formulas. Cross-layer commuting may add histories, so equality is not asserted.
O25 — CHECKED. For even n>=4, smallest size n/2-1>=n/4; for odd n>=5, size(n-1)/2>=n/4. The lengths still sum exactly N.
O26 — CHECKED. On each interval[k-1,k], ln x<=ln k, giving integral_1^s ln x<=ln(s!). The integral s ln s-s+1 is at least s ln s-s. s=1 is allowed.
O27 — CHECKED. Sum s_t(ln(n/4)-1) gives N(ln n-c0). Counting all length-N strings from n-1 indices bounds every class above by(n-1)^N, whether or not a string is reduced.
O28 — CHECKED. Divide by n² ln n. Both N/n² and ln(n-1)/ln n have the stated limits, while c0/ln n vanishes. No exact extremizer formula is needed.
O29 — CHECKED. Every multiplicity is an integer>=1, a singleton attains1 and the finite set attains its maximum. Thus both endpoints0,D_n belong to the log set.
O30 — CHECKED. Triangle inequality gives D_n<=|x|+|D_n-x|. All log multiplicities lie between the endpoints, so their common midpoint attains the matching bound D_n/2.
O31 — CHECKED. O28 gives normalized minimax coefficient1/4. An O(n²) bound is o(n² ln n), hence also ruled out. The statement quantifies over arbitrary b_n, not a selected normalization.
O32 — CHECKED. The average W/C is well-defined and gives the aggregate identity exactly; knowing its asymptotics is the missing task. Uniform extremal failure does not contradict this identity.
O33 — CHECKED. Each class has m preimages under the uniform word measure, hence Q=m/W. Uniform classes have U=1/C. Both probabilities are strictly positive on the same finite set.
O34 — CHECKED. At R, m=1, so U/Q=(1/C)/(1/W)=W/C. The reciprocal would have the opposite sign and is not used.
O35 — CHECKED. W>=m(O)>=J and ln C<=(N-1)ln H give the lower bound. W<=C(n-1)^N gives the upper. Their normalized leading coefficient is1/2.
O36 — CHECKED. log(Q/U)=log m+constant. The exact oscillation equals D_n. If BOTH directions had uniformly O(n²) log distortion, the oscillation would be O(n²), contradicting O28.
O37 — CHECKED. The event {R_n} may have probabilities tending0 under both measures. Large likelihood ratio on one such event does not prove differing typical events or noncontiguity; those conclusions are explicitly withheld.
O38 — CHECKED. Insert Q=m/W into -sum Q ln Q; use sum Q=1. This proves the finite chain-rule identity directly, with no asymptotic exchange.
O39 — CHECKED. Nonnegativity is termwise. For x>0, ln(1/x)<=1/x-1. With x=CQ, multiplication by Q and summation gives -sum Q ln(CQ)<=1-1=0, hence Ent<=ln C.
O40 — CHECKED. E_Q ln m=ln W-Ent>=ln W-ln C and is at most N ln(n-1). Use the same squeeze as O35. The error allowance O(n²) remains of the official order.
O41 — CHECKED. Swapping positions1,2 first produces2,1,3,4; swapping3,4 first produces1,2,4,3. The generators commute and extend to the same layered reversal class, but the first timed slice differs.
O42 — CHECKED. Positive m permits every real power. Z(0)=C and Z(1)=W exactly, with no 0^0 convention or missing class.
O43 — CHECKED. tau>0 preserves the lower bound on m(O); sum of at most C terms each <=(n-1)^(tau N) gives the upper. Dividing by n² ln n yields tau/2.
O44 — CHECKED. At tau=0, 0<=ln C<=(N-1)ln H and the larger normalization forces limit0. No positive-tau formula requiring division by tau is used.
O45 — CHECKED. For tau<0 each term<=1. The actual singleton contributes1, so log Z is between0 and log C. A positive power inequality is not incorrectly reversed.
O46 — CHECKED. O43–45 cover all fixed real tau. They do not assert uniform convergence in a moving neighborhood of0.
O47 — CHECKED. The normalized pressure kink is max(tau,0)/2. Dividing by n² ln n discards the n² entropy, so neither slope is identified with L. No differentiation-under-limit occurs.
O48 — CHECKED. For nonnegative tau, 1<=m^tau<=exp(tau N ln(n-1)); for nonpositive tau the endpoints reverse. Summing yields both sandwiches. At n=2 all factors equal1.
O49 — CHECKED. Taking logs of O48 yields the absolute finite bound for all real tau with no sign restriction or limit.
O50 — CHECKED. Divide O49 by n²; its upper error<=|tau_n|ln n/2. This tends0 under the stated hypothesis, allowing precisely the separately accepted scalar-limit comparison.
O51 — CHECKED. alpha>ln H>0 is fixed. The ONE O_n term gives log Z/n²>=(alpha/ln n)(N/n²)(ln n-c0), whose right side tends alpha/2.
O52 — CHECKED. PM9 yields L ln2<=ln H/2; alpha>ln H makes the gap strict. This is a separation for the auxiliary partition sum, not an improved bound for C.
O53 — CHECKED. For positive moving tau, the lower term is (N/n²)(tau ln n)(1-c0/ln n); if tau ln n diverges positively so does it. Negative tau has different monotonicity and is excluded from this claim.
O54 — CHECKED. No general finite-alpha pressure limit or iff scale theorem has been proved. Only a sufficient small scale and a specified larger positive-scale counterfamily are claimed.
O55 — CHECKED. Original AHRV uniform law is on full words Omega_n; Dauvergne's theorem statements use that law. Their full deep proofs were not read or imported; the measure formulas here are finite elementary counts.
O56 — CHECKED. Original marked/wiring/insertion sections identify the context. Dallant's Section3 finite construction is not a distribution theorem or a new input; its computational count was not replayed. Section4 proposals remain proposals.
O57 — CHECKED. The failed routes file distinguishes the abstract compatible-path warning, unproved actual multi-strand estimate and typical-family gap. No abstract graph is claimed an actual pseudoline counterexample.
O58 — CHECKED. One enormous class gives only one tiling. Earlier free/balanced and effective-rate limits remain intact. The evaluated pressure deliberately does not determine its n² coefficient.
O59 — CHECKED. New prefix metadata binds necessary accepted files and the immutable R20 parent plus its nine payloads; old historical counts are bound transitively, not copied or represented as fresh mathematical reads. Exact verification counts and digest belong to the generated baseline/validation and separate final read-only verification, not to this hand proof row.
O60 — CHECKED. The NEW admin enforces exclusive-create writes, exact payload/input fingerprints, all60 distinct labels, final model-readback attestation and a separate read-only verify mode. This hand row does not itself attest that future commands have run: final readback/verification timestamps and PASS outputs must accompany handoff. Acceptance still requires TWO OTHER blind WHOLE60 audits and coordinator reconciliation.
