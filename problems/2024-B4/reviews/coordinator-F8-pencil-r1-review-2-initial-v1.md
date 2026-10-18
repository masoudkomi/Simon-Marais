# Entire initially blind WHOLE FP0–FP2 audit, R2

2026-10-18 UTC. Reviewer `/root/review_2017_coarsening_r1` (C). This is an independent reconstruction of the NEW root-constructed FP argument. I did not construct FP0–FP2. My older CP1/composition and S3 construction roles, and older KC/three-bit review roles, concern separately accepted inputs; this report is not an independent recertification of my own old work. No NEW A FP report, finding, ledger, source record, program or metadata was read or hashed before this ENTIRE initial packet was frozen.

**Verdict within the submitted scope:** no substantive defect, required repair or advisory identified. All36 obligations were reconstructed. The conclusion is the six-line multiplicity inequality, an absolute-factor degree gap and a unique large absolutely irreducible component defined over F2. The proof leaves a possibly nonconstant small F2 cofactor. It does not establish whole-polynomial irreducibility, official membership/nonmembership or an annual classification. Only the coordinator can promote the scoped result after both OTHER whole audits and reconciliation.

The exact audited main is `notes/coordinator-F8-pencil-r1-candidate-v1.md`, 14313 bytes, SHA256 `68accf09323d692e4d4d6850e8c2c04d735d667e1ddaa56cbb73c451fb6402ef`. Its complete nine-file constructor packet, all36 obligations, failures, source limits and administrative code/metadata were read. Its code was inspected, not executed. All mathematical calculations below were done by hand; the only reviewer program checks bytes, SHA256, JSON, accepted-copy suffixes and obligation labels.

## 1. Domain and what is being proved

Put q=8^k, k>=2, n=7q+1, N=7q-2, and K=the algebraic closure of F2. Thus q>=64, n is positive and odd, and its binary support is {0,3k,3k+1,3k+2}. Define

    W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X),
    f=X^n+Y^n+Z^n+W^n, phi=f/R.

All polynomial equalities in the local geometry are over K. The later inequalities are over the ordinary real numbers. The official open part(b) concerns coefficientwise F2 factorization into two positive-degree factors, equivalently appropriate integer-polynomial lifts; it is not polynomial-function equality, nor just a factorization after extending the field. No preliminary proof was investigated or reproduced.

The q=8, n=57 endpoint is outside the theorem. The accepted neighbor-Frobenius result does not settle a=3k: its seven-neighbor conclusion covers 3 not dividing a. I read the complete accepted NF body and authorities and verified that the present argument reconstructs the vanished degree-q case rather than applying NF outside its hypotheses. The other accepted frontier authority records were context only, not hidden premises.

For a homogeneous divisor U of phi write e=deg U, m=m_P(U), P=(1:1:1). For the18 other prescribed-diagonal singularities write multiplicities u_i, and for the24 off-diagonal ones v_j. The proposed claims are

    FP0: T=sum(v_j) <= 6(e-m)-q*t,
    FP1: no factor degree lies in [2q+9,5q-11],
    FP2: a unique absolute component G has degree >=5q-10;
         its normalized polynomial and the cofactor are in F2,
         and the cofactor degree is <=2q+8.

Here t counts the six special tangent directions assigned to U at P. Constants and a factor missing P are allowed in FP0. The proof of FP1 uses a global quadratic bound and does not require FP0. That separation is explicit and valid.

## 2. Squarefreeness and every projective singularity

The coefficient of X^(n-1)Y in f is1, so f is nonzero. Each of X+Y, Y+Z, Z+X divides f; they are pairwise coprime linear polynomials, hence R divides f. The quotient is a nonzero homogeneous polynomial of degree N. If a product of nonzero polynomials is homogeneous, the sums of their least and greatest occurring degrees coincide. Degree spread is nonnegative and additive in a domain, so each factor is homogeneous.

Formal derivatives are

    f_X=(X^7+W^7)^q, f_Y=(Y^7+W^7)^q.

Since7 is odd, each underlying seventh-power expression splits into seven distinct lines. Their coefficient vectors may be written (1+zeta,zeta,zeta) and (eta,1+eta,eta), with zeta,eta in F8*. Proportionality with scalar c would force zeta=c eta from the Z coordinate and 1+zeta=c eta from X, a contradiction. Therefore f_X and f_Y have no common irreducible factor, including after taking qth powers. Any repeated irreducible factor of f divides both formal derivatives, even in characteristic2. Thus f, and then phi, are squarefree. Any factorization phi=UV consequently has coprime U and V.

At a singular projective point of phi, f=R phi implies f and the two derivatives in any affine chart vanish, even on R=0. Choose a nonzero coordinate, permute it into Z and set Z=1; the symmetric equation is unchanged. Write alpha=X, beta=Y, lambda=alpha+beta+1. Then

    alpha^7=beta^7=lambda^7=u,
    f=u^q(alpha+beta+lambda)+1=u^q+1.

Frobenius injectivity gives u=1. Hence alpha,beta,lambda are nonzero seventh roots, namely elements of F8*. If an original coordinate were zero, permuting a nonzero coordinate into Z would leave a zero among alpha,beta, contradicting this conclusion. Therefore all singularities are in the original Z=1 chart; none is omitted at infinity. Conversely the local calculations in the next section show that every projective F8 point with X,Y,Z,W all nonzero is singular.

There are (8^3-1)/(8-1)=73 projective F8 points. Each of X=0,Y=0,Z=0,W=0 contains9, the six pairwise intersections are distinct, and there is no triple intersection. Their union contains36-6=30. The complement consists of43 points. Each prescribed diagonal X=Y,Y=Z,Z=X contains9 F8 points, two excluded by the four-line union, hence P and six other good points. Those three diagonals intersect only at P. Thus the complete singularity list is P,18 other diagonal points and24 off-diagonal points. These finite incidence counts require no field enumeration.

## 3. Ordinary cones and exact local intersections

At P use X=1+x,Y=1+y,Z=1. Here R=xy(x+y) and

    (1+t)^n=(1+t)(1+t^q)^7.

The first nonzero numerator form is x^q y+x y^q. Its quotient cone is

    (x^(q-1)+y^(q-1))/(x+y)
      = product over b in F_q minus F2 of (x+b y).

It has q-2 distinct factors. None is x, y or x+y, so P is ordinary of multiplicity q-2 and none of the prescribed diagonals is tangent there.

At a nontrivial diagonal point, symmetry permits (b:1:1) with b in F8* minus{1}. Put c=b+1 and E=b^-1, translate X=b+x,Y=1+y. The degree-q numerator form vanishes because q fixes F8. The next form is

    E x^(q+1)+y^(q+1)+E(x+y)^(q+1)
       =y[E x^q+E x y^(q-1)+(1+E)y^q].

Since R has initial form c^2 y, phi has the degree-q cone

    (E/c^2)[x^q+x y^(q-1)+c y^q].

On y=1 the bracket has derivative1, so its finite roots are simple; at y=0 its value on (1:0) is1. There is no additional repeated/infinite tangent direction. Thus this is an ordinary q-fold point and the prescribed diagonal y=0 is transverse.

At an off-diagonal point (alpha,beta), R is a unit. The first nonzero form has degree q+1 and equals

    H=a x^(q+1)+b y^(q+1)+d(x^q y+x y^q),
    a=alpha^-1+lambda^-1,
    b=beta^-1+lambda^-1, d=lambda^-1.

Its derivatives are a x^q+d y^q and d x^q+b y^q. Their matrix determinant is

    ab+d^2=[(lambda+alpha)(lambda+beta)+alpha beta]
                 /(alpha beta lambda^2)
           =1/(alpha beta lambda) !=0.

They have no common nonzero projective zero. A repeated linear factor of the binary form would give one, so H has q+1 distinct linear factors. These points are ordinary of multiplicity q+1. This also proves the asserted converse for all43 points and rules out an accidentally vanishing initial form.

In phi=UV the initial cones at each ordinary point partition these distinct lines. Thus they are coprime, and the local intersection number is the product of the two multiplicities. This includes a multiplicity0, when one factor is a local unit and the intersection number is0. Conversely any common projective zero of U,V is singular on their product. Consequently the complete43-point list accounts for every term of the projective Bezout intersection; there is no missing smooth or infinite intersection term.

## 4. Three diagonal identities and the six-line inequality

On Y=Z, division by Y+Z can be evaluated by the transverse formal derivative, giving

    phi(X,Y,Y)=(X^(7q)+Y^(7q))/(X+Y)^2.

The right side is a polynomial of degree N, is nonzero at (1:0:0), and has only seven finite roots: P with contact q-2 and the six other seventh roots with contact q. The prescribed line is transverse at each such point by the preceding cones. Any zero of U restricted to this line is among these roots, and its contact equals its own multiplicity. No prescribed diagonal divides phi or U. Therefore on each of the three lines

    e=m+sum of its six u_i.

Writing z=e-m gives z>=0 and S=sum(u_i)=3z. Nothing requires m>0. The ordinary ranges are 0<=m<=q-2, 0<=u_i<=q and 0<=v_j<=q+1.

Of the nine F8 lines through P, three are prescribed diagonals. Each off-diagonal F8 singularity lies on exactly one of the remaining six, its join with P. No assertion about the number of points on an individual line is needed. Parameterize one of these six in the local chart by x=t,y=b t, b in F8 minus F2. The supported exponents in (1+t)^n are j q and j q+1, j=0,...,7. Along this line a coefficient at supported positive degree h is 1+b^h+(1+b)^h. Degrees1,q,q+1,2q vanish. The next supported degree2q+1 has coefficient

    1+b^3+(1+b)^3=b(1+b) !=0.

There is no intervening supported exponent. Here R=b(1+b)t^3 exactly. The restriction of phi therefore has first term t^(2q-2), with coefficient1. This proves both exact contact2q-2 at P and that none of the six lines is a component.

These six directions occur in the ordinary cone at P because F8 is a subfield of F_q. For each line, if its direction is absent from U's cone, U has contact m there. If present, that direction is absent from V's cone, so V has contact q-2-m. Additivity of contact for phi=UV then gives U contact (2q-2)-(q-2-m)=m+q. This reasoning still applies if U or V misses P.

At an off-diagonal singularity on such a line, contact is at least v_j; equality is neither claimed nor needed if the line is tangent. Contacts at all other points of the line, including smooth or infinite ones, are nonnegative. Summing the six line-Bezout identities gives

    6e >=6m+q t+T,
    T<=6(e-m)-q t.

That is FP0. If U is F2-defined, its cone is invariant under coefficientwise squaring. The six directions F8 minus F2 have two squaring orbits of length3, so t belongs to{0,3,6}. This restriction is not asserted for general K-defined factors.

## 5. Bezout and the optimization, including the endpoints

For a factor degree e and its complement degree N-e, the full projective intersection identity is

    e(N-e)=m(q-2-m)+sum u_i(q-u_i)+sum v_j(q+1-v_j).

Cauchy's inequality on respectively18 and24 entries, together with S=3z, yields

    e(N-e)<=m(q-2-m)+3qz-z^2/2+(q+1)T-T^2/24.

For every real T, (q+1)T-T^2/24 is at most6(q+1)^2; this follows by subtracting (T-12(q+1))^2/24. This is a GLOBAL maximum. In particular the argument does not insert FP0's upper T bound on an unproved monotonicity interval.

Substitute m=e-z and subtract e(N-e). The resulting upper difference is

    D(z)=-(3/2)z^2+(2e+2q+2)z-6qe+6(q+1)^2.

Completing the square for all real z gives

    D(z)<= (2/3)[e^2-(7q-2)e+10(q+1)^2].

This is an upper bound regardless of whether its maximizing z is feasible or integral. Direct expansion at e=2q+9 gives -3q+109. At e=(7q-2)/2 the bracket is -9q^2/4+27q+9. For q>=64 the first is at most-83, and the second is negative (already-7479 at64, decreasing thereafter). The bracket is a convex quadratic in e, hence no greater than the larger endpoint value throughout this interval. For 2q+9<=e<=N/2 the Bezout difference must thus be negative, contradicting the preceding inequality.

Finally, if any factor has degree in [2q+9,5q-11], replace it by its complement when necessary. The smaller degree is at most N/2 and at least2q+9, since N-(5q-11)=2q+9. This proves FP1, with both integer endpoints included. The strict signs fail at q=8; the proof correctly excludes that endpoint instead of extrapolating.

## 6. Grouping absolute components and descending the unique large one

Assume every absolute irreducible component had degree at most2q+8. The sum of all degrees is N>2q+8. Greedily add components until the sum first exceeds2q+8. The resulting integer e lies in[2q+9,4q+16]. Because q>=64, the upper endpoint is at most5q-11 and is less than N. The product of those components is therefore a proper factor forbidden by FP1. So some component has degree at least2q+9. FP1 forces its degree to be at least5q-10; this remains true if it is the entire phi.

Two components of degree at least5q-10 cannot fit in degree N, since 2(5q-10)>7q-2 for q>6. There is exactly one such component G and the complementary total degree is at most2q+8. This reasoning does not assume that all components have equal degree or form a single Frobenius orbit.

Normalize G's leading coefficient in a fixed monomial order to1. The coefficient-squaring automorphism of K fixes phi and permutes its normalized absolute factors, preserving degrees. Uniqueness fixes G itself. Every coefficient satisfies a^2=a, so G is defined over F2. If phi=GH, apply the same automorphism: G sigma(H)=GH. Cancelling G in the polynomial domain gives sigma(H)=H, and H also lies in F2[X,Y,Z]. A different fixed nonzero-coefficient normalization gives the same conclusion.

This proves FP2 only. H can still have positive degree up to2q+8. Producing an absolute F2 factor is weaker than proving whole irreducibility; it also does not certify the official two-factor condition unless H is known nonconstant. Neither inference is made by the submitted packet.

## 7. Source attribution, rejected imports and remaining scope

The official [2024 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf), B4(b), was checked directly. The classical projective Bezout/contact framework is also stated in [Hernando–McGuire, Section3.2 and Corollary8](https://arxiv.org/pdf/0903.2016v4). Their Theorem15 requires ordinary F2 irreducibility; it is not imported here. Theorem16 already supplies qualitative absolute-F2-component existence in the present family because7 properly divides q-1. I checked that statement, without claiming an independent reconstruction of its full proof. Quantitative priority is unestablished.

I checked the separate [Agrinsoni–Janwa–Delgado Theorem8](https://arxiv.org/pdf/2602.01583) lead and its stated squarefree-highest-form requirement. The default Z=1 chart does not supply that hypothesis: at a in F8 minus F2, the binary leading numerator at (a:1) and its derivative both vanish while its denominator is a unit. This is a repeated root of the leading binary form, not a singularity of the full projective curve at infinity; its Z derivative need not vanish. The new proof does not use this lead or assert that a generic changed-chart theorem has been proved.

No routine enumeration, mathematical program, CAS, factor table, numerical estimate, constructor rerun or finite-field certificate was used. The source record distinguishes the exact passages actually read from unread journal/original proof material. No paper was downloaded or redistributed in this audit. Source links are not fabricated retrieval hashes. The compact baseline binds all direct immutable inputs and the preceding own manifest without duplicating the historical inventory. The all36 ledger, issues, read limits, worklog, administrative freezer, metadata and hash manifest form this ENTIRE initially blind report packet.
