# Reviewed attributed finite-range first-case corollary

**Proved, independently reviewed partial corollary CF1**,
2026-10-17 UTC, with EXPLICITLY ATTRIBUTED published inputs.
Both fresh initially blind whole nonconstructor audits and coordinator
reconciliation are complete. Every new substitution, coprimality, residue,
relative/minus-rank and threshold inference was reconstructed. Both
primary theorem statements and their exact finite-range interfaces
were checked. No substantive objection or author repair remains.

The imported Mihailescu theorem proof (including its Eichler/Washington
inputs) and HHO's published large computation were NOT reconstructed
in full or rerun. This accepted corollary retains that dependency
boundary. It says only: for prime101<=p<2^31, |x|>=2 and
G_p(x)=y^p over the integers, x is0 or−1 modulo p. The two
residual classes and the general2025 classification remain open.
Theorem4, appendix/upper-bound repairs and binary-Thue results
are unused; the separate inspection note is not an accepted source
objection or theorem refutation. Novelty is unestablished.

The original complete candidate body follows byte-identically;
historical unverified labels are superseded only on this scope.

---

# Diagonal first-case exclusion from published class-group inputs

**Candidate proof - unverified**, coordinator, 2026-10-17 UTC.
Two fresh nonconstructor initially blind whole audits are required.
This is an attributed consequence of published inputs, not a new
proof of those inputs, an unrestricted classification, or a novelty claim.

Our term count is m=n+1, where n is the official degree. Consider

    G_p(x)=1+x+...+x^(p-1)=y^p,
    p prime, 101<=p<2^31, |x|>=2.

## Imported inputs and exact reading boundary

Mihailescu's [diagonal chapter](https://doi.org/10.1007/978-3-211-74280-8_15),
Theorem 1 (author-posted version2.0, 2007-09-17, printed pp2--3),
gives r>sqrt(p)-1 for coprime integers X,Y,Z satisfying
(X^p+Y^p)/(X+Y)=Z^p and p not dividing XY(X^2-Y^2).
Here r is the p-rank of the relative cyclotomic class group.
The full statement and its Section3 explanation were read in the
[author upload](https://www.researchgate.net/publication/226863681_Class_Number_Conditions_for_the_Diagonal_Case_of_the_Equation_of_Nagell_and_Ljunggren).
The proof invokes Eichler/Washington, and is not reconstructed here.
The later singular-system repair concerns an upper bound, not this input.

Hart--Harvey--Ong, [Irregular primes to two billion](https://arxiv.org/html/1605.02398v1),
Introduction items(2)--(3) and Table2, report that for every odd prime
p<2^31, the cyclotomic class group's p-part is (Z/pZ)^(i_p), with
i_p<=9, and Vandiver holds. These are published finite calculations,
not rerun here and not an assertion of unrestricted Vandiver.

## CF1. Exclusion outside the second-case residues

Under the published inputs above, a solution in the stated range
must satisfy x=0 or -1 mod p. In particular there is no solution
with x mod p outside {-1,0,1}; the residue1 is excluded separately
by elementary LTE.

Proof. If x=1 mod p, the accepted signed odd-prime LTE formula gives
v_p(G_p(x))=1. This cannot equal p v_p(y). Thus x!=1 mod p.

Suppose also x!=0,-1 mod p. Set X=x, Y=-1, Z=y. Since p is odd,

    (X^p+Y^p)/(X+Y)=(x^p-1)/(x-1)=G_p(x)=y^p.

The denominator x-1 is nonzero since |x|>=2. Integers X,Y,Z
are pairwise coprime: Y is a unit, and G_p(x)=1 mod x gives
gcd(x,y)=1. Further,

    XY(X^2-Y^2)=-x(x^2-1)

is not divisible by p by the three excluded residues. The published
Theorem1 therefore applies to this signed solution, giving
r>sqrt(p)-1. No positivity of x has been assumed or needed.

The relative p-primary class group is the minus direct summand of
the p-primary class group. One can also describe it as the kernel
of the norm to the maximal real subfield: extension composed with
norm is1+c, while norm composed with extension is multiplication
by2; p is odd. The idempotents (1+c)/2 and (1-c)/2 thus give the
plus/minus splitting on this finite p-group. In particular its
p-rank is at most the rank of the entire p-part. Under the HHO
input that part is the elementary abelian group (Z/pZ)^(i_p),
so r<=i_p<=9. (HHO's verified Vandiver also makes its plus part
zero, but this equality is unnecessary for the upper bound.)

For p>=101 one has sqrt(p)-1>9. This contradicts r<=9 and
r>sqrt(p)-1. It excludes every remaining first-case solution
and proves CF1, with exactly the imported-theorem boundary stated.

## What this does not prove

Residues x=0,-1 mod p remain unresolved by CF1. Invoking the
chapter's second-case Theorem4 would require auditing its separate
upper-bound/repair interface. It is not a premise here. No step
above applies Bartolome--Mihailescu's binary-Thue Theorem1.2 with
an unverified parameter condition gcd(p,phi(rad B))=1.

No statement about p<101, p>=2^31, off-diagonal exponents, composite
term counts, or full B4(b) follows from CF1 alone. No claim that
this finite-range consequence has never appeared before is made.
Searches for Nagell-Ljunggren together with2^31,2147483648 and
two billion found no usable additional primary source in this return;
that unsuccessful search does not establish priority or absence.

No new mathematical computation, prime table, class-group calculation
or numerical check was run. The finite calculation is the cited
published input. Administrative hashes are not mathematical evidence.
