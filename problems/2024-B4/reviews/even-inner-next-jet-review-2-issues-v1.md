# NJ-v2 R2 inference and issue ledger

2026-10-17 UTC. COMPLETE initially blind whole review by
`/root/review_2022_complexity_r2`. All ten constructor obligations are
covered below. Status **checked** means the stated inference was
reconstructed, including its qualifications. No substantive open issue
was identified within NJ1-v2/NJ2-v2; no author repair is requested.
This ledger is not coordinator promotion.

|ID|Constructor obligation / inference|Adversarial reconstruction and disposition|Status|
|---|---|---|---|
|NJR2-01|O1: official coefficient and factor domains|The official positive odd-n part(b) is coefficientwise over integer polynomials. Reducing to an F2 polynomial ring preserves the nonconstant requirement. Finite-field functions, absolute factors and APN status are different questions.|checked|
|NJR2-02|O1: exact q,r,s,K,H quantifiers|q=2^k>=4 with integer k; every even r>=2; s>=1; K algebraically closed characteristic2; arbitrary H in K[T]. P0 excluded; odd inner and other decompositions unclaimed.|checked|
|NJR2-03|O1: exact accepted GK recurrence and identity|Reconstructed the two-vector basis with determinant c+1 at a transcendental, full vector coefficients A(c),B(c), odd Frobenius propagation, pairing with the original vector and injective substitution. It is an identity at every specialization, not a finite-point inference.|checked|
|NJR2-04|O1: exact GK degrees and P2 normalization|A,B degrees q,q-1; recurrence leading-degree gap q^(2i)(q+1)>0. Thus P_i monic of degree E_i; first recurrence gives F=T^(q^2+1)+(T+1)^(q^2-q+1).|checked|
|NJR2-05|O2: nonconstant H and smaller s|E_s positive and increasing. E_s=(degH)E_r forces nonconstant H and excludes s<r.|checked|
|NJR2-06|O2: s=r has unique H|The degree-one outer map has leading coefficient1 and zero constant because H(P_r)=P_r. This remains valid over an arbitrary characteristic2 coefficient extension.|checked|
|NJR2-07|O2: all odd target indices|q^2+1 divides E_r for even r; the integer residue E_s is1 for odd s. This prevents E_r dividing E_s; no claim that E_r divides E_s iff r divides s is required.|checked|
|NJR2-08|O3: critical roots and distinctness|(T+1)A=T^(q+1)+1; the numerator derivative T^q is nonzero at every root. Remove only the simple root1. The q remaining roots exist in K, are nonzero and different from1.|checked|
|NJR2-09|O3: finite-constant Frobenius identities|alpha^q=alpha^-1, alpha^(q^2)=alpha, u^q=u/alpha and B(alpha)=alpha^-1. Odd powers q^(2i+1) therefore send B(alpha) to alpha. No identity-Frobenius assertion is made on an indeterminate or all K.|checked|
|NJR2-10|O3: F(alpha) and nonzero a|u^(q^2-q+1)=alpha*u, so F(alpha)=alpha. Formal derivatives give A'(alpha)=B'(alpha)=u^(q-2)!=0.|checked|
|NJR2-11|O3: all-index values|Evaluation reduces the exact recurrence to P_(i+2)(alpha)=alpha P_i(alpha); induction gives even alpha^h and odd alpha^(h+1). No characteristic-dependent step count is inserted.|checked|
|NJR2-12|O3: all-index derivatives|All coefficient derivatives vanish as positive 2-power exponents. Differentiate first, evaluate second; initial0,1 give even derivative0 and odd derivative alpha^h!=0.|checked|
|NJR2-13|O4: binary gaps of F|The support bits are {0,2k} and {0,k,...,2k-1}. There is no term of degree2 through q-1. F'=A^q removes the linear term.|checked|
|NJR2-14|O4: exact local order, not only a lower bound|The Z^q coefficient comes only from the second summand, is u^(q^2-2q+1)!=0, and is above the vanished lower coefficients. Thus ord(F-alpha)=q exactly.|checked|
|NJR2-15|O4: common q^5 jet at every even r|Every even recurrence i>=2 has exponent >=q^5, so its error from alpha P_i is divisible by Z^(q^5). Induction gives P_(2h)=alpha^(h-1)F modulo that same power, including h1.|checked|
|NJR2-16|O4: beta and repeated-value degeneracies|For r=2h, beta=alpha^h can equal1 or repeat. Nevertheless V=P_r-beta has leading coefficient alpha^(h-1)u^(q^2-2q+1) and orderq. Distinct critical values are unnecessary.|checked|
|NJR2-17|O5: fixed-r indexing|The next recurrence after inner r uses M=q^(2r+1), not the next integer exponent or q^(r+1). The minimum r2 gives M=q^5>1.|checked|
|NJR2-18|O5: error order M|R=A^M P_(r+1)+(B^M-alpha)P_r. Both coefficient factors have zero constant and only positive multiples of M, so ordR>=M. Their linear pre-Frobenius coefficients are a.|checked|
|NJR2-19|O6: first summand at M+1|Because 2M>M+1, only a^M Z^M times the linear coefficient of P_(r+1) contributes. Its value is a^M alpha^h!=0.|checked|
|NJR2-20|O6: second summand at M+1|B(alpha)^M-alpha=0. Its degree-M term would need the linear coefficient of P_r, which is0. No constant or higher Frobenius term supplies M+1, so cancellation is impossible.|checked|
|NJR2-21|O7: all later even recurrences|The next error threshold is q^(2r+5), strictly greater than M+1. Modulo Z^(M+2), each later step is multiplication by alpha. This includes arbitrarily many finite steps without accumulating a lower-order error.|checked|
|NJR2-22|O7: exact surviving coefficient for every even s>r|For t=(s-r-2)/2, c=alpha^(t+1), the error has order>=M and coefficient alpha^t a^M alpha^h at M+1. t0 is allowed; later powers are nonzero, not characteristic-sensitive sums.|checked|
|NJR2-23|O8: zero comparison polynomial|If H-cY is identically zero, its composition has no M+1 coefficient and immediately contradicts the established nonzero one. No undefined order of zero is used.|checked|
|NJR2-24|O8: exact order transfer|For nonzero K_beta, factor (Y-beta)^m W(Y), W(beta)!=0. After substitution W(P_r) is a unit and V has exact orderq, so the order is exactly qm, including inseparable H or zero H'(beta).|checked|
|NJR2-25|O8: allowed expansion and equality endpoint|The bound qm>=M implies m>=N=q^(2r). Thus coefficients below N vanish. The coefficient at N may also vanish, and the proof still applies; no assumption m=N is made.|checked|
|NJR2-26|O9: Frobenius exponent prohibition|N is a positive power of2 greater than1. Every exponent of V^N is divisible by N, while M+1=qN+1 is not. This is an exact polynomial identity with arbitrary K coefficients.|checked|
|NJR2-27|O9: all remaining Taylor terms|For j>=N+1, ordV^j>=q(N+1)=M+q>M+1. Consequently neither large degree nor inseparability of H can supply the forbidden coefficient.|checked|
|NJR2-28|O9: entire NJ1 conclusion|The contradiction excludes all larger even s; degree excludes all smaller or odd s; equality uniquely gives H=T. The argument uses only one root alpha and covers every submitted index.|checked|
|NJR2-29|O10: accepted invariant and CP1 bridge|Reconstructed the translation invariant basis, exact degrees, invertible homogeneous coordinate change and no lost u=0 component; rank-four free cover descends WHOLE division over F2.|checked|
|NJR2-30|O10: CP1 composition equivalence with multiplicities|The monic h-adic expansion proves difference-quotient division iff p=H(h). Canceling the same U+V requires no coprimality, retaining repeated diagonal factors and the unit endpoints of the accepted theorem.|checked|
|NJR2-31|O10: domain of the phi_(L_i) application|For q>=4 and i>=1, L_i is a positive odd integer >=d>=13. L0=1 is auxiliary and is not passed through CP1; all required odd a,b>=3 hypotheses are met.|checked|
|NJR2-32|O10: nonconstant g_d and injective substitution|g_d is monic of degree(d-1)/2>0. Therefore P_s(g_d)=H(P_r(g_d)) implies P_s=H(P_r) over F2, then NJ1 in an algebraic closure gives s=r.|checked|
|NJR2-33|O10: converse and equality cofactor|At s=r division is equality and the cofactor is1. It is not a qualifying two-nonconstant factorization; NJ2 is a whole-divisor classification rather than a new irreducibility test.|checked|
|NJR2-34|Failed-route and source boundaries|Degree alone leaves even targets; coarse CJ alone permits higher multiples. Only the exact next coefficient and exponent gap complete the new inference. DI, APN classification, monodromy and characteristic-zero Ritt are not used.|checked|
|NJR2-35|Official/application scope and small endpoints|q2 lies outside the claimed range; minimum q4,r2 and s=r+2 obey all strict inequalities. NJ2 does not exclude proper components, odd inner r, other exponents or the accepted smaller phi_d factors for s>=2.|checked|
|NJR2-36|Independence, integrity and proof/evidence separation|Whole v2 and exact accepted bodies read before any new NJ peer findings. Earlier GK review role disclosed. Old certificates are metadata-only, no author rerun/math scan. Frozen own chain preserved; hashes are not mathematical evidence.|checked|

## Attempted objections retained as resolved audit records

1. **Critical values may coincide or equal1.** True, but no distinct-value
   count occurs. The exact local order of P_r-beta and one nonzero
   alpha suffice (checks16,24).
2. **The B summand might cancel the next coefficient.** Its only
   eligible contribution uses P_r'(alpha)=0; this is precisely why the
   even-inner hypothesis matters (checks19--20).
3. **Many later even steps could cancel by parity.** Their errors all
   start above M+1; the retained coefficient is multiplied by alpha
   repeatedly, never added to another term at that exponent (21--22).
4. **H could be inseparable or vanish to strictly higher order.** Exact
   factorization gives order multiplication without differentiating H.
   The first permitted Taylor coefficient may be zero (23--27).
5. **Frobenius might be used as an identity on K.** Its identity-period
   property is used only at the finite constants alpha,u. On polynomials
   it raises exponents and coefficients, which is exactly the required
   support argument (9,26).
6. **Whole-phi descent might discard a homogeneous line or repeated
   factor.** CP1 retains full affine degree and cancels the same factor
   in a domain, without a coprimality requirement (29--32).
7. **A negative composition result could be mistaken for irreducibility.**
   The stated NJ2 and this review retain the fixed-family, whole-divisor,
   even-inner qualifications; the accepted smaller phi_d remains (33,35).

None of these resolved concerns is an author repair request. No
counterexample was found in the submitted domain. The ledger leaves
general odd inner indices, other decompositions and the complete
official factorization problem open.
