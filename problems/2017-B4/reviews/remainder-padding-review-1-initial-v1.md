# Blind whole reconstruction of RP1--RP3

2026-10-17 UTC. Reviewer `review_2021_reasoning_j15_r2`, fresh
nonconstructor. I did not construct the remainder packet and read no
peer remainder-padding report, issue ledger or finding before this
whole report and companion records froze. Requested gpt-6.1-sol/max;
no independently verified effective-setting readback. No enumeration,
CAS or mathematical subprocess was used.

## Disposition

RP1--RP3 survive the complete reconstruction below. I found no substantive
objection or required author repair. The globally ranked words form
the stated weak bands, including the touching-origin geometry and q=n.
The core is recovered exactly by restriction. The profile identity on
alpha*Z_1 and uniform Lipschitz control give the stated error on the
whole domain. Bounded remainders transfer an entropy lower bound only
when it already holds at all sufficiently large multiples, exactly as
the candidate states. Integer dilation of one base tiling supplies one
all-scale reference family with zero quadratic entropy.

I recommend coordinator reconciliation of these scoped partial claims
after both whole audits. This is not reviewer promotion, an entropy
proof at the multiples, a periodic-core matching theorem, PR, H, EAI
or a full 2017 solution. No novelty is asserted.

The input candidate has SHA256
`0b9b6fea18437bff50edd5217531b3beb6ffc7e46a90e88899ad6e03a2ab8c91`.
Its complete text and freeze were read. Accepted structural background
provides the marked word/positive-tile dictionary and uniform normalized
lift bounds. No annulus, CUT or clean-strata assertion is used.

## 1. RP1: valid global rank words and all comparisons

Each color has q global ranks. p and t use ranks 1,...,n in increasing
internal order, and b uses n+1,...,q in that same order. Therefore pb
and tb are legitimate ranked shuffles of the full q-rank content, even
though the first n ranks of different colors are interleaved before
the remaining ranks. No same-color inversion is introduced.

The sorted outer P0 has no cross-color inversion, and reversed-color
Q0 has every cross-color ranked inversion. Both pb and tb lie between
these extremes. Passing from p to t reverses only the blocks of first-n
ranks. Comparisons involving a remaining rank are the same in pb and
tb, since both first-n subwords occur before all of b. Hence

    P0<=pb<=tb<=Q0

is actual inversion inclusion on the full ranked label set. The middle
comparison is the usual reversal on the first-n labels, with no
extra permutation or rank assignment.

Every increasing adjacent-swap chain between comparable words is a
positive planar parallelogram shelling. A swap ij->ji raises its path
pointwise and fills precisely one positive ij tile above the current
path, so successive added interiors are disjoint. Fix once a chain
from P0 to pb and a chain from tb to Q0. Their lengths are finite and
their chosen tilings depend on n,q,D and the fixed boundaries only,
not on the inner filling.

The two middle paths start at the marked origin, follow p or t to
the common point n*sum_i v_i, then follow the identical suffix b.
Their sole positive-area middle region is exactly Z_n with its usual
prescribed full lifted boundary. At each x the lower band, that middle
region and upper band partition the interval between P0 and Q0. Their
interiors are disjoint and their union is Z_q. The unchanged suffix
is a zero-area seam, not a further tiled component.

The origin and some outer boundary edges may be shared by the inner
zonogon. The proof uses weak-band shellings, so no strict-nesting
annulus hypothesis is invoked. Directly Z_n is contained in Z_q since
[0,n*v_i] is contained in [0,q*v_i] for each i and Minkowski sums
preserve containment. The equality and pointwise-order argument above
also verify the precise placed subregion, rather than merely an
abstract isomorphic copy.

Every seam has the same full ranked word and vertex heights on both
sides. Primitive unit-x integer edges cannot hide a vertex subdivision
or a partial collinear overlap. Attaching any input tiling of Z_n
therefore gives an actual edge-to-edge tiling of Z_q. Its canonical
lift starts at zero, so it agrees with the original lift on the entire
simply connected inner zonogon. Restriction to this fixed physical Z_n
recovers the exact input. This proves the embedding and

    B_D(q)>=B_D(n)

with no fiber multiplicity or asymptotic error. The inequality agrees
with accepted full-count monotonicity; this candidate additionally
specifies the fixed-origin embedding used by RP2. For q=n, b is empty,
pb=P0, tb=Q0, both added bands are empty and the map is the identity.
n=1 and D=2 are also valid; no nonempty-remainder assumption is used.

## 2. RP2: exact normalized restriction and the inner domain

Let alpha=n/q and use canonical lifts based at the marked origin.
For x in alpha*Z_1, q*x lies in Z_n. The exact restriction just proved
gives a_q(q*x)=a_n(q*x), so

    h_q(x)=alpha*h_n(x/alpha).                         (R)

The argument uses the same physical placement and the same actual
integer lift, not closeness of boundary words or injectivity of V on
arbitrary integer vectors. The rescaled argument x/alpha belongs to
Z_1 exactly where (R) is stated.

The finitely many tile gradient formulas give one fixed Lipschitz
bound G_D for every h_n and h_q on the convex domain Z_1. A change of
scale leaves these gradients unchanged. Their canonical coordinates
lie in [0,1], so their norms have a uniform bound H_D in the chosen
finite-dimensional norm. These bounds also hold on X_D's uniform
closure and do not depend on n,q or the input tiling.

For x in alpha*Z_1, write the difference using the factor alpha:

    ||alpha*h_n(x/alpha)-h_n(x)||
      <=alpha*G_D*||x/alpha-x||+(1-alpha)*H_D
      <=(1-alpha)*(G_D*||x||+H_D).

Since ||x|| is uniformly bounded on Z_1, this proves the claimed
inner-domain error. In fact this decomposition cancels the possible
1/alpha factor and is valid for every 0<alpha<=1; the candidate's
stated alpha>=1/2 range is more than enough. If instead one first
uses a coarser Lipschitz comparison with 1/alpha, alpha>=1/2 gives
the same constant, while alpha<1/2 can be covered by a uniform-norm
bound. There is no hidden small-alpha obstruction to the final bound.

## 3. RP2: the whole-domain boundary strip and profile families

Every x in Z_1 has y=alpha*x in alpha*Z_1, and
||x-y||<=(1-alpha)*diam(Z_1), since 0 belongs to Z_1. The Lipschitz
bounds on both profiles give

    ||h_q(x)-h_n(x)||
      <=||h_q(x)-h_q(y)||+||h_q(y)-h_n(y)||
         +||h_n(y)-h_n(x)||
      <=C'_D*(1-alpha).

This is an estimate on the entire normalized zonogon, including the
strip outside the scaled core. It uses exact core agreement plus the
uniform geometric gradient bound. It never converts prefix-height
discrepancy into ranked-label displacement and needs no reference
color-gap bound. The equality case q=n has alpha=1 and zero error.

Consequently, for every input profile in a family satisfying
||h_n-h*||<=delta, its padded output satisfies

    ||h_q-h*||<=delta+C'_D*(q-n)/q.

The same constant works uniformly over all members of the family and
all n,q. It does not depend on how the two fixed padding chains were
chosen. The original exact restriction recovers each tiling, so adding
this profile constraint does not lose the injection. h* may be any
element of X_D; only the displayed uniform distance is used.

## 4. RP3: the all-multiples quantifier is essential and present

Fix p0 and set n(q)=p0*floor(q/p0) for every integer q>=p0. Then

    0<=q-n(q)<p0,  n(q)/q->1,

and n(q) tends to infinity through the multiples of p0. Use the supplied
family at that exact n(q), not just a family available on some sparse
subsequence. The hypothesis explicitly supplies families at ALL
sufficiently large multiples, and its profile inequality is understood
uniformly for every member of each such family.

Let E_q be the padded image. RP1 gives |E_q|=|F_(n(q))| and hence

    q^-2*log2|E_q|
      =(n(q)/q)^2 * [n(q)^-2*log2|F_(n(q))|].

For finite s, the liminf hypothesis at all multiples implies the claimed
liminf at all integers because the factor tends to one. Counts have
the fixed-D quadratic upper bound, and for a finite lower entropy bound
they are eventually nonempty, so there is no extended-value/product
ambiguity. If s is negative the nonnegative logarithms of nonempty
counts make the statement even weaker; an asserted positive bound is
preserved with the same factor limit. Finitely many small empty
families are irrelevant. No estimate at a missing intermediate multiple
is inferred from an isolated high-entropy size.

Uniformly over E_q the profile estimate is

    ||h_q-h*||<=delta+C'_D*p0/q=delta+o(1).

To fit a fixed epsilon ball, first choose delta<epsilon, then take q
large enough that the remainder error is less than epsilon-delta.
If the input profiles converge to h* uniformly over their families
along the multiples, the same triangle inequality proves convergence
uniformly over their padded images along all integers. This is exactly
the conditional transfer stated, not an assertion that those families
already exist or have optimal entropy.

## 5. Dilation gives one reference profile and zero new entropy

Take one finite tiling T of Z_(p0). Enlarge every tile and every origin
by integer M. Divide each enlarged ij parallelogram into its M-by-M
grid of unit ij parallelograms. Shared enlarged color edges divide into
the same M unit color edges from either side, so the subdivisions give
a genuine full tiling of Z_(M*p0). At every scaled old vertex, its
new canonical height is M times the old height. In each old tile the
fine lift has the same constant ij gradient as before. Thus

    h_(M*p0)=h_T

on all of Z_1 exactly. This is not merely convergence of the profiles.

At arbitrary q use M=floor(q/p0), n=M*p0 and the fixed RP1 extension.
The resulting profile differs from h_T by at most C'_D*p0/q. The
construction works at every sufficiently large q; divisibility cases
have zero padding error. It supplies an all-scale reference for this
one base profile. Approximating an element of X_D by a finite base
tiling can supply an arbitrarily close reference, but no positive
entropy follows from that observation.

There is only one chosen subdivided tiling at each multiple for one
base T. Its normalized logarithmic count is zero. Even retaining all
members of one fixed finite base family would give a bounded count,
also zero quadratic entropy. One cannot replace RP3's all-multiples
entropy hypothesis by this single-base construction or by a sparse
subsequence of large entropy. The candidate explicitly maintains both
distinctions, so no PR or H inference is hidden here.

## 6. Dependencies, scope and adversarial checks

The ranked-word positive-shelling dictionary, canonical lift and uniform
tile-gradient bound are matched to the accepted structural exposition.
The existing full-count monotonicity in accepted DC1 is consistent
background, not a substitute for the explicit RP1 restriction needed
by RP2. All the new geometric placement and profile estimates were
reconstructed directly above. No strict annulus, closed collar,
directed-geodesic, CUT, clean coarsening or arbitrary SFT filling theorem
is used. No new external theorem or novelty claim is needed.

The following possible failures were checked: first-n ranks not being
contiguous positions in P0; same-color order across the suffix;
inner/outer contacts at the origin and along edges; weak zero-area
tails; q=n; alpha near one or near zero; the argument x/alpha outside
its valid domain; the strip outside alpha*Z_1; uniformity over input
tilings; large-scale integer remainders; and entropy supplied only at
some multiples. None contradicts the written statements.

The repaired profile note previously left a remainder step open within
its own proof program. This separately proposed elementary construction
can discharge that particular step if independently accepted. It does
not retroactively make the old program complete, and no earlier bytes
are changed. Commensurate core replication, boundary/rank-phase matching,
stratum transfer, all-multiples entropy production, PR and H remain
different obligations. The report recommends no broader acceptance.

## 7. Integrity, independence and operations

The complete candidate and freeze were read before any peer remainder
finding. The clean-strata candidate was the previous separate whole
assignment; its frozen report and claims provide no premise here.
Accepted structural Sections1--2 and the DC1 background/acceptance
records were read in that immediately preceding task and match the
same dependencies used here. Source scope is recorded in the companion
file, without a new external retrieval.

The current input and accepted background hashes, and all ten older
own packets, are reverified unchanged by the one-time administrative
freeze. No candidate/shared-status edit, Git operation, spawning,
mathematical program, enumeration, CAS, paid API, contact, access bypass
or source-PDF redistribution occurred. Only the assigned remainder
review prefix is written. Latest authoritative group-transition weekly
telemetry is21% total used, 10080-minute window, reset1792745187,
under the90%-total cutoff with integration reserve. The coordinator
alone may promote scoped results after both whole reviews.
