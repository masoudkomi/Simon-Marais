# R8 WHOLE R2: all48 independent inference checks

2026-10-17 UTC. Initially blind WHOLE nonconstructor review. Main report
sections below refer to `reasoning-return-r8-review-2-initial-v1.md`.
These are review findings, not coordinator promotion or self-certification
of C's old accepted R6/R7 inputs.

|ID|Finding and independent reconstruction|Report|
|---|---|---|
|R8-01|Pass. Official all-integer n,q>=2 is distinct from the restricted signed prime diagonal n=p-1,q=p,p>=37,|x|>=2.|1|
|R8-02|Pass as accepted exact diagonal input. y>0 and p not dividing x-1 remain; negative x is retained and boundary x1 is excluded.|1|
|R8-03|Pass. COMPLETE accepted UW/R6/R7 and scopes read. B's UW authorship/root role and C's own R6/R7 authorship are disclosed, not independent recertification.|1,6|
|R8-04|Pass. Direct sigma/F and inverse M_r are consistently distinguished; actual positive sums preserve integer weight/complement and module membership.|1--2|
|R8-05|Pass as exact accepted UW premise on actual S. At least p-4 points, nonzero m1, normalized relation and six-point fibers include zero m3.|1--2|
|R8-06|Pass. Nonconstant nonzero u is invoked ONLY in the complementary branch and on its actual S, with the accepted all-field polynomial proof.|1--2|
|R8-07|Pass. Fixed-anchor ratio substitution produces exactly the quintic P; repeated u-values are handled separately.|2|
|R8-08|Pass. Coefficients35a^4 C5 and then -2400a C3 force both to vanish in a hypothetical zero polynomial; leading4608 then contradicts zero.|2|
|R8-09|Pass. P(a)=0 removes one DISTINCT root from degree<=5; at most four other u-values occur, with zero outside actual nonzero u(S).|2|
|R8-10|Pass. For each fixed tuple/root X, v3 is fixed, hence w=v3/X^3 fixed and at most six SOURCE points. No extra k is multiplied.|2|
|R8-11|Pass. A second u-value makes at most k possible v3 values in the anchor fiber, costing at most6k, not an assumed unconditional u-fiber bound.|2|
|R8-12|Pass. Outside24k plus anchor6k gives30k; these are actual ratio-image values, not pair descriptions.|2|
|R8-13|Pass. Automorphism translates are coefficient permutations. Their positive sum has F0,M1nonzero,0/1/2 coefficients,weightp-1,complement2N.|2|
|R8-14|Pass. Odd M_r action laws give the exact pair ratios and G-invariance. Different tuples imply nonconjugacy; M1 gives freeness. No converse used.|2|
|R8-15|Pass. In the action-zero branch w3,w5 cannot both vanish; every h!=-1 gives theta_h in I_f with nonzero m1(1+h^-1).|2|
|R8-16|Pass. The polynomial has forced root-1 and is not identically zero by constant/linear comparison. Division bounds every fiber by r-1 even at b0 or leading cancellation.|2|
|R8-17|Pass. Both branches give the exact ceiling q_p; p>=101 ensures at least4. No small-prime computation or sharp threshold claim.|2|
|R8-18|Pass. Half-sets remove j duplicates within free orbits; distinct orbits separate the rest. Canonical coefficients0/1/2 are distinct modulo p.|3|
|R8-19|Pass relative to accepted R6 A1/classical matched-prime input. Actual normalized beta are integral in the signed e0 sector; fraction-before-positive-ideal distinction retained.|1,3|
|R8-20|Pass. Actual k_v(a), oddness and R7 residual domain are used; no purity, kernel invariance or coefficientwise phase reduction assumed.|3|
|R8-21|Pass. Pullback gives Q+jQ with transported ell and tau; its real Kplus-linear system differs from the stronger complex K-linear one.|3|
|R8-22|Pass. tau_-a=tau_a and realness leave m rows per order. B is a common positive REAL scalar in separate embedding equalities, not Galois-acted on.|3|
|R8-23|Pass. Product binomial expansion times p^k k! is an integral multinomial expression at every k. No modular factorial division.|3|
|R8-24|Pass. Positive total exponent(p-1)/p<1 bounds each coefficient under every embedding by1 via the negative-binomial majorant.|3|
|R8-25|Pass. 1,zeta is a field basis over Kplus. A nonzero real-coordinate vector cannot make all ell zero; produced ell are integral.|3|
|R8-26|Pass. The two displayed row entries are exactly the coefficients of a_v,b_v; each is real integral with all-conjugate bound2p^k k!.|3|
|R8-27|Pass. Dimension is counted over Kplus:2q_p m>sm for the entire stated s range, including s1 and maximal2q_p-1.|3|
|R8-28|Pass. Independent actual rows and a regular r-minor produce a signed cofactor kernel on r+1 columns. Row-span dependence handles every omitted row; r0 unit convention safe.|3|
|R8-29|Pass. Hadamard under EVERY embedding gives C_s uniformly in actual phase/x; no determinant lower bound or numerical rank is assumed.|3|
|R8-30|Pass. At mostr+1 REAL coordinates contribute, so the sum of all |sigma ell| is <=A_s even when a,b share one column.|3|
|R8-31|Pass. At s2 the at-mostm first rows and r<=2m give the sharper[2(p-1)]^(p-1) cofactor bound and A2=pC2.|3|
|R8-32|Pass. H is the identity real trace with Kplus coefficients and vanishing orders<s. Other actual phase-row series are not declared conjugates of H.|4|
|R8-33|Pass. Individual branch-point loops multiply each canonical radical by its literal coefficient character; distinct vectors modulo p separate these characters.|4|
|R8-34|Pass. Continuing an analytic GERM identity and finite character averaging isolate each coefficient. No evaluated equality is transported and constants remain fixed.|4|
|R8-35|Pass. Nonzero ell and distinct theta/jtheta make formal H nonzero. Arithmetic delta nonvanishing is NOT inferred.|4--5|
|R8-36|Pass. D=1+...+T^(p-1), logarithmic numerator R_v and differentiated recurrence for P_vk are exact with denominator p^k D^k.|4|
|R8-37|Pass. Every recurrence step adds at most p-2 to numerator degree; determinant degree is the row-bound sum, with cancellation only lowering it.|4|
|R8-38|Pass. Analytic constant-independence gives finite Taylor elimination with distinct initial orders; falling-factorial Vandermonde proves Wronskian nonzero.|4|
|R8-39|Pass. D(0)=f_v(0)=1 are units, so the Wronskian order is at most the nonzero polynomial numerator degree.|4|
|R8-40|Pass. Column replacement by H gives order>=t-(N-1) when t>=N-1; smaller t immediate. Active real support bounds N<=2(R_s+1).|4|
|R8-41|Pass. rho_t=p^t t!h_t is nonzero in O_Kplus; its conjugate bound uses only A_s and the canonical coefficient majorant, not phase-row covariance.|4|
|R8-42|Pass. The coefficient norm has real degree m and yields precisely(p^t t!)^-1 H_t^(-(m-1)); it is not a norm of evaluated delta.|4|
|R8-43|Pass. Each embedding uses its OWN actual canceled row; the remaining geometric tail is <=4A_s B/|x|^s at |x|>=2.|5|
|R8-44|Pass. Nonzero evaluated delta has an integer real norm and gives exponent p/[p(s-1)+1], positive also at s1.|5|
|R8-45|Pass. Delta0 leaves nonzero formal h_t; tail plus its coefficient norm yields2H_t^m and the stated full factorial/T_s cost.|5|
|R8-46|Pass. Negative T,|x|2, arbitrary halves,repeated u,zero ratio moments,inactive columns and deficient rank do not alter the arguments.|2--5|
|R8-47|Pass in exact partial scope. No prescribed source target,full phase rank,chi restriction,useful unconditional bound,source refutation,exclusion or annual claim follows.|Verdict,6|
|R8-48|Pass subject to final integrity freeze. Complete primary read scopes and compact accepted/old bindings recorded; no mathcode,scan,CAS,author rerun,Git or shared/old/cache edits.|6; sources/integrity|

All48 substantive obligations were reconstructed; no result is certified
by a constructor self-check or by this ledger without the full report.
