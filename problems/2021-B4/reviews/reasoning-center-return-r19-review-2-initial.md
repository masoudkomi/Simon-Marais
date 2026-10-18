# R19 entire initially blind whole audit 2

2026-10-18 UTC. Independent OTHER reviewer B,
`/root/review_2022_complexity_r2`. Requested inherited gpt-6.1-sol/max;
independent effective-setting readback unavailable. **Candidate proof -
unverified; this report is not coordinator promotion.**

I reconstructed the entire proof and all 64 obligations by hand. The
precise normalized R19A, R19B, and R19C proofs withstand the algebraic,
valuation, and actual-witness checks described below. I identify **one
required explanatory scope correction, R19R2-01**: the introduction says
that a factor of the original carrier has a 2-Eisenstein translate,
whereas the proof establishes this for the factor of the SCALED carrier
G. Negative v2(s) makes that distinction mathematically necessary. The
formal R19C statement already gives the correct scaling. I have not
silently repaired the introduction or modified the candidate. A full
versioned author response/correction and both affected re-audits are
required before accepting the packet as written. Six other notes are
closed scope boundaries.

The whole initial report, ledger, sources, log, code, and metadata must
freeze, undergo full model readback and a separate read-only verification
before any corresponding NEW root R19 finding, report, hash, source,
code, or metadata is accessed. Findings remain embargoed until explicit
BOTH-entire confirmation. Root's already completed whole R1 supplies no
mathematical premise here. A is sole NEW constructor and is excluded.
Root supplied the broad question and no new construction inference.

I did not construct NEW R19. My older R5/R6/R7/R11–R16/R18 review roles
and earlier 2021 R9 construction are disclosed, not counted as fresh
self-recertification. R9 appears only as the author's exploratory
background, not an operative premise of this new dyadic proof; I do not
count my own old work as a fresh independent review. A's older R18/R8
and other input construction roles likewise retain their separate accepted
authorities. No NEW BT or other active peer packet was used.

## Exact packet, domain, and operative premises

Target main: `notes/reasoning-center-return-r19-candidate-v1.md`,17591B,
SHA256 `589eddbf5f305b3380ee2c499d774aff8bb1b4499aa46c15c3dbffcf1bd56462`.
Target freeze: `reasoning-center-return-r19-freeze-v1.json`,3893B,
SHA256 `dfe7b6b4f372b44a2806fc96ce41613bfc2fb7e8f5469fc2d10552aa83b835d3`.
All 13 author files were read in full: main, all64 obligations, checks,
failures, source MD/JSON, worklog, code log, admin code as text, baseline,
validation, metadata, and freeze. No author code was executed.

Official2021 B4(b) requires f over Q and an ACTUAL RATIONAL common value
with each derivative order1,…,d−1; the value may depend on the order.
A nonconstant gcd in Q[X] is a weaker condition. Preliminary(a) was
not reproved or investigated. This packet concerns only the complete
specified residual degree20 domain, not all official polynomials.

I freshly read the complete current accepted R18, R17, R8, and R5
mathematical bodies and each current MD/JSON authority, plus the stated
R18/R17/R8 failure/source boundaries. R18's actual three-frame table,
not a residue possibility list, is the input. It is in the full(S),(W)
branch: double0 and additional ACTUAL rational double s, simple r and1,
four distinct rational values0,1,r,s, all rational derivative witnesses
among those values, sole H3/J15 and actual m4 as specified. The actual
degree14 rational carrier g is separately accepted irreducible and
Eisenstein at19. Its other roots need not be rational or real.

R18 gives actual adjacent D12(1)=D11(1)=0, nu=1, and, after an ACTUAL
double-origin change if necessary, the full simple monic gcd frames:

| Frame | gcd(f,H13) | gcd(f,H16) | gcd(f,H18) |
|---|---|---|---|
| I | X | X−r | X |
| II | X | X−s | X−r |
| III | X−r | X | X |

The earlier W hypotheses include actual H2(r)=H4(r)=0. The new dyadic
proof does not manufacture those zeros from finite residues and does
not need a new 19-adic depth bound. Accepted R18/R17 scope is retained;
nonadjacent EC8, the different D11/D10 branch, m3, other root-slot or
J/multiplicity cases do not become covered automatically.

## 1. Actual rational witnesses give dyadic integrality

Set v=v2 with v(2)=1, v(0)=infinity. Since 1,r,s are nonzero rational
numbers, M=min(0,v(r),v(s)) is a finite integer, attained at a nonzero
ACTUAL root u in{1,r,s}. Put

    F(Z)=u^(−20)f(uZ), A_j=u^(−j)a_j,
    h=1/u, R=r/u, S=s/u, G(Z)=u^(−14)g(uZ).

All normalized actual witness values0,h,R,S lie in Z2, and one of the
last three equals1 EXACTLY. Also A0=1,A1=−h,A19=A20=0. Before any
reduction, the binomial identity

    binom(20,k) binom(20−k,20−j)
        =binom(20,j) binom(j,k)

gives `D_j^F=H_(20−j)(F)/binom(20,j)=sum_(k=0)^j binom(j,k)A_k Z^(j−k)`.
For every j=1,…,18 there is an ACTUAL normalized integral witness z_j.
Its equation gives

    A_j=−sum_(k<j) binom(j,k)A_k z_j^(j−k).

This triangular induction proves A_j∈Z2 without dividing by a binomial
nonunit. Original 19-integrality is not used as dyadic integrality.
A19,A20 are handled separately by exact vanishing. F is monic integral.

The exact factorization is
`F=Z²(Z−R)(Z−S)²(Z−h)G`. Each displayed linear factor is monic
integral, so successive monic divisions have integral quotients. The
remainders vanish by the existing rational factorization. Thus the
actual monic G is integral even if several residues coincide.

Any algebraic root of a monic integral polynomial is integral: if its
valuation were negative, the leading power would be uniquely minimal
against all lower integral terms. This argument works in the finite
extension containing the root, so it does NOT force its valuation to
be an integer. Integer valuations are used only for Q2/rational elements.

## 2. Full R19A and the published prohibition

In characteristic2, `(1+T)^20=(1+T^16)(1+T^4)`. Since A20=0,

    Fbar=Z^20+A4bar Z^16+A16bar Z^4.

F(1)=0 follows from the ACTUAL root u, hence A4bar+A16bar=1.
Both residues belong to F2, not merely an unspecified residue extension:
all coefficients and the scale u are rational. Therefore their ordered
pair is (0,1) or(1,0); neither is dropped as an alleged good-prime case.
At the normalized degree indices16 and4,

    D16bar=Z^16+A16bar,       D4bar=Z^4+A4bar.

Over an algebraic closure of F2 their unique root residues are the
different elements A16bar and A4bar. A common characteristic-zero root
of these monic integral polynomials would be integral, and reduction in
its finite local extension would give a common reduced root. This is
impossible. Nonzero scalar multiples do not change roots over Q2, so
H4(F) and H16(F) are coprime. The exact identity
`H_k(F)(Z)=u^(k−20)H_k(f)(uZ)` transports coprimeness back to f.
This also forbids non-f-root common roots of these two derivatives in
the given rational-witness normalization; the argument does not rely
only on selecting an f-root.

Frame I has the ACTUAL common value r at H4 by W and at H16 by the
accepted full gcd. This is a genuine contradiction, excluding the
entire frame. For `f_new(Y)=c f(a+bY)`, b,c nonzero rational,
`H_k(f_new)=c b^k H_k(f)(a+bY)`. The accepted origin exchange sends
r to (r−s)/(1−s) and preserves both zeros. Its dyadic scale need not
be a unit for a field-level common-root contradiction. The actual
frame-I partner is excluded as well.

The common-F-root order4/order16 prohibition is already published.
I checked Massri's version6 complete Proposition7.7 proof and Remark7.8,
including the nontrivial/multiple-root setting and actual derivative
index convention. The supplied proof above is self-contained and
stronger in its precise rational-normalization coprimeness wording; no
unread computation is imported. No priority or new general CA theorem
is asserted. The cited original CLO passage also gives related
common-root exclusions; the attribution is not a claim that Massri
was the first source. See source read limits.

## 3. Entire frame-II residue analysis and R19B

In frame II, H18,H4,H2 vanish at R and H16 vanishes at S after
scaling. Write rho=Rbar,sigma=Sbar,eta=hbar in F2. These are actual
evaluation equations, not roots supplied by a local lifting theorem.
D2(R)=0 gives `A2=2Rh−R²`, hence A2bar=rho. The power-of-two
equations give A16bar=rho and A4bar=sigma, so rho+sigma=1.

For degree18, `(1+T)^18=(1+T^16)(1+T²)` gives
`D18bar=Z^18+A2bar Z^16+A16bar Z²+A18bar`.
At R its first three terms each equal rho in F2. Actual H2(R)=0
therefore gives A18bar=rho. The derivative orders are H18↔D2,
H16↔D4, H4↔D16, H2↔D18; reversing these indices would be wrong.
The exact factors are binom(20,2)=binom(20,18)=190 with v=1,
and binom(20,4)=binom(20,16)=4845, odd.

**Case rho=1,sigma=0.** Then `Fbar=Z^4(Z−1)^16`, with EXACT zero
multiplicity4. Double0 and doubleS already supply Z^4. If eta=0,
Z−h supplies another Z, impossible irrespective of G. Thus eta=1.
The base factors now reduce to `Z^4(Z−1)^2`, so `Gbar=(Z−1)^14`
and G(0),R,h are units. The actual coefficient c2 of Z² is

    c2=R h S² G(0).

The two minus signs cancel. S is nonzero even, so v(c2)=2v(S)≥2.
But c2=190A18 and A18 is a unit, giving v(c2)=1. This eliminates
the whole case, not just v(S)=1 or a bounded-depth subcase.

**Case rho=0,sigma=1.** Here v(s)=M and v(r)>M. If M=0, h is a
unit and eta=1. The base factors are now `Z³(Z−1)^3` while
`Fbar=Z^16(Z−1)^4`; therefore `Gbar=Z^13(Z−1)`.
At the ACTUAL double root S, the Hasse product formula is

    H2(F)(S)=S²(S−R)(S−h)G(S).

The Hasse second derivative of (Z−S)² is1; its lower derivatives
vanish there. S and S−R are units, whereas S−h and G(S) are even.
The product has valuation at least2, with infinity allowed for the
inequality. In contrast, A2bar=A16bar=A18bar=0 makes D18(S) odd,
so H2(F)(S)=190D18(S) has EXACT valuation1. The contradiction
excludes every M=0 possibility. It does not assume H2(f)(s)=0:
an exact double root has a nonzero second derivative.

Thus `v2(s)=M<min(0,v2(r))` in the stated frame. The denominator
of rational s has an even factor. This is not an ordinary sign,
height, or 19-adic contradiction; v19(s)=1 and a negative v2(s)
can coexist. No upper bound on either root valuation was inferred.
Ties among minimum witness valuations were retained and ruled out
only where the actual equations give a contradiction.

## 4. Exact normalized carrier proof, R19C

Now choose u=s, so S=1 and R=r/s,h=1/s belong to2Z2. The base
reduces to `Z^4(Z−1)^2`, hence `Gbar=Z^12(Z−1)^2`.
D18(1) is odd. At the exact double root1,
`H2(F)(1)=(1−R)(1−h)G(1)`; both linear factors are units. Therefore
G(1) is an ACTUAL nonzero value with v=1.

For `Pbar=(Z−1)^2`, `Qbar=Z^12`, the factors are coprime to each
other, although neither is squarefree internally. Starting with monic
lifts of degrees2 and12 gives product congruent to G mod2. If the
current error is divisible by2^m, its leading coefficient cancels,
so it has degree<14. Solve

    U Qbar+V Pbar = (G−Pm Qm)/2^m mod2,
    deg U<2, deg V<12.

This map has dimension14 on both sides. Kernel zero follows from
Pbar|U Qbar and coprimeness, then Pbar|U, U=0, and V=0. Thus
the correction exists uniquely. The cross term2^(2m)UV is divisible
by2^(m+1) for every m≥1. Completeness of Z2 supplies the monic
limits, and the same coefficientwise unique corrections give uniqueness
with the prescribed reductions. This is a LOCAL Z2 factorization,
not a rational factorization of g over Q.

Q(1) is odd, so v(P(1))=v(G(1))=1. The monic quadratic
`P(T+1)=T²+bT+c` has v(b)≥1,v(c)=1. For a root t in a finite
algebraic extension, v(t)<1/2 makes t² the uniquely smallest term;
v(t)>1/2 makes c uniquely smallest. Both are impossible. This
includes b=0 with infinite valuation, and c is nonzero. Thus v(t)=1/2.
No Q2 root has that valuation; the quadratic is irreducible and, in
characteristic zero, separable. Its root field is ramified, with the
half-integral valuation directly witnessing that fact.

For z=t+1, the corresponding original carrier root is alpha=s z,
and `v2(alpha−s)=v2(s)+1/2`. The other12 G-roots are integral and
reduce to0 because the monic Q reduces toZ^12. This is a precise
local cluster statement. It is compatible with g being globally
irreducible over Q and Eisenstein at19. No local root is asserted
to be a rational common witness, and no factor/quotient inherits a
CA condition as its own derivatives.

## 5. Required correction R19R2-01: scaling before Eisenstein

The opening overview says:

> the actual degree14 carrier has a degree2 factor over Q2 whose translate is 2-Eisenstein.

The demonstrated 2-Eisenstein translate is P(T+1) for the factor of
the SCALED carrier G(Z)=s^(−14)g(sZ). The monic factor of the
ORIGINAL carrier obtained from it is

    E(X)=s² P(X/s).

Writing `P(T+1)=T²+bT+c` as above gives

    E(T+s)=T²+s b T+s²c,
    v2(s²c)=2v2(s)+1<0.

Thus this translate is not even in Z2[T], and is not 2-Eisenstein.
In fact no Q2 translation of this constructed E is integral: for
a∈Q2 and its root alpha=s(1+t), v(t)=1/2,

    alpha−a=s[t+(1−a/s)].

The second summand has integer valuation or is zero. Hence the
bracket has valuation at most1/2, and v(alpha−a)≤v(s)+1/2<0.
A monic integral translate could not have such a root. This shows why
translation alone cannot repair the omitted scaling.

A concrete counterexample to the omitted invariance implication is
`P(Z)=(Z−1)²−2`, `s=1/2`. Its correct translate is T²−2. The
original-variable factor is `E(X)=X²−X−1/4`, and
`E(T+1/2)=T²−1/2`, not integral. This is a counterexample to the
scaling/translation inference, NOT an example of an actual degree20
f or a counterexample to the original problem.

An unspecified different factor among the other12 roots is not proved
to have the overview's unscaled property either. The formal R19C
statement and its actual displacement formula already have the right
normalization and are unaffected. Nevertheless the entire packet's
unqualified original-carrier assertion needs author clarification;
I do not silently read it as a normalized assertion. No candidate or
shared file was edited. A versioned full author correction and both
affected re-audits should preserve the original sentence and this
counterargument. This objection does NOT refute the exact normalized
R19C theorem or the frame-I exclusion.

## Scope, sources, and final audit boundary

Frame III is not eliminated: H16 and H18 use0, while H4 usesr.
Its exact a2=a4=0 and actual D3(1)=0 give a3=2, hence
`D2=X(X−2)` and `D4=X(X−2)(X²−2X−4)`. The extra derivative
root2 is not thereby an f-root. Frame II still requires a genuine
global incompatibility argument. Forced ramification at2 is not
inconsistent with degree14 Eisenstein ramification at19. The published
ALL-roots-rational or ALL-roots-in-one-unramified-field exclusion has
stronger hypotheses and is not applicable. Other actual EC/m3 and
J/multiplicity cases remain outside this result. No degree20/annual,
height, unrestricted valuation-bound, rational-lift, or priority claim.

Primary source records state exactly what was read. Two attempted
web screenshots of Massri pages11/12 failed with cache-miss errors;
no visual proof verification or binary hash is claimed. The complete
operative text proof and matching remark were available and read,
and the new mathematics is self-contained. No source program or
finite certificate was rerun. All algebra, multiplicity divisions,
two residue branches, and factor-lifting steps above were checked
by hand, not a scan or CAS.

The NEW metadata-only program verifies declared immutable records and
all64 labels without proving mathematics. Mutable historical root-owned
research-map snapshots are preserved as historical observations, not
current mathematical premises or falsely unchanged files. Immediate
parent metadata is bound compactly. All old/shared/Git/cache bytes
remain unchanged; no other worker's process, active proof, or pending
peer packet was accessed or disturbed. The whole initial must remain
immutable after freezing, regardless of subsequent reconciliation.
