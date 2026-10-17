# Initially blind WHOLE sector3 review R2

2026-10-17 UTC. **Independent nonconstructor recommendation, not project promotion.** I reconstructed the entire submitted S3A--S3D argument and checked all 36 constructor obligations. I found no substantive defect in the stated scope. No author mathematical repair is requested. This is an audit of a scoped partial result, not a solution of the remaining ordinary reducibility problem.

The immutable target is `notes/reasoning-sector3-return-r1-candidate-v1.md`, 17157 bytes, SHA256 `e8ca03cd139df7dcbe7508ad4c701e66d220a177c58ea01f8fac23a1788edd6a`. Its constructor freeze is 3893 bytes, SHA256 `2a3cf9ce9d04b92f42a03e0847a478c6b3402e4eadf7067cb2addf4f97055be2`. I read the complete ten-file packet, including all proofs, obligations, failures, source/read-scope records, worklog and administrative freeze code; I did not execute that code.

I am `/root/review_2021_reasoning_j15_r2` (A). I previously constructed accepted T1--T4/C7/C11 and IC1--IC4, and reviewed several older CP/GK/KC/CJ/DI/CS/NJ/HR packets. Those roles are disclosed, not counted as fresh independent recertification of my earlier work. I did not construct or contribute to NEW S3A--S3D. C and root are contributors to this packet and are excluded from its two-independent-reviewer count. I have read no new B sector3 review, ledger, source file, manifest or finding. This complete initial report and its companion ledger/source/integrity records are being frozen before any peer comparison. Requested inherited settings are gpt-6.1-sol/max; independently verified effective readback is unavailable.

## 1. Exact domain and what the conclusion does

The official problem asks for coefficientwise congruence modulo 2 and TWO positive-degree factors. Thus the relevant object is ordinary reducibility of the established quotient `phi_n=f_n/R` in F2[X,Y,Z], not a relation of polynomial functions on F2-points and not splitting only after extending the field. I read the actual official B4(b) statement. I use existence of the quotient as an attributed accepted preliminary input and do not reproduce a preliminary solution.

For odd n>=3, phi_n is nonzero homogeneous of degree n-3. At n=1 the numerator is zero, which cannot be R times two nonzero positive-degree polynomials in a domain. At n=3 the quotient is 1. Neither qualifies. All S3B--S3D claims start at n=3 and never divide by the zero n=1 polynomial. A proper F2 factorization would lift coefficientwise to the official integer form, but this submission constructs no new such family.

The exact reviewed conclusions are:

- S3A: the attributed published WHOLE absolute irreducibility of phi_m for every m>3, m=3 mod 4, with a full supplied reconstruction. This excludes that sector from ordinary F2 reducibility.
- S3B: the stated two-case diagonal local germ for every odd target n>=3.
- S3C: for every such sector base m and every odd n>=3, a common absolute component forces n=m. Consequently the gcd is the whole phi_m at equality and 1 otherwise, over K=algebraic closure of F2 and over F2.
- S3D: the corresponding finite homogeneous-sum assertion, including the zero sum and coefficients in K.

The necessary remaining sector n>=5, n=1 mod 4 is not classified. Whole divisibility by itself, including the equality case, need not supply two positive-degree factors. No numerical search, old certificate or APN classification is part of the proof below.

## 2. Source theorem and the local factor lemma

I visually read the existing original McGuire thesis pages 7,12--15,18,20--25 (PDF page numbering), including the COMPLETE operative proof of Theorem 2.1' on printed pages 19--20 and the COMPLETE Proposition A proof on printed pages 9--10. The theorem actually gives the whole affine quotient for all t>3 congruent to 3 modulo 4, not just a component, and has no additional prime or coding premise. Printed page 2 explicitly identifies the joint Janwa--McGuire--Wilson journal content. The original journal full PDF remains unread; that limitation is retained. The supplied homogeneous reconstruction is independently checked below, so a terse source infinity comment is not doing unproved work.

The local lemma used twice is valid for every d>=1. If T has initial term cL^d and next homogeneous term not divisible by L, a hypothetical T=UV with U(0)=V(0)=0 has positive orders a,b with a+b=d. Unique factorization of the initial forms forces U_a=c1 L^a and V_b=c2 L^b. The degree d+1 term is U_a V_(b+1)+U_(a+1) V_b, hence divisible by L, a contradiction. For d=1 the two positive orders already contradict a+b=1. Therefore any factor through the point has a nonvanishing cofactor and exactly the full local order d. This is a statement about actual polynomial factors/local units and suffices; no stronger analytic unibranch theorem is silently invoked.

I also checked the actual Hernando--McGuire statements. Their conditional WHOLE theorem assumes ordinary irreducibility and the stated arithmetic case; their component theorem concludes existence of an absolutely irreducible F2 factor. The false general whole-polynomial conjecture is not used. Delgado--Janwa's selected-family coprimality lemma is contextual; it does not replace the new arbitrary-target proof. These read limits and attribution match the packet.

## 3. Whole reconstruction of S3A

Write m=2ell+1>3 with ell>=3 odd, f=f_m(x,y,1), w=(x+1)(y+1)(x+y), and g=phi_m(x,y,1). If g=g_x=g_y=0 at P=(alpha,beta), f=w g and the product rule imply f=f_x=f_y=0 even when w(P)=0. No division by w is used here.

Put lambda=alpha+beta+1. The first partials give alpha^(2ell)=beta^(2ell)=lambda^(2ell). Squaring is injective in K, so their ell-th powers have a common value u. The equation f(P)=0 reduces to `(alpha+beta+lambda)u^2+1=u^2+1=0`. Thus u=1, proving that alpha,beta,lambda are nonzero ell-th roots. Nonzero coordinates are a conclusion, not a hypothesis.

Both binomial coefficients (m choose 2) and (m choose 3) are odd since the last two binary digits of m are 11. Substitution of the root equations gives exactly the displayed F2 and F3 terms. I expanded the cubic directly; its mixed coefficients are lambda^(-2) and its pure coefficients alpha^(-2)+lambda^(-2), beta^(-2)+lambda^(-2).

The three cases exhaust all root triples:

- Type I is alpha=beta=lambda=1. The translated w is exactly xy(x+y), F2=0, and F3=xy(x+y), so comparing the first terms of f=w g gives g(P)=1. This point is absent from the quotient curve.
- Type II has alpha=1, beta=b!=1; the exchanged case; or alpha=beta=b!=1, lambda=1. In each case w has a nonzero linear term proportional to x, y or x+y, and F2 is a nonzero multiple of its square. Thus g has order 1 with that nonzero tangent. No denominator-zero coincidence is omitted.
- In Type III, alpha,beta are neither 1 and are unequal. Consequently lambda!=1 and w0=(alpha+1)(beta+1)(alpha+beta) is a unit. Put A²=(beta+1)/(alpha lambda), B²=(alpha+1)/(beta lambda). Both A,B are nonzero, and (A+B)²=(alpha+beta)/(alpha beta) is nonzero. Hence F2=(Ax+By)² is nonzero with one tangent L.

For the decisive Type III cubic calculation, evaluating the displayed F3 at (B,A) gives

    F3(B,A)=AB(A+B)(A²B²+lambda^(-2)),
    A²B²+lambda^(-2)=1/(alpha beta lambda).

For the second identity, over the common denominator alpha beta lambda² the numerator is `(alpha+1)(beta+1)+alpha beta=alpha+beta+1=lambda`. Every factor is nonzero. Thus L does not divide F3. Division by the unit w retains the essential correction:

    G2=F2/w0,      w0 G3=F3+w1 G2.

The correction is divisible by L and cannot cancel the nonzero class of F3 modulo L. The local lemma excludes two vanishing quotient factors at every Type III point. Discarding this correction would have been an unjustified inference; the actual packet keeps it correctly.

The projective conclusion is valid. At any point of P²(K), permute a nonzero coordinate into the third position and scale it to 1. Symmetry of phi_m gives exactly the same affine polynomial in this invertible chart. Any two factors vanishing at the projective point would yield g=g_x=g_y=0 and fall into the exhaustive cases above. Type I is absent, Type II is smooth, Type III is excluded by the lemma. This covers infinity by actual charts, not by assuming an affine computation is already global.

If a homogeneous polynomial in a domain factors, comparison of minimum and maximum total degrees forces each factor homogeneous. Two positive-degree homogeneous factors with no common component intersect by the projective Bézout theorem over the algebraically closed field K. The source's stated hypotheses are satisfied. If the factors share a component, that positive-degree projective curve has a point over K and supplies an intersection directly. At either kind of intersection both local factors vanish, which has just been excluded. This includes repeated-factor possibilities without assuming squarefreeness first. Thus the WHOLE homogeneous phi_m is absolutely irreducible.

I found no missing projective point, zero coordinate, coincident-root case, repeated component or arithmetic restriction in this reconstruction. In particular a finite fixed-field test is not being used to infer all ell.

## 4. Whole reconstruction of S3B

Let n=Qh+1 be arbitrary odd n>=3, where Q=2^v2(n-1)>=2 and h is odd. Differentiate the established identity f_n=R phi_n in Y and set Y=Z=1. Here R=0 and R_Y=(X+1)², whereas (f_n)_Y=X^(n-1)+1. This proves the polynomial identity

    (X+1)² phi_n(X,1,1)=X^(n-1)+1.

At a!=0,1 the vanishing condition is therefore a^h=1, using injectivity of the Q-th power. If h=1 there is no such a; in particular the n=3 unit cannot enter the germ. Under the germ's hypothesis h>=3, so there is room for every displayed term through degree Q+1. This is an actual diagonal Y=Z, not the coordinate boundary Y=0 used in my older IC1.

Set c=a+1, X=a+x,Y=1+y,Z=1. Direct multiplication gives

    w=c²y+c y²+x²y+x y².

Thus w1=c²y, w2=cy² and w3=x²y+xy², with c nonzero. Using `(b+z)^n=(b+z)(b^Q+z^Q)^h`, the constant and linear terms cancel, degrees 2 through Q-1 vanish, and only the degree 0 and 1 terms of the h-th power can contribute through Q+1. Write E=a^(-Q), b=1+a^(1-Q). The two surviving numerator forms are precisely

    F_Q=b y^Q,
    F_(Q+1)=y[E x^Q+E x y^(Q-1)+(1+E)y^Q].

I checked this separately including Q=2: the two base-a pure-x terms cancel, while the mixed terms come from `(x+y)^(Q+1)=x^(Q+1)+x^Q y+x y^Q+y^(Q+1)`. The root condition a^h=1 supplies all displayed negative exponents. There is no assumption h=ell, no bounded n check, and no arbitrary division by b.

If b!=0, the quotient has order Q-1 and first term `(b/c²)y^(Q-1)`. At the next degree the equation is w1 T_Q+w2 T_(Q-1)=F_(Q+1). Solving yields the packet's exact T_Q, including the extra `b/c³` contribution to y^Q. Its x^Q coefficient is E/c², a unit. Consequently y does not divide the next term; the local factor lemma applies with d=Q-1 and makes the cofactor of any vanishing factor a unit.

If b=0, F_Q vanishes but F_(Q+1) does not, since its x^Q y coefficient is E. Hence the quotient has order Q, with initial term exactly (9), and this term is not divisible by y. A smooth factor with tangent y would force divisibility of the product's initial form by y and is impossible. Finally b=0 is equivalent, for nonzero a, to a^(Q-1)=1, to a^Q=a, and to a in the unique finite field F_Q in K. The two branches are exhaustive and do not interchange their hypotheses.

## 5. Whole reconstruction of S3C and S3D

For every odd ell>=3, T^ell+1 is separable and has ell distinct roots in K. Choose any root a other than 1. It is automatically nonzero and outside F2. This works for composite ell and does not rely on a primitive cube root being present. The BASE m has Q=2; the b!=0 calculation therefore shows that phi_m is smooth at P=(a:1:1), with nonzero linear term proportional to y.

Suppose an absolute component is common with phi_n. Absolute irreducibility of the WHOLE base, already proved for m, forces phi_n=phi_m H over K. This is the precise point where ordinary irreducibility alone would have been insufficient. The factor identity makes phi_n(P)=0, so the SAME a satisfies the arbitrary-target root condition.

If a belongs to the target F_Q, the target's initial form is not divisible by y, contradicting the initial linear form y of phi_m. This branch needs no unit-cofactor assumption. If a is outside F_Q, the local lemma applied to the target forces H(P)!=0. Thus the target's order Q-1 equals the base order 1, so Q=2. Equivalently, Q>=4 would require H to vanish and directly violate the lemma. This is an exact local multiplicity argument, not a conclusion from restricted line multiplicities alone.

Only now is n=3 mod 4 known. The n=3 case is impossible because its quotient is a unit and cannot vanish at P. Thus S3A applies to the WHOLE target as well. A nonconstant factor phi_m of this absolutely irreducible target must be an associate, and equality of total degrees gives n=m. At equality the gcd is the given phi_m; at any unequal index no common K component exists. A nonconstant common F2 factor would remain a common K factor, so the same gcd alternatives hold over F2 without a separate descent assertion for arbitrary absolute factors.

The new proof does not require CS composition indecomposability, Kasami labels or an imported arbitrary-component theorem. The old m=7 and m=11 singletons are genuine special cases, not newly claimed discoveries or certificates rerun here.

For S3D, a principal ideal generated by nonzero homogeneous phi_m is graded: decompose a proposed cofactor into homogeneous pieces. The distinct nonzero phi_n have distinct degrees n-3. Hence division of a finite sum forces division of each nonzero homogeneous summand. A nonzero c_n in K is a unit, so S3C forces n=m for every nonzero coefficient. The converse, including the zero sum and an empty index set, is immediate. A degree-zero n=3 term cannot be a nonzero multiple of positive-degree phi_m. Excluding n=1 prevents a spurious nonzero coefficient multiplying the zero polynomial. No cancellation of pointwise values is used.

## 6. Adversarial checks, limitations and disposition

I explicitly tried the following failure points: w=0 before differentiating; nonzero alpha/beta assumed prematurely; all three Type II coincidences; loss of the quotient cubic correction; a shared repeated component evading the coprime Bézout statement; points at infinity; h=1/Gold targets and n=3; Q=2 in the first-perturbation expansion; a in F_Q versus outside it; a composite ell without a chosen cube root; a vanishing cofactor in only one branch; F2 irreducibility substituted for absolute irreducibility; and a graded zero-sum or constant-term cancellation. Each is resolved in the actual proof as reconstructed above.

The 44-row companion ledger covers every constructor obligation 01--36 and every substantive inference. It has zero substantive open issues and zero required author repairs. The source record distinguishes original-author proof access from the unread full journal PDF and unused external APN/factorization claims. The integrity check verifies the nine payload fingerprints, constructor manifest, 47 declared current source/input records and compact immutable parent metadata. It does not run the constructor's administrative or mathematical code, reproduce a historical file inventory, or read any new peer sector3 material.

I recommend coordinator acceptance of precisely S3A--S3D after the OTHER independent whole report and normal full reconciliation. The candidate and all older files remain unchanged. This report is not promotion and asserts neither a complete annual answer nor new qualifying exponents or priority. No mathematical executable, scan, CAS, author rerun, source/cache mutation, shared edit, Git operation, new agent, charge or contact was used.
