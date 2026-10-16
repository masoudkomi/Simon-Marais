# Exact fixed-factor criterion from a Cartier automaton, v1

**Candidate proof - unverified.** Constructed 2026-10-16. This is a
partial result for 2024 B4(b), not a complete reducibility classification.
Two fresh independent adversarial reviewer agents, including a whole
argument reconstruction, are required before coordinator promotion.
The two implementations below were written by the same proof author;
they are not independent reviewer agents.

Requested owner settings: gpt-6.1-sol, max reasoning. No verified
effective-backend setting readback is available. Coordinator reports
account-wide weekly usage at 4% at launch and retains telemetry ownership.

The official domain and target are in `../statement.md`: positive odd n,
coefficientwise equality over F2, and a product of two nonconstant
polynomials. This note concerns only one fixed factor and makes no claim
that every factorization has that factor. It does not reproduce the
preliminary part (a). The frozen `../proofs/fixed-factor-family-v1.md`
has not been edited.

## Proposed theorem

Work in T=F2[x,y,z]. For odd n>=3, set

    f_n = x^n+y^n+z^n+(x+y+z)^n,
    R = (x+y)(y+z)(z+x),       phi_n = f_n/R.

The quotient exists by the generating identity proved below. The claim is

    phi_13 divides phi_n in T
       if and only if
    n = (64*16^m+1)/5 for an integer m>=0.                    (T)

The right side starts 13,205,3277,52429,838861. For m>=1 this gives
two nonconstant factors of phi_n, with degrees 10 and n-13, hence
solutions to B4(b) for those exponents. For m=0 the displayed cofactor
is 1, so this fixed-factor statement alone does not decide B4(b) at
n=13. Absence of phi_13 for other n makes no assertion about other
possible factors.

This is a self-contained candidate reconstruction; novelty is not
established. The frozen family proof records prior work of
Hernando--McGuire at n=205 and Férard's announced fixed-factor criterion.
Férard's full theorem has not been inspected, so no comparison of exact
criteria or priority is claimed. The coordinator's Derksen preprint
lead motivated automata, but no external automaton theorem is used.

## 1. Generating functions and the formal divisor

Put

    Q = x^2+y^2+z^2+xy+yz+zx,       D = xyz(x+y+z).

The elementary symmetric polynomials of the list x,y,z,w=x+y+z,
with multiplicity, are 0,Q,R,D. Thus

    E(t) = product_(a in {x,y,z,w})(1+a*t)
         = 1+Q*t^2+R*t^3+D*t^4.

Every denominator here has constant term 1 and is a unit as a formal
power series. Formal differentiation, the product rule, and geometric
expansion give

    sum_(n>=1) f_n*t^n = t*E'(t)/E(t) = R*t^3/E(t).

It follows that R divides f_n for n>=3. Taking the even t-degree
part of 1/E=E/E^2 and writing s=t^2 gives

    sum_(j>=0) phi_(2j+3)*s^j
       = (1+Q*s+D*s^2)/(1+Q^2*s^2+R^2*s^3+D^2*s^4).           (1)

Introduce independent variables q,u,d and S=F2[q,u,d]. Define P_j by

    sum_(j>=0) P_j*s^j
       = (1+q*s+d*s^2)/(1+q^2*s^2+u*s^3+d^2*s^4).             (2)

Then phi_(2j+3)=P_j(Q,R^2,D). Coefficient extraction at j=5 gives

    P_5 = q^5+q*d^2+u*d =: A.                                (3)

In particular A(Q,R^2,D)=phi_13. All P_j are homogeneous of weight 2j
for weight(q,u,d)=(2,6,4), although the divisibility criterion below
does not need homogeneity.

Localize S at q and d, obtaining U=S[q^-1,d^-1]. Since d is a unit,

    U/(A) = F2[q,q^-1,d,d^-1],        u=q^5/d+q*d.

Writing b=d/q^2 identifies this with F2[q,q^-1,b,b^-1], where
d=q^2*b and u=q^3*(b+b^-1). Substituting s=z/q in (2) gives

    F(z,b) = P(z,b)/K(z,b),
    P(z,b) = 1+z+b*z^2,
    K(z,b) = 1+z^2+(b+b^-1)*z^3+b^2*z^4.                    (4)

Here the coefficient of z^j is the image of q^-j*P_j. It lies in
Lambda=F2[b,b^-1]. Every assertion that it vanishes means an identity
in the Laurent-polynomial indeterminate b, not evaluation at finitely
many field values.

For completeness, A is prime in S. As a polynomial in u over
F2[q,d], its coefficients d and q*(q^4+d^2) are coprime: a common
irreducible factor would divide both d and q^5. Thus A is primitive,
and its degree one over F2(q,d) makes it irreducible there and in S
by Gauss's lemma. S is a UFD, so A is prime. Its u-degree shows it
divides neither q nor d. Consequently

    A*U intersect S = A*S,

by clearing a power of q*d and using primality. Since the displayed
quotient U/(A) is an isomorphism and q is a unit, we have the exact
equivalence

    A divides P_j in S  iff  [z^j]F(z,b)=0 in Lambda.          (5)

## 2. Four Cartier maps on a 16-dimensional space

For r,t in {0,1}, define the F2-linear Laurent-series operator

    C_(r,t)(sum_(i>=0,h in Z) a_(i,h)*z^i*b^h)
       = sum_(a>=0,c in Z) a_(2a+r,2c+t)*z^a*b^c.

Each coefficient of z is a finite Laurent polynomial, so all sums
used in defining these operators are legitimate. For negative h,
parity is its residue 0 or 1 modulo 2 and c=(h-t)/2; there is no
rounding convention. In characteristic 2, K(z,b)^2=K(z^2,b^2).
Coefficient convolution therefore gives

    C_(r,t)(N/K) = C_(r,t)(N*K)/K.                           (6)

Indeed N/K=N*K/K(z^2,b^2), and a factor involving only z^2,b^2
can be removed from a Cartier operation with its arguments halved.
This also applies to the inverse of K, a unit formal series.

Let V be the F2-space with monomial basis

    z^i*b^h,       0<=i<=3,  -1<=h<=2.                       (7)

It has dimension 16. Multiplying any N in V by K gives exponents
0<=i<=7 and -2<=h<=4. Selecting either parity and halving gives
0<=i<=3 and -1<=h<=2 again. Thus the four linear maps

    L_(r,t): V -> V,       N |-> C_(r,t)(N*K)                 (8)

are defined on V. The initial numerator P belongs to V.

The important point is that a zero Laurent coefficient requires BOTH
b-parity sections to vanish. If h_i(b)=[z^i]H(z,b), then

    h_(2a+r)(b)
       = ([z^a]C_(r,0)H)(b^2)
           + b*([z^a]C_(r,1)H)(b^2).

The even and odd Laurent supports are disjoint, so the left side is
zero if and only if both coefficients on the right are zero.

## 3. Subspace automaton and its invariant

States are F2-linear subspaces W of V. Define

    W_start = span_F2(P),
    T_r(W) = span_F2{ L_(r,t)(N): N in W, t=0,1 }.

Because L_(r,t) is linear, a basis of W suffices to compute T_r(W).
A state is accepting exactly when every N in W has zero z^0
coefficient. This too can be checked on a basis. Since K(0,b)=1,
it is equivalent to [z^0](N/K)=0 for every N in W.

By the parity decomposition and (6), for every a>=0,

    [z^(2a+r)](N/K)=0 for every N in W
       iff
    [z^a](M/K)=0 for every M in T_r(W).                      (9)

Thus after reading bits r_0,...,r_(k-1) from least significant to
most significant, with ell=sum_(h<k)r_h*2^h, the reached state W
satisfies, for every a>=0,

    [z^(2^k*a+ell)]F=0
       iff
    [z^a](N/K)=0 for every N in W.                           (10)

This follows by induction using (9), starting with span(P). Setting
a=0 proves that acceptance after a finite bit word decides precisely
the zero coefficient at the integer encoded by that word. The empty
word encodes j=0 and is rejected. Appending zeros to a word means
adding leading zeros to its usual binary representation; (10) remains
valid for these words also.

No infinite-state or effectiveness theorem is being imported. V is
finite, so it has finitely many subspaces. More importantly, the
reachable graph below is explicitly closed after 48 states, which is
verified by a finite exact certificate.

## 4. Complete finite certificate and quotient

The machine-readable certificate is
`../computations/zero-automaton-v1-graph.json`. Its 16 coordinate bits
are ordered by increasing i=0,1,2,3 and, within each i, increasing
h=-1,0,1,2. A numerator sum is encoded by the nonnegative integer
whose corresponding bits are 1. The four maps L_(r,t) are recorded
by their 16 integer columns in this same basis. Each of the 48
reachable subspaces has a reduced binary basis, two transition
targets, and an acceptance output. A readable table is supplied in
`zero-automaton-certificate-v1.md`.

`zero-automaton-build-v1.py` builds each operator by multiplying each
basis monomial by the five terms of K, taking the specified parities,
and halving. It uses exact XOR Gaussian elimination to canonically
identify subspaces. Its bounded BFS was allowed at most 20000 states
and 40 internal seconds, under a 45-second child timeout, and closed
at 48 states with all 96 outgoing transitions present. Dimensions
are 1 through 6; exactly six subspaces accept. No cap or timeout was
reached.

`zero-automaton-verify-v1.py` does not import the constructor. It
rebuilds all 64 matrix columns by ordinary Laurent-polynomial support
multiplication and section. It represents a subspace as the COMPLETE
finite set of its vectors, using repeated symmetric differences,
without Gaussian elimination. It independently breadth-first builds
the 48 full-vector states and all 96 transitions, checks agreement
with the certificate, checks every acceptance flag, and confirms all
states are distinct. It also checks the reduced-basis coordinate
conditions directly. Hence the finite check does not assume that a
Gaussian-elimination implementation canonically identifies spaces.

The following eight classes partition all 48 subspace states. Entries
in the next two columns are classes, not original BFS state numbers.
Every member of a class has the displayed acceptance output and its
two successors lie in the displayed classes; these are finite exact
algebraic checks in the certificate. Moore refinement finds the same
partition, but minimality is not needed for the argument.

| Class | 0 successor | 1 successor | Accept? | Original BFS state members |
|---|---:|---:|---|---|
| X | X | X | no | 1,3,4,6,7,8,9,10,11,13,14,15,16,17,18,19,20,22,23,24,25,26,27,28,29,30,32,33,34,37,38,40,41,42,44,45,46,47 |
| S | X | A | no | 0 |
| A | B | X | no | 2 |
| B | X | C | no | 5,36 |
| Z | Z | X | yes | 35,39,43 |
| C | D | X | yes | 12 |
| D | E | X | yes | 21 |
| E | Z | B | yes | 31 |

The initial class is S. This table immediately gives the accepted
least-significant-first language

    101(0011)*0*.                                            (11)

To see both inclusions without guessing a pattern, a path that avoids
X must start S --1--> A --0--> B --1--> C. From C, a nonzero bit
immediately reaches X. Z accepts any number of zeros and sends any
1 to X. The only excursion from C that can read a future 1 and
return to acceptance is

    C --0--> D --0--> E --1--> B --1--> C.

If no future 1 is read, any number of zero steps from C is accepting
(C,D,E,Z,...). These alternatives prove (11) by induction on the
number of future 1 bits. This argument concerns all finite words,
not a bounded coefficient scan.

A positive integer's canonical least-significant-first binary word
ends in 1. Thus its accepted words are precisely

    101(0011)^m,       m>=0.

The initial `101` represents 5. Each subsequent `0011` block has
value 12 in its four local positions and is shifted by 3+4h bits,
so the represented integer is

    j_m = 5 + sum_(h=0 to m-1) 12*2^(3+4h)
        = 5+96*(16^m-1)/15
        = (32*16^m-7)/5.                                    (12)

The empty sum at m=0 is allowed. Combining (10)-(12) and (5)
proves the formal fixed-factor criterion

    A divides P_j in S  iff  j=j_m for some m>=0.             (13)

The coefficient checks through j=65535 in the verifier are explicitly
finite evidence only. The unrestricted conclusion comes from the
general Cartier invariant and the CLOSED finite graph, not from
extrapolating those coefficient checks.

## 5. Actual divisibility is equivalent to formal divisibility

Consider the homomorphism

    iota: S -> T,        (q,u,d) |-> (Q,R^2,D).

Use lexicographic monomial order x>y>z. Direct expansion gives the
leading monomials

    LM(Q)=x^2,        LM(R^2)=x^4*y^2,        LM(D)=x^2*y*z.

Their exponent vectors (2,0,0),(4,2,0),(2,1,1) have determinant 4
over Z, hence are linearly independent over Q. This determinant is
not being reduced modulo 2: it concerns equality of integer exponent
vectors. Products have the product of their leading monomials in a
monomial order. Therefore distinct monomials q^a*u^b*d^c have
distinct leading monomials after substitution. In a nonzero finite
linear combination of their images, the largest such leading
monomial cannot be cancelled by another summand: summands with lower
leading monomial have all their monomials lower. Thus iota is
injective. Identify S and its fraction field with their images.

Each of x,y,z is a root of

    X^4+Q*X^2+R*X+D,

since this polynomial is product_(a in {x,y,z,x+y+z})(X+a).
Squaring the equality at each root gives

    X^8+Q^2*X^4+R^2*X^2+D^2 = 0.                            (14)

This is a MONIC polynomial with coefficients in the image of S.
Thus x,y,z are integral over S. Since T=S[x,y,z], T is integral
over S. One may see the required finiteness directly: (14) reduces
every monomial to an S-linear combination of x^a*y^b*z^c with
0<=a,b,c<8, so the determinant trick gives a monic equation over S
for every element of T. No division by a specialized x,y,z,Q,D
is made here.

The polynomial ring S over a field is a UFD and hence integrally
closed in Frac(S). Suppose the ACTUAL divisibility phi_13|phi_n
holds for n=2j+3>=3. Its quotient H lies in T. By (1)-(3), and
injectivity of iota, the same quotient equals P_j/A in Frac(S).
Because H belongs to T it is integral over S, and because it
belongs to Frac(S), integral closedness implies H belongs to S.
Consequently P_j=A*H in S. The converse is immediate by substitution.
We have proved the exact equivalence

    phi_13 divides phi_(2j+3) in T
       iff A divides P_j in S.                              (15)

In particular, extra factors arising after extending from S to T
cannot produce an additional divisibility by the WHOLE fixed element
phi_13. The argument does not assert that all irreducible factors
of P_j(Q,R^2,D) lie in S.

Combining (13), (15), and n=2j+3 yields (T), because
2j_m+3=(64*16^m+1)/5. This number is an odd integer: 16=1 modulo
5 and 64=-1 modulo 5.

For the B4(b) consequence, f_n is nonzero for odd n>1: its mixed
coefficient at x^(n-1)*y is n=1 in F2. Hence phi_n is nonzero,
homogeneous of degree n-3. The divisor phi_13 has degree 10. Its
cofactor at n=n_m has degree n_m-13, positive exactly for m>=1.
Lifting the two F2 factors coefficientwise to integer polynomials
g,h gives the requested congruence for those m. This is only a
subset of the exponents that might satisfy the full open question.

## Reproduction, verification status and remaining obligations

From the repository root:

```sh
.venv/bin/python -u problems/2024-B4/computations/zero-automaton-run-v1.py
.venv/bin/python -u problems/2024-B4/computations/zero-automaton-verify-run-v1.py
.venv/bin/python problems/2024-B4/computations/zero-automaton-render-v1.py
```

Both jobs used Python 3.12.14 and the standard library only. Each
harness records its exact command, child PID, timeout, status, output
paths, and hashes, terminating only its own identified child if
necessary. The graph job closed in under a millisecond inside the
child (about 0.04 seconds including launch), and the verifier completed
in about 0.54 seconds including launch. Exact values and PIDs are
retained in the job JSONs, not rounded into the theorem.

The second implementation additionally checks the three actual
leading monomials and all three squared-quartic identities by direct
support multiplication in F2[x,y,z]. These finite identities support
the separate general injectivity and integrality argument; computation
alone does not establish integral closedness or quotient descent.

The proof still requires two fresh independent adversarial agents.
They should audit the official scope, parity decomposition for Laurent
exponents, formal-series convolution, both numerator degree bounds,
the state invariant and digit order, closure and every finite transition,
the quotient partition and its language, localization saturation,
leading-monomial injectivity over integer exponents, the monic
integrality relations, and the use of normality in (15). The initial
reports must be completed without seeing one another's conclusions.
No result in this note has been promoted to independently reviewed.
