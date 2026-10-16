# A concavity upper bound for the official tiling count

**Proved, independently reviewed (partial result)**, accepted exposition v1.1,2026-10-16 UTC. Both fresh blind whole audits and all issue dispositions are accepted; see ../reviews/concavity-acceptance.md. The frozen construction remains unchanged. The body retains its construction-stage proposed-result wording; that historical wording is superseded by this acceptance. Novelty and the exact rates remain unresolved.

**Finite-size clarification checked by both audits:** use the imported stronger zone estimate only for n>=2, initialize B2=1, and sum insertion bounds for j=2,...,n-1. This supplies the same asymptotic coefficient. The encoding-tree bound needs at most one blue successor. These are the reviewers’ already reconstructed source qualifications, not new mathematical premises.

## Source input and proposed result

Justin Dallant, *Improved Bound on the Number of Pseudoline Arrangements
via the Zone Theorem*, [arXiv:2502.20909v2](https://arxiv.org/pdf/2502.20909v2),
2025-03-07, Lemmas 3--7 and Section 2 (PDF pp. 3--6). The full author PDF is cached at
`.cache/literature/deep-literature-r2/2017-dallant-zone-2502.20909v2.pdf`,
SHA-256 `9ae4886f8b1fce91c6ae8e86c577c5690d0f2ef10355a6524235f95a18dfa03b`.
The published argument obtains 0.6496 by a branch-and-bound LP certificate.
The proposed replacement below is a concavity proof for its same necessary
six-variable entropy domain, together with five exact rational log bounds.

**Proposed C1:** for the official marked tiling/arrangement count,

    limsup_(n→∞) log2 C(n)/n² < 324757/500000 = 0.649514.

This is a candidate strengthening of the located published 0.6496 bound,
not an accepted new frontier result. Its originality has not been established.

Here a simple arrangement has one transverse crossing per pair and no
triple crossing. It is marked by a north unbounded cell; isomorphisms
preserve orientation and that cell. Let gamma_n be the maximum number of
north-to-south paths in the directed dual of its wiring diagram. The
following source input is an attributed combinatorial bound, not a new
proof of the zone theorem or its cutpath encoding.

For a path, k is its number of middle exits taken, u its unique exits
taken, and m all middle exits available among its visited cells. Primes
denote the same quantities after rotating the plane by 180 degrees.
Dallant's Lemma 3 bounds each class of paths by

    binom(n-u,k) * (m/(n-u))^k * 2^(n-k-u),                (S1)

and also by its primed counterpart. Its hypotheses are k<=m and k+u<=n;
the extra condition n-u<=m from the older Felsner--Valtr lemma has been
removed in Lemma 3. Each available middle exit uses a different
pseudoline, so m,m'<=n. A middle exit in one direction is a unique exit
in the opposite direction, so k<=u' and k'<=u. The source's zone theorem
implies that the visited cells have at most 5.5n-5 boundary edges. Counting
their lower and upper edges gives 4n+m+m'-u-u', hence the necessary,
slightly weakened inequality m+m'-u-u'<=1.5n. These are all the source's
integer feasibility constraints (Lemma 6). No sufficiency is asserted.

There are at most (n+1)^6 integer tuples. Put mu=m/n, a=k/n, u=u_integer/n
(and similarly with primes); from this point onward u is normalized.
For 0<=k<=N, the binomial theorem with p=k/N gives
binom(N,k)*p^k*(1-p)^(N-k)<=1, and therefore
binom(N,k)<=2^(N h(k/N)), including k=0,N by limits.
Apply this with N=n-u_integer to (S1). Taking log2 and dividing by n
gives f below; the class satisfies both the unprimed and primed bound,
so its logarithm is bounded by their minimum. If N=0 then k=0, all exits
are unique and the encoding has at most one path; the limiting formula
is f=0. At k=m=0, the factor with exponent zero is 1. Thus no division
by zero or omitted endpoint is used. Summing the classes gives

    gamma_n <= (n+1)^6 * 2^(n sup_D G),

where G=min(f(mu,kappa,upsilon),f(mu',kappa',upsilon')) and

    f(mu,a,u)=(1-u)h(a/(1-u))
              +a log2(mu/(1-u))+1-a-u.

The closed feasible domain D is given by nonnegative variables satisfying

    mu,mu' <= 1,
    kappa <= mu,  kappa' <= mu',
    kappa+upsilon <= 1,  kappa'+upsilon' <= 1,
    kappa <= upsilon',  kappa' <= upsilon,
    mu+mu'-upsilon-upsilon' <= 3/2.

The polynomial factor (n+1)^6 safely counts all integral six-tuples,
including zero endpoints; its exact lower-order choice is immaterial.
All endpoint expressions below use continuous limiting values. No numeric
optimization or claim of sufficiency of this entropy domain is needed.

## 1. Joint concavity permits symmetrization

Put b=1-u-a. Algebra gives

    f(mu,a,u) = a log2(mu/a) + b log2(1+a/b) + b.             (1)

The first term is the perspective of log, with scale a and numerator mu.
The second term is the perspective of log(1+x), with scale b and
numerator a. Both are jointly concave in their arguments; b is affine in
(a,u), so f is jointly concave on mu>=a>=0,b>=0. The limiting extension
is continuous there, including a=b=0 when it occurs in D.

For any feasible pair of triples T,T', their average bar(T) gives a
feasible symmetric six-tuple. In particular, kappa<=upsilon' and
kappa'<=upsilon imply bar(kappa)<=bar(upsilon); the zone constraint
gives bar(mu)-bar(upsilon)<=3/4. Concavity yields

    min(f(T),f(T')) <= (f(T)+f(T'))/2 <= f(bar(T)).           (2)

It therefore suffices to bound the symmetric feasible triples

    0<=u<=1,  0<=a<=min(u,1-u),
    a<=mu<=min(1,u+3/4).

For fixed a,u, f is nondecreasing in mu. Hence set
mu=min(1,u+3/4), with no loss for an upper bound.

## 2. The interval 0<=u<=1/4

Here mu=u+3/4. For fixed mu,u with a>0,b>0,

    partial f / partial a = log2(mu*b/(a*(1-u)))-1.

This decreases with a. At a=u its nonnegativity is equivalent to

    (u+3/4)(1-2u) >= 2u(1-u),

which reduces to 3/4 >= (5/2)u and holds throughout the interval.
Thus f is maximized at a=u. The u=0 endpoint follows by continuity.
Define the concave one-variable function

    Phi(u)=u log2((u+3/4)/u)
            +(1-2u)log2((1-u)/(1-2u))+1-2u.                (3)

Its concavity follows directly from (1) on this affine slice. At a0=21/100,

    Phi(a0)=(21/100)log2(32/7)+(29/50)log2(79/58)+29/50,

    Phi'(a0)=[ln(107648/43687)+7/32+21/79]/ln2-2.           (4)

The exact finite certificate below verifies

    Phi(a0) < 64951/50000 = 1.29902,
    0 < Phi'(a0) < 1/5000.

A concave function lies below its tangent. Since u-a0<=1/25,

    Phi(u) <= Phi(a0)+Phi'(a0)(u-a0)
            < 64951/50000 + (1/25)(1/5000)
            = 324757/250000 = 1.299028.                   (5)

The same bound covers u<a0, because the positive derivative makes the
tangent value smaller there. This is a uniform strict bound with positive
slack given by the exact constants in (4).

## 3. The interval u>=1/4

Set mu=1. The tangent of f(1,a,u) at a=u=1/4 has value

    F0=1+(1/2)log2(3/2),

and derivatives

    fa=log2(4/3)>0,
    fu=-log2(3/2)+1/(3ln2)-1.

Their sum is log2(8/9)+1/(3ln2)-1<0, because ln2>1/3.
For example, the first term of the positive logarithm series below gives
ln2>=2/3>1/3, while log2(8/9)<0.
Joint concavity and a<=u therefore give

    f(1,a,u) <= F0+fa(a-1/4)+fu(u-1/4)
              <= F0+(fa+fu)(u-1/4) <= F0.

The exact certificate verifies F0<1293/1000, smaller than the bound in (5).
By continuity this also covers all boundary cases with a=0 or b=0.

Combining (2), (5) and this last inequality gives sup_D G strictly less
than 324757/250000. Compactness and the uniform tangent bound make the
strict slack independent of n.

## 4. Passing from cutpaths to the official exponent

The marked-arrangement deletion/insertion inequality in the source is
B_(n+1)<=gamma_n B_n. Therefore summing the logarithms gives

    log2 B_n <= (A/2)n²+O(n log n)

for a fixed A<324757/250000. More explicitly, sum
6 log2(j+1)+Aj for 2<=j<n, starting from B2=1; their two sums are O(n log n) and
A*n*(n-1)/2, respectively. The [official notes](https://www.simonmarais.org/uploads/8/2/3/5/82358688/smmc-2017-solutions-preliminary_1.pdf),
p. 12, identify the fixed-polygon tilings with pseudoline arrangements
and give C(3)=2,C(4)=8. The marked-arrangement/rhombus-tiling dictionary
in Felsner--Valtr, Section 1, [author PDF](https://page.math.tu-berlin.de/~felsner/Paper/new-pla.pdf),
uses the fixed boundary order and orientation convention. We import this
attributed dictionary: C(n) is the marked count B_n, with no quotient by
polygon rotations or reflections and no count of reduced words before
commutation. Any label/mark convention discrepancy bounded by 2^O(n log n)
would also leave this exponent unchanged, but the claimed dictionary is
an explicit source-audit target, not a substitute for checking conventions.
Thus the proposed C1 follows. This is an upper bound only; neither a
matching lower bound nor existence of the normalized limit follows.

## 5. Exact finite certificate and remaining review

For rational r>1 put z=(r-1)/(r+1). For N=80 use

    L_N(r)=2 sum_(k=0)^(N-1) z^(2k+1)/(2k+1),
    0 < ln r-L_N(r)
        <= 2*z^(2N+1)/((2N+1)*(1-z²)).

This follows by bounding every remaining denominator from below by 2N+1
and summing the resulting geometric series. The source script uses exact
Fraction arithmetic for r=2,32/7,79/58,107648/43687,3/2 and propagates
interval bounds through (4). It asserts every displayed rational inequality
and saves full interval numerators and denominators. Floating-point values
are displayed for diagnostics only and are not the certificate.

Run from the repository root:

    python3 -u problems/2017-B4/computations/deep-literature-r2-concavity-certificate.py

The supervisor fixes a 30-second external cap, records the dedicated child
PID and checkpoints each logarithm, and reaps the child. No CAS, dependency
installation, global process cleanup, charge or separately billed API is
used. The job/result files record the exact outcome; they are construction,
not independent audit.

The preserved run began at 2026-10-16T17:26:45Z, child PID 59036, with
exit code 0, reaped after 0.086916375 seconds and no timeout. The script's
SHA-256 is `f26e2b9aabe20dc01457e6b7e4a4ce6e168f3a8be046db5965b7fc69d725e03b`;
the exact certificate's is `8b5222a9240d6d6dd8126ccaaff8a2585523f1914e8e4b2932b6ae07fa14714f`.
The separately written freeze manifest hashes this proof and all preserved
construction artifacts. Rerunning the script would replace its job/output
files; reviewers should run a copied script in their own assigned prefix.

Review must reconstruct all published cutpath hypotheses, the entropy
domain including endpoints, the two concave perspectives, the symmetry
step, both interval arguments, the log tail bounds and the conversion of
a strict objective bound to a limsup bound. Two independent reviewers are
required before any promotion. The current published-bound register must
not be changed merely because this candidate certificate passes.
