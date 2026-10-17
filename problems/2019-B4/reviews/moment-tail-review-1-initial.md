# 2019 B4(b): independent whole initial audit of moment/regular-tail packet, R1

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`.
Requested gpt-6.1-sol / max; independently verified effective settings
unavailable. This document recommends a disposition; only the coordinator
may promote a result after both independent audits.

## Identity, independence, and recommendation

Audited candidate:
`notes/coordinator-moment-regular-tail-candidate-v1.md`, SHA-256
`29b02df71668db17b7111319d40ccdcdf798bed19dad4a8b76c7bcedaa332ef2`.
Audited freeze manifest:
`notes/coordinator-moment-regular-tail-freeze-v1.json`, SHA-256
`320264ddc543a1936329ac8ffe78c7336f6b2064e591ca8f892791d11787171c`.

I did not construct this candidate or contribute its first-moment or
regular-tail argument. I reconstructed all of M1-M3 before seeing any
other new moment-tail review or findings. Accepted older expositions and
their acceptance registers were read as dependencies, not another fresh
review of this construction. I derived and ran an independent integer
sign certificate before opening the constructor's certificate code or
result. No histories, forbidden-factor sets, queue automata or larger
separation caps were enumerated during this audit.

**Recommendation:** M1, M2 and M3 withstand this whole audit in their stated
partial scope. There is no substantive objection or required author repair.
The uniform O(1/D) estimate and the strict rational lower bound follow
from the accepted inputs and the proofs below. Exact evaluation of the
growth constant, a complete obstruction grammar, and regularity or
algebraicity of the full obstruction series remain unresolved.

## 1. Official domain and accepted inputs

I compared the local statement with official Paper B, page 2, B4(b).
The objects counted there are distinct generated binary strings, not
insertion histories; the initial string and alternating end additions
match the normalization. The target is the two exponential liminf/limsup.
No preliminary part (a) proof was reconstructed or used as a new research
target in this review.

The accepted second-pass register covers the unchanged canonical-renewal
text and the complete 143-factor prefix through length 24. It identifies
the exponential growth of the canonical-history language K with that of
the official distinct-string sequence. Thus using lambda from canonical
counts here is an accepted exponential-rate interface, not an equality
between string counts and all insertion-history counts.

The accepted inputs needed by the new argument are precisely:

* K is factorial and consists of histories avoiding its intrinsic minimal
  forbidden set F. The set F is factor-free, with no nonempty proper
  suffix-prefix overlaps, including self-overlaps.
* C(z)=1/(1-2z+F(z)), R=1/lambda, F(R)=2R-1 and the nonnegative first
  moment sum F'(R)<=2 is finite.
* F_D is a subset of the actual F, agrees with F through length 2D+1,
  and Avoid(F_D) has root growth rho_D. No artificial extra forbidden
  words occur in this definition.
* F_3 is the accepted unambiguous regular subset with series
  z^4+z^12/(1-2z^5-z^8). The accepted length-24 coefficients are those
  displayed in the candidate.

I read the complete accepted second-pass renewal text, checkpoint 2,
third-pass exposition and both acceptance registers. The third-pass
language is an actual subset of F by its envelope/minimal-factor result;
it is not merely the minimal-factor set of an unrelated regular
superlanguage. This distinction is essential for the union in M3.
I did not rerun any of the already accepted history or automaton certificates.

## 2. M1: growth and renewal for an arbitrary actual obstruction subset

Fix an integer N>1 and any G subset F containing every F-word of length
less than N. It may be infinite. Let a_n count Avoid(G), with a_0=1.
The language is factorial, so cutting a length-(m+n) word at position m
injects it into the product of the two avoidance languages. Thus
a_(m+n)<=a_m a_n. The language contains K and in particular the all-L
word of each length; the latter is canonical because its right tape is
empty and hence its context admits no history containing R. Consequently
1<=a_n<=2^n.

The elementary submultiplicative lemma gives

    rho_G=lim a_n^(1/n)=inf_(n>=1) a_n^(1/n),
    1<=lambda<=rho_G<=2,       a_n>=rho_G^n.

Therefore A_G(z)=sum a_n z^n has radius R_G=1/rho_G, with
1/2<=R_G<=R, and it diverges at the boundary R_G: each term
a_n R_G^n is at least 1. No simple pole or analytic continuation is
needed for this divergence.

Both nonoverlap conditions are inherited by every subset G. Here is
the renewal bijection in the required generality. Appending L or R to
an avoiding word can first introduce a forbidden factor only as a suffix
ending at the new last letter. That suffix is unique by factor-freeness.
Removing it leaves an avoiding prefix. Conversely concatenate an avoiding
prefix with one g in G. Any other forbidden occurrence cannot lie in the
prefix, be properly inside g, or contain g, by avoidance and factor-
freeness. An occurrence crossing the join and intersecting g would give
a prohibited proper suffix-prefix overlap, unless it is the final g
itself. Thus the prefix of length one less than the concatenation avoids
G, exactly as required to reverse the appending construction.

For each degree there are only finitely many words on the two-letter
alphabet, even when G is infinite. The resulting recurrence and formal
identity are consequently valid coefficient by coefficient:

    a_n=2a_(n-1)-sum_(1<=j<=n) g_j a_(n-j),
    A_G(z)(1-2z+G(z))=1.

The identity alone is not used to guess a singularity. At every real
0<=x<R_G, A_G(x) converges by its radius, while G(x) converges because
G<=F coefficientwise and x<R. There
D_G(x)=1-2x+G(x)=1/A_G(x)>0. The series G is continuous throughout
[0,R], since its nonnegative coefficient sum at R is bounded by finite
F(R). As x increases to R_G, A_G(x) diverges, so

    D_G(R_G)=0.

This reasoning includes the endpoint possibility R_G=R. It requires
neither convergence of A_G at its radius nor a simple denominator zero.

## 3. M1: closed-interval calculus, cancellation, and the zero-gap case

By coefficientwise domination and the accepted first moment,
sum n g_n R^(n-1)<=F'(R)<=2. The derivative series therefore converges
uniformly on [0,R], dominated by that finite numerical sum. In particular
G is continuously differentiable there, with the one-sided endpoint
derivatives supplied by its series; the fundamental theorem of calculus
applies. Also G' is nondecreasing and G'(t)<=G'(R)<=2.

Put H=F-G, supported in degrees at least N, and set
A=2-G'(R)>=0. Nonnegative coefficients give

    H'(R)=F'(R)-G'(R)<=A,
    H(R)<= (R/N)H'(R)<= (R/N)A.

Since D_F(R)=0, one has D_G(R)=-H(R). Combining this with the root
at R_G yields

    H(R)=integral_(R_G)^R (2-G'(t))dt
         >=(R-R_G)(2-G'(R))=(R-R_G)A.

The inequality direction is correct because G'(t)<=G'(R) on this
interval. If A>0, cancellation gives R-R_G<=R/N. If A=0, the
nonnegative moment H'(R) is zero. Since R>0 and H has no constant
term (indeed it is supported at degrees >=N>1), every coefficient of
H is zero. Hence G=F and R_G=R. This branch handles the potentially
dangerous zero derivative gap instead of dividing by it.

In both cases

    R_G/R=lambda/rho_G>=1-1/N,
    (1-1/N)rho_G<=lambda<=rho_G,
    0<=rho_G-lambda<=rho_G/N<=2/N.

The exact subset G=F, infinite subsets, and allowed empty subsets are
all covered by the same proof. There is no strict-convexity premise.
For G=F_D, agreement through length 2D+1 means precisely that missing
factors have length at least 2D+2. Setting N=2D+2 therefore gives

    ((2D+1)/(2D+2))rho_D<=lambda<=rho_D,
    rho_D-lambda<=1/(D+1),              D>=1.

No larger-cap computation or claim about the actual error's asymptotic
size is needed for this uniform upper bound.

## 4. M2: the sign test only needs calculus up to the true boundary

Define E_G=D_G-(x/N)D_G'. The previous inequalities at R give

    E_G(R)=-H(R)+(R/N)A>=0.

On 0<x<R all series are analytic: coefficient domination by F and
convergence at R ensure absolute convergence within that disk. Therefore

    E_G'(x)=(1-1/N)D_G'(x)-(x/N)G''(x)<=0.

Here D_G'=G'-2<=0, G''>=0 and N>1; all three signs are necessary and
are supplied. Uniform convergence of G and G' on [0,R] makes E_G
continuous there, so the open-interval derivative inequality extends
to the monotonicity statement on the whole closed interval. No finite
second moment or value G''(R) is assumed.

It follows that E_G(t)>=E_G(R)>=0 for every 0<=t<=R. Suppose now
that a specified positive rational r is within the convergence range of
the known G and its first derivative, with E_G(r)<0. If r<=R, this
contradicts the preceding conclusion. Thus r>R, and positivity gives
lambda=1/R>1/r.

This is a valid contradiction argument even when the selected r lies
beyond the unknown convergence boundary of F. The derivative inequality
is used only under the temporary assumption r<=R. No monotonicity beyond
R or algebraic continuation of F is inserted into the numerical proof.

## 5. M3: actual set union and duplicate subtraction

Let P24 encode all actual F-words through length 24. The overlap with
the long branch of F_3 can be obtained by lengths alone from its accepted
unambiguous expression. With base length 12 and loops of lengths 5,5,8,
the long-branch terms through 24 are exactly

    z^12+2z^17+z^20+4z^22.

Indeed the only total loop lengths <=12 are 0, 5, 8 and 10, with
multiplicities 1, 2, 1 and 4. There is no lost length-24 term. Terms
of length 25 and greater remain in the tail. The separate z^4 branch
is already in P24 and is not added a second time.

Both ingredients in the candidate's union are subsets of the actual F.
Their intersection is exactly the known prefix of F_3 just identified.
Therefore its generating series is exactly

    G=P24+z^12/(1-2z^5-z^8)-z^12-2z^17-z^20-4z^22.

This is a set union, not an unconstrained signed series. More explicitly,
it can be written G=U+z^12/W with W=1-2z^5-z^8 and

    U=z^4+2z^14+3z^16+4z^18+8z^19+5z^20
      +20z^21+10z^22+40z^23+42z^24.

Every displayed coefficient of U is nonnegative. All actual minimal
factors of length <25 are in G, so N=25 is the correct missing-degree
threshold for M1 and M2. This does not claim completeness of F at
length 25 or above.

## 6. M3: independent finite integer reconstruction of the strict sign

I used the fixed trial r=p/q with p=100000000 and q=176522347; there
was no trial search, bisection or floating-point inference in my check.
First, 3q-5p=29567041>0 proves r<3/5. It follows already by hand that

    2r^5+r^8 < 2(3/5)^5+(3/5)^8=67311/390625<1.

Thus W(r)>0, and the nonnegative geometric long branch and its first
derivative converge absolutely at r. This convergence conclusion does
not use an assumed radius or root for the unknown F.

To avoid copying the constructor's quotient-derivative evaluation, I
derived a denominator-cleared polynomial identity. Write

    V(z)=25-48z+sum_n (25-n)u_n z^n.

Direct differentiation of z^12/W gives exactly

    25W(z)^2 E_G(z)
      =W(z)^2 V(z)+13z^12-36z^17-21z^20.         (*)

The last three terms arise from
13z^12 W+z^13 W', with W'=-10z^4-8z^7; the signs and coefficients
13,-36,-21 are consequently checked independently.

Let w=q^8-2p^5q^3-p^8 and let v=q^24 V(p/q), computed as an integer
homogenization. The right side of (*) multiplied by q^40 is the integer

    J=v w^2+13p^12q^28-36p^17q^23-21p^20q^20.

The independent saved certificate verifies w>0 and J<0 using ordinary
integer arithmetic. Therefore

    E_G(r)=J/(25q^24 w^2)<0.

Its entire unreduced J, positive w, and reduced numerator and denominator
are saved in `moment-tail-review-1-certificate-output-v1.json`. The same
independent homogenization of P24 verifies E_P24(r)>0. After deriving
and running this certificate, I opened the constructor's code and JSON:
both reduced fractions agree exactly, digit for digit, with my results.
Thus the check is not a rerun of the author's code or an assumption that
its chosen trial has the required sign.

The certificate child had PID 89100, an external 10-second timeout,
exit code 0, and was reaped after about 0.0284 seconds. The saved runner,
start/completion records and stderr preserve this small proof-critical
finite arithmetic. No history, factor set, automaton, queue state or
larger cap was searched.

Applying M2 now proves the candidate strict bound

    lambda>q/p=176522347/100000000=1.76522347.

The accepted previous lower bound 1.76521 is strictly smaller. The
positive E_P24 sign at this same trial verifies the stated particular
extra contribution of the known infinite tail. It does not establish
optimality of either test or rule out another argument using P24.
The upper bound lambda<1.834856083 remains an accepted dependency;
this audit does not supply a new check of its old large vector certificate.

## 7. Adversarial boundary checks and scope

The following potential failure modes were specifically tested by reasoning:

* Infinite G does not prevent a formal renewal identity, because every
  coefficient has finitely many words. Convergence at the later real
  evaluations is established separately.
* Root divergence is proved from the infimum growth formula, not inferred
  from a rational denominator or an unproved simple-pole assumption.
* The endpoint case R_G=R and the cancellation case A=0 are both handled.
  A possibly infinite second moment at R is not used.
* M2 makes no statement about the sign of E_G' beyond R; a positive
  rational convergence check for explicit G suffices for its contradiction.
* The regular branch consists of true minimal forbidden factors, not an
  approximation with false extra obstructions. Its duplicate prefix is
  removed only through length 24, with length 25 retained.
* The first missing degree is 25, not 24 or 26. Its weight in E is zero
  at degree 25; later tail degrees carry the additional negative weight.
* The exact numerical conclusion is strict because E_G(r)<0 strictly
  excludes r<=R. No rounded root or uncertified monotonic bisection is
  needed to deduce it.

No counterexample or unresolved inference was found within these claims.
The recommendation concerns these partial theorems only. It does not
identify the exact growth constant or promote a finite-cap rational model
to a model of the unrestricted canonical language.

## 8. Preservation, sources, and freeze

Only `reviews/moment-tail-review-1-*` files were written. All thirteen
constructor/dependency records in the supplied freeze were checked
unchanged, including the accepted mathematical texts. The original
candidate and any peer review were not edited. The preceding 2022 review
and all older own frozen work remain immutable. There was no Git operation,
spawning, new dependency, charge, external contact or source redistribution.

The primary official paper was opened directly. All additional mathematical
premises are explicitly accepted local results; no uninspected external
paper fills a gap. The source-check file records the exact interface and
the acceptance scope rather than claiming to re-enumerate accepted data.
Authoritative telemetry at transition read 24% total weekly used,
10080-minute window, reset 1792745187; cutoff 90% total with reserve.
This complete report, ledger, source checks, independent finite certificate
and manifest are frozen before its conclusions are disclosed to a peer or
before an author repair could be initiated.
