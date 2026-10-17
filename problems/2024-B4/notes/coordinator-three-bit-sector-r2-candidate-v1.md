# A complete exclusion of the three-bit sector

2026-10-17 UTC. **Candidate proof - unverified.** Root constructor.
TWO OTHER initially blind WHOLE nonconstructor audits and coordinator
reconciliation are required. This is a separate stronger packet; all
earlier candidate and reviewer bytes remain frozen. It concerns only
open2024B4(b), gives no preliminary construction, and makes no novelty
or full annual classification claim. No mathematical code, CAS, scan,
new factor table or saved certificate supplies any step.

## 0. Exact proposed theorem

Work coefficientwise over F2 and its algebraic closure K. Use the
established quotient

    f_n=X^n+Y^n+Z^n+(X+Y+Z)^n=R phi_n,
    R=(X+Y)(Y+Z)(Z+X).

The official target is a product of TWO positive-degree F2 polynomials
phi_n=UV; an extension-field factor alone is insufficient. The
existence of the quotient is an accepted preliminary input, not proved
again. Fix integers a>=2,d>=1 and put

    q=2^a, r=2^d, ell=r+1,
    n=1+2^a+2^(a+d)=qell+1, N=degphi_n=qell-2,
    g=gcd(ell,q-1).                                    (1)

Every odd exponent with EXACTLY three nonzero binary digits and
n=1mod4 has this unique form. The remaining three-bit odd exponents
are3mod4, already excluded by accepted attributed S3A; no proof of that
published sector theorem is reproduced here.

**Proposed R2 theorem.** For EVERY a>=2,d>=1:

* if n!=13, the WHOLE phi_n is absolutely irreducible;
* for n13, phi13 is irreducible over F2. Our argument needs only
  that any absolute splitting would consist of two quintics exchanged
  by Frobenius; it does not rely on the published Kasami factorization.

Consequently NO odd exponent with exactly three nonzero binary digits
qualifies for the official two-positive-degree-factor target.
The general binary-weight>=4 sector remains open. This does NOT
classify all exponents, produce a new qualifying family, or establish
literature priority. The theorem is UNVERIFIED until the whole protocol.

The new argument counts intersections with EACH of the three diagonal
lines before applying projective Bezout. It does not assume that all
absolute components pass P=(1:1:1), or that phi_n is F2-irreducible.
The older narrow r1 packet is not an accepted premise: its entire
needed local argument is reconstructed in Sections1--3 below.

## 1. Squarefreeness, lines and exact singular locations

Use the exact accepted T1: every odd n with binary weight>=3 has
NO absolute line factor in phi_n. Its complete17079-byte accepted
structural proof was freshly read. T2 and the original1993 Kasami
component theorem are not needed for this stronger proof. In particular
ANY positive-degree divisor A of phi_n satisfies

    degA>m_Q(A) at EVERY projective point Q.             (2)

Indeed equality would, after an invertible projective change putting
Q=(0:0:1), make A a binary homogeneous polynomial in the two local
coordinates. Over K it splits into lines, contradicting T1. This
argument also covers a reducible divisor, not just a component.

Here is the complete source-free squarefreeness argument. With
W=X+Y+Z, the first partials of f_n are

    f_X=(X^ell+W^ell)^q, f_Y=(Y^ell+W^ell)^q.

The polynomials before the q-th powers split into distinct lines
X+zeta W and Y+eta W, with zeta^ell=eta^ell=1, because ell is odd.
Their coefficient vectors(1+zeta,zeta,zeta),(eta,1+eta,eta) cannot
be proportional: the Z and X coefficients would imply zeta=c eta
and1+zeta=c eta. The partials are thus coprime. A repeated factor
of f_n would divide BOTH, so f_n and phi_n are squarefree. Every
partition of absolute components gives coprime homogeneous factors.

Consider a singular point of phi_n in the chart Z1, coordinates
(alpha,beta),lambda=alpha+beta+1. Product differentiation makes
f_n=f_X=f_Y=0 there, even if R0. Injective q-Frobenius gives
alpha^ell=beta^ell=lambda^ell=u, and f_n0 gives
(alpha+beta+lambda)u^q+1=u^q+1=0. Hence

    alpha^ell=beta^ell=lambda^ell=1.                    (3)

All three are nonzero. Since ell=r+1 and r is a power2, raising
lambda=alpha+beta+1 to r gives

    1/lambda=1/alpha+1/beta+1.

For S=alpha+beta,T=alpha beta, multiplication by T(S+1) gives
T=(S+T)(S+1), thus S(T+S+1)=0. Therefore

    alpha=beta, or alpha1, or beta1.                    (4)

No off-diagonal singularity is possible. Symmetry in X,Y,Z and
choosing ANY nonzero coordinate as the last affine coordinate make
this a GLOBAL projective statement. In fact(3) in that chart shows
all coordinates of a singular point are nonzero. No point at infinity
or zero coordinate is silently omitted.

The only possible singular points are P and the three disjoint lists
of coordinate permutations of(b:1:1), with b^ell1,b!=1. The lists
are disjoint because the three diagonals meet only at P. Conditions
(3)--(4) were derived from singularity, not assumed sufficient for
every possible type; the following exact germs decide intersections.

## 2. Ordinary points versus the unit-cofactor points

At P set X=1+x,Y=1+y,Z1. The denominator is xy(x+y) exactly.
From(1+z)^n=(1+z)(1+z^q)^ell the first surviving numerator term
is x^q y+x y^q. Thus phi_n has order q-2 and initial form

    C=(x^(q-1)+y^(q-1))/(x+y)
      =product_(b in F_q minus F2)(x+b y).              (5)

The q-2 tangent lines are distinct; in particular none is y0.

At(b:1:1), b^ell1,b!=1, put c=b+1,E=b^-q,B=1+b^(1-q), and
X=b+x,Y=1+y,Z1. The translated denominator is
c²y+cy²+x²y+xy². The first numerator terms, directly from the
same binomial identity, are

    F_q=B y^q,
    F_(q+1)=y[E x^q+E x y^(q-1)+(1+E)y^q].            (6)

The COMPLETE accepted S3B proof, freshly read, verifies exactly
these formulas for all odd targets; they are also explicitly used
here with all quotient corrections retained.

If b is outside F_q, B!=0. The quotient's first term is
(B/c²)y^(q-1); its NEXT term is

    (E/c²)x^q+(E/c²)xy^(q-1)
       +[(1+E)/c²+B/c³]y^q.                           (7)

The nonzero x^q coefficient means the next term is not divisible
by the sole initial tangent y. Two positive local factors could
have initial terms only y^s,y^t, s,t>=1. Their next product term
would be divisible by y, contrary to(7). Thus at most ONE factor
can vanish here; any vanishing factor has a UNIT cofactor.

If b is in F_q, B0,E=b^-1 and the initial term is instead

    (1/(bc²))[x^q+x y^(q-1)+c y^q].                   (8)

On y1 the bracket has derivative1 and q distinct roots. At y0
its value is x^q, so there is no additional binary-projective root.
This is an ORDINARY q-fold point, with no tangent y0. The common
ell and(q-1) roots are exactly the g-th roots: an integer Bezout
identity proves this, and their distinctness follows from g odd.
There are3(g-1) such ordinary points. P is ordinary of order q-2.

A common zero of two factors is singular on the product. Sections1--2
therefore show their intersections can occur ONLY at P and these
3(g-1) ordinary q-fold points. At such a point the factors' tangent
cones partition distinct lines. The classical coprime-tangent rule
gives EXACT local intersection m_Q(U)m_Q(V), not only a lower bound.
Together with projective Bezout, whose no-common-component hypothesis
was checked by squarefreeness, this supplies every global equality
used below. No original1993 factor theorem is an input.

If g1, P is the only possible intersection. For a factorization
phi_n=UV, Bezout would give degU degV=m_P(U)m_P(V), contradicting
the two strict inequalities(2). Hence WHOLE absolute irreducibility
already holds whenever g1. We may concentrate on g>1 thereafter.

## 3. The new exact diagonal-line equations

Consider any factorization phi_n=UV over K into positive homogeneous
degrees e,N-e, with U,V coprime. Set

    m=m_P(U), h=e-m>0.

For each diagonal L in{X=Y,X=Z,Y=Z}, write mu_Q=m_Q(U) at its
g-1 nontrivial ordinary points, and let t_L count the nontrivial
b outside F_q on that line where U vanishes. This is a count of
actual points, hence a nonnegative integer; no existence is presumed.

The exact homogeneous restriction identity is

    (X+Z)² phi_n(X,Z,Z)=X^(n-1)+Z^(n-1).              (9)

It follows by differentiating f_n=Rphi_n in Y and setting Y=Z,
or from accepted S3B's identity. On this diagonal, the zero at P
has multiplicity q-2, and every b^ell1,b!=1 has multiplicity q.
At(1:0:0) the quotient value is1, so the point at infinity on this
line contributes no zero. No diagonal is a component by T1.

At P and each ordinary point, the diagonal is NOT a tangent to
the whole cone(5)/(8), hence not to any factor. Restricting U to
the line has local zero order EXACTLY m or mu_Q respectively.
At an outside-F_q point the unit-cofactor result(7) gives zero
order q for U if it vanishes, zero otherwise. Projective line
intersection, or the degree-e binary restriction, therefore gives
the EXACT equation for EACH of the three lines:

    e=m+sum_(ordinary Q on L)mu_Q+q t_L.              (10)

Define T=sum_L t_L. Summing the three equations gives

    sum_(all3(g-1) ordinary Q)mu_Q=3h-qT.              (11)

The ordinary multiplicities of V are q-2-m at P and q-mu_Q at
the other points. Consequently GLOBAL Bezout is

    e(N-e)=m(q-2-m)+sum_Q mu_Q(q-mu_Q)
           =3qe-(2q+2)m-m²-q²T-sum_Q mu_Q²
           <=3qe.                                   (12)

Every negative term has its displayed sign and nonnegative magnitude.
There is no hidden contribution from nonordinary unit-cofactor points.
Dividing by e>0 gives N-e<=3q. Interchanging U,V gives e<=3q.
Therefore any factorization requires

    N<=6q.                                          (13)

For d>=3, ell=2^d+1>=9 and N=qell-2>6q for q>=4.
This contradicts(13), proving the WHOLE absolute-irreducibility
claim for EVERY d>=3, with no relative size restriction on a.

It remains to treat only ell5(d2) and ell3(d1), including cases
with small h where a crude product bound would lose information.

## 4. All ell5 targets are absolutely irreducible

Since5 is prime, g is1 or5. The g1 case is already proved.
Assume g5. Every nontrivial ell-root is then in F_q, so all t_L0.
For a hypothetical proper factorization choose e<=N/2=(5q-2)/2.
Each line has FOUR ordinary points, whose mu sum is h by(10).
The elementary sum-of-squares inequality gives sum_(Q on L)mu_Q²
>=h²/4. Applying this to(12), or directly to its first equality,
gives the necessary inequality

    0>= e(5q-2-e)-[m(q-2-m)+3qh-3h²/4]
       =m(4q-2h)+h(2q-2-h/4).                       (14)

If h<=2q, the first term is nonnegative and the second is strictly
positive: 2q-2-h/4>=3q/2-2>0. This is impossible.

If h>2q, then h<=e<5q/2 and m=e-h<5q/2-h. Since4q-2h<0,
the right side of(14) is bounded below by

    (5q/2-h)(4q-2h)+h(2q-2-h/4)
       =3q²+(7/4)(h-2q)²-2h
       >3q²-5q>0.                                   (15)

The final sign holds for every q>=4. Again impossible. Thus there
is no factorization over K. ALL d2 targets are absolutely irreducible;
no class-field, APN or factor-table assertion was used.

## 5. Ell3: the large-excess case and all small-excess exceptions

Now g1 or3; only g3 needs work. All ell-roots lie in F_q, so T0.
Choose an ABSOLUTELY IRREDUCIBLE component U of degree e<=N/2
from a hypothetical splitting. This is possible by taking one of
least degree, as N=3q-2. Write m,h as above. Each line now has
TWO ordinary points with mu sum h. Its squares sum is at least
h²/2. The first equality in(12) consequently yields

    0>= e(3q-2-e)-[m(q-2-m)+3qh-3h²/2]
       =2m(q-h)+(h/2)(h-4)=:E0.                      (16)

If h>q, use m=e-h<=(3q-2)/2-h. Multiplication by the NEGATIVE
coefficient2(q-h) reverses the comparison, giving

    E0>=2((3q-2)/2-h)(q-h)+(h/2)(h-4)
       =q(q-4)/2+(5/2)(h-q)²>0.                     (17)

This is impossible for every q>=4, including q4 because h>q.
If5<=h<=q, both summands in(16) are nonnegative and the second
is positive, also impossible. Thus only h1,2,3,4 remain.

For h1, E0=2m(q-1)-3/2. If m>=1 it is positive forq>=4;
if m0 then e1, forbidden by T1. Thus h1 never occurs.

For h2, E0=2m(q-2)-2. If m>=1 it is positive; only m0,e2
remains. An irreducible conic U over K cannot have multiplicity2
at a point, by the elementary cone argument(2). Thus mu_Q<=1
at every point. Since each pair on a diagonal has sum h2,
U must pass through ALL SIX nontrivial ordinary points.

Let omega,omega² be the two roots of b²+b+1. Those six points
are(omega:1:1),(omega²:1:1) and their coordinate permutations.
NO nonzero quadratic over K passes through all six. To prove this,
write it as AX²+BY²+CZ²+DXY+EXZ+FYZ. At the first pair,
b²=b+1 reduces its value to

    (A+D+E)b+(A+B+C+F).

Two distinct roots force BOTH coefficients zero. The other two
pairs similarly give B+D+F0,C+E+F0 and
A+B+C+E0,A+B+C+D0. Setting S=A+B+C gives D=E=F=S,
then A=B=C=0, hence S=D=E=F=0. This contradicts a nonzero conic.
The calculation is over K: it uses subtraction at two distinct roots,
not an invalid linear-independence claim over K. Thus h2 is excluded.

For h3, E0=2m(q-3)-3/2. If m>=1 it is positive; otherwise
e3,m0. At each pair on a diagonal, sum h3 forces one multiplicity
at least2. The three pairs are disjoint, so there are at least
three distinct double points on the irreducible cubic U. A line
through any two such points has intersection at least4 with U,
greater than degU3, contrary to Bezout since U has no line factor.
Thus h3 is excluded without using a genus theorem.

For h4, E0=2m(q-4). If q>4, m>=1 makes it positive. If m0,
e4, equality in(16) is necessary. It forces equality in EVERY
two-variable square bound: both multiplicities on each diagonal
are2. Thus an irreducible quartic would have SIX distinct double
points. Choose any five. There is a nonzero homogeneous quadratic
through them (six coefficients and five homogeneous linear conditions).
It shares no component with the irreducible quartic because its degree
is2<4. At the five points the intersection sum is at least10,
exceeding the product degree8, contradiction to Bezout. A reducible
or repeated quadratic still obeys this theorem; no smooth-conic
assumption was made. Hence the m0 quartic case is impossible.

This exhausts every component of degree<=N/2 for q>4. Such a
component must exist in any splitting, so all ell3,q>4 targets
are WHOLE absolutely irreducible.

## 6. The q4,ell3,n13 endpoint over F2

For q4 the preceding cases still exclude h1,2,3,h>4 and h4,m0.
In any hypothetical absolute splitting N10, a least-degree component
has e<=5 and must therefore have h4,m1,e5. Every component of
degree<=5 satisfies the same argument, so none has degree<5.
Consequently such a splitting consists of EXACTLY TWO irreducible
quintics, each passing P smoothly. There is no remaining room for
another component or repetition; squarefreeness was proved inSection1.

The cone(5) at P is(x+omega y)(x+omega²y). Each quintic has exactly
one of these tangents. Coefficient Frobenius fixes P, exchanges the
two tangent lines, and permutes absolute factors of the F2 polynomial.
Two components cannot share a tangent, because the WHOLE cone is
squarefree. Frobenius must therefore EXCHANGE the two quintics.
Their union is one Frobenius orbit, so it has no proper nonempty
Frobenius-stable subset. Every F2 divisor would select such a subset
of the distinct absolute factors, impossible. Thus phi13 is F2-
irreducible in this splitting case as well.

If phi13 were already absolutely irreducible, its F2 irreducibility
would be immediate. These two cases suffice; we do NOT assume or
reproduce the published absolute quintic construction. In particular
the known Kasami exception to absolute irreducibility does not become
a false official two-factor example over F2. This proves the n13
claim without using the unread original1993 proof or its component
formula. Combining Sections3--6 proves the entire proposed theorem.

## 7. Dependencies, source attribution and unproved scope

Operative accepted inputs are T1's no-absolute-line theorem, the exact
S3B germ (also displayed here), the quotient normalization, and S3A
only for the separate three-bit3mod4 exponents. The point-P cone,
squarefreeness, norm-one singular location, ALL new line equations,
global inequalities, small-component exclusions and Frobenius endpoint
are reconstructed in this packet. Classical projective Bezout and
the coprime-tangent equality are used with their full hypotheses.
The elementary line, quadratic-through-five and multiplicity bounds
are stated precisely; no unproved all-components-through-P inference.

The underlying singularity/Bezout strategy is established literature,
not a claimed new method. Primary Hernando--McGuire0903.2016v4
actual definitions/local tables and operative intersection statements
were read. Its general absolute-COMPONENT result is NOT substituted
for whole irreducibility. Literature priority for this specialized
three-bit conclusion remains unestablished. No published theorem is
refuted, and a targeted search's silence proves no absence.

The older r1 bound is a weaker candidate with one complete independent
audit, preserved unchanged. That audit does not automatically count
as a whole audit of THIS stronger r2. BOTH OTHER reviewers must read
and reconstruct the ENTIRE r2 proof and all companion obligations.
Root alone constructed every new r2 inference and is excluded.
Old accepted authorship/review roles must be disclosed, not counted
as fresh independent certification of old work.

The actual official set for binary-weight>=4 exponents, broader factor
patterns, new sufficient families and the annual classification remain
OPEN. All r2 claims remain UNVERIFIED pending both whole audits and
coordinator reconciliation. No mathematical executable or enumeration
is a premise. Older source/proof/review/cache bytes are preserved.
