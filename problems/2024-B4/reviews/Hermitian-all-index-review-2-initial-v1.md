# Initially blind WHOLE HR1/HR2 audit, reviewer 2

2026-10-17 UTC. Reviewer `/root/review_2021_reasoning_j15_r2`.
Requested `gpt-6.1-sol/max`; independently verified effective settings
remain unavailable. This is a review recommendation, not coordinator
promotion. The submission remains candidate proof - unverified until
the required independent review and reconciliation procedure finishes.

**Recommendation:** no substantive defect or required author repair was
found in the COMPLETE stated HR1/HR2 argument. This recommendation is
restricted to its fixed-q composition and WHOLE-divisor conclusions.
It supplies neither the full official reducibility classification nor
a statement about arbitrary proper factors or novelty.

## Exact target, independence and complete read scope

The entire target is
`notes/coordinator-Hermitian-all-index-return-v1.md`, 15281 bytes,
SHA256 `296241f7538f7eb86315998ff760f4fa363d3a2d1c911988d6fa2b1a4f0287cc`.
Its 3214-byte manifest has SHA256
`d93f76bb4aecc912bb9dc91a51714d41330d250ba333ca7a32061d39a36df0a3`.
I read the COMPLETE main, all 24 obligations, the entire source audit
and worklog, and the full accepted GK and CP mathematical bodies and
acceptances. I also read the complete accepted even-inner NJ body and
acceptance, and the separate unverified odd-period historical lead.
None of the new HR peer reports, findings or later root inspection was
read before this whole report, inference ledger and source/integrity
packet were completed and frozen. No substantive partial verdict was
sent to the constructor before the full initial freeze.

I authored older T1--T4/C7/C11 material, and previously reviewed the
CP, GK, critical-jet, indecomposability and even-inner NJ submissions.
Those roles are disclosed; this is not independent recertification of
my old work. I did NOT construct or contribute the NEW Hermitian-point,
full shifted-return or all-index HR construction. Root constructed HR
and is excluded from independent reviewer count. The old NJ theorem is
a consistency check here, not a substitute for reconstructing r=2.

The audit used hand algebra and actual public primary source reads.
No mathematical executable, scan, point enumeration, CAS, certificate
replay or author rerun was used. Administrative hash/JSON operations
are preservation checks only. All changes are confined to the assigned
`reviews/Hermitian-all-index-review-2-*` prefix. The preceding COMPLETE
2022 R6 constructor checkpoint was frozen before reading this target.

## 1. Definitions, degree obstruction and boundaries

Fix q=2^k>=4. All polynomials A, B and P_i are the accepted GK
polynomials, with P0=1, P1=T and

    P_(i+2)=A^(q^(2i+1)) P_(i+1)+B^(q^(2i+1)) P_i.

GK gives monic degree E_i=sum_(j=0)^(i-1) q^(2j) for i>=1, and
P2=F=T^(q²+1)+(T+1)^(q²-q+1). These are polynomial identities over
F2, and remain so over any algebraically closed characteristic-two K.
An arbitrary H in K[T] satisfying P_s=H(P_r) is nonconstant; therefore
E_r divides E_s as ordinary positive integers. Put Q=q² and write
s=br+t, 0<=t<r. The congruences Q^r=1 modulo E_r and E_r=0 modulo
itself give E_s=E_t modulo E_r, where E0 is the empty sum 0. For
0<t<r, 0<E_t<E_r. Hence r divides s. No converse composition
criterion is being inferred from that integer test.

The smaller targets fail by strictly increasing degrees. At s=r,
injectivity of K[Y] -> K[T], Y->P_r(T), forces H(Y)=Y. Index0 is
outside both claims; the special inner index1 is P1=T and permits
every P_s. The latter is essential for HR2 and is retained explicitly.

## 2. The Hermitian point and the bad-point bound

For r>=3 take the finite subfield F_(q^(2r)) inside K. The homogeneous
equation X^(q+1)+Y^(q+1)+Z^(q+1)=0 is projective and its geometric
partial derivatives X^q,Y^q,Z^q have no common projective zero.
Thus the plane curve is smooth after algebraic closure. A repeated
factor would contradict smoothness. Distinct positive-degree plane
components intersect over an algebraic closure, and their intersection
would also be singular. This proves geometric integrality rather than
assuming it from the word "Hermitian". The degree is q+1, prime to
characteristic2, and its genus is q(q-1)/2.

The attributed Hasse--Weil inequality applies with field size q^(2r)
and square root q^r. Subtracting at most q+1 points on Z=0 gives at
least

    q^(2r)-q(q-1)q^r-q

affine solutions of a^(q+1)+b^(q+1)=1. For x>=q³ the real expression
x²-q(q-1)x-q is strictly increasing: its difference at y>x is
(y-x)(y+x-q(q-1))>0. At x=q³, its excess over q^4 is
q^5(q-1)-q>0. Therefore the strict affine lower bound exceeds q^4
for EVERY r>=3, including r=3 and q=4. No exact Hermitian point count
or maximality assertion is required.

Write v=(a,b), v^[j]=(a^(q^j),b^(q^j)), and use the ordinary bilinear
dot product. Let c=v dot v^[3] and Delta=det(v^[2],v). The four
pairings with the two basis candidates and two functionals are

    v^[2] dot v^[1]=1,   v^[2] dot v^[3]=1,
    v dot v^[1]=1,       v dot v^[3]=c.

The determinant of this pairing matrix is c+1. The determinant of
its first factor is Delta, and that of the other is Delta^q (signs
coincide in characteristic2). Thus c+1=Delta^(q+1). If c=1,
Delta=0, and v^[2]=t v since v!=0. Pairing with v^[1] gives t=1.
Then both coordinates belong to F_(q²). There are at most q^4 such
ordered pairs in the ambient square. The strict count therefore
produces a good point with c!=1. This also gives B(c)!=0 and
A'(c)=B'(c)=(c+1)^(q-2)!=0. If a or b vanished, the other would
have order dividing q+1, hence lie in F_(q²), contradicting goodness.

The finite constants, not the polynomial variable or all of K, have
q^(2r)-Frobenius period. No exact period r is needed.

## 3. Two independent columns prove EVERY shifted return

At the good point v^[2],v are a basis. Pair v^[4]=alpha v^[2]+beta v
against v^[1],v^[3]. This gives alpha+beta=c^q and alpha+c beta=1.
The only division is by c+1, which is nonzero at the actual chosen
point, and the results are the polynomial values beta=B(c),
alpha=A(c). Thus the full vector relation, not merely two necessary
scalar equations, has been recovered.

Set w_i=v^[2i+1] and M_i=[[a_i,b_i],[1,0]], with
a_i=A(c)^(q^(2i+1)), b_i=B(c)^(q^(2i+1)). Frobenius gives
w_(i+2)=a_i w_(i+1)+b_i w_i. The stacked row matrix
S_i=[w_(i+1);w_i] satisfies S_(i+1)=M_i S_i. Its initial determinant
is Delta^q!=0, and every b_i is a unit, so every S_i is invertible.
Both S_(j+r)=S_j and M_(i+r)=M_i hold for the finite constants.
Consequently, for EVERY j>=0,

    (M_(j+r-1)...M_j) S_j=S_j,
    M_(j+r-1)...M_j=I.

This is a full two-dimensional matrix identity. One fixed scalar
column would not justify it. Period dividing r still gives the same
identity and causes no degeneracy.

The polynomial value vector (P_(i+1)(c),P_i(c)) starts at (c,1) and
obeys these same matrices. Separately differentiate the polynomial
recurrence: every coefficient Frobenius power has derivative0, so
the derivative vector obeys the same matrices with initial (1,0).
The return at j=0 therefore gives

    P_r(c)=1, P_(r+1)(c)=c,
    P_r'(c)=0, P_(r+1)'(c)=1.

No derivative of an evaluated constant identity has been taken.

## 4. Ramification order is exactly q

Put Z=T-c. The binary positions of q²+1 are 0 and 2k; those of
q²-q+1 are 0 and k,...,2k-1. The characteristic-two binomial
expansion at ANY c has no degrees2,...,q-1. Also F'=A^q, and
its degree-q Taylor coefficient is

    u=(c+1)^(q²-2q+1)!=0.

Only the second summand contributes to that coefficient. For all
recurrences with i>=1, coefficient perturbations have order at least
q³. Modulo Z^(q³), P1=T and P2=F therefore generate every subsequent
P_i as alpha_i F+beta_i T with constant coefficients. The two-row
matrix of coefficient pairs starts as the identity at P2,P1 and is
multiplied by invertible M_i. Its rows never vanish. Since P_r'(c)=0,

    alpha_r A(c)^q+beta_r=0.

If alpha_r were zero then beta_r would be zero too, impossible.
Thus alpha_r!=0. Subtracting P_r(c)=1 removes the constant; the
linear term vanishes, the terms2,...,q-1 are absent, and the q term
is alpha_r u!=0. The error threshold q³ is strictly larger than q.
This proves ord_Z(P_r(c+Z)-1)=q, including possible A(c)=0.

The argument does not mistake a repeated derivative root for an exact
ramification order, and does not assume F,T span arbitrary polynomials
without the stated truncation.

## 5. First perturbation, bottom inverse entry and persistence

Fix M=q^(2r+1), and let V_i(T)=(P_(i+1)(T),P_i(T))^t. Work modulo
Z^(M+2). Across the r steps i=r,...,2r-1, the perturbation of the
first matrix has order M; every later one has order at least q²M,
which is larger than M+1. The first error enters the TOP coordinate:

    epsilon=(A(c+Z)^M-a_r) P_(r+1)(c+Z)
            +(B(c+Z)^M-b_r) P_r(c+Z).

Each coefficient difference has only positive multiples of M as
possible exponents. Hence epsilon has order at least M and

    [Z^(M+1)]epsilon
       =A'(c)^M P_(r+1)'(c)+B'(c)^M P_r'(c)
       =A'(c)^M!=0.

The constant times a hypothetical coefficient at M+1 contributes
nothing because M does not divide M+1; the next multiple2M is too
large. The second displayed product is zero by P_r'(c)=0. This
accounts for both summands, including a possible A(c)=0.

Write R=M_(2r-1)...M_(r+1). The full shifted return at j=r gives
R M_r=I, so R=M_r^(-1). Thus

    V_(2r)(c+Z)-V_r(c+Z)=R(1,0)^t epsilon mod Z^(M+2).

The explicit inverse is [[0,1],[1/b_r,a_r/b_r]]; its first column's
BOTTOM entry is 1/b_r. The bottom components of V_(2r),V_r are
P_(2r),P_r respectively. Therefore their difference has order at
least M and coefficient A'(c)^M/b_r!=0 at M+1. The row/column and
index choices in the candidate agree exactly with this calculation.

In every later full block, beginning i>=2r, ALL coefficient errors
begin above M+1. Its constant product is I at its actual shifted
index. Therefore V_(br)=V_(2r) modulo Z^(M+2) for EVERY b>=2.
There is one retained perturbation; later blocks contribute no new
term at this degree. The characteristic-two parity of b is irrelevant,
as is any smaller actual period of the good point. This proves the
two claims in equation(12) for all multiples, without extrapolation.

## 6. Forbidden coefficient, with arbitrary outer polynomial

Suppose s=br>r and P_s=H(P_r). If J(Y)=H(Y)-Y is zero, the
nonzero coefficient above is immediately contradictory. Otherwise
write J(Y)=(Y-1)^m W(Y), W(1)!=0. With V=P_r(c+Z)-1 of exact
order q, the exact order of J(1+V) is qm. The lower bound M yields
m>=e=M/q=q^(2r). Its Taylor expansion can start at e or later.
The e-th term, if present, is a Frobenius power V^e and only has
exponents divisible by e; M+1=qe+1 is not such an exponent. Every
later Taylor term has order at least q(e+1)=M+q>M+1. Hence the
composition has ZERO coefficient there, contradicting the retained
nonzero coefficient. A missing e-th term makes no difference.

This proof allows inseparable H, zero derivative or high multiplicity
at1, arbitrary extension coefficients and arbitrary outer degree.
It completes the claimed exclusion for r>=3.

## 7. The r=2 endpoint is fully reconstructed

Choose a root alpha of A. The identity (T+1)A=T^(q+1)+1 gives
q simple roots, all nonzero and different from1, in F_(q²).
Thus alpha^q=alpha^(-1), B(alpha)=alpha^(-1), and
B(alpha)^(q^(2i+1))=alpha at every index. Differentiating the
recurrence before evaluation yields, for h>=0,

    P_(2h)(alpha)=alpha^h,       P_(2h)'(alpha)=0,
    P_(2h+1)(alpha)=alpha^(h+1), P_(2h+1)'(alpha)=alpha^h.

In particular F(alpha)=alpha, F'(alpha)=0, and its degree-q Taylor
coefficient is (alpha+1)^(q²-2q+1)!=0 by the same binary expansion.
Thus F-alpha has exact local order q. Degrees require any larger
target to have even s. With M=q^5,

    P4-alpha P2=A^M P3+(B^M-alpha)P2

has order at least M and coefficient A'(alpha)^M alpha!=0 at M+1.
All subsequent even recurrences have exponent at least q^9>M+1,
so for even s>=4,

    P_s=alpha^((s-4)/2) P4 mod Z^(M+2).

Subtract alpha^((s-2)/2)P2. This difference has the same order lower
bound and a nonzero M+1 coefficient, multiplied by a unit. Set
J(Y)=H(Y)-alpha^((s-2)/2)Y and expand at Y=alpha. Exact local order
q forces its Taylor multiplicity at least q^4; the first possible
power is Frobenius and all higher powers start at M+q. The same
forbidden coefficient gives a contradiction. No Hasse point for r=2
or preaccepted NJ conclusion has been substituted into this proof.
Smaller targets and equality were handled in Section1.

## 8. Both WHOLE-divisor directions and official scope

For r,s>=1, L_r and L_s are odd integers at least d=q²-q+1>=13.
The full accepted CP1 criterion gives

    phi_(L_r)|phi_(L_s) over F2
       iff g_(L_s)=H(g_(L_r)) for some H in F2[T].

The complete CP body includes the invertible homogeneous coordinate
change, full affine degrees (no lost dehomogenizing-line factor), the
rank-four free-module descent through both quadratic covers and the
monic h-adic argument. It does not cancel a diagonal factor by a
coprimality assumption. Thus multiplicities and homogeneous division
are within its accepted scope, rather than just finite-field values.

GK replaces the two sides by P_s(g_d) and H(P_r(g_d)). Since g_d
is nonconstant, substitution into it is injective over F2. Division
therefore implies P_s=H(P_r). For r>=2, the newly reconstructed HR1
forces s=r. Conversely equality gives division. For r=1, P1=T and
H=P_s give the polynomial identity, and CP1 gives division for every
s. These establish both directions of HR2, including the r1 exception.

At equality the cofactor is a unit. Proper components, other inner
polynomials, mixed q and arbitrary official exponents remain outside
the statement. The previously accepted smaller whole phi_d factors
persist for s>=2; this theorem does not assert irreducibility. The
auxiliary L0=1 is excluded; q=2 and the phi3 unit boundary are not
silently promoted into the q>=4 claim. Integer lifts and the official
coefficientwise interpretation remain as in accepted CP/GK; no function
identity on F2^3 replaces polynomial divisibility.

## Adversarial checks and disposition

The accompanying 48-row inference ledger covers every HR-O01--24,
including all shifts, exact local orders, both epsilon summands and
all endpoints. I specifically challenged scalar-only return, use of
an exact period, a zero A(c), cancellation after an even number of
blocks, high Taylor multiplicity, inseparability, r=2 and a lost
homogeneous factor. The complete proof supplies the needed information
in each case. No substantive issue or required repair remains in this
review. The source record distinguishes theorem imports from hand
deductions and from unused historical/context material.

This recommendation does not remove the coordinator's responsibility
to read both complete initially blind audits and reconcile their issue
ledgers. No acceptance, annual solution or priority claim is made here.
