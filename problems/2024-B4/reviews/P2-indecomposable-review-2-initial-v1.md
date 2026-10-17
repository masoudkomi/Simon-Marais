# Whole initially blind R2: DI1/DI2 composition indecomposability

2026-10-17 UTC. Reviewer: /root/review_2017_coarsening_r1.
Requested gpt-6.1-sol/max; effective-setting readback unavailable.
**Complete independent whole initial; coordinator reconciliation pending.**

Target: notes/coordinator-P2-indecomposable-return-v1.md,8550B,
SHA256 44a91d25943bb3d25f3c4a9c7fc2c2b7f498692889bf82b7dabbdb610b57c957.
Its complete three-record manifest, all eight obligations, embedded source/
failure discussion and accepted GK input were read. No new DI peer report,
finding or later coordinator disposition was read before this freeze.
No mathematical program, CAS, scan, sample, author rerun or certificate
was executed. Administrative hashing is not mathematical verification.

I authored older CP whole-divisor/composition background and previously
audited related KC/NV/CJ algebra. I did not construct DI1/DI2 or the new GK
recurrence. The separately accepted GK identity is a logical input, not
a claim of independent re-certification of my own older CP result.

## Verdict and exact scope

I find no substantive defect in DI1 or its DI2 application after
reconstructing the entire proof. All eight obligations pass in the
stated scope. The proof concerns indecomposability under POLYNOMIAL
COMPOSITION over an algebraic closure. It gives no ordinary multiplicative
irreducibility, no arbitrary-factor classification and no complete2024
B4(b) answer. The coordinator alone may accept after the other audit.

The independent reasoning follows in full, including the distinction
between derivative multiplicity and actual local order in characteristic2.

## 1. Official domain and logical dependency

The official open target is2024 B4(b), coefficientwise congruence of
integer polynomials, or equivalently reducibility of the nonzero
three-variable phi_n over F2 at odd n>=5, with the n=1 zero and n=3
unit boundaries treated separately. A statement about the auxiliary P2
is partial structural information only. It neither changes that field
nor solves it by proving an extension-field factorization.

The accepted GK identity needed here is exactly

    P2(T)=T^(q^2+1)+(T+1)^(q^2-q+1), q=2^k>=4.

The complete accepted GK body and acceptance metadata were read. Its
all-index recurrence and whole-divisor consequences are not used to
infer the new indecomposability. The root's prior CJ1 calculation is
related context, but every local fact used by DI2 is rederived below.

## 2. Reconstruct DI1 without tame or characteristic-zero assumptions

Let K be algebraically closed of characteristic p>0, and let f have
degree n>1 with p not dividing n. Assume distinct finite critical
points have distinct f-values and gcd(n,e_f(alpha))=1 at each such
point. Here e_f(alpha) is the actual order of f(T)-f(alpha) in K[T];
the polynomial is nonzero since f is nonconstant.

Suppose f=g(h), with a=deg g>1 and b=deg h>1. Nonconstant polynomial
degrees multiply over ANY field, so ab=n. Thus p divides neither a
nor b. In particular, the highest-degree term of g differentiates
nontrivially, and g' has degree a-1>=1. Algebraic closedness provides
a finite root beta of g'. No assumption that this root is simple is
needed.

Take any root alpha of h-beta. It exists because deg h=b>0 and K
is algebraically closed. The chain rule gives f'(alpha)=0, and
f(alpha)=g(beta). The same holds for EVERY distinct root of h-beta.
Injectivity of f on its critical points therefore forces h-beta
to have exactly one distinct root alpha0. Consequently, by
factorization over K,

    h(T)-beta=c(T-alpha0)^b, c nonzero.

This conclusion is about one fiber, not an assertion that h is
inseparable or that b is divisible by p.

Write the nonzero polynomial g(Y)-g(beta) as

    (Y-beta)^e V(Y), with e>=1 and V(beta) nonzero.

Substitution gives

    f(T)-f(alpha0)=c^e(T-alpha0)^(be) V(h(T)).

The last factor is a unit at alpha0, so the actual local order is
EXACTLY be. Thus b divides e_f(alpha0), as well as n=ab.
The gcd assumption implies b=1, a contradiction. No estimate on
a derivative multiplicity, branch-cycle formula, infinity
ramification or monodromy classification was used.

This also addresses a potential vacuity: p not dividing n implies
f' has degree n-1>=1, so finite critical points exist in K. The proof
only needs a critical point of the putative outer factor, which the
same prime-to-p argument ensures. Constant/degree0 factors are not
nontrivial decompositions; affine factors are the allowed endpoints.

## 3. All critical points of the exact P2

Work over K=algebraic closure of F2. Set

    F=T^(q^2+1)+(T+1)^(q^2-q+1),
    A=T^q+(T+1)^(q-1).

The second exponent is smaller than q^2+1 and both leading
coefficients are1, so deg F=q^2+1, an odd degree. Differentiation
uses odd exponents, and q-Frobenius yields

    F'=T^(q^2)+(T+1)^(q^2-q)=A^q.
    (T+1)A=T^(q+1)+1.

For the second identity expand (T+1)T^q+(T+1)^q and cancel the two
T^q terms. The numerator T^(q+1)+1 has derivative T^q, and none
of its roots is0. It has q+1 distinct roots. Its simple root1
is removed on division by T+1; A(1)=1, so no canceled root remains.

Thus A has precisely the q roots alpha in mu_(q+1) other than1.
They are simple roots of A, and precisely ALL roots of F' (each
with multiplicity q in F'). No additional finite critical point
can occur. For each alpha,

    alpha nonzero, alpha!=1,
    alpha^q=alpha^(-1), alpha^(q^2)=alpha.

Hence alpha lies in F_(q^2). The use of this finite field concerns
actual algebraic roots of polynomials; it is not replacement of a
polynomial identity by equality of functions on F2.

## 4. Exact critical VALUES

Put u=alpha+1. Both alpha and u are nonzero. Frobenius gives

    u^q=alpha^q+1=u/alpha,
    u^(q^2)=u,
    u^(q-1)=alpha^(-1).

The exponent subtraction in the second term of F is legitimate
because u is nonzero:

    u^(q^2-q+1)=u^(q^2)/u^(q-1)=alpha*u.

The first term is alpha^(q^2+1)=alpha^2. Therefore

    F(alpha)=alpha^2+alpha*(alpha+1)=alpha.

F fixes ALL its finite critical points. Since those points are
distinct, so are their critical values. This establishes the
first substantive hypothesis of DI1 for this exact F.

## 5. Exact local order, not derivative multiplicity plus one

In characteristic2, if m has binary support S, then

    (u+Z)^m=product_(i in S)(u^(2^i)+Z^(2^i)).

For m_1=q^2+1 the support is{0,2k}; its positive expansion
exponents below q^2 are only1. For m_2=q^2-q+1 the support
is{0,k,k+1,...,2k-1}; the only positive exponent below q
is1. Consequently the two summands of F(alpha+Z) have no
terms of degrees2,...,q-1.

Their combined linear coefficient is F'(alpha)=0. At exponent q,
the first summand has coefficient0 because its next bit is2k.
The second has a unique bit-subset contribution: take the
Z^(2^k) factor and the constant from every other factor. Its
coefficient is

    u^(m_2-q)=u^(q^2-2q+1)=u^((q-1)^2), nonzero.

Subtracting the constant F(alpha)=alpha gives

    F(alpha+Z)-alpha
        =u^((q-1)^2)Z^q+terms of higher degree.

Thus e_F(alpha)=q EXACTLY. The derivative has multiplicity q
at alpha; in this characteristic that does not imply a local
order q+1. The submitted proof correctly computes q instead.

At q=4 the supports are{0,4} and{0,2,3}; the nonzero coefficient
at Z^4 is u^9. No omitted low exponent appears. Uniformly for
all k>=2 the same bit-subset argument applies. The stated
q=2 omission is not a hidden failure: the same calculation
would have to be checked separately if that endpoint were
claimed, but DI2 deliberately needs only q>=4.

## 6. Apply DI1, including composite degrees and extensions

The degree n=q^2+1 is odd, so it is prime to characteristic2.
For every critical alpha, e_F(alpha)=q and gcd(q^2+1,q)=1.
All DI1 hypotheses therefore hold and F is indecomposable
over the algebraic closure of F2.

No primality of n was used. At q=8 the degree is65; the same
fiber/local-order argument applies to every factorization of
65 into two proposed component degrees, without enumerating
or factoring candidate polynomials.

For completeness, an arbitrary coefficient extension E/F2 need
not be a subfield of the algebraic closure of F2 when E has
transcendental elements. The conclusion over such E is still
valid: apply DI1 directly over an algebraic closure of E.
The roots of A are already the same q roots from F_(q^2);
there are no additional ones, by its degree and splitting.
The critical values and local-order calculations above remain
unchanged. Thus DI1 again forbids a decomposition, and hence
one over E. This reconstructs the candidate's “any extension”
sentence without assuming every extension is algebraic.

Polynomial decomposition is the only conclusion. It is
consistent with an identity P_s=H(P2), in which P2 is an
indecomposable INNER factor of another polynomial. It is
also logically distinct from ordinary reducibility of P2
or of the original homogeneous phi_n.

## 7. Primary source and attribution checks

The actual [Kreso primary paper](https://nyjm.albany.edu/j/2015/21-45p.pdf),
§2, printed990–991, was read through Lemma2.2, both corollaries
and the Morse definition/theorem context; its abstract/introduction
and the §3 characteristic-zero boundary were also read. The
critical outer-fiber method is properly treated as precedent,
not an applied black-box theorem or a priority claim.

The small-gcd corollaries are insufficient here: at a critical
value alpha the common factor of F-alpha and F' has degree q.
The Morse theorem requires simple derivative roots; F'=A^q
fails that hypothesis. No later characteristic-zero trinomial
or lacunarity theorem is being imported. DI1 itself is proved
by the elementary fiber factorization in section2 above.

A requested screenshot had a cache-miss error for one source
page; the actual usable read was the primary web text. No
binary download, invented PDF hash or unviewed image check
is claimed. Source limitations are explicit.

## 8. Final initial disposition

All eight author obligations were independently reconstructed
in full; the companion ledger splits them into18 checks.
No substantive objection or required repair was found.
This is a scoped pass recommendation to the coordinator,
not promotion and not an absolute-certainty statement.
The whole report, ledger, sources and integrity record were
frozen before any new DI peer conclusion was read.

