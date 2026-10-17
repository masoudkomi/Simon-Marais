# Hermitian rational points and the all-index fixed-family divisor criterion

2026-10-17 UTC. **Candidate proof - unverified.** Constructor: root.
TWO OTHER fresh initially blind WHOLE nonconstructor audits of this
COMPLETE submission are required. No mathematical program, CAS, scan,
sample or finite extrapolation supplied the argument. It strengthens
the separately accepted even-inner NJ theorem and the preserved
UNVERIFIED odd-period lead. Neither older mathematical body is edited.
No priority, full annual answer or ordinary irreducibility is claimed.

## Definitions, exact quantifiers and proposed results

Fix q=2^k>=4. Use the accepted GK polynomials in F2[T]:

    A=T^q+(T+1)^(q-1), B=(T+1)^(q-1),
    P0=1, P1=T,
    P_(i+2)=A^(q^(2i+1))*P_(i+1)+B^(q^(2i+1))*P_i,
    E_i=deg(P_i)=1+q²+...+q^(2i-2), i>=1,
    F=P2=T^(q²+1)+(T+1)^(q²-q+1).

The monic degrees and all-index GK identity are accepted premises.
Put d=q²-q+1, L_i=(q^(2i+1)+1)/(q+1). The accepted invariant
g_n is defined by x^n+(x+1)^n=g_n(x²+x), with auxiliary g1=1.
The accepted GK identity is g_(L_i)=P_i(g_d). For odd n>=3 let

    phi_n=[x^n+y^n+z^n+(x+y+z)^n]/[(x+y)(y+z)(z+x)].

**HR1.** For EVERY algebraically closed field K of characteristic2,
EVERY r>=2, EVERY s>=1 and EVERY H in K[T],

    P_s=H(P_r) iff s=r and H=T.                         (HR1)

Arbitrary coefficient extensions and inseparable H are allowed. The
inner r=1 is exceptional: P1=T and P_s=P_s(P1) for every s>=1.
The auxiliary index0 is excluded from both index ranges.

**HR2.** Within this SAME fixed-q family, for EVERY r,s>=1,

    WHOLE phi_(L_r) divides phi_(L_s) over F2
          iff r=1 or r=s.                             (HR2)

This is an exact fixed-family WHOLE-divisor classification. It leaves
proper components, other divisors and arbitrary exponents outside the
family open. In particular it does not claim P_r composition-
indecomposable through every possible inner polynomial or phi_(L_s)
irreducible under ordinary multiplication. For s>=2 the known smaller
whole phi_d factor remains. Equality has unit cofactor; it is not a
qualifying two-nonconstant factorization. The full2024 B4(b) remains
unresolved, and its preliminary part(a) is not a research target here.

The new external input is the CLASSICAL Hasse--Weil point-count bound
for smooth projective geometrically integral curves over finite fields,
with the usual smooth-plane genus formula. These published results are
attributed inputs, not new theorems or proofs of this project. Actual
primary expositions and exact hypotheses/read limits are recorded in
the companion source audit. All remaining deductions are supplied below.

## 1. Degree divisibility fixes the target indices

P_s is nonconstant, so a hypothetical H is nonconstant and E_r|E_s.
Let Q=q². Write s=br+t,0<=t<r. Since Q^r=1 modulo E_r and each
full block of r summands contributes0, E_s=E_t modulo E_r. For
0<t<r,0<E_t<E_r. Thus E_r|E_s implies r|s. This argument uses
ordinary positive INTEGER degrees, not finite-field function degrees.

Smaller s therefore fail, and s=r forces degH=1 and H=T, since
substitution by nonconstant P_r is injective. For s>r it remains
only to rule out s=br with integer b>=2. No converse claim about
composition follows from degree divisibility alone.

## 2. A good Hermitian point exists for EVERY r>=3

Fix r>=3 and work in the finite subfield F_(q^(2r)) of K. Consider
the projective plane curve

    X^(q+1)+Y^(q+1)+Z^(q+1)=0.                        (3)

It is smooth over the algebraic closure: its partial derivatives are
X^q,Y^q,Z^q and have no common projective zero. It is geometrically
integral: a repeated component would make it nonsmooth, and two
distinct positive-degree components over the algebraic closure would
intersect in the projective plane by Bezout, also making it nonsmooth.
The standard smooth-plane genus formula gives g=q(q-1)/2.

Hasse--Weil over the field of size q^(2r) gives at least

    q^(2r)+1-q(q-1)q^r

projective points. At most q+1 lie on Z0 (a nonzero binary homogeneous
polynomial of degree q+1). Thus the affine equation

    a^(q+1)+b^(q+1)=1                                (4)

has at least q^(2r)-q(q-1)q^r-q solutions. This is GREATER than q^4
for every r>=3. Indeed x²-q(q-1)x-q increases for x>=q³, by
factoring the difference at two such x; at x=q³ its excess over q^4
is q^5(q-1)-q>0. This is a symbolic bound at every q>=4, not a
finite point enumeration, maximality theorem or exact zeta formula.

For v=(a,b), write v^[j]=(a^(q^j),b^(q^j)) and use the ordinary
bilinear dot product. Define

    c=v dot v^[3], Delta=det(v^[2],v).

Equation(4) gives the four exact pairings

    v dot v^[1]=1, v^[2] dot v^[1]=1,
    v dot v^[3]=c, v^[2] dot v^[3]=1.

Taking the determinant of their two-by-two pairing matrix shows

    c+1=Delta^(q+1).                                 (5)

If c=1, Delta0 and v^[2]=t v for some t, because v is nonzero.
Pairing with v^[1] gives t=1. Hence a,b belong to F_(q²).
There are at most q^4 such affine pairs in the entire ambient square,
regardless of whether they lie on(4). The strict lower bound above
therefore supplies a point with c!=1. No exact count of bad Hermitian
points is needed. In particular a,b are nonzero at a good point:
if one vanished, the other would be a(q+1)-st root of1 and belong
to F_(q²), forcing c1.

We fix ONE such good point. Its coordinates, and c,A(c),B(c), lie
in F_(q^(2r)), and B(c)!=0. This does not assert that Frobenius is
periodic on a polynomial indeterminate or on the entire coefficient
field K. Only these chosen finite constants have the indicated period.

## 3. Full two-dimensional return, not just one scalar return

The pairing matrix above has determinant c+1!=0. Thus v^[2],v form
a basis, and the functionals pairing with v^[1],v^[3] are independent.
Write v^[4]=alpha v^[2]+beta v. Pairing gives

    alpha+beta=c^q, alpha+c beta=1,
    beta=(c+1)^(q-1)=B(c), alpha=A(c).

These are the same elementary vector relations used in accepted GK,
reconstructed here at the ACTUAL finite good point. The temporary
division is legitimate since c!=1; the coefficients are polynomials.

Set w_i=v^[2i+1] and, for i>=0,

    a_i=A(c)^(q^(2i+1)), b_i=B(c)^(q^(2i+1)),
    M_i=[[a_i,b_i],[1,0]].

Frobenius propagation gives w_(i+2)=a_i w_(i+1)+b_i w_i.
Every b_i is nonzero, so every M_i is invertible. The stacked matrix
with rows w1,w0 is invertible because its determinant is Delta^q!=0.
All subsequent stacked matrices remain invertible under these transfers.
Since v^[2r]=v, we have w_(i+r)=w_i and M_(i+r)=M_i. It follows
from the TWO independent vector columns that, for every j>=0,

    M_(j+r-1)...M_j=I.                               (6)

It would be insufficient merely to know that one scalar initial vector
is fixed. Equation(6) follows by multiplying an invertible stacked
two-dimensional vector matrix and comparing its exact return.

The scalar vectors (P_(i+1)(c),P_i(c)) obey the SAME transfers,
with initial(c,1). Differentiating the polynomial recurrence before
evaluation gives the SAME transfers for (P_(i+1)'(c),P_i'(c)), with
initial(1,0), because all Frobenius-power coefficient derivatives
vanish. Equation(6) now yields in particular

    P_r(c)=1, P_(r+1)(c)=c,
    P_r'(c)=0, P_(r+1)'(c)=1.                        (7)

Both scalar and derivative vectors are r-periodic at c. The proof
does not differentiate an evaluated value identity.

## 4. The local parameter has exact order q

Put Z=T-c. Binary support of the displayed exponents of F shows that
its expansion has no terms Z^e for2<=e<q, at ANY c: the only low
nonconstant binary position below q is1. Its derivative is F'=A^q.
Its coefficient of Z^q comes only from the second summand, and is

    (c+1)^(q²-2q+1)!=0.                              (8)

For every i>=1, the recurrence coefficient exponent is at least q³.
Consequently, modulo Z^(q³), each P_i(c+Z), i>=1, is a constant
linear combination alpha_i F(c+Z)+beta_i(c+Z). Start with coefficient
pairs(0,1) at i1 and(1,0) at i2, and use the invertible matrices M_i
for i>=1. The two-by-two coefficient matrix remains invertible, so
no individual coefficient pair is zero. By(7) the derivative of P_r
is zero, giving alpha_r A(c)^q+beta_r=0. Hence alpha_r!=0.

Subtract its constant P_r(c)=1. Its linear term vanishes by(7),
the degrees2 through q-1 vanish by the F/T representation, and(8)
gives the nonzero degree-q coefficient. The error starts at q³>q.
Thus

    V(Z)=P_r(c+Z)-1 has ord_Z V=q EXACTLY.            (9)

This step uses an actual binomial coefficient and invertible coefficient
matrix. A root of a repeated derivative alone would not justify(9).

## 5. The first perturbation survives a full r-step return

Fix M=q^(2r+1) and work modulo Z^(M+2). Let
V_i(T)=(P_(i+1)(T),P_i(T))^t. For steps i=r,...,2r-1, the ONLY
coefficient perturbation that can reach degree M+1 is at i=r:
every later exponent is at least q²M>M+1. The first perturbation is

    epsilon=(A(c+Z)^M-a_r)P_(r+1)(c+Z)
              +(B(c+Z)^M-b_r)P_r(c+Z).

It has order at least M. Since M is a power of characteristic2,
all coefficient-factor exponents are multiples of M. Equation(7)
therefore gives exactly

    [Z^(M+1)]epsilon
       =A'(c)^M P_(r+1)'(c)+B'(c)^M P_r'(c)
       =A'(c)^M!=0,                                 (10)

where A'(c)=B'(c)=(c+1)^(q-2). No higher multiple of M can contribute
because2M>M+1. The P_r derivative eliminates the second summand.

Let R=M_(2r-1)...M_(r+1) be the remaining CONSTANT transfer product.
Equation(6) says R M_r=I, hence R=M_r^-1. After inserting epsilon
in the first coordinate of the first updated vector, the complete
block gives

    V_(2r)(c+Z)-V_r(c+Z)=R*(1,0)^t*epsilon
                                            modulo Z^(M+2).

The BOTTOM coordinate of M_r^-1*(1,0)^t is1/b_r, a unit. Thus

    ord_Z(P_(2r)(c+Z)-P_r(c+Z))>=M,
    [Z^(M+1)](P_(2r)(c+Z)-P_r(c+Z))
                         =A'(c)^M/b_r!=0.           (11)

This matrix inverse fixes every propagation index and coefficient;
it does not guess a static transfer matrix or extrapolate an ell3 case.

For every subsequent full block, beginning at i>=2r, coefficient
perturbations start ABOVE M+1 and its constant transfer product is I
by(6). Therefore for EVERY integer b>=2,

    P_(br)(c+Z)-P_r(c+Z) has order>=M,
    its Z^(M+1) coefficient is A'(c)^M/b_r!=0.        (12)

There is one retained first-block perturbation; later blocks return
it unchanged modulo Z^(M+2). They do not add identical low-order
perturbations whose number could cancel in characteristic2.

## 6. Exclude compositions for every r>=3

Suppose s>r and P_s=H(P_r). Section1 gives s=br,b>=2. Set
J(Y)=H(Y)-Y. If J is zero, equation(12) is an immediate contradiction.
Otherwise factor J(Y)=(Y-1)^m W(Y), W(1)!=0, with exact m>=0.
By(9) its composition has exact order qm. The order lower bound
in(12) gives m>=M/q=q^(2r). Expand J at1. Its first POSSIBLE term
has exponent e=q^(2r), itself a power of characteristic2; its
coefficient may vanish. Substitution of V(Z) into that term has
only exponents divisible by e, so cannot supply M+1=qe+1.
Every higher term has order at least q(e+1)=M+q>M+1.
Thus J(P_r(c+Z)) has coefficient ZERO there, contradicting(12).

This proves HR1 for all r>=3, arbitrary H, including inseparability,
missing initial coefficients and arbitrarily large outer degree.
No root-value distinctness or derivative nonvanishing of H was used.

## 7. The r2 endpoint, reconstructed for the complete theorem

The accepted even-inner NJ theorem already covers r2, but the short
specialization is included so this whole submission does not depend
on a partial extension check. Choose alpha a root of A. Then
(T+1)A=T^(q+1)+1 implies alpha!=0,1, alpha in F_(q²),
alpha^q=alpha^-1 and B(alpha)=alpha^-1. For every recurrence index,
B(alpha)^(q^(2i+1))=alpha. Differentiating first and evaluating gives

    P_(2h)(alpha)=alpha^h, P_(2h)'(alpha)=0,
    P_(2h+1)(alpha)=alpha^(h+1), P_(2h+1)'(alpha)=alpha^h.

Here A'(alpha)=(alpha+1)^(q-2)!=0. F(alpha)=alpha;
its linear coefficient is zero and its exact first nonconstant
coefficient is at q, equal to(alpha+1)^(q²-2q+1), by the same
binary expansion as(8). Thus ord(F(alpha+Z)-alpha)=q.

Degrees force even s>2. Put M=q^5 and use P4=A^M P3+B^M P2.
The difference P4-alpha P2 has order>=M and coefficient at M+1
equal to A'(alpha)^M*alpha!=0. Every later EVEN recurrence exponent
is at least q^9>M+1, so modulo Z^(M+2),

    P_s=alpha^((s-4)/2)P4.

Hence P_s-alpha^((s-2)/2)P2 has order>=M and a nonzero coefficient
at M+1. Apply exactly the substitution argument of Section6 at
beta=alpha, with J(Y)=H(Y)-alpha^((s-2)/2)Y and e=M/q=q^4.
It again forbids that coefficient. Thus larger s fail; Section1
handles smaller s and equality. This completes HR1 for EVERY r>=2.

## 8. Exact whole-divisor application HR2

For r,s>=1, L_r,L_s are odd integers>=d>=13, so the accepted CP1
criterion applies in its full homogeneous/multiplicity scope:

    phi_(L_r)|phi_(L_s) iff g_(L_s)=H(g_(L_r)), H in F2[T].

By GK this is P_s(g_d)=H(P_r(g_d)). Since g_d is nonconstant,
substitution by it is injective, giving P_s=H(P_r). For r>=2,
HR1 over an algebraic closure of F2 forces s=r. For r1, P1=T
and H=P_s supplies the converse for every s. Equality also supplies
the r=s converse. These prove BOTH directions of HR2.

The unit/zero auxiliary boundaries are not passed through CP1.
This classifies only WHOLE members of one fixed-q sufficient family.
Other factors, mixed-q questions and all arbitrary official n remain
outside its conclusion. No new ordinary irreducibility claim follows.

## Sources, failed approaches and remaining scope

Accepted GK and CP1 supply exact definitions, degrees and the final
whole-divisor bridge. Their complete bodies and acceptance records
are fingerprinted. Accepted NJ is a consistency cross-check only:
the r2 deduction is reconstructed above. DI is unused. The older
odd-period lead worked with constants in Fq and could only cover
indices having factors in q²-1; it is preserved as UNVERIFIED history.
The new point over F_(q^(2r)) removes that artificial period restriction.

Hasse--Weil and the plane genus formula are attributed standard inputs.
Only their exact point-count/genus statements and source read scopes
are imported. No claim is made to reprove foundational intersection
theory or Riemann--Roch. Exact Hermitian maximality, automorphism-group
classification, quotient genera and a zeta-function formula are not
needed. The q4 bad-point bound is deliberately crude and sufficient.

This argument was developed by hand from the accepted Frobenius
recurrence and the retained-coefficient obstruction. Its crucial
checks are the TWO-dimensional return, local order EXACTLY q, the
bottom inverse-matrix coefficient1/b_r and the absence of low-order
perturbations in later blocks. New whole reviewers must reconstruct
all of those, rather than reading this as an assumed-proof extension.
No computation, source conjecture or peer finding fills them.

The full annual factorization classification and priority remain open.
Every assertion HR1/HR2 is CANDIDATE-UNVERIFIED until two OTHER fresh
initially blind whole audits and coordinator reconciliation are complete.
