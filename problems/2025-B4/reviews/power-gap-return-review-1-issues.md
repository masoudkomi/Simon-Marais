# PG1–PG4 R1: per-inference issue ledger

2026-10-17 UTC. Initial whole review completed before any peer PG findings.
Status below is this reviewer's recommendation; only the coordinator promotes.
No substantive defect or required author repair was found.

| ID | Target | Audit and disposition |
|---|---|---|
| PG1R1-01 | Candidate lines 8–14; official domain | Pass. Degree n=m-1; m>=3 for official equations, auxiliary G_2 allowed; only part (b) is researched. |
| PG1R1-02 | C1/C2/C4 accepted scope | Pass. Frozen proof and acceptance read; conjectural classification is not imported. |
| PG1R1-03 | Used C4 factorization/gcd | Pass. Product expansion and divisibility G_s(T)-s by T-1 give the exact gcd for signed x. |
| PG1R1-04 | Used C4 signed roots | Pass. Nonzero coprime factors have valuations divisible by q; odd q restores the sign. No even-q signed-root inference is used. |
| PG1R1-05 | Used C2 odd-prime LTE | Pass. q odd prime, q|(x-1), q does not divide x, positive m and nonzero integers; negative x is allowed. |
| PG1R1-06 | PG1 positive tail, lines 24–30 | Pass. Finite nonempty positive tail is strictly bounded by the infinite descending geometric series, including s=2. |
| PG1R1-07 | PG1 ratio, lines 31–39 | Pass. Exact exponent difference is s-q-1; q(1-2^(-q))>=3/2. No unproved asymptotic estimate. |
| PG1R1-08 | PG1 positive interval, lines 41–43 | Pass. Tail is smaller than the next binomial gap; absolute roots cover even q and both signs of t. |
| PG1R1-09 | PG1 alternating sign/tail, lines 45–53 | Pass. Closed geometric formula gives sign; D_d=u^d-D_(d-1) gives 0<D_d<=u^d, strict for d>=1. |
| PG1R1-10 | PG1 lower gap, lines 55–63 | Pass. B>1 and q>1 give strict gap>B^(q-1); s<=q+1 is exactly the exponent comparison. |
| PG1R1-11 | PG1 signed conclusion/endpoints | Pass. Odd q permits either sign of the sum; s=2, s=q+1, a=2 and q=2 checked by the proof, without enumeration. |
| PG1R1-12 | PG2 coprime branch, lines 76–84 | Pass. Both geometric factors nonzero; signed B is excluded by PG1(t=x). |
| PG1R1-13 | PG2 common-prime necessity, lines 86–89 | Pass. A genuine prime ell divides both A and s; ell cannot divide x, and x=1 mod ell is impossible for ell!=q. |
| PG1R1-14 | PG2 exact order, lines 89–91 | Pass. Order divides prime q and is not 1, so equals q; no composite-q generalization asserted. |
| PG1R1-15 | PG2 ell bound, lines 91–96 | Pass. ell=2 impossible; ell-1 is an even multiple of odd q, so ell>=2q+1>s. Remaining q|s forces s=q. |
| PG1R1-16 | PG2 Frobenius residue, lines 96–101 | Pass. Polynomial cancellation in F_q[X], followed by evaluation, includes x=1 without division by its residue. |
| PG1R1-17 | PG2 valuation contradiction, lines 101–111 | Pass. v_q(G_(q^2))=2 is incompatible with q>=3; negative y and x covered, m=q examples outside scope. |
| PG1R1-18 | PG3 last-block gcd, lines 122–126 | Pass. Correct r=q^(a-1), s=q, factors and exact gcd. |
| PG1R1-19 | PG3 non-1 residue, lines 128–133 | Pass. Iterated Frobenius gives G_r(X)=(X-1)^(r-1), so q does not divide A and gcd is 1. |
| PG1R1-20 | PG3 PG1 substitution, lines 134–138 | Pass. t=x^(q^(a-2)) is integral with absolute value >=2 for a>=2; t^q=x^(q^(a-1)), and s=q is allowed. |
| PG1R1-21 | PG3 necessary restrictions, lines 139–145 | Pass. Signed LTE forces q|a once x=1 mod q. No sufficiency or elementary exclusion of a=q,2q,... is inferred. |
| PG1R1-22 | Positive-base overlap, lines 154–162; source note 17–30 | Pass. Primary 2007 Theorem 1 inspected with its known exceptions and positive x,y domain. No negative-base application. |
| PG1R1-23 | PG4 external domain, source note 32–46 | Pass as attributed input. Primary signed Equation (1), complete Proposition 1 and Theorem 1 inspected; source n is project m. |
| PG1R1-24 | PG4 full theorem vs elementary fragment | Pass with retained dependency boundary. Printed p.17 exceptional case is resolved by the source's reference [10]; PG4 imports the whole theorem, not an elementary reconstruction. |
| PG1R1-25 | PG4 magnitude/example qualification, source note 55–57 | Pass. C1 supplies absolute y>1; all four known (m,q) pairs lie outside odd-prime a>=2. |
| PG1R1-26 | PG4 q=3 branch, source note 57–58 | Pass. Least prime divisor of 3^a is 3, contradicting the signed Proposition 1 input. |
| PG1R1-27 | PG4 q>=5 branch, source note 58–62 | Pass. a=Omega(q^a)<=3 conflicts with 2<=a<q and q|a. |
| PG1R1-28 | Scope and nonpremises, both file endings | Pass. No full classification, m=q exclusion, novelty, Vandiver assumption or unaudited class-group inference is asserted. |

No open repair requests. The external theorem's proof was not independently
reconstructed; this is an explicit scope limitation of PG4's review, not a
claim that the published theorem is elementary or newly proved here.
