# Blind full adversarial review 2: the 2017 B4 concavity candidate

**Review status: initial independent audit complete; mathematical C1 passes this
review, with a nonblocking small-size clarification.** This is a reviewer
opinion. The candidate remains **candidate proof - unverified** until the
coordinator completes the required independent-review process. This report
does not promote it, establish originality, solve all of B4, or establish
existence of a limit.

The review was carried out on 2026-10-16 UTC (2026-10-17 in Brisbane) by fresh
reviewer `/root/review_2017_concavity_r2`. Requested settings supplied by the
coordinator: `gpt-6.1-sol`, `max`; verified effective-setting readback:
**unavailable**. No other reviewer report or conclusion was read before this
report, its issue log, source audit, independent calculation, and freeze
manifest were completed. I did not construct the candidate. I read the proof
and construction manifest, but did not read the constructor's script or exact
output before completing my own derivation and certificate. I made no edits to
the candidate or shared research/status files and performed no Git mutation.

## 1. Target and audited inputs

The target is only

\[
\limsup_{n\to\infty}\frac{\log_2 C(n)}{n^2}
 <\frac{324757}{500000}=0.649514,
\tag{C1}
\]

for the official 2017 B4 fixed-polygon tiling count. Neither a lower bound nor
equality of the liminf and limsup is part of this candidate. All of 2017 B4 is
authorized, with no excluded preliminary part.

The frozen proof is
`notes/deep-literature-r2-concavity-candidate-v1.md`, SHA-256
`07dc9766e56eca4ec3359289a537072d47e6f5ce6b48129538552f54899728fc`.
The corresponding construction manifest has SHA-256
`ec9c085810926b24f43c3249653f84b3a43ec72cbb7e148d38f2fd149b9b65b0`.
Both matched the coordinator's supplied hashes before this audit.

I checked the original cached Dallant v2 PDF, pp. 1 and 3-6, against its arXiv
version record; inspected its actual pp. 5-6 visually; read the author-hosted
Felsner--Valtr paper, especially Sections 1-3; and visually checked the tiling
dictionary on its pp. 2-3 and official B4 notes on p. 12. The separate source
checks file gives hashes, URLs, exact locations, and the distinction between
imported results and the reconstruction below.

## 2. Independent reconstruction of the combinatorial input

Let \(A\) be a simple marked arrangement of \(n\) pseudolines. In its directed
dual, every north-to-south cutpath crosses every pseudoline exactly once.
Indeed, a dual edge crosses from the north side to the south side of its
underlying pseudoline; a directed path can never cross it back. The two end
cells are separated by every line, forcing all \(n\) crossings.

For each path let \(k\) count middle exits taken, \(U\) count unique exits
taken, and \(m\) count all available middle exits of its visited cells. The
primed quantities refer to traversing the rotated arrangement in the reverse
direction. Rotation here is the orientation-preserving half turn used to
describe the same path; it is not a quotient of tilings by polygon rotations.

The following necessary integer constraints are correct:

\[
0\le k\le m\le n,\quad k+U\le n,
\quad 0\le k'\le m'\le n,\quad k'+U'\le n,
\quad k\le U',\quad k'\le U.
\]

The bounds on \(m,m'\) use Knuth's one-middle-appearance lemma as stated by
Dallant. A selected middle becomes a unique exit in reverse; the converse
need not hold for unbounded cells, which is why the weak cross inequalities,
rather than equalities, are appropriate.

For completeness, I reconstructed the refined class bound independently
instead of merely trusting the removal of \(n-U\le m\) in v2. Fix a binary
string for the \(n-k-U\) left/right decisions. Branch over the possible middle
choices, take unique exits deterministically, restrict to the given class,
and contract the unique steps. The remaining rooted tree has:

* all root-to-leaf paths of length \(h=n-U\), with exactly \(k\) red (middle)
  steps;
* at most one blue (the prescribed left/right) successor at a node;
* at most \(m\) red out-edges in total along any root-to-leaf path.

Let \(P(M,H,K)\) be the maximum \(K\)-th elementary symmetric polynomial of
\(H\) nonnegative integer block sizes with sum \(M\). A balanced vector of
sizes maximizes all these polynomials simultaneously: replacing sizes
\(x,y\) by sizes with the same sum and closer values increases \(xy\), while
the polynomial's dependence on these two sizes is
\(e_K+(x+y)e_{K-1}+xy e_{K-2}\) of the other sizes. The coefficients are
nonnegative. Zero-sized blocks are permitted.

The tree has at most \(P(m,h,k)\) leaves. One proves this by induction on
\(h\). A root with \(s\) red successors has at most
\(P(m-s,h-1,k)+sP(m-s,h-1,k-1)\) leaves. Both terms can use the same balanced
block vector. Adding a block of size \(s\) shows that this sum is at most
\(P(m,h,k)\). Missing blue successors only reduce it. The base \(h=1\) has
at most one zero-red leaf and at most \(m\) one-red leaves. The case \(h=0\)
is deterministic and is handled separately.

Allowing real block sizes and repeatedly averaging two sizes gives
\(P(m,h,k)\le {h\choose k}(m/h)^k\). This also holds when \(m<h\): the
integer blocks may be zero, while the real equal vector remains available
for the upper bound. Multiplying by the \(2^{n-k-U}\) binary strings yields

\[
|\Gamma(m,k,U,m',k',U')|
 \le {n-U\choose k}\left(\frac m{n-U}\right)^k2^{n-k-U}.
\tag{R1}
\]

Thus no missing \(n-U\le m\) restriction is needed. This reasoning also
avoids an expository defect in the older tree description: after pruning to
an exact \(k\), a blue child may be absent, so "at most one" is the safe
property. The recurrence above uses precisely that weaker property. Dallant
v2 expressly states (R1) under the candidate's hypotheses.

I checked the edge accounting as follows. The \(n-U\) visited departure
cells with more than one exit contribute two extreme lower edges, all
middle edges contribute \(m\), and the unique cells contribute \(U\). The
total lower incidence count is \(2n+m-U\). Reversing gives upper count
\(2n+m'-U'\). The sink/source endpoint cells are accounted for in the
opposite direction, so they do not add an extra hidden term. Dallant's
imported zone bound therefore gives the weakened necessary inequality

\[
m+m'-U-U'\le \tfrac32n.
\tag{R2}
\]

Its stronger constant term is discarded in the safe direction. The precise
zone bound \(5.5n-5\) should be used only in its nontrivial size range; see
the small-size note CR2-01. No zone theorem or extremal zone construction is
claimed as a new result here.

All six nonnegative coordinates are at most \(n\), so \((n+1)^6\) safely
bounds the number of classes, including zeros. The proof does not need
feasibility to be sufficient.

## 3. Entropy reduction and closed boundary

For \(N=n-U>0\), put \(p=k/N\). The probability of the \(k\)-th binomial
term is at most one, giving
\({N\choose k}\le 2^{Nh(p)}\), also for \(p=0,1\) by direct evaluation.
With \(\mu=m/n\), \(a=k/n\), \(u=U/n\), the normalized logarithm of (R1)
is at most

\[
f(\mu,a,u)=(1-u)h\!\left(\frac a{1-u}\right)
 +a\log_2\!\left(\frac\mu{1-u}\right)+1-a-u.
\]

The class satisfies the primed bound too, so its exponent is bounded by
\(G=\min(f,f')\). The candidate's domain \(D\) is exactly the necessary
closed linear relaxation obtained from (R1)-(R2). There is no omitted
nonnegativity assumption.

Write \(b=1-u-a\). Expanding the entropy cancels the two \(a\log(1-u)\)
terms, yielding independently

\[
f=a\log_2(\mu/a)+b\log_2((a+b)/b)+b.
\tag{R3}
\]

This formula supplies the correct closed-domain interpretation. On
\(0\le a\le\mu\le1\), the first term tends to zero with \(a\), since it
lies between zero and \(a\log_2(1/a)\). On the bounded domain, the second
term tends to zero with \(b\), since it is bounded by
\(b\log_2(1+1/b)\). Both vanish when \(a=b=0\). At \(a=\mu=0\) with
\(1-u>0\), \(f=1-u\); at \(u=1\), necessarily \(a=b=0\) and \(f=0\).
For \(N=0\), every step is a unique exit, and there is at most one path,
independently of the otherwise unnecessary \(m\) value in the relaxed
domain. Thus the zero denominator is genuinely avoided. For \(k=m=0\),
the exponent-zero factor is one.

## 4. Concavity and symmetrization

I verified concavity directly, in addition to checking the perspective
interpretation. For natural logarithms, the Hessian quadratic form of
\(a\ln(\mu/a)\) is
\(-\left(\delta a/\sqrt a-\sqrt a\,\delta\mu/\mu\right)^2\).
For \(b\ln(1+a/b)\), it is
\(-\left(\sqrt b\,\delta a-a\,\delta b/\sqrt b\right)^2/(a+b)^2\).
Both are nonpositive in the interior; division by \(\ln2>0\), affine
substitution of \(b\), and the continuous boundary extension preserve
concavity. The linear term \(b\) makes no change.

The domain is invariant under swapping the two triples and is convex. Its
average is therefore feasible and symmetric. In particular,
\(\bar a\le\bar u\), \(\bar a+\bar u\le1\),
\(\bar a\le\bar\mu\le1\), and
\(\bar\mu-\bar u\le3/4\). Jensen's inequality gives

\[
\min(f(T),f(T'))\le\tfrac12(f(T)+f(T'))\le f((T+T')/2).
\]

This does not assert that an asymmetric class itself has equal directional
parameters. It maximizes over a necessary relaxation, which is sufficient
for an upper bound. Conversely, the symmetric tuples described by those
constraints do lie in \(D\). Since \(f\) is nondecreasing in \(\mu\), with
derivative \(a/(\mu\ln2)\) where defined, we can set
\(\mu=\min(1,u+3/4)\). At \(a=0\) this monotonicity holds by direct
evaluation. This upper cap always remains at least \(a\).

## 5. First interval and exact tangent

Let \(s=1-u\). At fixed \(\mu,u\), differentiation gives

\[
f_a=\log_2\!\left(\frac{\mu(s-a)}{as}\right)-1.
\]

It decreases with \(a\). For \(0<u\le1/4\), the feasible range is
\(0\le a\le u\), \(b\ge1/2\), and \(\mu=u+3/4\). At \(a=u\),
\(f_a\ge0\) is equivalent to
\((u+3/4)(1-2u)-2u(1-u)=3/4-(5/2)u\ge1/8>0\).
So the maximum occurs at \(a=u\), with \(u=0\) checked directly.

On this affine slice, the concave function is

\[
\Phi(u)=u\log_2((u+3/4)/u)
 +(1-2u)\log_2((1-u)/(1-2u))+1-2u.
\]

My independent derivative is

\[
\Phi'(u)=\frac{\ln\!\left(\frac{(u+3/4)(1-2u)^2}
 {u(1-u)^2}\right)+u/(u+3/4)+u/(1-u)}{\ln2}-2.
\]

At \(u_0=21/100\), this gives exactly the candidate's
\(107648/43687\), \(7/32\), \(21/79\), and the value involving
\(32/7\) and \(79/58\). There is no rounding in those identities.

My new standard-library `Fraction` certificate uses 96 terms, independently
written before inspecting any constructor code/data. For rational \(r>1\),
\(z=(r-1)/(r+1)\), integrating the geometric series for
\(2/(1-z^2)\) gives

\[
2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}<\ln r
 \le2\sum_{j=0}^{N-1}\frac{z^{2j+1}}{2j+1}
 +\frac{2z^{2N+1}}{(2N+1)(1-z^2)}.
\]

All quantities are exact rational numbers, with the positive denominator
interval propagated in the correct direction. The preserved calculation
verifies
\(\Phi(u_0)<64951/50000\) and \(0<\Phi'(u_0)<1/5000\).
The maximum tangent offset on \([0,1/4]\) is \(1/25\), since the slope is
positive. Thus a single constant
\(A_1=\Phi(u_0)+\Phi'(u_0)/25<324757/250000\) bounds the whole interval.
This proves uniform slack, not merely a different strict inequality at
each point. The exact intervals also verify the convenient uniform rational
ceiling \(A_1<1299027/1000000<324757/250000\). This auxiliary ceiling is
verification evidence for C1, not a promoted additional research result.

Diagnostic floats, unused as premises, are
\(\Phi(u_0)\approx1.299019323136631\),
\(\Phi'(u_0)\approx0.000136325438659\), and
\(A_1\approx1.299024776154177\).

## 6. Second interval and adversarial endpoints

For \(u\ge1/4\), \(\mu=1\). At \((a,u)=(1/4,1/4)\), I obtain

\[
F_0=1+\tfrac12\log_2(3/2),\quad
f_a=\log_2(4/3)>0,\quad
f_u=-\log_2(3/2)+\frac1{3\ln2}-1.
\]

Their sum is
\(\log_2(8/9)+1/(3\ln2)-1<0\): \(\ln2>1/3\) and \(8/9<1\)
suffice, and the independent exact log interval verifies the former.
The concave supporting plane, followed by \(a\le u\), gives

\[
f(1,a,u)\le F_0+f_a(a-1/4)+f_u(u-1/4)
 \le F_0+(f_a+f_u)(u-1/4)\le F_0.
\]

The independent certificate gives \(F_0<1293/1000\). No sign is reversed
when \(a<1/4\), since replacing \(a\) by \(u\) uses only the positive
coefficient \(f_a\). No assumption \(a=u\) is made on this interval.

The degenerate cases tested analytically were \(a=0\), \(\mu=a=0\),
\(b=0\), \(a=b=0\), \(u=0\), \(u=1/4\), \(u=1\), and saturation
of either \(a\le u\) or \(a+u\le1\). They are covered by direct values
or the continuous extension established in Section 3. I also challenged
the asymmetric-to-symmetric step, the discarded zone constant, the
monotonicity at \(a=0\), and the uniformity of the strict slack. None
produced a counterexample to C1. No unrestricted statement is inferred
from a finite grid or numerical optimizer.

## 7. Insertion, official dictionary, and strict limsup

Felsner--Valtr label the lines canonically by the fixed outside boundary
order. Deleting line \(n+1\) leaves a marked arrangement of \(n\) lines;
its reinsertion is encoded by one north-to-south cutpath. Their equation
(1), also explicitly imported in Dallant Section 2, is
\(B_{n+1}\le\gamma_n B_n\). This counts marked arrangements rather than
insertion histories or noncommuting reduced words.

Taking any single \(A<324757/250000\) that bounds both preceding
intervals gives
\(\gamma_j\le(j+1)^6 2^{Aj}\) for the needed sizes. Initializing at
\(B_2=1\), rather than relying on the literal small-size zone assertion,
and summing for \(j=2,\ldots,n-1\) gives

\[
\log_2 B_n\le\frac A2 n^2+O(n\log n).
\]

Consequently \(\limsup n^{-2}\log_2B_n\le A/2<324757/500000\).
The factor \(1/2\) is the triangular sum \(\sum j\), and the polynomial
number of classes accumulates only an \(O(n\log n)\) term.

The Felsner--Valtr Section 1 dictionary uses a regular polygon with vertices
in fixed clockwise order, a distinguished highest vertex, and rhombi with
the prescribed boundary directions. These are normalized duals of marked
simple arrangements. The north mark fixes the vertex, and the plane
orientation fixes clockwise order; arbitrary labels are not added. The
official B4 notes give \(C(3)=2,C(4)=8\), identify A006245, and explicitly
refer to the same counting literature. This supports \(C(n)=B_n\) with
rotations/reflections of the fixed polygon distinguished as intended.
It does not use an arbitrary fixed small set of directions while \(n\)
grows. The alternative lower-order-factor observation in the candidate is
unnecessary once this dictionary is checked.

This is an attributed dictionary, not a fresh proof that every conceivable
nonstandard meaning of a quadrilateral tiling has the same count. It
matches the official convention and thus suffices for this target.

## 8. Calculation provenance and verdict

Run from the repository root:

```text
/Users/uqmkamga/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -B -u problems/2017-B4/reviews/concavity-review-2-independent-check.py
```

The script launches a dedicated child with an external 30-second timeout,
preserves its PID and parameters before waiting, and records per-log
checkpoints. The run began `2026-10-16T21:17:26.764273+00:00`, used child
PID `64593`, exited with code 0, was reaped, and took about 0.137 s. There
was no timeout, CAS, dependency installation, global process cleanup, charge,
or separately billed API. The exact interval output, stdout/stderr, and job
record are separate review-prefix artifacts. Computation is recorded as
verification evidence; the unrestricted bound rests on Sections 2-7.

Authoritative account-wide telemetry at the start of this review read 15%
total weekly used, reset timestamp `1792745187`; ordinary usage was allowed.
This was below the 90% total-used ceiling, in the same weekly window.

**Verdict:** the concavity reduction, two supporting-plane bounds, finite
log certificate, entropy-domain endpoints, insertion factor, and official
count transfer withstand this audit. I found no substantive unresolved
objection to C1. CR2-01 recommends making the harmless finite-size start
explicit. Source wording caution CR2-02 is already resolved by the
independent reconstruction above. Peer review 1 and all constructor
computational artifacts remained unseen when this initial report was frozen.
