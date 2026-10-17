# Quantitative cap gaps from the actual omitted rigid family

2026-10-17 UTC. **Candidate proof - unverified.** Root constructor;
TWO OTHER fresh initially blind NONCONSTRUCTOR WHOLE audits are required.
Requested inherited gpt-6.1-sol/max; independently verified effective
settings unavailable. This concerns only2019 B4(b). No annual answer,
exact lambda, actual renewal regime or novelty is claimed.

This is a new deduction from the ALREADY accepted canonical renewal,
rigid two-history family, capped languages and first-moment theorem.
It neither rediscovers the rigid family nor constructs a larger cap.
The new ingredients are its exact asymmetric width and a lower bound
on the entropy error from an actual omitted positive tail. One bounded
exact rational certificate checks a proposed numerical upper endpoint.

## 0. Accepted inputs and the cap-seven bound actually used

Use K,F,c_n,lambda and R=1/lambda from the accepted second-pass
canonical marked-context dictionary and renewal result. The original
DISTINCT output strings have the SAME root rate lambda; their finite
counts are not identified with c_n. Accepted inputs give

    C(z)=1/(1-2z+F(z)), F(R)=2R-1, F'(R)<=2,
    1.765224 < lambda < 1.834856083 < 2.                 (I)

The derivative at R is the convergent nonnegative first-moment series.
The actual minimal obstruction set F is factor-free and has no proper
suffix-prefix overlap. For every integer D>=1,

    F_D={f in F: a strictly upper equal-context witness
                   has maximal separation at most D},
    K_D=Avoid(F_D), rho_D=lim_n |K_D intersect {L,R}^n|^(1/n).

Every F_D is an ACTUAL subset of F. The accepted renewal identity and
first-moment theorem apply to arbitrary subsets G of F, even infinite
ones. Also F_D agrees with F through length2D+1, and rho_D decreases
to lambda. No numerical cap reconstruction is performed here.

We need the stronger meaning of the old cap-seven certificate, rather
than merely the displayed old bound for lambda. Its accepted whole
proof, section6, gives an entrywise positive integer vector v on the
ENTIRE cap-seven accepting adjacency matrix A, with

    U=1834856083/1000000000,
    (Av)_i < U v_i for EVERY accepting state i.         (II)

The weighted-sup-norm argument in that proof therefore bounds the
growth of ALL K_7 paths: rho_7<U. It does not only bound the sublanguage
K. The old acceptance says both independent auditors checked every
one of the11662 rows. Here(II) is an accepted exact certificate input,
NOT a rerun, a floating eigenvalue, or a presumed fresh all-row audit.
Its archived source/output/proof identities are bound in the new
input record. Strict positivity of v makes the norm valid without
irreducibility. This explains the exact old premise needed below.

The accepted rigid family, for EVERY p,q>=1, is

    H(p,q)=RRL R^(2p) LR L^(2q) RLL,
    J(p,q)=LLR L^(2q) RL R^(2p) LRR.                     (III)

Its context has EXACTLY these two histories; H(p,q) belongs to F.
Distinct parameters give distinct words, of length2p+2q+8. This
special family's two-history theorem is not asserted for all of F.
The older SS1 checked the diagonal width only. The asymmetric check
below strengthens its odd-D agreement bound and quantifies a cap gap.

## 1. CG1: exact minimum width of every rigid word

The MINIMUM possible strictly upper witness width of H(p,q) is

    w(p,q)=2p+1                       if p=q,
           2 min(p,q)+2               if p!=q.          (1)

Write d(t)=L_J(t)-L_H(t), where L counts left moves among the first
t moves. At t=1,2,3 the values are1,2,1. After those first three
moves put u=t-3, and isolate the central blocks

    H: R^(2p) L R L^(2q),
    J: L^(2q) R L R^(2p),

of common length2p+2q+2. For every integer0<=u<=2p+2q+2, exactly

    d(3+u)=1+min(u,2q)+1_[u>=2q+2]-1_[u>=2p+1]
                          -min(2q,max(0,u-2p-2)).     (2)

These are just the exact numbers of consumed L's, including the
two isolated central moves. No asymptotic or feasible-path guess is
used. At the end of the central block d=1. The last three moves
then give2,1,0.

If p=q=d0, the central values increase from1 to2d0+1 as u runs to
2d0, equal2d0 at u=2d0+1, equal2d0+1 at u=2d0+2, and then decrease
one per move to1. If p>q, they increase to2q+1 at u=2q, keep that
value at2q+1, then equal2q+2 for2q+2<=u<=2p. At u=2p+1 and2p+2
they equal2q+1, and then decrease to1. If p<q, they increase to
2p+1 at u=2p, keep that value at2p+1, equal2p+2 for
2p+2<=u<=2q, equal2p+1 at2q+1 and2q+2, then decrease to1.
Every stated plateau is nonempty in its stated case, including
|p-q|=1. All INTERNAL d(t) are strictly positive.

Thus J is a strictly upper legal equal-context witness, with the
maximum in(1); the beginning/end values2 do not enlarge it because
p,q>=1. By the accepted EXACT two-history theorem, J is the ONLY
other complete history for this context. Every upper witness would
have to be that history. Hence the maximum is the MINIMUM possible
width, proving(1) with its lower as well as upper direction.

In particular H(p,q) is omitted by F_D exactly when w(p,q)>D.
Let tau_D be the first length with strictly more K_D words than K
words. The accepted SS1 minimal-factor/count argument identifies
tau_D with the least omitted obstruction length. Therefore

    2D+2<=tau_D<=2D+8               for EVERY D>=2,
    2D+2<=tau_D<=12                 when D=1.          (3)

For D=2h>=2 choose p=q=h. For D=2h+1>=3 choose p=h,q=h+1 (or the
reverse). Both choices have widthD+1 and length2D+8. At D=1 use
H(1,1), width3 and length12. This strengthens the old odd-D upper
bound by2; no exact equality for tau_D is inferred.

## 2. CG2: an exact known omitted-tail series

Let S_D(z) count EXACTLY the words of the already known rigid family
that are absent from F_D, each once. The family and all cap words
remain actual word sets. Formula(1) gives

    S_1(z)=z^12/(1-z^2)^2;
    S_D(z)=z^(2D+8)/(1-z^2)^2,          D even, D>=2;
    S_D(z)=z^(2D+8)(2-z^2)/(1-z^2)^2,   D odd, D>=3. (4)

For evenD=2h, omission is exactly p,q>=h. For oddD=2h+1 withh>=1,
it is p,q>=h EXCEPT(p,q)=(h,h). Indeed off-diagonal width exceeds
D iff min(p,q)>=h, while diagonal omission requires p=q>=h+1.
Summing z^(2p+2q+8) first gives

    z^(4h+8)[(1-z^2)^(-2)-1]

in the odd case; this is the third expression in(4). This derivation
proves all coefficients nonnegative despite its numerator2-z^2.
For D=1 all p,q>=1 are omitted. The formulas converge with first
derivatives at every real0<=z<1. In particular they converge at R<1.

S_D is only a SUBSET of F-F_D; it is not claimed to enumerate every
omitted obstruction. The old F_3 family has no further role here,
and there is no unjustified sum across two overlapping word families.

## 3. CG3: a universal lower error inequality for actual subsets

Let G be ANY proper subset of F, R_G=1/rho_G for Avoid(G), and
H(z)=F(z)-G(z). Suppose a known nonzero nonnegative series S counts
an actual subset of F-G, and all its support degrees are at least3.
Then

    rho_G-lambda >= (lambda*rho_G/2) H(R)
                 >= (lambda^2/2) S(R)>0.             (5)

Here G can be empty or infinite and need not be regular. Its counts
a_n satisfy1<=a_n<=2^n and are submultiplicative because Avoid(G)
is factorial. Thus rho_G=inf a_n^(1/n), a_n>=rho_G^n, and its
generating series diverges at R_G. Inherits-no-overlap gives the
FORMAL reciprocal identity A_G=1/(1-2z+G(z)). Since G<=F and F(R)
is finite, passage to the real endpoint gives

    D_G(R_G)=0, D_G(R)=-H(R), D_G=1-2z+G(z).         (6)

This is the endpoint argument of the accepted M1 proof, not analytic
continuation across an unknown singularity. In particular R_G<=R.
Because the nonnegative first moment F'(R) is finite, the series G'
converges uniformly on[0,R] by comparison with its value at R. Hence
D_G is continuously differentiable there, with one-sided endpoint
derivatives, and0<=G'(t)<=F'(R)<=2. Consequently

    H(R)=integral_[R_G,R] (2-G'(t))dt
         <=2(R-R_G).                               (7)

It follows that R-R_G>=H(R)/2. Multiplying by1/(RR_G)=lambda*rho_G
gives(5). Properness plus an actual missing word makes H(R)>0, so
the same argument also proves strict growth without a separate
automaton irreducibility argument. There is no division by the
possibly zero renewal defect2-F'(R).

Applying(5) to G=F_D and S=S_D gives an explicit POSITIVE lower bound
on EVERY finite cap error, in addition to the accepted upper bound
1/(D+1). A simple closed rational version uses lambda<2 and all
support degrees>=12: the series

    (lambda^2/2)S_D(1/lambda)
          =(1/2)sum_j s_(D,j) lambda^(2-j)

is STRICTLY decreasing in lambda>1 wherever finite. Therefore

    rho_D-lambda > 1/1152,                 D=1;
    rho_D-lambda > 1/(9*2^(2D+3)),          D even>=2;
    rho_D-lambda > 7/(9*2^(2D+5)),          D odd>=3. (8)

Indeed these are exactly2 S_D(1/2), using1-(1/2)^2=3/4. The strict
sign comes from lambda<2 and at least one positive coefficient,
not from assuming a strict derivative inequality. These exponential
lower bounds do NOT assert errors of order1/D or a matching rate.

## 4. CG4: a modest numerical upper improvement, without a new cap

Use the ACCEPTED rho_7<U from(II), and the odd case of(4):

    S_7(z)=z^22(2-z^2)/(1-z^2)^2.

Since lambda<U, the same positive-coefficient monotonicity gives

    rho_7-lambda > (U^2/2) S_7(1/U)
                  =(2U^2-1)/(2 U^18 (U^2-1)^2)=:b>0.

Hence, using the cap bound on rho_7 rather than only on lambda,

    lambda < U-b.                                  (9)

The companion exact rational certificate verifies, at the ONE fixed
published-certificate valueU and ONE fixed proposed endpoint,

    U-b < 1834847/1000000 = 1.834847.                (10)

Together with the unchanged accepted lower bound this proposes

    1.765224 < lambda < 1.834847.                    (11)

The certificate uses integer/Fraction arithmetic, no sampled word,
new factor coefficient, numerical root, transfer matrix construction,
floating eigenvalue or cap-state scan. Its complete exact fractions,
source, stdout/stderr and externally timed child's lifecycle accompany
the frozen submission. Neither the old all-row certificate nor any old
mathematical program is replayed.

## 5. Scope and failures

The older linear agreement theorem explicitly supplied no lower entropy
gap. This packet adds such a bound through a DIFFERENT inequality:
the same accepted endpoint integral is bounded ABOVE by2 times its
interval length. This is compatible with, but weaker in asymptotic
order than, the accepted O(1/D) upper error. It rules out arbitrarily
faster-than-exponential convergence of these particular cap rates.
It does not identify their true asymptotic error or the value of lambda.

An initial alternate route considered a reset-word/Perron-measure loss
estimate. It would require additional follower-automaton details and
give weaker constants. It is unused: positivity and the actual omitted
series suffice. The first diagonal-only argument would have retained
the old odd-D length2D+10; checking the entire rigid family exposes the
shorter asymmetric width and the full omitted-tail mass. No claim that
one missing word alone gives a polynomial cap error is made.

All new proofs await TWO OTHER whole audits. The canonical/original
rate dictionary, rigid family and classical nonoverlap-renewal method
are attributed to their accepted source packets. No uninspected
external theorem is imported. No source-author attribution, complete
grammar, original-output adjacent ratio, actual delta/mu, bounded
joining theorem, annual answer, best-possible bound or novelty claim
is made. Internal independent review will not be external validation.
All older mathematical bytes remain unchanged.
