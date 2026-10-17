# Whole initially blind R2: universal original-weight UW1–UW4

2026-10-17 UTC. Reviewer: /root/review_2017_coarsening_r1.
Requested gpt-6.1-sol/max; effective-setting readback unavailable.
**Complete whole initial; coordinator reconciliation pending.**

Exact target: notes/original-weight-universal-return-r1-candidate-v1.md,
19429B, SHA25689fb03923c61b7785dbcd2b4ff6e6b6f08e17b7fc1653be6ea72f004831040ed.
Read the COMPLETE main, all40 obligations, constructor checks/ledger,
source audit, full worklog and source/manifest records. The complete
accepted MS/FS/OW bodies and primary source passages were read, with a
bounded reread where combined output was truncated.

I did not construct the NEW UW argument or contribute its cubic/fifth
ratio strategy. I authored OLD FS1–FS3 and previously audited MS/OW
material. Those older independently accepted results retain their exact
scopes; this is NOT an independent re-audit of my own FS theorem.
The new universal two-orbit completion is independently reconstructed
below. Root and the author are its contributors and cannot count as
its independent reviewers.

No NEW UW peer finding/report, later reciprocal-kernel candidate, or
coordinator reconciliation was read before this entire initial freeze.
No mathematical program, prime scan, CAS, sample, certificate replay
or author rerun was performed. Source PDF extraction and administrative
hashing are not mathematical evidence.

## Verdict and scope

I find no substantive defect in UW1–UW4. All40 obligations pass in
their written domains. The new result supplies TWO nonconjugate FREE
positive module elements at ORIGINAL augmentation p-1 for every prime
p>=37, with complement2N, coefficients0/1/2 and nonzero inverse first
moment. The Fourier consequence is exact.

It does not supply cross-list faithfulness for the normalized reciprocal
map, higher-series rank, solution-specific Jacobi integrality, every-
conjugate cancellation, nonzero delta, size bounds or any new
Diophantine exclusion. No p<37 conclusion or novelty is inferred.
Only the coordinator may promote after the other whole audit.

## 1. Official target, module and index conventions

The annual target is2025 B4(b), all integer x,y and n,q>=2 with
1+x+...+x^n=y^q. The sum has n+1 terms. The candidate concerns an
auxiliary cyclotomic module at a prime p; it assumes no actual
solution and does not restrict or classify signed/boundary sectors.

Let G=F_p^* act by DIRECT sigma_a(zeta)=zeta^a. Define

    F(theta)=sum n_a a, M_r(theta)=sum n_a a^(-r) in F_p,
    wt(theta)=sum n_a in Z,
    vartheta=(1/p)sum c sigma_c^(-1),
    I=Z[G] intersect vartheta Z[G], I_f=I intersect ker F.

These are the exact source conventions. The inverse basis used
inside vartheta/Theta is not a redefinition of F as M_1.

I is additive and G-stable; G is abelian and multiplication by an
automorphism preserves both defining lattices. Direct reindexing gives

    F(sigma_h theta)=hF(theta),
    M_r(sigma_h theta)=h^(-r)M_r(theta).

Thus I_f is G-stable and M_1(theta)!=0 implies exact trivial stabilizer.
This is a necessary consequence of any exact group-ring equality,
so there is no lifting from a merely reduced-coefficient stabilizer.

For positive a prime to p, the coefficient of sigma_c^(-1) in
sigma_a vartheta is r_a(c)/p, where r_a(c) represents ac modp.
Consequently Theta_a=(a-sigma_a)vartheta has exactly the stated
integer floors. For1<=t<=p-2,

    psi_t=(1+sigma_t-sigma_(t+1))vartheta in I.

The residue carry c+r_t(c)-r_(t+1)(c) is0 orp, proving binary
coefficients. Floor reflection at p-c makes opposite coefficients
sum1. Hence psi_t is positive, has weight(p-1)/2 and complementN.
These facts hold throughout the allowed index range; no Fueter
basis or nonvanishing theorem is needed.

## 2. Reconstruct the direct action and three inverse moments

Set k_c=floor(ac/p). The nonzero residues ac-pk_c permute1,...,p-1.
Expanding their product modulo p^2 in Z_(p) gives

    1=a^(p-1)[1-(p/a)sum k_c/c] mod p^2.

The canceled factorial is a unit. Dividing the resulting multiple
of p and using Fermat's congruence yields

    sum k_c/c=(a^p-a)/p modp.

This is F(Theta_a), because the direct index of sigma_c^(-1) is c^-1.
Subtraction gives

    f(t)=F(psi_t)=((t+1)^p-t^p-1)/p modp.

The numerator is coefficientwise divisible by p. Its reduced
POLYNOMIAL has degree p-1 and top five coefficients
1,-1/2,1/3,-1/4,1/5 at degrees p-1,...,p-5. This follows from
binom(p,p-j)/p=binom(p-1,j-1)/j. No early X^p=X reduction occurs.

For ell=2,4,6, expand the equality of ell-th-power sums modulo p^2:

    (a^ell-1)S_ell
      =ell a^(ell-1)p sum c^(ell-1)k_c modp^2.

The exact Faulhaber polynomials displayed in the candidate give

    S_2/p=1/6, S_4/p=-1/30, S_6/p=1/42 modp.

I checked their endpoint substitution N=p-1 and constant terms;
their denominators6,30,42 are units for p>=11. Divisibility of
S_ell by p also follows from the finite-field power sum at
ell<p-1. The division is therefore in an integer congruence,
not by zero inside F_p.

Since M_r on sigma_c^(-1) contributes c^r, the exact results are

    M_1(Theta_a)=(a-a^-1)/12,
    M_3(Theta_a)=-(a-a^-3)/120,
    M_5(Theta_a)=(a-a^-5)/252.

The third calculation is the sixth-power identity, not a statement
about a fifth binomial-series coefficient. Its denominator is
invertible precisely in the claimed p>=11 range.

## 3. UW1 normalized identities and all fibers

For t!=0,-1, put H=t(t+1), Q=H+1. Subtract adjacent Theta moments.
The numerator identities

    (t+1)^3-t^3=3H+1,
    (t+1)^5-t^5=5H^2+5H+1

give exactly

    m_1=Q/(12H),
    m_3=-(H^3+3H+1)/(120H^3),
    m_5=(H^5+5H^2+5H+1)/(252H^5).

Let S={t in F_p:t!=0,-1,Q(t)!=0}; it has at least p-4 elements
and m_1 is nonzero everywhere on S. With T=H^2/Q^3,

    H^3+3H+1=Q^3-3H^2,
    H^5+5H^2+5H+1=Q^5-5H^2 Q^2.

Therefore

    w_3=m_3/m_1^3=-(72/5)(1-3T),
    w_5=m_5/m_1^5=(6912/7)(1-5T).

Multiplying out gives
7w_5+800w_3+4608=6912-11520+4608=0, with the T terms canceled.

For a fixed w_3 value b, clearing Q^3 gives a polynomial equation
of degree at most3 in H. It is never the zero polynomial: otherwise
H^3+3H+1 would be proportional to(H+1)^3; leading coefficients
force proportionality1, but the H^2 coefficients would say0=3.
Substitution H=t^2+t is injective on the polynomial ring and
doubles a nonzero polynomial's degree. The resulting nonzero
polynomial in t has degree<=6, so the fiber has at most six
distinct elements. A zero w_3 value is covered. No assertion
that m_3 or m_5 is everywhere nonzero is needed.

All these formulas hold for every prime p>=11. UW1 has no claim
at primes where a displayed denominator vanishes.

## 4. Reconstruct abstract UW2 with repeated u-values

Let char K>7, |S|>30, u:S->K^* be nonconstant, and suppose the
stated relation and six-point fibers for w=v_3/u^3 hold.
Assume every allowed pair with u(s)!=u(t) has the same tuple
of cubic/fifth ratios, say C_3,C_5.

If u(s)=u(t), choose r with a different u-value. The two cubic
ratios for(s,r),(t,r) have the same nonzero denominator and the
same value, forcing v_3(s)=v_3(t). The identical argument works
for v_5. Thus v_r descends to a function V_r of a u-value.

This step is essential: ONLY NOW is every u-fiber contained in
one w-fiber, so it has at most6 elements. Therefore the image
U=u(S) has at least ceil(|S|/6)>=6 distinct values. This does
not assert an unconditional image-size theorem for arbitrary u.

For r=3 or5 and distinct a,b in U, the common-ratio equations
imply every x in U is a root of

    (X-a)^r-(X-b)^r-(b-a)^r

if C_r!=0. Its degree is r-1 and its leading coefficient is
r(b-a), nonzero. Six distinct roots exceed both degrees2 and4.
Hence C_3=C_5=0. The equations then make V_3=A,V_5=B constant
on U, including repeated fibers.

The pointwise relation becomes

    4608 u^5+800 A u^2+7B=0 for every u in U.

This is a degree-five NONZERO polynomial, since4608=2^9*3^2
does not vanish in characteristic>7. It cannot have six
distinct roots. This contradiction proves UW2. It covers
A=0,B=0 and zero moment numerators as written.

Nonconstant u ensures allowed pairs exist. Reversing a pair
does not affect either odd ratio, so ordered/unordered pairing
does not hide a sign issue.

## 5. The nonexceptional direct-zero branch

For a prime p>=37, first suppose f(s)=0 at some s in S. Then
a=psi_s is an ACTUAL positive half-weight element in I_f with
M_1(a)!=0. Choose h!=1,-1; the field has such elements. Set

    theta_1=2a, theta_2=a+sigma_h a.

Both are positive I_f elements of augmentation p-1, complement2N
and coefficients0/1/2. Their inverse moments are2M_1(a) and
(1+h^-1)M_1(a), both nonzero, so both are free.

Coefficient permutations preserve the INTEGER Euclidean norm.
The identity

    ||a+sigma_h a||^2
      =4||a||^2-||a-sigma_h a||^2<4||a||^2

is strict because M_1(a)!=0 makes a free and h!=1. It
separates theta_2 from theta_1's entire Galois orbit.
This reconstructs OW1 under its ACTUAL supplied hypothesis;
there is no universally assumed half-weight kernel element
or sparse-zero condition.

## 6. The complementary branch's exact nonconstancy proof

Now f(t)!=0 for every t in S. Then u=fm_1 takes only nonzero
values there. If it were constant C, the polynomial

    P(X)=Q(X)[Q(X)f(X)-12C X(X+1)]

would vanish at every point of F_p: on S by the assumption;
at Q roots by the outer factor; at0,-1 by f=0 and X(X+1)=0.
Thus X^p-X divides P. Its degree is at most p+3, so the
quotient has degree at most3. The product's support then
has degrees at least p or at most4, giving coefficient0
at X^(p-1), since p-1>4.

But Q^2=X^4+2X^3+3X^2+2X+1, and the top five f coefficients
give the actual coefficient

    1/5-2/4+3/3-2/2+1=7/10, nonzero for p>=37.

The C-term has degree4 and contributes nothing there. This
is a contradiction. It proves nonconstancy on the EXACT S
used by UW2, with exceptional Q roots properly retained in
the all-field polynomial argument. The proof grants no
unconditional six-value image bound.

## 7. Actual positive pair elements and nonconjugacy

For s,t in S with u(s)!=u(t), define

    theta_(s,t)=sigma_(f(t))psi_s+sigma_(-f(s))psi_t.

The indices f(t),-f(s) are NONZERO field residues in this
branch. They are automorphisms, not scalar integer coefficients.
Each summand is a positive binary translate in I, so the
sum has coefficients0/1/2, augmentation p-1 and complement2N.
The direct action cancels, giving theta in I_f.

Direct reindexing gives

    M_1(theta)=(u(s)-u(t))/(f(s)f(t)), nonzero,
    M_r(theta)=(v_r(s)-v_r(t))/(f(s)f(t))^r, r=3,5,

where v_r=f^r m_r. The sign in the second summand is minus
because r is odd. Dividing by M_1^r gives exactly the
UW2 chord ratios. For every G translate, M_r/M_1^r is
unchanged, by the h^-r transformation law.

Here v_3/u^3=w_3 has six-point fibers, and multiplying
UW1 by u^5 gives precisely

    7v_5+800u^2 v_3+4608u^5=0.

The domain has |S|>=p-4>=33>30, and u is nonconstant and
nonzero. All UW2 hypotheses are now proved. It supplies
two PAIRS with different tuples. The corresponding theta
elements cannot be conjugate, since any conjugate pair
would have the same tuple. This implication does not require
that all pair parameters give different elements or that
the invariants classify all orbits.

Both chosen elements are free by their nonzero M_1.
The two branches together prove UW3 for EVERY prime p>=37,
including all p>=101, at the ORIGINAL augmentation.
No smaller-prime extension or actual Diophantine solution
is used. The threshold is symbolic p-4>30, not a scan.

## 8. UW4 Fourier consequence and the precise firewall

For theta=sum n_a sigma_a, E(theta)=sum n_a zeta^a.
If E(theta)=0, the polynomial sum_(a=1)^(p-1)n_a X^a has
degree at most p-1, zero constant term and is divisible by
the minimal polynomial Phi_p. The latter has degree p-1
and constant1, so the multiple is a rational scalar and
must be zero. Phi_p's irreducibility follows by Eisenstein
after X->X+1. Thus E is injective and equivariant.

A selected free theta has p-1 distinct Fourier orbit
values. A value common to the two orbits, by injectivity
and equivariance, would make theta_1 and theta_2 conjugate.
Hence the two full Fourier SETS are disjoint.

This is not a theorem about the later fixed-normalization
reciprocal map R_c. The residue test separates entries
WITHIN each nonzero-M_1 list; both lists' nonzero residues
range over F_p^*, so that test alone does not separate
them across lists. The two moment ratios are necessary
G-orbit invariants, not identities for all higher series
coefficients or a proof of a joint interpolation rank.

The explicit full-group-ring annihilator firewall is also
correct: (1+j)vartheta=N, so(1-sigma_2)(1+j) annihilates
vartheta and is nonzero at p>=37. No cancellation of
vartheta, Fueter basis independence or odd-character
nonvanishing is used.

## 9. Primary source checks and limits

The ORIGINAL author-uploaded Mihailescu diagonal chapter,
internal version2.0 dated2007-09-17 (published2008), was
read in §2.3 definitions and full Lemma3/proof, then the
COMPLETE §4.3 through printed p24. This confirms the
source role of weight-p-1 two-list selection and its
separate solution-specific application obligations.
The proof here does not import its count of pair
decompositions or automatically assume those lists free.

The later Bartolome–Mihailescu1412.5798v2 cached primary
PDF, internal version1.13 dated2021-11-02, was read in
bounded batches of COMPLETE PDF pp5–18, including the
moment definitions, Lemma2.6/2.7 and both appendices.
Its Voronoi even-m/unit hypotheses cover m=6 for p>=11.
The positive two-Fueter pairing is existing methodology;
the present direct derivations and UW2 are not labeled
a novel existence method. No full external theorem or
appendix repair is newly accepted or refuted.

The original map is Fourier evaluation; the later map
is reciprocal with a common normalization. Typographic
overbar extraction limits do not justify equating them.
No full binary of the author-text chapter is claimed.
The existing later cache hash is checked; it is not a
claim of byte identity with a live web renderer.

## 10. Complete initial disposition

All40 author obligations are reconstructed above and
mapped individually in the companion ledger. No
substantive defect or required repair was found.
This is a scoped pass recommendation pending the
other blind whole audit and coordinator reconciliation.

The source-specific singular/augmented systems, integral
cofactors, EVERY-conjugate cancellation, nonzero-delta
and archimedean comparisons remain separate obligations.
No new signed or unrestricted Nagell–Ljunggren exclusion,
class-number condition, full annual answer, absolute
certainty or novelty is claimed by this audit.

