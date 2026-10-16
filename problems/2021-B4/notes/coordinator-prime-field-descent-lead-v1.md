# Rational recycled witnesses and prime-field descent

2026-10-16 UTC. **Candidate lemma / research lead - unverified.**
No complete degree or new classification is claimed. This is separate
from the degree20 exact-family packet and is not one of its dependencies.

Proposed lemma: for any prime p, a nontrivial rational-coefficient
Casas-Alvero polynomial with rational recycled witnesses can be affinely
normalized over Q so that its reduction is a nontrivial degree-d Hasse
CA polynomial over F_p, with every reduced witness in F_p. There is also
an integral vector of binomial-normalized coefficients giving all
normalized derivative equations before reduction.

Proof sketch to audit: translate a chosen rational common root of f,f'
to0 and make f monic. From a fixed finite rational covering set, choose
a nonzero witness alpha of smallest p-adic valuation and scale x by
alpha, with the corresponding monic output scaling. The covering set
now consists of p-integral rational numbers and contains0 and1.
Write f=sum_(j=0)^d binom(d,j)*a_j*x^(d-j), a0=1, a_d=0.
The normalized degree-j derivative is

    D_j=sum_(k=0)^j binom(j,k)*a_k*x^(j-k).

Induction on j=1,...,d-1, using an integral rational common witness of
D_j and f, gives a_j in Z_(p); the coefficient of a_j is1. Consequently
f is monic integral as well. Its reduction has roots0 and1, so cannot
be a pure power of a linear polynomial. Hasse differentiation and
integral evaluation commute with reduction, retaining every common-root
condition. All reduced witnesses are F_p-rational. Binomial-normalized
D_j equations must be reduced from their integral coefficient expression,
never by dividing by binom(d,j) in F_p.

The nonzero recycled witness exists because a singleton covering set
forces a pure power. Other roots of f need not initially be rational or
chosen for this minimum; their integrality follows afterwards from the
monic integral polynomial. A finite field extension is therefore not
needed for this particular normalization. These points require independent
audit before this lemma is used as a proved input.

A possible approach is to find a prime field with no such nontrivial
rational-witness residue system in a target degree. Ordinary Hasse
conditions alone can be too weak. For example, degree20 over F2 admits
F(T)=T^20+T^4: its only nonzero Hasse derivatives below20 are orders4
and16, with common witnesses1 and0 respectively. It has roots0 and1
and is nontrivial. Its normalized residue vector a16=1 and all other
a_j=0 also supplies a witness0 or1 for every D_j. Thus even the stronger
first residue system is not automatically contradictory in degree20.
This is a finite-field obstruction to that first-level test, not a
characteristic-zero counterexample or a lift over Q_2.

Next work should examine additional primes or higher congruence structure,
and check existing literature on rational recycled witnesses. Merely
enlarging a finite integer-witness height box does not address the issue.
No novelty is asserted for this standard-looking descent argument.
