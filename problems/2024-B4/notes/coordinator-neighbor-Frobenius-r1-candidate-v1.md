# Neighbor-Frobenius criterion for whole absolute irreducibility

18 October 2026, Brisbane. **Candidate proof - unverified.**
Constructor: coordinator /root, solely responsible for the NEW argument.
Requested gpt-6.1-sol/max; independent effective-setting readback unavailable.
TWO OTHER fresh initially blind ENTIRE WHOLE nonconstructor audits and
coordinator reconciliation are required. No priority or annual solution
is claimed. Only the open 2024 B4(b) classification is investigated.

## 0. Official target and proposed claims

Over K=algebraic closure of F2, put

    f_n=X^n+Y^n+Z^n+(X+Y+Z)^n,
    R=(X+Y)(Y+Z)(Z+X), phi_n=f_n/R.

The established quotient is the official coefficientwise target:
two positive-degree F2 factors of phi_n are required. An absolute
splitting alone does not meet that target. Here n is odd and positive,
and the quotient has positive degree; no n1/n3 boundary convention or
preliminary family is substituted.

**NF1.** Let a>=2, q=2^a, and let ell>=3 be odd. If

    ell divides (q-2) OR ell divides (2q-1),             (NF)

then the WHOLE phi_(q ell+1) is absolutely irreducible. Equivalently the
arithmetic tests are ell | (2^(a-1)-1) OR ell | (2^(a+1)-1).
The first equivalence uses ell odd. Thus none of these n qualifies in(b).

**NF2.** Under the same hypotheses, every positive factorization
phi_n=UV over K would have its entire projective common-zero set
contained in P=(1:1:1). The ordinary cone there and Bezout then
contradict the degree. This is an intermediate impossibility argument,
not an assertion that all individual components must pass P.

**NF3.** In particular, for every a>=2 with 3 not dividing a,

    n=7*2^a+1

is excluded. These exponents have exactly FOUR binary1s. This is a
proper subfamily of the unresolved binary-weight>=4 sector. The a2
instance n29 is already covered by McGuire's published thesis Theorem8.
No novelty is claimed for that example or for the general criterion.
Exponents with 3|a, including the familiar n57 parameter, are NOT decided
by NF3; the local single-tangent argument genuinely fails there.

The arithmetic hypotheses imply gcd(ell,q-1)=1: a common divisor
would divide consecutive q-2,q-1 in the first case, or would make
2q both1 and2 in the second. Therefore no nontrivial ell-th root
belongs to F_q.

The proof below supplies ALL special local/projective arguments.
The only general imported facts are classical projective Bezout and
the local intersection product formula for disjoint tangent cones.
Their actual operative primary statements were read in Hernando--McGuire,
0903.2016v4 Section3.2/Corollary8. We do NOT import its absolute-component
existence theorem as whole irreducibility, or its Theorem15 without
its ordinary-irreducibility assumption. The method is attributed to
Janwa--McGuire--Wilson/McGuire singularity arguments. Accepted old
T1/S3/three-bit results are context, not needed as mathematical premises
of this self-contained proof.

## 1. Elementary unit-cofactor lemma

In a two-variable local expansion over K, suppose a nonzero polynomial
or power series H starts at degree m with c L^m, c!=0 and L linear,
and its next homogeneous term H_(m+1) is NOT divisible by L.
Then H cannot be a product of two series both vanishing at the point.

Indeed, if H=AB with positive orders s,t, then s+t=m and their initial
forms are nonzero scalar multiples of L^s,L^t. The degree m+1
product term is A_s B_(t+1)+A_(s+1) B_t. Each summand is divisible
by L since s,t>=1. This contradicts the displayed next term.
Thus a vanishing factor has a UNIT cofactor. Multiplication by a
local unit and invertible local coordinate changes preserve the
conclusion. We use this property, rather than an unsupported inference
from the total multiplicity alone.

## 2. Global squarefreeness and homogeneous coprime factors

Write W=X+Y+Z and n=q ell+1. Formal differentiation gives

    f_X=(X^ell+W^ell)^q, f_Y=(Y^ell+W^ell)^q.           (1)

As ell is odd, each polynomial before the qth power splits into
distinct lines indexed by ell-th roots zeta,eta. The line coefficient
vectors are (1+zeta,zeta,zeta) and (eta,1+eta,eta).
If proportional with scalar c, their Z and X coordinates give
zeta=c eta and 1+zeta=c eta, impossible. Thus the two partials are
coprime, even after their qth powers. A repeated irreducible factor
of f_n would divide both derivatives, also when its repeated power
differentiates to zero in characteristic2. Hence f_n and phi_n are
globally squarefree.

The numerator is nonzero: its mixed coefficient X^(n-1)Y is1.
Thus N=deg(phi_n)=q ell-2. Factors are homogeneous: the least and
greatest total degrees of a product add in a polynomial domain, and
a homogeneous product has degree spread zero. Any absolute reducibility
therefore yields coprime homogeneous U,V of positive degrees. We will
exclude EVERY such factorization.

## 3. Complete projective singularity list

At a singular point (alpha,beta) of phi in Z1, the product f=R phi
gives f=f_X=f_Y=0, also when R=0. Put lambda=alpha+beta+1.
Injectivity of qth powers in K gives

    alpha^ell=beta^ell=lambda^ell=u.

The numerator value is (alpha+beta+lambda)u^q+1=u^q+1. Hence u=1.
In particular alpha,beta,lambda are all NONZERO ell-th roots.
This is a necessary list for shared factor zeros; no point with a
zero denominator is silently retained in subsequent divisions.

The list splits into P=(1,1), points on one of the three prescribed
diagonals, and off-diagonal points

    alpha!=1, beta!=1, alpha!=beta,
    alpha,beta,lambda nonzero ell-th roots.             (2)

On a diagonal other than P the point is a coordinate permutation of
(b:1:1), b^ell=1,b!=1; when X=Y a normalization by b replaces b
by b^-1. All required divisions are by nonzero roots.

This is genuinely projective. Any nonzero homogeneous coordinate can
be permuted into Z and scaled to1, since f,R and phi are symmetric.
The same deduction forces the other two coordinates nonzero.
Consequently a singularity with any zero coordinate is impossible,
including every possible point at infinity of the original Z1 chart.
Thus the list above contains every possible projective common zero
of U,V, because a common zero is singular on their product.

## 4. The ordinary point P

Set X=1+x,Y=1+y,Z1. The exact denominator is xy(x+y).
Since ell is odd,

    (1+t)^n=(1+t)(1+t^q)^ell
            =1+t+t^q+t^(q+1)+terms of degree>=2q.

Constants, linear terms and pure qth powers cancel in the four-term
numerator. Its first nonzero term is x^q y+x y^q. Therefore phi has
order q-2 at P and initial form

    C=(x^(q-1)+y^(q-1))/(x+y)
      =product_(b in F_q minus F2)(x+b y).              (3)

It has q-2 DISTINCT tangent directions, with none of x0,y0,x+y0.
In any factorization U,V the initial cones partition these directions,
so they share no tangent. The local intersection at P is exactly
m_P(U)m_P(V), including value0 if either factor misses P.
There is no repeated component or extra local intersection hidden here.

## 5. All nontrivial diagonal points have a unit cofactor

At (b:1:1), let c=b+1, E=b^-q, B=1+b^(1-q).
Here b!=0,1, so c,E are nonzero. The arithmetic gcd condition makes
B!=0: B0 would put the nontrivial ell-root b in F_q.

Translate X=b+x,Y=1+y,Z1. Direct binomial expansion gives

    R=c²y+cy²+x²y+xy²,
    (f)_q=B y^q,
    (f)_(q+1)=y[E x^q+E x y^(q-1)+(1+E)y^q].          (4)

There are no intervening positive degrees below q. Dividing in f=R phi
first gives the degree-(q-1) quotient piece (B/c²)y^(q-1), then

    (phi)_q=(E/c²)x^q+(E/c²)x y^(q-1)
                   +[(1+E)/c²+B/c³]y^q.               (5)

The B/c³ correction comes from cy² times the preceding quotient piece.
The NONZERO x^q coefficient shows that (5) is not divisible by y.
The unit-cofactor lemma with m=q-1 excludes simultaneous vanishing
of two factors here. Coordinate symmetry covers the other two
diagonals. Thus no nontrivial diagonal point is a common zero of U,V.

## 6. The two off-diagonal homogeneous pieces

At a point satisfying(2), R is a local unit. The degree-q and degree-(q+1)
pieces of the numerator in X=alpha+x,Y=beta+y,Z1 are

    H_q=A x^q+B y^q,
    A=alpha^(1-q)+lambda^(1-q),
    B=beta^(1-q)+lambda^(1-q),

    H_(q+1)=(alpha^-q+lambda^-q)x^(q+1)
             +(beta^-q+lambda^-q)y^(q+1)
             +lambda^-q(x^q y+x y^q).                 (6)

Lower positive pieces vanish. These follow directly from the first
two nonzero binomial terms of degree q and q+1; all terms from the
next ell-bit begin at degree at least2q>q+1.

We show H_q is a nonzero power of ONE line L and that H_(q+1) is
not divisible by it, for BOTH alternatives of(NF). The unit-cofactor
lemma applies to f=(RU)V; since R is a unit at this point, it then
excludes simultaneous vanishing of U,V. No unproved quotient
expansion or ordinary-point claim is needed at an off-diagonal point.

## 7. First neighbor: ell divides q-2

In this case qth powers on every ell-th root equal squares.
Let F=F2(alpha,beta,lambda), a finite field. The q-Frobenius and
ordinary square maps agree on its generators, hence on all of F.

For concision in this section write u=alpha+1,v=beta+1.
Then lambda=1+alpha+beta, and alpha,beta,lambda,u,v,alpha+beta
are all nonzero by(2). Equation(6) gives

    A=alpha^-1+lambda^-1=v/(alpha lambda),
    B=beta^-1+lambda^-1=u/(beta lambda).

Both are nonzero. The unique qth root t of A/B lies in F because
q-Frobenius is an automorphism of the finite field F. It is also the
unique root in K by injectivity. Hence t^q=t² and

    t²=D=beta*v/(alpha*u)!=0.                          (7)

The line L can be written y+t x; thus its point x1 is y=t.
Evaluating the next piece using t^q=t² gives the SAME cubic value

    h=H_(q+1)(1,t)
      =(alpha^-2+lambda^-2)
       +(beta^-2+lambda^-2)t³+lambda^-2(t+t²).

Multiply by lambda², use lambda+alpha=v and lambda+beta=u,
then substitute(7):

    lambda² h = v²/alpha² + (u²/beta²)t³+t+t²
              = v²/alpha² + D
                    +t[uv/(alpha beta)+1]
              = lambda*[v/(alpha² u)+t/(alpha beta)].  (8)

Here uv+alpha beta=lambda; every equality is an exact field identity.
If h were zero, (8) would force

    t=beta*v/(alpha*u)=D=t².

Then t0 or1. Equation(7) excludes0. If t1, beta(beta+1)=alpha(alpha+1),
so (alpha+beta)²+(alpha+beta)=0. Distinct alpha,beta exclude
alpha+beta0; the remaining alpha+beta1 makes lambda0, impossible.
Therefore h!=0. The sole tangent line is not a factor of the next
piece; the off-diagonal point has a unit cofactor.

This reasoning is uniform in a and ell and uses no finite-field table.

## 8. Second neighbor: ell divides 2q-1

Now alpha^(2q)=alpha, and similarly for beta,lambda. Put
u=alpha+1,v=beta+1 again. Squaring the first coefficients in(6) gives

    A²=alpha+lambda=v, B²=beta+lambda=u.

Moreover ((v)^q)²=v and ((u)^q)²=u. Square injectivity gives
A=v^q,B=u^q, so the exact sole tangent is

    L=v x+u y, t=v/u at x1.                           (9)

Every denominator is nonzero. Rational expressions in the singular
coordinates obey t^(2q)=t. Square h=H_(q+1)(1,t) in(6) and use these
2q identities:

    lambda h² = v/alpha+(u/beta)t³+t²+t
               = (v/u²)[u²/alpha+v²/beta+v+u]
               = v*(alpha+beta)/(u² alpha beta).      (10)

For the last equality, u²/alpha=alpha+alpha^-1,
v²/beta=beta+beta^-1, and u+v=alpha+beta.
All factors in the final numerator and denominator are nonzero by(2).
Thus h²!=0 and h!=0. Again the unique tangent does not divide the
next homogeneous piece, so the point has a unit cofactor.

This is the local mechanism in McGuire's thesis Theorem8, with the
Frobenius congruence stated explicitly rather than only its displayed
special exponent family. It is attributed, not claimed as a new method.

## 9. Whole projective Bezout contradiction

All projective common zeros of coprime U,V are now confined to P.
Their tangent cones there are disjoint by(3). Classical projective
Bezout therefore gives

    deg U * deg V = m_P(U) * m_P(V).                  (11)

Let e=deg U>0,d=deg V>0. Multiplicities m<=e and m'<=d are
nonnegative. If either is zero, (11) is already impossible.
Otherwise equality of products forces m=e and m'=d: each ratio
m/e,m'/d is at most1, and their product is1. Since multiplicities
of a product ADD,

    q ell-2=deg phi=e+d=m+m'=m_P(phi)=q-2,

contradicting ell>=3. This proves NF1 and the intermediate NF2.
No hypothesis that every component passes P was assumed, and no
old no-line theorem was needed to get the final strict contradiction.

## 10. Four-bit corollary and remaining gaps

For ell7, 2 has order3 modulo7. If a1mod3, q2mod7 and ell|q-2.
If a2mod3, q4mod7 and 2q1mod7, so ell|2q-1.
These are exactly the integers a with 3 not dividing a.
Thus NF3 follows for all a>=2 in that range.
Since 7*2^a=2^a+2^(a+1)+2^(a+2), the binary weight is exactly4.

If 3|a, q is1 on F8. At every off-diagonal F8 point A=B0 in(6).
The single-tangent premise disappears and the first nonzero term
instead has degree q+1. Nothing in the proof excludes splitting in
that branch. Likewise other ell outside(NF), arbitrary four-bit
exponents, the whole binary-weight>=4 sector, sufficient positive
families and the annual classification remain unresolved.

The original coauthor thesis's displayed Theorem8 already proves the
special family ell=2^(a+1)-1; this is included in the second neighbor.
Its complete printed proof on pages24--26 was freshly viewed from
existing images. The present statement is a project deduction with
no priority certification. Jedlicka's general result and Hernando--McGuire's
component theorem are not substitutes for the whole conclusion.
No mathematical program, CAS, scan, factor table, author rerun or
finite-test extrapolation occurs anywhere in the proof.
