# Actual phase constraints and a higher-weight Jacobi obstruction

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
`/root/review_2017_coarsening_r1`; requested gpt-6.1-sol/max, effective
setting readback unavailable. TWO OTHER initially blind WHOLE audits
and coordinator reconciliation are required. No novelty, published
theorem refutation, new Diophantine exclusion or full annual answer is
claimed. Every statement below has its own domain.

## 0. Official target, accepted inputs and proposed scope

The official open target is B4(b): all integers x,y,n,q with n,q>=2
such that

    1+x+...+x^n=y^q.

The arithmetic statements here concern ONLY

    G_p(x)=1+x+...+x^(p-1)=y^p,
    p>=37 PRIME, x,y integers, |x|>=2.                 (0)

Thus the official degree is n=p-1 and q=p. Negative x is retained.
Here y>=2, because G_p(x)>1. Accepted C2 excludes x=1 modulo p;
put r=x-1, a unit modulo p. No preliminary proof, other exponent
sector, boundary classification or annual classification is attempted.

Use the complete accepted R6, UW, RK, FS and OW scopes. R6 A1 supplies
the matched-prime Jacobi ideal formula and its normalization argument,
the full integral module generation, and the actual e=0 Jacobi lift.
UW supplies an original-weight positive pair; RK supplies separation
on a fixed complement, not phase rank. Older FS and R6 were authored
by this constructor; their accepted authority comes from TWO OTHER
whole audits, not self-recertification here. The necessary arithmetic
extension is reconstructed in Sections1--3.

The proposed conclusions are:

* **R7A:** on the actual odd Fermat lattice, phase is additive, and
  its value on p times the odd Stickelberger lattice is forced by
  the DIRECT first moment. No coefficientwise reduction assumption
  is made.
* **R7B:** a divided direct moment Omega determines the entire
  character-one projection of the ACTUAL phase, including a product
  identity for the pulled-back original-weight phases.
* **R7C:** the remaining freedom is precisely a functional on an
  abstract lattice quotient. G-invariance of the actual phase kernel
  is equivalent to the pure character-one model. It is EXTRA arithmetic
  information, not a consequence of additivity or complex conjugation.
* **R7D:** a pure full-orbit phase is equivalent to rank1 of its full
  pulled-back constant matrix. For an ACTUAL ORIGINAL-weight nonnorm
  element it implies |x|<=4^p. This is CONDITIONAL, gives no new
  exclusion, and is not a global improvement over published bounds.
* **R7E:** actual normalized positive Jacobi products at a MUCH HIGHER
  weight can have free, disjoint Fourier/reciprocal arrays but rank1
  phase rows and rank2 stacked constant/first-jet rows. This is an
  exact counterexample ONLY to an overbroad weight-free rank assertion.
  Its inverse first moments vanish. No solution of(0) is constructed.

The original-weight higher-jet cancellation bridge remains open.
No mathematical code, scan, CAS, numerical table or certificate replay
is used. All algebra below is hand-derived. Classical input is attributed.

## 1. Conventions and the actual arithmetic lattice

Let zeta=exp(2*pi*i/p), K=Q(zeta), O=Z[zeta], lambda=1-zeta,
G=F_p^*, sigma_a(zeta)=zeta^a, j=sigma_(-1), and N=sum_a sigma_a.
Subscripts on sigma are DIRECT. For theta=sum_a n_a sigma_a put

    wt(theta)=sum_a n_a,
    F(theta)=sum_a n_a*a mod p,
    M_1(theta)=sum_a n_a/a mod p,
    E(theta)=sum_a n_a*zeta^a.

Use

    vartheta=(1/p)sum_(c=1)^(p-1)c sigma_c^(-1),
    I=Z[G] intersect vartheta Z[G],
    M={eta in I:j eta=-eta},
    L=M intersect ker F.                              (1)

M is defined literally as the odd sublattice, not as an unproved
identification with (1-j)I or with its coefficientwise mod-p image.
Both M and L are finitely generated free abelian groups. They are
G-stable; pM subset L and pL subset pM. Oddness gives weight0.

For a solution(0), let alpha=x-zeta. Accepted R6 A1 gives the integral
ideal A with A^p=(alpha), Norm(A)=y. Each rational prime ell dividing y
is 1 modulo p, and A has support at exactly ONE prime over each such
ell. These facts also follow directly: ell cannot divide x; if ell
divides G_p(x), then either x has order p modulo ell or ell=p and
x=1 modulo p. The latter is excluded. The p distinct roots of unity
modulo a split ell identify exactly one prime dividing x-zeta.
The same support description applies to A0=(x-zeta) for arbitrary
|x|>=2 with p not dividing x-1, whether or not(0) holds.

The map eta -> A^eta from Z[G] to fractional ideals is INJECTIVE.
Indeed choose ell dividing y and the unique prime P over ell occurring
in A, with valuation e>0. In A^eta the exponents at the p-1 distinct
primes sigma_a(P) are e*n_a, up to a fixed harmless indexing
permutation. Equality to the unit ideal forces every n_a=0.
The identical argument applies to A0, since G_p(x)>1. This is an
ideal-faithfulness assertion, not a class-group assertion.

The attributed classical matched-prime Jacobi ideal formula states
that, for every P over ell=1 modulo p and every nontrivial character
triple chi^a,chi^b,chi^(a+b), the appropriately matched minus-normalized
Jacobi sum has ideal P^psi(a,b), all absolute values sqrt(ell), and
is 1 modulo lambda^2. The exact formula and direct character-count
normalization are in accepted R6 A1, Section5, and in the original
Mihailescu diagonal chapter Section2.2. Its full ideal theorem is
not newly proved here.

Put Theta_a=(a-sigma_a)vartheta for 1<=a<p, Theta_p=p*vartheta,
and psi_t=Theta_(t+1)-Theta_t for 1<=t<=p-2. Accepted R6's integral
preimage argument gives

    I generated over Z by psi_1,...,psi_(p-2), j psi_1,
    wt(psi_t)=wt(j psi_1)=(p-1)/2,
    Theta_p=sum_t psi_t+N, N=psi_1+j psi_1.            (2)

Negative INTEGER coefficients are permitted in this generating
expression. No cardinality assertion about a chosen source basis,
nor cancellation of vartheta on the entire group ring, is required.

## 2. R7A: normalized odd Jacobi fractions and actual phase

For each eta in M, express it using(2). Its generator-coefficient sum
is zero, because all generators have the same nonzero weight and
wt(eta)=0. For each prime occurring in A take the matched Jacobi
sums, with the corresponding integer exponents and prime valuations.
Their product, allowing fractions, is an element Gamma_eta in K^*
such that

    (Gamma_eta)=A^eta,
    |sigma_a(Gamma_eta)|=1 for every a,
    Gamma_eta=1 mod lambda^2.                         (3)

The congruence is in the local ring at lambda. Negative powers are
allowed because the Jacobi factors are lambda-units. Two constructions
with(3) have quotient a unit with every absolute value1, hence a root
of unity by Kronecker's argument. The roots of unity in K are exactly
+/-zeta^h; only1 is 1 modulo lambda^2. Thus Gamma_eta is unique.
It follows that

    Gamma_(eta+nu)=Gamma_eta Gamma_nu,
    Gamma_(sigma_a eta)=sigma_a Gamma_eta.             (4)

No assertion of integrality for a general Gamma_eta is made.

The elements alpha^eta and Gamma_eta^p have the same fractional ideal.
Oddness gives every absolute value of alpha^eta equal to1. Their
quotient is again a unit root of unity. Locally,

    alpha^eta=prod_a(r+a lambda+O(lambda^2))^n_a
             =1+(lambda/r) sum_a n_a*a mod lambda^2.

Here wt(eta)=0 even for negative coefficients. Since zeta^h=1-h lambda
modulo lambda^2 and Gamma_eta^p=1 there, comparison gives the EXACT
identity

    Gamma_eta^p=zeta^(F(eta)/r)*alpha^eta, eta in M.   (5)

Exponents of zeta are in F_p; 1/r means its inverse modulo p.
In particular Gamma_theta^p=alpha^theta for theta in L.

For any integer group-ring vector nu define the canonical analytic
series, with constant1,

    f_nu(T)=prod_a(1-zeta^a*T)^(n_a/p), |T|<1.        (6)

Negative exponents are allowed. Products and conjugation agree with
the branches at0. For theta in L, its weight0 gives
f_theta(1/x)^p=alpha^theta. Define the ACTUAL additive phase by

    f_theta(1/x)=zeta^kappa(theta)*Gamma_theta,
    kappa:L -> F_p.                                  (7)

Both sides are nonzero. Equations(4) and multiplicativity of(6) prove
additivity. Complex conjugation, which is continuous at the real
argument1/x, proves kappa(j theta)=-kappa(theta). Additivity gives
kappa(p theta)=0 for theta in L; thus kappa factors through L/pL.
This is NOT a claim that it factors through coefficientwise F_p[G].

For ANY eta in M, p eta belongs to L and

    f_(p eta)(1/x)=alpha^eta,
    Gamma_(p eta)=Gamma_eta^p=zeta^(F(eta)/r)*alpha^eta.

Therefore

    kappa(p eta)=-F(eta)/r, eta in M.                 (8)

This is a restriction on actual phases, not a formally assigned model.
Additive phase and character decompositions are existing source ideas;
the precise integer-lattice restriction(8) is exposed to prevent an
unjustified reduction to coefficients modulo p.

## 3. R7B: the divided moment and the character-one projection

For theta=sum n_a sigma_a in L, using representatives1<=a<p, put

    Omega(theta)=(sum_a n_a*a^p)/p mod p.             (9)

The numerator is divisible by p, because F(theta)=0. Division is
over the INTEGERS before reduction modulo p. Then Omega is additive,

    Omega(sigma_c theta)=c Omega(theta),
    Omega(p eta)=F(eta), eta in M.                   (10)

For completeness, these facts and the needed projection can be proved
without any p-saturation hypothesis on I as follows. Let omega(a) be
the Teichmuller lift in Z_p: omega(a)^(p-1)=1 and omega(a)=a modulo p.
Its existence and uniqueness follow by successively correcting a root
modulo p^k, since the derivative(p-1)*a^(p-2) is a unit. Products obey
omega(ac)=omega(a)omega(c) by uniqueness; omega(-a)=-omega(a).
Also omega(a)=a^p modulo p^2: write a=omega(a)+p b and take its pth
power. Put

    Fhat(v)=sum_a v_a*omega(a),
    e_1=(1/(p-1))*sum_a omega(a)^(-1)*sigma_a in Z_p[G].

Direct multiplication gives

    e_1*v=Fhat(v)*e_1, Fhat(e_1)=1,
    j e_1=-e_1, e_1^2=e_1.                           (11)

For theta in L, Omega(theta)=Fhat(theta)/p modulo p.
This proves(10), including all changes of representative under a
translation. The use of p-adic coefficients is solely finite-rank
lattice algebra; no p-adic binomial evaluation is transported to C.

Write M_p=M tensor Z_p and L_p=L tensor Z_p, both inside Z_p[G].
Consider the ACTUAL integer vector

    eta_0=(1-j)Theta_p in M,
    eta_0=sum_(c=1)^(p-1)(2c-p)*sigma_c^(-1),
    F(eta_0)=-2.                                    (12)

The last equation uses DIRECT F: F(Theta_p)=p-1=-1 modulo p.
Thus Fhat(eta_0) is a p-adic unit. Equation(11) implies

    e_1*M_p=Z_p*e_1.

Since F:M->F_p is onto, completing the index-p sublattice gives

    L_p={v in M_p:Fhat(v) in p Z_p},
    e_1*L_p=p Z_p*e_1.                              (13)

For example this equality follows by a basis for the kernel of the
surjective map M->F_p, or by completing its short exact sequence.
It does NOT assert M_p is all odd coefficient vectors.

The additive map kappa extends Z_p-linearly to L_p with values F_p,
because it factors through the finite group L/pL. Its restriction(8)
extends to p M_p. For theta in L,

    kappa(e_1 theta)=-Omega(theta)/r
      =(1/(p-1))*sum_a a^(-1)*kappa(sigma_a theta).

Consequently the actual phase satisfies

    sum_a kappa(sigma_a theta)/a=Omega(theta)/r.       (14)

The sign uses p-1=-1 modulo p. In particular kappa is nonzero:
kappa(p eta_0)=2/r.

For an ORIGINAL-weight positive theta in I_f with theta+jtheta=2N,
delta=theta-N belongs to L. The normalized lift of N is y (indeed
y=1 modulo p), and uniqueness in(3) gives beta_theta=y Gamma_delta.
In(6), f_N(1/x)=y/B, B=|x|^((p-1)/p)>0. Hence the actual phase in

    sigma_a(beta_theta)=B*zeta^(-kappa_theta(a))
                              *f_(sigma_a theta)(1/x)

is exactly kappa_theta(a)=kappa(sigma_a delta). Define Omega(theta)
by(9) for this I_f element as well; the same integer divisibility
applies, and Omega(N)=0 by the paired Teichmuller sum. Thus(14) gives

    tau_a=zeta^(-kappa_theta(a)/a),
    product_(a in G) tau_a=zeta^(-Omega(theta)/r).    (15)

On any half-set H, one from each pair a,-a, tau_(-a)=tau_a, so
product_(a in H)tau_a=zeta^(-Omega(theta)/(2r)).
No nonvanishing assertion for Omega on the selected UW pair is made.

## 4. R7C: exact residual space and the kernel-invariance boundary

Define the compatible character-one functional on L by

    kappa_0(theta)=-Omega(theta)/r.                   (16)

It is additive, vanishes on pL, and has the required restriction(8).
EVERY additive map obeying(8), including the actual one, is uniquely

    kappa=kappa_0+chi,
    chi in Hom_(F_p)(L/pM,F_p).                       (17)

Indeed the difference annihilates pM; conversely every such chi gives
an additive map with(8). L/pM is a finite F_p-vector space because
pL subset pM subset L. It is an ABSTRACT lattice quotient, not
silently an image or quotient of the coefficientwise F_p group ring.
Every such map is odd since j acts as -1 on L. Equation(14) fixes its
character-one projection but not all the remaining components.

For the ACTUAL map the following equivalence is exact:

    ker(kappa) is G-stable  iff  kappa=kappa_0.       (18)

If the kernel is stable, G acts on the additive quotient L/ker(kappa),
which is F_p since kappa(p eta_0)!=0. Thus there is a SINGLE character
chi_G:G->F_p^* with kappa(sigma_a theta)=chi_G(a)kappa(theta).
Apply this to theta=p eta_0. Equation(8) forces chi_G(a)=a.
Therefore kappa(sigma_a theta)=a kappa(theta) for every theta. Applying
the averaged identity above(14) gives kappa(theta)=-Omega(theta)/r.
Conversely(10) makes the kernel of kappa_0 G-stable. This proves(18).

An equality between evaluated quotients therefore cannot simply be
acted on by the COEFFICIENTWISE G-action unless kernel stability has
been separately supplied. This is a structural issue, not an assertion
that coefficientwise action on formal power series is undefined.
For a small abstract check, let a cyclic group of order4 act on F_7^2
by R(u,v)=(-v,u), let j=R^2=-1, and let k(u,v)=u. Then k is additive
and odd, but its kernel is not invariant and its orbit on(1,0) has
values1,0,-1,0. No character law follows from these module properties.
This is NOT an arithmetic phase realization or a counterexample to a
published number-theoretic theorem.

The formal model kappa_0 gives kappa_theta(a)=a*kappa_theta(1).
It is compatible with the proved normalizations. No solution realizing
that model in the original-weight sector is asserted.

## 5. R7D: pure phases, exact rank1, and a conditional small bound

First let k:G->F_p be ANY odd function. Form the FULL square phase
matrix, with a,c in G,

    A_(a,c)=zeta^(-k(ac)/a).                          (19)

Then

    rank_K(A)=1 iff k(a)=a*k(1) for every a.          (20)

Every entry is nonzero. Rank1 makes every cross ratio with the first
row and column equal1. Comparing exponents gives

    k(ac)=a*k(c)+k(a)-a*k(1).

Put h(a)=k(a)-a*k(1). Then h(ac)=a h(c)+h(a).
Commutativity gives(a-1)h(c)=(c-1)h(a), so h(a)=t(a-1).
Oddness gives h(-1)=0, hence -2t=0 and t=0. The converse in(20) is
immediate: all pulled-back rows are the same. This is a FULL-orbit
criterion, not a claim about a selected pair of half-orbits.

Suppose now(0) holds and theta is positive in I_f, with

    theta+jtheta=2N, theta!=N,
    kappa_theta(a)=a*kappa_theta(1) for EVERY a.       (21)

Its weight is p-1. The accepted UW pair supplies examples satisfying
all EXCEPT the last, unknown phase condition; nonzero M_1 implies
theta!=N. Let

    rho=zeta^(kappa_theta(1))*beta_theta in O.

The pure phase condition gives, at each embedding,

    sigma_a(rho)=B*f_(sigma_a theta)(1/x).            (22)

No Galois action on the positive real scalar B is assumed. If rho=j rho,
their ideals imply A^theta=A^(jtheta). The ideal-faithfulness in Section1
would give theta=jtheta, and its complement would then give theta=N.
Thus rho-jrho is a NONZERO algebraic integer.

For positive theta of weight p-1, the binomial majorant gives

    |f_(sigma_a theta)(T)-1|
      <=(1-|T|)^(-(p-1)/p)-1<=2|T|, |T|<=1/2.

The last inequality uses(1-t)^(-s)<=(1-t)^(-1) for0<s<1.
Conjugation of(22) therefore yields

    |sigma_a(rho-jrho)|<=4B/|x|=4*|x|^(-1/p).

Taking the nonzero integral norm proves

    |x|<=4^p under(21).                              (23)

This is the existing zero-signature/norm mechanism after a root-of-unity
twist, not a new method. It supplies no unconditional upper bound,
no source lower-bound import, and no Diophantine exclusion. Published
unconditional bounds are stronger than accepted R6's weak global bound;
they are kept visible in the source audit and are not recertified here.

Consequently any hypothetical solution(0) with |x|>4^p has NONPURE
full-orbit phase on EVERY original-weight nonnorm theta of this type;
its full matrix(19) has rank>=2. In particular its actual phase kernel
on L cannot be G-stable, by(18). Rank>=2 is far short of the desired
full stacked rank or prescribed higher-order cancellation.

There is a second exact limitation. If all columns under consideration
have pure phases on their full orbits, their pulled-back factors tau_v
are independent of the embedding a. For fixed coefficients ell_v and
series coefficients d_(v,k), put Q_k=sum_v ell_v*tau_v*d_(v,k).
The kth REAL coefficient at embedding a is sigma_a(Q_k+jQ_k).
A nonzero element of K has no zero embedding. Thus such a coefficient
cannot vanish at all but one of two or more real embeddings. A pure
signature cannot realize that specific elementary target, even though
some weaker common cancellations may exist. This is a statement about
formal coefficients; it does not presume a nonzero jet evaluates
nonzero at T=1/x.

## 6. R7E: actual high-weight Jacobi products with collapsed rows

This section does NOT assume(0). Fix ANY p>=37 prime and ANY integer
|x|>=2 with p not dividing r=x-1. Set alpha=x-zeta, A0=(alpha),
G0=G_p(x)>1, and eta_0 as in(12). Put

    C=2(p-2), S=sum_(t=1)^(p-2)psi_t,
    u_i=C*N+i*eta_0, theta_i=p*u_i, i=1,2.           (24)

All these are ACTUAL integer elements of I. By(2) and(12),

    eta_0=2S-(p-2)N,
    u_1=2S+(p-2)N, u_2=4S.                         (25)

Thus both u_i have nonnegative coefficients, and(25) expresses them
as nonnegative integer combinations of Jacobi exponents and N.
The least coefficient of u_1 is p-2, and that of u_2 is0, because
the coefficients of eta_0 in the inverse-index order are the distinct
integers2c-p. Both vectors, and hence theta_i, have pairwise DISTINCT
integer coefficients. Each G-orbit is free. They obey

    theta_i+jtheta_i=2pC*N,
    wt(theta_i)=pC(p-1),
    F(theta_i)=M_1(theta_i)=0 mod p.                  (26)

They are not G-conjugate: coefficient permutation preserves the
Euclidean square norm, whereas

    ||theta_2||^2-||theta_1||^2=3p^2||eta_0||^2>0.

This uses wt(eta_0)=0 to cancel the cross term with N.
RK2 on the SAME complement2pC*N now gives two disjoint free reciprocal
arrays, EACH with p-1 values. Fourier arrays are also free and disjoint:
E is injective on Q[G], since a polynomial sum_(a=1)^(p-1)n_a X^a
with value0 at zeta is a multiple of Phi_p(X), whose constant term1
forces that multiple to be zero. Nonzero inverse moment is not needed
for this exact freeness; in(26) it is explicitly absent.

For A0 every supporting prime is split, as in Section1. Form matched
Jacobi products with the NONNEGATIVE exponents in(25), and use G0 for
the N factor. This produces genuine integral positive Jacobi products
gamma_i with

    (gamma_i)=A0^u_i,
    every |sigma_a gamma_i|=G0^C,
    gamma_i=1 mod lambda^2.                          (27)

This is stronger than merely forming an arbitrary fraction and later
using its ideal for integrality. The N factor is normalized because
G0=1 modulo p. For the actual integer alpha^u_i, weight C(p-1) makes
r^(wt u_i)=1 modulo lambda^2, and F(u_i)=-2i. Therefore the explicit
algebraic integers

    beta_i=zeta^(-2i/r)*alpha^u_i                    (28)

are 1 modulo lambda^2. They have the ideals and absolute values in(27).
Their quotients by gamma_i are unit roots of unity congruent1 modulo
lambda^2. Uniqueness gives beta_i=gamma_i: these are ACTUAL normalized
Jacobi products, not formally assigned phases. They satisfy EXACTLY

    beta_i^p=alpha^theta_i.                          (29)

There is no claim G0 is a pth power. If(0) happened to hold, (29) would
also have(beta_i)=A^theta_i; its unconditional construction requires
no such solution.

In(6), f_(theta_i) is now a FINITE polynomial, since each exponent
n_a/p is the nonnegative integer coefficient of u_i. With the common
positive scalar B0=|x|^(C(p-1)), direct evaluation gives

    sigma_s(beta_i)=B0*zeta^(-2is/r)
                                  *f_(sigma_s theta_i)(1/x).

Hence their actual phases are kappa_i(s)=2is/r. For columns(i,c),
with any one-per-conjugate-pair half-set for EACH i, the pulled-back
factors are

    tau_(a,(i,c))=zeta^(-2ic/r), INDEPENDENT of a.     (30)

The constant phase matrix has rank1. The stacked constant/ordinary
first-jet COMPLEX pulled-back matrix has rank EXACTLY2 over K: its
only two possible rows are
(tau_v)_v and(tau_v*d_(v,1))_v, where
d_(v,1)=-E(theta_v)/p=-E(sigma_c u_i). The Fourier argument above
makes these first coefficients pairwise distinct, so the two rows
are independent. There are p-1>2 columns. No rank2 claim for its
K^+-realification is made. Likewise every higher REAL
coefficient is the set of embeddings of ONE element, as in Section5,
and cannot support the all-but-one target there.

The exact admissibility boundary is essential:

* Weight is pC(p-1), with C=2(p-2), MUCH larger than p-1.
* Coefficients are not restricted to0/1/2; both M_1 values vanish.
* Free/nonconjugate fixed-complement arrays, integral normalized Jacobi
  products and the actual pth-root identities ARE retained.
* No integer solution of the official equation or of(0) is supplied.
* These are not the original source's least-residue coefficient lifts.

Thus(24)--(30) disprove only a lemma that discards original weight and
inverse-moment restrictions while asserting phase rank from those
remaining data. They do not refute UW, the original-weight rank target,
or a published Diophantine theorem. They also show why ACTUAL phases
on arbitrary integer lifts cannot generally factor through coefficientwise
reduction: theta_i is zero in F_p[G], but kappa_i is nonzero. This does
not change a source statement explicitly restricted to canonical lifts.

## 7. Primary-source boundary and the exact remaining inference

Original phase additivity, character idempotents, Jacobi normalization,
and zero-signature norm methods are attributed to Mihailescu's original
diagonal chapter. The later Bartolome--Mihailescu appendix provides the
existing Vandermonde/bouquet context. Neither source's complete arithmetic
conclusions nor a blanket higher-jet target are imported. Exact read
limits and published stronger upper bounds are in the companion audit.

Liu--Mihailescu, *An alternative proof of the Catalan conjecture* (2025),
Proposition1, is a newly read PRIMARY lead. Its setting has q>p and
its final remark leaves q=p for later work. It is NOT an input here.
For a diagonal adaptation, the action on equality classes of evaluated
quotients would require the G-stability isolated in(18); coefficientwise
action on the underlying formal series alone does not supply that
condition. No counterexample to the paper's actual arithmetic theorem
is claimed. The abstract check in Section4 has only its stated scope.

The unresolved arithmetic question is now precise. On ORIGINAL-weight
UW elements one would need enough control of the ACTUAL residual
functional chi in(17), together with the exact semilinear coefficient
system, to construct small integral coefficients giving the desired
higher-order cancellations and a nonzero arithmetic difference. The
moment product(15), rank>=2, or mere exclusion of the pure signature
does not establish this. No prescribed target, effective coefficient
bound or compatible arithmetic contradiction has been proved here.

The packet ends at a genuine partial mathematical checkpoint. It does
not defer an unrecorded proof behind source retrieval, a larger scan,
or a claimed independent formalization. TWO OTHER WHOLE audits must
reconstruct R7A--R7E and their stated limits before any promotion.
