# Reciprocal jets, the actual phase system, and a weak height bridge

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
`/root/review_2017_coarsening_r1`; requested gpt-6.1-sol/max, effective
setting readback unavailable. TWO OTHER initially blind whole audits
are required. No novelty, source-theorem refutation, new Diophantine
exclusion or full annual solution is claimed.

## 0. Domain, inputs and precise proposed conclusions

The official open target is B4(b), all integer solutions of

    G_(n+1)(x)=1+x+...+x^n=y^q,  n,q>=2.

Here the arithmetic application is ONLY the prime diagonal sector

    G_p(x)=y^p,  p>=37 prime,  x,y integers, |x|>=2.       (0)

Thus the official degree is n=p-1 and q=p. Negative x is retained;
y is positive in(0), since p is odd and G_p(x)>0. Boundary sectors,
other term counts and exponents are not reconsidered. No preliminary
part(a) proof is reproduced.

Use the accepted MS, FS, OW, UW and RK bodies with their exact scopes.
In particular UW supplies TWO positive integer elements theta_i in I_f,
with weight p-1, complement2N, coefficients0/1/2, nonzero M_1 and
different G-orbits. MS/UW supply faithful Fourier evaluation. RK
supplies separation for the unnormalized reciprocal map on a FIXED
complement. The constructor authored older FS, and reviewed MS/OW/UW/RK;
this submission is not an independent re-audit of any such background.
All older bytes are preserved. The new candidate has the following parts.

* **J1:** an integral normalized recurrence for EVERY reciprocal jet,
  giving b_k(theta)=M_1(theta)^k modulo1-zeta for every k>=0.
* **J2:** suitable complementary half-orbits of the two UW elements
  give an invertible joint matrix of the first p-1 reciprocal jets.
  This is an ordinary jet matrix, not the phase matrix below.
* **P1:** an exact reconstruction of the pulled-back semilinear system
  for cancellation at EVERY conjugate, including the weaker REAL system.
  Formal zero phase gives a precise obstruction to a blanket full-rank
  two-jet assertion. No such signature is asserted to occur for a solution.
* **A1:** from the classical Jacobi ideal formula, a full derivation of
  the required normalized Jacobi lifts for(0) and the selected theta_i.
* **H1:** for the ACTUAL solution-specific phases there is an integral
  combination cancelling constants at every conjugate and having a
  nonzero first coefficient at one embedding. This uses the existing
  bouquet/Vandermonde mechanism in a deliberately weaker form.
* **H2:** that weaker system yields the explicit bound

    |x| <= (4 p^2 m^m)^p,  m=(p-1)/2,                 (1)

  in(0), conditional only on the explicitly attributed classical Jacobi
  ideal input and accepted UW selection. It handles both delta=0 and
  delta!=0. The bound is MUCH weaker than published upper bounds; it
  is no new arithmetic exclusion and does not repair the stronger
  all-but-one higher-order cancellation claim.

The formal jet recurrence, exact phase reconstruction, attributed lift,
and weak height bridge are separated to prevent a false implication
between different matrices and different expansion centers.

## 1. Conventions and classical arithmetic input

Fix an odd prime p, zeta=exp(2*pi*i/p), K=Q(zeta), O=Z[zeta],
lambda=1-zeta, G=F_p^*, sigma_a(zeta)=zeta^a, j=sigma_(-1), and
N=sum_(a in G)sigma_a. Subscripts on sigma are DIRECT. For
theta=sum_a n_a sigma_a put

    wt(theta)=sum_a n_a,
    F(theta)=sum_a n_a a mod p,
    M_r(theta)=sum_a n_a a^(-r) mod p,
    E(theta)=sum_a n_a zeta^a,
    L(theta)=sum_a n_a/(1-zeta^a).

The Stickelberger/Fermat modules are

    vartheta=(1/p)sum_(c=1)^(p-1)c sigma_c^(-1),
    I=Z[G] intersect vartheta Z[G],  I_f=I intersect ker F.

The arithmetic input used here is the CLASSICAL Jacobi ideal formula,
as stated in Mihailescu's original diagonal chapter, §2.2 equations
(10)--(11), printed p5. For a prime ell=1 mod p, a suitable order-p
character chi on F_ell, and nonzero a,b,a+b modulo p, the minus-normalized
Jacobi sum

    J(chi^a,chi^b)=-sum_z chi^a(z)chi^b(1-z)

has ideal L_ell^psi(a,b), where L_ell is a corresponding prime above ell
and

    psi(a,b)=sum_(c=1)^(p-1)
       [floor(c(a+b)/p)-floor(ca/p)-floor(cb/p)]sigma_c^(-1).

The matched character can be chosen for any prime above ell by Galois
conjugation. All complex absolute values of this J equal sqrt(ell),
by the usual Gauss-sum identity (all three characters are nontrivial).
This ideal theorem is ATTRIBUTED, not proved here from Gauss sums.
We use ordinary cyclotomic arithmetic O_K=Z[zeta], the unique prime
lambda over p, its ramification degree p-1, and the roots of unity
in K being exactly +/-zeta^h. These are classical background, also
used in the source's §2.2. Kronecker's unit argument is recalled in §5.

The original complete §4.3 and later Bartolome--Mihailescu complete
Appendices5.1--5.2 were read. The later Lemma5.1 supplies the EXISTING
proper-row-space/diagonal-growth idea rederived in §6. Its existence
conclusion alone does not identify a prescribed elementary target
vector in the full system. We do NOT import the chapter's Theorems3/4,
the later binary-Thue theorem, or a claimed source upper-bound repair.

## 2. J1: an all-order reciprocal recurrence

For ANY theta in Z[G], allowing negative coefficients, define the formal
power series with constant1

    R_theta(D)=prod_a(1+D/(1-zeta^a))^(n_a/p)
              =sum_(k>=0)c_k(theta)D^k in K[[D]],
    b_k(theta)=p^k k! lambda^k c_k(theta),
    U_l(theta)=sum_a n_a (lambda/(1-zeta^a))^l, l>=1.   (2)

The quotient lambda/(1-zeta^a) is a cyclotomic unit: its inverse is
1+zeta+...+zeta^(a-1), an algebraic integer of norm1 for1<=a<p.
It reduces to a^(-1) modulo lambda. Thus U_l belongs to O and

    U_l(theta)=M_l(theta) mod lambda.                  (3)

Logarithmic differentiation gives

    R_theta'(D)=R_theta(D)*(1/p)
                 sum_a n_a/(1-zeta^a+D).

Compare coefficients and multiply by p^(k+1)k!lambda^(k+1). The result is

    b_0=1,
    b_(k+1)=sum_(l=0)^k (-1)^l [k!/(k-l)!]
                 p^l U_(l+1) b_(k-l),  k>=0.         (4)

Every factor k!/(k-l)! is an INTEGER; no division by k! modulo p is
made. Induction proves b_k in O for EVERY k>=0. Reducing(4) modulo
lambda kills every l>=1 term, since p is in(lambda). Therefore

    b_k(theta)=M_1(theta)^k mod lambda, EVERY k>=0.     (5)

For k0 this is1, even when M_1=0. There is no k<p assumption in(4)--(5).
This is a direct derivation; it does not extend the published restricted
jet theorem merely by dropping its N restriction. It proves b_k integral,
not an unstated stronger divisibility of b_k/k! at all orders.

## 3. J2: a joint p-1 reciprocal-jet matrix

Let theta_1,theta_2 be the accepted UW pair and u_i=M_1(theta_i)!=0.
Choose A subset F_p^* containing exactly ONE of a,-a from each pair.
Define

    H_1={c in G:u_1/c in A},
    H_2={c in G:u_2/c in -A}.

Each H_i has m elements and exactly one of c,-c. The selected columns
are theta_(i,c)=sigma_c theta_i for c in H_i. Their inverse first
moments u_i/c run through ALL p-1 nonzero residues without repetition.
Writing h=p-1, the h-by-h matrix

    V=(b_k(theta_(i,c)))_(0<=k<h; selected(i,c))        (6)

reduces modulo lambda to a Vandermonde matrix on these distinct
residues. Its determinant is nonzero modulo lambda and hence in K.
The unnormalized coefficient matrix(c_k(theta_(i,c))) has nonzero
determinant too: it differs only by nonzero row multipliers.

The p-1 endpoint is thus PROVED from(4), and is not read into the later
paper's Lemma2.10, which states0<N<p-1. The construction uses specially
chosen halves. It does not claim EVERY arbitrary pair of half-orbits
has disjoint reduced first moments. Indeed both complete arrays reduce
to the same nonzero residue set. RK gives exact reciprocal separation
of the two full arrays, but exact distinctness by itself is not the
mod-lambda Vandermonde hypothesis used in(6).

A SINGLE complete free orbit with M_1!=0 also gives a p-1 matrix by
the same proof. Two distinct orbits are needed to match the source's
two-list, one-per-conjugate-pair interface, not for a novelty claim
about ordinary Vandermonde interpolation. Most importantly, (6) is
NOT the matrix of simultaneous constant/linear cancellation at all
embeddings, and its expansion center is the later reciprocal D chart.

## 4. P1: the exact all-conjugate phase equations

We first give a general calculation; its actual arithmetic realization
at infinity is established in §§5--6. Suppose columns beta_v in K
have formal expansions at all embeddings of the form

    sigma_a(beta_v)=B zeta^(-kappa_(a,v))
                       sum_(k>=0)sigma_a(d_(v,k))T^k,  (7)

where B is the SAME positive real scalar for all a,v, T is real,
d_(v,0)=1, and kappa_(a,v) is a residue modulo p. No operation
sigma_a(B) is asserted: (7) is a separate equality at each embedding,
so B need not belong to K. Define

    tau_(a,v)=zeta^(-kappa_(a,v)/a),
    A_a=(tau_(a,v))_v.

For fixed coefficients ell_v in K and Delta=sum_v ell_v beta_v,
put

    Q_(a,k)=sum_v ell_v tau_(a,v)d_(v,k).              (8)

The kth coefficient of sigma_a(Delta)/B is EXACTLY sigma_a(Q_(a,k)).
Consequently complex cancellation through order s-1 at EVERY conjugate
is equivalent to Q_(a,k)=0 for ALL a and0<=k<s. The fixed-coefficient
linear equations have rows

    A_a diag(d_(v,k)),  for every a,k.                 (9)

One original equation does not transport with ell_v held fixed.
Applying sigma_a transports the coefficients as sigma_a(ell_v), and
the actual phase kappa_(a,v) must also be used. Pullback by sigma_a^(-1)
explains the division by a in tau. Omitting it changes the system.

For the REAL integer delta=Delta+jDelta, the exact, generally weaker,
condition is instead

    Q_(a,k)+j Q_(a,k)=0.                               (10)

Indeed j commutes with sigma_a and T,B are real. This is a linear
system over K^+ after realification, not in general a K-linear system
in the ell_v. The stronger complex equations(8)=0 suffice for(10)
and are the ones we actually impose in §6.

### A formal obstruction, with an explicit admissibility firewall

Take any N>2 distinct first coefficients d_(v,1), and set every kappa
to0. Then every row A_a is the all-ones vector. The complex constant
plus first-jet matrix from(9) has rank exactly2, regardless of a full
ordinary N-jet Vandermonde matrix. Thus distinct first coefficients,
or ordinary jet regularity, do NOT imply this doubled phase matrix
is invertible or has every prescribed elementary vector in its image.
For an explicit formal model, take f_v(T)=exp(d_v T) for distinct
d_v in K and use coefficientwise Galois conjugation at other embeddings.
Its first N coefficient rows are a Vandermonde divided by k!, while
the all-conjugate constant/linear matrix above still has rank2.

In this covariant zero-phase case, the kth coefficient of a fixed
real combination is sigma_a(z_k) for a SINGLE z_k in K^+. If z_k is
nonzero, every embedding is nonzero. It therefore cannot be supported
at exactly one of m>1 real embeddings. Setting all phases to0 satisfies
the necessary oddness relation kappa_i(-s)=-kappa_i(s) below. This is
an exact FORMAL counterexample to an inference from those stated data.
It is NOT an actual solution to(0), NOT a constructed Jacobi signature,
and NOT a refutation of the original/later theorems. Additional
solution-specific constraints could rule it out; no such converse
realizability theorem is assumed here.

## 5. A1: actual Jacobi lifts in the signed prime-diagonal sector

Assume(0). Accepted signed C2 gives p not dividing x-1: otherwise
v_p(G_p(x))=1, impossible for y^p. We invoke that accepted valuation
result without reproducing its preliminary context. Put alpha=x-zeta.
Then lambda does not divide alpha. Any common prime of two distinct
conjugates x-zeta^a,x-zeta^b would divide zeta^a-zeta^b, whose prime
support is only lambda. Thus those conjugate ideals are pairwise coprime.

If a prime L over a rational prime ell divides alpha, then ell!=p and
the residue of zeta equals the ordinary integer x. Since O=Z[zeta],
the residue field is F_ell. Moreover zeta has order p there: its order
divides p and cannot be1 unless ell divides Phi_p(1)=p. Hence ell=1
mod p, and ell splits completely in K. Exactly one prime over ell
divides alpha, by pairwise coprimality. From Norm(alpha)=G_p(x)=y^p,
its valuation is a multiple of p. Consequently

    (alpha)=mathfrakA^p,  mathfrakA integral,
    Norm(mathfrakA)=y,                                 (11)

and all rational prime divisors of Norm(mathfrakA) are1 mod p.

We next derive the generation needed to apply the classical Jacobi
formula to arbitrary theta in I, rather than assume a stated basis
cardinality. For v=sum_a t_a sigma_a in Z[G], the coefficient of
vartheta v at sigma_c^(-1) is p^(-1)sum_a t_a r_a(c), where r_a(c)
represents ac modulo p in1,...,p-1. Hence

    vartheta v in Z[G] iff sum_a t_a a=0 mod p.        (12)

The integer vectors satisfying(12) are generated by p sigma_1 and
sigma_a-a sigma_1 for2<=a<=p-1: subtract those latter multiples and
the remaining coefficient at sigma_1 is divisible by p. Therefore I
is generated over Z by Theta_p=p vartheta and
Theta_a=(a-sigma_a)vartheta,2<=a<=p-1. With Theta_1=0,

    psi_t=Theta_(t+1)-Theta_t, 1<=t<=p-2,
    Theta_a=sum_(t=1)^(a-1)psi_t,
    Theta_p=Theta_(p-1)+N,
    N=psi_1+j psi_1.                                  (13)

The penultimate identity uses(1+j)vartheta=N. Thus I is generated
by the psi_t and j psi_1, all of which have weight m and are translates
of the Jacobi exponents psi(1,t). Negative INTEGER coefficients in
this generating expression are allowed. No cancellation of vartheta
on the entire group ring or odd-character nonvanishing is used.

For a fixed prime L over ell=1 mod p and any theta in I of weight p-1,
write theta as an integer combination of these weight-m generators.
The coefficient sum in this expression is2, by augmentation. Multiply
the associated minus-normalized Jacobi sums with those integer powers,
allowing a fraction at this intermediate step. The resulting gamma_L
has ideal L^theta and every complex absolute value ell.

For completeness the normalization J=1 mod lambda^2 follows directly
from the character sum. If chi(z)=zeta^(t(z)) on F_ell^*, expand
zeta^h=1-h lambda mod lambda^2. Over z!=0,1, each residue t in F_p
occurs(ell-1)/p times in the unrestricted nonzero sum; removing z=1
removes only t=0. The sum of these t's is0 modulo p, as p is odd.
The same holds after replacing z by1-z. The constant of J is
-(ell-2)=1-(ell-1), congruent1 mod lambda^2 because p divides ell-1
and p has lambda-valuation p-1>=2. The linear coefficient is divisible
by p and hence contributes0 modulo lambda^2. Thus J=1 mod lambda^2.
This remains true for negative powers in the local ring at lambda.

Multiply gamma_L to the powers occurring in mathfrakA. For any
POSITIVE theta in I, weight p-1, this gives beta_theta in K with

    (beta_theta)=mathfrakA^theta, all |sigma_a beta_theta|=y,
    beta_theta=1 mod lambda^2.                         (14)

The ideal in(14) is integral because theta is positive, so beta_theta
is actually in O. This proves integrality AFTER allowing fractions,
and does not presume negative Jacobi powers are integral individually.
Here a normalized Jacobi lift means precisely this fraction-product
element with the properties(14); no additional membership in a
semigroup of products with only nonnegative exponents is asserted.

Now suppose also theta+jtheta=2N and F(theta)=0, as for UW. From(11),
alpha^theta and beta_theta^p generate the same ideal. The complement
gives |sigma_a(alpha^theta)|=y^p for all a. Therefore their ratio is
a unit with EVERY conjugate of absolute value1. Kronecker's argument
makes it a root of unity: the monic integer polynomials having all
conjugates of each positive power on the unit circle have uniformly
bounded integer coefficients; two such powers coincide. In K the
ratio is consequently +/-zeta^h.

Put r=x-1, a unit locally at lambda. Expanding only modulo lambda^2,

    alpha^theta=prod_a(r+a lambda)^n_a
       =r^(p-1)[1+(lambda/r)sum_a n_a a]=1 mod lambda^2.

Here Fermat's congruence makes r^(p-1)=1 mod p, and F(theta)=0 makes
the displayed linear sum divisible by p. These are local congruences
at lambda, equivalent to the stated ideal congruences for integral
elements. By(14), beta_theta^p=1 mod lambda^2 as well. Among +/-zeta^h
the only root congruent1 mod lambda^2 is1: reduction modulo lambda
first excludes the negative sign, and the coefficient of lambda then
forces h=0 modulo p. We obtain the EXACT identity

    beta_theta^p=(x-zeta)^theta.                       (15)

No class-number assumption, primary-singular theorem, source Lemma14
second-case parity condition, or p^e-denominator has been imported.
Our equation(0) has e=0. We do NOT claim this argument has proved the
generalized G_p(x)=p*y^p case or changed the source's weight conventions.

## 6. H1: an actual full-kernel construction with one nonzero jet

Choose the UW pair theta_i and ANY half-sets H_i of G, one from each
pair c,-c. There are h=2m=p-1 selected columns v=(i,c). Put

    theta_v=sigma_c theta_i, beta_v=sigma_c beta_(theta_i),
    e_v=E(theta_v),  D=diag(e_v).

All e_v are pairwise distinct by the accepted faithful Fourier map,
freeness and disjointness of the two UW orbits. They satisfy
|sigma_a e_v|<=p-1 for every a. These are FOURIER values, not the
reciprocal first coefficient L(theta). The source's original infinity
chart is

    f_theta(T)=prod_a(1-zeta^a T)^(n_a/p),
    f_theta(0)=1, [T]f_theta=-E(theta)/p.               (16)

It is analytic for |T|<1 by the branch at0, and Galois acts on its
coefficients. Set T=1/x and B=|x|^((p-1)/p). Since p-1 is even,
the pth powers in(15)--(16) agree and give, at every embedding,

    sigma_s beta_(theta_i)
       =B zeta^(-kappa_i(s)) f_(sigma_s theta_i)(1/x). (17)

Every f value is nonzero, and two pth roots differ by a pth root of
unity, so kappa_i(s) is uniquely defined modulo p. Complex conjugation
of(17), using real x and the canonical series, gives

    kappa_i(-s)=-kappa_i(s).                           (18)

The ACTUAL pulled-back constant rows are therefore

    A_(a,(i,c))=zeta^(-kappa_i(ac)/a).                 (19)

Equation(18) gives A_(-a)=A_a. There are at most m distinct rows;
write their K-row space as W, of dimension1<=r<=m<h. Every row is
free of zero coordinates.

Here is the existing bouquet argument, with the exact conclusion we
need. If W D were contained in W, take a row w in W with no zero
coordinate. All w,wD,...,wD^(h-1) would belong to W. Their determinant
is (prod_v w_v) times the Vandermonde on the DISTINCT e_v, nonzero.
That contradicts dim W<h. Thus W D is not contained in W. Since W
is spanned by the ACTUAL A rows, at least one actual row A_(a0)D is
outside W. This last statement follows by linearity; it is not an
identification of an arbitrary bouquet row with an elementary target.

Choose r independent A rows, append A_(a0)D, and choose r+1 columns
on which the resulting square matrix S is regular. Write d0=det S.
On these columns put

    Lambda=adj(S)e_(r+1),

and extend it by zeros to all h columns. The cofactor formula gives

    A_a Lambda=0 for EVERY a,
    A_(a0)D Lambda=d0!=0.                             (20)

Every Lambda_v is an r-by-r minor using ONLY the constant A rows:
the appended weighted row is deleted in this cofactor. Hence Lambda_v
is integral and every conjugate has absolute value<=r^(r/2) by
Hadamard. For a convenient integral uniform constant put

    C=m^m, K0=4(m+1)C, H=2(m+1)(p-1)C=m K0.          (21)

Then all |sigma_a Lambda_v|<=C, and there are at most r+1<=m+1
nonzero entries. Equation(20) and the e_v bound give

    |sigma_a d0| <= (m+1)(p-1)C, EVERY a.             (22)

Choose u among1 and zeta^(a0^(-1)) so that

    rho=sigma_(a0)(u d0)+j sigma_(a0)(u d0)!=0.        (23)

This is possible: if z=sigma_(a0)d0 has nonzero real part, choose1.
Otherwise z is nonzero purely imaginary, and multiplication by zeta
gives nonzero real part since sin(2*pi/p)!=0. Set ell_v=u Lambda_v,

    Delta=sum_v ell_v beta_v,
    delta=Delta+jDelta in O_(K^+).                    (24)

All conjugate constants cancel by the STRONG complex equations(20)
and §4, not by transporting a single equation with fixed coefficients.
At embedding a0 the real first coefficient is -rho/p and is nonzero.
The number rho is a nonzero algebraic integer in K^+, and every one
of its conjugates has absolute value<=H by(22). Notice that this
does NOT force delta itself to be nonzero at the particular T=1/x.
That branch is treated separately in §7.

This construction makes NO claim that A stacked with A D has full
rank h, or that e_(chosen embedding) lies in its image. It guarantees
only a strict rank increase and one nonzero first coefficient after
cancelling ALL constants. It is valid even when the actual A has
rank smaller than m. The general weak mechanism would also work
with a SINGLE complete free orbit; universal two-orbit selection is
not logically necessary for this deliberately weak height bound.

## 7. H2: a weak uniform height bound, both delta branches

For any positive theta of weight p-1 and at every embedding, the
coefficients of f_theta from(16) are majorized in absolute value by
those of

    (1-T)^(-alpha), alpha=(p-1)/p in(0,1).

Indeed |binom(s,k)|<=binom(s+k-1,k) for s>=0, by comparing each
factor |s-l|<=s+l, and multiplication preserves coefficientwise
majorization. Sum the exponents s=n_a/p to get alpha. The kth
coefficient of the majorant is alpha(alpha+1)...(alpha+k-1)/k!<=1.
Consequently, for real |T|<=1/2,

    |f_theta(T)-1|<=2|T|,
    |f_theta(T)-1+E(theta)T/p|<=2|T|^2,               (25)

uniformly under EVERY embedding. No unstated analytic continuation,
positivity of x or asymptotic O-constant is used.

By(20),(24),(25) and the support/cofactor bounds, for every real
embedding a of K^+,

    |sigma_a(delta)| <= K0 B/|x|
                      =K0 |x|^(-1/p).               (26)

If delta!=0, its norm is a nonzero rational integer, so multiplying
(26) over the m real embeddings yields

    1 <= K0^m |x|^(-m/p),  hence |x|<=K0^p.          (27)

If delta=0, use the FIRST coefficient at the chosen embedding a0,
where(23) ensures nonzero rho. The remainder part of(25), with the
same support bounds, yields

    B |rho|/(p|x|) <= K0 B/|x|^2,
    |x| <= p K0/|rho|.                               (28)

All conjugates of the nonzero integer rho in K^+ are bounded by H.
Its nonzero integer norm therefore gives |rho|>=H^(-(m-1)). Thus

    |x| <= p K0 H^(m-1) when delta=0.                 (29)

Combining the two branches gives the more precise valid bound

    |x|<=max{K0^p, p K0 H^(m-1)}.                    (30)

Since K0<=4pC, H=mK0<=pK0, and m<=p, both terms in(30) are at
most(4p^2 C)^p. This proves the proposed(1). All constants depend
only on p; the actual phase pattern and the chosen minor may depend
on x. Their uniform cofactor bounds were proved before taking norms.

The exponent and constants are intentionally loose. Even C could
be replaced by the sharper Hadamard factor, without giving the
source's stronger all-but-one cancellation. No finite search is
proposed as a replacement for the remaining Diophantine inference.

## 8. What is still missing, and what actually failed

J1/J2 prove a reciprocal-chart jet statement with a common normalization.
They do not make the actual infinity-chart matrix(19),(9) regular.
RK's exact separation and UW's disjoint orbits are necessary useful
inputs to several interpolation routes; they are not a theorem about
solution-specific phases or every-conjugate elementary targets.

H1 solves a weaker EVERY-conjugate constant problem using the ACTUAL
phase rows. It does not solve the desired source pattern: constants
zero at every real embedding and first jets zero at all but one.
The formal covariant example in §4 shows why a generic rank lemma
cannot assert that pattern from ordinary jet separation alone. To
deduce it for actual solutions needs additional arithmetic information
about kappa_i(s), or a different construction with quantitative bounds.
No claim that the formal bad pattern is arithmetically realizable
has been made.

H2 is a genuine weak arithmetic consequence of the stated inputs,
not an exclusion. Its upper endpoint is at least p^(2p). For example,
even a hypothetical independent lower bound of the size
p^(2p-5)/2^(p-2) would be SMALLER than this upper endpoint, so the two
would not contradict each other. That comparison is elementary and
does NOT import or audit the original lower-bound proof. The previously
accepted CF1 finite first-case corollary is unchanged. Residues x=0,-1
mod p, other primes, off-diagonal parameters and the full annual
classification remain open in the record.

The published original two-list method, later binomial/Vandermonde
method and bouquet lemma are explicitly attributed. This packet does
not certify the entire published proof, declare its theorem false,
or claim its weak bound improves known work. It records complete
separated proofs of the valid interfaces and a precise remaining gap.

No mathematical program, CAS, scan, sample table, certificate replay
or enlarged orbit count was used. Source reads, metadata hashing and
preservation checks have only their stated documentary roles. All
claims in this new packet remain candidate-unverified until TWO OTHER
whole adversarial audits and coordinator reconciliation are complete.
