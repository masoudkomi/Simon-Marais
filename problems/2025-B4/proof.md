# 2025 B4 proof register

No candidate full solution is proposed. The unrestricted nontrivial problem remains unresolved in this project. Published results are attributed in references.md; the elementary arguments below are project-written observations, with no novelty claim.

## P2025-v1: elementary domain reductions

**candidate proof - unverified**. Version 1, 2026-10-16. This is a partial result only, awaiting two independent blind adversarial reviews, including one reconstruction. Finite checks in computations/ are evidence and do not change this status.

Write
\[
G_m(x)=1+x+\cdots+x^{m-1},\qquad m=n+1\ge3.
\]
Here n always denotes the official degree; m always denotes the number of terms. No argument for the preliminary degree-three, odd-exponent equation is reproduced.

### C1. All boundary families and the sign restriction

Claim: all solutions with |x|<=1 are the following, with n,q>=2 throughout:

1. x=0, y=1 for every q, and y=-1 when q is even; n is arbitrary.
2. x=-1, n even: y=1 for every q, and y=-1 when q is even.
3. x=-1, n odd: y=0 for every q.
4. x=1: choose an integer a>=2, q>=2, put n=a^q-1, and take y=a; y=-a is also allowed exactly when q is even.

For |x|>=2, |G_m(x)|>1. Thus the listed families also contain every solution with y in {-1,0,1}. If x>=2, G_m(x)>1. If x=-a<=-2, then
\[
G_m(-a)=
\begin{cases}
(a^m+1)/(a+1)>1,&m\text{ odd},\\
-(a^m-1)/(a+1)<-1,&m\text{ even}.
\end{cases}
\]
Consequently, outside the boundary families, a negative sum occurs precisely for x<=-2 and n odd; it forces q odd and y<=-2. A positive sum forces y>=2 when q is odd, and allows either sign of y when q is even.

Proof. Direct substitution gives G_m(0)=1, G_m(1)=m, and G_m(-1)=1 for m odd and 0 for m even. The integer roots of 0 and 1 give families 1-3. The roots of m>=3 give family 4. For x>=2 positivity and the magnitude bound follow from the first three terms. For x=-a<=-2, multiply the displayed sums by -a-1. In the odd case m>=3 and (a^m+1)/(a+1)>=a^2-a+1>=3. In the even case m>=4 and (a^m-1)/(a+1)>1, since a^m-1>=a^4-1>a+1. These bounds exclude any further y in {-1,0,1}; the remaining sign assertions follow from the parity of a power. This proves C1 as a candidate argument.

### C2. Coprimality and valuations

Claim: for every integer x and m>=3,
\[
\gcd(G_m(x),x)=1,\qquad
\gcd(G_m(x),x-1)=\gcd(m,x-1).
\]
Gcds are nonnegative. For |x|>=2, if an odd prime p divides x-1, then
\[
v_p(G_m(x))=v_p(m).
\]
Continue to assume |x|>=2. If x is odd and m is even, then
\[
v_2(G_m(x))=v_2(x+1)+v_2(m)-1.
\]
If x is even, or if x is odd and m is odd, G_m(x) is odd.

Proof. The congruences G_m(x)=1 modulo x and G_m(x)=m modulo x-1 give the gcd identities, with x=0 or 1 checked directly. For the odd-prime formula use
\((x-1)G_m(x)=x^m-1\) and the standard integer LTE identity
\(v_p(x^m-1)=v_p(x-1)+v_p(m)\), whose hypotheses here are p odd, p|(x-1), p not dividing x, and m>0. Negative x is allowed. For the two-adic formula the relevant LTE hypotheses are x odd, |x|>=2, and m positive even, giving
\(v_2(x^m-1)=v_2(x-1)+v_2(x+1)+v_2(m)-1\); subtract v_2(x-1). The oddness claims follow by reducing the sum modulo 2. Thus for an actual solution the displayed valuations must be multiples of q. This proves C2 subject to checking these stated standard LTE identities during review.

### C3. Degree two admits no nontrivial even exponent

Claim: if n=2 and q is even, then x is 0 or -1 and y is 1 or -1.

Proof. The polynomial x^2+x+1 is unchanged by replacing x by -x-1. For x outside {0,-1}, let t=max(x,-x-1)>=1. Then
\[
t^2<t^2+t+1<(t+1)^2.
\]
It is not a square. An even power is a square, so no such x occurs. The remaining cases follow from C1. This treats a portion of (b), not the preliminary degree-three equation.

### C4. Exponent reduction and a safe factorization rule

Claim: if q>=2 and a prime ell divides q, any solution gives
\[
G_m(x)=Y^\ell,\qquad Y=y^{q/\ell}\in\mathbb Z.
\]
If m=rs for positive integers r,s, then
\[
G_m(x)=G_r(x)G_s(x^r),\qquad
\gcd(G_r(x),G_s(x^r))=\gcd(G_r(x),s).
\]
Thus, for |x|>=2, when this gcd is 1 and the product is a qth power, each factor's absolute value is a qth power. This rule does not assert that arbitrary cyclotomic factors are coprime.

Proof. The exponent identity is immediate. The factorization expands each monomial x^(i+rj) once, for 0<=i<r and 0<=j<s. The polynomial G_s(T)-s is divisible by T-1 in Z[T]. Substituting T=x^r and using x^r-1=(x-1)G_r(x) shows that G_s(x^r)-s is an integer multiple of G_r(x), including when G_r(x)=0; the gcd identity follows. For two nonzero coprime factors, every prime valuation of one factor is the corresponding valuation of the product, hence a multiple of q. Unique factorization in the integers proves the absolute-value assertion. In the applications here |x|>=2, so neither geometric factor vanishes.

## Conjectural full answer, not a proof

The usual integer Nagell-Ljunggren conjecture, together with C1, predicts the above boundary families and exactly these nontrivial official-domain quadruples:
\[
(3,\pm11,4,2),\quad(7,\pm20,3,2),\quad
(18,7,2,3),\quad(-19,7,2,3).
\]
Each displayed identity was checked by exact substitution. The claim that there are no further nontrivial solutions has not been proved here. Positive-x results cannot silently establish this integer-domain conclusion. No result in this file has been promoted to proved, independently reviewed.
