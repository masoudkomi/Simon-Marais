# Bounded integer corrections of a hypothetical positive A/B lift

2026-10-17 UTC. **Research deduction — unverified.** Root constructor. This note is separate from the accepted R4 scope; it needs two fresh whole audits before any promotion. It supplies a limitation on a further expansion-multiplicity route, not an ordinary infinite lift or a termination proof.

Use the accepted full-step restricted A/B system

    10Q_(n+1)=11Q_n+h_n,

where each block is A:(h_(2j),h_(2j+1))=(0,0), or B:(−1,1). Assume an infinite POSITIVE ordinary integer lift Q_n exists. It must contain infinitely many B blocks: otherwise from some index on 10Q_(n+1)=11Q_n, and integrality at every later step makes that fixed positive starting integer divisible by arbitrarily high powers of10, impossible. This is only a conditional property; existence is not established.

Consider ANY bounded sequence of ordinary integers c_n, with corrections

    Z_n=Q_n−c_n,
    10Z_(n+1)=11Z_n+d_n,  0<=d_n<=10.

There is no causality assumption: c_n may be chosen with the entire future known. Subtracting the recurrences gives

    10c_(n+1)=11c_n+h_n−d_n.                 (1)

The proposed rigidity statement is that every such bounded correction is CONSTANT:

    c_n=c for all n, with c in{1,...,9},
    d_n=h_n+c.

Conversely every constant c in that range satisfies(1) and keeps all digits in the FULL alphabet0,...,10. This is not the narrower ceiling alphabet0,...,9.

## Lower escape

If c_n<=0, then using h_n<=1 and d_n>=0,

    c_(n+1)<=floor((11c_n+1)/10)<=c_n.

Thus it stays nonpositive. If it is0, the next occurrence of h=−1 forces c_(n+1)<=−1; such occurrences exist arbitrarily late because B occurs infinitely often. Once c_n<=−1, at every first step of a subsequent block we have h<=0 and

    c_(n+1)<=floor(11c_n/10)<=c_n−1.

At intervening steps it cannot increase. There are infinitely many block-first steps, so c_n is unbounded below, a contradiction. Therefore a bounded correction satisfies c_n>=1 at EVERY index, not merely eventually.

## Upper escape

From h_n>=−1 and d_n<=10,

    c_(n+1)>=c_n+ceil((c_n+h_n−10)/10).

For c_n>=10 this is at least c_n, so it never drops below that value. If it is10, the next h=1 forces it at least11; these events occur infinitely often. Once c_n>=11, at each block-second step h>=0 and the displayed ceiling is at least1. At other steps it remains nondecreasing. Thus it is unbounded above, again a contradiction. A bounded correction therefore has c_n<=9 at EVERY index.

## Interior rigidity

For1<=c_n<=9, equation(1) becomes

    10(c_(n+1)−c_n)=c_n+h_n−d_n.

The right side lies in[−10,10], so the integer difference can only be−1,0,1. The value−1 is possible only when c_n=1,h_n=−1,d_n=10, and then c_(n+1)=0, already excluded. The value1 is possible only when c_n=9,h_n=1,d_n=0, and then c_(n+1)=10, also excluded. Hence the difference is zero at every step. Then(1) gives d_n=h_n+c as asserted. For each c1,...,9 these digits lie in0,...,10, proving the converse.

## Growth-equivalent integer trajectories

The same statement can be phrased without assuming a priori bounded c. For any ordinary integer Z trajectory with digits0,...,10, both limits

    C_Q=lim Q_n(10/11)^n,
    C_Z=lim Z_n(10/11)^n

exist by the convergent correction series, since h and d are bounded. More explicitly,

    Q_n=C_Q(11/10)^n−sum_(j>=0) h_(n+j)/(11(11/10)^j),
    Z_n=C_Z(11/10)^n−sum_(j>=0) d_(n+j)/(11(11/10)^j).

Each displayed tail is uniformly bounded. Thus C_Z=C_Q forces Q_n−Z_n bounded, and the rigidity proof applies. Exactly the nine constant offsets give the same growth coefficient at this common index normalization. Each offset indeed has that coefficient because a fixed integer times(10/11)^n tends to zero. This conclusion does not assert an ordinary-integer bijection for the inverse-limit maps.

The accepted positive A/B lift, if it exists, has Q_n>=81 at every full step (accepted R4E2), so these nine Z_n are positive and can supply admissible finite-prefix paths under the earlier rational-base construction. This note does not separately classify EVERY real expansion with arbitrary radix/left normalization; that would require matching that representation convention to the common-index condition above. It does prove that no tenth bounded integer correction, even chosen with future knowledge, enlarges this exact full-alphabet trajectory family.

This explains a limit of trying to force more than the nine already obtained paths by adding bounded carries. The source upper multiplicity bound of11 permits nine and still gives no contradiction. No claim of at-most-nine for all reals, no no-triple theorem, no universal termination, no infinite positive ordinary counterexample, and no full annual or novelty result is made. All-A zero and other nonpositive or finite paths are outside the hypothesis. Full ten-control paths may have different h and are not classified here. No mathematical code, CAS, scan or certificate rerun was used.
