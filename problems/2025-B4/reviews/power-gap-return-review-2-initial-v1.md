# Initial whole independent audit R2: signed power gaps

2026-10-17 UTC. Reviewer /root/review_2022_complexity_r2 did not construct
either target. Requested gpt-6.1-sol/max; independent effective-setting
readback is unavailable. This full initial report, per-claim ledger and
source checks are frozen before any peer power-gap findings are read.

Targets are the complete coordinator-power-gap-return-candidate-v1.md
(SHA-256 233e00fec364f6f865179c6e3f810173d92b2cd0f5e8a59279e63b605a5d05fb),
its complete sources-v1.md
(ae388dc3e6030dcc01b61fe000ff5398b6f3958df252fd9188759e90a1078f60)
and freeze-v1.json
(b6612a8286379c12340df3686421c52b3aedb1a6926bd5fa0c9d0a09d88cd9d3).
The worklog, official domain and exact accepted C1/C2/C4 inputs were read.

**Finding:** PG1--PG3 reconstruct over their stated signed integer
domains, and PG4 follows from the precisely attributed published inputs.
I found no substantive objection or needed mathematical repair.
PG4 is an application of external theorems; this audit does not claim a
new reconstruction of those theorems' complete proofs. This is a partial
result and no novelty or full B4(b) classification is inferred.
Only the coordinator may decide acceptance after both independent audits.
No mathematical computation, search, enumeration or CAS was used.

## 1. Official quantifiers and accepted elementary interfaces

The [official 2025 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc2025_paper_b.pdf),
page 2, B4(b), asks about integers x,y,n,q with n,q>=2 and degree n.
The packet consistently writes

    G_m(x)=sum_(j=0)^(m-1) x^j,       m=n+1>=3.

The literature's exponent of x in the numerator is m, not official n.
PG1 is an auxiliary lemma with possibly s=2; its use of a two-term
geometric sum does not assert an official case with n=1. PG2 has
m=qs>=6 and PG3/PG4 have m=q^a>=9, so all their applications lie
in the official domain. Only open part (b) is audited. No proof of the
excluded preliminary equation was investigated.

The exact accepted proof register is proof.md, SHA-256
c422139567ee3e2f4eafd852c9a3f5fac73cb6c8e0bfdf9e2c9c5311a9348b0d.
The reviewed partial exposition and coordinator acceptance limit that
acceptance to C1--C4; a separate conjectural full list in the register is
not a premise here. The present targets use only the following interfaces.

C1 gives |G_m(x)|>1 when |x|>=2 and m>=3. This includes negative x:
for x=-a, a>=2, the magnitude is (a^m+1)/(a+1) when m is odd,
and (a^m-1)/(a+1) when m is even. Thus a solution in the present
applications has |y|>1 and y is nonzero. This is the bridge to the
nontrivial published domain in PG4.

C4 is exact over integers:

    G_(rs)(x)=G_r(x)G_s(x^r),
    gcd(G_r(x),G_s(x^r))=gcd(G_r(x),s).

Indeed G_s(T)-s is divisible by T-1 in Z[T], and
x^r-1=(x-1)G_r(x). Hence the second factor is s modulo the
first. This is not a claim that every cyclotomic factor is coprime.
When the two factors are nonzero and coprime, unique prime
factorization shows that each absolute value is a q-th power if
their product is. The sign can also be restored when q is odd.
All factors used below are nonzero for |x|>=2, even when the
auxiliary term count is two. No valuation of zero is taken.

C2 gives, for an odd prime p with p|(x-1),

    v_p(G_m(x))=v_p(m).

The signed hypotheses are correct. Write x=1+p^h u with h>=1,
p not dividing u, allowing u negative. A binomial expansion shows
that an exponent coprime to p preserves v_p(x-1); raising to p
then increases it by exactly one, since p is odd. Iterating and
splitting m into its p-primary and coprime parts proves the used
LTE identity without x>0. The targets invoke it only for p=q
and positive m. The two-adic variant and C3 are not needed.

## 2. PG1: both gaps and all endpoints

Fix q>=2, 2<=s<=q+1 and an integer t with a=|t|>=2.
Set B=a^(s-1), so B is an integer at least two. If t^q>0,
the leading term of G_s(t^q) is B^q and the remaining tail T
is positive. Extending its descending geometric series gives

    T<a^(q(s-2))/(1-a^(-q)).

The strictness is valid even when s=2: the finite series then has
one term while its infinite extension has additional positive
terms. The next power has gap at least q B^(q-1), since every
other term in the binomial expansion is nonnegative. The ratio is

    T/(qB^(q-1))
      < a^(s-q-1)/(q(1-a^(-q)))
      <= 1/(q(1-2^(-q))) <= 2/3.

The exponent calculation is
q(s-2)-(s-1)(q-1)=s-q-1<=0.
For the last inequality, q>=2 and 1-2^(-q)>=3/4
already suffice. Thus

    B^q<G_s(t^q)<(B+1)^q.

For a positive value, an integer q-th power would equal the
q-th power of an integer's absolute value. Consecutive positive
integer q-th powers leave no such value strictly between them.
This handles both signs of t for even q and positive t for odd q.
No assumption that q is prime is made or needed in PG1.

The remaining case is t<0 and q odd, hence q>=3. Put u=a^q>1.
The leading term determines the sign of the alternating series:
the absolute value is

    |G_s(-u)|=B^q-D,
    D=u^(s-2)-u^(s-3)+...+(-1)^(s-2).

Pairing adjacent descending terms, including a final positive
constant if necessary, gives D>0. Its geometric expression also
gives D<=u^(s-2), with equality only at s=2. For s>2, what
is subtracted from the leading term of D is positive.

Let z=1-1/B, so 0<z<1. Since q>1, z^q<z, and consequently

    B^q-(B-1)^q > B^(q-1).

The same endpoint comparison s<=q+1 gives

    D<=a^(q(s-2))<=a^((s-1)(q-1))=B^(q-1).

Therefore the strict interval is

    (B-1)^q<|G_s(-u)|<B^q.

It excludes an odd signed q-th power as well, since taking
absolute values of such a power produces an ordinary positive
integer q-th power. There is no parity loophole when s is even
and the sum is negative. At s=2 the value D=1 still gives strict
inequalities; at s=q+1 the exponent comparison may be equality,
but the power gap remains strictly larger. The least allowed
a=2 and q=2 in the first case do not close either gap.

PG1 is thus proved by the proposed elementary argument on its full
stated domain. The restrictions s<=q+1 and |t|>=2 have actually
been used, and are not discarded in later applications.

## 3. PG2: a common prime, its order, and the remaining LTE case

Here q>=3 is an odd prime, 2<=s<=q+1, m=qs and |x|>=2.
Factor using C4 with

    A=G_q(x),        B=G_s(x^q),
    G_m(x)=AB,       gcd(A,B)=gcd(A,s).

If the gcd is one and AB=y^q, prime valuations of |B| are
multiples of q. Thus |B| is a q-th power. Oddness of q restores
the sign of B by choosing the sign of its root. This contradicts
PG1 with t=x and the same s. An absolute-value statement alone
would not be enough for an arbitrary even q; the packet correctly
keeps q odd here.

If the gcd is larger than one, some positive prime ell divides both
A and s. First suppose ell!=q. Reducing A modulo x shows
ell does not divide x. If x=1 mod ell, then A=q mod ell,
contrary to ell|A and ell!=q. The identity

    (x-1)A=x^q-1

therefore gives x^q=1 mod ell with x!=1 mod ell.
The multiplicative order of this nonzero residue divides prime q
and is not one; it is exactly q. Lagrange's theorem yields
q|(ell-1). This already rules out ell=2. Since q is odd,
ell-1 is divisible by both 2 and q, hence by 2q. Thus
ell>=2q+1, whereas ell|s gives ell<=s<=q+1.
The contradiction is strict for every permitted q.
Negative x causes no change in this finite-field argument.

It remains that the common prime is ell=q. Then q|s and
2<=s<=q+1 force s=q, hence m=q^2. In F_q[X],

    (X-1)G_q(X)=X^q-1=(X-1)^q.

Cancellation of the nonzero polynomial X-1 in this integral
domain yields G_q(X)=(X-1)^(q-1). Consequently q|A if and
only if x=1 mod q, including residues x=0 without exception.
C2 now applies and gives

    v_q(G_(q^2)(x))=2.

For a nonzero y^q the same valuation must be q v_q(y),
which cannot be two when q>=3. This closes the entire
noncoprime branch, without assuming it is the only branch
before proving that fact. PG2 follows with official n=qs-1.
The prime diagonal m=q, including the known q=3 identities,
is outside s>=2. This matters for the asserted exclusion.

## 4. PG3: prime-power term counts

Assume q>=3 odd prime, a>=2 and m=q^a. Apply C4 with
r=q^(a-1), s=q. Then

    A=G_(q^(a-1))(x),    B=G_q(x^(q^(a-1))),
    gcd(A,B)=gcd(A,q).

The characteristic-q identity generalizes exactly:
because r is a q-power, X^r-1=(X-1)^r in F_q[X], and
cancelling X-1 gives G_r(X)=(X-1)^(r-1).
If x!=1 mod q then q does not divide A, so A and B are
coprime. As in PG2, oddness of q makes the signed factor B
a q-th power. But putting t=x^(q^(a-2)) gives

    B=G_q(t^q),       |t|>=2.

PG1 applies with s=q. The a=2 endpoint uses t=x, since
q^(a-2)=1, and is fully included. Thus the assumption
x!=1 mod q is impossible.

For x=1 mod q, the same signed LTE interface gives

    v_q(G_(q^a)(x))=a=q v_q(y),

so q|a is necessary. This does not assert sufficiency or
exclude a=q,2q,... using elementary PG3 alone. The case
a=1 is not covered: the proof's use of the previous q-power
and PG1 would then have no valid t. All stated ranges
are respected. No induction assumes the target conclusion.

## 5. PG4: source interface and attributed deduction

I directly checked the [author-posted Bennett--Levin paper](https://personal.math.ubc.ca/~bennett/BeLe-Mona-2015.pdf),
printed pages 15--17: Equation (1) allows |x|,|y|>1,
term count m>2 and q>=2. Outside the four displayed
identities, Proposition 1 requires least prime divisor of
m at least five. Theorem 1 states Omega(m)<=3, counting
prime factors with multiplicity. These signed statements,
not a positive-base substitute, are precisely the imports.
The paper explicitly completes its exceptional Runge case
using another published input; no missing exception is
retained in the theorem being applied.

C1 supplies |y|>1, so all imported domain hypotheses hold.
For m=q^a with q odd and a>=2, none of the displayed
exceptions can occur: their term counts/exponents are
(5,2), (4,2), (3,3), (3,3). For q=3, the least prime
divisor is three, which violates the imported restriction.
For q>=5, Omega(q^a)=a<=3 makes 2<=a<q, contrary to
PG3's necessary q|a. This is the complete deduction.

The exclusion of negative roots for odd powers needs no
extra published classification: an odd power's sign is
fixed by its value, and C1 already handles the magnitude.
For the even-power known identities, choosing the negative
integer root does not change their term counts; in any
case PG4 assumes odd q and cannot meet them.

PG4 therefore follows as an attributed corollary conditional
on the published theorems. I have checked their statements,
domain and the application's logic, not reconstructed the
entire external Runge/cyclotomic proof. The elementary
PG1--PG3 deductions do not depend on that import.

## 6. Positive-base overlap and unresolved scope

I also checked the [primary Bugeaud--Mihailescu paper](https://journals.msp.org/mscand/article/download/659/658/690),
Equation (1) and Theorem 1, printed pages 177--178.
Its domain is x,y>1, m>2, q>=2. Its final clause says that,
outside its listed exceptions, q|m forces m=q. For the
positive-base instances of PG2 and PG3 this is stronger.
The known odd-prime exception has m=q=3 and lies outside
both exclusions. The packet correctly records this overlap
and does not extend that positive-base theorem to negative x.

The alternative class-group and finite prime-range leads in
the source note are explicitly not premises. They are not
used to eliminate the unresolved prime diagonal m=q or
general composite term counts. There is no assumption of
Vandiver, no search table treated as a theorem, and no
automatic reduction of the full integer problem to the
restricted ranges above.

The candidate leaves |x|<=1 to accepted C1, retains all official
signs, distinguishes n from m throughout, and states its prime
q restrictions. PG4's stronger prime-power conclusion is
properly separated from PG3's elementary necessary conditions.
These partial claims do not supply a complete classification.

## 7. Adversarial checks, preservation and disposition

The independent reconstruction checked all of the following:
finite versus infinite-tail strictness; s=2 and s=q+1;
q=2 only in PG1; odd negative powers and negative sums;
nonzero factors; the gcd-one sign step; ell=2 and ell=q;
the order exactly q rather than merely dividing q;
characteristic-q cancellation; a=2 and a=1 separation;
signed LTE hypotheses and integer valuations; source m=n+1;
the nontrivial |y| bound; all known-exception term counts;
and the distinction between attributed input and elementary proof.

None yielded a counterexample or unresolved substantive gap.
No routine examples, larger scans or finite certificates were needed.
Only assigned power-gap-return-review-2-* records were created.
No source/candidate/shared edits, Git, spawning, charge or external
contact occurred. Existing source-cache hashes and all earlier own
frozen records are verified separately by administrative metadata.
The source papers remain in ignored cache; no full paper is
redistributed in this review.

Latest authoritative account-wide telemetry obtained in this audit:
26% weekly total used at 2026-10-17 06:28:49 UTC,
10080-minute window, reset1792745187, ordinary usage allowed.
The total ceiling is 90%, with integration/review reserve.
This frozen initial report is the basis for coordinator comparison;
it neither promotes the packet nor claims absolute certainty.
