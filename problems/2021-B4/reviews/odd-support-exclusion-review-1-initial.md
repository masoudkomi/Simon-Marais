# PN1–PN4: initially blind whole review R1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol/max; verified effective settings unavailable.
This is an independent review recommendation for the new packet, not a
promotion of it or a fresh review of a dependency I authored.

I find no substantive defect in PN1–PN4 on their explicit domains. I
independently reconstructed the operator formula, every prefix and all 64
first-endpoint residues by hand, and checked the derivative, Taylor and
application steps. No constructor program or output was read or executed
for this reconstruction. The complete per-claim ledger and source record
are frozen with this report before any peer PN findings have been read.

## Independence and the exact accepted-dependency boundary

The coordinator authored the new finite lemma, its operator expansion,
eight-by-eight classification and the PN3/PN4 applications. I did not
construct or contribute those new arguments. I did author the earlier
PP1/PP2 parity projection and PB1 residue diagnostic. They have since been
accepted after two other fresh nonconstructor whole audits. I therefore
do not present this report as another independent review of PP1, PP2 or
PB1, and I do not count my prior construction as an independent audit of
them. Their accepted exact scopes are the dependency interface below.
The new exhaustive classification is independently reconstructed here;
recognizing the old PB1 vector alone would not verify that classification.

No peer PN report, issues, conclusions or findings was read before this
initial freeze. Existing acceptance of the dependencies is not peer
review of this new packet. No candidate, dependency, old review, shared
file or Git state was edited. No subagent was launched.

The exact new candidate is
`notes/coordinator-odd-support-exclusion-candidate-v1.md`, SHA-256
`a7845441df7725edc5d30e28f7b8f28c529b0b710168ad4b068d279582c1857c`.
The constructor freeze-v1 manifest has SHA-256
`337a43225bd6637d666bc992738a49afab8e7b569f526281add45564ab17b592`.
Its 13 listed records, including arithmetic-program artifacts whose bytes
are checked only for integrity, are preserved. The review's mathematical
certificate does not depend on those programs or their saved output.

## Finite domain, integrality and the operator

There are exactly six optional indices 3,5,7,9,11,13. Indices 1 and 15 are
mandatory. Thus there are exactly 2^6=64 subsets under consideration,
with no degree, prime, mask or lifting search hidden in the certificate.
For each I, b_0=1 and, for 1<=j<=15, b_j is zero when j is not in I,
and otherwise is minus the indicated integer binomial sum. This recursively
defines ordinary integers, without reduction choices or divisions.

Every binomial polynomial binom(Z,j) has denominator dividing j!, and
j<=15<19. Therefore F_I is in Z_(19)[Z]. It has degree at most 15 for
every support; the first-endpoint cases below have degree exactly 15
even modulo 19. No universal nonvanishing of b_15 has been presumed.

Suppose F represents the already selected smaller indices and j is newly
added as the largest index. Its old value F(j) is exactly the sum of the
old binomial coefficients at j. Adding b_j=-F(j) gives

    T_j F(Z)=F(Z)-F(j)binom(Z,j).

This is an exact rational-polynomial identity before reduction. At every
nonnegative integer h<j the added binomial is zero, so the earlier selected
integer roots are preserved. In particular I always contains 1 and
b_1=-1, hence F_I(1)=0 exactly, not merely modulo 19.

## Independent reconstruction of all eight prefixes

Begin with F_{1}=1-Z. In increasing index order, adding 3 gives b_3=2.
Adding 5 without 3 gives b_5=4; adding it after 3 gives

    b_5=-(1-5+2*binom(5,3))=-16=3 mod19.

If 7 is selected, the four possibilities according to the presence of
3 and 5 give respectively

    b_7=6,
    b_7=-(1-7+4*binom(7,5))=-78=17 mod19,
    b_7=-(1-7+2*binom(7,3))=-64=12 mod19,
    b_7=-(1-7+2*binom(7,3)-16*binom(7,5))=272=6 mod19.

Thus the eight prefix coefficient triples (b_3,b_5,b_7) are:

| Indicators 3,5,7 | b_3 | b_5 | b_7 |
|---|---:|---:|---:|
|000|0|0|0|
|001|0|0|6|
|010|0|4|0|
|011|0|4|17|
|100|2|0|0|
|101|2|0|12|
|110|2|3|0|
|111|2|3|6|

For an independent evaluation certificate, the required ordinary binomial
values, followed by their residues in parentheses, are:

| z | binom(z,3) | binom(z,5) | binom(z,7) |
|---|---:|---:|---:|
|9|84 (8)|126 (12)|36 (17)|
|11|165 (13)|462 (6)|330 (7)|
|13|286 (1)|1287 (14)|1716 (6)|
|15|455 (18)|3003 (1)|6435 (13)|
|17|680 (15)|6188 (13)|19448 (11)|

The unmodified vector 1-z at z=9,11,13,15,17 is (11,9,7,5,3).
Taking its linear combination with the three residue columns above and
the independently derived coefficient triples gives every row below:

| 3,5,7 | f_9 | f_11 | f_13 | f_15 | f_17 |
|---|---:|---:|---:|---:|---:|
|000|11|9|7|5|3|
|001|18|13|5|7|12|
|010|2|14|6|9|17|
|011|6|0|13|2|14|
|100|8|16|9|3|14|
|101|3|5|5|7|13|
|110|6|15|13|6|15|
|111|13|0|11|8|5|

For example row 011 uses (0,4,17), not three independent corrections
to the original base: its value at 9 is 11+4*12+17*17=348=6 mod19.
This checks the dependence of the coefficient at 7 on earlier choices.
All other rows were formed by the same displayed matrix multiplication,
not by copying an opaque recursion output. The matrix and coefficient
tables determine and verify all 40 prefix entries.

## Independent expansion for the last three indicators and index 15

Write a,b,c for the indicators of 9,11,13 respectively. The required
ordinary binomial integers, in a fixed order, are

    (C(11,9), C(13,9), C(13,11), C(15,9), C(15,11),
     C(15,13), C(17,9), C(17,11), C(17,13), C(17,15))
      =(55,715,78,5005,1365,105,24310,12376,2380,136).

Their respective residues are

    (17,12,2,8,16,10,9,7,5,3).

The operator at 9 changes the evaluation at 11 to

    g_11=f_11-17a f_9=f_11+2a f_9.

At 13, after both possible earlier operators, its evaluation is

    g_13=f_13-12a f_9-2b g_11
        =f_13-2b f_11-a(12+4b)f_9.

Before the mandatory operator at 15, its evaluation is

    g_15=f_15-8a f_9-16b g_11-10c g_13
        =f_15-10c f_13+b(3+c)f_11
          +a(11+6b+6c+2bc)f_9.

The final evaluation at 17 is therefore

    f_17-9a f_9-7b g_11-5c g_13-3g_15
      =f_17-3f_15+6c f_13
        +b(3+7c)f_11
        +a(15+6b+4c+14bc)f_9.                 (*)

In the coefficient of a f_9, the unreduced combination is
-42-32b+42c+14bc, whose reduction is the one displayed. This checks
the mixed bc term and not merely the three single-indicator terms.
All operator signs and index orders agree with the exact integer model.

## Reconstruction of all 64 residues

To independently simplify the eight-column computation, set

    A=f_17-3f_15, U=6f_13, V=3f_11, W=10f_11, D=f_9.

For columns abc in order 000,001,010,011,100,101,110,111, formula (*)
becomes exactly

    A,
    A+U,
    A+V,
    A+U+W,
    A+15D,
    A+U,
    A+V+2D,
    A+U+W+D.                                  (**)

In particular the 001 and 101 columns must coincide: when a=c=1,b=0,
the f_9 coefficient is 15+4=0 mod19. This is a check on the mixed
terms in (*), not an extra assumed symmetry.

Here are all the independently formed residue inputs for (**):

| 3,5,7 | A | U | V | W | 15D | 2D | D |
|---|---:|---:|---:|---:|---:|---:|---:|
|000|7|4|8|14|13|3|11|
|001|10|11|1|16|4|17|18|
|010|9|17|4|7|11|4|2|
|011|8|2|0|0|14|12|6|
|100|5|16|10|8|6|16|8|
|101|11|11|15|12|7|6|3|
|110|16|2|7|17|14|12|6|
|111|0|9|0|0|5|7|13|

Adding the eight expressions in (**) for each row gives all 64 outputs:

| 3,5,7 / 9,11,13 |000|001|010|011|100|101|110|111|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|000|7|11|15|6|1|11|18|17|
|001|10|2|11|18|14|2|9|17|
|010|9|7|13|14|1|7|17|16|
|011|8|10|8|10|3|10|1|16|
|100|5|2|15|10|11|2|12|18|
|101|11|3|7|15|18|3|13|18|
|110|16|18|4|16|11|18|16|3|
|111|0|9|0|9|5|9|7|3|

This verifies every entry in the target table with a distinct reduction
route after the operator expansion. As explicit checks, the first row is
(7,7+4,7+8,7+4+14,7+13,7+4,7+8+3,7+4+14+11) mod19; the last row is
(0,9,0,9,5,9,7,9+13) mod19. The intervening six rows are obtained from
the fully displayed auxiliary table, with no omitted cases.

The only zeros are prefix 111 with final indicators 000 and 010.
They mean exactly I={1,3,5,7,15} and I={1,3,5,7,11,15}. In the first,
the prefix coefficients are (2,3,6), no 9/11/13 correction is made,
and b_15=-f_15=-8=11 mod19. In the second, f_11=0, so the added 11
coefficient is 0 mod19 and the whole reduced polynomial remains the same,
including b_15=11. Together with b_0=1,b_1=-1 this is exactly PN1's
coefficient vector. It is not a claim that b_11 is the integer zero in the
second support. It is zero modulo 19 and violates PP1's actual-support
nonvanishing requirement. The first support has no such violation.

The classification PN1 itself did not impose that requirement, so excluding
the second support from PP1 does not justify omitting it from the finite
arithmetic lemma. It was included and checked above.

## Derivative, lifting modulo 19^2 and PN2

For j>=2, differentiating the product for binom(Z,j) at Z=1 leaves just
the factor where Z-1 was differentiated. The product of the other factors
is (-1)^(j-2)(j-2)!, hence the derivative is

    (-1)^(j-2)/(j(j-1)).

For odd j>=3 this is -1/(j(j-1)). The derivative for j=1 is 1, and
the constant term contributes zero. Since all the denominators in this
calculation are 19-units, either PN1 vector therefore gives

    F'_I(1)=-1-(2/6+3/20+6/42+11/210) mod19.

The four terms reduce independently to 13,3,11,11: 6 inverse is 16,
20 is 1, 42 is 4 with inverse 5, and 210 is 1 modulo 19. Their sum is
38=0 modulo 19. Consequently F'_I(1)=-1 modulo 19, a nonzero residue.
The possible 11 coefficient in the second support is a multiple of 19
and contributes zero to this derivative residue. Its exact integer lift
cannot change the conclusion.

Because F_I has coefficients in Z_(19)[Z], expansion at 1 gives

    F_I(1+19)=F_I(1)+19F'_I(1)+19^2 C, C in Z_(19).

Here F_I(1)=0 exactly. Moreover F_I(20) is an integer, as every b_j
and binom(20,j) is an integer. Thus

    F_I(20)=-19 mod361,

not 0 modulo 19^2. This calculation applies to both first-endpoint
supports, without assuming coefficient nonvanishing. If an I has both
endpoint congruences, PN1 places it in these two cases, and the displayed
calculation contradicts the second endpoint. This proves PN2 for every
I in the stated class. It is a complete finite-domain proof, not an
unrestricted inference from a finite sample or an assumption of a lift.

## PN3: precise use of the accepted PP1 interface

The accepted PP1/PP2 mathematical text has SHA-256
`6506e371c2a3eb8506f75c55ef3d80be9933ecbcd187be21fe5bd18932fe8789`.
Its scope and acceptance are given in `proofs/reviewed-return-r3-v1.1.md`
and `reviews/return-r3-acceptance.md`/`.json`. The historical statement
that joint endpoint nonvanishing was still unproved describes the accepted
dependency's own scope; it does not certify PN1 or PN2 in advance.

In that accepted interface f is a rational degree-20 polynomial normalized
at 19, with f(0)=f'(0)=f(1)=0, exact multiplicity two at 0, normalized
coefficients in Z_(19), and last unit index J=15. Every nonconstant
derivative has an actual rational root in common with f. The extra
hypotheses in PP1 are the exact center equation H3(f)(1)=0 and the
nonunit congruences for all even normalized indices 2,4,...,18.

Under these assumptions PP1 produces an I among exactly the 64 above,
with 1,15 included, b_j nonzero mod19 at actual supported indices and
F_I=(-1)^|I|d(I;Z). It produces both endpoint divisibilities. Multiplying
by a unit sign changes neither divisibility modulo 19 nor modulo 19^2.
PN2 is valid even without the additional supported-coefficient condition,
so it contradicts the PP1 output immediately. There is no discarded
lifting condition and no replacement of a rational witness by a merely
19-adic root at this stage.

It follows that the two PP1 extra hypotheses cannot hold simultaneously.
Since every normalized a_j is 19-integral, failure of the assertion that
all even a_j are 0 modulo19 means at least one even a_j is a 19-unit.
Thus the equivalent formulation in PN3 is correct whenever H3(f)(1)=0.
The conclusion does not exclude every J15 polynomial or every mask.

## PN4: precise use of the accepted PP2 interface

The repeated-root application is restricted to the exact PP2 setting:
the same normalized rational-witness J15 multiplicity-two branch, the
sole-H3 center configuration D3, the two 2R slots equal to one double root
d, and the five extra exact equations H6(r)=H8(r)=...=H14(r)=0 at the
specified r. The final extra assumption is an actual rational noncenter
H18 common witness, not an arbitrary local root or merely a residue.

PP2 proves that this conjunction supplies both PP1 extra hypotheses.
PN3 now contradicts them. This is the entire implication asserted by PN4.
It does not import the earlier unrelated collision packet as an extra
theorem or assert that the even ladder or noncenter H18 witness is
automatic. In particular no conclusion is obtained here from a single
center equation, from distinct 2R slots, from another multiplicity mask,
or from a general repeated-root branch. The phrase explicitly scoped in
PN4 correctly retains the remaining PP2 premises.

## Sources, adversarial cases and recommendation

I read the official 2021 B4(b) hypotheses directly. They require rational
common roots, and the new applications retain that stronger requirement.
Only part (b) is researched. The general descent recurrence was rechecked
in the complete statement and proof of Proposition 2.1 of the primary
Diaz-Lopez–Harris–Insko–Omar–Sagan paper. The general one-nonzero-root
connection is attributed to Marashdeh; I checked its complete Theorem B
statement and one-root boundary. Neither a new external nonvanishing
theorem nor a multi-root classification is used in PN1–PN4.

The attacks checked include an incorrect operator order; loss of a mixed
indicator coefficient; accidental support-complement orientation; treating
an inactive residue coefficient as nonzero; confusing an exact integer
coefficient with its reduction; using a derivative with a nonunit
denominator; obtaining only a mod19 rather than mod361 endpoint; dropping
the exact F(1)=0; overlooking the second first-endpoint support; and
overextending PP2's rational-witness or ladder scope. The explicit
reconstruction resolves each within the stated domain.

No substantive issue or required author repair was found. I recommend
accepting PN1–PN4 after a second fresh independent whole audit and root's
integration, with the dependency-authorship disclosure above retained.
Only the coordinator may promote. These conclusions do not establish
degree20, any annual classification, a rational lift, every remaining
necessary mask, or novelty. All older frozen bytes are preserved.

The one-time administrative freeze records all 13 constructor records,
the previous 23 own frozen packets, source scope, hand reconstruction of
64 cases, and 26% total weekly usage (reset 1792745187; 90%-total cutoff
with integration reserve). No mathematical program, CAS or larger search
was run for this review.
