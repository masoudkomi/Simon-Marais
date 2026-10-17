# J15 double zero: the sole-H4 low-center pattern

2026-10-16 UTC. **Candidate proof - unverified.** Constructor: coordinator.
Two fresh independent nonconstructor whole audits are required. This is
an analytic residue classification, with no enumeration or CAS premise.
No full center mask, J15 case or degree 20 is excluded, and no novelty
is claimed. Only the rational-witness open part B4(b) is investigated.

## Scope and accepted dependencies

Use D1 and D2 from the accepted J15 double-zero packet
`../proofs/reviewed-reasoning-J15-v1.1.md`, and its explicit earlier
normalization/Newton/rational-cover dependencies. In particular

    f=X^2(X-u)(X-v)(X-w) B_res,
    B_res=(X-1)g,  deg g=14,

over Q19, where g is Eisenstein, all three nonzero small root slots are
in Q19, and at least two distinct small roots are rational over Q.
The third need not be rational over Q or eligible as a contest witness.
The normalized center 1 is simple; H_k denotes the k-th Hasse derivative.
Assume J=15, multiplicity two at zero, and

    H2(f)(1) != 0, H3(f)(1) != 0.

The full rational-witness hypothesis supplies noncenter rational
witnesses for H2 and H3. D2 implies that the three positive root
valuations are equal, say nu>=1: unequal valuations would force at
least two of H2,H3,H4 to vanish at the center. It also follows below
that H4 has no noncenter witness, so H4(f)(1)=0.

## Candidate conclusion

There is a unique small root r that can witness H2, and it is rational
over Q. Set R=r/19^nu modulo 19. Up to the order of the other two slots,
the small-root residue multiset and the only possible H3 witness are
exactly the following necessary possibilities:

| Case | Residues divided by R | Actual H3 witness |
| --- | --- | --- |
| I | {1,6,10} | zero |
| II | {1,12,16} | the same actual root r |
| III | {1,3,8} | the unique actual root whose residue is 3R |

All three residue slots are distinct in every case. In case III, the
root in the 3R slot is rational over Q because it is the actual rational
H3 witness. These are necessary residue patterns, not assertions that
any complete derivative mask or full Casas–Alvero polynomial lifts.

## Reduction to a split degree-five polynomial

The accepted local coefficient estimates imply that, after scaling the
small roots by 19^nu and dividing by the leading valuation, the initial
form is

    F(T)=T^2(T-U)(T-V)(T-W)
        =T^5-s T^4+t T^3-z T^2,

where U,V,W are nonzero in F19 and z=UVW is nonzero. Hasse scaling and
reduction preserve all necessary common-root equations. The fourteen
fractional-valuation roots cannot be rational witnesses; the only other
rational candidates are zero, the center, and the three small roots.

For a nonzero cubic root A, direct elimination of z gives

    H2(F)(A)=A(9A^2-5sA+2t),
    H3(F)(A)=10A^2-4sA+t,
    H4(F)(A)=5A-s.

Also H2(F)(0)=-z, H3(F)(0)=t, and H4(F)(0)=-s.
Thus H2's noncenter witness has a nonzero residue R. Divide all three
residues by R and rename this residue as 1. The formulas are homogeneous,
so this is legitimate. If x,y are the other two residues, then

    s=1+x+y, t=x+y+xy, 2t=5s-9.                 (1)

No root difference or possibly zero residue has been divided out.

## Exhausting the H3 witness

If H3 uses zero, its necessary residue equation is t=0. Equation (1)
gives s=9/5=17 in F19. Hence x+y=16 and xy=3. Their discriminant is

    16^2-4*3 = 16 in F19,

so {x,y}={6,10}. This is case I.

If H3 uses a small root reducing to 1, its equation is
10-4s+t=0. Together with (1) this gives 3s=11, hence s=10 and t=11.
Then x+y=9, xy=2, and their discriminant 9^2-8=16 gives
{x,y}={12,16}. This is case II. This calculation also covers a priori
the possibility that another slot had residue 1; its resulting roots
are distinct, so that possibility is eliminated rather than assumed.

Otherwise name the H3 witness residue x, with x!=1. Equation (1)
becomes

    2xy-3x-3y+4=0.

The denominator 2x-3 is nonzero: if it vanished, x=3/2 and the
remaining term would be -3x+4=-1/2, nonzero. Therefore

    y=(3x-4)/(2x-3).

The H3 equation at x is

    6x^2-3x+y(1-3x)=0.

Substitution gives, exactly before reduction,

    12x^3-33x^2+24x-4=0.

Over F19 its factorization is

    (x-3)(12x^2+3x+14)=0.                       (2)

The quadratic discriminant is 2 in F19, a nonsquare: the nonzero
squares are {1,4,9,16,6,17,11,7,5}. Its leading coefficient is nonzero.
Thus x=3 and then y=8. This is case III. This exhausts zero and every
small-root possibility for the actual H3 witness, including a priori
repeated slots or repeated residues.

## Exact witness identification and the H4 center

In each resulting case every residue occurs in exactly one root slot.
The residue equations have the following complete sets of roots within
{0,1,x,y}; the H2 column lists nonzero roots, since H2(F)(0)=-z:

| Case | (s,t) | Nonzero H2 witness residues | H3 witness residues | Root of 5T-s |
| --- | --- | --- | --- | --- |
| I | (17,0) | {1} | {0} | 11 |
| II | (10,11) | {1} | {1} | 2 |
| III | (12,16) | {1} | {3} | 10 |

Here the final column lies outside the small-root multiset in every
row, and s is nonzero, excluding zero for H4 as well. These entries
follow from the displayed quadratic and linear Hasse expressions. For
example, the second H2 root in cases II and III is respectively 13
and 12, outside their small-root multisets; in case I its only nonzero
root is 1. The second H3 root in cases I, II and III is respectively
3,3,17, also outside their multisets. No residue table search is used.

Consequently the actual H2 witness is the unique slot r. An actual
H3 witness in cases II and III is likewise determined by its single
slot, not just by equality of residues. In case I only zero can witness
H3; none of the nonzero small-root slots has a zero residue. All actual
witnesses are rational by the contest hypothesis. H4 has no noncenter
rational witness, so the hypothesis that every derivative has a
rational common root forces H4(f)(1)=0.

## Limits and use

The table sharpens the description of the sole-H4 low-center branch.
It does not prove that this branch is empty. In particular, it supplies
no odd-valuation contradiction analogous to the unit-a14 collision
case of D4: all three leading residues here are distinct. Additional
derivative equations or a global arithmetic obstruction are still needed.
Sole-H2 center patterns, multiple low center equations, the separate
triple-zero case, lower J, and the full annual question remain outside
this candidate. Two fresh whole adversarial audits must check the
finite-field algebra, exhaustive witness split, local versus global
root fields, accepted dependencies, and precise conclusion before any
promotion. No new computation, source import or native child was used.
