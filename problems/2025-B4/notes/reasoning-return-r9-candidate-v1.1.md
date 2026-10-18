# Actual short coefficients and two precise arithmetic obstructions, v1.1

2026-10-18 UTC. **Candidate proof - unverified.** Constructor C,
`/root/review_2017_coarsening_r1`. Requested inherited gpt-6.1-sol/max;
effective setting readback is unavailable. TWO OTHER initially blind
WHOLE audits and coordinator reconciliation are required. No annual
classification, new Diophantine exclusion, useful unconditional height
improvement, novelty or refutation of a source's final theorem is claimed.

This is the FULL versioned author repair after BOTH original-v1 WHOLE
initials froze. Original v1 and both initial packets remain immutable.
R9R1-01/R9R2-01 are addressed by separating the equality for every0<R<H
from the nonzero unit witnesses for1<=R<H. R9R2-N3 is made explicit:
the model's CHOSEN generator a_0^p is nonlinear; no statement excluding
all other linear generators of its ideal is proved. BOTH affected
reaudits and coordinator reconciliation remain required. The separate
later Runge packet is NOT a premise or an unreviewed repair input here.

## 0. Scope, authority and conclusions

The official open problem is 2025 B4(b), determining all integer solutions
of `1+X+...+X^n=Y^q`, `n,q>=2`. Only the prime diagonal sector

    G_p(X)=Y^p, p>=37 prime, X an integer, |X|>=2             (0)

is used below. Thus the official degree is p-1 and q=p. Both signs of X
remain; Y is positive. Accepted C/R6 gives p not dividing X-1 and the
exact e=0 characteristic ideal. No preliminary proof is reproduced.

The COMPLETE accepted R8 body is
`proofs/reviewed-reasoning-return-r8-v1.1.md`, 28730 bytes,
SHA256 `f00a2b2816f128df54060fd800cba83d726abf07303c1cc7c92688a61557ca15`.
Its actual phase system, canonical radical functions, normalized Jacobi
input, majorants and Wronskian lemma are imported in their stated scopes.
The exact matched-prime Jacobi construction in accepted R6, especially
its section5, is used also for a binary half-weight element. That extension
is derived in section3 below, rather than presumed from the original-weight
statement alone. C authored OLD R6 and FS and reviewed OLD R8 and other
inputs; this construction supplies no new independent audit of those inputs.

The proposed partial statements are these.

* **R9A:** at q_p>=32, the ACTUAL s=2 real phase system has a nonzero
  integral solution whose real integral-basis coordinates are -1,0,1.
  Its sum of archimedean coefficient sizes is at most 4q_p m^2.
* **R9B:** this gives the conditional evaluated-nonzero branch
  `|X| <= (16q_p m^2)^(p/(p+1)) <16q_p m^2`. A complete, much larger
  zero-branch bound is retained with the ACTUAL possible dense support.
* **R9C:** a homogeneous first-small-vector theorem does not ensure
  avoidance of a prescribed codimension-one subspace. An exact rational
  counterexample, including all the one-vector perturbations relevant to
  the attempted argument, and a valid cofactor replacement are given.
* **R9D:** two noncomplementary binary Fueter halves have overlapping
  actual characteristic-ideal support. At that overlap the quotient used
  in a proposed Kronecker step has a pole. Separate divisibilities cannot
  be multiplied. This is a conditional actual-ideal statement.
* **R9E:** for ANY hypothetical solution(0), an explicit positive element
  Theta in I_f, relative weight6, nonzero M_1 and coefficients<=6 has
  beta_Theta congruent1 modulo2. Its all-conjugate equality ideal at an
  even homogeneous coordinate is nonunit. This does not have original
  weight and cannot be transferred to R8's original-weight columns.
* **R9F:** an explicit cyclotomic model has the same original-weight,
  positivity, moment, ideal-disjointness and normalization data and a
  nontrivial equality ideal. Its CHOSEN p-th-power generator a_0^p is NOT
  a linear cyclotomic number. Whether its ideal has another linear
  generator up to a unit is not established. The actual linear
  Diophantine input is therefore not supplied by this model; it supplies
  no actual solution or ideal-level exclusion of such a generator.

The sources, their versions and exact reading limits are recorded
separately. A current 2025 revision has a different proof from its 2021
version; an objection to one must not silently be assigned to the other.

## 1. R9A: small coefficients for the actual two-order real system

Put K=Q(zeta), O=Z[zeta], lambda=1-zeta, j(zeta)=zeta^-1,
m=(p-1)/2, and use DIRECT sigma_a(zeta)=zeta^a. For a group-ring element
theta=sum n_a sigma_a set

    F(theta)=sum n_a a mod p, M_r(theta)=sum n_a a^(-r) mod p.

Let q=q_p=ceil((p-4)/30). Accepted R8 supplies q free, mutually
nonconjugate original-weight theta_i in I_f, with coefficients0/1/2,
theta_i+jtheta_i=2N and nonzero M_1. Choose arbitrary half-orbits as
there, giving q m columns theta_v and their actual Jacobi integers beta_v.
For the ACTUAL solution-specific phases tau_(a,v), R8's real equations
at k=0,1 are

    sum_v [ell_v tau_(a,v) J_(v,k)
                       +j(ell_v tau_(a,v) J_(v,k))]=0,
    a in G/{1,-1}, k=0,1,                              (1)

where ell_v=a_v+zeta b_v, a_v,b_v in Kplus,
J_(v,0)=1 and J_(v,1)=-sum n_(v,c) zeta^c. The tau are actual p-th
roots of unity and even in a; they are not free formal controllers.

### 1.1 An integral real basis and its multiplication

For h=1,...,m write t_h=zeta^h+zeta^-h, extend indices modulo sign
and p, and set t_0=2. Then

    1=-sum_(h=1)^m t_h, t_u t_h=t_(u+h)+t_(u-h).       (2)

The t_h form a Z-basis of O intersect Kplus. Indeed represent an element
by an integral coefficient vector at the p powers zeta^0,...,zeta^(p-1).
Its difference from its conjugate is a multiple of the all-one vector,
the only integral polynomial relation of degree<=p-1. Its coefficient
at0 is zero, so that multiple is zero. The vector is symmetric and the
element is an integer combination of1 and t_h. Equation(2) eliminates1.
If an integer combination of t_h is zero, its polynomial has zero constant
coefficient and is a rational multiple of Phi_p; this multiple must be0.
Thus they are also independent. This argument uses O=Z[zeta], an accepted
classical input, and does not divide by2 in an integral lattice.

Expand every a_v,b_v in this basis. There are

    U=2q m^2 integer unknowns and at most V=2m^2 equations.       (3)

Every entry of the expanded integer matrix has absolute value<=8.
For k=0 its unexpanded entry is t_d for a shifted root of unity (or
t_0=2). Multiplication by t_h in(2), followed by t_0=-2 sum t_r,
has coefficients bounded by2.

For k=1 a column entry is -sum_c n_c t_(c+d), possibly with another
shift d from the factor zeta in ell_v. After multiplication by t_h this is

    -sum_c n_c [t_(c+d+h)+t_(c+d-h)].                 (4)

At any nonzero folded index, at most four n_c contribute, each between0
and2; the resulting negative coefficient lies in[-8,0]. The possible
t_0 terms have total coefficient -(n_(-d-h)+n_(-d+h)), in[-4,0].
Eliminating t_0 adds the SAME number between0 and8 at every basis index.
The combined coefficient therefore lies in[-8,8]. Indices which coincide
or have n_0=0 only decrease the bound. No estimate grows with a phase
exponent, and no archimedean bound is mistaken for an integral-coordinate
bound.

### 1.2 Pigeonhole and coefficient height

Map the 2^U binary vectors by this integer matrix. Every image coordinate
lies in[-8U,8U], so there are at most(16U+1)^V images. If

    2^q>16U+1,                                       (5)

then U=q V (with V taken as its upper bound2m^2) gives more binary vectors
than images. The difference of two with the same image is a nonzero
{-1,0,1} vector satisfying(1).

Condition(5) holds whenever q>=32. From the definition of q,
p<=30q+4, so m<=16q for q>=2, and U<=512q^3. At q=32,
2^q=2^32>2^28+1=8192q^3+1. Inductively, (1+1/q)^3<2 at q>=32,
so doubling preserves 2^q>8192q^3+1. Hence(5). In the prime domain,
p>=937 is a sufficient, not asserted optimal, threshold.

For this vector each conjugate of each a_v,b_v has modulus<=2m,
because |sigma(t_h)|<=2. Thus every ell_v is integral, not all vanish
since1,zeta are independent over Kplus, and

    sum_v |sigma_a ell_v| <= A:=4q m^2, EVERY a.      (6)

The vector depends on the actual signature. This is not one vector that
works for all signatures, and it has not been made to avoid an evaluated
equality subspace. A vector may use all q m columns.

## 2. R9B: both evaluation branches, with the correct support cost

Let delta=sum ell_v beta_v+j(sum ell_v beta_v), an actual real algebraic
integer. R8's all-embedding identities and coefficient majorant apply
unchanged to(1),(6). At every real embedding,

    |sigma_a delta|<=4A |X|^(-1-1/p).                (7)

If delta is nonzero, its real-field norm is a nonzero integer. The product
of(7) therefore gives

    |X| <= (4A)^(p/(p+1))=(16q m^2)^(p/(p+1)).       (8)

This is conditional on delta!=0. It does not exclude the alternative.

For completeness use the nonzero formal series in R8 section4.1 with
these same ell_v. The canonical vectors theta_v and jtheta_v are distinct
modulo p, so radical monodromy independence still proves it is nonzero.
Here the number of active functions is at most

    n_* =2q m, T_*=(p-2)n_*(n_*-1)/2+n_*-1.          (9)

R8's GENERAL nfun-function Wronskian argument gives a first nonzero
coefficient h_t at 2<=t<=T_*. Its integral witness p^t t!h_t has all
conjugates bounded by2A p^t t!. If delta=0, the same coefficient-norm
and analytic-tail argument gives

    |X| <= 2[2A p^T_* T_*!]^m.                      (10)

In particular one must NOT reuse R8's smaller support bound
2(R_2+1) for its sparse cofactor vector. The pigeonhole vector is generally
dense; T_* may be of order p^5. The polynomial coefficient height in(6)
does not by itself improve the zero branch or the known published height
theorems. The missing useful inference is an actual evaluated-nonzero
choice, or a much sharper actual zero-branch argument.

## 3. Actual binary half-weight Jacobi integers

This section fixes the arithmetic hypotheses in the remaining statements.
Under(0), accepted R6 section5 proves

    (X-zeta)=A^p, A integral nonunit, Norm(A)=Y>1,     (11)

and its p-1 conjugate ideals are pairwise coprime. All primes dividing A
are over rational primes ell=1 mod p. Also Y is odd: G_p(X) is odd for
both parities of X.

A binary Fueter half psi is a translate of a classical Jacobi exponent
psi(1,t), with coefficients0/1 and psi+jpsi=N. For every prime L of A,
use the matched-character Jacobi sum from accepted R6's attributed
classical formula. Its ideal is L^psi, every archimedean modulus is
sqrt(ell), and its minus normalization is1 modulo lambda^2. Multiply
these sums to the actual valuations of A. The result b_psi is integral
and satisfies

    (b_psi)=A^psi, b_psi*j(b_psi)=Y,
    b_psi=1 mod lambda^2.                           (12)

The second equality follows from every complex modulus sqrt(Y), or from
the Jacobi Gauss-sum identity, with its positive real sign. Any two
generators with THESE ideal and modulus properties have a quotient that
is an integral unit, all of whose conjugates have modulus1. Kronecker
makes the quotient +/-zeta^h; the common lambda^2 normalization makes
it1. Thus the construction is unique, G-equivariant and multiplicative
on its generated group. This use of Kronecker is valid because the
quotient has the SAME ideal in numerator and denominator.

Write beta_theta for the corresponding product when theta is a sum of
such exponents. Positivity ensures its final ideal is integral. In
particular beta_(sigma_a psi)=sigma_a b_psi and beta_N=Y. For any
positive theta in this generated group with theta+jtheta=2kN and F=0,
the same normalization proof as accepted R6 gives

    beta_theta^p=(X-zeta)^theta.                    (13)

Indeed the quotient has ideal1 and all conjugate moduli1. Modulo
lambda^2 the latter power is (X-1)^(k(p-1)) times a linear term killed
by F=0, hence is1; beta_theta^p is1 too. This removes its root of unity.
We only need k=1,3. No generalized e=1 theorem is being imported.

## 4. R9C: small nonzero is not small outside a subspace

Let d>=17 and H>1 be integers, and let R be real with0<R<H. In Q^d with standard
integer basis e_i define

    W''=span{e_1+H e_2,e_3,...,e_15},
    v=e_1, W'=W''+Qv,
    S'=(W'')^perp, S=(W')^perp.                     (14)

These row spaces have ranks14,15. Their integer kernels satisfy

    S': w_1+H w_2=0, w_3=...=w_15=0,
    S:  w_1=...=w_15=0.                            (15)

If an integer w in S' has sup norm<=R, then |w_1|<H forces w_2=0
and w_1=0. Consequently

    S' intersect Z^d intersect[-R,R]^d
          =S intersect Z^d intersect[-R,R]^d.       (16)

Equality(16) holds over that ENTIRE range0<R<H, including0<R<1. In the
latter range the integer cube contains only0, so no nonzero-point
assertion is intended. For example H=2,d=17,R=1/2 gives precisely these
two zero-only sets; the original-v1 sentence asserting e_16 in both sets
at every allowed R was false.

Now assume additionally1<=R<H. Both sides of(16) contain e_16 because
its sup norm is1. There are therefore very short NONZERO homogeneous
solutions and NONE avoids S at that height. The other basis rows
e_16,...,e_d complete the rows of W' to a basis. For any such j let

    W^(j)=W''+Q(v+e_j), S^(j)=(W^(j))^perp.

For every0<R<H a short integer point of S^(j) also has w_j=0: the
W'' equations first give w_1=w_2=0, and the added row gives w_j=0.
For1<=R<H it has a unit point e_k for any k>=16 different from j;
d>=17 guarantees such k. Thus, in this latter radius range, all these
perturbed homogeneous systems also have NONZERO unit solutions; they
do not imply a short point of S' outside S. At R<1 those kernels also
have only the zero integer point in the box, which gives no nonzero
counterexample. Choosing R=sqrt(H) is valid since1<sqrt(H)<H, and
shows the precise large-height failure. The strict upper bound is also
necessary: at R=H, the vector(-H,1,0,...,0) lies in S' outside S.
Even a valid small first-successive-minimum bound for every perturbed
kernel cannot identify an escaping vector.

This is a rational linear-algebra counterexample, not a Jacobi system
asserted arithmetically realized. Primary Fukshansky's theorem and its
sharpness discussion distinguish avoidance from ordinary Siegel's lemma.
No external small-vector theorem is required to verify(14)--(16).

A safe replacement is elementary. If A_0 is an integral r by d matrix
of rank r, |entries|<=B with B>=1, and a row b is NOT in its rational
row space, choose r+1 columns on which the augmented r+1 determinant
is nonzero. The signed r-minors of A_0 on those columns give z in Z^d
with A_0 z=0, bz!=0 and

    ||z||_infinity <=r! B^r.                       (17)

For r=0 use the empty determinant1 at a nonzero coordinate of b. The
determinant expansion proves both equations and the bound. This is an
avoidance bound, but has the potentially large full-minor cost. Replacing
it by a first-minimum exponent requires a real additional hypothesis.

## 5. R9D: the exact overlap pole in original weight

Let psi_1,psi_2 be two binary Fueter halves and S_i their supports in G.
Each support has m elements. They are disjoint if and only if their
sum is N. Therefore whenever theta=psi_1+psi_2!=N, their supports overlap.
This includes the accepted R8 selections: their nonzero M_1 excludes N.

Under(11),(12), put b_i=beta_(psi_i). Choose an overlapping index a.
Every conjugate of A is nonunit, so choose a prime Q in the conjugate
at that index and put e=v_Q(sigma_a A)>0. Pairwise coprimality gives

    v_Q(b_1)=v_Q(b_2)=v_Q(Y)=e.                     (18)

Now suppose D is a nonzero rational integer coprime to Y and

    b_1 b_2-Y=D chi, chi in O.                     (19)

The two terms on the left have valuations2e and e, so their difference
has valuation EXACTLY e. Thus

    v_Q(chi)=e, v_Q(chi/(b_1 b_2))=-e.              (20)

In fact each b_i divides Y, since Y/b_i=jb_i is integral. It divides
b_1 b_2 too, and is coprime to D; therefore b_i|chi separately holds
globally. Those TWO divisibilities do NOT imply b_1 b_2|chi. The quotient
in(20) is not integral. The
identity `1-D chi/(b_1 b_2)=Y/(b_1 b_2)` has all complex moduli1,
but this rational-norm-one quantity has a pole and is not an integral
unit. Kronecker's integral-unit conclusion is unavailable.

The only way to make the two half ideals coprime in this setting is
psi_1+psi_2=N, in which case their product is Y and M_1=0. That repair
removes the nontrivial original-weight element. This is a valuation
obstruction under ACTUAL characteristic-ideal hypotheses; it is not a
counterexample to existence or nonexistence of(0).

## 6. R9E: the actual finite-2 kernel at relative weight6

Choose the specific binary half

    psi=sum_(c=m+1)^(p-1) sigma_(c^(-1)).

This is the classical psi(1,1); psi+jpsi=N. Direct calculation gives

    M_1(psi)=sum_(c=m+1)^(p-1)c=1/8 mod p !=0.       (21)

The last equality uses total sum0 modulo p and m(m+1)=-1/4 modulo p.
Let b=beta_psi from(12), and define

    Theta=2 sigma_2 psi+4 jpsi.                     (22)

It is positive and belongs to I. Its canonical integer coefficients
belong to{0,2,4,6}, all <p. The two transformations of the moments are
F(sigma_a psi)=aF(psi) and M_1(sigma_a psi)=a^(-1)M_1(psi). Hence

    Theta+jTheta=6N, F(Theta)=0,
    M_1(Theta)=-3M_1(psi)!=0.                       (23)

It has relative weight6, ordinary augmentation3(p-1), and is in the
source's J_3 (the half-relative-weight index is3). Since p>=37, 3<=m.
Nonzero M_1 excludes a norm-element reduction modulo(p,N); it also
shows the G-orbit is free. No ambiguity from a p-multiple of coefficients
or a norm element explains the following equality.

For EVERY u in Z[zeta],

    sigma_2 u=u^2 mod2O,                            (24)

by the characteristic2 binomial identity. This does not require 2 to
split completely or any assertion about a complex phase. Multiplicativity
and the normalization in section3 give

    beta_Theta=(sigma_2 b)^2 (jb)^4
              =b^4(jb)^4=Y^4=1 mod2O.              (25)

In particular sigma(beta_Theta)=1 modulo2O for EVERY sigma in G.

Choose w=X if X is even, and w=X-1 otherwise, and remove its p-part
to obtain w'. Then w' is nonzero and even. Define the actual ideals

    D_sigma=(w', beta_Theta-sigma beta_Theta),
    D_Theta=intersection_(sigma in G) D_sigma.       (26)

Every generator of each D_sigma lies in2O. Thus

    0!=D_Theta subseteq(2), so (2) divides D_Theta, D_Theta!=O.  (27)

The nonzero assertion follows since all D_sigma contain(w'). The ideal
inclusion direction in(27) is important. This uses actual Jacobi integers
of any hypothetical(0), not a freely assigned residue controller.

To compare with the homogeneous source equation, positive X uses
(x,y,z)=(X,-1,Y), while X=-A uses(A,1,Y). The relevant even coordinate
is among{x,y,x+y}. Their characteristic ideals are a G-conjugate of(11),
which does not alter(24)--(27). In particular the construction confronts
an all-positive-element equality-ideal assertion at weight6. It does not
establish an actual solution which refutes a source nonexistence theorem;
under no solutions every such conditional assertion would be vacuous.

### 6.1 Why this is not the desired original-weight bridge

To change the complement6N to the original complement2N by adding a
multiple of N, the ONLY possible change is Theta-2N. But sigma_2 psi
and psi are different binary supports of equal size: their M_1 differ
by the nontrivial factor1/2. There is therefore an index at which
psi=1 and sigma_2 psi=0. At that index jpsi=0, so Theta=0 and
Theta-2N has coefficient-2. It is not positive. Neither a G-translate
nor a mere norm shift repairs this positivity failure at original weight.

Consequently(25) cannot be inserted as an original-weight column or as
an assertion about R8's actual infinity signature. That interface remains
unproved. For primes2 and infinity, Frobenius congruence and a complex
analytic branch are different structures.

## 7. R9F: a model retaining the linear-generator obligation

This model is unconditional cyclotomic algebra and NOT a solution(0).
Fix p>=37, c=2p^2, a_0=1+c zeta, A_0=(a_0) and

    Z=Norm(a_0)=(c^p+1)/(c+1)>1.                    (28)

Z is odd and a_0=1 modulo lambda^2. The conjugate ideals A_0 are
pairwise coprime. A common prime of two conjugates would divide
c(zeta^a-zeta^b). A prime over a divisor of c cannot divide either
1+c zeta^a, and the remaining difference has only lambda support;
lambda does not divide a_0. This proves the assertion without factoring Z.
Moreover every rational prime ell below a prime of A_0 splits completely:
in that residue field zeta=-1/c lies in the prime field, has order p,
and ell!=p. Hence ell=1 mod p and the residue field is F_ell. The
matched-prime Jacobi input of section3 applies to A_0 as well.

Take ANY accepted original-weight R8 element theta=psi_1+psi_2 with
F=0,M_1!=0, and set b_i=a_0^psi_i. Then these are actual integral
cyclotomic numbers, normalized1 modulo lambda^2, with ideals A_0^psi_i
and b_i jb_i=Z. The half-support identity gives every conjugate modulus
sqrt(Z), so they have exactly the Jacobi normalization properties used
above. Their product beta_theta has original weight, coefficients0/1/2,
F=0 and M_1!=0. Because a_0=1 modulo2,

    beta_theta=1 mod2O, sigma beta_theta=1 mod2O.    (29)

Using w'=2 in(26) gives D_theta=(2) EXACTLY. Also chi=(b_1 b_2-Z)/2
is integral, and the overlap argument(18)--(20) gives a genuine pole in
chi/(b_1 b_2). Thus neither original weight nor nonzero M_1 alone repairs
the product-divisibility step at the level of these ideal data.

The missing actual Diophantine condition is substantial. Here the
CHOSEN generator a_0^p of A_0^p is not a linear y+x zeta. Indeed its coefficients
at zeta^(p-2) and zeta^(p-1) of(1+c zeta)^p are
`p(p-1)c^(p-2)/2` and `p c^(p-1)`, which differ for c=2p^2.
If the polynomial represented a linear number, all coefficients at
degrees2,...,p-1 would be the same multiple of Phi_p; these two would
be equal. Hence this CHOSEN number is not linear.

This coefficient calculation does NOT prove that the IDEAL A_0^p has
no other linear generator: another generator differs by a unit, whose
effect is not controlled by this calculation. A diagnostic in the SAME
field is zeta^2(2+zeta). It is nonlinear in1,zeta for p>=37: its degree3
polynomial representative cannot differ from a linear polynomial by a
nonzero multiple of Phi_p, whose degree is p-1>3. Nevertheless it
generates the same ideal as the linear number2+zeta, because zeta^2 is
a unit. This diagnostic makes no assertion about another generator of
the specific A_0^p. Such an ideal-level linear-generator exclusion is
NOT proved or needed for the model's narrower ideal/normalization and
chosen-number statements.

No actual X, homogeneous coordinates or suitable linear characteristic
p-th power has been supplied. Whether a different unit multiple could
meet that further Diophantine condition remains unchecked. Thus no
solution of the original equation, and no impossibility theorem about
all linear generators of this ideal, has been constructed. The source
theorem is not declared false from this model.

## 8. Source boundary and the remaining useful bridge

The [2005 primary avoidance theorem of Fukshansky](https://arxiv.org/pdf/math/0409375v3) explicitly treats
escape from proper subspaces; it supports the distinction made in R9C.
Our counterexample and cofactor substitute are fully proved above and
do not depend on importing its quantitative theorem.

[Mihailescu's 2021 arXiv v1](https://arxiv.org/pdf/2108.08572v1) uses an adelic/carry and small-vector route.
The [CURRENT arXiv v4](https://arxiv.org/pdf/2108.08572v4), by Bartolome and Mihailescu, revised2025, instead
uses ideals formed from differences of Jacobi conjugates, a unit step,
and splitting at2. We do not conflate these versions. In v4 Lemma5 the
inference from two separate divisibilities to their product is precisely
the step challenged by section5; a repair requires more than those
divisibilities. Section6 gives a necessary higher-weight equality under
the actual hypotheses. It must be reconciled by any proof claiming those
equality ideals are units. Neither observation alone refutes the final
nonexistence theorem or supplies its proof.

What is achieved here is a small-height ACTUAL two-order cancellation,
and exact obstructions preventing two attractive shortcuts from closing
its evaluated-zero branch. A positive bridge still requires new use of
the linear characteristic p-th power, an actual low-height escaping
coefficient vector, or a useful bound for the first actual zero-branch
coefficient. Formal monodromy, many orbits, finite-2 Frobenius, a generic
Siegel bound and Kronecker without integrality do not supply that step.
Published stronger diagonal bounds and class-number conditions remain
visible in the accepted source map and are not claimed improved here.
