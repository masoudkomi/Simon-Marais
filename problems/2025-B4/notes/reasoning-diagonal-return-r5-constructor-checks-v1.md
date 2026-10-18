# RD1--RD4 hand reconstruction and boundary checks

2026-10-18 UTC. Candidate proof - unverified; B author checks only.
No mathematical executable, numerical example, scan or optimizer ran.

## Trace-degree and support checks

The critical degree argument is quadratic, not linear. The pair
(beta_a,beta_-a) has common productY^2. Equal pair sums force the
same unordered pair, so distinct BD conjugates give exactly d sums.
Even a possible zero sum could not create a repeated trace: the same
quadratic argument applies. No normal-basis assertion enters.

At ell|Y the complementary coefficient pairs are exactly0/2 or1/1.
There are r of the first kind and d-r of the second. Unequal orders
0/2 cannot cancel; equal1/1 orders may cancel, so only a LOWER
bound is used. The guaranteed denominator exponent is
2*binom(d-r,2), NOT an exponent copied from the full D-field
discriminant. In particular r=d and r=d-1 both give Hplus0.

Expanding the new exponent directly gives

    d(d-1)-(d-r)(d-r-1)=2dr-r^2-r=r(2d-r-1).

At r=d and r=d-1 it is d(d-1). For every other allowed r the
nonnegative integer product(d-r)(d-r-1) is the exact gap. This
does not require a uniform sparse support, which RS rules out across
large primes under a fixed-r assumption.

## Ramification and collision factors

For V_a=1+a^t u0 lambda^t+..., the exact algebra
V_a+V_a^-1-2=(V_a-1)^2/V_a gives leading coefficient a^(2t)u0^2.
Its order is2t, not t. Real differences have even order; when that
coefficient cancels the guaranteed improvement is2, not merely1.
On the d trace indices the leading map has kernel g, not2g; the
full G map has2g. Thus squared differences give

    baseline:2*(2t)*binom(d,2)=2t*d(d-1),
    extra:   2*2*[d(g-1)/2]=2d(g-1).

Dividing by v_lambda(p)=2d gives t(d-1)+g-1. This calculation is
for a rational discriminant, not for Norm(alpha) of an arbitrary
K-element. The g1 case is valid with an empty tied-pair set. Actual
trace differences are nonzero, so no infinite valuation is secretly
used to produce a nonzero integer norm.

## Interval bound and exact residual threshold

The first monic polynomials are C1=T,C2=T^2-2,C3=T^3-3T.
The determinant uses the column1,not C0=2. Otherwise an unwanted
factor2 would enter. Hadamard only uses the bounds on these columns,
not their discrete orthogonality at the actual trace points.

At residual depth s, the threshold A0=p^[2(s-1)] gives

    A0^[d(d-1)]=p^[(p-1)(s-1)(d-1)].

This EXACT exponent cancels the s-dependent part of the lower bound.
The remaining p^[3(d-1)] is compared with2*4^(d-1)d^d. The simple
induction d<=2^(d-1) reduces the latter to at most(8D)^(d-1).
Since p^3>8D, the contradiction is uniform in EVERY s>=2. No
logarithmic rounding or asymptotic p estimate is required.

The full-field BD exponent would instead leave an s-dependent loss;
its worst-support comparison at this squared-distance threshold has
exponent difference D(4-s)-3 BEFORE its D^D factor. It therefore
does not supply this all-depth cancellation by the same argument.
This comparison is not a novelty claim or an audit of all possible
consequences of the old inequalities.

The triangle inequality U<=1+c p^s works equally for X positive
or negative and for a0=0 or-1. At s2 the conclusion is just c>=2;
at s3 it becomes c>=p+1. A fixed cofactor bound therefore restricts
unbounded p to s2. It does not bound the number of those primes or
solve the resulting X=-1+/-c p^2 equations. Exact p-divisors of a
displayed non-p-free C are absorbed into s before applying the rule.
