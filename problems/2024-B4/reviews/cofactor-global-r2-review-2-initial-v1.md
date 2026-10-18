# CG1–CG3: independent ENTIRE WHOLE initial review2

2026-10-18 UTC. Reviewer `/root/review_2022_complexity_r2` (B).
Requested inherited `gpt-6.1-sol/max`; independent effective readback
unavailable. This review was reconstructed and frozen WITHOUT reading,
hashing or receiving ANY corresponding C NEW CG review finding, file or
metadata. Root is sole NEW constructor and excluded; B supplied no NEW
CG construction or repair. Only official2024 B4(b) is reviewed.

## Whole status and exact target

I find no substantive mathematical defect in CG1–CG3 in their EXACT
stated domains. All56 constructor obligations are independently disposed
in the separate full ledger. The general geometry, the two global
optimizations, reduced-product correction and positive-integer threshold
argument reconstruct by hand. No author repair is required for these
three theorem statements. Five closed scope/source notes remain in the
issue file; in particular the qualitative Hernando–McGuire theorem must
retain its PROPER-divisor condition and is not a proof premise here.
This is a reviewer recommendation, NOT coordinator promotion, external
validation, a priority finding or a full annual classification.

Target main:
`notes/cofactor-global-r2-candidate-v1.md`,15586B,
SHA256`9dac8137a3b47637e25ee66a5c2bf5ff00146e9d1d54ba55764002111d5376f9`.
Target complete freeze:
`notes/cofactor-global-r2-freeze-v1.json`,2322B,
SHA256`3e63984333d64dcfe8bb32395d28e948ab1023ce8f4ab367e0ea374d51dfeaef`.
All NINE constructor files were read in full: main,56 obligations/checks,
source audit, failures/worklog, administrative source, baseline, metadata,
validation and freeze. The source was READ, not executed. Fresh local
hash checks are administrative only. The separate complete source record
states the precise original passages read and source limitations.

B previously reviewed accepted structural T1–T4, GK/NJ/HR/NF/CS and other
2024 partial packets; those old roles are not fresh independent
recertification of their accepted claims. B did not construct CG, FP or
FS. The old T1 authority is the no-line premise. The accepted FP and FS
bodies and full authority scopes were freshly read, but the new proof
does not assume their special F8 orbit structure for general Q. No
unverified live note or unread theorem was promoted to a premise.

## 1. Official interpretation and integer domain

The official(b) asks for odd positive n and an identity COEFFICIENTWISE
over F2, with two nonconstant reductions of integer polynomials after
the three prescribed lines are removed. It is not a polynomial-function
identity on F2^3. Over K=F2bar, absolute irreducibility of the nonzero
homogeneous quotient excludes such F2 factors: reduce the proposed
integer factors, cancel nonzero R in the domain, and obtain a proper
positive-degree factorization over K, a contradiction. No converse
from extension-field reducibility to F2 reducibility is being used.

Here s>=3, Q=2^s, ell=Q-1>=7, k>=1, q=Q^k, n=ell*q+1. The
binary digits are bit0 and the s bits sk through sk+s-1, so n has
weight s+1>=4 and is odd. In particular n>=57, outside n1/n3/zero
boundaries. q fixes F_Q and is at least8. All inequalities involving
degrees and multiplicities are over the ORDINARY integers/reals,
not arithmetic in characteristic2. Aell=(ell-2)(ell+1)>0 and
o=(ell-1)(ell-3)>0 have no zero denominator in the claimed domain.

The coefficient of X^(n-1)Y in f is1, so f is not zero. Each prescribed
line divides f by substitution, and their distinctness makes their
product R divide f. Thus phi is a nonzero homogeneous form of degree
N=n-3=ell*q-2. In a polynomial domain the least and greatest total
degrees both add in a product. Consequently EVERY factor of phi is
homogeneous, even if homogeneous factors were not initially requested.
Accepted T1 applies at this binary weight and excludes ABSOLUTE lines.
Its source-supported coefficient proof was freshly read, including
zero-denominator cases and removal of the prescribed line factors.

## 2. CG1: reducedness and the complete projective set

Direct differentiation, with n odd and n-1=ell*q, gives

    f_X=(X^ell+W^ell)^q, f_Y=(Y^ell+W^ell)^q.

Because ell=Q-1 is odd, Z^ell-1 has simple roots exactly F_Q*.
The first derivative's linear factors have vectors
(1+zeta,zeta,zeta); the second has(eta,1+eta,eta).
If proportional by c, their Z entries give zeta=c*eta while their X
entries give1+zeta=c*eta, impossible. The parameters are nonzero, so
there is no exceptional zero-vector factor. No additional factor at
W0 occurs. Therefore the two derivatives are coprime. Any repeated
irreducible factor of f divides BOTH derivatives, also when its
multiplicity is even, so f and its divisor phi are reduced.

A singular point of phi has phi=0 and all local first derivatives0.
Differentiating f=Rphi then gives f=f_X=f_Y=f_Z=0 even on R0.
Choose a nonzero one of X,Y,Z and permute it into Z, normalizing Z1.
This is legitimate because f,R,phi are symmetric. Write
alpha=X,beta=Y,lambda=alpha+beta+1. The X/Y equations imply
alpha^ell=beta^ell=lambda^ell=u. Then

    f=alpha*u^q+beta*u^q+1+lambda*u^q=u^q+1.

Hence u=1 by injectivity of q-Frobenius. All alpha,beta,lambda lie
in F_Q*. Thus every singular point is projectively F_Q-rational and
all four coordinates X,Y,Z,W are nonzero. This also excludes any
singularity at infinity of the original Z1 chart; the chart was
chosen AFTER permuting the putative point. The converse follows
from the explicit ordinary cones below, not just from f's gradient.

The four projective F_Q lines X0,Y0,Z0,W0 have no triple intersection
and six distinct pair intersections. Their union has4(Q+1)-6=4Q-2
points. Removing it from Q^2+Q+1 leaves Q^2-3Q+3=ell^2-ell+1.
Each prescribed diagonal contains Q+1 points and has only two on
that union, leaving ell relevant points. The three diagonals share
only P111. Thus the remaining list is P,3(ell-1) other diagonal
points, and o=(ell-1)(ell-3) off-diagonal points. These are exact
incidence identities, requiring neither field enumeration nor
transitivity under any coordinate/Frobenius action.

## 3. All local cones and contacts, with equality conditions

At P put X=1+x,Y=1+y,Z1. The expansion
(1+t)^n=(1+t)(1+t^q)^ell starts1+t+t^q+t^(q+1), with later
terms of degree>=2q. Constants, linear and pure q terms cancel in
f. The first surviving piece is x^q y+xy^q. Dividing by the EXACT
xy(x+y) gives

    (x^(q-1)+y^(q-1))/(x+y)
       =product_(b in F_q minus F2)(x+b*y).

It has q-2 distinct factors and contains none of x,y,x+y. P is
ordinary of multiplicity q-2 and all prescribed directions are
transverse to every factor through it. No field equality F_q=F_Q
is assumed when k>1.

At a non-P diagonal point(b:1:1), b in F_Q* minus1, put c=b+1,
E=b^-1 and X=b+x,Y=1+y. The coefficient at degree q is1 on each
of the three varying source terms, hence cancels. The next numerator
piece is

    E*x^q*y+E*x*y^q+(1+E)*y^(q+1).

The denominator starts c^2*y. The quotient cone is therefore
(E/c^2)[x^q+x*y^(q-1)+c*y^q]. At y1 its polynomial is
x^q+x+c, with derivative1. At y0 the value of the cone is x^q,
so there is no omitted root at infinity. Thus the cone is squarefree,
the multiplicity is q, and the diagonal y0 is not tangent. A claim
that its two homogeneous derivatives never vanish together would
be stronger and false at the off-curve point(1:0); the candidate
correctly uses the affine simple-root test instead.

At an off-diagonal(alpha,beta,1), R is a unit. The q-degree piece
cancels, and the next piece is

    a*x^(q+1)+b*y^(q+1)+d*(x^q*y+x*y^q),
    a=alpha^-1+lambda^-1, b=beta^-1+lambda^-1,
    d=lambda^-1.

Its derivative matrix on(x^q,y^q) has determinant

    a*b+d^2=[(lambda+alpha)(lambda+beta)+alpha*beta]
                           /(alpha*beta*lambda^2)
           =1/(alpha*beta*lambda),

since lambda+alpha+beta=1. It is invertible. The two partials have
no common nonzero projective zero, so this odd-degree cone has q+1
distinct lines. This proves both the ordinary multiplicity and the
claimed converse of the singularity list. All nonzero listed
multiplicities are>=6 in this domain, so they really are singular.

For phi=UH, reducedness makes U,H coprime. At a listed ordinary
point their initial forms partition the distinct linear factors
of the total cone. Thus they have no common tangent and their local
intersection is exactly m_U*m_H, including the zero cases. Every
U/H intersection is singular on phi. The entire projective Bezout
sum therefore has no additional terms.

One can obtain the diagonal restriction without dividing0/0: on
Y=Z differentiate f=Rphi transversely. Then f_Z=(X^ell+Y^ell)^q
and R_Z=(X+Y)^2, giving the displayed polynomial restriction.
It has degree N, is nonzero at(1:0:0), and has contact q-2 at P,
q at each other ell-th-root point. The prescribed diagonal is NOT
tangent at these points, so U's contact equals its multiplicity.
It is not a component of U by T1. Three line Bezout identities give

    S=sum r_j=3(e-m)=3t.

This covers m0, and does not suppose a factor passes P. Combining
the complete local list with projective Bezout gives exactly

 e(N-e)=m(q-2-m)+sum r_j(q-r_j)+sum v_j(q+1-v_j). (B)

## 4. First global bound: no hidden feasible maximizer

Put V=sum v_j. Cauchy gives sum r_j^2>=3t^2/(ell-1) and
sum v_j^2>=V^2/o. The latter quadratic has a GLOBAL real maximum:
(q+1)V-V^2/o<=o(q+1)^2/4. After m=e-t, subtracting the left
side of(B) from these upper bounds gives

 0<=-(ell-1)q e+2(e+q+1)t
                    -[(ell+2)/(ell-1)]t^2+o(q+1)^2/4.

Maximizing only this concave t quadratic over ALL real t gives

 0<=(ell-1)/(ell+2)
       *[e^2-(ell*q-2)e+Aell*(q+1)^2/4].          (I)

The constant simplification uses4+(ell-3)(ell+2)=Aell.
All upper bounds enlarge the allowed region; no actual integer
maximizer, orbit-constant multiplicities or monotonic substitution
on a quadratic's wrong side is assumed. The prefactor is positive.
This applies to any proper factor, so in particular to one of degree
at most N/2, without a unique large component argument.

## 5. Reduced correction and the positive integer

The original classical source is checked in the separate source record.
For an irreducible degree d>=2 curve over perfect K, some partial is
nonzero; otherwise the polynomial is a square. Derivative intersection
first bounds delta=sum binom(m_P,2). Degree d-1 forms have dimension
M=d(d+1)/2. Impose the singular jets and M-delta-1 distinct smooth
points. There are at most M-1 conditions, leaving a nonzero form;
degree<d prevents a shared component. Its intersection gives
delta<=(d-1)(d-2)/2. This argument uses no characteristic-zero
Hessian, polar separability or genus formula for a product.

Now write the REDUCED U as c distinct absolute factors of degrees d_i.
T1 makes every d_i>=2, so c<=e/2. The pointwise identity for
binom(sum m_i,2), the irreducible bound separately on each factor,
and pairwise projective Bezout give

 sum_P binom(m_P(U),2)
 <=sum_i (d_i-1)(d_i-2)/2+sum_(i<j)d_i*d_j
 =(e-1)(e-2)/2+c-1<=e(e-2)/2.

The c-1 correction is retained. Keeping only listed nonnegative
summands yields

    m^2-m+sum(r_j^2-r_j)+sum(v_j^2-v_j)<=e^2-2e. (M)

Rearrange exact(B), using S=3t, to

 qD=2e+e^2-2m-m^2-sum r_j^2+V-sum v_j^2,
 D=(ell-3)e+2m-V=(ell-1)e-2t-V.

From(M), the right side is at least4e-3m-S=e. Thus qD>=e>0
and D is an ORDINARY positive integer, so D>=1. No F2-definition,
coefficient orbit divisibility, global component through P, or
irreducibility of the product U is required. This is the essential
place where a falsely irreducible multiplicity bound would fail;
the actual proof does not make that error.

## 6. Second global completion, with all coefficients checked

Reapply Cauchy to the qD equality and substitute
B0=(ell-1)e-D and V=B0-2t. With a=(ell+2)/(ell-1), its upper side is

    (ell-1)e-D+2et-a*t^2-(B0-2t)^2/o.

The negative t^2 coefficient is -(a+4/o)=-Aell/o. The global
completed-square contribution is

    [o*e^2+4eB0-a*B0^2]/Aell
    =[-(ell-1)e^2+2ell*eD-a*D^2]/Aell.

This independently verifies every sign, particularly the eD and D^2
terms. Moving terms then yields

 D[q+1-(2ell/Aell)e]
 <=(ell-1)e-(ell-1)e^2/Aell
                       -[(ell+2)/((ell-1)Aell)]D^2
 <=(ell-1)Aell/4.                                 (II)

The e maximum is at Aell/2 over all reals. No positivity of the
left bracket was needed to derive the inequality; that positivity
is established separately below. No divisibility in characteristic2
was used in the rational real coefficients.

## 7. CG3: small-factor constraint and all threshold endpoints

If reduced phi is reducible, its least-degree absolute component
has0<e<=N/2. No F2 factor is needed to choose it. Let
e0=(ell-2)q/2. Then N/2-e0=q-1>0. For
P(e)=e^2-N e+Aell(q+1)^2/4, exact substitution gives

 P(e0)=(ell-2)/4[-q^2+2(ell+3)q+(ell+1)].

At q0=2ell+7 the bracket is -ell-6; its derivative in real q is
negative for q>=q0. Thus P(e0)<0 throughout that range. P is
nonincreasing through e<=N/2 and strictly decreases below its
endpoint. Consequently P(e)<0 for EVERY e in[e0,N/2], including
both endpoints. Inequality(I) forces the STRICT e<e0.

It follows that

    q+1-(2ell/Aell)e > q/(ell+1)+1 >0.

Only now multiply this positive lower bound by D>=1. If q>=Lell,
its left side in(II) is strictly greater than
q/(ell+1)+1>=(ell-1)Aell/4+1, a contradiction. The strict1 margin
survives both possible threshold equalities. No rounded-degree,
small e, m0, V0, equal-degree or missing-P exception remains.

For k>=4, q>=Q^4 while Lell=(Q-2)(Q-3)Q^2/4<Q^4/4, and
2ell+7=2Q+5<Q^2. Thus EVERY s>=3,k>=4 satisfies the explicit
threshold. The result is only a restricted family. The accepted
s3 special FS theorem covers more cases and is not weakened.
k1 is outside the threshold; no blanket decision is made for k2,
k3, arbitrary binary weight or other odd parts. Nothing reproduces
the known preliminary sufficient construction.

## 8. Adversarial limits and source distinction

I challenged projective-infinity omissions, factors missing P, repeated
or nonhomogeneous factors, possible zero multiplicities, lack of orbit
transitivity, unequal degrees, infeasible quadratic maximizers, incorrect
reduced-genus use, denominator signs and threshold equality. The complete
reconstructions above resolve those challenges within the exact domain;
no real counterexample or unresolved proof gap was found.

Hernando–McGuire Theorem16 states ell divides q-1 AND ell!=q-1,
and supplies an absolute F2 COMPONENT. This is sufficient for that
attribution in the claimed large-q regime, not at k1. The constructor
source-audit's shortened divisibility wording must not be extended
to k1; this is recorded as closed source note N3, not an imported
step. Their component theorem is never substituted for CG3.
The recent Frobenius paper additionally assumes an absolutely
irreducible hypersurface, condition(A) and strict p^r<q. It cannot
prove CG3 from a displayed q-th-power gradient. CG does not use it.
The Férard sequel remains unread in its operative body; priority
and possible overlap with published classifications are unresolved.

All nine target files, all56 rows, exact accepted scopes, primary
read limits and metadata code are covered. The ledger and source
records are part of this initial report, not a future promised
extension. No C NEW CG material was read or hashed before the
ENTIRE review freeze. Send only completion identity until BOTH
independent entire initials are confirmed. Coordinator alone may
promote after reading/reconciling both complete packages.
