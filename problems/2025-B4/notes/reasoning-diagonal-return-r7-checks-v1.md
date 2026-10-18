# Constructor hand reconstruction of ALL48

18 October2026UTC. **Candidate proof - unverified.** Every entry records a
completed HAND proof check, not an independent review. No mathematical
program, sample test, table, CAS or old/source executable replay was used.

| ID | Hand disposition and reason |
| --- | --- |
| DR7-01 | Checked. Official degree is one less than the number of terms; this is degree p-1 and exponent p, both ordinary signed variables retained. |
| DR7-02 | Checked. (S) explicitly includes p divides X(X+1). No claim every solution enters it. |
| DR7-03 | Checked. Consecutive integers cannot both be divisible by p; X-a is nonzero since abs(X)>=2. |
| DR7-04 | Checked. For negative X=-U, Phi=(U^p+1)/(U+1)>1; positive sign follows directly. Odd exponent then forces Y>1. |
| DR7-05 | Checked. For positive U, Phi=(U^p-1)/(U-1)<U^p, including U2. For negative sign, 1<U^(p+1) gives the strict bound. |
| DR7-06 | Checked. The derivative of (T-1)Phi=T^p-1 at-1 gives1-2Phi'(-1)=p; derivative at0 is1. |
| DR7-07 | Checked. Phi(X)-1=(X-a)A_a(X); A_a(a) is a p-unit in either case. No higher-term cancellation changes this. |
| DR7-08 | Checked. Y^p=1 modp, and t^p=t in F_p, imply Y1 modp. |
| DR7-09 | Checked. Linear binomial term has order h+1, interior terms at least1+2h, top term ph>h+1 for odd p>=3. Thus s=h+1>=2. |
| DR7-10 | Checked. c is p-free, and Y^p=1 mod every ell dividing c, so Y is nonzero there. |
| DR7-11 | Checked. Order divides the prime p; hence its only possibilities are1,p. |
| DR7-12 | Checked. At Y1 modell, Phi_p(Y)=p modell is a unit since ell!=p; all required valuation is in Y-1. This includes ell2 without a separate LTE formula. |
| DR7-13 | Checked. In orderp, Y-1 is an ell-unit and all c valuation lies in Phi_p(Y). |
| DR7-14 | Checked. These two alternatives are disjoint at each prime and take the whole power in c; therefore both gcd identities and gcd(g,b)=1 follow. |
| DR7-15 | Checked. Order1 is allowed even when ell1 modp; no converse to Lagrange is used. |
| DR7-16 | Checked. Orderp implies p divides ell-1; ell is odd and p odd, so2p divides ell-1. Products of these powers, or the empty product, are1 mod2p. |
| DR7-17 | Checked. At0 the residual polynomial value is1; at-1 its value-K is a unit for ell>=2p+1. Combined with ell not dividing Y-1 this gives equality. |
| DR7-18 | Checked. g divides Y-1 and is coprime to p, so multiply by its exact p-part p^h. Quotient m is a positive p-unit. |
| DR7-19 | Checked. U=p*b*Q at0 and U=p*b*Q-epsilon at-1. The actual integer inequality Y<U gives Y-1<p*b*Q even for epsilon-. |
| DR7-20 | Checked. All coefficients are ordinary integers; the two roots use Phi(a)=1 and the original solution, respectively. |
| DR7-21 | Checked. Coefficient is p(epsilon*b-m) at0 and p(-epsilon*K*b-m) at-1. No m3 trace sign is borrowed. |
| DR7-22 | Checked. Phi degree p-1; only -(1+mT)^p supplies degree p, with nonzero coefficient -m^p. |
| DR7-23 | Checked. For2<=j<=p-1 the Phi term has p^j as a factor and the binomial coefficient is divisible by p. |
| DR7-24 | Checked. The first quadratic summand vanishes modp² and binomial(p,2)/p=K is a p-unit. Thus B2 has EXACT order1. |
| DR7-25 | Checked. In F(Q)/Q, the quadratic term has order1+h. Every degree j>=3 below p has order at least1+(j-1)h>1+h. |
| DR7-26 | Checked. Top order is (p-1)h; subtracting1+h leaves (p-2)h-1>=2 for p>=5. No depth cap is needed. |
| DR7-27 | Checked. There can be no cancellation of that unique least term unless pL has the same order1+h. This also excludes L0. |
| DR7-28 | Checked. F(Q)/Q=pL+Q times an integer; hence Q divides pL in Z. |
| DR7-29 | Checked. Since gcd(g,p)=1, g divides L. Its coprimality with p^h and v_p(L)=h imply g*p^h divides L. |
| DR7-30 | Checked. J is then an actual nonzero integer with p-order0; it is not merely an element of Z_p. |
| DR7-31 | Checked. The first term becomes J, each B_j/p is integral, and Q^(p-2)/p is an integer. |
| DR7-32 | Checked. Its order is (p-2)h-1>=2; at the minimum p5,h1 it is2, still positive. |
| DR7-33 | Checked. Only J+B2/p survives modulo p, yielding J=K*m². |
| DR7-34 | Checked. p divides L, so m=epsilon*b or epsilon*b/2 modp. With b1 modp and K=-1/2, the residues become -1/2,-1/8. All modular halves stay in F_p. |
| DR7-35 | Checked. Substitute m=epsilon*b-JQ or -epsilon*K*b-JQ into Y=1+mQ; X or X+1 is divisible by p. |
| DR7-36 | Checked. Nonzero multiples2J+1 or8J+1 have magnitude at least p. If J<0, the magnitude is2abs(J)-1 or8abs(J)-1, giving the stronger signed lower bound. |
| DR7-37 | Checked. L=b-m is between -(p-1)b and b; abs(L)<(p-1)b and abs(J)>=K give Q<2b. |
| DR7-38 | Checked. L=-b-m<0 has magnitude less than(p+1)b; negative J has magnitude at least(p+1)/2, again Q<2b. |
| DR7-39 | Checked. L=-Kb-m<0 has magnitude less than(3p-1)b/2. Divide by the actual negative-J lower bound(p+1)/8. |
| DR7-40 | Checked. For positive J use L<Kb and J>=(p-1)/8; for negative J use abs(L)<(p+1)b/2 and abs(J)>=(p+1)/8. Both give Q<4b. |
| DR7-41 | Checked. Multiply g*p^h<kappa*b by b, then use gb=c and b<=c. All quantities are positive so strictness persists. |
| DR7-42 | Checked. b1 would give Q>=p>=37 but Q<12. This needs no old c1 exclusion or class-number theorem. |
| DR7-43 | Checked. b>1 supplies an actual prime of its support. Congruence1 mod2p forces ell>=2p+1; b and c are at least that large. |
| DR7-44 | Checked. The excluded family allows unbounded c with arbitrarily many prime powers, provided no prime is1 modp. The quantitative bound also restricts general mixed support. |
| DR7-45 | Checked. Old RD/DR6 are contextual comparisons only; Sections2-6 reconstruct the whole new result from(S). A's DR6 authorship is explicit. |
| DR7-46 | Checked. BMR positive-X hypothesis and Bennett-Levin signed scope are attributed; the neighboring quantitative assertion is hand proved, with no source absence or priority claim. |
| DR7-47 | Checked. Large actual b remains unbounded; no p-adic construction is called ordinary, no all-center/all-exponent or annual conclusion is asserted. |
| DR7-48 | Checked administratively. New prefix only, no peer R20 access, requested/effective distinction and authorized window/reserve retained; independent audits remain required. |
