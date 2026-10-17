# GK1–GK3: independent whole initial review R2

2026-10-17 UTC. Initial report frozen before reading any other GK review or coordinator reconciliation. Reviewer: `review_2022_complexity_r2`. Requested gpt-6.1-sol/max; independent effective-setting readback unavailable. The coordinator constructed GK; this reviewer did not. The candidate remains **candidate proof — unverified** until the coordinator completes the prescribed independent review process.

## Result and scope

I find no substantive objection to GK1–GK3 in the exact submitted scope. I reconstructed the two-dimensional relation, its propagation for every index, polynomial descent, leading degrees, whole homogeneous divisibility, integer lifts, and the valuation exclusion. No repair is requested by this initial review. This is one independent whole audit, not a promotion or a full solution of 2024 B4(b).

The reviewed main file is `notes/coordinator-generalized-Kasami-r1-candidate-v1.md`, 10290 bytes, SHA256 `f99bae5f5d3877e556a30347a38616daf6b54fde300ae60543f849893a7dc4b8`. Its six-artifact manifest is 2042 bytes, SHA256 `50c3269d28a49327e28e216a857fdb711dae8875cab127645bc4081f2ac9ec65`. I read the complete main proof, source note, worklog, sixteen-obligation list and administrative freeze code. I also read both complete accepted mathematical dependencies and their acceptance scopes. The inference ledger records the individual checks, including failed counterexample routes.

Earlier context: I previously audited the 2024 T1–T4 structural packet and the C7/C11 divisor packet. I did not construct those packets, CP1–CP3, or GK1–GK3. I was not one of the two CP1–CP3 reviewers identified in its acceptance record. Reading accepted CP and the older phi13 theorem is disclosed dependence, not a fresh audit of their entire historical finite certificate. No new GK peer findings or later coordinator GK inspection were read. Hashing old review artifacts did not entail reading their conclusions.

## 1. Official domain and exact dependencies

I directly reopened the [official 2024 Paper B, p.2 B4(b)](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf). The requested integers are positive and odd. Factorization is a coefficientwise congruence of integer polynomials, with both unspecified factors nonconstant after reduction modulo two. It is not a statement about polynomial functions on a finite set. I used only the open part and the already accepted quotient normalization; no proof of preliminary part(a) is supplied here.

Write R=(X+Y)(Y+Z)(Z+X), and phi_n=f_n/R for odd n>=3 in F2[X,Y,Z]. The accepted normalization makes phi_n nonzero homogeneous of degree n−3. The n=1 zero numerator cannot be R times two nonconstant F2 polynomials in a domain. The n=3 quotient is a unit. Neither endpoint qualifies. A factorization over an extension field alone would not meet the domain.

The new proof imports these exact accepted facts:

1. `proofs/reviewed-composition-Kasami-v1.1.md`, SHA256 `f1e82d443b5ac997889c7a7f7f340437f8401516cccf9516eac132558df220c5`: for ALL odd d,n>=3, the WHOLE phi_d divides phi_n over F2 precisely when g_n=H composed with g_d for H in F2[T]. Here x^n+(x+1)^n=g_n(x²+x), and g_n is monic of degree (n−1)/2. The exact full-degree homogeneous transport is part of the accepted theorem. CP2 is used only for the r=2 comparison, not as a recurrence premise.
2. `notes/zero-automaton-criterion-reviewed-v1.1.md`, SHA256 `362f2541b2bb1ab1e22ba768b41d55e7282f08631b0ad39522682244d213f226`: for odd n>=3, the WHOLE phi13 divides phi_n iff n=(64*16^j+1)/5, j>=0. Only this exact theorem is needed for GK3. Its finite certificate is previously accepted and was not rerun here.

I checked that the cited acceptance records actually grant these scopes. Their historical unverified labels in preserved submission suffixes do not supersede the accepted headers. Neither dependency classifies arbitrary factors.

For CP1 I also reconstructed the mathematical transport rather than assuming an extension-field factor statement suffices. The invariant ring for x->x+1 is F2[x²+x], because F2[x] has basis 1,x over that ring and the odd/even leading degrees give uniqueness. For odd n>1, cancellation of the x^n terms leaves leading term x^(n−1), so deg g_n=(n−1)/2. If Q_n(U,V)=(g_n(U)+g_n(V))/(U+V), the invertible homogeneous linear change (X,Y,Z)=(s+u,s,t) gives the dehomogenization

    phi_n(s+1,s,t)=Q_n(s²+s,t²+t).

Its degree is exactly n−3: highest terms double in total degree and have distinct even exponent pairs. Thus homogenization loses no line at u=0. The cover F2[U,V] -> F2[s,t] is free with basis 1,s,t,st, so divisibility by the WHOLE Q_d descends; comparing basis coefficients forces the quotient back into F2[U,V]. Finally, for monic h, the unique h-adic expansion p(U)=sum_(j<deg h) U^j C_j(h(U)) shows that h(U)+h(V) divides p(U)+p(V) exactly when p=H composed with h. Cancellation of the SAME nonzero U+V from the two difference quotients preserves repeated diagonal factors; no coprimality is required. These are the CP1 hypotheses actually used by GK2.

## 2. Exponent domain, auxiliary roots and the pairing matrix

Fix k>=1 and q=2^k. For every r>=0 the integer polynomial identity

    (q+1)*sum_(j=0)^(2r) (-q)^j=q^(2r+1)+1

shows L_r is an integer. Equivalently the alternating quotient has last term 1 and all other terms even, so L_r is odd and positive. Directly from the formula, L_0=1, L_1=q²−q+1=d. The sequence strictly increases with r. In particular the use of CP1 starts at r=1, where d,L_r>=3; the auxiliary g_1=1 is confined to the recurrence initial value.

Take a transcendental a over F2, b=a+1, and an algebraic closure K of F2(a). Roots A^(q+1)=a and B^(q+1)=b exist in K, and both are nonzero. Their sum identity is A^(q+1)+B^(q+1)=1. No finite-field specialization or Frobenius-period assumption has entered.

Use v=(A,B), v^[j]=(A^(q^j),B^(q^j)) and the ordinary bilinear dot product. Its possible isotropic vectors in characteristic two cause no difficulty: all rank claims below are proved by an explicit determinant. Since (q+1)L_r=q^(2r+1)+1,

    D_r=v dot v^[2r+1]=a^L_r+b^L_r=g_(L_r)(a²+a).

The exponents are literal positive integers. This equality proves the desired scalars are independent of the root choices; it does not presume the vectors themselves are independent of those choices.

Let c=D_1. D_0=1, and c=g_d(a²+a). The invariant-degree result gives positive degree (d−1)/2 even at q=2,d=3. Consequently c is not constant and c+1 is a nonzero element of K. This is the precise reason division by c+1 is allowed at the generic point. A finite a with c=1 would not support this division and is handled later by polynomial descent.

The four pairings have exact Frobenius orders:

    v dot v^[1] = 1;
    v^[2] dot v^[1] = (v dot v^[1])^q = 1;
    v dot v^[3] = c;
    v^[2] dot v^[3] = (v dot v^[1])^(q²) = 1.

Thus the two linear functionals given by pairing with v^[1],v^[3], evaluated on the ordered vectors v^[2],v, give [[1,1],[1,c]]. Its determinant is c+1. If the columns or the functionals were dependent, this matrix would have rank at most one, so both are independent. In dimension two the columns therefore form a basis. This establishes a full vector relation; it is stronger than merely deriving two necessary scalar equations.

## 3. Coefficients and all-index propagation

There are unique alpha,beta in K with v^[4]=alpha v^[2]+beta v. Pairing with v^[1] gives alpha+beta=c^q, since v^[4] dot v^[1]=(v^[3] dot v)^q. Pairing with v^[3] gives alpha+c beta=1, since v^[4] dot v^[3]=(v dot v^[1])^(q³). Adding these equations yields

    (c+1)beta=c^q+1=(c+1)^q.

Because c+1 is nonzero in this function field,

    beta=(c+1)^(q−1),
    alpha=c^q+(c+1)^(q−1).

These are exactly B_q(c),A_q(c), with coefficients in F2. In particular no negative exponent remains. The same nonzero pairing determinant makes the two scalar equations sufficient to recover the already existing full vector relation. Neither a Hermitian-space theorem nor a claim that q²-Frobenius is the identity is needed.

For an arbitrary integer r>=0, apply the q^(2r+1)-power Frobenius to the FULL relation. Coordinate orders add, rather than multiply:

    v^[2r+5]=A_q(c)^(q^(2r+1)) v^[2r+3]
               +B_q(c)^(q^(2r+1)) v^[2r+1].

Now pair with the unchanged original v. The three vector indices 2r+5,2r+3,2r+1 are exactly those defining D_(r+2),D_(r+1),D_r. This proves the advertised scalar recurrence, including r=0. D_0=1 and D_1=c agree with P_0(c),P_1(c). Ordinary induction therefore proves D_r=P_r(c) for every r>=0. The argument has no bounded-index premise, trace/order assumption, or extrapolation from the known r=2 identity.

Both g_(L_r)(a²+a) and P_r(g_d(a²+a)) lie in F2[a]. Their equality in K is an equality in that polynomial ring. Since substitution U->a²+a sends a nonzero degree-e polynomial to a degree-2e polynomial, it is injective. This proves GK1 in F2[U]. It consequently holds at every finite specialization, including those with c+1=0. One must not repeat the generic division at such a point, but the candidate does not do so.

As an adversarial endpoint check directly tied to that denominator concern, at c=1 the recurrence itself has A_q(1)=1 and B_q(1)=0 because q−1>=1. Its initial values are both 1, so P_r(1)=1 for every r. The visibly degenerate choices a=0 or 1 therefore provide no contradiction. This is an analytic check of the threatened denominator locus, not finite-field sampling or a premise of the universal identity.

## 4. Leading degrees, equality cases and the CP2 comparison

A_q(T) is monic of degree q because its other summand has degree q−1. B_q is monic of degree q−1. Let E_0=0, E_r=1+q²+...+q^(2r−2) for r>=1. With monic P_r,P_(r+1), the first recurrence term has degree q^(2r+2)+E_(r+1)=E_(r+2). The second has degree (q−1)q^(2r+1)+E_r. Subtracting the latter from the former gives

    q^(2r+1)+(E_(r+1)−E_r)=q^(2r)(q+1)>0.

So leading cancellation is impossible at every r>=0. P_0=1 and P_1=T begin this induction, including the constant-degree-zero endpoint. The resulting outer composition degree agrees with

    (L_r−1)/(d−1)=(q^(2r)−1)/(q²−1)=E_r.

In particular no recurrence term can silently become zero or constant in the range r>=1.

For P_2, raising A_q and B_q to q gives

    P_2=T^(q²+1)+(T+1)^(q(q−1))T+(T+1)^(q(q−1))
       =T^(q²+1)+(T+1)^(q²−q+1).

This matches CP2 exactly. The earlier proof of every index did not use this match. For r=1, P_1=T gives g_(L_1)=g_d and divisibility is equality; a unit cofactor is correctly excluded from the genuine factor conclusion.

## 5. Whole factors over F2 and the actual integer congruence

For every q=2^k,k>=1 and r>=1, both d and L_r are odd and at least three. GK1 supplies H=P_r in the exact CP1 criterion. It follows that the WHOLE homogeneous phi_d divides phi_(L_r) in F2[X,Y,Z]. No extension-field component, value equality on finite points, or unspecified coefficient-field descent is being used.

For q>=4, d−3=q²−q−2>0. For r>=2, strict increase in L_r gives L_r>d, so the quotient degree L_r−d is positive. Both factors are nonzero. The cofactor can be taken homogeneous: in a graded domain, multiplication by a nonzero homogeneous factor sends distinct homogeneous components to distinct total degrees, so a homogeneous product has only the component of the required degree. Alternatively this follows from the exact homogeneous transport in CP1. Repeated factors do not invalidate either argument.

Taking coefficientwise 0/1 integer lifts of these actual F2 factors produces integer polynomials g,h with the requested congruence. Their positive degrees after reduction prevent either from being constant modulo two. There is no need for irreducibility of either factor, and no claim that every factor arises by this mechanism.

Writing m=r−1 gives n_(k,m)=(q^(2m+3)+1)/(q+1), m>=1. The claimed correspondence of indices is exact. For each fixed k>=2, increasing m strictly increases the exponent, so the construction persists at every advertised index. The q=8 values 3641 and 233017 are simple substitutions into this symbolic formula; no computation or finite certificate for the second was needed. At q=2, d=3 and phi3=1, so GK2a is true but supplies no qualifying factorization. This does not purport to decide all possible factors at those exponents. At r=0 the CP1 domain is not entered. At r=1 the cofactor is a unit. These restrictions are present where the candidate states its genuine factor conclusion.

## 6. The whole-phi13 exclusion and remaining scope

For r>=1, q^(2r)−1 is divisible by q+1 because q=-1 modulo q+1 and 2r is even. Both it and q+1 are odd integers, so their integer quotient is odd. Therefore

    L_r−1=q*(q^(2r)−1)/(q+1),     v2(L_r−1)=k.

The accepted exact phi13 exponents satisfy

    n−1=4*(16^(j+1)−1)/5,

where the last quotient is an odd integer. Their valuation is exactly two, including j=0,n=13. Consequently k>=3,r>=1 excludes equality with EVERY exponent in that exact accepted iff. This proves absence of the WHOLE phi13 divisor, not merely absence from an old sufficient list. It says nothing about an individual absolute or irreducible component of phi13.

At q=4, substituting r=m+1 gives L_r=(64*16^m+1)/5. Thus r>=2 corresponds to m>=1 in the old genuine factor family; r=1 corresponds to its equality/unit-cofactor endpoint m=0. The candidate does not claim new necessity for any general q, or novelty even for its new sufficient families. GK1–GK3 supply no classification of all reducible phi_n and no numerical enumeration of all qualifying n.

## 7. Source and integrity conclusions

The GK argument adds no external factor, APN, MCM-monodromy, or Galois theorem as a logical premise. I verified the accepted CP1 and exact phi13 scopes, and reconstructed the parts of CP1 needed for actual F2 homogeneous divisibility. I read the complete accepted phi13 exposition to identify the exact theorem and its actual/formal quotient bridge; its previously independently checked finite graph is an accepted input, not a certificate rebuilt in this audit. The source-check record gives the precise read limits, including literature that is motivation only and was not independently re-read here.

Administrative verification confirmed all six author artifact hashes and the target manifest. The author input-validation record has exactly 417 core record occurrences over 214 paths, all matching their recorded bytes and SHA256 values. Its separate motivation-only PDF cache entry also matches, making 418 occurrences and 215 paths if included. CP acceptance's nine embedded path/bytes/hash records and phi13 acceptance's ten path-to-hash entries were checked without reading historical peer report bodies. These counts have different provenance and are not mathematical evidence.

All 147 earlier own paths, including the completed all-D global construction packet, were verified unchanged. Only new `generalized-Kasami-review-2-*` files were written. No candidate/shared/Git edits, math code, CAS, enumeration, certificate rerun, paid API, contact, or access bypass occurred. Direct weekly telemetry at 10:58:57 UTC was 31% TOTAL used, reset 1792745187; the 90% TOTAL cutoff and reserve remain in force. No absolute-certainty, originality, full-classification or annual-solution claim follows from this review.
