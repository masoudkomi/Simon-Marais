# Reviewed signed power-gap reductions

**Proved, independently reviewed partial results**, 2026-10-17 UTC.
The coordinator accepts PG1--PG3 as elementary signed results, and PG4
as an explicitly attributed corollary importing Bennett--Levin's
finished signed Proposition1/Theorem1. Both fresh initially blind
nonconstructor whole audits reconstructed every new inference and
checked all published-input hypotheses and known exceptions. Root read
both full reports, complete issue ledgers and source-check records.
No substantive objection or author repair remains.

PG1 excludes G_s(t^q) being a q-th power for q>=2,2<=s<=q+1,|t|>=2.
PG2 excludes G_(qs)(x)=y^q for odd prime q,2<=s<=q+1,|x|>=2.
PG3 gives x=1 mod q and q|a as necessary for term count q^a,a>=2.
PG4 excludes all such composite prime-power diagonal term counts
using the explicitly cited signed published restrictions. The entire
external Runge/cyclotomic proof was not reconstructed by this project;
PG4 retains that attributed dependency. The positive-base overlap
is acknowledged and supplies no negative-base premise.

The official degree is always n=m-1. Prime diagonal m=q, general
term counts, the full integer classification and novelty remain
unresolved. Class-group/finite-range leads are not accepted premises.
No mathematical computation, enumeration or CAS was needed.

The two frozen bodies below are preserved unchanged. Their historical
candidate labels are superseded only for PG1--PG4 in this exact scope.

---

# 2025 B4(b): signed power gaps and divisible term counts

**Candidate proof - unverified.** Coordinator construction, version 1,
2026-10-17 UTC. These are partial results for the open part (b).
Two independent initially blind whole nonconstructor audits are required.
No novelty or unrestricted classification is asserted.

Write G_m(x)=1+x+...+x^(m-1). The official degree is n=m-1;
the number of terms is m. The power exponent is q. Only |x|>=2
is considered below. The previously accepted C1 supplies the boundary
families, and C2/C4 supply signed LTE and the exact block gcd identity.
The internal geometric sums G_2 are used as auxiliary expressions;
this does not change the official condition m>=3. No proof of the
preliminary part (a) is investigated.

## PG1. An elementary signed power-gap lemma

For integers q>=2, 2<=s<=q+1, and |t|>=2, the integer

    G_s(t^q)

is not a q-th power in Z.

Proof. Put a=|t|>=2 and B=a^(s-1)>=2. First suppose t^q>0.
The leading term is B^q and the remaining positive tail T satisfies

    0<T=sum_(j=0)^(s-2) a^(qj)
       <a^(q(s-2))/(1-a^(-q)).

The strict inequality follows by extending the descending geometric
sum indefinitely. The binomial theorem gives

    (B+1)^q-B^q >= q B^(q-1).

Since s<=q+1,

    T/[q B^(q-1)]
       <a^(s-q-1)/[q(1-a^(-q))]
       <=1/[q(1-2^(-q))] <=2/3<1.

Thus B^q<G_s(a^q)<(B+1)^q. A positive q-th power of an integer
is the q-th power of its absolute value, so none lies in that interval.
This includes even q and either sign of t, as well as odd q with t>0.

It remains that q is odd and t<0. Put u=a^q>=8. The alternating sum
has sign (-1)^(s-1), and its absolute value can be written

    |G_s(-u)|=u^(s-1)-D=B^q-D,
    D=u^(s-2)-u^(s-3)+...+(-1)^(s-2).

Pairing adjacent terms, or the finite geometric formula, gives
0<D<=u^(s-2). For s=2, D=1; for s>2 the upper inequality is
strict. On the other hand

    B^q-(B-1)^q > B^(q-1),

because (1-1/B)^q<1-1/B for B>1 and q>1. Moreover

    u^(s-2)=a^(q(s-2)) <= a^((s-1)(q-1))=B^(q-1),

where the exponent comparison is exactly s<=q+1. Consequently

    (B-1)^q < |G_s(-u)| < B^q.

For odd q, an integer q-th power has absolute value equal to the
q-th power of the absolute value of its root, so this is impossible
for either sign of G_s(-u). This proves PG1.

## PG2. A signed small-cofactor exclusion

Let q>=3 be an odd prime, 2<=s<=q+1, and m=qs.
For |x|>=2 there is no integer y satisfying

    G_m(x)=y^q.

Proof. The accepted C4 identity is

    G_m(x)=A B,  A=G_q(x),  B=G_s(x^q),
    gcd(A,B)=gcd(A,s),

with gcds nonnegative. Both factors are nonzero. If gcd(A,B)=1,
the prime valuations of |B| are multiples of q. Since q is odd,
|B| being a q-th power also makes the signed integer B a q-th
power. This contradicts PG1.

There must therefore be a prime ell dividing s and A. Suppose
ell!=q. The congruence A=1 mod x gives ell not dividing x.
Also x cannot be 1 mod ell, since then A=q mod ell would be
nonzero. The identity (x-1)A=x^q-1 now implies that the
multiplicative order of x mod ell is q: it divides the prime q
and is not 1. Therefore q divides ell-1. The prime ell cannot
be 2, and q is odd, so ell-1 is a positive even multiple of q.
Thus ell>=2q+1. This contradicts ell<=s<=q+1.

The only possible common prime is ell=q. As q divides s and
2<=s<=q+1, this forces s=q and m=q^2. In characteristic q,

    G_q(X)=(X-1)^(q-1),

since (X-1)G_q(X)=X^q-1=(X-1)^q. Hence q divides A exactly
when x=1 mod q. The odd-prime signed LTE formula from C2 gives

    v_q(G_(q^2)(x))=v_q(q^2)=2.

This cannot be the valuation of y^q, since q>=3 does not divide 2.
Every possibility has been excluded. The proof permits negative x
and negative y and does not use a positive-base literature theorem.

In official degree notation this excludes n=qs-1 for the stated q,s.
It does not exclude m=q. In particular the known solutions with
m=q=3 are outside PG2, as required.

## PG3. A prime-power term-count restriction

Let q>=3 be an odd prime, a>=2 an integer, m=q^a, and |x|>=2.
If G_m(x)=y^q for an integer y, then

    x=1 mod q,       q divides a.

In particular there is no such solution when q does not divide a.

Proof. Apply C4 to r=q^(a-1) and s=q:

    G_(q^a)(x)=A B,
    A=G_(q^(a-1))(x),  B=G_q(x^(q^(a-1))),
    gcd(A,B)=gcd(A,q).

Suppose x!=1 mod q. The same characteristic-q identity, now using
X^(q^(a-1))-1=(X-1)^(q^(a-1)), gives

    G_(q^(a-1))(X)=(X-1)^(q^(a-1)-1) mod q.

Thus q does not divide A, and A,B are coprime. By C4, B is a signed
q-th power since q is odd. But, with t=x^(q^(a-2)), one has

    B=G_q(t^q),  |t|>=2.

This contradicts PG1 with s=q. Therefore x=1 mod q is necessary.
Signed odd-prime LTE then gives

    v_q(G_(q^a)(x))=v_q(q^a)=a.

Since the left side is q times the integer valuation v_q(y), one
must have q dividing a. This proves PG3. It leaves a=q,2q,...
unresolved; the necessary conditions are not asserted sufficient.

## Proof dependencies and literature boundary

All three proofs are elementary inequalities, finite field orders,
integer prime valuations and the already accepted C2/C4 interfaces.
No class-number conjecture, finite prime computation, unpublished
claim or positive-base classification is a premise.

The positive-base overlap must be attributed: Bugeaud--Mihailescu,
"On the Nagell--Ljunggren equation", Math. Scand. 101 (2007),
177--183, [Theorem 1](https://journals.msp.org/mscand/article/view/659),
already gives the stronger conclusion m=q when an odd prime q
divides m under its positive integer domain (its known q=3 example
also has m=q). The present packet
does not claim that domain covers negative x. The exact signed
statements above and their elementary proofs are the review targets.
No novelty or priority claim is made.

Bennett--Levin's signed results and published diagonal class-group
conditions are relevant additional leads. The signed prime-power
consequence is isolated in the companion source note: it imports
their published theorem, whereas PG1--PG3 above have only the
elementary dependencies explicitly listed. No full diagonal
classification (which includes m=q) is inferred.

No mathematical computer search, numerical experiment, enumeration
or CAS calculation was used to construct this packet. Administrative
hashing and version freezes are not mathematical evidence. The
unrestricted integer-domain open problem remains unresolved.


---

# Signed power gaps: sources and an attributed consequence

2026-10-17 UTC. **Candidate proof - unverified** pending two whole
audits with the companion PG1--PG3 candidate. No novelty is claimed.

The [official 2025 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf)
is already transcribed and source-checked in statement.md and the
initial reviews. Its geometric degree n is m-1 in our notation.
No preliminary part (a) proof is included.

The exact elementary inputs C2/C4 are the accepted frozen proof.md,
SHA-256 c422139567ee3e2f4eafd852c9a3f5fac73cb6c8e0bfdf9e2c9c5311a9348b0d,
as covered by proofs/reviewed-partial-v1.1.md and reviews/acceptance.md.
This return does not change those files or silently promote any
other conjectural conclusion in the original proof register.

## Positive-base overlap

Y. Bugeaud and P. Mihailescu, *On the Nagell--Ljunggren equation*,
Math. Scand. 101 (2007), 177--183,
[journal](https://journals.msp.org/mscand/article/view/659),
[PDF](https://journals.msp.org/mscand/article/download/659/658),
[DOI](https://doi.org/10.7146/math.scand.a-15038).
The root read the cached primary text through Theorem 1, including
its Equation (1) domain x,y>1, m>2, q>=2 and its known-exception
clause. For odd prime q, its m divisible by q conclusion is stronger
than PG2/PG3 for positive x. That positive domain does not itself
justify negative x. A fresh web retrieval of the PDF failed; the
already cached primary PDF/text supplies this reading. No new claim
of having reconstructed its entire proof is made.

## Signed published restriction

M. A. Bennett and A. Levin, *The Nagell--Ljunggren equation via Runge's
method*, Monatsh. Math. 177 (2015), 15--31,
[author-posted published PDF](https://personal.math.ubc.ca/~bennett/BeLe-Mona-2015.pdf),
[DOI](https://doi.org/10.1007/s00605-015-0748-1).
The root opened the author-posted PDF and read its Equation (1),
Proposition 1, Theorem 1 and their surrounding qualifications on
printed pages 15--17. It explicitly uses integers |x|,|y|>1,
m>2 and q>=2. Proposition 1 says that a solution outside their
four known examples has least prime divisor of m at least 5.
Theorem 1 states Omega(m)<=3, counting prime factors with multiplicity.
Their symbol n denotes our m. These are attributed published inputs;
this return does not reconstruct their entire Runge proof or its
exceptional-case import. No positive-base assumption is added.

### PG4. Attributed signed prime-power diagonal corollary

Assuming the two published Bennett--Levin restrictions just stated,
together with the elementary PG3, there are no integer solutions

    G_(q^a)(x)=y^q, |x|>=2, q an odd prime, a>=2.

Proof. By the accepted C1 magnitude bound |y|>1. None of the four
known examples has term count m=q^a with q odd and a>=2: their
(m,q) are (5,2), (4,2), (3,3), (3,3). If q=3, the least prime
divisor restriction in published Proposition 1 is violated. If q>=5,
published Theorem 1 gives a=Omega(q^a)<=3. Thus 2<=a<=3<q,
contradicting the necessary condition q divides a from PG3.
This proves the displayed corollary conditional on those attributed
published theorems, not a new proof of the imported theorems.

PG4 treats composite prime-power term counts with the same prime
as the power exponent. It leaves m=q (the prime diagonal case)
and general term counts unresolved. It makes no claim about the
known even-exponent term count m=4. It is not a full solution of B4(b).

## Separate class-group lead, not a premise or accepted inference

Mihailescu's 2008 diagonal chapter, the Bartolome--Mihailescu v2
appendix clarification, and Hart--Harvey--Ong's finite calculations
suggest a finite prime-range corollary. The root has not completed
the full hypothesis and proof-interface audit for that inference.
Nothing from it is used in PG1--PG4. No unrestricted Vandiver
conjecture or unreviewed recent preprint is assumed.

All full papers remain in ignored local cache. This note records
citations and theorem scope only, and redistributes no full paper.
