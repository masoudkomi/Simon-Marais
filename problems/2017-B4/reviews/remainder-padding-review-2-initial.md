# RP1–RP3: second independent whole initial audit

2026-10-17 UTC. Initially blind nonconstructor whole review by
review_2022_complexity_r2. Requested gpt-6.1-sol / max; independently
verified effective settings unavailable.

Audited candidate: notes/coordinator-remainder-padding-candidate-v1.md,
SHA-256 0b9b6fea18437bff50edd5217531b3beb6ffc7e46a90e88899ad6e03a2ab8c91.
I read the complete candidate and freeze and reconstructed every claim.
No peer remainder-padding report, ledger, or conclusion was read before
the full initial report, issue ledger, source checks and manifest froze.
No enumeration, CAS or mathematical computation was used.

I find no substantive defect. RP1 gives an actual rank-preserving
injective extension for every 1<=n<=q. RP2 has a uniform fixed-D
profile estimate, including small n/q. RP3 removes a bounded remainder
only when the needed families already exist at all sufficiently large
multiples. It does not generate positive entropy from a single base
tiling or settle H, EAI, PR or the official growth rates.

## 1. Model, domain and dependencies

The official 2017 B4 asks for both normalized logarithmic rates of
marked regular-2n-gon tilings for n>=2. In this packet D is fixed and
n,q are integer multiplicities per direction in the intermediate
zonogon Z_n=sum_i[0,n v_i], v_i=(1,i-1). They are not the official
number of directions.

The accepted integer dictionary uses rank-labelled color shuffles,
positive adjacent swaps ij -> ji for i<j, actual edge-to-edge
parallelogram tilings, and canonical lift normalized to zero at the
marked origin. It provides both the geometric shelling of comparable
positive paths and a uniform coordinate-gradient bound G_D.
These accepted facts are sufficient here. No annulus, cutting, clean
stratum, fixed reference gap bound, or all-scale recovery theorem
is an input.

## 2. RP1: the proposed ranked words really are valid

At outer size q, color i has ordered ranks i_1,...,i_q. Let p
and t list ranks 1,...,n in sorted and reversed color-block order,
respectively, preserving rank order inside each color. Let b list
the remaining ranks n+1,...,q in sorted color-block order. In both
concatenations p b and t b, a color's first n ranks precede all of
its remaining ranks. Thus these are globally valid ranked shuffles.
There is no relabeling conflict at the seam.

The lower full word P0 is the minimum and the full reversed color
word Q0 is the maximum of the shuffle interval. Hence
P0<=p b and t b<=Q0. Reversing only the first n color blocks adds
their cross-color inversions without changing any comparison with
the terminal word b. This proves p b<=t b. All intermediate
comparisons therefore hold in the same outer ranked interval.

Fix once a positive swap chain for P0 to p b, and one for t b to
Q0. These choices depend only on D,n,q and the marked boundary,
not on the varying tiling placed between p and t.

## 3. RP1: actual weak bands and the restriction inverse

Each full word has length Dq and describes an x-monotone path.
At every intermediate x a positive swap raises the path, so the
three regions between

    P0,   p b,   t b,   Q0

have disjoint interiors and together cover Z_q. They may have
zero-width parts and common boundary edges. Their fixed positive
swap chains tile the lower and upper regions by actual positive
parallelograms.

The p and t paths start at the marked origin and end at
n sum_i v_i. They are exactly the lower and upper boundaries of
Z_n. Their common terminal path b begins at that same point, so
between p b and t b it contributes no area. The only
positive-area middle region is the fixed physical Z_n at the
origin, not a translated or rank-renamed copy.

Attach any input tiling of Z_n. Along the seams its rank increments
are the first n ranks of each color and match the globally specified
band ranks. The union is a full tiling of Z_q; no tile interiors
overlap. The Minkowski inclusion Z_n subset Z_q also follows directly
from n<=q. Shared boundary edges are allowed, so no strictly nested
annulus hypothesis is being used.

Restriction to the known fixed Z_n recovers every original tile.
If two inputs differed, the corresponding outputs therefore differ.
This proves the exact injection and B_D(q)>=B_D(n), with no
multiplicity, entropy loss, rank permutation factor, or matching
ambiguity. The extension can be deterministic by the fixed band
choices above.

When q=n, b is empty, P0=p and Q0=t, both outer bands have zero
area, and the map is the identity. D=2 has no exceptional geometry;
the argument remains valid for its unique two-direction grids.
n=1 is allowed and gives a genuine D-direction zonogon at D>=2.
The excluded n=0 case is not needed.

## 4. RP2: exact restriction identity and uniform constants

Let a_n be the input canonical lift and a_q the extension. On the
fixed physical Z_n their lifts agree, since both are zero at the
marked origin and have the same edge increments. Put

    h_n(x)=a_n(n x)/n,   h_q(x)=a_q(q x)/q,
    alpha=n/q.

For x in alpha Z_1, the point q x is in Z_n, so exactly

    h_q(x)=alpha h_n(x/alpha).

This is an equality of full vector profiles, including all boundary
points, not a consequence inferred from small physical path error.
Every profile has the same fixed-D Lipschitz bound, and every
coordinate lies in [0,1]. These bounds include the newly attached
bands because they consist of the same fixed prototiles.

For alpha>=1/2, the candidate's comparison on alpha Z_1 is valid:
|x/alpha-x| <=diam(Z_1)(1-alpha), since x/alpha belongs to Z_1.
Combining this with the bounded profile norm gives a constant
times 1-alpha. To extend to the rest of Z_1, use alpha x as a
nearby point; convexity and the origin in Z_1 ensure alpha x is
inside. Its distance from x is at most
diam(Z_1)(1-alpha). Both profiles have the uniform Lipschitz bound,
so the same order holds on the full domain.

There is also a simpler global estimate that handles all
0<alpha<=1 at once. For any x in Z_1 the exact identity at alpha x is

    h_q(alpha x)=alpha h_n(x).

Thus, in a fixed coordinate norm,

    |h_q(x)-h_n(x)|
      <= |h_q(x)-h_q(alpha x)|+(1-alpha)|h_n(x)|
      <= [G_D diam(Z_1)+M_D](1-alpha).

Here M_D is a uniform bound for |h_n|, equal to 1 in the coordinate
sup norm. This reconstructs the stated uniform estimate even when
alpha<1/2. In particular no missing small-alpha case invalidates
the claim. One can instead absorb that case directly by bounded
norms, since 1-alpha>=1/2.

The resulting C'_D is independent of the input tiling, n,q and the
choice of interior filling. For any target h* in the compact closure
X_D, the triangle inequality gives

    ||h_q-h*|| <= ||h_n-h*||+C'_D(q-n)/q.

An entire family in a delta-ball is carried injectively into the
stated enlarged ball. No convexity of X_D or extension of h* is
assumed; the same fixed domain Z_1 is used throughout.

## 5. RP3: quantifiers at all scales

Fix p0 before q. The choice
n(q)=p0 floor(q/p0) satisfies 1<=n<=q for q>=p0, and
0<=q-n<p0. Therefore n/q tends to one and the uniform profile error
is at most C'_D p0/q.

Suppose the family F_n is already supplied at every sufficiently
large multiple of p0, with the stated liminf lower bound s.
For every sufficiently large integer q the needed F_n(q) exists.
By RP1 the padded family has exactly |F_n(q)| elements, so

    q^-2 log2 |image(F_n)| =
      (n/q)^2 [n^-2 log2 |F_n|].

For every eta>0 the bracket is at least s-eta at all sufficiently
large multiples. The prefactor tends to one. This proves the
claimed liminf at every large q. It is not a choice of an occasional
favorable q or a subsequence with uncontrolled gaps.

If only one sequence of good multiples were known, with unbounded
relative gaps, this reasoning would not cover all q. The candidate
expressly assumes all sufficiently large multiples. Likewise the
fixed p0 cannot grow with q while silently retaining the bounded
remainder conclusion.

For profiles, a fixed delta-ball transfers to delta+o(1). To
deduce membership in a target epsilon-ball, first choose
delta<epsilon, then take q sufficiently large. One cannot set
delta=epsilon and discard a positive padding error. If the
families' profile error itself tends to zero, the padded profiles
converge as well.

## 6. Dilation of one base tiling

Take a single Z_p0 tiling and dilate physical coordinates by M.
Its enlarged ij tile is the parallelogram generated by M v_i,
M v_j. Subdivide it into the M-by-M grid of unit ij tiles.
Both sides of a shared original edge acquire the same M
subedges, so the grids match. The resulting full tiling has
boundary multiplicity M p0 in every color.

The canonical lift on the dilated patch is M times the base lift
at the corresponding point. This is true on vertices and agrees
affinely within every grid tile. Therefore its normalized profile
on Z_1 is exactly the base normalized profile. There is no small
boundary mismatch at integer multiples.

For arbitrary q>=p0 use M=floor(q/p0), n=M p0 and RP1. The exact
base profile is then approximated with error at most C'_D p0/q.
This proves all-scale reference-profile existence from one finite
base, independently of any nonuniform phase-matching construction.

The M-by-M two-direction grid in a given enlarged tile supplies
one prescribed filling. A single base therefore gives one output
at each multiple, then one padded output at each q. Its logarithmic
count divided by q^2 is zero. Even keeping all finitely many
base tilings would leave a bounded-size family. No exponential
family at the multiples is manufactured by this operation.

## 7. Adversarial scope checks

I checked repeated ranks, seams meeting the outer boundary,
the common tail, q=n, n=1, D=2, alpha close to zero,
alpha close to one, profile values on the newly added bands,
uniformity across all fillings, exact restriction injectivity,
and the order of target-ball and large-q choices. The argument
handles them with its stated model and fixed parameters.

RP1–RP3 discharge a bounded-remainder/reference-existence
obligation. They do not supply a positive-entropy family
at multiples, arbitrary profile recovery, commensurate
periodic-core matching, cut-window insertion, rank-phase
compatibility or zero-minor stratum repair. The earlier
fixedD note's open-program statements remain valid for
that earlier packet; no frozen text needs rewriting.
No H, EAI, PR, exact official rate or novelty claim is
established here.

The companion ledger records all checked concerns. No
substantive issue remains from this independent audit;
the coordinator alone may decide a scoped acceptance
after the other independent review and reconciliation.
