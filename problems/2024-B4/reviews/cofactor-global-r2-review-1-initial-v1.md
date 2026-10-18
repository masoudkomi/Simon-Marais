# ENTIRE initially blind OTHER WHOLE CG1--CG3 review R1

2026-10-18 UTC. Reviewer `/root/review_2017_coarsening_r1` (C).
The submission is **candidate proof - unverified**. Root is its sole
NEW constructor and is excluded. I supplied no new CG inference, and
read no corresponding B CG review, finding, file, hash or metadata
before this ENTIRE initial packet was frozen. All56 author obligations
are reconstructed below and in the individual ledger. Mathematical
verdict and findings are withheld from root until BOTH entire initials
are confirmed frozen; the first completion notice is identity only.

Internal verdict: I found no substantive mathematical defect or
required proof repair in CG1--CG3 within the displayed threshold
hypotheses. One source-context qualification is retained: HM Theorem16
requires a PROPER divisor, not merely ell|q-1. That condition is
automatic under CG3's threshold, whereas the k1 endpoint is not within
that source theorem. HM is not a premise of the new proof. This closed
scope note neither certifies the broader source sentence for k1 nor
changes the proposed CG theorem. Coordinator reconciliation and the
OTHER whole review remain necessary; this is not promotion.

I authored older2024 CP/sector3 work and reviewed older structural,
FP and FS packets. Generic original-source preparation for FS supplied
no problem-specific CG construction. Those separately accepted inputs
are not being independently self-recertified here. The new ALL-Q
geometry, both completions and threshold are independently reconstructed,
rather than inferred from those older proofs or from constructor checks.
Requested inherited gpt-6.1-sol/max; independently effective readback
unavailable. No mathematical executable, CAS, scan or author rerun.

## 1. Exact target, family and dependency boundary

The actual official question is coefficientwise factorization over F2
of the homogeneous quotient phi_n, with BOTH factors of positive degree.
It is not a question about functions on F2³ or about having a factor
only after extending coefficients. The submission excludes a restricted
family by proving the stronger WHOLE absolute irreducibility. It does
not purport to classify all official odd exponents or solve(a).

Write

    Q=2^s, s>=3; ell=Q-1; q=Q^k, k>=1;
    n=ell*q+1; N=n-3=ell*q-2;
    A=(ell-2)(ell+1); o=(ell-1)(ell-3);
    L=(ell-1)(ell-2)(ell+1)^2/4.

Then ell>=7 is odd, q fixes F_Q, and n has bit0 and the s consecutive
bits sk,...,sk+s-1. These sets do not overlap, so its binary weight
is s+1>=4. Accepted T1 therefore excludes ALL absolute line factors,
not just F2 lines. N>0 and the numerator is nonzero: the coefficient
of X^(n-1)Y is1. Thus neither the n1 zero convention nor n3/unit
case occurs in this parameter family.

The complete accepted structural, FP and FS bodies and current scopes
were read. Only the no-absolute-line assertion is needed as an external
accepted problem-specific premise in the new deductions. General
singularities and contacts are rederived. FP's unique component and
FS's special S4/Frobenius uniformity are NOT assumed for larger Q.
The live general/Frobenius notes are explicitly unverified history,
not authorities. The classical curve facts have their hypotheses
checked in Section6 below and the source record.

The proposed sufficient irreducibility threshold is exactly

    q>=max(2ell+7,L).                             (R1)

This permits some smaller k in particular fields but does not decide
EVERY k1/k2/k3. The uniform corollary k>=4 is a sufficient symbolic
comparison; it does not override the separately stronger accepted
Q8 result at k2.

## 2. Reducedness and the complete projective singularity list

Put W=X+Y+Z and f=X^n+Y^n+Z^n+W^n, R=(X+Y)(Y+Z)(Z+X).
Polynomial divisibility by R and the official quotient interpretation
are established context, not a new preliminary construction.

Because n is odd and n-1=ell*q,

    f_X=(X^ell+W^ell)^q,
    f_Y=(Y^ell+W^ell)^q.

The ell roots are exactly F_Q*, all simple. The first derivative base
splits into lines with vectors(1+z,z,z); the second into lines with
vectors(h,1+h,h), z,h nonzero. Proportionality would give from Z
and X the simultaneous identities z=c*h and1+z=c*h, impossible.
There is no common line, hence no common factor in the split bases
or their qth powers. A repeated factor of f would divide BOTH
partials. Thus f and its quotient phi are reduced.

Homogeneous factors require no hidden assumption: if U*H has degree
spread0, additivity of its least and greatest nonzero total degrees
in a domain forces both spreads0. Every factor can be treated as a
homogeneous plane curve. Accepted T1 removes any degree1 absolute
component of phi.

If T is singular on phi, differentiation of f=R*phi gives all partials
of f zero even when R(T)=0. Permute coordinates so one nonzero
coordinate is Z, then normalize Z1. With alpha=X,beta=Y and
lambda=alpha+beta+1, the X/Y derivative equations give
alpha^ell=beta^ell=lambda^ell=u. Since alpha+beta+lambda=1,

    f(alpha,beta,1)=u^q+1.

Its zero forces u=1 by injectivity of Frobenius. Therefore alpha,
beta,lambda are all nonzero members of F_Q. In particular no singular
point can lie on ANY of X0,Y0,Z0,W0. This chart argument is complete:
some coordinate is always nonzero, and its permutation does not change
the polynomial. It does not miss infinity points.

Conversely the local cones in Section3 below show every projective
F_Q point outside those four lines IS singular. The complement count
is exact. Four general-position lines have4(Q+1) incidences, six
distinct double intersections and no triple intersection, giving union
4Q-2. Subtracting from Q²+Q+1 leaves

    Q²-3Q+3=ell²-ell+1.

Each prescribed diagonal has Q+1 points, exactly two on that union.
Its ell remaining points contain P111; the three diagonals intersect
only at P. Thus the complete singularities are

    P; 3(ell-1) non-P diagonal points;
    o=(ell-1)(ell-3) off-diagonal points.

Neither a transitive action on the last set nor an F2-definition of
an individual factor is needed or asserted.

## 3. Three exact ordinary cones, independently expanded

For a nonzero a in F_Q, q fixes a and a^ell=1. Expansion of
(a+x)(a^q+x^q)^ell shows the constant, linear, q and q+1 coefficients
of(a+x)^n are respectively a,1,1,a^-1. Every remaining degree is
at least2q. Since q>=8, no omitted term interferes with the first
surviving pieces below.

At P take X=1+x,Y=1+y,Z1. Constant, linear and q-degree pieces
cancel. The degree q+1 part is x^q*y+x*y^q. Here R=xy(x+y)
exactly, so the quotient cone is

    (x^(q-1)+y^(q-1))/(x+y)
      = product_(b in F_q minus{0,1})(x+b*y).

It has q-2 distinct lines. The directions x0,y0,x+y0 are absent;
P is ordinary and all three prescribed diagonals are transverse.

At a non-P diagonal point(b:1:1), let c=b+1 and E=b^-1. With
X=b+x,Y=1+y the first numerator piece is

    E*x^(q+1)+y^(q+1)+E*(x+y)^(q+1)
      =y[E*x^q+E*x*y^(q-1)+(1+E)*y^q].

The denominator starts c²*y. Since(1+E)/E=c, the quotient cone is
(E/c²)[x^q+x*y^(q-1)+c*y^q]. Its affine polynomial x^q+x+c has
derivative1; y0 is not a factor. Thus this point is ordinary of
multiplicity q and the prescribed diagonal y0 is transverse. There
are no vanishing denominators b0/c0, as those cases were excluded
in the point list.

At an off-diagonal point, R is a unit. Put lambda=alpha+beta+1 and

    a=alpha^-1+lambda^-1,
    b=beta^-1+lambda^-1, d=lambda^-1.

Its leading numerator is

    a*x^(q+1)+b*y^(q+1)+d*(x^q*y+x*y^q).

The two gradient entries are a*x^q+d*y^q and d*x^q+b*y^q. The
coefficient determinant equals

    ab+d²=(lambda+alpha+beta)/(alpha*beta*lambda)
          =1/(alpha*beta*lambda) !=0.

Hence no nonzero projective common gradient zero exists. The binary
homogeneous form has degree q+1 and is squarefree; over K it is a
product of q+1 distinct lines. Thus every remaining listed point is
ordinary of multiplicity q+1. This also supplies the required converse
to the complete singularity classification in Section2.

## 4. Exact contacts and exact Bezout, including factors missing P

Let phi=U*H, degU=e and degH=N-e, both positive. Reducedness makes
them coprime. Write m=mP(U), r_j for diagonal multiplicities and v_j
for off-diagonal multiplicities; t=e-m,S=sum r_j,V=sum v_j.

At a listed ordinary point, the two tangent cones partition its
distinct lines. They share no tangent, so their local intersection
number is exactly the product of their multiplicities. A point common
to U and H is necessarily singular on their product phi. There are
therefore no missing terms outside the complete list. All multiplicity
quantities are ORDINARY integers; none of the subsequent divisions
or inequalities takes place in characteristic2.

To check the restriction rather than assume it, differentiate the
identity f=R*phi transversely to Y=Z. On that line its numerator
derivative is X^(n-1)+Y^(n-1), while the derivative of R is(X+Y)².
This yields the polynomial identity

    phi(X,Y,Y)=(X^(ell*q)+Y^(ell*q))/(X+Y)².

It has degree N and is nonzero at(1:0:0). Its roots are the ell
simple ellth roots, raised to q; division subtracts two at P and
nowhere else. Contacts are q-2 at P and q at the other ell-1 points.
Section3 proves the line is transverse to the WHOLE curve at all
these points, hence to each factor. Degree e restriction consequently
has total e=m+sum_on_line r_j. No diagonal is a component by T1.
Sum over the three lines to obtain S=3t, even if m0.

Projective Bezout is now exactly

    e(N-e)=m(q-2-m)+qS-sum r_j²
                         +(q+1)V-sum v_j².       (R2)

This equality, rather than a subset of singularities or an orbit
average, supports BOTH later completions.

## 5. First global completion and a necessary factor-degree polynomial

The diagonal count gives sum r_j²>=3t²/(ell-1). The off-diagonal count
gives sum v_j²>=V²/o, with o>0 because ell>=7. Its entire V quadratic
obeys (q+1)V-V²/o<=o(q+1)²/4 for EVERY real V.

Substitute m=e-t,S=3t in(R2), then subtract e(N-e). I obtain

    0<=-(ell-1)q*e+2(e+q+1)t
                  -(ell+2)/(ell-1)*t²+o(q+1)²/4.

The t-quadratic has GLOBAL maximum
(ell-1)(e+q+1)²/(ell+2). Factoring the remaining upper bound gives

    0<=(ell-1)/(ell+2)
          [e²-(ell*q-2)e+A(q+1)²/4].             (R3)

For verification, its constant coefficient in(q+1)² is
1+(ell+2)(ell-3)/4=A/4, and its linear e coefficient is2-ell*q.
Thus P(e)=e²-Ne+A(q+1)²/4 is nonnegative for every actual proper
factor. Neither maximizing V nor maximizing t is asserted to be an
actual integer, feasible point, or compatible multiplicity choice.
Allowing an infeasible maximizer only enlarges an upper bound.

## 6. Characteristic-two multiplicity bound, reduced correction, D>=1

For an absolute irreducible degree d>=2 curve, a nonzero polar of
degree d-1 exists: all zero partials over perfect K would make its
equation a square. Polar Bezout bounds
delta=sum binom(mP,2)<=d(d-1)/2. Degree d-1 forms have vector dimension
M=d(d+1)/2. Conditions of order mP-1 impose at most delta linear
constraints. Add M-delta-1 distinct smooth points; their number is
nonnegative and infinitely many smooth K points are available. A
nonzero form survives and shares no component with the degree d
irreducible curve. Bezout gives d(d-1)>=2delta+M-delta-1, or
delta<=(d-1)(d-2)/2. This is the classical Fulton proof, valid here
without a characteristic-zero tangent-genericity hypothesis.

For reduced U=product U_i, absolute degrees d_i, let c be their number.
At every point use binom(sum m_i,2)=sum binom(m_i,2)+sum_(i<j)m_i*m_j.
Apply the bound individually and bound the cross products by pairwise
Bezout. This gives

    sum_P binom(mP(U),2)
      <=(e²-3e+2c)/2
       =(e-1)(e-2)/2+c-1
      <=e(e-2)/2,                               (R4)

since T1 gives every d_i>=2 and c<=e/2. This is the indispensable
REDUCED correction. Applying the irreducible bound to U directly
would have been wrong; the submitted proof does not do so.

Restrict(R4) to the listed points to get

    m²+sum r_j²+sum v_j² <= e²-2e+m+S+V.         (R5)

From exact(R2), define D=(ell-3)e+2m-V=(ell-1)e-2t-V. Moving all q
terms gives

    qD=2e+e²-2m-m²-sum r_j²+V-sum v_j².

Use(R5), S=3t and e=m+t to obtain qD>=4e-3m-3t=e>0. The field of
definition of U has no role in its integer multiplicities. D is an
ordinary INTEGER, so D>=1. This is not a presumed sign or a genus
claim about a reducible curve.

## 7. Second GLOBAL completion, with each coefficient checked

Apply both Cauchy bounds directly to the qD identity and put
B=(ell-1)e-D, a=(ell+2)/(ell-1). Since V=B-2t, I obtain

    qD <=(ell-1)e-D+2et-a*t²-(B-2t)²/o.          (R6)

Its t² coefficient is -(a+4/o)=-A/o. The maximum of the last three
terms is

    [o*e²+4eB-a*B²]/A
      =[-(ell-1)e²+2ell*eD-a*D²]/A.

The identity follows by expanding B: the e² coefficient becomes
o+4(ell-1)-(ell+2)(ell-1)=-(ell-1), and the eD coefficient becomes
-4+2(ell+2)=2ell. Thus the exact submitted completed-square upper
bound is correct, including its negative D² term. Rearrangement gives

    D[q+1-(2ell/A)e]
      <=(ell-1)(e-e²/A)-a*D²/A
      <=(ell-1)A/4.                              (R7)

The last completion is at e=A/2 over all real e, followed by dropping
a nonpositive term. No positivity of the left bracket has been used
yet. It must come from the independent factor-degree bound next.

## 8. Actual degree control and strict threshold contradiction

If phi is reducible, its reduced absolute decomposition has at least
two components. One of minimum degree supplies 0<e<=N/2. No greedy
grouping, equal-degree assumption or unique large component is needed.

Put e0=(ell-2)q/2. Then N/2-e0=q-1>0. Direct substitution in P yields

    P(e0)=(ell-2)/4[-q²+2(ell+3)q+(ell+1)].       (R8)

At q=2ell+7 the bracket is -ell-6; its derivative is negative beyond
that point. Under(R1), P(e0)<0. Since P'(e)=2e-N<=0 throughout
e<=N/2, all e in[e0,N/2] violate P(e)>=0. Therefore e<e0 strictly,
with no integer assumption on e0 needed.

The bracket in(R7) now satisfies

    q+1-(2ell/A)e > q+1-ell*q/(ell+1)
                          =q/(ell+1)+1>0.

Multiplication by D>=1 is safe. The left side of(R7) is strictly
greater than q/(ell+1)+1. But q>=L makes this at least
(ell-1)A/4+1, contradicting(R7). The strictness and +1 retain the
threshold endpoints. This proves the candidate CG3 conclusion if
both independent reviews and coordinator reconciliation accept it.

For k>=4, q>=Q^4 and L=(Q-2)(Q-3)Q²/4<Q^4/4. Also2ell+7=2Q+5
<Q²<=q for Q>=8. Hence the stated all-s/all-k>=4 family follows by
symbolic inequalities, not a tested exponent table. For k1 neither
threshold holds in general and no claim is made. For small k2/k3 the
exact sufficient threshold, rather than a blanket verdict, governs
this theorem. The separately accepted Q8 special result stays stronger
at k2 and is not weakened.

## 9. Adversarial degeneracies, source qualification and limits

I explicitly checked: m0; some or all r_j/v_j zero; complementary
unequal degrees; U reducible but squarefree; U defined only over K;
factors missing P; infinity/chart permutations; diagonal contacts at
P versus elsewhere; no hidden diagonal component; q8 geometry versus
the stronger threshold; ell>=7 ensuring positive Cauchy denominators;
real maximizers outside feasible multiplicity boxes; D integrality
over arbitrary coefficient fields; and all strict inequality endpoints.
No counterexample or missing premise emerged for CG1--CG3.

Closed source-context qualification CGR1-N1: actual HM Theorem16 assumes
ell|2^i-1 AND ell!=2^i-1, and concludes an absolute irreducible factor
defined overF2. Here i=sk. The proper-divisor condition holds for k>=2,
in particular under q>=2ell+7, but not for k1. Thus the submission's
short phrase 'this divisor regime' must be read within its actual
whole-irreducibility threshold when attributing that component theorem;
it is not an all-k1 component assertion. The context should retain
the word PROPER if reused separately. The proof of CG does not use
HM, so no new mathematical argument or author repair is needed for
the exact stated theorem. No full HM proof or source classification is
silently accepted from an abstract.

Fulton's original §5.4 Theorem2 complete proof, local multiplicity
property and AppendixA were read. The actual char2 verification above
avoids generic tangent lines, Hessians or the characteristic-zero-only
parts nearby. Férard2017 remains an unread priority source; no absence
of a theorem there or novelty follows. The Gauss-map/Frobenius lead is
not used: no separability, component-field descent or strict-exponent
hypothesis is assumed verified by the displayed q-power gradients.

Absolute irreducibility over K implies the required absence of two
positive-degree F2 factors for the displayed restricted family. It is
not merely existence of an F2-defined absolute component. The result
does not give the complete ordinary reducibility classification for
all odd n, decide every smaller k, or prove the annual problem solved.

## 10. ENTIRE packet, blindness and administrative scope

All nine constructor artifacts, all56 obligations and code/metadata
were read. The16 declared protected old identities are verified
directly in this review's administrative freezer. Complete accepted
structural/FP/FS bodies and current authority scopes were read; an
initial combined FS display clipped a middle range, then bounded
overlapping reads recovered that ENTIRE text before this claim.
The original structural accepted copy has a documented editorial
heading change, so no false whole-byte-suffix assertion is made.
FP/FS accepted suffixes are checked under their actual authorities.

The new review contains ALL56 individual dispositions, explicit issues,
primary read scopes, worklog, administrative-only code and all compact
metadata. It creates only the assigned NEW review prefix. The immediate
own632->642 constructor parent binds older bytes compactly. No
corresponding B new CG report, finding, filename content, hash or metadata
was opened; no constructor program/certificate or mathematical code
was rerun. No cache/source/shared/Git mutation, cost, contact, restriction
bypass, pending approval or native mathematical child occurred.

This report is the ENTIRE initial OTHER WHOLE R1, not an acceptance
authority. Its mathematical verdict remains withheld until both entire
initials freeze. Root alone may reconcile/promote exact scopes after
both reviews and any substantive repairs; neither hashes nor this
reviewer's confidence supplies a full annual proof or novelty.
