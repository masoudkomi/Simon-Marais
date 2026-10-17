# MR1 and conditional MR2: complete initially blind whole review R1

2026-10-17 UTC. Reviewer `/root/review_2022_complexity_r2`.
Requested gpt-6.1-sol, reasoning max; independent effective-setting
readback unavailable. **Initial whole audit; not coordinator promotion.**

No substantive defect is identified in either complete claimed theorem.
The signed-recurrence proof gives MR1 with precisely the stated strict
indices. The finite-union injection and accepted unconditional ratio
limit give MR2 under its explicitly UNPROVED uniform joining hypothesis.
Nothing in this review proves that hypothesis or selects the actual
defect/mean regime. The 32-check companion ledger covers all 12 complete
author obligations. No mathematical program, sample, CAS, finite count
scan, certificate replay or constructor script was run.

## 1. Independence, exact target and actual complete reads

Root constructed the new MR submission and cannot count as either of its
two independent reviewers. I did not construct or contribute to MR1,
MR2 or the separate short-joining research lead. I previously independently
reviewed the moment, nonregularity, linear-output and complete R7 packets.
Those older roles are disclosed; they are not a new audit of my own work
and are not counted as fresh recertification of the accepted premises.
No other NEW MR peer report, ledger or finding was read before this
complete initial packet froze.

Exact main target, relative to `problems/2019-B4/`:
`notes/coordinator-monotone-ratio-return-v1.md`, 9239 bytes, SHA256
`67649f48ebd0f599461fa01cde4e5c37c8fdff0781b9decf4430705848396c29`.
Exact manifest: `notes/coordinator-monotone-ratio-manifest-v1.json`,
1763 bytes, SHA256
`0af3087adb6814707b7c9257985256b882def1081f339a371b456af4f88dec8f`.

I read AGENTS.md, the entire new main including both proofs, source/role/
worklog limitations and all 12 obligations, and its manifest. This small
packet has no separate frozen source or worklog companion: those records
are sections of the complete main. I also read the entire canonical
renewal body, second-pass accepted register and acceptance records,
the entire accepted R7 body and acceptance JSON, the initial accepted
proof and acceptance scope, the second-pass checkpoint-2 text, the
official-domain normalization, and the entire separate short-joining
research note. The latter is explicitly outside the proof premises.
An output truncation in a combined read was repaired by rereading the
complete affected R7 introductory acceptance section; it does not leave
an unread mathematical passage represented as read.

## 2. Official sequence versus the canonical count

The official 2019 B4(b) target concerns distinct binary output strings:
start at the seed 1 and add 0 at odd length or 1 at even length, at
either end. It asks for the lower and upper root-growth limits. No
preliminary-part proof is investigated here.

The new theorem concerns the accepted canonical history language K.
A history writes alternating bits 0,1,0,1,... onto two chronological
tapes, and K contains the lexicographically least history for each
tape pair. It has one representative for each marked chronological
context, not one for each unmarked physical output. Write c_n for its
length-n count, with c0=1. These are positive finite integers: at least
one tape pair occurs at every length, and its finite fiber has a least
history. Histories, marked contexts and original strings are not
interchanged in either new argument.

The accepted context comparison gives the same root growth lambda for
c_n and the original b_n, but does not give equality of their counts
or convergence of b_n/b_(n-1). The current accepted enclosure remains
1.76522347<lambda<1.834856083. MR neither computes counts nor changes
that numerical enclosure or evaluates lambda.

## 3. Exact renewal and the first nonzero obstruction

I checked the complete accepted renewal body and its accepted register.
Canonical histories form a factorial language; minimal noncanonical
factors F are factor-free. The accepted upper-witness grid argument
excludes every proper suffix-prefix overlap: two shifted upper witnesses
must meet between the overlap endpoints, furnishing a smaller equal-
context history for a proper factor. Phase complement preserves equality
at odd as well as even starting indices. These facts justify the actual
full-language renewal bijection, rather than one for a cap or a regular
approximation.

Appending either letter to a canonical prefix gives 2c_(n-1) words.
A newly bad word has a unique minimal forbidden suffix. Removing it
leaves a canonical prefix, and conversely each canonical prefix followed
by a minimal bad factor gives just such a bad extension. A crossing
second forbidden factor would create an excluded overlap. Therefore

    c_n=2c_(n-1)-sum_(j=2)^n f_j c_(n-j), n>=1,
    f_j=|F intersect {L,R}^j|>=0.

Here f1=f2=f3=0. The accepted finite prefix gives f4=1. There is also
a direct structural check requiring no enumeration: the accepted witness
lemma forces every minimal bad factor to begin RR and end LL. At
length four the only possible one is RRLL; LLRR is a smaller history
for the same two chronological tapes (both tapes are 01 at starting
phase zero), while every shorter factor is canonical. Thus exactly
RRLL occurs at length four. This is a check of the already accepted
coefficient, not a new count table or preliminary-part solution.

The equality counts the ACTUAL full minimal obstruction language. Its
generating function is C(z)=1/(1-2z+F(z)), where F(z)=sum f_jz^j.
All summands at a fixed coefficient are finite. Nonnegativity of every
f_j and positivity of the ENTIRE c sequence are the hypotheses needed
by the new comparison. No finite-prefix absence is extrapolated.

## 4. The general signed-recurrence induction, with every index

Let a0=1, a_n>0, alpha>0, b_j>=0 for j>=2, and

    a_n=alpha a_(n-1)-sum_(j=2)^n b_j a_(n-j).

Define r_n=a_n/a_(n-1) only for n>=1. At n=1 the sum is empty,
so a1=alpha and r1=alpha. At n=2,
r2=alpha-b2 a0/a1<=r1, with positive denominator. Assume the
ratios are nonincreasing through r_(n-1), for n>=3.

For every common index 2<=j<=n-1, the two ratios of recurrence
terms satisfy the EXACT identity

    (a_(n-j)/a_(n-1))/(a_(n-j-1)/a_(n-2))
       =(a_(n-j)/a_(n-j-1))/(a_(n-1)/a_(n-2))
       =r_(n-j)/r_(n-1)>=1.

The smallest numerator index is n-j=1, so this never invokes r0
or a negative-index a. Every a in the displayed denominators is
positive, including a0 if n-j-1=0. Dividing the recurrences at
n and n-1 by their respective positive preceding terms and subtracting
gives

    r_(n-1)-r_n
       =sum_(j=2)^(n-1) b_j [a_(n-j-1)/a_(n-2)]
                    [r_(n-j)/r_(n-1)-1]
          +b_n a0/a_(n-1).

Every common summand and the extra j=n term is nonnegative. Thus
r_n<=r_(n-1), closing the induction for every n. The extra terminal
term is kept separately; falsely applying the common-term ratio to
it would introduce an invalid negative index. The lemma does NOT
cover a recurrence that eventually gives zero or negative terms;
global positivity is explicit. Zero b_j are allowed and need not give
strictness. No assertion about arbitrary positive sequences or arbitrary
avoidance languages follows without this particular recurrence.

## 5. Application and strictness at every claimed index

Apply the lemma with a=c, alpha=2 and b_j=f_j. The exact initial
coefficients give

    c0=1, c1=2, c2=4, c3=8, c4=15,
    rho1=rho2=rho3=2, rho4=15/8<2.

For n>=5 the j=4 term exists in the common sum. Inductively
rho_(n-2)>rho_(n-1), with base rho3>rho4 when n=5.
Already-proved nonincrease gives

    rho_(n-4)>=rho_(n-2)>rho_(n-1).

At n=5 this reads rho1>=rho3>rho4, and the multiplier is
f4*c0/c3>0, so no zero or negative subscript is hidden at the
endpoint. At all larger n the multiplier
f4*c_(n-5)/c_(n-2) stays strictly positive. Hence this one common
summand is strictly positive and all remaining summands are nonnegative.
It follows that rho_n<rho_(n-1) for every n>=5. Together with
rho4<rho3 this is exactly rho_(n+1)<rho_n for every n>=3.

Since the counts are positive,

    rho_(n+1)<=rho_n iff c_n²>=c_(n-1)c_(n+1).

There are equalities at n=1 and n=2 and strict inequalities at every
n>=3. This checks the statement's log-concavity indexing, not only
the direction of ratio monotonicity.

The accepted R7 theorem already proves each rho_n>lambda and
rho_n->lambda. Thus the minimum of the first N ratios is exactly
rho_N, remaining strictly above lambda for every finite N and
decreasing strictly from the N=3 to N=4 transition onward. Individual
algebraic lower roots from R7 are not thereby monotone; their finite
maxima retain the previously accepted nested-bound property. This
adds monotonicity, not new numerical data. R7's diagnostic about a
generic submultiplicative sequence is consistent: such a sequence
need not have this signed recurrence with all f_j nonnegative.

## 6. R7 authority used in the conditional theorem is unconditional

I read the COMPLETE accepted R7 body and checked the needed implications,
rather than using my old review verdict as a new premise. Let R=1/lambda,
delta=2-F'(R)>=0. At the actual endpoint, accepted renewal gives
F(R)=2R-1, finite F'(R)<=2 and 1/2<R<1.

For n>=1 set q_n=sum_(j>n)f_jR^j, but set q0=0 deliberately. The
positive coefficient factorization gives

    1-2Rx+F(Rx)=(1-x)(1-Q(x)),
    Q(1)=1-Rdelta<=1, Q(x)=sum_(n>=1)q_nx^n.

The formal series U=1/(1-Q)=sum u_nx^n has u0=1 and 0<u_n<1
because q1=2R-1 lies strictly between zero and one. Consequently
s_n=c_nR^n=sum_(j<=n)u_j increases strictly. The identity
rho_n=lambda*(1+u_n/s_(n-1)) proves rho_n>lambda. If s_n is
bounded, its increments u_n tend to zero; if it is unbounded, u_n<1
and s_(n-1) tends to infinity. In either case rho_n->lambda.
Thus this limit does not assume positive defect.

When delta>0, summing the nonnegative geometric series gives
sum u_n=1/(Rdelta), and s_n tends to that finite number. When
delta=0, Q(1)=1 and U(x) tends to infinity as x increases to one;
nonnegative monotone convergence gives sum u_n=infinity. Therefore

    s_n bounded iff delta>0,
    if bounded, lim s_n=1/(Rdelta).

No analytic continuation, simple-pole assertion or finite second moment
is needed for these facts. The complete accepted R7 critical finite-
and infinite-mean alternatives and its original-output fiber limits
remain retained; MR does not select or strengthen them unconditionally.

## 7. Uniform joining: finite-union injection with variable bridges

MR2 assumes the additional property J_C for ONE FIXED integer C>=0:
for every u,v in the ACTUAL K, there exists w with |w|<=C and
uwv in K. The bridge is allowed to depend on the entire pair and
its length may vary. No single common w, unique bridge, common
parity or regular finite model is assumed. The uniform bound over
all pairs, before any limit, is essential and UNPROVED here.

Fix n,m>=0. The two sets of canonical words are finite. Select one
allowed bridge for each pair, for example the first under length then
lexicographic order. If the chosen length is k, the resulting word
is in K_(n+m+k). Its prefix of known length n recovers u, and its
suffix of known length m recovers v. These pieces cannot overlap,
since the total length is n+m+k with k>=0. Thus two different pairs
cannot map to the same word. Different k give different total lengths,
so the codomain is the DISJOINT union, not a union with uncounted
length collisions. Counting yields

    c_n c_m<=sum_(k=0)^C c_(n+m+k).

The empty word belongs to K, so n=0 or m=0 has the same proof,
with empty known cuts and no ambiguity. This injection is between
literal canonical history words, not between equivalence classes of
arbitrary histories or unmarked output strings. No context-collision
correction is missing.

## 8. Correct order of limits and the exact defect inequality

Divide by c_m>0. With n fixed, k fixed and m tending to infinity,
the unconditional accepted ratio limit gives

    c_(m+n+k)/c_m
       =product_(i=1)^(n+k)rho_(m+i)
       ->lambda^(n+k).

If n+k=0 the product is empty and exactly one. Since C is fixed
and finite, the sum contains finitely many such products; passage to
the limit yields

    c_n<=lambda^n S_C, S_C=sum_(k=0)^C lambda^k.

This is valid for each n, giving the single uniform bound
s_n<=S_C for all n. No uniform ratio convergence in growing k or
growing n is used, and no boundedness is assumed while proving the
ratio limit. There is no reliance on MR1's new monotonicity in this
implication.

The exact accepted boundedness criterion then forces delta>0. Finally,
take n to infinity in s_n<=S_C and use the finite limit above:

    1/(Rdelta)<=S_C,
    delta>=1/(R S_C).

Both factors R and S_C are positive and finite, so this rearrangement
has the stated sign and includes equality as a permissible conclusion.
It is not a numerical positive-defect bound until an actual uniform
C is established. In particular a bound C(n,m) or bridges known only
for a finite list of lengths would not justify it.

## 9. Degenerate boundaries and failed stronger readings

At C=0 the implication is still valid as a conditional theorem. Its
antecedent would say K is closed under concatenation, and is actually
false: RR and LL are canonical, but RRLL is not. That simple boundary
does not refute MR2, which does not claim J_0 or J_C for any C.
I do not promote the separate root note's J_2 obstruction or length-8
J_3 diagnostic to an accepted theorem in this review. That note is
unverified research context; its reported absence of finite failures
cannot prove uniform J_3. No diagnostic data or word list enters the
strict-induction proof or the conditional finite-union injection.

Nor does log-concavity choose delta>0: the accepted critical alternatives
are not excluded by the new ratio inequalities. No ratio statement is
transferred to b_n through the marked-fiber comparison alone. No
individual lower-root monotonicity, rationality, algebraicity, simple
pole, analytic continuation, exact lambda, full annual evaluation or
priority is inferred. The candidate expressly preserves these gaps.

## 10. Sources, preservation and disposition

The new arguments are proved directly by finite sums and fixed-length
products. No new external theorem is imported. Canonical renewal and
R7 are exact accepted inputs, with source read scopes and acceptance
authority recorded separately. Generic Kaluza/reciprocal-series search
context and cross-bifix-free-code metadata are not substituted for a
theorem about this actual language. The source record does not claim
that unidentified search material or an unread theorem was audited.

Only NEW files in `problems/2019-B4/reviews/monotone-ratio-review-1-*`
are written. The metadata freezer binds the constructor's main and
manifest, all five declared accepted input records, additional actually
read bodies/scopes, old accepted hash maps, and all previous own frozen
artifacts. Prior records are preservation only, without mathematical
reruns. Old R7 peer report contents are not reread as a substitute for
the accepted theorem, and NEW MR peer findings stay unread until this
whole initial freeze.

Disposition: **no substantive scoped issue; no author repair requested.**
MR1 is unconditional from its accepted premises. MR2 is only the
implication from J_C, whose unrestricted truth remains open. Two OTHER
independent whole audits and coordinator reconciliation are required
before promotion. This audit makes no annual or novelty conclusion.
