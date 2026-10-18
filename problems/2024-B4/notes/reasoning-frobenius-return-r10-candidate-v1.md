# A linear intersection budget for the actual nonordinary singularities

18 October 2026 UTC. **Candidate proof - unverified.** Constructor C,
`/root/review_2017_coarsening_r1`. TWO OTHER initially blind ENTIRE WHOLE
audits and coordinator reconciliation are required before promotion.
Only the open 2024 B4(b) is investigated. Requested inherited settings are
gpt-6.1-sol/max; effective-setting readback is unavailable.

## 0. Proposed results and their boundary

Work in K, an algebraic closure of F2. Put

    W=X+Y+Z, R=(X+Y)(Y+Z)(Z+X),
    f_n=X^n+Y^n+Z^n+W^n, phi_n=f_n/R.

Use the established polynomial quotient, without redoing preliminary(a).
Write

    n=ell*q+1, ell>=3 odd, q=2^i, i>=2,
    d=gcd(ell,q-1), N=ell*q-2.

Thus q is the MAXIMAL power of two dividing n-1, and phi_n has degree N.
Define the ordinary integer expression

    P(ell,d,q)=(4ell-d^2+d-5)q^2
                  -[4(ell-2)^2-2(d-1)(d-3)]q-4.          (1)

The proposed conclusions are:

**FR10A.** At a nonordinary off-diagonal singular point, if two coprime
actual factors of phi_n both vanish, their local orders are 1 and q-1
and their intersection number is EXACTLY q. If they do not both vanish,
the intersection number is zero. A possible intersection is not discarded
merely because the point has one tangent.

**FR10B.** If the WHOLE phi_n is reducible over K, then

    P(ell,d,q)<=0.                                         (2)

More precisely, Section6 proves a bound retaining the actual numbers of
root-of-unity quadruples, before replacing them by elementary upper bounds.
Consequently P>0 implies WHOLE absolute irreducibility, and excludes the
official coefficientwise factorization over F2.

**FR10C.** In particular, phi_n is absolutely irreducible if

    q>=ell-1 and d<=3,

except for the single parameter pair (ell,q)=(3,4), which is deliberately
not decided by this criterion. One family is

    q=2^i, i>=3, 1<=s<=i-1,
    ell=q-2^s-1, n=q(q-2^s-1)+1.                          (3)

Another is n=q(q-7)+1 for every power q>=16 of two.

**FR10D.** An additional concrete infinite family is

    n=35*2^(6t+3)+1, t>=1.                               (4)

Here d=7, so this is not an application of FR10C. For every member, the
accepted R8 no-four-root condition and accepted R9 J condition both FAIL;
the accepted R7 gcd hypothesis also fails. The odd part35 is outside the
Mersenne odd-part family in accepted R6D, and the binary weight is four.
Thus (4) is an extension beyond those precise reviewed hypotheses, not a
restatement of their conclusions. Published overlap remains unresolved:
no priority, new-method or full annual classification claim is made.

The exact input is accepted **R6B/R6C**: phi_n is reduced; for odd n of
binary weight at least three EVERY positive-degree absolute component,
and hence every actual nonconstant divisor, has degree at least q.
The complete accepted R6 body and current MD/JSON authority were freshly
read. Its separately reviewed T1 no-line input is retained through R6C;
it is not independently recertified here by its old constructor/reviewer.
The present ell>=3 guarantees at least two set bits in ell; shifting by
i>=2 and adding the bit0 gives binary weight at least three.

The complete accepted R9 body/authority were also freshly read for exact
scope and comparison. R9's J hypothesis is NOT a premise here. All local
computations needed for this new budget are exposed below, including
diagonal and infinity points. No component is assumed to be F2-defined,
to contain the center, to have a common stabilizer, or to have equal
degree with another component. Complementary factors may be reducible.

Fulton's local intersection definition/properties and projective Bezout
theorem are the only primary geometric theorems applied. Their complete
operative proofs and AppendixA were freshly read. The required proofs are
algebraic and remain valid in characteristic2. No genus, Hessian,
characteristic-zero tangent theorem or Newton-Puiseux theorem is invoked.

## 1. A local lemma, including the formal branch calculation

Let q>=2 be a power of two. In local affine coordinates x,y at0, suppose
a polynomial F has expansion

    F=x^q+H_(q+1)+terms of degree at least q+2,              (5)

where H_(q+1) is a squarefree homogeneous binary form. Suppose F=UV,
where U,V are coprime and both vanish at0. If x does not divide H_(q+1),
this is impossible: if u,v are their positive orders, u+v=q, their initial
forms are scalar multiples of x^u,x^v, and the degree-(q+1) term of their
product is divisible by x^min(u,v).

If x divides H_(q+1), squarefreeness says x^2 does not divide it. The same
product calculation forces min(u,v)=1. Interchange the factors and rescale
so that V has initial form x and U has initial form x^(q-1). There is a
unique formal series h(y), of order at least two (or zero), with

    V(h(y),y)=0.

This elementary formal implicit step requires only V_x(0)=1: determine
each coefficient of h successively, since its coefficient in the next
equation is1. Formal division of V(x,y)-V(h(y),y) by x-h(y) shows that
V=(x-h(y))*E with E a formal unit. Evaluation at x=h(y) therefore identifies

    K[[x,y]]/(V) with K[[y]].

Because x is a SIMPLE factor of H_(q+1), the coefficient gamma of x*y^q
in it is nonzero. Differentiating (5) with respect to x gives

    F_x(h(y),y)=gamma*y^q+terms of y-order greater than q.  (6)

Indeed, the derivative of x^q is zero. A derivative of any other term of
H_(q+1), after substituting h of order>=2, has order>q; derivatives of
terms of total degree>=q+2 have order>=q+1. These assertions also hold
when h is identically zero. Differentiating F=UV and restricting to V=0
instead gives

    F_x(h(y),y)=U(h(y),y)*V_x(h(y),y),

where V_x is a unit. Consequently U(h(y),y) has EXACT order q.

By Fulton's local-ring definition, I_0(U,V) is the length of
O_0(A^2)/(U,V). Computing that finite length in K[[x,y]] gives the same
answer. For clarity, this last passage does not import a convergence
theorem: coprimality makes the local quotient finite; some power of the
maximal ideal is zero in it. Modulo that power, local polynomials and
formal power series have the same finite truncations and the same units,
so their two quotients have the same length. The displayed evaluation
identification then makes the length equal to ord_y U(h(y),y)=q.

We have proved:

    F=UV, U(0)=V(0)=0 under (5)
       ==> {ord U,ord V}={1,q-1}, I_0(U,V)=q.              (7)

If one factor is a unit, I_0 is zero. The argument is unchanged by an
invertible linear coordinate transformation, a nonzero scalar, or by
absorbing a local unit into either factor. It applies to an actual
complement containing several components as well as to an irreducible
factor. It does NOT say that the local branches belong to distinct
global components in every curve; (7) is asserted only for an actual
coprime split which has both factors at the point.

## 2. All affine off-diagonal candidate intersections

In the chart Z=1, write f_n(x,y)=x^n+y^n+1+(x+y+1)^n.
Let P=(a,b), c=a+b+1, with R(P)!=0. If phi_n(P)=0 and its two affine
partials vanish, then the same is true of f_n. Its partials imply

    a^(ell*q)=b^(ell*q)=c^(ell*q).

None of a,b,c is zero: if c=0 the two equalities force a=b=0, contrary
to c=a+b+1; and the other cases follow in the same way. Frobenius is
injective, so a^ell=b^ell=c^ell=u. Substituting in f_n(P)=0 gives

    0=(a+b+c)*u^q+1=u^q+1,

because a+b+c=1. Again injectivity gives u=1. Therefore

    a,b,c in mu_ell, and a,b,c,1 are four distinct points. (8)

Conversely these conditions give a singular point of f_n, and hence of
phi_n since R(P) is a unit. Distinctness follows directly from the three
excluded equalities a=1,b=1,a=b, and c=a+b+1; it also excludes c=0.

Translate by (a,b). Exact Frobenius/binomial expansion gives no terms of
degrees1,...,q-1, and the next two forms are

    F_q=(A*x+B*y)^q,
    A^q=a^(1-q)+c^(1-q), B^q=b^(1-q)+c^(1-q),

    H=F_(q+1)=C*x^(q+1)+D*(x^q*y+x*y^q)+E*y^(q+1),
    C=a^(-q)+c^(-q), D=c^(-q), E=b^(-q)+c^(-q).          (9)

For example, use (a+x)^n=(a+x)(a^q+x^q)^ell and ell odd. The binomial
coefficients at q and q+1 are1 modulo2. The identities a^ell=b^ell=c^ell=1
give exactly the coefficients in (9), as POLYNOMIAL Taylor coefficients.

The following calculation supplies the needed squarefreeness:

    H_x=C*x^q+D*y^q, H_y=D*x^q+E*y^q,
    CE+D^2=(a+b+c)^q/(abc)^q=1/(abc)^q!=0.               (10)

Thus H_x,H_y cannot both vanish at a nonzero vector. A repeated linear
factor of the binary form H would make both partials vanish at a nonzero
point on that line. Over K the form splits into linear factors, so H has
q+1 DISTINCT linear factors. This familiar property is recorded in
Hernando-McGuire Lemma5 (attributed there to earlier Janwa-McGuire-Wilson
work); (9)-(10) are the full hand verification used here.

If (A,B)!=(0,0), F_q is a nonzero q-th power of one linear form L.
Apply the local lemma after taking x=L. In an actual global split
phi_n=UV, the numerator is F=RUV and R is a unit at this point. Absorb it
into one factor; local orders and intersection numbers of U,V are
unchanged. This proves FR10A, with no assumption L does or does not
divide H. If it does not divide H, the intersection is zero; if it does
and both factors occur, the intersection is q. In particular the latter
possibility is accounted for, not incorrectly declared unibranch.

If A=B=0, the point is instead ordinary of multiplicity q+1, since its
initial form is the squarefree H. We now identify and count THESE points
without assuming that every singular point is ordinary.

## 3. Exactly which off-diagonal points are ordinary

From (9), A=B=0 if and only if

    a^(q-1)=b^(q-1)=c^(q-1).

Write a=lambda*c,b=mu*c. Then lambda,mu belong to F_q^*, while

    (lambda+mu+1)*c=a+b+c=1.

Consequently lambda+mu+1 is nonzero, c belongs to F_q^*, and then a,b
belong to F_q^*. Conversely if a,b,c are in F_q^* then A=B=0. Combining
this with (8), the ordinary off-diagonal points are EXACTLY those with

    a,b,c,1 in mu_d, d=gcd(ell,q-1).                     (11)

The normalization a+b+c=1 is essential. No assertion is made about
arbitrary unnormalized ratio data; no different fixed-field hypotheses
are intersected. The source's tables are not needed as a substitute for
the argument (11).

For any odd positive integer s, let M_s denote the number of ordered
pairs (a,b) for which a,b,c=a+b+1,1 are four distinct members of mu_s.
Thus there are M_ell off-diagonal singular points in total, of which
EXACTLY M_d are ordinary. M_1=0. For s>=3 odd, fix a!=1 in mu_s. The
eligible values b lie in the set mu_s minus {1,a}, which has odd size s-2.
The involution b -> a+b+1 has no fixed point and preserves the eligible
set. Hence its size is even and at most s-3. Summing over a gives

    M_s<=(s-1)(s-3), for s>=3; M_1=0.                   (12)

In particular M_3=0. The same numerical formula is zero at s=1, so it
can be used uniformly for the d and ell appearing below. This counting
argument is classical: compare Hernando-McGuire Lemma6 and its proof.
No root enumeration, finite-field computation or empirical cap bound is
used in (12).

At each of the M_d ordinary points, factors U,V have coprime tangent
cones: their product is the full squarefree initial form. If their orders
are u,v, then u+v=q+1 and I_P(U,V)=u*v. Consequently

    I_P(U,V)<=floor((q+1)^2/4)=q(q+2)/4.                (13)

The remaining M_ell-M_d points contribute at most q each by FR10A.
These are counts of actual affine points; no projective orbit size or
Frobenius transitivity assumption has been inserted.

## 4. The three diagonal lines and their center

Any intersection of two distinct components must be a singular point
of phi_n. It remains to locate the possible ones on R=0. Off the center
(1,1,1), the three lines are disjoint and are permuted by coordinate
symmetry. Analyze P=(b,1,1), b!=1. The value of the polynomial quotient
there is

    phi_n(b,1,1)=(b^ell+1)^q/(b+1)^2.

This follows by taking the first coefficient in y-1 of the polynomial
identity f_n=R*phi_n; it does not divide by zero as a rational function.
Thus only b in mu_ell minus {1} can lie on phi_n on this line.

Set x=b+u,y=1+v. The translated denominator has

    w_1=(b+1)^2*v, w_2=(b+1)*v^2,
    w_3=u^2*v+u*v^2.

The numerator forms are

    F_q=(b^(1-q)+1)*v^q,
    F_(q+1)=b^(-q)*u^q*v+b^(-q)*u*v^q
                  +(b^(-q)+1)*v^(q+1).                (14)

If b is NOT in F_q, the coefficient of F_q is nonzero. The quotient
therefore has multiplicity q-1 and initial form a nonzero multiple of
v^(q-1). Its degree-q form has NONZERO coefficient

    [u^q]phi_(degree q)=b^(-q)/(b+1)^2.

Indeed w_2 times the preceding quotient form contains v, so cannot
cancel this pure u^q term after division by w_1. Hence v does not divide
the next quotient form. If both factors U,V vanished here, their initial
forms would be powers of v and the next product form would be divisible
by v, a contradiction. The local intersection is zero.

If b IS in F_q, then F_q=0 and the quotient has multiplicity q, with
initial form, up to a nonzero scalar,

    u^q+u*v^(q-1)+(1+b)*v^q.                            (15)

Its u and v partials are v^(q-1) and u*v^(q-2). A repeated linear factor
would have to occur at v=0, but the u^q coefficient is nonzero. Thus (15)
is squarefree and the point is ordinary of multiplicity q. There are
d-1 choices of b on each diagonal line, and the three sets are disjoint
away from the center. Their total contribution to I(U,V) is at most

    3(d-1)*q^2/4.                                       (16)

Finally translate (1,1,1) by X=1+u,Y=1+v,Z=1. Here R=u*v*(u+v) and
the initial numerator form is u^q*v+u*v^q. The quotient's initial form is

    (u^(q-1)+v^(q-1))/(u+v),                            (17)

of degree q-2, with q-2 DISTINCT linear factors: q-1 is odd, and division
removes the single root u=v from the q-1 root ratios. Neither axis is a
factor. Therefore the center is ordinary, and contributes at most

    (q-2)^2/4.                                         (18)

All bounds in (13),(16),(18) are ordinary inequalities between integers
or rational numbers, not division by4 in K. They hold when either
factor is a unit at the point as well. They do not require an irreducible
complement or that a chosen component contain the center.

## 5. No missing intersections at infinity

On Z=0, away from R=0, the homogeneous derivative

    (f_n)_Z=(X+Y)^(n-1)

is nonzero. At a point of phi_n=0 there, R is a unit, so the gradient of
phi_n is nonzero. Such a smooth point cannot be an intersection of U,V.

The three R=0 points at infinity are (1:0:0),(0:1:0),(1:1:0).
At the first point the lowest local numerator term in the chart X=1 is
Y+Z; the lowest denominator term is also Y+Z, for EVERY odd n. Polynomial
division gives phi_n(1,0,0)=1. Coordinate symmetry gives the other two
values; for (1:1:0) one can also use the linear symmetry permuting the
four entries X,Y,Z,W. Thus none of these points lies on phi_n.

For explicitness at (1:1:0), put X=1,Y=1+u,Z=v. Then W=u+v and the
linear term of f_n is u. The linear term of R is u as well, so the same
value1 follows directly. This avoids relying on a symmetry not explicitly
checked. There are no intersections at infinity at all.

The full list of possible intersections is now the center, the ordinary
noncentral diagonals, and the two types of off-diagonal point already
counted. At R-unit affine points singularity was derived in Section2;
at R=0 all possible zeros were derived in Section4. No point is omitted
by a choice of affine chart or a singularity-table convention.

## 6. Global budget on an actual least component

Suppose phi_n is reducible over K. Accepted R6 reducedness permits a
coprime split phi_n=UV where U is an absolute component of least degree
e and V is the FULL actual complementary product. Then

    q<=e<=N/2,
    e(N-e)>=q(N-q)=(ell-1)q^2-2q.                      (19)

The lower bound q is accepted R6C, with its binary-weight hypothesis
checked in Section0. Monotonicity in (19) can be checked without calculus:
e(N-e)-q(N-q)=(e-q)(N-e-q)>=0. No equal-degree grouping is assumed.

Fulton's projective Bezout theorem applies because U,V have no common
component. It gives e(N-e)=sum_P I_P(U,V). Using Sections2-5 gives the
more precise actual-quadruple budget

    e(N-e)<=B_actual
       =(q-2)^2/4 + 3(d-1)q^2/4
          +q*(M_ell-M_d)+q(q+2)*M_d/4
       =(q-2)^2/4 + 3(d-1)q^2/4
          +q*M_ell+q(q-2)*M_d/4.                       (20)

Since q>=4, both coefficients used in replacing M_ell,M_d by (12) are
nonnegative. We obtain

    B_actual<=B_upper
       =(q-2)^2/4 + 3(d-1)q^2/4
          +q*(ell-1)(ell-3)
          +q(q-2)*(d-1)(d-3)/4.                       (21)

This is the direction of the inequality needed for contradiction; no
upper bound on intersection multiplicity is inferred from its usual
LOWER bound alone. Ordinary coprime cones give equality to the product
of local orders; the nonordinary upper bound is the independent lemma
of Section1.

Subtracting (21) from the lower bound (19), and multiplying by4, gives

    4[(ell-1)q^2-2q-B_upper]
       =[4ell-3d-2-(d-1)(d-3)]q^2
          +[-4-4(ell-1)(ell-3)+2(d-1)(d-3)]q-4
       =(4ell-d^2+d-5)q^2
          -[4(ell-2)^2-2(d-1)(d-3)]q-4
       =P(ell,d,q).                                    (22)

Reducibility would force the bracket on the left to be nonpositive.
This proves (2), and its contrapositive proves FR10B. It is a WHOLE
polynomial conclusion: if there were at least two absolute components,
the actual least one and its actual complement would give the impossible
inequalities. Reducedness rules out a power of a single component.

## 7. A uniform small-gcd range

For d=1, (1) becomes

    P=(4ell-5)q^2-4(ell-2)^2*q-4.

If q>=ell-1, then

    (4ell-5)q-4(ell-2)^2
       >=(4ell-5)(ell-1)-4(ell-2)^2=7ell-11>0.

Thus P>=q(7ell-11)-4>0 for ell>=3,q>=4.

For d=3 the expression is

    P=(4ell-11)q^2-4(ell-2)^2*q-4.

Here ell is a multiple of3. If ell>=9 and q>=ell-1, then

    (4ell-11)q-4(ell-2)^2>=ell-5>=4,

so P>0. The only remaining ell is3. Then P=q^2-4q-4. At q=4 it is -4,
so the pair (3,4) is explicitly excepted. For any power q>=8 it is
positive. These cases prove FR10C, without falsely excluding the known
Kasami endpoint n=13. No preliminary factorization at that endpoint is
recomputed or used in the proof.

For (3), ell=q-2^s-1 is odd and at least3 for i>=3,1<=s<=i-1. Further

    gcd(ell,q-1)=gcd(2^s,q-1)=1,

and q>=ell-1. The maximal-power and positive-degree hypotheses therefore
hold. For ell=q-7 with q>=16, ell>=9 is odd and

    gcd(ell,q-1)=gcd(6,q-1)<=3.

Thus FR10C applies to this second family too. These are exact families,
not conclusions from a table of tested exponents.

## 8. A family outside the reviewed NF4 and J hypotheses

Let t>=1, i=6t+3, q=2^i, ell=35. Then q>=512 and

    7 divides q-1, while 5 does not divide q-1,
    d=7,
    P(35,7,q)=93q^2-4308q-4.

The first statement uses 2^3=1 modulo7. The second uses i odd, whereas
the order of2 modulo5 is4. For every real q>=47,

    93q-4308>=93*47-4308=63,
    P>=47*63-4=2957>0.

Therefore FR10B gives whole absolute irreducibility for EVERY t>=1,
proving FR10D. The first member is n=17921; that integer is only an
endpoint illustration and has not been factored by a program.

To check that this is not simply an invocation of R8/R9, use the subfield
F8 of K. Its seven nonzero elements lie in mu_35. Choose any two-dimensional
F2-subspace V of F8 and b outside V. The four points of b+V are distinct
and nonzero, and their sum is zero. Hence the accepted R8 NF4 hypothesis
fails. Since q=1 modulo7, delta=q^2-q+1=1 modulo7, and raising these four
points to delta leaves them unchanged. Their delta-power sum is zero as
well, so R9's J hypothesis also fails.

Furthermore ord_35(2)=lcm(3,4)=12 and gcd(i,12)=3. Thus accepted R7's
gcd=1 criterion is unavailable. The odd part35 is not Q-1 for any power
Q of two. Finally 35=2^5+2+1, so 35q+1 has binary weight four and is not
in the reviewed three-bit exclusion sector. These observations concern
the stated scopes of those old packets, not a claim to have classified
every possible consequence of every earlier theorem or published paper.

## 9. Official consequence, sources and remaining gaps

For P>0, phi_n is a nonconstant absolutely irreducible homogeneous
polynomial over F2. An official pair of integer polynomials, both
nonconstant modulo2, would reduce to a product of two positive-degree
polynomials over F2. This is impossible even if those two polynomials
are not homogeneous. Polynomial factors, not polynomial functions on
F2^3, are being considered.

n=1 gives the zero numerator and is outside the parameterization used
here; n=3 gives the unit quotient. Neither endpoint is silently inserted
into the criterion. q=2 and ell=1 are also outside this packet, with
their prior published/accepted contexts unchanged. The sign condition
P<=0 is NECESSARY for absolute reducibility, not sufficient. Nothing
here decides every remaining odd n, every smaller q, a general Frobenius
descent classification, or the annual question.

The squarefree next form and root-counting argument are classical local
ingredients from the Janwa-Wilson/Janwa-McGuire-Wilson/Jedlicka/Hernando-
McGuire literature. Their exact roles and literal fresh read limits are
in the source companion. The operative original Jedlicka paper and the
Férard2014/2017 full proofs were not obtained/read; their possible
overlap with (1)-(4) remains OPEN. Abstracts and secondary summaries are
not imported as whole-polynomial theorems. In particular the published
exceptional-APN classification only guarantees an absolute component in
its general form; it does not replace the least-component contradiction
in Section6. No novelty or first-publication claim is made.

C alone constructed this NEW packet. C's older R6/R7/R8 authorship and
R9 review roles are disclosed, not counted as independent recertification
of those accepted inputs. Root provided the broad task and received
unverified progress summaries, but supplied no new proof inference.
Root's unverified degree-gap note was NOT read or used. Corresponding
NEW R21 peer material was not accessed; C's own frozen R21 verdict was
withheld until root explicitly confirmed BOTH ENTIRE initials and was
then released without peer access. No R11 review findings were read.

The full64 obligations/constructor dispositions, issues, source MD/JSON,
failed routes, worklog, no-math-code record and compact byte-integrity
metadata accompany this candidate. There is no mathematical code,
factor scan, CAS, source executable, old certificate or routine test in
the proof. TWO OTHER ENTIRE WHOLE reviewers must reconstruct the proof,
including the characteristic2 local algebra and ALL intersection cases,
before root alone can consider promotion. Internal review is not external
validation or absolute certainty.
