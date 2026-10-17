# A sparse-support obstruction for the two descent endpoints

2026-10-17 UTC. **Candidate proof - unverified.** Constructor:
review_2021_reasoning_j15_r2. Requested gpt-6.1-sol/max; effective
readback unavailable. Two fresh independent nonconstructor audits are
required. This preserves the frozen parity packet. No enumeration,
CAS or mathematical program was used. No novelty is claimed.

## Precise arithmetic lemma SD1

Let I be a subset of{1,3,5,7,9,11,13,15} containing1 and15.
Let d(I;Z) be the published descent polynomial in the length
variable Z. Suppose

    d(I;-2)=0 and d'(I;1)=0 mod19.                 (A)

Then |I|>=4. All denominators are19-units because max I=15.
No nonvanishing-coefficient assumption is needed for this lemma.

Via the separately UNREVIEWED parity projection PP1, this would
force a putative polynomial in that explicitly stated parity
branch to have at least two additional unit odd normalized
coefficients among a3,a5,a7,a9,a11,a13, in addition to a1,a15.
That application is conditional on PP1 being audited; SD1 below
is an independent arithmetic statement and proves no full branch
or degree20 exclusion.

## Proof from the published recurrence

Use the classical recurrence, read in full as Proposition2.1 of
Diaz-Lopez--Harris--Insko--Omar--Sagan, arXiv1710.11033v2:

    d(J union{m};Z)=binom(Z,m)d(J;m)-d(J;Z),
    m>max J.

Define F_I=(-1)^|I| d(I;Z). Equivalently
F_empty=1 and

    F_(J union{m})(Z)=F_J(Z)-F_J(m)binom(Z,m).      (1)

This also follows directly by induction, so no conjecture about
descent polynomials or new computational table is imported.

The minimal possible I={1,15} has

    F_I(Z)=1-Z+14binom(Z,15).

Modulo19,

    F_I(-2)=3-16*14=7,

because binom(-2,15)=-16. Thus |I|=2 is impossible.
A set of size1 cannot contain both1 and15.

For size3 write I={1,k,15}, where
k is one of3,5,7,9,11,13, and let J={1,k}.
The initial recurrence gives exactly

    F_J(Z)=1-Z+(k-1)binom(Z,k),
    F_J(-2)=4-k^2,
    F'_J(1)=-(k+1)/k.                              (2)

For the derivative identity use
[d/dZ binom(Z,k)] at1=-1/[k(k-1)], since k is odd.

Applying(1) at m=15 and imposing(A) yields

    F_J(-2)+16F_J(15)=0,
    F'_J(1)+F_J(15)/(15*14)=0 mod19.               (3)

Eliminate F_J(15). Since15*14*16=-3 mod19, the result is

    F_J(-2)+3F'_J(1)=0.

By(2), multiplying by the nonzero k gives

    k^3-k+3=0 mod19.                              (4)

The cubic factors exactly modulo19 as

    k^3-k+3=(k-15)(k^2-4k+15).

The quadratic discriminant is16-60=-44=13 mod19.
The nonzero squares modulo19 are
{1,4,9,16,6,17,11,7,5};13 is not one of them.
Thus the only F19 root of the cubic is15, whereas our k is
different from15. This contradiction excludes size3 and proves
proposed SD1.

This is a symbolic exclusion of all six possible intermediate
indices at once, rather than six evaluations or a support table.
It does not decide any support with four or more indices.

## Scope and provenance

The descent polynomial, its recurrence, and the one-nonzero-
recycled-root/MacMahon relation are published; see the frozen
parity packet's primary source record. This addendum uses only
the explicit recurrence above, and rederives the endpoint
elimination and nonsquare obstruction by hand.

No assertion is made that(A) has no larger support, that the
coefficient nonvanishing conditions hold automatically, that
any residual pattern lifts to Q, or that all rational witnesses
can be replaced by zeros. The first general return, exact mirror,
collision-depth and parity packets remain candidate-unverified
until fresh independent audits and root promotion.

No shared/Git edits, contacts, charges, bypass, spawning or
separately billed API occurred. Weekly total remains23% with
reset1792745187 and90% total ceiling plus integration reserve.

