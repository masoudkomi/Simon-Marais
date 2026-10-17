# UW1–UW4: initially blind independent whole R1 audit

2026-10-17 UTC. Reviewer `/root/review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; independently verified effective settings unknown.
Target: 19429 bytes, SHA256
`89fb03923c61b7785dbcd2b4ff6e6b6f08e17b7fc1653be6ea72f004831040ed`.
Constructor manifest: 4060 bytes, SHA256
`96ea49d93cec3b08514c1d5d67704f72163332bdbe7feb354c86b821ee90c1a7`.

I reconstructed the WHOLE argument, all forty author obligations, actual
coefficient-vector constructions and relevant original source passages.
No substantive defect or required author repair was found. I recommend
only UW1–UW4 in their written algebraic scopes after both complete
independent audits and coordinator reconciliation. This review does not
promote the candidate or supply a Diophantine exclusion.

I previously whole-reviewed the older FS and conditional OW packets and
PG/CF1 material. I did not construct MS or NEW UW, supply its cubic lead,
derive its fifth-moment completion or repair it. Those old review roles
do not independently recertify any old authored work. The UW constructor
and root co-contributor are excluded as independent reviewers. No new UW
peer report, conclusion or later root inspection was read before this
complete initial freeze. DI was frozen before the first UW target read;
the queued reciprocal-kernel packet remains unread throughout this audit.

## Integer membership and the three separate functionals

In the direct basis, translation by sigma_h replaces a by ha. Thus F
is multiplied by h and M_r by h^(-r). The integer augmentation and
coefficient norm are different invariants. In particular, M_1 nonzero
implies exact trivial stabilizer, since h^(-1)M_1=M_1 forces h=1.
This does not assume that every positive Fermat-module element is free.

The coefficient of sigma_c^(-1) in sigma_a vartheta is r_a(c)/p:
the old index is the representative of ac, rather than a^(-1)c.
Consequently (a-sigma_a)vartheta has the integer floor coefficients
defining Theta_a. Taking the difference gives psi_t in the ACTUAL
intersection I, not merely a vector in F_p[G]. For 1<=t<=p-2, adding
c to the representative of tc produces either the representative of
(t+1)c or that representative plus p. Equality to p is impossible
because (t+1)c is nonzero modulo p. Thus every floor difference is
0 or1. Reflecting c to p-c shows that opposite coefficients sum1.
Their weight is (p-1)/2 and psi_t+j psi_t=N. These identities hold
for the entire allowed index set, without a Fueter-basis assertion.

All later module operations are integer sums of G-translates. An index
-f(s) is a nonzero group element when f(s)!=0; it is not a negative
integer coefficient. This distinction verifies positivity and I-membership
even when a chosen field representative is negative.

## UW1: independent residue calculation and exact fiber bound

For a positive a prime to p write ac=r_a(c)+p k_c. Equality of the
products of r_a(c) and c, expanded in Z_(p) modulo p^2, gives

    1=a^(p-1)(1-(p/a)sum k_c/c) mod p^2.

The factorial and a are units. Writing a^(p-1)=1+p q_p(a) before
dividing the congruence by p gives sum k_c/c=a q_p(a)=(a^p-a)/p.
This is F(Theta_a) because the direct index of its inverse-index term
is c^(-1). It is NOT M_1. Subtracting consecutive a gives the integer
polynomial f=((X+1)^p-X^p-1)/p, reduced coefficientwise afterward.
Its degree is p-1, endpoints0,-1 vanish, and its top five coefficients
are 1,-1/2,1/3,-1/4,1/5 in descending order. No polynomial-function
reduction X^p=X is made before the coefficient comparison.

For ell=2,4,6, equality of the ell-th power sums of the same residues
gives

    (a^ell-1) S_ell/p
       = ell a^(ell-1) sum c^(ell-1) k_c mod p.

Division is first in the integer identity, with S_ell divisible by p
at p>=11. The displayed exact formulas for S_2,S_4,S_6 have reductions
1/6,-1/30,1/42 after division by p. They also follow by telescoping
successive endpoint polynomials; their denominators are units here.
The resulting direct inverse moments are respectively

    M_1(Theta_a)=(a-a^-1)/12,
    M_3(Theta_a)=-(a-a^-3)/120,
    M_5(Theta_a)=(a-a^-5)/252.

The fifth inverse moment comes from the SIXTH power sum. It is not
an asserted fifth coefficient of a cyclotomic binomial series.

Put H=t(t+1), Q=H+1. At allowed t, H is nonzero. Subtraction gives
the candidate's numerators Q, H^3+3H+1, H^5+5H^2+5H+1, with signs
and denominators exactly as written. The elementary differences of
consecutive cubes and fifth powers verify these identities in every
permitted characteristic. On S, Q is also nonzero. Normalization by
the first moment is therefore legitimate and yields, with T=H^2/Q^3,

    w_3=-(72/5)(1-3T),
    w_5=(6912/7)(1-5T).

The coefficient of T in 7w_5+800w_3 is -34560+34560=0; its constant
plus4608 is 6912-11520+4608=0. Thus the linear relation is exact.

A fixed value of w_3 becomes a cubic polynomial equation in H after
clearing Q^3. It cannot be identically zero: proportionality of
H^3+3H+1 and (H+1)^3 would have proportionality constant1 by their
leading terms, then force 0=3 at H^2. Both the factor72/5 and3 are
nonzero at p>=11. Composition with t^2+t preserves a nonzero polynomial
and gives degree at most6. It has at most six distinct roots, including
for a prescribed zero value. This proves the EXACT fiber bound on S.
The set S omits0,-1 and at most two Q-roots, so |S|>=p-4.

## UW2: whole common-ratio contradiction

Suppose the two pair ratios are constant C_3,C_5 on every pair with
different nonzero u-values. Because u is nonconstant, for two points
in one u-fiber a third point in a different fiber exists. Comparing
pairs using that third point cancels the SAME nonzero denominator.
It forces both v_3 and v_5 to be constant within the original fiber.
Hence they give well-defined V_3,V_5 on U=u(S).

Only AT THIS STAGE is each u-fiber contained in a w=v_3/u^3 fiber.
The assumed six-point bound then gives |U|>=ceil(|S|/6)>=6. Without
the common-ratio hypothesis such a transfer of fiber bounds would
be unjustified; no unconditional six-value claim is used.

For r=3 or5 and a in U, the common ratio gives
V_r(x)-V_r(a)=C_r(x-a)^r at every x in U, including x=a as0=0.
Compare this identity with the one based at distinct b in U and use
the pair(a,b). If C_r!=0, all x in U are roots of

    (X-a)^r-(X-b)^r-(b-a)^r.

Its degree is exactly r-1 and its leading coefficient r(b-a) is
nonzero in characteristic greater than7. Six distinct roots exceed
both degree2 and degree4. Therefore C_3=C_5=0. Pairwise comparison
then makes V_3=A and V_5=B constant on all of U.

The pointwise assumed relation now makes every member of U a root
of 4608X^5+800AX^2+7B. Its leading coefficient is never zero in the
stated characteristic, since 4608=2^9*3^2. This degree-five polynomial
cannot have six distinct roots. The contradiction allows A=0 or B=0,
repeated u-values, and zero v_3 or v_5. It proves nonconstancy of the
TUPLE on the allowed pair set, not injectivity of either component.

## UW3: both branches produce two actual original-weight orbits

Fix a prime p>=37. If some s in S has f(s)=0, then a=psi_s is a
positive binary half-weight element in I_f with nonzero M_1. Choose
h different from1,-1, possible since p>=37. The elements2a and
a+sigma_h a are positive I_f elements, have coefficients0/1/2,
augmentation p-1, complement2N and inverse moments2M_1(a) and
(1+h^-1)M_1(a), both nonzero. Freeness of a makes sigma_h a!=a.
The exact integer identity

    ||a+sigma_h a||^2=4||a||^2-||a-sigma_h a||^2

is then strict. Its two sides' invariant norms separate the two
conjugacy classes. No reduction of that norm modulo p is used.
This supplies, rather than presumes, the older OW1 starting hypothesis.

In the complementary branch f(t)!=0 for every t in S. Thus
u(t)=f(t)Q/(12t(t+1)) is everywhere nonzero. To check nonconstancy
on precisely this S, suppose u=C and form P=Q(Qf-12C X(X+1)).
On S it vanishes by the supposition; at Q-roots the outer factor
vanishes; at0,-1 the endpoint identities apply. It vanishes at ALL
field elements, so the product of the p distinct linear factors,
X^p-X, divides P in the POLYNOMIAL ring. Its degree is at most p+3,
giving a quotient of degree at most3. Such a product has zero
coefficient at X^(p-1), since p-1>4. Direct convolution with Q^2
instead gives1/5-2/4+3/3-2/2+1=7/10, nonzero for p>=37. The
C-term has degree4. This proves exactly the needed nonconstancy,
including every exceptional root case.

For each pair with different u-values, both nonzero automorphism
indices in theta_(s,t)=sigma_(f(t))psi_s+sigma_(-f(s))psi_t are
defined. The DIRECT moment cancels; the first INVERSE moment is

    (u(s)-u(t))/(f(s)f(t)),

which is nonzero. Consequently these actual positive I_f vectors
are free, with coefficients0/1/2, augmentation p-1 and complement2N.
For odd r=3,5 the negative automorphism contributes the correct minus
sign. Setting v_r=f^r m_r gives exactly the pair ratios in UW2 after
division by M_1^r. These ratios are NECESSARY G-orbit invariants,
as translation scales their numerator and denominator by h^-r.
No completeness of the invariants or distinct parameter count is needed.

Here w=v_3/u^3 is precisely the established w_3, and multiplying UW1
by u^5 gives7v_5+800u^2v_3+4608u^5=0. The set has at least33 points,
hence more than30. Every UW2 premise is now satisfied for the actual
source functions. Two pairs with differing tuples exist and give two
nonconjugate vectors with all required properties. This closes the
complementary branch and the complete UW3 proof for EVERY p>=37.
The omitted smaller primes are not inferred from examples or failure
of a threshold; no assertion about them is made by this proof.

## UW4, adversarial limits and whole conclusion

The Fourier evaluation map E on integer vectors is faithful: a kernel
polynomial of degree at most p-1 and constant0 would be a rational
multiple of Phi_p, whose constant is1, and hence zero. Its irreducibility
follows from Eisenstein after translation by1. Equivariance then
identifies exact stabilizers. Each selected orbit has p-1 distinct
Fourier values, and equality between the two sets would force exact
conjugacy of the integer vectors, contradicting UW3.

This proof has not applied Fourier injectivity to the fixed-normalization
reciprocal map. Its nonzero inverse-moment residues each run through
the same nonzero field elements and do not give reciprocal cross-list
separation. Nor do the two moment invariants prove higher-series rank,
Jacobi normalization/integrality, cancellation in every conjugate, a
nonzero delta branch or a compatible archimedean bound. Those source
application obligations remain outside UW1–UW4. The separate source
appendix note is not converted into a refutation of an external theorem.

The displayed full-group-ring annihilator of vartheta is valid and
explains why no cancellation by vartheta can replace the proof:
(1+j)vartheta=N and (1-sigma_2)N=0, while
(1-sigma_2)(1+j) is nonzero for p>=37. No odd-character nonvanishing,
basis independence, sparse-zero input, decomposition-count estimate or
higher-weight FS3 element is used. Repeated u-values are addressed
before counting, all normalization denominators are nonzero, and zero
higher moments are retained through the final contradiction.

This is a whole algebraic reconstruction, not a collection of unrelated
local checks or an extrapolation from samples. The primary source
definitions and original two-list application were checked with the
limits in the separate source record. No mathematical code, scan,
CAS, certificate replay or author rerun was used. Administrative hashes
are not mathematical evidence. All older packets and current inputs
remain byte-identical, and only this assigned prefix was written.
The separate per-inference ledger covers all forty obligations.
Coordinator reconciliation after the other complete independent audit
remains required; no annual classification, novelty or promotion is made.
