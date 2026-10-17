# Reviewed finite odd-support obstruction and scoped applications

**Proved, independently reviewed partial results PN1–PN4**,
2026-10-17 UTC. Both fresh initially blind whole nonconstructor
audits and coordinator reconciliation are complete. Both reviewers
independently reconstructed all64 cases BY HAND, each with an explicit
complete alternative certificate, then the derivative/Taylor and exact
accepted-dependency applications. No substantive objection or author
repair remains. Root read both complete reports, issue ledgers and
source checks and verified the frozen integrity records.

PN1 classifies the two first-endpoint supports in the exact six-optional-
index class; PN2 excludes the joint endpoint modulo19². PN3/PN4 retain
the full normalized rational-witness J15 multiplicity-two, center,
parity, repeated-root ladder and actual H18 witness qualifications.
No full J15, mask, repeated-root branch, degree20 or annual solution
is accepted. Novelty remains unestablished. The constructor's small
probe is provenance/diagnostic evidence, not an independent audit.

The historical unverified body follows unchanged as an exact byte suffix.

---

# Exact odd-support endpoint obstruction in the J15 branch

**Candidate proof - unverified**, coordinator, 2026-10-17 UTC.
This is a finite arithmetic lemma and two scoped applications of the
already reviewed PP1/PP2. Two fresh initially blind nonconstructor
whole audits, including independent reconstruction of the finite
table, are required. No full degree20 or annual classification,
rational lift, or novelty is claimed.

## PN1--PN2. The finite lemma

For a subset I of {1,3,5,7,9,11,13,15} containing1 and15, define
integers b_0,...,b_15 by b_0=1, b_j=0 outside I, and

    b_j=-sum_(k<j) binom(j,k)b_k when j is in I.

Put F_I(Z)=sum_(j=0)^15 b_j binom(Z,j). All its coefficients
are19-integral since15! is a19-unit. The exact integer recursion
is equivalently the following operator when a new largest index j
is added:

    T_j F(Z)=F(Z)-F(j)binom(Z,j).

The following finite statements hold as CANDIDATES:

**PN1.** If F_I(17)=0 mod19, then I is either
{1,3,5,7,15} or {1,3,5,7,11,15}. In both cases its coefficient
vector modulo19 is

    b_0=1,b_1=-1,b_3=2,b_5=3,b_7=6,b_15=11,
    every other b_j=0.

The second support has b_11=0 mod19 and therefore fails the actual
nonzero-coefficient condition of reviewed PP1.

**PN2.** There is no I in this class with both

    F_I(17)=0 mod19 and F_I(20)=0 mod19^2.

The nonzero-coefficient condition is unnecessary for PN2.

### Complete finite proof certificate

Work modulo19. Let J=I intersect{1,3,5,7}, F=F_J, and write
f_z=F(z). Put a=1 if9 is in I, b=1 if11 is in I, c=1 if13
is in I, and otherwise put the respective indicator0. Index15
is always added last. Expanding the four operators gives exactly

    F_I(17)=f_17-3f_15+6c f_13
             +b(3+7c)f_11
             +a(15+6b+4c+14bc)f_9.                 (1)

Here is a derivation, so the last three indicators are not an
unjustified lookup. Before adding11, its evaluation is
g_11=f_11+2a f_9, using binom(11,9)=17 mod19.
Before adding13 it is
g_13=f_13-2b f_11-a(12+4b)f_9.
Before adding15 it is

    g_15=f_15-10c f_13+b(3+c)f_11
           +a(11+6b+6c+2bc)f_9.

The needed Pascal residues are binom(13,9)=12,
binom(13,11)=2, binom(15,9)=8, binom(15,11)=16,
binom(15,13)=10. Finally binom(17,9), binom(17,11),
binom(17,13), binom(17,15) are9,7,5,3. Substitution into
f_17-9a f_9-7b g_11-5c g_13-3g_15 gives (1).

Starting from F_{1}=1-Z and applying T_3,T_5,T_7 when selected
gives the following eight prefix vectors. The row label lists
the indicators of3,5,7 in that order; all entries are residues0--18.

|3,5,7|f_9|f_11|f_13|f_15|f_17|
|---|---:|---:|---:|---:|---:|
|000|11|9|7|5|3|
|001|18|13|5|7|12|
|010|2|14|6|9|17|
|011|6|0|13|2|14|
|100|8|16|9|3|14|
|101|3|5|5|7|13|
|110|6|15|13|6|15|
|111|13|0|11|8|5|

For a further explicit check of how to reproduce this small table:
T_3(1-Z)=1-Z+2binom(Z,3), T_5(1-Z)=1-Z+4binom(Z,5),
and T_7(1-Z)=1-Z+6binom(Z,7). The general T_j rule, in
increasing order of j, supplies every remaining row, with no
descent-polynomial conjecture or opaque recurrence solver.

Substituting these eight vectors into (1) gives ALL64 possibilities:

|3,5,7 \ 9,11,13|000|001|010|011|100|101|110|111|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|000|7|11|15|6|1|11|18|17|
|001|10|2|11|18|14|2|9|17|
|010|9|7|13|14|1|7|17|16|
|011|8|10|8|10|3|10|1|16|
|100|5|2|15|10|11|2|12|18|
|101|11|3|7|15|18|3|13|18|
|110|16|18|4|16|11|18|16|3|
|111|0|9|0|9|5|9|7|3|

Only the two stated positions vanish. The direct recursion at
these two supports gives the same residues displayed in PN1;
adding11 in the second position has zero coefficient modulo19.
This proves PN1 by an explicit exhaustive finite certificate,
not by extrapolation from sample cases.

For either vector,

    F'_I(1)=-1-[2/6+3/20+6/42+11/210]=-1 mod19,

since the four bracket terms are13,3,11,11, whose sum is0
mod19. For each odd j>=3 the derivative of binom(Z,j) at1
is -1/[j(j-1)], which gives that displayed formula. Every
denominator is a19-unit. Also F_I(1)=0 exactly, by b_1=-1.
Taylor expansion over Z_(19) therefore gives

    F_I(20)=19 F'_I(1) mod19^2.

Thus F_I(20) is NOT0 mod19^2 in either of the two possible
first-endpoint cases. PN2 follows.

## PN3--PN4. Exact applications of accepted PP1/PP2

The accepted register proofs/reviewed-return-r3-v1.1.md covers
the frozen parity packet, SHA-256
6506e371c2a3eb8506f75c55ef3d80be9933ecbcd187be21fe5bd18932fe8789,
including PP1 and PP2. Its historical unverified labels are superseded
only in that register's stated partial scope.

**PN3.** In that normalized rational-witness J15 multiplicity-two
setting, the hypotheses

    H3(f)(1)=0 and a_j=0 mod19 for every even j=2,4,...,18

cannot hold simultaneously. Indeed PP1 produces precisely an I
in the finite class above with both endpoint divisibilities.
The scalar factor F_I=(-1)^|I| d(I;Z) is a unit sign and changes
neither divisibility. PN2 gives the contradiction. Hence if
H3(f)(1)=0, at least one even normalized coefficient is a19-unit.
This is a restriction, not the exclusion of every J15 case.

**PN4.** The explicitly scoped repeated2R-root setting in PP2
cannot have both the exact even ladder H6(r)=H8(r)=...=H14(r)=0
and an actual rational noncenter H18 common witness. PP2 proves
that those hypotheses imply precisely the two hypotheses of PN3.
This excludes that conjunction only. A single center equation,
a merely local root, a different multiplicity mask, or a general
repeated-root branch is not silently included.

## Computation, provenance and limits

The construction began with a counterexample/intuition probe of the
explicit unresolved PP1 endpoint obstruction, not a larger mask or
rational-lifting search. The saved standard-library script visits
all64 supports, calculates exact integer b_j,F_I(17),F_I(20), and
independently checks the derivative/Taylor residue identity at each.
It found the two first-endpoint supports and no joint endpoint.
Child PID90921 had an external10-second timeout, exited0, and
was reaped after0.050045791seconds. Full output and records remain.
An inline formatting calculation also reconstructed the eight prefix
vectors using the same explicit binomial recursion. That calculation
is construction work, not an independent review.

The proof above supplies the hand-reconstructible operators, residues
and complete table. It must receive two independently reconstructed
whole audits before promotion; the saved program alone does not
promote PN1--PN4. The already accepted barrier PB1 is consistent:
it is exactly PN1's valid first-endpoint vector and fails the
second endpoint. No earlier version or failed approach is overwritten.

MacMahon descent polynomials and their Casas--Alvero connection
remain attributed as in the accepted PP1 source record; no novelty
is asserted for that connection. The new finite lemma uses only
the displayed binomial recursion. It does not establish degree20,
the annual classification, all remaining684 necessary masks, or
existence/nonexistence of a characteristic-zero rational lift.
