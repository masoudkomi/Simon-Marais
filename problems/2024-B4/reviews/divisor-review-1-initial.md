# Initial independent whole audit of the two fixed-divisor criteria

2026-10-17 UTC. Reviewer: `review_2017_coarsening_r1`. Requested model
`gpt-6.1-sol`, reasoning `max`; no verified effective-setting readback.
This is a fresh nonconstructor audit of the entire divisor packet. I did
not read another divisor review, its issues, or its conclusions before
freezing this report and the accompanying records. Earlier assignments
and frozen files are preserved. Only 2024 B4(b) is considered.

Candidate: `../notes/divisor-reasoning-r2-candidate-v1.md`, SHA256
`48d2ca76b3492584b38d8798650e078c7c9771fea97bae8db4d7cd51b21e2fc4`.
The supplied fourteen-artifact manifest has SHA256
`76143ab6f93a41f0fe5c3db8088e184f41c0159c8d61b089e0bdb66c3477b971`.
Every listed artifact was rehashed successfully. My independent finite
checker was written and executed before reading the constructor's checker.

## Recommendation and exact scope

I found no substantive mathematical defect. I recommend accepting the
following partial results once the coordinator has the second independent
audit and reconciles both issue ledgers:

* For every odd integer n>=3, the whole polynomial phi_7 divides phi_n
  exactly when n=7, and phi_11 divides phi_n exactly when n=11.
* Using the attributed Janwa--McGuire--Wilson absolute-irreducibility
  theorem, the displayed gcd and common absolute-component consequences
  hold over F2 and its algebraic closure.
* The finite odd-degree sum corollary, including the zero sum, holds.
* The fixed irreducible factor reduction is a correct consequence of
  published effective recurrence zero-set theory, with its stated field
  hypotheses.

This is a recommendation by one reviewer, not promotion of the candidate.
It neither classifies all reducible phi_n nor identifies all factors of
degrees four or eight. At n=7 and 11 the respective fixed factor has unit
cofactor, so the criteria do not produce a new reducible exponent. The
packet makes no priority or new general-method claim.

## 1. Official domain, polynomial meaning, and endpoints

I checked the [official 2024 Paper B, page 2](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2024_paper_b.pdf)
and the local statement. The requested domain is positive odd n and
coefficientwise congruence, with both integer factors nonconstant modulo
two. Work in T=F2[x,y,z] therefore has the correct meaning: an F2
factorization lifts by choosing integer representatives of coefficients.
Replacing polynomial equality by equality of functions on F2^3 would be
invalid and is not done here.

Write R=(x+y)(y+z)(z+x), f_n=x^n+y^n+z^n+(x+y+z)^n, and
phi_n=f_n/R for odd n>=3. For n>1 odd, the coefficient of x^(n-1)y
in f_n is one. Consequently f_n and phi_n are nonzero and phi_n is
homogeneous of degree n-3. At n=1 the zero numerator cannot be Rgh
with nonzero nonconstant g,h in a domain. At n=3 the quotient is one.
Neither endpoint is silently included in a positive-degree factor claim.
No preliminary infinite family was reconstructed or used in this audit.

## 2. The attributed general recurrence reduction

Let G be a nonconstant F2-irreducible polynomial not dividing R. Since
T is a UFD, (G) is prime. The field K=Frac(T/(G)) is explicitly finitely
generated over F2. Put a_i equal to the images of x,y,z,x+y+z. For
v(n)=sum a_i^n, n>=0, the monic polynomial product_i(U+a_i)
annihilates v under the shift operator. Each power sequence is killed by
its own first-order factor; commuting factors kill their sum. This remains
true with repeated a_i or with a_i=0. The convention 0^0=1 makes the
zero-root sequence (1,0,0,...) satisfy that first-order relation also at
index zero.

For the relevant odd n>=3, reduction modulo G gives

    G divides phi_n  iff  f_n=0 in T/(G)  iff  v(n)=0 in K,

because the image of R is nonzero. The quotient domain embeds in its
fraction field, so the final equivalence loses no information.

[Derksen, Theorems 1.10 and 4.14](https://arxiv.org/pdf/math/0510583v1)
apply: the former requires a field finitely generated over F_p and an
explicit recurrence; the latter gives automaticity in positive
characteristic without a simplicity assumption. The effective proof also
constructs automata from its output descriptions. All hypotheses hold
here; possible degeneracies are covered by the stated theorems. Intersecting
with odd n>=3 is an effective regular-language restriction. The resulting
claim concerns a fixed G and supplies no finite list of all possible G.

The candidate correctly attributes this method. Its particular singleton
sets are established below rather than inferred from the general theorem.

## 3. Formal generating identity and actual divisibility

I reconstructed the tools repeated from the accepted phi_13 packet rather
than treating its status as a substitute for checking the new application.
For the four entries x,y,z,x+y+z the elementary symmetric functions are
0,Q,R,D, with Q=x^2+y^2+z^2+xy+yz+zx and D=xyz(x+y+z). Thus

    E(t)=1+Qt^2+Rt^3+Dt^4,
    sum_(n>=1) f_n t^n = t E'(t)/E(t) = Rt^3/E(t).

These are formal identities because E has constant term one. Multiplying
the inverse by E/E and extracting the relevant parity of t gives

    sum_(j>=0) phi_(2j+3) s^j
      = (1+Qs+Ds^2)/(1+Q^2s^2+R^2s^3+D^2s^4).

For independent q,u,d define P_j by the same series with (Q,R^2,D)
replaced by (q,u,d). Direct coefficient comparison gives P_0=1,
P_1=q, P_2=q^2+d, P_3=q^3+u,
P_4=q^4+q^2d+qu+d^2. In particular the two elements A_2 and A_4
used in the candidate really map to phi_7 and phi_11.

For iota:F2[q,u,d]->T, the three leading monomials in lexicographic
order x>y>z are x^2, x^4y^2, x^2yz. The exponent vectors have
integer determinant four. This is linear independence of exponent
vectors over Q, not a determinant computation in F2. Distinct source
monomials have distinct leading images; selecting the largest leading
image in a nonzero linear combination proves injectivity. No cancellation
by a smaller leading image is possible in a monomial order.

Each of x,y,z satisfies its quartic root equation
U^4+QU^2+RU+D=0. Squaring yields

    U^8+Q^2U^4+R^2U^2+D^2=0,

a monic equation over the embedded S=F2[q,u,d]. Since T=S[x,y,z],
T is integral over S. If iota(A) divides iota(B) for nonzero A,B in
S, its actual quotient belongs to T and equals B/A in Frac(S). It is
integral over S and lies in Frac(S); normality of the polynomial ring
therefore puts the quotient in S. The converse is substitution.

This proves the whole-element divisibility bridge. It makes no assertion
that every irreducible factor created in T descends to S. Neither q=0
nor another specialization was removed by this argument.

## 4. The two prime ideals and saturation

A_2=d+q^2 is prime since S/(A_2)=F2[q,u], and q is nonzero in this
quotient. Localize at q, set d=q^2, and write b=u/q^3. The quotient
is exactly F2[q,q^-1,b]. Substitution s=z/q yields

    F_7=(1+z+z^2)/(1+z^2+bz^3+z^4).

Its z^j coefficient is the image of q^-j P_j. Thus it vanishes
identically in the polynomial parameter b exactly when P_j lies in
(A_2) after localization. Because (A_2) is prime and q is outside it,
clearing a power of q proves that this is equivalent to A_2|P_j in S.

For A_4=qu+q^4+q^2d+d^2, its coefficients as a linear polynomial
in u have gcd one in F2[q,d]: the constant coefficient is d^2 modulo
q. It is primitive and irreducible over F2(q,d), hence irreducible by
Gauss's lemma and prime in S. It does not divide q. Localizing at q,
eliminating u, and setting b=d/q^2 gives

    d=q^2b,  u=q^3(1+b+b^2),
    F_11=(1+z+bz^2)/K,
    K=1+z^2+(1+b+b^2)z^3+b^2z^4.

Again the quotient is exactly F2[q,q^-1,b]; saturation of the prime
ideal at q proves A_4|P_j iff [z^j]F_11=0 in F2[b]. These are
identities in a transcendental parameter, not finite-field value tests.
In particular, there is no unchecked exceptional q=0 component.

## 5. Complete unrestricted reconstruction of C7

Set A(z)=1+z+z^2. Since the denominator of F_7 is A^2+bz^3,

    F_7=sum_(k>=0) b^k z^(3k) A^(-(2k+1)).

For fixed j only 0<=k<=floor(j/3) contributes, and the coefficient
of b^k has no contributions from a different k. Let
a_t=[z^t]A^-1, with a_t=0 for t<0. From
A^-1=(1+z)/(1+z^3), a_t equals one for nonnegative residues 0,1
modulo three, and zero for residue two.

Write j=3m+r. For r=0 or 1, the coefficient of b^m is the constant
or linear coefficient of A^(-(2m+1)), respectively; both equal one.
For r=2 that coefficient is binom(2m+1,2)=m modulo two, so m odd
is settled. At m=0 only k=0 contributes and a_2=0, so j=2 is a
zero coefficient polynomial.

The remaining case is positive even m. Write m=2^v s with v>=1
and s odd, and choose k=m-2^(v-1). This is a nonnegative allowed
index. Put t=j-3k=3*2^(v-1)+2. Then

    2k+1=1+2^v(2s-1),
    A^(-(2k+1))=A^-1 B(z^(2^v)),
    B=A^(-(2s-1)).

The first three coefficients of B are 1,1,0: the quadratic one is
binom(2s-1,2)=s-1 modulo two. The inequality t<3*2^v is strict
even when v=1, so later coefficients cannot contribute. The selected
coefficient is therefore a_t+a_(t-2^v). Now t is two modulo three,
while t-2^v=2^(v-1)+2 is nonnegative and is zero or one modulo
three. The result is one. This supplies an explicit nonzero coefficient
of b for every remaining index, with no search or bounded validation.

All j>=0 have been exhausted. The only zero [z^j]F_7 is j=2.
The prime-ideal equivalence and whole-element bridge give C7, including
both necessity and sufficiency at n=7.

## 6. The C11 section invariant is a conjunction

All series lie in F2[b][[z]], where each z coefficient has finite
polynomial b support. Define C_(r,t) by selecting the two exponent
parities and halving after subtracting r,t. The identity
K^2=K(z^2,b^2) gives

    C_(r,t)(N/K)=C_(r,t)(NK)/K.

Multiplication by a series in z^2,b^2 can be taken outside the section
with its arguments halved. This justifies the identity for the inverse
unit as well as for polynomials. For V=span{z^i b^h:0<=i<=3,
0<=h<=2}, NK has exponents at most seven and four. Each section
therefore stays in V; no negative exponent or missing boundary column
is possible.

If H=N/K, coefficient parity gives exactly

    [z^(2a+r)]H(b)
      = ([z^a]C_(r,0)H)(b^2)
        + b([z^a]C_(r,1)H)(b^2).

The summands have disjoint b parities. Their sum vanishes if and only
if both vanish. Extending this condition to every N in a state W and
then to their linear span proves the claimed equivalence with
T_r(W)=span{C_(r,t)(NK):N in W,t=0,1}. This is not an existential
choice of a parameter section. Iterating yields the candidate's invariant
for every a>=0 and every finite least-significant-first word. At a=0,
K(0,b)=1 makes acceptance exactly the disappearance of the z-constant
part of every numerator.

As a hand check independent of coding, for N_0=1+z+bz^2 I obtain

    N_0 K=1+z+(1+b)z^2+(b+b^2)z^3+z^4
             +(b+b^3)z^5+b^3z^6.

Its four sections have encodings L_00=73, L_01=1032, L_10=17,
L_11=200. They give exactly states 1 and 2 from the start state.
The independent program checks all remaining section data in the same
explicit polynomial model.

## 7. Independent exact certificate, all states and all edges

I copied the frozen static certificate to this review's own prefix after
checking its SHA256. The independent implementation uses frozensets of
exponent pairs for polynomials, symmetric difference for addition,
convolution with cancellation for multiplication, and direct parity
selection. The denominator and initial numerator are separately fixed in
my code from the displayed rational function; they are not trusted merely
because the certificate contains them. No constructor code, stored columns,
or check output was read before this implementation completed.

The only executed mathematical computation reconstructs a fixed finite
certificate. It is neither an n scan nor a search for larger automata.
The program checks all 48 operator columns, expands every advertised basis
into its entire vector set, proves those bases independent and the fifteen
subspaces distinct, and checks all thirty transitions by equality of full
vector sets. Each transition is also checked using basis images separately.

| State | Dimension | Number of vectors | 0 successor | 1 successor | Accept |
|---|---:|---:|---:|---:|---|
| 0 | 1 | 2 | 1 | 2 | no |
| 1 | 2 | 4 | 3 | 4 | no |
| 2 | 2 | 4 | 5 | 6 | no |
| 3 | 4 | 16 | 7 | 8 | no |
| 4 | 4 | 16 | 9 | 10 | no |
| 5 | 4 | 16 | 11 | 10 | no |
| 6 | 4 | 16 | 5 | 12 | no |
| 7 | 4 | 16 | 9 | 13 | no |
| 8 | 5 | 32 | 14 | 5 | yes |
| 9 | 6 | 64 | 9 | 10 | no |
| 10 | 6 | 64 | 9 | 10 | no |
| 11 | 5 | 32 | 9 | 10 | no |
| 12 | 5 | 32 | 5 | 12 | no |
| 13 | 5 | 32 | 9 | 10 | no |
| 14 | 5 | 32 | 14 | 5 | yes |

The complete columns, vectors and transition-image spaces are retained in
`divisor-review-1-check-output.json`. The output test checks every member
of each space, not only one designated vector. All fifteen states are
reachable in the given finite graph; witness words are retained. Reachability
is a finite graph check, not an attempt to discover states by numerator
enumeration. Closure of the listed graph and the general section invariant
are what establish the result for unrestricted word length.

For the partition S={0}, A={1}, B={3}, Z={8,14},
X={2,4,5,6,7,9,10,11,12,13}, the program verifies every member's
output and both successor classes. The resulting graph is

    S: 0->A, 1->X;  A: 0->B, 1->X;  B: 0->X, 1->Z;
    Z: 0->Z, 1->X;  X: 0->X, 1->X.

Only Z accepts. Any accepting word must first read 001 and then only
zeros; all such words accept. Thus the full finite-word language is
0010*, least significant bit first. Appending zero digits adds leading
zeros to the conventional representation and leaves its value four. The
canonical positive word ends in one, so only j=4 is accepted. The empty
word and every representation of zero reject. This proves C11 through
the already checked equivalences, without appealing to a finite range of j.

The child was launched under a ten-second external subprocess timeout.
PID 76805 completed and was reaped, return code zero, in
0.046486167004331946 seconds including launch. Incremental checkpoints
record the columns, every full subspace, all edges, quotient and completion;
stderr is empty. The exact command, Python 3.12.14, UTC timestamps and
cleanup policy are in the job records. Nothing was written to a constructor
output. The later inspection of its frozen checker found no contradictory
mathematical convention.

## 8. Absolute irreducibility, scalar extension, gcd and sums

The [McGuire thesis, Theorem 2.1', printed pages 19--20](https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf)
asserts absolute irreducibility when t>3 and t is three modulo four.
Its homogeneous and affine definitions match this packet. Both seven and
eleven meet the hypotheses; this is the attributed joint result, not a
new irreducibility proof here. I checked the full stated theorem and its
two-page proof, as well as the definitions on printed pages 15--16.

There is no hidden extra factor at infinity in passing back to homogeneous
coordinates. The coefficient of x^(t-1)y in f_t(x,y,0) is one for odd
t>1, and R(x,y,0)=xy(x+y) is nonzero. Hence phi_t(x,y,0) is nonzero,
so phi_t(x,y,1) retains total degree t-3 and z is not a factor. A
nontrivial homogeneous factorization would dehomogenize nontrivially:
a homogeneous positive-degree factor dehomogenizing to a constant would
be a scalar power of z, already excluded. This verifies the candidate's
rehomogenization step for the two applications.

Whole divisibility by a fixed base-field polynomial G is unchanged by
extension of scalars: T/(G) injects into its tensor product with any field
extension of F2. Thus the C7/C11 exclusions also hold over the algebraic
closure. Since the two fixed polynomials are absolutely irreducible and
have different degrees four and eight, they are coprime there. Any common
absolute factor with their product must be associated to one of them.
This proves the claimed gcd: phi_7 at n=7, phi_11 at n=11, and one
otherwise, with the indicated monic normalization. Repeated factors of
phi_n cause no issue because the fixed product contains each divisor once.

Finally (phi_t) is a homogeneous ideal. If a finite sum of terms of
distinct homogeneous degrees belongs to it, each homogeneous component
belongs to it, by decomposing any quotient into homogeneous components.
The nonzero phi_n for odd n>=3 have distinct degrees n-3. Applying
C7/C11 term by term proves the sum criterion, with the empty or all-zero
sum giving the vacuous condition. No cancellation between different degrees
can create a further divisibility. This argument uses no APN classification.

## 9. Adversarial checks and remaining limits

I specifically tried the potentially dangerous alternatives: a lost q=0
component, failure of descent after substituting invariants, cancellation
between b powers in the 2-adic witness, one omitted parameter section,
an unchecked subspace transition, reversed digit order, extra accepted
leading-zero words, a lost component at infinity, change of divisibility
under extension, and cancellation in a nonhomogeneous sum. The preceding
arguments resolve each concern without a new assumption.

The remaining limitations are explicit and not defects of these partial
statements. There can be other fixed factors and other reducible exponents;
the generic effective reduction does not enumerate all of them. The
literature check is bounded and supports no novelty inference. Published
irreducibility and automaticity results retain their original attribution.
No unreviewed structural restriction is needed. The full official B4(b)
classification remains unresolved by this packet.
