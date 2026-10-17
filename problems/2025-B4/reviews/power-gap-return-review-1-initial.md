# 2025 B4(b): initially blind whole audit of PG1–PG4

2026-10-17 UTC. Reviewer: `review_2021_reasoning_j15_r2`.
Requested launch settings: gpt-6.1-sol / max. An independent effective-setting
readback is unavailable. This is a review recommendation, not a promotion.

I find no substantive defect in PG1–PG3, or in PG4 as an explicitly attributed
corollary importing the full published Bennett–Levin restrictions. Each proof
has been reconstructed below. PG4 is not an elementary proof of the imported
theorem. The packet remains a partial result; it does not classify all solutions
of the official problem.

The coordinator constructed the target packet. I did not construct or
contribute these proofs. I completed this report, its per-inference issue
ledger and source checks before reading any other new PG review or findings.
No peer PG review has been read. No mathematical enumeration, numerical
experiment, CAS or mathematical computer program was used in this audit.
Python was used only for source-text extraction and administrative integrity
checks. The candidate, dependency and earlier review files were not edited.

## Inputs and status boundary

The full targets are:

- `notes/coordinator-power-gap-return-candidate-v1.md`, SHA-256
  `233e00fec364f6f865179c6e3f810173d92b2cd0f5e8a59279e63b605a5d05fb`;
- `notes/coordinator-power-gap-return-sources-v1.md`, SHA-256
  `ae388dc3e6030dcc01b61fe000ff5398b6f3958df252fd9188759e90a1078f60`;
- the constructor's worklog and freeze-v1 manifest, whose SHA-256 is
  `b6612a8286379c12340df3686421c52b3aedb1a6926bd5fa0c9d0a09d88cd9d3`.

I read the official B4(b) statement directly, the complete frozen C1–C4 proof
register and its acceptance, and the complete two-file new candidate. I checked
the published source statements in primary full text, not merely abstracts.
The freeze script separately checks all ten constructor-listed local inputs.

The official variable n is the degree. Here m=n+1 is the number of terms, and
G_m(x)=1+x+...+x^(m-1). Thus official n>=2 corresponds to m>=3. The q in the
new packet is the power exponent, never the official degree. PG1 is an
auxiliary lemma and may use G_2 without asserting an official m=2 solution.
The new packet treats |x|>=2; the accepted C1 handles the boundary values.
I did not investigate or reproduce preliminary part (a).

For PG2–PG4, nonvanishing is automatic: the geometric formula and |x|>=2 give
G_k(x) != 0 for every positive k. In actual applications k>=2. With m>=3,
accepted C1 also gives |G_m(x)|>1. Hence y cannot be 0 or a unit in these
applications. Negative x and negative y are permitted throughout their stated
domains.

## Used dependency interfaces

The accepted proof register has SHA-256
`c422139567ee3e2f4eafd852c9a3f5fac73cb6c8e0bfdf9e2c9c5311a9348b0d`.
Its status is supplied by `proofs/reviewed-partial-v1.1.md` and
`reviews/acceptance.md`; the historical candidate wording inside the frozen
proof is not a reversal of that acceptance. Only the stated C1/C2/C4 interfaces
are used. The conjectural complete list in that register is not a premise.

I independently checked the interfaces used here. Expanding the product gives
G_(rs)(x)=G_r(x)G_s(x^r). Since G_s(T)-s is divisible by T-1, and
x^r-1=(x-1)G_r(x), the second factor is congruent to s modulo the first.
Consequently

    gcd(G_r(x),G_s(x^r)) = gcd(G_r(x),s).

Both gcds are nonnegative and signs do not affect the equality. In every new
application the factors are nonzero. If their product is a q-th power and they
are coprime, each factor's prime valuations are divisible by q. Unique
factorization gives a q-th power for each absolute value. For odd q this also
gives a signed integer q-th root: if B<0 and |B|=b^q, then B=(-b)^q.
This sign step would require care for even q, but PG2/PG3 explicitly use odd q.

The used odd-prime LTE has all its hypotheses here: q is odd prime,
q|(x-1), q does not divide x, |x|>=2 and the exponent m is positive. It yields
v_q(x^m-1)=v_q(x-1)+v_q(m), hence v_q(G_m(x))=v_q(m). Integer valuations use
absolute values, so a negative x-1 or numerator causes no change. Neither
integer in the quotient is zero. For an actual y^q the valuation is q v_q(y),
also when y is negative.

## PG1: reconstruction of the full signed gap

The hypotheses are integer q>=2, integer 2<=s<=q+1, and integer |t|>=2.
Set a=|t|>=2 and B=a^(s-1), an integer at least 2. There are exactly two sign
cases: t^q>0, or q odd and t<0. The first includes both signs of t when q is
even. No case t^q=0 occurs.

For t^q>0, split the leading term from the positive tail:

    G_s(a^q) = B^q + T,
    0<T=sum_(j=0)^(s-2) a^(qj)
       <a^(q(s-2))/(1-a^(-q)).

The strict tail bound is valid also when s=2: the infinite descending
geometric sum adds positive terms to a nonempty finite sum. The binomial gap
is at least q B^(q-1). The exponent difference in their ratio is

    q(s-2) - (s-1)(q-1) = s-q-1 <= 0.

Since a>=2 and q>=2,

    T/(q B^(q-1))
       <a^(s-q-1)/(q(1-a^(-q)))
       <=1/(q(1-2^(-q))) <=2/3.

The last bound follows from q>=2 and 1-2^(-q)>=3/4 separately; it is not an
unverified monotonicity assertion. Thus T is strictly smaller than the gap
to (B+1)^q. We obtain the strict interval

    B^q < G_s(a^q) < (B+1)^q.

A positive q-th power of an integer has the form |z|^q, so no signed root is
lost by comparing consecutive nonnegative roots B and B+1.

For the other case q is odd, t<0, and u=a^q>=8. The closed geometric formula
shows G_s(-u) has sign (-1)^(s-1). Its absolute value is

    |G_s(-u)| = u^(s-1)-D = B^q-D,
    D=sum_(k=0)^(s-2) (-1)^k u^(s-2-k).

Here D is positive and at most u^(s-2). One entirely explicit verification is
to put D_d=u^d-u^(d-1)+...+(-1)^d. Then D_0=1 and D_d=u^d-D_(d-1).
Induction gives 0<D_d<u^d for d>=1, because 0<D_(d-1)<=u^(d-1)<u^d.
This checks the alternating-sign claim, the s=2 case D=1, and the strict
upper bound for s>2 without assuming positivity of an alternating tail.

As 0<1-1/B<1 and q>1,

    (1-1/B)^q < 1-1/B,
    B^q-(B-1)^q > B^(q-1).

The exponent inequality

    q(s-2) <= (s-1)(q-1)

is precisely s<=q+1. Therefore

    0<D<=u^(s-2)<=B^(q-1)<B^q-(B-1)^q,
    (B-1)^q < |G_s(-u)| < B^q.

Odd powers have |z^q|=|z|^q, so this excludes both positive and negative
integer q-th powers of the original sum. This proves PG1 on the entire
stated signed domain.

I specifically checked the lower endpoint s=2, the upper endpoint s=q+1,
the minimum a=2, and q=2. At s=q+1 the exponent comparison becomes equality,
but both gap arguments retain the required strictness. The q=2 case is
entirely in the first sign case. Primality is not used in PG1.

## PG2: reconstruction of the cofactor and order argument

Here q>=3 is an odd prime, 2<=s<=q+1, m=qs, |x|>=2 and y is an arbitrary
integer. The block decomposition gives nonzero A=G_q(x), B=G_s(x^q) with
G_m(x)=AB and gcd(A,B)=gcd(A,s).

If the gcd is 1, the signed-root consequence of C4 makes B a q-th power in
Z. PG1 applies with t=x and the same q,s, giving a contradiction. Thus any
putative solution has a prime ell dividing gcd(A,s); in particular ell|s and
ell<=s. This uses an actual common prime, not an assumed cyclotomic
coprimality statement.

Suppose ell!=q. If ell divided x, the sum A would be 1 modulo ell, impossible.
If x were 1 modulo ell, A would be q modulo ell, again nonzero. Therefore
x is a nonzero residue different from 1. The identity
(x-1)A=x^q-1 gives x^q=1 modulo ell. Its multiplicative order divides the
prime q but is not 1, hence is exactly q. Consequently q divides ell-1.
The prime ell cannot be 2, whose unit group has no element of odd order q>1.
So ell-1 is positive and even. Since q is odd, (ell-1)/q is a positive even
integer, and ell>=2q+1. This contradicts ell<=s<=q+1.

Only ell=q can occur. Then q|s and 2<=s<=q+1 force s=q (because 2q>q+1).
Thus m=q^2 and q divides A. In F_q[X],

    (X-1)G_q(X)=X^q-1=(X-1)^q,
    G_q(X)=(X-1)^(q-1).

Cancellation here is polynomial cancellation in an integral domain. It is
not division by the evaluated residue x-1. The resulting polynomial identity
can be evaluated at every residue, including x=1, and gives q|A exactly when
x=1 modulo q. Signed LTE now gives v_q(G_(q^2)(x))=2. But a nonzero integer
q-th power has valuation divisible by q, while no prime q>=3 divides 2.
This is the final contradiction.

All factor signs are covered by odd q. In particular, when x<0 and s is
even, B and G_m(x) can be negative; no positive-base theorem has been used
to dispose of that case. Primality is essential to the exact-order step and
is present in the claim. The official excluded degrees are n=qs-1. The known
m=q=3 examples fail the hypothesis s>=2 and are not excluded.

## PG3: reconstruction for prime-power term counts

Now q>=3 is an odd prime, a>=2 an integer, m=q^a and |x|>=2. With
r=q^(a-1) and s=q, the exact C4 gcd is

    A=G_(q^(a-1))(x),  B=G_q(x^(q^(a-1))),
    G_(q^a)(x)=AB,      gcd(A,B)=gcd(A,q).

Suppose x is not 1 modulo q. Iterated Frobenius in F_q[X] and the same
polynomial cancellation give

    G_(q^(a-1))(X)=(X-1)^(q^(a-1)-1).

Evaluation at x is nonzero, so q does not divide A and the displayed gcd
is 1. The q-th power product therefore makes B a signed integer q-th power.
Set t=x^(q^(a-2)). Since a>=2, this is an integer with |t|>=2, including
the endpoint a=2 where t=x. Direct multiplication of the exponents gives
t^q=x^(q^(a-1)). Thus B=G_q(t^q), contradicting PG1 with s=q.

It follows that x=1 modulo q is necessary. Signed LTE gives
v_q(G_(q^a)(x))=a, and equality with y^q forces q|a. There is no converse
assertion. In particular the elementary proof does not exclude a=q,2q,...
after this step. It does not treat a=1, for which the t substitution and
last-block obstruction would not have the stated form. The known prime
diagonal examples are therefore untouched. The official degrees here are
n=q^a-1, not n=q^a.

## Published-input audit and PG4

I freshly opened Bennett–Levin's author-posted published PDF and inspected
the entire relevant statements and surrounding qualifications on printed
pages 15–17. Their Equation (1) explicitly uses integers |x|>1, |y|>1,
n>2 and q>=2; this is a signed domain. Their n equals the term count m
used here. Proposition 1 applies outside the four displayed examples and
in particular forces the least prime divisor of that term count to be at
least 5. Theorem 1 bounds its total prime-factor multiplicity by 3.
[Primary full text](https://personal.math.ubc.ca/~bennett/BeLe-Mona-2015.pdf).

The paragraph following the theorem matters: the elementary portion of
their proof retains a possible case (n,q)=(p^5,5), p prime dividing x-1;
the paper resolves it by importing its reference [10]. The printed theorem
is stated without that exception. PG4 explicitly imports the complete
published result, not only the elementary portion. I checked this interface
and the theorem's complete hypotheses, not the entirety of the external
Runge proof or the proof of its external reference.

For the displayed PG4 equation, m=q^a>=9. The C1 magnitude bound supplies
|y|>1, and |x|>=2 supplies |x|>1. Thus its geometric formula is a solution
of the source equation with n_source=m=n_official+1>2. None of the four
source examples qualifies: the two even-power examples have q=2, and
the two odd-power examples have m=q=3 with a=1. Therefore the proposition's
known-example qualification is satisfied.

If q=3, the least prime divisor of m=3^a is 3, contrary to Proposition 1.
If q>=5, Theorem 1 gives Omega(q^a)=a<=3. PG3 simultaneously requires q|a,
but 2<=a<=3<q. This proves PG4 with exactly its stated published inputs.
It does not use a finite prime range, a class-number conjecture, or a
positive-base theorem as a substitute for a negative-base result.

For the positive-base overlap, I also read Bugeaud–Mihailescu's primary
2007 paper directly from its cached PDF, independently extracting all seven
pages. Its Equation (1) is restricted to x,y>1. The last assertion of its
Theorem 1 supplies m=q when q divides the term count, outside its known
examples; the known odd-prime example also has m=q. Hence the candidate's
attribution of a stronger positive-base result is accurate. That theorem
cannot supply the negative-x part of PG2/PG3, and is not used for it.
[Journal source](https://journals.msp.org/mscand/article/view/659).

The separate class-group/finite-prime lead is explicitly left unaudited and
unused by the author. I make no acceptance recommendation for it and have
not treated it as a mathematical premise of PG1–PG4.

## Adversarial checks and disposition

The plausible failures I tested by reasoning were: losing a negative q-th
root after factorization; incorrectly treating the alternating tail as
positive; losing strictness at s=q+1; canceling x-1 at the exceptional residue;
using an order smaller than q; allowing ell=2; applying LTE to a negative
base outside its hypotheses; using the a=1 case in PG3; confusing degree
with term count; and silently dropping the external exceptional-case
import. None occurs in the frozen target. The report above supplies the
corresponding checks without a finite scan.

There are no open substantive issues and no required author repair from
this review. The issue ledger records each inspected inference separately.
I recommend acceptance of PG1–PG3 as the stated elementary partial results,
and of PG4 with its explicit published-theorem attribution, only after the
second fresh independent audit and coordinator integration. I do not promote
the packet, establish novelty, independently reprove the imported theorem,
or claim a full solution of B4(b).

The accompanying one-time freeze validates the complete constructor manifest
and all earlier own frozen packets. It records requested settings separately
from unknown effective settings and account-wide weekly usage of 25%, with
reset 1792745187 and the 90%-total stop policy. No Git or shared-file change
was made.
