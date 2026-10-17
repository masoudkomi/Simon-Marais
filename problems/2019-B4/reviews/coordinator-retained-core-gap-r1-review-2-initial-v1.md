# Retained-core gap: independent whole initial R2

2026-10-17 UTC. Reviewer C, `/root/review_2017_coarsening_r1`.
This is a COMPLETE initially blind WHOLE review of root's new submission,
not a constructor self-check or an acceptance register. The main is
6152 bytes, SHA256
`9bea48691719c0384e0a027131e6db1fad83ddd0572e8ae59578f72d71431b42`;
its frozen five-artifact packet and all sixteen obligations were read.
All new A retained-core reports, findings AND metadata remained unread
through this complete initial freeze.

I find no substantive defect or required repair in the exact scoped
retained-word inequality and proposed strict upper bound 1.834843,
relative to the separately accepted premises identified below. Root is
the constructor and is excluded from the two independent reviews. I
reviewed the older CG theorem and supplied the earlier hand power-chain
method; the new main attributes and rederives that method. I did not
construct the NEW retained-core inference. This review is not a fresh
independent recertification of my old contribution or of the old finite
matrix certificate.

## 1. Official target and exact imported domain

I read the official 2019 Paper B's B4 statement, including the part (b)
target, through the official PDF and read the local normalization.
The original objects are DISTINCT binary strings generated from the
specified seed and end-insertion rule. The open part asks for their
lower and upper root growth. The accepted canonical marked-context
dictionary transfers only the common exponential rate lambda. It does
not identify the two finite counting sequences. No preliminary proof is
reproduced here.

The operative accepted inputs are the complete cap-gap CG1--CG4 body
and acceptance, the complete third-pass body and the complete M1--M3
moment-tail body. They supply:

* The actual minimal obstruction word set F, its nonoverlap properties,
  canonical growth lambda, R=1/lambda, F(R)=2R-1, and the finite
  nonnegative endpoint first moment F'(R)<=2.
* For an ACTUAL subset G of F, Avoid(G), its positive factorial word
  counts and root growth rho, r=1/rho, and the formal renewal identity
  A_G=1/(1-2z+G(z)).
* The nested ACTUAL cap sets F_D, F_3 containing RRLL, and hence
  RRLL in F_7. Their cap rates decrease to lambda.
* The independently accepted positive-vector inequalities on ALL
  accepting cap-seven states, implying rho_7<U at the fixed rational
  U=1834856083/10^9. This is stronger than merely lambda<U.
* The known omitted rigid WORD subset at cap seven, with its exact
  series S_7(z)=z^22(2-z^2)/(1-z^2)^2. It is a subset of F-F_7,
  not the entire missing set. Its exact word/width proof is an accepted
  CG input and is not re-enumerated here.

The finite certificate's all-row signs remain an accepted premise
supported by the old audits. I neither replayed them nor claimed to
have freshly checked all 11662 rows. The new proof needs no outside
enumerative theorem or source-author conjecture.

## 2. Reconstruction of the endpoint identity

It matters that G is an actual forbidden WORD subset. Its inherited
nonoverlap gives the formal renewal identity coefficient by coefficient;
this cannot be replaced by an arbitrary signed or rational series.
The counts a_n of Avoid(G) are positive and submultiplicative, so
rho=inf a_n^(1/n), a_n>=rho^n and A_G diverges at r=1/rho.
Since K is contained in Avoid(G), rho>=lambda and r<=R.

For 0<=z<r, all relevant nonnegative series converge and the reciprocal
identity is an identity of real numbers. Moreover G(R)<=F(R)<infinity.
As z increases to r, divergence of A_G and continuity of G at r give
D_G(r)=0 for D_G(z)=1-2z+G(z). This also works at r=R. The accepted
equation D_F(R)=0 yields D_G(R)=-H(R), with H=F-G.

Because the endpoint first moment is finite, the derivative series of
G is uniformly convergent on [0,R]: every tail is bounded by the
corresponding tail of the convergent series F'(R). Thus D_G is C1 on
that closed interval, with one-sided derivatives at the ends, and

    H(R) = D_G(r)-D_G(R)
         = integral_r^R (2-G'(t)) dt.                (A)

Nonnegative coefficients give 0<=G'(t)<=F'(R)<=2. No analytic
continuation, simple pole, second endpoint moment, or positive value
of 2-F'(R) is needed. If G is proper then an actual missing word has
strictly positive weight at R>0, so H(R)>0. Equation (A) itself then
forces r<R and rho>lambda. The candidate's use of the accepted strict
actual-subset theorem is therefore also internally consistent.

## 3. Reconstruction of the NEW retained-core estimate

Assume that RRLL belongs to G, rho<=U and U>3/2. The retained word's
generating monomial is t^4, hence its derivative contribution is 4t^3.
For the ENTIRE integration interval,

    t>=r=1/rho>=1/U,
    G'(t)>=4t^3>=4/U^3.

This is precisely why a cap bound on rho is needed: a bound only on
lambda gives no lower bound on r. Put A(U)=2-4/U^3. The direction of
the reciprocal comparison is correct, and

    A(U)>2-32/27=22/27>0.

Together with (A) this proves

    H(R)<=A(U)(R-r),
    rho-lambda=(R-r)/(Rr)
              >=lambda*rho*H(R)/A(U)
              >=lambda^2*S(R)/A(U),                 (B)

for a known nonzero actual omitted subseries S<=H. The second
inequality uses rho>=lambda and H(R)>=S(R)>0, all factors positive.
It does not cancel the possibly zero endpoint renewal defect.

For the strict fixed-U substitution, write

    x^2 S(1/x)=sum_j s_j x^(2-j).

If every supported j exceeds 2, this expression is strictly decreasing
on its convergence range for x>0. Termwise comparison of nonnegative
series suffices; no derivative of S beyond its radius is taken.
Properness gives lambda<rho<=U, so lambda<U. Comparison is legitimate
at both endpoints because S(R)<=F(R)<infinity and 1/U<R. Consequently

    rho-lambda>U^2*S(1/U)/A(U).                      (C)

This proves the submitted strict estimate even when rho=U. The general
theorem excludes empty G because it explicitly retains RRLL. Infinite
and nonregular G cause no new problem. It asserts no strict gap between
two arbitrary consecutive cap languages.

## 4. Actual cap-seven specialization and positive omitted mass

The accepted F_3 word language includes RRLL, and F_3 is contained in
F_7, so the derivative hypothesis is satisfied. The old all-state
positive vector v gives beta=max_i(Av)_i/v_i<U over finitely many
states. In the norm ||x||_v=max_i |x_i|/v_i, nonnegativity gives
||A||_v=beta. Thus all accepted path counts are O(beta^n), and their
root growth rho_7 is <=beta<U. No irreducibility or Perron eigenvector
assumption is used.

The accepted omitted subset is nonempty and positive. Independently,
its displayed compact form expands as

    S_7(z)=sum_(k>=0) (k+2) z^(22+2k).

Thus the subtraction in 2-z^2 does not supply a negative word count;
the first coefficient is exactly 2 and all supported lengths exceed 2.
R<1 from the accepted growth enclosure, so the displayed series and
its needed values converge. Its exact identification with actual
omitted words, rather than mere coefficient positivity, remains the
separate accepted CG word/width premise.

Direct symbolic substitution, with no mathematical executable, gives

    U^2 S_7(1/U)
       =(2U^2-1)/(U^18 (U^2-1)^2)=2b,
    b=(2U^2-1)/(2U^18(U^2-1)^2)>0.

Using (C) and rho_7<U gives lambda<U-2b/A(U). The exponent 18 and
factor 2 are correct; treating b itself as the new omitted mass would
lose the stated improvement.

## 5. Independent HAND check of the rational endpoint

All decimals here mean exact rationals, and this entire calculation
was done symbolically by hand. No sign script, author child, numerical
root or old certificate was run.

First U<37/20, so

    U^3<50653/8000<51200/8000=32/5,
    4/U^3>5/8, 0<A(U)<11/8.                         (D)

Also 11/6<U<1.835. The numerator therefore satisfies

    2U^2-1>103/18>57/10.

For the denominator, U^2<1.835^2=3.367225<3.368. Squaring and
multiplying positive upper bounds yields the following exact chain:

    U^4<3.368^2=11.343424<11.344,
    U^8<11.344^2=128.686336<128.69,
    U^16<128.69^2=16561.1161<16562,
    U^18<16562*3.368=55780.816<55781,
    (U^2-1)^2<2.368^2=5.607424<5.608.

Hence

    2U^18(U^2-1)^2<2*55781*5.608
                    =625639.696<626000,
    b>(57/10)/626000=57/6260000.                     (E)

Equations (D)--(E) give

    2b/A(U)>16b/11>912/68860000.

The proposed endpoint V=1834843/10^6 satisfies U-V=13083/10^9.
The final exact cross multiplication is

    13083*68860000=900895380000,
    912*10^9-13083*68860000=11104620000>0.

Thus 912/68860000>U-V and

    lambda<U-2b/A(U)<U-912/68860000<V=1.834843.

Every denominator and factor compared is positive; each strict sign
is supplied by a displayed exact rational comparison. The proof has
ample slack and does not rely on decimal rounding.

## 6. Adversarial checks and exact limits of this verdict

I checked the dangerous substitutions explicitly: an upper bound on
lambda cannot replace rho<=U; empty G fails the retained-word
hypothesis; an arbitrary formal subseries cannot replace an actual
forbidden set; endpoint defect zero cannot be divided out; positive
coefficient monotonicity uses supported degrees >2; and S_7 is only
the known omitted subset. The zero-defect case, infinite subsets and
possible reducible cap automaton do not break the proof as stated.

The inherited lower bound 1.765224 remains a separately accepted
input. The new work would therefore refine that accepted interval to
1.765224<lambda<1.834843 after both fresh whole audits and root
reconciliation. It does not determine lambda, the full obstruction
language, its renewal regime, matching cap-error order, adjacent
original-output ratios, or the annual answer. No priority or novelty
claim follows. Only the coordinator can promote the submission.

The companion ledger covers all RC-01--RC-16 individually. All five
constructor artifacts, the complete operative accepted bodies and
necessary authorities were read. Administrative fingerprints validate
53 declared occurrences across 37 deduplicated paths and bind the
earlier own inventory compactly through its immutable parent. They
are preservation checks, not mathematical computations or old replays.
