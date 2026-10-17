# R6 reciprocal jets, actual phases and weak height: whole initial R2

2026-10-17 UTC. Reviewer `/root/review_2022_complexity_r2`.
Requested gpt-6.1-sol/max; independent effective-setting readback
unavailable. **Fresh initially blind nonconstructor WHOLE audit.**

I identify no substantive defect in J1, J2, P1, A1, H1 or H2 within
their stated scopes. A1/H2 retain the explicitly attributed classical
Jacobi ideal formula and standard cyclotomic background. The formal
zero-phase construction is not asserted arithmetically realizable.
The height bound is deliberately weak and implies no new exclusion.
This is not promotion, an audit of the entire published Diophantine
proof, a source-theorem refutation, an annual answer or a novelty claim.
The companion 60-check ledger covers all 50 author obligations.

## 1. Independence, version and complete reads

The NEW R6 constructor is `/root/review_2017_coarsening_r1`. I did
not construct, contribute to, or preview its new proof. Root is assigned
the other independent whole audit; I did not read its NEW R6 report,
ledger or findings before freezing this entire initial packet.

I authored the older UW universal original-weight selection packet;
root contributed its exploratory ratio lead. Neither of us was counted
as an independent UW auditor. UW was separately accepted after the
OTHER two whole audits. Its exact accepted result is a premise here,
not an alleged fresh independent review of my own proof. I previously
reviewed MS, PG and CF1. Those historical roles likewise provide no
extra independent R6 audit. FS was authored by the R6 constructor and
separately accepted after other whole reviews. OW and RK have their
own accepted scopes. All these distinctions are visible in their
complete accepted bodies and acceptance records.

Exact target, relative to `problems/2025-B4/`:
`notes/reasoning-return-r6-candidate-v1.md`, 25588 bytes, SHA256
`bdf566f44dcabb5b7bbfb96778b1dd58b7375bf46fcd697c3579564e5e9da627`.
Constructor freeze: `notes/reasoning-return-r6-freeze-v1.json`,
3350 bytes, SHA256
`72885d683855f2bf61f5aeb225f7d17ccecc2dc1e8898c7aae88161b549a26f0`.

I read the COMPLETE main, all 50 obligations, source audit, source JSON,
constructor check and worklog; the full accepted MS/FS/OW/UW/RK bodies
and their acceptance JSONs; the accepted C register and complete C1–C4
body, including the operative signed C2; the accepted PG and CF1 bodies;
the appendix-inspection research note and the official statement.
Combined-output truncation affecting UW's ending and FS's earlier
portion was resolved with explicit bounded reads covering the missing
sections. No unread passage is represented as a complete read.
Primary reading scopes are recorded in the separate source report.
No mathematical program, sample, scan, CAS, certificate or constructor
script was run.

## 2. Exact domain, maps and logical dependencies

The official open part is 2025 B4(b), integers x,y,n,q with n,q>=2,
and 1+x+...+x^n=y^q. The arithmetic claim here covers only

    G_p(x)=y^p, p>=37 prime, |x|>=2,
    G_p=1+x+...+x^(p-1), official degree n=p-1.

For odd p this sum is positive even for negative x, so y>0. All
signed estimates below use |x| and real T=1/x; no positive-base
literature result is used to cover negative x. Boundary |x|<=1,
p<37, other term counts, off-diagonal exponents and generalized
G_p(x)=p*y^p are not conclusions. No preliminary proof is reproduced.

Let K=Q(zeta), O=Z[zeta], lambda=1-zeta, j=sigma_(-1),
G=F_p^*, h=p-1, m=h/2 and N=sum sigma_a. All sigma indices are
DIRECT: sigma_a(zeta)=zeta^a. For theta=sum n_a sigma_a,

    wt(theta)=sum n_a,
    F(theta)=sum n_a a mod p,
    M_r(theta)=sum n_a a^(-r) mod p,
    E(theta)=sum n_a zeta^a,
    L(theta)=sum n_a/(1-zeta^a).

These maps must remain distinct. The fixed normalization lambda on
ALL reciprocal columns is not replaced by sigma_c(lambda). The
original infinity coefficient is -E(theta)/p, not -L(theta)/p.
The defined module is I=Z[G] intersect vartheta Z[G], with
vartheta=(1/p)sum c sigma_c^(-1), and I_f=I intersect ker F.
No cancellation of multiplication by vartheta on the whole group ring
is permitted or needed.

The actual selection input from UW is TWO positive integral theta_i
in I_f, each of weight h, complement theta_i+j theta_i=2N,
coefficients 0/1/2, nonzero M1, free orbits, and different G-orbits.
MS supplies faithful equivariant E. Thus their Fourier orbits are
disjoint and free. RK's exact reciprocal separation is read accurately
on the SAME complement, but its cotangent theorem is not logically
needed to prove J1/J2 or H1/H2. OW's conditional starting hypotheses
are not promoted to universal facts. The p>=37 threshold here comes
from the accepted actual UW pair, not a new small-prime calculation.

## 3. J1: exact all-order normalization and integrality

For every theta in Z[G], including negative coefficients, the formal
binomial product with constant one is well-defined in K[[D]]:

    R_theta(D)=prod_a(1+D/(1-zeta^a))^(n_a/p)
              =sum c_k(theta)D^k.

The geometric sum (1-zeta^a)/lambda is an algebraic integer of norm
one, since numerator and denominator have norm p. Therefore its inverse
is a global cyclotomic unit, not only a local unit. It reduces to
a^(-1) modulo lambda. Hence

    U_l=sum n_a (lambda/(1-zeta^a))^l in O,
    U_l=M_l(theta) modulo lambda.

Logarithmic differentiation is a formal operation at a unit series:

    (k+1)c_(k+1)
       =(1/p)sum_(l=0)^k(-1)^l S_(l+1)c_(k-l),
    S_(l+1)=lambda^(-(l+1))U_(l+1).

Set b_k=p^k k! lambda^k c_k. Multiply the last coefficient equality
by p^(k+1)k!lambda^(k+1) and substitute b_(k-l). All lambda powers
cancel and the remaining p factor is precisely p^l. Thus

    b0=1,
    b_(k+1)=sum_(l=0)^k(-1)^l [k!/(k-l)!]
                 p^l U_(l+1)b_(k-l).

The falling factorial is an ordinary integer for every k and l in
range, including k>=p. This proves b_k integral by induction without
inverting k! modulo p. Modulo lambda every l>=1 summand vanishes
because it contains p. The l=0 term gives b_(k+1)=U1*b_k, so

    b_k=M1(theta)^k modulo lambda for every k>=0.

The k=0 value is one even if M1=0. Zero theta and negative integer
coefficients cause no exception to the formal recurrence. Nothing
here asserts unrestricted integrality of b_k/k! or changes the
published lemma's cutoff by declaration. The normalization is proved
directly, not extrapolated from small k.

## 4. J2: specially chosen half-orbits, ordinary jets only

Let u_i=M1(theta_i)!=0. Choose any representative set A of the
nonzero residues modulo sign. For

    H1={c:u1/c in A}, H2={c:u2/c in -A},

each H_i contains exactly one of c,-c. Inversion and multiplication
by u_i preserve those pairs, and the resulting h column moments
run through A and -A, all nonzero residues exactly once. With rows
k=0,...,h-1 the b_k matrix therefore reduces to the Vandermonde on
these distinct residues. Its determinant is a unit modulo lambda,
so is nonzero in K. Dividing rows by the SAME nonzero
p^k k!lambda^k gives the ordinary c_k coefficient matrix and retains
invertibility.

This proves the actual h=p-1 endpoint instead of importing it from
the later source, whose N is strictly less than p-1. It does not
assert that two arbitrary halves have disjoint residues. The two
complete arrays each reduce to the same nonzero residue set, even
when RK separates them exactly. Conversely one complete free orbit
with nonzero M1 would already give an ordinary h-jet matrix; the
two-half interface is a particular arrangement, not a new universal
interpolation principle. This is a reciprocal-chart ordinary jet
matrix, and does not prove rank of the solution-specific infinity
phase equations below.

## 5. P1: exact semilinear pullback, real trace and formal obstruction

Suppose the embeddingwise expansions are

    sigma_a(beta_v)=B zeta^(-kappa_(a,v))
                       sum_k sigma_a(d_(v,k))T^k,

where B is the same positive REAL scalar, T is real and d_(v,0)=1.
One need not and must not apply sigma_a to B as an element of K.
For fixed ell_v in K define

    tau_(a,v)=zeta^(-kappa_(a,v)/a),
    Q_(a,k)=sum_v ell_v tau_(a,v)d_(v,k).

Because sigma_a(tau)=zeta^(-kappa), the kth coefficient of
sigma_a(sum ell_v beta_v)/B is exactly sigma_a(Q_(a,k)). Thus
strong complex cancellation at EVERY conjugate is the collection of
K-linear equations with rows A_a diag(d_(v,k)), for every a and k.
The inverse a in the phase is essential. Transporting one equation
while keeping its coefficients fixed would not prove these equations:
the Galois action also sends ell_v to sigma_a(ell_v).

For delta=Delta+jDelta, conjugation commutes with sigma_a and fixes
the real B,T, so the exact real coefficient is
sigma_a(Q_(a,k)+jQ_(a,k)). These are generally weaker realified
K^+-linear equations, not a K-linear system in the original ell_v.
Imposing Q_(a,k)=0 is a sufficient stronger condition, used later.

The formal zero-phase model is a valid algebraic warning with an
explicit limitation. Take N>2 distinct d_v in K and f_v(T)=exp(d_vT),
with coefficientwise conjugation at other embeddings and all kappa=0.
The ordinary N coefficient rows form a Vandermonde times nonzero
factorial row factors. But all pulled-back constant rows are the
single row (1,...,1) and all first rows are (d_v), so the stacked
constant/first matrix has rank exactly two. A real coefficient is
then sigma_a(z_k) for one z_k in K^+; a nonzero algebraic number
cannot have a zero embedding, so for m>1 it cannot be supported at
exactly one real embedding. Zero phases satisfy the necessary oddness
condition but are not proved to be a solution-specific Jacobi signature.
This formal model is not an actual Diophantine counterexample, a
realizability theorem, or a refutation of either published theorem.

## 6. A1 first stage: actual ideals and their rational prime support

Assume the stated integer solution. Signed C2 at term count p shows
that p|(x-1) would give v_p(G_p(x))=1, impossible for y^p.
Thus lambda does not divide alpha=x-zeta. Distinct conjugates
x-zeta^a and x-zeta^b have difference supported only at lambda,
since 1-zeta^(a-b) is associated to lambda. Their ideals are
therefore pairwise coprime.

If a prime ideal L above a rational ell divides alpha, ell!=p.
The residue of zeta equals the ordinary integer x. As O=Z[zeta],
the quotient field O/L is generated over F_ell by that scalar,
so equals F_ell: residue degree is one. The residue of zeta has
exact order p. If it were one, Phi_p(1)=p would vanish modulo
ell, forcing ell=p. Hence ell=1 modulo p and splits completely.
There is only one prime above ell in (alpha), either by the unique
linear factor zeta=x modulo ell or by conjugate coprimality. Since
Norm(alpha)=G_p(x)=y^p, each such prime valuation is a multiple of
p. Consequently

    (alpha)=mathfrakA^p, mathfrakA integral,
    Norm(mathfrakA)=y>0,

and all rational prime factors of this norm are 1 modulo p. This
checks rational prime support and valuation multiplicities, not merely
coprimality of formal factors. Negative x changes none of these steps.

## 7. A1 module generation, matched Jacobi products and normalization

The ONLY new non-elementary arithmetic formula imported is the
classical Jacobi ideal formula stated in original Section 2.2, with
its nontrivial-character absolute-value identity. For ell=1 modulo p,
a suitable matched character of order p gives the minus-normalized
Jacobi sum J(chi^a,chi^b) with ideal L^psi(a,b) and all absolute
values sqrt(ell), provided a,b,a+b are nonzero modulo p. Conjugating
the character and prime transfers the matched formula to any chosen
prime over ell. I checked that actual statement, sign and inverse
indices in the primary source. I do not claim to prove the entire
Stickelberger ideal theorem from first principles.

For v=sum t_a sigma_a in Z[G], the coefficient of vartheta*v at
sigma_c^(-1) is (1/p)sum t_a r_a(c), r_a(c)=ac modulo p in
1,...,p-1. Thus its integrality is equivalent to
sum t_a a=0 modulo p: necessity follows at c=1 and sufficiency
at every c. These preimage vectors are generated over Z by
p sigma1 and sigma_a-a sigma1, 2<=a<=p-1. Their images generate
I; injectivity of multiplication by vartheta is not assumed.

Writing Theta_a=(a-sigma_a)vartheta and Theta1=0, one has

    psi_t=Theta_(t+1)-Theta_t,
    Theta_a=sum_(t=1)^(a-1)psi_t,
    Theta_p=Theta_(p-1)+N,
    N=psi1+jpsi1.

The penultimate equality follows from (1+j)vartheta=N. Therefore
I is generated by psi_t, 1<=t<=p-2, and jpsi1. Every one has
weight m and is a Jacobi exponent or its Galois translate. In
particular psi_t=psi(1,t), with 1,t,1+t all nonzero; jpsi1 uses
the conjugate character. This verifies the exact interface needed,
without a questionable cardinality claim about a Fueter basis.

Express any weight-h theta in I as an INTEGER combination of these
generators. The coefficient sum of that expression is h/m=2.
For a fixed L form the corresponding product of Jacobi sums with
those integer powers, allowing negative powers. Its ideal is L^theta
and every absolute value is ell because the total exponent is two.
It may initially be a fraction; individual negative powers are not
asserted integral.

The minus normalization gives J=1 modulo lambda² by direct counting.
Write chi(z)=zeta^t(z) and expand zeta^b=1-b lambda modulo lambda².
Over nonzero z each t residue appears (ell-1)/p times. Removing z=1
removes only t=0, so the exponent sum is zero modulo p, since p
is odd; the same applies to 1-z. The constant term of J is
-(ell-2)=1-(ell-1), equal to one modulo lambda² because p divides
ell-1 and v_lambda(p)=p-1>=2. Its linear exponent sum is divisible
by p and also vanishes at this precision. Negative powers preserve
the congruence in the local ring since these Jacobi sums are units
at lambda.

Multiplying these products over the prime powers of mathfrakA gives
beta_theta with ideal mathfrakA^theta, all absolute values y and
beta_theta=1 modulo lambda². When theta is positive its final ideal
is integral, so beta_theta is an algebraic integer. This is the
correct order: form the fraction, identify the final positive ideal,
then infer global integrality. No stronger nonnegative-product
semigroup membership is asserted.

## 8. A1 removes the root of unity in the e=0 sector

For the UW elements, theta+jtheta=2N, so for every embedding

    |sigma_a(alpha^theta)|²=(Norm alpha)²=y^(2p).

Hence alpha^theta and beta_theta^p have equal ideals and equal
absolute values at every embedding. Their ratio is a unit on the
unit circle at all embeddings. Kronecker's finite-polynomial argument
therefore makes it a root of unity, necessarily +/-zeta^t in K.
This classical cyclotomic root classification is attributed background.

Put r=x-1, an integer unit at lambda. Modulo lambda²,

    alpha^theta
       =r^(p-1)[1+(lambda/r)sum n_a a]=1.

Fermat's congruence removes r^(p-1)-1, since p lies in lambda^(p-1),
and F(theta)=0 removes the linear coefficient. Both statements hold
for negative r as well. Also beta_theta^p=1 modulo lambda².
Among +/-zeta^t the negative sign is first excluded modulo lambda
(p odd), and 1-zeta^t=t lambda modulo lambda² forces t=0.
Consequently the exact identity is

    beta_theta^p=(x-zeta)^theta.

This argument does not assume a class-number condition or invoke
the source's second-case parity or relative-weight conventions. It
is derived only in G_p(x)=y^p, not G_p(x)=p*y^p. No primary-singular
or generalized e=1 theorem is smuggled into this normalization.

## 9. Actual signed infinity expansions and the complete constant rows

Choose ANY half-sets H_i and the h=2m selected columns
theta_v=sigma_c theta_i, beta_v=sigma_c beta_i. The faithful Fourier
map and two disjoint free UW orbits make all e_v=E(theta_v) distinct.
Positivity and weight h give |sigma_a(e_v)|<=h everywhere.

The infinity-chart series is

    f_theta(T)=prod_a(1-zeta^a T)^(n_a/p),
    f_theta(0)=1, [T]f_theta=-E(theta)/p.

It is the analytic branch given by its binomial series for |T|<1,
with no zeros there. At T=1/x put B=|x|^(h/p)>0. Since h is
even, x^h=|x|^h also for negative x. The preceding pth-power
identity gives unique phases kappa_i(s) modulo p with

    sigma_s beta_i=B zeta^(-kappa_i(s)) f_(sigma_s theta_i)(1/x).

Conjugation, real B,T and coefficientwise conjugation of the canonical
series give kappa_i(-s)=-kappa_i(s). For column (i,c) the exact
pulled-back constant row is

    A_(a,(i,c))=zeta^(-kappa_i(ac)/a).

In particular A_(-a)=A_a. Let W be the K-row space of ALL these
actual rows; 1<=r=dim W<=m<h. Every actual row is nonzero in every
coordinate. These rows can depend on the solution x, but their
entries remain roots of unity. No generic arbitrary phase is
substituted for the actual solution-specific row space.

## 10. H1: full constant kernel and one actual weighted row

Let D=diag(e_v). If W D were contained in W, choose an actual row
w with all entries nonzero. Then w,wD,...,wD^(h-1) all belong to
W. Their determinant is (product w_v) times the Vandermonde on
the distinct e_v, so these h vectors are independent, contradicting
dim W<h. Thus W D is not contained in W. Since actual A rows
span W, at least one ACTUAL weighted row A_(a0)D is outside W.
This is the exact safe bouquet conclusion, not the assertion that
any desired elementary target lies in the image of a stacked matrix.

Choose r independent actual constant rows and append A_(a0)D.
They have rank r+1, so some r+1 columns give a regular square S.
For d0=det S, put Lambda=adj(S)e_last on those columns and zero
elsewhere. The defining adjugate identity gives

    A_a Lambda=0 for EVERY a,
    A_(a0)D Lambda=d0!=0.

Each Lambda coordinate is a cofactor obtained by deleting the
appended WEIGHTED row. Its entries are therefore solely constant
root-of-unity phases. Thus Lambda is integral, has at most r+1<=m+1
nonzero coordinates, and EVERY conjugate coordinate is at most
r^(r/2) by Hadamard. With C=m^m this is certainly at most C.
The weighted relation then gives

    |sigma_a d0|<=(m+1)h C for every a.

Take u=1 if z=sigma_(a0)d0 has nonzero real part. If z is purely
imaginary and nonzero, take u=zeta^(a0^(-1)), so sigma_(a0)u=zeta;
its product with z has nonzero real part because sin(2pi/p)!=0.
Then

    rho=sigma_(a0)(u d0)+j sigma_(a0)(u d0)

is a nonzero integer of K^+, and every conjugate has absolute value
at most H=2(m+1)hC. Set ell_v=u Lambda_v, Delta=sum ell_v beta_v,
and delta=Delta+jDelta. These are integral and delta is real.
Multiplication by u preserves ALL strong complex constant equations.
At embedding a0 the exact real first coefficient of delta/B is
-rho/p and is nonzero. A nonzero formal coefficient does not prove
that delta at T=1/x is nonzero; the proof properly leaves both
evaluation branches open.

## 11. H2: uniform analytic majorants for both signs

For positive theta of weight h, compare each falling-factorial
coefficient of (1-zeta^a T)^s, s=n_a/p>=0, with the rising-factorial
coefficient of (1-|T|)^(-s). The inequality |s-l|<=s+l for every
integer l>=0 proves coefficientwise majorization, and nonnegative
convolution preserves it. The product majorant is
(1-|T|)^(-alpha), alpha=h/p in (0,1). Each of its coefficients
is at most one because alpha+j<=j+1. Thus for real |T|<=1/2,

    |f_theta(T)-1|<=2|T|,
    |f_theta(T)-1+E(theta)T/p|<=2|T|².

The same bound holds under EVERY embedding since each conjugate
zeta still has absolute value one. It does not apply to an arbitrary
negative-coefficient theta, and none is needed in H2. The actual UW
columns are positive.

Put K0=4(m+1)C. All constants cancel at every embedding; at most
m+1 coefficients have modulus at most C. The first remainder bound,
twice for the real trace, gives at each real embedding

    |sigma_a(delta)|<=K0 B/|x|=K0|x|^(-1/p).

This is uniform even though phases, minor and coefficients may depend
on x. Their conjugate size bounds were established before norms are
taken. No unstated asymptotic O-constant depends on the solution.

## 12. Both norm branches and the final explicit constant

If delta!=0, its norm from K^+ is a nonzero rational integer.
There are m real embeddings, so

    1<=K0^m |x|^(-m/p), hence |x|<=K0^p.

If delta=0, expand at the selected a0 instead. The nonzero linear
coefficient -rho/p and second-order remainder give

    B|rho|/(p|x|)<=K0 B/|x|²,
    |x|<=pK0/|rho|.

Since rho is a nonzero integer of K^+ and all conjugates are at most
H, its integer norm gives |rho|>=H^(-(m-1)). This remains valid
if rho lies in a smaller subfield: the degree-m norm counts the
embeddings with multiplicity. Therefore

    |x|<=max{K0^p, pK0 H^(m-1)}.

Here H=mK0 exactly. Since K0<=4pC, H<=pK0 and m<=p, the
second branch is at most (pK0)^m<=(4p²C)^p and the first branch
has the same loose upper bound. Thus

    |x|<=(4p²m^m)^p.

All constants are finite positive integers for p>=37. Negative x,
|x|=2, possibly zero delta, proper-subfield rho, small row rank and
arbitrary allowed half-sets are covered. No p-dependent phase was
mistaken for a universal coefficient vector independent of the solution;
only the SIZE bound is uniform.

## 13. Whole scope, rejected inferences and disposition

J1/J2 do not imply full all-conjugate phase rank. P1's formal failure
model does not refute arithmetic sources. A1 supplies the exact e=0
normalized lift from an explicitly attributed classical input. H1
annihilates ALL constant rows and retains one actual nonzero first
coefficient; it does not prescribe zero first coefficients at all but
one real embedding. H2 proves its own weak bound in BOTH delta
branches. It neither repairs nor imports the stronger published
inhomogeneous/singular cancellation conclusion.

The new upper endpoint is at least p^(2p). A hypothetical lower scale
p^(2p-5)/2^(p-2) is smaller, so there is no exclusion by comparing
those quantities. No lower-bound theorem or entire class-number proof
is imported in that comparison. Existing finite-range CF1 and earlier
PG conclusions retain their scopes. The residue classes x=0,-1
modulo p and the full signed annual classification are not settled.

Primary original Section 2.2 and the complete original Section 4.3,
the later ordinary-jet statement/proof and complete Appendices 5.1–5.2
were inspected with actual read limitations recorded. The existing
two-list, Vandermonde and bouquet mechanisms are attributed. The
source's larger theorems, class-group computations, appendix target
assertion and binary-Thue parameter hypotheses are not premises.

Only NEW files in the assigned review prefix are written. All candidate,
accepted, older review, shared, cache and Git bytes are preserved.
Metadata-only hashes bind the complete initial report, all inference
checks, source record, exact current inputs and older own chain before
any NEW peer R6 finding is read. No substantive scoped issue or
repair request is identified by this whole audit. The other whole
initial and coordinator reconciliation remain required before promotion.
