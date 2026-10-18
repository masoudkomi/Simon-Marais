# A positive degree-four moment and an improved actual cutpath bound

2026-10-18 UTC. **Candidate proof - unverified.**
Root alone constructs NEW PM9A–PM9C; root is EXCLUDED from both required
OTHER initially blind ENTIRE WHOLE audits. No worker supplied the new
moment/interpolation/comparison inference. Complete constructor packet,
FULL final model readback and SEPARATE verification remain required
before review handoff. No claim of annual solution, priority or external
validation. Requested inherited gpt-6.1-sol/max; effective readback unknown.

## Significance, accepted interface and proposed improvement

The exact official2017 question asks for the lower/upper quadratic
logarithmic growth rates of unit-rhombus tilings of the fixed regular
2n-gon. The accepted marked-arrangement dictionary turns an upper estimate
into an actual cutpath count. The newly accepted PM8 geometry supplies a
uniform conditional escape at every degree-four cell. Its split into
few degree-four visits, many visits/low penalties, and high penalties
gave a strict base J<K. Here a finite weighted moment and Hölder
interpolation use that SAME actual local geometry without that three-way
split. The resulting base H is proved STRICTLY smaller than PM8's J,
with no numerical parameter search. Classical finite flow and Hölder are
methods, not claims of new general probability theory.

The operative accepted PM8A–PM8E copy is
`proofs/reviewed-reasoning-path-mass-return-r8-v1.1.md`,29343B,SHA
4e538d9369ae4a2ae9c7c47fa400e947740de08d7ce84a8579f837fd9f9b18d3.
Its current acceptance MDJSON, ENTIRE11 author packet and BOTH entire
OTHER review packets were fully read/reconciled before its promotion.
Root did not construct PM8; root did construct the older WC/WO inputs.
That old role is disclosed and is not independent self-recertification.
The new proposal uses PM8's precise accepted hypotheses and conclusions.

Fix an actual simple MARKED arrangement of n>=2 pseudolines. Every
complete cutpath has n edges, the same path set indexes both directions,
and there are no nonterminal dead ends. Retain the accepted constants

    ell>2, ell^4-2ell^3-1=0,
    M=2ell/(ell²-1), V=ell/M, K=ell M^(3/4),
    rho=max(sigma0,sigma3) in(0,1),
    L0=19/9, M0=171/140, K0=L0 M0^(3/4),
    chi=61880/61731>1, 1<K0<K,
    kappa=1/[4(V+1)²] in(0,1/16).

For the normalized WO forward and reverse path weights P(p),Q(p),
write b(p) for BOTH-direction positive nonunique degree2/>=5 penalties,
c_F(p),c_R(p) for forward/reverse degree4 tail counts, and c=c_F+c_R.
These statistics are exactly PM8's, with orientation-specific terminal
zero degrees excluded. The accepted operative facts are

    sqrt(P(p)Q(p)) >= K^(-n) rho^(-b(p)/2),       (I1)
    sum_p chi^(-c(p)/2) <= K0^n.                 (I2)

PM8 also supplies an adapted greedy block decomposition in either
orientation: two edges at current degree4, otherwise one ordinary edge.
If t is the number of trials and S the number of successful trials,

    c_F<=2t, S<=b                              (I3)

in forward orientation, with c_R in reverse. Its target sets are
disjoint; success means at least one of the next two vertices is bad.
Conditional success probability after ANY prefix at a trial start is
at least kappa. Complete ordinary/two-edge conditional row masses are1.
These are accepted ACTUAL arrangement facts, not independent trials,
uniform-path sampling or abstract DAG assumptions.

Define NEW fixed constants

    r=sqrt(rho) in(0,1),
    a_star=1-kappa(1-r) in(0,1),
    q=-ln(a_star)>0, z=a_star^(-1/2)>1,
    B=ln chi>0,
    theta=B/(B+ln z)=2B/(2B+q) in(0,1),
    H=K^theta K0^(1-theta).

Proposed **PM9A**, a positive absolute moment valid for EVERY actual
arrangement at EVERY n>=2:

    sum_p z^(c(p)/2) <= K^n.                    (1)

Proposed **PM9B**, a uniform improved complete count:

    #completecutpaths <= H^n, 1<K0<H<K.          (2)

Proposed **PM9C**, quantitative strict comparison to the CURRENT accepted
PM8 base J and transfer to the EXACT official count:

    H<J2<=J<K,
    log2 C(N)<=[N(N-1)/2-1]log2 H  (N>=2),      (3)
    limsup log2 C(N)/N² <=(1/2)log2 H
                         <(1/2)log2 J.          (4)

No existence/value of an attaining arrangement, exact entropy, effective
all-scale upper R, new decimal or matching lower bound is asserted.

## 1. A finite block moment with a variable success discount

Use PM8's adapted forward block tree, retaining every distinct prefix
even when graph paths reconverge. At a trial let Y in{0,1} indicate its
success. The complete conditional row satisfies

    E[r^Y | prefix]
      =1-(1-r)Pr(Y=1 | prefix)
      <=1-kappa(1-r)=a_star.                    (5)

Give an ordinary block its P conditional transition weight. Give each
two-edge trial its P conditional weight times r^Y/a_star. Every block
row is substochastic, by(5); the tree is finite and all paths complete.
Induction from the leaves or finite prefix flow proves

    sum_p P(p) r^(S(p)) a_star^(-t(p)) <=1.      (6)

No optional stopping or independence theorem is used. The block choice
depends only on the current degree and the past; it never conditions on
the eventual b or c statistic. Deterministic scanning is a unique
decomposition of each actual complete path, so leaves are exactly paths.

Now z>1 and c_F<=2t give z^c_F<=z^(2t)=a_star^(-t). Also 0<r<1 and
S<=b give r^b<=r^S. Multiplying these POSITIVE pointwise inequalities
in their correct directions and summing(6) yields

    sum_p P(p) z^(c_F(p)) r^(b(p)) <=1.          (7)

The identical reversed argument, using the same complete paths and the
same BOTH-direction b, gives

    sum_p Q(p) z^(c_R(p)) r^(b(p)) <=1.          (8)

The penalty factor r^b is a weight on the full path. It was not inserted
as a future-conditioned transition rule: the comparison to the adapted
tree moment is pointwise after that moment has been proved.

## 2. Cancellation of the penalty in SAME-path Cauchy

Apply finite Cauchy–Schwarz to(7),(8):

    sum_p sqrt(P(p)Q(p)) z^(c(p)/2) r^(b(p))
       <=sqrt[(sum P z^c_F r^b)(sum Q z^c_R r^b)]
       <=1.                                    (9)

The BOTH-direction b is the SAME number in both factors. By(I1) and
r=sqrt(rho), EVERY summand on the left is at least

    K^(-n) rho^(-b/2) z^(c/2) r^b
       =K^(-n) z^(c/2).                         (10)

Thus(9) proves(1). This is an ABSOLUTE sum over actual paths relative
to the certificate K^n. It is neither a moment under uniform paths nor
a claim that the total path count is close to K^n. The exact choice of
r cancels the penalty; it does not delete a previously unproved cost.

## 3. Hölder interpolation with the complementary paid tilt

For each path put X_p=z^(c(p)/2)>0 and Y_p=chi^(-c(p)/2)>0. The fixed
theta is chosen so theta ln z=(1-theta)ln chi. Hence

    X_p^theta Y_p^(1-theta)=1.                  (11)

Finite Hölder with exponents1/theta and1/(1-theta), both>1, gives

    #paths=sum_p X_p^theta Y_p^(1-theta)
       <=(sum X_p)^theta (sum Y_p)^(1-theta)
       <=(K^n)^theta (K0^n)^(1-theta)=H^n.       (12)

For completeness this finite Hölder inequality follows from scalar Young.
Normalize X_p and Y_p by their positive sums. For any u>0,
theta*u+(1-theta)-u^theta>=0: its derivative is
theta*(1-u^(theta-1)),negative below1 and positive above1,with value0
at1. Substitute the ratio of the two normalized terms and sum to get
sum normalized_X^theta normalized_Y^(1-theta)<=1. Undo normalization.
The actual path set is nonempty;an empty set would make(12)trivial.
Thus no unread infinite-measure interpolation theorem is imported.

This uses the positive moment(1) and the separately accepted PAID raw
tilt(I2). It does not assume feasibility of the original unnormalized
degree4 row; the chi factor remains exactly where PM8C placed it.
Constants are chosen before the arrangement/size. Since0<theta<1 and
1<K0<K, strict weighted-geometric-mean inequalities give1<K0<H<K.
This proves(2) for EVERY n>=2, with no multiplicative prefactor4.

## 4. Strict improvement over the CURRENT PM8 base, by hand

The simpler conclusion H<K would not alone improve the now accepted
J<K. The following direct comparison establishes the stronger H<J2.
Introduce POSITIVE quantities

    A=ln(K/K0), B=ln chi, t=-ln(1-kappa/2),
    h=-ln r, delta=min(1,A/B).

The accepted PM8 eta=delta*t/(8 ln2) and J2=K rho^(eta/2) satisfy

    ln(K/J2)=delta*t*h/(8 ln2).                 (13)

Our definition gives

    ln(K/H)=A*q/(2B+q).                         (14)

First bound q<B with exact rational comparisons. Accepted PM8 proves
ell<19/9, so rho>=sigma0=2/ell>18/19. Consequently

    r>sqrt(18/19)>35/36,

where18*1296-19*1225=53>0 verifies the second strict inequality. Also
kappa<1/16 becauseV>1. Thus x=kappa(1-r)<1/576. The integral
inequality -ln(1-x)<=x/(1-x) for0<x<1 gives

    q<1/575.

On the other hand, ln(1+y)>y/(1+y) fory>0, here y=149/61731, gives

    B>149/61880>1/575,

the last gap having cross numerator149*575-61880=23795>0. Therefore
q<B, with no root/logarithm approximation.

Next -ln r<=(1-r)/r and r>1/2 imply1-r>h/2. Since -ln(1-x)>=x,

    q>=kappa(1-r)>kappa*h/2.

The same upper integral bound gives

    t<=kappa/(2-kappa)<16kappa/31,

becausekappa<1/16. Hence

    q>31*t*h/32.                               (15)

By the definition ofdelta, A>=delta B. Usingq<B in(14) and then(15),

    ln(K/H)>delta*q/3>31delta*t*h/96.

Finally ln2>1/2, by integrating1/x>1/2 on1<=x<2, so

    delta*t*h/(8 ln2)<delta*t*h/4
       =24delta*t*h/96<31delta*t*h/96.

Comparison with(13) proves ln(K/H)>ln(K/J2), so H<J2<=J. All logs,
denominators and exponents are positive as specified; the proof covers
bothdelta=1 anddelta=A/B without a hidden branch assumption.

## 5. Exact official insertion and remaining limits

The separately accepted marked dictionary/insertion is
B_(n+1)<=gamma_n B_n,B2=1,C(n)=B_n. Withgamma_n<=H^n from(12),
sumj=2,...,N-1 to obtain(3), including the emptyN2 product. There is
no per-insertion factor4 and no new label/symmetry/history quotient.
Dividing byN² gives(4), with strict comparison already proved before
the limit. This bound does not establish an effective error for the
different growing-window entropy interface R or determine the exact
official limit inferior/superior. No annual completion or priority.

## 6. Attribution and operational record

PM8's accepted actual geometry, disjoint-trial structure and PAID tilt
are attributed inputs. Older normalized WO weights and marked/zone/
dictionary inputs retain their exact accepted source scopes; root's old
WC/WO role is not an independent review of those inputs. The new finite
discount, exact cancellation, positive moment, Hölder interpolation and
strict H<J2 comparison are root's hand construction. Full proposed
constructor obligations/checks/issues/failures/source/log/code/ALLmetadata
and TWO OTHER initially blind ENTIRE WHOLE audits remain to be completed.

No mathematical executable,CAS,scan,numerical optimizer,routine test,
source/author or old certificate replay supplied any assertion here.
No binary third-party paper or unavailable retrieval hash is invented.
Classical inequalities are derived above; no unread probability theorem
is imported. A fixed exact symbolic improvement is not evidence of
published priority, external validation or an exact entropy formula.

## 7. Additional primary lead checked during final construction

Freshly opened Krit Boonsiriseth,The maximum number of k-gons in the zone
of a pseudoline,MIT UROP+2020,mentor Pakawut Jiradilok,project suggested
by Alexander Postnikov:
https://math.mit.edu/research/undergraduate/urop-plus/documents/2020/Boonsiriseth.pdf
Read introduction/preliminaries,COMPLETE operative Lemma3.5 and
Theorem3.1 proofs,and Theorem4.1 statement with its early setup through
extracted346. Its full zone theorem proof,Sections5–8 and all54pages
were NOT audited. The manuscript concerns face-degree zone/half-zone
inequalities. It is useful context,NOT a premise of PM9;no theorem from
it is applied. Literal searches for weight/cutpath had no matches,which
does not certify nonoverlap or priority. Earlier PM8's unread-lead record
remains truthful for that earlier checkpoint;this new read is later.
