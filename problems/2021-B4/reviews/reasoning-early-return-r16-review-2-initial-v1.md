# R16A–C: entire initially blind whole review 2

18 October 2026 UTC. Reviewer `/root/review_2022_complexity_r2`.
Requested inherited **gpt-6.1-sol / max**; independently verified
effective-setting readback unavailable. This is an independent review
recommendation, not coordinator promotion. The submission remains a
candidate until the required other whole audit and reconciliation.

**Whole finding:** R16A, R16B and R16C pass in their exact stated scopes.
I found no substantive proof defect, unresolved objection or required
mathematical repair. All 56 obligations have independently reasoned
ledger entries. Six closed scope/dependency notes are preserved in the
issue record. I reconstructed the entire argument, including every
entry of both affine certificates and all nine quartic cases, by hand.
No mathematical executable, scan, CAS, sample testing, finite-certificate
generator or author/source/freezer rerun was used.

The target is the 18,818-byte
`problems/2021-B4/notes/reasoning-early-return-r16-candidate-v1.md`,
SHA256 `d9765b700bf7f7a0c13bcb0b5729a38150e87fe847156df29d4c592abad0b2d1`.
Its complete twelve-file constructor packet, including the hand checks,
all 56 obligations and constructor dispositions, failures, sources,
worklog, administrative code and all metadata, was read. Exact target
freeze and preservation fingerprints are in this review's baseline and
manifest. A clipped combined hand-check/constructor-check output was
subsequently reread in two complete separate outputs; completeness does
not rest on the clipped read.

## Independence and permitted input authority

A is the sole new constructor and is excluded from independent review.
Root supplied the broad task and no new R16 inference. I did not
construct, advise on or repair this new proof. No corresponding NEW
root R16 report, ledger, source record, code, finding, hash or metadata
was accessed before this entire initial freeze. Completion is sent as
IDENTITY ONLY until root confirms its entire other initial has frozen.

I previously reviewed R5 and several other 2021 return packets and
constructed the older R9 packet. I also have older single-center/J15
review roles. These roles are disclosed and are not new independent
recertification of those old inputs. Here I freshly read the COMPLETE
accepted R8 and R5 bodies and their complete current MD/JSON acceptance
authorities, checked the exact operative claims, and reconstructed all
new uses. R8's Euler estimate and fork are separate accepted premises;
R5's actual global carrier distinction is retained. Their large
historical integrity inventories are bound compactly, not replayed.

The author's unverified R15 is NOT a premise. Its preservation hashes
are metadata, not a mathematical endorsement. I did not need or read
any new R15 peer findings. R10/R12/R13/R14 appear only as author context;
the R16 proof does not invoke their center-exclusion certificates. The
new argument is therefore not conditional on promoting R15 or silently
using R12 with a possibly unit a8.

## Official domain and the actual-witness dictionary

I freshly checked the official [2021 Paper B](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2021-paper-b.pdf),
B4 setup and (b), against the local statement. The coefficients and
each shared-root value are rational; the chosen value can change with
the derivative. Other roots need not be rational or real. The target
is the degree classification, while this packet treats one residual
degree-20 branch. No preliminary proof was researched or reproduced.

The exact hypotheses are (S) and (W): the normalized rational degree-20
polynomial, a_j in Z_(19), a0=1, a1=-1, ord_0 f=2, f(1)=0, J=15,
sole low center H3(1)=0 with H2(1),H4(1) nonzero, and the ADDITIONAL
actual rational double s. There are precisely four rational root
values 0,1,r,s; 0 and s are double, r and 1 simple,
v(r)=v(s)=nu>=1 and s/r=2 modulo19. The actual factorization is

    f=X²(X-r)(X-s)²(X-1)g,  deg g=14,

with g rational irreducible. The rationality here follows from actual
division, and is not inferred merely from a local Eisenstein cluster.
R16C's degree comparisons only require this global irreducibility.

Over Q, BEFORE reducing, the normalized derivative is

    D_j=H_(20-j)(f)/binom(20,j)
       =sum_(k=0)^j binom(j,k)a_k X^(j-k),
    D_j'=j D_(j-1),  binom(20,j)=19 beta_j.

For 2<=j<=18, beta_j is a 19-unit. At an actual rational noncenter
w in {0,r,s}, the integral D_j reduces to a_j. Thus the actual
witness property implies a_j D_j(1)=0 in F19. This is a NECESSARY
product only. Unit a15 makes every rational noncenter unavailable to
H5, so D15(1)=0 over Q. H3(1)=0 gives D17(1)=0. The third center
row is the ORIGINAL rational f(1)/19 equation, not f modulo19 with
its informative factor19 lost.

## R16A: reconstruction of the global obstruction

Under Q*, the only possibly nonzero residues are a0,a1 and
a2,a3,a4,a5,a6,a7,a8,a9,a13,a15. In particular a11 and a17 are
zero RESIDUES; they are not asserted to be zero rational coefficients.
Set A,B,C,E,V,x,U,y,w,u in that order for a2,a3,a4,a5,a6,a7,a8,a9,a13,a15.

The beta residues for j=2,3,4,5,6,7,8,9,13,15 are

    10,3,8,-1,7,14,-1,5,14,-1.

I checked their integer quotients before reduction. For example
15504/19=816=-1, 77520/19=4080=14 and 125970/19=6630=-1.
Consequently the original divided equation is

    0=L+14x-U+5y+14w-u,
    L=-1+10A+3B+8C-E+7V.

This fixes the potentially dangerous a7 sign. The D15 row uses
coefficients 10,-1,-3,1,8,13,13,8,10,1; the D17 row uses
3,15,5,13,7,11,9,9,5,3, at the same displayed indices. Their
constants are 5 and3. This gives exactly the three main rows (1),
with right sides L-U, R+6U and S-9U and the stated R,S.

Temporarily retaining z=a11, subtracting the first row and its triple
gives

    2z+5w=K-8x+6y+7U,
    3z+9w=N+4x-5y-6U,
    K=R-L, N=S-3L.

The determinant is3. Elimination gives z=3K-8N+x+y+12U and
w=7N-K-2x-3y+8U. My independent expansions are

    Z=3K-8N=7+14A+15B+8C+4E+8V,
    W0=7N-K=4-2A+5B+11C+6E+9V.

We may now impose z=0. No variable coefficient was inverted.

Actual products at indices2 through5 give precisely

    A(A-1)=0, B(B-2+3A)=0,
    C(C-3+6A+4B)=0,
    E(E-4+10A+10B+5C)=0.

Hence (A,B) is one of (0,0),(0,2),(1,0),(1,-1), C is 0 or its
displayed complement, and E is 0 or E*. All eight prefixes and E*
in the certificates follow; no residue-support hypothesis was added.
The independent low expansions give

    V*=5-15A-B-15C-6E,
    p7=13+2A+16B+16C+2E+7V,
    q9=11+17A+8B+12C+12E+8V,
    T=12+9A-B+13C-E+9V,

and the products V(V-V*)=0, x(x+p7)=0, U(U+T+8x)=0, with
S9=D9(1)=y-2x+q9+9U. Under the contradictory assumption S9=0,

    y=2x-q9-9U, 3U=q9-Z-3x,
    q9-Z=4+3A-7B+4C+8E.

The V cancellation is exact.

### Complete affine cases with x nonzero

Here x=-p7. Substitution yields

    U=8+3A+B+11C+11E+7V,
    U+T+8x=11+15A+5B+10C+13E+17V.

At V=V*, these become 5+12A+13B+C+7E and
1+7A+7B+2C+6E. For the ordered four functions the slopes are
11,13,7,6 and inverses 7,3,11,16. Computing minus each constant
times its inverse by hand gives ALL32 zeros:

|A,B,C|E*|four unique E zeros|
|---|---:|---|
|0,0,0|4|1,5,2,3|
|0,0,3|8|17,10,7,2|
|0,2,0|3|6,13,1,7|
|0,2,14|9|11,11,18,15|
|1,0,0|13|18,17,3,5|
|1,0,16|9|2,12,17,6|
|1,-1,0|4|6,13,13,3|
|1,-1,1|18|5,2,2,9|

Every entry differs from 0 and its E*. Both factors of the required
U product would be nonzero. V*=0 occurs at some allowed inputs;
evaluating both algebraic formulas still covers it, without imposing
V*!=0. If the computed x happens to be zero, the calculation merely
considered a superset of the x-nonzero case; nothing valid was lost.

### Complete affine cases with x zero

There is now NO p7=0 hypothesis. Direct substitution instead gives

    U=14+A+4B+14C+9E,
    U+T=7+10A+3B+8C+8E+9V.

At V* the second becomes 14+8A+13B+6C+11E. Slopes9,8,11
have inverses17,12,7, producing ALL24 zeros:

|A,B,C|E*|three unique E zeros|
|---|---:|---|
|0,0,0|4|9,11,16|
|0,0,3|8|17,8,4|
|0,2,0|3|6,15,5|
|0,2,14|9|18,1,6|
|1,0,0|13|11,5,17|
|1,0,16|9|3,8,10|
|1,-1,0|4|3,3,13|
|1,-1,1|18|12,2,9|

Exactly one zero is allowed: A=B=0,C=3,E=8,V=0. Here V*=7,
so this is a real exceptional endpoint, not a duplicate. Direct
substitution gives Z=6,q9=10,W0=9 and

    x=0, U=14, y=16, w=16.

It satisfies z=0,S9=0 and the lower products. Also u=1, so J15
does not discard it. An additional ACTUAL equation is indispensable.
The correct index13 expansion is

    S13=w+6x+14U+12y+c13,
    c13=7+2A+B+12C+14E+6V.

At this tuple c13=3 and S13=407=8 in F19. Then w S13=128=14,
contradicting the actual H7 witness product. All mixed a8,a9 terms
are retained; no division by w hides a zero case.

Thus D9(1) is a field unit. Since H11=19 beta9 D9, the original
H11(1) has valuation EXACTLY1. Its actual rational common root must
be 0,r or s. In D9 at that value every nonconstant term has valuation
at least nu, which forces v(a9)>=nu. If the witness is 0, a9=0
exactly, included by v(0)=infinity. This proves R16A for arbitrary
nu>=1 with no upper root-depth, ordinary-sign or displacement bound.

## R16B: actual m4 cubic exclusion

I checked the COMPLETE accepted R8 fork, not just its table headings.
The present M4 means H2(r)=H4(r)=H6(r)=0 and H8(r)!=0. Reducing
the first three integral equations makes a18,a16,a14 nonunits.
Both accepted m4 cubic rows have finite sigma=v(a9), 0<=sigma<nu,
and depths at a10,a11,a12 at least nu+sigma,2nu+sigma,3nu+sigma.
All are nonunits, even at sigma0. Thus Q* follows for BOTH actual
rows. R16A contradicts sigma<nu.

This reasoning does not depend on either row's additional exact gaps,
does not require positive sigma, and does not select a double origin.
The accepted Euler proof includes delta=s-2r zero and every finite
displacement depth; the contradiction adds no delta division. There
is no residue-to-rational lift. Removing those two rows from the whole
R8 fork leaves precisely a NONZERO NONUNIT essential center at8/9/10
with full gcd X-1 and the stated lower constant depth, OR T4. These
may coexist. Neither is eliminated and m3 is not excluded.

## R16C: entire quartic and actual contact reconstruction

The extra unit a8 and actual noncenter witnesses for H8,H9,H10 are
explicit hypotheses. In a no-(EC), T4 case they are indeed supplied:
if an order8/9/10 had no rational noncenter witness, its only shared
rational value would be1. Its constant cannot be zero (or0 would
also witness), has finite depth>=nu by T4, and its carrier of degree14
cannot share a root with derivative degree12/11/10. Simplicity of1
then gives exactly (EC), a contradiction. An available center may
coexist with a noncenter; this argument does not conflate them.

T4 and the ladder imply Q*, so R16A supplies H11's fourth actual
noncenter witness. Set P(z)=D12(rz)/(a8 r^4) over Q. The four
low-depth bounds make its coefficients of degrees0..3 integral;
the degree4 coefficient is495=1 modulo19. Every higher-degree term
has excess at least nu. Thus the reduction q is monic quartic.
Differentiating BEFORE reducing gives, for 0<=i<=4,

    H_i(P)=binom(12,i) D_(12-i)(rz)/(a8 r^(4-i)).

The scalars12,66,220,495 are units; in particular the H11-to-H3(q)
step is legitimate. High-degree reduction and its derivatives are
justified by these integral identities, not by differentiating a
nonintegral expression after discarding terms.

The accepted Euler expression is W(r²), with terms h8,h10r²,
h12r4,h14r6,h16r8,h18r10,r12. It is zero if delta=0, otherwise
has valuation>=7nu+1. Division over Q by19 beta12 a8 r4 leaves
positive excess>=3nu on the left. The last four right terms have
excess at least2nu,4nu,6nu,8nu-1, all positive even at nu1.
Only the first three survive. Beta12=beta8=18, beta10=15,
66=9 and495=1 give

    q(1)+11 H2(q)(1)+H4(q)(1)=0.

The final coefficient is1, not the coefficient3 from a different
m5 functional. The actual zeros give q(w)=q'(u)=H2(q)(t)=H3(q)(v)=0,
with w=0 or2 and u,t,v in {0,1,2}. M4 excludes the actual witness r
for H8, regardless of whether q might initially have an extra root1.

Reflection q(2-z) is monic, preserves the even-at1 functional and
permutes the allowed nodes. It is a residue-polynomial operation,
not an assumption that f is symmetric or s=2r over Q. For w0,
write q=z4-4v z3+C0z²+B0z. Then

    C0=12vt-6t²,
    B0=-4u³+12vu²-2C0u,
    (-3+11t+12u²+14tu)v+11-4u³+(4+12u)t²=0.

I independently recomputed all nine coefficient/constant pairs:

|u,t|coefficient of v|constant|solution|
|---|---:|---:|---|
|0,0|16|11|10|
|0,1|8|15|10|
|0,2|0|8|impossible|
|1,0|9|7|14|
|1,1|15|4|1|
|1,2|2|14|12|
|2,0|7|17|3|
|2,1|8|7|11|
|2,2|9|15|11|

The zero-coefficient cell is contradictory, not divided away. The
only solution with v in {0,1,2} is u=t=v=1. Hence q=(z-1)^4-1,
which is itself invariant under reflection, covering both w choices
and all possible coincident nodes. Its derivatives are

    q'=4(z-1)³, H2(q)=6(z-1)², H3(q)=4(z-1).

The only allowed derivative node is1. Because the actual rational
noncenter values 0,r,s have DISTINCT residues0,1,2 after division
by r, the existing actual H9,H10,H11 witnesses are all r. This is
the direction actual zero -> residue restriction -> identification
of that actual value. It is not a lifting argument.

H11's center is unavailable by R16A; its other small values are
excluded by those nodes. The rational irreducible degree14 g cannot
share an algebraic root with H11 of degree9. Since r is simple in f,
the FULL monic gcd is X-r, including after algebraic scalar extension.
Unit a8 also makes D8 at every rational noncenter a unit, so H12(r)
is nonzero and the contest's actual H12 witness must be1.

The coefficient comparisons are

    11 a9/(a8r)=-4, 9 a10/(a8r²)=6,
    12 a11/(a8r³)=-4, a12/(a8r4)=0 mod19.

They yield ratios10,7,6, all nonzero, proving the three EXACT depths
nu,2nu,3nu. The last depth is at least4nu+1, including infinity;
it is not an exact rational coefficient gap. Finally the first three
ordinary derivatives of D12 at r vanish, while its fourth is
12*11*10*9 D8(r)!=0. Thus D12-D12(r) has exact multiplicity4 at r.
M4 says D12(r)!=0, so no quadruple root of f or D12 was asserted.

## Adversarial endpoints, sources and conclusion limits

I challenged zero low coefficients, a6/a7/a8/a9 nonunits or units,
x0, V*=0, the genuine affine exception, node coincidences, every
nu>=1, exact delta0, arbitrary displacement, the coefficient-zero
quartic cell, simple versus double roots, and algebraic versus merely
rational gcds. The displayed reasoning covers these cases. The
quartic itself is a surviving leading diagnostic, not an actual
Casas–Alvero polynomial or a Q19/Q lift. It satisfies the correct
functional (-1)+0+1=0 and therefore supplies no local contradiction.

Fresh operative inspection of [Castryck–Laterveer–Ounaies](https://arxiv.org/pdf/1208.5404)
covered equation7, complete Sections3.4–3.5, Lemmas17–18, and the
entire Proposition19 proof/unramified remark. This is a passage
inspection, not a full23-page/source-program audit. Its stronger
all-root/unramified conclusion is not applied to the ramified carrier.
The earlier prime5 correction is preserved, not freshly reread or used
as a positive theorem. Detailed scopes are in the source-check record.

R16B removes BOTH actual m4 cubic alternatives, while EC/T4 and m3
remain. R16C retains EXTRA a8-unit and noncenter hypotheses. No full
m4/J15/degree20/annual classification, maximal-depth bound, quotient
CA property, all-real-root theorem, rational lift, novelty or priority
is claimed. Only the coordinator may accept the precise result after
both whole reviews and full reconciliation. My frozen initial and all
older artifacts are to remain byte-for-byte preserved.
