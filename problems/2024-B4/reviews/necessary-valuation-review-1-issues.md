# NV R1: complete inference and issue ledger

2026-10-17 UTC. Frozen with the whole initial report, before new peer NV findings. Reviewer `review_2022_complexity_r2`; nonconstructor. **Open substantive issues: 0. Repair requests: 0.** A pass is scoped to the exact whole-divisor implication and is not promotion.

| ID | Inference challenged | Independent reconstruction / attempted failure | Result | Obligation |
| --- | --- | --- | --- | --- |
| NV-R1-01 | Official domain and conclusion | Part (b) has coefficientwise integer-polynomial factorization. NV concerns one whole divisor over F2, a partial necessary condition only. No replacement by finite-field functions. | Pass | O01/O11 |
| NV-R1-02 | Exact accepted CP1 premise | Full body and scope checked: all odd d,n at least three, whole divisibility iff polynomial composition, including repeated factors. CP2/CP3 not used. | Pass | O01 |
| NV-R1-03 | Degree relation | Nonconstant monic g_j has degree (j−1)/2. Thus deg H=(n−1)/(d−1) is a positive integer. This forces n≥d. | Pass | O02 |
| NV-R1-04 | Two uses of integer divisibility | d−1=q(q−1) yields both s≥k and q−1 dividing n−1. The latter is retained for local constant/linear coefficients. | Pass | O02/O08 |
| NV-R1-05 | G_j derivative at zero | Odd j implies derivative x^(j−1)+(x+1)^(j−1), equal to one at zero for j≥3. No j=1 substitution. | Pass | O03 |
| NV-R1-06 | H value and derivative | Evaluate and differentiate G_n=H(G_d) at zero; both input/output derivatives equal one. Obtain H(1)=H′(1)=1. | Pass | O03 |
| NV-R1-07 | Factor Q is a local unit | Factor H+1 by T+1, differentiate at one to get Q(1)=1. Q(G_d) is nonzero at any point with G_d=1. | Pass | O04 |
| NV-R1-08 | Exact root multiplicity | In F_q[[z]], multiplying by this unit preserves order even if H ramifies elsewhere or either polynomial has repeated roots. | Pass | O04 |
| NV-R1-09 | Existence and properties of α,b | q≥4 gives α outside F2. α,b=α+1 are nonzero, sum to one and have (q−1)st power one. | Pass | O05 |
| NV-R1-10 | Kasami binomial support | d=1+q(q−1) and Frobenius give support degrees iq,iq+1. Through q+1 only 0,1,q,q+1; next 2q exceeds q+1. | Pass | O06 |
| NV-R1-11 | Binomial coefficients | The i=1 coefficient is q−1, odd, hence one in F2. No hidden sign changes occur in characteristic two. | Pass | O06 |
| NV-R1-12 | Constant and linear Kasami coefficients | d≡1 and d−1≡0 modulo q−1 give constant one and linear zero after summing α,b expressions. | Pass | O07 |
| NV-R1-13 | Degree-q coefficient | d−q=(q−1)^2, giving one plus one, hence zero. | Pass | O07 |
| NV-R1-14 | First nonzero Kasami coefficient | d−q−1=q(q−2)≡−1 mod(q−1); inverse sum is (α+b)/(αb)=1/(αb)≠0. Exact order q+1. | Pass | O07 |
| NV-R1-15 | General-n binomial support | n=1+2^s h gives only degrees i2^s,i2^s+1. This is valid without α^(2^s)=α and for every positive odd h. | Pass | O08 |
| NV-R1-16 | Constant and linear cancellation for n | q−1 divides n−1, so constant of G_n is one and linear coefficient zero. Adding one removes constant. | Pass | O08 |
| NV-R1-17 | Larger-order inequality | s>k gives ord≥2^s≥2q>q+1; no nonzero leading coefficient at 2^s is required. | Pass | O09 |
| NV-R1-18 | Finite order | G_n has degree n−1 with leading coefficient one for odd n≥3. Thus G_n+1 is not identically zero. | Pass | O09 |
| NV-R1-19 | Final quantifier | Contradiction excludes every s>k; prior degree comparison excludes s<k. Conclude exactly s=k, for every n in the stated domain. | Pass | O09 |
| NV-R1-20 | q=2 attempted counterexample | Whole φ3 is a unit, and n=5 gives v2(n−1)=2. This is a genuine counterexample only to extending the theorem to k=1, which is explicitly excluded. | Pass; restriction essential | O10 |
| NV-R1-21 | n=d and smallest q | H=T and valuation k cover equality. q=4 leaves all support degrees distinct and α,b available. n=3 is ruled out by degree. | Pass | O02/O05/O10 |
| NV-R1-22 | Whole versus individual factors | CP1 is not inferred from one component or a polynomial-function zero set. Extension-field α is used only to evaluate a genuine polynomial identity. | Pass | O01/O10 |
| NV-R1-23 | Sources, attribution and claim ceiling | Only accepted CP1 and proved local identities are used. No imported MCM/ramification/APN result, full progression necessity, reducibility classification or novelty claim. | Pass | O11 |

No omission requiring author repair was found. Exact-order preservation, rather than a generic separability claim, is the key point. The complete report gives the calculations rather than relying on this ledger's labels. No new peer report, issue list or conclusion was read before this joint freeze.
