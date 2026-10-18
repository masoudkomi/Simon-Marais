# R10: constructor's hand checks of ALL64 obligations

Candidate proof - unverified. These are author checks, not either required
OTHER whole audit. Every mathematical disposition remains reviewable.

| ID | Constructor reconstruction/check |
|---|---|
| R10-01 | Official statement was freshly read; p terms gives n=p-1, not n=p. |
| R10-02 | Main restricts to p>=5 and(D); it never eliminates other exponents. |
| R10-03 | For X>1 the sum is >1; for X=-U<-1, Phi_p(X)=(U^p+1)/(U+1)>1. Odd q makes Y positive. |
| R10-04 | Division by6 and the t^3 coefficient require p>=5. No p=3 conclusion. |
| R10-05 | Local endpoints give zeta^2,zeta,-zeta; all are kept. Actual |X|>=2 removes the endpoints only. |
| R10-06 | The class condition is displayed in every global root/cofactor assertion. Local sufficiency is explicitly weaker. |
| R10-07 | Phi_p(1+T) is Eisenstein; pi uniformizer, degree and ramification p-1, residue F_p. |
| R10-08 | zeta^a=1+a*pi mod pi^2 gives all p residue classes exactly once. |
| R10-09 | p*z has valuation e+t; intermediate terms e+k*t, final term p*t; both exceed it for t>=2. |
| R10-10 | Intermediate contraction coefficients have valuation t(k-1)>0; final coefficient has e(t-1)>0. |
| R10-11 | The polynomial is a strict Lipschitz contraction on complete O_L; its fixed point gives the full root. |
| R10-12 | Teichmuller factors of order p-1 have bijective p-th powering; a power in U1 has trivial residue factor. Then U1^p=U2^p. |
| R10-13 | p*v(gamma)=0 for a unit power, so v(gamma)=0 even if gamma was initially fractional. |
| R10-14 | Reducing the monic Eisenstein relation gives t^(p-1)=0; both rings have dimension p-1 over F_p. |
| R10-15 | Every positive t degree becomes at least p under p-th powering, hence vanishes. Residue r=1 makes the remaining constant1. |
| R10-16 | Num=d+(d-1)t-t^2, den=d+x*t. Thus d*a+x=d-1 and d*a=-2. |
| R10-17 | a[d(a-1)/2+x]=a*d/2=-1, the correct left coefficient. |
| R10-18 | d(a-2)+3x=d*a-2(x-1)+3x=x. At p=5, t^3 is still below t^4. |
| R10-19 | Numerator difference is X(zeta-zeta^-1); denominator unit. pi valuation is s*e+1. |
| R10-20 | Numerator difference is (X+1)(1-zeta); denominator at center-1 reduces to-2. |
| R10-21 | Cancel pi first; u-1=-delta(1+zeta)/(pi*(1+delta*zeta/pi)). Denominator unit, valuation s*e-1. |
| R10-22 | Here u=1 mod pi^3, so r=-zeta mod pi^2. The sign is (-1)^p. |
| R10-23 | Depth1 gives p at centers0/-1 and p-2 at center1, below p+1. Depth2 gives2p-1 or2p-3, sufficient for p>=5. |
| R10-24 | Necessity first identifies a residue and then its depth; sufficiency invokes the surjective U2 p-th power map. |
| R10-25 | Nontrivial mu_p lies in U1 outside U2. Only exponents1,2 occur, so exponent0 is impossible. |
| R10-26 | All coefficient arguments assume X integral at p. Main explicitly excludes a general Q_p or binary-fraction conclusion. |
| R10-27 | Generic lemma requires alpha,beta nonzero, coprime, unequal, exponent>=2, B,D integral. |
| R10-28 | At D of exponent d, gamma-1 has valuation-d and the sum has valuation-(r-1)d, with unique least terms. |
| R10-29 | At B gamma has positive valuation, making gamma-1 and its geometric sum units. |
| R10-30 | Elsewhere gamma is a unit and both polynomials are integral. Product identity excludes a zero factor. |
| R10-31 | (gamma^r-1)*D^r=(alpha-beta), with no loss of the beta denominator. |
| R10-32 | A common prime is outside D and has gamma=1, so the second factor reduces to r. |
| R10-33 | Integral I divides the difference. Powers of one principal prime are principal; no claim about arbitrary real representatives. |
| R10-34 | Differences of conjugates are associates of pi. X!=1 modp makes every characteristic factor a pi-unit. |
| R10-35 | In the ideal product(Y)^q a prime occurs in at most one conjugate; its exponent is divisible by q. Norm then gives N(A)=Y. |
| R10-36 | At X=1+p*t, Phi_p(X)=p modp^2. The required p-divisible valuation is1, impossible. |
| R10-37 | Generator b of A/jA has b^q and r with identical ideal; quotient is a genuine global unit, not just norm1. |
| R10-38 | Unit ratio is integral with all moduli1, hence root of unity. Roots in K are mu_(2p); mod P ratio1 removes the minus sign. |
| R10-39 | Raising (b/jb)^u*r^v to q uses2u+qv=1. Both factors have norm1 under conjugation. |
| R10-40 | mu_p has invertible q-th powering for q!=p. This root is obtained before the principality proof. |
| R10-41 | Forward construction retains a mu_p error; converse takes ideals and uses unique p-th ideal roots. |
| R10-42 | Source defines hminus as the quotient size. A q-torsion class has zero image if q is coprime to that size; lifted real classes are fixed. |
| R10-43 | Apply R10B to alpha-jalpha, whose ideal is P to exponent1. I is P^0 or P^1, so A is principal. |
| R10-44 | An integral generator exists because A is integral. Solve2qt=b0 modp to make its residual unit fixed by conjugation. |
| R10-45 | At k1 the constants cancel; at2k1 modp, zeta^(1-k)=zeta^k and zeta^(k-1)=zeta^-k. Difference is(X+1)pi_k. |
| R10-46 | All p roots differ by mu_p; exactly one belongs to U2. This normalization preserves their p-th powers. |
| R10-47 | v(gamma^p-1)=s*e+1 by the exact normalized ratio; p-th powering in U2 subtracts exactly e. |
| R10-48 | Product difference has valuation s*e+1; subtracting(s-1)e+1 leaves e for H0. |
| R10-49 | Removing pi_k p^(s-1) and p removes EXACT P valuations and no other prime valuations. |
| R10-50 | Common primes before division can only lie over p; after division both ideals are p-free. Product is(sign*c)=(c). |
| R10-51 | [I]=[jA]; [H0]=[jA]^(p-1). Removed factors are principal. Nontrivial p-torsion is retained. |
| R10-52 | j(gamma-1)=-(gamma-1)/gamma, and (gamma)^-1*A=jA. Their ideals cancel exactly. |
| R10-53 | The conjugated sum is gamma^[-(p-1)] times itself; this cancels A^(p-1) against(jA)^(p-1). |
| R10-54 | Cyclotomic discriminant is a p-power. At every other real prime, invariant split pairs or inert primes are extensions with unchanged exponents. |
| R10-55 | The normalized root of the fixed ratio is unique, so arbitrary generator/Bezout choices give the same I,J,H. |
| R10-56 | gamma*jgamma=1 implies all complex moduli1. No embedding can equal-1 unless gamma=-1, excluded by residue1. |
| R10-57 | Norm(pi_k)=p and Norm(p^(s-1))=p^[(s-1)e]. Positive integral ideal norm>=1 gives the strict lower bound. |
| R10-58 | Classes in(4) are nontrivial inverses if[A]!=1. A principal real ideal would have principal extension. |
| R10-59 | Frobenius in F_p^times/{+/-1} gives real-prime norms +/-1 modp; a positive nonunit norm is>=p-1. Full-field norm is its square. |
| R10-60 | A real ideal supported at principal primes is principal. An inert rational prime has the single real prime(ell), so the stated implication follows. |
| R10-61 | Complete primary paper read in returned web-text windows. Actual theorem assumes distinct primes and retains p<29,x<0 exception. No exclusion theorem imported. |
| R10-62 | DR8 uses actual ordinary gcds/unitary factors, which are not identified with J,H. Its upper-support gap survives. |
| R10-63 | No existence from local roots; no global(C) from local roots; no useful new height/prime exclusion or full annual conclusion. |
| R10-64 | No mathematical program or search. Only new documentation/integrity code; all old guarded bytes checked, C constructor excluded from TWO OTHER reviews. |
