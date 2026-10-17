# Two fixed absolute divisors: exact exclusion criteria

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
`review_2021_reasoning_j15_r2`, in a constructive assignment separate
from its frozen reviews and earlier structural packet. Requested model
`gpt-6.1-sol`, reasoning `max`; effective-setting readback unavailable.
Two fresh independent nonconstructor audits are required. Only open
part (b) is investigated. No complete reducibility classification or
novelty is claimed.

## Proposed results and published context

For odd n>=3, in T=F2[x,y,z], put

    R=(x+y)(y+z)(z+x),
    phi_n=(x^n+y^n+z^n+(x+y+z)^n)/R.

The new proposed exact criteria are

    phi_7 divides phi_n   if and only if n=7,                 (C7)
    phi_11 divides phi_n  if and only if n=11.                (C11)

C7 has a direct unrestricted coefficient proof, with no finite graph or
mathematical computation. C11 uses a proved Frobenius-section invariant
and a fully checked closed 15-state certificate. The previous coordinator
probes suggested these singleton sets; their bounded coefficient scan is
not a premise. The graph used here has the same finite size, and there
is no larger search or index scan in this packet.

Janwa--McGuire--Wilson's published absolute-irreducibility theorem for
`t>3, t=3 mod 4` applies to both fixed divisors. It is stated and proved
in the original-author [McGuire thesis, Theorem 2.1', printed pp. 19--20](https://thesis.caltech.edu/4053/01/McGuire_gm_1995.pdf),
parallel to the 1995 joint paper. Using this attributed result, C7 and
C11 give, over F2 or its algebraic closure,

    gcd(phi_7*phi_11,phi_n) = phi_7,   n=7;
                             phi_11,  n=11;
                             1,       otherwise.             (G)

Gcds are normalized up to the unique nonzero scalar in F2. No assertion
that these are all possible degree-four/eight factors is made.

Primary literature already supplies broad methods relevant here:

- Delgado--Janwa [arXiv:1207.5528v1, Lemma 1, p. 5](https://arxiv.org/pdf/1207.5528v1)
  gives coprimality in selected exceptional-degree families, including
  distinct Welch degrees. It does not state either fixed-divisor
  criterion for arbitrary odd n.
- Their [arXiv:1602.02576v1, Theorem 10](https://arxiv.org/pdf/1602.02576v1)
  is a coprimality theorem with a divisor in a different designated
  exponent family. Its hypotheses do not include 7 or 11 as that fixed
  divisor. It is not used as a substitute for C7 or C11.
- Derksen's [Theorems 1.10 and 4.14](https://arxiv.org/pdf/math/0510583v1)
  makes zero sets of recurrences over finitely generated fields of
  positive characteristic effectively computable. Adamczewski--Bell's
  [Theorems 1.4--1.5](https://arxiv.org/pdf/1205.4091v1) generalize this
  to algebraic-series coefficients. These justify the general research
  method; the exact singleton sets still require identification.

The section immediately below records a useful attributed consequence
of the recurrence theorem. The remaining proof uses elementary
generating functions and explicit finite algebra and does not import
the proof of an automatic-set theorem. Férard's complete 2014/2017
texts remain unavailable in the previously documented normal public
routes; no claim of priority or exhaustive literature absence follows
from this bounded source audit.

## 1. Every fixed irreducible divisor has an effective zero-set problem

This is a deduction from **published Derksen**, not a new general
automaticity theorem. Let G be any nonconstant F2-irreducible polynomial
in T that does not divide R. Then K=Frac(T/(G)) is a finitely generated
field over F2. In K let a_1,a_2,a_3,a_4 be the images of
`x,y,z,x+y+z`, respectively. The sequence

    v(n)=sum_(i=1)^4 a_i^n,   n>=0,

satisfies the monic order-at-most-four recurrence with characteristic
polynomial `product_i(U+a_i)`. Repetitions or zero a_i cause no problem:
each individual power sequence satisfies the corresponding first-order
factor, and the product annihilates their sum. At n=0 use a_i^0=1,
including when a_i=0, consistent with polynomial evaluation.

For n>=3, primeness of (G) and G not dividing R give

    G | phi_n  iff G | R phi_n  iff v(n)=0 in K.             (A)

Derksen Theorem 1.10 applies to this explicitly finitely generated
characteristic-two field and recurrence. Consequently the set of such
n is an effectively computable 2-automatic set; restriction to odd
n>=3 preserves automaticity. This does not bound which G must occur
as n varies, and therefore does not classify all reducible phi_n.
It explains why a **fixed** candidate factor is a finite exact
zero-set problem rather than a conjecture to be extrapolated from tests.

## 2. The accepted generating identity and a universal descent lemma

The already reviewed whole-phi13 criterion establishes the following
tools. They are repeated to expose the exact hypotheses used for the
new divisors. Put

    Q=x^2+y^2+z^2+xy+yz+zx,    D=xyz(x+y+z).

For independent q,u,d let S=F2[q,u,d] and define P_j by

    sum_(j>=0) P_j s^j
       =(1+q s+d s^2)/(1+q^2 s^2+u s^3+d^2 s^4).            (1)

Then `phi_(2j+3)=P_j(Q,R^2,D)` for j>=0. One obtains this by taking
the odd power sums of the four entries x,y,z,x+y+z, whose elementary
symmetric functions are 0,Q,R,D. Equivalently their product
`E(t)=1+Qt^2+Rt^3+Dt^4` has `tE'(t)/E(t)=Rt^3/E(t)`.
All denominators have constant term one, so these are formal identities.
Coefficient extraction gives

    P_0=1, P_1=q, P_2=q^2+d, P_3=q^3+u,
    P_4=q^4+q^2d+qu+d^2.                                  (2)

The homomorphism iota:S->T taking `(q,u,d)` to `(Q,R^2,D)` is
injective, and T is integral over S. For injectivity, in lex order
x>y>z the leading exponent vectors are `(2,0,0),(4,2,0),(2,1,1)`.
Their determinant is the nonzero integer 4. Distinct products therefore
have distinct leading monomials; a largest leading term cannot cancel.
For integrality, each of x,y,z satisfies the monic equation

    U^8+Q^2 U^4+R^2 U^2+D^2=0,                             (3)

obtained by squaring its quartic root equation. Thus every element of
T is integral over S. The polynomial ring S is integrally closed.

It follows for **any** nonzero A,B in S that

    iota(A) | iota(B) in T  iff A | B in S.                 (4)

Indeed an actual quotient belongs to T and equals B/A in Frac(S).
Integrality and normality imply that quotient lies in S. The reverse
direction is substitution. This is divisibility by the whole fixed
element iota(A); it does not assert that every individual factor of
iota(B) comes from S. No specialization q=0 is discarded by (4).

## 3. Formal quotients for the two divisors

Write `A_2=d+q^2` and `A_4=qu+q^4+q^2d+d^2`. Their actual images
are phi_7 and phi_11 by (2).

A_2 is prime, being monic linear in d, and does not divide q. After
inverting q, imposing d=q^2 and putting b=u/q^3, the coefficient
of z^j in

    F_7(z,b)=(1+z+z^2)/(1+z^2+bz^3+z^4)                   (5)

is the image of q^(-j) P_j under s=z/q. The quotient is exactly
F2[q,q^(-1),b]. Primeness and A_2 not dividing q make localization
saturated, so

    A_2 | P_j  iff [z^j]F_7=0 in F2[b].                    (6)

For A_4, view it as a polynomial in u over F2[q,d]. Its coefficients
q and `q^4+q^2d+d^2` are coprime, since the latter is d^2 modulo q.
It is primitive and linear over F2(q,d), hence irreducible in S by
Gauss's lemma, and prime because S is a UFD. It does not divide q.
After inverting q, eliminate u and set b=d/q^2. Then

    d=q^2b, u=q^3(1+b+b^2),

and the normalized series is

    F_11(z,b)=(1+z+bz^2)/K(z,b),
    K=1+z^2+(1+b+b^2)z^3+b^2z^4.                          (7)

The localized quotient is again exactly F2[q,q^(-1),b]. Clearing a
power of q and using primality gives

    A_4 | P_j  iff [z^j]F_11=0 in F2[b].                   (8)

These are identities in a transcendental polynomial parameter. Testing
a few values of b, or using a noninjective specialized curve, would not
establish either equivalence.

## 4. An unrestricted coefficient witness for F_7

Let `A(z)=1+z+z^2`. In characteristic two the denominator in (5) is
`A(z)^2+bz^3`. Hence

    F_7=sum_(k>=0) b^k z^(3k) A(z)^(-(2k+1)).               (9)

For any fixed z-index only finitely many k contribute. Also

    A(z)^(-1)=(1+z)/(1+z^3).

Write a_t=[z^t]A^(-1), with a_t=0 for t<0. For t>=0,
`a_t=1` if t is 0 or 1 modulo 3 and `a_t=0` if t is 2 modulo 3.

Take j=3m+r, r in {0,1,2}. If r=0 or r=1, the coefficient of b^m
in [z^j]F_7 is respectively the constant or linear coefficient of
`A^(-(2m+1))`, hence one. If r=2, the same coefficient is

    [z^2](1+z)^(2m+1)/(1+z^3)^(2m+1)
       = binom(2m+1,2) = m modulo 2.                       (10)

Thus it is nonzero when m is odd. When m=0, j=2 and (9) has only
its k=0 contribution, namely a_2=0. This supplies the desired zero.

It remains to give a nonzero witness when m is positive and even.
Write m=2^v s, with v>=1 and s positive odd, and choose

    k=m-2^(v-1)>=0,
    t=j-3k=3*2^(v-1)+2,
    2k+1=1+2^v(2s-1).

Frobenius gives

    A^(-(2k+1))=A^(-1) B(z^(2^v)),
    B(z)=A(z)^(-(2s-1)).                                  (11)

The first three coefficients of B are `1,1,0`: its quadratic
coefficient is `binom(2s-1,2)=s-1=0 mod 2`. Since `t<3*2^v`,
only these three coefficients can contribute at degree t. Therefore

    [z^t]A^(-(2k+1))=a_t+a_(t-2^v).

Here `t=2 mod 3`, so a_t=0, while
`t-2^v=2^(v-1)+2` is 0 or 1 modulo 3 and is nonnegative. The
last displayed coefficient is exactly one. By (9), the coefficient of
b^k in [z^j]F_7 is consequently one.

This exhausts every nonnegative j. Thus

    [z^j]F_7=0 iff j=2.                                    (12)

Combining (4), (6) and n=2j+3 proves C7. The witness is explicit for
each index; no bounded range, graph closure, or computation is used.

## 5. Frobenius sections for F_11

Use the 12-dimensional F2 space V with monomials

    z^i b^h, 0<=i<=3, 0<=h<=2.

For r,t in {0,1}, C_(r,t) selects terms with z exponent r and b
exponent t modulo two and halves the two exponents after removing
r,t. Because K^2=K(z^2,b^2), formal multiplication gives

    C_(r,t)(N/K)=C_(r,t)(NK)/K.                             (13)

The operator `L_(r,t)N=C_(r,t)(NK)` preserves V: NK has z degree
at most seven and b degree at most four. There are no negative
parameter exponents. This is the same elementary general invariant
used in the accepted phi13 criterion, with a smaller numerator space.

For a subspace W of V define

    T_r(W)=span_F2{L_(r,t)N: N in W, t=0,1}.

The even and odd b supports of a coefficient are disjoint, so for a>=0

    [z^(2a+r)](N/K)=0 for every N in W
      iff [z^a](M/K)=0 for every M in T_r(W).               (14)

This is a conjunction of both parameter sections. Starting at
`W_0=span(1+z+bz^2)`, induction on a least-significant-first word
`r_0,...,r_(l-1)`, whose value is e, gives

    [z^(2^l a+e)]F_11=0
       iff [z^a](N/K)=0 for every N in the reached state.    (15)

A state accepts if every numerator has zero constant coefficient in z,
since K(0,b)=1. Taking a=0 in (15) proves that every finite word,
including words with appended leading zeros and the empty word,
decides precisely the coefficient indexed by its integer value.

## 6. A complete closed finite certificate, not a scan

Encode z^i b^h by bit `3i+h` of an integer. The following table gives
15 subspace bases, both transitions and the output. It is transcribed
from the existing exploratory graph, and the accompanying new checker
reconstructs every map from multiplication by the actual K in (7).
It does not trust exploratory operator columns or an index scan.

| State | Basis integers | 0 | 1 | Accept |
|---|---|---|---|---|
| 0 | 137 | 1 | 2 | no |
| 1 | 1032,73 | 3 | 4 | no |
| 2 | 200,17 | 5 | 6 | no |
| 3 | 1025,513,129,64 | 7 | 8 | no |
| 4 | 1024,137,72,25 | 9 | 10 | no |
| 5 | 1025,128,64,9 | 11 | 10 | no |
| 6 | 128,72,24,1 | 5 | 12 | no |
| 7 | 1024,512,137,72 | 9 | 13 | no |
| 8 | 1024,128,64,16,8 | 14 | 5 | yes |
| 9 | 1024,512,128,64,8,1 | 9 | 10 | no |
| 10 | 1024,128,64,16,8,1 | 9 | 10 | no |
| 11 | 1025,513,129,64,9 | 9 | 10 | no |
| 12 | 128,64,16,8,1 | 5 | 12 | no |
| 13 | 1025,129,64,17,9 | 9 | 10 | no |
| 14 | 1024,512,128,64,8 | 14 | 5 | yes |

The exact support checker uses the complete finite vector set of each
subspace, obtained by symmetric differences. For each of the 30 edges
it checks equality of the target vector set with the span of **all**
relevant section images (the two t sections for the selected r, applied
linearly to the whole state). More simply: it computes
T_r exactly and compares both complete subspaces. All 48 operator
columns and complete vector sets are retained in its output. The
constant-term test is the mask of bits 0,1,2.

The following quotient partition is checked for every member's output
and both successors:

    S={0}, A={1}, B={3}, Z={8,14},
    X={2,4,5,6,7,9,10,11,12,13}.

Its transitions are

| Class | 0 | 1 | Accept |
|---|---|---|---|
| S | A | X | no |
| A | B | X | no |
| B | X | Z | no |
| Z | Z | X | yes |
| X | X | X | no |

Every accepting word must first read `001` from S, then only zeros;
each such word accepts. Thus the exact finite-word language is
`0010*`, read least significant bit first. A canonical positive integer
word ends in one, so the only accepted index is j=4. The empty word
for j=0 rejects. Equation (15) gives

    [z^j]F_11=0 iff j=4.                                   (16)

Combining (4), (8) and n=2j+3 proves C11.

The single executed mathematical computation was the finite symbolic
certificate check, under an explicit five-second child timeout. PID
75264 completed with return code zero in about 0.049 seconds including
launch. This is an exact certificate for the displayed general invariant,
not finite empirical support for an infinite pattern. No breadth-first
search, multivariate factorization, coefficient scan or native CAS was
run in this assignment. Reproduction:

    .venv/bin/python problems/2024-B4/notes/divisor-reasoning-r2-phi11-run-v1.py

The harness and checker use create-new output files; copy to a new
version/prefix before rerunning so the frozen run is preserved.

## 7. Absolute factors, polynomial sums and scope limits

By the attributed JMW result, phi_7 and phi_11 are absolutely
irreducible of degrees four and eight. They are coprime.
The source's affine version is `g_t=phi_t(x,y,1)`. For t=7 or 11,
`f_t(x,y,0)` is nonzero because its x^(t-1)y coefficient is one, while
`R(x,y,0)=xy(x+y)` is nonzero. Hence phi_t(x,y,0) is nonzero,
dehomogenization retains degree t-3 and z is not a factor. Absolute
affine irreducibility therefore rehomogenizes without an extra component.
Over an extension field, divisibility of one fixed F2 polynomial by another
is unchanged: the quotient module T/(G) embeds into its scalar
extension as an F2 vector space. Thus C7 and C11 exclude division
even over Fbar_2. Absolute irreducibility then makes exclusion of the
whole divisor equivalent to absence of any common absolute component,
giving G.

There is a small useful extension to nonhomogeneous sums. Let I be
any finite set of odd integers at least three and a_n in F2. Then

    phi_7 | sum_(n in I) a_n phi_n
       iff every nonzero a_n has n=7,
    phi_11 | sum_(n in I) a_n phi_n
       iff every nonzero a_n has n=11.                       (17)

This includes the zero sum. A principal ideal generated by a homogeneous
polynomial is graded: decompose a quotient into homogeneous components.
As the nonzero phi_n have distinct degrees n-3, divisibility of the sum
forces divisibility of each included homogeneous component. Apply C7 or
C11. No APN-function classification is inferred from (17).

The official n=1 is outside the quotient/divisor statement; its zero
numerator cannot equal Rgh with two nonconstant factors in a domain.
For n=3, j=0 and phi_3=1, correctly rejected by both criteria. At n=7
or 11 the certified fixed divisor has unit cofactor, so these criteria
produce no new positive-degree cofactor or new reducible exponent.
The published absolute-irreducibility theorem independently excludes
those self cases from part (b).

For other odd n these results rule out only these two fixed absolute
components. The accepted phi13 criterion and its infinite reducible
family remain unchanged. All other possible components, their fields
and the full B4(b) classification remain unresolved by this packet.
The earlier structural T1--T4 packet is unverified context, not a
dependency. No preliminary construction was investigated or reproduced.

Review targets include the 2-adic witness in (11), coefficient bounds
in (9), saturation at q for both prime divisors, universal quotient
descent in (4), all 48 section columns and 30 subspace equalities,
conjunctive parameter sections, digit order, appended zeros, the
absolute-to-gcd source premise, and the zero-sum boundary in (17).
