# 2024 B4 proof register

No full solution has been proposed. The infinite fixed-factor family below is **proved, independently reviewed (partial result)**. Other candidates retain their individual unverified labels.

## Accepted exact whole-phi13 criterion, v1.1

For odd n>=3, phi_13 divides phi_n in F2[x,y,z] **if and only if** n=(64*16^m+1)/5 for an integer m>=0. This criterion is **proved, independently reviewed (partial result)** after two fresh blind full reconstructions. The original polynomial ring converse is included via an injective integral extension and normality; a closed 48-state Cartier automaton proves the complete fixed-divisor language.

See [accepted criterion](notes/zero-automaton-criterion-reviewed-v1.1.md), [frozen v1](notes/zero-automaton-criterion-v1.md), [explicit certificate](notes/zero-automaton-certificate-v1.md), and [coordinator acceptance](reviews/criterion-acceptance.md). The sufficient family below remains accepted as an earlier independent argument. For m>=1 both factors are nonconstant; at m=0 the cofactor is 1. Neither this theorem nor absence of phi13 classifies other factors. The full B4(b) classification and novelty remain unresolved. Later small-divisor probes retain unverified labels.

## Accepted fixed-factor family, v1.1

For every integer m>=0, phi_13 divides phi_n in F2[x,y,z] at n=(64*16^m+1)/5. For m>=1 the factor degrees are 10 and n-13, so both are nonconstant and meet B4(b). At m=0 the cofactor is 1. This is a sufficient family, not a full classification or a novelty claim.

See [accepted proof](proofs/fixed-factor-family-reviewed-v1.1.md), [frozen candidate](proofs/fixed-factor-family-v1.md), and [coordinator acceptance](reviews/family-acceptance.md). Both independent initial audits reconstructed the full argument, including the universal symbolic Cartier identities, localization descent and nonvanishing. The separate exact zero-automaton criterion has its own acceptance record above; its stronger necessary direction was not part of the earlier sufficient-family audit.

Every future proof begins as **candidate proof - unverified**. Distinguish published reproductions from original results. Do not relabel until two independent adversarial audits, a reconstruction and all repairs are complete.

## v0.1: Boundary and invariant lemmas, candidate proof - unverified

All identities here are in F2[x,y,z]. Put w=x+y+z, R=(x+y)(y+z)(z+x), and define Q,D as in research.md.

The elementary symmetric functions of x,y,z,w are 0,Q,R,D. Therefore

    product_{a in {x,y,z,w}} (1+a t)=1+Qt²+Rt³+Dt⁴.

Logarithmic differentiation is valid in the formal power-series ring because the denominator has constant term 1. Its derivative is Rt² (the other terms have even degree), while differentiating the product gives

    sum_a a/(1+a t)=Rt²/(1+Qt²+Rt³+Dt⁴).

Expanding 1/(1+a t) geometrically and multiplying by t gives

    sum_{n>=1} (x^n+y^n+z^n+w^n)t^n
        =Rt³/(1+Qt²+Rt³+Dt⁴).

Coefficient comparison and cancellation of the nonzero R in the integral domain proves

    sum_{n>=3} phi_n t^(n-3)=1/(1+Qt²+Rt³+Dt⁴).

Equivalently, H_0=1, H_j=0 for j<0, and H_j=QH_{j-2}+RH_{j-3}+DH_{j-4}, where phi_n=H_{n-3}. In the geometric expansion, each monomial Q^a R^b D^c in H_j has 2a+3b+4c=j. For odd n, j=n-3 is even, so b is even. This parity argument does not assert anything about individual factors.

The n=1 numerator is zero. Since zero is constant modulo 2 and F2[x,y,z] is an integral domain, two nonconstant polynomials cannot produce the prescribed zero product. The generating identity gives phi_3=1, so n=3 is excluded too. For every odd n>1 the original numerator is nonzero: in its binomial expansion the coefficient of x^(n-1)y is n=1 in F2, and pure terms do not cancel it. Thus the quotient is nonzero and has degree n-3.

## v0.1: finite identity at n205, candidate proof - unverified

The known Hernando--McGuire degree-10 factor, after homogenization, is phi_13=Q^5+QD²+R²D. This identification and phi_205=phi_13 B are checked by the exact script and certificate in computations/. The coefficient arrays in n205-certificate.json specify B completely. A reviewer can check multiplication over F2 without needing any irreducibility theorem or factorization oracle. This is an attributed published counterexample with an independently reproducible finite certificate, not a new solution to B4(b).

No proof based on a bounded scan has been proposed.

## v1: infinite fixed-factor family, candidate proof - unverified

The original v0.1 mathematical bodies above are preserved. A new,
self-contained construction is versioned separately in
`proofs/fixed-factor-family-v1.md`. It proposes

    phi_13 divides phi_((64*16^m+1)/5), for every integer m>=0.

For m>=1 both factors have positive degree, giving a partial family
for B4(b). It does not classify all exponents, claim novelty, or assert
irreducibility of its factors. The known n205 example remains attributed
to Hernando--McGuire. Férard's 2014 original abstract announces a related
divisibility result and an infinite family; the full theorem has not yet
been accessible, so exact prior-family attribution remains pending.

The candidate is supported by exact symbolic Laurent-polynomial identities
in `computations/cartier_family_certificate_v1.py` and
`computations/cartier-family-certificate-v1.json`. Its unrestricted claim
rests on a coefficient-selection span induction plus prime-ideal descent,
not on the finite checks at n=13,205,3277. A frozen hash manifest records the
versions queued for two fresh independent adversarial audits. The
coordinator and this owner are constructors and cannot supply those audits.
