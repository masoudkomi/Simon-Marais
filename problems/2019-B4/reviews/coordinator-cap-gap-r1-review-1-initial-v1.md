# Independent WHOLE initial audit R1: cap-gap CG1--CG4

2026-10-17 UTC. Reviewer C, `/root/review_2017_coarsening_r1`.
**Initially blind WHOLE nonconstructor review.** The entire constructor
main, all 24 obligations and all 12 frozen artifacts were read before
this report was completed. No new cap-gap R2 report or peer finding was
opened or received. This report and its entire ledger/source/integrity
packet freeze before any comparison.

Target main: 11796 bytes, SHA256
`0e8afb24ec9e58004ee9464de327b309d834058b277eae4a2608d0d7afde5f33`.
Target freeze: 3669 bytes, SHA256
`9b3751764cb2ba0177f3b8ff9e5f90721acf134f3e92c42cf4be67e5179d3d49`.
Both match the assignment. I did not construct CG1--CG4. I previously
whole-audited the accepted SS1--SS3 input and performed separate older
original-output/linear-language research. Those roles do not make this
an independent recertification of their old proofs; the NEW asymmetric
width, omitted-tail and integral-lower-gap deductions are reconstructed
below. The coordinator constructed this submission and cannot count as
one of its two independent reviewers.

## Verdict and exact dependency boundary

I find **no substantive defect** in the stated CG1--CG4 scope, relative
to the exact accepted canonical-context/renewal/rigid-family inputs and
the accepted all-state cap-seven certificate. The new upper endpoint
has an independent short hand proof below; no author script, large
fraction, matrix, cap scan or old computation was rerun.

In particular the old positive-vector proof really bounds rho_7<U,
not merely lambda<U. This stronger consequence is essential. It follows
from its all-accepting-state norm argument, which I freshly read in the
complete accepted third-pass body. I rely on its accepted all-row data
and two older independent checks; I do NOT claim a new 11662-row audit.

The proposed conclusions remain partial. They do not evaluate lambda,
identify the actual renewal regime, prove a matching cap-error rate,
determine original-output adjacent ratios, or solve the annual open
target. A second OTHER initially blind whole audit and coordinator
reconciliation are still required before promotion.

## 1. Official count and accepted source roles

The official open 2019 B4(b) counts DISTINCT generated binary strings.
It does not count insertion histories. The canonical language K here
counts marked chronological contexts; the accepted dictionary transfers
only their common root growth lambda to the official counts. None of
the finite counts a_(D,n), c_n or the obstruction coefficients are
identified with the original b_n.

I read the full local statement, accepted second-pass register and its
actual canonical-renewal and rigidity notes, the COMPLETE accepted
third-pass exposition and acceptance, the COMPLETE moment-tail proof,
and the COMPLETE accepted SS body and acceptance. The historical
candidate labels inside those frozen bodies are qualified by their
accepted registers. The NR acceptance was read for the prior qualitative
strictness scope; no NR argument is needed for the new inequality.
The new proof imports no unread external theorem.

Write R=1/lambda. The relevant accepted facts are

    F is factor-free and has no proper suffix-prefix overlaps,
    C=1/(1-2z+F), F(R)=2R-1, sum n f_n R^(n-1)<=2,
    K_D=Avoid(F_D), F_D subset F, agreement through length 2D+1,
    1.765224<lambda<U=1834856083/10^9<2.

The derivative at R is a finite nonnegative series; no analytic
continuation or simple-root premise is part of this input.

The old cap-seven accepted adjacency matrix A has a vector v>0 with
Av<Uv on EVERY accepting state. Since there are finitely many states,

    beta=max_i (Av)_i/v_i < U.

For ||x||_v=max_i |x_i|/v_i, nonnegativity gives ||Ax||_v<=beta||x||_v.
Thus e_start^T A^n 1 is bounded by a fixed positive constant times
beta^n, regardless of irreducibility. Its root growth is rho_7, so
rho_7<=beta<U. This reconstructs the exact old-premise implication
needed by CG4 without changing or rechecking the old vector data.

## 2. Complete width reconstruction (CG1)

For p,q>=1 the accepted rigid context has EXACTLY two histories

    H=RRL R^(2p) L R L^(2q) RLL,
    J=LLR L^(2q) R L R^(2p) LRR.

The accepted forced-choice proof, including p=1 or q=1, was read.
Let d(t) be the left-count of J minus that of H at common source time.
The first three values are 1,2,1. At t=3+u, across the central block,

    d=1+min(u,2q)+1_(u>=2q+2)-1_(u>=2p+1)
                   -min(2q,max(0,u-2p-2)).

This counts J's initial 2q left moves and later singleton separately,
and subtracts H's earlier singleton and later 2q left moves. It is
valid at every integer 0<=u<=2p+2q+2, not just the turning points.

If p=q=r, the values rise from 1 to 2r+1 at u=2r, then are 2r and
2r+1 at u=2r+1,2r+2, then decrease to 1. If p>q, they rise to 2q+1,
stay there at u=2q+1, take the value 2q+2 for
2q+2<=u<=2p, equal 2q+1 at u=2p+1,2p+2, and then decrease to 1.
If p<q, the corresponding list has its maximum 2p+2 on
2p+2<=u<=2q, with the neighboring plateau values 2p+1. These maximal
intervals are nonempty even when |p-q|=1. After the central block the
last three values are 2,1,0. All internal values are positive.

Consequently J is a strictly upper witness with width

    w(p,q)=2p+1 if p=q; otherwise 2 min(p,q)+2.

The prefix/suffix extrema 2 do not exceed these central maxima because
p,q>=1. Exact two-history rigidity makes J the ONLY possible different
complete witness. Thus this is the MINIMUM width, not merely a width
of one selected path. No universal two-history claim for F is used.

For an omitted rigid word, membership in F_D is therefore exactly
w<=D. For D=2h>=2, choose p=q=h to obtain width D+1 and length 2D+8.
For D=2h+1>=3, choose p=h,q=h+1 to obtain the same width D+1 and
length 2D+8. For D=1, H(1,1) has width 3 and length 12. The separate
D=1 bound is correctly weaker than what the accepted short obstruction
already gives; no sharp tau_1 claim is made.

The first strict avoidance-count discrepancy equals the least omitted
minimal-factor length m: below m every forbidden factor belongs to F_D;
at length m an omitted f itself avoids F_D by factor-freeness. Thus
tau_D=m. Agreement through 2D+1 supplies the lower bound 2D+2.
This proves the proposed intervals for tau_D, including every endpoint.

## 3. Exact subset series (CG2)

Distinct positive pairs (p,q) give distinct H words. For D=2h>=2,
omission is exactly p,q>=h, yielding

    S_D=z^(4h+8)/(1-z^2)^2=z^(2D+8)/(1-z^2)^2.

For D=2h+1>=3, off-diagonal omission requires min(p,q)>=h, while
diagonal omission requires p=q>=h+1. Hence omit exactly all p,q>=h
except (h,h). Their sum is

    z^(4h+8)[(1-z^2)^(-2)-1]
       =z^(2D+8)(2-z^2)/(1-z^2)^2.

For D=1 all p,q>=1 are omitted and S_1=z^12/(1-z^2)^2. This also
checks that the odd numerator, despite its minus sign, represents a
nonnegative actual word set, and that S_7 starts with TWO words of
length 22. All series and their first derivatives converge at R<1.
They count a SUBSET of the omitted factors, not the entire unknown tail.
No additional union with F_3 is taken, so no word-overlap subtraction
from the older SS proof is being silently reused.

## 4. Arbitrary actual subsets and the cap-gap direction (CG3)

Let G be any proper subset of F and a_n count Avoid(G). It contains
the all-L word, is factorial, and 1<=a_n<=2^n. Submultiplicativity
gives rho_G=inf a_n^(1/n) and a_n>=rho_G^n; its series A_G therefore
diverges at R_G=1/rho_G. Since K is contained in Avoid(G), R_G<=R.

The nonoverlap append/remove-suffix bijection holds for EVERY subset G,
including an infinite nonregular one. Its coefficientwise formal
identity is A_G(1-2z+G)=1. For 0<=z<R_G the two series converge,
because G<=F and z<R_G<=R. Letting z increase to R_G gives

    D_G(R_G)=0,   D_G(R)=-H(R),   H=F-G,

using finite G(R)<=F(R), continuity and divergence of A_G. This argument
does not cross a radius or assume a simple root. It includes R_G=R
before strictness is deduced.

Since sum n g_n R^(n-1)<=2, the derivative series for G converges
uniformly on [0,R] by the Weierstrass comparison with that finite sum.
It supplies continuous one-sided endpoint derivatives and
0<=G'(t)<=2. The exact fundamental theorem identity is consequently

    H(R)=integral_(R_G)^R (2-G'(t)) dt <=2(R-R_G).

This is the upper integral estimate needed for a LOWER gap bound; its
direction is correct. It never divides by 2-F'(R), which can be zero.
Taking reciprocals gives

    rho_G-lambda=(R-R_G)/(R R_G)
       >=(lambda rho_G/2)H(R)
       >=(lambda^2/2)S(R)>0

for any nonzero actual missing subset series S. As a useful boundary
check, for G empty the first inequality is equality, since D_G=1-2z,
R_G=1/2 and H(R)=2R-1. Thus the empty-language cap convention is not
an exception. Properness supplies a missing word and positive mass;
G=F is correctly excluded from the strict statement.

If S has support only in degrees j>=3,

    (lambda^2/2)S(1/lambda)=(1/2)sum_j s_j lambda^(2-j)

strictly decreases as lambda increases, by termwise comparison of the
nonnegative convergent sums and at least one strictly decreasing term.
No differentiation of an unknown tail at another point is required.
For the three rigid series, substitution at lambda=2 gives exactly

    2S_1(1/2)=1/1152,
    2S_D(1/2)=1/[9*2^(2D+3)]       (D even>=2),
    2S_D(1/2)=7/[9*2^(2D+5)]       (D odd>=3).

Because lambda<2, the proposed strict lower floors follow. They are
exponential lower bounds and are compatible with the accepted O(1/D)
upper error. No matching asymptotic is established.

## 5. Independent hand sign for the numerical endpoint (CG4)

From rho_7<U and the positive-coefficient comparison at lambda<U,

    rho_7-lambda > b,
    b=(U^2/2)S_7(1/U)
      =(2U^2-1)/(2U^18(U^2-1)^2).

Thus lambda<U-b. The following independent rational bounds prove the
endpoint without using the constructor's Fraction output or rerunning
its source. All terminating decimals here are exact rational numbers.

First 11/6<U<1.835. Hence

    2U^2-1>103/18>57/10.

For the denominator, repeated strict rational upper bounds give

    U^2 <3.368,
    U^4 <3.368^2=11.343424<11.344,
    U^8 <11.344^2=128.686336<128.69,
    U^16<128.69^2=16561.1161<16562,
    U^18<16562*3.368=55780.816<55781,
    (U^2-1)^2<2.368^2=5.607424<5.608.

Therefore

    2U^18(U^2-1)^2 <2*55781*5.608
                    =625639.696<626000,
    b>57/6260000 >9083/10^9.

The last strict sign is the small integer comparison

    57*10^9 -9083*6260000
       =57000000000-56859580000=140420000>0.

But U-1834847/10^6 is EXACTLY 9083/10^9. Thus

    U-b<1834847/10^6=1.834847.

This proves the proposed strict improvement with independent slack.
I read the constructor's exact source, full saved fractions and child
lifecycle, but the present argument needs none of its large numerators.
The archived child completed and was reaped; I started no mathematical
child. The old lower 1.765224 is unchanged and accepted, giving exactly
the proposed open interval for the common original-output root rate.

## 6. Final audit scope

All 24 obligations are addressed individually in the ledger. The issue
log records no substantive defect and no required repair in this exact
scope. Counterchecks included D=1, D=2, |p-q|=1, the diagonal singleton
steps, empty G, arbitrary infinite G, endpoint derivative zero, the two
first odd-tail words, and the distinction rho_7 versus lambda.

Source roles and original-count limitations are explicit. No external
paper or theorem about arbitrary formal series replaces the actual
obstruction-subset hypotheses. No new universal two-history, regularity,
positive renewal defect, complete grammar, annual evaluation or priority
claim is accepted by implication. Old bytes and the entire constructor
packet remain unchanged. Integrity verification and this independent
internal review are not external mathematical validation.
