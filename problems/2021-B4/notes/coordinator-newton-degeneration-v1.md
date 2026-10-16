# A Newton degeneration forces a low-order center witness

2026-10-16 UTC. **Candidate proof - unverified.** Constructed by the
coordinator, independently of the frozen Newton packet's reviewers. This
note requires two fresh adversarial audits of its own. No complete degree
or solution of B4(b), and no novelty, is claimed.

## Precise setup and claim

Use the normalization and notation of
`padic-rational-newton-obstructions-v1.md`: p>=5 is prime, d=p+1,

    f(x)=x^d-d*x^(d-1)+sum_(j=2)^(d-2) binom(d,j)*a_j*x^(d-j),
    a_j in Z_(p), f(0)=f'(0)=f(1)=0,
    J=max{j:v_p(a_j)=0}, h=d-J, m=ord_0(f)>=2.

The hypothesis is a nontrivial contest counterexample: f has rational
coefficients and each derivative H_k=f^(k)/k!, 1<=k<=d-1, has a common
**rational** root with f. Only these recycled roots, rather than every root
of f, are assumed rational. The center 1 is simple. Assume J>=d/2.

Suppose there is **no nontrivial Casas-Alvero polynomial of degree h over
the algebraic closure of F_p**, using Hasse derivatives. Then

    H_k(f)(1)=0 for at least one k in {2,...,h-1}.       (D1)

For h=2 this is an empty range and rules the case out. For h=3,4,5 at
p=19, the cited primary results verify the characteristic-p hypothesis.
Thus in degree 20, J=15 additionally requires

    H_2(f)(1)=0 or H_3(f)(1)=0 or H_4(f)(1)=0.         (D2)

The older J=17 and J=16 conditions are recovered in a common framework;
their exact-family J=17 exclusion is a separate result. No analogous
claim at h=6 or h=7 follows from these particular published inputs:
19 is a bad prime for those degrees.

## Proof proposed for audit

Write c_t for the ordinary coefficients. The supporting-line argument in
the frozen packet gives the edge

    (h,1) -> (d-1,0), width J-1, slope -s_0,
    s_0=1/(J-1),

with every other nonzero coefficient point strictly above that line.
Hence its J-1 roots, counted with multiplicity, have valuation s_0,
which is nonintegral and so unavailable as rational witnesses. There is
one valuation-zero root, the simple root 1. The other h root slots
consist of 0 with multiplicity m and h-m nonzero roots of valuation
strictly greater than s_0. The strict inequality follows from strict
increase of slopes between different lower Newton edges, and the strict
supporting-line statement rules out an extension of this edge to the left.

First, if h=m, all rational root choices are 0 and 1. The published
two-recycled-root obstruction excludes a nontrivial f. Thus h>m.
Let nu be the **smallest** valuation of the h-m remaining nonzero roots;
then nu>s_0. The Newton edge with slope -nu immediately to the left
of (h,1) has a left endpoint (i,v(c_i)) for some m<=i<h. Its supporting
line is

    L(t)=1+(h-t)*nu.

All coefficient points are on or above this line, and those with t>h
are strictly above it. In particular its two endpoints lie on it.
Choose a finite extension K/Q_p containing all roots of f and an element
alpha with v(alpha)=nu; an actual root of valuation nu may be chosen.
Use beta=c_h*alpha^h, so v(beta)=1+h*nu, and set

    g(T)=beta^(-1)*f(alpha*T) in O_K[T].

The supporting-line inequalities make every coefficient integral. In its
residue reduction G in k[T], the term T^h has coefficient exactly 1,
every term of degree >h vanishes, and the term T^i is nonzero. All terms
of degree below m vanish identically. Thus G has degree h, is divisible
by T^m, and has another nonzero coefficient at degree i<h. In particular
G is not T^h and is not a power of a linear polynomial: it has the root
0, so any pure h-th power with that root would be a scalar times T^h.

Assume, toward a contradiction, that no center equation H_k(f)(1)=0
holds for k=2,...,h-1. It also fails for k=1 since 1 is simple. For
each k=1,...,h-1 choose a common rational root w_k of f and H_k(f).
It is not 1; it is not in the long fractional-valuation cluster; it is
therefore 0 or one of the remaining roots, of valuation >=nu. Consequently
z_k=w_k/alpha is integral. The exact polynomial identity

    H_k(g)(T)=alpha^k/beta * H_k(f)(alpha*T)

holds over K. Both sides are integral polynomials, since the left side is
a Hasse derivative of g. It follows that g(z_k)=H_k(g)(z_k)=0, and reducing
gives G(zbar_k)=H_k(G)(zbar_k)=0. Hasse differentiation commutes with
coefficient reduction, with no division by a factorial in the residue
field. These witnesses exhibit a nontrivial CA polynomial G of degree h
over k, hence over the algebraic closure of F_p. This contradicts the
hypothesis and proves (D1), subject to independent audit.

The proof uses rationality exactly to exclude the long cluster's
nonintegral valuation. K and the reduction witnesses need not be rational
or F_p-rational. Multiplicity is retained throughout the Newton count.

## Published characteristic-p inputs, verified directly

Castryck, Laterveer and Ounaies,
[Constraints on counterexamples to the Casas-Alvero conjecture, and a
verification in degree 12](https://arxiv.org/abs/1208.5404), cached full
author version `.cache/literature/2021/cited-66c5af6a0f0239f5.pdf`.
The printed/PDF pages 4-5 were read directly on 2026-10-16.

- Definition 1 uses Hasse derivatives over an algebraically closed field
  and expressly excludes powers of linear polynomials.
- Paragraph 1.7 states that degree 3 has only the bad prime 2, and degree
  4 has exactly the bad primes 3,5,7, attributing the latter to Draisma
  and de Jong. Degree 2 has no bad primes.
- Theorem 4 gives the degree-5 bad primes exactly as
  2,3,7,11,131,193,599,3541,8009. Thus 19 is good in degree 5. That theorem
  is a published computational input, not re-proved by this note.
- Its Table 1 includes 19 as bad in degree 6. Its degree-7 statement says
  the smallest nonbad prime other than 7 is 127, so 19 is bad there too.

The normalization, two-recycled-root obstruction, and Newton multiplicity
theorem have their primary references and hypothesis checks in the frozen
packet. Stoll, *p-adic Analysis in Arithmetic Geometry*, Theorem 3.6,
explicitly states multiplicities; its author-posted source is recorded in
the separate R1 source manifest. These published ingredients are distinct
from the proposed degeneration argument here.

## Finite filter and limits

`computations/coordinator-newton-degeneration-v1.py` independently builds
ordinary Hasse coefficients modulo 19^2, enumerates all 2^17 necessary
center/noncenter flags, and measures (D2)'s effect on J=15. Center flags
mean that center 1 is selected whenever it is available. Noncenter flags
are only necessary residue conditions, so retained masks form a superset
of actual rational counterexamples. No mask is asserted to lift to Q_p
or Q. The exact finite output and job metadata are separate artifacts.

The completed ordinary-coefficient check took 0.350 seconds under a
20-second external timeout (child PID 28679). Of the 461 J=15 masks,
392 lack all three low-order center flags and 69 are retained. The
disjunction also retains 73 at J=17 and 88 at J=16, agreeing with the
earlier necessary conditions. Combining this **unverified** extra filter
with the separate exact exclusion of all J=17 families would reduce the
earlier 1164 masks to 772. Neither this arithmetic nor the existence of
772 surviving necessary masks settles any polynomial degree.

This is a necessary-condition theorem, not a proof of rational-witness
Casas-Alvero in degree 20. Unrestricted J<d/2 is outside this supporting
line argument. Neither a larger search nor an unproved claim of absence
of CA polynomials in characteristic 19 at degree 6 is substituted for it.
