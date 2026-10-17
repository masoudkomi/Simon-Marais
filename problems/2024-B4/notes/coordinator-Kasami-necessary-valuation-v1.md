# A necessary valuation for a whole Kasami divisor

2026-10-17 UTC. **Candidate proof — unverified; research continuation.** Root constructor. This is NOT part of the separately accepted GK1–GK3 scope and requires two independent whole audits before promotion. It gives a necessary condition, not general-q necessity of the entire sufficient progression.

Fix q=2^k with k>=2, d=q²−q+1, and odd n>=3. The proposed statement is:

    phi_d divides phi_n over F2  ==>  v2(n−1)=k.          (NV)

By exact accepted CP1, the hypothesis is equivalent to g_n=H(g_d), H in F2[T]. The accepted degree relation gives d−1=q(q−1) dividing n−1. Thus n>=d and s=v2(n−1)>=k. The argument below rules out s>k.

Write G_j(x)=x^j+(x+1)^j=g_j(x²+x) for odd j>=3. At x=0, G_j(0)=1 and G_j'(0)=1. The latter follows by differentiating, since j is odd and j−1>=2. Therefore G_n=H(G_d) implies

    H(1)=1, H'(1)=1.

Consequently H(T)+1=(T+1)Q(T) for a polynomial Q with Q(1)=1. At ANY point where G_d=1 the vanishing order of G_n+1 is exactly that of G_d+1. This follows by substitution: Q(G_d) is nonzero at that point. No separability of the entire map H is assumed.

Choose alpha in F_q minus F2, which exists because k>=2, and put b=alpha+1. Both alpha and b are nonzero and alpha+b=1. Since d=1+q(q−1), the binomial identity

    (alpha+z)^d=(alpha+z)(alpha^q+z^q)^(q−1)

shows that its terms through degree q+1 can occur only at exponents0,1,q,q+1. The analogous expression holds for b. For the sum G_d(alpha+z), their coefficients are as follows:

- constant: alpha^d+b^d=alpha+b=1, since d=1 mod(q−1);
- degree1: alpha^(d−1)+b^(d−1)=1+1=0;
- degreeq: alpha^(d−q)+b^(d−q)=1+1=0, since d−q=(q−1)²;
- degreeq+1: alpha^(d−q−1)+b^(d−q−1)=alpha^(-1)+b^(-1)=1/(alpha b), which is nonzero.

The binomial coefficient at q and q+1 is q−1=1 in characteristic2. There are no other terms of degrees less than q+1. Thus

    ord_(x=alpha)(G_d(x)+1)=q+1.                       (1)

Now assume s>k and put n=1+2^s h with h odd. Since n−1 is divisible by q−1, alpha^(n−1)=b^(n−1)=1. The identities

    (alpha+z)^n=(alpha+z)(alpha^(2^s)+z^(2^s))^h

and its b analogue show that degrees strictly between1 and2^s do not occur. The constant in G_n(alpha+z)+1 is0, since n=1 mod(q−1), and its degree1 coefficient is1+1=0. Consequently

    ord_(x=alpha)(G_n(x)+1)>=2^s>=2q>q+1.              (2)

The order is finite because G_n is nonconstant. Equations(1)–(2) contradict H(1)=1,H'(1)=1 and the exact-order preservation above. Hence s=k, proving the candidate implication(NV).

The restriction k>=2 is essential: at q=2 there is no alpha outside F2 and the whole divisor phi3 is a unit, which divides every phi_n. For instance n=5 would contradict(NV) if that restriction were omitted. At n=d the conclusion is v2(d−1)=k, consistent with equality/unit cofactor. This argument concerns the WHOLE fixed divisor, not any individual Kasami component.

No new external MCM, Janwa–Wilson, APN or ramification theorem is used. The exact accepted CP1 and elementary finite-field identities are the inputs; the local binomial orders are proved here. For q=4, the condition also follows from the older exact phi13 iff. For general q it is weaker than a full whole-divisor classification: it does not force n=(q^(2m+3)+1)/(q+1). No computation, finite-field sampling, broad scan, full annual solution or novelty claim is made.
