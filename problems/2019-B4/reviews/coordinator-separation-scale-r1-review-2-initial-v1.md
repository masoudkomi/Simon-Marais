# 2019 SS1--SS3: initially blind whole independent review 2

2026-10-17 UTC. Reviewer `/root/review_2017_coarsening_r1` (C).
Requested `gpt-6.1-sol`, `max`; independently verified effective-setting
readback unavailable. Target is the ENTIRE root-constructed
`notes/coordinator-separation-scale-r1-candidate-v1.md`, 9068 bytes,
SHA256 `d08d778d7bfe2e915b67d85833d4dfb312d78393f0e80aeecdc7859abae5070e`,
and its complete 14-artifact packet. Constructor freeze: 3809 bytes,
SHA256 `33abb0fd6e571f623f31c9d767be471b95cad1990f39d898700f3568acad732c`.
All 13 whole obligations have independent ledger rows. No NEW SS peer
report, ledger, source, metadata or findings was read before this ENTIRE
initial freeze.

**Initial verdict:** no substantive mathematical defect and no required
author repair in the exact SS1--SS3 scope. The first count-discrepancy
bounds, actual two-tail word-set union and strict lower bound
lambda>1.765224 survive this audit. There is one optional editorial
count-of-blocks wording note, with no effect on any inference. This is
one independent audit, not coordinator promotion or an exact annual
answer. Mathematical findings are to be withheld until the other whole
initial has frozen as well.

I did not construct or contribute any NEW SS1--SS3 inference. Older
2019 linear-output construction and chronological/auxiliary-presentation
review roles are disclosed and preserved; none counts as an independent
re-audit of my own older work. The second-pass, third-pass and M1--M3
results here are separately accepted dependencies. Root's authorship
of the older moment result and of NEW SS excludes root from both fresh
independent SS reviewer counts. Author checks and source metadata are
not substitutes for the reconstruction below.

## 1. Official target, objects and operative accepted premises

The official 2019 B4(b) concerns DISTINCT binary output strings from
seed1, alternately adding 0/1 at either end. It requests liminf and
limsup of b_n^(1/n). I read the actual official B4 statement and local
statement. No preliminary(a) proof is reproduced. The accepted marked
context argument gives an existing common root rate lambda for canonical
history counts c_n and original outputs b_n; it identifies root growth,
not their exact counts, polynomial prefactors or adjacent ratios.

Use chronological histories on L,R, lexicographic order L<R, and the
canonical least history for each chronological two-tape context. The
canonical language K is factorial. Its minimal noncanonical factors F
are factor-free and admit strictly upper equal-context witnesses. If
L_h(t) counts left moves in the first t source-time moves, a witness g
for f has L_g(t)>L_f(t) at every internal t. Its separation is
max_t(L_g(t)-L_f(t)). The cap uses the EXISTENCE of such a witness,
not the width of an arbitrarily chosen alternative:

    F_D={f in F: some strictly upper witness has separation<=D},
    K_D=Avoid(F_D), D>=1.

The complete accepted second-pass canonical-renewal, rigidity and
staircase bodies, third-pass bounded-separation body and moment candidate
were read. Their exact acceptance scopes were read in full. Historical
candidate labels are not interpreted as overriding those exact current
acceptances. The accepted moment register has a byte-identical copy
of its frozen mathematical body. In particular:

    C(z)=1/(1-2z+F(z)), F(R)=2R-1, F'(R)<=2, R=1/lambda;
    F_D=F through length2D+1;
    F_3=RRLL | RRLRRLRL(RRLRL|LRLRL|LRLRRLRL)*LRLL.

The precise accepted rigid family has exactly TWO histories H(p,q),
K(p,q), p,q>=1, and each proper factor has unique context. This is
not asserted for all F; the older three-history counterexamples remain
outside that claim. P24 is accepted complete finite data, not a newly
enumerated prefix in this audit. No older certificate or automaton is
rerun.

## 2. SS1 reconstructed: minimum width and the first count discrepancy

For p=q=d the alternate K(d,d) is the letterwise side exchange of
H(d,d). Consequently at each source time

    L_K(t)-L_H(t)=t-2L_H(t).

Reading the FIVE displayed groups RRL, R^(2d), LR, L^(2d), RLL gives
respectively the following values after the successive moves:

    1,2,1;
    2,3,...,2d+1;
    2d,2d+1;
    2d,2d-1,...,1;
    2,1,0.

These lists include d=1. Every value at a strictly internal time is
positive, the endpoint is zero, and the maximum is exactly 2d+1.
By the accepted TWO-history rigidity, this is the only alternative
for the complete context. Hence it is the MINIMUM possible separation
among upper witnesses; a narrower third path cannot put this H in F_D.
The rigid word has length 4d+8.

For even D>=2 choose d=D/2; then 2d+1=D+1 and the word length is
2D+8. For odd D>=1 choose d=(D+1)/2; then the width is D+2 and
length2D+10. Both choices have d>=1, including D=1. In each case H
is an ACTUAL member of F omitted from F_D. Thus an omitted factor
exists for every cap.

Let m be the least omitted-factor length. For n<m, a word that avoids
F_D but is outside K would contain some f in F of length<=n<m, and
that f would be in F_D, a contradiction. Therefore counts agree below
m. At length m choose an omitted f. Factor-freeness says no proper
factor of f is in F, hence no member of F_D can be a proper factor;
f itself is absent from F_D. Thus f is in K_D but outside K. Since
K subset K_D, this gives a STRICT count discrepancy with no possible
cancellation. Its first length tau_D is exactly m.

The accepted F_D=F through length2D+1 implies m>=2D+2. Combined with
the selected rigid word, this gives exactly

    2D+2 <= tau_D <= 2D+8  (D even),
    2D+2 <= tau_D <= 2D+10 (D odd).

This tau is defined for canonical histories and their capped avoidance
language, not the original-output count at the same numerical index.
It disproves quadratic exact PREFIX agreement for this cap model.
It does not give a lower bound on rho_D-lambda: one omitted long word
can have very small weighted mass. No stronger entropy statement follows.

## 3. SS2 reconstructed as an actual word-set union

The rigid H(p,q) has a run R^(2p) and a run L^(2q) with the specified
separating letters, so p>=2 or q>=2 creates an actual run of length
at least4. Every accepted F_3 word has runs at most2, including across
loop and terminal boundaries. Thus any common word must have p=q=1.
Direct substitution gives

    H(1,1)=RRLRRLRLLRLL=RRLRRLRL . LRLL,

the long F_3 branch with zero loops. This proves the exact WORD
intersection {H(1,1)}, rather than inferring it from equal lengths
or coefficients. It also separates the short RRLL branch.

Distinct positive (p,q) give distinct rigid words and length2p+2q+8.
For fixed s=p+q, there are s-1 choices. Hence the full rigid series is
z^12/(1-z^2)^2 and its prefix through24 is

    B(z)=z^12+2z^14+3z^16+4z^18+5z^20+6z^22+7z^24.

The long F_3 branch has base length12 and uniquely parsed loops of
lengths5,5,8. For additional length<=12, the options are zero loops,
one of the two length5 loops, the length8 loop, and two length5 loops.
The prefix is therefore

    A(z)=z^12+2z^17+z^20+4z^22.

For completeness, uniqueness follows from the accepted expression's
prefix-free loops: the R-start loop is separate, the two L-start loops
differ at their fifth letter, and LRLL terminates before any L-start
loop could be confused with it. No new language equality with F_3 is
inferred from this length calculation; the full equality is the named
accepted third-pass input.

P24 already contains every word in both prefixes, including RRLL.
Subtracting A and B from their respective infinite families removes
ALL words of those families through24. Their only common word was
length12, now removed, so the two remaining tails are disjoint from
each other and from the full prefix. Thus G is an ACTUAL subset of F,
contains every member of F of length<25, and its exact series is SS2.
All coefficients are nonnegative by this set decomposition, despite
the written subtractions. No complete coefficient beyond24 is asserted.

## 4. M2's exact application and an independent integer sign certificate

For N=25, the accepted moment criterion applies to this possibly
infinite ACTUAL G. For clarity, its relevant inference can be rederived.
H=F-G has only terms of degree>=N. At the true radius R,

    H(R)<= (R/N)H'(R)<= (R/N)(2-G'(R)).

Since 1-2R+G(R)=-H(R), this gives E_G(R)>=0. On the OPEN interval
(0,R), G'<=2 and G''>=0, so

    E_G'(x)=(1-1/N)(-2+G'(x))-(x/N)G''(x)<=0.

Continuity at R needs only the finite first moment, already accepted.
Thus E_G(x)>=0 for 0<=x<=R. A trial where the explicitly known G and
G' converge and E_G is negative must be greater than R. This uses no
simple root, positive renewal defect, finite endpoint second moment
or analytic continuation beyond R. The linear coefficient is exactly
-2(1-1/25)=-48/25.

I independently simplified the fixed rational sign by the Euler operator
25-x*d/dx, rather than rerunning the constructor's Fraction derivative
program. Put x=r=125000/220653, a=1-2x^5-x^8 and b=1-x^2. SS2 gives

    G=Q+x^12/a+x^12/b^2,
    Q=x^4-x^12+8x^19+20x^21+4x^22+40x^23+35x^24.

The negative coefficient in Q is harmless: Q is only an algebraic
intermediate, whereas the actual G is the proved word-set union. Applying
the operator gives

    25 E_G = U + (13x^12-36x^17-21x^20)/a^2
                  + (13x^12-17x^14)/b^3,
    U=25-48x+21x^4-13x^12+48x^19+80x^21
                     +12x^22+80x^23+35x^24.

In particular, differentiating the b^-2 term has the correct factor2.
Define the INTEGER polynomial

    P=U*a^2*b^3+(13x^12-36x^17-21x^20)*b^3
                        +(13x^12-17x^14)*a^2.

Its degree is46. With m=125000, n=220653, the homogeneous evaluation
n^46 P(m/n) is strictly NEGATIVE. The independent certificate saves
every coefficient and its full integer value; it begins
-7296822224397251035059412997387977328751962004379765... . The positive
denominator for E_G(r) is 25*n^24*a_num^2*b_num^3, where

    a_num=n^8-2m^5*n^3-m^8
         =4903943101894796717794731889784381951068961 >0,
    b_num=n^2-m^2=33062746409 >0.

Thus the sign is exact integer arithmetic, not floating approximation.
Also 5m=625000 < 3n=661959 proves 0<r<3/5<1. These inequalities give
2r^5+r^8<1 and r^2<1, so both geometric tails and their first derivatives
converge at r.

For the OLD subset without the rigid tail, the independently derived
Euler polynomial before clearing a^2 is

    V=25-48x+21x^4+22x^14+27x^16+28x^18+48x^19
                     +25x^20+80x^21+30x^22+80x^23+42x^24.

The degree40 polynomial V*a^2+(13x^12-36x^17-21x^20) has POSITIVE
homogeneous evaluation n^40 times its value at m/n, beginning
2282366024145303607452535395141506144309046278018140... . Only after
computing these signs did the child compare its fully reduced rational
values with the saved author JSON; both agreed exactly. The author
script was never executed or imported. All complete integers/fractions
are in this review's new `sign-v1.json`.

The certificate is a single prescribed finite sign check, not history,
factor, automaton, count-row, prime, root or trial enumeration. Dedicated
child PID32567 used an EXTERNAL10-second timeout, exited0 and was reaped
after0.0364934999961406 seconds. New source, start/job records, stdout
and empty stderr are frozen under this review prefix. No CAS or package
installation was used.

M2 now gives lambda>1/r=220653/125000=1.765224. The positive old sign
at THIS trial establishes the extra sign information from the rigid
tail at this point. It does not establish the best possible trial for
the old method. The accepted upper bound remains1.834856083.

## 5. Source hypotheses, preservation and scope

All new mathematical premises are the exact separately accepted
second/third-pass and M1--M3 results. Their complete operative bodies and
acceptance scopes were checked, without rerunning historical finite
certificates. A fresh read of Banderier's entire20-line page confirms
that its relevant parity/asymptotics sections are unfinished. It is not
an enumeration theorem or proof premise. Official attribution of the
four-move relation remains with the official solutions; this review
does not reproduce preliminary(a) or import a fixed-two-string hardness
claim, linear-language growth theorem or conjectural grammar.

The entire14-artifact constructor packet was read, including the FIRST
metadata checker and its retained path-format failure. Its repair only
resolves exact legacy problem-relative metadata paths; no mathematical
certificate was rerun by that repair. The review integrity freezer uses
the same path meaning while retaining a blind guard against new peer
SS metadata and findings. All prior own bytes and necessary accepted
fingerprints are verified compactly through immutable parent references.
No historical inventory is copied wholesale. Fingerprints are preservation
evidence, not mathematical verification.

One attempted read of a nonexistent documentary filename returned a
no-such-file error and changed nothing. No pending native job or tool
approval remains. No old/shared/Git/cache byte was edited, no worker
commit/push or spawn occurred, and no charge/contact/access bypass was
used. Requested settings and actual weekly telemetry are separately
recorded; effective-setting readback is not invented.

The unrestricted SS1/SS2 reasoning and finite SS3 arithmetic have distinct
roles. The new lower endpoint is modest. Exact lambda, the full obstruction
series, renewal regime, entropy-gap lower bounds, joining/mixing, original
output ratios and novelty remain open. Only the coordinator may reconcile
BOTH complete independent audits and promote this precise partial scope.
