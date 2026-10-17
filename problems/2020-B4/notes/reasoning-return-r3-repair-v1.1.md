# Full2020 return repair: prime-order fixed subgroup

2026-10-17 UTC. **Candidate proof - unverified.** Constructor author
repair for2020R2-01; requested gpt-6.1-sol/max, effective readback
unavailable. Both initially blind whole audits froze before I read
their complete reports, issue ledgers and source checks. The original
candidate and both initials remain unchanged. Both affected reaudits
and coordinator resolution are required; the author does not promote.

## The substantive defect

F1 correctly fixes arbitrary T, H=G^T and E=D intersect H. But its
prime-order paragraph F4 subsequently introduced one element t and
counted its one/ell orbits while still using h,f,m for the common
fixed subgroup of all T. The count instead uses D^<t>. For a larger
T that can be a strictly larger set than D^T. This was a real
statement-domain error, not just an optional notation preference.
The first initial reviewer did not detect it; the second supplied
an actual difference-set counterexample. Both original reports are
preserved without retroactive correction.

## Exact retained counterexample

Take q=4,v=21,D={7,9,14,15,18} in Z/21Z. Its ten positive
undirected cyclic separations, with all pairs specified, are:

|pair|separation|
|---|---:|
|7,9|2|
|7,14|7|
|7,15|8|
|7,18|10|
|9,14|5|
|9,15|6|
|9,18|9|
|14,15|1|
|14,18|4|
|15,18|3|

They are exactly1 through10, so all twenty nonzero ordered differences
are represented once. This verifies the actual difference-set property
by hand. Its sum is63=0 modulo21. Multiplication by2 cycles(7,14)
and(9,18,15), so D is fixed setwise by T=<2>. The powers of2
are2,4,8,16,11,1; its order is6. The common fixed subgroup has
size gcd(2-1,21)=1, hence H={0}, E empty and f=0.

For t=8 of order2 the old literal h=1 clause would assert5=0
modulo2, false. For t=4 of order3 it would assert5=0 modulo3,
also false. This uses the same D and same absent singleton0;
inconsistent singleton choices are not the problem.

The corrected fixed groups are exact:

    H_8={0,3,6,9,12,15,18}, E_8={9,15,18}, f_8=3,m_8=2;
    H_4={0,7,14}, E_4={7,14}, f_4=2,m_4=1.

Now5=3 modulo2 and5=2 modulo3, or q-m_8=2 and q-m_4=3,
as the corrected F4 requires. The order-one smaller difference set
for H_4 is expressly allowed and is not called a nondegenerate plane.
This finite example diagnoses the false quantifier; no preliminary(a)
existence construction or general scan is redone.

## Full versioned repair and proof

The complete new main copy keeps the arbitrary common T,H,E of F1
for the closure/subplane statements. For a known prime-order element
t it then explicitly defines

    H_t=G^<t>, h_t=|H_t|, E_t=D intersect H_t, f_t=|E_t|.

Apply the already proved F1 with T=<t>. If h_t>1, let m_t=f_t-1;
then h_t=m_t²+m_t+1. All t-orbits on D have size1 or ell,
and the size1 points are EXACTLY E_t. Thus |D|=f_t modulo ell,
which gives q-m_t=0 modulo ell. If h_t=1, f_t is the actual
membership of0 in D, giving q+1=f_t modulo ell. This singleton
membership is shared when different elements each have h_t=1.

The text explicitly prohibits substituting the possibly smaller common
H=G^T from a larger group into this congruence. It makes no orbit
congruence for D^T merely because t lies in T. The proof is complete
after this exact domain repair. No new arithmetic or geometric theorem
is imported.

The recursive-use sentence is also qualified: on a genuine smaller
E one resets all hypotheses in its group H, especially the order of
the restricted multiplier and that element's own fixed group. The
restriction of a prime-order original automorphism can be identity;
the original order is not blindly retained. This closes a downstream
version of the same quantifier issue without weakening valid closure.

## Every downstream use checked

|Part|Fixed group actually used|Effect of repair|
|---|---|---|
|F1 closure/F1-F3 size and subplane bounds|Arbitrary common H=G^T|Unchanged. Unique representing points are individually fixed by EACH t. No prime-order orbit congruence was used.|
|F1a cofactor and7p family|G^<p> for the known multiplier p|Unchanged conclusion. Now stated explicitly. p is a prime integer divisor of q, but its automorphism order need not be prime; only F1, not F4, is used.|
|F2 projections and fiber count|B=G^<t> for its one exact involution|Unchanged. The invocation of F1 now explicitly says T=<t>. The symmetric-fiber count,2R=a-1 and square factorization do not use F4.|
|F2 odd-order consequence/F2a coherence|Individual full-order elements and their halfway involutions|Unchanged. F2 gives the unique involution; no larger common fixed cardinality is inserted.|
|F3 relative trace|The SAME B for the specified involution|Unchanged. E=D intersect B, its actual count and half-map drive F11.|
|F3a sign-pair necessity and lift|That same involution-fixed B|Unchanged. The nonzero B difference invokes F1 for T=<t>, now made explicit. F15 remains a coefficientwise iff, not an orbit average.|
|B1 real and integral norm statements|No fixed subgroup or orbit count|Unchanged exact algebra.|
|Final prime-v/odd-order barrier|No F4 assertion for an arbitrary larger T|Unchanged. Nonidentity fixed group is trivial when v is prime, but any orbit test still needs its own actual action.|

No theorem beyond these existing scoped claims is added. The original
source attribution and missing raw-byte BBB hash remain as recorded;
neither source supplies a reason to restore the false general-T statement.
The nonsquare odd-multiplier branch and complete classification remain
open. Both reviewers must check this full copy, counterexample and
downstream ledger before coordinator acceptance.
