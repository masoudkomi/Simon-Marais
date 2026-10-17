# Reviewed J15 single-center residue classification

**Proved, independently reviewed (partial necessary conditions)**,
2026-10-16 UTC. Two fresh initially blind nonconstructor reviewers
reconstructed this whole argument. The coordinator read both complete
reports and issue ledgers, reconciled them and checked all frozen records.
No substantive objection or author repair remains. The unchanged frozen
body below retains its historical candidate label, superseded by this
scoped acceptance. No row is proved to lift or to be globally impossible;
no complete mask or degree20 is excluded. Novelty is unestablished.
See ../reviews/single-center-acceptance.md/json.

---

# J15 double zero: the sole-H2 low-center pattern

2026-10-16 UTC. **Candidate proof - unverified.** Constructor: coordinator.
This is separate from the sole-H4 note; neither depends on the other.
Two fresh independent nonconstructor whole audits are required. No
enumeration, CAS, complete-mask exclusion, degree-20 solution or novelty
is claimed. Only the open rational-witness B4(b) is investigated.

## Accepted input and proposed scope

Use D1 and D2 from the accepted double-zero J15 packet
`../proofs/reviewed-reasoning-J15-v1.1.md` and its recorded normalization,
Newton and rational-cover dependencies. There are three nonzero small
slots in Q19, at least two distinct ones in Q, besides double zero,
simple center 1, and fourteen fractional-valuation slots unavailable as
rational witnesses. The third small root need not belong to Q. Assume

    H3(f)(1) != 0 and H4(f)(1) != 0.

Both derivatives therefore have actual rational noncenter witnesses.
D2 forces the three small-root valuations to equal nu>=1: otherwise
at least two of H2,H3,H4 would use the center. The scaled initial form is

    F=T^2(T-U)(T-V)(T-W)=T^5-sT^4+tT^3-zT^2,
    U,V,W nonzero in F19, z=UVW nonzero.

At a nonzero cubic root A, direct elimination of z gives

    H2(F)(A)=A(9A^2-5sA+2t),
    H3(F)(A)=10A^2-4sA+t,
    H4(F)(A)=5A-s.

At zero these values are -z,t,-s. Accepted Hasse scaling and reduction
give necessary equations for the actual witnesses. The proposed complete
necessary residue patterns, up to common nonzero scale R and permutation,
are as follows:

| Case | Small residues divided by R | Actual H3 witness | Actual H4 witness |
| --- | --- | --- | --- |
| A | {1,7,11} | zero | zero |
| B | {1,8,15} | unique root r of residue R | same r |
| C | {1,7,16} | unique root of residue 16R | unique root r of residue R |
| D | {1,9,14} | unique root of residue 9R | unique root r of residue R |

In A, R can be any one small residue. All rows have three distinct
slots. In C and D both displayed distinct actual witnesses are rational
over Q; in B their common actual witness is rational. The third small
root is not presumed globally rational. H2 has no noncenter witness in
any row, so the full hypothesis forces H2(f)(1)=0. These are necessary
patterns, not claimed complete polynomial or mask lifts.

## 1. H4 using zero

Then s=0. If H3 also uses zero, t=0. The nonzero roots form the split
cubic T^3-z. Scaling one root to 1 makes the others the roots of
X^2+X+1, namely 7 and 11 in F19. Their sum is -1 and product 1;
characteristic 19 does not divide three. This gives A.

If H3 instead uses a nonzero root, scale it to 1. Its equation gives
t=-10=9. The other roots have sum -1=18 and product t+1=10, whose
discriminant is 18^2-40=18 in F19. This is a nonsquare, contradicting
splitting. The nonzero squares are {1,4,9,16,6,17,11,7,5}. Coincident
slots give no exception to a nonsquare discriminant.

In A, H3(F)(A)=10A^2 and H4(F)(A)=5A are nonzero at every nonzero
small root. Thus their actual witnesses are both zero. Also
H2(F)(A)=9A^3 is nonzero there and H2(F)(0)=-z is nonzero.

## 2. H4 using a nonzero small root

Scale its residue to 1 and write x,y for the other residues. Then

    s=5, x+y=4, xy=t-4.                         (1)

If H3 uses zero, t=0 and xy=-4=15; the discriminant of x,y is
16-60=13 in F19, a nonsquare. Thus H3 uses a nonzero small root.

If that residue is 1, its equation is 10-20+t=0, giving t=10.
Now x+y=4 and xy=6, with discriminant 11 and square roots +/-7.
Thus {x,y}={8,15}, giving B. This conclusion also eliminates any
a priori repeated slot of residue 1 rather than assuming it away.

Otherwise name the H3 residue x. Since y=4-x, (1) gives
t=4+4x-x^2. The H3 equation is

    9x^2-16x+4=0.                               (2)

Its discriminant is 17 in F19, with square roots +/-6. The denominator
18 is -1, giving x=16 or x=9. Respectively y=7,t=2 and y=14,t=16.
These are C and D. No root difference has been divided out. Zero,
the H4 residue 1, or another small slot exhaust the H3 witnesses.

## 3. Actual witness identification and the missing H2 witness

In B,C,D, H4=5T-5 has only the small-root zero 1 and its value at
zero is nonzero. H3 is 10T^2-20T+t. In B it has the double root 1;
in C its roots are 16 and 5; in D they are 9 and 12. The second roots
in C and D are outside the respective small-root multisets, and t is
nonzero in all three cases. Every allowed H3 witness therefore occupies
exactly the slot in the table. Slot uniqueness gives equality of actual
roots where claimed, rather than just equality of residues. The actual
witnesses are rational over Q by the contest hypothesis.

For H2, the equation at a nonzero small root is
9A^2-25A+2t=0. In B its discriminant is zero and its only root is
13, outside {1,8,15}. In C its roots are 8 and 18, outside {1,7,16}.
In D its roots are 3 and 4, outside {1,9,14}. The discriminants are
respectively 0,6,5 with square roots 0,+/-5,+/-9; the quadratic
formula uses the unit denominator 18. Zero fails because z is nonzero.
Case A was checked above. Thus H2 has no noncenter rational witness
and must use the center.

## Exact remaining gap

No row is claimed to lift to every derivative equation, and none is
excluded by this argument. All three leading residues are distinct, so
the repeated-residue parity obstruction in accepted D4 does not directly
apply. Additional equations or a global obstruction are needed. The
separate sole-H4 candidate and accepted sole-H3 result concern the other
single-center patterns and are not new dependencies here. Multiple low
centers, multiplicity three, lower J and degree 20 remain unresolved.
All new assertions need both fresh independent whole audits. No
computational experiment or new source import is a premise.
