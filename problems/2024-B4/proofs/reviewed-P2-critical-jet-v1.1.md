# Accepted P2-critical-jet: exact coordinator scope

2026-10-17 UTC. **Proved, independently reviewed scoped partial result.**

CJ1 is a NECESSARY congruence for q=2^k>=4,j>=1: if the exact accepted GK polynomials satisfy P_(2j)=H(P2) with H in F2[T], then H(T)=T^(1+(j-1)q^4) modulo A(T)^(q^4), A=T^q+(T+1)^(q-1). The q simple roots alpha of A lie in F_(q^2), are fixed by P2 and have EXACT local order q. The even recurrence has a common q^5 jet at each alpha. Factoring H(Y)-alpha^(j-1)Y transfers multiplicity by q, including zero and inseparable cases. Coprime local powers and monic division descend to the actual F2 polynomial congruence.

Degree forces a hypothetical composition through P2 to have even index. j1 is the identity case. j2 is excluded by the directly rederived 0/1 endpoint obstruction, already recorded earlier. For j>=3 the modulus leaves possible higher-degree multiples: the condition is not sufficient and supplies no complete composition or factorization classification. The powers q^4/q^5 are ordinary exponents and Frobenius is periodic only on the stated finite constants. No finite-field function identity is substituted for a polynomial identity.

Constructor: coordinator root. Fresh initially blind WHOLE nonconstructor reviewers: review_2021_reasoning_j15_r2 and review_2017_coarsening_r1. They covered all6 author obligations with30/6 checks. Their older structural/CP authorship and GK/KC audit roles are disclosed; the exact accepted GK recurrence/degrees are the sole mathematical theorem input. Earlier unverified critical/higher-family notes are context only and every needed local or endpoint step is rederived. Root is NOT an independent reviewer of its own construction. The coordinator read BOTH COMPLETE reports, ALL inference ledgers, BOTH source checks and the complete constructor main/obligations, and reconciled both against the exact accepted GK scope. No substantive issue or required repair remained.

The official target remains B4(b), coefficientwise reduction modulo2 with two nonconstant integer polynomial reductions. No new external APN, component, monodromy or decomposition theorem is imported. No characteristic-zero Ritt argument, mathematical program, CAS, scan, sample, old certificate or author rerun is used. No general sufficiency, indecomposability, arbitrary-factor theorem, full annual answer or novelty is claimed.

The COMPLETE frozen mathematical submission follows as a byte-identical suffix. Its historical unverified label records submission status; this header and acceptance record state the current exact scope.

---

# A necessary high-multiplicity congruence for composition through P2

2026-10-17 UTC. **Candidate proof — unverified.** Root constructor.
This is separate from accepted CP/GK/KC and from the earlier unverified
critical-fixed research note. Two other fresh whole audits are required
before promotion. It classifies no full annual factorization and makes
no novelty claim. No mathematical code, CAS, scan or sample was used.

Fix q=2^k>=4. Use the accepted GK polynomials

    A=T^q+(T+1)^(q-1), B=(T+1)^(q-1),
    P0=1, P1=T,
    P_(r+2)=A^(q^(2r+1))*P_(r+1)+B^(q^(2r+1))*P_r.

Their accepted degrees are E_r=(q^(2r)-1)/(q²-1), r>=1, and

    P2=T^(q²+1)+(T+1)^(q²-q+1).

**Proposed CJ1.** If j>=1 is an integer and H in F2[T] satisfies
P_(2j)=H(P2), then

    H(T) = T^(1+(j-1)q^4) mod A(T)^(q^4).             (CJ)

Here q^4 and q^5 mean ordinary integer powers of q. The modulus has
degree q^5. This is a necessary congruence, not a sufficient composition
criterion. The separately known necessary degree condition for arbitrary
P_s=H(P2) forces s even; CJ studies that even case only.
Indeed E_s=1+q²+...+q^(2s-2) is congruent modulo q²+1 to zero for
even s and to one for odd s, while deg(P2)=q²+1 must divide E_s.

## 1. Critical points and their local multiplicity, reconstructed

(T+1)A=T^(q+1)+1. The numerator has q+1 distinct roots, since its
derivative is T^q and its roots are nonzero. A therefore has precisely
the q simple roots alpha in mu_(q+1) other than1. They lie in F_(q²),
and alpha^q=alpha^-1. Put u=alpha+1, which is nonzero. Then

    u^q=u/alpha,  u^(q²)=u,
    B(alpha)=u^(q-1)=alpha^-1,
    P2(alpha)=alpha²+u^(q²-q+1)
             =alpha²+alpha*u=alpha.

For every integer r>=0 the odd q-Frobenius exponent gives
B(alpha)^(q^(2r+1))=alpha. The other coefficient vanishes at alpha.
The accepted recurrence thus gives P_(r+2)(alpha)=alpha P_r(alpha).

The binary digits of q²+1 are at exponents0,2k, while those of
q²-q+1 are at0,k,k+1,...,2k-1. The characteristic-two identity
(u+Z)^n=product_(i:bit_i(n)=1)(u^(2^i)+Z^(2^i)) consequently has
no terms Z^a with2<=a<q in either summand of P2(alpha+Z).
Its linear coefficient is P2'(alpha)=A(alpha)^q=0. The first
nonzero coefficient is at Z^q and comes only from the second summand:

    P2(alpha+Z)-alpha
      = u^(q²-2q+1) Z^q + terms of higher order.       (1)

Its coefficient is nonzero. The exact local order is q, including
the possibility of later terms of order q+1; no tame ramification
inference is made from the multiplicity of the derivative.

## 2. A longer common local jet of all even-index polynomials

For even r>=2 put N_r=q^(2r+1), so N_r>=q^5. Since A(alpha)=0,
A(T)^N_r is divisible by (T-alpha)^N_r. Frobenius also gives

    B(T)^N_r = B(alpha)^N_r mod (T-alpha)^N_r
             = alpha mod (T-alpha)^N_r.

The recurrence therefore implies, for every even r>=2,

    P_(r+2)(T) = alpha P_r(T) mod (T-alpha)^(q^5).

Starting from P2 and iterating gives for every j>=1

    P_(2j)(T) = alpha^(j-1) P2(T)
                   mod (T-alpha)^(q^5).             (2)

The first step already has threshold q^5; later steps have larger
thresholds, so none reduces it. For j1 the difference is identically
zero and (2) is still valid.

## 3. Transfer the local jet through the ramified polynomial

Assume the stated composition. Set

    K_alpha(Y)=H(Y)-alpha^(j-1)Y.

Equation(2) says K_alpha(P2(T)) is divisible by
(T-alpha)^(q^5). Also P2(alpha)=alpha. If K_alpha is nonzero, its
order of vanishing at alpha is some integer m>=0; factoring
K_alpha(Y)=(Y-alpha)^m V(Y), V(alpha)!=0, and using (1) shows

    ord_alpha K_alpha(P2(T)) = q*m.

This argument uses ordinary polynomial factorization and the exact
local order, with no separability requirement on K_alpha. Thus m>=q^4.
If K_alpha is identically zero, the same divisibility conclusion holds.
For every root alpha of A,

    H(T)-alpha^(j-1)T is divisible by (T-alpha)^(q^4). (3)

Since alpha belongs to F_(q²), alpha^(q^4)=alpha. Frobenius gives
T^(q^4)=alpha mod (T-alpha)^(q^4), whence

    T^(1+(j-1)q^4) = alpha^(j-1)T
                         mod (T-alpha)^(q^4).

Subtracting this from (3) makes H(T)-T^(1+(j-1)q^4) divisible by
each of the pairwise coprime polynomials (T-alpha)^(q^4). Their product
is A(T)^(q^4). This proves the proposed necessary congruence over the
algebraic closure. Its numerator and monic divisor both lie in F2[T],
so ordinary monic division descends the divisibility to F2[T].

## 4. What this does and does not resolve

For j2, the accepted degree formula forces degH=q^4+1. The comparison
monomial has that same degree, smaller than q^5. CJ would force
H=T^(q^4+1). In fact P4 cannot compose through P2 at all: directly
A(0)=B(0)=1 makes P0(0),...,P4(0) equal1,0,1,1,0, while
A(1)=1,B(1)=0 gives P_r(1)=1 for every r>=1. Thus P2(0)=P2(1)=1
but P4(0)!=P4(1). This is the already saved elementary obstruction,
not a newly claimed endpoint exclusion.

For j>=3 the degree of H, if it exists, is

    E_(2j)/E2=1+q^4+...+q^(4j-4),

which can exceed the q^5 modulus degree. CJ then does not force H
to be the comparison monomial, nor rule out a remainder multiple.
It gives many necessary coefficient conditions but no complete
classification. It is not an indecomposability proof for P2, a theorem
about arbitrary factors or individual Kasami components, or a full
criterion for phi_(L2) dividing phi_n. Higher local thresholds might
impose additional conditions, but no compatible all-order argument is
provided here. No characteristic-zero Ritt theorem is imported.

## Source, dependencies and review obligations

The exact recurrence, all-index identity and degrees come only from the
accepted [GK mathematical body](../proofs/reviewed-generalized-Kasami-v1.1.md).
The critical-fixed computation from the earlier research note is fully
reconstructed above, so that unverified note is not an accepted premise.
The earlier [higher-family composition research](coordinator-higher-family-composition-return-v1.md)
supplies context for the already known 0/1 endpoint obstruction.
No new external theorem, paper quotation, download or source import is
used. All full third-party papers remain in ignored local cache.

Both future whole reviewers must reconstruct: (i) exact q distinct
critical roots and P2(alpha)=alpha; (ii) the binary-exponent argument
giving local order EXACTLY q; (iii) every even-index recurrence and its
uniform threshold q^5; (iv) order multiplication q*m including zero
K_alpha and inseparable H; (v) the q^4 monomial congruence and coprime
product descent; (vi) degree/endpoint comparisons and the explicit lack
of a sufficient criterion. Author root cannot supply either independent
review. Administrative file checks would not prove these six steps.
