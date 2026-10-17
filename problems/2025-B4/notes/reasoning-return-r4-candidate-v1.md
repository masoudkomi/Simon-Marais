# 2025 B4(b): free positive Fermat-module elements and exact Fueter symmetry

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
`/root/review_2017_coarsening_r1`. Two other independent, initially blind
whole adversarial audits are required. The arguments below are elementary
group-ring and finite-field arguments; novelty is unestablished. They supply
NO new Nagell–Ljunggren exclusion, upper bound, class-number criterion,
source-proof repair, or complete solution of the annual problem.

The official problem has integer x,y and degree n_off>=2, exponent q>=2:

    G_m(x)=1+x+...+x^(m-1)=y^q,  m=n_off+1>=3.

The motivating unresolved sector is the diagonal m=q=p. Accepted CF1 leaves
two second-case residues in its finite prime range, and accepted MS1–MS5
identify an unresolved stabilizer condition in a source's coefficient
selection. The results here address that algebraic selection condition.
No assertion about arbitrary signed x or an actual solution follows merely
from constructing these group-ring elements. The preliminary part(a) is
not investigated or reproduced.

## Definitions and precise proposed results

Let p be an odd prime, G=F_p^* written as automorphisms sigma_a with
sigma_a(zeta)=zeta^a for a primitive p-th root zeta. ALL automorphism indices
in the definitions F and M_r below are DIRECT. Put

    Z[G] = {theta=sum_a t_a sigma_a : t_a in Z},
    N=sum_a sigma_a,  j=sigma_(-1),
    F(theta)=sum_a t_a a in F_p,
    M_r(theta)=sum_a t_a a^(-r) in F_p  (r positive).

Thus zeta^theta=zeta^(F(theta)), whereas M_1 is the INVERSE moment in the
accepted MS packet. The two are different. For h in F_p^*,

    F(sigma_h theta)=h F(theta),
    M_r(sigma_h theta)=h^(-r) M_r(theta).                     (1)

Let wt(theta)=sum_a t_a; call theta positive when every t_a>=0. Define

    vartheta=(1/p) sum_(c=1)^(p-1) c sigma_c^(-1),
    I=Z[G] intersect vartheta Z[G],
    I_f=I intersect ker F,   I_0={theta in I_f : theta positive}.

Only membership in this explicitly defined module is used; no annihilation,
Jacobi-generator, class-field or Diophantine theorem is imported. These
definitions and the inverse-index convention match the original diagonal
chapter, Section2.3, equations14–18. For 1<=t<=p-2 put

    Theta_a=sum_c floor(ac/p) sigma_c^(-1)  (a>0,p not dividing a),
    psi_t=Theta_(t+1)-Theta_t
         =sum_c nu_c(t) sigma_c^(-1),
    nu_c(t)=floor((t+1)c/p)-floor(tc/p).                      (2)

The Fueter index t is NOT the official degree or term count. In particular
t=0,-1 mod p are excluded. Source formulas will be rederived where used.

**FS1 (exact stabilizer).** For every prime p>=5 and 1<=t<=p-2,

    Stab_G(psi_t)={1},                     if t^2+t+1!=0 mod p;
    Stab_G(psi_t)={1,t,t^2},               if t^2+t+1=0 mod p.

In the second case t has order3 and F(psi_t)=M_1(psi_t)=0. This is an actual
threefold coefficient symmetry, not merely the failure of one freeness test.
The cubic inverse moment is M_3(psi_t)=-1/40 there. That formula is used
only for p>=7; an exceptional t cannot exist at p=5.

**FS2 (one universally available free positive element).** For EVERY prime
p>7 there is theta in I_0 with

    wt(theta)=p-1,  theta+j theta=2N,  M_1(theta)!=0.         (3)

It is explicitly constructed as twice one Fueter element or as the sum of
two Galois translates of Fueter elements. Its G-stabilizer is trivial.
This is not a claim of two distinct free orbits at this same weight.
The existence conclusion already occurs in Bartolome–Mihailescu,
Lemma2.7 of [arXiv1412.5798v2](https://arxiv.org/pdf/1412.5798v2), internal
version1.13,2021-11-02. Here it receives a self-contained alternative
proof for p>7, with nonconstancy proved on the NONEXCEPTIONAL indices.
It is not presented as a new existence theorem or a novel method.

**FS3 (many separated free orbits at a larger weight).** For EVERY prime
p>7 and integer k>=2 there are k+1 positive elements of I_f, each of weight
k(p-1), whose G-stabilizers are trivial and which are pairwise NOT Galois
conjugate. Consequently their Fourier values comprise k+1 disjoint sets
of p-1 distinct values. In particular, at weight2(p-1) one obtains THREE
such free orbits. The increase in weight is explicit and proof-critical.

## 1. Elementary coefficient identities

For any positive a prime to p let r_a(c) be the representative in
{1,...,p-1} of ac mod p. The coefficient of sigma_c^(-1) in sigma_a
vartheta is r_a(c)/p. Therefore

    Theta_a=(a-sigma_a) vartheta in I,
    psi_t=(1+sigma_t-sigma_(t+1)) vartheta in I.             (4)

The inverse-index coefficient calculation, not a change to direct indices,
justifies these identities. For (2), write

    p nu_c(t)=c+r_t(c)-r_(t+1)(c).

The right side is either0 or p, so nu_c(t) is0 or1. Since t and t+1 are
nonzero mod p, floor(a(p-c)/p)=a-1-floor(ac/p) for each a=t,t+1, whence

    nu_c(t)+nu_(p-c)(t)=1,
    psi_t+j psi_t=N,  wt(psi_t)=(p-1)/2.                  (5)

In particular N belongs to I. All positive sums used below remain in I;
G-translates permute coefficients and preserve positivity and weight.
Also F(N)=M_1(N)=0, since the nonzero residues and their inverses each sum
to0 in F_p. Formula(1) follows by multiplying DIRECT indices; it also
shows that M_1(theta)!=0 forces a trivial stabilizer.

## 2. Two exact moments of the Fuchsian elements

We reconstruct the accepted inverse-moment computation and add its cubic
analogue. Set u_c=floor(ac/p), r_c=ac-pu_c. The r_c permute1,...,p-1.
Write S_2=sum c^2=p(p-1)(2p-1)/6. For p>=5, S_2/p is integral and
S_2/p=1/6 mod p. The identity sum r_c^2=S_2, reduced modulo p^2 and divided
by p, gives

    2a sum c u_c=(a^2-1)/6 mod p,
    M_1(Theta_a)=sum c u_c=(a-a^(-1))/12.                 (6)

The index in Theta_a is sigma_c^(-1), whose DIRECT inverse is c; this is
why (6) is M_1 rather than F.

For p>=7 use the exact sum

    S_4=sum c^4=(p-1)p(2p-1)(3p^2-3p-1)/30.

Its denominator is prime to p, S_4/p is integral, and S_4/p=-1/30 mod p.
(The displayed polynomial sum is also obtained by telescoping consecutive
fifth powers and the lower power sums.) Expanding sum r_c^4=S_4 modulo
p^2 gives

    4a^3 sum c^3 u_c=(a^4-1) S_4/p mod p,
    M_3(Theta_a)=sum c^3 u_c=-(a-a^(-3))/120.              (7)

All omitted expansion terms contain p^2; the division by p occurred in an
integer identity. Thus no division by a nonunit modulo p occurs in (6)
or (7) at their written primes. Subtracting consecutive a gives

    m(t):=M_1(psi_t)=(t^2+t+1)/(12t(t+1)),                (8)
    M_3(psi_t)=-(1+t^(-3)-(t+1)^(-3))/120.                (9)

Formula(8) is valid for p>=5; formula(9) only for p>=7.

## 3. Proof of FS1, including the exceptional symmetry

If t^2+t+1 is nonzero, (8) and (1) imply that every stabilizer element h
has h^(-1)m(t)=m(t), hence h=1.

Now t^2+t+1=0. At p>=5 this implies t^3=1 and t!=1, so t has order3.
Thus 3 divides p-1 and p>=7; this also rules out an exception at p=5.
Since t+1=-t^2,

    p nu_c(t)=c+r_t(c)+r_(t^2)(c)-p.                     (10)

Replacing c by r_t(c) cyclically permutes the three residues on the right.
Hence nu_(r_t(c))(t)=nu_c(t), which is EXACT integer equality of coefficients.
The coefficient of sigma_c^(-1) in sigma_t psi_t is precisely
nu_(r_t(c))(t). Therefore sigma_t psi_t=psi_t, and its stabilizer contains
the order3 subgroup {1,t,t^2}.

In (9), t^(-3)=1 and (t+1)^(-3)=-1, so M_3(psi_t)=-3/120=-1/40 is nonzero.
If sigma_h psi_t=psi_t, formula(1) with r=3 gives h^3=1. There are at most
three roots of X^3-1 in F_p, and the displayed subgroup already has three
elements. This proves the exact stabilizer claim. Finally F transforms
under sigma_t by multiplication by t; invariance and t!=1 force
F(psi_t)=0. Formula(8) supplies M_1=0. This proves FS1.

No endpoint at p=3 is claimed in FS1 or the formulas with denominator12.
There is only t=1 in its allowed index range there, and psi_1=sigma_2 has
trivial stabilizer. Thus extending the exceptional-root criterion to p=3
would be FALSE: t^2+t+1=0 then does not imply a nontrivial order3 subgroup.

## 4. The action-on-zeta functional as a polynomial

For a>0 prime to p the product of the residues r_c is exactly (p-1)!.
Expanding their product modulo p^2 in Z_(p), whose denominators are units,
gives

    (p-1)!=a^(p-1)(p-1)![1-(p/a) sum u_c/c] mod p^2.

Cancel (p-1)!, insert a^(p-1)=1+p q_p(a), and divide the resulting
congruence in Z_(p) by p. This yields

    F(Theta_a)=sum u_c/c=a q_p(a)=(a^p-a)/p mod p.         (11)

This is a direct reconstruction of the source's Fermat-quotient identity;
no external Voronoi theorem is required. Consequently

    f(t):=F(psi_t)=((t+1)^p-t^p-1)/p mod p.               (12)

Let f(X) denote the integer polynomial ((X+1)^p-X^p-1)/p reduced modulo p.
It has degree p-1, f(0)=f(-1)=0, and for 1<=j<=5, when p>7,

    [X^(p-j)] f(X)=(-1)^(j-1)/j.                         (13)

Indeed binom(p,p-j)/p=binom(p-1,j-1)/j, and the latter binomial coefficient
reduces to (-1)^(j-1). These are polynomial coefficients over F_p, not
function coefficients obtained by prematurely identifying X^p with X.

## 5. A nonconstancy lemma and proof of FS2

Set Q(X)=X^2+X+1. For t in F_p\{0,-1} with Q(t)!=0 define

    u(t)=f(t)m(t)=f(t)Q(t)/(12t(t+1)).

**Claim.** For every prime p>7, u(t) is NOT constant on this domain.

Suppose it were a constant C. Then

    P(X)=Q(X)[Q(X)f(X)-12C X(X+1)]                       (14)

vanishes at every element of F_p. At a nonexceptional t this is the
supposition; at a root of Q the outer factor vanishes; at0,-1 use f=0
and X(X+1)=0. Polynomial division, or successively removing the p distinct
linear factors, implies X^p-X divides P in F_p[X]. Here deg P=p+3, so its
quotient has degree3. In a product (X^p-X)A(X) with deg A<=3 the coefficient
of X^(p-1) is0: the high part has degrees at least p and the low part at
most4, while p-1>4.

On the other hand, Q^2=X^4+2X^3+3X^2+2X+1, and (13) gives

    [X^(p-1)] P
      =1/5-2/4+3/3-2/2+1
      =7/10 !=0 in F_p.                                 (15)

The C-term has degree4 and does not contribute. The numerator and
denominator are nonzero because p>7. This contradiction proves the claim.
It also explains why p=7 cannot be silently included in this step.

Choose two indices s,t, represented in1,...,p-2, with Q(s),Q(t)!=0 and
u(s)!=u(t). Both m(s),m(t) are nonzero. If f(s)=0, take theta=2 psi_s;
if f(t)=0, take theta=2 psi_t. Each choice is positive, belongs to I_f,
has weight p-1 and nonzero inverse moment (p is odd). They cannot both
have f=0, since then their u values would coincide.

In the remaining case f(s)f(t)!=0, choose the nonzero DIRECT automorphism
indices a=f(t), b=-f(s) in F_p, and put

    theta=sigma_a psi_s+sigma_b psi_t.

This is a SUM with positive coefficients; b may be a negative residue but
sigma_b is still a coefficient permutation, not a negative scalar.
By (1),

    F(theta)=f(t)f(s)-f(s)f(t)=0,
    M_1(theta)=m(s)/f(t)-m(t)/f(s)
              =(u(s)-u(t))/(f(s)f(t)) !=0.               (16)

Membership in I, positivity and weight follow from Section1. Equation(5)
gives theta+j theta=2N in both cases. Nonzero M_1 proves freeness by(1).
This proves FS2 without any enumeration or assumption on Fermat quotients.
The source's Appendix5.2 also argues via the products of the two moments.
The shorter polynomial coefficient argument here is an explicit
reconstruction of this selection route, not an attribution of the route
to this project. We use neither its complete appendix proof nor an
extension of Lemma2.7 to small primes as an external premise.

## 6. Proof of FS3: a common-zero translate and an integer norm

Fix a theta from FS2. Its integer coefficients n_a satisfy

    0<=n_a<=2,  n_a+n_(-a)=2.                            (17)

They are not all1, since M_1(theta)!=0 whereas M_1(N)=0. There is therefore
at least one0 and at least one2. There must be at least TWO zero entries.
If the only zero were at v, the only2 would be at -v by(17), and all other
entries would be1. Then

    theta=N-sigma_v+sigma_(-v),
    F(theta)=-2v !=0,

contrary to theta in I_f. Choose distinct zero indices v,w, and set h=v/w.
They cannot be negatives of one another by(17), so h!=1,-1. Define

    gamma=theta+sigma_h theta.

At the DIRECT index v its coefficient is n_v+n_(h^(-1)v)=n_v+n_w=0.
As gamma+j gamma=4N, it has coefficient4 at -v, and all its coefficients
are between0 and4. It is positive and in I_f. Moreover

    M_1(gamma)=(1+h^(-1))M_1(theta)!=0,                   (18)

so gamma is free.

For a fixed integer k>=2 put

    A_l=(k-l)theta+lN,          l=0,...,k-1,
    B=gamma+(k-2)N.                                      (19)

All k+1 elements are positive, in I_f, and have weight k(p-1). Every A_l
is free: sigma_g A_l=A_l implies (k-l)(sigma_g theta-theta)=0 in the
torsion-free abelian group Z[G], so sigma_g theta=theta and g=1. B is free
because adding the invariant (k-2)N does not change gamma's stabilizer.
This argument includes k divisible by p: vanishing of a reduced moment
for some A_l does not invalidate its exact integer freeness.

The minimum coefficient of A_l is l and its maximum is2k-l. Thus the A_l
are pairwise nonconjugate. The minimum of B is k-2, so B could only
be conjugate to A_(k-2)=2theta+(k-2)N. They are separated by the integer
Euclidean norm ||sum n_a sigma_a||^2=sum n_a^2, preserved by coefficient
permutations. Since h!=1 and theta is free,

    ||theta+sigma_h theta||^2
       =4||theta||^2-||theta-sigma_h theta||^2
       <4||theta||^2=||2theta||^2.                        (20)

Both gamma and2theta have weight2(p-1). Adding the same constant vector
(k-2)N changes their squared norms by the same quantity, so the inequality
continues to separate B from A_(k-2). This proves pairwise nonconjugacy.

For completeness the Fourier map E(sum n_a sigma_a)=sum n_a zeta^a is
injective: its kernel polynomial has degree at most p-1 and constant0,
whereas the minimal polynomial Phi_p has degree p-1 and constant1. A
rational multiple of Phi_p with constant0 is zero. Equivariance follows
by multiplying direct indices. Thus free elements have p-1 distinct
Fourier conjugates and nonconjugate elements have disjoint Fourier sets.
This reconstructs the accepted MS2 interface and proves the last part
of FS3. It does NOT transfer Fourier injectivity to the reciprocal map.

## 7. Exact consequences, source boundaries and remaining obstruction

For p>7, FS2 supplies ONE positive element of the source's weight p-1
with a complete Fourier orbit. FS3 supplies THREE separate complete
Fourier orbits at weight2(p-1), and k+1 at weight k(p-1). These are
unconditional algebraic existence statements. They have no x,y parameter
and do not require Vandiver, class-number data, Wieferich assumptions,
or an actual solution. No assertion of two nonconjugate FREE elements
at the original weight p-1 has been proved here.
FS2 overlaps the later source Lemma2.7 and is attributed accordingly;
FS1 and FS3 are additional project deductions, with priority unestablished.

The original diagonal chapter's Lemma3 states two nonconjugate positive
elements of weight p-1; its use of those elements in Section4.3 has
additional cancellation and size requirements. This packet neither
imports nor refutes its counting argument. In particular it does not
declare every positive Fermat-module element free. FS1 exhibits an
entire exact family of nonfree ones; the norm element is another boundary.

Higher weight changes the Diophantine estimates. Conditionally, if a
solution-specific construction gives beta^p=(x-zeta)^eta and
eta+j eta=2kN with G_p(x)=y^p and y>0, taking complex absolute values would
give |beta|=y^k, not y. Thus the source's original truncation/cancellation
estimates cannot be reused unchanged for (19). Even though there are
k+1 disjoint full first-coefficient Fourier lists, their higher series
coefficients are not shown here to be a single Vandermonde system or to
have the required simultaneous rank. First-coefficient separation does
not prove arbitrary higher-jet interpolation, integral coefficients,
cancellation through EVERY conjugate, a nonzero delta, or a compatible
archimedean estimate. The later reciprocal normalization is distinct and
has a nonzero kernel; cross-list Fourier separation is not transferred.

The exact remaining targeted task is either (i) construct TWO nonconjugate
free positive elements at weight p-1 with all source selection conditions,
or (ii) prove a complete higher-weight interpolation/cancellation and
size argument for families such as(19). Neither is completed here. Even
completion of one selection task alone would not prove the second-case
class-number theorem or unrestricted Nagell–Ljunggren equation.

The integer k>=2 condition in FS3 cannot be dropped from this construction:
at k=1 its proposed extra element would be gamma-N, with coefficient-1
at the chosen common zero. This is an exact failure of that attempted
weight reduction, not a proof that a different pair at weight p-1 cannot
exist. At p=7 the coefficient obstruction(15) vanishes; FS2 makes no
existence or nonexistence assertion there.

A different attempted elementary route only recovers the already printed
source Lemma7, x=0 or-1 mod p => x=0 or-1 mod p^2 in the diagonal equation;
it is attributed rather than claimed new. No further p-adic exclusion,
height bound or local-to-integer inference is asserted. The complete
accepted C/PG/CF1/MS scopes, signed source exceptions and accepted narrow
strongFC objections remain unchanged. No preliminary proof, mathematical
program, CAS, scan, certificate rerun, or paid source supplies this packet.
