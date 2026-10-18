# WO constructor exact hand checks

2026-10-18 UTC. **Candidate proof - unverified.** These are constructor
checks to challenge, not independent audits. No mathematical executable.

FAMILY algebra: d1 multiplied by L gives2L+M<=L²M. For d2 multiply
by L to obtain2L+2M<=L²M². The positive root is
[1+sqrt(1+2L³)]/L²; the minus root is negative. At f1, the numerator
over(L²-1)² is4L⁴-4L(L²-1)-2L(L²-1)²
=-2L⁵+4L⁴+2L=-2L P(L). Thus the f1/f2 comparison has the
claimed direction, not its reverse.

P'=4L³-6L² is positive for L>=2. P2=-1;
P(9/4)=(9/4)³(1/4)-1=(729-256)/256=473/256.
(9/4)²=81/16<7, and9/4<1+sqrt2 since5/4<sqrt2.
The latter proves ell²-2ell-1<0 and M*>1. Since ell>2,
ell²-1>3>2, giving M*<ell and V*>1.

At the proposed parameters d1/d2 are equalities, so g2/g1=1.
The ratio is [1+1/(2V*+d)]/M*, strictly decreasing. Every integer
d>=2 ratio is strictly less than1; this covers ALL higher degrees,
not an empirical claim. d0 gives2/ell<1 separately.

Differentiation on the first envelope gives
1/L+(3/4)[1/L-2L/(L²-1)]=(L²-7)/[4L(L²-1)].
On the second, differentiating L²M²-2M-2L=0 gives
(L²M-1)M'=1-LM². The logarithmic derivative numerator becomes
M(L²M-1)+(3/4)L(1-LM²)
=(1/4)L²M²+(3/4)L-M=(5/4)L-(1/2)M.
F_L(L)=L⁴-4L>0 on L>=2, while the only positive root is f2,
so M<L. This proves the second derivative is positive even as
L grows without bound and f2 may fall below1. It is only a lower
envelope there; actual feasible M remains>1.

The old-rational comparison uses527²=277729,
527³=146363183,27*527³=3951805941,250⁴=3906250000.
Their difference45555941 is positive. This proves L0>ell by strict
monotonicity, without a numerical root/log. The accepted old triple
is feasible, so its objective exceeds the exact unique minimum.

ACTUAL paths: a complete path visits n nonterminal tail cells. Exactly
u are unique, so W=ell^(-(n-u))M*^-m V*^-k. Combining orientations,
sqrtWW'=ell^-n M*^[-(m+m'-U)/2]V*^[(U-T)/2]. V*>1 and U>=T
make the last factor>=1; M*>1 and defect<=3n/2 make the middle
factor>=M*^(-3n/4). These signs still hold for negative defect.
Flow and same-path Cauchy therefore bound the NUMBER of paths.

RENORMALIZATION: all row sums are positive, so W/S is exactly the
product of the normalized edges, with local sum1. It is not a
path-dependent probability assignment. Prefix-tree expansion counts
every original path, retaining reconvergent histories separately.
Every costly visit contributes sigma<=rho, all other visits sigma1.
Thus SS'<=rho^b and sqrt[WW'/(SS')]>=K*^-n rho^(-b/2).
Two independent sums are NOT multiplied in the wrong direction:
Cauchy bounds the sum of square roots by1, yielding the moment.

For b>=h and0<rho<1, rho^(-b/2)>=rho^(-h/2); the tail count bound
follows by restricting a nonnegative sum. It is not normalized by
the actual path count. WO4 requires a genuine independent bound on
the actual LOW-cost subfamily; no new realization/counting theorem
supplies it. The strict K_new<K* uses both J<K* and eta>0.
Summing a constant log2(2) per insertion contributes O(n), while
sum j=n²/2+O(n); the official exponent is half the path exponent.

All boundaries L2, d0/1/2/3/arbitrarily large d, open M/V>1,
negative defect, b0, h0/real or empty high-cost tail, finite initial
insertion size and rho strictly between0/1 are included. No geometric
arrangement attaining the family optimum is supplied or required.
