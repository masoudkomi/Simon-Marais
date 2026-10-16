# Leading restrictions for J=15 with a triple root at zero

2026-10-16 UTC. **Candidate proof — unverified.** Constructor: coordinator.
Only the multiplicity-three subcase of rational degree 20 is considered.
No entire J=15 center mask is removed from the accepted 772-mask cover:
its multiplicity-two case remains. Two independent full audits are
required for every new deduction below. No novelty is claimed.

Accepted T3 gives the complete rational root set {0,1,u,v}, with u,v
distinct simple small roots, and f=x³(x−1)(x−u)(x−v)g, where g is
degree 14 and Eisenstein at 19. Write B=(x−1)g. Its constant coefficient
b₀ has valuation one; b₁,b₂ have valuation at least one. Hence

    c₃=b₀uv,
    c₄=−b₀(u+v)+b₁uv,
    c₅=b₀−b₁(u+v)+b₂uv.

Put ν=min(v₁₉(u),v₁₉(v)), u=19^ν U, v=19^ν V. With
c_(20−j)=binom(20,j)a_j and β_j=binom(20,j)/19, these identities give

    v₁₉(c₅)=1,  v₁₉(a₁₇)≥2ν,  v₁₉(a₁₆)≥ν,
    β₁₆ a₁₆/19^ν + β₁₅ a₁₅(U+V)=0 mod19.

Also a₁₈=0 exactly because zero has multiplicity three.

If the valuations differ, the two width-one small-root Newton edges
have exponent endpoints (3,4) and (4,5). The accepted width-one lemma
excludes both small roots as witnesses for H₃ and H₄. Neither derivative
vanishes at zero: c₃≠0 and c₄ has a unique term of smallest valuation.
Thus both H₃(1) and H₄(1) must vanish.

If the valuations agree, both residues U,V are nonzero. Rescaling
by c₅19^(5ν) reduces f(19^ν T) to T³(T−U)(T−V). Its H₄ values
at 0,U,V are −(U+V), 4U−V, 4V−U. H₃ cannot use zero since c₃≠0;
its other values are 3U(2U−V), 3V(2V−U). Consequently:

- If only H₃ has the center witness, require U+V=0 or 4U−V=0 or 4V−U=0.
- If only H₄ has the center witness, require 2U−V=0 or 2V−U=0.
- If neither has the center witness, the possible ratios V/U from
  the first list are {18,4,5}, and from the second {2,10}; they are
  disjoint in F₁₉. This subcase is impossible.

No distinctness of reduced residues was presumed. When both center
equations hold, one residue may be zero; unequal valuations remain
in the finite cover.

For each of the 69 accepted J=15 masks, define the exact ordinary
normalized recursion a₀=1,a₁=−1 and

    a_j=−Σ_(h<j) binom(j,h)a_h w_j^(j−h),  2≤j≤18,

where w_j=1 for a center bit and otherwise 0,u,v. Let a_j⁰=a_j(0,0)
and A_j,B_j be the coefficients of u,v modulo 19. They obey the same
triangular first-order recursion as in the earlier J=16 constructor;
this is explicit method reuse, not independent verification.

Set q₀=−1+Σ β_j a_j⁰. Every nonconstant monomial at (u,v) has a
factor 19^ν. The center-root equation therefore forces
ν≤v₁₉(q₀) whenever q₀≠0. The exact finite calculation finds nonzero
q₀ for all masks: 61 have bound one, six bound two, and two bound four.
For each ν within its bound, require divisibility of a₁₆⁰,a₁₇⁰,a₁₈⁰
by q=19^ν. Four necessary affine equations are

    q₀/q + Σ β_j(A_j U+B_j V)=0,
    a₁₈⁰/q + A₁₈U+B₁₈V=0,
    a₁₇⁰/q + A₁₇U+B₁₇V=0,
    β₁₆ a₁₆⁰/q +(β₁₆A₁₆+C₅)U+(β₁₆B₁₆+C₅)V=0 mod19,

where C₅=β₁₅a₁₅⁰ modulo 19. The third equation is a deliberately
weaker consequence of v(a₁₇)≥2ν when ν>1. At least one residue is
nonzero, and the preceding low-derivative conditions must also hold.

Only noncenter positions with a_(j−1)⁰ a 19-adic unit need labels for
this first-order test; other choices have identical zero linear term.
Every full assignment projects to one of these choices. For a later
full assignment we can always choose zero at a noncenter H₂ index
j=18, since its multiplicity-three zero is an available witness.
Center assignments retain their original equation and a₁₈=0 constraint.

The bounded constructor visits all 69 masks and 6,570 projected
label/valuation cases, testing all 361 residue pairs per eligible case.
It leaves 23 masks in this subcase, 298 leading branches (296 at ν=1,
two at ν=2). Restoring all inactive labels, with the described H₂
choice, would give 63,954 full keys. Neither this expansion nor any
higher-digit exclusion has yet been run in this note's version.

The full projection child PID 54286 finished in 1.654 seconds, exit 0,
under a 30-second external cap and was reaped. Source, exact equations,
every passing branch, result and flushed output are saved under
computations/coordinator-J15-triple-leading-v1*. This is constructor
evidence. No full J=15 or degree-20 exclusion is accepted.

Next approach: divide the formal polynomial with its c₂ term removed
by x³, take the monic-quadratic remainder R₁x+R₀, and combine
(f(1)/(19q),a₁₈/q,R₀/(19qβ₁₇),R₁/(19q)). The extra a₁₈ equation
ensures that an actual solution really has the removed coefficient zero.
An integral constant-Jacobian digit argument must be derived before
using this proposed system. This is a lead, not a proved continuation.
