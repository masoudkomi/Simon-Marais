# Whole Kasami criterion KC: whole initial review 2

2026-10-17 UTC. Reviewer `/root/review_2017_coarsening_r1`. Fresh initially
blind nonconstructor WHOLE audit of the NEW necessity argument by root.
Requested gpt-6.1-sol/max; effective readback unavailable. I have read no
new peer KC review, findings or coordinator reconciliation. The complete
2019 linear-output construction was frozen before I opened KC.

**Finding:** no substantive mathematical objection found. All26 submitted
obligations pass. The claimed iff is supported in exactly the domain

\[
 q=2^k,\quad k\ge2,\quad d=q^2-q+1,\quad n\ge3\text{ odd}:
 \qquad
 \phi_d\mid\phi_n\text{ over }\mathbf F_2
 \iff n=\frac{q^{2r+1}+1}{q+1}\text{ for some integer }r\ge1.
\]

This is a WHOLE-divisor theorem, not a classification of individual
Kasami components, arbitrary factors, or the annual reducibility target.
No new numerical test, external group classification or novelty premise
is needed. This review does not promote the candidate.

Exact main7192bytes,
SHA256`390d795343eb32a9496aa9a64c054b4809bd400c37c8195264053d343ba180bf`.
Exact author manifest1202bytes,
SHA256`f08044ef0a1a9d8fa38e26f50e2b261d46ef761e68604060f918c5119816a3f3`.
The entire candidate, all26obligations, entire source audit/JSON and
manifest were read, along with BOTH complete accepted CP/GK bodies and
their scope records. No mathematical program/CAS/scan/author rerun was
used. The integrity packet preserves all earlier frozen bytes.

## Independence boundary and exact dependencies

I constructed OLD CP1--CP3. Accepted CP1 is therefore an explicit
accepted dependency here, not a theorem for which this is a fresh
independent nonconstructor re-audit. I did NOT construct the NEW KC
necessity argument or the separately accepted GK recurrence. The old
CP acceptance rests on its two OTHER initially blind whole reviews.
My earlier audit of NV does not supply a KC proof premise; KC actually
subsumes its valuation conclusion without using its local-order proof.

The official B4(b) asks for all odd positive n admitting coefficientwise
modulo-two factors each nonconstant modulo two. It is a polynomial
factorization problem over F2, not finite-field functional equality or
absolute factorization. The present iff fixes one whole divisor. I do
not reproduce preliminary part(a), assume that all factors are whole
phi_d, or treat the unit-cofactor endpoint as an annual exclusion.

The accepted CP1 input applies to all odd d,n>=3 and gives the actual
F2 identity g_n=H(g_d) iff WHOLE homogeneous phi_d divides phi_n. Its
complete body retains all multiplicities, full dehomogenized degree,
homogenization, rank-four quadratic-cover descent and monic h-adic
composition. Thus it is legitimate to use that exact implication here,
with no individual-factor descent assumption.

Accepted GK1--GK2 applies to EVERY q=2^k,k>=1 and EVERY r>=1, giving
whole phi_d divisibility for n=(q^(2r+1)+1)/(q+1). Its auxiliary r0
value is outside CP1 and is used only as a recurrence start; r1 is
equality. The complete GK body proves an all-index polynomial recurrence,
not an extrapolation from its known r2 instance. Its source/degree scope
is retained in the sufficiency reconstruction below.

## 1. CP1 on the correct affine level set

In the algebraic closure K of F2, use independent variables X,Y and set

\[
 F=X^{q+1}+Y^{q+1},\qquad C=X^{q^3+1}+Y^{q^3+1},
 \qquad m=(q+1)n,\quad P_m=X^m+Y^m.
\]

Here m is odd and greater than one; (q+1)d=q^3+1. CP1 gives H in
F2[T] with G_n=H(G_d) as a univariate POLYNOMIAL identity, where
G_j(x)=x^j+(x+1)^j. At EVERY K-point v=(X,Y) with F(v)=1, put
x=X^(q+1). Characteristic two gives x+1=Y^(q+1), and then

\[
 G_n(x)=P_m(v),\qquad G_d(x)=C(v).
\]

Consequently P_m(v)=H(C(v)) on F=1. This involves no denominator,
generic-point assumption, or finite-field sampling. It does NOT assert
that P_m=H(C) on the whole plane; H need not be homogeneous, and that
invalid extension is not used.

## 2. A genuine nonsingular constant matrix, all entries nonzero

Choose t in F_q outside{0,1}; q>=4 is used HERE. Algebraic closure
supplies nonzero a,b with a^(q+1)=t and b^(q+1)=t+1. Since t and
t+1 are nonzero F_q elements,

\[
 a^{q^2-1}=t^{q-1}=1,\qquad
 b^{q^2-1}=(t+1)^{q-1}=1.
\]

Thus a,b and their qth powers belong to F_(q²). For

\[
 M=\begin{pmatrix}a&b\\ b^q&a^q\end{pmatrix},
 \quad M^{[1]}=\begin{pmatrix}a^q&b^q\\ b&a\end{pmatrix},
 \quad M^T=\begin{pmatrix}a&b^q\\ b&a^q\end{pmatrix},
\]

all four entries of M are nonzero and
det M=a^(q+1)+b^(q+1)=t+(t+1)=1. Direct multiplication, without a
unitary-group theorem, gives

\[
 M^TM^{[1]}=
 \begin{pmatrix}
 a^{q+1}+b^{q+1}&ab^q+b^qa\\
 ba^q+a^qb&b^{q+1}+a^{q+1}
 \end{pmatrix}=Id.
\]

Entrywise q³th powers of CONSTANT M equal its entrywise qth powers,
because its entries lie in F_(q²). No variable X or Y is assumed fixed
by q²-Frobenius. Writing v^[j] for entrywise q^jth powers of variables,
ordinary Frobenius polynomial identities give

\[
 F(Mv)=v^TM^TM^{[1]}v^{[1]}=F(v),
 \qquad C(Mv)=v^TM^TM^{[3]}v^{[3]}=C(v).
\]

These are homogeneous identities for independent variables. The field
used in accepted GK's auxiliary transcendental computation is different;
no finite-field periodicity from this NEW constant matrix is being
silently imposed there.

## 3. Homogeneous difference and the passage to all points

If F(v)=1, also F(Mv)=1 and C(Mv)=C(v), so P_m(Mv)=P_m(v). Define

\[
 D(v)=P_m(Mv)+P_m(v).
\]

D is homogeneous of degree m, EVEN THOUGH H(C) need not be homogeneous.
If F(v) is nonzero, choose a nonzero scalar l in K with
l^(q+1)=1/F(v). Algebraic closure supplies it. Then F(lv)=1, and
homogeneity gives

\[
 0=D(lv)=l^mD(v),\qquad D(v)=0.
\]

No division by F(v)=0 occurs. To pass from this vanishing set to a
polynomial identity, take v=(x,1). The nonzero polynomial
F(x,1)=x^(q+1)+1 has at most q+1 roots. K is infinite, so D(x,1)
vanishes for infinitely many x and is identically zero. For a homogeneous
binary polynomial of fixed degree, substitution Y=1 is injective on its
coefficient vector: X^iY^(m-i) becomes X^i. Hence D itself is zero, and

\[
 (aX+bY)^m+(b^qX+a^qY)^m=X^m+Y^m.                    \tag{A}
\]

This justifies the potentially delicate inference in full. Neither
irreducibility of F=1 nor a density theorem or a function identity on
F_(q²) is required. Points of F=0, the line Y=0, and the origin are
included by the resulting polynomial identity, not by illegal scaling.

## 4. Binary support and two proper adjacent coefficients

If S is the set of nonzero binary positions of m, then

\[
 (1+Z)^m=\prod_{i\in S}(1+Z^{2^i}).
\]

Each subset contributes a unique binary sum, so binomial(m,j) is odd
exactly for these sums. Suppose m has at least three set bits. Its
oddness puts0 in S; choose h>=1 in S and let j=2^h. The subsets
{h} and{0,h} give both j and j+1. A further set bit outside that
pair exists, so

\[
 0<j<j+1<m.
\]

Thus BOTH are genuine mixed coefficients in(A), not pure-endpoint
terms. With binomial factors equal to one, their vanishing says

\[
 a^{m-j}b^j=(b^q)^{m-j}(a^q)^j,
 \qquad
 a^{m-j-1}b^{j+1}=(b^q)^{m-j-1}(a^q)^{j+1}.
\]

Every factor used in division is nonzero, and dividing gives
b/a=a^q/b^q. Therefore b^(q+1)=a^(q+1), contradicting their sum1
(equivalently, forcing det M=0). This is a complete coefficient proof,
without a classification of automorphisms of Fermat forms.

The binary weight is at most two. Weight zero is impossible for m>1;
weight one and oddness would give m=1, also impossible. Exactly two
bits remain, one at position0, so

\[
 m=2^s+1,\qquad s\ge1.                                \tag{B}
\]

The nonsingularity and ALL-four-nonzero-entry hypotheses are essential
to the ratio proof. In particular a monomial matrix symmetry would not
provide this conclusion. Their actual construction above, rather than
an asserted group order, supplies precisely the required matrix.

## 5. Integer divisibility and endpoints

By definition q+1 divides m; (B) gives2^k+1 dividing2^s+1. Write
s=A k+B with A>=0 and0<=B<k. Reducing modulo2^k+1 gives the integer
representative(-1)^A2^B+1. If A is even this is strictly between0
and2^k+1, so divisibility is impossible. If A is odd its absolute
value2^B-1 is smaller than2^k+1; divisibility forces B=0. Hence A
is a positive odd integer, A=2r+1 with r>=0, and

\[
 s=k(2r+1),\qquad n=\frac{q^{2r+1}+1}{q+1}.
\]

The r0 value is n1, outside n>=3, leaving r>=1. This proves the
ENTIRE necessary progression, with no restriction to a residue slice,
small r, or experimentally observed exponents. Its minimum n is the
r1 value d; in particular no n<d in the stated domain can have the
whole divisor. The elementary remainder proof avoids an unproved
multiplicative-order assertion for the composite integer2^k+1.

## 6. Sufficiency from the complete accepted all-index GK input

For clarity I checked the complete accepted GK mechanism, not only its
statement. In its transcendental auxiliary setting the ordinary vector
pairings of v and its Frobenius powers yield D0=1,D1=c. A pairing
matrix with determinant c+1 gives

\[
 v^{[4]}=A_q(c)v^{[2]}+B_q(c)v,
 \quad A_q(T)=T^q+(T+1)^{q-1},\quad B_q(T)=(T+1)^{q-1}.
\]

The temporary division by c+1 cancels in these polynomial coefficients.
Frobenius propagation and dotting with the ORIGINAL v gives its stated
all-index recurrence for P_r, with D_r=P_r(c). The transcendental
evaluation and injective substitution U=a²+a descend to an actual F2
polynomial identity g_(L_r)=P_r(g_d), valid also at finite zeros of
c+1. The monic degree induction compares its two summands; their
degree difference q^(2r)(q+1)>0 prevents leading cancellation. Thus
this accepted input covers every r, rather than assuming the r2
identity continues.

For r>=1, L_r is odd>=3, so CP1 converts this F2 composition into
whole homogeneous divisibility over F2. This gives exactly the converse
needed for KC. For q>=4,r>=2, degrees d-3>0 and L_r-d>0 give two
nonconstant F2 factors; coefficientwise0/1 integer lifts then meet the
official congruence. No extension-field factor is being descended from
an absolute factorization theorem. At r1 the cofactor is a unit, as
correctly stated; no conclusion about whether phi_d itself has some
OTHER official factorization is drawn from that fact.

## 7. Adversarial boundaries, source role and remaining annual question

* q4 is included: t in F4 outside{0,1} exists, and the matrix proof
  applies without a hidden odd-k assumption. Its progression agrees
  with the older exact phi13 criterion. The latter is a compatibility
  check, not the necessity premise for arbitrary k.
* q2 must stay excluded. phi3=1 divides every phi_n; n5 would violate
  the written progression. There is also no t outside{0,1} in F2,
  so the required all-entry matrix is not falsely claimed there.
* n3 is the unit quotient and cannot contain nonconstant phi_d for
  q>=4. n1 is outside CP1/KC and retains the official zero-polynomial
  discussion; I do not assert an artificial failure of division into
  zero. Even n is outside the theorem and the odd-m support step.
* At r1, n=d and the whole equality is valid. At every r>=2 the
  positive-degree cofactor assertion has the correct strict inequality.
* The iff implies NV because n-1=q(q^(2r)-1)/(q+1), with the indicated
  integer quotient odd. This agrees with v2(n-1)=k but does not
  use or change the earlier frozen NV proof.
* Partial F=1 symmetry is not mistaken for a global H(C) identity;
  finite-field Frobenius fixes only constants; and actual polynomial
  invariance is established over an infinite algebraic closure.

The source motivation note is historical/unverified context. Primary
Zieve and Cohen--Matthews introductory material was inspected only in
that role. None of its absolute-component, monodromy, exceptionality,
finite-group or group-order claims supplies a proof step here. The
matrix and binary coefficient reasoning stand on their displayed
elementary identities plus accepted CP1/GK. No unread external theorem
fills a gap, no mathematical code or finite orbit test was needed,
and novelty is unestablished. KC does not decide arbitrary phi_n
reducibility or the annual problem. No repair requested in this scope;
coordinator reconciliation with both whole blind initials is required.
