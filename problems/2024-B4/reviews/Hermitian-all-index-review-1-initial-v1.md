# HR1/HR2: complete initially blind nonconstructor whole review R1

2026-10-17 UTC. Reviewer `/root/review_2022_complexity_r2`.
Requested `gpt-6.1-sol`, reasoning `max`; an independent effective-setting
readback is unavailable. **Initial whole audit, not coordinator promotion.**

I find no substantive objection to HR1 or HR2 in their stated fixed-q
scopes. This conclusion covers the entire submission, including the
degree reduction, the geometric existence argument, the two-dimensional
shifted return, all local orders and propagation indices, the separately
reconstructed r=2 endpoint, and both whole-divisor directions. It does
not certify a complete answer to the annual problem or any novelty.
The companion ledger records 48 inference checks covering all 24 author
obligations. No mathematical executable, sample, CAS, point scan,
certificate replay or constructor script was used.

## 1. Independence, exact submission and read boundaries

The constructor is root. I did not contribute to this new HR construction
and did not read any other NEW HR report, issue ledger or conclusions
before completing and freezing this entire initial packet. Root's future
inspection cannot be an independent audit of its own construction.

I previously reviewed the complete GK packet as reviewer 2 and the
complete even-inner NJ-v2 packet as reviewer 2. Those historical roles
are disclosed, not counted as a fresh independent recertification of
those premises here. I was neither a constructor nor an original
independent auditor of CP1; I have read and reconstructed its accepted
body as a dependency. Older structural, divisor and valuation review
context supplies no additional premise for this audit.

Exact target: `notes/coordinator-Hermitian-all-index-return-v1.md`,
15281 bytes, SHA256
`296241f7538f7eb86315998ff760f4fa363d3a2d1c911988d6fa2b1a4f0287cc`.
Exact constructor manifest: `notes/coordinator-Hermitian-all-index-manifest-v1.json`,
3214 bytes, SHA256
`d93f76bb4aecc912bb9dc91a51714d41330d250ba333ca7a32061d39a36df0a3`.
Paths in this paragraph are relative to `problems/2024-B4/`.

I read the complete main text, 24 obligations, source audit and worklog;
the complete accepted GK, CP and NJ mathematical bodies and acceptance
JSONs; the preserved odd-period lead; AGENTS.md and the official-domain
normalization. The source companion distinguishes actual primary web
reads from foundational results imported with attribution and from
metadata-only preservation. NJ is a consistency check, not an unproved
shortcut over r=2. The odd-period note remains unverified history. DI,
the MCM lead, individual-component classifications and the whole-phi13
criterion are not needed for HR1/HR2.

## 2. Official domain and exact claim being reviewed

The official open target is 2024 B4(b): positive odd n, coefficientwise
congruence in integer polynomials, with both residual factors
nonconstant modulo 2. It concerns formal polynomials, not their values
on a finite set. No preliminary-part proof is investigated here.

HR fixes q=2^k>=4, works over every algebraically closed K of
characteristic 2, and uses

    A=T^q+(T+1)^(q-1), B=(T+1)^(q-1),
    P0=1, P1=T,
    P_(i+2)=A^(q^(2i+1))*P_(i+1)+B^(q^(2i+1))*P_i.

Accepted GK gives monic degree E_i=1+q²+...+q^(2i-2) for i>=1,
F=P2=T^(q²+1)+(T+1)^(q²-q+1), and

    g_(L_i)=P_i(g_d), d=q²-q+1,
    L_i=(q^(2i+1)+1)/(q+1).

The invariant is defined by x^n+(x+1)^n=g_n(x²+x). HR1 says exactly:
for every r>=2, s>=1 and H in K[T], P_s=H(P_r) if and only if
s=r and H=T. It permits inseparable H and arbitrary coefficient
extensions. It excludes the identity inner P1 and the constant P0.
It is not a claim about composition through every possible inner
polynomial.

HR2 says that, within this single fixed-q family and for r,s>=1,
the WHOLE homogeneous phi_(L_r) divides phi_(L_s) over F2 exactly
when r=1 or r=s. This concerns multiplicities of the whole divisor,
not containment of some component. The r=s cofactor is a unit, so
equality alone is not an official two-positive-degree factorization.
The separately established sufficient factors for target s>=2 remain.

## 3. Accepted algebraic bridge and integer degrees

I checked the full CP1 body and its accepted scope rather than importing
an affine component heuristic. Its invariant ring argument uses the
unique expansion A(x²+x)+xB(x²+x), and g_n is monic of degree
(n-1)/2 for odd n>=3. The invertible projective change
(X,Y,Z)=(s+u,s,t), followed by u=1, gives

    phi_n(s+1,s,t)=Q_n(s²+s,t²+t),
    Q_n(U,V)=(g_n(U)+g_n(V))/(U+V).

The affine total degree remains n-3, so homogeneous division is not
lost on u=0. The free-module basis 1,s,t,st over F2[U,V] descends
division of WHOLE Q polynomials through the two quadratic covers.
Finally the monic h-adic expansion of p proves that h(U)+h(V)
divides p(U)+p(V) precisely when p=H(h). Cancelling the SAME
nonzero U+V on both sides retains diagonal multiplicities without a
coprimality assumption. Thus CP1 really gives full homogeneous
division over F2 iff g_n=H(g_d) over F2. Its d=3 unit case and
n=3 case are retained in the accepted body, although HR applies only
to L_i>=13. Nothing in this descent asserts that individual factors
are themselves invariants.

The GK body also proves its identity as a polynomial identity: a
transcendental auxiliary vector gives the recurrence, division by
c+1 cancels into polynomial coefficients, and injective substitution
descends the result. A nonzero function-field denominator is not
asserted to stay nonzero at every finite specialization. HR supplies
its own good finite point and basis below. GK's strict leading-degree
gap prevents cancellation and gives exactly the E_i used here.

For HR's degree argument set Q=q². Since (Q-1)E_r=Q^r-1, one has
Q^r=1 modulo the positive INTEGER E_r without division modulo E_r.
Writing s=br+t, 0<=t<r, each complete block of r summands contributes
zero, so E_s=E_t modulo E_r, with an empty final sum when t=0.
If 0<t<r then 0<E_t<E_r. A composition therefore forces r|s.
The argument uses actual polynomial degrees, not degrees of finite-field
functions. A constant H cannot give nonconstant P_s. Smaller s fail;
if s=r, H has degree one and injective substitution in (H-T)(P_r)=0
forces H=T. Only s=br, b>=2, remains. Divisibility of degrees alone
is not treated as sufficient for composition.

## 4. Every r>=3 has an actual good finite point

Every algebraically closed K of characteristic 2 contains the finite
subfield of q^(2r) elements. Over it consider

    C: X^(q+1)+Y^(q+1)+Z^(q+1)=0.

Because q+1 is odd, the partial derivatives are X^q,Y^q,Z^q;
they have no common projective zero even over the algebraic closure.
Thus the curve is geometrically smooth. A repeated geometric component
would make the gradient vanish on that component. Distinct positive
degree projective plane components intersect, and at an intersection
the product rule again makes the gradient zero. Consequently there is
one reduced component over the closure: C is geometrically integral.
The standard smooth-plane genus formula gives g=q(q-1)/2. I checked
the finite-field and geometric hypotheses of Hasse--Weil separately;
no maximality theorem or exact Hermitian point count is substituted.

The LOWER bound over a field of size q^(2r) is

    #C >= q^(2r)+1-q(q-1)q^r.

At most q+1 points are on Z=0 because the restricted binary form is
nonzero of degree q+1. Therefore the affine equation
a^(q+1)+b^(q+1)=1 has at least

    h(q^r), h(x)=x²-q(q-1)x-q

solutions. For x2>x1>=q³,
h(x2)-h(x1)=(x2-x1)(x2+x1-q(q-1))>0. At x=q³,
h(x)-q^4=q^5(q-1)-q>0. Hence the affine number is strictly greater
than q^4 for EVERY r>=3 and q>=4. This checks the smallest permitted
parameters by the symbolic inequality, not by enumeration.

For v=(a,b), let v^[j] denote coordinatewise q^j-Frobenius. The
ordinary bilinear pairing, not a positive inner product, gives

    v·v^[1]=1, v^[2]·v^[1]=1,
    v·v^[3]=c, v^[2]·v^[3]=1.

Put Delta=det(v^[2],v). The determinant of the pairing matrix is
c+1, while the determinant product of its two vector matrices is
Delta*Delta^q; signs coincide in characteristic 2. Thus
c+1=Delta^(q+1). If c=1, v^[2]=t v since v is nonzero, and pairing
with v^[1] forces t=1. These bad points have a,b in F_(q²), so
there are at most q^4 even in the entire ambient square. Strictly
more affine solutions supplies a good one with c!=1.

If a=0 or b=0, the other coordinate has order dividing q+1 and is
in F_(q²), which makes c=1. Thus both coordinates are nonzero at
the selected good point. In particular B(c)!=0 and
A'(c)=B'(c)=(c+1)^(q-2)!=0. There is no need to require c!=0,
A(c)!=0, or exact extension degree r for the constants. A period
dividing r is sufficient. Frobenius periodicity applies only to these
finite constants, never to the indeterminate T or every element of K.

## 5. Full vector return and the separate derivative vector

The nonzero pairing determinant proves that v^[2],v are a basis and
the two pairing functionals are independent. Writing
v^[4]=alpha v^[2]+beta v yields

    alpha+beta=c^q, alpha+c beta=1.

Division by c+1 is legitimate here and gives
beta=(c+1)^(q-1)=B(c), alpha=c^q+B(c)=A(c). These are exactly the
GK coefficients; no function-field determinant is blindly specialized.

Define w_i=v^[2i+1], a_i=A(c)^(q^(2i+1)),
b_i=B(c)^(q^(2i+1)), M_i=[[a_i,b_i],[1,0]]. Raising the vector
relation by q^(2i+1) gives w_(i+2)=a_i w_(i+1)+b_i w_i. Let S_i
be the matrix with rows w_(i+1),w_i. Then S_(i+1)=M_i S_i;
det S0=Delta^q!=0 and every b_i is nonzero. Thus every S_i is
invertible. Since v^[2r]=v, both S_(j+r)=S_j and M_(j+r)=M_j.
For EVERY j>=0,

    M_(j+r-1)...M_j S_j=S_j
    => M_(j+r-1)...M_j=I.

This is a return on TWO independent vector columns. One scalar
initial vector being fixed would not prove the needed matrix identity.

The evaluated scalar state (P_(i+1)(c),P_i(c)) has initial vector
(c,1). Differentiate the POLYNOMIAL recurrence first: every positive
Frobenius power on a coefficient has zero derivative. Thus the
derivative state obeys the same M_i with initial vector (1,0).
Their r-step returns give

    P_r(c)=1, P_(r+1)(c)=c,
    P_r'(c)=0, P_(r+1)'(c)=1.

These derivative equalities are not obtained by differentiating an
already evaluated finite identity. All shifted returns remain available
for subsequent blocks, whether or not r is the minimal period.

## 6. Exact local order, including possible A(c)=0

Use Z=T-c. The binary digits of q²+1 are positions 0 and 2k;
those of q²-q+1 are position 0 and positions k through 2k-1.
Consequently F(c+Z) has no terms of degree 2 through q-1.
Differentiation gives F'=A^q. The coefficient of Z^q comes only
from the second summand and equals (c+1)^(q²-2q+1), a unit.
The first summand has no q-th term by its binary support.

For every recurrence index i>=1, the coefficient powers are at least
q³. Modulo Z^(q³) all these coefficients may be evaluated at c.
Starting from P1=T and P2=F, the coefficient pairs in the basis
(F,T) evolve by invertible M_i. Their initial state matrix is
invertible, so no individual pair (alpha_i,beta_i) vanishes. Thus

    P_r(c+Z)=alpha_r F(c+Z)+beta_r(c+Z) modulo Z^(q³).

Since P_r'(c)=0, alpha_r A(c)^q+beta_r=0. Were alpha_r=0,
beta_r would also be zero, impossible. Hence alpha_r!=0, even
when A(c)=0. After subtracting P_r(c)=1, the linear term vanishes,
degrees 2..q-1 vanish, and the q-th coefficient is nonzero. The
error threshold q³ is larger than q. Therefore

    ord_Z(P_r(c+Z)-1)=q EXACTLY.

A repeated critical point without this coefficient and matrix argument
would not justify the exact order, and is not used as a substitute.

## 7. The first perturbation: indices, bottom coordinate, persistence

Put M=q^(2r+1), and write the polynomial state as
V_i(T)=(P_(i+1)(T),P_i(T))^t. Work modulo Z^(M+2).
In the block of transfer steps i=r,...,2r-1, every coefficient
perturbation after i=r has order at least q²M>M+1. At i=r the
extra term enters the TOP coordinate and is exactly

    epsilon=(A(c+Z)^M-a_r)P_(r+1)(c+Z)
             +(B(c+Z)^M-b_r)P_r(c+Z).

It has order at least M. Each coefficient factor has only degrees
that are positive multiples of M; 2M>M+1. Its M+1 coefficient
therefore is

    A'(c)^M P_(r+1)'(c)+B'(c)^M P_r'(c)=A'(c)^M!=0.

Let R=M_(2r-1)...M_(r+1). The full shifted return gives R M_r=I,
so R=M_r^(-1)=[[0,1],[1/b_r,a_r/b_r]]. In particular
R(1,0)^t=(0,1/b_r)^t. Propagating the extra term to state index
2r therefore gives

    V_(2r)-V_r=R(1,0)^t epsilon modulo Z^(M+2).

Here the constant product acts on the entire POLYNOMIAL vector V_r;
all perturbations before index r are already in that vector and cancel
under I. There is no omitted assumption that V_r(T) is constant.
Taking the bottom coordinate yields

    ord(P_(2r)-P_r)>=M,
    [Z^(M+1)](P_(2r)-P_r)=A'(c)^M/b_r!=0.

Every later full block starts at an index at least 2r, with first
coefficient perturbation at least q^(4r+1)>M+1. Its constant product
is I by the shifted return. Thus V_(br)=V_(2r) modulo Z^(M+2)
for every integer b>=2. The SAME nonzero coefficient persists in
P_(br)-P_r. There is one retained perturbation, not b-1 repeated
low-order insertions that could cancel modulo 2. This holds for all
later multiples, not just 2r or one subsequence of them.

## 8. Forbidden coefficient and arbitrary outer polynomial

Suppose P_s=H(P_r), s>r. Degree reduction gives s=br with b>=2.
Set J(Y)=H(Y)-Y. If J=0, the just-proved nonzero coefficient already
contradicts the equality. Otherwise J has an exact factorization
(Y-1)^m W(Y), with m>=0 and W(1)!=0. Its composition has exact
Z-order qm. Since P_s-P_r has order at least M, one obtains
m>=e=M/q=q^(2r), a power of characteristic 2 greater than one.

Write J(1+Y)=b_e Y^e+sum_(j>e)b_jY^j, allowing b_e=0.
The term (P_r-1)^e has only exponents divisible by e and cannot
supply M+1=qe+1. All later terms have order at least
q(e+1)=M+q>M+1. Their sum therefore has zero M+1 coefficient,
contradicting the one retained above. This handles inseparable H,
arbitrary coefficients in K, unbounded outer degree and a missing first
permitted coefficient. It does not assume that H' is nonzero, that
the finite critical values are distinct, or that the exact order is M.
This completes HR1 for every r>=3.

## 9. Complete r=2 reconstruction

No unreviewed extension of the even-inner theorem is needed. The
identity (T+1)A=T^(q+1)+1 supplies a root alpha of A with
alpha!=0,1, alpha in F_(q²), alpha^q=alpha^(-1). It also gives
B(alpha)=alpha^(-1), so the odd Frobenius powers occurring in every
coefficient equal alpha. Polynomial differentiation before evaluation
gives, for every h>=0,

    P_(2h)(alpha)=alpha^h, P_(2h)'(alpha)=0,
    P_(2h+1)(alpha)=alpha^(h+1),
    P_(2h+1)'(alpha)=alpha^h.

In particular P2(alpha)=alpha, P2'(alpha)=0, P3'(alpha)=alpha.
The same explicit binary expansion gives
ord_Z(P2(alpha+Z)-alpha)=q. Also A'(alpha)!=0.

For M=q^5, subtract the constant-coefficient part of the recurrence
P4=A^M P3+B^M P2. The difference P4-alpha P2 has order at least
M and nonzero M+1 coefficient A'(alpha)^M alpha; the other
contribution vanishes because P2'=0. For later EVEN recurrence
indices i>=4 the exponent is at least q^9>M+1. The term involving
P_(i+1) is killed modulo Z^(M+2) by its coefficient A^q^(2i+1),
even though that odd polynomial can have lower-order terms.
Consequently, for every even s>=4,

    P_s=alpha^((s-4)/2)P4 modulo Z^(M+2).

Thus P_s-alpha^((s-2)/2)P2 has order at least M and a nonzero
M+1 coefficient. If P_s=H(P2), use
J(Y)=H(Y)-alpha^((s-2)/2)Y at beta=alpha. Exact local order q
and e=M/q=q^4 give precisely the forbidden-coefficient contradiction
of Section 8, including J=0. Degree divisibility excludes odd s,
smaller s, and treats s=2 uniquely. This proves the entire r=2
endpoint independently of merely assuming the older NJ statement.

## 10. Both whole-divisor directions and retained boundaries

For r,s>=1, L_r and L_s are positive odd integers at least
d=q²-q+1>=13. CP1 is therefore within its exact full homogeneous
domain and gives

    phi_(L_r)|phi_(L_s)
       iff g_(L_s)=H(g_(L_r)), H in F2[T].

GK rewrites this as P_s(g_d)=H(P_r(g_d)). Since g_d is
nonconstant, substitution is injective by degree, yielding
P_s=H(P_r). When r>=2, HR1 over an algebraic closure excludes
every s except r. Conversely s=r is equality. When r=1, P1=T
and H=P_s is in F2[T], so CP1 gives division for every s>=1.
These are both directions, with no extension-field-only factor passed
off as an F2 divisor.

No auxiliary P0 or L0=1 goes through CP1. The ordinary n=1 zero
and n=3 unit boundaries of the annual question are not qualifying
two-nonconstant factorizations. The excluded q=2 endpoint is not
silently inferred: there d=3 supplies a unit divisor, while HR assumes
q>=4 throughout. The common q=4 family, r=1 identity inner, s=r
unit cofactor, arbitrary b, A(c)=0, possibly c=0 and nonminimal
finite periods have all been challenged within the proof. None gives
a counterexample to the stated claim.

## 11. Source and integrity disposition

The only new external theorem imports are the standard smooth-plane
genus formula and Hasse--Weil. The source audit records actual primary
read scopes, including Milne's complete modern geometric curve-bound
argument, and separately checks projective component intersection in
Stacks. I do not claim a new proof of Riemann--Roch, intersection theory,
Hodge index or original Weil proofs. The q=1 modulo 4 quotient theorems
in the contextual Montanucci--Zini paper do not apply here and are not
imported. No exact Hermitian maximality, zeta or quotient classification
is used.

The metadata-only freezer verifies the exact constructor records,
declared accepted/context inputs, accepted raw suffixes, prior own
frozen artifacts and prior declared preservation records. Hashes are
administrative integrity, not mathematical evidence. The three complete
review texts and their ledger must exist before a freeze is emitted.
Only this assigned review prefix is written. A missing filename suffix
in an initial read-only attempt was corrected using the exact own file
inventory; no old artifact or candidate was changed.

Disposition: **no substantive scoped issue identified; no author repair
requested on this audit.** The independently frozen second whole audit
and coordinator reconciliation remain required before promotion.
Only HR1/HR2 as stated have been reviewed: all arbitrary annual
exponents, proper components, mixed-q questions, general inner
composition classification, numerical conclusions and novelty remain
outside this result.
