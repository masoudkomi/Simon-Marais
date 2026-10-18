# FR10 ENTIRE WHOLE audit obligations and constructor hand checks

**Candidate proof - unverified.** All64 rows are required of EACH of TWO
OTHER initially blind ENTIRE WHOLE reviewers. The constructor's dispositions
are self-checks, not independent certification or acceptance. A reviewer
must reconstruct the whole actual proof rather than adopting these checks.

| ID | Exact obligation | Constructor hand disposition and location |
|---|---|---|
| 01 | Match official odd-positive n, coefficientwise integer factorization, nonconstant-mod2 domain. | Checked main0,9 against official page2 B4 setup/(b)/definition; the conclusion is only a restricted exclusion. |
| 02 | q is maximal, ell odd>=3, i>=2, d correct. | n-1=ell*q uniquely, d=gcd(ell,q-1); all hypotheses explicit in0. No arbitrary subpower replaces q. |
| 03 | R6C's binary-weight hypothesis really holds. | Odd ell>=3 has at least two bits; shifting by i and adding bit0 makes at least three. Main0. |
| 04 | Positive-degree nonzero quotient and N are correct. | Established quotient phi has degree n-3=ell*q-2>=10; no function-on-F2 interpretation. Main0,9. |
| 05 | Actual reducedness and its scope are legitimate old inputs. | Full R6 body/current MDJSON read; R6B proves reduced numerator/quotient for odd n>=3. Main0,6. |
| 06 | EVERY actual component has degree>=q, rather than a selected central one. | R6C is imported with exact all-component domain; no equal-degree or common-center assumption. Main0,6. |
| 07 | Old authorship is disclosed without counting self-review. | C authored old R6/R7/R8 and reviewed R9; their accepted inputs are not independently recertified here. Main0,9. |
| 08 | Applied local/Bezout theorems hold in characteristic2 with a reducible complement. | Fresh complete operative Fulton proofs/AppendixA; only coprimality, lengths and algebraic degree exactness used. Main0,1,6; source companion. |
| 09 | Local expansion lemma uses a nonzero leading L^q and squarefree next form. | Both are explicit hypotheses of(5); later established at every nonordinary off-diagonal point. Main1,2. |
| 10 | Initial forms of an actual split are powers of the SAME L. | Product of initials is L^q in K[x,y]; unique factorization gives scalar L^u,L^v with positive u+v=q. Main1. |
| 11 | If L does not divide next form, no actual split meets there. | Degree-(q+1) product term is divisible by L^min(u,v), hence by L. Contradiction. Main1. |
| 12 | If L divides the squarefree next form, it occurs exactly once. | Squarefree H means L² does not divide H; no inference from multiplicity alone. Main1. |
| 13 | Actual local orders are necessarily1,q-1. | min(u,v)<=1 from preceding product term, while both are positive; hence min=1 and sum=q. Main1. |
| 14 | Formal smooth branch exists uniquely and has order>=2. | Normalize V_1=x. Successive coefficients of V(h(y),y)=0 have coefficient1; no y-linear term. Main1. |
| 15 | Evaluation gives the required formal quotient. | V=(x-h(y))*unit by difference division and V_x(0)=1; quotient is K[[y]]. Main1. |
| 16 | Formal-length computation equals the polynomial local intersection. | Actual coprime local quotient is finite; a power of its maximal ideal vanishes. Both rings have identical finite truncations and units. Main1; Fulton3.3. |
| 17 | Leading derivative coefficient is nonzero and has order q. | Simple x factor of H gives gamma*x*y^q, gamma!=0; derivative x^q vanishes in characteristic2. Main1. |
| 18 | No other differentiated term cancels gamma*y^q. | On x=h of order>=2, other degree-(q+1) monomials have derivative order>q; all higher forms give order>=q+1. Identically zero h also covered. Main1. |
| 19 | Exact I=q follows, not only a lower bound. | F_x restricted to V equals U*V_x with V_x unit; exact y-order q gives length q via the displayed quotient. Main1. |
| 20 | Units, coordinates and reducible complements do not invalidate the local lemma. | Local orders/length invariant under invertible linear maps/scalars/units. R can be absorbed locally, and no irreducibility of U,V is used. Main1,2. |
| 21 | Every R-unit affine component intersection satisfies F0=F1=0. | phi=UV gives both affine partials zero at a common zero; R unit transfers to f. Main2. |
| 22 | a,b,c are all nonzero. | If c=0, equality of partial powers forces a=b=0, contradicting c=a+b+1; a=0 or b=0 forces c=0 similarly. Main2. |
| 23 | F0 plus F1 really force ell-th roots of unity. | Common ell-th power u, then f(P)=(a+b+c)u^q+1=u^q+1; Frobenius injectivity twice gives u=1. Main2. |
| 24 | The four roots a,b,c,1 are distinct, and converse holds. | R-unit excludes a=1,b=1,a=b; c=a+b+1 makes all remaining pair equalities equivalent. Conditions give both f value and partials zero. Main2. |
| 25 | All missing degrees and q/q+1 Taylor coefficients are exact polynomials. | (a+x)(a^q+x^q)^ell, ell odd, gives no intermediate degrees and coefficients1 at q,q+1. Main2. |
| 26 | Coefficients A,B,C,D,E in(9) have correct exponents. | a^(n-q)=a^(1-q), a^(n-q-1)=a^(-q), and similarly b,c using ell-th roots. Main2. |
| 27 | H_x,H_y have the displayed form. | q even kills x^q derivatives; q+1 odd and the mixed terms yield the two Frobenius-linear expressions. Main2. |
| 28 | The determinant is exactly1/(abc)^q, hence nonzero. | CE+D² has its c^(-2q) terms cancel and numerator (a+b+c)^q=1. Main2. |
| 29 | Nonzero determinant proves squarefree H over K. | A repeated linear factor yields a nonzero common zero of both partials; invertible matrix forbids that. H splits over K. Main2. |
| 30 | FR10A applies to the actual phi split, with no hidden unibranch claim. | Numerator RUV has R(P)unit. If L divides H and both factors occur, the lemma counts q; otherwise intersection0. Main1,2. |
| 31 | A=B=0 is characterized by equal (q-1)-st powers. | Frobenius roots in(9), all a,b,c nonzero; equivalence immediate without finite-field sampling. Main3. |
| 32 | Equal ratios force the normalized a,b,c themselves into F_q. | a=lambda*c,b=mu*c, lambda,mu in F_q*, and (lambda+mu+1)c=1, forcing nonzero denominator and c in F_q. Main3. |
| 33 | Ordinary off-diagonal points are EXACTLY M_d, not only at most. | A=B=0 iff all a,b,c in F_q; intersection with mu_ell is mu_d; H squarefree gives orderq+1. Main3. |
| 34 | Definition M_s counts ordered affine points once. | Ordered (a,b) with c=a+b+1 and four distinct roots; no quotient by S4/Frobenius or projective rescaling. Main3. |
| 35 | The involution bound M_s<=(s-1)(s-3) is valid. | For fixed a!=1, eligible b subset has fixed-point-free involution and lies in odd-size s-2 set; even size<=s-3. Main3. |
| 36 | d=1 and d=3 boundaries do not introduce a negative count. | M1=0 separately; product formula at1 is0. M3=0 by at most three roots/involution. Main3. |
| 37 | Ordinary off-diagonal local cones are coprime for an actual split. | Full H squarefree, so two subproducts have disjoint tangents; Fulton equality gives I=uv. Main3. |
| 38 | Exact integer maximum at order q+1 is q(q+2)/4. | q even, q+1 odd; maximum integer product is floor((q+1)²/4). Main3. |
| 39 | All noncentral R-line zeros have b in mu_ell. | Coefficient of y-1 in f=Rphi gives phi(b,1,1)=(b^ell+1)^q/(b+1)², b!=1. Main4. |
| 40 | Translated denominator forms on that line are correct. | v[(b+1)²+(b+1)v+u²+uv] gives w1,w2,w3 exactly. Main4. |
| 41 | Numerator F_q,F_(q+1) on that line are correct. | Specialize a=b,b_coordinate=1,c=b in(9), retaining u^qv and uv^q coefficients. Main4. |
| 42 | b not in F_q gives multiplicityq-1 with tangent v^(q-1). | b^(1-q)+1 is nonzero, denominator has order1, and b+1!=0. Main4. |
| 43 | The next quotient form really has a nonzero pure u^q term. | w2 times initial quotient is pure v-power; after division by w1 it cannot cancel b^(-q)/(b+1)²*u^q. Main4. |
| 44 | Nonordinary diagonal points contribute ZERO to a split. | If both factors occur their initial cones are v-powers; the next product form would be divisible by v, contradicting row43. Main4. |
| 45 | b in F_q gives exact multiplicityq and displayed tangent form. | Fq vanishes, Fq1 nonzero; divide its single v factor by w1 to obtain(15). Main4. |
| 46 | Its q tangents are distinct. | Partials v^(q-1),u*v^(q-2); at v0 the form is u^q nonzero for u!=0. No repeated linear factor. Main4. |
| 47 | Count and local maximum on the three diagonal lines are correct. | d-1 choices each, disjoint outside center, total3(d-1); each I<=q²/4 by coprime cones. Main4. |
| 48 | Center quotient starts at degreeq-2 with(17). | R=uv(u+v) exactly, numerator starts u^qv+uv^q; cancel only this exact homogeneous factor. Main4. |
| 49 | Center tangent form is squarefree and of the asserted degree. | q-1 odd gives distinct root ratios; remove u=v once; axes absent, leaving q-2 distinct lines. Main4. |
| 50 | Center bound is at most(q-2)²/4 for an arbitrary actual complement. | Local orders add toq-2, cones disjoint as subproducts of full squarefree cone; I=uv. Main4. |
| 51 | Infinity away from R cannot conceal intersections. | Homogeneous f_Z=(X+Y)^(n-1)!=0 on Z0,Runit; at phi0, Rphi_Z=f_Z. Smooth point cannot meet both factors. Main5. |
| 52 | The three R-line vertices at infinity are absent from phi. | Local linear numerator/denominator coincide at(1:0:0) and(1:1:0); coordinate swap gives(0:1:0); quotient value1. Main5. |
| 53 | The complete intersection locus is exhausted. | R-unit affine singularity classification, all diagonal zeros/center, and all infinity points handled separately. No hidden chart or normalization exception. Main2-5. |
| 54 | Least absolute component/full complement form the same actual coprime split. | Homogeneous polynomial has homogeneous absolute components; reducedness makes U,V coprime; V is full complement, possibly reducible. Main6. |
| 55 | Lower bound e(N-e)>=(ell-1)q²-2q is justified. | q<=e<=N/2; difference equals(e-q)(N-e-q)>=0. No equal-size grouping assumption. Main6. |
| 56 | Bezout applies globally with all intersections and no common component. | Field K algebraically closed, homogeneous actual U,V and coprime; Fulton5.3 degree product; infinity explicitly checked. Main6. |
| 57 | Actual budget(20) counts each kind with the correct multiplicity. | Center plus3(d-1) ordinary diagonal plusMell-Md nonordinary plusMd ordinary off-diagonal; ordinary max and exactq local lemma used in correct places. Main6. |
| 58 | Replacement by M bounds has the required direction and sign. | q>0 andq(q-2)/4>0; replace the TWO nonnegative-coefficient counts only after combining the off-diagonal terms. Main6. |
| 59 | Expansion and sign of P are correct and necessary, not sufficient. | Displayed two-line coefficient expansion in(22); reducibility implies lower<=Bactual<=Bupper, hence P<=0; only contrapositive used. Main6. |
| 60 | Entire d=1,q>=ell-1 range follows with strict positivity. | (4ell-5)q-4(ell-2)²>=7ell-11; P>=q(7ell-11)-4>0. Main7. |
| 61 | Entire d=3 range and n13 endpoint are correctly separated. | ell multiple3: ell>=9 gives P>=q(ell-5)-4>0; ell3 gives q²-4q-4, exceptq4, positiveq>=8. Main7. |
| 62 | Both parametric small-gcd families have exact domains and maximal q. | ell=q-2^s-1>=3 odd,d1; ell=q-7>=9 odd,d=gcd(6,q-1)<=3 forq>=16. Main7. |
| 63 | Infinite ell35 family, strict sign and genuine old-scope distinctions are proved. | i=6t+3>=9,d7; P93q²-4308q-4>0 forq>=47. F8 affine coset witnesses NF4/J failure; ord35=12 andgcdi12=3; ell35 nonMersenne andbinaryweight4. Main8, failed routes. |
| 64 | Official conclusion, publication/read limits, eligibility and all remaining gaps remain explicit. | Absolute whole conclusion excludes F2 factors; n1,n3,q2,ell1/P<=0/no converse and annual/priority limits stated. Original Jedlicka/Ferard operative bodies unread; no abstract theorem import, no root degree-gap premise. Main0,9/source/failures. |

No row is supported by a scan or mathematical executable. The independent
auditors should challenge especially rows16-19,32-33,43-44,51-59 and63.
An error there requires a full versioned author repair and BOTH affected
reaudits; it cannot be cured by a coordinator scope summary alone.
