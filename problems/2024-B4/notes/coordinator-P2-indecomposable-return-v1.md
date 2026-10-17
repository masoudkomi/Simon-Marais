# Distinct critical values and absolute indecomposability of P2

2026-10-17 UTC. **Candidate proof - unverified.** Constructor: coordinator root.
This is a new complete mathematical submission, separate from accepted CJ1.
It requires TWO OTHER initially blind whole audits before acceptance. No
mathematical program, CAS, enumeration, numerical sample or author rerun was
used. It gives no complete answer to the official B4(b) factorization problem.

## DI1. An elementary criterion over an algebraically closed field

Let K be algebraically closed of characteristic p>0. Let f in K[T] have
degree n>1 with p not dividing n. For each finite critical point alpha,
write e_f(alpha) for the order of the nonzero polynomial
f(T)-f(alpha) at T=alpha. Suppose that:

1. Distinct finite critical points have distinct f-values.
2. gcd(n,e_f(alpha))=1 at every finite critical point.

Then f is indecomposable over K: an identity f=g(h(T)), g,h in K[T],
forces deg(g)=1 or deg(h)=1.

Proof. Suppose a=deg(g)>1 and b=deg(h)>1. Degrees of nonconstant
polynomials multiply over any field, so ab=n and p divides neither a nor b.
In particular g' has degree a-1>=1: its leading coefficient is the
nonzero leading coefficient of g multiplied by the nonzero scalar a.
It therefore has a root beta in K.

For EVERY root alpha of h(T)-beta, the chain rule gives f'(alpha)=0,
and f(alpha)=g(beta). The polynomial h-beta has degree b and at least
one root. The first hypothesis implies that it has only ONE DISTINCT
root, say alpha0. Consequently h(T)-beta=c(T-alpha0)^b with c!=0.
This is an equality of polynomials over the algebraically closed field;
it does not assert that h is inseparable or that b is divisible by p.

Factor g(Y)-g(beta)=(Y-beta)^e V(Y), V(beta)!=0. This polynomial is
nonzero because g is nonconstant, so e is a finite positive integer.
Substituting h gives

    f(T)-f(alpha0)=c^e (T-alpha0)^(be) V(h(T)).

Since V(h(alpha0))=V(beta)!=0, its EXACT vanishing order is be. Thus
b divides e_f(alpha0) and also n. The second hypothesis forces b=1,
contrary to the proposed decomposition. This proves DI1.

This proof includes inseparable local behavior and arbitrary coefficient
extensions. It uses no tame ramification formula, inverse derivative,
monodromy classification or characteristic-zero decomposition theorem.
The assumptions n prime to p and injective critical values are essential
to the actual argument: they provide a critical point of g and collapse
its entire h-fiber to one point. They are not omitted.

## DI2. Apply the criterion to the exact GK polynomial

Fix q=2^k>=4 and set

    F(T)=P2(T)=T^(q^2+1)+(T+1)^(q^2-q+1),
    A(T)=T^q+(T+1)^(q-1).

The exact identity for P2 is the accepted GK input; the local calculations
below are fully rederived rather than assumed from the older CJ1 note.
Its degree is n=q^2+1 because the second exponent is strictly smaller;
n is odd. Work throughout over the algebraic closure of F2.

Direct differentiation and Frobenius give

    F'(T)=T^(q^2)+(T+1)^(q^2-q)=A(T)^q,
    (T+1)A(T)=T^(q+1)+1.

The polynomial T^(q+1)+1 has q+1 distinct nonzero roots, since its
derivative T^q does not vanish at a root. Its root1 is simple and is
removed by division by T+1; A(1)=1. Hence A has exactly q distinct
roots alpha in mu_(q+1) other than1. They are precisely ALL finite
critical points of F. Each lies in F_(q^2), since q+1 divides q^2-1;
it satisfies alpha^q=alpha^(-1). In particular alpha and alpha+1 are
nonzero.

Put u=alpha+1. Then u^q=u/alpha and u^(q^2)=u. Therefore

    u^(q-1)=alpha^(-1),
    u^(q^2-q+1)=u/u^(q-1)=alpha*u,
    F(alpha)=alpha^2+alpha*u=alpha.

Thus all finite critical values are distinct: F acts as the identity
on its q distinct critical points. There are no additional finite
critical points missing from the calculation, by F'=A^q.

It remains essential to compute the EXACT local order; the derivative
multiplicity q does not justify adding one in this characteristic.
The binary support of q^2+1 is {0,2k}, and that of q^2-q+1 is
{0,k,k+1,...,2k-1}. The identity

    (u+Z)^m=product_(i: bit_i(m)=1)(u^(2^i)+Z^(2^i))

shows that neither summand in F(alpha+Z) has any exponent between2
and q-1. The linear coefficient is F'(alpha)=0. At exponent q the
first summand contributes nothing, whereas the second contributes
EXACTLY u^(q^2-2q+1), which is nonzero. Its constant term is alpha.
Consequently

    F(alpha+Z)-alpha
       =u^(q^2-2q+1) Z^q + terms of larger exponent,
    e_F(alpha)=q.

Since gcd(q^2+1,q)=1, all hypotheses of DI1 hold for F. We conclude:

**Proposed DI2. For every q=2^k>=4, the auxiliary polynomial P2 is
indecomposable over the algebraic closure of F2. In particular no
nontrivial polynomial decomposition exists over F2 or any extension.**

The argument is uniform in k and includes q=4. It does not rely on
q^2+1 being prime. For example the proof still addresses the composite
degree65 when q=8 without factoring that degree or enumerating fields.
No assertion for q=2 is needed for the stated GK scope.

## Exact scope and limitations

Indecomposable here means under POLYNOMIAL COMPOSITION. It does not mean
irreducible under ordinary polynomial multiplication, nor absolute
irreducibility of the original three-variable phi_n. In particular it
does NOT exclude P_s=H(P2): in such an identity P2 would be the inner
indecomposable factor, not a decomposition of P2 itself. No new criterion
for which P_s have that identity is claimed. The accepted necessary CJ1
congruence, whole Kasami-divisor criterion and arbitrary-factor gap remain
unchanged. No group classification or full annual answer follows here.

## Literature search, actual reads and failed routes

The primary search for distinct-critical-value decomposition criteria
found Dijana Kreso, *On common values of lacunary polynomials at integer
points*, New York J. Math.21(2015),987-1001:
[primary paper](https://nyjm.albany.edu/j/2015/21-45p.pdf).
Actual fresh reads: abstract/introduction context and COMPLETE section2,
printed990-991, including Lemma2.2, its proof, Corollaries2.3-2.4 and the
Morse definition/Theorem2.6 discussion. The critical outer-fiber method
is standard and is attributed to this source as related methodology.
No priority claim is made for DI1 or DI2. No paper download or licence
claim is needed for this web-only read.

The stated small-gcd corollaries do not directly give DI2: here the
critical-fiber gcd has degree q, not1 or2. F' has q-multiple roots,
so its critical points are not simple and the displayed Morse theorem
is not applicable. Sections3-4 use characteristic-zero hypotheses in
other results and are not imported. No symmetric-monodromy claim is
made. DI1 is proved above by the same elementary fiber strategy plus
the additional coprime local-order observation, independently of any
unread decomposition theorem. Search hits on MCM/Dickson polynomials
did not supply an identity with this exact P2 and are not premises.

The earlier attempt to strengthen only the high-order CJ1 congruence
would still leave high-degree remainder multiples for j>=3. DI2 uses
the simpler distinct-critical-value information for a different question;
it does not close that previous gap. No unsupported rational-function
decomposition, positive-characteristic Ritt theorem or arbitrary-factor
classification has been added to the conclusion.

## Whole review obligations

1. The degree multiplication/prime-to-characteristic hypothesis ensures
   g' has a finite root for every proposed nontrivial decomposition.
2. Chain rule applies to ALL roots of h-beta; distinct critical values
   force a SINGLE distinct root, without assuming separability of h-beta.
3. The exact factorization and unit substitution prove b divides the
   ACTUAL local order, and the gcd contradiction is valid.
4. F has degree q^2+1 and derivative A^q, with exactly the stated q
   simple roots of A and no omitted finite critical points.
5. All critical roots lie in F_(q^2), have the stated u-identities and
   are fixed by F, giving injective critical values.
6. The binary product gives EXACT local order q, including q4 and the
   cancellation of the linear term; no tame shortcut is used.
7. DI1 applies over the algebraic closure and therefore to all coefficient
   subfields/extensions; composite n does not invalidate the reasoning.
8. Composition indecomposability is not ordinary irreducibility, does not
   prohibit an inner P2 factor in other polynomials, and supplies no full
   annual answer or novelty. Primary source hypotheses are not enlarged.
