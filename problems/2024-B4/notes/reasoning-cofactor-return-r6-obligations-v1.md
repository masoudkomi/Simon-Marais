# R6 entire-proof obligations

18 October 2026 UTC. **Candidate proof — unverified.** These are ALL48
obligations, not a numerical test suite. The constructor's hand resolutions
are exposed so TWO OTHER whole reviewers can reconstruct or reject them.
No row is promoted by the constructor or by an administrative hash check.

| ID | Entire mathematical/source obligation | Constructor resolution / exact location |
|---|---|---|
| R6-01 | Match official positive odd n, coefficientwise identity and open part(b). | Main §0,§6; official page2 B4(b), local statement. No preliminary(a) construction. |
| R6-02 | Distinguish whole absolute irreducibility from an F2-defined component. | Main §0,§6: only the former excludes every ordinary factorization. HM16 is unused. |
| R6-03 | State all new claims as unverified and retain two OTHER whole audits. | Main heading,§7; constructor excluded, no external-validation/priority claim. |
| R6-04 | Preserve unique n=ell*q+1 normalization with q the maximal 2-power. | Main §2: n>=3 odd, i=v2(n-1)>=1, q=2^i, ell odd positive. |
| R6-05 | Give the exact hypotheses of the line-restriction lemma. | Main §1: F=hJ, h irreducible nonlinear, P smooth on h, J(P)!=0, actual tangent and actual gap. |
| R6-06 | Prove the restricted numerator has zero constant and linear coefficients. | Main §1: h(P)=0 and product rule F_grad(P)=J(P)h_grad(P); tangent annihilates linear term. |
| R6-07 | Prove h restricted to this line is not identically zero. | Main §1: zero restriction gives a linear divisor after an invertible affine change, contradicting nonlinear irreducibility. |
| R6-08 | Check zero direction, missing field points and line parameter degeneracy. | Main §1 uses a nonzero vector over the point's field; main §3 chooses it explicitly over infinite K. |
| R6-09 | Transfer the exact order through the complementary factor. | Main §1: J restriction has nonzero constant coefficient and order0; both restrictions are nonzero. |
| R6-10 | Bound that finite order by component degree. | Main §1: nonzero univariate h(P+Tv) has degree<=deg h and zero order>=q. |
| R6-11 | Avoid characteristic-zero tangent/Hessian or Gauss separability hypotheses. | Main §1 proof is only coefficient/order algebra, valid in characteristic2. |
| R6-12 | Show why repeated components or a line cannot be silently admitted in R6A's use. | Main §1,§2; failures preserved separately; generic unit complement is essential. |
| R6-13 | Prove f_n nonzero without sampling. | Main §2: coefficient X^(n-1)Y is n=1 modulo2 for n>1. |
| R6-14 | Compute all THREE homogeneous partials exactly. | Main (2): (X^ell+W^ell)^q and its Y,Z analogues; n odd, q a 2-power. |
| R6-15 | Exclude W=0 in the common gradient zero set. | Main §2: then all X,Y,Z vanish, forbidden in projective space. |
| R6-16 | Prove the projective gradient zero set is finite over K. | Main §2: W=1 leaves at most ell^3 root triples, additionally satisfying X+Y+Z=1. |
| R6-17 | Prove a repeated factor lies in that gradient zero set even for even multiplicity. | Main §2 product rule: multiplicity>=2 leaves h in every partial; even coefficients may vanish but cannot remove the h divisor. |
| R6-18 | Justify that an entire component cannot be a finite set. | Main §2 includes the affine polynomial/root argument over algebraically closed infinite K; lines also infinite. |
| R6-19 | Obtain reducedness over the algebraic closure, not just over F2. | Main §2 factors over K from the outset; f_n and its nonzero quotient phi_n are reduced there. |
| R6-20 | Check homogeneous factor selection and dehomogenization. | Main §3; factors of a homogeneous polynomial are homogeneous; nonlinear h is not Z, dehomogenization has degree<=e. |
| R6-21 | Choose an actual affine point of h outside the common gradient zeros. | Main §3: infinite affine component minus a finite set; no assumed rational point over a prescribed finite field. |
| R6-22 | Infer J(P)!=0 and smoothness of h from the chosen point. | Main (3): grad f_n(P)=J(P)grad h(P) is nonzero. |
| R6-23 | Ensure an affine tangent exists, rather than using only homogeneous nonvanishing. | Main §3 uses Euler with Z=1 and f_n(P)=0 to rule out F_X=F_Y=0. |
| R6-24 | Check the explicit tangent vector in characteristic2. | Main §3: (F_Y,F_X) is nonzero and F_X F_Y+F_Y F_X=0. |
| R6-25 | Establish the entire Taylor coefficient gap on ANY chosen line. | Main (4): (a+cT)^n=(a+cT)(a^q+c^qT^q)^ell; only degrees0,1 precede q. |
| R6-26 | Include a=0, c=0 and constant coordinate/constant W cases. | Main §3: (4) is a polynomial identity with no division; constant cases retain the gap. |
| R6-27 | Apply the gap to all four numerator terms and their sum. | Main §3 gives X,Y,Z=1,W restrictions explicitly; cancellation cannot introduce forbidden powers. |
| R6-28 | Keep the unit transfer on f_n, not an unjustified gap assertion for phi_n or h. | Main §3 invokes R6A with f_n=hJ; the quotient/factor is never assigned f_n's Taylor coefficients. |
| R6-29 | Exclude tangent lines that are entire components, including a different numerator line. | Main §3: h nonlinear; J(P)!=0 excludes every other component through P; nonzero restrictions already proved. |
| R6-30 | Conclude degree>=q for every absolute nonlinear component, with no central-point restriction. | Main R6B includes arbitrary h and arbitrary allowed point P, avoiding all listed singular-point classifications. |
| R6-31 | Check T1's exact odd binary-weight>=3 domain and absolute coefficients. | Main §0,§4; accepted T1 includes arbitrary K-line coefficients; full operative proof freshly read. |
| R6-32 | Derive r<=ell-1 without ignoring multiplicity or requiring common fields. | Main (5): reducedness and degree sum; q>=2, integer r<ell. |
| R6-33 | Pass the absolute-component bound to any actual nonconstant divisor. | Main (6): a divisor contains at least one absolute component of degree>=q. Formal polynomials are not divisors by default. |
| R6-34 | Keep n1, n3, Gold binary-weight2 and q2 endpoints honest. | Main §4: n1 excluded, n3 unit/vacuous, lines not covered by nonlinear bound, q2 gives no whole-sector theorem. |
| R6-35 | Read the exact current R4A accepted body and authority. | Main §0,§5; current accepted MD/JSON, complete proof read; baseline verifies declared accepted-copy fingerprint. |
| R6-36 | Retain EVERY/ACTUAL/over-K/smaller-factor quantifiers and reduced-product correction in R4A. | Main §0 imports exactly 0<e<=N/2, q>=2ell+7 =>e<A; no genus bound on a reducible product is substituted. |
| R6-37 | Show q=Q^k is exactly the maximal 2-power for this family. | Main §5: Q-1 odd, q=2^(sk), so v2(n-1)=sk. |
| R6-38 | Prove binary weight s+1 without a carry or overlap at bit0. | Main §5: ks>=2s>=6; shifted s-bit block and bit0 are disjoint; T1 applies. |
| R6-39 | Check Q>=8 and all strict size comparisons symbolically. | Main (7): Q^2>2Q+5 and A=Q(Q-3)<Q^2<=q. No finite scan. |
| R6-40 | Obtain an actual least-degree absolute factor e<=N/2 under reducibility. | Main §5: at least two positive-degree components of total degree N>0; reducedness already proved. |
| R6-41 | Apply R4A to that same actual factor and get the contradiction. | Main (8) e<A<=q and R6B e>=q; strict A<q gives contradiction. No congruence substitutes for positivity. |
| R6-42 | Keep the main proof independent of the extra R4B grouping/descent hypotheses. | Main §5 imports R4A only; optional R4B presentation checks N>=3A-2 explicitly and is not needed. |
| R6-43 | Translate whole absolute irreducibility to the exact official ordinary polynomial identity. | Main §6: nonconstant reductions would be two positive-degree F2 factors; nonhomogeneous originals are allowed. |
| R6-44 | Retain all s,k and other-family boundaries; do not claim annual closure. | Main §0,§6: only s>=3,k>=2 family; k1/s<3/other ell unresolved here. |
| R6-45 | Treat corrected R5 as a current old result, not a premise or a repaired literal v1. | Sources/worklog bind accepted AUTHORv2/current authority/precision; all historical errors and reviews unchanged. |
| R6-46 | Audit source hypotheses and exact read limits, especially char2 and Férard. | Source audit: hand proof avoids the p>ambient-dimension hypothesis of AS3.1; Férard2017 body remains unread, no theorem/novelty import. |
| R6-47 | Preserve unsuccessful actual routes without promoting a formal-cofactor inference. | Failed-routes file records orbit-only, invariant-ring, derivative-cancellation, and abstract-source failures; none is a hidden premise. |
| R6-48 | Preserve old bytes, compact parent integrity, honest code/budget/settings and full initial blindness. | Freezer validates only bytes/JSON/48 labels; parent bound compactly; no mathematical executable; two OTHER audits mandatory before promotion. |

All48 constructor resolutions are provisional proof checks, not independent
adversarial acceptance. A substantive objection requires a full versioned
author repair and BOTH affected reaudits, preserving this initial packet.
