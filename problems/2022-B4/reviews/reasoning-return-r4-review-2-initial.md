# E1–E2 and V1–V4: independent whole initial audit R2

2026-10-17 UTC. Reviewer `review_2022_complexity_r2`; requested gpt-6.1-sol/max, independently verified effective-setting readback unavailable. This report is frozen before reading any new R4 peer finding or coordinator reconciliation. Constructor of the submitted R4 packet: `review_2017_coarsening_r1`, with the coordinator's power100 shadow lead disclosed in its log. Neither construction role is counted as an independent audit. This reviewer did not construct or supply the new R4 proofs. The packet remains **candidate proof — unverified** until the coordinator completes the prescribed process.

## Outcome and prior-role disclosure

I find no substantive objection to the exact E1–E2/V1–V4 claims, and request no author repair. I reconstructed all six new claims, including full prefix admissibility, the ninth full-alphabet expansion, every stopped-branch index, both-prime valuation proofs, the normalized binomial congruence, finite-shadow universality, and the inverse-limit/ordinary-domain counterexample. The companion ledger contains58 inference checks covering all28 author obligations. No termination, positive infinite avoiding lift, novelty or full annual solution is established by this review.

The complete target is `notes/reasoning-return-r4-candidate-v1.md`,23750 bytes, SHA256 `cf3df09a2b38097bcbbe5c80c332a9bf1787f07a2114bf67b6108651240e2b2a`. The constructor's eight-artifact freeze is3530 bytes, SHA256 `f579d150c8b52450e5c20630fd36621ba8d36c3a6168c23235d352068c413f66`. I read the entire main proof, source audit, worklog, failed-routes note,28 obligations and administrative source/freeze records.

I authored the EARLIER, separately accepted R0–R3/S1–S2 packet, whose full preserved body is in `proofs/reviewed-return-r3-v1.1.md`. It had two OTHER independent whole audits and coordinator acceptance. I also previously independently audited the arithmetic-complexity packet. This report is not presented as a fresh independent audit of my own older R3 theorem. I read its complete accepted body and exact scope as an input, and reconstructed every NEW R4 inference. The new E1–E2/V1–V4 proofs and power100 shadow strategy were not my construction. This prior role was disclosed to the coordinator before reporting any mathematical finding. No new R4 peer report or conclusions were read.

## 1. Official domain and exact restricted input

The [official2022 Paper B, page2 B4(b)](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2022-paper-b.pdf) was directly reopened. Starts are positive ordinary integers, their product is at least600 inclusively, both updates use the old pair, and equality at time0 counts. Only(b) is audited. The attributed preliminary strip result is background; it is not reproved here.

I read all four complete accepted bodies: initial partials, repaired fixed-offset density, attributed arithmetic complexity, and the full R0–R3/S1–S2 return exposition. I checked the initial, complexity and return acceptance scopes. Finite lifting, density one, irrational examples, or a bounded-carry obstruction do not already resolve an individual infinite ordinary orbit.

The logical restricted input is the A/B loop arithmetic at(d,r)=(1,0). The exact quotient equation is10Q'=11Q+h. LoopA has controls(0,0), residues0,0,0 and corrections(0,0); loopB has controls(1,9), residues0,6,0 and corrections(−1,1). At residues0 and6, c(1,r)=0 and d'=1, so the claimed loop states are correct. For X_j=Q_(2j), composition gives

    100X_(j+1)=121X_j−w_j.

The B correction is11*(−1)+10*1=−1. For ordinary X, A requires X=0 mod100; B requires X=81 mod100 because21*81=1 mod100. These also ensure the intermediate controls: an A first quotient11X/10 is0 mod10, while a B first quotient(11X−1)/10 is9 mod10. Conversely these controls force the same classes. The final block equation has not lost an intermediate condition.

On these two classes, the block map is respectively121X/100 and(121X−1)/100, hence floor(121X/100). It STOPS on every other class. With Y=X−1, the correction in100Y'=121Y+21−w is21 or20, exactly the least nonnegative ceiling correction for Y=99 or80 mod100. This equivalence concerns the stopped domain; the unrestricted floor and ceiling maps are not claimed conjugate on all integers. A positive infinite lift yields the actual contest pair(60X_0+1,60X_0), whose differences stay1. Leaving this subfamily does not itself mean equality has occurred in the full contest dynamics.

## 2. E1: finite integer language before real multiplicity

Fix coprime p>q>=2 and beta=p/q. The source convention is val(a_k...a_0)=(1/q)sum a_i beta^i, using ALL digits0,...,p−1. This differs from ordinary greedy beta-expansions. Modified division qN=pN'+a with0<=a<p strictly decreases positive N, so it terminates and gives a finite canonical integer representation. Its successive prefixes represent the reversed chain of earlier integer states.

For any length-m word of ordinary integer value N, multiplying its value formula by q^m and reducing modulo p gives a_0=qN modp: the factor q^(m−1) is invertible modulo p. The prefix value is(qN−a_0)/p, an integer. Repetition proves uniqueness after ignoring leading zeros. In particular if qN_next=pN+d with d in the full alphabet and both states ordinary positive integers, appending d to N's canonical word recovers exactly N_next by its last modified-division step. This proves prefix admissibility rather than assuming a digit series is automatically in the rational-base language.

From qQ_(n+1)=pQ_n+h_n and bounded ordinary integer h_n, real iteration yields

    C=Q_0+sum_(n>=0) h_n/(p beta^n).

The sum converges absolutely. If H=max(|L|,|U|), the omitted geometric tail after multiplication by beta^n is bounded by H/(p−q), giving Q_n=C beta^n+O(1). The explicit hypothesis C>0 therefore gives eventual positive growth. It cannot be inferred from an arbitrary Z10 lift.

Because p−q>0, the shift interval defined by L+(p−q)c>=0 and U+(p−q)c<=p−1 is finite. If it is empty, the lemma asserts nothing. Otherwise choose one N with Q_n>max Cset for ALL n>=N. For each allowed c,

    Z_n=Q_(N+n)−c>0,
    d_n=h_(N+n)+(p−q)c,
    qZ_(n+1)=pZ_n+d_n.

The sign of the shift and correction is correct. All digits are in0,...,p−1. Begin with the finite canonical word for Q_N−c and append these digits. Every finite prefix, both within the seed and afterward, belongs to the integer language up to harmless leading zeros.

With the radix point after the seed, the appended digit d_n has exponent−(n+1), so its weight is d_n/(q beta^(n+1))=d_n/(p beta^n). Therefore the real value is

    Q_N−c+sum d_n/(p beta^n)
      =Q_N+sum h_(N+n)/(p beta^n)=beta^N C,

since the constant correction's geometric sum is exactly c. Pad all finitely many seed words on the LEFT to one common length m. Moving the radix point before these common-length seeds multiplies every value by the SAME beta^(−m). This produces root-language expansions of one positive value beta^(N−m)C, not separately rescaled numbers.

Different shifts give tails differing by the nonzero constant(p−q)(c−c') at every aligned position. They remain distinct after common padding. A purported extra leading-zero copy of a normalized fractional stream would multiply its positive value by a nontrivial beta power, so it cannot identify two streams of the same positive value. Equivalently, with their radix indices fixed, removal of leading zeros does not remove the infinitely many tail differences. E1 is consequently a genuine expansion-multiplicity lemma, not merely a real-series equality.

The general endpoints p>q, q>=2, a one-element shift set, or negative shifts pose no difficulty. C<=0 and an empty shift interval are expressly outside the multiplicity assertion. No theorem about all rational-base digit words or arbitrary inverse-limit controller states is inserted.

## 3. E2: nine expansions, correct branches, and an unproved hypothesis

A positive allowed block X is at least81. At each full-time step h>=−1, and(11Q−1)/10>Q for Q>=81, so every intermediate Q_n remains at least81. Subtracting c=1,...,9 is valid from time0. Grouping the signed correction pairs in the REAL growth series gives

    C=X_0−sum_(j>=0) w_j 100^j/121^(j+1),
    0<=sum<=1/21.

Indeed the pair contributes−1/(11 beta^(2j))+1/(11 beta^(2j+1))=−1/(121 gamma^j), gamma=121/100. Thus C>0. The real sum is not identified with the inverse-limit sum written with the same formal terms.

For p11,q10,L−1,U1, E1 gives exactly c=1,...,9 and digits h+c in0,...,10. Each seed is the ordinary positive X_0−c; all appended prefix values are Q_n−c. Hence all nine are admissible. With radix after the seed their value is C; with one common root normalization it is the same positive scaled C for all nine. The conclusion is AT LEAST nine, not exactly nine total.

At an ordinary nonnegative integer node z, allowed digits satisfy d=−11z mod10 with0<=d<=10. If z is not divisible by10 there is one digit in1,...,9. If z is divisible by10 there are precisely0 and10. The least choice gives ceil(11z/10), while the greatest gives floor((11z+10)/10). Direct calculation also verifies max(z)+1=min(z+1). These are successor states; minimal/maximal words are the tails from their respective integer seed nodes, not nine different globally minimal root paths.

The shifts c1,...,8 have digits0,...,9 and therefore follow the least branch. Shifts c2,...,9 have digits1,...,10 and follow the greatest branch. The common c2,...,8 tails use1,...,9 only; every one of their nodes has a single child, so these seven rays are both minimal and maximal. The c9 tail uses digit10 on every h=1 occurrence and cannot be treated as an extra ceiling orbit.

There are infinitely many B steps in a positive infinite A/B orbit. An all-A tail would require100^m to divide one fixed positive integer X for every m, because121 is coprime to100. This is impossible. Thus h=−1 and h=1 both occur infinitely often. It follows that the constant shifts fitting THIS full correction sequence are exactly1,...,9, with c1 not maximal and c9 not minimal at those recurring branch times. Among the nine supplied rays the minimal/maximal overlap is precisely the seven stated unary tails. No assertion about all other expansions follows.

I inspected the original rational-base definitions and multiplicity statements. [AFS Proposition37](https://perso.telecom-paristech.fr/jsaka/PUB/Files/RBNS-rev.pdf) permits k+1 expansions for integer k>(q−1)/(p−q); at11/10, k10 gives a bound11 and does not exclude nine. Its Corollary38 requires p>=2q−1, whereas11<19. [AEV Conjecture3.9 and Section3.3](https://arxiv.org/html/2510.11723v2) retain the general at-most-two assertion as a conjecture. Its conditional normality implication is not an unconditional theorem. The candidate therefore correctly states only: a no-ninefold theorem for positive reals would exclude positive A/B lifts. That hypothesis is not supplied or imported.

For the FULL signed controller bounds−10<=h<=10 at11/10, the shift inequalities require c>=10 and c<=0, so their interval is empty. A different actual path could have a smaller alphabet, but E2 has no uniform extension to the entire contest controller. Even proving the restricted stopped map terminates would not settle every avoiding path.

## 4. V1: all-time valuation balance and exact finite stopping

Use ordinary prime valuations only for positive integers. Starting from ANY time on a positive infinite restricted orbit, a later B must exist by the all-A argument. If k A steps occur before its next B, the unit at that B is121^k x/100^k, congruent to81 mod100. Since121 is a unit at both2 and5, this is possible only if

    nu_2(x)=nu_5(x)=2k.

This includes k0 at a current B state. It is necessary at every block time, not just at the initial input.

For a finite input with unequal valuations or common odd valuation, the first s=floor(min(a,b)/2) updates are A: before that time both valuations are at least2. After s updates at least one is0 or1 and the pair is not(0,0). The state is not divisible by100 and is not a unit of class81, so it is the FIRST stopping state. This includes s0, meaning the initial state itself is disallowed. If instead a=b=2k, exactly k initial A steps lead to the unit U=121^k x/100^k. That state stops unless U=81 mod100, in which case its next transition is B. Valuation balance alone is not enough.

At a B state U, A_U=121U−1 is positive and divisible by100. After B the value is A_U/100. Infinite continuation requires exact valuations2k at both primes for some k>=0 and the next unit condition, giving precisely

    nu_2(A_U)=nu_5(A_U)=2(k+1),
    U_next=121^k(121U−1)/100^(k+1)=81 mod100.

Conversely these constraints for ordinary positive U_j and finite nonnegative k_j give ordinary B followed by EXACTLY k_j A steps, then the required next B unit. The valuation condition itself also forces each U_j to be81 mod100. Concatenating all these finite blocks produces an infinite positive orbit. Every intermediate full-time control is restored by the accepted A/B correspondence. Thus the accelerated formulation is both-directional, while supplying no solution to its all-time ordinary-integer constraints.

Every allowed positive A or B step increases x, because the increments are21x/100 and(21x−1)/100 respectively, positive on their allowed positive classes. There is no descent argument hidden in the acceleration.

## 5. V2: fixed points, shadows and the second-B congruence

For the signed ceiling extension, ceil(121Y/100)=Y is equivalent to−100/21<Y<=0. Its integer fixed points are−4,...,0. Only−1 has an allowed residue99 or80 mod100. It maps to X0 and the contest pair(1,0), outside the official positive domain. This is a legitimate signed fixed point, not an admissible counterexample or a limit of positive ordinary starts.

Let K be a positive ordinary integer and start X_0=100^K. For0<=j<=K the initial formula is X_j=121^j100^(K−j). For j<K it is divisible by100, so these are exactly K initial A updates. At stateK, the unit121^K is1+20K mod100. It is81 precisely when K=4 mod5. Otherwise the first stop is stateK; no next update was allowed. If it is allowed, the first B at stateK gives Z=(121^(K+1)−1)/100 at stateK+1.

For EVERY positive r,

    nu_2(121^r−1)=3+nu_2(r),
    nu_5(121^r−1)=1+nu_5(r).

These follow elementarily. Removing an odd exponent via its odd geometric sum leaves the2-valuation unchanged, and each subsequent squaring adds one because the base remains1 mod8. For5, removing an exponent prime to5 gives a unit geometric sum, and each fifth power adds one: in(1+t)^5−1 the first term5t has strictly least5-valuation when5 divides t. Iteration proves the formulas without a hidden LTE theorem.

For r=K+1 divisible by5, the post-B valuations are a=1+nu_2(r), b=−1+nu_5(r). If unequal or common odd, V1 gives the first stopping state K+1+floor(min(a,b)/2). If equal2ell, necessarily ell>=1 and

    nu_2(r)=2ell−1, nu_5(r)=2ell+1,
    r=R_ell u, R_ell=2^(2ell−1)5^(2ell+1), gcd(u,10)=1.

Exactly ell A updates after the first B give the next unit

    U_2=121^ell(121^r−1)/100^(ell+1).

To determine it modulo100, let M=100^(ell+1). The first normalized binomial term of((1+120)^r−1)/M is120r/M=3u. The second is180u(r−1)=20u mod100 because250 divides r. For j>=3 the normalized term is

    3u*120^(j−1)(r−1)...(r−j+1)/j!.

Its2-valuation is at least3(j−1)−nu_2(j!)>=2(j−1)>=4. Its5-valuation is at least(j−1)−nu_5(j!)>=2; the elementary bound nu_5(j!)<j/4 proves this for every j>=3, including j3. In its original form binom(r,j)120^j/M, the only possible denominator primes are2 and5. The displayed bounds therefore prove integrality and divisibility by100, not just a formal congruence of an undefined fraction. Terms beyond j=r are zero.

It follows that(121^r−1)/M=23u mod100 and U_2=23*21^ell*u mod100. Since23^−1=87 and21^ell=1+20ell mod100, U_2=81 exactly when

    u=47+60ell mod100.

If that fails, the stopping state is K+1+ell. If it holds, the SECOND B is permitted at that state; no infinite-survival assertion follows.

For even K with K=4 mod5, r is odd and a1, so the post-B value is immediately disallowed: the first stop is K+1. Every other even K stops atK. The symbolic witnesses are also consistent: K249 has r250,ell1,u1 and U_2=83 mod100, hence stop251; K1749 has r1750,ell1,u7 and U_2=81 mod100, hence the second B is permitted. These are exact consequences of the displayed congruence, not executed orbit tests.

## 6. V3: two-prime isometry, residue bijections and finite continuations

Fix ell>=1, R=R_ell, M=100^(ell+1), Lambda=121^R. The preceding valuation identities give

    nu_2(Lambda−1)=nu_5(Lambda−1)=2ell+2.

Thus Lambda=1 modM, and Phi_ell(u)=121^ell(Lambda^u−1)/M is an ordinary nonnegative integer for each u>=0, with Phi(0)=0. No p-adic exponential or logarithm is used to define it on those inputs.

For distinct nonnegative u,v, factor Lambda^u−Lambda^v by the unit Lambda^min(u,v). The remaining factor is Lambda^|u−v|−1, up to sign. The same geometric-sum and repeated-square/fifth-power argument applies, since Lambda=1 mod16 and1 mod5. Division by M subtracts exactly2ell+2 from each valuation, while121^ell is a unit. Hence

    nu_2(Phi(u)−Phi(v))=nu_2(u−v),
    nu_5(Phi(u)−Phi(v))=nu_5(u−v).

Both primes are essential. For EVERY N>=1 this proves well-definedness and injectivity on Z/(100^N), using both valuations>=2N. A self-map of that finite set is then surjective. The functions are induced by the same ordinary formula, so their reductions commute; their unique inverses commute as well. They give a bijection of the inverse-limit space Z10 because100^N=10^(2N) is cofinal among its moduli. This is a statement about a compatible-residue space, not an additive/multiplicative ring automorphism, a field, or a bijection of ordinary integers.

With v0, the identities also show Phi(u) is a unit at both primes exactly when u is. For positive unit u, set K=R_ell u−1. Then K is a positive ordinary integer, K=4 mod5, and r=K+1 has the exact balanced valuations required above. The shadow from100^K follows A^K B A^ell through every ordinary intermediate state and reaches EXACTLY Phi_ell(u), the next unit. These are ordinary exponentiations with ordinary exponents.

For completeness the finite lifting needed for an arbitrary binary word v=w_0...w_(N−1) can also be read directly from

    100^N X_N=121^N X_0
                −sum_(j=0)^(N−1) w_j121^(N−1−j)100^j.

Since121 is a unit modulo100^N, there is exactly one initial class. Peeling the congruence modulo100 at each step gives the A/B residue class at every intermediate block, and the accepted two-control argument supplies both full-time moves. When v begins B, its initial class x_v is81 mod100 and a unit.

The unique Phi preimage of x_v modulo100^N is therefore a unit class and has arbitrarily large ordinary positive representatives u. Each produces an actual ordinary K and follows A^K B A^ell v. All states are positive; the allowed positive A/B branches preserve positivity. Thus every prescribed finite post-B continuation beginning B occurs in this shadow family. Taking v=B^N proves that no uniform bound on the number of B updates can hold across all these shadows. This is stronger than long initial A delays and needs no scan.

For a fixed infinite v, the compatible classes determine only one u in Z10. The positive ordinary representatives, and K=R_ell u−1 as an ordinary exponent, may depend on depth. Nothing asserts a single ordinary positive u or defines100 to a nonordinary inverse-limit exponent. Finite realizations have not been promoted to an infinite positive orbit.

## 7. V4: a concrete failure of ordinary surjectivity

For ell1, R250 and M10000. Phi_1(0)=0. For every ordinary u>=1,

    Phi_1(u)>=121(121^250−1)/10000>81.

The last strict inequality already follows from replacing250 by2; monotonicity follows from Lambda>1. Thus81 has no ordinary nonnegative preimage. This is an actual image gap, not merely an unbounded search that failed to find one.

At each residue depth N the V3 permutation nevertheless gives a unique class mapping to81. The classes are compatible, unit classes, with arbitrarily large positive representatives. Their inverse-limit value u_* cannot be an ordinary nonnegative integer: otherwise the fixed ordinary difference Phi_1(u_*)−81 would be divisible by100^N for all N and hence equal zero, contradicting the image gap. No stronger claim that u_* is irrational or is not an ordinary negative integer is needed or made.

The target81 has one B transition to98 and then stops, since98 is neither0 nor81 mod100. V4 therefore diagnoses the ordinary-parameter completion fallacy; it is not an infinite avoiding target or a counterexample to the contest assertion. This exact example justifies the finite/infinite warning in V3.

## 8. Source and integrity disposition

The source record identifies all actual reading scopes. I read the complete accepted input bodies and the return attribution/scope, directly inspected AFS's modified division, node digits, evaluation, Proposition37 and Corollary38 in the original author manuscript, and checked the relevant AEV conjectural/conditional contexts. A read-only cached-PDF extraction supplied unambiguous source formulas. I also read the public author-uploaded original Dubickas–Mossinghoff Section1 and Proposition3.2 singleton proof/context. Their singleton result does not cover the two allowed classes80,99 modulo100. No new external theorem proves the missing no-ninefold or ordinary all-time assertion.

All eight constructor artifact hashes and the3530-byte freeze match. Its input-validation JSON has205 record occurrences over204 paths, all verified. The three accepted-scope JSONs contribute ten initial/density hash-map entries, eight complexity embedded records and one return-proof record, all checked without reading any new R4 peer report. All159 earlier own paths, including the full prior R3 construction, all-D global packet, GK audit and NR audit, remain unchanged. Only new files under the assigned review prefix were written.

No mathematical program, scan, CAS, coefficient/orbit enumeration, finite certificate or author rerun was used. Python performed only administrative byte/JSON checks and extraction of six named existing source-PDF pages. No source download, tracked full-paper copy, paid API, contact, access bypass, shared/Git mutation or spawning occurred. Direct account-wide telemetry at11:20:47UTC was33% TOTAL weekly use, reset1792745187. The90% TOTAL ceiling and reserve remain applicable. No substantive repair is requested; the coordinator alone may reconcile the two independent audits and accept the exact partial scope.
