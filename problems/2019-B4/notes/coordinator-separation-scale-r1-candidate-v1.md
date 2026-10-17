# A sharp linear agreement scale and a second known infinite tail

2026-10-17 UTC. **Candidate proof — unverified.** Root constructor;
TWO OTHER fresh initially blind WHOLE nonconstructor audits are required.
Requested gpt-6.1-sol/max; effective-setting readback unavailable.
Only the open part (b) is researched. No exact growth constant, annual
answer, positive renewal defect or novelty is claimed.

The rigid two-parameter collision family and the separation-three
regular family are ALREADY accepted project results. This packet does
not rediscover either family. It uses the first to show that the exact
agreement length of the capped language really is linear in its cap,
then combines the two known infinite families as SETS. One small exact
rational sign certificate is used for a proposed improved lower bound.
It enumerates no histories, factors, count rows or automaton states.

## 0. Exact accepted inputs

Use the actual canonical history language K, its minimal obstruction
set F, the counts c_n, and the growth rate lambda of BOTH canonical
contexts and the original distinct strings. Their equality of root
rates is accepted; polynomial prefactors and adjacent original-output
ratios are not identified. Let R=1/lambda. The complete accepted
second-pass renewal and rigidity, third-pass capped-language theorem,
and moment-tail M1--M3 give:

    C(z)=1/(1-2z+F(z)), F(R)=2R-1, F'(R)<=2,
    K_D=Avoid(F_D), D>=1,
    F_D={f in F: some strictly upper witness has separation<=D}.

F is factor-free. F_D agrees with F through length2D+1. A witness's
separation is max_t(L_g(t)-L_h(t)), using source-time left counts.
The accepted rigid family, for p,q>=1, is

    H(p,q)=RRL R^(2p) LR L^(2q) RLL,
    K(p,q)=LLR L^(2q) RL R^(2p) LRR.

These have EXACTLY the same chronological context, whose only histories
are those two. All proper factors have unique contexts, and H(p,q)
is in F. Distinct parameters give distinct words. The existing family
generating function is z^12/(1-z²)^2. No assertion that EVERY f has
only two histories is made; that stronger claim is already false.

The other accepted family is

    F_3 = RRLL | RRLRRLRL (RRLRL | LRLRL | LRLRRLRL)* LRLL,
    F_3(z)=z^4+z^12/(1-2z^5-z^8).

Its words have every run of length at most2, with the stated
unambiguous loop expression. The complete accepted polynomial through24 is

    P24=z^4+z^12+2z^14+3z^16+2z^17+4z^18+8z^19
             +6z^20+20z^21+14z^22+40z^23+42z^24.

For ANY actual subset G of F containing all words of length<25,
the accepted moment sign criterion is

    E_G(t)=1-(48/25)t+G(t)-(t/25)G'(t),
    E_G(r)<0 and convergence at r  ==> lambda>1/r.       (M)

This uses the actual first-moment bound, with no simple-pole or
finite second-moment hypothesis. The earlier lower bound is1.76522347;
the accepted upper bound is1.834856083.

## 1. SS1: the first capped count discrepancy is at 2D+O(1)

Let tau_D be the least n for which |K_D intersect {L,R}^n|>c_n.
Then tau_D exists for EVERY D>=1 and

    2D+2 <= tau_D <= 2D+8  when D is even,
    2D+2 <= tau_D <= 2D+10 when D is odd.             (SS1)

First take p=q=d>=1. K(d,d) is the letterwise side-exchange of
H(d,d). Thus their left-count difference equals t-2L_H(t).
Read H in its seven displayed runs/blocks. Its successive difference
values are:

* across RRL:1,2,1;
* across R^(2d): increasing from1 to2d+1;
* across LR:2d,2d+1;
* across L^(2d): decreasing to1;
* across RLL:2,1,0.

Every internal difference is strictly positive, including d1.
The maximum is EXACTLY2d+1. Since there are only two histories for
this context, this is the MINIMUM possible upper-witness separation
for H(d,d), not merely the width of a convenient witness. Its length
is4d+8=2(2d+1)+6.

For even D choose2d+1=D+1; for odd D choose2d+1=D+2. These give
d>=1 at all endpoints D>=1. The selected H has no cap-D witness,
so belongs to F minus F_D and has the claimed upper-bound length.

To relate this to counts precisely, let m_D be the least length in
F minus F_D. Such a length exists by the construction. Below m_D,
the two avoidance languages agree: any forbidden factor for K in a
word of that length would already belong to F_D. At length m_D,
an omitted f avoids EVERY F_D factor, because F is factor-free and
f itself is not in F_D. Thus f belongs to K_D minus K. Consequently
tau_D=m_D, and the accepted agreement through2D+1 gives the lower
bound. This proves all of SS1 without a scan.

The conclusion concerns EXACT prefix agreement, not entropy error.
It excludes a proposed universal quadratic agreement length for this
actual cap construction. It does NOT rule out faster convergence of
the actual growth rates by a different tail/mass argument, and it
does not prove a matching lower bound for rho_D-lambda.

## 2. SS2: the exact union with the rigid infinite family

Write Hset={H(p,q):p,q>=1}. Its intersection with F_3 is EXACTLY
{H(1,1)}. Indeed, whenever p>=2 or q>=2 the displayed word has a
run of at least4, whereas every F_3 word has runs at most2. At p=q1,
the length12 word is exactly the long branch of F_3 with no loops.
This proves the intersection as WORD SETS, not by comparing counts.

Put

    G=(F of length<=24) union F_3 union Hset.

The long F_3 prefix through24 is
z^12+2z^17+z^20+4z^22. The rigid prefix through24 is

    T24=z^12+2z^14+3z^16+4z^18+5z^20+6z^22+7z^24.

For the latter coefficient, length2p+2q+8 fixes p+q, giving exactly
p+q-1 positive pairs. All these prefix words are already in P24.
After removing both prefixes, the two remaining tails are DISJOINT,
because their entire intersection was the removed length12 word.
Thus the following is the exact series of G:

    G(z)=P24(z)
       +z^12/(1-2z^5-z^8)-z^12-2z^17-z^20-4z^22
       +z^12/(1-z²)^2-T24(z).                       (SS2)

Every coefficient is nonnegative by the set-union proof. Formal
subtraction is used only for overlaps proved to be known words.
G is a subset of the ACTUAL F and contains its complete prefix
through24; no new full obstruction coefficient beyond24 is asserted.

## 3. SS3: an exact rational lower endpoint

Take the single prescribed trial

    alpha=220653/125000=1.765224,
    r=125000/220653.

The saved standard-library Fraction certificate verifies EXACTLY

    1-2r^5-r^8>0, 1-r²>0, r<3/5,
    E_G(r)<0.                                      (SS3 sign)

These strict rational inequalities are stored with their complete
integer numerators/denominators. The two geometric tails and their
derivatives converge at r: the first denominator condition gives
2r^5+r^8<1, and0<r<1 gives convergence for the second. Therefore(M)
applies to the actual subset G and yields the candidate strict bound

    lambda>1.765224.                                (SS3)

At this SAME trial the earlier subset without the rigid tail has
POSITIVE E, also recorded exactly. Hence the new tail supplies
additional sign information at this precise trial. This is not a claim
that no other old-method trial could improve the older endpoint.
The old upper bound is unchanged. No numerical root, fitted recurrence,
finite history sample or floating-point eigenvalue enters the proof.

## 4. What this does and does not establish

SS1 makes the exact agreement scale precise up to an additive constant.
SS2 uses two already accepted infinite families with their overlap
fully controlled. SS3 is a modest proposed lower-bound improvement.
None evaluates lambda, distinguishes the defective/critical renewal
regime, proves bounded joining, determines original-output ratios,
supplies the missing entropy-tail theorem or solves the annual target.

The initial tempting quadratic agreement idea had used the staircase
family's quadratic length as intuition. The accepted rigid family
has a linear length/width relation, so that inference is unavailable.
Conversely, one missed obstruction per cap does not imply an entropy
gap of order1/D: its weighted mass can be very small. No such gap is
claimed.

The new sign script is a proof-critical EXACT rational certificate,
not a new enumeration. One child PID31896 ran with an external10second
timeout, exited0 and was reaped after0.04163237498seconds. Source,
full fractions, stdout, empty stderr, start and completion records are
retained. It was not rerun. No package or paid API was installed/used.

All mathematical inputs above are the repository's accepted full
second/third-pass and moment-tail results. Their complete operative
bodies and acceptance scopes were reread for this construction.
Root constructed the older moment-tail packet and is not independently
recertifying it. The new result still needs TWO OTHER WHOLE audits.
No preliminary part(a) proof is reproduced. A fresh primary Banderier
web page on parity-constrained Dyck shuffles proved to be an unfinished
outline; no enumeration theorem from it is imported. Primary source
attribution for the older methods remains in their immutable ledgers.

All older frozen mathematical bytes remain unchanged. No full third-party
paper is tracked. Novelty and external validation remain unestablished.
