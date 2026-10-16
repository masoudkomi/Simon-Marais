# Further small fixed divisors, exploratory checkpoint

2026-10-16. **Candidate deductions - unverified.** These finite closed
graphs were constructed by the coordinator, so they are not independent
reviews. They concern whole fixed divisors, not every irreducible factor
and not the full B4(b) classification. No novelty is asserted.

Using the universal P_j generating function from the separate frozen
zero-automaton candidate, direct coefficient expansion gives

    P_2=d+q^2,
    P_3=u+q^3,
    P_4=q*u+q^4+q^2*d+d^2.

The main further targets are P_2 (the actual phi_7) and P_4 (phi_11).
Their possible occurrences as factors of other phi_n concern B4(b).
P_3 (phi_9) was included only as a diagnostic known-family baseline;
no further investigation or proof of its preliminary Gold-family
consequence is proposed, because part (a) is outside scope.

## Formal quotient models

For P_2=0, invert q and set b=u/q^3, so d=q^2. The normalized
series is

    (1+z+z^2)/(1+z^2+b*z^3+z^4).

For P_4=0, invert q and set b=d/q^2, so
u=q^3*(1+b+b^2). The normalized series is

    (1+z+b*z^2)/(1+z^2+(1+b+b^2)*z^3+b^2*z^4).

P_2 is prime, being monic linear in d. P_4 is primitive linear in u
over F2[q,d]: gcd(q,q^4+q^2*d+d^2)=1. The same Gauss/primality
argument as in the phi13 candidate makes P_4 prime. Neither divides q.
Thus the displayed localization should be saturated for each divisor.
The injective integral extension S=F2[q,u,d] -> F2[x,y,z] from the
separate criterion candidate would transfer whole-divisor divisibility
in both directions. These inferences need independent audit; that
candidate's ongoing reviews do not automatically cover this note.

## Exact finite graphs and proposed consequences

`../computations/coordinator-small-divisor-probe-v1.py` uses all four
two-variable Cartier maps N -> C_(r,t)(N*K), and conjunctive F2 subspaces.
For P_2 the invariant numerator basis has 0<=z-degree<=3 and
0<=b-degree<=1 (dimension 8); for P_4 use 0<=b-degree<=2 (dimension 12).
Multiplication by K and parity selection/halving preserve these bounds.
The general subspace invariant would then apply to all binary lengths.

The P_2 graph closed at eight states and 16 edges. Its quotient has
four classes, initial S, with transitions

    S: 0 -> A, 1 -> X
    A: 0 -> X, 1 -> Z
    X: 0 -> X, 1 -> X
    Z: 0 -> Z, 1 -> X      (only Z accepts).

Thus its candidate accepted language, least-significant bit first, is
01 followed by any number of zeros. Its only canonical integer index
is j=2. Subject to the entire general argument and exact certificate
checks, this would prove phi_7 | phi_n only when n=7, for odd n>=3.

The P_4 graph closed at 15 states and 30 edges. Its five-class quotient is

    S: 0 -> A, 1 -> X
    A: 0 -> B, 1 -> X
    B: 0 -> X, 1 -> Z
    X: 0 -> X, 1 -> X
    Z: 0 -> Z, 1 -> X      (only Z accepts).

Its candidate accepted language is 001 followed by any number of zeros;
the only canonical index is j=4. Subject to the same obligations, this
would prove phi_11 | phi_n only when n=11.

These exclusions do not imply that phi_n is irreducible at other n.
They only rule out these entire particular divisors. Neither graph
has received an independent reconstruction yet. The quotient languages
are not guessed from scanning coefficients: all transitions are closed
in the saved graph, and acceptance of a canonical integer follows
from that whole language once the general invariant is established.

## Evidence and next step

The dedicated child PID 16873 had an explicit 25-second external timeout,
7 seconds per model and 10,000-state caps. It completed with return code 0
in about 0.045 seconds including launch. Parameters, all operator columns,
state bases, edges, quotient classes, outputs and hashes are retained in
the `coordinator-small-divisor-probe-v1*` files. The scan below 8192 is
supplementary finite evidence only. No native factorization was performed.

Before promoting either exclusion, independently rebuild the quotient
models, all operator columns/edges, the canonicalization and language,
and the formal-to-actual bridge; check the exact original domains and
all degeneracies. Obtain two fresh adversarial audits. Prefer developing
a useful general family of exclusions or factors over accumulating
isolated fixed-divisor computations without a classification strategy.
