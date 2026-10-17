# An exact mirrored repeated-root subfamily cannot satisfy the full witnesses

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
review_2021_reasoning_j15_r2. This separate supplement preserves the
earlier reasoning-return-r3 candidate bytes. Requested gpt-6.1-sol/max;
independent effective readback unavailable. Two fresh independent
nonconstructor whole audits are required. No complete J15 mask,
nonunit branch, degree20 or annual classification is excluded.
No novelty is claimed. No enumeration, CAS or mathematical program
was used; the six symbolic cases below are part of the hand proof.

## Precise proposed exclusion

Use the accepted J15 multiplicity2, sole-H3 D3 setting from
reviewed-reasoning-J15-v1.1.md. In particular, f is monic degree20 over Q,

    f=X20-20X19+sum_(j=2)^18 binom(20,j)a_j X^(20-j),
    a_j in Z_(19), f(0)=f'(0)=f(1)=0,

and r is the rational simple small root sharing H2,H4. The other
two small slots have residues2R after scaling by19^nu, where
nu=v(r)>=1 and R=r/19^nu mod19.

**Proposed M1.** There is no full rational-witness polynomial in this
setting for which BOTH the following additional conditions hold:

    the other two small roots are exactly2r,2r;
    H6(f)(r)=H8(f)(r)=H10(f)(r)=H12(f)(r)=H14(f)(r)=0. (M)

The EXACT equality2r is essential. Accepted D3 asserts only the
repeated residue2R, not(M). The extra even derivative equations
are also not automatic. Thus M1 is a strict subfamily exclusion,
not a new exclusion of any entire accepted leading pattern.

These hypotheses include the previously accepted explicit low-order
barrier family, and also allow a general degree14 even part in its
residual factor. M1 uses actual rational witnesses for the TOP three
derivatives, not an assumption about all unused roots being rational.

## 1. Exact reflection fixes H16 and H18 at r

Set F(T)=f(r+T), h_k=H_k(f)(r), and E(T)=(F(T)+F(-T))/2.
f(r)=0, H2(r)=H4(r)=0 and(M) imply

    E(T)=h16 T16+h18 T18+T20.

Both0 and2r are double roots. Hence E(r)=E'(r)=0.
Since r!=0, division by r16 and r15 gives

    h16+h18 r2+r4=0,
    16h16+18h18 r2+20r4=0.

Subtracting16 times the first equation yields

    h18=-2r2, h16=r4.                                (1)

Equivalently E(T)=T16(T2-r2)^2. Nothing here divides by a difference
of the two equal roots, and no conclusion is drawn merely from
their residues.

For the normalized derivatives use

    D2=X2-2X+a2,
    D3=X3-3X2+3a2 X+a3,
    D4=X4-4X3+6a2 X2+4a3 X+a4.                       (2)

The plus sign in4a3 X is important. H18=190D2 and H16=4845D4.
Writing h=96/95, equation(1) gives exactly

    a2=2r-h r2,                                     (3)
    a4=r4/4845-r4+4r3-6a2 r2-4a3 r.                (4)

Since v(h)=-1, v(4845)=1 and nu>=1, (3) has v(a2)>=1.
All terms of(4) have positive valuation, even if a3 is a unit;
thus a4 is also nonunit.

The rational roots of f are exactly0,1,r,2r. Indeed removing their
rational factors X2(X-1)(X-r)(X-2r)^2 leaves the local degree14
Eisenstein factor as a polynomial over Q. Its fractional valuations
exclude rational roots. This elementary division is explicit;
no rationality of a general local factor is assumed.

## 2. A unit a3 is impossible

Suppose a3 is a19-adic unit. D3 has no zero in19Z19 because its
reduction there is a3. The rational common witness for H17 must
therefore be1. D3(1)=0 gives

    a3=2 mod19.                                    (5)

D4 has a4 nonunit and linear coefficient4a3 a unit. For x,y in19Z19,

    v(D4(x)-D4(y))=v(x-y).

But D4(r)=r4/4845 has valuation4nu-1>nu. Thus D4 is nonzero at r,
and at x=0 or2r its unit linear difference from D4(r), of valuation
nu, cannot cancel that higher-valuation value. None of0,r,2r is
an H16 common witness. H16 must also use1. Its equation reduces to

    -3+4a3=0 mod19, so a3=15 mod19,

contradicting(5). Hence a3 is nonunit.

It follows that D2(1)=-1, D3(1)=-2 and D4(1)=-3 modulo19.
None of H18,H17,H16 can use the center. By(1), H18 and H16
cannot use r either. Their rational witnesses therefore satisfy

    H18:0 or2r; H17:delta*r,delta in{0,1,2};
    H16:eta*r,eta in{0,2}.                          (6)

These exhaust actual rational roots. No Q19-only root is selected.

## 3. H18 leaves two exact values of r

Using(3) in D2(0)=0 or D2(2r)=0 gives respectively

    r=95/48 or r=95/142.                             (7)

Both have valuation1. Their scaled residues R=r/19 mod19 are

    R=10 or R=9,                                   (8)

because r/19=5/48 or5/142, whose denominators reduce to10 or9.
The first exact value is greater than1, the second less than1.

## 4. Six symbolic H17/H16 cases

For delta in{0,1,2}, D3(delta*r)=0 gives

    a3=3delta(delta-2)r2+delta(3h-delta2)r3.          (9)

Eliminate a4 using(4), and set D4(eta*r)=0 with eta=0 or2.
After division by r3 and insertion of(3),(9), this is

    C(delta,eta)+r A(delta,eta)=0,                  (10)

where

    C=4(1-eta3)+12(eta2-1)+12delta(delta-2)(eta-1),
    A=eta4-1+1/4845-6h(eta2-1)
        +4delta(3h-delta2)(eta-1).

For clarity these are ordinary powers, so eta4 means eta^4, etc.
All algebra in(10) is exact over Q. Since19h=96/5=4 mod19 and
19/4845=1/255=12 mod19, its leading reduction is

    C+R*(19A)=0 mod19,
    19A=36-24eta2+48delta(eta-1) mod19.

The resulting necessary R values, computed by division by the
nonzero displayed coefficient, are:

| eta | delta0 | delta1 | delta2 |
| --- | --- | --- | --- |
| 0 | 15 | 13 | 10 |
| 2 | 9 | 6 | 4 |

For verification, when eta=0 the pairs(C,19A) modulo19 are
(11,17),(4,7),(11,16); when eta=2 they are
(8,16),(15,7),(8,17). These six pairs completely reproduce the table;
all denominators are nonzero. This is the proof's exact six-case
certificate, not a computational search.

Comparing with(8), only two cases survive:

- eta=0,delta=2,R=10, so H18 requires r=95/48;
- eta=2,delta=0,R=9, so H18 requires r=95/142.

## 5. The two exact comparisons contradict H18

For eta=0,delta=2, equation(10) has

    C=-8, A=31-18h+1/4845=62068/4845.

It requires r=9690/15517<1, contrary to95/48>1.

For eta=2,delta=0, equation(10) has

    C=8, A=15-18h+1/4845=-15452/4845.

It requires r=9690/3863>2, contrary to95/142<1.

No actual rational r remains. This proves proposed M1 subject to
the two independent audits. It uses only the normalized degree2,
degree3 and degree4 derivative equations, the exact reflection
relations and their actual rational witness options.

## What remains and relation to the earlier candidate

The earlier G1/G2/C1/C2/W packet is NOT a proof dependency of M1.
M1 uses accepted D1/D3 and the normalization, and explicitly handles
the rational residual quotient only when all three small slots are
given rational. Its top-derivative witness split is reconstructed
directly, not inferred from a leading mask.

The accepted low-order family has centered odd factor
T(T2-r2)^2 and residual odd part T15, so its even part is exactly
T16(T2-r2)^2 and(M) holds. M1 confirms that such a family cannot
be a full rational-witness counterexample, consistent with its
original explicit low-order-only status. It does not assert a
failure of any of its stated low-order properties.

A repeated root s=t with s/r=2 mod19 but s!=2r is outside M1.
So are polynomials with an earlier nonzero even derivative at r.
The general tied-weight problem and actual higher witness equations
remain unresolved. No full degree, mask or nonunit branch is closed.

