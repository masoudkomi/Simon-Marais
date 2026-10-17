# Linear-output R2 per-inference issue ledger

2026-10-17 UTC. COMPLETE initially blind whole audit of the exact
17,270byte constructor main, SHA
`b1bec632971326a661a4188135ce23d40f0fdcc6a121197aefe10d2237f6e1fa`.
No new peer linear-output finding was read before this ledger and the
whole report/source record froze. Requested gpt-6.1-sol/max;
effective setting unknown. Reviewer is not a constructor.

All50 checks below pass in the candidate's stated partial scope.
Unresolved substantive issues: **0**. Requested author repairs: **0**.
The author's source/ambiguity/closure limitations remain limitations,
not silently discharged claims. The counterexample in C29--C31 is
to the failed shortcut retained by the author, not to LO1--LO6.

|ID|Claim / constructor obligation|Independent reconstruction or boundary attack|Disposition|
|---|---|---|---|
|LOR2-C01|Official domain / LO01|Distinct unmarked outputs from seed1, alternate added bits by existing-length parity, both ends; only(b). Histories are not words.|Pass|
|LOR2-C02|LO1 / LO01--02|A nonseed odd output has last-added1 at an end, leaving even output; either grammar odd wrapping is conversely legal.|Pass|
|LOR2-C03|LO1 / LO01--02|An even output has last-added0 at an end, leaving odd output; both even productions are conversely legal.|Pass|
|LOR2-C04|LO1 / LO02--03|Only stop is O->1, no empty output; all nonterminal rules add one letter. Both states reachable/productive and two-way dependent.|Pass|
|LOR2-C05|LO2 / LO04|Mandated totals are k zeros/k+1 ones in O_k, k+1 each in E_(k+1). These are used as necessary conditions, not a full membership test.|Pass|
|LOR2-C06|LO2 / LO05|Repeated legal wrap0w1 gives every0^r1^(r+1), including r0, proving odd slice converse.|Pass|
|LOR2-C07|LO2 / LO05|Prepending0 to0^(r-1)1^r gives every even slice word0^r1^r, r>=1, with correct shortest endpoint.|Pass|
|LOR2-C08|LO2 / LO06|Pumping within P initial zeros violates the balance in both exact slices. B regular would imply its odd restriction O regular. No series nonrationality follows.|Pass|
|LOR2-C09|LO2 / LO07|Every finite binary w is a subsequence of alternating emissions from either start; skipped emissions may all go right.|Pass|
|LOR2-C10|LO2 / LO07--08|Chosen left letters stay adjacent before the sole variable. Nonempty completion makes w a proper factor in either terminal-state language.|Pass|
|LOR2-C11|LO3 / LO09|Length-n derivation has exactly n-1 binary orientation choices, then O->1; initial state is selected by n parity. Counts2^(n-1),4^k,2*4^k exact.|Pass|
|LOR2-C12|LO3 / LO10|For(10)^k1 only P/S outer forms fit endpoints, both leave exactly(10)^(k-1)1. Distinct production pairs double multiplicity from seed1.|Pass|
|LOR2-C13|LO3 / LO11|Linear equations give weighted A=z/(1-4z²), E=2z²/(1-4z²), sum z/(1-2z); coefficients count derivations.|Pass|
|LOR2-C14|LO3 / LO11|Actual mean multiplicity root is(2^(n-1)/b_n)^(1/n)->2/lambda>1, using accepted limit and strict bound only.|Pass|
|LOR2-C15|LO1--3 / LO11|O/E are parity-state languages; B is their disjoint union. Ambiguity of this presentation and its mean loss do not establish inherent ambiguity of B.|Pass|
|LOR2-C16|LO4 / LO12|P10w,Q1w0,R0w1,Sw01 are all legal two-move maps and injective on actual distinct odd words.|Pass|
|LOR2-C17|LO4 / LO13|P(u)=Q(v) iff0u=v0 iff u=t0,v=0t; unique t gives exactly I_k intersection words.|Pass|
|LOR2-C18|LO4 / LO13|R(u)=S(v) cancels its terminal1 to the same0u=v0; another intersection of size I_k.|Pass|
|LOR2-C19|LO4 / LO13|P(u)=S(v) is exactly10u=v01; one component determines the other and gives J_k.|Pass|
|LOR2-C20|LO4 / LO13|P/R,Q/R disjoint by first bit; Q/S by last bit. Every triple contains a disjoint pair, so no omitted inclusion-exclusion term.|Pass|
|LOR2-C21|LO4 / LO13--14|Four-image inclusion-exclusion gives4a_k-2I_k-J_k. Even0O/O0 overlap has identical I parametrization, giving2a_k-I_k.|Pass|
|LOR2-C22|LO4 / LO15|At O0={1}, I0=0 and J0=1 from101=101. Initial overlapping fixed decorations cannot be dropped.|Pass|
|LOR2-C23|LO4 / LO15|Only for k>=1 do u=t01,v=10t force a middle word of nonnegative length2k-1. No negative middle length at k0 is introduced.|Pass|
|LOR2-C24|LO5 / LO18|I projects injectively to t0 in O_k; J projects to u and uniquely determines v even at k0. Thus both <=a_k.|Pass|
|LOR2-C25|LO5 / LO16|w->(w01,10w) maps O_k injectively into J_(k+1); delete fixed suffix to recover w.|Pass|
|LOR2-C26|LO5 / LO17|t=10w1 has length2(k+2); t0=Q(R(w)),0t=R(P(w)) lie in O_(k+2), with unique deletion recovery.|Pass|
|LOR2-C27|LO5 / LO18|The fixed-shift lower bounds and a_k upper bounds squeeze both(2k)th roots to lambda. Small zero coefficients do not affect the tail.|Pass|
|LOR2-C28|LO5 / LO18--20|Root formula yields radius1/lambda for A,I,J even with unsupported parity coefficients zero. No lower-entropy overlap hypothesis survives.|Pass|
|LOR2-C29|LO5 / LO19|t01110 is not O2 because any nonseed odd output has outer added1 at an endpoint. This excludes membership without a table.|Pass|
|LOR2-C30|LO5 / LO19|Q(R(R1))=1001110=10t and R(Q(Q1))=0111001=t01 are actual nested legal outputs.|Pass|
|LOR2-C31|LO5 / LO19|The J injection realizes every t in O2; extra t01110 is distinct and outside it, so J3>=a2+1, refuting the attempted closure.|Pass|
|LOR2-C32|LO5 / LO20|Even series has E=2zA-z²I with the displayed exponents and k0 coefficient retained.|Pass|
|LOR2-C33|LO5 / LO20|Odd shift yields(1-4z²)A=z-z³(2I+J); seed z and J0 term both correct.|Pass|
|LOR2-C34|LO5 / LO20|Acceptedlambda<2 puts1/2 strictly inside all three radii. Evaluation gives2I(1/2)+J(1/2)=4 by ordinary analytic substitution.|Pass|
|LOR2-C35|LO5 / LO21|Cancellation of the apparent1/2 pole does not evaluate the actual radius or prove rational/algebraic series; same-entropy overlaps remain unspecified.|Pass|
|LOR2-C36|LO6 / LO22|Greedy embedding of an m-bit word in either alternating phase uses at most2m emissions, so one fixed EVEN block length works for both starts.|Pass|
|LOR2-C37|LO6 / LO22|Fix the selected positions, emit those left and all other positions right: one deterministic orientation block has left projection exactly f.|Pass|
|LOR2-C38|LO6 / LO23|At any interior uTv the block creates ufUv'. Subsequent rewriting only U cannot separate letters of f; earlier context is external.|Pass|
|LOR2-C39|LO6 / LO24|L=2m even makes all aligned block starts share the initial parity state. The forbidden block depends on state alone, not prior output.|Pass|
|LOR2-C40|LO6 / LO24|Each full block permits at most2^L-1 choices; remainder at most2^r. This proves all n>=1, including zero full blocks and seed length1.|Pass|
|LOR2-C41|LO6 / LO24--25|Taking limsup gives beta_m=(2^(2m)-1)^(1/(2m))<2. Its bounded remainder constant also gives the same cumulative-length upper rate.|Pass|
|LOR2-C42|LO6 / LO25|Distinct avoiding words have at least one counted derivation, but a bound below2 is not a generic bound belowlambda for every f. No transfer asserted.|Pass|
|LOR2-C43|Conditional route / LO26|Reduced reachability extends any ambiguity at an auxiliary variable through one fixed context to start ambiguity. Thus all variables are unambiguous under the premise.|Pass|
|LOR2-C44|Conditional route / LO26|Within each production fixed decorations give an injective word map; across productions unambiguity ensures disjoint contributions to each F_i.|Pass|
|LOR2-C45|Conditional route / LO26|Positive terminal length in nonterminal productions gives M(0)=0. Finite formal inverse exists and is rational by determinant/adjugate.|Pass|
|LOR2-C46|Conditional route / LO26|Dropping unambiguity changes the matrix's interpretation to derivation counts, explicitly witnessed by LO3. Existence of another suitable grammar is not assumed.|Pass|
|LOR2-C47|Source hypotheses / LO27|Actual2007 Definitions1.1/1.4 and Theorems1.2/1.5 require the occurrence/ergodicity and unambiguity conditions. The former are checked; the latter fails for this grammar.|Pass|
|LOR2-C48|Source hypotheses / LO27|Section5 defines rightmost-derivation weights, cumulative in length. Exact full rates here also give cumulative rate2; no external unweighted theorem is imported. Soloauthor and dates match primary title page.|Pass|
|LOR2-C49|2005 source / LO27|Primary publisher-indexed abstract and2007's own discussion concern an unambiguous-linear growth alternative. Unread full2005 body supplies no theorem to the candidate.|Pass|
|LOR2-C50|Dependencies and scope / LO28|Complete accepted existence/strict-bound proof reread; no old certificate rerun, no CCL/NR canonical-language premise substituted, no numerical value, annual solution or novelty claim.|Pass|

Every LO01--LO28 constructor obligation appears in the table. No
counterexample was found to a stated new scoped claim. Formal B-union
notation and cumulative/exact source growth conventions were checked
explicitly, so they are not unexamined theorem-transfer assumptions.
Root alone may promote after the other fresh whole audit is reconciled.
