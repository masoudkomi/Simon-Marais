# DR6 constructor checks: ALL48, not independent review

18October2026UTC. **Candidate proof - unverified.** These hand checks
describe why each obligation was retained. TWO OTHER full auditors must
challenge the WHOLE proof; these are not tests or computational evidence.

| ID | Constructor disposition and exact check |
| --- | --- |
| DR6-01 | CHECKED: actual sector is Phi_p(X)=Y^p, p>=37, degree p-1; official(b) freshly read. |
| DR6-02 | CHECKED: negative X gives (U^p+1)/(U+1)>1, p odd; positive immediate. |
| DR6-03 | CHECKED: p cannot divide both X and X+1; c=absolute distance/p^s and p∤c by definition. |
| DR6-04 | CHECKED: RD3 handles same ordinary sector, both signs/centers and all actual s; used only for higher depths/depth bound/c1. |
| DR6-05 | CHECKED: all5 current accepted bodies and MDJSON read completely; A's earlier reviews are not fresh self-certification. |
| DR6-06 | CHECKED: formal root note is unused; no new Jacobi phase, normal-basis, support or unit assertion. |
| DR6-07 | CHECKED: Phi at0/-1 modp is1 and Y^p≡Y, so Y1modp. |
| DR6-08 | CHECKED: first term p^(h+1)u has unique minimum, middles>=1+2h, lastph>h+1 for oddp. |
| DR6-09 | CHECKED: Phi-1=X times a factor1modp. |
| DR6-10 | CHECKED: (X^(p-1)-1)/(X²-1) has residue(p-1)/2≠0; X,X-1 p-units. |
| DR6-11 | CHECKED: s=h+1>=2 and distance>=p² implies U>=p²-1. |
| DR6-12 | CHECKED: j2 binomial term contains p³; intermediate terms at leastp^(j+1); lastp^p has exponent>=3. |
| DR6-13 | CHECKED: Phi(X)=1+epsilon*c*p² modp³ gives k≡epsilon*c. |
| DR6-14 | CHECKED: p-1 alternating derivative terms pair to-1,(p-1)/2 times. |
| DR6-15 | CHECKED: shifted integer polynomial has integer Taylor coefficients; T² has p^4 factor. |
| DR6-16 | CHECKED: multiply congruence by2 before cancelling p², so 2k≡epsilon*c. Odd c remains legitimate. |
| DR6-17 | CHECKED: sign(X)=epsilon in neighboring case because cp²>1; U=cp²-epsilon. |
| DR6-18 | CHECKED: triangle sum strictly below U^p/(U-1), both signs. |
| DR6-19 | CHECKED: binomial coefficients/(p-1)^j<=1/j!, factorial tail<1, multiplier<=3/2. |
| DR6-20 | CHECKED: 1/(U-1)<=1/5<(1-1/p)^p; hence strict lower gap. |
| DR6-21 | CHECKED: for negative X, U/(U+1)>1-1/U>=(1-1/U)^(p-1). |
| DR6-22 | CHECKED: Y>(U-1)^(1-1/p), and exact exponential inequality gives both additive1 and logU/p. |
| DR6-23 | CHECKED: actual Y integer makes Delta integer; positivity is proved, not read from residues. |
| DR6-24 | CHECKED: substitute Y=cp²-Delta in Y≡1+epsilon*cp modp². |
| DR6-25 | CHECKED: negative-sign multiple is Delta-cp+1>1 by gap. |
| DR6-26 | CHECKED: substitute U=cp²-epsilon into2(Y-1); obtain2Delta+epsilon*cp+2epsilon+2. |
| DR6-27 | CHECKED: negative neighboring sign gives Delta>cp+1/p, so2Delta-cp>0. |
| DR6-28 | CHECKED: both positive multiples are at leastp²; center0 bound is stronger than the common one. |
| DR6-29 | CHECKED: target threshold<p since denominator>1, so c>=p already suffices. |
| DR6-30 | CHECKED: c<=p-1 implies U<=p³-p²+1<p³. |
| DR6-31 | CHECKED: two gap constants1 contribute2 and table contributes4; log term adds6logp/p; all sum<12. |
| DR6-32 | CHECKED: p²-12>p(p-1) because p>12; positive denominator preserves strict sign. |
| DR6-33 | CHECKED: RD c>p^(s-2)>=p for s>=3, independent of cofactor growth. |
| DR6-34 | CHECKED: published prime ell1modp dividing X must divide c; ell≥2p+1. Context stronger at center0 only. |
| DR6-35 | CHECKED: c<=C gives p<6C logp+C+1<8C logp, using C>=1,logp>1. |
| DR6-36 | CHECKED: at x0=16C log16C,8C logx0<x0; increasing x/logx on x>e yields p<x0. |
| DR6-37 | CHECKED: RD's strict p^(s-2)<c<=C yields strict s<2+logC/logp. C1 consequently has no actual depth. |
| DR6-38 | CHECKED: finite p,s,c,center,sign specify all candidateX; no mathematical scan or list was executed. |
| DR6-39 | CHECKED: for displayed C, c=C/p^v_pC and s=a+v_pC; c<=C retained. |
| DR6-40 | CHECKED: c2 with p>=37 is p-free; s1 fails section1, s>=3 fails RD. |
| DR6-41 | CHECKED: U<=2p²+1, double upper gap and table yield exact constants2p+6 and4p+2/p. |
| DR6-42 | CHECKED: F'=1+6/p²+4log(3p²)/p³-8/p-4/p³>0 via p²(p-8)>4. |
| DR6-43 | CHECKED: exact sum j0..4 at9/8 is300993/98304, greater than3; exponential has more positive terms. |
| DR6-44 | CHECKED: terms j2..6 at15/4 exceed7,35/4,8,6,7/2 respectively; total including j0/1 is38. |
| DR6-45 | CHECKED: 35-6/37>174/5; coefficient<401/100; log<69/8; product27669/800<173/5. |
| DR6-46 | CHECKED: monotonicF rules out all realp>=37 at c2/s2; together with other depths gives all4 families, not finite samples. |
| DR6-47 | CHECKED: strong original lower-bound passage assumes real class condition;2026 theorem distinctprimes, unused. No full foundations audit claimed. |
| DR6-48 | CHECKED: unbounded c remains; no actual formal-lift construction, annual answer, novelty, code/scan/CAS/replay or old-byte edit. |

Boundary challenges: known p3,X=-19 is outside the cutoff and shows
why the neighboring cofactor2 conclusion must not be extended without
a new proof. Negative multiples in the lattice were separately addressed;
an arbitrary negative representative would invalidate the step. Both
odd/even c and coefficients divisible by p in a displayed family were
checked symbolically with the exact normalized c,s. The only finite
numerical inequalities used are the explicit hand rational certificates
for F(37); no source computation was imported or rerun.
