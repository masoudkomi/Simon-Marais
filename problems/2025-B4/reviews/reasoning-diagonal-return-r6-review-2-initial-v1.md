# DR6A–DR6D: independent whole initial review 2

18 October 2026 UTC. Reviewer C, `/root/review_2017_coarsening_r1`.
This is an OTHER nonconstructor ENTIRE WHOLE review of all 48 obligations.
The constructor is A. Root is the other reviewer. No corresponding NEW
root DR6 report, finding, source, code, hash or metadata was accessed before
this entire packet froze, received full final model readback, and underwent
a separate read-only verification. Findings remain embargoed until root
explicitly confirms BOTH entire checkpoints.

**Initial disposition: all 48 obligations pass in the stated scope.** No
substantive defect or required author repair was found. Seven closed scope
notes are recorded separately. This is a recommendation to the coordinator,
not a promotion, independent external validation or a full annual solution.

C constructed the OLD accepted R6 arithmetic/phase packet and has older
review roles in RS, BR and BD. These roles are disclosed. This audit is of
the NEW DR6 proof; it is not an independent recertification of C's older
theorem. The separately accepted RD3 consequence is the only nonelementary
old result used in the new proof. All five current accepted bodies and
their complete MD/JSON authorities were freshly read, including their exact
limitations. No new proof inference was supplied to A during construction.

## 1. Exact statement, actual quantities and dependency

The official open (b) asks for ordinary integer solutions of
`1+X+...+X^n=Y^q`, with n,q>=2. DR6 works only with

    Phi_p(X)=Y^p, p>=37 prime, |X|>=2,

so the official degree is p-1, and the number of terms and perfect-power
exponent are p. It additionally assumes the ACTUAL residual condition
`p|X(X+1)`. It does not assert that all prime-diagonal solutions are residual.
Both signs of X and the two distinct residue centers are retained. No
preliminary (a) proof or other annual sector is supplied.

For an actual residual solution, exactly one a0 in {0,-1} is congruent to X
mod p. With s=v_p(X-a0), the definitions

    X=a0+epsilon*c*p^s, c=|X-a0|/p^s,
    c in positive ordinary integers, p∤c, epsilon in {1,-1}

are exact. An arbitrary unnormalized displayed coefficient cannot replace c.
The accepted RD3 applies to precisely this signed prime-diagonal sector and
gives `c>p^(s-2)` once s>=2. Its actual integral Jacobi lift, characteristic
ideals, finite-prime arguments and attributed classical matched-prime Jacobi
ideal theorem remain accepted dependencies; DR6 neither removes nor adds
an assumption to that chain. The new depth-two calculation itself uses
only the actual integer equation and elementary real inequalities.

The proposed conclusions are the signed lattice table and root gap at s2;
the growing bound `c>(p-1)/(6 log p+1)` at all actual depths; exclusion of
the four whole twice-distance families at p>=37; and explicit finiteness
for each fixed bounded residual cofactor. They are not an unrestricted
prime bound or a bound on c in every actual solution.

## 2. Ordinary valuations and the depth-two congruences

Put U=|X|. For negative X, `Phi_p(-U)=(U^p+1)/(U+1)>1`; for positive X
the assertion is immediate. Since p is odd, an actual integral Y is positive
and >1. At either residual center Phi_p(X) is 1 mod p. Fermat therefore
gives Y=1 mod p. If h=v_p(Y-1)>=1, the first term of `(1+p^h u)^p-1`
has valuation h+1. Every middle term has valuation at least 1+2h and the
last has valuation ph>h+1 for odd p>=3. Thus its unique minimum gives
`v_p(Y^p-1)=h+1`.

At center0, `Phi_p(X)-1=X(1+...+X^(p-2))`, with a p-unit second factor.
At center-1, `Phi_p(X)-1=X(X^(p-1)-1)/(X-1)` and X,X-1 are p-units.
The quotient `(X^(p-1)-1)/(X^2-1)` has residue (p-1)/2, a p-unit, while
`v_p(X^2-1)=v_p(X+1)=s`. Both centers consequently give s=h+1>=2 and
U>=p²-1. The argument is valid for either ordinary sign, without a source
class-field hypothesis.

At s2 write Y=1+pk. Mod p³ the first binomial term is p²k, the j2 term
has a p³ factor, every remaining middle term a still higher factor, and
the final pth term has p^p. Hence `Y^p=1+p²k mod p³`.

For center0, `X=epsilon*c*p²` makes `Phi_p(X)=1+epsilon*c*p² mod p³`,
so `Y=1+epsilon*c*p mod p²`. For center-1 put T=X+1. The shifted
integer polynomial Phi_p(-1+T) has constant 1 and derivative

    1-2+3-4+...+(p-2)-(p-1)=-(p-1)/2.

Its degree>=2 terms are integer multiples of T², hence vanish mod p³ at
T=epsilon*c*p². Multiplication by 2 before cancelling p² proves
`2k=epsilon*c mod p`, or `2(Y-1)=epsilon*c*p mod p²`.
The factor 2 is indispensable: for odd c its modular inverse cannot be
replaced by a real half when measuring an interval. This proof retains it.

## 3. Signed root gap and all four positive lattice representatives

For odd p>=3 and U>=6,

    Phi_p(X)<U^p/(U-1).

The finite binomial expansion gives
`(1+1/(p-1))^(p-1)<=sum 1/j!<3`; the factorial tail after 1+1 is <1
since j!>=2^(j-1), with strict inequalities in the tail. Multiplication by
p/(p-1)<=3/2 gives `(1-1/p)^(-p)<9/2<5`. Since U-1>=5, taking the
positive real pth root gives `Y<U(1-1/p)`.

For the other direction, `Phi_p(X)>(U-1)^(p-1)` holds at positive X by
the top term. At negative X use

    (U^p+1)/(U+1)>U^(p-1)*U/(U+1)
       >U^(p-1)*(1-1/U)
       >=U^(p-1)*(1-1/U)^(p-1).

Thus, for the ACTUAL positive integer Delta=U-Y,

    U/p<Delta<1+(U-1)log(U-1)/p<1+U log U/p.

The strict upper estimate follows from 1-exp(-z)<z for z>0. The actual
residual lower U>=p²-1 easily meets U>=6. No asymptotic error is used.

Substituting U-Y=Delta into the congruences gives exactly:

|Center|Actual U|Integer multiple of p²|
|---|---|---|
|0|cp²|Delta+epsilon*cp+1|
|-1|cp²-epsilon|2Delta+epsilon*cp+2(epsilon+1)|

For epsilon=1 each is positive. For center0/epsilon=-1, Delta>cp makes
the first >1. For center-1/epsilon=-1, U=cp²+1 gives Delta>cp+1/p, so
`2Delta-cp>0`. These are positive ORDINARY integer multiples of p²,
not merely residues. They therefore yield the common inequality

    p²<=2Delta+cp+4.

Both corners of the sign table, and the additive 4 in its neighboring
positive-sign row, are correctly retained. This reconstructs DR6A.

## 4. Growing cofactor and the exact all-depth extension

At depth2, c>=p already implies the proposed lower bound. Otherwise
c<=p-1 and U<=cp²+1<p³. The gap and common lattice bound give

    p²<cp(6log p+1)+6+6log(p)/p
       <cp(6log p+1)+12.

The additive 6 is 2 from twice the root-gap constant plus 4 from the
lattice table. The additional 6log(p)/p accounts for U's possible +1.
Because p>=37>12, `p²-12>p(p-1)`, and the strict bound follows:

    c>(p-1)/(6log p+1).

At s>=3 the separate accepted RD3 gives `c>p^(s-2)>=p`, which is stronger.
No quadratic congruence is silently continued to other depths, and s1
was already excluded. This proves the stated all-residual DR6B.

At center0 the signed published prime-divisor restriction is stronger:
an eligible prime ell|X with ell=1 mod p must divide c, is not p, and is
at least 2p+1 (p+1 is even >2). This is attributed overlap. It is not used
to prove the neighboring-center inequality or substituted for RD3.

## 5. Whole cofactor-two exclusion: hand constants and endpoints

If c=2, s1 fails the elementary valuation calculation and s>=3 fails
RD3 at p>=37. At s2, U<=2p²+1. The common lattice inequality and gap
imply

    p²<2p+6+(4p+2/p)log(2p²+1)
       <2p+6+(4p+2/p)log(3p²).

Define `F(p)=p-2-6/p-(4+2/p²)log(3p²)`. Direct differentiation gives

    F'=1+6/p²+4log(3p²)/p³-8/p-4/p³
       >1-8/p-4/p³>0, p>=37,

using p²(p-8)>4. Thus it suffices to prove F(37)>0. I independently
checked every rational comparison, without a logarithm program:

* At 9/8, the j0..4 exponential sum has numerator
  `98304+110592+62208+23328+6561=300993` over 98304, exceeding 3.
* At 15/4 the j2..6 terms are `225/32`, `3375/384`, `50625/6144`,
  `759375/122880`, `11390625/2949120`. They exceed respectively
  7,35/4,8,6,7/2. Adding j0,j1 gives a strict lower bound 38>37.
* Hence log3<9/8 and log37<15/4. Also `35-6/37>174/5`,
  `4+2/37²<401/100`, and `log(3*37²)<69/8`.
  Their product bound is `27669/800<173/5`, since 27669<27680.

Consequently F(37)>1/5 and F(p)>0 for every real p>=37, contradicting
the displayed strict inequality. This is uniform over every prime and
all four sign/center cases. RD3 already excludes c1. The proposed c>=3
and all four whole families in DR6C follow. The known p3 negative example
lies outside this cutoff and is not contradicted. No claim for p<37 follows.

## 6. Effective bounded-cofactor sector and its limits

For fixed positive INTEGER C with actual c<=C, DR6B gives

    p<6C log p+C+1<=6C log p+2C<8C log p.

Let L=8C and x0=2Llog(2L). Here 2L>=16>e and x0>e. The inequality
`log log(2L)<log(2L)` gives `Llog x0<x0`. Since x/log x increases on
x>e, `p<Llog p` forces `p<x0=16C log(16C)`. Separately, the SAME
actual RD3 inequality `p^(s-2)<c<=C` gives the strict bound
`s<2+log C/log p`.

The finite parameter set is therefore explicit: primes in the displayed
interval, integer depths in the displayed interval, 1<=c<=C with p∤c,
two centers, two signs. They specify X exactly and each X has at most one
positive Y. This is an effective finite search prescription for bounded
residual cofactor, not a performed search or unrestricted finite list.
If a displayed C is divisible by p, the actual normalized quantities are
`c=C/p^v_p(C)` and `s=a+v_p(C)`; c<=C survives. C1 and C2 are empty by
the preceding results. Arbitrarily large c is still permitted, so no
uniform prime bound, global finite reduction or annual solution follows.

## 7. Sources, actual versus formal scope, and audit boundary

The official open signed domain was freshly checked. Bennett–Levin's
signed Proposition1 was inspected as an attributed overlap statement;
its constituent historical proofs were not newly certified. Mihailescu's
original author text was read at the domain/theorem passages, complete
Lemma7 statement and supplied proof, and the Section5 opening/returned
operative context. The strong lower-bound route there starts under a
real class-number hypothesis. Neither it nor the whole later theorems,
appendices, foundations or historical calculations is imported by DR6.
The source itself leaves some Lemma7 details to the reader; the new
elementary proof above supplies the needed 0/-1 residual argument.

The distinct-prime 2026 result is unused, and its whole proof is not
freshly read or certified here. The coordinator higher-trace note is
only an unverified FORMAL diagnostic. It supplies no actual Jacobi
construction, field realizability, extra cancellation or DR6 premise.
No root-of-unity phases, support, class-number condition, ideal unit,
unproved higher jet or all-generator theorem enters the ordinary proof.

All 13 constructor files, all 48 obligations/checks, sources, failures,
worklog, administrative code, baseline, validation, metadata and freeze
were read. The earlier combined tool output clipped the tail of two
context files; their complete texts were separately recovered before
this report. No missing passage is described as a full read. The new
code checks preservation only; no mathematical executable, scan, CAS,
table, numerical logarithm, author/source program or old freezer replay
was used. No pending tool approval, retrieval or native child exists.
The compact baseline records exact parent/input fingerprints rather
than duplicating the entire historical inventory. Every older byte is
preserved. Final disposition remains subject to the other complete
whole audit and coordinator reconciliation.
